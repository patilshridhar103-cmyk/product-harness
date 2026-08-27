# Product Knowledge

> SHARED across every project. The current state of the product — what exists,
> how it's built, what's live. Gives the agent grounding so opportunities and
> specs fit reality instead of proposing what already exists or what can't ship.

**Last updated:** 2026-08-27 · **Owner:** [PM name]

---

## Domain
**Domain:** B2B
> The agent reads this to auto-select the metric lens from knowledge/domains/.
> B2B → knowledge/domains/b2b.md (ACV, CAC, LTV, NRR). Change to B2C or internal
> if the product type changes. If blank, the agent must ASK before money/metrics work.

---

## Product Overview
[One paragraph: what the product is today, its main surfaces/modules.]

## Current Capabilities (what exists)
- **[Module 1 — e.g. Roadmap]:** [what it does] · adoption: [%] · health: [good/weak]
- **[Module 2 — e.g. Prioritization]:** [status — e.g. "in build, PRI project"]
- **[Module 3 — e.g. Analytics]:** [what it does] · adoption: [%]
- **[Module 4]:** [...]

## Known Weak Spots (evidence-backed)
[Where the product underperforms today — seeds for opportunities.]
- [e.g. "Analytics adoption stuck at 12% — users can't export for reporting."]
- [e.g. "Mobile experience is thin — see Mobile Redesign project."]

## Technical Context (constraints the agent must respect in specs)
- **Stack:** [e.g. Node.js backend, React web frontend]
- **Platforms:** [e.g. responsive web only — no native mobile app]
- **Key integrations:** [e.g. Jira, Slack — live; Linear — requested, not built]
- **Scale today:** [e.g. ~1,000 concurrent users; not yet architected for 10k]
- **Hard constraints:** [e.g. "No native mobile", "Must work offline for X"]

## What's In Flight (live projects — pointer, not detail)
> Detail lives in each project's own workspace. This is just so the agent knows
> what's moving without loading those projects.
- **PRI — Smart Prioritization:** BUILDING (spec approved).
- **MOB — Mobile Redesign:** DISCOVERY.

## Recently Shipped (with outcomes)
- [e.g. "Onboarding v2 (ONB, Jun 2026): +12% activation."]

## Product Principles
[Durable rules the agent should honor when proposing/spec'ing.]
- [e.g. "Evidence before build."]
- [e.g. "Ship the smallest thing that tests the hypothesis."]
- [e.g. "Don't add a setting where a good default will do."]
