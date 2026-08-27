#!/usr/bin/env python3
"""
Product Harness — approval-gate PreToolUse hook.

Enforces the harness rule "never create an artifact without an approved prompt
preview" as a mechanism instead of a norm. Registered in .claude/settings.json on
Write|Edit|MultiEdit|NotebookEdit|Artifact.

Decision protocol (Claude Code PreToolUse):
  - print JSON {"hookSpecificOutput": {"hookEventName": "PreToolUse",
                "permissionDecision": "deny"|"allow", "permissionDecisionReason": "..."}}
  - exit 0. (We only emit an explicit decision when we want to DENY; otherwise we
    stay silent and let normal permission flow proceed.)

What is gated:
  - The `Artifact` tool (any publish), always.
  - Writes whose target is a harness artifact / decision record:
      artifacts/**, projects/*/artifacts/**, projects/*/archive/**,
      projects/*/{ACTIVE,SUMMARY,decision_log}.md, memory/INDEX.md
Everything else (CLAUDE.md, .claude/**, skills/**, knowledge/**, system/**,
scratchpad, files outside the harness) is allowed through untouched.

Approval: a single-use, time-limited token at .claude/.harness-approval created by
.claude/hooks/approve.sh. Each non-comment line is `*` (approve anything) or a path /
fnmatch glob relative to the harness root. A matching line is consumed on use.
"""
import sys, os, json, time, fnmatch, re

HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOKEN = os.path.join(HARNESS_ROOT, ".claude", ".harness-approval")
TOKEN_REL = ".claude/.harness-approval"
TTL_SECONDS = 15 * 60

GATED_RE = [
    re.compile(r"^memory/INDEX\.md$"),
    re.compile(r"^artifacts/"),
    re.compile(r"^projects/[^/]+/(archive|artifacts)/"),
    re.compile(r"^projects/[^/]+/(decision_log|SUMMARY|ACTIVE)\.md$"),
]


def emit(decision, reason):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def allow_silently():
    # No explicit decision -> normal permission flow continues.
    sys.exit(0)


def rel_to_root(path):
    if not path:
        return None
    try:
        ap = os.path.abspath(path)
    except Exception:
        return None
    root = HARNESS_ROOT.rstrip("/") + "/"
    if ap == HARNESS_ROOT or ap.startswith(root):
        return os.path.relpath(ap, HARNESS_ROOT).replace(os.sep, "/")
    return None  # outside the harness — not our concern


def is_gated(rel):
    return rel is not None and any(rx.search(rel) for rx in GATED_RE)


def token_lines():
    if not os.path.exists(TOKEN):
        return None, "no approval on file"
    age = time.time() - os.path.getmtime(TOKEN)
    if age > TTL_SECONDS:
        return None, "approval expired (older than 15 min)"
    try:
        with open(TOKEN, "r", encoding="utf-8") as fh:
            lines = [ln.strip() for ln in fh]
    except Exception as exc:
        return None, "approval unreadable (%s)" % exc
    return [ln for ln in lines if ln and not ln.startswith("#")], None


def approval_matches(target_key):
    """Return (ok, reason). Consumes the matched line on success."""
    lines, err = token_lines()
    if lines is None:
        return False, err
    matched_idx = None
    for i, pat in enumerate(lines):
        if pat == "*" or pat == target_key or fnmatch.fnmatch(target_key, pat):
            matched_idx = i
            break
    if matched_idx is None:
        return False, "approval on file does not cover '%s'" % target_key
    # Consume the matched line (single-use). Remove the whole token if it was the last.
    remaining = [ln for j, ln in enumerate(lines) if j != matched_idx]
    try:
        if remaining:
            with open(TOKEN, "w", encoding="utf-8") as fh:
                fh.write("\n".join(remaining) + "\n")
        else:
            os.remove(TOKEN)
    except Exception:
        pass  # best-effort consume; do not fail the write on cleanup error
    return True, "approved"


DENY_HELP = (
    "Harness approval gate: this is a gated artifact write. Show the PM a "
    "'## [PROMPT PREVIEW]' and have THEM approve by running:\n"
    "    bash \".claude/hooks/approve.sh\" \"%s\"\n"
    "(or \"*\" to approve the next gated write). Do not self-approve to bypass the PM."
)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        allow_silently()  # can't parse -> don't block the user

    tool = data.get("tool_name", "")
    ti = data.get("tool_input", {}) or {}

    # The Artifact publish tool is always gated (keyed by its file path if present).
    if tool == "Artifact":
        key = ti.get("file_path") or "artifact:publish"
        ok, why = approval_matches(key)
        if ok:
            emit("allow", "Approved artifact publish: %s" % why)
        emit("deny", "Publishing an Artifact is gated. %s" % (DENY_HELP % (ti.get("file_path") or "*")))

    # File-writing tools.
    path = ti.get("file_path") or ti.get("notebook_path")
    rel = rel_to_root(path)

    # Never let a tool write the approval token itself.
    if rel == TOKEN_REL:
        emit("deny", "The approval token must be created by the PM via approve.sh, "
                     "not written by a tool.")

    if not is_gated(rel):
        allow_silently()

    ok, why = approval_matches(rel)
    if ok:
        emit("allow", "Approved harness artifact write: %s" % why)
    emit("deny", "Writing a harness artifact/decision record is gated (%s). %s"
                 % (why, DENY_HELP % rel))


if __name__ == "__main__":
    main()
