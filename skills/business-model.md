# Business Model Skill

## Role
Define how the product creates, delivers, and captures value. For revenue products
that's how it makes money; for internal products that's how it creates measurable
value. Uses the domain lens.

## When to Use
- New product/feature idea where the value-capture mechanism isn't obvious
- Before or alongside a business case (the model defines what the case measures)
- When choosing a revenue model (subscription vs. usage vs. freemium, etc.)
- Brainstorming a new venture/product line

## Reads First
- `knowledge/domains/<b2b|b2c|internal>.md` — **decides the whole frame**
- `knowledge/company.md` · `knowledge/customers.md` · `knowledge/constraints.md`

## Critical Constraints
- Pick the frame from the domain FIRST (revenue model for B2B/B2C; value model for internal)
- Don't invent willingness-to-pay — ask or mark as assumption to validate
- Model must be internally consistent (cost structure vs. revenue mechanism)

## Process

### Step 1: Determine domain & frame
Read the domain file. B2B/B2C → money model. Internal → value model (time/cost/risk).

### Step 2: Value Creation
- What value, for whom (customer/user/business)?
- The core JTBD it serves

### Step 3: Value Delivery
- How it reaches users (channels, self-serve vs. assisted, rollout for internal)
- What it costs to deliver (cost structure)

### Step 4: Value Capture
- **Revenue products:** model (subscription/usage/freemium/transactional/ads),
  pricing basis (per-seat/usage/tier/value), price hypothesis
- **Internal products:** value basis (hours saved × cost, cost avoided, risk reduced)

### Step 5: Unit Economics (rough)
- Per-unit: what does one customer/user cost vs. return?
- Pull the right metrics from the domain file (LTV:CAC for revenue; value:cost for internal)

### Step 6: Produce Artifact
`artifacts/strategy/BM-<NNN>.md`

## Output Template

```markdown
# Business Model BM-###: [Product/Idea]

**Date:** YYYY-MM-DD · **Domain:** [B2B/B2C/internal] · **Related:** [O-### / STRAT-###]

## Value Creation
- **Value:** [what problem solved, what enabled]
- **For:** [customer / user / business]

## Value Delivery
- **Channels:** [how it reaches users / internal rollout path]
- **Cost structure:** [main costs to build + run + serve]

## Value Capture
### (Revenue product)
- **Model:** [subscription / usage / freemium / transactional / ads]
- **Pricing basis:** [per-seat / usage / tier / value-based]
- **Price hypothesis:** $[X] — **assumption, validate**
### (Internal product)
- **Value basis:** [hours saved × loaded cost × users] / [cost avoided] / [risk reduced]
- **Estimated annual value:** $[X] — **assumption, validate**

## Unit Economics (rough)
- [Revenue: LTV, CAC, LTV:CAC, payback — from domains/<x>.md]
- [Internal: annual value per user vs. build+run cost per user]

## Key Assumptions (→ risk-assumption-tracker)
- [Assumption 1 — the load-bearing one]
- [Assumption 2]

## Viability Read
- [Does capture exceed cost of delivery, on the domain's terms? Confidence?]
```

## Questions Agent MUST Ask
1. Is this B2B, B2C, or internal? (if not clear from product.md)
2. Do we have any willingness-to-pay / value data, or is it all assumption?
3. What's the rough cost to build + run? (ask engineering for a t-shirt size)

## What NOT to Do
❌ Apply revenue metrics to an internal product (or vice versa)
❌ Fabricate a price or value number — mark assumptions, ask for inputs
❌ Model capture without cost structure (half a model)

## Success Criteria
✅ Frame matches domain (revenue vs. value)
✅ Creation + delivery + capture all present and consistent
✅ Unit economics use domain-correct metrics
✅ Load-bearing assumptions flagged for validation

## Integration
Feeds: business-case (defines what to quantify), gtm-strategist (pricing).
Reads: knowledge/domains, product-strategy.
