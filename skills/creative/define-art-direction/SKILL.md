---
name: define-art-direction
description: "Define or revise an art direction contract for a game, brand, character, scene, or graphic system. Use when translating a desired feel or selected references into concrete visual rules, or correcting style drift across outputs."
---

# Define art direction

Turn the intended feeling into observable rules that prompts, code, motion, and graphic assets can share. Keep the contract small enough to use during production.

## Establish visual authority

Read selected references, existing contracts, owner decisions, and rejected studies. Follow explicit decisions over rough previews. Preserve unrelated choices. If direction is exploratory, label the contract as a candidate and provide distinct studies when those help settle it.

Derive subject, audience, cultural context, style, and medium from the brief. References illustrate selected traits; they do not supply unrelated project requirements.

Check currency when historical prompts disagree with production or runtime contracts. Record the active source instead of carrying stale counts, dimensions, or implementation assumptions into another batch.

Use concrete visual language. Replace "cute," "premium," or "cozy" alone with the traits that create the feeling: proportions, edge behavior, value grouping, material, spacing, lighting, and movement.

## Write the contract

Use [CONTRACT.md](CONTRACT.md) for the fields relevant to the deliverable. Omit irrelevant fields; a logo needs different rules from a rendered game world.

- Define **constants** that carry identity and **variables** that may change between assets. Character identity, line treatment, and palette roles should not be reinvented for every export.
- Attribute references by trait. Composition does not automatically determine anatomy, subject matter, interface styling, or rendering technique.
- Separate expressive artwork from functional graphics when their needs differ. Define each treatment from its purpose and legibility needs.
- State rules at the scale where the work is used. An attractive close-up may fail as a map marker, thumbnail, trailer frame, or slide cutout.
- Cover type and graphic hierarchy when relevant: roles, spacing, contrast, lettering treatment, and how marks relate to illustration. Use actual project font choices or label suggestions as candidates.
- Preserve cultural specificity without reducing a community to decorative symbols. Use `research-visuals` to verify unfamiliar claims when needed.

## Prove the direction

Choose a representative sample that exposes the hard constraints: a small character, environment crop, mixed UI/world scene, or slide composition. Match the requested medium and fidelity. A schematic wireframe does not prove a painterly direction; a generated still does not prove code-built art or game feel.

Compare the sample with the contract at intended size. State deviations and revise the relevant rule or sample. Do not silently promote the sample to the source of truth. Mark selection only when the user has selected it; proceed with reversible candidate work within scope.

## Carry the decision forward

Save the contract beside creative artifacts, following the project's layout or `{agentRoot}/creative/`. Record selection and the decision it supersedes. Link the authoritative contract from prompts, production notes, and asset manifests instead of duplicating it everywhere.

Use `write-image-prompts` for generator instructions, `create-procedural-art` for code-built visuals, `design-motion` for movement, `design-sound` for sonic character, and `build-asset-library` for a reusable set when requested. Load only the relevant skill through the available mechanism or read its entrypoint directly.
