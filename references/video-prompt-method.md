# Video Generation Prompt Method

For TVC multi-phase product films, multi-grid-to-video conversion, or continuous long takes, also use `advanced-storyboard-and-film-structures.md`.

Translate an approved storyboard into a direct, model-readable prompt. Adapt terminology and reference syntax to the target generator. If the platform is unknown, write a clear, model-neutral prompt.

## Core structure

Build the prompt from the elements required by the shot:
- Duration and aspect ratio.
- Reference assets and what each one controls.
- Scene setup and starting frame.
- Time-segmented action in physical order.
- Framing and camera movement.
- Subject and product movement.
- Lighting and color palette, described separately.
- Dialogue, voice-over, music, sound effects, or silence.
- Ending frame, continuity locks, and negative constraints.

For progressive action, divide the full duration into clear time ranges. State the action and end state in each segment, and how that state leads into the next. Do not overload a segment with unrelated actions or contradictory camera moves.

## Reference assets and continuity

Use generic labels such as attached product reference image, character reference, wardrobe reference, or scene reference. If the model supports native tags, preserve them exactly and explain what each tag controls. For every reference, state its identity and visible design, what it controls, allowed state changes, and what must remain fixed. Never include local filesystem paths or filenames in a prompt intended for a third-party model.

Lock identity, product geometry, packaging, logo placement, wardrobe, props, location, lighting, palette, and camera behavior wherever continuity matters. Describe physical actions rather than abstract emotions. Do not invent readable text, product UI, logo details, product behavior, or packaging. Composite exact brand artwork in post when generation may distort it.

## Sound and camera

Specify sound only where it contributes: dialogue, voice-over, ambience, music, effects, or deliberate silence. If the user asks for production sound only, say so and exclude music or added ambience. Keep camera movement physically possible and motivated. Separate camera movement from subject or product movement.

## Complex continuous shots

For a demanding one-take, establish reusable assets first; define the world, sound, visual tone, color, framing and composition; then write the ordered physical action chain, ending event, and negative constraints. Include hand/object interaction, trigger, state change, consequence, and how the final action affects the frame. Use this expanded structure only when it improves continuity or action clarity.

## Negative constraints and regeneration

Block only plausible failure modes for the shot, such as identity drift, extra fingers, warped hands, product deformation, wrong logo or packaging, random text or subtitles, watermarks, flicker, frame jumps, camera jitter, inconsistent lighting, or unrelated props.

For a revision, separate what must be preserved, what must change, acceptable variation, and what must never change. Keep approved material fixed while correcting the observed failure.

## Prompt template

Duration and aspect ratio:
Reference map:
Scene and starting frame:
Time segments:
Camera:
Subject and product movement:
Lighting and color:
Dialogue, voice-over, music, and sound:
Ending frame:
Continuity locks:
Negative constraints:
