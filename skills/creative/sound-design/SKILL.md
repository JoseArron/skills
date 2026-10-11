---
name: sound-design
description: "Design sound effects, game audio cues, sonic identity, and audio-generation briefs. Use when defining material, weight, response, cue families, procedural audio, or mix roles; song selection and trailer music structure belong to trailer-direction."
---

# Sound design

Make each cue communicate an event, material, or state while fitting the project's identity. Distinct events need distinguishable sounds; louder is not automatically clearer.

## Read the cue's job

Read the current audio brief, event map, art direction, existing cues, and target platform. Identify the event, listener perspective, expected response, and neighboring sounds that could be confused with it. Preserve selected cues and unrelated behavior.

Infer material and personality from the project's actual direction rather than adding generic cinematic impacts. A soft toy, paper card, metal gate, and silk thread should not share an arbitrary impact preset.

## Write a usable cue brief

For each cue, specify the relevant fields:

- Event and semantic role: confirmation, warning, movement, contact, damage, ambience, or character voice.
- Physical or imagined source, material, weight, and listener perspective.
- Attack, body, tail, pitch range, texture, and silence where useful.
- Variations, repetition behavior, looping, and how it differs from neighboring cues.
- Duration, mix priority, concurrency, and relation to animation or input.
- Output needs: format, sample rate, channels, looping boundary, engine naming, and import settings when established.

Treat numeric settings as proposed targets unless measured. For generator prompts, make each brief self-contained and specify unwanted speech, music, ambience, or reverberation only when those would interfere with the intended cue.

## Produce and listen within scope

For prompt requests, return prompts. For actual audio, use available audio tools, the project's procedural synthesis path, or editable source arrangements as appropriate. Do not claim to have generated or heard files you cannot inspect. A timing plan is a separate output from rendered sound.

For procedural audio, expose meaningful parameters and test envelopes, repetition, and playback in the target environment. For recorded or sourced material, preserve source and known usage information; online availability alone does not establish release permission.

Listen to cues alone and in context. Check clipping, abrupt boundaries, loop seams, tiring repetition, intelligibility, and whether cues remain distinguishable under music or simultaneous events. Exercise the actual event-to-sound mapping when implemented. Record which checks were performed.

Deliver cue files or prompt pack with a cue sheet and source/parameter notes when useful. Link selected sonic rules from the art or audio contract. Use `motion-design` for animation synchronization and `trailer-direction` for musical edit structure; load only the entrypoints needed for the task.
