# Product Harness

A local-first system that turns customer evidence into product decisions — with a
**PM in the loop at every step**. It's not an app and not a chatbot. It's a folder
you open in Claude Code (or any agent runtime) where a **single agent** uses
**skills** as tools, works inside **project-scoped memory**, and creates nothing
without your approval.

> The LLM isn't the product. The **state machine + evidence + artifacts + memory**
> are the harness. The agent is the thing that moves work through it.

---

## Why this exists

Ask a chatbot "analyze these 100 interviews and tell me what to build" and it gives
a good answer — once. Two weeks later, new evidence arrives and you start a fresh
conversation. The reasoning doesn't persist; decisions can't be operationalized.

A harness instead remembers. `O-001` already exists. New evidence `EV-193` arrives
and the system can say: *"O-001 now has 7 supporting sources, but EV-195 contradicts
assumption A-3 — re-evaluate H-12."* Every agent action traces back to a product
decision, and every decision to its evidence. That's the difference between a pile
of AI-generated documents and a **product-development graph**.

---

## Core principles

1. **PM in the loop.** Before any artifact, the agent shows a *prompt preview* —
   what it will do, which skill, what it will create, what it needs. You approve,
   reject, or modify. Nothing runs ahead of you.
2. **Ask, don't assume.** Missing data, contradictions, ambiguous scope → the agent
   asks. It never fabricates quotes, numbers, or evidence.
3. **One agent, many skills.** Not a swarm of agents. One agent with full context
   that loads a skill (a procedure) when the task calls for it.
4. **Flat memory, forever.** Tiered, self-compacting, project-scoped memory keeps
   session-start context roughly constant whether it's session 5 or 500.
5. **The harness orchestrates; specialist tools render.** It doesn't draw pixels —
   it briefs a design runtime (Claude Design / Figma) and specs the result.

---

## The loop

```
evidence → synthesis → opportunities → hypotheses → experiments → decision
   ▲                                                                  │
   │                                                                  ▼
learning ◄── measure ◄── launch ◄── GTM ◄── spec ◄── (design handoff)
   │
   └─────────► fed back into evidence for the next cycle
```

Every hop is a skill, every output an artifact, every artifact gated by you and
recorded in memory.

---

## Repository layout

```
Product harness/
├── README.md                    ← you are here
├── .claude/
│   └── pm-harness-agent.md       ← THE single agent (session start, gates, rules)
│
├── memory/
│   └── INDEX.md                  ← portfolio router: which projects exist
│
├── system/                       ← the rulebook the agent follows
│   ├── skills-registry.md         · which skill, when (+ design & domain protocols)
│   ├── compaction.md              · keeps memory flat (HOT/WARM/COLD tiers)
│   ├── evaluation-framework.md    · quality rubric per artifact type
│   ├── artifact-templates.md      · the output format for each artifact
│   └── evidence-schema.md         · quality bar for incoming evidence
│
├── knowledge/                    ← shared context, loaded every session
│   ├── company.md · product.md · customers.md · constraints.md
│   └── domains/                   ← reference (NOT skills): the metric lens
│       ├── b2b.md                  (ACV, CAC, LTV, NRR, buyer≠user)
│       ├── b2c.md                  (DAU/MAU, retention, ARPU, virality)
│       └── internal.md             (adoption, time-saved, cost-avoided)
│
├── skills/                       ← 26 skills (procedures the agent loads)
│   └── researcher.md · opportunity-generator.md · … · post-launch-analyst.md
│
├── projects/                     ← one self-contained workspace per project
│   └── <project>/
│       ├── ACTIVE.md              · HOT memory: focus, open Qs, last 3–5 decisions
│       ├── SUMMARY.md             · WARM memory: one line per past item → archive
│       ├── decision_log.md        · append-only audit trail (never bulk-read)
│       ├── archive/<ID>.md        · COLD: full detail, retrieved by ID on demand
│       ├── evidence/              · raw evidence for this project
│       └── artifacts/             · non-memory work products
│
└── docs/
    └── GETTING_STARTED.md        ← 45-minute first-run walkthrough
```

---

## Memory model (why it scales)

Three tiers per project, plus an immutable trail:

| Tier | File | Loaded at start? | Grows? |
|------|------|------------------|--------|
| **HOT** | `ACTIVE.md` | always | no — capped at last 3–5 decisions |
| **WARM** | `SUMMARY.md` | always | slowly — one line per item |
| **COLD** | `archive/<ID>.md` | on demand, by ID | yes, unbounded |
| **AUDIT** | `decision_log.md` | never (bulk) | yes, append-only |

A session loads `INDEX` + one project's `ACTIVE` + `SUMMARY` + shared `knowledge/`
— a near-constant footprint. Old detail is pulled one file at a time, by ID, only
when relevant. `system/compaction.md` is the rule that keeps HOT small forever.

**Multiple projects** are handled by the router: the agent reads `memory/INDEX.md`,
resolves which project this session is about (by name, by an ID's prefix, or by
asking), and loads only that workspace. IDs carry their project prefix
(`PRI-D-004`), so the ID itself is the routing key.

---

## The 26 skills

Grouped by phase (full when-to-use in `system/skills-registry.md`):

- **Strategy & framing:** product-strategy · business-model · business-case (napkin/full)
- **Discovery:** user-research-facilitator · researcher · design-thinking-facilitator · journey-mapper · persona-developer
- **Decision:** opportunity-generator · hypothesis-validator · competitive-analyst · risk-assumption-tracker · experiment-planner · decision-evaluator
- **Design:** prototype-brief · design-reviewer · design-handover  *(hand off to a design runtime — the harness doesn't draw)*
- **Spec & planning:** product-spec-writer · roadmap-planner · effort-estimator · stakeholder-manager
- **Launch:** go-to-market-strategist · launch-coordinator · agile-coach
- **Learning:** analytics-strategist · post-launch-analyst *(closes the loop back to evidence)*

---

## How to use it

1. **Open the folder** in Claude Code: `claude code "Product harness"`.
2. The agent runs its session-start routine (`.claude/pm-harness-agent.md`):
   reads the router, resolves the project, loads that project's memory + shared
   knowledge, and greets you with a 4-line state summary.
3. **Tell it what you want** ("analyze these interviews", "is this idea worth it?",
   "create a prototype for X", "did the launch work?").
4. It returns a **prompt preview**. You approve.
5. It executes the skill, creates the artifact, and updates memory.

New here? Walk through `docs/GETTING_STARTED.md` — a full evidence → decision →
build → measure → learn cycle in about 45 minutes.

---

## Before first real use

The four `knowledge/*.md` files ship as **templates with `[placeholders]`**. Fill in
your real company, product, customers, and constraints — the whole system reasons
from them. Set `**Domain:**` in `knowledge/product.md` (B2B / B2C / internal) so the
agent auto-selects the right metric lens.

The two projects under `projects/` (`prioritization`, `mobile-redesign`) are a
**worked example** — a real traceable cycle you can read, then delete or keep as a
reference.

---

## What this is not

- Not a multi-agent swarm. One agent, skills as tools.
- Not autonomous. It gates every artifact on your approval.
- Not a design tool. It briefs and specs; Claude Design / Figma render.
- Not a chatbot with a good memory prompt. The memory is on disk, tiered, and
  survives every session.

---

## Status

Framework complete and self-consistent: single agent · tiered project memory ·
compaction · 26 skills · domain-knowledge layer · evaluation framework · artifact
templates · evidence schema · a worked two-project example. Personalize `knowledge/`
and start a project.
