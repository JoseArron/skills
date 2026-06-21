# Memoization & Caching

When a memo or cache earns its keep — and when it is noise. The canonical offenders are React's `useMemo`, `useCallback`, and `React.memo`, but the same logic governs any cache: a Vue `computed`, a Python `@lru_cache`, a memoized selector, or a hand-rolled `Map`. The examples below are React (that is where this cruft is epidemic); the decision shortcut at the end is language-agnostic.

## When memoization is justified

- Computation is **expensive** — measured: visible in a profiler, large array transforms, deep traversals, parsing. Not "feels heavy".
- The result's **identity is consumed by something that compares by reference** — a hook dependency (`useEffect`, `useMemo`), a memoized child (`React.memo`, a virtualized row), a `Context` provider value with many subscribers, or an external subscription (event bus, observer, third-party lib).
- A **pure function is called repeatedly with the same arguments** and the call is measurably hot — a real cache with a hit rate, not a guess.

## When memoization is cruft

- Wrapping primitives (`number`, `string`, `boolean`) — there is no identity to preserve.
- Wrapping cheap object/array literals used only by local markup in the same component.
- Wrapping handlers passed to plain DOM elements (`<button onClick={...}>`).
- `useCallback` whose deps include every value the function references — same identity churn, plus overhead.
- `React.memo` on a component whose props change every render anyway (e.g. receives a new inline object).
- `useMemo` whose deps change every render (the cache never hits).
- A cache with no measured hit rate, no eviction, and no key strategy (see also [OVER-ENGINEERING.md](OVER-ENGINEERING.md)).

## Examples

### useMemo on a primitive

DON'T:

```ts
const isAdmin = useMemo(() => role === "ADMIN", [role]);
```

Why: comparison is cheaper than the memo bookkeeping, and the result is a primitive — no identity to preserve.

DO:

```ts
const isAdmin = role === "ADMIN";
```

### useCallback handed to a DOM element

DON'T:

```tsx
const onClick = useCallback(() => setOpen(true), [setOpen]);
return <button onClick={onClick}>Open</button>;
```

Why: `<button>` is not memoized; stable identity buys nothing. `setOpen` from `useState` is already stable.

DO:

```tsx
return <button onClick={() => setOpen(true)}>Open</button>;
```

### useMemo on a derived list rendered once

DON'T:

```ts
const sorted = useMemo(() => items.slice().sort(byName), [items]);
return <List items={sorted} />;
```

Why: sort is cheap for typical UI lists, and `<List>` is not memoized — the output is consumed immediately.

DO:

```ts
const sorted = items.slice().sort(byName);
```

### Memoization that actually pays

DO:

```ts
const onSelect = useCallback((id: string) => {
  selectItem(id);
}, [selectItem]);

useEffect(() => {
  bus.subscribe("select", onSelect);
  return () => bus.unsubscribe("select", onSelect);
}, [onSelect]);
```

Why: `onSelect` is a dep of `useEffect`. Without `useCallback`, the effect resubscribes on every render. The same justification holds outside React — stabilize an identity only when something downstream compares by reference.

### React.memo with unstable props

DON'T:

```tsx
const Row = React.memo(function Row({ user, options }: Props) { ... });

<Row user={user} options={{ compact: true }} />
```

Why: a fresh `options` object every render defeats the memo. Either lift the literal out, memoize it, or drop `React.memo`.

DO: lift the literal:

```tsx
const ROW_OPTIONS = { compact: true } as const;
<Row user={user} options={ROW_OPTIONS} />
```

## Decision shortcut

Ask in order. First "no" wins → remove the memoization or cache.

1. Is the cost measured (profiler / >1ms / re-render storm / a real hit rate)?
2. Is the identity or cached result actually consumed by something that compares by reference (memoized child, hook dep, context value, external subscription)?
3. Are the deps / keys stable enough that the cache actually hits more than once?
