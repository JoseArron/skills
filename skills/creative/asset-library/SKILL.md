---
name: asset-library
description: "Produce and organize a consistent reusable visual asset set with editable sources, exports, a manifest, and a preview gallery. Use for game art kits, pitch-deck cutouts, graphic elements, icons, or branded illustration collections."
---

# Asset library

Deliver assets the user can find, preview, and reuse without rebuilding the direction for every item.

## Plan the set

Read selected direction, approved anchors, existing library, and target uses. Inventory before generating. Prioritize assets the requested screens, slides, or scenes need; do not expand a small request into an exhaustive catalog.

Set stable IDs, filenames, dimensions, transparency, scale, and formats. Keep editable sources separate from exports. Identify draft, selected, and rejected work; file presence is not approval.

## Produce with a common grammar

Use the established vector or code system where it serves the asset. For raster work, load the available image-generation skill. Use `image-prompts` for generator instructions or `procedural-art` for code-built collections when needed; read their entrypoints if the harness has no skill-loading tool.

Start with a representative sample when the look is unresolved or expensive to repeat. With a selected direction, continue production within scope. Carry the same contour, palette roles, light, proportions, framing, and visual weight across the set.

For slide cutouts, test placement on the intended background and near text. For game graphics, check in-game scale. A pretty contact sheet alone does not establish usability.

## Catalog the actual files

Use the project manifest when it has one. Otherwise [MANIFEST.md](MANIFEST.md) gives a portable JSON shape. Record sources, exports, prompts or parameters, references, and review status. Do not invent provenance for earlier files.

A reusable set should have a gallery when browsing is part of the request. Show previews, titles, useful tags, review state, and links to real files. Transparent assets need a checkerboard or background comparison. Preview animations as animations; give 3D files a suitable viewer or labeled render.

For a simple local library, `scripts/build_gallery.py` builds searchable static HTML from the manifest without dependencies. Use the environment's Python and keep output inside the library directory. For an interactive editor, follow the application stack instead.

## Verify and hand over

Check manifest files, links, and requested export sizes/formats. Visually inspect representative assets and a contact sheet; check alpha edges, clipping, and background compatibility where relevant. Open the gallery and exercise search and file links. Report draft or unchecked outputs accurately.

Deliver library root, gallery, manifest, and reusable formats. A gallery screenshot is not the asset set. Preserve unrelated and previously selected assets during revisions.
