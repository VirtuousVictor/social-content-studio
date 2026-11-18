# Advanced Storyboard and Film Structures

Use when producing a cinematic TVC/brand film, multi-grid storyboard, product-film sequence, multi-segment video, or a client-ready shot plan. The regular short-form social standards in `SKILL.md` still apply unless the user chooses a different format.

## Think before the shot table

Before describing frames, write the film spine: audience memory, one-sentence theme, protagonist or visual subject, goal/tension, turning point, product role, emotional curve, and ending. Define the visual system (framing, lens character, camera movement, lighting, color, texture, performance, sound, edit rhythm). Every shot must advance story, product understanding, or emotion.

## Director-level shot plan

Use continuous timecodes that sum exactly to the requested duration. For every shot, record only the fields useful to execution, including:

- shot number, in/out time and duration;
- story beat/purpose, framing and camera angle;
- camera movement, speed, direction, focus, and transition;
- visible action and actor performance;
- product presence, state, interaction, and proof;
- dialogue/VO, on-screen text, ambience, SFX, and music;
- continuity/reference locks and any post-production composite.

Include a film synopsis, emotional curve, and visual language before the table when the user asks for a complete storyboard. Distinguish the script/story spine from the model-ready prompt; do not bury the story explanation inside prompt prose.

## Multi-grid storyboard method

First write a separate **video spine**: one sentence that describes the sequence of motion, light, color, and product-state changes. Then design the grid as frozen moments that let the intended video be reconstructed. A low-narrative product film still needs temporal logic; it can progress through camera movement, light change, and verified product states.

Build a grid prompt with four layers:

1. Global visual direction and image quality.
2. Reference map: which supplied asset controls product, character, wardrobe, scene, or style.
3. Narrative/visual spine and a numbered description for every cell.
4. Continuity anchors and negative constraints.

Choose a grid size to fit story density and output constraints. High-density grids carry a continuous action; medium-density grids show a journey or escalation; low-density grids prioritize visual beats and need an explicit motion spine. Keep cell numbers, order, and framing unmistakable. For every cell specify the decisive action, shot size, angle, product state, light, color, and visual link to the next cell. Avoid labels or text in the generated art when they can be added later.

Plan multiple grids as adjacent segments with a shared continuity block. State the time span, world type, density, and narrative function of each grid. Keep the last frame of one segment and the first frame of the next compatible in screen direction, movement, lighting, color, and emotional state. Split a selected cell into a standalone keyframe prompt only when a higher-fidelity frame is useful.

For product-led commercial grids, a useful legacy TVC default is to keep the product visibly present in at least 70% of cells, avoid more than two product-absent cells in a 3×3 grid, and avoid three product-absent cells in a row. Apply this only when it supports the chosen story; a deliberate human or environment beat can override it.

## Match cuts and world transitions

Connect scenes through a visible bridge: matched shape, direction, rotation, gesture, object movement, texture, sound, or color. A transition is motivated when the outgoing action creates the incoming shot. For product-world/brand-world crosscuts, let each segment finish a coherent beat before switching worlds. Do not alternate worlds as a disconnected montage.

Examples of bridge logic (adapt to actual material): a turning wheel to a circular product detail; a hand gesture to the product button; a moving light reflection to a scene light; a fabric or water texture to a product surface. Do not imply causality or feature behavior unsupported by product evidence.

## Product-film structures

For cinematic product breakdown, reveal only verified construction and functions. A flexible six-beat arc is:

1. **Reveal:** silhouette, restrained motion, or a striking first detail.
2. **Separate:** components move apart only if real parts are known and the effect is requested.
3. **Reassemble:** motion returns to a coherent whole; preserve geometry.
4. **Activate:** show a verified function or UI exactly as supplied.
5. **Explore:** move into a genuine material/detail macro.
6. **Land:** close on the image or action that delivers the payoff. A separate end card is an option when the current brief calls for it.

For a short product film, choose the length of the reveal, proof and payoff based on what the viewer needs to see. Use one memory point; do not force an explosion animation, extra function, or logo if the concept does not support it. For a 30-second crosscut film, one optional rhythm is: 0–3s use-world hook; 3–6s first product reveal; 6–10s use-world escalation; 10–15s verified function reveal and a movement bridge; 15–19s continuation into product detail; 19–23s product state change/hero motion; 23–27s material or emotional anchor; 27–30s brand landing. Determine exact durations from the approved concept, not a fixed percentage formula.

## Cross-world transitions and product motion

Use a visible bridge rather than a decorative wipe. Match movement, shape, texture, light/color, gesture, or sound. For product-world/brand-world crosscuts, let each segment finish a coherent beat before switching. Internal-product motion must define the axis, order, separation, camera path, speed change, and final alignment. Use only known parts and plausible product states; never infer internal construction from an exterior photograph.

For function visualization, specify the supplied screen or verified behavior and the light it casts; add exact text and numbers in post. For a material macro, move from a real surface feature to a clear focal point, with light motivated by that texture.

## Multi-grid density and panel controls

Match density to what the viewer must understand:

- **High narrative density:** each panel is a cause-and-effect action beat; panel order carries the story.
- **Medium density:** panels show a journey or task; state the journey spine before listing images.
- **Low narrative density:** panels are visual beats; state the camera/light/product-state progression so the sequence still has time and momentum.

When combining density levels, keep one dominant logic per grid and explain why it changes. Label every cell in reading order, use one decisive frozen instant per cell, and define the visual bridge to the next. A grid is a planning image; a separate prompt describes how those frozen moments become moving video.

## Convert the storyboard into video prompts

Write the time chain in continuous, non-overlapping segments whose durations add to the total. For each segment say what starts it, what changes, what motivates the camera move, and what visible state ends it. Use a separate prompt per shot/segment when the model cannot maintain the required action reliably in one generation.

Include duration, ratio, scene, action, camera, product movement/state, light/color, sound/voice, final frame, reference mapping, continuity locks, and negative constraints. Preserve supplied reference tags exactly when the chosen generator requires them; explain the role of each reference. A grid image can anchor composition while a product multi-view anchors identity, if the target model supports both.

### Continuous-shot / long-take structure

For a one-take prompt, explicitly describe:

1. base references and continuity anchors;
2. starting location, framing, and initial subject/product state;
3. a timed, causal action chain;
4. camera path, speed changes, focus behavior, and subject path;
5. lighting, atmosphere, palette, and texture;
6. sound/ambience/music or silence;
7. the ending event and final composition;
8. prohibited cuts, jumps, identity drift, extra objects, and unsupported changes.

Do not ask for a continuous take if separate actions, unseen physics, or model limits make a cut safer. State the intended continuity and let the user choose segmentation when necessary.

## Sound, end frame, and model limits

Plan ambience, tactile effects, score, VO, and silence as separate layers. If the edit will add score later, explicitly exclude generated music from the prompt; otherwise follow the user's sound brief. Protect approved logo geometry and exact copy by compositing in post when possible. Respect the user's chosen end-frame content and hold; do not assume the end card must include a slogan or product shot.

Model-specific constraints (supported reference count, face visibility, tags, aspect ratios, or image-to-video behavior) must be checked against the target model and current workflow. Do not present an old model limitation as universal. If unknown, write a model-neutral prompt and label assumptions.
