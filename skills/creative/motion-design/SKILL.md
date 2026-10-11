---
name: motion-design
description: "Design or implement animation and motion rules for characters, procedural objects, interfaces, or graphic sequences. Use when defining movement feel, timing, easing, deformation, transitions, or animation prompt briefs."
---

# Motion design

Make movement express weight, personality, and purpose. A mood word becomes useful when it changes timing, pose, path, or material response.

## Read the movement's job

Read selected direction, motion notes, object or character model, and interaction. Identify the trigger, message, state change, and feeling. Preserve selected movement and unrelated behavior.

Use `ux-flows` for the user's journey or feedback placement; this skill owns how chosen feedback moves. Use `trailer-direction` for shot order, musical structure, and overall pacing. Load the needed entrypoint through the available skill mechanism or read it directly.

## Define observable motion

Describe key poses and timing, path, acceleration, easing, anticipation, overlap, settling, and holds. Include contact, pivots, deformable regions, and anchors. Specify durations or curves as design parameters unless measured from a source.

- Match deformation to the material. Squash, stretch, wobble, smear, and rigidity are options, not defaults.
- Preserve identity landmarks in extreme poses. A face sliding across the body can break identity even when motion is smooth.
- Distinguish authored exaggeration from simulation. Test repeated inputs, touch locality, release, interruption, collision, and rest where relevant. Whole-object scaling does not prove local soft-body response.
- For graphic motion, define hierarchy: what moves first, what the eye follows, and what stays readable. Avoid identical bounce on every layer.
- For a loop, inspect the seam. For a transition, define entry, exit, interruption, and final state.
- Where interface movement is optional, respect reduced-motion settings and preserve state information without the effect.

## Make it reviewable

Deliver a timing sheet, keyframe brief, generator-ready motion prompt, or runnable preview according to the request. For code, expose the parameters that affect feel. A still image does not prove motion.

Inspect at normal speed and relevant extremes. Check readability, contact, overshoot, settling, and interruptions. Separate observed behavior from planned behavior. Keep comparison runs identifiable so rejected movement does not become the default.

For export, record duration, frame rate, dimensions, alpha/background, loop convention, and state names as needed. For sprites, include frame order, pivots, and atlas layout. Carry selected rules into the contract or linked motion note; reusable sets belong in `asset-library`.
