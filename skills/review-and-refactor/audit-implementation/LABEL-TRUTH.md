# Label-Truth

A control's visible text is a contract with the user. Honor it or change the control. Never relabel to fit a buggy implementation.

## Smells

- **Half-truth navigation** — "Pending Orders" card or "View all" link goes to the unfiltered list page instead of the filtered list.
- **Filter-dropping redirect** — clicking a filtered widget item navigates somewhere that loses the user's current filter/sort/page.
- **Hidden side-effect button** — "Save" that closes the dialog without persisting; "Edit" that opens a read-only view; "Delete" that only soft-archives without saying so.
- **Plural/singular drift** — "1 Pending Orders", "0 Items selected" instead of "1 Pending Order", "No items selected".
- **Disabled without reason** — a disabled button with no tooltip, `aria-disabled`, or helper text explaining why.
- **CTA mismatch on empty state** — "Add your first booking" button that opens an unrelated form, or no action at all.
- **Tab/route asymmetry** — tab label "Active" maps to a route or query state that does not actually filter to active.
- **Count mismatch** — badge says "5 pending" but the destination shows 4 because the destination uses a different cutoff (e.g., today vs. last 7 days) than the count source.
- **Role-blind label** — an action shown to a role whose permission check will reject it.
- **Unconditional action buttons** — action buttons (edit, delete, approve, reject, etc.) that render without checking permission for the specific resource/action, leading to permission errors on click or disabled states without explanation.

## Heuristics

- **Click-and-read.** Click the control, read the label out loud, look at the destination. Do they describe the same thing? If not, the implementation is lying.
- **Filter survives navigation.** A filtered widget's "View all" passes the filter as a search param the destination respects. If it does not, fix the destination first.
- **Counts share a source.** The number on the card and the number of rows you land on come from the same query/predicate, not two queries that drift.
- **Disabled is documented.** If a control can be disabled, its disabled state has a reason the user can see (`title`, tooltip, helper text, `aria-describedby`).
- **Permission-aware rendering.** A control whose action will be rejected by a permission check should not render — not render-then-error.

## Examples

### Half-truth "View all"

DON'T:

```tsx
// Widget renders only pending orders, but "View all" drops the filter.
<DashboardWidgetShell
  title="Pending Orders"
  viewAllHref="/orders"
>
```

DO:

```tsx
<DashboardWidgetShell
  title="Pending Orders"
  viewAllHref="/orders?status=pending"
>
```

If `/orders` does not yet honor `?status=pending`, **change the list page to honor it** (read the search param, seed the filter store, persist on navigation). Do not change the widget title to "All Orders" to make the lie consistent.

### Filter-dropping row click

DON'T:

```tsx
// User filtered to "this week" then clicked a row; detail page back-button
// returns to the unfiltered list.
<button onClick={() => router.push(`/orders/${id}`)}>
```

DO: navigate with the source filter preserved, or use the URL as the source of truth so back navigation restores it.

```tsx
<Link href={`/orders/${id}`} prefetch>
  …
</Link>
```

Pair with URL-driven filter state on `/orders` (search params), so back/forward and refresh round-trip the filter. The browser already gives you this — do not reinvent it with sessionStorage.

### Hidden side-effect button

DON'T:

```tsx
<Button onClick={() => setOpen(false)}>Save</Button>
```

DO:

```tsx
<Button
  onClick={async () => {
    await mutate.mutateAsync(values);
    setOpen(false);
  }}
  disabled={mutate.isPending}
>
  {mutate.isPending ? "Saving…" : "Save"}
</Button>
```

### Plural/singular drift

DON'T:

```tsx
<span>{count} Pending Orders</span>
```

DO: use a `pluralize` helper if the project has one, or inline the conditional. The label always reads correctly for `0`, `1`, and `n`.

```tsx
<span>{count === 1 ? "1 Pending Order" : `${count} Pending Orders`}</span>
```

### Disabled without reason

DON'T:

```tsx
<Button disabled={!canApprove}>Approve</Button>
```

DO:

```tsx
<Tooltip>
  <TooltipTrigger asChild>
    <span>
      <Button disabled={!canApprove} aria-describedby="approve-reason">
        Approve
      </Button>
    </span>
  </TooltipTrigger>
  {!canApprove ? (
    <TooltipContent id="approve-reason">
      Only an admin can approve this order.
    </TooltipContent>
  ) : null}
</Tooltip>
```

Better yet: if `hasPermission(role, "orders", "approve")` is false, do not render the button at all. The disabled state is for transient reasons (loading, validation), not for missing permissions.

### Unconditional action buttons

DON'T:

```tsx
// Action button renders for all roles, but only an admin can actually perform it.
<Button onClick={() => handleApprove()}>
  Approve
</Button>

// Or worse: renders disabled without explanation, leaving the user confused.
<Button disabled={!isAdmin}>
  Approve
</Button>
```

DO:

```tsx
// Check permission before rendering the button at all.
const canApprove = hasPermission(role, "orders", "approve");

{canApprove && (
  <Button onClick={() => handleApprove()}>
    Approve
  </Button>
)}
```

Apply this pattern to all action buttons: edit, delete, approve, reject, assign, complete, archive, etc. A central permission helper is the single source of truth for authorization — do not duplicate role checks with hardcoded role arrays or inline comparisons.

### Count mismatch

DON'T: card uses `getOrders({ status: "pending", limit: 5 })` to show `total`, but `/orders?status=pending` uses a different default range (e.g., last 30 days) — the user lands on a list with fewer rows than the count promised.

DO: card and destination read the same predicate. Either the source query mirrors the destination's defaults, or the destination accepts the source's predicate via search params and applies it on first paint.

## Decision shortcut

1. Read the label. State its promise in one sentence.
2. Click it. Did it deliver that exact thing? If no — fix the destination, the filter handoff, or the side-effect.
3. Is it sometimes disabled? Is the reason visible to the user? If no — add `aria-describedby`/tooltip, or hide the control entirely if the reason is permission-based.
4. Does it carry a number? Does the destination land on the same number? If no — share the predicate.
