# PRI-PS-001 — Product Spec: Smart Prioritization

**Project:** PRI · **Type:** Product Spec · **Date:** 2026-08-26
**Skill:** product-spec-writer · **From:** PRI-D-001 · **Status:** Approved

---

## Problem
SMB PMs spend ~4 hrs/week manually prioritizing; no tool weights customer requests
vs. business value. (9/12 customers — PRI-SYN-001)

## User story
As a PM, I want to input weighted criteria and have features auto-ranked, so I can
decide in ~30 min instead of 4 hours.

## Core features (MVP)
1. **Criteria input** — 5+ custom weighted criteria, saveable templates
2. **Feature ranking** — live re-sort as weights change (<1s), shows reasoning
3. **Export** — CSV / PDF / Jira sync

## UI
Nav pattern per PRI-D-004 (side-rail + pinned criteria; bottom-sheet <768px).

## Out of scope (v1)
AI criteria suggestions · team sharing · real-time collab · Jira integration (TBD)

## Technical
Node.js + React · 1000 concurrent users · <1s ranking · existing design system

## Success metrics
50% adoption month 1 · ≥40% time reduction · NPS >7

## Timeline
Design 1wk · Build 3wk · Test 1wk · Launch 1wk
