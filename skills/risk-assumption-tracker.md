# Risk & Assumption Tracker Skill

## Role
Identify what could go wrong, what you're assuming, and what must be validated before building. De-risks decisions before they become expensive.

## When to Use
- After Decision to BUILD
- Before Spec is finalized
- To validate risky assumptions
- To identify technical blockers
- To plan mitigation strategies

## Critical Constraints
- Distinguish between risks (what could go wrong) and assumptions (what you believe)
- Only flag risks that are actionable
- Get input from technical team on technical risks
- Ask clarifying questions when risk is unclear
- Prioritize by likelihood × impact

## Input
PM provides:
- Feature/product spec
- Original decision & hypothesis
- Technical architecture (if available)
- Team/resource constraints
- Market/competitive context

## Process

### Step 1: Identify Assumptions

For the product/feature, list what you're assuming:
- About customers (do they really want this?)
- About usage (how will they actually use it?)
- About adoption (will they pay?)
- About business model (will it be profitable?)
- About technical feasibility (can we build it?)
- About market (is it a real market?)

### Step 2: Assess Each Assumption

For each assumption:
1. **State it explicitly** - What exactly are we assuming?
2. **How confident?** - HIGH / MEDIUM / LOW
3. **Why believe it?** - What's the evidence?
4. **Risk if wrong** - What breaks if this assumption is false?
5. **Can we test it?** - How would we validate?

### Step 3: Identify Technical Risks

Ask engineering:
- What's architecturally risky?
- Any third-party dependencies risky?
- Performance unknowns?
- Integration complexities?
- Scaling concerns?

### Step 4: Identify Market Risks

- Competitor response?
- Customer adoption barriers?
- Pricing sensitivity?
- Regulatory issues?
- Market timing?

### Step 5: Prioritize

Focus on:
1. **High likelihood + High impact** = CRITICAL (mitigate before building)
2. **High likelihood + Medium impact** = IMPORTANT (plan mitigation)
3. **Low likelihood + High impact** = MONITOR (watch for)
4. **Low likelihood + Low impact** = ACCEPT (ok to proceed)

### Step 6: Create Artifact

Artifact: `specs/risks_[product]_[date].md`

## Output Artifact Format

```markdown
# Risk & Assumption Register: [Product Name]

**Date:** YYYY-MM-DD
**Product:** [Name]
**Related Decision:** D-###

---

## Critical Assumptions (MUST VALIDATE)

### Assumption 1: [Specific assumption]

**Statement:** "We assume [X] because [why]"

**Confidence:** MEDIUM (based on 5 customer interviews)

**Evidence:** 
- [Interview quote]
- [Competitive analysis]
- [Data point]

**Risk if wrong:** If customers don't actually want this, product has no users

**Can we test?** 
- ✅ Yes: Run prototype test with 5 customers
- **Cost:** 1 week, 5 hours PM time
- **Owner:** [Person]

**Status:** PENDING VALIDATION
- [ ] Validated
- [ ] Partially validated
- [ ] Invalidated
- [ ] Accepted risk

### Assumption 2: [Specific assumption]
- [Same format above]

---

## Technical Risks (Reviewed with Engineering)

### Risk 1: [Technical risk]

**Description:** "Third-party API integration may not support [X]"

**Likelihood:** MEDIUM (API docs unclear)

**Impact:** HIGH (blocks core feature)

**Mitigation:**
1. Request API documentation from vendor
2. Build spike to test integration
3. Identify alternative if it doesn't work

**Owner:** [Engineer]

**Timeline:** Complete by [Date]

### Risk 2: [Technical risk]
- [Same format]

---

## Market Risks

### Risk 1: [Market risk]

**Description:** "Competitor [Name] launches similar product"

**Likelihood:** MEDIUM (they have roadmap for this)

**Impact:** MEDIUM (slows our adoption, not fatal)

**Mitigation:**
1. Move launch forward if possible
2. Differentiate on [specific dimension]
3. Launch with unique positioning

**Owner:** [PM]

### Risk 2: [Market risk]
- [Same format]

---

## Customer Adoption Risks

### Risk: Low adoption despite building

**Likelihood:** MEDIUM (adoption curves are unpredictable)

**Impact:** HIGH (wastes engineering time)

**Mitigation:**
1. Define success criteria upfront
2. Plan early measurement
3. Have pivot strategy ready
4. Can pivot to [Alternative direction]

---

## Business Model Risks

### Risk: Pricing doesn't work

**Likelihood:** MEDIUM (pricing is often wrong initially)

**Impact:** MEDIUM (revenue target miss)

**Mitigation:**
1. A/B test pricing in market
2. Have alternative pricing models ready
3. Can adjust after 3 months

---

## Adoption Barriers (Customer Education)

### Barrier: Complex feature, slow to learn

**Mitigation:**
- Invest in onboarding walkthrough
- Create tutorial videos
- Have customer success check-ins first month

---

## Go/No-Go Checklist

**Before building, ALL CRITICAL risks must be mitigated:**

- [ ] Customer demand validated (assumption test)
- [ ] Technical spike complete (technical risk addressed)
- [ ] Pricing tested (business model risk addressed)
- [ ] Competitor threat assessed (market risk understood)
- [ ] Team capacity confirmed (resource risk addressed)

**If any critical assumption is HIGH RISK + UNVALIDATED:**
→ Don't build yet. Validate first.

---

## Assumption Validation Plan

| Assumption | Validation Method | Duration | Owner | Status |
|-----------|-------------------|----------|-------|--------|
| [A-1] | [Method] | [X days] | [Person] | PENDING |
| [A-2] | [Method] | [X days] | [Person] | PENDING |

---

## Risk Scorecard

| Risk | L | I | Score | Priority | Mitigation |
|------|---|---|-------|----------|-----------|
| [R-1] | H | H | 9 | 🔴 CRITICAL | [Plan] |
| [R-2] | M | H | 6 | 🟠 IMPORTANT | [Plan] |
| [R-3] | L | M | 2 | 🟡 MONITOR | [Plan] |

Legend: L=Likelihood, I=Impact

---

## Post-Launch Assumption Validation

After shipping, measure:
- **A-1:** Did customers adopt? YES/NO → Validates/Invalidates
- **A-2:** Did they spend less time? YES/NO → Validates/Invalidates

---

## Lessons for Next Feature

Based on validating/invalidating assumptions:
- [Pattern 1: If we see X in discovery, it usually means Y]
- [Pattern 2: Pricing assumptions usually miss by Z]
- [Pattern 3: Customer adoption barriers we should watch for]
```

## Questions Agent MUST Ask

Before creating risk register:
1. What specifically are we uncertain about?
2. Have engineering review technical risks
3. What decisions hinge on which assumptions?
4. Which risks would kill the product if true?
5. Which assumptions can we test before building?

## Questions Agent MUST Ask PM

```
"I've identified assumptions and risks for [product].

Critical issues requiring mitigation:
1. [Assumption A-1]: [Risk if wrong] → Validate via [method]
2. [Risk R-1]: [Impact] → Mitigate by [action]

Questions:
1. Do you agree these are the critical assumptions?
2. Are there risks I missed?
3. Which should we validate before building?
4. What's our risk tolerance?"
```

## What NOT to Do

❌ DON'T list every possible risk
```
WRONG: "Server might catch fire"
RIGHT: "Server performance under peak load unknown - test with load testing"
```

❌ DON'T assume without evidence
```
WRONG: "Customers will pay $X"
RIGHT: "We assume customers will pay $X based on [evidence]; need to validate"
```

❌ DON'T ignore technical risks
```
WRONG: "Engineering will figure it out"
RIGHT: "Third-party API integration is risky - needs spike to validate"
```

❌ DON'T proceed with high-risk assumptions unvalidated
```
WRONG: "Let's build and see if it works"
RIGHT: "Build only after validating [critical assumption]"
```

## Success Criteria

Output passes if:
✅ Critical assumptions explicitly stated
✅ Evidence for each assumption documented
✅ Risks ranked by likelihood × impact
✅ Mitigations identified and realistic
✅ Go/No-Go criteria clear
✅ Validation plan specific (who, when, method)
✅ Technical risks reviewed with engineering
✅ Nothing building starts without high-risk validation

## Integration

This skill:
- Uses output from **Decision Evaluator** (decision to build)
- Uses output from **Competitive Analyst** (market risks)
- Feeds into **Product Spec Writer** (risk mitigation approaches)
- Updates **decision_log.md** with risk assessment
- Post-launch, validates assumptions with **Post-Launch Analyst**

## Critical: Risk de-risking

High-risk assumptions should be validated BEFORE expensive build:

```
Assumption: "Customers want X"

Option A: Build full feature ($100K) then find out nobody wants it
Option B: Prototype ($5K), validate with customers, THEN decide to build

Option B is the right answer.
```

This skill ensures you choose Option B.
