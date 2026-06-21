# Over-engineering

Abstractions, options, and optimizations added for futures that did not arrive.

## Smells

- **Single-implementation interface** — one `IFooService` with one `FooService` implementing it. The interface costs vocabulary; the implementation does the work.
- **Factory of one** — `createFoo()` that always returns the same shape with no varying inputs.
- **Wrapper function** (or hook/component) that only forwards its args with no added behavior.
- **Generic with one type argument** ever passed in practice.
- **Config object with knobs nobody flips.** Each unused option is a future bug surface.
- **Premature port + adapter** for a dependency with one transport in production and no test stand-in yet.
- **Abstract base class** with one subclass.
- **Custom event bus / pub-sub** wrapping a direct function call.
- **Indirection layer** between caller and library that adds no invariant — just renames methods.
- **Pre-emptive splitting** of a small, cohesive function into many "single-responsibility" helpers that are only called in sequence.
- **Micro-optimizations without measurement** — manual loop unrolling, `for` over `map` "because faster", regex re-compiled per call concerns where there is no profile evidence.
- **Caching layers without a measured cache-hit rate or eviction policy.**
- **Custom error classes** for cases nobody catches differently.

## Heuristics

- **Rule of three.** Don't extract until three concrete callers exist (not two — two can still diverge or be merged).
- **Deletion test.** If deleting the abstraction concentrates complexity, it earned its keep. If it just relocates complexity, it was indirection.
- **One adapter is a hypothetical seam. Two is real.** (See [`improve-codebase-architecture`](../improve-codebase-architecture/SKILL.md).)
- **YAGNI on options.** Add a knob only when a real caller needs it differently.
- **Profile, don't guess.** Optimization without a measurement is decoration.

## Examples

### Single-impl interface

DON'T:

```ts
export interface OrderRepository {
  findById(id: string): Promise<Order | null>;
}
export class PrismaOrderRepository implements OrderRepository { ... }
```

when the Prisma impl is the only one and tests use the real DB or PGLite.

DO:

```ts
export class OrderRepository { ... }
```

Re-introduce the interface only when a second adapter is actually written.

### Factory of one

DON'T:

```ts
export function createLogger() {
  return { info: console.log, warn: console.warn, error: console.error };
}
```

DO: export the object directly, or just use `console`. Re-introduce the factory when at least one caller needs a different config.

### Wrapper hook

DON'T:

```ts
export function useUserSession() {
  const session = useSession();
  return session;
}
```

DO: callers use `useSession` directly until you actually add behavior on top.

### Premature generic

DON'T:

```ts
function pickFirst<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

when every caller passes `string[]`.

DO: keep the generic only if the caller set is genuinely heterogeneous; otherwise specialize.

### Unused config knob

DON'T:

```ts
type Options = { compact?: boolean; legacyHeader?: boolean; verbose?: boolean };
function render(opts: Options = {}) { ... }
```

when `legacyHeader` and `verbose` are never set anywhere.

DO: delete the unused fields and any branches reading them.

### Custom event bus over a function call

DON'T:

```ts
const bus = new EventBus();
bus.on("user:created", handler);
// elsewhere
bus.emit("user:created", user);
```

when `emit` and `on` happen in the same module with one listener.

DO:

```ts
handler(user);
```

### Unmeasured "optimization"

DON'T:

```ts
// "faster than .map"
const ids: string[] = [];
for (let i = 0; i < users.length; i++) ids.push(users[i].id);
```

DO:

```ts
const ids = users.map((u) => u.id);
```

If a profile actually shows this hot, optimize then — with the profile in the PR description.

### Cache without a hit-rate

DON'T: add an LRU cache around a function "to be safe" with no measurement of how often it is called with the same args, no TTL, no invalidation strategy.

DO: leave the call direct. Add a cache when there is a measured repeat-call rate and a clear eviction rule.

## Decision shortcut

1. Does the abstraction have ≥2 real consumers today? If no → inline.
2. Does removing it duplicate non-trivial logic across callers? If no → inline.
3. Is the optimization backed by a profile or measurement? If no → revert to the simple version.
4. Does the option / knob have a caller that flips it? If no → delete it.
