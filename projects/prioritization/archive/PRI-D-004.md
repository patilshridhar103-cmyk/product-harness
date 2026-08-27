# PRI-D-004 — Navigation Pattern for Prioritization UI

> Full archived detail. NOT loaded at session start. Retrieved by ID only when
> relevant — e.g. when Mobile Redesign (MOB-O-002) reaches spec and needs to
> reuse this pattern. This is the "cold" tier: complete, permanent, on-demand.

**Project:** Smart Prioritization (PRI) · **Type:** Decision · **Date:** 2026-08-19
**Status:** Approved · **Related:** PRI-PS-001 (spec), MOB-O-002 (cross-project reuse)

---

## Decision
Use a **persistent left side-rail** for prioritization criteria, with the ability
to **pin** up to 3 criteria to the top. Ranked feature list occupies the main pane
and re-sorts live as criteria weights change.

## Alternatives Considered
| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| **Side-rail + pinning** | Criteria always visible; live re-sort; scales to many criteria | More horizontal space | ✓ CHOSEN |
| Top toolbar dropdown | Compact | Criteria hidden behind clicks; poor for frequent re-weighting | Rejected |
| Modal criteria editor | Clean main view | Breaks flow; can't see list while editing weights | Rejected |

## Rationale
Prioritization is an *iterative* task — users re-weight and watch the ranking move.
That demands criteria and results visible **simultaneously**. The side-rail is the
only option that keeps both in view during weight changes.

## Approved Prompt (audit)
Skill: `design-reviewer` · PM approved 2026-08-19 · PM note: "Side-rail, but cap
pinned criteria at 3 so it doesn't get cluttered."

## Key Constraint for Reuse (relevant to MOB)
The side-rail assumes **≥768px width**. On mobile it must collapse to a bottom
sheet — the pattern does NOT transfer directly. Any mobile reuse (MOB-O-002) must
re-solve the small-screen layout; only the *interaction model* (live re-sort on
weight change) carries over, not the side-rail chrome itself.

## Success Metric Tie-in
Supports PRI-H-001 (cut prioritization time): live re-sort removes the
export-to-spreadsheet-and-recalculate loop that cost users the most time.
