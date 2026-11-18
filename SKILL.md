---
name: social-content-studio
description: Plan and produce fact-checked social content systems for brands and products, including short-form video stories, storyboards, still-image and video prompts, platform copy and recurring calendars. Use for social content campaigns and ongoing content operations; actual media generation requires an available image or video tool.
---

# Social Content Studio

Create reusable social content that is specific to the brand, audience, market and channel. Treat the task as both editorial planning and production writing: shape the idea, make the story legible, keep claims grounded, and give the user assets they can publish or hand to production.

## Start from the user's context

- Review the current project conversation, supplied files, product references and latest content packages before asking questions.
- Within the current brand and project, carry forward confirmed brand preferences, product corrections, campaign themes, approved slogans, forbidden claims and output formats. Do not ask again for information already established.
- For a new product, establish a compact profile before the first campaign. Extract from context and files, then ask one concise bundled set only for essential gaps: product and models, verified features and proof, audience and market, goal, platform and language, duration and ratio, visual references, production mode or talent constraints, approved wording, and legal or claim restrictions. Ask about price or offers only when the requested content needs them.
- For an established product, reuse the confirmed profile and preferences. Ask only about new missing details that materially affect the current deliverable; do not repeat answered questions. If a detail is nonessential, proceed with a reasonable assumption and label it.
- Distinguish verified product facts from creative interpretation. Never invent features, specifications, app screens, product behavior, customer results, testimonials, legal status, performance or reach.

## Route the work

This is one self-contained social-content and video-production skill. Its professional workflows are implemented in internal references, templates, and optional table-export scripts; do not call or require separate TVC skills. The skill carries the methods and prompts, while image/video rendering tools are separate capabilities that may or may not exist on the computer using it.

Use the [workflow map](references/workflow-map.md) to select the work the user asked for. The user's current brief and the rules in this entrypoint govern every stage. Preserve the approved story, product facts, assets, language, delivery format and remaining runtime as work passes from one stage to the next.

| Request | Read and apply |
|---|---|
| One caption, Story or community post | Use the product profile and Platform copy below. Deliver the requested channel and language. |
| New campaign or several creative directions | Gather only the missing brief decisions, then use [brief and concept development](references/complete-brief-routing-and-concept-methods.md). For an approved idea, continue directly with that idea. |
| Establish a visual style or plan stills | Use [director treatment](references/complete-cinematic-direction-and-treatment-methods.md) and [visual assets](references/complete-visual-assets-and-image-prompt-methods.md). Carry the approved camera, performance, light and brand choices into the storyboard. |
| Daily video package | Check the last episode, theme and current beat. Develop the story, then its [timed storyboard and prompt](references/complete-storyboard-and-video-prompt-methods.md). Use that same story, feature and time budget for the requested platform copy and review. |
| Seedance commercial, prompt diagnosis or result review | Start with the [Seedance core workflow](references/complete-professional-source-library.md#src-seedance-tvc-director-skill-md). Read the relevant sections by title or anchor. For example, use [reference mapping and prompt compilation](references/complete-professional-source-library.md#src-seedance-tvc-director-references-seedance-2-5-prompting-md), [product actions](references/complete-professional-source-library.md#src-seedance-tvc-director-references-product-actions-md), [voiceover](references/complete-professional-source-library.md#src-seedance-tvc-director-references-voiceover-md) or [delivery checks](references/complete-professional-source-library.md#src-seedance-tvc-director-references-delivery-and-qc-md). Use the requested deliverable and the known configuration to choose sections. |
| Production planning, editing or review | Use the relevant section of [production and review](references/complete-production-review-and-delivery-methods.md). For a revision, identify the observed failure, change the affected layer and keep approved decisions. |

The [source inventory](references/full-source-inventory.md) links the original methods to their full text. The [capability map](references/capability-crosswalk.md) locates methods by task. The combined source library and the [original overview](references/professional-source-overviews.md) preserve standalone examples for consultation. Interpret their specialist names as stages within this skill and their model settings as examples subject to host capabilities. Resolve conflicting source defaults using the current brief and this entrypoint.

Use the [original professional templates](assets/templates/professional-template-library.md) or the individual templates in `assets/templates/` for requested handoffs. A storyboard can be delivered in the conversation. When a spreadsheet is requested, prepare a TSV and use `scripts/make_content_tables.py` for CSV or `scripts/make_content_excel.py` for XLSX.

For a prompt-only or text-only request, deliver text at every stage, including director treatment and nine-panel storyboards. When a user requests stills or a substantial visual-development package that includes approval images, use a compatible host image tool for those assets. When rendering is unavailable, deliver the production prompt and identify the outstanding asset. Render video only on explicit request using an available compatible tool.

## Recurring series and themes

For an ongoing calendar, review the latest package and sequence before creating the next episode. Continue the established weekly theme and mapped beat when one exists. Start a new theme only at the agreed cadence. Track recent hooks, locations, actions and plot devices to prevent repetition. Each episode should work on its own while advancing the larger series.

When establishing a new weekly theme, provide a compact map with the premise, recurring visual thread and a distinct beat for each day. Keep the map grounded in verified product facts and realistic audience needs.

## Story and hook standard

For every short-form video, establish:

1. A protagonist and concrete goal.
2. A recognizable tension, hesitation or obstacle.
3. A turning point connected to one verified product fact.
4. A visible or emotional payoff.

Put a clear attention hook in the first three seconds. Begin with action, a surprising image, a sharp question or a conflict that the story resolves. Do not spend the opening on a slow establishing shot, logo or list of features. Make each shot motivate the next through action, reaction, a match-on-motion or a recurring story object. Avoid feature-demo sequences and disconnected montages presented as stories.

## Reference-video analysis

When a user provides a video reference, analyze the accessible material before setting a style standard. Separate what is directly observable from what is inferred. If only selected frames or screenshots were inspected, say so; do not claim to have watched the complete clip. Describe the relevant opening, transitions, pacing, presenter/product balance, overlays, payoff and end frame. Do not copy a reference's claims or product behavior unless they are verified for the user's product and market.

Translate the reference's useful craft into the new brand's story. Preserve the user's existing requirements for narrative, hooks, safety and claim accuracy even when the reference uses a different structure.

## Storyboard writing

For each shot, specify continuous timecodes that add up exactly to the requested duration, framing, camera movement, visible action, performance, product state, dialogue or voice-over, sound and on-screen text. Every shot needs a narrative or informational purpose. Use concrete camera grammar and motivated transitions. Preserve actor, wardrobe, prop, product, location, lighting and color continuity.

Put readable text, logos and complex interfaces in post-production unless authentic assets are supplied and the production workflow supports them. Never ask a video model to invent legible product UI or brand typography.

## Video-generation prompts

When requested, write the prompt in the language the user specifies. Make it directly executable and include:

- Duration and aspect ratio.
- Generic or supplied reference mapping that explains what each asset controls.
- Scene setup and a time-segmented action chain.
- Camera movement, subject/product movement, lighting and palette.
- Dialogue, voice-over, sound and music cues when useful.
- Actor/product/prop continuity locks.
- Negative constraints for known failure modes.

Do not put local filesystem paths or local filenames into a prompt intended for a third-party video model. Refer to supplied references generically, such as “attached product reference image(s).” Do not claim to generate or render media unless the user explicitly requests that and the available workflow supports it.

## Choosing the ending

Choose the final beat to fit the current story and deliverable. The final action or line may use the full running time. Add a separate brand card when the current project's brief or brand rules call for one. Use that project's specified artwork, copy and timing. A master approved for one project or episode carries over only where its use was agreed. Treat timing tables in the reference manuals as examples for their own briefs.

## Platform copy

Write distinct, native-sounding copy for each requested channel. Make it descriptive rather than a generic one-liner: connect a specific scene or audience need to one verified product fact and a natural next step. Do not reuse one caption with minor edits across channels. Use emojis intentionally when they support readability and fit the brand and platform; do not omit them by default in informal consumer-facing copy or add them mechanically.

Common adaptations when requested:

- Instagram: immediate hook, vivid scene, a natural save/comment prompt and a small set of relevant hashtags.
- Facebook: warmer context, a conversational explanation and a useful next step or link.
- YouTube: searchable title and a fuller description that summarizes the story, states the verified fact and gives a clear next step.
- Stories: concise on-screen copy with legible hierarchy; follow the requested language split between production directions and publish-ready copy.
- Community posts: one clear question, poll or announcement with relevant context.

Do not claim views, reach, virality, sales lift or engagement without evidence.

## Competitor research

Research competitors only when the user requests it or it is part of the established recurring brief. Respect the exact competitor scope. Use a current official post, product page or support article when possible; cite the direct source and date. Extract one concrete creative lesson, not just a feature summary. Label interpretation as an editorial lesson. Do not broaden into other brands or make performance claims without evidence.

Browse for current, niche, legal, regulatory, product or market information when accuracy depends on it. Prefer official sources for product claims and local regulations. If a claim's legality or meaning is uncertain, avoid using it until verified.

## File and automation boundaries

- Save files only when requested or clearly part of the established project workflow, and only in an authorized writable location.
- Never say a document was saved unless the file was actually written and verified. If the project location is read-only or unavailable, explain that the work is delivered in chat and identify the access limitation.
- Treat creating or changing a recurring automation as a separate action. Do it only when the user requests or clearly authorizes an ongoing schedule. Prefer updating an existing automation over creating a duplicate.
- Do not publish, send, upload or contact others unless the user explicitly authorized that destination and action.

## Final quality check

Check the following for the deliverables in scope:

- The package uses the current episode and weekly beat without repeating recent material.
- Story timings are continuous and match the target duration.
- The opening hook, product role, turning point and payoff are clear.
- Every product claim matches supplied or cited evidence.
- Brand assets, slogan, end frame and restricted claims follow the latest user instructions.
- Platform copy is distinct, descriptive and appropriately localized.
- Competitor citations support the stated observation.
- Any file or media operation is accurately reported.
