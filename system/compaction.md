# Compaction Routine

> How the agent keeps context flat forever. This is the rule that turns the
> memory system from "works in a demo" into "works at session 500." The agent
> runs this per-project, never across projects.

---

## The three tiers (recap)

| Tier | File | Loaded? | Grows? | Purpose |
|------|------|---------|--------|---------|
| **HOT** | `ACTIVE.md` | Always | **No — capped** | Current focus, open questions, last 3–5 decisions |
| **WARM** | `SUMMARY.md` | Always | Slowly (1 line/item) | Compressed history, one line each → archive link |
| **COLD** | `archive/<ID>.md` | On demand, by ID | Yes, unbounded | Full detail. Never bulk-read. |
| **AUDIT** | `decision_log.md` | Never (bulk) | Yes, append-only | Immutable trail. Queried by ID if ever needed. |

The invariant: **HOT stays small.** WARM stays one-line-per-item. Everything
heavy lives COLD and is pulled only when a specific ID is relevant.

---

## When to run compaction

Check these triggers at the END of any session where an artifact was created:

1. **Count trigger** — `ACTIVE.md` "Last Decisions" list has grown past **5 items**.
2. **Size trigger** — `ACTIVE.md` exceeds roughly **2 pages / ~2.5 KB**.
3. **Phase trigger** — the project just crossed a phase boundary
   (e.g. DECIDING → BUILDING, or a feature shipped). Natural moment to sweep.

Any one trigger fires compaction. When none fire, do nothing — don't compact for
its own sake.

---

## The routine (step by step)

For the CURRENT project only:

### Step 1 — Identify what's cold
In `ACTIVE.md`, find "Last Decisions" older than the most recent 3.
A decision is safe to move out when **all** of these are true:
- It is resolved (not an open question, not an in-flight experiment).
- It has a full `archive/<ID>.md` file.
- It has a one-line entry in `SUMMARY.md`.

If any is missing, create it first (see Step 2), then move.

### Step 2 — Ensure WARM + COLD exist for each
For each decision being swept out:
- **COLD:** confirm `archive/<ID>.md` holds the full detail. If the detail only
  ever lived in `ACTIVE.md`, write the archive file now before deleting from HOT.
- **WARM:** confirm one line exists in `SUMMARY.md`:
  `**<ID>:** <one-sentence what + outcome> → archive/<ID>.md`

### Step 3 — Trim HOT
Remove the swept decisions from `ACTIVE.md`. After trimming, `ACTIVE.md` retains
ONLY:
- Current Focus
- Next Step
- Open Questions (unresolved only)
- Last Decisions — **the most recent 3**
- Resolved Assumptions (keep — these are guardrails against re-litigating)
- Cross-Project Notes (keep if still live)

### Step 4 — Never touch AUDIT
`decision_log.md` is append-only. Compaction NEVER edits or prunes it. It is the
permanent record; its size doesn't matter because it's never bulk-loaded.

### Step 5 — Update the router
Touch this project's row in `memory/INDEX.md` (status + last-touched). If a
resolved assumption or changed decision affects a cross-project dependency,
update the Dependencies section too.

---

## What NEVER gets compacted out of ACTIVE.md

Keep these in HOT regardless of age — they are cheap and prevent expensive errors:

- **Open Questions** — until actually answered.
- **Resolved Assumptions** — e.g. "A-1 RESOLVED: pain is structure, not value.
  Do not re-litigate." One line that stops the agent re-opening settled ground.
- **Live Cross-Project Notes** — the dependency flags. Dropping these re-hides a
  dependency the agent must see every session.
- **Blocking notes** — anything that gates the next step.

---

## Worked example

**Before compaction** — `ACTIVE.md` "Last Decisions" has grown to 6:

```
- PRI-PS-001  (spec approved)          ← recent
- PRI-D-001   (BUILD approved)         ← recent
- PRI-D-004   (nav pattern)            ← recent
- PRI-E-001   (WoZ test)               ← older, resolved
- PRI-H-001   (hypothesis)             ← older, resolved
- PRI-OPP-001 (5 opportunities)        ← older, resolved
```

Count trigger fires (>5). The oldest 3 are resolved, archived, and summarized.

**After compaction** — HOT keeps the recent 3:

```
## Last Decisions (most recent first)
- PRI-PS-001  (spec approved)   → archive/PRI-PS-001.md
- PRI-D-001   (BUILD approved)  → archive/PRI-D-001.md
- PRI-D-004   (nav pattern)     → archive/PRI-D-004.md
```

The three swept items (`E-001`, `H-001`, `OPP-001`) are gone from HOT but each
still has its `SUMMARY.md` line and `archive/` file. Nothing is lost — it moved
tiers. If the agent later needs the hypothesis detail, it reads the one-line
SUMMARY, sees `PRI-H-001` is relevant, and retrieves `archive/PRI-H-001.md`.

---

## The property this guarantees

```
Session   ACTIVE.md size   What loads at start
   5          ~2 KB         INDEX + ACTIVE + SUMMARY + knowledge
  50          ~2 KB         (same — SUMMARY grew ~45 lines, still tiny)
 500          ~2 KB         (same — archive/ is huge but COLD, unread)
```

Start-of-session context is **constant**, not cumulative. That is the whole point.

---

## Agent checklist (paste into agent.md if not already referenced)

At session end, if an artifact was created:
- [ ] Appended to `decision_log.md`
- [ ] Added one line to `SUMMARY.md`
- [ ] Updated `ACTIVE.md` (focus, next step, open Qs)
- [ ] Triggers checked (count > 5 / size > 2pg / phase crossed)?
- [ ] If triggered: archived + summarized + trimmed HOT to last 3
- [ ] Kept open questions, resolved assumptions, cross-project notes in HOT
- [ ] Updated `INDEX.md` row
- [ ] Left `decision_log.md` untouched
