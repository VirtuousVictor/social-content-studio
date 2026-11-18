# Still Image and Keyframe Prompt Method

For TVC keyframes, use `advanced-image-prompt-library.md` for the production frame types, style families, composition, and visual failure diagnosis.

Use this module when the user requests text prompts for still images, storyboard keyframes, packshots, or image-to-video starting frames. If the user explicitly asks to render a still image, follow `image-generation-workflow.md` and use a compatible host tool only if available. This Skill carries the method but does not itself provide an image model.

## Eight-layer order

Write the prompt in this order:
1. Subject: visible traits, product shape, material, or packaging.
2. Action: what is visibly happening at the captured instant.
3. Environment: location, time, weather, and relevant props.
4. Composition: shot size, placement, foreground and background, and negative space.
5. Camera: angle, lens character, depth of field, and motion style if relevant.
6. Lighting: actual sources, direction, contrast, and shadow behavior.
7. Color palette: hue, saturation, and tonal treatment.
8. Style reference: requested photographic or illustrative treatment.

Translate abstract feelings into visible expression, posture, action, composition, light, color, and texture. Keep product and character identity tied to supplied references.

## Brand and text fidelity

Use supplied product and logo artwork as the source of truth for shape, material, label, and placement. Do not invent logos, packaging copy, claims, interface text, or fine typography. Add exact text and brand marks in post-production when accuracy matters.

## Negative constraints

Name likely failure modes, such as distorted product geometry, wrong logo, hallucinated text, unreadable labels, extra fingers, inconsistent wardrobe, unwanted objects, watermarks, or a style shift. Preserve the requested framing and brand identity.
