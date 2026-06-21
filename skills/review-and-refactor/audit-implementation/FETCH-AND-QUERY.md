# Fetch & Query Shape

Every fetch is justified by what the screen actually renders. Every cache key is consistent with its siblings. Every `staleTime`, `enabled`, and invalidation is a deliberate call, not a copy-paste.

Examples use TanStack Query and a typed API client (`api.*`), but the heuristics apply to any client-side cache (SWR, Apollo, RTK Query) — substitute your library's equivalent of keys, staleness, and invalidation.

## Smells

- **Refetch of parent data.** A child component re-fetches data the parent already has in cache (or even passes as a prop), with a different key.
- **Drifting cache keys.** `["users"]` here, `["userList"]` there, `["staff"]` over yonder — all returning the same rows. Invalidation hits one and not the others.
- **Over-fetching.** A list endpoint that returns full relations for a card that only needs `id`, `name`, `status`. Or a detail page that pulls a 50-row history just to render "Last updated".
- **Under-fetching ⇒ N+1.** Render loop calls a per-row query (a query inside `.map`) instead of one batched fetch with `include`.
- **Client-side pagination of a server-paginated endpoint.** Or vice versa — fetching all rows and slicing in the browser.
- **Random `staleTime` values.** `30_000` here, `60_000` there, `Infinity` somewhere — none documented, none matched to the data's actual change rate.
- **`refetchOnMount: "always"` paired with `refetchOnWindowFocus: false`.** Inconsistent freshness story; the user sees stale data on focus but fresh on remount, which makes no sense to them.
- **Missing `enabled`.** Query fires with `undefined` inputs, hits the server with garbage, errors, then the user sees a flash of error UI before the real query runs.
- **Mutation that does not invalidate.** Or invalidates the wrong key, or invalidates the world (`invalidateQueries()` with no filter).
- **Manual cache surgery instead of invalidation.** `setQueryData` patches one key but the same data lives under two keys, so the other goes stale.
- **Polling instead of invalidation.** A `refetchInterval` for data that only changes via mutations the same client triggers.
- **Suspense boundary mismatch.** A suspense query for data that is not actually critical to first paint, blocking the shell.

## Heuristics

- **The screen explains the shape.** Look at what is rendered. The query selects exactly those fields plus what is needed for actions, no more.
- **Same data ⇒ same key.** If two surfaces show the same rows, they share a query key (or one is `select`-derived from the other). Otherwise invalidations drift.
- **`staleTime` matches the change rate.** Daily-changing data: minutes. User-mutated data: 0 with explicit invalidation. Real-time data: short polling or websockets.
- **`enabled` guards required inputs.** Never fire a query whose inputs can be `undefined` until they resolve.
- **One mutation, one invalidation set.** Each mutation lists the keys it dirties. The list is exhaustive and tested by clicking through.
- **Pagination lives where the data is.** Server-paginated endpoint ⇒ client renders pages, never re-paginates. Client-only data ⇒ no pagination params on the server.
- **Suspense for shell-blocking data only.** Everything else uses a normal query with skeletons.

## Examples

### Drifting cache keys for the same data

DON'T:

```ts
// widget-A.tsx
useQuery(api.orders.getList.queryOptions({ input: { status: "pending" } }));

// widget-B.tsx — same data, different key shape
useQuery({
  queryKey: ["pending-orders"],
  queryFn: () => fetch("/api/orders?status=pending").then(r => r.json()),
});
```

DO: route everything through the contract-derived key from the typed client. The key is generated from the input, so siblings using the same input share the same cache entry automatically.

```ts
const opts = api.orders.getList.queryOptions({ input: { status: "pending" } });
useQuery(opts); // both widgets call this; both share the cache entry
```

### Refetch of parent data

DON'T:

```tsx
function OrderDetail({ id }: { id: string }) {
  const detail = useQuery(api.orders.getById.queryOptions({ input: { id } }));
  return <Items orderId={id} />;
}

function Items({ orderId }: { orderId: string }) {
  // Fetches the order again just to read its items.
  const order = useQuery(api.orders.getById.queryOptions({ input: { id: orderId } }));
  return <ul>{order.data?.items.map(…)}</ul>;
}
```

DO: pass items down as a prop, or use `select` to derive a slice without a new fetch.

```tsx
const items = useQuery({
  ...api.orders.getById.queryOptions({ input: { id: orderId } }),
  select: (order) => order.items,
});
```

### N+1 inside a map

DON'T:

```tsx
{orders.map((order) => (
  <Row key={order.id} order={order} />
))}

function Row({ order }: { order: OrderSummary }) {
  // One query per row.
  const author = useQuery(api.users.getById.queryOptions({ input: { id: order.createdBy } }));
  return <span>{author.data?.fullName}</span>;
}
```

DO: include the joined data in the list query (the list read model should already do this). If the list returns `createdByName` already, render it directly.

### Random `staleTime`

DON'T:

```ts
useQuery({ ...opts, staleTime: 30_000, refetchOnMount: "always", refetchOnWindowFocus: false });
```

with no comment, on a list that is mutated only via the same client's invalidations.

DO: pick a freshness story per data class and apply it consistently. For mutation-driven data:

```ts
// Pattern: cache forever, invalidate on mutate. Comment the choice once at the
// shared query options helper, not per call site.
useQuery({ ...opts, staleTime: Infinity });
```

For data that drifts independently (other users editing): a small `staleTime` with `refetchOnWindowFocus: true` so coming back to the tab refreshes.

### Missing `enabled`

DON'T:

```ts
const { id } = useParams<{ id?: string }>();
useQuery(api.orders.getById.queryOptions({ input: { id: id! } }));
```

DO:

```ts
const { id } = useParams<{ id?: string }>();
useQuery({
  ...api.orders.getById.queryOptions({ input: { id: id ?? "" } }),
  enabled: Boolean(id),
});
```

### Mutation that does not invalidate

DON'T:

```ts
useMutation({
  ...api.orders.approve.mutationOptions(),
  onSuccess: () => {
    toast.success("Order approved");
  },
});
```

DO: invalidate every list/detail that shows the affected order. Invalidate by the contract's key prefix so all input variants are caught.

```ts
useMutation({
  ...api.orders.approve.mutationOptions(),
  onSuccess: async (_, vars) => {
    await Promise.all([
      queryClient.invalidateQueries({ queryKey: api.orders.getList.key() }),
      queryClient.invalidateQueries({
        queryKey: api.orders.getById.queryOptions({ input: { id: vars.id } }).queryKey,
      }),
    ]);
    toast.success("Order approved");
  },
});
```

### Polling for self-mutated data

DON'T: `refetchInterval: 5_000` on a list whose only mutations are triggered by the same logged-in user. Burns network for nothing.

DO: invalidate on mutation. Add polling only when other actors can change the data and the staleness window matters.

## Decision shortcut

1. What does the screen render from this query? Trim the selection to that.
2. Does another surface render the same data? If yes — share the key, do not duplicate.
3. How does this data change — only by this user, by other users, by time? Pick `staleTime`/`refetchOnWindowFocus` to match.
4. Does the input ever start as `undefined`? Add `enabled`.
5. Every mutation: list the keys it dirties. Invalidate exactly those, no more, no less.
6. Pagination: server or client — pick one, never both.
