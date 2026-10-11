# Validation of the v1.3.1 resync and creative suite

Checked on 2026-10-11.

- Repository discovery lists 55 skills, including four adopted upstream skills
  and nine original creative skills.
- All nine creative skills pass the bundled skill creator's `quick_validate.py`.
- The repository audit checks required frontmatter, unique folder-aligned names,
  UI metadata, and supporting Markdown links outside fenced examples.
- Explicit-only upstream skills retain their invocation policy. The bundled
  validator does not accept their `disable-model-invocation` field; that validator
  limitation is not a reason to remove the policy.
- Live skill instructions contain no retired `CONTEXT.md` convention or
  `resolving-merge-conflicts` reference. Attribution records the historical names.
- Five gallery tests pass: safe file resolution, preserved sources, escaped
  labels, duplicate and missing file rejection, and output path protection.
- A Chrome check of an isolated three-asset fixture confirms transparent
  previews, filtering by review state and tags, result counts, an empty state,
  and an actual asset download. The source link returns HTTP 200 for the expected
  SVG. Playwright times out while inspecting that standalone SVG document, so
  source-page browser inspection remains unverified. The fixture server's only
  missing resource is its optional favicon.
- `git diff --check` passes.

The [creative evaluation](creative-skill-evaluation.md) records three independent
text exercises. The [implementation evaluation](implement-spec-evaluation.md)
records integration failure cases and the fixes verified against the final
instructions. These checks evaluate skill instructions and the gallery helper;
they do not establish the quality of future artwork, audio, or game behavior.
