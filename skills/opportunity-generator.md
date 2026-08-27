# Opportunity-Generator Skill

## Role
Turn synthesized insights into opportunity candidates — problems worth solving,
framed solution-agnostically, evidence-backed.

## When to Use
- After a synthesis exists (researcher output)
- To convert insight into a decidable set of opportunities

## Reads First
- The synthesis (`artifacts/synthesis/<ID>.md`) · `product-strategy` (STRAT-###)
  as a filter if it exists · `knowledge/company.md` (non-goals)

## Critical Constraints
- Frame the PROBLEM, not a solution ("PMs spend 4hrs/week", not "build a tool")
- Every opportunity evidence-backed with frequency
- List key assumptions explicitly; mark unvalidated ones
- Respect company non-goals; flag opportunities that conflict with strategy

## Process
1. Read synthesis; identify distinct problem spaces
2. Generate 3–5 opportunities, each: problem, why it matters, evidence,
   assumptions, hypotheses to test
3. Assess signal strength per opportunity
4. Flag strategy fit / non-goal conflicts
5. Produce `artifacts/<project>/opportunities/O-###.md` (one file each)

## Output
Per opportunity: problem statement (specific + quantified), solution-agnostic
reframe, key assumptions, testable hypotheses, evidence strength, next step.
(See evaluation-framework.md → Opportunity rubric; passing 14/21.)

## Questions Agent MUST Ask
1. Any strategic filter (STRAT-###) to prioritize against?
2. Segment focus?

## What NOT to Do
❌ Propose solutions disguised as opportunities ❌ Unsourced opportunities
❌ Ignore company non-goals

## Success Criteria
✅ Problem-framed ✅ Evidence + frequency ✅ Assumptions listed
✅ Hypotheses testable ✅ Strategy fit checked

## Integration
Fed by: researcher, product-strategy. Feeds: hypothesis-validator, roadmap-planner.
