# Product-Spec-Writer Skill

## Role
Write the detailed product (and engineering-handoff) spec from a validated
decision — clear enough to build, bounded enough to ship.

## When to Use
- After a BUILD decision
- Absorbing design-handover UI detail into a buildable spec

## Reads First
- The decision (`D-###`) · design-handover (`HANDOVER-###`) if design exists ·
  `knowledge/product.md` (stack, platform, design system)

## Critical Constraints
- Problem evidence-backed · scope explicitly bounded (in AND out)
- Acceptance criteria testable · success metrics specific
- Respect technical constraints from product.md

## Process
1. Read the decision + design handover
2. State problem, value prop, user story
3. Define core features with acceptance criteria
4. Bound scope (in/out); note technical requirements
5. Define success metrics + timeline
6. Produce `artifacts/<project>/specs/PS-###.md`

## Output
Problem · value prop · user story · features + acceptance criteria · out-of-scope
· technical requirements · success metrics · timeline · handoff. (evaluation-
framework.md → Spec rubric; passing 14/21.)

## Questions Agent MUST Ask
1. Target stack / platform confirmed?
2. Performance / scale requirements?
3. Integrations in scope for v1?

## What NOT to Do
❌ Vague acceptance criteria ❌ Unbounded scope ❌ Ignore product.md constraints

## Success Criteria
✅ Problem clear ✅ Requirements complete ✅ Criteria testable
✅ Scope bounded ✅ Metrics specific

## Integration
Fed by: decision-evaluator, design-handover, effort-estimator.
Feeds: engineering, launch-coordinator, analytics-strategist.
