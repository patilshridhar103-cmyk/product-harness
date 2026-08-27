# Domain Knowledge: B2B Products

> REFERENCE, not a skill. Skills (business-case, business-model, product-strategy,
> analytics-strategist, gtm-strategist) READ this to pick the right metrics and
> mental model when the product is B2B. Load when knowledge/product.md indicates
> B2B, or when the PM says so.

---

## The defining truth of B2B
**The buyer is usually not the user.** A manager/exec/procurement buys; a team uses.
This splits every decision: value must land for the *user* (adoption) AND the
*buyer* (ROI, budget justification). A feature users love that buyers can't
justify still fails. A feature buyers love that users won't adopt also fails.

## How money works
- **Revenue model:** subscription/contract (annual most common), often seat-based,
  usage-based, or tiered. Expansion revenue (more seats/upsell) is where the
  economics are won.
- **Deal shape:** fewer, larger deals. Sales-assisted or sales-led above ~$10–15k
  ACV; self-serve possible below that (PLG).
- **Sales cycle:** weeks to quarters. Longer with more stakeholders / higher price.

## Core metrics (use THESE for B2B cases, not DAU/MAU)
| Metric | What it is | Why it matters |
|--------|-----------|----------------|
| **ACV / ARR** | Annual contract value / recurring revenue | The unit of B2B revenue |
| **CAC** | Cost to acquire a customer | Sales+marketing ÷ new customers |
| **CAC payback** | Months to recover CAC | <12 mo healthy; <18 acceptable |
| **LTV** | Lifetime value | ACV × gross margin × avg lifetime |
| **LTV:CAC** | Ratio | >3:1 healthy |
| **NRR** | Net revenue retention | >100% = growing without new logos; **the** B2B health metric |
| **Logo churn** | % customers lost | Different from revenue churn |
| **Revenue churn** | % revenue lost | Can be low even if logo churn high (small accounts leave) |
| **Seat expansion** | Growth within accounts | Cheapest growth there is |
| **Sales cycle length** | Time to close | Drives cash flow + forecasting |
| **Win rate** | % of qualified deals won | Sales efficiency |

## Who's in the room (stakeholders)
- **Economic buyer** — controls budget, needs ROI/justification.
- **Champion** — internal advocate who wants it; sells it for you internally.
- **User(s)** — must actually adopt or renewal dies.
- **Blockers** — IT/security/legal/procurement. Any one can kill a deal.
- Implication: value props and business cases must speak to *multiple* audiences.

## What "good" looks like
- NRR > 100%. Adoption inside accounts, not just logos signed.
- CAC payback < 12 months. LTV:CAC > 3.
- Champions who renew and expand.

## Business-case levers (what to model)
- New logo revenue + **expansion** (usually the bigger lever).
- Retention/churn impact (retaining ACV is often worth more than winning it).
- Sales efficiency (does this shorten the cycle / raise win rate?).
- Cost to serve (support load, onboarding cost).

## Common traps the agent should flag
- Modeling B2B like B2C (DAU, virality) — wrong frame.
- Ignoring the buyer≠user split — building only for users, no ROI story.
- Forgetting procurement/security can block an otherwise-won deal.
- Counting logos when the board cares about revenue (or vice versa).

## GTM shape
- Sales-led, PLG, or hybrid. Champions, pilots/POCs, case studies, ROI calculators.
- Pricing anchored to value delivered to the *business*, not cost-plus.
