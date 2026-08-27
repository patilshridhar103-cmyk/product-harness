# Hypothesis-Validator Skill

## Role
Turn an opportunity into a testable hypothesis with clear success/failure criteria
and the assumptions it rests on.

## When to Use
- After an opportunity is selected to pursue
- Before designing an experiment

## Reads First
- The opportunity (`O-###`) · related synthesis

## Critical Constraints
- Must be an if/then/for-whom statement
- Success AND failure criteria, both with specific thresholds
- List assumptions that would break it
- Grounded in the opportunity's evidence

## Process
1. Read the opportunity + its evidence
2. Write the if/then/for-whom hypothesis
3. Define success thresholds (specific numbers) + failure thresholds
4. List load-bearing assumptions
5. Recommend a test approach (hand to experiment-planner)
6. Produce `artifacts/<project>/hypotheses/H-###.md`

## Output
If/then statement · evidence base · success criteria (thresholds) · failure
criteria · assumptions · recommended test. (evaluation-framework.md → Hypothesis
rubric; passing 14/21.)

## Questions Agent MUST Ask
1. What metric defines success, and at what threshold?
2. What would prove this false?

## What NOT to Do
❌ Vague hypotheses ("users will like it") ❌ Missing failure criteria
❌ Untestable claims

## Success Criteria
✅ Clear if/then ✅ Testable ✅ Success + failure thresholds
✅ Assumptions listed ✅ Test plan outlined

## Integration
Fed by: opportunity-generator. Feeds: experiment-planner, risk-assumption-tracker.
