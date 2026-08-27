# Experiment-Planner Skill

## Role
Design the cheapest test that credibly validates or kills a hypothesis.

## When to Use
- After a hypothesis is defined
- To validate assumptions before expensive build

## Reads First
- The hypothesis (`H-###`) · `knowledge/constraints.md` (budget, capacity)

## Critical Constraints
- Sample size justified · success/failure/inconclusive all pre-defined
- Prefer the fastest credible method (Wizard-of-Oz, prototype, survey)
- Realistic timeline + cost · risks with mitigations

## Process
1. Read the hypothesis + its success criteria
2. Propose 2–3 test options (fast→rigorous) with pros/cons
3. Recommend one; justify sample size + duration
4. Define success / failure / inconclusive thresholds
5. List risks + mitigations
6. Produce `artifacts/<project>/experiments/E-###.md`

## Output
Test design · sample + justification · timeline · success/failure/inconclusive
criteria · cost · risks · decision tree. (evaluation-framework.md → Experiment
rubric; passing 14/21.)

## Questions Agent MUST Ask
1. Can we reach customers directly?
2. Budget / timeline constraints?
3. 1-week or deeper test acceptable?

## What NOT to Do
❌ Vague sample ("a few customers") ❌ No failure threshold
❌ Building the full thing to "test" it

## Success Criteria
✅ Hypothesis linked ✅ Sample justified ✅ Criteria specific
✅ Cost defined ✅ Risks + mitigations

## Integration
Fed by: hypothesis-validator, risk-assumption-tracker, business-case (assumptions).
Feeds: decision-evaluator (results).
