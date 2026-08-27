# Artifact Templates

Agent must use these templates. This ensures consistency, readability, and compliance with evaluation framework.

Copy and paste these when creating artifacts.

---

## 1. Synthesis Template

**File:** `synthesis/insights_[session_date].md`

```markdown
# Synthesis: Evidence Analysis [DATE]

**Date:** YYYY-MM-DD  
**Session:** [Number]  
**Evidence Reviewed:** [# of interviews, # support tickets, # datasets]  
**Data Age:** [Newest: X days old, Oldest: X days old]

---

## Pain Points (Ranked by Signal Strength)

### Pain Point #1: [SPECIFIC NAME]

**Signal Strength:** HIGH  
**Frequency:** X/X sources (X%)  
**Quantification:** [Specific number: hours/week, failures/month, etc.]

**Evidence:**
- [Customer quote]: "[Direct quote with context]" - Source: [Name, Role, Date]
- [Customer quote]: "[Direct quote]" - Source: [Name, Role, Date]
- [Data point]: [Support tickets mentioning X: N in Jan 2025]
- [Data point]: [Analytics: X% of users report Y problem]

**Impact Level:**
- Pain intensity: HIGH / MEDIUM / LOW
- Frequency: Daily / Weekly / Monthly
- Workaround available: Yes / No

### Pain Point #2: [SPECIFIC NAME]

**Signal Strength:** MEDIUM  
**Frequency:** X/X sources (X%)  

[Same format as above]

---

## Feature Requests (By Frequency)

### Request #1: [Feature]

**Frequency:** X/X customers (X%)  
- [Customer 1]: "[Direct quote]"
- [Customer 2]: "[Direct quote]"

**Underlying Need:** [What customer actually needs vs what they asked for]

---

## Contradictions Found ⚠️

### Contradiction #1: [Description]

**Observation A:** [Evidence point A]  
- Source: [Who said this]

**Observation B:** [Evidence point B - contradicts A]  
- Source: [Who said this]

**Implication:** [What does this contradiction mean?]  
**Action needed:** [Should we investigate deeper?]

---

## Patterns Across Segments

### Pattern by Company Size

| Size | Pain | Evidence | Signal |
|------|------|----------|--------|
| SMB (1-50) | [Pain] | [# mentions] | HIGH |
| MID (50-500) | [Pain] | [# mentions] | MEDIUM |
| ENT (500+) | [Pain] | [# mentions] | LOW |

### Pattern by User Role

| Role | Pain | Evidence | Signal |
|------|------|----------|--------|
| PM | [Pain] | [# mentions] | HIGH |
| Eng | [Pain] | [# mentions] | MEDIUM |

---

## Data Quality Assessment

| Source | Quality | Freshness | Reliability |
|--------|---------|-----------|-------------|
| Customer interviews | HIGH | Recent (0-30 days) | HIGH |
| Support tickets | HIGH | Recent (0-30 days) | HIGH |
| Analytics | MEDIUM | Current (real-time) | HIGH |
| [Other] | MEDIUM | Older (90 days) | MEDIUM |

---

## Missing Evidence / Gaps

- [ ] No data on X (we need this to understand Y)
- [ ] Data is old (6+ months): [Which data]
- [ ] Only 5 customers interviewed (low sample size)
- [ ] No mobile user data
- [ ] No churn data

**Recommendation:** [Wait for evidence / Proceed with gap / Clarify with PM]

---

## Top 3 Findings

1. **[Highest signal finding]** (X/X sources, HIGH signal)
   - Evidence: [One sentence]
   - Action: [What should we do with this?]

2. **[Second finding]** (X/X sources, MEDIUM signal)
   - Evidence: [One sentence]
   - Action: [What should we do with this?]

3. **[Third finding]** (X/X sources, MEDIUM signal)
   - Evidence: [One sentence]
   - Action: [What should we do with this?]

---

## Recommendation for Next Step

**Ready for:** Opportunity generation / Deeper investigation / More data collection

**Confidence level:** HIGH / MEDIUM / LOW

**Reasoning:** [1-2 sentences on why we're ready or not]
```

---

## 2. Opportunity Template

**File:** `opportunities/O-###_[Name].md`

```markdown
# Opportunity O-###: [SPECIFIC OPPORTUNITY NAME]

**Created:** YYYY-MM-DD  
**Status:** Candidate / Validated / Approved  
**Related:** [Links to synthesis, hypothesis, etc.]

---

## Problem Statement

### What's the Problem?

[Specific, not a solution]

Example:
- ❌ WRONG: "We should build a prioritization tool"
- ✓ RIGHT: "PMs spend 4 hours/week manually prioritizing features"

### Why Does It Matter?

- **Impact:** [Quantified - hours/week, $K/year, % of customers]
- **Frequency:** [How often does this problem occur]
- **Severity:** [Critical / High / Medium / Low]

### Evidence

- **Frequency:** X/X customers mentioned this (X%)
- **Quotes:** 
  - "[Quote 1]" - [Source, Date]
  - "[Quote 2]" - [Source, Date]
- **Data:** [Support tickets / analytics / metrics showing problem]

---

## The Opportunity

### Reframe (Solution-Agnostic)

[NOT: "Build X"]  
[BUT: "Help customers achieve Y"]

Example:
- ❌ "Build a prioritization tool"
- ✓ "Help PMs make prioritization decisions faster and with more confidence"

### Opportunity Scope

**Addressable by:**
- Tool
- Process change
- Better data/information
- Training
- [Other]

**Boundaries:**
- In scope: [What's included]
- Out of scope: [What's not included, and why]

---

## Key Assumptions

### Assumption A-1: [Specific Assumption]

**Evidence supporting it:** [What makes us believe this is true?]

**Risk if wrong:** [What breaks if this is false?]

**How to test:** [How do we validate before building?]

### Assumption A-2: [Specific Assumption]

[Same format]

---

## Hypotheses to Test

### Hypothesis H-1: [If/Then statement]

**If:** [Action we could take]  
**Then:** [Expected outcome]

**Metric:** [How we'll measure]

**Success criteria:** [Specific threshold]

### Hypothesis H-2: [If/Then statement]

[Same format]

---

## Evidence Strength

| Evidence | Frequency | Signal |
|----------|-----------|--------|
| [Pain point 1] | X/X (X%) | HIGH |
| [Pain point 2] | X/X (X%) | MEDIUM |
| [Request 1] | X/X (X%) | MEDIUM |

**Overall Signal Strength:** HIGH / MEDIUM / LOW

**Why:** [One sentence on what makes this opportunity valuable]

---

## Potential Challenges

- **Adoption:** [Risk that customers won't use solution]
- **Competition:** [Existing solutions customers might prefer]
- **Technical:** [Possible technical blockers]
- **Market:** [Market size / addressable segments]

---

## Next Steps

**Validate:** Hypothesis H-1 and H-2  
**Method:** [Test approach - survey, prototype, interview, etc.]  
**Timeline:** [How long will validation take?]  
**Owner:** [Who owns this?]

---

## Success Metrics (Post-Launch)

If we solve this opportunity, we'll see:
- [Metric 1]: Current X → Target Y
- [Metric 2]: Current X → Target Y
- [Metric 3]: Current X → Target Y

---

## Decision Checklist

- [ ] Problem is evidence-backed (not assumed)
- [ ] Opportunity scope is clear (not a solution)
- [ ] Key assumptions are listed
- [ ] At least 2 hypotheses to test
- [ ] Next step is clear
```

---

## 3. Hypothesis Template

**File:** `hypotheses/H-###_[Name].md`

```markdown
# Hypothesis H-###: [SPECIFIC HYPOTHESIS]

**Created:** YYYY-MM-DD  
**Status:** Candidate / Testing / Validated / Invalidated  
**Related:** [Opportunity O-###, Experiment E-###]

---

## The Hypothesis

### If/Then Statement

**If** [specific action/solution]:  
**Then** [specific outcome will happen]:  
**For** [which user/customer type]:  

### Example:
**If** we provide a structured prioritization tool,  
**Then** PMs will spend 80% less time prioritizing,  
**For** SMB product managers.

---

## Why We Believe This

### Evidence Base

- **Opportunity:** [Related to O-###]
- **Supporting evidence:** [What makes us think this is true?]
- **Similar patterns:** [Have we seen this work elsewhere?]

### Assumptions Required

For this hypothesis to be true, we must assume:
1. [Assumption A-1]
2. [Assumption A-2]
3. [Assumption A-3]

**If any of these are false, the hypothesis likely fails.**

---

## Success & Failure Criteria

### Success (Hypothesis is TRUE)

✓ The hypothesis is confirmed when:
- [Specific metric] reaches [target threshold]
  - Example: "Time spent < 1 hour/week"
- [Specific adoption metric] reaches [threshold]
  - Example: "> 70% of test users adopt it"
- [Specific outcome metric] shows [result]
  - Example: "Customers report satisfaction > 7/10"

### Failure (Hypothesis is FALSE)

✗ The hypothesis is rejected when:
- [Specific metric] fails to reach [threshold]
  - Example: "Time spent still > 2 hours/week"
- [Adoption metric] stays below [threshold]
  - Example: "< 30% adoption"
- [Outcome metric] shows opposite result
  - Example: "Customer satisfaction < 5/10"

---

## Test Plan

### Recommended Test: [Option A / B / C]

**Duration:** [Time required]  
**Sample size:** [Number of customers]  
**Cost:** [Estimated PM hours + resources]  

**Method:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Measurement:**
- [How you'll measure success criteria 1]
- [How you'll measure success criteria 2]

**Risks:**
- [Risk 1 + mitigation]
- [Risk 2 + mitigation]

### Alternative Tests

**Option B:** [Brief description]  
- Pros: [Advantage]
- Cons: [Disadvantage]

**Option C:** [Brief description]  
- Pros: [Advantage]
- Cons: [Disadvantage]

---

## Timeline

- **Prep:** [X days]
- **Execution:** [X days]
- **Analysis:** [X days]
- **Total:** [X days]

---

## What We'll Learn

If successful:
- ✓ [What we'll know]
- ✓ [What we'll know]
- ✓ [What we'll know]

If unsuccessful:
- ✗ [What we'll know]
- ✗ [Pivot direction 1]
- ✗ [Pivot direction 2]

---

## Owner & Status

**Owner:** [Who runs this test?]  
**Status:** PENDING → TESTING → COMPLETE  
**Result:** [To be filled after test]

---

## Key Questions

Before testing, confirm with PM:
1. [Clarification question 1?]
2. [Scope question 2?]
3. [Constraint question 3?]
```

---

## 4. Experiment Plan Template

**File:** `experiments/E-###_[Name].md`

```markdown
# Experiment E-###: [EXPERIMENT NAME]

**Created:** YYYY-MM-DD  
**Hypothesis:** H-### [Link to hypothesis being tested]  
**Status:** Planned / Running / Complete  
**Timeline:** [Start date] - [End date]

---

## The Test

### What We're Testing

**Hypothesis:** H-### - [If/Then statement]

**Question:** [What specific question are we answering?]

### Why This Test

**Why now:** [What makes this urgent?]  
**Why this method:** [Why this test vs alternatives?]  
**Why sample size N:** [Statistical justification]

---

## Test Design

### Sample

**Target N:** [Number of test subjects]  
**Selection criteria:** [Who are we testing with?]

**Specific customers:**
- [Customer 1]: [Reason]
- [Customer 2]: [Reason]
- [Customer 3]: [Reason]

### Method

**Approach:** Quick prototype / Deep prototype / Wizard of Oz / Survey / Interview

**Steps:**
1. [Detailed step 1]
2. [Detailed step 2]
3. [Detailed step 3]

### Timeline

| Phase | Duration | Owner | Notes |
|-------|----------|-------|-------|
| Prep | [X days] | [Person] | [What gets done] |
| Run | [X days] | [Person] | [What happens] |
| Analyze | [X days] | [Person] | [How we interpret] |

**Total:** [X days]  
**Start date:** [When]  
**End date:** [When]

---

## Success Criteria

### Success (Hypothesis Confirmed)

✓ Test passes if:
- [Metric 1]: [Specific number/threshold]
- [Metric 2]: [Specific number/threshold]
- [Metric 3]: [Specific number/threshold]

**Example:** "4/5 customers report time savings of >60%"

### Failure (Hypothesis Rejected)

✗ Test fails if:
- [Metric 1]: [Falls below X]
- [Metric 2]: [Falls below Y]
- [Metric 3]: [Universal complaint about Z]

### Inconclusive (Keep Learning)

? Test is inconclusive if:
- [Results are mixed, e.g., 3/5 pass, 2/5 don't]
- [Need to refine hypothesis]
- [Need bigger sample size]

---

## Resource Plan

### Team

| Role | Hours | Cost | Notes |
|------|-------|------|-------|
| PM (you) | [X hrs] | [Cost] | Design + execution |
| Engineer | [X hrs] | [Cost] | Prototype [feature] |
| Research | [X hrs] | [Cost] | [Task] |
| Customers | [X hrs] | [Cost] | Beta testing |

**Total cost:** [$ or time estimate]

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| [Customers don't respond] | Medium | Critical | [Have backup list] |
| [Prototype breaks] | Low | High | [Test internally first] |
| [Results are ambiguous] | Low | Medium | [Pre-define criteria] |

---

## Measurement Plan

### Data Collection

| Metric | How we'll measure | When | Owner |
|--------|-------------------|------|-------|
| Time spent | Manual log by customer | Daily | Customer |
| Satisfaction | Post-test survey | Day 7 | PM |
| Adoption | Usage analytics | Real-time | PM |
| Feedback | Interview notes | Day 6-7 | PM |

### Analysis Plan

**How we'll analyze:**
1. [Step 1: Collect data]
2. [Step 2: Aggregate]
3. [Step 3: Compare to success criteria]
4. [Step 4: Write recommendation]

**Timeline:** [X days after test ends]

---

## Decision Tree

```
If ALL success criteria met:
  → Hypothesis CONFIRMED
  → Recommendation: PROCEED to next phase
  → Next experiment: E-[next]

If MOST success criteria met:
  → Hypothesis PARTIALLY CONFIRMED
  → Recommendation: REFINE and retest
  → Next experiment: E-[revised]

If FEW success criteria met:
  → Hypothesis REJECTED
  → Recommendation: KILL or PIVOT
  → Options: [Pivot direction 1], [Pivot direction 2]
```

---

## Owner & Status

**Test Owner:** [Person running this]  
**Status:** PLANNED → RUNNING → COMPLETE  
**Result:** [To be filled after test completes]

---

## Pre-Test Checklist

- [ ] Hypothesis is clear (H-###)
- [ ] Success criteria defined (specific numbers)
- [ ] Sample customers confirmed and contacted
- [ ] Prototype / materials ready
- [ ] Measurement plan set
- [ ] PM approval on test plan
- [ ] Timeline realistic
```

---

## 5. Decision Template

**File:** `decisions/D-###_[Name].md`

```markdown
# Decision D-###: [DECISION NAME]

**Date:** YYYY-MM-DD  
**Decision:** BUILD / KILL / TEST / PIVOT  
**Related:** [Opportunity O-###, Experiment E-###]

---

## The Decision

### What We Decided

**Decision:** [BUILD / KILL / TEST / PIVOT]

[Feature/Product Name]

---

## Why We Decided This

### Evidence Summary

**Evidence supporting this decision:**
- [Experiment E-### result: X/Y customers confirmed hypothesis]
- [Customer feedback: "Would definitely use this"]
- [No competitor in this space]
- [Addresses #1 pain point]

**Evidence against:**
- [Consideration 1]
- [Consideration 2]

---

## Hypotheses Validated

| Hypothesis | Result | Confidence |
|-----------|--------|-----------|
| H-1: [If/then] | CONFIRMED ✓ | HIGH (4/5 customers) |
| H-2: [If/then] | CONFIRMED ✓ | HIGH (data shows) |
| H-3: [If/then] | PARTIAL ✓ | MEDIUM (3/5 confirmed) |

---

## Alternatives Considered

### Option A: BUILD [Decision chosen]
**Pros:**
- [Pro 1]
- [Pro 2]
- [Pro 3]

**Cons:**
- [Con 1]
- [Con 2]

### Option B: WAIT for more data
**Pros:** [Pros]  
**Cons:** [Cons]  
**Why rejected:** [Why this didn't win]

### Option C: PARTNER with vendor
**Pros:** [Pros]  
**Cons:** [Cons]  
**Why rejected:** [Why this didn't win]

---

## Key Assumptions

**Critical assumptions this decision depends on:**

1. **Assumption 1:** [Specific]
   - Confidence: HIGH / MEDIUM / LOW
   - Risk if wrong: [What breaks?]
   - How to monitor: [How we'll know if wrong]

2. **Assumption 2:** [Specific]
   - [Same format]

---

## Implementation Plan

**Timeline:**
- Phase 1 [Dates]: [What gets done]
- Phase 2 [Dates]: [What gets done]
- Phase 3 [Dates]: [What gets done]

**Owner:** [Person responsible]  
**Dependencies:** [What must happen first?]  
**Blockers:** [What could delay this?]

---

## Success Metrics

**We'll know this decision was right if:**
- [Metric 1]: Current X → Target Y by [date]
- [Metric 2]: Current X → Target Y by [date]
- [Metric 3]: Current X → Target Y by [date]

**We'll know this decision was wrong if:**
- [Negative metric 1]: [Threshold indicating failure]
- [Negative metric 2]: [Threshold indicating failure]

---

## Escalation Path

**If assumptions change:** Escalate to [Person]  
**If engineering timeline extends:** Escalate to [CTO]  
**If customer feedback contradicts hypothesis:** Escalate to [PM Lead]  
**If market changes:** Escalate to [CEO]

**Regular review:** Weekly [Day] at [Time]

---

## Next Steps

1. [Step 1]: [Owner], by [Date]
2. [Step 2]: [Owner], by [Date]
3. [Step 3]: [Owner], by [Date]

---

## Sign-Off

**PM:** [Name] - [Date]  
**Product Lead:** [Name] - [Date]  
**CTO:** [Name if needed] - [Date]

```

---

## 6. Product Spec Template

**File:** `specs/PS-###_[Name].md`

```markdown
# Product Spec PS-###: [FEATURE/PRODUCT NAME]

**Date:** YYYY-MM-DD  
**Status:** Draft / Approved / In Development  
**Related:** [Decision D-###, Opportunity O-###]

---

## Overview

### What Are We Building?

[One sentence description]

### Why?

[Problem we're solving + evidence]

### For Whom?

[Target user + role]

---

## Problem & Opportunity

### The Problem

[Specific problem with evidence and quantification]

### The Opportunity

[How we're addressing it]

---

## User Value

### For End Users

[Specific benefits for primary user]

### For Business

[Specific business benefits]

---

## Core Features

### Feature 1: [Feature Name]

**What:** [What does this feature do?]

**Why:** [Why is this critical?]

**User story:**
As [user role]  
I want [goal]  
So that [benefit]

**Acceptance Criteria:**
- [ ] [Specific testable criterion]
- [ ] [Specific testable criterion]
- [ ] [Specific testable criterion]

### Feature 2: [Feature Name]

[Same format]

---

## Out of Scope

**Not in MVP:**
- [Feature not included + why]
- [Feature not included + why]

**Future versions:**
- [Feature for v2]
- [Feature for v3]

---

## Technical Requirements

- **Performance:** [Latency targets, throughput, etc.]
- **Scale:** [Expected users, data volume]
- **Reliability:** [Uptime targets, error rates]
- **Security:** [Auth, data protection, compliance]
- **Integrations:** [3rd-party systems to connect]

---

## Design Considerations

### User Flow

[Brief description or wireframe reference]

### UI/UX Principles

- [Principle 1]
- [Principle 2]
- [Principle 3]

---

## Success Metrics

**Adoption:**
- Target: [% of users adopt by date]

**Engagement:**
- Target: [Usage metric by date]

**Impact:**
- Target: [Business metric by date]

---

## Timeline & Milestones

| Phase | Duration | Owners | Deliverables |
|-------|----------|--------|--------------|
| Design | [X weeks] | [Team] | [Spec, wireframes] |
| Build | [X weeks] | [Team] | [Working code] |
| Test | [X weeks] | [Team] | [QA sign-off] |
| Launch | [X weeks] | [Team] | [Live in production] |

**Go-live date:** [Specific date]

---

## Risks & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| [Adoption slower than expected] | Medium | High | [Mitigation: strong onboarding] |
| [Engineering complexity higher] | Medium | High | [Mitigation: phased rollout] |

---

## Dependencies

- [ ] [Dependency 1]
- [ ] [Dependency 2]
- [ ] [Dependency 3]

---

## Handoff to Engineering

**Engineer:** [Name]  
**Start date:** [Date]  
**Contact:** [How to reach PM]

**Raw materials provided:**
- [x] Design specs
- [x] User stories + acceptance criteria
- [x] Technical requirements
- [x] Success metrics + instrumentation

```

---

## Using These Templates

### For Agents

Copy the relevant template.  
Fill in all fields.  
Run through evaluation framework rubric.  
If score < minimum, revise before showing PM.

### For PMs

Check that:
- ✓ All required sections are filled
- ✓ Evidence is sourced (not assumed)
- ✓ Specific numbers (not "some" or "many")
- ✓ Ready for next step

---

## Template Versions

As your harness matures, you can:
- Add new sections to templates (consensus with team)
- Create variant templates (Quick vs Detailed)
- Remove sections that never get used
- Link between templates (PS links to D, D links to E, etc.)

Keep templates in decision_log.md for continuity.
