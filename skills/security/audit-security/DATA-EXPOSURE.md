# Data Exposure

The confidentiality boundary: secrets and sensitive data reaching somewhere they should never be visible — a JS bundle, a log, an error page, a response field the screen never needed. Nothing here is an "attack" the way injection is; it is data leaking across a line, and the fix is to keep it on the right side.

## Never reaches the client

**Secrets** — third-party API keys (Stripe, AWS, …), database connection strings, JWT signing secrets, encryption keys, OAuth client secrets, internal service URLs and credentials. Any call that needs a secret runs on the server; the browser calls _your_ backend, which holds the secret.

**Sensitive user data** — full card numbers, SSNs, passwords (even hashed), security answers. Send only what the screen renders, and mask the rest server-side (`•••• 1234`) rather than shipping the full value and hiding it in CSS.

**Infrastructure detail** — internal IPs, DB schemas, dependency versions, debug flags, and stack traces. These hand an attacker a map.

## Where secrets hide

Check these — a secret "removed from the UI" often survives in:

- JS bundles and their source maps
- HTML comments, hidden form fields, `data-*` attributes
- `localStorage` / `sessionStorage`
- SSR hydration / initial-state blobs
- Build-time public env vars (`NEXT_PUBLIC_*`, `REACT_APP_*`) — anything with a public prefix ships to the browser; a secret with that prefix is exposed by definition.

## Heuristics

- **Secrets live in the environment, used server-side only.** `.env` (git-ignored) on the server; never inlined into client code or a public-prefixed var.
- **Send the minimum.** An API response carries the fields the view uses, not the whole row. Over-fetching is a leak waiting for a client bug to expose it.
- **Errors are generic to the user, detailed in the log.** The user sees "Something went wrong"; the stack trace, query, and ids go to server logs only.
- **Mask server-side.** Truncate or redact before the value leaves the server, not in the client.
- **Enforce transport.** HTTPS everywhere, with HSTS so the browser refuses to downgrade.

## Security headers

The transport- and exposure-related response headers (the XSS/clickjacking set lives in [XSS.md](XSS.md)):

```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Referrer-Policy: strict-origin-when-cross-origin
Cache-Control: no-store          # on responses with sensitive data
```

`no-store` on sensitive responses keeps them out of shared caches and the browser's back/forward cache.

## API over-exposure

Two server-side leaks that hide in otherwise-normal endpoints:

- **GraphQL** — disable introspection in production, and bound query **depth**, **complexity/cost**, and **batch size** so a single request cannot walk or hammer the graph.

  ```javascript
  new ApolloServer({
    introspection: process.env.NODE_ENV !== "production",
    validationRules: [depthLimit(10), costAnalysis({ maximumCost: 1000 })],
  });
  ```

- **Verbose serializers** — a `SELECT *` piped into the response, or an ORM model serialized whole, ships columns (password hash, internal flags, soft-delete metadata) the client never asked for. Serialize an explicit field set.

## Decision shortcut

1. Grep the client bundle and SSR state for anything secret-shaped (keys, tokens, connection strings). Any hit is a finding.
2. For each public-prefixed env var: is its value actually safe to publish?
3. For each API response: does it carry fields the screen never renders? Trim to the view's needs.
4. Trigger an error: does the user-facing message leak a stack trace, query, or internal id?
5. Is HSTS set, and is `Cache-Control: no-store` on sensitive responses?
