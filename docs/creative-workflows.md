# Creative workflows

Use these skills to carry a chosen direction across references, prompts, code,
motion, sound, and reusable output. They follow project decisions rather than
prescribe a house art style. The [local research](agents/research/creative-workflows.md)
records the evidence from Gagambattle, procedural-pets, fake-news, and the supplied
naming prompts.

| Skill | Use it for | Deliverable |
| --- | --- | --- |
| [visual-research](../skills/creative/visual-research/SKILL.md) | Find and compare useful references | Cited observations and annotated moodboard or comparison |
| [art-direction](../skills/creative/art-direction/SKILL.md) | Turn a desired feel into concrete rules | Art contract and representative proof criteria |
| [image-prompts](../skills/creative/image-prompts/SKILL.md) | Translate direction into generator instructions | Paste-ready prompts or edit briefs; images only when requested |
| [procedural-art](../skills/creative/procedural-art/SKILL.md) | Draw or render through code | Editable SVG, Canvas, shader, or 2D/3D study with requested exports |
| [motion-design](../skills/creative/motion-design/SKILL.md) | Define movement and response | Timing rules, motion prompts, or runnable animation |
| [sound-design](../skills/creative/sound-design/SKILL.md) | Define sonic character and event cues | Cue sheet, audio prompts, or actual audio when requested and available |
| [asset-library](../skills/creative/asset-library/SKILL.md) | Make a coherent family reusable | Sources, exports, manifest, and searchable preview gallery |
| [creative-naming](../skills/creative/creative-naming/SKILL.md) | Analyze wordplay or generate names | Source/sound mappings, naming prompts, candidate rounds, or researched shortlist |
| [trailer-direction](../skills/creative/trailer-direction/SKILL.md) | Let music and footage shape a trailer | Song/reference research, timed treatment, storyboard, or edit plan |

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
it does not prove touch-local deformation or a playable game. Test code-built
art in its renderer, motion in movement, and reusable assets in their destination.
Record checks actually performed, including anything still uninspected.

## Example requests

- "Use $visual-research to compare three directions for this game. Explain the
  traits to borrow and avoid; keep the characters and setting original."
- "Use $art-direction to turn this selected reference into a contract covering
  world art, UI, typography, motion, and the proof we need."
- "Use $image-prompts to prepare transparent cutout prompts from our contract.
  Return prompts only, with shared identity and per-asset changes."
- "Use $procedural-art and $motion-design for a playable code-only study of this
  squishy character. Preserve its identity across touch, release, and rest."
- "Use $asset-library to deliver a consistent pitch kit with editable sources,
  transparent exports, a manifest, and searchable local HTML."
- "Use $creative-naming to analyze these Filipino spider puns and write a prompt
  for another round. Explain spoken transformations and keep prior names excluded."
- "Use $trailer-direction to research hip-hop-driven game trailers and map our
  footage to this track. Verify song sections and reference timestamps."

## Boundaries with other skills

`research` provides general source investigation. `visual-research` and
`trailer-direction` add creative evidence and comparison criteria. `prototype`
owns throwaway design questions; `procedural-art` owns the code-made artwork.
`ux-flows` and `make-it-obvious` own screen behavior and clarity; `art-direction`
owns visual identity. `concrete-naming` owns code identifiers; `creative-naming`
owns product and character names. The available image-generation skill owns
raster tool execution; `image-prompts` owns the production brief.

`choose-skill` routes to these jobs without requiring a full pipeline. `retro`
can examine a creative session's process; visual fixes remain with the relevant
creative skill.
