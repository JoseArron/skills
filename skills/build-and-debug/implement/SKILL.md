---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Use /tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Before the final review, run the focused review skills that match the work:

- Use /prune-cruft when the implementation added or exposed memoization, defensive type checks, dead code, wrappers, pass-through abstractions, speculative options, or other code that may not earn its keep.
- Use /audit-implementation when the implementation includes user-facing controls, routing, data fetching, query shape, framework idioms, persistence, or tool choices whose behavior must match their labels and the stack's native path.

Keep these separate from /code-review. /prune-cruft removes unearned complexity, /audit-implementation checks feature truth and stack fit, and /code-review checks the final diff against repo standards and the originating spec or tickets.

Once done, use /code-review to review the work.

Commit your work to the current branch.
