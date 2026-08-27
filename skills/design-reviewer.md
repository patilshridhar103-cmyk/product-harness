# Design-Reviewer Skill

## Role
Critique a rendered prototype/wireframe against UX best practices before it goes to
handover — usability, hierarchy, states, accessibility.

## When to Use
- After a design runtime renders a prototype (from prototype-brief)
- Before design-handover

## Reads First
- The BRIEF (`BRIEF-###`) + rendered output · `knowledge/product.md` (design system)

## Critical Constraints
- Check against the brief's intent + hypothesis
- Verify all states present (empty/loading/error/success), not just happy path
- Reference the design system; flag one-off deviations
- Give specific, actionable feedback with alternatives

## Process
1. Review rendered output vs. the brief
2. Assess usability, hierarchy, IA, accessibility
3. Check state coverage + edge cases
4. Give prioritized, specific feedback
5. Produce a critique note (feeds iteration + design-handover)

## Output
Prioritized critique · state-coverage check · a11y check · specific fixes.

## Questions Agent MUST Ask
1. Is this the version we're iterating on or the final?
2. Any constraint from product.md I should weight heavily?

## What NOT to Do
❌ Vague feedback ("make it cleaner") ❌ Ignore missing states

## Success Criteria
✅ Specific + actionable ✅ States checked ✅ A11y checked ✅ Design-system referenced

## Integration
Fed by: prototype-brief (+ design runtime). Feeds: design-handover (iteration loop).
