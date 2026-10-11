# Creative workflows

Use these skills to carry a chosen direction across references, prompts, code,
motion, sound, and reusable output. They follow project decisions rather than
prescribe a house art style. The [local research](agents/research/creative-workflows.md)
records the evidence from Gagambattle, procedural-pets, fake-news, and the supplied
naming prompts.

Choose subject, culture, language, aesthetic, tone, and medium from each task's
brief. The research examples explain why the skills exist; they do not prescribe
the output. Examples illustrate transferable traits rather than defaults for
another project.

| Skill | Use it for | Deliverable |
| --- | --- | --- |
| [research-visuals](../skills/creative/research-visuals/SKILL.md) | Find and compare useful references | Cited observations and annotated moodboard or comparison |
| [define-art-direction](../skills/creative/define-art-direction/SKILL.md) | Turn a desired feel into concrete rules | Art contract and representative proof criteria |
| [write-image-prompts](../skills/creative/write-image-prompts/SKILL.md) | Translate direction into generator instructions | Paste-ready prompts or edit briefs; images only when requested |
| [create-procedural-art](../skills/creative/create-procedural-art/SKILL.md) | Draw or render through code | Editable SVG, Canvas, shader, or 2D/3D study with requested exports |
| [design-motion](../skills/creative/design-motion/SKILL.md) | Define movement and response | Timing rules, motion prompts, or runnable animation |
| [design-sound](../skills/creative/design-sound/SKILL.md) | Define sonic character and event cues | Cue sheet, audio prompts, or actual audio when requested and available |
| [build-asset-library](../skills/creative/build-asset-library/SKILL.md) | Make a coherent family reusable | Sources, exports, manifest, and searchable preview gallery |
| [brainstorm-names](../skills/creative/brainstorm-names/SKILL.md) | Analyze wordplay or generate names | Source/sound mappings, naming prompts, candidate rounds, or researched shortlist |
| [plan-trailer](../skills/creative/plan-trailer/SKILL.md) | Let music and footage shape a trailer | Song/reference research, timed treatment, storyboard, or edit plan |

For exploration, start with references and a candidate direction. For production,
read the selected contract and go straight to the required medium. Naming can
start independently; a selected name can feed visual identity. A trailer uses
the chosen visuals, motion, sound, and footage, but does not require rebuilding
all of them.

## Shared decisions

The project owns its palette, characters, typography, dimensions, renderer,
and medium constraints. Keep those choices in its art contract and production
notes. A reference can supply linework or composition without supplying subject
matter. Separate selected, candidate, superseded, and rejected work.

Proof must match the request. A moodboard tests comparison and composition;
it does not prove interactive behavior or finished production assets. Test code-built
art in its renderer, motion in movement, and reusable assets in their destination.
Record checks actually performed, including anything still uninspected.

## Example requests

- "Use $research-visuals to compare directions for this project. Explain the
  traits to borrow, their sources, and their production implications."
- "Use $define-art-direction to turn this selected reference into a contract covering
  world art, UI, typography, motion, and the proof we need."
- "Use $write-image-prompts to prepare transparent cutout prompts from our contract.
  Return prompts only, with shared identity and per-asset changes."
- "Use $create-procedural-art and $design-motion for an interactive code study
  of the requested visual behavior. Preserve the chosen direction."
- "Use $build-asset-library to deliver a consistent pitch kit with editable sources,
  transparent exports, a manifest, and searchable local HTML."
- "Use $brainstorm-names to develop names for this concept and audience. Compare
  approaches that fit the brief and keep prior names excluded."
- "Use $plan-trailer to research references and plan a trailer for this
  project. Choose structure and pacing from its purpose and available material."

## Boundaries with other skills

`research` provides general source investigation. `research-visuals` and
`plan-trailer` add creative evidence and comparison criteria. `prototype`
owns throwaway design questions; `create-procedural-art` owns the code-made artwork.
`ux-flows` and `make-it-obvious` own screen behavior and clarity; `define-art-direction`
owns visual identity. `concrete-naming` owns code identifiers; `brainstorm-names`
owns product and character names. The available image-generation skill owns
raster tool execution; `write-image-prompts` owns the production brief.

`choose-skill` routes to these jobs without requiring a full pipeline. `retro`
can examine a creative session's process; visual fixes remain with the relevant
creative skill.
