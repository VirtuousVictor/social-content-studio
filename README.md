# Social Content Studio

A self-contained agent skill for fact-checked social content strategy, short-form video storytelling, storyboards, image and video prompts, platform copy, and recurring content calendars.

**Social Content Studio** is a reusable workflow for Codex and supported ChatGPT Skills environments. The package consolidates the professional TVC methods, references, and templates into one Skill folder; it does not require installing separate TVC Skills.

[中文使用说明 / Chinese usage guide](USAGE.md)

## What it does

- Builds or updates a product profile from the user's brief, files, and confirmed facts.
- Develops campaign briefs, concepts, director treatments, and visual directions when the task needs them.
- Writes story-driven short-form scripts, timed storyboards, and continuity-aware image or video prompts.
- Adapts copy for Instagram, Facebook, YouTube, Stories, and recurring content calendars.
- Checks claims, platform requirements, safety constraints, and continuity before delivery.
- Interprets review feedback and prepares revisions or production handoffs when requested.

For a new product, the Skill gathers essential missing information before the first campaign. For an established product, it carries forward confirmed preferences and asks only about gaps that affect the current work.

## Install in Codex

Install the packaged `social-content-studio.zip` or clone this repository into a folder named `social-content-studio`. If you use GitHub’s **Code → Download ZIP**, rename the extracted source folder to `social-content-studio` before placing it in your skills directory. On Windows, the installed entrypoint should be here:

```text
%USERPROFILE%\.agents\skills\social-content-studio\SKILL.md
```

The packaged ZIP already contains the folder with the correct name. Extract it to the skills directory shown above, then open a new Codex session and invoke the skill:

```text
$social-content-studio
```

For an existing installation, update the folder where that installation already lives. Some installations use `~/.codex/skills`. Keep one copy in the set of directories your client scans. If the Skill is not discovered, confirm that `SKILL.md` is directly inside the `social-content-studio` folder and start a new session.

## Use in ChatGPT

ChatGPT Skills are installed separately from Codex Skills. In an eligible ChatGPT workspace, open **Plugins → Skills → Create → Upload from your computer**, upload the Skill package as the interface allows, and complete the security scan and installation. Availability and upload permissions depend on the account plan, product rollout, and workspace administrator settings. Once installed, type `@` and select `social-content-studio`. See the [official ChatGPT Skills guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

A regular GPT chat without Skills support will not discover the Skill merely because its ZIP was extracted. A file upload in one chat may provide temporary reference material, but it does not install a persistent Skill.

## Workflow

1. Review the conversation, product materials, brand preferences, and latest content.
2. Verify the product baseline and ask once for essential missing details.
3. Select only the relevant internal stages: brief, concept, director treatment, storyboard, prompts, platform copy, review, or production handoff.
4. For video, establish the protagonist, goal, obstacle, product-linked turning point, and payoff before writing shots.
5. Check facts, timing, continuity, brand requirements, and output format before delivery.

Routine social posts do not need the full TVC production process. Detailed methods are loaded from the complete manuals in `references/` as needed.

## Included files

- One active entrypoint: `SKILL.md`.
- Complete workflow manuals in `references/` for brief strategy, concepts, cinematic direction, visual assets, storyboards, video prompts, and production review.
- One consolidated full-text library containing all 54 Markdown source documents from 13 specialist Skill sources, including the complete Seedance TVC method set and all eight original templates; the original separate Skill folders are not required.
- A [source inventory](references/full-source-inventory.md) and [capability map](references/capability-crosswalk.md). The package includes the original 31 Seedance evaluation cases as offline review data.
- Reusable templates in `assets/templates/`.
- Two optional TSV-to-CSV/XLSX conversion scripts in `scripts/`.
- Three upstream MIT notices and a [source attribution table](THIRD_PARTY_NOTICES.md).

The full-text source library is about 415 KB when extracted. Markdown compresses heavily in ZIP archives, so the compressed ZIP size is not a measure of how much source material is included.

## Tool requirements and boundaries

This Skill provides written methods, prompts, and local templates. It does not bundle an image or video model, renderer, API client, credentials, or external service. Actual image or video generation requires a compatible tool in the host environment. Without one, the Skill can prepare prompts and production instructions.

The conversion scripts only turn TSV data into CSV or XLSX; they do not generate media or call model APIs. The Skill does not publish content or contact third parties.

## License

Social Content Studio is distributed under the [MIT License](LICENSE). See the [third-party notices](THIRD_PARTY_NOTICES.md) for upstream authors, versions and copyright notices.

## Official documentation

- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Skill invocation and installation locations](https://learn.chatgpt.com/docs/build-skills)
- [Codex Skills evaluation guide](https://developers.openai.com/blog/eval-skills)