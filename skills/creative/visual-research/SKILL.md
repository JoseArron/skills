---
name: visual-research
description: "Research visual references and build annotated moodboards for games, brands, characters, environments, or graphic styles. Use when choosing an aesthetic, comparing art territories, or investigating visual identity references."
---

# Visual research

Find references that help the user make a visual decision. An annotated board explains what to borrow from each reference and what to leave behind.

## Start with the decision

Read the project's selected art contract, identity notes, owner feedback, and relevant experiments first. Separate selected direction, candidate direction, and rejected work. A convenient preview or recent file does not supersede an explicit decision.

Identify the question: character proportions, environment treatment, material, typography, composition, cultural setting, or the whole identity. Use the audience, intended feeling, output medium, and production constraints already supplied. Ask only for a missing choice that changes the research.

## Collect usable evidence

- Prefer creators' portfolios, official game pages, press kits, studio breakdowns, museum collections, and original publications. Trace reposted images to their creator when practical.
- Inspect the actual visual before describing it. If you can access only text, label that limit; do not invent a visual analysis.
- Record creator, work, source URL or local path, and the specific image, screen, or timestamp examined. For live references, verify the link.
- Describe visible traits: silhouette, proportion, contour, value grouping, palette relationships, material, lighting, type hierarchy, framing, and density. Separate observation from your proposed interpretation.
- Separate subject matter from visual treatment. A sketchbook reference can inform linework and spacing without requiring a literal notebook background.
- For cultural references, identify the place, community, object, or practice represented. Verify language and heritage claims rather than treating a national label as a visual style.

## Build a useful comparison

Group references into distinct directions when the user is exploring. Change the underlying visual grammar, not just the palette. Each direction needs a rationale, useful traits, traits to exclude, and production implications.

When a board helps, use an editable HTML page or the requested format with labeled reference images and source links. Keep originals distinguishable from your generated studies. Use permitted embeds, supplied local images, or links; do not present a generated imitation as source evidence. If the request is research only, a cited comparison can be enough.

For each reference, answer: **What does this help us decide?** Omit attractive images with no role in that decision. Note when references contradict one another instead of implying that all their traits fit together.

## Deliver

Give a supported recommendation and annotated reference set. Mark unresolved choices as candidates. Save durable research in the project's established location, preferably `{agentRoot}/research/`, when useful. Follow the configured agent root; a one-off board needs no setup ceremony.

When the user selects a direction, use `art-direction` to turn it into production rules. Load its entrypoint through the harness's skill mechanism, or read `SKILL.md` directly when no mechanism is available. Research does not itself approve a direction.
