# Effort-Estimator Skill

## Role
Estimate effort (story points, t-shirt sizes) and capacity so roadmap sequencing
and specs are grounded in reality.

## When to Use
- Before engineering starts · for roadmap sequencing · business-case cost input

## Reads First
- The spec (`PS-###`) or opportunity · `knowledge/constraints.md` (capacity)

## Critical Constraints
- Estimates reviewed with engineering, not invented by the agent
- Use relative sizing (Fibonacci / t-shirt), not false precision
- Surface dependencies and estimation risks

## Process
1. Break the work into estimable items
2. Propose relative estimates (flag as needing eng confirmation)
3. Identify dependencies + risks
4. Roll up into capacity view
5. Produce estimate + capacity note (feeds roadmap-planner, business-case)

## Output
Item estimates · dependencies · capacity roll-up · confidence/risks.

## Questions Agent MUST Ask
1. Has engineering reviewed these, or are they placeholders?
2. Any known technical unknowns to spike first?

## What NOT to Do
❌ Precise hour estimates from thin air ❌ Ignore dependencies

## Success Criteria
✅ Eng-reviewed ✅ Dependencies clear ✅ Capacity realistic

## Integration
Fed by: product-spec-writer. Feeds: roadmap-planner, business-case.
