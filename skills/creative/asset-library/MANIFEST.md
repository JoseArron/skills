# Portable library manifest

Use the project's format when one exists. This shape is for a local library with no manifest:

```json
{
  "title": "Visual asset library",
  "art_contract": "art-contract.md",
  "assets": [
    {
      "id": "guide-neutral",
      "title": "Guide, neutral pose",
      "file": "exports/guide-neutral.png",
      "preview": "exports/guide-neutral.png",
      "source": "sources/guide-neutral.svg",
      "kind": "character",
      "tags": ["guide", "neutral", "transparent"],
      "status": "draft",
      "prompt": "prompts/guide-neutral.md",
      "reference": "references/guide-anchor.png"
    }
  ]
}
```

Paths are relative to the manifest directory. Each asset requires only `id`, `title`, and `file`. IDs must be unique. Optional fields describe actual files and decisions. `reference` is a local visual anchor; store remote attribution in notes or an additional provenance field.

The builder checks `art_contract`, `file`, `preview`, `source`, `prompt`, and `reference` paths. Those files must exist inside the library directory. Use `preview` for a 3D render or another file a browser cannot display. `status` reflects the project's actual review state, such as `draft`, `selected`, or `rejected`.

```text
python path/to/asset-library/scripts/build_gallery.py path/to/library/manifest.json --output index.html
```

Output is relative to the manifest directory and must stay inside it. Default: `index.html`. The builder creates only HTML and links to source and export files without repackaging them.
