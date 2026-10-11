---
name: image-prompts
description: "Write image-generator prompts and edit briefs from art direction, references, and asset needs. Use for consistent characters, scenes, pitch assets, style studies, or reusable prompt packs; writing prompts does not itself request generation."
---

# Image prompts

Translate a visual brief into prompts that preserve identity while changing the requested subject, scene, or state.

## Read the visual rules

Use the selected art contract and approved anchors. Read only relevant parts. If direction is supplied in the request, work from it without requiring a document. For unresolved choices, offer a labeled candidate prompt; use `art-direction` only when defining direction is part of the task.

Inspect supplied references before describing or editing them. Distinguish style, identity, and composition references. Tell the generator which role each reference serves when its interface supports that control.

## Construct the prompt

Keep stable rules together and separate the variable request. [PROMPT-PACK.md](PROMPT-PACK.md) provides a portable structure for series and edits.

Describe the subject and action, framing and camera, shape language, contour, materials, palette roles, lighting, background, and output requirements that matter. Use concrete traits before broad labels. Include intended use and reading scale when they affect the result.

- Preserve recurring identity landmarks, proportions, wardrobe, palette, and orientation. Pose changes should not redesign a character.
- For pitch or graphic assets, specify cutout boundaries, transparency when needed, empty space, cropping, and compatible visual weight. Put precise typography in editable layout code when that better serves the deliverable.
- Make each series prompt self-contained enough to paste into the target tool. "Same style" works only when the tool receives the reference or prior prompt.
- For an edit, state what changes and what must remain. Supply the target image through the supported reference mechanism.
- Use negative instructions for concrete likely failures. Avoid generic quality slogans and incompatible styles.

Default to portable natural-language prompts when the generator is unspecified. Adapt syntax, references, seeds, aspect ratios, and negative-prompt fields only to features supported by the named tool; verify unfamiliar controls. A repeated seed or phrase does not guarantee identity consistency.

## Deliver or generate within scope

If asked for prompts, return prompts. If asked for images, load the available image-generation skill and use its tool for raster work. For code-native or vector outputs, use `procedural-art` or the established vector system when appropriate.

Inspect generated results against the contract and anchors. Record visible drift and revise the smallest relevant prompt section. Do not call uninspected outputs consistent or production-ready. Retain prompt-to-output mappings and selected/rejected state for batches so `asset-library` can catalog the files.
