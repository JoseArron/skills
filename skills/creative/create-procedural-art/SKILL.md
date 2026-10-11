---
name: create-procedural-art
description: "Create or refine visuals through code, including SVG, Canvas, shaders, procedural 2D or 3D geometry, and generative graphics. Use when the artwork itself must be editable, parameterized, reproducible, or generated at runtime."
---

# Create procedural art

Translate direction into a controllable visual system. The code is the medium; its output still needs art review.

## Choose the rendering path

Read the art contract, target device, stack, and proof renders. Follow constraints such as code-only geometry, a shared rig, or a specific engine. Choose SVG, Canvas, shaders, mesh geometry, or an established library based on behavior and export.

Choose subject, visual grammar, and production constraints from the brief. Abstract graphics, lettering, environments, and representational subjects need different parameters and proofs.

Extending the established vector system can be enough for a static graphic. A bitmap texture belongs with image generation when requested and allowed. Do not hide raster images in a deliverable described as entirely procedural.

## Build the visual grammar

Expose parameters representing art decisions: proportions, silhouette landmarks, contour variation, palette, material response, texture scale, light, camera, composition, and motion inputs. Separate shape, rendering, and behavior only where it makes requested variation easier.

- Seed randomness when reproduction matters. Keep identity stable while changing rendering or motion.
- For recognizable subjects, preserve defining landmarks at intended size. For abstract work, check the requested composition, relationships, and variation.
- For 3D, check silhouette before material polish, then light, roughness, depth, occlusion, and camera. For 2D, check contour, values, layering, and texture scale.
- When the direction calls for irregularity or texture, make it deliberate. Choose clean geometry or variation according to the brief.
- Use the same model across render comparisons when the question is the renderer. Changing anatomy confounds the comparison.

## Prove the hard part

Build a representative still or playable study exposing the difficult behavior. For exploration, compare different treatments at the same scale and camera. For a selected direction, refine its traits instead of continuing to branch.

Show useful controls without building an unrequested editor. Preserve approved and unrelated runs. A playable request needs the interaction, not just a turntable or direction board. Read [REVIEW.md](REVIEW.md) before declaring readiness.

## Deliver

Provide editable source, the command or page that runs it, key parameters, and requested exports. Record seed and renderer/version when reproduction depends on them. Link the contract and label unresolved questions. Use `design-motion` for movement and `build-asset-library` for production catalogs when needed.
