# Stack-Native Idiom

Use what the stack already gives you. If a tool offers a feature, prefer it over a hand-rolled lookalike. Reinvention is debt.

The examples below assume a common web stack — React + a data-fetching library (TanStack Query) + a typed API client + an ORM + Tailwind and a component library (shadcn-style) + a shared utilities package. Translate each to whatever your project actually uses; the heuristics do not depend on the specific tools.

## Smells

- **New CSS color** when an existing token already names it (`#a60202` instead of `var(--brand)`).
- **Conditional `className` strings** when `data-*` variants or `cva` would be cleaner and re-usable.
- **Hand-rolled spinner / skeleton** when your component library's `Skeleton` and empty-state primitives exist.
- **Custom hook wrapping a query** that just forwards args — adds a layer that hides the contract.
- **Re-validating already-validated input** inside a backend handler after the API contract validated it on the wire.
- **Manual `fetch` with hand-typed response** instead of the typed API client's call.
- **An effect to derive state** when the value is a pure function of props/state.
- **Imperative navigation for a static link** when a `<Link>` works (and gives prefetch and a11y for free).
- **New date/format helper** when the shared package already exports one.
- **Reimplementing `cn()`** or class-merge logic instead of the util your UI package already exports.
- **Custom dropdown / dialog / tooltip** when component-library primitives exist.
- **New Button color** instead of adding/using a `Button` variant.
- **`useState` + an effect for URL state** when search params are the source of truth.
- **`useState` to mirror server data** when the query cache already holds it.
- **Custom permission checks** scattered around when a single `hasPermission(role, resource, action)` helper is the source of truth.

## Heuristics

- **Search the tool's docs first.** Before writing a helper, check whether your data-fetching library / ORM / CSS framework / component library / API client already exposes the behavior. Most "I need a wrapper" feelings dissolve in a `select`, an `enabled`, a `data-*` variant, or a `cva` variant.
- **Tokens over hex.** Any color already in your theme/stylesheet is the answer. New tokens go there, not inline.
- **Variants over conditionals.** If the conditional class set will be used twice, it is a variant, not three nested ternaries at every call site.
- **Contracts over re-validation.** The API contract validates input on the wire; the handler trusts the parsed input.
- **Shared helpers over per-app copies.** The shared and UI packages are the home for cross-app code. New helper? Check both before creating one.

## Examples

### Use existing CSS variables

DON'T:

```tsx
<div className="bg-[#a60202] text-white hover:bg-[#8a0101]">…</div>
```

DO:

```tsx
<div className="bg-brand text-white hover:bg-brand-hover">…</div>
```

If `--brand` and `--brand-hover` are already defined in your global stylesheet, the framework turns the CSS variable into a utility. New brand shade? Add it to the stylesheet once, use the utility everywhere.

### `data-*` variants over conditional class strings

DON'T:

```tsx
<button
  className={cn(
    "px-3 py-2 rounded",
    isActive ? "bg-brand text-white" : "bg-neutral text-muted",
    isActive ? "border-brand" : "border-default",
  )}
>
```

DO:

```tsx
<button
  data-active={isActive ? "true" : undefined}
  className={cn(
    "px-3 py-2 rounded border",
    "bg-neutral text-muted border-default",
    "data-[active=true]:bg-brand data-[active=true]:text-white data-[active=true]:border-brand",
  )}
>
```

For multi-variant components (size + tone + state), reach for `cva` (class-variance-authority) or your library's equivalent.

### Use `<Link>` for navigation

DON'T:

```tsx
<button onClick={() => router.push(`/orders/${id}`)}>
  …
</button>
```

DO:

```tsx
<Link href={`/orders/${id}`} prefetch className={…}>
  …
</Link>
```

`<Link>` gives prefetch, keyboard support, middle-click, and screen-reader semantics. Reach for imperative navigation only when it is a side effect of a non-link action (after a mutation, after a confirm dialog, etc.).

### Use component-library variants instead of new buttons

DON'T:

```tsx
<button className="bg-brand text-white px-4 py-2 rounded hover:bg-brand-hover">
  Save
</button>
```

DO:

```tsx
<Button variant="brand">Save</Button>
```

Need a new tone? Add a variant to the shared `Button` once. Every caller benefits.

### Use query options instead of wrapper hooks

DON'T:

```ts
function useOrders(status: OrderStatus | "all") {
  const query = useQuery(api.orders.getList.queryOptions({ input: { status } }));
  return query.data?.items ?? [];
}
```

The wrapper hides the contract, hides loading/error states, and forces every caller to lose them.

DO: call the query at the call site so loading, error, and refetch are visible. Use `select` to shape the result.

```ts
const { data: items = [], isLoading, error } = useQuery({
  ...api.orders.getList.queryOptions({ input: { status } }),
  select: (page) => page.items,
});
```

### Trust the contract; do not re-validate

DON'T:

```ts
@Controller()
export class OrdersController {
  @Post()
  create(@Body() body: unknown) {
    const parsed = createOrderSchema.parse(body); // already done at the contract boundary
    …
  }
}
```

DO: rely on the API contract's input. The handler signature is the parsed type.

### Reuse shared helpers

DON'T: write a new `formatDate` in one app when the shared package already exports `formatRelativeTime`, `formatCurrency`, etc.

DO: import from the shared package. If the helper does not yet exist and ≥2 apps would consume it, add it there (rule of three for stand-alone helpers; rule of two when both apps clearly need the same behavior).

### URL as the source of truth for filters

DON'T:

```ts
const [status, setStatus] = useState<OrderStatus>("pending");
const [page, setPage] = useState(1);
// …also stored in a global store for "convenience"
```

DO: use search params. Filter UI reads/writes them, the server fetch keys off them, back/forward and refresh round-trip them, deep-links work, and "View all → filtered list" works for free (see `LABEL-TRUTH.md`).

```ts
const params = useSearchParams();
const status = (params.get("status") ?? "pending") as OrderStatus;
```

### Use `hasPermission`, not role string equality

DON'T:

```ts
if (user.role === "admin" || user.role === "editor") {
  // show button
}
```

DO:

```ts
if (hasPermission(user.role, "orders", "approve")) {
  // show button
}
```

A central role-permissions module is the single source of truth. Magic role checks drift; the helper does not.

## Decision shortcut

1. The thing I am about to write — does the stack already do it? Search your UI package, shared package, and the tool's docs.
2. Is this a CSS color, spacing, radius, or shadow? Use a token from the theme. Missing? Add it once.
3. Is this a conditional class set? `data-*` variant or `cva`. Two callers ⇒ extract.
4. Is this a query wrapper? Inline the call; use `select` for shape.
5. Is this re-validating server data? Drop it; trust the contract.
6. Is this a role check? Replace with `hasPermission`.
