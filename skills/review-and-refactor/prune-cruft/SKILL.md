---
name: prune-cruft
description: Surface and remove code that does not earn its keep — unnecessary memoization or caching, redundant type checks and casts, dead or unused code, over-engineered abstractions, and premature/unmeasured optimizations — in any language or framework. Use when the user wants to simplify a file or codebase, audit for cruft, cut needless memoization (useMemo/useCallback/React.memo, computed, lru_cache, hand-rolled caches), find dead code, drop redundant type guards, or asks "is this over-engineered" / "is this premature optimization".
---

# Prune Cruft

Cut code that does not earn its keep. Default is the simplest code that solves the problem; anything more must justify itself with a real, current reason.

## Glossary

- **Cruft** — code present without a current reason: unused, redundant, defensive past the point of need, or optimized for a non-problem.
- **Earned its keep** — has a real, current caller; a measured perf win; or a documented invariant. Hypothetical futures do not count.
- **Load-bearing** — removing it breaks something a real caller depends on today.
- **Deletion test** — imagine deleting it; if complexity vanishes it was a pass-through, if complexity reappears across callers it earned its keep.

## Categories

Each category has a detail file with heuristics and do/don't examples. Read the relevant file before classifying a finding. Examples lean on TypeScript/React because that is where this cruft is most epidemic, but every category applies to any language.

- **Unnecessary memoization** — a memo or cache (`useMemo`/`useCallback`/`React.memo`, Vue `computed`, a `lru_cache`, a hand-rolled `Map`) without a real referential-stability or measured perf reason. See [MEMOIZATION.md](MEMOIZATION.md).
- **Redundant type checks** — runtime guards the type system already proves, double null checks, defensive `?.` on non-nullable values, casts restating inference, double validation of already-validated data. See [TYPE-NARROWING.md](TYPE-NARROWING.md).
- **Dead / unused code** — exports, files, branches, params, flags, translation keys, enum members with no current consumer. See [DEAD-CODE.md](DEAD-CODE.md).
- **Over-engineering** — premature abstraction, single-implementation interfaces, factories of one, wrapper functions, options no caller flips, ports without a second adapter, unmeasured micro-optimizations. See [OVER-ENGINEERING.md](OVER-ENGINEERING.md).

## Principles

- **Default to inline.** Reach for a helper, wrapper, or abstraction only when removing it concentrates real complexity (deletion test).
- **Types are guards too.** If the type system already proves the case impossible, the runtime check is noise — and it lies about the contract.
- **Measure before optimizing.** No memoization, cache, or micro-opt without a measured runtime/CPU problem.
- **One caller is not a pattern.** Configurable knobs and ports need at least two real callers; rule-of-three for extraction.
- **Pruning removes, it does not redesign.** If a finding wants a new abstraction, escalate to `improve-codebase-architecture` instead.

## Process

### 1. Scope

Confirm what to scan: a file, a directory, a feature slice, or the whole app. Do not boil the ocean — pick a bounded surface so findings stay reviewable.

### 2. Scan

Walk the scope and tag findings against the four categories. For each candidate record:

- **Where** — file + line range
- **Category** — memoization / type-narrowing / dead-code / over-engineering
- **Why it is cruft** — concrete reason, not vibes — cite the heuristic from the detail file
- **Risk if removed** — none / low / needs callsite check / load-bearing

When a finding is ambiguous, prefer "needs callsite check" over deleting blind. For dynamic lookups, generated code, and cross-package exports, verify across the whole codebase (every app/package in a monorepo), not just the current file.

### 3. Present findings

Group by category, highest confidence first. Use this shape per finding:

- **File** — `@absolute/path:start-end`
- **Smell** — one line
- **Proposed change** — what to delete or replace with
- **Reasoning** — which heuristic from the category file applies
- **Verification** — typecheck / lint / test command, or "visual check on route X"

Do NOT bulk-apply yet. Ask the user which findings to action, or if they want a category swept at once.

### 4. Apply, then verify

Apply approved changes minimally — prefer deletion over rewrites, single-line edits over refactors. After each cluster:

- Run the project's typecheck or build (e.g. `tsc --noEmit`, `cargo check`, `go build`, `mypy`).
- Run lint / formatter on touched files.
- Run any tests that cover the touched modules.
- For UI changes, name the route(s) the user should re-click.

If a deletion breaks types, do NOT add casts to silence it — that is just relocating cruft. Fix the contract or revert the deletion.

### 5. Stop conditions

Stop when:

- Remaining findings are load-bearing or contested.
- A change would require redesigning a module — escalate to `improve-codebase-architecture`.
- The user signals enough.

Never invent new abstractions while pruning. Never weaken or delete tests to make a deletion typecheck — that hides regressions instead of preventing them.
