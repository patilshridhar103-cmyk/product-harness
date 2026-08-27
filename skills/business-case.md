# Business Case Skill

## Role
Justify (or reject) an investment by comparing cost to benefit on the domain's
terms. Has TWO MODES so it works both for a PM brainstorming and for a build
decision.

## The Two Modes

### 🟡 Napkin Mode (brainstorming)
- **Purpose:** "Is this even worth investigating?" — a fast directional read.
- **Rigor:** mostly assumptions, every number flagged.
- **Output:** rough value vs. rough cost + a list of what to validate.
- **When:** PM is brainstorming, no validation yet, deciding whether to explore.

### 🟢 Full Mode (build decision)
- **Purpose:** "Should we commit engineering to this?" — a rigorous justification.
- **Rigor:** evidence-backed numbers, sensitivity analysis, tied to a decision.
- **When:** post-validation, before decision-evaluator recommends BUILD.

**The agent picks the mode by asking, or from context (brainstorm vs. validated).**

## When to Use
- PM brainstorming an idea → Napkin
- Validated opportunity heading to a build decision → Full
- Comparing two investments → either mode, both options

## Reads First
- `knowledge/domains/<b2b|b2c|internal>.md` — **which metrics/value frame applies**
- `knowledge/constraints.md` (budget, capacity, risk tolerance, escalation thresholds)
- `business-model` output if it exists (BM-###) — defines what to quantify

## Critical Constraints
- **Never fabricate numbers.** Ask for inputs; mark every estimate as an assumption.
- Use the domain's value frame (revenue for B2B/B2C; time/cost/risk for internal).
- Flag when a number would trip a constraint (escalate per constraints.md).
- Napkin mode must be LABELED as such — never let a napkin case masquerade as full.

## Process

### Step 1: Set mode & domain
Confirm Napkin vs. Full. Read the domain file for the value frame.

### Step 2: Gather inputs (ASK for what's missing)
```
Agent (napkin example):
  For a napkin case I need three things I don't have:
    1. Rough target size (segment or # internal users)?
    2. Rough value per unit (price, or hours saved/user if internal)?
    3. Rough build cost — shall I ask engineering for a t-shirt size?
  Everything else I'll mark as an assumption to validate.
```

### Step 3: Model the benefit (domain-correct)
- **Revenue:** reach × conversion × value × retention (B2C) / new+expansion ACV,
  retention impact (B2B)
- **Internal:** hours saved × users × frequency × loaded cost + cost avoided + risk

### Step 4: Model the cost
- Build (eng weeks × cost), run/maintain, cost-to-serve, change-management (internal)

### Step 5: Compare
- Net value, payback period, ROI. Full mode: + sensitivity (what if adoption is
  half? price is 30% lower?).

### Step 6: Produce Artifact
`artifacts/strategy/CASE-<NNN>.md`

## Output Template

```markdown
# Business Case CASE-###: [Idea/Product]

**Date:** YYYY-MM-DD · **MODE: 🟡 NAPKIN / 🟢 FULL** · **Domain:** [B2B/B2C/internal]
**Related:** [O-### / BM-### / D-###]

> ⚠ NAPKIN MODE: assumption-heavy, directional only. Not a build justification.
  (delete this line in Full mode)

## The Question
[Invest in X? Compare A vs B?]

## Benefit (domain frame: [revenue / time-cost-risk])
| Driver | Estimate | Basis | Confidence |
|--------|----------|-------|-----------|
| [e.g. hours saved/user/wk] | [2.5] | ASSUMPTION — validate | LOW |
| [e.g. # users] | [200] | knowledge/customers.md | MED |
| [e.g. loaded hourly cost] | [$60] | ASSUMPTION | LOW |
| **Annual benefit** | **$[X]** | derived | — |

## Cost
| Item | Estimate | Basis |
|------|----------|-------|
| Build | [8 eng-wks] | eng t-shirt — ASSUMPTION |
| Run/maintain (annual) | $[X] | — |
| Change mgmt (internal) | $[X] | — |
| **Total yr-1 cost** | **$[X]** | — |

## Comparison
- Net (yr 1): $[benefit − cost]
- Payback: [X months]
- ROI: [X%]

## (Full mode only) Sensitivity
- If adoption = 50% of assumed → net becomes $[Y]
- If value/unit −30% → net becomes $[Z]
- Break-even needs: [the threshold assumption]

## Assumptions to Validate (biggest first)
1. [Load-bearing assumption] → validate via [method] → hand to experiment-planner
2. [...]

## Constraint Check
- Budget vs constraints.md: [ok / exceeds → escalate]
- Capacity: [ok / conflict with in-flight project]

## Recommendation
- 🟡 Napkin: [Worth investigating? Yes/No + what to validate first]
- 🟢 Full: [Build / Don't / Conditional on validating X]
```

## Questions Agent MUST Ask
1. Napkin or full? (or: is this validated yet?)
2. What inputs do we have vs. need? (size, value/price, cost)
3. B2B/B2C/internal? (sets the benefit frame)

## What NOT to Do
❌ Invent numbers to fill the model — ask, or mark ASSUMPTION
❌ Let a napkin case read as a committed justification
❌ Revenue math on an internal product
❌ Ignore change-management / run cost (common under-count)

## Success Criteria
✅ Mode labeled clearly
✅ Every estimate has a basis + confidence
✅ Benefit frame matches domain
✅ Assumptions ranked and routed to validation
✅ Constraint check done (escalates if tripped)
✅ Full mode has sensitivity analysis

## Integration
Reads: knowledge/domains, business-model, constraints. Feeds: decision-evaluator,
experiment-planner (validation of assumptions), risk-assumption-tracker.
