# Dead Code

Code with no current caller, no current consumer, no current configuration path.

## Smells

- Exports nobody imports — verify across **every consumer** in the codebase (every app/package in a monorepo), not just the current file.
- Files imported only by themselves or by other dead modules.
- Function params with default values, never overridden by any caller.
- Component props never set by any caller; default values that mask absence.
- Feature flags that are always `true` or always `false` in every environment config.
- `if (false) { ... }`, commented-out blocks, `// eslint-disable` covering deleted intent.
- `// TODO` older than the feature it sits in, with no owner and no ticket.
- Translation / i18n keys not referenced from any component or template.
- Enum / union members nobody constructs and nobody matches.
- Routes registered but never linked to and never visited (404 in practice).
- DB columns / API fields the client/server stopped reading.
- Tests that exist only for a function that itself is dead.

## Verification before deletion

Tooling has false positives — verify each finding by hand.

- Search the whole codebase, not just the current file or package (in a monorepo, every app).
- Check **dynamic references**: string-keyed lookups, `require(name)`/reflection, route registries, DI tokens, factory maps, dynamic component creation.
- Check **generated artefacts**: ORM clients (Prisma/etc.), OpenAPI / GraphQL / RPC contracts, schema-derived types, codegen output.
- Check **entrypoints and config**: framework conventions (e.g. `main.*`, Next.js `page.tsx`/`route.ts`/`middleware.ts`, Rails initializers, Spring component scan), test setup files, `*.config.*` — these often look orphan to dead-code tools but are real entrypoints.
- Check **tests**: a function consumed only by tests is not dead, but the tests themselves may be — delete them together if the production caller is gone.
- For UI components: search markup/JSX usage, registry maps, and any lazy/dynamic `import(...)` paths.

## Examples

### Unused export

DON'T leave:

```ts
export function legacyFormat(d: Date) { ... }
export function format(d: Date) { ... }
```

when only `format` is imported anywhere in the workspace.

DO: delete `legacyFormat` and any tests that exist solely for it.

### Always-true flag

DON'T:

```tsx
if (FEATURES.newCheckoutFlow) {
  return <NewFlow />;
}
return <OldFlow />;
```

when `FEATURES.newCheckoutFlow` is `true` in every environment.

DO: inline `<NewFlow />`, delete `<OldFlow />` and the flag definition.

### Prop nobody sets

DON'T:

```tsx
type Props = { title: string; subtitle?: string; legacyMode?: boolean };
```

when `legacyMode` has zero callsites.

DO: drop `legacyMode` and any branches that read it.

### Default param never overridden

DON'T:

```ts
function send(payload: Payload, retries = 3) { ... }
```

when every caller calls `send(payload)`.

DO: remove the param and inline `3` (or hoist it as a named constant if it has meaning).

### Commented-out block

DON'T:

```ts
// const oldHandler = (e: Event) => {
//   ...
// };
```

DO: delete it. Git history is the archive; the file is not.

## Anti-patterns when deleting

- Don't just comment it out — delete.
- Don't keep a "just in case" wrapper around the removed code.
- Don't leave a no-op stub "for compatibility" unless an external consumer truly depends on it (and document that consumer).
- Don't delete and re-add an `as any` to make the rest typecheck — fix the contract instead.

## Tooling hints

- The project's own dead-code reports (e.g. `knip`, `ts-prune`, `fallow`, coverage output, IDE "unused" hints) are a starting point, not a verdict. Always verify by hand.
- A typecheck or build after deletion catches broken imports (e.g. `tsc --noEmit`, `cargo check`, `go build`).
- Repo-wide grep for the symbol name plus kebab/snake case variants and any string-key form.
- For routes and i18n keys, search the literal string, not just the identifier.
