# Advanced Image Prompt Library

Use for director visual development, TVC keyframes, product frames, multi-grid prompts, and image review. This is a prompt and visual-design reference; the image model/tool is supplied by the host environment.

## Prompt hierarchy

Put the most important visual control first. A useful order is:

1. intended image quality or medium (only when the target model responds to it);
2. subject and verified appearance;
3. visible action or product state;
4. environment, scale, surfaces, and atmosphere;
5. lighting sources/direction and shadow behavior;
6. composition, shot size, angle, focus, and negative space;
7. color and palette;
8. style anchor and constraints.

For the eight-layer production prompt, use: **Subject → Action → Environment → Composition → Camera → Lighting → Color → Style**. Keep the prompt concise enough to remain legible. For a single subject, state only relevant details; for a complex scene, separate labeled blocks and assign clear reference roles.

Translate abstract words into visible evidence. “Premium” may mean controlled reflections, precise machining, restrained background, and confident camera movement; choose only cues supported by the requested direction. Put exact text, logos, labels, claims, and complex UI in post unless the user has supplied authentic artwork and the tool can preserve it.

## Visual direction families

Use these as broad choices, not locked recipes. Confirm the direction when the project needs client approval; for a routine social deliverable, follow the approved brand look or state a practical assumption.

| Family | Visual intent | Prompt controls |
|---|---|---|
| Photographic naturalism | Reads as a real captured photograph | Natural imperfections, plausible optics, practical light, authentic skin/material detail |
| Cinematic live-action | Film still with deliberate lighting and grade | Lens perspective, motivated key/fill/rim, filmic contrast, controlled grain |
| Stylized 3D/CG | Clearly designed CGI with a deliberate art direction | Render/material language, geometry, stylization, lighting model |
| Photoreal CG | CGI made to approach physical realism | PBR surfaces, plausible reflections, global illumination, accurate scale; avoid mixing with live-action cues unless intended |
| Named or specific aesthetic | A user-defined look such as ink, cyberpunk, anime, or documentary | Describe its concrete line, texture, palette, lighting, and composition traits; respect applicable style/IP constraints |

The source library's A–E labels map to these five families. Do not treat those letters as universal model parameters. If the target image generator has its own style controls, use current platform documentation or the user's supplied workflow.

## Twelve production frame types

Select only the frame types the approved story needs:

### Product-world frames

1. **Hero:** one accurate product, controlled backdrop, material cues, readable silhouette, intentional copy-safe area.
2. **Breakdown:** known components only; define their spatial order and relation. Never invent internals.
3. **Function visualization:** depict only verified display/interface/behavior. Use supplied UI and values; do not fabricate labels or data.
4. **Material macro:** real surface, scale cue, raking light, shallow focus, physical texture.
5. **Pack shot:** verified packaging and product arrangement; preserve all text and proportions.
6. **End frame:** stable pose and approved logo/copy treatment; reserve safe area and composite precise brand artwork in post.

### Brand-world frames

7. **Action/sport:** freeze a physically credible moment; show relevant product and gear without false use.
8. **Lifestyle:** lived-in environment, natural interaction, plausible props and light.
9. **Emotional:** readable expression/gesture, relationship, and product's truthful role.
10. **Environment/atmosphere:** location-only establishing or bridge frame; define its transition function.

### Bridge frames

11. **Match-cut bridge:** match the outgoing/incoming shape, motion, texture, color, gesture, or sound.
12. **Product reveal:** use occlusion, focus shift, movement, light, or an action to reveal the real product.

### Frame-specific prompt skeletons

Use these as starting structures, not literal fill-in-the-blank requirements:

1. **Hero:** quality/medium → supplied product appearance → stable angle and state → restrained studio/background → key and rim light → product scale and negative space → accurate material and identity constraints.
2. **Breakdown:** supplied product → only verified components in a named spatial order → controlled separation distance and view angle → studio light on each component → exact return/reassembly state if animated → prohibit extra or invented parts.
3. **Function:** supplied product and authentic UI → verified display/function state → real interaction or supported use → camera relationship to screen/product → screen light and surrounding surfaces → prohibit fabricated numbers, labels, features, or unreadable text.
4. **Material macro:** actual product region → real material and microtexture → magnification cue → low-angle/raking light and reflection → focal plane/depth of field → prohibit changing shape or finish.
5. **Pack shot:** exact supplied packaging and product → supported arrangement and orientation → clean background → soft/key/rim light → package-product hierarchy and safe area → preserve all logos and typography.
6. **End frame:** approved product state or logo artwork → quiet background → fixed placement and scale → exact safe area/hold → list only the copy the user approved → no extra marks.
7. **Action/sport:** real environment and action → performer pose and equipment → accurate product placement/use → plausible debris/wind/water/snow if present → motion angle and camera path → preserve physical safety and true product use.
8. **Lifestyle:** time/place → person's visible action and wardrobe → natural product interaction → credible lived-in details → motivated practical light → candid framing and depth → no staged reaction unless requested.
9. **Emotional:** relationship/context → visible gesture and expression → product's credible role → lighting/color linked to the emotional beat → framing that carries performance → avoid sentimental shorthand that is not in the story.
10. **Environment:** location/scale/surfaces → time and weather → atmospheric light/particles → foreground-to-background layers → wide composition/leading lines → no people/product if it is meant to be a clean plate.
11. **Match-cut bridge:** outgoing frame geometry/motion/color → exact matching property → incoming frame property → point of transition → same direction/tempo/light cue → prohibit unrelated visual changes.
12. **Reveal:** concealment mechanism → reveal action (focus, movement, occlusion, light, or gesture) → timing and final readable product frame → composition and exposure → preserve identity during reveal.

For reference-driven images, attach the mapping to the prompt skeleton: product identity, character identity, scene, style, or edit target. Do not let a style image overwrite the product's verified design.

## Composition and ending frame

Choose a shot size and viewpoint to support the story: wide for geography, medium for interaction, close for readable action, macro for real material detail. Set foreground/midground/background layers, subject placement, perspective, depth of field, and visual path. Reserve negative space only when copy or a logo will actually be added.

For a brand end card, keep it distinct from generated story frames when exact logo fidelity matters. Describe background, approved logo position/scale, safe areas, hold duration, and any approved text. Do not add slogan, URL, CTA, or feature copy if the user chose a logo-only card.

For a TVC storyboard, composition can use reveal framing (controlled occlusion or shadow), hero framing (clear silhouette and edge separation), scale framing (foreground reference to communicate size), or split-world framing (visual bridge across a cut). Pick a single main hierarchy. Keep on-screen copy and logo within platform-safe areas and have exact text added in post.

## Prompt length and precision

As a rough starting point for text-oriented generators, a simple single-subject image may need only a short paragraph; a subject plus location and light needs a few well-prioritized sentences; a complex multi-layer scene can use labeled blocks. The source workflow's 30–80 / 80–150 / 150–300 Chinese-character bands are optional planning ranges, not universal generator limits. Target-model behavior and clarity take priority. Remove redundant style adjectives before adding more detail.

## Reference image mapping

Label every attachment by role (edit target, product identity, character identity, wardrobe, scene, style, composition, or supporting insert). State which attributes each reference controls and which may change. For an edit, state exactly what changes and what remains invariant. Never assume all attachments are edit targets.

## Common failures and iteration

Check for product-shape drift, wrong color/material/logo, illegible or invented text, fabricated UI, unwanted accessories/props, extra limbs/fingers, inconsistent identity/wardrobe, mismatched camera direction, flattened depth, muddled lighting, and style conflicts. Diagnose the layer that caused the error:

- wrong subject → revise identity/product detail;
- poor composition → move placement/framing instructions earlier;
- excess visual noise → remove competing objects and equal-weight details;
- bad light/texture → specify source direction, surface, and reflection behavior;
- wrong realism level → remove conflicting style anchors and select one family;
- wrong element present → remove prompt wording that implies it and add a direct avoid constraint.

Change one major dimension per iteration. After repeated small misses, revise the composition or concept rather than piling on adjectives. Preserve exact product and brand identity throughout.

### Visual diagnosis shortcuts

| Observed problem | Likely cause | Targeted correction |
|---|---|---|
| Too bright/dark | Conflicting implied light sources or vague exposure | Name the key source, direction, intensity, shadow depth, and what remains unlit |
| Unwanted objects | Scene wording or context implies props | Remove the inducing phrase, simplify the set, then state a concise avoid list |
| Space feels small/flat | No scale cue, vertical extent, or depth layers | Add architecture/foreground scale references, perspective, and atmospheric depth |
| Face/hand deforms | Too many identity details, difficult pose, or poor light | Simplify the action, lock identity with a supplied ref, use a readable pose and softer face light |
| Color drifts | Palette conflicts with light source or style anchor | Choose one dominant palette, align practical/key light color, remove contradictory anchors |
| Subject is lost | Equal-weight details, poor placement, or clutter | Reduce secondary objects, state one focal hierarchy, specify shot size and focus |
| Material looks fake | Surface named generically without physical behavior | Describe grain, roughness, reflection, edge, and how raking light reveals it |
| Frame looks flat | Everything shares one focal plane or contrast level | Separate foreground/midground/background and define focus and shadow depth |
| Realism/CG style wobbles | Photographic and render instructions conflict | Choose one visual family and remove competing realism/style terms |

If several small fixes do not improve the result, question whether the concept, reference, or composition itself is wrong before iterating again.
