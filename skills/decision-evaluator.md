# Decision-Evaluator Skill

## Role
Analyze experiment results against the hypothesis and recommend BUILD / KILL / TEST
/ PIVOT — with honest reasoning and alternatives considered.

## When to Use
- After an experiment produces results
- At a go/no-go gate

## Reads First
- The experiment results (`E-###`) · the hypothesis (`H-###`) ·
  `business-case` (full) if it exists · `risk-assumption-tracker` output

## Critical Constraints
- Compare actual vs. predicted honestly (report gaps)
- Consider ≥2 alternatives with pros/cons
- Validate/invalidate each assumption
- Define success metrics + escalation path for the decision

## Process
1. Review results vs. hypothesis success/failure criteria
2. Validate/invalidate assumptions
3. Weigh alternatives (build/wait/partner/pivot)
4. Recommend with rationale
5. Define success metrics + escalation
6. Produce `artifacts/<project>/decisions/D-###.md`

## Output
Decision · evidence summary · hypotheses validated · alternatives · assumptions
· timeline · success metrics · escalation path. (evaluation-framework.md →
Decision rubric; passing 14/21.)

## Questions Agent MUST Ask
1. Does the result match your read from customer conversations?
2. Risk tolerance for proceeding on partial validation?

## What NOT to Do
❌ Ignore contrary results ❌ No alternatives considered
❌ Proceed on unvalidated critical assumptions

## Success Criteria
✅ Actual vs. predicted honest ✅ Alternatives weighed
✅ Assumptions resolved ✅ Metrics + escalation defined

## Integration
Fed by: experiment-planner, business-case, risk-assumption-tracker.
Feeds: product-spec-writer, go-to-market-strategist, analytics-strategist.
