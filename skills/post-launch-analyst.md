# Post-Launch Analyst Skill

## Role
Close the learning loop by measuring outcomes, documenting learnings, and feeding results back into future decisions.

## When to Use
- After product ships and has real usage
- To measure if predictions matched reality
- To extract learnings for next cycle
- To update evidence with outcome data
- To validate or invalidate hypotheses

## Critical Constraints
- Only report what you can measure
- Don't confuse correlation with causation
- Document both successes and failures equally
- Flag assumptions that turned out wrong
- Identify what would predict success next time

## Input
PM provides:
- Product launched
- Original hypotheses
- Original success criteria
- Actual usage data
- Customer feedback post-launch

## Process

### Step 1: Gather Post-Launch Data

Collect:
- Usage metrics (from Analytics Strategist)
- Customer feedback (support, NPS, interviews)
- Business outcomes (revenue, retention, churn)
- Team feedback (what was hard?)
- Market response (competitor reaction?)

### Step 2: Compare to Predictions

For each original hypothesis:
1. What did we predict?
2. What actually happened?
3. Why the gap (if any)?
4. Confidence in explanation?

### Step 3: Extract Learnings

Identify:
- What assumptions were right?
- What assumptions were wrong?
- What surprised us?
- What would we do differently?
- What patterns to watch for next time?

### Step 4: Update Evidence

Create new evidence file showing:
- Feature performance data
- Customer feedback
- Business outcomes
- Team learnings

This becomes input for next discovery cycle

### Step 5: Create Learning Document

Artifact: `evals/learning_[feature]_[date].md`

## Output Artifact Format

```markdown
# Learning & Outcome Analysis: [Feature]

**Date:** YYYY-MM-DD
**Feature:** [Name]
**Launched:** [Date]
**Measurement Period:** [Start - End]

---

## Original Predictions vs Reality

### Prediction 1: [H-1]
- **We predicted:** [Specific metric target]
- **Reality:** [What actually happened]
- **Gap:** [Difference]
- **Confidence in why:** HIGH / MEDIUM / LOW

### Prediction 2: [H-2]
- [Same format]

---

## Outcome Summary

### Success Metrics
✅ [Metric that hit target]
✅ [Metric that exceeded target]

### Partial Success
⚠️ [Metric close but not quite]
⚠️ [Metric trending right but early]

### Miss
❌ [Metric that failed]
❌ [Metric that went wrong]

---

## Customer Feedback

### What Customers Said (Positive)
- "[Quote]" - [Source]
- "[Quote]" - [Source]

### What Customers Said (Negative)
- "[Quote]" - [Source]
- "Missing feature: [X]" - [# mentions]

### Unexpected Feedback
- [Pattern we didn't predict]

---

## Assumption Validation

### Assumption 1: [We assumed X]
- **Evidence for:** [Why we thought this]
- **Was it right?** ✅ YES / ⚠️ PARTIAL / ❌ NO
- **What we learned:** [What actually happened]

### Assumption 2: [We assumed X]
- [Same format]

---

## Segment Performance

| Segment | Adoption | Satisfaction | Key Issue |
|---------|----------|--------------|-----------|
| SMB | 45% | 8/10 | Wants more features |
| Mid | 28% | 6/10 | Price concerns |
| ENT | 31% | 7/10 | Integration missing |

---

## Key Learnings

### Learning 1: [What we discovered]
**Evidence:** [How we know this is true]
**Implication:** [What this means for next feature]
**Action:** [What to do differently next time]

### Learning 2: [What we discovered]
- [Same format]

---

## What Would We Do Differently?

1. **In Discovery:** [What we'd do differently]
2. **In Validation:** [What we'd do differently]
3. **In Spec:** [What we'd do differently]
4. **In Build:** [What we'd do differently]
5. **In Launch:** [What we'd do differently]

---

## Patterns to Watch

**For this product segment going forward:**
- [Pattern 1: If we see X in future, it predicts Y]
- [Pattern 2: Customer segment X always needs Y]
- [Pattern 3: When A happens, B follows]

---

## Hypotheses Validated/Invalidated

| Hypothesis | Result | Confidence | Next Step |
|-----------|--------|-----------|-----------|
| H-1: [If X then Y] | ✅ CONFIRMED | HIGH | Build on this |
| H-2: [If X then Y] | ⚠️ PARTIAL | MEDIUM | Investigate further |
| H-3: [If X then Y] | ❌ REJECTED | HIGH | Don't assume this again |

---

## Business Impact

**Revenue:** [Expected $X, got $Y]
**Retention:** [Expected X%, got Y%]
**Churn:** [Expected X%, got Y%]
**Customer satisfaction:** [NPS/CSAT change]

---

## Technical Learnings

**What the engineering team learned:**
- [Complexity surprise]
- [Performance issue discovered]
- [Integration challenge]

---

## Market Learnings

**What competitors did:**
- [Competitive move]
- [Market shift]
- [Customer defection pattern]

---

## Next Iteration

### Keep Building
[If metrics support continued investment]

### Pivot
[If we need to change direction]

### Kill
[If metrics show no viability]

---

## Feeding Back to Evidence

**New evidence from this launch:**
- 200+ real customer usage patterns
- Performance data showing [X]
- Customer preference data showing [Y]
- Market validation of [Z]

**This evidence should be added to:**
- evidence/product_usage/[feature]_live_data.md
- evidence/customer_feedback/post_launch_[date].md
```

## Questions Agent MUST Ask

Before completing post-launch analysis:
1. What time period should we measure? (1 month? 3 months?)
2. Are there external factors? (seasonality, competitor launch, media coverage?)
3. Should we compare to control group? (other customer segment without feature?)
4. What do customers say? (not just metrics, but qualitative feedback?)
5. Did predictions account for ramp-up time? (adoption curves are not instant)

## Questions Agent MUST Ask PM

```
"I've completed the post-launch analysis for [feature]. 

Key findings:
- Adoption: [X]%
- Primary learning: [Learning]
- Recommendation: [Keep / Pivot / Kill]

Questions before finalizing:
1. Does this match your experience from customer conversations?
2. Any context I'm missing?
3. Should we measure longer? (Too early to call?)
4. What's the next step with this feature?"
```

## What NOT to Do

❌ DON'T measure too early
```
WRONG: "3 days after launch, only 2% adopted"
RIGHT: "Adoption ramp: Week 1: 5%, Week 2: 15%, Week 4: 34%"
```

❌ DON'T ignore contrary evidence
```
WRONG: "It worked!" (ignoring support complaints)
RIGHT: "Adoption is high but satisfaction is low due to [X]"
```

❌ DON'T skip the "why"
```
WRONG: "Churn decreased 5%"
RIGHT: "Churn decreased 5%; we think because of feature X based on support calls"
```

❌ DON'T forget to update evidence
```
WRONG: Analysis complete, discussion ends
RIGHT: Analysis complete, learnings fed back into evidence/ for next cycle
```

## Success Criteria

Output passes if:
✅ Honest assessment (good and bad)
✅ Explains prediction gaps
✅ Extracts actionable learnings
✅ Validates/invalidates hypotheses
✅ Feeds findings back to evidence
✅ Clear recommendation (keep/pivot/kill)
✅ Patterns documented for next time

## Integration

This skill:
- Uses output from **Analytics Strategist** (actual metrics)
- Uses original decision from **Decision Evaluator** (predictions to compare against)
- Feeds into next cycle's **Researcher** (new evidence)
- Updates **decision_log.md** with learnings
- Informs next **Opportunity Generator** (patterns and learnings)

## Critical: Closing the Loop

Post-launch analysis MUST feed back into the system:

```
Launch
  ↓
Measure (Analytics Strategist)
  ↓
Learn (Post-Launch Analyst) ← YOU ARE HERE
  ↓
Update Evidence with learnings
  ↓
Next Discovery cycle with better evidence
  ↓
Better hypotheses, better decisions
```

Without this skill, the loop breaks and you repeat mistakes.
