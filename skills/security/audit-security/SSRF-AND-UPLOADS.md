# Untrusted URLs & Uploads

The untrusted-resource boundary: the server fetches a URL, redirects a user to one, or accepts a file — none of which it originated. URL handling (SSRF, open redirect) shares one root cause: a parser disagrees with your validation about what a URL means. Uploads add a second: a blob that claims to be one type and behaves as another.

## SSRF (Server-Side Request Forgery)

The server makes a request to a URL the user supplied or influenced, and an attacker points it at internal services or cloud metadata.

**Vulnerable features:** webhooks (user-provided callback), URL previews, "import from URL", PDF/image generators that fetch URLs, RSS/feed readers, proxy endpoints, any integration with a user-supplied endpoint.

**Defense:**

1. **Allowlist destinations** where possible — only pre-approved domains.
2. **Resolve DNS, then validate the resolved IP** is not private/internal/link-local before connecting, and **pin that IP** for the request so it cannot re-resolve.
3. **Block cloud metadata explicitly** — `169.254.169.254` (AWS/GCP/Azure/DO), `metadata.google.internal`.
4. Scheme allowlist (http/https only), disable or validate redirects hop-by-hop, set timeouts and a response-size cap, and isolate the fetcher at the network layer.

**IP/DNS bypasses to block** — a denylist of `127.0.0.1`/`localhost` strings is not enough:

| Technique              | Example                                     | Why it works                   |
| ---------------------- | ------------------------------------------- | ------------------------------ |
| Decimal IP             | `http://2130706433`                         | 127.0.0.1 as a decimal         |
| Octal / hex IP         | `http://0177.0.0.1`, `http://0x7f.0.0.1`    | Alternate radixes              |
| IPv6 loopback / mapped | `http://[::1]`, `http://[::ffff:127.0.0.1]` | Bypasses IPv4 checks           |
| Shortened IP           | `http://127.1`                              | Expands to 127.0.0.1           |
| DNS rebinding          | resolves external, then internal            | TOCTOU between check and fetch |
| CNAME to internal      | attacker domain → internal host             | DNS points inward              |
| Parser confusion       | `http://attacker.com#@internal`             | Libraries disagree on the host |
| Redirect to internal   | external 302 → internal                     | Each hop must be re-validated  |

**DNS rebinding** specifically: resolve once, validate the IP, and connect to _that pinned IP_ — do not let the stack re-resolve between your check and the request.

## Open redirect

An endpoint takes a URL/path and redirects to it, letting an attacker bounce victims to a malicious site under your domain's trust (phishing, OAuth token theft).

**Defense, best first:**

1. **Relative paths only** — accept `/dashboard`, reject anything with a scheme or `//`.
2. **Indirect map** — `?next=dashboard` → look up `/dashboard`, never redirect to a raw URL.
3. **Host allowlist** — if absolute URLs are unavoidable, parse and check the host against an allowlist; convert to Punycode first to defeat IDN homographs (`legіt.com` with a Cyrillic і).

**Bypasses to block** (the same parser-confusion family as SSRF):

| Technique              | Example                                |
| ---------------------- | -------------------------------------- |
| `@` in authority       | `https://legit.com@evil.com`           |
| Backslash              | `https://legit.com\@evil.com`          |
| Protocol-relative      | `//evil.com`                           |
| Double-encoded slashes | `%252f%252fevil.com`                   |
| Scheme abuse           | `javascript:…`, `data:text/html,…`     |
| Whitespace/null        | `https://legit.com%09.evil.com`, `%00` |
| Fragment trick         | `https://legit.com#@evil.com`          |

## File upload

An uploaded file must be validated on type, content, and size — and served so it can never execute.

**Validate (never one check alone):**

- **Type** — extension against an allowlist _and_ magic-byte signature matching the claimed type. MIME from the client is a hint, not proof.
- **Content** — re-process images through an image library (rejects malformed/polyglot files); for documents, parse with external entities disabled (see [INJECTION.md](INJECTION.md)).
- **Size** — server-side maximum, mirrored in the proxy/web-server config.

**Bypasses to block:**

| Attack                  | Example                          | Prevention                         |
| ----------------------- | -------------------------------- | ---------------------------------- |
| Double / fake extension | `shell.php.jpg`, `shell.jpg.php` | Single extension, allowlist        |
| Null byte               | `shell.php%00.jpg`               | Reject null bytes in the name      |
| MIME spoofing           | Content-Type lies                | Verify magic bytes                 |
| Magic-byte prefix       | valid header + payload           | Parse the whole file as its type   |
| Polyglot                | valid JPEG _and_ JS              | Re-encode; reject if parse fails   |
| SVG with script         | `<svg onload=…>`                 | Sanitize or disallow SVG           |
| XXE via DOCX/XLSX       | XML inside the upload            | Disable external entities          |
| Zip slip                | `../../etc/passwd` in archive    | Validate every extracted path      |
| Filename injection      | `; rm -rf /` in the name         | Discard the name; use a random one |

**Magic bytes (hex):** JPEG `FF D8 FF` · PNG `89 50 4E 47 0D 0A 1A 0A` · GIF `47 49 46 38` · PDF `25 50 44 46` · ZIP/DOCX/XLSX `50 4B 03 04`.

**Serve uploads safely:** rename to a random id (discard the original name), store outside the webroot or on a separate domain/CDN, serve with `Content-Disposition: attachment`, `X-Content-Type-Options: nosniff`, and a correct `Content-Type`, and ensure stored files are never executable.

## Decision shortcut

1. Does the server fetch any user-influenced URL? If so: allowlist or resolve-validate-pin, and is metadata IP blocked?
2. Does any endpoint redirect to a user-supplied target? Relative-only or host-allowlist (Punycode-normalized)?
3. For uploads: extension allowlist + magic-byte check + size cap; re-encoded/sanitized; random name; served `nosniff` + `attachment` from outside the webroot.
