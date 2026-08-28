# Skills Registry

> The agent reads this to know WHICH skill to reach for and WHEN. Skills are tools,
> not agents — the single agent loads the relevant skill file, follows it, gates on
> PM approval, and records the result. 26 skills across the product lifecycle.

---

## How to select a skill
1. Identify the PM's intent (discover? decide? spec? design? justify? launch? learn?)
2. Match to the phase below.
3. If a skill needs domain framing, read `knowledge/domains/<b2b|b2c|internal>.md` first.
4. Announce the chosen skill in your PROMPT PREVIEW before executing.

---

## Skills by phase

### Strategy & Framing (higher altitude)
| Skill | Use when | Reads |
|-------|----------|-------|
| `product-strategy` | Setting direction, where-to-play/how-to-win | company.md, domains/ |
| `business-model` | How value is created/captured | domains/ |
| `business-case` | Justify an investment (🟡napkin / 🟢full modes) | domains/, constraints.md |

### Discovery
| Skill | Use when |
|-------|----------|
| `user-research-facilitator` | Designing research, interviews, personas |
| `researcher` | Extracting patterns from evidence |
| `design-thinking-facilitator` | Creative reframing / ideation |
| `journey-mapper` | Mapping end-to-end experience |
| `persona-developer` | Building customer segments |

### Decision
| Skill | Use when |
|-------|----------|
| `opportunity-generator` | Turning insights into opportunities |
| `hypothesis-validator` | Defining testable hypotheses |
| `competitive-analyst` | Competitive landscape |
| `risk-assumption-tracker` | De-risking before build |
| `experiment-planner` | Designing validation tests |
| `decision-evaluator` | Recommending build/kill/test |

### Design & Prototyping  ⚑ special handoff
| Skill | Use when | Note |
|-------|----------|------|
| `prototype-brief` | "Create a prototype for [idea]" | Produces BRIEF, then **hands off to a design runtime** — see below |
| `design-reviewer` | Critiquing a rendered prototype/wireframe | |
| `design-handover` | Speccing approved design for engineering | Every state + a11y + acceptance criteria |

### Specification & Planning
| Skill | Use when |
|-------|----------|
| `product-spec-writer` | Writing the product/engineering spec |
| `roadmap-planner` | Prioritizing + sequencing (RICE/Kano/MoSCoW) |
| `effort-estimator` | Story points / capacity |
| `stakeholder-manager` | Alignment, RACI, comms |

### Launch & Execution
| Skill | Use when |
|-------|----------|
| `go-to-market-strategist` | Positioning, messaging, pricing, launch strategy |
| `launch-coordinator` | Executing the launch |
| `agile-coach` | Sprint ceremonies, team execution |

### Measurement & Learning
| Skill | Use when |
|-------|----------|
| `analytics-strategist` | KPIs, measuring outcomes, A/B analysis |
| `post-launch-analyst` | Closing the learning loop → back to evidence |

---

## ⚑ The design handoff (critical — the harness does NOT draw pixels)

When a PM asks for a prototype:

```
prototype-brief            → agent writes structured BRIEF (input, not pixels)
   ↓  [APPROVAL GATE]
DESIGN RUNTIME renders      → Claude Design canvas (`design` skill) OR Figma (Figma MCP)
   ↓                          THIS is where actual artboards/prototype are generated
design-reviewer            → critiques the rendered output
   ↓  [iterate ↑]
design-handover            → full spec for engineering (states, tokens, a11y, criteria)
   ↓
product-spec-writer        → absorbs UI detail into the spec
```

The agent orchestrates; the design tool renders. Never attempt to produce the
visual prototype from inside the harness — invoke the runtime.

---

## ⚑ Domain lens (which world are we in?)

Before any strategy / business-model / business-case / analytics / gtm work, the
agent determines the domain from `knowledge/product.md` (or asks) and reads the
matching file:
- `knowledge/domains/b2b.md` — ACV, CAC, LTV, NRR, buyer≠user, sales cycle
- `knowledge/domains/b2c.md` — DAU/MAU, retention curves, ARPU, virality (K)
- `knowledge/domains/internal.md` — adoption, time-saved, cost-avoided, no revenue

Applying the wrong domain's metrics is a flagged error.

---

## Common request → skill map (quick lookup)

| PM says... | Reach for |
|-----------|-----------|
| "Is this idea worth pursuing?" | `business-case` (napkin) → maybe `business-model` |
| "What's our direction here?" | `product-strategy` |
| "How would this make money?" | `business-model` |
| "Create a prototype for X" | `prototype-brief` → design runtime → `design-reviewer` |
| "Get this design ready for eng" | `design-handover` |
| "Should we build this?" | `risk-assumption-tracker` → `business-case` (full) → `decision-evaluator` |
| "Analyze these interviews" | `researcher` |
| "Did it work?" | `analytics-strategist` → `post-launch-analyst` |
```
