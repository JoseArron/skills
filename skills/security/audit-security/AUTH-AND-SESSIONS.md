# Auth & Sessions

The identity boundary: is the requester who they claim to be, is their session still valid, and is this state-changing request something they actually intended? Covers how credentials are stored, how tokens are signed and carried, and how a forged cross-site request is rejected.

## Smells

- **Weak password hashing** — passwords stored with MD5, SHA1, or plain SHA256, or with no per-user salt.
- **Password policy theater** — forced composition rules ("1 upper, 1 symbol") and a low max length that block strong passphrases while doing little against guessing.
- **`alg: none` accepted** — the JWT verifier trusts the algorithm named in the token header, so an attacker sets `none` and strips the signature.
- **Algorithm confusion** — a verifier that accepts both RS256 and HS256 lets an attacker sign with the public key as an HMAC secret.
- **Weak or shared HMAC secret** — a JWT signed with a guessable secret or a password-like phrase instead of 256+ bits of random.
- **No expiry** — tokens without an `exp` claim, or sessions that never time out.
- **Tokens in `localStorage`** — JWTs or session ids in `localStorage`/`sessionStorage`, readable by any XSS.
- **Missing cookie flags** — session cookies without `HttpOnly`, `Secure`, or `SameSite`.
- **No CSRF defense on state change** — a `POST`/`PUT`/`PATCH`/`DELETE` that relies only on an ambient session cookie, so any site can submit it on the user's behalf.
- **Login/reset CSRF** — pre-auth endpoints (login, signup, password reset, OAuth callback) with no CSRF or origin check.
- **State change on GET** — a `GET` that mutates, which sails past CSRF defenses and gets pre-fetched.

## Heuristics

- **Hash with a memory-hard KDF.** Argon2id, bcrypt, or scrypt — never a bare hash. Allow long passphrases; do not cap length low or forbid characters.
- **Pin the verification algorithm.** The verifier specifies the expected algorithm explicitly and rejects everything else, including `none`. Never read the algorithm from the token.
- **Tokens are short-lived and carry `exp`.** Pair short access tokens with rotating refresh tokens (each refresh invalidates the prior one) and a `jti` for revocation.
- **Store tokens in `HttpOnly` cookies, not JS-readable storage.** `HttpOnly; Secure; SameSite=Strict` keeps the token out of XSS reach.
- **CSRF check does not depend on the token being present.** A missing token is a _rejected_ request, not a skipped check.
- **Validate intent for every state change**, via a CSRF token tied to the session _and_ a same-origin check on `Origin`/`Referer`. `SameSite` cookies are a layer, not the only one — CORS misconfig or a subdomain can undercut them.

## JWT vulnerabilities

| Vulnerability               | Fix                                                                  |
| --------------------------- | -------------------------------------------------------------------- |
| `alg: none` accepted        | Reject `none`; pin the expected algorithm on verify.                 |
| Algorithm confusion (RS/HS) | Accept exactly one algorithm; never derive it from the token header. |
| Weak HMAC secret            | 256+ bits of cryptographic random, from an env var, not a phrase.    |
| Missing expiration          | Always set and validate `exp`; keep it short.                        |
| Token in `localStorage`     | `HttpOnly; Secure; SameSite=Strict` cookie instead.                  |

```javascript
// SIGN — secret from env, short exp, jti for revocation
const token = jwt.sign(
  {
    sub: userId,
    exp: Math.floor(Date.now() / 1000) + 15 * 60,
    jti: crypto.randomUUID(),
  },
  process.env.JWT_SECRET,
  { algorithm: "HS256" }
);

// SEND — keep it out of JS reach
res.cookie("token", token, {
  httpOnly: true,
  secure: true,
  sameSite: "strict",
});

// VERIFY — pin the algorithm; never trust the token header
jwt.verify(token, process.env.JWT_SECRET, { algorithms: ["HS256"] });
```

## CSRF

State-changing endpoints — and pre-auth endpoints like login, signup, password reset, and OAuth callbacks — must reject forged cross-site requests.

Defenses, used together:

1. **CSRF token** — cryptographically random, tied to the session, validated on every state change, regenerated on login (to also kill session fixation). A double-submit cookie (token in both a cookie and a header, server checks they match) is the stateless variant.
2. **`SameSite` cookies** — `Strict` for maximum isolation, `Lax` for a usable default. `Set-Cookie: session=…; SameSite=Strict; Secure; HttpOnly`.
3. **Origin/Referer check** — for JSON APIs especially: a JSON content-type does not prevent CSRF on its own.

Watch for: CSRF tokens leaked in URLs (use a header, e.g. `X-CSRF-Token`), tokens not scoped against subdomain takeover, and overly permissive CORS that re-opens what `SameSite` closed.

## Checklists

**JWT**

- [ ] Algorithm pinned on verify; `alg: none` rejected
- [ ] Secret is 256+ bits of random, from env (not a phrase)
- [ ] `exp` always set and validated
- [ ] Token in `HttpOnly` cookie, not `localStorage`
- [ ] Refresh-token rotation; old refresh token invalidated on use

**CSRF**

- [ ] Token is cryptographically random and tied to the session
- [ ] Validated server-side on every state-changing request
- [ ] Missing token ⇒ rejected (the check never depends on presence)
- [ ] Token regenerated on auth-state change
- [ ] `SameSite`, `Secure`, `HttpOnly` set on session cookies
- [ ] Origin/Referer validated on JSON endpoints
