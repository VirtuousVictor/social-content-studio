# Still-Image Generation and Editing

Use this module when the user asks to generate or edit a still image, or when a substantial director-treatment/visual-development deliverable calls for approval images. For routine social packages, storyboards and prompt-writing requests, deliver written prompts and production directions without generating images unless requested.

## Capability check

- Use the host's built-in image-generation tool when one is available; it is the default for ordinary image generation and editing.
- The Skill contains the decision process and prompt method, not the image model or tool. If no compatible image tool is exposed, provide the ready-to-use prompt and state that rendering is unavailable in this environment.
- Do not silently switch to a command-line/API fallback, ask for API keys, or claim the image was rendered. Use a fallback only if the user explicitly asks for or approves that mode and its prerequisites are available.
- This still-image method does not render video. A video prompt is not evidence that a video was generated.

## Choose the right operation

1. **Generate:** create a new image. If supplied images guide style, composition, mood or subject, label each as a reference rather than an edit target.
2. **Edit:** change an existing image while preserving specified elements. If the target is a local file and the host tool requires conversation-visible input, inspect it first with the host's image-viewing tool.
3. **Use native artwork instead:** for a logo, vector mark, diagram, simple UI or other code-native asset, prefer editing the source vector or building the asset directly rather than raster generation.

## Prepare and run

- Decide whether the result is a preview or a project asset, and collect the exact copy, constraints, output ratio, and input images first.
- Label every input image by role: edit target, style reference, composition reference, product reference or supporting insert.
- Use `references/image-prompt-method.md` for the eight-layer prompt structure. Add only details that improve the stated request; do not invent brand choices, claims, product details or narrative elements.
- For edits, state the one intended change and list the visual invariants that must remain unchanged. Preserve product geometry, logo, label and identity from supplied references.
- Request genuine transparency when a transparent cutout is required. Do not simulate transparency with a solid checkerboard background.
- For multi-asset requests, use a separate prompt and generation for each distinct asset. One prompt may produce variants only when the user wants variations of the same asset.

## Inspect and deliver

- Review the output for subject accuracy, framing, brand/product fidelity, exact text, unwanted objects, artifacts and requested transparency. Iterate with one targeted change at a time.
- For a project-bound image, place the chosen final asset in the authorized project location and verify the saved file. For an inline concept preview, show the image in the conversation where supported.
- Never overwrite an existing source image unless the user explicitly asks for replacement; otherwise use a versioned sibling name.
- Report whether an image was actually rendered, which available tool path was used, and the verified saved path for project assets. Do not report an unavailable capability as completed.

## Prompt scaffold

Use only the fields that help the specific asset:

```text
Use case: <asset category>
Asset type: <intended use>
Primary request: <user's request>
Input images: <Image 1: role; Image 2: role> (if supplied)
Scene/backdrop: <visual setting>
Subject and action: <what is visible at this moment>
Style/medium: <photo, illustration, 3D, etc.>
Composition/framing: <shot size, placement, negative space>
Camera and lighting: <viewpoint, lens character, light and shadow>
Color/material: <only if specified or materially useful>
Text (verbatim): "<exact copy>" (if needed)
Constraints: <invariants and required elements>
Avoid: <likely failure modes>
``` 
