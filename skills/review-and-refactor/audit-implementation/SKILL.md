---
name: audit-implementation
description: Audit a feature implementation across four axes — label-truth (controls do exactly what their label says), fetch & query shape (every query is justified, deduplicated, and consistent with siblings), stack-native idiom (use what the stack already gives you), and misused tools (tools used against their grain — DB views as a "speed-up", effects for derived state). Use when implementing a feature, opening a PR, or asked to "verify this is justified", "does this button do what it says", "are we using X right", "is this query needed". Escalates big architectural calls to an ADR.
---

# Audit Implementation

Verify a feature actually does what it claims, fits the stack idiomatically, and earns its complexity. Default is the simplest stack-native path; anything else must justify itself with a real, current reason.

Examples lean on a web stack (React + a data-fetching library + an ORM) because that is where these smells cluster, but the four axes apply to any stack — swap the tool names for whatever yours provides.

## Glossary

- **Label-truth** — the visible action navigates or mutates exactly what the user reads. "Pending Orders" → list filtered to pending, not the unfiltered list.
- **Justified query** — a fetch whose shape, freshness, and key are explained by what the screen renders today; not "in case", not "for symmetry".
- **Stack-native** — uses what the chosen tool already provides (CSS variables, `data-*` variants, your data-fetching library's options, your ORM's relation includes, your API contract's input validation, component-library variants) instead of a hand-rolled equivalent.
- **Misused tool** — a tool used for the wrong job. Looks load-bearing, actually adds friction without paying back.
- **Earns its keep** — has a real current caller, a measured win, or a documented invariant. Hypotheticals do not count.

## Axes

Each axis has a detail file with heuristics and do/don't examples. **Read the relevant file before classifying a finding** — the heuristics are the citation, not vibes.

- **Label-truth** — buttons, links, tabs, kebab menu items, summary cards, "View all", empty-state CTAs must navigate or filter to exactly what the label promises. See [LABEL-TRUTH.md](LABEL-TRUTH.md).
- **Fetch & query shape** — every query is justified, sized to the screen, consistent with sibling queries (cache keys, `staleTime`, `enabled`, invalidation targets), and not refetching what a parent already has. See [FETCH-AND-QUERY.md](FETCH-AND-QUERY.md).
- **Stack-native idiom** — prefer existing capabilities (CSS variables, `data-*` attribute variants, data-fetching options, ORM relation includes, API contracts, shared helpers, design-system variants) over hand-rolled lookalikes. See [STACK-NATIVE.md](STACK-NATIVE.md).
- **Misused tool** — flag tools used against their grain (DB views as a "performance optimization", effects for derived state, refs for state that affects render, transactions around read-only queries). See [MISUSED-TOOLS.md](MISUSED-TOOLS.md).

## Principles

- **The label is a contract.** If the implementation cannot honor it, change the implementation, not the label. Half-truth labels mislead — guide the user, do not mislead them.
- **One query, one purpose.** Two siblings fetching the same data with different keys is a bug, not a coincidence.
- **Default to inline.** Reach for an abstraction or new variable only when the stack does not already give you the same thing.
- **Measure before optimizing.** No DB views, caches, indexes, or memoization without a measurement that justifies them.
- **Auditing removes or simplifies. It does not redesign.** If a finding wants a new abstraction, escalate to `improve-codebase-architecture`. If it wants deletion, escalate to `prune-cruft`.

## Process

### 1. Scope

Name the surface: a route, a feature slice, a PR, or a single component/widget. Do not boil the ocean — bounded surface so findings stay reviewable in one pass.

### 2. Walk the four axes

In order — label-truth, fetch-query, stack-native, misused-tool. For every finding record:

- **Where** — `@absolute/path:start-end`
- **Axis** — label-truth / fetch-query / stack-native / misused-tool
- **Smell** — one line citing the heuristic from the axis detail file
- **Stack-native fix** — what the existing stack already provides
- **Risk** — none / behavior change / data-shape change / contract change / needs design call

When a finding is ambiguous, prefer "needs callsite check" over a guess. For dynamic lookups, generated code, and cross-package exports, verify across the whole codebase.

### 3. Present, then act

Group by axis, highest confidence first. Do **not** bulk-apply yet. Ask the user which findings to action.

For each approved fix, apply the minimal stack-native change. **If honoring the label requires changing the target page or contract** (e.g., a list page that does not accept the filter the source button promises), change the target — never paper over with a half-truth label or a redirect that drops state.

After each cluster:

- Run the project's typecheck or build (e.g. `tsc --noEmit`, or the per-package equivalent in a monorepo).
- Run lint / formatter on touched files.
- For UI changes, name the route(s) the user should re-click to verify.
- For query changes, name the screens that should re-render and the cache keys that should invalidate.

### 4. Record the architectural calls

If a finding required a real architectural decision (replacing a DB view with a query, changing a contract input, dropping a pattern across an app), record it as an ADR in `docs/adr/` (see `domain-modeling`'s `ADR-FORMAT.md`). Skip ADR entries for ephemeral, obvious, or purely local fixes — only record decisions a future reviewer would otherwise re-litigate.

## Stop conditions

Stop when:

- Remaining findings are load-bearing or contested.
- A finding wants a redesign — escalate to `improve-codebase-architecture`.
- A finding wants a deletion sweep — escalate to `prune-cruft`.
- The user signals enough.

Never invent abstractions while auditing. Never silence a finding by weakening tests or adding casts. Never re-label a control to fit a buggy implementation.
