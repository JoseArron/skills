---
name: ux-flows
description: >
  Design and implement app screens and user flows with calm, user-first UX —
  obvious CTAs, feedback at the point of action, thumb-zone layout, and
  domain-modularized components. Use when the user asks to build or polish
  UI/UX, design a user flow, make a screen "feel" right, or mentions
  effortless/calm design, confirmations, error states, or empty states.
---

# UX Flows

Design every screen by walking the user's journey, not by listing widgets.

## The lens

Before building, answer for each state of the flow:

1. **What did the user just do?** The screen must acknowledge it instantly.
2. **What do they want to know right now?** Show exactly that — nothing else.
3. **What will they most likely do next?** Make that the one obvious CTA and lead them into it.
4. **Where are they looking / where is their thumb?** Feedback appears where they look; primary actions sit in the bottom bar or a bottom sheet (thumb zone). Never bury the next step at the top.

If a component's purpose is an action, the CTA must be unmissable. If its purpose is information, remove every label the content already implies (no "Truck" eyebrow above a plate number).

## Feedback at its locality

The user's context stays in one place; the consequence of an action shows up right there.

- State changes animate in place (status color/progress on the same card), paired with haptics on mobile.
- Confirmations and results come up from the bottom (bottom sheet on mobile, inline/toast on web) — never navigate away to confirm.
- After creating something: highlight the new item in the list. After deleting: themed toast with **Undo** — the most likely next wish.
- Celebrate completions (Duolingo-style): one springy check moment at the _end_ of a journey. Don't celebrate intermediate steps — that's noise.

## Action weight

Match friction to consequence:

- **Harmless / expected action** → fires directly, button shows its own spinner.
- **Irreversible or bulk action** → one confirm sheet stating the consequence in plain words ("This can't be undone") with an easy way out ("Not Yet").
- **Legal / responsibility moment** → deliberate two-step: explicit checkbox statement gates the CTA.

Never stack two celebrations or two confirms in a row.

## Errors

- Map error codes to human views in a domain component (title + what happened + what to do), never raw messages.
- The primary CTA is the most likely recovery (Refresh when state is stale, Try Again for network). Dismiss is always available for recoverable errors.
- Errors appear at the same locality as the action that caused them (sheet over the same screen).

## Empty & loading states

- Empty state greets and points at the single way to begin.
- Every async CTA shows loading on the button itself; full-screen spinners only for initial load.

## Modularization

Organize by domain, not by widget type. One common layout (adapt to your framework):

- **Domain components** (`components/<domain>/`) — flow-specific pieces: sheets, summaries, status maps.
- **Shared primitives** (`components/ui/`) — reusable building blocks: button, card, checkbox, feedback sheet.
- **Behavior layer** (`hooks/<domain>/`, or your framework's equivalent) — fetching, async + error→result mapping, haptics. View state (which sheet is open) stays inline in the screen.
- Readability over reusability: make components native to their domain instead of building generic abstractions.

## Checklist before done

- [ ] Each flow state answers the four lens questions.
- [ ] One primary CTA per screen state, in the thumb zone.
- [ ] No redundant labels; content speaks for itself.
- [ ] Friction matches consequence (direct / confirm / checkbox).
- [ ] Errors are human, local, and lead to recovery.
- [ ] End-of-journey state celebrates, then offers a clean reset.
