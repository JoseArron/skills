---
name: design-motion
description: "Design or implement animation and motion rules for characters, procedural objects, interfaces, or graphic sequences. Use when defining movement feel, timing, easing, deformation, transitions, or animation prompt briefs."
---

# Design motion

Make movement express the brief's purpose and intended feeling. Weight, personality, abstraction, and material response are choices for the subject; a mood word becomes useful when it changes timing, pose, or path.

## Read the movement's job

Read selected direction, motion notes, object or character model, and interaction. Identify the trigger, message, state change, and feeling. Preserve selected movement and unrelated behavior.

Use `ux-flows` for the user's journey or feedback placement; this skill owns how chosen feedback moves. Use `plan-trailer` for shot order, musical structure, and overall pacing. Load the needed entrypoint through the available skill mechanism or read it directly.

## Define observable motion

Describe key poses and timing, path, acceleration, easing, anticipation, overlap, settling, and holds. Include contact, pivots, deformable regions, and anchors. Specify durations or curves as design parameters unless measured from a source.

- Match deformation to the material. Squash, stretch, wobble, smear, and rigidity are options, not defaults.
- Preserve identity landmarks in extreme poses. A face sliding across the body can break identity even when motion is smooth.
- Distinguish authored animation from simulation. For interactive motion, test the requested input, interruption, and final state. For a physical simulation, test relevant contact, deformation, release, and rest behavior.
- For graphic motion, define hierarchy: what moves first, what the eye follows, and what stays readable. Avoid identical bounce on every layer.
- For a loop, inspect the seam. For a transition, define entry, exit, interruption, and final state.
- Where interface movement is optional, respect reduced-motion settings and preserve state information without the effect.

## Make it reviewable

Deliver a timing sheet, keyframe brief, generator-ready motion prompt, or runnable preview according to the request. For code, expose the parameters that affect feel. A still image does not prove motion.

Inspect at normal speed and relevant extremes. Check readability, contact, overshoot, settling, and interruptions. Separate observed behavior from planned behavior. Keep comparison runs identifiable so rejected movement does not become the default.

For export, record duration, frame rate, dimensions, alpha/background, loop convention, and state names as needed. For sprites, include frame order, pivots, and atlas layout. Carry selected rules into the contract or linked motion note; reusable sets belong in `build-asset-library`.
