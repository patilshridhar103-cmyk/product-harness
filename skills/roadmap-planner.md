# Roadmap Planner Skill

## Role
Turn decisions into execution sequence. Prioritize features using frameworks and create realistic product roadmaps.

## When to Use
- After multiple opportunities are validated
- To sequence features across quarters
- To balance customer needs vs business goals
- To create roadmap presentations

## Input
- Multiple validated opportunities (O-###)
- Business strategy and goals
- Resource capacity
- Customer priorities

## Process

### Step 1: Apply Prioritization Framework

Choose framework based on decision type:
- **RICE:** Reach × Impact ÷ Confidence ÷ Effort (best for many features)
- **Kano:** Basic vs Performance vs Delighter (best for satisfaction)
- **MoSCoW:** Must/Should/Could/Won't (best for time-boxed releases)
- **Lean Matrix:** Importance vs Urgency (best for strategic focus)

### Step 2: Score Each Feature

For RICE example:
- **Reach:** How many users affected? (0-100)
- **Impact:** How much benefit? (3=massive, 2=high, 1=medium, 0.5=small)
- **Confidence:** How sure? (0-100%)
- **Effort:** How many weeks? (1-20)
- **Score = (R × I × C) ÷ E**

### Step 3: Sequence into Roadmap

- **Q1 (Now-3mo):** Top priorities with dependencies
- **Q2 (3-6mo):** Secondary priorities
- **Q3-Q4:** Exploratory/strategic bets

### Step 4: Create Dependencies

Map:
- What blocks what?
- What requires infrastructure?
- What needs customer success setup?

### Step 5: Communicate Roadmap

Show:
- Top 3 priorities for next quarter
- Why (business rationale)
- Expected launch dates
- Customer impact

## Output: `roadmap/[quarter]_roadmap.md`

```markdown
# Q[X] Roadmap

## Prioritization Results (RICE Score)

| Feature | Reach | Impact | Confidence | Effort | RICE Score | Rank |
|---------|-------|--------|-----------|--------|-----------|------|
| [F-1] | 100 | 3 | 90% | 12 wks | 22.5 | 1 |
| [F-2] | 50 | 2 | 80% | 8 wks | 10 | 2 |
| [F-3] | 30 | 1 | 70% | 4 wks | 5.25 | 3 |

## Q[X] Committed (Top Priorities)

### Priority 1: [Feature] (RICE: 22.5)
- **Why:** [Business rationale]
- **Customer impact:** [How it helps]
- **Timeline:** [Launch date]
- **Dependencies:** [What it needs]
- **Owner:** [PM + Eng lead]

### Priority 2: [Feature] (RICE: 10)
- [Same format]

### Priority 3: [Feature] (RICE: 5.25)
- [Same format]

## Q[+1] Planned (Exploring)

- [Feature 4]
- [Feature 5]

## Roadmap Rationale

1. [Why this order?]
2. [What's deferred and why?]
3. [Strategic bets?]
```

## Success Criteria

✅ Features ranked consistently
✅ Business rationale clear
✅ Dependencies identified
✅ Capacity realistic
✅ Roadmap communicated to team
