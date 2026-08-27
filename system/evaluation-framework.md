# Evaluation Framework

Every artifact the agent creates must pass quality checks before PM approval.

The agent uses these rubrics to self-evaluate before showing PM.
PM uses these to decide: "Is this good enough to approve?"

---

## Synthesis Artifact

**Used by:** Researcher Agent  
**Purpose:** Extract patterns from raw evidence  
**File:** `synthesis/insights_*.md`

### Quality Rubric

| Criterion | Poor (0) | Fair (1) | Good (2) | Excellent (3) |
|-----------|----------|----------|----------|---------------|
| **Evidence Sourcing** | Claims not linked to evidence | Some claims linked, some not | Most claims linked to sources | Every claim has source + frequency |
| **Specificity** | Generic ("users want features") | Somewhat specific | Specific with context | Specific + quantified (8/12, "4 hrs/week") |
| **Contradictions** | Ignored or not mentioned | Some contradictions noted | Clear contradictions identified | Contradictions highlighted with implications |
| **No Speculation** | Includes opinions/guesses | Minimal speculation | No speculation, facts only | Clear distinction between facts and questions |
| **Frequency Counts** | No frequency data | Some frequencies | Most patterns have frequency | All patterns: # mentions / # total sources |
| **Signal Strength** | No assessment | Vague ("people mentioned") | Clear assessment (HIGH/MED/LOW) | Assessment with supporting data |
| **Missing Data Flagged** | Doesn't mention gaps | Mentions some gaps | Most gaps identified | All gaps identified with implications |

### Passing Score
**12/21 points minimum** (6/9 criteria at Fair level)

### Example: PASS

```markdown
# Synthesis: Customer Evidence Analysis

## Pain Points (Ranked by Frequency & Impact)

### 1. Prioritization Takes Too Much Time
**Frequency:** 9/12 interviews (75%)
**Impact:** HIGH (quantified)

**Evidence:**
- Sarah Chen: "I spend 4 hours a week in spreadsheets"
- Alex Patel: "2-hour sprint planning just to rank features"
- Jordan: "No good way to track customer requests"
- [6 more similar mentions]

**Signal Strength:** HIGH
- Consistent across company sizes
- Quantified impact (2-4 hours/week)
- Described as painful/urgent

### 2. Can't See ROI on Features
**Frequency:** 6/12 interviews (50%), 4/8 support tickets
**Impact:** MEDIUM

**Evidence:**
- Interview: "We ship features customers ask for but they don't use them"
- Support: "How do I know if a feature is working?"
- Analytics: No connection between feature requests and usage

**Signal Strength:** MEDIUM
- Mentioned by customers and support
- Pattern not as consistent as #1
- Less quantified

### 3. Analytics Feel Disconnected
**Frequency:** 5/12 interviews (42%), analytics data shows 12% usage
**Impact:** MEDIUM (unclear)

**Signal Strength:** MEDIUM-LOW
- Users mention it but behavior unclear
- Analytics usage is low but not explained
- Need clarification: Is low usage because it's not useful OR not discoverable?

## Missing Evidence
- No data on mobile prioritization workflow
- No support ticket analysis specifically for this topic
- No churn data linked to prioritization issues

**Note:** Data only 3 months old - still fresh.
```

### Example: FAIL

```markdown
# Synthesis: What Customers Want

Users struggle with priorities. They need better tools.

Many customers mentioned they want AI features.

Competitors are doing well because they ship faster.

Dashboard isn't used much because it's confusing.

Mobile users are different and need special attention.
```

**Why it fails:**
- ❌ No evidence links
- ❌ No frequency counts
- ❌ No quotes or sources
- ❌ Speculation ("need AI")
- ❌ No contradictions explored
- ❌ No signal strength assessment

---

## Opportunity Artifact

**Used by:** Opportunity Generator  
**Purpose:** Propose something to build  
**File:** `opportunities/O-###.md`

### Quality Rubric

| Criterion | Poor (0) | Fair (1) | Good (2) | Excellent (3) |
|-----------|----------|----------|----------|---------------|
| **Problem Clarity** | Vague or generic | Somewhat clear | Clear with context | Specific, quantified, evidence-backed |
| **Evidence Backing** | No evidence cited | Some evidence | Multiple evidence sources | 3+ evidence sources with frequency |
| **Not a Solution** | Proposes solution ("build tool") | Hints at solution | Problem-only framing | Solution-agnostic (problem, not solution) |
| **Key Assumptions Listed** | None listed | 1-2 listed | 3-4 listed | All assumptions explicit + testable |
| **Hypotheses Defined** | None | Vague | Clear hypotheses | 3+ clear, testable hypotheses |
| **Addressable Scope** | Too broad or too narrow | Somewhat focused | Well-scoped | Clear scope with boundaries |
| **Success Metrics** | None | Vague | Specified | Specific, measurable metrics |

### Passing Score
**14/21 points minimum** (5/7 criteria at Fair level or higher)

### Example: PASS

```markdown
# Opportunity O-001: Reduce Feature Prioritization Overhead

## Problem Statement
**The Problem:** Product managers spend 2-4 hours per week manually prioritizing features because they lack a tool that weights customer requests against business value.

**Why it matters:** 
- 9/12 customers mentioned this (75%)
- Time investment: 8-16 hours/month of PM work
- Workaround: Using spreadsheets (error-prone, hard to track)

**Evidence:**
- Sarah Chen (SaaS, 50 people): "4 hours weekly in spreadsheets"
- Alex Patel (SaaS, 200 people): "2-hour meeting every sprint just to prioritize"
- Jordan (SaaS, 20 people): "We use a shared Google sheet that nobody trusts"

## Opportunity
**NOT:** "Build a prioritization tool" ← This is solution
**BUT:** "Help PMs make prioritization decisions faster and with more confidence"

This could be solved by:
- Better tool
- Better process
- Better data visibility
- Any combination

## Key Assumptions

1. **Assumption A-1:** The problem is "lack of structure" not "unclear business value"
   - Evidence: Customers described "spreadsheets" and "meetings," not "don't know value"
   - Risk if wrong: They need help with business value definition, not structure
   - Test: Ask 5 customers: "What would help most: tool or training?"

2. **Assumption A-2:** Customers would switch tools (not use spreadsheets forever)
   - Evidence: 9/12 complained about spreadsheets
   - Risk if wrong: They'll keep using spreadsheets even with new tool
   - Test: Prototype test with 3 customers

3. **Assumption A-3:** This is a universal PM pain (not just our specific users)
   - Evidence: We've seen it with 9 customers
   - Risk if wrong: It's specific to our customer segment
   - Test: Research if other SaaS PMs have same problem

## Hypotheses to Validate

**H-1:** If we provide a structured prioritization approach, PMs will spend 80% less time prioritizing.
- Metric: Time spent on prioritization task (current: 4 hrs/week)

**H-2:** If we help structure prioritization, PM confidence in decisions will increase.
- Metric: PM satisfaction with decision ("Confident" vs "Uncertain")

**H-3:** If prioritization is faster, more features get shipped.
- Metric: Features shipped per quarter (current: X)

## Next Step
**Validate Hypothesis H-1 & H-2** with 5 customers using:
- Option A: Quick survey (1 week)
- Option B: Prototype (3 weeks)
- Option C: Wizard of Oz (2 weeks)

**Recommend:** Option A first (fastest validation)
```

### Example: FAIL

```markdown
# Opportunity: AI-Powered Prioritization Tool

Customers need better prioritization. We should build an AI tool that:
- Predicts which features to build
- Integrates with Jira
- Uses machine learning

This will make customers happy and increase retention.

Some customers mentioned prioritization issues.
```

**Why it fails:**
- ❌ Proposes solution ("AI tool") not problem
- ❌ No evidence cited
- ❌ No frequency or specifics
- ❌ No assumptions listed
- ❌ No hypotheses
- ❌ No scope boundaries

---

## Hypothesis Artifact

**Used by:** Hypothesis Validator  
**Purpose:** Define what you're testing  
**File:** `hypotheses/H-###.md`

### Quality Rubric

| Criterion | Poor (0) | Fair (1) | Good (2) | Excellent (3) |
|-----------|----------|----------|----------|---------------|
| **Clear If/Then** | Fuzzy hypothesis | Somewhat clear | Clear if/then | Specific: "If [action], then [outcome]" |
| **Testable** | Not testable | Hard to test | Testable | Very specific, measurable metric |
| **Based on Evidence** | No basis | Weak basis | Referenced evidence | Explicitly links to opportunity evidence |
| **Success Criteria** | None | Vague | Defined | Specific threshold (>70%, <2 hrs, etc.) |
| **Failure Criteria** | None | Vague | Defined | Specific threshold |
| **Assumptions Listed** | None | Some | Most | All assumptions that could break it |
| **Test Plan Outlined** | None | Vague | Clear | Specific, actionable test |

### Passing Score
**14/21 points minimum**

### Example: PASS

```markdown
# Hypothesis H-001: Prioritization Tool Reduces Time Spent

## Hypothesis Statement
**If** we provide PMs with a structured prioritization tool that weights criteria,  
**then** time spent on prioritization will decrease by at least 80% (from 4 hours to 48 minutes per week).

## Based on Evidence
- Opportunity O-001 identified prioritization as pain point
- 9/12 customers spend 2-4 hours/week on it
- Workaround: Manual spreadsheets (inefficient)
- Root cause: No structured approach

## Success Criteria
✓ **Hypothesis is TRUE if:**
- Users report spending <1 hour/week on prioritization (80%+ reduction)
- Time savings confirmed by usage analytics (session duration decreases)
- At least 70% of test users find tool "helpful"

✗ **Hypothesis is FALSE if:**
- Users still spend 3+ hours/week (no significant improvement)
- Tool adoption <30%
- Users say "nice but I don't use it"

## Assumptions That Could Break This

1. **A-1:** Users actually WANT to reduce time (not enjoy the process)
   - If wrong: They like the meetings/spreadsheet work
   - How to test: Ask directly in survey

2. **A-2:** The bottleneck is tool, not decision quality
   - If wrong: They could use spreadsheets faster but want better decisions
   - How to test: Prototype shows fast tool but they still want to "think about it"

3. **A-3:** Users will adopt a new tool (not stick with spreadsheets)
   - If wrong: "Nice feature but we'll keep using Excel"
   - How to test: Track actual usage, not just satisfaction

## Test Plan
**Option A (Recommended): Quick Prototype + Survey**
- Duration: 1 week
- Cost: Low
- Sample: 5 customers
- Method: 
  1. Create prioritization template in Notion
  2. Ask 5 customers to use it for 1 week
  3. Survey: Time spent, satisfaction, would use?
- Success: ≥3/5 say "this saves time" + would use

**Option B: Deeper Prototype**
- Duration: 3 weeks
- Cost: Medium
- Sample: 10 customers
- Method:
  1. Build working prototype
  2. Beta test with 10 customers
  3. Track actual usage time
  4. Post-test interview
- Success: Usage data shows 60%+ time reduction

**Option C: Wizard of Oz**
- Duration: 2 weeks
- Cost: Low
- Sample: 3 customers
- Method:
  1. Manually run prioritization for 3 customers
  2. Track their time investment
  3. Compare to their current process
- Success: They report time savings immediately
```

### Example: FAIL

```markdown
# Hypothesis: Users Want Better Prioritization

Users want a prioritization tool. This will help them. If we build it, they'll use it.

Success metric: They like it.
```

**Why it fails:**
- ❌ Not an if/then statement
- ❌ Not testable ("like it" is vague)
- ❌ No success criteria
- ❌ No failure criteria
- ❌ No assumptions

---

## Experiment Plan Artifact

**Used by:** Experiment Planner  
**Purpose:** Design how to validate hypothesis  
**File:** `experiments/E-###.md`

### Quality Rubric

| Criterion | Poor (0) | Fair (1) | Good (2) | Excellent (3) |
|-----------|----------|----------|----------|---------------|
| **Clear Hypothesis** | Vague | Somewhat clear | Clear | Explicitly linked to H-### |
| **Sample Size Justified** | No justification | Weak justification | Justified | Includes power calculation |
| **Timeline Realistic** | Unrealistic | Somewhat realistic | Realistic | Detailed schedule |
| **Success Criteria Clear** | Vague | Somewhat clear | Clear | Specific numbers/percentages |
| **Budget Defined** | Not defined | Vague | Defined | Detailed breakdown |
| **Risks Identified** | None | Some | Most | All risks + mitigations |
| **Execution Clear** | Unclear | Somewhat clear | Clear | Step-by-step instructions |

### Passing Score
**14/21 points minimum**

### Example: PASS

```markdown
# Experiment E-001: Prioritization Tool Validation

## Hypothesis Being Tested
H-001: If we provide a prioritization tool, time spent will decrease by 80%

## Experiment Option A: Quick Prototype (Recommended)

### Timeline
- Day 1: Create template
- Day 2-3: Invite 5 customers
- Day 4-5: They use template (1 week usage)
- Day 6-7: Interview + survey
- **Total: 1 week**

### Sample Size
- **N = 5 customers** (SMB, all current users)
- Rationale: Just enough to validate direction, not measure precisely
- Criteria: Different company sizes, both prioritization pain levels high

### Success Criteria
✓ **Test is SUCCESSFUL if:**
- ≥3/5 customers report time savings (any amount)
- ≥4/5 say "would use this tool"
- ≥3/5 say "saves at least 2 hours/week"
- No major usability blockers

✗ **Test is UNSUCCESSFUL if:**
- <2/5 report time savings
- <3/5 would use it
- Customers prefer their spreadsheets
- Universal complaint about usability

### Sample Selection
Customer list:
- Sarah Chen (SaaS, 50 people, high pain) ✓
- Alex Patel (SaaS, 200 people, high pain) ✓
- Jordan (SaaS, 20 people, high pain) ✓
- [2 others matching profile]

### Execution Details

**Step 1: Prepare Template (Day 1)**
- Create Notion template based on O-001 spec
- Test with internal team first
- Refine UX based on feedback

**Step 2: Invite Customers (Day 2-3)**
- Email: "We want your feedback on a prioritization template"
- Include: Template link + 2-min video showing how to use
- Ask: "Would you try this for 1 week?"
- Expected: 5+ responses (2/3 of invites)

**Step 3: Customer Usage (Day 4-5)**
- Customers use template for their next prioritization cycle
- You track: Usage (login time), how they interact
- They track: Time spent (manual log)

**Step 4: Validate (Day 6-7)**
- 15-min call with each customer
- Questions:
  - "How much time did you spend?" (vs normal)
  - "Would you use this regularly?"
  - "What was missing?"
  - "Would you pay for this?"
- Survey (5 min): Likert scale on ease, usefulness, adoption

### Cost Breakdown
- Time to create template: 3 hours (PM)
- Time to manage experiment: 4 hours (calls, survey)
- Cost to customers: 5 hours each (their feedback)
- **Total cost: ~12 PM hours**

### Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Only 2 customers respond | Medium | Critical | Have backup list ready |
| Template is hard to use | Medium | High | Do internal test first |
| Customers forget to use it | Medium | High | Send reminder emails |
| Results are ambiguous | Low | Medium | Pre-define success criteria |

### What We'll Learn
- ✓ Do customers actually want this?
- ✓ Does the concept solve the problem?
- ✓ What's missing?
- ? Will they pay for it? (answered in next test)

### Next Decision Point
**If successful:** Move to Option B (deeper prototype)  
**If unsuccessful:** Kill opportunity or pivot
```

### Example: FAIL

```markdown
# Experiment: Test Prioritization Tool

Build a prioritization tool and give it to some customers.
See if they like it.
Success = they use it.

Timeline: 3 weeks
Sample: "A few customers"
Cost: Unknown
```

**Why it fails:**
- ❌ No clear hypothesis link
- ❌ Sample size not justified
- ❌ Success criteria too vague
- ❌ Budget not defined
- ❌ Risks not identified

---

## Decision Artifact

**Used by:** Decision Evaluator  
**Purpose:** Record a major decision (build/kill/test)  
**File:** `decisions/D-###.md`

### Quality Rubric

| Criterion | Poor (0) | Fair (1) | Good (2) | Excellent (3) |
|-----------|----------|----------|----------|---------------|
| **Clear Decision** | Vague | Somewhat clear | Clear (BUILD/KILL/TEST) | Specific with rationale |
| **Evidence Reviewed** | Not mentioned | Some evidence | Most evidence reviewed | All relevant evidence cited |
| **Assumptions Validated** | Not addressed | Some addressed | Most addressed | All key assumptions reviewed |
| **Experiment Results** | Not mentioned | Mentioned vaguely | Clear results | Specific numbers/data |
| **Alternative Considered** | No alternatives | 1 alternative | 2+ alternatives | 3+ alternatives with pros/cons |
| **Timeline Realistic** | Unrealistic | Somewhat realistic | Realistic | Detailed with dependencies |
| **Escalation Path Clear** | Not mentioned | Vague | Clear | Specific person + process |

### Passing Score
**14/21 points minimum**

### Example: PASS

```markdown
# Decision D-001: BUILD Smart Prioritization Tool

## The Decision
**DECISION: BUILD** the Smart Prioritization tool (feature version 1)

## Evidence Summary

### Evidence Supporting BUILD
- **Opportunity O-001:** 9/12 customers struggle with prioritization (75%)
- **Hypothesis H-001:** Validated via experiment E-001
  - 4/5 customers reported time savings (80% reduction)
  - 5/5 said "would use this"
- **Problem:** Quantified (4 hrs/week → 48 min/week predicted)
- **Market:** No clear competitor solving this for SMB

### Assumptions Validated
- ✓ A-1: Problem is lack of structure (confirmed in testing)
- ✓ A-2: Customers would adopt new tool (5/5 would use)
- ✗ A-3: Would reduce time by 80% (only 60% in test)
  - Adjusted: Realistic target = 60% time reduction

### Alternatives Considered

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| **A: BUILD** | Direct problem solution, customers want it, no competitor | Takes 8 weeks, resource intensive | ✓ CHOSEN |
| **B: PARTNER** | Faster, lower resource | Less aligned with customers, takes 6 weeks to negotiate | Rejected |
| **C: TEMPLATE** | Fast, low cost | Not robust long-term | Tried in E-001, insufficient |
| **D: WAIT** | More learning possible | Customers keep suffering, competitors might move | Rejected |

## Timeline & Dependencies

**Preconditions Met:**
- ✓ Problem validated
- ✓ Solution concept tested
- ✓ Engineering feasibility confirmed
- ✓ Budget approved ($80K for dev)

**Implementation:**
- Weeks 1-2: Design & spec (ES-001)
- Weeks 3-6: Build (MVP)
- Week 7: Beta testing
- Week 8: Launch to all

**Dependencies:**
- Engineering capacity available (confirmed)
- Jira integration available (confirmed)
- Customer beta testing (TBD)

## Success Metrics

We'll know this is successful when:
- ✓ 50% of users adopt feature in month 1
- ✓ Time spent decreases by >40%
- ✓ Feature gets NPS >7
- ✓ Monthly churn decreases by >2%

## Risk Assessment

| Risk | Mitigation |
|------|-----------|
| Adoption slower than expected | Include onboarding walkthrough |
| Engineering takes 3x longer | Use MVP scope + phased rollout |
| Customers want different solution | Built-in feedback loop during beta |

## Escalation Path

**If things change:**
- Market shifts: Escalate to CEO + product leadership
- Engineering blockers: Escalate to CTO + product manager
- Customer feedback contradicts hypothesis: Investigate immediately
- Churn increases instead of decreases: Halt and investigate

**Escalation point:** Weekly sync every Monday until launch

## Next Steps

1. Hand off to engineering (see ES-001)
2. Identify beta customers (5-10)
3. Plan launch communication
4. Setup success metrics dashboard
5. Establish measurement schedule
```

### Example: FAIL

```markdown
# Decision: Build Prioritization Tool

We think customers want a prioritization tool so let's build it.
This will help them prioritize better.
Timeline: 2 months
Cost: TBD
```

**Why it fails:**
- ❌ No evidence cited
- ❌ Alternatives not considered
- ❌ Assumptions not validated
- ❌ Success metrics not defined

---

## Product Spec Artifact

**Used by:** Product Spec Writer  
**Purpose:** Detailed product specification  
**File:** `specs/PS-###.md`

### Quality Rubric

| Criterion | Poor (0) | Fair (1) | Good (2) | Excellent (3) |
|-----------|----------|----------|----------|---------------|
| **Problem Clear** | Vague | Somewhat clear | Clear | Specific + evidence-backed |
| **Value Prop** | Missing | Vague | Clear | Specific benefits for each segment |
| **Requirements Complete** | Incomplete | Some gaps | Most defined | Comprehensive with priorities |
| **Acceptance Criteria** | Vague | Somewhat specific | Specific | Very specific, testable |
| **Scope Bounded** | Unclear | Somewhat clear | Clear (in/out) | Very clear with rationale |
| **Design Considered** | Not addressed | Vague sketches | Some consideration | Detailed with wireframes |
| **Success Metrics** | None | Vague | Defined | Specific with targets |

### Passing Score
**14/21 points minimum**

### Example: PASS

```markdown
# Product Spec PS-001: Smart Prioritization Tool

## Problem
Customers spend 2-4 hours/week manually prioritizing features because they lack a tool that weights customer requests against business value (9/12 customers, O-001).

## Value Proposition

**For Product Managers:**
- Spend 80% less time prioritizing (4 hrs → 48 min/week)
- Make prioritization decisions with confidence (based on data, not gut)
- Align team on priorities transparently

**For Companies:**
- Ship features customers actually want (reduce waste)
- Improve prioritization quality
- Increase PM productivity

## User Story

**As a** product manager  
**I want to** input my prioritization criteria and have features automatically ranked  
**So that** I can make prioritization decisions in 30 minutes instead of 4 hours

## Core Features (MVP)

### Feature 1: Criteria Input
- User can add 5+ custom criteria (Customer Requests, Business Value, Effort, Risk, etc.)
- Each criterion has a weight (1-10 scale)
- Save criteria sets for reuse
- **Acceptance Criteria:**
  - [ ] Can add/edit/delete criteria
  - [ ] Weights persist across sessions
  - [ ] Can save criteria template
  - [ ] Clear UI with <2 min onboarding

### Feature 2: Feature Ranking
- User uploads/imports list of features (from Jira, CSV, or manual)
- System ranks features based on criteria
- User can manually adjust weights and see rankings update
- **Acceptance Criteria:**
  - [ ] Results show in <1 second
  - [ ] Ranking updates in real-time with weight changes
  - [ ] Shows reasoning (why #1 ranked higher than #2)
  - [ ] Can pin/reorder manually

### Feature 3: Export
- Export prioritized list as CSV, PDF, or back to Jira
- Share prioritization with team
- **Acceptance Criteria:**
  - [ ] Export works in <5 seconds
  - [ ] Format is clean and usable
  - [ ] Jira sync updates task priorities

## Out of Scope (Version 1)
- AI-generated criteria suggestions
- Sharing between teams
- Real-time collaboration
- Mobile app

## Technical Requirements
- Performance: Load criteria in <500ms, rank features in <1s
- Scale: 1000 concurrent users
- Uptime: 99.9%
- Integrations: Jira, CSV import

## Success Metrics

**Adoption:**
- 50% of active users adopt feature in month 1
- 70% by month 3

**Engagement:**
- Weekly active users: >60%
- Average session time: >15 minutes

**Impact:**
- Time spent on prioritization: <1 hour/week (vs 4 current)
- Feature NPS: >7
- Churn reduction: >2%

## Timeline
- Design: 1 week
- Build: 3 weeks
- Testing: 1 week
- Launch: 1 week

**Go-live date:** [8 weeks from now]
```

---

## Using the Rubrics

### Agent Self-Evaluation
Agent creates artifact and runs through rubric:
```
"I created this opportunity. Let me self-evaluate:
- Evidence sourcing: Good (2/3)
- Specificity: Excellent (3/3)
- Contradictions: Fair (1/3)
- No speculation: Good (2/3)
- Frequency counts: Good (2/3)
- Signal strength: Excellent (3/3)
- Missing data: Fair (1/3)

Total: 17/21 points - PASSES
Ready to show PM."
```

### PM Decision Checklist
PM reviews artifact against rubric:
```
Is this opportunity good?
✓ Evidence is sourced and specific
✓ Assumptions are listed
✓ Not a hidden solution
✓ Testable hypotheses

→ APPROVE
```

If scores are low:
```
Missing: Frequency counts, contradiction analysis
Ask agent: "How many customers mentioned this? Any contradictions?"
```

---

## Minimum Viable Quality

Each artifact must score at least:
- **12 points** for Synthesis
- **14 points** for Opportunity
- **14 points** for Hypothesis
- **14 points** for Experiment
- **14 points** for Decision
- **14 points** for Spec

Below minimum = Send back to agent with feedback.
