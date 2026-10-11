# Should creative skill names describe actions?

## Answer

Prefer action names for these nine task skills. This is a naming recommendation, not a rule that every skill must start with a verb. The local skill-creator guidance says to prefer short action-oriented names; the repository uses both task names and reference names. Keep names tied to the work a user requests. Do not rename reference skills just to make the whole catalog grammatically uniform. Sources checked: 11 October 2026. [Skill-creator naming guidance](C:/Users/josee/.codex/skills/.system/skill-creator/SKILL.md:166)

Keep the creative suite independent of a particular culture or concept. Its instructions should read the user's audience, language, subject, references, and chosen direction. Philippine languages and spider puns belong to examples selected by a matching brief. The creator guidance explicitly warns against turning a particular example or personal preference into a universal requirement. [Preserve user intent and scope](C:/Users/josee/.codex/skills/.system/skill-creator/SKILL.md:16)

## Findings

This assessment reads the pre-rename version. Source links point to the renamed skills; the example-specific rules described below are removed in the follow-up implementation.

- The repository mixes verb names such as `implement`, `choose-skill`, `understand-the-user`, and `setup-pre-commit` with names such as `plain-english`, `domain-modeling`, and the nine creative names. This demonstrates a mixed catalog, not an enforced verb convention. [Repository overview](../../../README.md), [implement](../../../skills/build-and-debug/implement/SKILL.md), [plain-english](../../../skills/productivity/plain-english/SKILL.md), [domain-modeling](../../../skills/requirements-and-planning/domain-modeling/SKILL.md)
- Categories organize sources but flatten to skill names on installation. Choose names that identify the task outside the `creative` directory. [Repository structure](../../../README.md)
- `creative-naming` already reads the concept, audience, and languages from the brief. Its language-specific rule and `WORDPLAY.md` examples nevertheless emphasize Philippine languages and spider constructions. Generalize the rule to preserving distinctions among languages and communities; use varied examples to demonstrate the same reusable mechanisms. This is a recommendation based on the source, not a claim that the whole suite requires those subjects. [Creative naming](../../../skills/creative/brainstorm-names/SKILL.md), [Wordplay mechanisms](../../../skills/creative/brainstorm-names/WORDPLAY.md)
- The workflow guide states that project decisions own the visual direction. Its supplied naming request specifically invokes Filipino spider puns. Broader examples make that intended flexibility easier to discover. [Creative workflows](../../creative-workflows.md)

| Proposed name | Assessment against the documented scope |
| --- | --- |
| `research-visuals` | Fits reference investigation, comparisons, and moodboards. Keep the description explicit so users do not confuse research with generation. |
| `define-art-direction` | Fits contracts and visual rules. Preserve revision and correction in the description. |
| `write-image-prompts` | Fits prompts and edit briefs. Preserve the boundary that writing a prompt does not request image generation. |
| `create-procedural-art` | Fits artwork made through code. Preserve refinement of supplied work in the description. |
| `design-motion` | Fits timing, response, and motion rules. Preserve implementation and runnable animation in the description. |
| `design-sound` | Fits cues, sound identity, and audio briefs. Preserve actual audio when requested and tools are available. |
| `build-asset-library` | Fits reusable sources, exports, manifest, and preview gallery. Preserve organizing and extending a supplied collection. |
| `brainstorm-names` | Clear, but narrower than analysis, reusable prompt writing, evaluation, and shortlist research. Keep those modes in the description; do not let the verb force candidate generation for every naming request. |
| `plan-trailer` | Fits research, timed treatment, storyboard, and edit plan. Keep music-led design in the description. Do not imply that the skill always renders a finished video. |

These scope assessments derive from the nine descriptions and their deliverables in the [creative workflow table](../../creative-workflows.md). All nine proposed names use lowercase letters and hyphens and stay under the creator guidance's 64-character limit. [Naming guidance](C:/Users/josee/.codex/skills/.system/skill-creator/SKILL.md:166)

## Sources checked

- [Repository maintenance instructions](../../../AGENTS.md)
- [Repository overview and installation structure](../../../README.md)
- [Creative workflow guide](../../creative-workflows.md)
- All nine `skills/creative/*/SKILL.md` frontmatter descriptions; [creative naming body](../../../skills/creative/brainstorm-names/SKILL.md) and [WORDPLAY.md](../../../skills/creative/brainstorm-names/WORDPLAY.md)
- [Local skill-creator guidance](C:/Users/josee/.codex/skills/.system/skill-creator/SKILL.md)
- [Plain English guidance](../../../skills/productivity/plain-english/SKILL.md)

## Open questions

None blocks this recommendation. Renaming is a separate implementation step; this note changes no skill names.
