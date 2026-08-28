#!/usr/bin/env bash
# Product Harness — grant a single-use approval for the next gated artifact write.
#
# Usage (run by the PM, from the harness root):
#   bash ".claude/hooks/approve.sh" "projects/mobile-redesign/artifacts/design/BRIEF-001.md"
#   bash ".claude/hooks/approve.sh" "*"          # approve the very next gated write, any path
#
# Each invocation APPENDS one approval line. Lines are single-use (consumed by the
# gate on the matching write) and the whole token expires 15 minutes after its last
# write. Paths are relative to the harness root; fnmatch globs are allowed
# (e.g. "projects/mobile-redesign/artifacts/**").
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
TOKEN="$ROOT/.claude/.harness-approval"

if [ "$#" -lt 1 ] || [ -z "${1:-}" ]; then
  echo "usage: approve.sh <path-relative-to-harness-root | glob | '*'>" >&2
  exit 2
fi

TARGET="$1"
{
  echo "# approved $(date '+%Y-%m-%d %H:%M:%S')"
  echo "$TARGET"
} >> "$TOKEN"
# Refresh mtime so the 15-minute TTL runs from now.
touch "$TOKEN"

echo "Approved next gated write for: $TARGET"
echo "Token: $TOKEN (single-use, expires in 15 min)."
