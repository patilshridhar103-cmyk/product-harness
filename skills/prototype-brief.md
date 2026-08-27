# Prototype-Brief Skill

## Role
Turn an idea into a structured brief a DESIGN RUNTIME can execute, then orchestrate
the handoff. **The harness does not draw pixels — it produces the brief and invokes
a design tool (Claude Design canvas or Figma) that renders the actual prototype.**

## The mental model
```
IDEA ──(this skill: brief)──▶ [APPROVAL] ──▶ DESIGN RUNTIME renders ──▶
        design-reviewer critiques ──(loop)──▶ design-handover specs it
```
This skill owns the INPUT (brief) and the handoff. It does not own the pixels.

## When to Use
- PM says "create a prototype for [idea]"
- Need to make an idea tangible to think with, or to validate a hypothesis
- Before design-reviewer and design-handover

## Reads First
- `knowledge/product.md` — **platform + stack + existing design system are constraints**
- `knowledge/customers.md` — the user + JTBD the prototype serves
- Related `O-###` / `PS-###` if the idea is already scoped

## Critical Constraints — ASK FIRST
Before writing the brief, resolve fidelity + intent (don't assume):
```
Agent: Two questions before I brief this:
  1. Is this a THROWAWAY concept prototype to think with, or a VALIDATION
     prototype for a specific hypothesis? (changes fidelity + rigor)
  2. Fidelity: low (structure/flow), mid (layout+content), or high
     (visual, near-real)?
```
- Respect platform constraints from product.md (e.g. "responsive web only — no
  native mobile"). A prototype that violates the platform is waste.
- Use REAL content, not lorem — the brief specifies actual copy.
- Cover states: empty, loading, error, success — not just the happy path.

## Process

### Step 1: Confirm intent + fidelity (above)

### Step 2: Frame the brief
- User + JTBD (from customers.md)
- The hypothesis (if validation prototype)
- Scope: which flow, which screens — and what's explicitly OUT

### Step 3: Specify the flow, screen by screen
For each screen: purpose, key elements, content (real), states, interactions.

### Step 4: Capture design constraints
- Platform/stack (product.md), existing design system/tokens, accessibility bar

### Step 5: Produce the brief artifact
`artifacts/design/BRIEF-<NNN>.md`

### Step 6: [APPROVAL GATE] then HAND OFF to the design runtime
After PM approves the brief, invoke the design tool:
- **Claude Design canvas** (the `design` skill) for multi-artboard screen flows, or
- **Figma** (Figma MCP) if the team works in Figma
Pass the brief as the spec. The runtime renders artboards/prototype.
Record the runtime output location alongside the brief.

## Output Template (the BRIEF)

```markdown
# Prototype Brief BRIEF-###: [Idea]

**Date:** YYYY-MM-DD · **Intent:** [throwaway concept / validation]
**Fidelity:** [low / mid / high] · **Related:** [O-### / H-### / PS-###]

## User & Job
- **User:** [persona] · **JTBD:** [job]
- **Hypothesis (if validation):** [If they see X, they'll do Y]

## Scope
- **In:** [the flow being prototyped]
- **Out:** [explicitly not included]

## Flow (screen by screen)
### Screen 1: [Name]
- **Purpose:** [why this screen]
- **Key elements:** [components]
- **Content:** [REAL copy, not lorem]
- **States:** empty / loading / error / success — [what each shows]
- **Interactions:** [what the user can do → where it goes]
### Screen 2: [Name]
- [...]

## Design Constraints (from knowledge/product.md)
- **Platform:** [e.g. responsive web only]
- **Stack/system:** [e.g. React + existing design system tokens]
- **Accessibility:** [bar — e.g. WCAG AA, keyboard nav]

## Handoff
- **Runtime:** [Claude Design canvas / Figma]
- **Rendered output:** [location/link once generated]
```

## Questions Agent MUST Ask
1. Throwaway concept or validation prototype?
2. What fidelity?
3. If validation — what's the exact hypothesis it must test?
4. Any platform/system constraints I should confirm beyond product.md?

## What NOT to Do
❌ Try to "draw" the prototype in the harness — hand off to the design runtime
❌ Assume fidelity/intent — ask
❌ Lorem ipsum — specify real content
❌ Happy-path only — specify empty/loading/error states
❌ Violate platform constraints from product.md

## Success Criteria
✅ Intent + fidelity confirmed with PM
✅ Every screen has purpose, real content, and states
✅ Platform/system constraints captured
✅ Approval gate before rendering
✅ Handed to a real design runtime; output location recorded

## Integration
Feeds: design-reviewer (critiques the rendered output), design-handover (specs it
for eng). Reads: knowledge/product.md, customers.md. Invokes: `design` skill / Figma.
```
