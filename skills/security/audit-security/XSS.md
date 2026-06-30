# XSS & Output Encoding

The browser-render boundary: untrusted data is written into an HTML, JavaScript, URL, or CSS context without encoding for _that_ context, so the browser executes it as markup or script. Every input the user controls — directly or indirectly — is a candidate, and the safe encoding depends entirely on where the value lands.

## Input sources to track

**Direct:** form fields, search queries, uploaded file names, rich-text/WYSIWYG content.

**Indirect:** URL params and query strings, the URL fragment (`#…`), request headers you display (Referer, User-Agent), data from third-party APIs, WebSocket messages, `postMessage` payloads, and `localStorage`/`sessionStorage` values that get rendered.

**Often missed:** error messages that echo input, PDF/document generators that accept HTML, email templates with user data, admin log viewers, JSON rendered as HTML, **SVG uploads** (can carry `<script>`), and Markdown that allows raw HTML.

## Heuristics

- **Encode at output, for the exact context.** The same string needs different escaping in HTML body, an HTML attribute, inside `<script>`, in a URL, and in CSS. Encode where it is written, not where it is read.
- **Prefer the framework's auto-escaping.** React JSX `{value}`, Vue `{{ value }}`, and server templates escape HTML context by default — the danger is the escape hatch (`dangerouslySetInnerHTML`, `v-html`, `|safe`, string-built HTML).
- **Sanitize HTML you must allow with a real library.** DOMPurify with an explicit tag/attribute allowlist for rich text — never a hand-rolled regex.
- **Treat the URL context specially.** A value placed in `href`/`src` must be a validated http(s) URL; block `javascript:` and `data:` schemes.
- **CSP is the backstop, not the fix.** Encoding prevents the bug; CSP limits the blast radius if one slips through.

## Contextual encoding

| Context             | Encoding                                                          |
| ------------------- | ----------------------------------------------------------------- |
| HTML body           | HTML-entity encode (`<` → `&lt;`)                                 |
| HTML attribute      | attribute-encode; always quote the attribute                      |
| `<script>` / JS     | JavaScript string escape (or inject as JSON via a data attribute) |
| URL (`href`, `src`) | URL-encode the value; validate the scheme                         |
| CSS                 | CSS escape; avoid user data in `style`                            |

## Content Security Policy

A strict CSP turns a successful injection into a blocked script load:

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self';
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https:;
  connect-src 'self' https://api.yourdomain.com;
  frame-ancestors 'none';
  base-uri 'self';
  form-action 'self';
```

- Avoid `'unsafe-inline'` and `'unsafe-eval'` in `script-src`; use a nonce or hash for any genuinely needed inline script.
- `frame-ancestors 'none'` (or `X-Frame-Options: DENY`) blocks clickjacking.
- Report violations with `report-uri` / `report-to` to catch attempts in the wild.

## Supporting headers

```
X-Content-Type-Options: nosniff      # stop MIME sniffing turning an upload into script
X-Frame-Options: DENY                # clickjacking (or CSP frame-ancestors)
Referrer-Policy: strict-origin-when-cross-origin
```

## Examples

DON'T:

```jsx
<div dangerouslySetInnerHTML={{ __html: comment }} />
```

DO:

```jsx
// Plain text — let JSX escape it
<div>{comment}</div>

// Rich text that must allow some HTML — sanitize with an allowlist
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(comment) }} />
```

## Decision shortcut

1. For each rendered value, name its context (HTML body / attribute / JS / URL / CSS).
2. Is it auto-escaped by the framework, or does it go through an escape hatch? Trace every escape hatch to its source.
3. URL sinks: is the scheme validated against `javascript:`/`data:`?
4. Any SVG/Markdown/HTML you accept: is it sanitized with a library and an allowlist?
5. Is there a CSP without `unsafe-inline`/`unsafe-eval`, and is `nosniff` set?
