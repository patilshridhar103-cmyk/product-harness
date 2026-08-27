# Domain Knowledge: B2C Products

> REFERENCE, not a skill. Skills read this when the product is consumer-facing.
> The mental model and metrics are fundamentally different from B2B — do not
> mix them.

---

## The defining truth of B2C
**The buyer IS the user, and there are many of them.** Decisions are fast,
emotional, individual, low-commitment. You win through volume, retention, and
often network/viral effects — not through a few large deals. Switching costs are
usually low, so **retention is everything**.

## How money works
- **Revenue models:** subscription (consumer SaaS), freemium→paid conversion,
  transactional/marketplace take-rate, ads (attention monetization), in-app
  purchase.
- **Deal shape:** many tiny "deals." Self-serve by default; no sales team in the loop.
- **Cycle:** seconds to days. Impulse to habit.

## Core metrics (use THESE for B2C, not ACV/NRR)
| Metric | What it is | Why it matters |
|--------|-----------|----------------|
| **DAU / MAU** | Daily / monthly active users | Core engagement volume |
| **DAU/MAU ratio** | Stickiness | >20% decent, >50% excellent (habitual) |
| **Retention curve** | % still active at D1/D7/D30 | Flattening curve = product-market fit signal |
| **Activation rate** | % reaching "aha" moment | Predicts retention |
| **ARPU / ARPPU** | Avg revenue per user / paying user | Monetization efficiency |
| **Conversion rate** | Free → paid, visitor → signup | Funnel health |
| **Viral coefficient (K)** | New users each user brings | K>1 = organic growth engine |
| **LTV** | Lifetime value | ARPU × avg lifetime × margin |
| **CAC** | Cost to acquire | Paid channels; must beat LTV |
| **Churn rate** | % leaving per period | Consumer churn is high; retention design is the job |
| **Session frequency/length** | Usage intensity | Habit strength |

## The engine to reason about
```
Acquisition → Activation → Retention → Referral → Revenue
(AARRR / "pirate metrics")
```
Consumer growth = retention × referral compounding. A leaky retention bucket
can't be filled by acquisition spend — fix retention first.

## What "good" looks like
- Retention curve that **flattens** (not decays to zero) — the PMF signal.
- DAU/MAU showing habit. K approaching or exceeding 1 for viral products.
- LTV > 3× CAC on paid channels.

## Business-case levers (what to model)
- Reach × conversion × ARPU × retention.
- Viral/organic coefficient (reduces effective CAC).
- Retention lift (small % retention gains compound massively over time).
- Engagement → monetization link (for ad/IAP models).

## Common traps the agent should flag
- Modeling B2C like B2B (ACV, sales cycle) — wrong frame.
- Optimizing acquisition while retention leaks — filling a leaky bucket.
- Vanity metrics (total signups) over cohort retention.
- Assuming willingness to pay; consumers are price-sensitive and fickle.

## GTM shape
- Product-led, content/SEO, paid social, app-store optimization, referral loops,
  influencer. Speed-to-value in the first session is decisive.
