---
name: ux-review
description: >
  Evaluate a built screen or flow against UX heuristics and report what to fix —
  each finding with a severity and a concrete fix. Use to review or audit a UI's
  usability, before shipping a flow, or to turn "this feels off" into specific,
  rankable problems. The UX counterpart to /code-review.
---

# UX Review

Walk a built UI against known heuristics and report the violations — ranked, located, each with a fix. You are **evaluating, not redesigning**: the output is a list of problems worth fixing, not a new design. Hand the fixes to `/ux-flows` and `/make-it-obvious`.

## Set up the evaluation

1. **Know who you're evaluating for.** Pull the persona and mental model from `USER-BRIEF.md` (`/understand-the-user`) if it exists; otherwise state the assumed user in one line. A heuristic violation only matters relative to a user trying to do something.
2. **Walk the real thing.** Run the UI if you can and go through the flow state by state — empty, loading, success, error, edge. If you can't run it, review the markup and components. Never review from memory of how it "should" look.

## The heuristics

Check every screen and transition against each. Most are violated by *omission* — the missing feedback, the absent escape hatch.

1. **Visible status** — the system always shows what's happening; every action gets feedback where it happened.
2. **Match the user's model** — words, icons, and flow match the user's world, not the database schema or the org chart.
3. **Obvious & scannable** — actionable things look actionable; the screen is self-evident at a glance (`/make-it-obvious`).
4. **Control & escape** — undo, back, cancel everywhere; no dead ends, no trap states.
5. **Consistency & conventions** — the same thing looks and behaves the same throughout; platform conventions honored.
6. **Error prevention & forgiveness** — slips blocked by constraints; irreversible actions confirmed or gated. Prevent the error rather than scold it.
7. **Recognition over recall** — choices and context are visible; the user never has to remember something from a previous screen.
8. **Plain-language errors** — failures explained in human terms with a way forward, never a raw code or a dead end.
9. **Orientation** — every screen answers "where am I, and where can I go from here."
10. **Calm & minimal** — nothing competes with the primary content; no needless words, no noise. Doesn't deplete goodwill (no asking for data you don't need, no dark patterns).
11. **Accessible** — keyboard-reachable, screen-reader-labeled, sufficient contrast, never color alone for meaning.

## Report

For every finding:

```
[SEVERITY] Heuristic — where it is
What's wrong (one line) → the fix (one line)
```

Severity:
- **Blocker** — users can't complete the task, or lose data/trust.
- **Major** — completable, but with real friction, confusion, or error risk.
- **Minor** — noticeable rough edge; works.
- **Polish** — cosmetic.

_Done when:_ every screen state has been walked against all eleven heuristics, findings ranked by severity (blockers first), each located and paired with a fix, and the single highest-leverage fix called out at the end. Each blocker or major is a candidate issue for `/to-issues` or a task for the review-and-refactor skills.
