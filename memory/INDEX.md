# Portfolio Index

> Router for the product harness. The agent reads THIS FILE FIRST at every
> session start — it is the map of all projects. Keep it small: one row per
> project, plus dependencies. Never put decision detail here; that lives in
> each project's own SUMMARY.md / archive/.

**Last updated:** 2026-08-27

---

## Active Projects

| Prefix | Project              | Status      | Focus right now                     | Last touched |
|--------|----------------------|-------------|-------------------------------------|--------------|
| PRI    | Smart Prioritization | BUILDING    | Spec approved → engineering handoff | 2026-08-26   |
| MOB    | Mobile Redesign      | DISCOVERY   | Synthesizing 8 interviews           | 2026-08-25   |

**Status vocabulary:** DISCOVERY · VALIDATING · DECIDING · SPEC · BUILDING · LAUNCHING · MEASURING · CLOSED

---

## Cross-Project Dependencies

> Declared, one-directional links. When a project's ACTIVE.md references one of
> these, the agent retrieves the single archived file by ID — never the whole
> other project.

- **MOB → PRI:** `MOB-O-002` (mobile filtering) may reuse the nav pattern decided in `PRI-D-004`.
  Retrieve `projects/prioritization/archive/PRI-D-004.md` if/when MOB reaches spec.
- **MOB → PRI:** MOB should not finalize its information architecture until `PRI` ships
  (shared navigation component). Blocking note, revisit after PRI launch.

---

## ID Scheme

`<PREFIX>-<TYPE>-<NNN>` — the prefix routes to the project, the type names the artifact.

| Type | Meaning        | Type | Meaning              |
|------|----------------|------|----------------------|
| SYN  | Synthesis      | E    | Experiment           |
| O    | Opportunity    | D    | Decision             |
| H    | Hypothesis     | PS   | Product Spec         |
| RISK | Risk register  | GTM  | Go-to-Market         |
| LEARN| Learning/outcome | LAUNCH | Launch plan       |

Example: `PRI-D-004` = Smart Prioritization → Decision 004.

---

## Archived / Closed Projects

| Prefix | Project        | Outcome                          | Closed     |
|--------|----------------|----------------------------------|------------|
| ONB    | Onboarding v2  | Shipped — +12% activation        | 2026-06-30 |

---

## Routing Rules (for the agent)

1. **PM names a project** → match to prefix, load that workspace.
2. **PM cites an ID** (e.g. "why did we park PRI-O-003?") → prefix routes the load.
3. **Ambiguous / nothing named** → show this roster, ask which project. Do NOT guess.
4. **Switching mid-session** → checkpoint the current project's ACTIVE.md first, then switch.
5. **"State of everything?" (portfolio mode)** → read each active project's ACTIVE.md
   header only; never pull archives.
