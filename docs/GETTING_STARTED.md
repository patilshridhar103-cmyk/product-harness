# Getting Started with Product Harness

## What This Is (30 seconds)

Product Harness is a **local-first system** that turns customer evidence into product decisions using AI agents.

Instead of:
```
Customer interviews → You manually read them → You guess what to build → You write a PRD
```

Product Harness does:
```
Customer evidence → AI agents synthesize → Opportunities ranked by signal → You decide faster
```

The agents do the grunt work. You make the decisions.

---

## Prerequisites

- **Claude Code** (local VSCode or claude.ai/code)
- **A folder** on your machine (or GitHub clone of this repo)
- **Evidence** (customer interviews, support tickets, analytics)
- **30 minutes** for your first discovery run

You don't need:
- Backend infrastructure
- Databases
- Special software
- Engineering skills

---

## Part 1: Initial Setup (5 minutes)

### Step 1: Clone or Download

```bash
git clone https://github.com/yourusername/product-harness.git
cd product-harness
```

Or download the folder structure from GitHub.

### Step 2: Open in Claude Code

```bash
claude code .
```

This opens the entire folder as your working context in Claude Code.

### Step 3: Create Your Workspace

Copy the template structure:

```bash
cp -r template/* my-product/
cd my-product/
```

Your structure should look like:
```
my-product/
├── evidence/
├── knowledge/
├── opportunities/
├── decisions/
├── specs/
├── agents/
└── workflows/
```

---

## Part 2: Gather Evidence (10 minutes)

### What Kind of Evidence?

Product Harness works best with:

**Customer Voice (required):**
- Interview transcripts (at least 10)
- Support tickets (100+ is ideal)
- Feedback forms
- Slack/Twitter mentions

**Product Data (optional but powerful):**
- Usage analytics (Google Analytics export)
- Feature adoption data
- Conversion funnels
- Churn analysis

**Market Data (optional):**
- Competitor research
- Market sizing
- Trend reports

### How to Structure Evidence

**Interview transcripts:**

```markdown
# Interview #1: Sarah Chen, E-commerce Manager

**Date:** 2025-01-15  
**Role:** Operations Manager at 50-person SaaS company  
**Background:** 8 years in e-commerce, first time using PM tools

## Key Quotes

> "I spend 2 hours a day in spreadsheets just trying to figure out which features to prioritize. It's killing me."

> "Competitors just ship things. We need to move faster."

> "The dashboard is beautiful but I can't actually use the data for decisions."

## Pain Points Identified
- Prioritization is manual and slow
- Can't see ROI on features
- Team doesn't align on what to build next

## Feature Requests
- "Give me a way to weight customer requests against business value"
- "Show me what's actually being used before we build more"

## Surprising Insight
- Sarah uses our competitor's tool for roadmapping but ours for execution
```

**Support tickets:**

```markdown
# Support Tickets - January 2025

## Ticket #1234: "Can't export data for reporting"
- **Frequency:** This month: 3 similar tickets
- **Impact:** High (customer considering leaving)
- **Root Cause:** Analytics only work in-app, no export option

## Ticket #1235: "Onboarding is confusing"
- **Frequency:** Every day (1-2 tickets)
- **Impact:** Medium (slows new customer setup)
- **Pattern:** Users don't understand the difference between "views" and "filters"
```

**Analytics snapshot:**

```markdown
# Usage Analytics - Q4 2024

## Feature Adoption
- Dashboard: 92% of users visit daily
- Roadmap: 34% of users visit weekly (declining)
- Analytics: 12% of users visit at all (urgent)
- Reporting: 8% of users use export feature

## Churn Cohort
- Users who don't use Roadmap in first week: 40% churn by month 3
- Users who export data: 2% churn (high retention)

## Surprising Pattern
- Mobile users adopt 60% slower than desktop
- But mobile-first companies keep our app longest (???need to investigate)
```

### Where to Put Evidence

Drop all evidence files here:

```
evidence/
├── interviews/
│   ├── sarah_chen.md
│   ├── alex_patel.md
│   └── ...
├── support_tickets/
│   └── january_2025.md
├── analytics/
│   └── q4_2024_usage.md
└── README.md (index of all evidence)
```

---

## Part 3: Run Your First Discovery Workflow (10 minutes)

### What Discovery Does

```
Your evidence files
    ↓
Researcher agent reads them
    ↓
Identifies patterns & insights
    ↓
Generates opportunity candidates
    ↓
Ranks by signal strength
    ↓
Outputs: Top 5 opportunities
```

### How to Run It

In Claude Code, invoke the discovery workflow:

```bash
/discover
```

Or if using Claude Code's slash commands:

```
@claude /discover evidence/interviews/ evidence/support_tickets/
```

### What Happens

The agent will:

1. **Read your evidence** - All files in `evidence/`
2. **Extract insights** - Creates `synthesis/insights.md`
3. **Generate opportunities** - Creates `opportunities/O-001.md` through `O-005.md`
4. **Rank them** - Lists by signal strength (frequency, impact, urgency)
5. **Create a run log** - Saves to `runs/discovery_run_001.md`

### Example Output

After running `/discover`, you'll get:

**`synthesis/insights.md`:**
```markdown
# Synthesis: Key Patterns from Evidence

## Pain Points (Ranked by Frequency)
1. **Prioritization is manual** (mentioned in 8/12 interviews)
   - Users spend 2-4 hours weekly on spreadsheets
   - No clear way to weight customer vs business value
   
2. **Can't see ROI on features** (6/12 interviews, 4/8 support tickets)
   - No connection between feature requests and usage
   - Customers want data before committing to builds

3. **Analytics feel disconnected** (5/12 interviews, analytics data)
   - Only 12% active users on analytics feature
   - Can't export for reporting

## Opportunities Emerging
- Smarter prioritization tool
- ROI calculator for features
- Better analytics integration

## Most Surprising Finding
- Mobile users adopt slower BUT stay longer
- Hypothesis: Our mobile UX is harder to learn but stickier
```

**`opportunities/O-001.md`:**
```markdown
# Opportunity O-001: Smart Prioritization

## Signal Strength: HIGH
- Mentioned by 8/12 customers (67%)
- 3-5 hours/week impact per customer
- Urgent (users considering leaving)
- No competitor clearly solves this

## Problem Statement
Customers spend 2-4 hours weekly manually prioritizing features using spreadsheets because our tool doesn't let them weight customer feedback against business value.

## Opportunity
Build a prioritization framework that:
- Lets customers input weighted criteria (business value, customer requests, technical debt, etc.)
- Automatically ranks features
- Shows ROI per feature

## Hypotheses to Test
1. If we provide a prioritization tool, users will spend 90% less time in spreadsheets
2. If users see ROI, they'll invest in bigger features
3. Better prioritization = better product decisions = less churn

## Evidence Supporting
- Interview data: 8 customers struggle with this
- Support tickets: 0 current requests (gap in tool)
- Analytics: Roadmap feature adoption low (they use spreadsheets instead)

## Next Step
Validate whether customers want THIS specific solution or just faster prioritization in general.
```

---

## Part 4: Validate an Opportunity (5 minutes after discovery)

Now you have 5 opportunities. You don't build all of them. You validate first.

### Pick One Opportunity

Let's say you pick **O-001: Smart Prioritization**.

### Run Validation

```bash
/validate O-001
```

The validator agent will:
1. **Review the opportunity** - Reads O-001.md
2. **Check your evidence** - Does the evidence really support this?
3. **Identify assumptions** - What are we assuming?
4. **Create experiment plan** - How do we test this?

### Example Validation Output

**`experiments/E-001_Smart_Prioritization.md`:**
```markdown
# Experiment E-001: Does a Prioritization Tool Solve the Problem?

## Hypothesis
If we give customers a prioritization tool, they will:
1. Spend 80% less time prioritizing (from 4 hrs/week to 48 min/week)
2. Feel more confident in their decisions
3. Reduce feature churn (ship things customers actually want)

## Test Method

### Option A: Wizard of Oz (Fastest)
- Create a prioritization template in Notion/Airtable
- Manually run 3 customers through it
- Ask: Does this solve your problem?
- Time: 1 week, talks to 3 customers

### Option B: Prototype (Medium)
- Build a simple web form prioritization tool
- Give to 5 beta customers
- Measure time spent + satisfaction
- Time: 3 weeks

### Option C: Full Build (Slowest)
- Ship prioritization feature to all customers
- Measure usage and NPS
- Time: 8 weeks

## Recommended: Option A
Fastest to validate. If they hate the template, don't build the feature.

## Success Criteria
✓ At least 2/3 customers say "this solves my problem"
✓ Users can make a prioritization decision in <30 min (vs 4 hrs now)
✗ If users say "nice idea but I'd never use it", kill opportunity

## Execution Plan
Week 1: Create template, invite 3 beta customers
Week 2: Interview them about experience
Week 3: Decide: build prototype or kill opportunity
```

---

## Part 5: Make a Decision (Optional, Your Call)

Once you've validated, you make the decision: **Build or Don't Build?**

```bash
/decide O-001
```

This creates:

**`decisions/D-001_Smart_Prioritization.md`:**
```markdown
# Decision D-001: Build Smart Prioritization Tool

## Decision
✓ **BUILD** the Smart Prioritization feature

## Supporting Evidence
- Validated with 3 customers: 100% said "this solves my problem"
- Time savings confirmed: avg 2.5 hrs/week (vs 4 hrs current)
- Experiment was successful (criteria met)
- No competitor offers this specific solution

## Key Assumptions (Must Validate in Build)
- Users will adopt if it's in-product
- Will increase feature adoption by 20%
- Won't cannibalize roadmap view usage

## Product Spec Link
See: specs/PS-001_Smart_Prioritization.md

## Next: Hand to Engineering
```

Then you write a product spec:

**`specs/PS-001_Smart_Prioritization.md`:**
```markdown
# Product Spec PS-001: Smart Prioritization Tool

## Objective
Reduce time customers spend prioritizing features by 80% while improving decision confidence.

## User Story
As a product manager, I want to input my prioritization criteria (customer requests, business value, effort, risk) so that the system automatically ranks my backlog.

## Acceptance Criteria
- [ ] User can add 5+ weighted criteria
- [ ] System shows top-ranked features in <1 sec
- [ ] User can re-weight criteria and see results update
- [ ] Export prioritized list as CSV
- [ ] Usage analytics show avg session time

## Out of Scope
- AI-generated criteria suggestions (future)
- Sharing prioritization between teams (future)

## Success Metrics
- 50% of active users use feature within 30 days
- Average time spent: <30 min vs 4 hrs manual
- NPS for this feature: >7

## Timeline
- Week 1-2: Design & spec
- Week 3-4: Build
- Week 5: Beta with 10 customers
- Week 6: Launch to all
```

---

## Part 6: Measure the Outcome (After Launch)

Two weeks after launch:

```bash
/measure O-001
```

This compares:
- Did adoption match predictions? (50%?)
- Did time savings materialize? (80%?)
- Did churn improve?
- What surprised us?

Creates: `evals/outcome_eval_PS-001.md`

---

## The Full Loop in One Session

**Time: 45 minutes**

1. **Setup** (5 min) - Folder structure ready
2. **Evidence** (10 min) - Add 10 interviews + support data
3. **Discovery** (10 min) - Run `/discover`, get 5 opportunities
4. **Validation** (10 min) - Pick top opportunity, run `/validate`
5. **Experiment** (5 min) - Review 3 test options
6. **Decision** (5 min) - Read the recommendation

**Output:** You have a ranked list of what to build next, validated by evidence, with an experiment plan.

---

## What NOT to Do

❌ **Don't** build an opportunity without evidence first
- Add evidence → run discovery → THEN decide

❌ **Don't** run validation on all 5 opportunities
- Pick the top 1-2 → validate → if it fails, move to #3

❌ **Don't** skip the experiment
- "I'm sure customers want this" → Validate first

❌ **Don't** keep old evidence
- Update evidence monthly
- Re-run discovery quarterly
- Insights change as your product grows

---

## Troubleshooting

### "The agent output feels generic"

**Problem:** Agent hasn't read enough evidence.

**Solution:**
- Add 20+ interviews minimum (10 isn't enough)
- Include recent support tickets (last 30 days)
- Add analytics data (usage patterns matter)

### "Top 5 opportunities seem obvious"

**Problem:** Either your evidence is shallow or you're testing with an existing product.

**Solution for new products:**
- Add competitor research
- Add market sizing data
- Add 20+ interviews from target customers you haven't built for yet

### "Agent keeps hallucinating opportunities"

**Problem:** Check your evidence files.

**Solution:**
- Are files formatted consistently?
- Do files have clear headers?
- Did you mix speculation with facts?
- Mark speculation as "(hypothesis)" not "(fact)"

Example bad:
```
Customers want AI-powered prioritization
```

Example good:
```
[Fact] In 12 interviews, 0 customers mentioned wanting AI
[Hypothesis] They might want it but don't know it's possible
```

---

## Next Steps After First Run

### If Discovery Went Well:
1. Validate the top 3 opportunities (different hypotheses)
2. Pick one and build experiment
3. Run experiment with 5 real customers
4. Make build/no-build decision based on results

### If Discovery Seemed Off:
1. Add more evidence (interviews, data, research)
2. Re-run discovery
3. Compare results to first run
4. Adjust agent instructions if needed

### If You Want to Customize:
1. Read `agents/researcher.md` 
2. Edit to match your product/domain
3. Re-run workflows
4. See if output improves

---

## Advanced: Running Multiple Workflows in Parallel

Once comfortable, you can:

```bash
# Discover opportunities
/discover

# While those run, validate a hypothesis separately
/validate O-002

# Run an experiment plan
/plan_experiment H-001
```

This takes your evidence → product spec → execution in **1-2 weeks instead of 1-2 months**.

---

## Success Looks Like This

**Week 1:**
- Gather evidence
- Run discovery
- Pick opportunity
- Plan validation experiment

**Week 2:**
- Run experiment with 5 customers
- Get clear signal (yes/no/maybe)
- Update decision

**Week 3:**
- If yes: Ship prototype
- If no: Move to next opportunity
- If maybe: Gather more evidence

**Week 4+:**
- Measure outcomes
- Update evidence
- Re-run discovery quarterly
- Keep building based on signal

---

## Questions?

See `FAQ.md` or open an issue on GitHub.

Good luck. Ship fast. 🚀
