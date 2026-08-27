# Product Strategy Skill

## Role
Set direction at a higher altitude than the roadmap. Define where to play, how to
win, and what NOT to do — so every downstream opportunity and decision has a spine
to align to.

## When to Use
- PM is defining/refreshing product direction (quarterly, annual)
- Multiple opportunities exist and need a strategic filter
- Before roadmap-planner (strategy sets the criteria roadmap prioritizes against)
- When a decision feels like "should we even be in this space?"

## Reads First
- `knowledge/company.md` (mission, company strategy, non-goals)
- `knowledge/domains/<b2b|b2c|internal>.md` (what winning looks like in this world)
- `knowledge/customers.md` (who we serve)
- Portfolio `memory/INDEX.md` (what's already in flight)

## Critical Constraints
- Strategy must name trade-offs — what we WON'T do is as important as what we will
- Must align with company strategy in knowledge/company.md (flag conflicts, don't override)
- Grounded in a real advantage, not aspiration ("we'll be better" is not a strategy)
- Ask the PM for the strategic intent if it isn't derivable

## Process

### Step 1: Diagnosis (where are we?)
- Current position: strengths, weak spots (from knowledge/product.md)
- Market/competitive reality (from competitive-analyst output if available)
- The core challenge this strategy must overcome

### Step 2: Where to Play
- Which segments/JTBD do we go after? Which do we explicitly NOT?
- Which use cases are the wedge vs. expansion vs. off-limits?

### Step 3: How to Win
- The advantage: why us, why here, why now
- The differentiated bet (must be defensible, not just "better UX")

### Step 4: Strategic Bets & Sequence
- 2–4 big bets that ladder to the goal
- Sequence + rationale (why this order)
- What each bet needs to be true (assumptions → hand to risk-assumption-tracker)

### Step 5: Guardrails (what we won't do)
- Explicit non-goals for this horizon
- These become a filter for opportunity-generator + decision-evaluator

### Step 6: Produce Artifact
`artifacts/strategy/STRAT-<NNN>.md`

## Output Template

```markdown
# Product Strategy STRAT-###: [Theme / Horizon]

**Date:** YYYY-MM-DD · **Horizon:** [e.g. H2 2026 – 2027] · **Domain:** [B2B/B2C/internal]

## Diagnosis
- Current position: [strengths / weak spots]
- Core challenge: [the one thing this strategy must overcome]

## Where to Play
- **We WILL focus on:** [segments / JTBD / use cases]
- **We will NOT:** [explicit exclusions]

## How We Win
- **Our advantage:** [defensible why-us]
- **The bet:** [differentiated position, one sentence]

## Strategic Bets (sequenced)
1. **Bet 1:** [what] — needs to be true: [assumption] — by [when]
2. **Bet 2:** [...]
3. **Bet 3:** [...]

## Guardrails / Non-Goals (this horizon)
- [What we're deliberately not doing, and why]

## Success (strategy-level)
- [Metric tied to domain — NRR / retention / adoption per knowledge/domains]

## Alignment Check
- Company strategy (company.md): [aligned / tension — flag]
- In-flight projects (INDEX): [fit / conflict]
```

## Questions Agent MUST Ask
1. What's the time horizon?
2. What's the one outcome this strategy must drive?
3. What's our real, defensible advantage (not aspiration)?
4. What are we willing to explicitly NOT do?

## What NOT to Do
❌ "Be the best [X]" — not a strategy, no trade-off
❌ Strategy that says yes to everything — no guardrails = no strategy
❌ Ignore company non-goals in company.md
❌ Bets with no "what must be true" (unfalsifiable)

## Success Criteria
✅ Names explicit trade-offs (where to play AND not play)
✅ Advantage is defensible and specific
✅ Bets are sequenced with assumptions
✅ Non-goals stated
✅ Aligned to (or conflicts flagged with) company strategy
✅ Success metric matches the domain

## Integration
Feeds: opportunity-generator (filter), roadmap-planner (prioritization criteria),
decision-evaluator (strategic fit test). Reads: business-model, competitive-analyst.
