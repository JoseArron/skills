# Access Control

The authorization boundary: can _this_ principal perform _this_ action on _this specific_ resource? Authentication proves who you are; authorization decides what you may touch. Most real-world breaches are a missing ownership check, not a broken crypto primitive.

## Smells

- **IDOR (Insecure Direct Object Reference)** — a handler loads a resource by an id from the request and returns it without checking the caller owns it. `GET /invoices/123` returns invoice 123 to anyone logged in.
- **Horizontal escalation** — user A reaches user B's resource at the same privilege level (another user's order, message, file).
- **Vertical escalation** — a regular user reaches an admin-only action because the check lives only in the hidden UI, not the endpoint.
- **Mass assignment** — the handler spreads the whole request body into a model, letting the client set fields it should never control (`role`, `isAdmin`, `ownerId`, `balance`).
- **Route-level-only checks** — middleware confirms the user is _logged in_ but never that they own the _specific_ row the handler then loads.
- **Tenant bleed** — a multi-tenant query filters by id but not by `orgId`, so a member of org A reads org B's row.
- **Sequential ids as the only guard** — guessable `/users/1`, `/users/2` ids where obscurity was doing the access-control job.
- **Stale access** — a user removed from an org, or a deactivated account, keeps working tokens/sessions until they expire.
- **Parent-child gap** — the caller owns the parent but the action targets a child the check never re-validated (owns the post, edits a comment under it that belongs to someone else).

## Heuristics

- **Check ownership at the data layer.** The authorization predicate belongs in the query (`WHERE id = ? AND owner_id = ?`) or immediately after the load — not at the router, where a second handler can skip it.
- **Every id from the client is hostile.** For each request-supplied id, ask: what stops me from putting _someone else's_ id here? If the answer is "the UI doesn't show it," that is not an answer.
- **Allowlist writable fields.** A write accepts an explicit set of fields; it never trusts the body's shape.
- **Re-check after privilege changes.** A role or membership change invalidates cached authorization — re-validate on the next request, do not trust a token minted under the old role.
- **Revoke on lifecycle events.** Removal from an org or account deactivation invalidates sessions and API keys _now_, via a revocation list or short-lived tokens, not "whenever the JWT expires."
- **Use non-guessable ids** (UUIDv4 or similar) for anything reachable by id, unless the user explicitly wants sequential ids. Non-guessability is defense in depth, never the primary control — the ownership check is.

## Examples

### IDOR — load then authorize

DON'T:

```python
# Any authenticated user can read any invoice by guessing the id.
def get_invoice(invoice_id, user):
    return db.invoices.find(invoice_id)
```

DO:

```python
def get_invoice(invoice_id, user):
    invoice = db.invoices.find(invoice_id)
    if invoice is None or invoice.owner_id != user.id:
        if not user.has_org_access(invoice.org_id if invoice else None):
            raise NotFound()   # 404, not 403 — do not confirm the row exists
    return invoice
```

### Mass assignment — spreading the request body

DON'T:

```javascript
// Client sends { name, email, role: "admin" } and becomes an admin.
User.update(userId, req.body);
```

DO:

```javascript
const allowed = ["name", "email", "avatar"];
User.update(userId, pick(req.body, allowed));
```

This applies to every ORM and framework — define which fields a request may modify; never hand the model an unfiltered body.

### Tenant isolation — id without org

DON'T:

```sql
SELECT * FROM documents WHERE id = :id
```

DO:

```sql
SELECT * FROM documents WHERE id = :id AND org_id = :current_org_id
```

The tenant predicate is part of _every_ query against tenant-scoped data, not a separate "and also check the org" step that some handlers forget.

## Decision shortcut

1. List every request that takes a resource id or a writable body.
2. For each: where is the ownership/tenant check, and is it in the query or right after the load? If it is only at the router, it is not enough.
3. For each write: is the set of writable fields an explicit allowlist? If the body is spread in, find the field that escalates.
4. On role removal / account deletion: are existing sessions and tokens revoked immediately? If they ride until expiry, that is the finding.
