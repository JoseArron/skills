# Type Narrowing

Redundant runtime checks the type system already proves, casts that restate inference, and double-validation of already-validated data.

Examples are TypeScript, but the principle — never re-check what the type system already guarantees — holds in any statically-typed language (Rust, Kotlin, Swift, C#, Go). The trust-boundary exception is universal too.

## Smells

- `?.` on a property typed as required.
- `!` non-null assertion stacked on top of a guard that already narrows.
- Double null checks: `if (user && user.id)` when `user.id` is non-nullable on `User`.
- `as Foo` casts that restate what TS already infers, or fight the type instead of fixing it.
- `typeof x === "string"` when `x: string`.
- Re-parsing data with the same Zod / Valibot / Yup schema it was already parsed with upstream.
- `if (x !== undefined && x !== null)` when `x` is non-nullable.
- Defaulting a value the type guarantees: `value ?? defaultValue` when `value` is not nullable.
- `JSON.parse(JSON.stringify(x))` to "make sure" — usually wrong, almost never needed.
- Boolean coercion inside an `if` branch where the variable is already boolean.

Keep the check when the value crosses a real trust boundary: network, storage, user input, `JSON.parse`, `process.env`, `localStorage`, deeply third-party SDK.

## Examples

### Optional chaining on a required field

DON'T:

```ts
type User = { id: string; name: string };
function greet(u: User) {
  return `Hi ${u?.name ?? "guest"}`;
}
```

Why: both `u` and `u.name` are required. The `?.` and `??` lie about the contract and hide bugs at the real callsite that passes `undefined`.

DO:

```ts
function greet(u: User) {
  return `Hi ${u.name}`;
}
```

If callers actually pass `undefined`, fix the type to `User | undefined` and handle it once at the boundary.

### Redundant guard after narrowing

DON'T:

```ts
if (typeof v === "string") {
  if (v) doThing(v as string);
}
```

Why: inside the first branch TS already knows `v: string`. The cast is noise; the truthiness check should say what it actually means.

DO:

```ts
if (typeof v === "string" && v.length > 0) {
  doThing(v);
}
```

### Defensive null check that should be a contract

DON'T:

```ts
function format(date: Date | undefined) {
  if (!date) return "—";
  return date.toISOString();
}
```

Sometimes correct — but if every caller already guarantees `date`, the check is cruft and the type is wrong.

DO:

```ts
function format(date: Date) {
  return date.toISOString();
}
```

Handle the missing case at the one place it actually arises (e.g. the row that renders `"—"`).

### Re-validating already-validated data

DON'T:

```ts
const parsed = UserSchema.parse(input);
const safe = UserSchema.parse(parsed);
```

Why: the second parse cannot fail; it only burns CPU and obscures intent.

DO:

```ts
const user = UserSchema.parse(input);
```

### Cast that fights inference

DON'T:

```ts
const ids = users.map((u) => u.id) as string[];
```

Why: TS already infers `string[]`. The cast is a smell; if the inferred type is wrong, fix the source type.

DO:

```ts
const ids = users.map((u) => u.id);
```

### `??` on a non-nullable

DON'T:

```ts
const name: string = user.name;
const display = name ?? "Anonymous";
```

Why: `name` cannot be nullish — the fallback is unreachable.

DO:

```ts
const display = user.name;
```

If empty string should fall back, say so explicitly: `user.name || "Anonymous"`.

## Decision shortcut

1. Does the static type already exclude the case? → drop the check.
2. Does the value cross a real trust boundary (network, storage, user input, env, JSON.parse)? → keep the check.
3. Is the cast restating what TS already infers, or fighting a wrong type? → drop the cast / fix the source type.
4. Has this data already been validated by the same schema upstream? → drop the second parse.
