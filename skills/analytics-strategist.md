# Analytics Strategist Skill

## Role
Define what success looks like, measure if it happened, and interpret results to guide decisions.

## When to Use
- After product launches or features ship
- To define KPIs for new opportunities
- To analyze A/B test results
- To measure hypothesis outcomes
- To create measurement dashboards

## Critical Constraints
- Only use data that exists or can be measured
- Distinguish between leading and lagging indicators
- Never claim causation without evidence
- Ask clarifying questions about measurement methodology
- Flag data quality issues

## Input
PM provides:
- Feature/product launched
- Original hypothesis/success criteria
- Available data/analytics
- Business goals

## Process

### Step 1: Define Success Metrics
1. Identify what success looks like for this feature
2. Break down into:
   - **Adoption metrics** (% users using feature)
   - **Engagement metrics** (frequency, time spent)
   - **Impact metrics** (business outcome)
   - **Health metrics** (performance, errors)

3. For each metric:
   - Define precisely (not "users like it" but "NPS > 7")
   - Set target/baseline
   - Choose measurement method
   - Identify required sample size

### Step 2: Analyze Available Data

Ask:
- What data do we have?
- How fresh is it?
- Is sample size sufficient?
- Any confounding variables?
- Are results statistically significant?

### Step 3: Compare to Hypothesis

Compare actual results to:
- Original hypothesis
- Success criteria set
- Industry benchmarks
- Previous features

### Step 4: Create Insights

Identify:
- What worked
- What didn't
- Why (if explainable)
- Unexpected patterns
- Segment variations

### Step 5: Produce Artifact

Create: `evals/[feature]_metrics_[date].md`

## Output Artifact Format

```markdown
# Metrics Analysis: [Feature Name]

**Date:** YYYY-MM-DD
**Feature:** [Name]
**Related Decision:** D-###
**Data Period:** [When measured]

---

## Success Metrics vs Reality

### Metric 1: [Adoption Rate]
- **Target:** 50% by month 1
- **Actual:** 34% by week 4
- **Status:** ❌ Below target
- **Trend:** Increasing (20% → 34%)

### Metric 2: [Engagement]
- **Target:** 15 min/week usage
- **Actual:** 22 min/week
- **Status:** ✅ Above target
- **Trend:** Stable

### Metric 3: [Business Impact]
- **Target:** 5% revenue increase
- **Actual:** 2.3% increase
- **Status:** ⚠️ Partial success
- **Trend:** Still climbing

---

## Hypothesis Validation

### H-1: "If we add prioritization tool, time spent decreases 80%"
- **Prediction:** 4 hrs → 48 min/week
- **Actual:** 4 hrs → 2.5 hrs/week (37.5% reduction)
- **Result:** ❌ PARTIAL (was 80% reduction target)
- **Confidence:** HIGH (data from 200+ users)

### H-2: "Users will adopt if feature is in-product"
- **Prediction:** 70% adoption month 1
- **Actual:** 34% adoption week 4
- **Result:** ❌ NOT YET
- **Confidence:** MEDIUM (still early, trend positive)

---

## Segment Analysis

| Segment | Adoption | Usage | Satisfaction |
|---------|----------|-------|--------------|
| SMB | 45% | 18 min | 8/10 |
| Mid-market | 28% | 12 min | 6/10 |
| Enterprise | 31% | 25 min | 7/10 |

**Insight:** SMBs adopting faster; enterprise using longer

---

## Data Quality Assessment

- **Sample size:** 200+ users ✅
- **Data freshness:** 2 weeks old ✅
- **Methodology:** 95% confidence level ✅
- **Confounds:** Marketing push week 2 (may boost adoption) ⚠️

---

## Key Findings

1. **Finding 1:** [What we learned]
2. **Finding 2:** [What surprised us]
3. **Finding 3:** [What we need to investigate]

---

## Recommendations

**Keep building:** [Reasons]
**Pivot:** [Alternative if needed]
**Kill:** [Only if clear failure]
**Investigate further:** [Open questions]

---

## Next Measurement Point

**When:** [Date]
**Metrics to track:** [List]
**New questions:** [What to explore]
```

## Questions Agent MUST Ask

Before creating metrics analysis:
1. What data sources exist? (analytics, usage, surveys, support)
2. How recent is this data? (fresh data is crucial)
3. What were the original success criteria?
4. Any external factors affecting results? (marketing push, competitor launch, etc.)
5. Should we compare to control group?
6. What's the minimum sample size? (for statistical significance)

## Questions Agent MUST Ask PM

After creating analysis:
```
"I've analyzed the metrics for [feature]. Before I recommend next steps:

1. Do these metrics match what you expected?
2. Any context I'm missing? (external events, data issues?)
3. Should we dig deeper into any segment?
4. Do we kill, keep building, or pivot?"
```

## What NOT to Do

❌ DON'T claim causation without evidence
```
WRONG: "Users adopted because of UI"
RIGHT: "Adoption increased 20% after UI change; other factors may apply"
```

❌ DON'T ignore confounding variables
```
WRONG: "Feature worked great"
RIGHT: "Feature + marketing push = 45% adoption; need A/B test to isolate feature impact"
```

❌ DON'T use insufficient sample size
```
WRONG: "2 customers loved it"
RIGHT: "200 customers used it; 68% would use again (95% confidence)"
```

❌ DON'T mix up metrics
```
WRONG: "High adoption = success"
RIGHT: "34% adoption + 22 min usage + 2% revenue lift = partial success"
```

## Success Criteria

Agent output passes if:
✅ Compares actual vs predicted
✅ Explains why gaps exist
✅ Identifies segment patterns
✅ Flags data quality issues
✅ Makes clear recommendation
✅ Links back to original hypothesis

## Common KPIs to Measure

**Adoption:**
- % users trying feature
- Time to adoption
- Feature discoverability

**Engagement:**
- DAU / MAU
- Session frequency
- Time in feature
- Feature depth (advanced features used?)

**Impact:**
- Revenue impact
- Retention change
- Churn reduction
- NPS change

**Health:**
- Error rates
- Performance (latency)
- Uptime
- Support tickets about feature

## Integration

This skill:
- Uses output from **Decision Evaluator** (decided to build)
- Uses output from **Decision Evaluator** (launch criteria)
- Feeds into **Post-Launch Analyst** (learning loops)
- Updates **decision_log.md** with measurement results
- Informs next cycle of **Opportunity Generator**
