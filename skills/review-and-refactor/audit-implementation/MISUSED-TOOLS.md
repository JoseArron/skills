# Misused Tools

Tools used against their grain. They look load-bearing, they add complexity, and a simpler use of the existing stack would do the same job — usually faster and clearer.

Examples mix a Postgres/ORM backend and a React frontend because that is where these crop up most; the principle — don't use a tool against its grain — is universal. Map each one to your stack's equivalent.

## Smells

- **DB views as a "speed-up"** — a regular `VIEW` (not `MATERIALIZED VIEW`) is just a saved query. It does not cache results, it does not pre-compute. Using one for "performance" without an index strategy is theatre. Worse, it hides the join shape from the ORM so changes ripple through SQL files outside the schema.
- **DB views to avoid writing an ORM query** — the ORM's relation include would have produced the same SQL with full type safety.
- **Materialized views without a refresh strategy** — they go stale silently. Every reader sees yesterday's data; nobody knows.
- **Indexes added without `EXPLAIN ANALYZE`** — guessing at indexes adds write cost without confirming a read win.
- **Transactions wrapping read-only queries** — locks for nothing; usually a copy-paste from a write path.
- **`useEffect` for derived state** — recomputing in an effect when the value is a pure function of inputs.
- **`useState` for server data** — duplicates the query cache; goes stale; never invalidates.
- **`useRef` for state that affects render** — the ref mutation does not re-render, the UI lies.
- **`setTimeout` for "wait for the DOM"** — racy. The right hook is `useLayoutEffect` or `requestAnimationFrame` depending on intent.
- **Custom event bus / pub-sub inside one module** — wraps a direct function call.
- **Global store for ephemeral component state** — local `useState` is enough; the store is overhead and a debugging trap.
- **A query primitive for one-shot RPCs** — a mutation is the right primitive; a query with `enabled: false` and manual `refetch` is not.
- **Custom error classes nobody catches** — unique error types only earn their keep when at least one `catch` discriminates on them.
- **Framework interceptor / filter doing the work of a service** — cross-cutting concerns only.
- **Raw SQL for what the ORM already supports** — skips type-safety; usually a sign the author did not find the relation/aggregate API.

## Heuristics

- **Views are saved queries, not caches.** A view's query runs every time. If you wanted caching, you wanted `MATERIALIZED VIEW` + a refresh policy + a staleness contract — and almost always you did not.
- **`EXPLAIN ANALYZE` or it did not happen.** Performance claims need a query plan with row counts before and after.
- **Effects are for the outside world.** Subscriptions, network, DOM, timers. Deriving values is `useMemo` or inline.
- **Server data lives in the query cache.** Local state mirrors of server data drift. Make the cache the source of truth.
- **Refs do not re-render.** If the UI must change, it is `useState`.
- **One adapter is a hypothetical seam.** A pub-sub with one publisher and one subscriber is just a function call.

## Examples

### DB view as fake cache

DON'T: create `order_list_read_v` to "make the list page fast" when the underlying query is one join + one count and no measurement was taken. The view runs the same SQL on every read; you only added a layer the ORM cannot statically reason about.

```sql
CREATE OR REPLACE VIEW order_list_read_v AS
SELECT o.id, o.name, o.status, o.created_at,
       u.full_name AS created_by_name,
       count(i.id)::int AS item_count
FROM "order" o
JOIN "user" u ON u.id = o.created_by
LEFT JOIN order_item i ON i.order_id = o.id
GROUP BY o.id, u.full_name;
```

DO: write the query in the ORM with `include` and `_count`. Index `order(status, created_at desc)` and `order_item(order_id)`. Verify with `EXPLAIN ANALYZE`.

```ts
prisma.order.findMany({
  where: { status },
  include: {
    createdBy: { select: { fullName: true } },
    _count: { select: { items: true } },
  },
  orderBy: { createdAt: "desc" },
  take: limit,
  skip: (page - 1) * limit,
});
```

The ORM query is type-checked end-to-end, the relation appears in the schema, and the SQL is the same shape as the view. If a real perf problem shows up under `EXPLAIN`, escalate to `improve-codebase-architecture` and consider a `MATERIALIZED VIEW` with an explicit refresh trigger — and record the decision as an ADR in `docs/adr/`.

### Materialized view without refresh

DON'T: `CREATE MATERIALIZED VIEW dashboard_summary_v AS …` and read from it forever. The numbers freeze on the day it was created.

DO: if a materialized view is genuinely the right tool, pair it with `REFRESH MATERIALIZED VIEW CONCURRENTLY …` triggered by the right write path or a cron, and document the staleness window the UI promises. Otherwise compute on read.

### `useEffect` for derived state

DON'T:

```tsx
const [fullName, setFullName] = useState("");
useEffect(() => {
  setFullName(`${first} ${last}`);
}, [first, last]);
```

DO:

```tsx
const fullName = `${first} ${last}`;
```

Or `useMemo` only if the derivation is provably expensive (after measuring).

### `useState` mirror of server data

DON'T:

```tsx
const [orders, setOrders] = useState<Order[]>([]);
useEffect(() => {
  fetch("/api/orders").then(r => r.json()).then(setOrders);
}, []);
```

DO: use a query. The cache is the source of truth; mutations invalidate it.

```ts
const { data: orders = [] } = useQuery({
  ...api.orders.getList.queryOptions({ input: { status: "pending" } }),
  select: (p) => p.items,
});
```

### `useRef` for state that affects render

DON'T:

```tsx
const countRef = useRef(0);
function increment() {
  countRef.current += 1; // UI does not update
}
return <span>{countRef.current}</span>;
```

DO: `useState`.

### `setTimeout` to "wait for the DOM"

DON'T:

```tsx
useEffect(() => {
  setTimeout(() => {
    inputRef.current?.focus();
  }, 0);
}, []);
```

DO: focus inside `useEffect` directly (DOM is committed by the time the effect runs), or `useLayoutEffect` if the focus must happen before paint.

```tsx
useEffect(() => {
  inputRef.current?.focus();
}, []);
```

### Custom event bus inside one module

DON'T:

```ts
const bus = new EventEmitter();
bus.on("order:approved", refresh);
// later, same module
bus.emit("order:approved");
```

DO: call `refresh()` directly. Reach for an event bus only when emitter and listener live in genuinely separate modules with no shared call path.

### Global store for component-local state

DON'T: a global store named `useOrderDialogStore` that holds `isOpen` and `selectedId`, used by exactly one dialog component.

DO: `useState` inside the dialog. A global store is for state read/written across distant subtrees.

### Raw SQL for what the ORM supports

DON'T:

```ts
prisma.$queryRaw`SELECT o.*, u.full_name FROM "order" o JOIN "user" u ON u.id = o.created_by`;
```

DO:

```ts
prisma.order.findMany({
  include: { createdBy: { select: { fullName: true } } },
});
```

Reach for raw SQL only when the ORM genuinely cannot express the shape (recursive CTEs, unusual `lateral` joins, geometry, etc.) — and document why.

## Decision shortcut

1. Tool added "for performance"? Show the `EXPLAIN ANALYZE` before/after. If you cannot, revert.
2. View / materialized view? State the staleness contract and the refresh trigger. If neither exists, replace with an ORM query.
3. `useEffect` setting state that depends only on other state/props? Inline it.
4. `useState` shadowing server data? Replace with a query.
5. `useRef` whose mutation should change UI? Replace with `useState`.
6. Pub-sub / event bus / interceptor / store / class — does it have ≥2 real consumers in different modules? If no, inline it.
