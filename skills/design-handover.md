# Design-Handover Skill

## Role
Turn an approved design/prototype into the complete spec engineering needs to build
it — every state, edge case, token, and acceptance criterion. Closes the gap
between "looks done" and "buildable."

## When to Use
- After a prototype is approved (via prototype-brief → design runtime → design-reviewer)
- Before or alongside product-spec-writer (design-handover fills the UI detail the spec references)
- Whenever design is going to engineering

## Reads First
- The approved `BRIEF-###` and its rendered output
- `design-reviewer` critique (so known issues are resolved, not shipped)
- `knowledge/product.md` (design system, stack, platform)

## Critical Constraints
- Specify EVERY state, not just the happy path — missing states = engineering guesses = bugs
- Reference the existing design system/tokens (don't invent one-off values)
- Every interaction needs defined behavior (including failures)
- Acceptance criteria must be testable
- Ask design/eng where a behavior is genuinely undefined — don't invent it

## Process

### Step 1: Inventory screens & components
List every screen and the components on each. Map to existing design-system
components where possible; flag any net-new component.

### Step 2: Enumerate states (per screen/component)
For each: default, empty, loading, error, success, disabled, edge (long text,
zero items, max items, offline). This is where handovers usually fail — be exhaustive.

### Step 3: Define interactions
Every action → what happens, transitions, validation, failure behavior.

### Step 4: Specify tokens & layout
Spacing, type, color, breakpoints — as references to the design system, not raw
one-off values. Responsive behavior per breakpoint.

### Step 5: Accessibility
Keyboard nav, focus order, ARIA/labels, contrast, screen-reader behavior.

### Step 6: Acceptance criteria
Testable checklist engineering + QA can verify against.

### Step 7: Produce Artifact
`artifacts/design/HANDOVER-<NNN>.md` (feeds product-spec-writer / engineering)

## Output Template

```markdown
# Design Handover HANDOVER-###: [Feature]

**Date:** YYYY-MM-DD · **Related:** BRIEF-### · PS-### · **Platform:** [from product.md]

## Screen/Component Inventory
| Screen | Components | Design-system match | Net-new? |
|--------|-----------|---------------------|----------|
| [S1] | [comp list] | [existing tokens/components] | [yes/no] |

## States (exhaustive, per screen)
### [Screen 1]
- **Default:** [description]
- **Empty:** [what shows when no data]
- **Loading:** [skeleton/spinner behavior]
- **Error:** [message + recovery action]
- **Success:** [confirmation behavior]
- **Edge:** [long text / 0 items / max items / offline]

## Interactions
| Trigger | Behavior | Transition | Validation | On failure |
|---------|----------|-----------|-----------|-----------|
| [click X] | [what happens] | [anim/route] | [rules] | [error behavior] |

## Tokens & Layout (reference design system)
- **Spacing/type/color:** [token references, not raw values]
- **Breakpoints:** [behavior at each — e.g. side-rail → bottom sheet <768px]

## Accessibility
- Keyboard: [tab order, shortcuts]
- ARIA/labels: [key elements]
- Contrast: [meets AA/AAA]
- Screen reader: [announced behavior]

## Acceptance Criteria (testable)
- [ ] [Criterion — every state renders correctly]
- [ ] [Criterion — interaction behaves + fails gracefully]
- [ ] [Criterion — responsive at each breakpoint]
- [ ] [Criterion — a11y bar met]

## Open Questions for Design/Eng
- [Anything genuinely undefined — ask, don't invent]
```

## Questions Agent MUST Ask
1. Is the reviewed prototype the final approved version?
2. Are there design-system components for these, or net-new ones needed?
3. Any interaction whose failure behavior isn't defined yet?

## What NOT to Do
❌ Happy-path only — enumerate every state
❌ Invent token values — reference the design system
❌ Leave failure behavior undefined — specify or ask
❌ Ship the reviewer's flagged issues into handover unresolved

## Success Criteria
✅ Every screen's states enumerated (incl. edge cases)
✅ Every interaction has defined behavior incl. failure
✅ Tokens reference the design system
✅ Accessibility specified
✅ Acceptance criteria testable
✅ Undefined behaviors surfaced as questions, not guesses

## Integration
Reads: prototype-brief output, design-reviewer critique, product.md.
Feeds: product-spec-writer (UI detail), effort-estimator, engineering handoff.
```
