# Evidence Schema & Quality Standards

The agent reads evidence to extract insights. For the agent to work well, evidence must be:
1. **Structured** - Consistent format
2. **Sourced** - Clearly attributed
3. **Fresh** - Recent enough to be relevant
4. **Credible** - From reliable sources

This schema ensures quality evidence that leads to quality insights.

---

## Evidence Quality Checklist

Before agent reads evidence, it must pass:

- [ ] **Complete:** All required fields filled (see templates below)
- [ ] **Sourced:** Every claim can be traced to original source
- [ ] **Dated:** When was this collected? (Recent is better)
- [ ] **Specific:** Includes quotes, numbers, details (not summaries)
- [ ] **Credible:** From identified person/source (not anonymous)
- [ ] **Fresh:** Not older than 6 months (or marked as "archive")
- [ ] **Labeled:** Clear category (interview, support, analytics, etc.)

**Fail 2+ checks?** → Ask PM to provide better evidence

---

## 1. Customer Interview Evidence

**File:** `evidence/interviews/[Name]_[Date].md`

### Template

```markdown
# Interview: [Customer Name]

**Date:** YYYY-MM-DD  
**Duration:** [X minutes]  
**Interviewer:** [Your name]  
**Role:** [Customer's job title]  
**Company:** [Company name]  
**Company Size:** [1-50 / 50-500 / 500+]  
**Product/Service:** [What do they make/do?]

---

## Key Quotes

> "[Direct quote from interview]"  
> *Context: [Why they said this, what prompted it]*

> "[Another quote]"  
> *Context: [Context]*

---

## Pain Points Identified

### Pain Point 1: [Specific name]

**Customer quote:** "[Direct quote expressing this pain]"

**Intensity:** Casual / Frustrated / Critical  
**Frequency:** "How often does this happen?" - [Their answer]  
**Workaround:** "[What do they do instead?]"  
**Impact:** "[How does it affect their work?]"

### Pain Point 2: [Specific name]

[Same format]

---

## Feature Requests

### Request 1: [What they asked for]

**Customer quote:** "[What they said exactly]"

**Underlying need:** "[What do they actually need vs what they asked for?]"

**Current solution:** "[How do they solve this now?]"

---

## Surprising Insights

[Anything unexpected or counter-intuitive that came up]

---

## Product Usage

**How they currently use our product:**
- [Feature 1]: [How they use it]
- [Feature 2]: [How they use it]

**What they don't use:**
- [Feature]: [Why not?]

**Integration with other tools:**
- [Tool 1]: [How they use it alongside our product]

---

## Segment Information

**Maturity:** Startup / Growth / Mature  
**Team structure:** [Org size and relevant roles]  
**Budget constraints:** [If mentioned - budget level, process]  
**Timeline:** [If they mentioned a project timeline]

---

## Interview Quality

**Rapport:** Good / Neutral / Tense  
**Candor level:** HIGH / MEDIUM / LOW  
**[Why low?]:** [If they seemed guarded, what might they not have said?]  

**Overall reliability:** HIGH / MEDIUM / LOW  
[Why not HIGH?]

---

## Next Steps

**Follow-up needed:** Yes / No  
**If yes:** [What to ask next time?]

---

## Notes for Agent

[Anything that might help the agent interpret this?]
- [Note 1]
- [Note 2]
```

### Quality Scoring

| Criterion | Poor (0) | Fair (1) | Good (2) |
|-----------|----------|----------|----------|
| **Sourcing** | No name/date | Name only, no date | Name + date + role |
| **Specificity** | Summary only | Some quotes | Direct quotes + context |
| **Freshness** | >1 year old | 6-12 months | <6 months |
| **Depth** | <10 min interview | 15-20 min | 30+ minutes |
| **Credibility** | Anonymous | Known person | Known + verified |

**Passing score: 6+ points**

---

## 2. Support Tickets Evidence

**File:** `evidence/support_tickets/[Month]_[Year].md`

### Template

```markdown
# Support Tickets - [MONTH YEAR]

**Date range:** [First to last ticket]  
**Total tickets:** [Number]  
**Reviewed by:** [Person]  
**Data age:** [How fresh is this?]

---

## Tickets by Category

### Category: [Name]
**Frequency:** [X tickets this month]  
**Trend:** Increasing / Stable / Decreasing

#### Ticket #1
**Issue:** [One sentence summary]  
**Customer quote:** "[If quoted in ticket]"  
**Impact:** HIGH / MEDIUM / LOW  
**Root cause:** [What's really wrong?]  
**Status:** [Resolved / Pending / Duplicate]  
**Date:** [When submitted]

#### Ticket #2
[Same format]

---

## Patterns Across All Tickets

### Pattern 1: [Description]

**Frequency:** [# of tickets in this category]  
**Examples:** [Ticket #X, #Y, #Z]  
**Trend:** Increasing / Stable / Decreasing  
**Impact:** [What problems does this cause?]

---

## Most Urgent Issues

1. [Issue 1] - [X tickets] - Trend: [Increasing]
2. [Issue 2] - [X tickets] - Trend: [Stable]
3. [Issue 3] - [X tickets] - Trend: [Decreasing]

---

## Data Quality

**Completeness:** HIGH / MEDIUM / LOW  
[How many tickets have full description vs just title?]

**Accuracy:** [Are these bugs or user error?]

**Representativeness:** [Do these tickets represent all customer issues, or just support channel issues?]

---

## Notes for Agent

[Anything that changes how to interpret this data?]
```

### Quality Scoring

| Criterion | Poor (0) | Fair (1) | Good (2) |
|-----------|----------|----------|----------|
| **Categorization** | No categories | Some grouping | Clear categories |
| **Frequency data** | No counts | Mentioned vaguely | Specific numbers |
| **Sourcing** | No dates | Vague timeline | Specific dates |
| **Root cause** | User error vs bug unclear | Mostly clear | Clear classification |
| **Trends** | Not noted | Mentioned | Tracked (increasing/stable/decreasing) |

**Passing score: 6+ points**

---

## 3. Analytics/Data Evidence

**File:** `evidence/analytics/[Source]_[Month]_[Year].md`

### Template

```markdown
# Analytics Data: [SOURCE - e.g., Google Analytics, Product Usage]

**Period:** [Date range]  
**Source:** [Tool or system data came from]  
**Collected by:** [Person who exported/compiled]  
**Data age:** [How fresh?]

---

## Key Metrics

### Metric 1: [Name]

**Current value:** [X]  
**Previous period:** [X] - Trend: [↑ / ↓ / →]  
**Target:** [Y]  
**Analysis:** [What does this number mean?]

### Metric 2: [Name]

[Same format]

---

## User Segments

### Segment: [Description]

| Metric | Value | Trend |
|--------|-------|-------|
| Users | X | ↑ |
| [Metric] | X | ↓ |
| [Metric] | X | → |

---

## Cohort Analysis

**Cohort: [How grouped - e.g., by signup date, plan type]**

| Metric | New Users | 1-3 Mo Old | 3-6 Mo Old | 6+ Mo Old |
|--------|-----------|-----------|-----------|-----------|
| Retention | X% | X% | X% | X% |
| Usage | X | X | X | X |
| Churn | X% | X% | X% | X% |

**Insight:** [What pattern do you see?]

---

## Feature Adoption

### Feature: [Name]

**Adoption rate:** [X% of users]  
**Active daily:** [X% of active users]  
**Trend:** Increasing / Plateau / Declining  
**Segment analysis:** 
- [Segment 1]: X% adoption
- [Segment 2]: X% adoption

### Feature: [Name]

[Same format]

---

## Churn Analysis

**Monthly churn rate:** [X%]  
**Churn cohort:** [Which users are leaving?]

**Users who churn typically:**
- [Characteristic 1]
- [Characteristic 2]
- [Feature usage pattern: X]

**Correlation:** [Do churning users show any common pattern?]

---

## Data Quality Assessment

**Completeness:** [What data is missing?]  
**Accuracy:** [How confident are you in these numbers?]  
**Recency:** [Is this current?]  
**Sampling:** [Is this all users or a sample?]

---

## Notes for Agent

[Anything that affects interpretation?]
- [Note 1]
- [Note 2]
```

### Quality Scoring

| Criterion | Poor (0) | Fair (1) | Good (2) |
|-----------|----------|----------|----------|
| **Metrics clear** | Vague definitions | Some definition | Very specific |
| **Data sourcing** | Unknown source | Source mentioned | Source + methodology |
| **Freshness** | Older than 3 months | 1-3 months old | Current/recent |
| **Context** | Numbers without context | Some interpretation | Full analysis |
| **Completeness** | Very incomplete | Some gaps | Complete dataset |

**Passing score: 6+ points**

---

## 4. Market Research Evidence

**File:** `evidence/market_research/[Topic]_[Date].md`

### Template

```markdown
# Market Research: [TOPIC]

**Date:** YYYY-MM-DD  
**Researcher:** [Person]  
**Sources:** [Where did you find this?]  
**Confidence:** HIGH / MEDIUM / LOW

---

## Competitive Landscape

### Competitor 1: [Name]

**Product:** [What do they do?]  
**Target:** [Who do they serve?]  
**Pricing:** [How much?]  
**Key features:** [What's unique?]  
**Positioning:** [How do they describe themselves?]  
**Strengths:** [What are they good at?]  
**Weaknesses:** [What are they missing?]

### Competitor 2: [Name]

[Same format]

---

## Market Sizing

**Total Addressable Market (TAM):** [$ estimate or # of potential customers]  
**Serviceable Market (SAM):** [Our addressable subset]  
**Serviceable Obtainable Market (SOM):** [What we could realistically get]

**Data sources:** [Where did you get these numbers?]  
**Confidence:** [HIGH / MEDIUM / LOW - why?]

---

## Market Trends

### Trend 1: [Description]

**Evidence:** [Source]  
**Implication:** [Why this matters]  
**Relevance:** [How does this affect our opportunity?]

---

## Customer Willingness to Pay

**Research method:** [How did you determine this?]  
**Price sensitivity:** 
- [Segment 1]: Would pay $X/month
- [Segment 2]: Would pay $X/month

**Justification:** [Why these prices?]

---

## Sources & Attribution

- [Source 1]: [Link or reference]
- [Source 2]: [Link or reference]
- [Source 3]: [Link or reference]

---

## Notes for Agent

[Anything affecting interpretation?]
```

### Quality Scoring

| Criterion | Poor (0) | Fair (1) | Good (2) |
|-----------|----------|----------|----------|
| **Source attribution** | No sources | Some sources | All sources cited |
| **Freshness** | Older than 1 year | 6-12 months | Recent |
| **Methodology clear** | Unknown how gathered | Vague | Clear methodology |
| **Confidence stated** | Not mentioned | Vague | Explicitly stated |
| **Multiple sources** | Single source | 2-3 sources | 5+ sources |

**Passing score: 6+ points**

---

## Agent's Evidence Validation Process

### Step 1: Check Quality Score

For each evidence file:
- Run through quality rubric (see above)
- If score < 6/10: Flag as "Lower quality evidence"

### Step 2: Flag Age

- If >6 months old: Flag as "Archive - May be stale"
- If >12 months old: Flag as "Very old - Validate elsewhere"

### Step 3: Note Sourcing

For each claim in synthesis:
```
[Claim] (X/Y sources)
- Source 1: [Who/what]
- Source 2: [Who/what]
- Source 3: [Who/what]
```

### Step 4: Ask PM if Missing

If agent notices:
- No data on [topic]
- Data older than 6 months
- Only 1-2 sources on key claim
- Contradictions between sources

**Agent asks:** "Should I wait for better data or proceed with what we have?"

---

## Evidence Organization

```
evidence/
├── interviews/
│   ├── Sarah_Chen_2025-01-20.md
│   ├── Alex_Patel_2025-01-18.md
│   └── Jordan_2025-01-15.md
│
├── support_tickets/
│   ├── January_2025.md
│   ├── December_2024.md
│   └── November_2024.md
│
├── analytics/
│   ├── Google_Analytics_January_2025.md
│   ├── Product_Usage_January_2025.md
│   └── Churn_Analysis_January_2025.md
│
├── market_research/
│   ├── Competitive_Analysis_Jan_2025.md
│   ├── TAM_Analysis_2024.md
│   └── Pricing_Research_Jan_2025.md
│
└── README.md
    # Evidence Inventory
    - 15 interviews (Jan 2025, fresh)
    - Support tickets (Jan 2025, fresh)
    - Product analytics (Jan 2025, current)
    - Market research (Dec 2024, 1 month old)
    - Competitor data (Dec 2024, 1 month old)
```

---

## Evidence Intake Process

When adding new evidence:

1. **Choose right category** (interview / support / analytics / market)
2. **Use template** (copy from templates above)
3. **Fill all required fields** (sourcing, dating, specificity)
4. **Self-assess quality** (use rubric above)
5. **Add to evidence/README.md** (keep inventory)
6. **Tag with date** (filename includes date)

Once added → Agent can read it immediately

---

## Regular Evidence Refresh

**Monthly:**
- Add new interviews (at least 5)
- Update support ticket analysis
- Export analytics updates

**Quarterly:**
- Refresh market research
- Update competitive analysis
- Review evidence age (archive stale data)

**Annually:**
- Deep market sizing
- Complete competitive refresh
- Strategic trend review

**Agent alerts if:**
- No evidence added in 30 days
- All evidence is >6 months old
- Only 1-2 sources on key claim
