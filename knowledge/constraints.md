# Constraints Knowledge

> SHARED across every project. The boundaries every decision must live inside —
> resources, timelines, budget, compliance, and standing policy. The agent checks
> proposals against these so it never recommends something the org can't do.

**Last updated:** 2026-08-27 · **Owner:** [PM name]

---

## Resource Constraints
- **Engineering capacity:** [e.g. "2 squads, ~6 engineers total. One squad is
  committed to PRI through Q4."]
- **Design capacity:** [e.g. "1 designer, shared across all projects."]
- **PM capacity:** [e.g. "You — running 2 active projects; 3 is the practical ceiling."]

## Time Constraints
- **Planning horizon:** [e.g. "We plan in quarters. Current: Q3 2026."]
- **Fixed dates / commitments:** [e.g. "Board update Oct 15 — PRI expected shipped by then."]
- **Cadence:** [e.g. "Weekly ship cycle. Anything needing >8 weeks gets scrutiny."]

## Budget Constraints
- **Build budget:** [band or per-project cap, if any]
- **Tooling / vendor spend:** [what's approved, what needs sign-off]
- **Pricing floor/ceiling:** [if relevant to GTM decisions]

## Compliance / Legal / Security
- [e.g. "GDPR applies — no PII in URLs or third-party analytics without review."]
- [e.g. "SOC 2 in progress — new data flows need security review before build."]
- [Anything the agent must flag rather than decide alone.]

## Standing Policy (agent must respect, not override)
- [e.g. "No customer data sent to external services without explicit PM approval."]
- [e.g. "No public commitments (roadmap dates to customers) without PM sign-off."]
- [e.g. "Irreversible actions — deletes, sends, publishes — always confirm first."]

## Escalation Triggers
> When a proposal bumps a constraint, the agent should stop and escalate to the
> PM rather than proceed.
- Exceeds engineering capacity for the quarter → escalate.
- Requires spend above [threshold] → escalate.
- Touches compliance/security surface → escalate for review.
- Contradicts a company non-goal (see company.md) → escalate.

## Risk Tolerance
[One line on how much uncertainty the org accepts before building.]
- [e.g. "Low tolerance for building on unvalidated demand — validate first.
  Higher tolerance for small reversible experiments."]
