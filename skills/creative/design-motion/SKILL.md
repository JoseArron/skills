---
name: design-motion
description: "Design or implement motion for creative work across media, including animation, graphic sequences, interfaces, and interactive pieces. Use when defining timing, movement feel, transitions, or animation briefs."
---

# Design motion

Make movement express the brief's purpose and intended feeling. Weight, personality, abstraction, and material response are choices for the subject; a mood word becomes useful when it changes timing, pose, or path.

## Read the movement's job

Read selected direction, motion notes, the subject or composition, and interaction when relevant. Identify the movement's purpose, message, timing context, and feeling. Preserve selected movement and unrelated behavior.

Use `ux-flows` for the user's journey or feedback placement; this skill owns how chosen feedback moves. Use `plan-trailer` for shot order, musical structure, and overall pacing. Load the needed entrypoint through the available skill mechanism or read it directly.

## Define observable motion

Describe key poses and timing, path, acceleration, easing, anticipation, overlap, settling, and holds. Include contact, pivots, deformable regions, and anchors. Specify durations or curves as design parameters unless measured from a source.

- Match deformation to the material. Squash, stretch, wobble, smear, and rigidity are options, not defaults.
- For recognizable subjects, preserve defining features across extreme poses. For abstract sequences, preserve the intended geometry and compositional relationships.
- Distinguish authored animation from simulation. For interactive motion, test the requested input, interruption, and final state. For a physical simulation, test relevant contact, deformation, release, and rest behavior.
- For graphic motion, define hierarchy: what moves first, what the eye follows, and what stays readable. Avoid identical bounce on every layer.
- For a loop, inspect the seam. For a transition, define entry, exit, interruption, and final state.
- Where interface movement is optional, respect reduced-motion settings and preserve state information without the effect.

## Make it reviewable

Deliver a timing sheet, keyframe brief, generator-ready motion prompt, or runnable preview according to the request. For code, expose the parameters that affect feel. A still image does not prove motion.

Inspect at normal speed and relevant extremes. Check readability, contact, overshoot, settling, and interruptions. Separate observed behavior from planned behavior. Keep comparison runs identifiable so rejected movement does not become the default.

For export, record duration, frame rate, dimensions, alpha/background, loop convention, and state names as needed. For sprites, include frame order, pivots, and atlas layout. Carry selected rules into the contract or linked motion note; reusable sets belong in `build-asset-library`.
