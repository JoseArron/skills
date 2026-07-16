---
name: audit-security
description: Audit code for security vulnerabilities across six trust boundaries — access control (IDOR, privilege escalation, mass assignment), auth & sessions (passwords, JWT, CSRF), injection (SQL, XXE, path traversal), XSS & output encoding, untrusted URLs & uploads (SSRF, open redirect, file upload), and data exposure (secrets, PII, leaky errors). Use when hardening or reviewing a feature, before shipping anything that handles untrusted input, auth, or sensitive data, or when asked to "scan for vulnerabilities", "is this secure", "check for IDOR/XSS/SQLi/SSRF", "security review". Defaults to fail-closed, least-privilege, server-side checks.
---

# Audit Security

Find where untrusted data crosses a **trust boundary** without the right check, and close the gap without breaking the feature. Approach the code as a bug hunter: assume every input is hostile until a server-side check proves otherwise.

Examples lean on a web stack (HTTP, a browser, an ORM, JWT) because that is where these bugs cluster, but the boundaries apply to any stack — swap the mechanism for whatever yours uses.

## Glossary

- **Trust boundary** — the line untrusted data crosses on its way into a sensitive operation: network → app, input → interpreter, app → browser, one principal → another's resource. Every vulnerability here is data crossing one of these without the check that boundary demands.
- **Fail closed** — on any error, ambiguity, or missing check, deny. A thrown exception must not land the user inside the protected action.
- **Least privilege** — every principal, token, and database role gets the minimum scope the task needs, nothing held "just in case".
- **Server-side truth** — every security decision is re-made on the server. Client-side checks are UX, never enforcement; a control the user cannot see is still reachable by a crafted request.
- **Defense in depth** — no single control is the only thing standing between an attacker and the asset.

## Axes

A security audit walks six trust boundaries. Each has a detail file with the smells, heuristics, and fixes for that boundary. **Read the relevant file before classifying a finding** — the heuristic is the citation, not a hunch.

- **Access control** — can this principal perform this action on this _specific_ resource? IDOR, horizontal/vertical access, privilege escalation, mass assignment, tenant isolation, account lifecycle. See [ACCESS-CONTROL.md](ACCESS-CONTROL.md).
- **Auth & sessions** — is the requester who they claim, is the session valid, and is this state change intentional? Password storage, JWT, cookie/session security, CSRF. See [AUTH-AND-SESSIONS.md](AUTH-AND-SESSIONS.md).
- **Injection** — does untrusted input reach an interpreter as code or structure? SQL, XXE, path traversal, command/template injection. See [INJECTION.md](INJECTION.md).
- **XSS & output** — is untrusted data rendered into a browser context unencoded? Reflected/stored/DOM XSS, contextual encoding, CSP, sniffing/framing headers. See [XSS.md](XSS.md).
- **Untrusted URLs & uploads** — does the server fetch a URL or accept a file it did not originate? SSRF, open redirect, insecure file upload. See [SSRF-AND-UPLOADS.md](SSRF-AND-UPLOADS.md).
- **Data exposure** — do secrets or sensitive data reach where they should not be visible? Secrets in client code, PII handling, transport headers, leaky errors. See [DATA-EXPOSURE.md](DATA-EXPOSURE.md).

## Principles

- **Validate on the server.** Client-side validation is a convenience for honest users; the server re-validates everything.
- **Encode for the destination, not the source.** The same string is safe in one context and an exploit in another — encode at the point of output for that exact context.
- **Allowlist over denylist.** Enumerate what is permitted; a denylist of known-bad patterns is always one bypass behind.
- **Return 404, not 403, on unauthorized resource access.** A 403 confirms the resource exists; a 404 leaks nothing.
- **Choose the restrictive option when unsure**, and leave a comment naming the threat it addresses.
- **Auditing hardens; it does not redesign.** A finding that needs a new abstraction escalates to `improve-codebase-architecture`; one that wants a deletion sweep escalates to `prune-cruft`.

## Process

### 1. Scope

Name the surface: a route, an endpoint, a feature slice, a PR. Bounded surface so findings stay reviewable in one pass — do not boil the ocean.

### 2. Walk the six boundaries

In order — access control, auth & sessions, injection, XSS, untrusted URLs & uploads, data exposure. For every finding record:

- **Where** — `@absolute/path:start-end`
- **Boundary** — which axis above
- **Smell** — one line citing the heuristic from that axis's file
- **Severity** — see rubric below
- **Fix** — the smallest change that closes the boundary

When a finding depends on something off-screen (a caller, a middleware, a DB grant), record it as "needs check at X" rather than guessing. Trace user input from its entry point to every sink it reaches.

### 3. Severity rubric

| Severity     | Test                                                                                                                                                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Critical** | Unauthenticated remote attacker gets data or code execution (SQLi, auth bypass, SSRF to metadata, stored XSS in a shared view). Fix before anything ships. |
| **High**     | Authenticated attacker escalates across users/tenants or reaches admin actions (IDOR, privilege escalation, CSRF on a sensitive action).                   |
| **Medium**   | Requires a precondition or yields limited impact (reflected XSS behind a click, open redirect, verbose errors leaking internals).                          |
| **Low**      | Defense-in-depth gap with no direct exploit today (missing security header where another control covers it).                                               |

### 4. Present, then act

Group by severity, critical first. Do **not** bulk-apply. Surface the list and let the user choose what to action.

For each approved fix, apply the minimal change that closes the boundary, and **fail closed** — when the check cannot pass, deny rather than fall through. Never weaken a control to fit calling code; fix the caller.

After each cluster:

- Run the project's typecheck/build and its tests; security fixes change control flow and break tests that asserted the insecure path.
- For an authorization fix, name the request a different user should now be denied.
- For an injection or XSS fix, name the payload that should now be neutralized.

### 5. Record the decision

If a fix changed an architectural call (replaced a denylist with an allowlist contract, moved a secret server-side, changed a token model), record it as an ADR in `{agentRoot}/docs/adr/` (see `domain-modeling`'s `ADR-FORMAT.md`). Skip ADRs for local, obvious fixes — only record what a future reviewer would otherwise re-litigate.

## Stop conditions

Stop when:

- Remaining findings are accepted risks the user has signed off on.
- A finding needs a redesign — escalate to `improve-codebase-architecture`.
- A finding is actually dead code — escalate to `prune-cruft`.
- The user signals enough.

Never silence a finding by weakening a test or adding a cast. Never log or echo a secret to "verify" it. Never widen a permission to make a fix compile.
