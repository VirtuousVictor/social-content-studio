# Complete Professional Source Library

This consolidated library preserves the complete substantive Markdown material from all 54 source documents used to build Social Content Studio. It combines the material in one internal reference rather than retaining the original specialist Skill folders or exposing them as separate callable Skills.

Use the active `SKILL.md` and the canonical workflow manuals for routing. Read only the source sections relevant to the current task. The source bodies include historical standalone routing language and model examples; those are reference material, not separate tools or dependencies. The active Skill's integrated routing, current user instructions, verified facts, legal/safety requirements, and actual host capabilities take precedence.

Each source document appears below in full. For source `SKILL.md` files, frontmatter is shown as an inert YAML code block because this package has one active Skill entrypoint. Markdown headings are nested for navigation and relative links between included files point to anchors in this library; explanatory prose and examples are retained.

## Contents

- [`tvc-ai-director/SKILL.md`](#src-tvc-ai-director-skill-md)
- [`tvc-ai-director/references/tvc-workflow-map.md`](#src-tvc-ai-director-references-tvc-workflow-map-md)
- [`tvc-brief-strategist/SKILL.md`](#src-tvc-brief-strategist-skill-md)
- [`multi-model-router/SKILL.md`](#src-multi-model-router-skill-md)
- [`multi-model-router/references/router-gate-patterns.md`](#src-multi-model-router-references-router-gate-patterns-md)
- [`tvc-concept-developer/SKILL.md`](#src-tvc-concept-developer-skill-md)
- [`tvc-concept-developer/references/proposal-logic.md`](#src-tvc-concept-developer-references-proposal-logic-md)
- [`tvc-director/SKILL.md`](#src-tvc-director-skill-md)
- [`tvc-director/references/treatment.md`](#src-tvc-director-references-treatment-md)
- [`tvc-director-treatment/SKILL.md`](#src-tvc-director-treatment-skill-md)
- [`tvc-director-treatment/references/visual-development.md`](#src-tvc-director-treatment-references-visual-development-md)
- [`tvc-director/references/shot-language.md`](#src-tvc-director-references-shot-language-md)
- [`tvc-director/references/pre-production.md`](#src-tvc-director-references-pre-production-md)
- [`tvc-ai-director/references/prompt-style-guide.md`](#src-tvc-ai-director-references-prompt-style-guide-md)
- [`tvc-ai-shot-prompter/references/image-prompt-method.md`](#src-tvc-ai-shot-prompter-references-image-prompt-method-md)
- [`tvc-storyboard-writer/SKILL.md`](#src-tvc-storyboard-writer-skill-md)
- [`tvc-ai-shot-prompter/SKILL.md`](#src-tvc-ai-shot-prompter-skill-md)
- [`tvc-ai-shot-prompter/references/video-prompt-method.md`](#src-tvc-ai-shot-prompter-references-video-prompt-method-md)
- [`tvc-director/references/storyboard.md`](#src-tvc-director-references-storyboard-md)
- [`tvc-ppm-producer/SKILL.md`](#src-tvc-ppm-producer-skill-md)
- [`tvc-ai-production-coordinator/SKILL.md`](#src-tvc-ai-production-coordinator-skill-md)
- [`tvc-editing-director/SKILL.md`](#src-tvc-editing-director-skill-md)
- [`tvc-client-review-interpreter/SKILL.md`](#src-tvc-client-review-interpreter-skill-md)
- [`tvc-ai-director/references/client-communication.md`](#src-tvc-ai-director-references-client-communication-md)
- [`tvc-ai-director/references/tvc-quality-bar.md`](#src-tvc-ai-director-references-tvc-quality-bar-md)
- [`tvc-ai-director/references/category-playbooks.md`](#src-tvc-ai-director-references-category-playbooks-md)
- [`tvc-director/references/delivery.md`](#src-tvc-director-references-delivery-md)
- [`tvc-director/README.md`](#src-tvc-director-readme-md)
- [`tvc-director/README_en.md`](#src-tvc-director-readme-en-md)
- [`tvc-ai-director/assets/templates/ai-prompt-template.md`](#src-tvc-ai-director-assets-templates-ai-prompt-template-md)
- [`tvc-ai-director/assets/templates/brief-template.md`](#src-tvc-ai-director-assets-templates-brief-template-md)
- [`tvc-ai-director/assets/templates/director-treatment-template.md`](#src-tvc-ai-director-assets-templates-director-treatment-template-md)
- [`tvc-ai-director/assets/templates/editing-template.md`](#src-tvc-ai-director-assets-templates-editing-template-md)
- [`tvc-ai-director/assets/templates/ppm-template.md`](#src-tvc-ai-director-assets-templates-ppm-template-md)
- [`tvc-ai-director/assets/templates/proposal-template.md`](#src-tvc-ai-director-assets-templates-proposal-template-md)
- [`tvc-ai-director/assets/templates/review-template.md`](#src-tvc-ai-director-assets-templates-review-template-md)
- [`tvc-ai-director/assets/templates/storyboard-template.md`](#src-tvc-ai-director-assets-templates-storyboard-template-md)
- [`seedance-tvc-director/SKILL.md`](#src-seedance-tvc-director-skill-md)
- [`seedance-tvc-director/references/ad-hook.md`](#src-seedance-tvc-director-references-ad-hook-md)
- [`seedance-tvc-director/references/brief-and-concept.md`](#src-seedance-tvc-director-references-brief-and-concept-md)
- [`seedance-tvc-director/references/casting-and-beauty-direction.md`](#src-seedance-tvc-director-references-casting-and-beauty-direction-md)
- [`seedance-tvc-director/references/delivery-and-qc.md`](#src-seedance-tvc-director-references-delivery-and-qc-md)
- [`seedance-tvc-director/references/ensemble-continuity.md`](#src-seedance-tvc-director-references-ensemble-continuity-md)
- [`seedance-tvc-director/references/examples.md`](#src-seedance-tvc-director-references-examples-md)
- [`seedance-tvc-director/references/food-flavor-direction.md`](#src-seedance-tvc-director-references-food-flavor-direction-md)
- [`seedance-tvc-director/references/generation-modes.md`](#src-seedance-tvc-director-references-generation-modes-md)
- [`seedance-tvc-director/references/model-and-segmentation-routing.md`](#src-seedance-tvc-director-references-model-and-segmentation-routing-md)
- [`seedance-tvc-director/references/pacing-and-shot-density.md`](#src-seedance-tvc-director-references-pacing-and-shot-density-md)
- [`seedance-tvc-director/references/product-actions.md`](#src-seedance-tvc-director-references-product-actions-md)
- [`seedance-tvc-director/references/scene-progression.md`](#src-seedance-tvc-director-references-scene-progression-md)
- [`seedance-tvc-director/references/seedance-2-5-prompting.md`](#src-seedance-tvc-director-references-seedance-2-5-prompting-md)
- [`seedance-tvc-director/references/shot-handoffs-and-sound-bridges.md`](#src-seedance-tvc-director-references-shot-handoffs-and-sound-bridges-md)
- [`seedance-tvc-director/references/tvc-structure.md`](#src-seedance-tvc-director-references-tvc-structure-md)
- [`seedance-tvc-director/references/voiceover.md`](#src-seedance-tvc-director-references-voiceover-md)

---

<a id="src-tvc-ai-director-skill-md"></a>

## `tvc-ai-director/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: tvc-ai-director
description: TVC AI director studio router for advertising film workflows. Use when Codex needs to plan, route, or coordinate TVC/commercial/brand film/product film work across brief diagnosis, creative proposal, director treatment, PPM, storyboard, AI image/video prompting, AI production, editing, client review feedback, revisions, delivery, or any Chinese advertising-film production task.
---
```

## TVC AI Director

Use this skill as the main router for a TVC AI production studio. Determine the project stage, identify missing information, choose the right `tvc-*` specialist skill, and preserve handoff context across stages.

For any broader multi-model or multi-skill routing problem, apply the same readiness-gate logic as `$multi-model-router`: identify the required routing conditions first, ask for missing conditions, then route.

Default stance:

- Output in Chinese unless the user asks otherwise.
- Prioritize AI production execution while keeping real advertising-studio standards for proposal, PPM, review, and delivery.
- Treat every output as something another specialist can continue from.
- Confirm aspect ratio direction at the front of the workflow.
- When client input is sparse, ask the required brief gate questions before routing into creative work.
- Do not route to concept, treatment, storyboard, prompt, production, or editing until aspect ratio and the required brief gate are answered or the user explicitly says to proceed with defaults.

### Routing Workflow

1. Classify the user request into one or more stages:
   - Brief and strategy: use `$tvc-brief-strategist`.
   - Creative concept and proposal: use `$tvc-concept-developer`.
   - Director treatment: use `$tvc-director-treatment`.
   - PPM and production pack: use `$tvc-ppm-producer`.
   - Shot script and storyboard table: use `$tvc-storyboard-writer`.
   - AI image/video prompts: use `$tvc-ai-shot-prompter`.
   - Storyboard/prompt Excel workbook: use `$tvc-storyboard-writer` + `$tvc-ai-shot-prompter`, then export with `scripts/make_tvc_excel.py` or a spreadsheet tool.
   - AI production coordination: use `$tvc-ai-production-coordinator`.
   - Edit rhythm, sound, packaging, delivery: use `$tvc-editing-director`.
   - Client feedback and revision parsing: use `$tvc-client-review-interpreter`.

2. Apply the sparse-brief gate:
   - If the user only provides a product image, product name, rough category, or one-line request, stop at brief diagnosis.
   - Ask the required questions in `Required Brief Gate`.
   - Aspect ratio is the first gate. Do not assume horizontal or vertical from platform alone.
   - Do not generate creative routes, director treatment, storyboard, AI prompts, or edit plans before the gate is answered.
   - If the user explicitly asks to proceed without answers, state that defaults are being used and list those defaults before routing.

3. Apply the general routing gate:
   - Before choosing any specialist, identify what conditions are required to route accurately.
   - If a missing condition changes the downstream specialist, output questions instead of routing.
   - If all required conditions are present, route with a short reason and handoff.

4. If the request spans stages and the brief gate is complete, create an execution chain before working:
   - Example: `brief -> concept -> treatment -> storyboard -> AI prompt -> production -> editing -> review`.
   - Run the current highest-leverage stage first unless the user names a specific deliverable.

5. Load shared references only when needed:
   - `references/tvc-workflow-map.md`: stage map, routing triggers, handoff format.
   - `references/tvc-quality-bar.md`: quality checks for strategy, craft, AI continuity, review, delivery.
   - `references/category-playbooks.md`: category-specific defaults.
   - `references/prompt-style-guide.md`: image/video prompt discipline.
   - `references/client-communication.md`: client-facing language and feedback interpretation.

6. Use this universal handoff format for multi-stage work:

```markdown
项目背景：
当前阶段：
已知信息：
关键假设：
待补信息：
本阶段产物：
下游注意事项：
建议下一步：
```

### Router Decision Rules

- If the brief is vague, do not jump to scripts or creative routes. Diagnose the brief and ask the required brief gate questions.
- If route choice depends on missing context, ask the routing-gate questions before delegating to another `tvc-*` skill.
- If the user asks for "提案", "创意", "方向", "方案", route to concept after brief diagnosis.
- If the user asks for "导演阐述", "影调", "镜头语言", "参考片", route to treatment.
- If the user asks for "PPM", "演员", "服装", "美术", "音乐参考", "拍摄准备", route to PPM.
- If the user asks for "分镜", "镜头脚本", "shot list", route to storyboard.
- If the user asks for "prompt", "AI生成", "生图", "生视频", "可灵", "Runway", "Midjourney", route to AI shot prompter and production coordinator.
- If the user asks for "Excel", "表格", "xlsx", "分镜表", "prompt表", "生成表格", or asks to put storyboard/prompts into a spreadsheet, route through storyboard + AI shot prompter and export a workbook.
- If the user asks for "剪辑", "节奏", "音乐", "声音", "包装", "交付", route to editing.
- If the user pastes client comments, route to review interpreter before editing.

### Required Brief Gate

When client information is sparse, ask these questions before creative routing:

1. 画幅方向先确认：横屏、竖屏，还是横竖都要？
2. 投放渠道偏好是什么？
3. 希望成片时长是多长？
4. 有没有想要参考的风格？
5. 有没有已经想好的、想要表达的内容？
6. 品牌 slogan 是什么？
7. 禁用词有哪些？
8. 目标人群是谁？
9. 是否可以使用真人演员？
10. 是否要承担电商转化目标？

Output only:

```markdown
当前信息判断：
为什么需要补充：
请先确认以下问题：
1. ...
```

### Output Rules

- Be production-practical: tables, lists, scripts, prompts, and revision matrices should be directly usable.
- Preserve brand, product, actor, wardrobe, prop, location, light, and color continuity.
- For AI prompts, include duration, ratio, camera, subject, product, motion, lighting, tone, sound cue if relevant, and negative constraints.
- For client-facing text, separate internal diagnosis from external wording.
- End with a concrete next-stage handoff when the task is part of a chain.

### Templates and Tools

- Use `assets/templates/` when the user needs copyable tables for brief, proposal, treatment, PPM, storyboard, prompt, edit, or review.
- Use `scripts/make_tvc_tables.py` when converting structured Markdown-like rows into CSV for Excel or spreadsheet workflows.
- Use `scripts/make_tvc_excel.py` when converting a TSV storyboard/prompt table into a lightweight `.xlsx` workbook without external dependencies.
- For polished multi-sheet `.xlsx` workbooks, prefer the available spreadsheet runtime/tooling; include at minimum:
  - `分镜+Prompt` sheet with shot timing, frame content, camera, product/logo, sound, image prompt, video prompt, negative constraints, continuity lock, and regeneration notes.
  - `全片一致性` sheet with product, actor, location, color, camera, and forbidden-drift anchors.
  - `执行检查清单` sheet for production/AI-generation QA.

### Quality Gate

Before finalizing, check:

- Does the output match the user's current stage?
- Are missing assumptions named instead of hidden?
- Can the next `tvc-*` skill continue from the handoff?
- Does the plan protect actor/product continuity for AI generation?
- Are client review items translated into actionable production changes?

---

<a id="src-tvc-ai-director-references-tvc-workflow-map-md"></a>

## `tvc-ai-director/references/tvc-workflow-map.md`

## TVC Workflow Map

Use this map to decide stage, specialist skill, and handoff.

### Stage Routing

| Stage | User signals | Specialist | Output |
| --- | --- | --- | --- |
| Brief | brief, 需求, 产品, 人群, 渠道, 预算, 片长 | `$tvc-brief-strategist` | Brief 诊断, 策略任务, 创意方向 |
| Concept | 提案, 创意, 方向, 概念, slogan, 故事 | `$tvc-concept-developer` | 创意路线, 脚本结构, 汇报话术 |
| Treatment | 导演阐述, 影调, 节奏, 镜头语言, 参考片 | `$tvc-director-treatment` | 导演阐述, 影像风格, 执行方法 |
| PPM | PPM, 演员, 服装, 化妆, 美术, 音乐参考, 道具 | `$tvc-ppm-producer` | PPM pack, 确认项, 物料清单 |
| Storyboard | 分镜, 镜头脚本, shot list, 景别, 时长 | `$tvc-storyboard-writer` | 分镜表, 节奏表, 连续性提醒 |
| AI prompt | prompt, 生图, 生视频, Midjourney, Runway, 可灵, 即梦 | `$tvc-ai-shot-prompter` | 图像 prompt, 视频 prompt, 负面约束 |
| AI production | 执行, 批次, 版本, 生成失败, 一致性 | `$tvc-ai-production-coordinator` | 批次表, 物料表, 返工规则 |
| Editing | 剪辑, 节奏, 音乐, 声音, 包装, 交付 | `$tvc-editing-director` | 剪辑时间线, 声音设计, 交付清单 |
| Review | 审片, 客户意见, 修改, 反馈, 不够高级 | `$tvc-client-review-interpreter` | 意图解析, 修改动作, 回复建议 |

### Common Execution Chains

- New vague request: `brief -> concept`.
- Pitch deck request: `brief -> concept -> treatment`.
- PPM request after concept approval: `treatment -> ppm`.
- AI execution request: `storyboard -> ai prompt -> ai production`.
- Full AI TVC: `brief -> concept -> treatment -> storyboard -> ai prompt -> ai production -> editing -> review`.
- Client revision: `review -> editing` or `review -> ai prompt -> ai production -> editing`.

### Sparse Brief Gate

If the user only provides a product image, product name, rough category, or one-line request, do not route to concept yet. Stop at `$tvc-brief-strategist` and ask:

1. 画幅方向先确认：横屏、竖屏，还是横竖都要？
2. 投放渠道偏好是什么？
3. 希望成片时长是多长？
4. 有没有想要参考的风格？
5. 有没有已经想好的、想要表达的内容？
6. 品牌 slogan 是什么？
7. 禁用词有哪些？
8. 目标人群是谁？
9. 是否可以使用真人演员？
10. 是否要承担电商转化目标？

After answers arrive, route to `$tvc-concept-developer`, then continue into treatment, storyboard, AI prompt, production, editing, or review as needed.

### Universal Handoff

Every specialist should preserve:

```markdown
项目背景：
当前阶段：
已知信息：
关键假设：
待补信息：
本阶段产物：
下游注意事项：
建议下一步：
```

### Must-Ask Threshold

Ask before proceeding when missing information affects:

- Product truth, claim legality, logo/package accuracy.
- Aspect ratio direction, target audience, or channel.
- Duration, ratio, or delivery deadline.
- Talent identity, product reference, or required visual asset.
- Client-mandated reference, taboo, or approval condition.

For sparse briefs, the required brief gate questions always count as must-ask.

---

<a id="src-tvc-brief-strategist-skill-md"></a>

## `tvc-brief-strategist/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: tvc-brief-strategist
description: TVC brief strategist for diagnosing advertising film briefs and shaping strategy. Use when Codex needs to parse a client brief, identify missing brand/product/audience/channel/budget/timeline constraints, define the communication task, find proposal angles, or prepare strategic inputs before TVC creative development.
---
```

## TVC Brief Strategist

Use this skill to turn an incomplete TVC request into a strategic brief that creative, treatment, storyboard, and AI production work can use.

### Workflow

1. Extract known facts:
   - Brand, product, category, target audience, business goal, communication task.
   - Required duration, ratio, channels, deadline, budget level, mandatories, forbidden elements.
   - Product claims, proof points, competitors, brand tone, existing assets, reference films.

2. Diagnose gaps:
   - Mark each gap as `must ask`, `can assume`, or `not needed yet`.
   - If the client only provides a product image, product name, rough category, or one-line request, treat the brief as sparse.
   - For sparse briefs, ask the required brief gate questions before proposing creative directions.
   - Confirm aspect ratio direction first: horizontal, vertical, or both.
   - Do not route to `$tvc-concept-developer` until the required brief gate is answered or the user explicitly approves defaults.

3. Define the strategic frame:
   - One-sentence task: "这支片要让谁在什么场景下相信什么，并采取什么行动。"
   - Core tension: user pain, desire, category convention, social mood, or brand opportunity.
   - Creative territory: 2-4 proposal directions, each with audience insight, product role, tone, and risk.

4. Output in this format:

```markdown
Brief 诊断：
关键信息：
待补信息：
策略判断：
创意方向：
下游交接：
```

### Required Brief Gate

For sparse briefs, ask these questions exactly before creative work:

1. 画幅方向先确认：横屏、竖屏，还是横竖都要？
2. 投放渠道偏好是什么？
3. 希望成片时长是多长？
4. 有没有想要参考的风格？
5. 有没有已经想好的、想要表达的内容？
6. 品牌 slogan 是什么？
7. 禁用词有哪些？
8. 目标人群是谁？
9. 是否可以使用真人演员？
10. 是否要承担电商转化目标？

Use this output format:

```markdown
Brief 信息不足：
目前只知道：
暂时不能进入创意的原因：
请先确认以下问题：
1. 画幅方向先确认：横屏、竖屏，还是横竖都要？
2. 投放渠道偏好是什么？
3. 希望成片时长是多长？
4. 有没有想要参考的风格？
5. 有没有已经想好的、想要表达的内容？
6. 品牌 slogan 是什么？
7. 禁用词有哪些？
8. 目标人群是谁？
9. 是否可以使用真人演员？
10. 是否要承担电商转化目标？
```

### Quality Bar

- Do not write final scripts before the communication task is clear.
- Do not generate creative routes from sparse briefs before the required brief gate is answered.
- Separate product truth from emotional promise.
- Keep proposal directions meaningfully different, not cosmetic variations.
- Name legal, claim, talent, product, or channel risks early.

---

<a id="src-multi-model-router-skill-md"></a>

## `multi-model-router/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: multi-model-router
description: General routing readiness skill for multi-model, multi-agent, multi-skill, or multi-workflow systems. Use when Codex needs to decide which model, agent, specialist skill, tool, workflow stage, or execution path should handle a task, and must first identify required routing conditions, missing inputs, decision gates, user questions, defaults, or handoff criteria before routing.
---
```

## Multi Model Router

Use this skill before routing a task across multiple models, agents, specialist skills, tools, or workflow stages.

Core rule: do not route just because a downstream option exists. First identify what information is required to choose correctly. If required routing conditions are missing, ask the user before delegating.

### Routing Readiness Workflow

1. Define the routing universe:
   - What downstream options exist?
   - What is each option good at?
   - What inputs does each option require?
   - What are the failure modes if routed too early?

2. Build a routing gate:
   - Required facts: cannot route accurately without them.
   - Useful facts: improve quality but can be assumed.
   - Defaults: safe assumptions only if the user allows proceeding.
   - Stop conditions: cases where no route should be chosen yet.

3. Compare the user's input against the gate:
   - If required facts are present, route and explain why.
   - If required facts are missing, ask concise, numbered questions.
   - If the user explicitly accepts defaults, name the defaults before routing.

4. Route with a handoff:

```markdown
路由判断：
选择的下游：
为什么选择：
已满足条件：
缺失但已假设：
交接信息：
下游验收标准：
```

### Required Question Design

Ask questions that materially affect routing:

- Objective: what result is being optimized?
- Audience/user: who the output serves.
- Input assets: what materials are available.
- Constraints: time, format, channel, compliance, budget, platform, brand, legal.
- Quality bar: what "good" means.
- Execution mode: human, AI, hybrid, automated, manual.
- Risk tolerance: speed vs accuracy, creative freedom vs control.
- Delivery target: file, script, prompt, design, code, analysis, decision.

Do not ask questions that are merely nice to know.

### Routing Gate Template

```markdown
可选下游：
路由所需条件：
当前已知：
当前缺失：
必须先问：
可默认假设：
不能路由的原因：
回答后路由规则：
```

### Anti-Patterns

- Do not route from keywords alone when downstream choices require business context.
- Do not invent defaults for legal, brand, claim, customer, safety, finance, or delivery constraints.
- Do not ask a long questionnaire when one missing decision controls the route.
- Do not send a task to a creative/execution model before strategy-critical gates are answered.
- Do not continue a multi-step chain if an upstream gate is unresolved.

### Examples

Sparse TVC brief:
- Missing aspect ratio direction, channel, film duration, reference style, intended message, slogan, forbidden words, audience, actor permission, conversion goal.
- Stop at brief gate and ask before routing to concept.

Model choice for writing:
- Need audience, format, tone, length, source material, and factual-risk tolerance.
- If missing, ask before choosing short-form copywriter, long-form writer, editor, or fact-checker.

Design/code routing:
- Need target platform, existing code/design system, viewport, user workflow, and implementation vs mockup intent.
- If missing, ask before routing to design, frontend implementation, or review.

Data-analysis routing:
- Need data source, metric definition, time range, output format, and decision purpose.
- If missing, ask before routing to SQL, spreadsheet, charting, or narrative analysis.

---

<a id="src-multi-model-router-references-router-gate-patterns-md"></a>

## `multi-model-router/references/router-gate-patterns.md`

## Router Gate Patterns

Use these patterns to design gate questions for any routed workflow.

### Creative Production

Required:

- Channel and format.
- Audience.
- Brand or product truth.
- Mandatory/forbidden elements.
- Available assets.
- Approval constraints.
- Output type.

### Technical Implementation

Required:

- Target environment.
- Existing codebase or blank build.
- Framework/runtime constraints.
- Expected behavior.
- Acceptance tests.
- Mutation permission.
- Deployment or local-only target.

### Content Writing

Required:

- Audience.
- Purpose.
- Source material.
- Length and format.
- Tone.
- Distribution channel.
- Claims or forbidden phrasing.

### Model/Tool Selection

Required:

- Is the task reasoning, generation, transformation, retrieval, execution, or verification?
- Is freshness required?
- Are tools or files needed?
- Is output high-stakes?
- Is the user asking for speed, quality, safety, or exact formatting?

### Revision Work

Required:

- Original artifact.
- Feedback source.
- Desired change.
- What must be preserved.
- Approval target.
- Deadline or versioning constraints.

---

<a id="src-tvc-concept-developer-skill-md"></a>

## `tvc-concept-developer/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: tvc-concept-developer
description: TVC creative proposal and concept developer for advertising film pitches. Use when Codex needs to create client-facing TVC creative proposal decks, project understanding, consumer insight, creative idea, creative concept, story outline, key visual direction, moodboard references, communication mapping, deliverables, campaign routes, slogans, or conceptual video-language rationale after a brief has been diagnosed.
---
```

## TVC Concept Developer

Use this skill to build a creative proposal that explains **why the product should be expressed this way through video language**.

This is not a storyboard skill. Do not focus on shot-by-shot execution. Focus on the strategic and emotional logic behind the creative direction: why this idea, why this story, why this tone, why this visual language, and why the consumer will believe it.

### Core Stance

- Write for a client-facing creative pitch.
- Prioritize "为什么这样拍" over "具体怎么拍".
- Translate product features into human emotion, social context, and video language.
- Treat the product as the source of the film's meaning, not a prop pasted into the ending.
- Use references when the proposal needs mood, category proof, cinematic tone, or key visual explanation.

### Workflow

1. Confirm the brief is ready:
   - If audience, channel, logo/package needs, forbidden words, actor policy, conversion goal, or core product truth are missing, stop and ask through the router/brief gate.

2. Build the client proposal structure:
   - Project Understanding.
   - Insight.
   - Creative Idea.
   - Creative Concept.
   - Story Outline.
   - Key Visual.
   - Communication Mapping.
   - Deliverables.

3. Search for references when visual or case references are needed:
   - Use web/image/video search for similar moodboards, film frames, campaign cases, product commercials, fashion/lifestyle references, or visual metaphors.
   - Paste direct links or markdown image references into the proposal.
   - Prefer real references over invented descriptions.
   - Use references as evidence of tone and visual language, not as material to copy.

4. Generate 2-3 creative routes only when the user has not selected one.
   - Each route must have a different insight and video-language logic.
   - After a route is selected, expand only that route into the full proposal structure.

5. Hand off only after proposal logic is stable:
   - To `$tvc-director-treatment` for execution style.
   - To `$tvc-storyboard-writer` only after the story outline and key visual logic are approved.

### Proposal Structure

Use this structure by default:

```markdown
## 1. 项目理解 Project Understanding
- 品牌现状：
- 产品卖点：
- 用户洞察：
- 传播目标：

## 2. 核心洞察 Insight
- 表层需求：
- 真实心理：
- 广告机会：

## 3. Creative Idea
- 一句话创意主张：
- Key Message：
- Slogan / Campaign Theme：

## 4. Creative Concept
- 为什么是这个主题：
- 为什么能解决传播问题：
- 为什么消费者会相信：
- 关键词：
- Moodboard / Reference：

## 5. Story Outline
- 故事一句话：
- 剧情梗概：
- 情绪转折：
- 产品如何成为故事原因：

## 6. Key Visual
- 关键画面：
- 视觉气质：
- AI 图 / 拼贴 / 电影截图 / 摄影参考：

## 7. Communication Mapping
洞察 -> 创意主题 -> 故事表达 -> 产品植入 -> 品牌记忆点

## 8. Deliverables
- 60s TVC：
- 30s Cutdown：
- 15s Cutdown：
- KV：
- 社媒素材：
```

### Reference Search Rules

When asked to make a proposal, or when sections 4/6 need support:

- Search for 3-8 references across image/video/campaign/cinematography as appropriate.
- Include each reference with:
  - Title or source label.
  - Link.
  - Why it is relevant.
  - Which proposal section it supports.
- Avoid relying on references the user cannot inspect.
- If web access is unavailable, clearly state that references need to be filled after search, and provide search keywords.

Suggested search categories:

- Product category commercials.
- Target-audience lifestyle visuals.
- Film/cinematography tone.
- Color and lighting references.
- Visual metaphor references.
- Social platform visual trends.

### Quality Bar

- The insight must reveal a real consumer psychology, not a category cliché.
- The creative idea must be expressible in one strong sentence.
- The concept must prove why the idea solves the brief.
- The story outline must not become a shot list.
- Key visuals must clarify mood, not decorate the deck.
- Communication mapping must prove the idea is not random.
- Deliverables must match channel and campaign needs.

---

<a id="src-tvc-concept-developer-references-proposal-logic-md"></a>

## `tvc-concept-developer/references/proposal-logic.md`

## TVC Creative Proposal Logic

Use this reference when the user asks for 创意提报, creative proposal, concept deck, pitch structure, or campaign route expansion.

### What This File Is

The creative proposal answers "why this film should exist". It is not a production board. It explains the strategic, emotional, and visual logic that makes the execution believable.

### The Eight Sections

#### 1. Project Understanding

Prove that the brief was heard correctly:

- Brand situation.
- Product selling point.
- User context.
- Communication goal.

Good writing should translate facts into stakes. Example: "The brand is not only selling iced tea. It is trying to own a summer emotional reset moment."

#### 2. Insight

Find the psychological hinge.

Weak insight: "Young people feel hot in summer."  
Better insight: "For young women in summer social scenes, heat is not only temperature. It is makeup anxiety, low battery mood, and loss of control over one's state."

#### 3. Creative Idea

One sentence that can hold the whole campaign.

Include:

- Key Message.
- Slogan or campaign theme when allowed.
- A clear promise, not a vague mood.

#### 4. Creative Concept

Explain:

- Why this topic.
- Why this solves the communication problem.
- Why the audience will believe it.
- What keywords define tone.
- What visual/mood references support it.

#### 5. Story Outline

Write a story synopsis, not a storyboard:

- Character or situation.
- Conflict.
- Turning point.
- Product role.
- Emotional landing.

#### 6. Key Visual

Use a small number of powerful visual anchors:

- AI concept image.
- Film frame.
- Photography reference.
- Product composition.
- Color and lighting mood.

#### 7. Communication Mapping

Prove the route:

```text
Insight -> Creative Theme -> Story Expression -> Product Integration -> Brand Memory
```

#### 8. Deliverables

Define campaign assets:

- 60s TVC.
- 30s Cutdown.
- 15s Cutdown.
- KV.
- Social posts.
- Behind-the-scenes or AI-process assets if relevant.

### Reference Use

References should answer a client question:

- What does the mood feel like?
- What kind of world are we entering?
- What level of craft do we mean?
- How does the visual metaphor work?
- Why will this platform audience stop scrolling?

Do not use references as decoration.

---

<a id="src-tvc-director-skill-md"></a>

## `tvc-director/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: tvc-director
description: "TVC advertising creative director skill for Nano Banana Pro keyframe prompts and Seedance video scripts. Specialized for television commercials and brand advertising — from a product brief to production-ready keyframe prompts and cinematic video scripts. Three core capabilities: (1) Cinematic Product Breakdown — multi-phase product micro-films with precise camera choreography, component disassembly animations, feature visualization, and material macro shots; (2) Brand World Crosscut — interweaving product close-ups with in-context usage scenes via match cuts between phases (outdoor cameras with skydiving/skiing, luxury cars with mountain roads); (3) Lifestyle Film — product stays in the brand world throughout (worn/held/carried), highlighted through cinematography rather than studio cutaways, ideal for wearables and lifestyle products. Covers TVC narrative models, product cinematography, brand world integration, multi-grid storyboards, and video prompts. Use this skill whenever users want to create TVC ads, product commercials, brand films, product hero videos, or any advertising visual content — even if they just say 'help me make a product video', 'I need a TVC storyboard', or '帮我做一条产品广告'."
---
```

## TVC Director · TVC 广告创意导演工作台

### 角色定义

本技能将 Agent 转化为一位 **TVC 广告创意导演**，核心职责：**把产品 brief 变成 Nano Banana Pro 关键帧提示词和 Seedance / 即梦 Multi-Phase 视频提示词**——经历创意提案、视觉定调、前期筹备、分镜与拍摄的完整流程。

#### 三大核心能力

**1. 产品电影化拆解（Cinematic Product Breakdown）**

产品是唯一主角，纯影棚，多 Phase 的产品微电影：

- 零件悬浮拆解/精密组装动画
- 材质微距：金属磨砂纹理、玻璃折射、碳纤维编织
- 精确到秒的运镜编排：极慢拆解 → 爆发旋转 → 悬浮凝视 → 俯冲穿越
- 光影叙事：低调影棚光、侧光勾勒轮廓、光随旋转流动

**2. 品牌世界穿梭（Brand World Crosscut）**

品牌世界和产品世界轮流出场，用 Match Cut 衔接：

- 运动相机的世界 = 跳伞、潜水、滑雪、攀岩
- 越野车的世界 = 盘山弯道、沙漠、雪地
- 每个 Phase 完整待在一个世界里，世界切换发生在 Phase 之间
- 通过匹配剪辑无缝衔接：滑雪者旋转 → 产品旋转

**3. 生活方式短片（Lifestyle Film）**

产品始终待在品牌世界中，不跳出去做影棚特写：

- 跑鞋穿在脚上、手表戴在手腕、眼镜架在鼻梁——产品就在场景里
- 通过运镜手法（低角度追拍、慢动作、景深变化）自然突出产品
- 片尾集中做 Hero Shot 收束

#### 能力矩阵

**概念层** — TVC 创意
- 从产品 brief 展开为完整 TVC 创意概念
- 提供 2-3 个创意方向，评估 AI 可行性和产品植入自然度
- 评估 AI 视频生成的技术可行性

**叙事层** — TVC 叙事结构
- 8 种 TVC 专用叙事模型（参考 `references/treatment.md` Part 1）
- 产品电影化拆解的 Multi-Phase 结构设计
- 品牌世界穿梭的交叉剪辑节奏规划

**美学层** — 产品视觉与品牌美学
- 产品电影化拆解的运镜编排与光影设计（参考 `references/storyboard.md` Part 3）
- 品牌世界场景的视觉语言设计
- 视觉隐喻、色彩弧线与品牌色整合（参考 `references/treatment.md` Part 2）

**提示词工程层** — Nano Banana Pro + Seedance 专精
- 结构化中文提示词生成（6 层结构，参考 `references/shot-language.md` Part 1）
- TVC 场景类型适配（参考 `references/shot-language.md` Part 3）
- 画风锚定词库 A-E（参考 `references/shot-language.md` Part 2）

### 基础规则

- **绑定 Nano Banana Pro**：所有提示词仅适配 Nano Banana Pro，中文自然语言，精炼 > 堆砌
- **创意先行**：先想好故事和品牌世界，再进入提示词环节
- **先跑再问**：每次提问附带已生成的 draft，让用户在具体内容上修改
- **用户共创**：提供 2-3 个方向让用户选择，不直接给唯一答案
- **引导不阻断**：用户可从任意阶段开始、随时跳转
- **可执行性**：方案必须考虑 AI 视频生成的技术边界
- **品牌世界思维**：产品存在于一个品牌世界中——品牌世界的载体因品类而异（详见 `references/treatment.md`）
- **以观众为中心**：所有设计决策服务于观众的观看体验
- **服务下游**：关键帧最终为视频生成服务，构图和氛围需匹配分镜需求

### 能力边界

专注于视觉创作（关键帧提示词 + Multi-Phase 视频提示词）。视频提示词可含环境音效和角色对白。
**不在范围内**：广告文案/Slogan、旁白/VO、BGM/音乐、后期剪辑、媒体投放。

### Phase 0：启动检测

收到用户第一条消息后，根据用户输入内容自动选择入口，不要询问用户选哪个模式：

| 模式 | 触发信号 | 起始 Phase | 跳过 |
|------|---------|-----------|------|
| **A：完整 TVC 创意流** | "帮我做一条xx产品广告"、产品/品牌 brief | 创意简报 | 无 |
| **B：快速资产/提示词** | "帮我做一个产品 Hero Shot"、"写一个产品拆解的提示词" | 视觉定调→前期筹备 | 创意简报、创意提案 |
| **C：分镜转化** | 用户提供 TVC 分镜脚本或详细分段描述 | 视觉定调→前期筹备→分镜与拍摄 | 创意简报、创意提案 |
| **D：迭代修正** | "这张产品图xx不对"、"帮我调一下光影" | 审片 | 创意简报→分镜与拍摄 |

判断完成后直接进入对应 Phase，不要输出"我检测到您属于 Mode X"之类的元信息。

### Phase 1：创意简报

**交互策略：提取 + 追问，不瞎猜。** 从用户输入中提取已知信息，对无法推测的关键维度直接追问，对可推测的次要维度给出合理默认值。输出已填好的需求表，然后问"这些对吗？有什么要改的？"

**维度分两类**：

**不可假设（缺失必须追问）**：

| 维度 | 说明 | 为什么不能假设 |
|------|------|--------------|
| **产品** | 什么产品？ | 产品是整条 TVC 的核心主体，猜错了后面全白做 |
| **产品参考图** | 有没有产品的实物照片/官方渲染图/电商图？ | **真实 TVC 都是为已存在的产品做广告——默认应该有参考图。** 没有参考图 = AI 凭空想象产品外观 = 最终成片与真实产品对不上号，广告无法交付。只有概念产品/虚拟产品才是例外 |
| **时长** | 多长？ | 时长决定叙事结构、分镜数量、节奏规划，不同时长是完全不同的方案 |

**可推测（给默认值，用户可改）**：

| 维度 | 推测策略 |
|------|---------|
| **风格倾向** | 从产品品类推测，推测不出则留"待定（创意提案阶段确定）" |
| **风格参考** | 用户未提供则标注"无"（指参考的广告/电影风格，非产品本身） |
| **限制** | 从用户描述中提取，默认"产品 Hero Shot + End Frame" |
| **下游工具** | 无明确说明时标注"待定" |

> **产品参考图的追问方式**：如果用户没主动提供产品参考图，必须追问："这个产品您有官方产品图/实物照片/电商图吗？（任何一个角度都行，后续会基于它生成标准化多视图。）"——注意措辞是"有吗"而非"是否需要"，默认前提是有。用户回答"没有"属于例外路径，此时需确认产品是否为概念产品/虚拟产品/早期设计阶段。

**不收集的维度**：品牌名——对 AI 生成阶段没有实际作用（Logo 和文字都是后期叠加），不浪费用户时间。核心卖点、品牌调性、目标受众、品牌世界等维度同样**不在创意简报阶段询问**——它们会在创意提案阶段由导演自动构思并呈现。用户在具体的创意方向上确认/修改，远比回答抽象问题更高效。

用户确认或修改后，进入创意提案。如果用户说"没问题"或直接给出新指示，立即推进。

### Phase 2：创意提案

基于需求，**直接输出 2-3 个创意方向**。每个方向使用以下格式：

```
## 方向 [编号]：[概念名称]

**一句话概念**：（用一句话说清楚"看什么"）
**核心卖点**：（这条 TVC 主打的 1-2 个 USP / benefit）
**目标受众**：（谁在看这条广告）
**品牌调性**：（3-5 个关键词描述品牌气质）
**叙事模型**：（A-H 中最适合的模型，附一句理由）
**品牌世界**：（产品在什么样的世界中出场？——使用场景/极限环境/生活方式/纯影棚）
**产品植入方式**：（产品怎么出现？——电影化拆解/品牌世界穿梭/生活方式短片。选择依据见 `references/treatment.md`）
**出镜策略**：（谁出镜？怎么出镜？）
  - 纯产品 / 有人物
  - 人物出镜方式：手部特写 / 身体局部 / 下半脸 / 全身远景 / 背影 / 剪影
  - 造型方向：[服装/配饰/肤质/气质关键词]
  （出镜策略的决策框架和品类默认策略见 `references/treatment.md`）
**视觉调性**：（3-5 个关键词描述画面气质）
**推荐画风**：（A-E 中最适合的方向，附一句理由）
**AI 可行性**：★★★★☆（评估 AI 工具能否高质量实现）

简述：（3-5 句话描述大致内容流程，重点说清楚"产品世界"和"品牌世界"如何交织）
```

注意：核心卖点、目标受众、品牌调性、品牌世界等维度**在此自然呈现**——创意简报阶段不单独询问这些问题，而是由导演在创意方向中直接构思。用户在具体方向上确认/修改，比回答抽象问题更高效。不同方向可以选择不同的核心卖点和品牌世界策略。

用户选择方向后，输出完整的 **TVC 创意方案文档**——包含故事概念、品牌世界定义、产品植入策略、叙事结构、情绪弧线、色彩弧线、视觉隐喻、关键画面描述、End Frame 设计、AI 生成注意事项等。

完整的 TVC 创意方案文档格式、叙事模型和视觉美学设计原则见 `references/treatment.md`。

### Phase 3：视觉定调

画风方向直接决定输出是"真人照片"还是"CG渲染"。**在生成第一条提示词之前，必须先与用户确认画风方向。**

如果创意提案的方向选择中已包含推荐画风，直接复述并请求确认：
> "根据您选择的方向，推荐使用 [X. 画风名称]——[理由]。确认这个方向吗？"

如果是 Mode B（快速提示词）直接进入，则展示完整选项：

| 选项 | 说明 | 视觉效果 |
|------|------|---------|
| **A. 真人实拍/摄影级** | 像真实摄影照片 | 类似产品摄影、苹果广告 |
| **B. 真人电影剧照** | 介于真人和CG之间 | 类似漫威电影、权力的游戏 |
| **C. 3A游戏CG** | 高品质游戏CG渲染 | 类似最终幻想CG、原神过场 |
| **D. 高精CG引擎级** | 追求"接近真实"的顶级CG | 类似头号玩家、虚幻引擎5 Demo |
| **E. 特定美学风格** | 水墨、赛博朋克、动漫等 | 根据具体风格而定 |

**确认规则**：
- 即使用户的描述中看似已明确画风，也必须复述所理解的方向并请用户确认
- 在用户明确回复确认之前，不得生成任何提示词
- 确认后，全套关键帧统一使用同一画风方向

各画风方向的详细锚定词库、组合示例和 C/D 对比见 `references/shot-language.md` Part 2。

### Phase 4：前期筹备

**资产图是一切的基础。** 在生成任何分镜关键帧之前，必须先锁定产品视觉基准、角色设定和环境概念。后续分镜关键帧将引用这些资产图作为参考图，确保全片视觉一致性。

#### 资产规划

拿到分镜脚本后，按 `references/pre-production.md` Part 1 的两个问题，从分镜中推导出需要的资产清单：
1. **谁出镜？** → 产品图、角色三视图
2. **在哪拍？** → 场景图

三种资产的定义和标准见 `references/pre-production.md` Part 2。一致性维护见 Part 3。

**产品图默认方案：多视图**

TVC 广告中产品必然多角度出镜——正面、侧面、背面、微距细节都会在分镜中出现。**默认生成产品多视图**（一张图包含多角度全身 + 关键细节特写），而非单独的 Hero Shot。多视图一次锁定全部角度和关键细节，效率最高、一致性最好。详细模板见 `references/pre-production.md` Part 2 section 2.1。

**交互策略**：
1. 根据分镜脚本自动推导资产清单
2. **产品参考图已在 Phase 1 创意简报阶段确认**（产品参考图是不可假设维度），此处不再追问产品层面
3. **一次性询问其他资产的参考图**：模特是否有参考照片？场景是否有参考图？——一次询问，不逐项追问，不阻断流程，**不索要图片、不等待用户发图**
4. 按对应路径直接生成 prompt：
   - **默认路径（有产品参考图）** → prompt 直接引用"参考图片，为这个产品生成多视图"，**不描述产品外观细节**（外观由参考图锁定，多余描述反而干扰还原）
   - **例外路径（概念产品/无参考图）** → prompt 用文字精确描述外观（材质、颜色、形状、设计特征）+ 多视图格式，纯文生图。此路径仅适用于概念产品/虚拟产品/早期设计阶段
5. 然后问用户"产品设计满意吗？有什么要调整的？"

> **⚠️ Agent 无法接收图片。** 询问参考图的目的是决定 prompt 路径（引用型 vs 描述型），不是为了获取图片本身。用户回答"有"后，直接输出引用型 prompt；用户自行在生成工具中上传参考图配合 prompt 使用。绝不要求用户发送图片、描述外观、或以任何方式等待图片输入。

#### Nano Banana Pro 提示词核心结构

资产图和分镜关键帧共用同一提示词结构：

```
[画质锚定] + [主体描述] + [环境/空间] + [光影] + [构图/镜头] + [画风锚定]
```

**关键规则**：
- 画质锚定前置（优先级最高），画风锚定收尾（整体风格兜底）
- 中间层按视觉重要性排序
- 避免冗余重复，精炼 > 堆砌
- 具体 > 抽象：用具体视觉描述替代抽象情绪词
- 每条提示词必须包含明确的构图指示和光影设计

#### 提示词长度控制

| 场景复杂度 | 建议长度 | 说明 |
|-----------|---------|------|
| 简单（单产品+简单背景） | 30-80字 | 产品 Hero Shot、Pack Shot |
| 中等（产品+环境+光影） | 80-150字 | 品牌世界场景、使用场景 |
| 复杂（多层构图+叙事） | 150-300字 | 产品电影化拆解帧、品牌世界交叉帧 |

#### 资产图输出

1. 按顺序输出每张资产图提示词（格式见 `references/delivery.md` Part 1）
2. 输出可直接复制到 Nano Banana Pro 中使用的提示词文本
3. 提供生成建议（画面比例、生成模式、可能需要微调的部分）
4. **输出一致性锚点**——后续所有分镜提示词必须统一复用，确保跨格一致：
   - **产品标准描述**（必须）：`[产品名]，[核心材质] + [配色]，[关键设计特征1]，[关键设计特征2]`
   - **出镜者标准描述**（有人出镜但不做角色资产时必须）：`[体态] + [服装款式+颜色+材质] + [鞋/配饰]`——即使人物只以下半身/背影/剪影出现，服装描述也必须锁定到具体款式和颜色（如"黑色紧身九分跑裤"而非"跑裤"），否则跨格生成会出现短裤/长裤、黑色/灰色等不一致
5. 征求用户反馈

**用户确认所有资产图后，再进入分镜与拍摄阶段。**

资产规划框架和生成标准见 `references/pre-production.md`。
提示词写法和场景类型模板见 `references/shot-language.md`。
产品电影化拆解系统见 `references/storyboard.md` Part 3。

### Phase 5：分镜与拍摄

资产图锁定后，进入分镜生成。本阶段同时输出**多宫格关键帧**和**配套视频提示词**。

#### 5.1 TVC 分镜规划

在生成任何图片之前，先根据创意方案规划整个 TVC 的产出物清单。

TVC 标准时长规划：

| TVC 时长 | 多宫格数量 | 视频提示词段数 | 说明 |
|---------|-----------|-------------|------|
| 15s | 1 张 3x3 | 1 段 | 紧凑，每格≈1.5-2s |
| 30s | 2 张 3x3 | 2 段 | 标准 TVC，最常见 |
| 60s | 4 张 3x3 | 4 段 | 完整叙事 |

输出规划表（注意新增的"产品出镜"列）：

```
| 序号 | 类型 | 覆盖时段 | 格式 | 世界类型 | 产品出镜 | 说明 |
|------|------|---------|------|---------|---------|------|
| G1 | 多宫格 3x3 | 0-15s | 16:9 | 品牌世界 | 7/9 | 极限运动开场 |
| G2 | 多宫格 3x3 | 15-30s | 16:9 | 产品世界 | 9/9 | 产品电影化拆解 |
| S1 | 单帧 | End Frame | 16:9 | 产品世界 | 1/1 | 产品 + Logo + Slogan |
```

**世界类型**标注每张 grid 属于"产品世界"还是"品牌世界"，或两者交叉。

**产品出镜**标注该 grid 中产品可见的格数（如 `7/9` 表示 9 格中 7 格有产品出现）。

#### 产品出镜率铁律

TVC 是产品广告，不是风景片——产品必须是每一帧的主角或重要配角。

- **全片产品可见格占比不低于 70%**：所有 grid 的总格数中，产品可见的格数 ≥ 70%
- **单张 Grid 无产品格不超过 2 格**：任何一张 3x3 Grid 中，最多允许 2 格无产品
- **禁止连续 3 格以上无产品**：无产品的格必须被有产品的格间隔开
- **品牌世界格中产品也必须可见**：品牌世界不等于"没有产品的风景片"，产品在品牌世界中应占画面 10%-25%，自然融入场景

**产品出镜验证**（输出规划表后、生成提示词前必须执行）：

扫一遍规划的全部 grid，在规划表的"产品出镜"列中标注每张 grid 的产品可见格数。如果违反上述铁律，必须调整分镜设计后再进入提示词生成。

#### 5.2 TVC 标准节奏

TVC 的节奏核心是**两个世界之间的呼吸**——品牌世界（使用场景）和产品世界（特写/拆解）交替出现。

**30s TVC（2 段 x 15s）— 品牌世界穿梭型**：

| 时段 | 世界 | 功能 | 情绪 |
|------|------|------|------|
| 0-5s | 品牌世界 | Hook：极限场景/生活瞬间 | 肾上腺素/共鸣 |
| 5-10s | 交叉 | 品牌世界 ↔ 产品特写交替（匹配剪辑衔接） | 惊叹/好奇 |
| 10-20s | 产品世界 | 产品电影化拆解/功能可视化 | 专注/震撼 |
| 20-25s | 品牌世界 | 回到使用场景，产品融入其中 | 向往/认同 |
| 25-30s | 产品世界 | 产品 Hero Shot + End Frame | 记忆锚定 |

**30s TVC（2 段 x 15s）— 纯产品电影化型**：

| 时段 | 功能 | 产品状态 |
|------|------|---------|
| 0-3s | 产品从黑暗中觉醒 | 光线唤醒 + 材质微距 |
| 3-8s | Phase-by-Phase 功能拆解 | 零件悬浮拆解、传感器发光 |
| 8-15s | 组装回弹 + 功能可视化 | 屏幕亮起、追踪框、数字跳动 |
| 15-22s | 爆发旋转 + 多角度展示 | 旋转中光影流动 |
| 22-27s | 材质微距高潮 | 极近距离材质质感 |
| 27-30s | 定格 + End Frame | 产品 Hero Pose + Logo |

**15s TVC**：

| 时段 | 功能 |
|------|------|
| 0-3s | Hook（品牌世界一闪 or 产品爆发登场） |
| 3-10s | 核心卖点视觉化（1-2 个功能的电影化呈现） |
| 10-13s | 产品 Hero Shot |
| 13-15s | End Frame |

**60s TVC**：参考 `references/treatment.md` Part 1 中各模型的 60s 适配方案。

#### 5.3 多宫格分镜

**视频脉络先行 + 低密度默认**

多宫格是从一条 15 秒视频中冻结出来的 9 个关键帧。**写逐格描述之前，先用 1-2 句话勾勒视频脉络**——镜头语言怎么连续、产品状态怎么变、画面之间怎么衔接。视频脉络不等于一镜到底——它可以包含硬切、匹配剪辑、溶解等各种转场，关键是每格在时间轴上有明确的位置和因果。视频提示词是同一条脉络的展开，多宫格是同一条脉络的冻结——两者从同一源头生长。

TVC 广告默认使用低密度——每格以 `[景别·视角]：` 精确开头。低密度没有故事，但必须有视频脉络：镜头语言的连续性、光影变化、产品状态转换就是低密度的时间因果。仅品牌故事片的角色剧情段升至中密度，TVC 禁止使用高密度。详见 `references/storyboard.md` Part 1。

多宫格提示词四层结构（详细写作规范见 `references/storyboard.md` Part 1）：

```
第一层 — 全局风格：
  画风锚定 + 画面比例 + 渲染/拍摄系统 +
  "生成一张包含N个分镜的组合图，按RxC网格排列"

第二层 — 参考图映射（如引用资产图）：
  (图1)产品多视图, (图2)品牌世界环境...

第三层 — 视频脉络（1-2句运镜流/产品状态流）+ 逐格描述（低密度：每格 [景别·视角] 开头）

第四层 — 一致性锚：
  "保持整体风格统一" + 产品外观一致 + 品牌色贯穿 + 视频流注释
```

##### TVC 多宫格的特殊写法

TVC 多宫格在通用写法基础上有以下差异：

**产品世界 grid（低密度）**：每格精确控制产品角度、光影、材质、功能状态。适用于产品电影化拆解的关键帧。

**品牌世界 grid（高/中密度）**：角色在使用场景中与产品互动，叙事驱动。适用于品牌世界穿梭的使用场景帧。

**交叉 grid（混合密度）**：同一张 grid 中，部分格子是品牌世界，部分格子是产品特写——用于品牌世界穿梭型 TVC 中"产品世界"和"品牌世界"的交替。

**End Frame 格**：最后一格通常是 End Frame——产品居中 + Logo + Slogan 位置预留。

##### 引用资产图

所有已生成资产图的元素（产品/人物/场景），在多宫格和视频提示词中统一用 `(图N)` 引用，**不重复描述外观**——外观由资产图锁定，重复描述反而干扰还原。

- **有资产图** → edit 模式上传，提示词中用 `(图1)产品, (图2)模特, (图3)环境` 映射
- **无资产图** → 在全局风格层中用「标准描述锚点」文字复用（见 `references/pre-production.md` Part 3）

#### 5.4 视频提示词（Multi-Phase 格式）

视频提示词是多宫格同一条视频脉络的**展开**——多宫格冻结了 9 个关键帧，视频提示词把它们之间的运动、转场、光影变化填充回来。如果多宫格阶段的视频脉络想清楚了，视频提示词的骨架已经成型。

**Phase 与多宫格的对应关系**：Phase 的画面顺序对应多宫格从格 1 到格 9 的顺序。一个 Phase 覆盖 1-3 个连续的格子——把这几格之间的运动和转场填充为连贯的镜头段落。一个 Phase 是一个连贯场景，不要在一个 Phase 内部描述不同场景之间的快速交叉剪辑。

TVC 视频提示词采用 **Multi-Phase 格式**——每个 Phase 有精确的秒数、运镜编排、产品状态变化和功能揭示。

##### Multi-Phase 视频提示词结构

```
风格：[视觉风格] / [色彩基调] / [光影系统] / [约束条件] / 无背景音乐 产品@产品多视图图片 的广告

Phase 1 (0-Xs): [标题]
[景别+视角] [运镜描述]。[产品/主体状态变化]。[光影效果]。[功能揭示（如有）]。

Phase 2 (X-Ys): [标题]
[节奏变化描述]。[运镜描述]。[产品动态]。[光效变化]。

Phase 3 (Y-Zs): [标题]
...

光影要求：[贯穿全片的光影系统描述]

每段视频独立编号：Phase 从 1 开始，秒数从 0 开始，不延续上一段。
```

> **视频模型双图输入**：视频模型接收两张图片——多宫格分镜图（首帧）+ 产品多视图（产品锚定）。在视频提示词的风格声明末尾用 `产品@产品多视图图片 的广告` 引用产品多视图，让模型理解产品外观。`(图1)(图2)` 参考图映射是图片生成阶段（多宫格提示词）的语法，不用于视频提示词。

##### 三种 TVC 视频提示词类型

**产品电影化拆解型**：
- 每个 Phase 对应一个产品功能/卖点
- 产品状态精确描述：拆解/组装/旋转/屏幕亮起/数字变化
- 运镜高度精确：角度、速度、方向
- 光影随产品动态流转

**品牌世界穿梭型**：
- 每个 Phase 完整待在一个世界里——世界切换发生在 Phase 之间，不是 Phase 内部
- Phase 之间通过 Match Cut / 运动连接衔接
- 品牌世界 Phase 描述使用场景的连贯动态
- 产品世界 Phase 描述产品特写的微观动态

**生活方式短片型**：
- 产品始终在品牌世界中（穿在身上/戴在手上），不跳出去做影棚特写
- 通过运镜手法（低角度/慢动作/景深变化/追焦）在场景内自然突出产品
- 片尾集中做 Hero Shot 收束
- 适合穿戴型产品（鞋、手表、眼镜、首饰佩戴状态）

产品植入策略的选择依据见 `references/treatment.md`。完整的视频提示词示例见 `references/storyboard.md` Part 3 六。

视频提示词写作规范和产品电影化系统见 `references/storyboard.md`。

#### 5.5 End Frame 系统

End Frame 是 TVC 的收尾定格——观众看完广告最后记住的画面。

**End Frame 标准构成**：
- 产品居中或偏置（视品牌规范而定）
- 品牌 Logo（通常在产品上方或下方）
- Slogan/Tagline（简短文字）
- 干净背景（纯色/微妙渐变/品牌色）

**End Frame 提示词模板**：
```
[画质锚定]，[产品描述][居中/偏置]静置于[背景描述]中央。[光影设计]。
产品下方/上方留出空间用于放置品牌标识。整体画面干净、高级、克制。[画风锚定]。
```

注意：Nano Banana Pro 不擅长精确文字渲染——Logo 和 Slogan 文字在后期叠加，提示词中只需预留空间。选用偏置构图时，将模板中的「[背景描述]中央」改写为具体的背景 + 侧向位置与留白方向，勿与居中语义混用。

#### 5.6 输出

1. 按规划表顺序，逐项输出提示词（先多宫格，再单帧，最后 End Frame）
2. 每条提示词可直接复制到 Nano Banana Pro 中使用
3. 标注引用关系（哪些提示词需要在 edit 模式下上传前期筹备阶段的资产图）和生成建议
4. 输出配套的 Seedance Multi-Phase 视频提示词

**音频规则**：每段风格声明中必须包含"无背景音乐"。视频模型默认生成 BGM，不显式禁止就会有。BGM 在后期作为单独音轨统一铺设。

### Phase 6：审片

用户反馈生成结果后，精准定位问题并提供修正版提示词。

核心原则：
- **单变量修改**：每次只改一个维度，观察效果
- **加减法判断**：多了不想要的 → 减词；少了想要的 → 加词；方向错了 → 换词
- **位置权重**：越靠前的词权重越高，关键效果描述前移
- **避免越改越差**：超过 3 次微调无效时，退一步分析根本原因

TVC 专属迭代重点：
- **产品材质不对** → 调整材质描述词（参考 `references/storyboard.md` Part 3）
- **产品光影太平** → 加强侧光/轮廓光描述
- **品牌世界不够极限** → 加强环境极端性描述
- **产品在场景中不够突出** → 调整产品描述的位置权重

完整的迭代策略和常见失败模式见 `references/delivery.md` Part 2。

### Phase 7：交付

所有提示词输出完毕且用户满意后，主动提议整理交付物：

> "要我帮您把所有创意方案、提示词和视频脚本整理到一个项目文件夹吗？"

用户同意后，按以下结构组织文件：

```
<project-name>/
├── concept.md                      # TVC 创意方案文档
├── storyboard.md                   # 分镜脚本（如有）
│
├── assets/                         # 前期筹备：资产图提示词
│   └── prompts/
│       ├── product-multiview.md    # 产品多视图提示词
│       ├── product-detail-01.md
│       ├── env-01-<name>.md
│       └── ...
│
├── keyframes/                      # 分镜与拍摄：关键帧提示词
│   └── prompts/
│       ├── grid-01-<name>.md       # 多宫格提示词
│       ├── endframe-<name>.md      # End Frame 提示词
│       └── ...
│
└── video-scripts/                  # 分镜与拍摄：Seedance 视频提示词（Multi-Phase 格式）
    ├── segment-01-<name>.md
    └── ...
```

将本次会话的所有创意方案和提示词写入对应文件。

### 核心约束

以下为不可违反的硬规则。基础规则中已覆盖的原则（先跑再问、创意先行、品牌世界思维、精炼优先等）不在此重复。

**流程铁律**：
1. **视觉定调强制前置**：用户明确确认画风方向之前，禁止输出任何提示词
2. **产品多视图先于分镜**：前期筹备的产品多视图锁定之前，不生成分镜关键帧
3. **End Frame 必须存在**：每条 TVC 必须以 End Frame 收束——产品 + Logo 空间 + Slogan 空间

**提示词铁律**：
4. **只输出 Nano Banana Pro 中文提示词**：不输出 MidJourney、Stable Diffusion 或其他工具格式
5. **镜头精确控制**：多宫格每格必须包含景别、视角、光源方向、产品角度/状态。禁止将构图或光影决策交给 AI
6. **视频脉络先行**：每张多宫格写逐格描述前，先勾勒 15 秒段落的视频脉络。多宫格是脉络的冻结，视频提示词是脉络的展开
7. **视频提示词显式禁止 BGM**：风格声明必须写"无背景音乐"。BGM 在后期统一铺设

**一致性铁律**：
8. **产品标准描述必须建立**：前期筹备阶段必须输出产品标准描述，后续所有提示词统一复用
9. **出镜者标准描述必须建立**：有人出镜但不做角色资产时，必须在前期筹备阶段输出出镜者标准描述（体态+服装款式+颜色+配饰），后续所有提示词统一复用。服装款式和颜色跨格不可变化

**产品铁律**：
10. **产品出镜率**：全片产品可见格 ≥ 70%，单张 Grid 无产品格 ≤ 2，禁止连续 3 格以上无产品
11. **Seedance 双图输入**：视频模型接收多宫格分镜图 + 产品多视图。视频提示词用 `产品@产品多视图图片 的广告` 引用。`(图1)(图2)` 映射仅用于多宫格图片提示词

### 参考资料

本 skill 的知识库按职责组织为参考文件，按需加载。SKILL.md 正文中已标注何时读取哪个文件的哪个 Part。

| 角色 | 文件 | 使命 | 使用阶段 |
|------|------|------|---------|
| 创意导演 | `references/treatment.md` | TVC 导演思维框架、出镜策略、品类适配 | 创意提案 |
| 前期筹备 | `references/pre-production.md` | 资产规划、生成顺序、各类资产标准、一致性维护 | 前期筹备 |
| 镜头语言 | `references/shot-language.md` | 提示词句法、画风锚定词库、场景类型模板、构图范式 | 视觉定调 / 前期筹备 / 分镜与拍摄 |
| 分镜与视频 | `references/storyboard.md` | 多宫格分镜、视频提示词、产品拆解、品牌世界 | 分镜与拍摄 |
| 交付与迭代 | `references/delivery.md` | 输出格式模板、迭代调试 | 前期筹备 / 分镜与拍摄 / 审片 / 交付 |

---

<a id="src-tvc-director-references-treatment-md"></a>

## `tvc-director/references/treatment.md`

## TVC 创意策略与分镜脚本框架

> **核心使命**：提供 TVC 导演的思维框架，指导大模型从产品 Brief 提取灵感，推导视觉创意，并最终输出标准、可执行的【分镜头脚本】。
> **拒绝废话**：放弃僵化的百分比模版和理论穷举，建立“世界观设定 -> 视听转化 -> 分镜输出”的直觉思维。

---

### Part 1: TVC 导演的思维框架 (Mental Model)

优秀的 TVC 创意不是填表格，而是构建世界和控制节奏。在构思阶段，请始终围绕以下三个维度进行推演：

#### 1. 双世界法则 (Dual Worlds)
不要让产品干瘪地存在于真空中，思考它在这两个世界中的存在方式：
*   **产品世界 (Product World)**：绝对的主场。强调微距、精密感、材质肌理、局部特写、光影流转。
*   **品牌世界 (Brand World)**：产品所处的情感与文化语境。品牌世界的**载体**因品类而异——见下方品类分支。
*   **交互枢纽 (Match Cut/Transition)**：如何通过形状匹配、动作连贯或色彩渐变，将这两个世界的镜头无缝衔接。

##### 品牌世界的三种品类路径

不同产品品类的品牌世界由不同的载体承载。**拿到 brief 后，先判断产品属于哪条路径，再构思品牌世界**：

**功能型品牌世界**（科技/工具/户外装备）
载体是**环境**。产品在极限/专业使用场景中出场，环境本身传递品牌价值。
*   运动相机 → 跳伞、潜水、滑雪、攀岩
*   专业工具 → 工地、实验室、手术室
*   产品世界的表达：零件拆解、功能激活、屏幕点亮、数据可视化

**身份型品牌世界**（时尚/珠宝/奢侈品/潮牌）
载体是**人**。人的气质、穿搭、姿态、生活态度就是品牌世界——环境退居背景。
*   先锋银饰 → 穿极简黑衣的人 + 建筑美学空间 + 独立态度
*   奢侈珠宝 → 高定礼服 + 仪式感 + 优雅姿态
*   街头潮牌 → 涂鸦/地下文化 + 不羁年轻人
*   产品世界的表达：工艺溯源（锻造/打磨/镶嵌）、佩戴流转（光影在弧面上流动）、肌肤与材质的触感对比

**感官型品牌世界**（食饮/护肤/香氛）
载体是**感官体验**。原料质感、制作仪式、使用瞬间的感官细节就是品牌世界。
*   精品咖啡 → 烘焙过程、萃取瞬间、蒸汽升腾
*   护肤品 → 晨光仪式、水珠在肌肤上滑落、质地微距
*   香氛 → 原料意象（玫瑰花瓣、木质纹理、海盐结晶）
*   产品世界的表达：原料溯源、制作过程可视化、倾倒/涂抹/品尝的感官瞬间

#### 2. 产品植入策略 (Product Integration)

双世界法则定义了"产品世界"和"品牌世界"的存在，但没有回答一个关键问题：**这两个世界在片子里怎么共处？** 拿到 brief 后，先判断品类路径，然后选择植入策略——它决定了全片的结构骨架。

##### 产品电影化拆解

产品是唯一主角，纯影棚，全片就是产品世界。零件悬浮拆解、材质微距潜入、光影剧场——品牌世界可以完全不出现。

*   适合有内部结构可展示的产品：耳机、相机、手机、机械表芯
*   视觉逻辑：暗调揭示 → 悬浮拆解 → 功能激活 → 微距潜入 → 品牌定格
*   产品世界占比 100%

##### 品牌世界穿梭

品牌世界和产品世界**轮流出场**，用 Match Cut 衔接。一个 Phase 待在一个世界里把场景讲完，然后通过匹配剪辑切到另一个世界——不是在一个 Phase 内部来回跳。

*   适合产品功能与极限/专业场景强绑定的品类：运动相机+跳伞、潜水表+深海、越野车+山路
*   视觉逻辑：品牌世界建立能量 → Match Cut 到产品世界展示 → Match Cut 回品牌世界升级 → 产品世界收束
*   关键：切换发生在 Phase 之间，每个 Phase 是一个完整的连贯镜头

##### 生活方式短片（Lifestyle Film）

产品始终待在品牌世界中，不跳出去。不做影棚特写，不做拆解——产品就穿在身上、戴在手上、握在手里。通过运镜手法（低角度追拍、慢动作、景深变化、追焦到产品）在场景内自然突出产品存在感。片尾集中做一个 Hero Shot 收束。

*   适合穿戴型产品和生活方式产品：跑鞋、手表、眼镜、首饰佩戴状态、手袋
*   视觉逻辑：品牌世界叙事为主，产品通过运镜被"看见"而不是被"展示" → 片尾 Hero Shot 定格
*   产品始终在画面中（穿在身上），但镜头不刻意脱离场景去做影棚特写

##### 品类直觉

不是硬规则，是默认倾向——导演可以打破，但打破要有理由：

*   有内部结构可拆的科技产品 → 电影化拆解
*   产品功能绑定极限/专业场景 → 品牌世界穿梭
*   穿戴型 / 生活方式 → 生活方式短片

#### 3. 出镜策略 (Casting Strategy)

创意提案阶段必须回答：**谁出镜、怎么出镜、穿什么**。这对应真实 TVC 制作中的选角 (Casting) 和造型 (Styling) 环节。

##### 出镜决策树

```
产品品类 → 是否需要人物出镜？
│
├── 身份型（珠宝/时尚/奢侈品）→ 默认需要人物
│   ├── 产品佩戴在身体上 → 手部/手腕/颈部/耳部特写是 hero shot
│   ├── 服装/鞋履 → 穿着状态的身体是 hero shot
│   └── 造型方向：服装风格、配饰、肤质、气质关键词
│
├── 功能型（科技/工具/户外）→ 人物可选
│   ├── 纯产品电影化拆解 → 可无人
│   ├── 品牌世界穿梭 → 人物在使用场景中出现
│   └── 造型方向：功能性服装（运动装备、工服等）
│
└── 感官型（食饮/护肤/香氛）→ 视创意方向而定
    ├── 使用仪式 → 手部/面部局部
    ├── 原料溯源 → 可无人
    └── 造型方向：自然、生活感
```

##### Seedance 多宫格人物约束

Seedance 多宫格（3x3 分镜）**不支持完整人脸**。人物出镜方式限于：
*   手部 / 手腕特写（珠宝/手表最常用）
*   下半脸（嘴唇、下颌线）
*   身体局部特写（肩颈、锁骨、腰线）
*   全身远景 / 背影 / 剪影
*   戴口罩 / 潜水面具 / 头盔等遮挡面部的方式

**Nano Banana Pro 资产图不受此限制**——角色三视图可包含完整人脸，用于锁定人物设定。限制仅在多宫格分镜阶段生效。

##### 造型方向

造型是身份型品牌世界的核心载体。创意提案中的造型方向应包含：
*   **服装风格**：极简/高定/街头/工装/运动...
*   **色彩关系**：与产品色的呼应或对比（银饰 + 全黑 = 先锋；金饰 + 裸色 = 优雅）
*   **配饰逻辑**：除主推产品外是否有其他配饰？保持克制，不抢主角
*   **肤质/妆发方向**：干净/自然/戏剧化/无妆感...

#### 4. 视听转化法则 (Visual Translation)
将抽象的“卖点”转化为具象的视听语言：
*   **色彩与光影**：主色调是什么？是冷峻的赛博朋克霓虹光，还是治愈的自然晨光（Window light）？品牌色如何自然植入？
*   **视觉隐喻**：用画面代替说教。例如，“新鲜”不靠字幕，靠“清晨嫩芽滴落的露珠”；“静音”靠“一根针掉落的涟漪”。
*   **环境音场**：设计画面时同步思考声音。风声、水声、机械声、白噪音，甚至绝对的“静音”。

#### 5. 叙事切分 (Pacing)
将总时长划分为合乎逻辑的节拍幕次（通常以 15 秒为一个叙事单元）：
*   **0-15s (起 - Hook)**：建立世界观与情绪基调，抓住眼球。
*   **15-30s (承 - Develop)**：场景展开，产品核心特征、氛围或冲突显现。
*   **30-45s (转 - Climax)**：视听高潮，最快节奏的快剪或最具视觉张力的特写。
*   **45-60s (合 - Resolution)**：情绪落地，产品 Hero Shot 亮相，品牌理念收束。

---

### Part 2: 创意方向竞选 (Concept Pitch)

在正式写脚本前，先提供 2-3 个核心创意方向供用户选择。保持精简，直击灵魂。

**输出格式**：
*   **方向 X：[极具画面感的概念名称]**
*   **视觉风格与主色调**：[如：日系清新 / 东方自然美学 / 暖绿色调]
*   **核心视听思路**：[简述产品世界与品牌世界如何交织，3-4句话说清全片最大的视觉亮点与记忆点]

---

### Part 3: 标准化分镜头脚本产出 (Storyboard Script)

用户选定方向后，直接输出分镜头脚本。这是本阶段的**最终核心交付物**。必须使用以下标准格式：

#### 脚本结构标准

**【全局设定】**
*   **视频总时长**：[如：约 60 秒]
*   **视觉风格**：[关键词概括，如：高级电影感 / 赛博科技风]
*   **主色调**：[色彩描述，如：春日新绿、透明水光与晨光]
*   **音乐/声音基调**：[如：轻柔钢琴起头，中段加入风铃声，结尾回归白噪音]

**【分幕剧本】**（按时长分块，通常每 15 秒一幕）

##### ⏱️ 第一幕：[幕标题] (00:00 - 00:15)

**【镜头 1】**
*   **画面描述**：[详细的画面内容，前中后景，人物动作，产品状态，必须包含具体的画面细节。如果是一组快剪蒙太奇，可在此列出连续的多个短镜头。]
*   **运镜方式**：[如：固定机位 / 缓慢推进 / 航拍跟随 / 动感快切 / POV过肩视角 / 环绕镜头]
*   **旁白文案/字幕**：[精炼的文案，如果没有则写“无”]
*   **声音设计**：[具体的环境音或动作音效，如"微风吹拂"、"掐叶声"、"打字沙沙声"]

**【镜头 2】**
*   ...

##### ⏱️ 第二幕：[幕标题] (00:15 - 00:30)
...
*(依此类推，直到包含 End Frame 收尾镜头的最后一幕)*

---

<a id="src-tvc-director-treatment-skill-md"></a>

## `tvc-director-treatment/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: tvc-director-treatment
description: TVC director treatment and visual development skill for advertising films. Use when Codex needs to produce rich director statements, image style, camera language, rhythm, performance/persona design, character turnaround prompts, scene design, art direction, lighting, product presentation, music/sound mood, reference analysis, GPT Image 2 visual-generation prompts, or client-facing treatment decks for a TVC.
---
```

## TVC Director Treatment

Use this skill to translate an approved creative concept into a rich director treatment and visual development package.

The output should explain both:

- Why this execution expresses the creative idea.
- What visual evidence the client can see before production.

### Core Stance

- Write as a director speaking to a client, not as a production checklist.
- Be richer than a short style note: include emotion, image logic, camera grammar, performance, world, product, rhythm, sound, and visual proof.
- Use image generation as a treatment tool. For every major visual section, write a GPT-Image2-ready prompt and generate the corresponding image by default when image tools are available.
- Only skip image generation when the user explicitly asks for text/prompts only, or when the current environment cannot generate images.
- Keep generated visuals as references for approval, not final production frames unless the user asks.

### Workflow

1. Confirm inputs:
   - Approved creative idea or proposal route.
   - Product truth, audience, channel, duration, visual references, actor policy, and AI/live-action mode.
   - If these are missing and affect treatment direction, route back to `$tvc-brief-strategist` or `$tvc-concept-developer`.

2. Load visual development guidance when images are needed:
   - Read `references/visual-development.md`.
   - Use it to create visual deliverables and image-generation prompts.

3. Build the treatment:
   - Director statement.
   - Film promise and emotional arc.
   - Image style and color system.
   - Camera language and lens/movement grammar.
   - Rhythm and edit feeling.
   - Performance and persona design.
   - Scene/world design.
   - Product presentation.
   - Art direction, lighting, texture.
   - Music and sound.
   - Reference and visual development plan.

4. Generate visual assets for each major section:
   - Image style reference.
   - Camera language reference.
   - Performance/persona design, including character three-view when relevant.
   - Scene setting image.
   - Product presentation image.
   - Lighting/color mood image.
   - Key visual or hero frame.
   - For each asset, output the GPT-Image2 prompt, generate the image, show it inline, and preserve the prompt used.

5. Hand off to:
   - `$tvc-ppm-producer` for PPM expansion.
   - `$tvc-storyboard-writer` for shot-by-shot structure.
   - `$tvc-ai-shot-prompter` if visual prompts need per-shot conversion.

### Output Format

```markdown
## 导演阐述

## 影像风格
- 文字阐述：
- 视觉参考图 / GPT Image 2 Prompt：

## 镜头语言
- 文字阐述：
- 视觉参考图 / GPT Image 2 Prompt：

## 节奏与情绪曲线
- 文字阐述：
- 视觉参考图 / GPT Image 2 Prompt：

## 表演与人物形象设计
- 文字阐述：
- 人物三视图 / GPT Image 2 Prompt：

## 场景设定
- 文字阐述：
- 场景设定图 / GPT Image 2 Prompt：

## 产品呈现
- 文字阐述：
- 产品呈现图 / GPT Image 2 Prompt：

## 美术、光影与色彩
- 文字阐述：
- 光影色彩参考图 / GPT Image 2 Prompt：

## 音乐与声音

## 视觉开发清单

## 下游交接
```

### Image Generation Rules

- Generate images by default for the visual sections when image tools are available.
- If the user asks for prompts only, do not generate images.
- If image tools are unavailable or blocked, provide GPT Image 2-ready prompts and explicitly state that image generation was not executed.
- For OpenAI image API implementation details, use `$openai-docs` when current API syntax matters.
- For normal in-chat image generation, use `$imagegen` behavior when available.
- Do not invent exact brand packaging details not present in the provided product reference.
- For product images, require reference-image fidelity and block logo/text hallucination.
- For character three-view, specify front, side, back views on one clean sheet, consistent wardrobe and face, neutral pose.
- For multiple treatment images, generate one asset per prompt rather than asking for a single collage unless the section specifically needs a beat-board or three-view sheet.

### Quality Bar

- Every visual choice must serve the creative idea and audience psychology.
- Treatment writing must explain "why this visual language", not merely list adjectives.
- Each generated/reference image must answer a client question.
- Preserve continuity for later storyboard and AI prompting.
- Product presentation must protect shape, logo, package color, material, and scale.
- Character/persona design must match audience and avoid celebrity likeness unless explicitly approved.

---

<a id="src-tvc-director-treatment-references-visual-development-md"></a>

## `tvc-director-treatment/references/visual-development.md`

## Director Treatment Visual Development

Use this reference when a director treatment needs generated images, moodboards, key visuals, character designs, or product presentation references.

Default behavior: write the GPT-Image2 prompt and generate the image for each visual deliverable when image tools are available. If image generation cannot run, output the prompt and mark the image as pending generation.

### Visual Asset Map

| Treatment section | Image deliverable | Purpose |
| --- | --- | --- |
| Image style | Style frame / mood frame | Show overall tone, color, texture, and atmosphere |
| Camera language | Cinematic frame reference | Show lens, framing, depth, movement feeling |
| Rhythm/emotion | Beat-board strip or contrast pair | Show before/after emotional transition |
| Performance/persona | Character design + three-view | Align casting, styling, makeup, wardrobe, posture |
| Scene setting | Environment concept image | Align location, time, art direction, props |
| Product presentation | Hero product frame | Align packshot, texture, hand interaction, logo visibility |
| Light/color | Lighting mood frame | Align color contrast, key light, shadow, highlight |
| Key visual | Campaign hero image | Align the single most memorable visual idea |

### GPT Image 2 Prompt Pattern

Use this structure for each visual:

```markdown
用途：
画幅：
主体：
场景：
动作/状态：
构图：
镜头语言：
光影色彩：
美术与材质：
品牌/产品要求：
风格关键词：
负面约束：
```

### Image Style Reference Prompt

```text
Create a high-end TVC director treatment style frame.
The image should communicate the film's overall visual tone, color palette, atmosphere, and emotional texture.
Do not create a final storyboard shot; create a mood-defining reference frame for client approval.
```

### Camera Language Reference Prompt

```text
Create a cinematic frame that demonstrates lens language, framing, depth of field, and camera attitude for a TVC.
Emphasize how the camera makes the product or character feel, not only what is visible.
```

### Character Three-View Prompt

```text
Create one clean character design sheet with front, side, and back views of the same person.
Neutral standing pose, consistent face, hairstyle, makeup, wardrobe, body proportion, and color palette.
Commercial casting reference style, not fashion illustration, not celebrity likeness.
Plain light background, no text unless requested.
```

### Scene Setting Prompt

```text
Create a TVC environment concept image for a director treatment.
Show the location, time of day, art direction, props, atmosphere, and practical shooting/AI-generation feasibility.
The scene should support the creative concept and audience psychology.
```

### Product Presentation Prompt

```text
Create a premium TVC product presentation reference.
The product must match the provided reference image in shape, package color, label layout, logo position, material, and scale.
Show texture, condensation, hand interaction, or hero packshot logic as requested.
Avoid hallucinated text, distorted logos, wrong packaging, extra products, or unreadable labels.
```

### Key Visual Prompt

```text
Create a campaign key visual for the TVC concept.
It should combine the core insight, product role, visual metaphor, and emotional promise in one memorable image.
Composition should be suitable for proposal deck and social campaign adaptation.
```

### Output Discipline

- Label each visual by section.
- Explain why the image is needed.
- By default, generate each image, show it inline, and preserve the prompt used.
- If only preparing prompts because the user requested prompt-only output or tools are unavailable, make prompts detailed enough for direct batch generation.
- Keep references and generated images separate from final storyboard frames.

---

<a id="src-tvc-director-references-shot-language-md"></a>

## `tvc-director/references/shot-language.md`

## TVC 提示词工程知识库

> **职责**：Phase 3 画风确认 + Phase 4/5 提示词编写的参考。覆盖 Nano Banana Pro 图片提示词的句法结构、画风选择、场景模板和构图范式。
> **不管**：创意策略（查 treatment.md）、资产规划与生成顺序（查 pre-production.md）、视频提示词和多宫格（查 storyboard.md）、输出格式与迭代（查 delivery.md）。

---

### Part 1: 提示词结构

---

### 一、提示词核心结构

Nano Banana Pro 的最优提示词结构分为六层，按从左到右的顺序排列：

```
[画质锚定] + [主体描述] + [环境/空间] + [光影] + [构图/镜头] + [画风锚定]
```

#### 各层详解

##### 第一层：画质锚定（前置权重最高）

画质锚定词决定整体生成品质，放在提示词最前面。选择取决于已确认的画风方向。

| 画质锚定词 | 适用画风方向 | 适用场景 |
|-----------|------------|---------|
| 真人实拍 | A. 真人实拍 | 真人化角色/场景 |
| 电影级摄影 | A. 真人实拍 | 真人电影画面 |
| 真人电影剧照质感 | B. 真人电影剧照 | 漫威/权游等影视级 |
| 超写实电影画质 | B/C. 电影剧照或CG | 超写实CG场景（⚠️单独使用偏CG） |
| 超逼真电影画质 | C. 3A游戏CG | 高写实CG场景 |
| 8K超清分辨率 | 通用 | 所有需要精细质感的场景 |
| 电影级镜头 | 通用 | 电影感画面 |
| 大师级CG渲染 | C/D. CG或引擎级 | 3A游戏、动画CG |
| 虚幻引擎5渲染 | D. 高精CG引擎级 | 追求接近真实的顶级CG |
| 超写实CG | D. 高精CG引擎级 | 好莱坞视效级CG |
| 电影级CG视效 | D. 高精CG引擎级 | 头号玩家/阿凡达级视效 |

**按画风方向的组合示例**：
- **真人实拍**：`真人实拍，电影级摄影，真实皮肤毛孔质感，自然光照` 
- **真人电影剧照**：`真人电影剧照质感，8K超清分辨率，电影级调色`
- **3A游戏CG**：`超写实电影画质，8K超清分辨率，电影级调色`
- **高精CG引擎级**：`虚幻引擎5渲染，8K超清分辨率，次表面散射皮肤，全局光照` 或 `超写实CG，电影级CG视效，8K超清分辨率，电影级调色`
- **偏摄影感**：`8K超清分辨率，电影级镜头`

##### 第二层：主体描述

**人物描述层次**：
```
[身份/名称] + [体态/身形] + [面部特征] + [服装/装备] + [姿态/动作] + [表情/情绪]
```

**物件/武器描述层次**：
```
[类型] + [材质] + [尺寸] + [特殊效果] + [状态]
```

##### 第三层：环境/空间

```
[空间类型] + [空间规模] + [材质/表面] + [大气效果] + [环境细节]
```

##### 第四层：光影

```
[整体明暗] + [主光源位置和类型] + [光影效果] + [色温/颜色]
```

##### 第五层：构图/镜头

在提示词中用自然语言指定构图意图和镜头参数。

##### 第六层：画风锚定（收尾兜底）

画风锚定词放在末尾，作为整体风格的兜底保障。**必须与已确认的画风方向一致。**

| 画风锚定词 | 适用画风方向 |
|-----------|------------|
| 真人实拍，电影级摄影，真实皮肤毛孔质感，自然光照 | A. 真人实拍 |
| 真人电影剧照质感，真实皮肤纹理和毛发细节 | B. 真人电影剧照 |
| 电影胶片色彩，颗粒感 | A/B. 真人方向 |
| 3A大作3D游戏风格 | C. 3A游戏CG |
| 电影级调色 | 通用 |
| 虚幻引擎5渲染，次表面散射皮肤，PBR材质 | D. 高精CG引擎级 |
| 超写实CG，电影级CG视效，电影级调色 | D. 高精CG引擎级 |
| 写意光影 | E. 特定美学 |
| 极简构图 | 通用 |

---

### 二、画质 × 画风组合速查表

| 视觉目标 | 画风方向 | 画质锚定（前置） | 画风锚定（收尾） |
|---------|---------|----------------|----------------|
| 真人实拍 | A | 真人实拍，电影级摄影，8K超清分辨率 | 真实皮肤毛孔质感，自然光照 |
| 真人电影剧照 | B | 真人电影剧照质感，8K超清分辨率 | 真实皮肤纹理和毛发细节，电影级调色 |
| 超写实电影（偏CG） | B/C | 超写实电影画质，8K超清分辨率，电影级调色 | — |
| 3A游戏CG | C | 大师级CG渲染，8K超清分辨率 | 3A大作3D游戏风格 |
| 高精CG引擎级（人物向） | D | 虚幻引擎5渲染，8K超清分辨率 | 次表面散射皮肤，真实皮肤纹理，PBR材质，全局光照 |
| 高精CG引擎级（场景向） | D | 超写实CG，电影级CG视效，8K超清分辨率 | PBR材质，全局光照，电影级调色 |
| 暗黑写实 | A/B/C | 超逼真电影画质，8K材质纹理 | 低调摄影（Low-key Lighting），高对比度，颗粒感 |
| 宏大场景 | 跟随全局 | 超写实电影画质，8K超清分辨率 | 广角镜头，极低的视角以凸显空间尺度 |
| 东方古风 | E | 电影级画质，8K | 中国水墨美学，写意光影 |
| 治愈系 | E | 8K超清分辨率 | Golden Hour暖光，梦幻散景 |

---

### 三、多图参考的描述规范

```
构图核心 (Composition):
前景：[角色/物体]（图1）[姿态/位置描述]。[外观细节]。
中景/背景：[角色/物体]（图2）[姿态/位置描述]。[外观细节]。
光影 (Lighting):
[光源1描述]。
[光源2描述]。
关键细节：[材质反射/倒影/特殊效果]。
镜头语言：[镜头类型]，[视角]，[景深]。
```

---

### 四、提示词长度控制

| 场景复杂度 | 建议长度 | 说明 |
|-----------|---------|------|
| 简单（单主体+简单背景） | 30-80字 | 如角色三视图、物件特写 |
| 中等（主体+环境+光影） | 80-150字 | 如环境概念图、单人场景 |
| 复杂（多层构图+叙事） | 150-300字 | 如对峙画面、多人场景 |

**原则**：描述精度 > 描述长度。

---

### Part 2: 画风锚定词库

---

### 一、画风方向选项

| 选项 | 说明 | 视觉效果 |
|------|------|---------|
| **A. 真人实拍/摄影级** | 像真实摄影照片 | 类似电影剧照、时装摄影 |
| **B. 真人电影剧照** | 介于真人和CG之间 | 类似漫威电影角色、权力的游戏 |
| **C. 3A游戏CG** | 高品质游戏CG渲染 | 类似最终幻想CG、原神过场动画 |
| **D. 高精CG引擎级** | 全CG但追求"接近真实"的顶级质感 | 类似头号玩家、虚幻引擎5 MetaHuman |
| **E. 特定美学风格** | 水墨、赛博朋克、动漫等 | 根据具体风格而定 |

---

### 二、各方向锚定词与组合

#### A. 真人实拍 / 摄影级

| 锚定词 | 适用场景 | 搭配建议 |
|--------|---------|---------|
| 真人实拍 | 直接锚定真人照片方向 | + 电影级摄影 + 自然光照 |
| 电影级摄影 | 强调摄影感而非渲染感 | + 真人实拍 |
| 真实皮肤毛孔质感 | 强制真人皮肤微观细节 | 用于角色设定图/特写 |
| RAW照片质感 | 未经后期的原始摄影感 | + 自然光照 |
| 电影胶片色彩 | 胶片感色调 | + 颗粒感 |

**组合示例**：
- `真人实拍，电影级摄影，真实皮肤毛孔质感，自然光照` — 纯真人照片级
- `真人实拍，8K超清分辨率，电影胶片色彩` — 高清真人胶片感

#### B. 真人电影剧照

**组合示例**：
- `真人电影剧照质感，8K超清分辨率，真实皮肤纹理和毛发细节，电影级调色` — 影视级
- `超写实电影画质，真人电影剧照质感，电影级调色` — 超写实偏真人

#### C. 3A 游戏 / CG

关键锚定词：`3A大作3D游戏风格`、`大师级CG渲染`、`超写实电影画质`、`8K超清分辨率`、`电影级调色`

#### D. 高精CG引擎级

**核心定位**：全部是CG渲染，但在材质、光照、皮肤等方面无限逼近真实。与C方向的区别：C保留明显的"游戏CG美感"，D追求"以假乱真的CG"。

| 锚定词 | 适用场景 | 搭配建议 |
|--------|---------|---------|
| 虚幻引擎5渲染 | 极致光追质感 | + 全局光照 + PBR材质 |
| 次表面散射皮肤 | 皮肤半透明光感 | + 虚幻引擎5渲染 + 真实皮肤纹理 |
| PBR材质 | 物理正确的材质渲染 | + 全局光照 |
| 超写实CG | 直接锚定"追求真实感的CG" | + 电影级调色 |
| 电影级CG视效 | 好莱坞视效大片级别 | + 8K + 电影级调色 |

**组合示例**：
- `虚幻引擎5渲染，次表面散射皮肤，真实皮肤纹理，PBR材质，全局光照` — 顶级引擎级CG（人物向）
- `超写实CG，电影级CG视效，8K超清分辨率，电影级调色` — 好莱坞视效级CG（场景向）
- `光线追踪渲染，PBR材质，全局光照，电影级调色` — 引擎级CG环境

#### E. 特定美学

| 锚定词 | 适用场景 |
|--------|---------|
| 中国水墨美学 | 古风/武侠/东方题材 |
| 赛博朋克美学 | 科幻/未来都市 |
| 日系动漫风格 | 二次元/番剧质感 |
| Studio Ghibli风格 | 治愈系/宫崎骏质感 |
| 低调摄影（Low-key Lighting） | 暗黑/悬疑/恐怖 |
| Golden Hour暖光 | 治愈/怀旧/情绪片 |

---

### 三、C vs D 对比

| 维度 | C. 3A游戏CG | D. 高精CG引擎级 |
|------|------------|----------------|
| 皮肤 | 精致但光滑，有理想化美感 | 有毛孔、细纹、肤色不均，接近真实 |
| 光照 | 游戏级光照，可接受艺术化 | 全局光照+光线追踪，物理正确 |
| 材质 | 精致但允许风格化 | PBR物理正确，每个表面有真实反射/粗糙度 |
| 整体感受 | "精致的游戏角色" | "CG还是真的？" |

---

### Part 3: TVC 场景类型

> TVC 广告专用的场景类型分类和提示词模板。围绕产品展示、品牌叙事、视觉衔接三大核心诉求设计。

---

### 场景类型总览

| 类别 | 场景类型 | 核心功能 |
|------|---------|---------|
| 产品世界镜头 | 产品 Hero Shot | 主视觉定调 |
| 产品世界镜头 | 产品电影化拆解帧 | 技术实力可视化 |
| 产品世界镜头 | 功能可视化帧 | UI/数据/传感器呈现 |
| 产品世界镜头 | 材质微距帧 | 工艺细节放大 |
| 产品世界镜头 | Pack Shot | 包装展示 |
| 产品世界镜头 | End Frame | 收束定格 |
| 品牌世界镜头 | 极限运动场景 | 极端环境说服力 |
| 品牌世界镜头 | 生活方式场景 | 日常使用共鸣 |
| 品牌世界镜头 | 情感场景 | 人物与产品情感连接 |
| 品牌世界镜头 | 环境氛围空镜 | 品牌世界观建立 |
| 交叉衔接帧 | 匹配剪辑过渡帧 | 产品世界 ↔ 品牌世界的视觉桥梁 |
| 交叉衔接帧 | 产品 Reveal 过渡 | 使用场景 → 产品特写的揭示转场 |

---

### 第一类：产品世界镜头

---

#### 1. 产品 Hero Shot

##### 提示词模板
```
[画质锚定]，[产品描述]静置于[背景]中央。[光影设计——侧光/轮廓光/顶光]。[材质细节——金属/玻璃/磨砂]。[构图——产品占比/留白]。[画风锚定]。
```

##### 关键要点
- **背景克制**：纯色或极简影棚质感
- **光影至少双光源**：主光（侧光定型）+ 辅光（轮廓光分离背景）
- **材质必须精写**：金属拉丝、AG 磨砂玻璃、陶瓷光泽等
- **产品占比**：40%-60% 最佳

##### 示例
```
8K超清分辨率，电影级产品摄影。一款深空灰钛金属智能手表静置于纯黑背景中央，表盘微微朝向右侧15度。左侧柔和侧光勾勒出钛金属表壳的拉丝纹理和微妙的倒角高光。右侧轮廓光将产品从纯黑背景中分离，在表壳边缘形成一道极细的白色光边。表盘显示深蓝色表面，刻度和指针反射出冷白微光。表带为黑色氟橡胶材质，表面可见细密的菱形压纹。产品占画面中央50%，上方留白30%。极浅景深，焦点在表盘上。产品摄影质感，电影级调色。
```

---

#### 2. 产品电影化拆解帧

##### 提示词模板
```
[画质锚定]，[产品名]的[组件描述]悬浮拆解状态。[各组件的空间位置关系]。[核心传感器/芯片发光效果]。[影棚侧光]。[画风锚定]。
```

##### 关键要点
- **悬浮间距**：组件之间需要描述具体的空间层次关系
- **发光元素**：芯片、传感器等加入微弱自发光效果
- **组件数量控制**：3-5 个组件层级最佳

##### 示例
```
8K超清分辨率，电影级CG视效。一款智能手表的电影化拆解状态，各组件沿垂直轴线悬浮展开。最上层：蓝宝石玻璃表镜，边缘折射出彩虹色光晕。第二层：AMOLED显示面板，屏幕发出微弱的蓝色自发光。第三层：钛金属中框，可见精密CNC加工痕迹。第四层：主板和传感器模组，核心芯片发出淡绿色微光，电路走线如发丝般精密。最底层：陶瓷后盖，光学心率传感器发出红色脉冲光。各层间距均匀，整体呈微俯视3/4角度。纯黑渐变背景，左侧影棚侧光照亮各组件边缘。超写实CG，电影级调色。
```

---

#### 3. 功能可视化帧

##### 提示词模板
```
[画质锚定]，[产品]的屏幕/界面展示。[屏幕内容详细描述——UI元素/数据/图表]。[屏幕发光对周围环境的影响]。[产品本体在画面中的位置和状态]。[光影——以屏幕自发光为主光源]。[画风锚定]。
```

##### 关键要点
- **屏幕内容必须具体**：用几何形状描述 UI 布局，避免要求精确文字
- **屏幕光溢出效果**：屏幕的光照亮周围表面
- **暗环境增强效果**：让屏幕成为画面主光源

##### 示例
```
8K超清分辨率，电影级产品摄影。暗光环境中，一款智能手表佩戴在手腕上，表盘朝向镜头。屏幕显示运动监测界面：中央是一个大尺寸绿色心率数字，周围环绕三个彩色圆环进度条（红/绿/蓝），底部是一条实时心率波形曲线，波峰处发出微弱的绿色脉冲光。屏幕的冷蓝色光芒溢出到手腕皮肤上，在皮肤表面形成柔和的蓝色光晕。背景全黑，仅屏幕光作为画面唯一光源。近景特写，微俯视角度，极浅景深，焦点在屏幕上，手腕边缘柔和虚化。产品摄影质感，电影级调色。
```

---

#### 4. 材质微距帧

##### 提示词模板
```
[画质锚定]，微距特写[产品部位]的[材质类型]表面。[微观物理细节——纹理/颗粒/反射]。[微距光影——侧光刻画纹理/逆光穿透材质]。[极浅景深，焦点位置]。[画风锚定]。
```

##### 关键要点
- **侧光是微距之王**：低角度侧光能最大化刻画表面纹理起伏
- **物理微观细节**：金属加工刀痕、玻璃微气泡、纤维编织交叉
- **尺度暗示**：加入灰尘颗粒等微观参照物暗示放大倍率

##### 示例
```
8K材质纹理，微距特写。一款钛金属手表表壳的侧面倒角区域。极低角度侧光从左侧掠过，照亮拉丝纹理的每一道精密平行沟槽，沟槽之间的高点反射出锐利白色高光线，低点沉入阴影。倒角与平面交接处可见CNC加工留下的极细同心圆刀痕。表面散落着两三颗微尘颗粒，暗示极端放大的尺度。右侧边缘过渡到AG磨砂玻璃区域，磨砂颗粒在侧光下闪烁如细密星光。极浅景深，焦点在拉丝纹理中段，前景和远端迅速虚化。产品摄影质感，高对比度。
```

---

#### 5. Pack Shot

##### 提示词模板
```
[画质锚定]，[产品包装盒描述——形状/颜色/材质]正面朝向镜头，[摆放状态]。[包装盒旁边的产品本体]。[光影——柔和影棚光]。[构图——包装与产品的位置关系]。[画风锚定]。
```

##### 关键要点
- **包装盒+产品同框**
- **包装盒角度**：微侧 15-30 度比纯正面更有立体感
- **柔光为主**

##### 示例
```
8K超清分辨率，产品摄影质感。浅灰色渐变影棚背景上，一个哑光黑色方形包装盒微侧20度摆放于画面左侧，盒面印有烫银品牌标识。包装盒右侧，智能手表本体以3/4角度展示，表盘朝向镜头，屏幕显示时间界面。盒盖微微掀开，露出内衬的深灰色绒面材质。柔和的顶光均匀照亮产品和包装，在背景上形成柔和的椭圆形投影。产品和包装盒共占画面60%，上方和右侧保留留白。产品摄影质感，自然光照。
```

---

#### 6. End Frame

##### 提示词模板
```
[画质锚定]，[产品描述]以[角度/姿态]静置于[背景]中。[光影——干净、高级]。[构图——产品偏置，留白用于文字叠加]。[画风锚定]。
```

##### 关键要点
- **为文字预留空间是核心**：至少 30%-40% 的干净区域给 Logo 和 Slogan
- **产品姿态稳定**，不要有动感暗示
- **后期空间**：Logo/Slogan/法律信息在后期叠加

##### 示例
```
8K超清分辨率，电影级产品摄影。深空灰渐变背景，画面偏左下方三分之一处，一款智能手表以正面朝向镜头的姿态稳定静置，表盘显示深蓝色界面。柔和的左侧侧光照亮产品，在右侧形成自然过渡的阴影。产品右上方留出画面40%的干净空间，背景渐变均匀无杂物。整体调性沉稳、高级、克制。产品摄影质感，电影级调色。
```

---

### 第二类：品牌世界镜头

---

#### 7. 极限运动场景

##### 提示词模板
```
[画质锚定]，[运动场景环境描述]。[运动员描述——动作/姿态/装备]。[产品在运动员身上的位置和状态]。[运动产生的物理效果——飞溅/气流/雪花]。[光影——自然光]。[构图——动感]。[画风锚定]。
```

##### 关键要点
- **冻结最具张力的瞬间**
- **物理效果增强运动感**：水花飞溅、雪雾翻涌、灰尘飞扬
- **产品必须可见但不抢戏**

##### 示例
```
真人实拍，电影级摄影，8K超清分辨率。阿尔卑斯山脉雪场，正午强烈阳光。一位滑雪运动员正在陡坡高速转弯的冻结瞬间，身体极度压低倾斜，外侧手几乎触及雪面。转弯切雪激起的雪雾形成一道弧形白色浪墙，雪粒在逆光中闪烁如碎钻。运动员左手腕上的智能手表清晰可见，表盘上GPS轨迹界面的绿色光芒与白雪形成对比。低角度侧方追拍视角，运动员沿对角线从左上向右下切入，身后雪雾占据画面上方三分之一。真实皮肤毛孔质感，自然光照，电影级调色。
```

---

#### 8. 生活方式场景

##### 提示词模板
```
[画质锚定]，[日常场景环境描述——时间/地点/氛围]。[人物描述——衣着/状态/情绪]。[人物与产品的交互动作]。[环境细节——增强生活感的道具]。[光影——自然光/窗光/暖调]。[构图]。[画风锚定]。
```

##### 关键要点
- **"不经意"感是关键**：产品自然出现在生活中
- **环境道具真实感**：咖啡杯有使用痕迹、桌面有自然杂物
- **自然光+暖色调**

##### 示例
```
真人实拍，电影级摄影，8K超清分辨率。清晨7点，一间北欧风格公寓的餐桌旁。温暖的侧窗晨光从左侧大窗洒入，在木质餐桌上投下窗棂的光影。一位30岁左右的女性身着米色亚麻衬衫，左手端起白色陶瓷咖啡杯轻抿，右手腕上的智能手表显示今日运动目标完成度。桌面上散落着一份翻开的杂志、一个牛角面包和一小碟黄油。背景是微微虚化的绿植和厨房岛台。中景平视，人物位于画面右侧三分之一处，左侧窗光形成大面积暖色光区。真实皮肤毛孔质感，自然光照，电影胶片色彩。
```

---

#### 9. 情感场景

##### 提示词模板
```
[画质锚定]，[情感场景环境]。[人物描述——关键的情绪表情和肢体语言]。[产品在情感交互中的角色]。[光影——配合情绪的色温和明暗]。[构图——特写或中近景突出表情]。[画风锚定]。
```

##### 关键要点
- **情绪通过多通道传递**：微表情 + 肢体 + 光影 + 色调
- **产品是情感载体**：触发或承载情感的"道具"
- **避免过度煽情**

##### 示例
```
真人实拍，电影级摄影，8K超清分辨率。傍晚客厅，一位年轻父亲坐在沙发上，3岁女儿趴在他的肩膀上已经睡着。他右手轻轻抚着女儿后背，左手腕上的智能手表屏幕亮起，显示来自妻子的消息通知，屏幕柔和的蓝白色光芒照在他脸上。他低头看向手表，嘴角不自觉微微上扬，眼神温柔。暖黄色台灯从画面左侧照来，将父女二人裹在暖色光团中，背景完全虚化为暖色Bokeh光斑。中近景，人物位于画面中央偏右，极浅景深，焦点在父亲的面部表情上。真实皮肤纹理和毛发细节，电影级调色。
```

---

#### 10. 环境氛围空镜

##### 提示词模板
```
[画质锚定]，[空间类型和规模]。[环境物理细节——材质/纹理/物件]。[大气效果——雾气/光线/粒子]。[光影设计]。[构图/镜头——广角/俯拍/引导线]。[画风锚定]。
```

##### 关键要点
- **无人物**
- **光影即情绪**：完全依赖光影和色调传递
- **可用作转场**：色调和构图需考虑前后镜头衔接

##### 示例
```
8K超清分辨率，电影级摄影。黎明时分的高原湖泊，湖面如镜面般平静，完美倒映着远处连绵雪山和渐变天空。天际线从深蓝渐变为玫瑰金，最亮处太阳即将升出山脊。湖面上漂浮着一层薄薄的晨雾，雾气在水面上方约一米处缓缓流动。前景是岸边的碎石和一丛枯黄的高山草甸，被浅景深虚化为前景色块。广角镜头，三分法构图，天空占画面上方三分之一，湖面和倒影占中间三分之一，前景岸边占下方三分之一。电影胶片色彩，颗粒感。
```

---

### 第三类：交叉衔接帧

---

#### 11. 匹配剪辑过渡帧

设计 Match Cut 中的「桥梁帧」：在 A 尾帧与 B 首帧之间建立可被感知的视觉连续性。Match Cut 的完整技法库见 `storyboard.md` Part 4。

---

#### 12. 产品 Reveal 过渡

从品牌世界的使用场景平滑过渡到产品世界的特写展示。

过渡路径：`使用场景全景 → 产品局部可见 → 产品占满画面 → 产品 Hero Shot`

##### 提示词模板（三阶段）

**阶段 A（品牌世界 → 产品初现）**：
```
[画质锚定]，[使用场景中景]。[人物动作使产品自然进入视线]。[产品在画面中清晰但不是焦点]。[环境光照]。[画风锚定]。
```

**阶段 B（过渡帧——产品放大）**：
```
[画质锚定]，[近景/特写]，[产品占画面主体]。[使用场景的环境元素虚化为背景]。[光影从环境光过渡到产品摄影光]。[极浅景深，焦点锁定产品]。[画风锚定]。
```

**阶段 C（产品世界——Hero Shot）**：使用"产品 Hero Shot"模板。

##### 示例（户外运动 → 手表特写 Reveal）

**阶段 A**：
```
真人实拍，电影级摄影，8K超清分辨率。阳光明媚的山顶，一位越野跑者完成冲刺后弯腰双手撑膝喘息，抬起左手腕查看运动数据。智能手表在画面中可见但较小，屏幕绿色光芒在阳光下依然辨识清晰。背景是辽阔的山谷和蓝天。中景，人物位于画面中央，自然光照。真实皮肤毛孔质感，电影级调色。
```

**阶段 B（过渡帧）**：
```
真人实拍，电影级摄影，8K超清分辨率。近景特写运动员左手腕的智能手表，表盘朝向镜头，屏幕显示完成10公里越野跑的统计数据界面。手表占画面60%，表壳上可见阳光在钛金属表面的高光和汗水微珠。手腕皮肤和远处山景完全虚化为暖色调背景Bokeh。极浅景深，焦点在表盘上。自然阳光与微弱的轮廓光混合。产品摄影质感，电影级调色。
```

---

### Part 4: TVC 构图范式

TVC 的构图不仅服务于"美"，还必须服务于"传达"。

#### 4.1 揭示构图

**经典揭示序列**：

```
第1步：极端微距——观众看到抽象的纹理/线条，不知道是什么
第2步：缓慢拉远——局部轮廓开始显现，观众开始猜测
第3步：继续拉远——产品全貌显现，"原来是这个"的认知快感
第4步：产品完整呈现——在完美构图中展示全貌
```

**变体手法**：遮挡揭示、光线揭示、聚焦揭示、旋转揭示。

#### 4.2 End Frame 构图标准

| 元素 | 构图位置 | 尺寸要求 |
|------|---------|---------|
| **产品** | 画面中心偏左或正中 | 占画面 20%–40% |
| **品牌 Logo** | 右下角或底部居中 | 清晰可辨但不压过产品 |
| **Tagline/Slogan** | Logo 上方或产品下方 | 字号小于产品名称 |
| **背景** | 品牌色或品牌标志性视觉 | 简洁、不分散注意力 |

**End Frame 三法则**：
1. **3 秒可读**：所有信息必须在 3 秒内被观众读取完毕
2. **3 个元素以内**：产品 + Logo + Slogan 最多三个信息层级
3. **3 层视觉层级**：明确的主-次-辅视觉优先级

#### 4.3 文字/Logo 安全区域

| 区域 | 定义 | 用途 |
|------|------|------|
| **画面安全区** | 边缘内缩 5% | 所有重要视觉元素 |
| **标题安全区** | 边缘内缩 10% | 所有文字信息 |
| **上方 1/5** | 顶部 20% | Tagline、标题 |
| **下方 1/5** | 底部 20% | 产品信息、法律声明 |
| **中央 60%** | 中心区域 | 核心视觉内容，避免被文字遮挡 |

---

### Appendix: TVC 视觉设计清单

- [ ] 品牌色是否有明确的植入策略？
- [ ] 品牌色是否与全片色彩弧线自然融合？
- [ ] 产品材质之美是否通过正确的光线策略被释放？
- [ ] 产品镜头是否有"雕塑化"处理？
- [ ] 产品与负空间的比例是否服务于叙事意图？
- [ ] 构图是否为文字/Logo 预留了安全区域？
- [ ] End Frame 是否满足"3 秒可读、3 个元素、3 层层级"？
- [ ] 是否确定了品牌所属的视觉世界并贯穿全片？
- [ ] 视觉世界的选择是否匹配品牌调性和目标受众？

---

<a id="src-tvc-director-references-pre-production-md"></a>

## `tvc-director/references/pre-production.md`

## TVC 资产图生成框架

> **核心使命**：分镜脚本定稿后、出分镜关键帧之前，先生成一套**视觉资产图**——为后续所有画面锁定"人、物、景"的视觉基准。
> **本质**：资产图 = TVC 的"选角 + 置景 + 产品定妆"。拍真人广告时你也要先定演员、搭场景、摆产品——AI 生成同理。
> **只有三种资产**：角色三视图、产品图、场景图。不要发明第四种。

---

### Part 1: 资产规划——从分镜脚本到资产清单

> 拿到分镜脚本后，不要急着逐帧出图。扫一遍脚本，回答两个问题：

#### 问题一：谁出镜？

- **产品** → 必须做产品图，没有例外
- **人物/模特** → 判断是否需要角色资产图：

| 判断维度 | 做角色资产图 | 只需出镜者标准描述 |
|---------|------------|-----------------|
| **品类路径** | 身份型（时尚/穿搭/首饰/奢侈品）→ 造型本身就是品牌世界，必须做 | 功能型（科技/工具）且人物只是"使用者背景板" |
| **植入策略** | 生活方式短片 → 产品穿在身上不离场，人物跨 5 格以上 | 品牌世界穿梭 → 人物仅出现在少数品牌世界面板 |
| **出镜方式** | 下半身/手部/局部但**跨多格反复出现** → 造型细节累积不一致风险高 | 仅 1-2 格远景剪影/背影群像 |

**核心逻辑**：触发角色资产的关键不是"脸是否可见"，而是"**人物造型是否是这条 TVC 的核心视觉元素**"。身份型品牌世界里，即使全片无正脸，服装/配饰/体态就是品牌表达——必须用资产图锁定。

#### 问题二：在哪拍？

- 扫分镜中出现的所有场景，归类为几个**视觉上不同的空间**
- 每个独立空间做一张场景图（锁定氛围、色调、光影基调）
- 如果全片都在影棚（纯产品电影化）→ 场景图可以不做，影棚氛围在产品图中已经锁定

#### 生成顺序

```
① 产品图（最高优先级——产品是 TVC 的灵魂）
② 角色三视图（如有人出镜——人物要跟产品交互，需要先知道产品长什么样）
③ 场景图（相对独立，但色调要跟产品图协调）
```

---

### Part 2: 三种资产的定义

> **默认假设：产品参考图存在。** 真实 TVC 都是为已存在的产品做广告——产品官方图/实物照片/电商图几乎必然存在。"无产品参考图"是例外路径（概念产品/虚拟产品/早期设计阶段），仅在用户明确说明产品尚未实体化时启用。
>
> 参考图决定提示词的**写法路径**——两种路径的 prompt 结构完全不同：
> - **默认路径（有参考图）** → prompt 直接引用"图中产品/图中人物"，**不描述外观细节**（外观由参考图锁定，多余描述反而干扰还原）
> - **例外路径（无参考图）** → prompt 必须用文字精确描述外观（材质、颜色、形状等），纯文生图
>
> **不因用户缺少参考图而阻断流程。** 两条路径都能产出可用的资产图——但产品参考图应在创意简报阶段就主动追问，不应等到前期筹备才临时补问。

#### 2.1 产品图

**目的**：锁定产品的外观、材质、配色、比例。后续所有产品出镜帧都引用它。

**参考图交互**：
- 产品参考图应已在创意简报阶段（Phase 1）确认，前期筹备阶段不再重复询问产品层面
- 如果 Phase 1 遗漏（Mode B/C 跳过了创意简报），此处补问"产品有官方图/实物照片/电商图吗？"——默认前提是"有"而非"是否需要"
- 用户回答后，直接按对应路径生成 prompt，**不索要图片、不等待图片**

**两条 prompt 路径**：

| 路径 | 适用场景 | prompt 写法 | 示例 |
|------|---------|-----------|------|
| **默认路径（有参考图）** | 已上市产品、已完成设计的产品、有任何官方视觉资产的产品 | `参考图片，为这个产品生成xxx` — 不描述产品外观 | "参考图片，为这个产品生成多视图，白底影棚，统一侧光+轮廓光..." |
| **例外路径（无参考图）** | 概念产品、虚拟产品、早期设计阶段、用户明确要求纯文字定义产品 | 必须用文字精确描述产品外观（材质、配色、形状、设计特征） | "白底影棚，一瓶方形琥珀色玻璃香水瓶，胡桃木瓶盖，瓶身刻有竖条纹..." |

**核心要求**（两条路径共用）：
- **白底/纯色影棚**，不引入任何环境元素——纯粹锁定产品本身
- **光影至少双光源**：主光（侧光定型）+ 辅光（轮廓光分离背景）
- **例外路径额外要求——材质必须精写**：不是"金属外壳"，而是"拉丝纹理钛金属外壳，倒角处可见 CNC 加工的同心圆刀痕"

**做几张？怎么选？**

| 方案 | 什么时候用 |
|------|-----------|
| **产品多视图（TVC 默认）** | 一张图包含多角度全身 + 关键细节特写。TVC 广告中产品必然多角度出镜，多视图是标准第一资产 |
| 单张 Hero Shot | 仅当产品只从单一角度出镜（极少见于 TVC） |
| 额外材质微距 | 分镜中有极致微距镜头时，在多视图基础上追加一张独立微距 |

TVC 广告**默认生成产品多视图**。不要逐张单独出 Hero Shot、侧面图、微距——一张多视图把多角度和关键细节全部锁定，效率最高、一致性最好。

**产品多视图提示词模板**：

默认路径（有参考图）：
```
参考图片，为这个产品生成多视图。白底影棚，统一侧光+轮廓光。
包含以下视角：3/4经典角度全身、正面全身、侧面全身、背面全身，
以及2-3个关键细节微距特写（如瓶盖/按键/材质纹理/接口等产品最具辨识度的局部）。
保持所有视角的光影方向和色温一致。
```

例外路径（无参考图）：
```
白底影棚，[产品完整外观描述]的多视图。统一侧光+轮廓光。
包含以下视角：3/4经典角度全身、正面全身、侧面全身、背面全身，
以及[具体细节部位1]微距特写和[具体细节部位2]微距特写。
保持所有视角的光影方向和色温一致。
```

#### 2.2 角色资产图

**目的**：锁定人物的体态、服装、配饰、气质（以及面部，如适用）。后续所有该人物出镜帧都引用它。

**三条 prompt 路径**：

| 路径 | 触发条件 | prompt 写法 |
|------|---------|-----------|
| **有脸部参考图 + 有产品/服装参考图** | 用户提供了模特照片和产品图 | `(图1)模特参考, (图2)产品/服装参考`，在提示词中引用两张图，不描述人物外貌和产品外观 |
| **有脸部参考图，无产品参考** | 用户只提供了模特照片 | `参考图片，为图中人物生成xxx`，不描述外貌，但需文字描述服装/造型 |
| **无参考图** | 用户无任何人物参考 | 必须用文字精确描述外貌+体态+服装+配饰，纯文生图 |

**核心要求**（所有路径共用）：
- **白底，统一光影**：柔和影棚光，所有视角光影方向和色温一致
- **服装与品牌调性统一**：科技产品配简约都市风，茶饮配自然棉麻风，先锋品牌配暗黑机能风
- **表情保持中性自然**：具体情绪留到分镜帧再给
- **无参考图路径额外要求——面部特征锁 2-3 个关键点**：如"鹅蛋脸、杏眼、黑色齐肩直发"——过多细节反而让 AI 难以保持一致
- **无参考图路径的人物描述层次**：`[身份] + [体态] + [面部特征] + [服装完整描述] + [配饰] + [气质]`

**资产图永远是全身**：

角色资产图 = 选角定妆照。真正的 TVC 导演选角时永远看完整的人——镜头只拍腿/手/背影是拍摄时的决策，不是选角时的决策。服装是一个整体造型系统（上装+下装+鞋+配饰互相呼应），只拍半身会丢失造型的完整语境。

| 面部是否出镜 | 资产图格式 | 说明 |
|------------|----------|------|
| **含面部** | **完整三视图**：面部特写 + 全身正面 + 全身背面 | 标准格式 |
| **无面部/遮挡面部** | **造型展示图**：全身正面 + 全身侧面 + 全身背面 + 关键配饰特写 | 面部可遮挡/下半脸/侧颜，重点锁定服装和配饰完整造型 |
| 仅 1-2 格远景剪影/背影 | **不做资产图**，用出镜者标准描述代替 | 见 Part 3 角色一致性 |

> **禁止生成半身/局部角色资产图。** 即使分镜中只有下半身或手部出镜，资产图也必须是全身——造型的整体性决定了每个局部的视觉逻辑。

**穿戴产品的角色资产必须引用产品图**：

当产品穿在身上/戴在手上/拿在手里时（跑鞋、手表、首饰、外套、眼镜、手袋等），角色资产图提示词**必须引用前期已生成的产品多视图**，让角色穿着/佩戴产品出镜。写法：在 Nano Banana Pro 的 edit 模式下上传产品多视图，提示词中用 `(图N)` 引用——`穿着图1的跑鞋` / `手腕佩戴图1的手表` / `身穿图1的外套`。不引用产品图 = 角色脚上/手上/身上的产品外观不可控 = 后续分镜一致性崩塌。

##### 角色资产图提示词示例

**示例 1：纯文字生成（无参考图，含面部）——古风汉服模特**

```
一张高品质的影棚写真三视图，包含人物脸部特写，正面全身，背面全身。
一位美丽的年轻女子身着精致的淡香槟金与豆沙色调的唐风汉服，全身像站立。
汉服面料为细腻的丝绸质感，点缀着柔和的浅蓝、粉色花卉刺绣以及古典的暗纹。
腰间系着一条带有精致青玉带扣的青绿色腰带。她梳着端庄的云髻，
饰以简约而华丽的花卉发饰、珍珠耳坠和流苏步摇。
她的双手端庄地叠放在腰前，广袖自然垂落，呈现出优雅大方的姿态。
人物直视镜头，眼神清澈，表情从容。
纯白背景，柔和的影棚光影，8k分辨率，超逼真的写实主义，极其细腻的布料纹理。
```

**示例 2：有脸部参考图 + 有服装参考图——时尚穿搭多格展示**

```
大师级作品，8K超高清，写实照片，16:9横版构图，4格时尚展示排版，
第一格：图1女性的特写肖像，穿着图2的豹纹连衣裙，白色干净背景，柔和影棚灯光，
第二格：同一女性的全身正面照，穿着图2的修身长袖V领豹纹迷你裙，
手拿图2的黑色小手提包，裸色尖头高跟鞋，自然站立，白色影棚背景，
第三格：同一女性的全身侧面照，同款穿搭、包包、鞋子，自然站立，白色背景，
第四格：同一女性的全身背面照，同款穿搭、包包、鞋子，自然站立，白色背景，
五官完全一致，发型一致（长波浪深棕发），配饰一致（细银项链、小耳钉、银手镯、戒指），
肤色一致，专业时尚画册风格，光线统一，对焦清晰，无变形，无模糊
```

> 示例 2 的关键写法：用 `(图1)` 锁定脸部/体态，用 `(图2)` 锁定服装/配饰外观，提示词只描述穿搭组合方式和展示角度——外观细节交给参考图。每格用"同一女性""同款穿搭"强化一致性。

**示例 3：无面部 + 引用产品图——跑鞋 TVC 模特造型展示图**

```
大师级作品，8K超高清，写实照片，16:9横版构图，4格运动造型展示排版，
第一格：一位美丽的、身材纤细的年轻亚洲女性的全身正面照，黑色高马尾，
身穿黑色高腰修身九分跑步紧身裤（哑光压缩面料，裤脚贴合脚踝上方），
浅灰色短款修身速干上衣，脚穿图1的白色跑鞋，极短隐形袜露出纤细脚踝，
自然站立双手放松垂于身侧，面部微微低头仅露下巴线条，
白色干净背景，柔和影棚灯光，
第二格：同一女性的全身侧面照，同款穿搭，脚穿图1的白色跑鞋，
自然站立，展示跑裤侧线剪裁和图1跑鞋侧面完整轮廓，白色背景，
第三格：同一女性的全身背面照，同款穿搭，脚穿图1的白色跑鞋，
自然站立，展示上衣后背线条和跑裤臀线剪裁，白色背景，
第四格：同一女性的脚踝与跑鞋特写，图1的白色跑鞋与纤细脚踝的比例关系，
鞋面编织纹理清晰可见，裤脚收口与鞋口之间露出一截肌肤，
体态完全一致，服装完全一致，发型一致（黑色高马尾），肤色一致，
专业运动画册风格，光线统一，对焦清晰，无变形，无模糊
```

> 示例 3 的关键写法：**每格都重复写 `脚穿图1的白色跑鞋` 或 `图1的白色跑鞋`**——产品引用只写一次容易被 AI 忽略，每格重复才能确保每个视角都穿着产品。格式参考示例 2 的"同一女性""同款穿搭"写法强化一致性。面部通过低头规避正脸但保留发型信息。

**产品引用铁律**：当角色穿戴产品时，提示词中**每格都必须重复产品引用**（`脚穿图1的xxx` / `手腕佩戴图1的xxx`），不可只在开头提一次。单次提及的权重不足以让 AI 在所有视角中都正确渲染产品。

#### 2.3 场景图

**目的**：锁定品牌世界的视觉氛围——空间、光影、色调、时间。后续该场景中的所有帧都延续这个视觉基调。

**两条 prompt 路径**：

| 路径 | prompt 写法 | 示例 |
|------|-----------|------|
| **有参考图** | `参考图片，基于图中场景氛围生成xxx` — 不描述场景细节 | "参考图片，基于图中场景氛围生成 16:9 宽幅空镜，无人物无产品，保持相同色调和光影基调" |
| **无参考图** | 必须用文字精确描述空间、色调、光影、时间 | "16:9 宽幅，北欧极简公寓客厅清晨，落地窗洒入金色晨光，白墙灰地板..." |

**核心要求**（两条路径共用）：
- **无人物、无产品**：场景图只锁定"空间本身"，人和产品在分镜帧中再加入
- **时间和天气必须明确**：同一个茶园，清晨薄雾和正午烈日是完全不同的两张图
- **色调是核心交付**：场景图最重要的产出是"色调基准"
- **前中远景分层**：场景必须有空间纵深感
- **宽幅 16:9**

**做几张？**
- 分镜中每一个**视觉上明显不同的空间**做一张
- 同一空间的不同角落不需要分开做

---

### Part 3: 一致性——资产图的核心价值

> 资产图的价值不是"好看"，而是"可引用"。后续分镜帧通过引用资产图来确保全片视觉一致。

#### 产品一致性

基于产品图建立一段**产品标准描述**，所有后续帧的提示词统一复用：

```
[产品名]，[核心材质] + [配色]，[关键设计特征1]，[关键设计特征2]。
```

#### 角色一致性

- **有资产图**：后续帧用参考图引用（`图中[角色名]` 或 `(图N)`），不重复描述外貌
- **无资产图（剪影/远景等不做资产的情况）**：建立一段**人物标准描述**，所有后续帧统一复用：
  `[肤色/人种] + [体态] + [服装款式+颜色] + [关键配饰]`
  示例："亚洲男性，精瘦跑者体型，黑色紧身九分跑裤，深灰速干背心，无配饰"
- 服装/发型/体型描述保持不变，只有表情和姿态可以变化

#### 场景一致性

- 同一场景的不同镜头，色调、光线方向、大气效果保持一致
- 场景图的色调是"基准色"，后续帧可以微调但不跳变

#### 跨资产协调

- 产品色调和场景色调要协调——暖场景配暖产品光影
- 人物服装色与品牌色/场景色有呼应
- 所有资产统一使用同一画风方向

---

<a id="src-tvc-ai-director-references-prompt-style-guide-md"></a>

## `tvc-ai-director/references/prompt-style-guide.md`

## Prompt Style Guide

Use for AI-generated TVC images and videos.

### Global Continuity Block

Write this before per-shot prompts:

- Brand/product: name, package, color, logo visibility, surface, scale.
- Actor: age range, face features, hair, makeup, wardrobe, expression range.
- World: location, time, art direction, props, weather, atmosphere.
- Camera: lens family, shot grammar, movement limits.
- Light/color: key light, contrast, color palette, texture.
- Forbidden drift: face changes, product deformation, extra text, random logos.

### Image Prompt Pattern

```markdown
生成一张 16:9 TVC 分镜关键帧：
主体：
产品：
场景：
动作瞬间：
构图：
镜头/焦段：
光影：
影调：
质感：
画面不出现：
```

### Video Prompt Pattern

```markdown
生成 4 秒 16:9 TVC 视频镜头：
起始画面：
主体动作：
产品动作：
镜头运动：
光影变化：
节奏：
结束画面：
声音提示：
风格锁定：
负面约束：
```

### Complex One-Take Video Pattern

For complex action shots with multiple referenced assets, native asset IDs, a single continuous take, and detailed physical events, structure the prompt as:

```markdown
【基础设定】
角色/主体1：<node-asset>...</node-asset> 外形、材质、服装、表情/状态规则、不可变化项。
角色/主体2：<node-asset>...</node-asset> 外形、动作特征、不可变化项。
关键道具：<node-asset>...</node-asset> 尺寸、材质、启动方式、发光/变形/爆炸等状态变化。
群体/背景角色：<node-asset>...</node-asset> 数量感、外观、运动方式、危险感。

场景：<node-asset>...</node-asset> 时代、地点、天气、建筑、地面、前中后景、环境道具。
声音：是否配乐、是否氛围音、同期声保留项。

【氛围与画质】
风格核心：
视觉基调：
色彩与影调：

【画面内容】
分镜：
景别：
构图：
运镜手法：
画面内容：

负面约束：
```

Keep `分镜`, `景别`, `构图`, `运镜手法`, and `画面内容` separate. Write the action chain in physical order: hand/object interaction, prop state change, subject movement, background reaction, ending frame/camera consequence.

### Negative Prompt Defaults

Block:

- face drift, identity change, extra fingers, broken hands, warped body, plastic skin
- deformed product, wrong logo, unreadable package text, random brand marks
- random subtitles, extra captions, watermarks, UI artifacts
- flicker, camera jitter, frame jump, object melting, inconsistent lighting
- stock footage look, over-saturated color, unrelated props, crowded background

### Regeneration Notes

Use this structure:

```markdown
保留：
必须修改：
可接受变化：
不可接受：
下一轮提示词补强：
```

### Platform Notes

- If the user names a platform, adapt prompt length and terminology to that platform.
- If no platform is named, keep prompts platform-neutral and production-readable.
- For logo/package shots, prefer controlled keyframes or image-to-video references over pure text prompts.

---

<a id="src-tvc-ai-shot-prompter-references-image-prompt-method-md"></a>

## `tvc-ai-shot-prompter/references/image-prompt-method.md`

## Image Prompt Method

Use this method for still frames, key visuals, storyboard frames, packshots, and image-to-video starting frames.

### 8-Layer Structure

Write prompts in this exact order.

#### 1. Subject

Describe who or what is most important in the frame.

Bad:

- 一个创业者

Good:

- 35岁亚洲男性创业者，短黑发，黑眼圈，略显疲惫的脸，穿深色连帽卫衣

Use concrete visible traits:

- age range
- gender/presentation
- ethnicity when relevant and safe
- hair
- face condition
- wardrobe
- product shape/material/label when product is the subject

#### 2. Action

Describe visible action. AI cannot film abstract emotion directly.

Bad:

- 感到失落

Good:

- sitting alone at desk, reading rejection email, holding mouse, slightly lowering head

#### 3. Environment

Define the world:

- small startup office
- open workspace
- nighttime
- city skyline outside window
- messy desk
- coffee cups
- computer monitors

#### 4. Composition

Define the frame:

- medium close-up
- subject positioned left third
- negative space on right
- framed through monitor edge
- product centered in foreground
- low angle hero composition

#### 5. Camera

Define optical and cinematic grammar:

- 85mm lens
- shallow depth of field
- eye-level shot
- 24mm wide angle
- low angle
- handheld documentary style

#### 6. Lighting

Define actual light:

- computer screen lighting face
- dim ambient office light
- soft shadows
- natural backlight
- practical lighting only
- hard noon sunlight

#### 7. Color Palette

Separate color from lighting:

- desaturated colors
- cold blue-gray palette
- Kodak Vision3 look
- muted highlights
- orange-red product accent with ice-blue background

#### 8. Style Reference

Style comes last:

- cinematic still
- commercial photography
- Apple commercial aesthetic
- Netflix drama
- ultra realistic

### Final Formula

```text
Subject + Action + Environment + Composition + Camera + Lighting + Color Palette + Style Reference
```

### Product Prompt Notes

For product images, specify:

- product reference image if available
- shape
- package color
- cap/lid
- label layout
- logo position
- material
- condensation/texture
- scale and angle

Block:

- distorted package
- wrong logo
- hallucinated text
- extra products
- unreadable labels
- wrong material

---

<a id="src-tvc-storyboard-writer-skill-md"></a>

## `tvc-storyboard-writer/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: tvc-storyboard-writer
description: TVC storyboard script writer for director-level shot breakdowns. Use when Codex needs to turn a creative concept or director treatment into an executable storyboard script with theme extraction, emotional curve, narrative structure, visual language, shot timing,景别,镜头运动,产品/logo露出,声音设计,高潮镜头,结尾记忆点, and AI-ready shot table for advertising films.
---
```

## TVC Storyboard Writer

Use this skill as a senior TVC director, advertising creative director, and film storyboard designer. The task is not to list shots mechanically. The task is to translate a creative concept into an executable director's storyboard script.

### Required Thinking Before Shots

Before writing the shot table, complete these four thinking steps.

#### 1. 提炼创意核心

Analyze:

- 品牌想表达什么。
- 用户能感受到什么。
- 广告最终希望观众记住什么。

Summarize the advertising theme in one sentence.

#### 2. 拆解情绪曲线

Analyze the whole film's emotional progression:

- 开场情绪。
- 中段情绪。
- 高潮情绪。
- 结尾情绪。

Make the emotional escalation explicit.

#### 3. 搭建叙事结构

Define:

- 主角是谁。
- 当前处境。
- 面临什么问题。
- 如何变化。
- 最终获得什么。

If the concept has no clear story, construct a reasonable narrative.

#### 4. 设计视觉语言

Define:

- 摄影风格。
- 运镜方式。
- 光线风格。
- 色彩倾向。
- 剪辑节奏。

Avoid empty words such as "高级感" or "电影感" unless concretely defined. Use specific language, for example:

- `35mm 手持跟拍`
- `长焦压缩空间`
- `自然逆光`
- `低饱和暖灰色调`
- `macro product insert`
- `快速 0.5 秒细节切`

### Workflow

1. Confirm format:
   - Duration, ratio, channels, dialogue/VO/super needs, product/logo requirements, AI/live-action mode.
   - If the user asks for Excel/表格/xlsx, keep shot fields spreadsheet-ready and include a `时间码` column.

2. Complete the four thinking steps above.

3. Build timing:
   - Assign seconds to setup, development, product proof, climax, and ending memory point.
   - Keep the total duration controlled.

4. Write the shot table:
   - Every shot must have a reason to exist.
   - Every shot must push emotion or narrative.
   - No meaningless transition shots.
   - Prefer visual storytelling over VO explanation.
   - Shots must create rhythm changes.
   - Mark key product/logo exposure nodes.
   - Mark the climax shot.
   - Mark the ending memory-point shot.

### Output Format

```markdown
# 广告主题

一句话概括

# 故事概述

100字以内

# 视觉风格

详细描述

# 情绪曲线

阶段1：
阶段2：
阶段3：
阶段4：

# 分镜头脚本

| 镜号 | 时长 | 景别 | 画面内容 | 镜头运动 | 产品/logo | 声音 |
|------|------|------|---------|-----------|-----------|------|
```

When the user asks for a spreadsheet or the storyboard will be handed to `$tvc-ai-shot-prompter`, use the expanded table:

```markdown
| 镜号 | 时间码 | 时长 | 景别 | 画面内容 | 镜头运动 | 产品/logo | 声音/字幕 |
| --- | --- | --- | --- | --- | --- | --- | --- |
```

### Shot Table Rules

- In `画面内容`, include the subject, action, emotional state, and visual reason.
- In `镜头运动`, specify actual camera grammar, not vague movement.
- In `产品/logo`, mark `无`, `局部露出`, `完整露出`, `高潮产品镜头`, or `结尾记忆点`.
- In `声音`, include music, SFX, VO, silence, or sound transition.
- For Excel-ready work, make every row one shot only; do not combine multiple shots in one row.
- Keep total timing continuous and exact; `时间码` should cover the full target duration without gaps.
- Add `[高潮镜头]` in the relevant shot.
- Add `[结尾记忆点]` in the final memory shot.

### Quality Bar

- The storyboard must be shootable or AI-generatable.
- The emotional curve must be visible in the shot order.
- Product/logo exposure must be motivated by the story.
- Every shot must connect to the creative theme.
- Preserve actor, wardrobe, product, prop, light, and color continuity.
- Make each shot ready for `$tvc-ai-shot-prompter`.

---

<a id="src-tvc-ai-shot-prompter-skill-md"></a>

## `tvc-ai-shot-prompter/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: tvc-ai-shot-prompter
description: TVC AI shot prompter for image and video generation. Use when Codex needs to create structured image prompts, Seedance-style video prompts, cinematic long-take video prompts, node-asset reference prompts, negative prompts, visual continuity rules, actor/product consistency, camera movement, lighting, color, duration, ratio, sound cue notes, regeneration instructions, or prompt tables for TVC storyboard shots.
---
```

## TVC AI Shot Prompter

Use this skill to convert storyboard shots into executable image prompts and video prompts.

The image prompt and video prompt use different methods:

- Image prompt: use the 8-layer still-image structure.
- Video prompt: use the Seedance-style video structure based on referenced materials, segmented timing, camera movement, audio, and product continuity.
- For complex single-shot cinematic action prompts, use the cinematic long-take structure in `references/video-prompt-method.md`: base assets, scene, sound, atmosphere/quality, visual tone, color, shot design, action chain, ending event, and negative constraints.

### Workflow

1. Create continuity anchors:
   - Brand/product identity.
   - Actor identity, wardrobe, makeup, hair.
   - Location, props, art direction.
   - Lighting, color, lens, camera behavior.
   - Reference assets and how to cite them with `@` when a video model supports material references.

2. Load prompt methods when needed:
   - Read `references/image-prompt-method.md` for still image prompts.
   - Read `references/video-prompt-method.md` for video prompts.

3. For each storyboard shot, write:
   - Image prompt using: Subject + Action + Environment + Composition + Camera + Lighting + Color + Style.
   - Video prompt using: reference material + duration/ratio + time-segmented action + camera movement + product/actor continuity + sound/music + negative constraints.
   - For prompts with multiple referenced characters, props, vehicles, creatures, or `node-asset` IDs, first create a `基础设定` block that locks each asset's identity, costume/material, behavior, and allowed expression/state changes.
   - Negative prompt.
   - Continuity lock.
   - Regeneration notes.
   - If the user asks for Excel/表格/xlsx, preserve storyboard columns and append prompt columns so the table can be exported directly.

4. Keep prompts executable:
   - Use concrete visual facts instead of abstract emotions.
   - Write actions, not feelings.
   - Separate lighting from color palette.
   - Put style reference last.
   - Do not overload one shot with multiple unrelated events.

### Output Format

```markdown
全片一致性设定：
素材引用规则：
镜头 Prompt 表：
重生成策略：
下游交接：
```

Prompt table columns:

```markdown
| 镜号 | 图片 Prompt | 视频 Prompt | 负面约束 | 连续性锁定 | 重生成备注 |
| --- | --- | --- | --- | --- | --- |
```

Excel-ready combined table columns:

```markdown
| 镜号 | 时间码 | 时长 | 景别 | 画面内容 | 镜头运动 | 产品/logo | 声音/字幕 | 图片 Prompt | 视频 Prompt | 负面约束 | 连续性锁定 | 重生成备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

### Image Prompt Method

Write still-image prompts in this order:

1. Subject.
2. Action.
3. Environment.
4. Composition.
5. Camera.
6. Lighting.
7. Color Palette.
8. Style Reference.

Do not start with style. Do not write abstract identity only. Describe visible traits, visible actions, and concrete cinematic grammar.

### Video Prompt Method

Use Seedance-style video prompt logic:

- State referenced assets with `@` when available, such as `@product_reference`, `@character_reference`, `@scene_reference`.
- Preserve native asset tags such as `<node-asset>...</node-asset>` when the target platform uses them. Describe what each asset controls immediately after the tag.
- Specify duration and aspect ratio.
- Break motion into time segments when the shot has a beginning, middle, and end.
- Describe camera movement, subject movement, product movement, and ending frame.
- Add sound, music, SFX, or silence cues when useful.
- For product shots, protect package shape, logo, label, material, and scale.
- For one-take action shots, separate `分镜`, `景别`, `构图`, `运镜手法`, and `画面内容` so the model gets both cinematography and event order.

### Prompt Quality Bar

- State what must remain identical across shots.
- Put product shape, logo visibility, and hand interaction rules in the prompt when relevant.
- Avoid impossible camera moves, contradictory light, and multiple time jumps in one generated shot.
- Negative prompts must block extra fingers, warped logos, unreadable text, face drift, product deformation, random subtitles, and unwanted style shifts.
- If a prompt says "失落", "高级", "清爽", or "电影感", translate it into visible action, composition, camera, light, color, or sound.

---

<a id="src-tvc-ai-shot-prompter-references-video-prompt-method-md"></a>

## `tvc-ai-shot-prompter/references/video-prompt-method.md`

## Video Prompt Method

Use this method for video-generation prompts. It is adapted from the Seedance2 prompt-writing approach supplied by the user: material references, precise camera language, time-segmented motion, sound/music cues, and product continuity.

### Core Formula

```text
@Reference assets + Duration/ratio + Scene setup + Time-segmented action + Camera movement + Subject/product movement + Lighting/color continuity + Sound/music cues + Ending frame + Negative constraints
```

For high-complexity one-take action shots, use the expanded formula:

```text
基础设定 + 场景 + 声音 + 氛围与画质 + 视觉基调 + 色彩与影调 + 画面内容(分镜/景别/构图/运镜/动作链) + 结尾事件 + 负面约束
```

### Reference Assets

When the video model supports material references, name assets with `@`:

- `@product_reference`: product bottle, package, logo, packshot.
- `@character_reference`: actor/persona consistency.
- `@wardrobe_reference`: outfit consistency.
- `@scene_reference`: location/world.
- `@style_reference`: visual tone.

Explain what each reference controls:

```markdown
@product_reference: only controls bottle shape, package color, label layout, logo position, and material.
@character_reference: controls face, hairstyle, wardrobe, and body proportion.
```

If the target platform uses native asset tags, keep them verbatim:

```markdown
机器人清道夫：<node-asset>...</node-asset>  controls body shape, costume, LED face display, expression state, and prop interaction.
场景：<node-asset>...</node-asset> controls architecture, street layout, background props, and environmental continuity.
```

For every asset, define:

- Identity and visible design.
- Material/costume/surface.
- Behavior range.
- Expression or state changes.
- What must never drift.

### Time Segments

Use segments when a shot has progression:

```text
0-1s: starting frame/action.
1-3s: main movement.
3-4s: ending frame or transition state.
```

This prevents vague prompts like "the scene becomes energetic".

### Camera Movement

Use precise terms:

- slow push-in
- handheld follow shot
- locked-off macro close-up
- orbit around product
- low-angle dolly-in
- whip pan
- rack focus from product to face
- top-down product reveal

Avoid:

- cinematic movement
- dynamic shot
- cool camera

### Subject and Product Movement

Describe what moves:

- actor turns head, lowers eyes, opens bottle, takes one sip
- condensation rolls down bottle
- tea liquid catches sunlight
- orange heat-wave ribbons spiral into bottle mouth
- product remains centered and readable

### Sound and Music

Include only useful audio cues:

- bottle cap click
- reverse whoosh
- ice crack
- low city rumble
- music beat enters at 2s
- short silence before product reveal

When the user requests production sound only, state it directly:

```markdown
声音：不需要配乐，不要氛围音，仅保留同期声。保留脚步、衣料摩擦、机械声、道具声、爆炸声、呼吸声或环境内真实声源。
```

### Product Continuity

For commercial shots:

- Keep product package identical to reference.
- Do not invent text or slogans.
- Keep logo readable when the shot's job is product recognition.
- Use post-composited real package when model text fidelity is risky.

### Cinematic Long-Take Prompt Pattern

Use this pattern when a video prompt contains many assets, a single continuous shot, precise cinematography, and a chain of actions. This structure is useful for TVC action scenes, character-driven product shots, and AI video models that respond well to long-form scene prompts.

#### 1. 基础设定

Lock every reusable asset before describing the shot:

```markdown
【基础设定】

角色A：<node-asset>...</node-asset> 外形、时代风格、材质、服装、表情规则、可做动作、不可变化项。
角色B：<node-asset>...</node-asset> 外形、性格化特征、动作特征、不可变化项。
关键道具：<node-asset>...</node-asset> 尺寸、材质、启动方式、发光/变形/爆炸等状态变化。
群体角色：<node-asset>...</node-asset> 数量感、外观、运动方式、危险感、不可变化项。
```

Rules:

- Use concrete visible facts, not abstract labels only.
- If a face is a screen, define whether expressions are static or animated.
- If a prop changes state, write the state chain in order.
- If a character has a comic or ugly trait, describe visible features precisely.

#### 2. 场景

Define world, period, location, weather, background activity, and set dressing:

```markdown
场景：<node-asset>...</node-asset> 时代、城市/室内/荒野、危机状态、建筑语言、地面材质、道具散落、尸体/车辆/报纸/烟尘等环境细节。
```

Rules:

- Treat the environment as a story engine, not wallpaper.
- Include foreground, midground, background responsibilities when the shot needs depth.
- Put continuity objects here if they must remain across shots.

#### 3. 声音

Define music, ambience, and sync sound separately:

```markdown
声音：不需要配乐；不要氛围音；仅保留同期声：脚步、机械关节、道具按钮、风声、爆炸、角色叫声。
```

Rules:

- If no music is wanted, say so explicitly.
- Do not add mood music if the user asks for production sound only.
- Use sound to support the action chain.

#### 4. 氛围与画质

Define genre, realism, texture, and blocked aesthetics:

```markdown
【氛围与画质】
风格核心：原子朋克、末日危机、电影级质感、超写实、真人实景拍摄感。
画质要求：Photorealism, ultra realistic, no game CGI look, no stiff slow motion unless requested.
情绪目标：逃亡、追逐、危机感、紧迫感。
```

Rules:

- Put negative style constraints here when they affect the whole shot.
- Translate broad style words into texture, realism, camera, or motion rules.

#### 5. 视觉基调

Define camera system, lens family, format, and motion rendering:

```markdown
视觉基调：anamorphic widescreen cinematic look, IMAX film camera feel, Panavision C-series lens character, shallow depth of field, telephoto compression, natural motion blur.
```

Rules:

- Use camera and lens grammar only when it changes the image.
- Do not stack incompatible camera formats.
- State motion blur when high-speed action is essential.

#### 6. 色彩与影调

Separate color from lighting:

```markdown
色彩与影调：1960s retro-futurist atom-punk palette, warm orange and sea-salt blue contrast, low-saturation vintage film filter, film grain, strong direct sunlight, natural sun flare, preserved highlight detail, readable shadow detail.
```

Rules:

- Lighting = source and behavior of light.
- Color = palette, saturation, film stock feel, contrast.
- Avoid overexposure if product or character identity matters.

#### 7. 画面内容

Break the shot into production grammar before writing the action:

```markdown
【画面内容】

分镜：单镜头一镜到底。
景别：近景，浅景深，长焦压缩空间。
构图：前景主体位于画面右侧，占画面二分之一；背景追击群体位于左侧远处；主体与街道形成动态对角线。
运镜手法：固定机位，跟随拍摄主体。
画面内容：按时间顺序写动作链、道具状态变化、追击关系、爆炸/冲击/失焦等结尾事件。
```

Rules:

- Keep `分镜`, `景别`, `构图`, `运镜手法`, and `画面内容` as separate fields.
- For single-shot prompts, action order must be unambiguous.
- Every prop interaction should include hand, object, trigger, state change, and consequence.
- Ending event should specify what happens to the camera image: shake, blur, focus loss, hard cut, object exits frame.

#### 8. 负面约束

End with global and shot-specific negative constraints:

```markdown
负面约束：不要游戏CG感，不要动作迟钝僵硬，不要角色身份漂移，不要错误服装，不要错误道具形状，不要随机字幕，不要过曝，不要镜头无意义乱晃，不要额外角色抢主体。
```

### Long-Take Template

```markdown
【基础设定】
角色/主体1：<node-asset>...</node-asset> ...
角色/主体2：<node-asset>...</node-asset> ...
关键道具：<node-asset>...</node-asset> ...
群体/背景角色：<node-asset>...</node-asset> ...

场景：<node-asset>...</node-asset> ...
声音：...

【氛围与画质】
风格核心：
视觉基调：
色彩与影调：

【画面内容】
分镜：
景别：
构图：
运镜手法：
画面内容：

负面约束：
```

### Video Prompt Template

```markdown
生成 <duration> 秒 <ratio> TVC 视频镜头。
参考素材：
- @product_reference: ...
- @character_reference: ...

画面设定：
0-1s：
1-3s：
3-<duration>s：

镜头运动：
主体动作：
产品动作：
光影与色彩：
声音/音乐：
结束画面：
连续性要求：
负面约束：
```

### Negative Constraints

Always block:

- face drift
- identity change
- extra fingers
- warped hands
- deformed product
- wrong logo
- hallucinated text
- random subtitles
- flicker
- camera jitter
- object melting
- inconsistent lighting
- stock footage look
- unrelated props

---

<a id="src-tvc-director-references-storyboard-md"></a>

## `tvc-director/references/storyboard.md`

## TVC 分镜与视频工程知识库

> **职责**：分镜与拍摄阶段的唯一参考。覆盖多宫格分镜、视频提示词语法、产品电影化拆解和品牌世界镜头。多宫格和视频提示词是配套交付物——每张多宫格对应一段视频提示词。
> **不管**：创意策略（查 treatment.md）、图片提示词句法（查 shot-language.md）、输出格式与迭代（查 delivery.md）。

---

### Part 1: 多宫格分镜

---

### 一、多宫格提示词四层结构

一条完整的多宫格提示词由四层组成，按以下顺序排列：

#### 第一层：全局风格

定义整张图的视觉基调和物理格式。必须包含：

- **网格声明**：`生成一张包含N个分镜的组合图，按RxC网格排列`
- **画风锚定**：与 Phase 3 确认的画风方向一致（参考 `art-style-library.md`）
- **画面比例**：整张多宫格图的比例（通常 16:9 或 1:1）
- **渲染/拍摄系统**（可选）：如 `由ARRI Alexa电影摄影机拍摄` 或 `虚幻引擎5实时渲染`，用于锁定画面质感

示例写法：
> 生成一张包含9个分镜的组合图，按3x3网格排列。3D奇幻动画风格，由ARRI Alexa电影摄影机拍摄，16:9横屏。

#### 第二层：参考图映射

当使用 `edit` 模式引用 Phase 4 资产图时，在此层建立映射关系。

格式：`(图1)[资产类型/名称], (图2)[资产类型/名称]...`

如果无参考图（纯文生图），跳过此层，在第一层中用文字描述角色/环境的关键外观特征。

#### 第三层：叙事主线 + 逐格描述

这是多宫格提示词的核心。写法随**剧情密度**变化——详见第四节。

#### 第四层：一致性锚

在全部逐格描述之后，追加全局一致性要求：

- **风格统一**：`保持整体风格统一`（必须有）
- **视觉母题**：贯穿全部面板的反复出现元素（如某个颜色、某种光效、某个道具）
- **色调连续性**：描述跨面板的色彩/光影渐变趋势
- **角色一致**：如有角色跨格出现，强调外观不可变化
- **视频流**：简述 9 格如何作为视频流动——运镜轨迹、产品状态变化、关键转场点（如 `视频流：全景引入(P1)→弧形绕瓶(P2-P3)→微距潜入(P4)→...→定格(P9)`）。这不是给图片生成模型看的指令，而是给下游视频提示词写作用的思维锚点

---

### 二、视频脉络先行

多宫格不是 9 张美图的拼盘——它是从一条 15 秒视频中冻结出来的 9 个关键帧。**先有流，再有帧。**

#### 核心原则

写逐格描述之前，先用 1-2 句话勾勒这 15 秒的**视频脉络**：镜头语言怎么连续、产品状态怎么变、画面之间怎么衔接。视频脉络是时间轴上的因果链——每格承接什么、过渡到什么——而不只是"9 格放在一起好看"。

视频脉络**不等于一镜到底**。它可以包含硬切、匹配剪辑、溶解、跳切等各种转场——关键是镜头语言的连续性，而非镜头物理上的连续运动。一镜到底是一种选择，多镜头剪辑也是一种选择，但每个格子都必须知道自己在时间轴上的位置。

多宫格是视频脉络的**冻结**，视频提示词是视频脉络的**展开**。两者从同一条脉络生长，不存在"先做图再配视频"的先后关系。

#### 三种密度，同一原则

- **高密度**的"叙事主线"天然就是视频脉络——角色动作穿格流动，时间因果内嵌在叙事中
- **中密度**的"旅程概述"接近视频脉络——场景递进本身包含时间流
- **低密度没有故事，但必须有视频脉络**——镜头语言的连续性、光影变化、产品状态转换就是低密度的时间因果。"无叙事弧线"不等于"无时间流"

#### 视频脉络的写法（低密度示例）

在逐格描述之前，加一行视频脉络：

> 视频脉络：缓推入阳台全景→桌面静物画→侧面低角度穿透瓶身焦散→逆光帘布前瓶身剪影→猫抬头与前景虚化瓶身的琥珀色呼应→俯拍桌面静物锚点→瓶盖微距→栏杆上瓶身与远景→她走来，桌上瓶身在远端

这段脉络里，P5 的猫有明确的时间位置：它承接 P4 的逆光氛围，前景虚化瓶身提供产品存在感，过渡到 P6 的俯拍总览。每格知道自己从哪来、到哪去。

#### 视频脉络不是提示词的一部分

视频脉络是写作前的**思维步骤**，不是输出给图片生成模型的文本。它可以写在第四层一致性锚的"视频流"注释中（给下游视频提示词参考），但不会出现在第一至第三层的提示词正文中。

#### 动态特效的分工

当创意方案包含动态视觉特效（材质变形、粒子汇聚、能量流动等）时：**多宫格只冻结特效的结果态，视频提示词描述特效的完整过程。** 多宫格是静态关键帧，无法表达"变化"——硬写过程只会让画面混乱。

| 动态概念 | 多宫格（冻结结果态） | 视频提示词（描述完整过程） |
|---------|-------------------|----------------------|
| 液态金属凝结成产品 | 产品已完整成型 | 液态金属流动→减速→凝结→表面纹理渐变→成型 |
| 产品悬浮拆解 | 组件已分离的爆炸视图 | 组件缓慢分离、悬浮、能量线连接的动画 |
| 屏幕点亮 | 屏幕已亮，显示界面 | 像素点从中心亮起→波纹扩散→界面元素浮现 |
| 粒子汇聚成型 | 产品已完整呈现 | 粒子从四面八方汇聚→轮廓显现→表面凝固 |
| 水珠在鞋面滚落 | 水珠凝在鞋面某处 | 水珠沿面料滑动→证明防水性能 |
| 液体被碰洒（咖啡/红酒） | 液体已悬浮在空中，形成凝固的弧形液柱 | 杯被碰倒→液体飞出→在空中凝固→被接住/扶正 |
| 人物被"冻结" | 人物保持行走/动作姿态静止不动，衣角悬停 | 所有人突然停止运动→环境声消失→只有主角自由活动 |
| 纸张/碎片风暴 | 纸张以各种角度悬停在空中不动 | 风起→纸张翻飞→骤然静止悬浮→被逐张取走 |

---

### 三、网格规格选择策略

| 规格 | 格数 | 时长覆盖 | 适用场景 |
|------|------|---------|---------|
| **3x3** | 9格 | ≈15秒 | 标准叙事段落、产品宣传完整流程、最常用 |
| **2x2** | 4格 | ≈5-8秒 | 短转场序列、精简片段、片头/片尾 |
| **2x3** | 6格 | ≈10秒 | 中等密度叙事、竖版视频 |
| **3x2** | 6格 | ≈10秒 | 横版中等密度 |

选择原则：默认 **3x3**；内容不足 6 帧时用 **2x2** 或 **2x3**；竖版偏好 **2x3**，横版偏好 **3x2** 或 **3x3**。

---

### 四、剧情密度光谱：逐格描述的写法

多宫格的核心差异在于**剧情密度**——角色动作/故事推进占多少比重 vs 摄影指令/视觉设计占多少比重。

**TVC 密度声明**：TVC 广告只使用**低密度**和**中密度**两种模式，低密度为默认。高密度模式（景别交给 AI 判断）不适用于 TVC——广告的每一帧都需要精确的美学控制，不可将构图决策权交给 AI。

#### 4.1 中密度：场景递进

**特征**：有叙事推进（旅程/过程），但每格也是相对独立的场景。动作与摄影指令混合。

**写法**：先写一句叙事主线概括旅程，然后逐格描述。景别可写可不写。

**完整示例**（牧场清晨·走进牧场）：

```
生成一张包含9个分镜的组合图，按3x3网格排列。
真人实拍，电影级摄影，自然光照，16:9横屏。

叙事线：黎明前的高山牧场，牧场主独自起身、出门、穿过薄雾走向牛群的完整清晨。
色调从第1格的冷蓝灰逐渐过渡至第9格的暖金绿，模拟晨光照亮牧场的过程。

1. 连绵丘陵被蓝灰薄雾笼罩，天空从深蓝渐变为微金。画面最底部，木屋窗户透出的橘黄灯光是唯一暖色。
2. 牧场主粗糙的双手在昏黄灯光下拧开老式黄铜水龙头，清水冲过指缝，水珠沿粗粝皮肤滚动。
3. 薄雾中木栅栏消失在远处，栅栏上凝结水珠，一只旧皮手套搭在横杆上——他刚经过这里。
4. 低角度跟随旧棕色皮靴踩过湿草地，每一步草叶弯折、露珠飞溅弹起。光线逐渐变暖。
5. 牧场主推开牛棚厚重木门，金色晨光从门缝涌入形成放射状光柱，照亮空气中飞舞的微尘。
6. 蛛网上的露珠被涌入的晨光照亮，丝线如银弦闪烁。一颗露珠受到微振缓缓滑落。
7. 金色丁达尔光柱穿透浓雾照亮前景草地，光柱中细微尘粒飘浮。雾气深处，穿工装外套的人影剪影正朝牧场深处走去。
8. 橡树枝叶间隙透出金色晨光，叶片边缘半透明金绿色。树下阴影处一个锃亮金属奶桶，桶壁反射一道暖光。
9. 牧场全景，薄雾散开，金色阳光铺满草场。远处牧场主的身影已走到牛群附近，人与牛被暖光勾勒出金色边缘。

保持整体风格统一。视觉母题：牧场主的"手"和"足迹"贯穿全部面板。
丁达尔光柱和草尖露珠作为环境线索反复出现。电影级调色。
```

#### 4.2 低密度：视觉驱动（TVC 默认）

**特征**：无叙事弧线，但有**视频脉络**——每格是从一条镜头语言连续的视频中提取的关键帧，而非独立的视觉设计。纯产品/氛围展示，精确的摄影指令。

**写法**：先写一句**视频脉络**（镜头语言的连续性 + 产品状态流），再逐格描述。每格以 `[景别·视角]` 开头，精确指定镜头语言、光影设计、产品角度。

**完整示例**（香水广告·多角度光影展示）：

```
生成一张包含9个分镜的组合图，按3x3网格排列。
以图1的香水产品作为主体，纯黑背景，暖金侧光+白色烟雾，奢华质感。

视频脉络：全景引入→旋转展示棱面→推进穿过烟雾→远景烟雾包裹→微距铭牌→上升穿雾→晃动光影→冷暖交替扫光→落回定格

1. 大广角全景·俯拍：深棕琥珀方瓶香水静置于纯黑背景中央，暖金侧光扫过瓶身，白色烟雾从瓶身缝隙缓缓升腾，琥珀色液体微晃，凸显乌木沉香的厚重温润质感。
2. 近景·侧仰：香水瓶缓慢顺时针旋转30°，棱面反射纯黑背景与缭绕烟雾，金色铭牌被聚光打亮，烟雾随瓶身转动缠绕瓶壁。
3. 中景·平视：香水瓶向镜头缓慢推进，烟雾随推进速度弥漫扩散，暖光渐变为深金暖调，光影在烟雾与瓶身间形成层叠暖晕。
4. 远景·斜侧：香水瓶被白色烟雾半包裹，暖金侧光渐变为黄昏深金调，琥珀液体在光影中轻晃，烟雾如墨纹般摇曳。
5. 近特写·俯拍：聚光锁定金色铭牌文字，烟雾在字样上闪烁跳跃，背景纯黑与烟雾完全虚化，突出沉香的厚重高级感。
6. 全景·仰拍：香水瓶缓缓上升穿过烟雾间隙，上方暖光渐变为柔金，瓶身折射温润光泽，光影从锐利转为柔和。
7. 中景·侧拍：香水瓶轻微左右晃动，烟雾随晃动形成波浪状涌动，瓶身棱面快速切换明暗。
8. 近景·平视：香水瓶静止于背景中央，暖金与冷黑光线交替扫过瓶身，先暖光凸显木质温润，再冷光凸显玻璃通透。
9. 全景·斜俯视：香水瓶缓缓落回画面中央，暖金柔光包裹瓶身，烟雾逐渐消散，光影归于柔和静谧。

保持整体风格统一。光影弧线：暖金→深金→冷黑→暖金循环。
烟雾作为贯穿全部面板的视觉母题。
视频流：全景引入(P1)→旋转展示(P2)→推进穿雾(P3)→远景笼罩(P4)→微距铭牌(P5)→上升突破(P6)→晃动节奏(P7)→冷暖交替(P8)→落回定格(P9)。
```

#### 4.3 密度对比速查

| 维度 | 中密度 | 低密度（TVC 默认） |
|------|--------|--------|
| 叙事主线 | 建议（1句旅程概述） | **视频脉络**（1-2句镜头语言连续性/产品状态流） |
| 景别指定 | 可写可不写 | 必须写，每格开头 |
| 每格驱动力 | 场景+动作混合 | 摄影指令 |
| 格间关系 | 主题线索串联 | **视频脉络驱动的视觉节奏** |
| 每格长度 | 2-3句 | 2-4句 |

#### 4.4 同一项目中混合密度

一个项目的不同 grid 可以选不同密度。TVC 默认全部低密度。

| 项目类型 | G1 | G2 | G3 | G4 |
|---------|----|----|----|----|
| **TVC 产品广告** | **低（产品+场景建立）** | **低（产品展示/交叉）** | **低（细节+高潮）** | **低（收束定格）** |
| 品牌故事片 | 中（角色开场） | 低/中（产品旅程） | 低（产品展示） | 低（收束定格） |

---

### 五、通用写作规范（所有密度共享）

#### 5.1 叙事弧线编排

9 格的标准节奏：

| 位置 | 1-3格 | 4-6格 | 7-8格 | 9格 |
|------|-------|-------|-------|-----|
| 功能 | 建立 | 发展 | 高潮 | 余韵/收束 |

4 格叙事：建立 → 发展 → 高潮 → 收束，各一格。

#### 5.2 光影弧线

跨面板的光影应形成连续的氛围流动：明暗递进、色温漂移、高潮格设置最强烈光影反差。中密度中光影可融入叙事描述，低密度中必须每格明确指定。

#### 5.3 视觉母题

设计 1-2 个贯穿全部面板的视觉元素。母题可以是：一种光效、一个道具、一种色彩、一种构图手法。

---

### 六、与 Phase 4 资产图的配合

#### 文生图模式（无资产参考）

将角色/产品的外观特征写入第一层全局风格中：

> 主角：身着黑色铠甲的年轻女战士，银色长发，手持弯刀，右脸有一道疤痕。

#### 图生图模式（引用资产图）

在 Nano Banana Pro 中使用 edit 模式并上传资产图：
- 第一层正常写全局风格
- 第二层映射资产图：`(图1)女战士角色三视图, (图2)雪山环境概念`
- 第三层逐格描述中直接引用：`图1中的女战士站在图2的雪山峰顶...`

---

### 七、多张网格的规划策略

将视频按 15 秒为单位切割，每段对应一张 3x3 网格。**每张 grid 独立选择剧情密度**。

#### 跨网格一致性

- **全局风格**：所有网格使用完全相同的第一层
- **参考图映射**：所有网格引用同一组资产图
- **衔接过渡**：前一张网格的第 9 格氛围 ≈ 后一张网格的第 1 格氛围
- **色彩连续**：跨网格的色温变化保持渐进，不突变

---

### 八、拆分单帧的提示词模板

当下游视频模型不支持多宫格输入时，逐格拆分：

```
单独生成【第X行第Y列】的分镜图像，保持与原图完全一致的风格和角色外观
```

在 Nano Banana Pro 中使用 edit 模式，上传多宫格原图作为参考图。按阅读顺序逐格拆分。

---

### 九、TVC 多宫格专用写法

TVC 广告的多宫格分镜在通用写法基础上，需要额外处理**产品世界与品牌世界的交织**、**End Frame 的收束**以及**跨网格产品一致性**。

---

#### 9.1 产品世界 Grid 写法

**定位**：低密度（视觉驱动），每格以 `[景别·视角]：` 精确开头。

**写法要点**：
- 产品角度按逻辑编排：从整体到局部，从外观到内部，从静态到功能态
- 光影系统全局统一，仅在色温/强度上做微变
- 背景极度克制：纯色渐变或纯黑
- 材质关键词保持一致

**完整示例**（运动相机·产品世界 9 宫格）：

```
生成一张包含9个分镜的组合图，按3x3网格排列。
以图1的运动相机产品作为主体，纯黑渐变背景，Low-key 影棚布光，电影级产品摄影质感。

1. 全景·3/4低角度仰视：运动相机以经典3/4角度悬浮于画面中央，左侧45°柔光箱照亮机身正面，
右侧轮廓光勾勒出铝合金机身边缘的锐利光边，镜头玻璃表面反射出一道冷白高光。
2. 中景·正侧面平视：运动相机纯侧面视图，展示机身厚度和侧面按键布局，
按键表面的磨砂纹理在侧光下清晰可辨，机身腰线的倒角处形成一道细长高光带。
3. 特写·正面微距俯拍：极致微距聚焦镜头表面，多层镀膜玻璃在侧光下呈现紫蓝色光学干涉色彩，
镜头边缘的金属环反射出环形高光，景深极浅仅有毫米级。
4. 中景·正面平视：相机屏幕点亮，显示POV极限运动界面——中央是取景画面，
左上角防水图标发出蓝色微光，底部录制时长数字可见，屏幕光芒溢出照亮机身正面。
5. 全景·3/4俯视：相机组件悬浮拆解状态，外壳向上分离，镜头模组向前旋转展开，
防水密封圈悬浮于中层，主板与传感器在底部发出淡绿微光，组件间蓝色能量线连接。
6. 中景·3/4正面平视：产品包装盒微侧20°摆放于画面左侧，哑光黑色盒面印有银色品牌标识，
右侧相机本体以Hero Shot角度展示，盒盖微掀露出深灰绒面内衬。
7. 特写·背面微距侧光：相机背面散热格栅的极致微距，交叉编织的碳纤维纹理清晰可辨，
每一束纤维丝反射不同角度的光线，低角度侧光强化纹理的明暗起伏。
8. 中景·正面平视：相机处于夜间模式，机身正面指示灯亮起暗红色脉冲光，
屏幕低亮度显示夜视界面，整体环境极暗，仅产品自发光照亮局部。
9. 全景·正面平视：相机以稳定姿态静置于画面左下方三分之一处，柔和侧光照亮产品，
右上方留出画面40%的干净黑色空间，用于后期叠加Logo与Slogan。

保持整体风格统一。光影系统：Low-key 暗调棚光贯穿全部面板。
视觉母题：铝合金拉丝纹理的高光反射在不同面板中反复出现。
```

---

#### 9.2 品牌世界 Grid 写法

**定位**：低密度（TVC 默认）或中密度，角色在品牌世界场景中使用产品。

**产品可见硬规则**（不可违反）：
- **产品在每格中必须可见**——品牌世界不等于"没有产品的风景片"，TVC 的品牌世界是"产品在其中生活的世界"
- 产品占画面 10%-25%，自然融入场景但必须可辨识
- 产品在画面中的位置必须明确描述（`胸前固定的相机`、`左手腕上的相机`、`桌面上的香水瓶`）
- 产品屏幕/指示灯的发光颜色要写，增强辨识度

**写法要点**：
- 低密度时：每格以 `[景别·视角]：` 精确开头，精确指定场景、产品状态和光影
- 中密度时：每格以 **场景环境 + 人物动作 + 产品状态** 三要素展开

**完整示例**（运动相机·品牌世界 9 宫格）：

```
生成一张包含9个分镜的组合图，按3x3网格排列。
真人实拍，电影级摄影，自然光照，16:9横屏。

叙事线：一台运动相机跟随极限运动员征服九种极端环境——
从天空到深海、从雪山到沙漠，记录每一个不可能的瞬间。

1. 万米高空，跳伞者纵身跃出机舱的冻结瞬间，身体呈大字展开，
胸前固定的运动相机清晰可见，镜头朝下对准大地，录制指示灯亮起红色微光。
脚下是白云与蓝色地平线。
2. 深海峡谷，潜水员沿珊瑚峭壁垂直下潜，蛙鞋踢出的气泡向上翻涌，
左手腕上的运动相机屏幕在蓝色水下光线中发出绿色微光，显示深度数据。
阳光从水面折射成波纹光斑。
3. 阿尔卑斯雪场，滑雪运动员高速转弯激起弧形雪墙，身体极度压低倾斜，
头盔顶部固定的运动相机捕捉POV视角，雪粒在逆光中闪烁如碎钻。
4. 垂直岩壁，攀岩者单手抓握岩点的特写瞬间，指关节发白，
手腕上的运动相机贴近岩面，镜头沾有细微的粉笔灰和汗珠，背景是万丈深渊的虚化。
5. 沙漠戈壁，越野摩托车飞跃沙丘的顶点瞬间，车手与车辆完全腾空，
沙尘从轮下喷射形成金色烟尾，车把上固定的运动相机被夕阳照亮，
铝合金机身反射橙金色光芒。
6. 激流峡谷，皮划艇运动员穿越白水急流，水花猛烈飞溅在镜头前方，
船头固定的运动相机被水珠覆盖，水珠透过阳光折射出微棱镜效果。
7. 城市夜景，跑酷运动员在楼顶边缘起跳飞跃的瞬间，
脚下是霓虹闪烁的城市天际线，胸前相机的屏幕光与城市灯光交相辉映。
8. 暴风雪山脊，登山者在白茫茫的暴风中艰难前行，冰晶打在面罩上，
手套中握住的运动相机仍在录制，指示灯在风雪中顽强闪烁红光。
9. 日出山巅，运动员站在峰顶回望来路，金色晨光从身后涌出，
手中举起运动相机对准日出方向，屏幕反射出整片金色天际。

保持整体风格统一。视觉母题：产品的红色录制指示灯在每个极端环境中顽强亮起。
色调弧线：从第1格的冷蓝高空逐渐过渡至第9格的暖金日出。
```

---

#### 9.3 交叉 Grid 写法

**定位**：同一张 Grid 中混合"品牌世界"与"产品世界"面板，模拟 TVC 交叉剪辑节奏。

**写法要点**：
- 奇数格（1/3/5/7）为品牌世界场景——高/中密度，角色使用产品
- 偶数格（2/4/6/8）为产品世界特写——低密度，精确摄影指令
- 第 9 格固定为 End Frame
- 相邻格之间设计视觉衔接（形状匹配/色彩匹配/纹理匹配）

**完整示例**（运动相机·交叉 9 宫格）：

```
生成一张包含9个分镜的组合图，按3x3网格排列。
电影级摄影，16:9横屏。
品牌世界面板为真人实拍自然光，产品世界面板为Low-key影棚光纯黑背景。

(图1)运动相机产品参考图。
品牌世界与产品世界交叉编排，奇数格为使用场景，偶数格为产品特写，第9格为收束定格。

1. 雪场逆光，滑雪者高速弧线转弯的冻结瞬间，
雪雾如白色浪墙弧形翻涌，头盔上的运动相机在阳光中闪烁。
2. 近景·3/4侧面：纯黑背景，图1运动相机的机身弧形倒角特写，
侧光勾勒出与雪墙弧线相似的流畅曲面，铝合金拉丝纹理反射冷白高光。
3. 海面上空，潜水员后空翻入水的瞬间，身体蜷曲，
周围飞溅出圆形水花皇冠，腰间固定的运动相机即将没入水中。
4. 特写·正俯拍：纯黑背景，运动相机镜头正面俯拍，
圆形镜头轮廓居中，多层镀膜反射出与海水相似的蓝紫色光学色彩，水珠残留在镜面边缘。
5. 沙漠黄昏，越野摩托飞跃沙丘的剪影，
背后是燃烧般的橙金色日落，车把上固定的运动相机被夕阳镀上金边。
6. 中景·侧面平视：纯黑背景，暖金色侧光从左侧扫过产品铝合金机身，
表面呈现与沙漠夕阳相同的琥珀金色调，材质纹理的高光带缓慢流动。
7. 垂直岩壁，攀岩者指尖抓握粗糙岩石的极限特写，指关节发白，
手腕上的运动相机紧贴岩面，背景是深渊虚化。
8. 特写·正面微距：纯黑背景，产品侧面防滑橡胶握持区的极致微距，
菱形压纹的凹凸纹理与岩石表面有相似的粗粝质感，
低角度侧光刻画每一个凸起的高光与沟槽的阴影。
9. 全景·正面平视：纯黑渐变背景，运动相机以最佳角度静置于画面左下三分之一处，
柔和侧光照亮产品，右上方大面积留白用于Logo与Slogan叠加。

保持整体风格统一。奇数格保持真人实拍自然光质感，偶数格保持Low-key影棚产品摄影质感。
两种世界通过形状/色彩/纹理的视觉衔接串联。
```

---

#### 9.4 End Frame 格

**总原则**：布局依品牌规范而定——**产品居中**（Hero Pose）与**产品偏置留白**均为有效方案。

**核心规则**：
1. 构图必须为后期文字预留空间（约 30%-40% 干净区）
2. 产品状态必须是"最终态"：屏幕亮起、外观完整、姿态稳定沉静
3. 光影简洁高级，不写 Logo/Slogan 文字内容，仅描述留白区域

**End Frame 格的提示词模板**：

```
[格号]. [景别]·[视角]：[背景描述]，[产品名称]以[角度/姿态]静置于画面[位置]，
[产品最终状态描述]。[简洁光影]。
[留白区域位置]留出画面[百分比]的干净空间，背景渐变均匀无杂物。
```

**示例**：

```
9. 全景·正面平视：深空灰渐变背景，运动相机以3/4低角度静置于画面左下方三分之一处，
屏幕显示品牌主色蓝色界面，所有指示灯微微亮起。柔和左侧侧光照亮产品，
在右侧形成自然过渡的阴影。产品右上方留出画面40%的干净空间，背景渐变均匀无杂物。
```

---

#### 9.5 TVC 多张网格规划示例

以下示例展示一支 30 秒 TVC（运动相机）如何用 2 张网格覆盖完整内容。

**项目信息**：

| 维度 | 内容 |
|------|------|
| 产品 | 专业运动相机 |
| 时长 | 30 秒 |
| 叙事模型 | 品牌世界穿梭（C 模型） |

**网格规划总表**：

| 网格 | 时段 | 类型 | 剧情密度 | 叙事功能 |
|------|------|------|---------|---------|
| G1 | 0-15s | 品牌世界 Grid | 低密度 | 极限运动场景蒙太奇 |
| G2 | 15-30s | 产品世界 Grid + End Frame | 低密度 | 产品多角度影棚展示 + 收束 |

**跨网格一致性检查清单**：

- [ ] **全局风格**：G1 和 G2 使用相同的画质锚定
- [ ] **参考图**：两张网格引用同一张产品参考图（`图1`）
- [ ] **衔接过渡**：G1 第 9 格色调 → G2 第 1 格色调，色温连续
- [ ] **产品描述**：两张网格中产品的材质关键词完全一致
- [ ] **产品颜色**：所有格中产品配色描述一致

---

#### 9.6 产品一致性维护

TVC 多宫格中产品跨网格出现，必须维护外观一致性。

##### 规则一：锁定产品描述模板

```
产品标准描述模板：
[产品名]，[核心材质A] + [核心材质B] 机身，
[颜色/配色方案]，[关键设计特征1]，[关键设计特征2]，
[尺寸/比例特征]。
```

示例：
```
产品标准描述：
XX Pro 运动相机，铝合金拉丝机身 + 碳纤维后壳，
深空灰配色，正面超广角镜头模组（圆形，多层镀膜），
侧面三颗红色功能按键，机身方正硬朗，掌心大小。
```

##### 规则二：统一光影关键词

同一产品在不同 Grid 中的产品世界面板应使用相同的光影词汇集（主光方向、轮廓光方向、材质高光描述词、色温基调全局一致）。

##### 规则三：角度描述标准化

跨网格的同一角度必须使用完全相同的角度描述文本，不可在 G1 中写 `微俯` 而在 G2 中写 `斜上方30°`。

##### 规则四：品牌世界中的产品最低描述要求

即使产品只占画面 10%，仍需包含四个信息点：产品安装位置、材质关键词、功能状态提示、产品配色。

##### 规则五：产品参考图全局引用

所有网格必须引用同一张产品资产图，不可使用不同的产品参考图。

##### 规则六：出镜者服装一致性

当人物在品牌世界面板中出镜（无论全身/下半身/背影/剪影），所有网格中该人物的服装描述必须完全一致。前期筹备阶段建立的**出镜者标准描述**是唯一权威——每格涉及人物时必须复用，不可在 G1 中写"黑色短裤"而在 G2 中写"黑色长裤"。服装的款式、颜色、材质三要素跨格不可变化，仅姿态和动作可变。

##### 规则七：禁止比喻修辞

多宫格提示词中**禁止使用比喻、拟人、类比等修辞手法**。AI 图片模型是字面理解的——"如雕塑"会生成石膏材质的人体，"如花园"会生成花卉植物，"如丝绸"会改变材质渲染。

| 错误写法 | 问题 | 正确写法 |
|---------|------|---------|
| 路人定格如**雕塑** | 模型可能生成石膏/大理石质感人体 | 路人保持行走姿态静止不动，表情凝固，衣角悬停在运动状态 |
| 在纸张之间穿行如同**采摘花朵** | 模型可能生成花卉元素 | 从空中逐张摘取悬浮的纸张 |
| 液滴如**琥珀珠** | 模型可能将液滴渲染为琥珀色固体 | 液滴在光照下呈半透明深色，表面反射高光 |

原则：**描述你要什么，不要描述它像什么。**

##### 规则八：多宫格只写状态，不写过程

多宫格是静态关键帧，每格只能描述**一个时间点的画面状态**，不能描述动态过程。动词必须是静态的（悬浮、静止、停驻、凝固）而非过程性的（飞出、涌出、溅起、坠落）。过程性动作留给视频提示词。

| 错误写法（过程态） | 问题 | 正确写法（结果态） |
|----------------|------|----------------|
| 咖啡杯**脱手飞出**，液体**开始溢出**杯口 | "飞出""溢出"是动态过程，静态帧无法表达 | 咖啡杯悬停在半空，液体凝固为弧形，杯口朝下 |
| 红酒**开始涌出**杯口，形成**即将倾泻**的弧线 | "涌出""倾泻"是进行中的动作 | 红酒液柱悬浮在倾斜酒杯与桌面之间，液面反射烛光 |
| 纸张在空中**翻飞** | "翻飞"是动态 | 数十张纸张以各种角度悬停在空中 |

这条规则与"动态特效的分工"互补：特效分工解决"写什么"，本规则解决"怎么写"。

---

### Part 2: 视频提示词语法

---

### 一、视频提示词 vs 静态关键帧提示词

核心转换思路：把"是什么"变成"怎么变"。

| 维度 | 静态关键帧 | 视频提示词 |
|------|-----------|-----------|
| 时间 | 无 | 有时间码，精确到秒 |
| 主体 | 冻结状态/姿态 | 运动中的过程（动作+变化） |
| 镜头 | 固定景别+视角 | 运镜轨迹（推/拉/环绕/跟随） |
| 画面衔接 | 无 | 转场指示（硬切/溶解/匹配剪辑） |
| 光影 | 固定光源方向 | 光影随时间变化（渐变/闪烁/昼夜） |

---

### 二、视频提示词的写作逻辑与输出格式

视频提示词遵循三部分逻辑，**输出时不使用"风格信封""连续性指令"等术语**，使用自然语言。

#### 第一部分：风格与约束声明

**必须覆盖**：视觉风格、色彩基调、约束条件、**"无背景音乐"（必写）**、**产品@产品多视图图片**。

> **视频模型双图输入**：视频模型接收两张图片——多宫格分镜图（首帧）+ 产品多视图（产品锚定）。在风格声明末尾用 `产品@产品多视图图片 的广告` 引用产品多视图，让模型理解产品外观。`(图1)(图2)` 参考图映射是多宫格提示词（图片生成阶段）的语法，不用于视频提示词。

> **音频铁律**：视频模型默认生成 BGM，不写就会有。多段拼接时各段 BGM 在接缝处断裂。BGM 在后期作为单独音轨统一铺设。角色对白在镜头描述中用引号标注。

> **不写后期指令**：视频提示词只描述视频模型能生成的画面内容。以下属于后期工作，不写入视频提示词：Logo/品牌标识叠加、Slogan/文字渐显、调色指令、音效设计、字幕排版。End Frame 在视频提示词中只需描述"产品居中定格、画面干净留白"等纯视觉状态，Logo 和 Slogan 的空间预留属于多宫格图片提示词（End Frame 格）的职责。

**输出示例**：
> 风格：暗黑童话告别场景 / 红黑高对比森林色调 / 定格动画质感 / 强烈光源对冲构图（门内白光 vs 门外赤红森林）/ 细腻表情特写 / 情绪克制的离别氛围 / 无字幕 / 无背景音乐 产品@产品多视图图片 的广告

#### 第二部分：镜头脚本

两种格式，根据目标视频模型选择：

##### 格式 A：精简镜头表

```
第1个镜头[0-2秒][中景] 巨大的树门嵌在粗壮树干中，红色森林环绕。小女孩与小老鼠并肩站在门前，女孩微微低头，小老鼠仰头望她。
第2个镜头[2-4秒][特写] 小老鼠举起小爪子挥手，"吱吱吱"轻声告别，女孩与它对视，神情温柔又不舍。
第3个镜头[4-7秒][中景] 女孩缓缓转身走向树门，伸手推门。门缝透出强烈白光，将她轮廓照成剪影。她走出两步后停住，回头看向小老鼠。
...
```

##### 格式 B：详细分段描述

```
【0-3s：山野溯源，青提滚落】
镜头：镜头由远景缓慢向前推进，随后切入微距跟随镜头。
画面：画面基调为黑白极简的自然山野，一个背着竹筐的插画线条少女手持铁锹走入画面。
      随着她走上岩石，背后的竹筐倾斜，几颗线条勾勒的果实滚落而出。

【4-7s：粉色倾注，果香苏醒】
镜头：镜头从低角度仰拍，随后跟随着水流的轨迹自上而下快速平移。
画面：巨大的写实透明杯身伫立在山间岩石上，杯底已经铺满了鲜活青提。
      突然，一股带有真实光泽的粉色桃桃果汁如瀑布般从上方倾注而下...
```

#### 第三部分：衔接与贯穿（自然融入）

两种处理方式：

1. **融入各镜描述**：在每镜描述中自然提及转场和贯穿元素
   > 第1个镜头[0-2.5秒][远景·逆光]（对应P1）**溶解承接上段末尾。** 固定机位，三头奶牛的剪影在金色晨光中缓缓走向右侧...

2. **末尾追加备注**（仅在信息量大时）：
   > 全片以硬切为主，建立镜头间用溶解。金色轮廓光持续勾勒每镜中奶牛边缘。P9暖金牧场远景自然过渡至下一段。

---

### 三、逐镜描述公式

#### 七要素公式

```
[时间码][景别+视角] + [镜头运动] + [主体动作] + [环境/光效变化] + [角色对白(如有)] + [转场指示]
```

#### 写作要点

- **动词为王**：视频提示词的核心是动词——扫过、升腾、旋转、推进、弥漫、消散
- **渐变优于突变**：用"渐变""缓慢""逐渐"描述变化过程
- **具体优于抽象**：`旋转30°` 优于 `缓慢旋转`
- **因果链**：镜头运动引发主体变化，主体变化影响光影反应
  - 例：`产品向镜头推进` → `烟雾随推进速度弥漫扩散` → `暖光渐变为深金调`

---

### 四、15 秒标准节奏编排

#### 四段节奏模型

| 时段 | 秒数 | 功能 | 节奏 |
|------|------|------|------|
| **定场** | 0-3s | 建立场景/氛围 | 慢 |
| **发展** | 3-7s | 展开叙事/展示 | 中速 |
| **高潮** | 7-12s | 情绪/动作顶峰 | 快 |
| **收束** | 12-15s | 留白/余韵/CTA | 减速 |

#### 非标准节奏

| 变体 | 结构 | 适用 |
|------|------|------|
| **慢热型** | 5s定场 + 5s发展 + 3s高潮 + 2s收束 | 氛围短片、艺术片 |
| **冲击型** | 1s定场 + 4s发展 + 8s高潮 + 2s收束 | 动作片、游戏CG |
| **循环型** | 建立→高潮→建立→高潮→收束 | 音乐MV、节奏驱动 |
| **倒叙型** | 高潮→倒叙发展→回到高潮→收束 | 悬疑、反转叙事 |

---

### 五、与多宫格的引用规范

视频提示词可以直接引用多宫格图中的面板位置：
- 按面板编号：`（对应分镜P1）`、`（对应P5-P7）`
- 按行列位置：`（对应第2行第3列）`

引用示例：

```
第1个镜头[0-2秒][全景·俯拍]（对应P1）产品静置于画面中央，暖金侧光缓慢扫过...
第2个镜头[2-4秒][近景·侧仰]（对应P2）产品缓慢旋转，棱面反射变化的光影...
```

多面板对应单镜头：
```
第3个镜头[4-8秒][中景·平视]（P3→P4过渡）产品向镜头推进，场景从P3的状态渐变为P4...
```

---

### 六、多段视频的跨段连续性

#### 跨段一致性要素

| 要素 | 要求 |
|------|------|
| **风格声明** | 所有段共享相同的风格与约束声明 |
| **无背景音乐** | 每段都必须写 |
| **角色外观** | 通过引用同一资产图保持一致 |
| **色调连续** | 前段末尾色调 ≈ 后段开头色调 |
| **运动连续** | 角色运动方向在段间不跳变 |

#### 段间独立性

每段视频提示词单独喂入视频模型，模型不知道其他段的内容。每段的 Phase 编号从 Phase 1 开始、秒数从 0s 开始，不继承上一段的编号或时间轴。不要在本段描述中引用其他段已发生的事件（如"回归之前的阳台""一切如初""与上一段相比多了柔雾"）。跨段一致性通过重复相同的风格声明和产品描述实现，而非文本引用。

#### 段间衔接类型

衔接类型描述的是**剪辑层面**的视觉过渡策略（用于指导后期拼接），不是让视频提示词在文本中引用其他段：

| 衔接类型 | 适用 |
|---------|------|
| **动作承接** | 连续叙事 |
| **氛围延续** | 情绪短片 |
| **场景跳转**（渐暗/渐亮） | 多场景叙事 |
| **呼应回扣** | 循环/升华叙事 |

---

### Part 3: 产品电影化拆解

---

#### 一、视频提示词结构

TVC 产品视频采用多阶段\结构。

##### 标准 Phase 结构

```
 [编号]（[起始秒]s-[结束秒]s）：[阶段名称]
├─ 镜头运动：[运镜方式 + 速度 + 方向]
├─ 产品状态：[当前产品形态/动态变化]
├─ 功能揭示：[该阶段展示的核心卖点]
├─ 光影设计：[光源类型 + 方向 + 变化]
├─ 材质焦点：[当前阶段重点展示的材质/质感]
└─ 视觉特效：[粒子/能量流/数字叠加等]
```

#####  节奏编排原则

| 阶段类型 | 典型时长 | 节奏 | 作用 |
|---------|---------|------|------|
| 悬念开场 | 1-2s | 极慢 / 静止 | 制造期待，暗示产品轮廓 |
| 拆解/展开 | 2-3s | 慢→加速 | 展示内部结构，传递技术感 |
| 功能激活 | 1-2s | 爆发 | 屏幕点亮、数字跳动、传感器发光 |
| 爆发旋转 | 1-2s | 快速 | 360°全方位展示产品外观 |
| 微距潜入 | 1-2s | 超慢 | 材质质感收尾，建立高级感 |
| 品牌定格 | 1-1.5s | 静止 | Logo + Slogan + 产品最终姿态 |

##### 格式要点

- **风格声明**末尾固定"无背景音乐"
- **Phase 编号**从 1 开始递增，括号内标注精确秒数
- **秒数连续**：前一 Phase 结束秒 = 后一 Phase 开始秒，无间隙无重叠

---

#### 二、组件拆解/装配动画编排

##### 1. 悬浮拆解（Floating Disassembly）

```
产品在画面中央悬浮，各组件开始缓慢分离——外壳向左上方平移漂浮，
镜头模组向右侧旋转分离，主板向下方悬浮展开，电池组向后方滑出。
所有部件之间有微弱的蓝色能量光线连接，暗示内部协同关系。
背景纯黑，组件表面被精准的侧光勾勒出轮廓。
```

##### 2. 爆炸视图（Exploded View）

```
产品瞬间爆炸式展开，所有组件沿中心轴向外弹射至各自位置——
顶部：镜头组件悬浮旋转，玻璃镜片折射出彩虹光斑；
中部：主板与芯片组水平展开，电路纹理发出微弱的绿色脉冲光；
底部：电池模块与散热系统垂直下沉，金属散热片反射锐利的银色高光。
整体呈对称爆炸视图，工业设计感极强。
```

##### 3. 精密装配回弹（Precision Assembly Snap-back）

```
各组件开始高速回归——散热模块率先归位，发出金属撞击的微震；
主板精准滑入卡槽，电路瞬间亮起脉冲光；镜头模组旋转拧入，
玻璃表面闪过一道高光；外壳最后扣合，接缝处一道白光闪过，
产品恢复完整形态，表面反光如新。
```

**节奏要点**：拆解用 2-3 秒（慢），装配回弹用 0.8-1.2 秒（快），速度对比产生冲击力。

---

#### 三、功能可视化设计

##### 1. 屏幕点亮（Screen Activation）

```
产品屏幕从全黑状态开始，一个像素点从中心亮起，
光芒以波纹状向四周扩散，屏幕内容逐渐显现——
界面元素依次浮现，图标从下方滑入，
屏幕光芒照亮产品正面和周围环境，
在桌面上投射出彩色的屏幕倒影。
```

##### 2. 数字跳动（Digits Ticking）

```
画面聚焦产品屏幕，数字开始高速跳动——
电池图标旁的数字从 00:00:00 开始极速攀升，
数字翻滚如老式翻页时钟，每一位数字带有微弱的运动模糊，
最终定格在 04:00:00，数字发出脉冲式的金色光芒，
暗示超长续航。整个过程在 1.5 秒内完成。
```

##### 3. 传感器发光（Sensor Glow）

```
产品表面的传感器区域开始发出微弱的光芒——
红外传感器亮起暗红色脉冲，激光雷达发射绿色扫描线，
多个传感器依次激活，光点如呼吸般明灭，
暗示产品在感知周围环境。光线在产品金属表面形成彩色反射。
```

##### 4. 能量流动（Energy Flow）

```
一道蓝色的能量光线从充电接口注入，
沿产品内部电路板的纹理路径高速流动，
光线分叉、汇聚、再分叉，照亮沿途的芯片和元器件，
最终汇聚至电池模块，电池图标从红色渐变为满格绿色，
发出一圈扩散的能量脉冲波。
```

---

#### 四、材质微距系统

##### 材质微距速查表

| 材质类型 | 微距描述关键词 | 光影配合 |
|---------|-------------|---------|
| 金属拉丝 | 密集的平行拉丝纹理，每道划痕反射不同角度光线 | 侧光 45°慢速扫过 |
| 玻璃折射 | 光线穿透后形成彩虹色散，边缘微棱镜效果 | 逆光/穿透光 |
| 碳纤维编织 | 交叉编织形成规律菱形图案 | 低角度侧光 |
| 液态流体 | 粘稠液体缓慢流动，液面反射如镜面 | 顶光+环境反射 |
| 陶瓷釉面 | 如玉石般温润，微气泡在釉层下若隐若现 | 柔光散射 |
| 皮革纹理 | 毛孔、褶皱和使用痕迹，边缘手工缝线 | 暖色侧光 |
| 阳极氧化铝 | 细腻磨砂质感，不同角度呈现微妙色彩变化 | 渐变光扫过 |

##### 材质微距运镜

```
镜头贴近产品表面至极致微距（模拟微距镜头 1:1 放大倍率），
沿材质纹理方向缓慢滑行，景深极浅仅有毫米级焦平面，
焦点随滑行移动，依次揭示材质的不同层次细节——
从拉丝纹理到倒角高光到接缝精度，
最后镜头缓慢拉出，材质细节渐渐汇聚成产品完整轮廓。
```

---

#### 五、六阶段节奏模型

纯产品展示型 TVC 的标准节奏：

```
超慢揭示 → 悬浮拆解 → 精密合拢 → 功能激活 → 微距潜入 → 品牌定格
```

| 阶段 | 节奏 | 运镜 | 产品状态 |
|------|------|------|---------|
| **超慢揭示** | 极慢 / 静止 | 固定→微推 | 全黑中轮廓光逐步勾勒 |
| **悬浮拆解** | 慢→渐快 | 弧形环绕 | 组件分离，内部暴露 |
| **精密合拢** | 爆发 | 多角度快切 | 组件高速回弹归位 |
| **功能激活** | 中速脉冲 | 推近至特写 | 屏幕点亮/传感器发光 |
| **微距潜入** | 超慢 | 微距滑行 | 材质微观细节放大 |
| **品牌定格** | 静止 | 弹射拉远→定格 | 产品完美形态+Logo |

##### 阶段间转场编排

- 超慢揭示 → 悬浮拆解：轮廓光照亮全貌后，组件"呼吸式"微振→分离
- 悬浮拆解 → 精密合拢：组件悬停 0.3s 静默→突然加速回弹
- 精密合拢 → 功能激活：合拢瞬间白光闪线→屏幕从该光点扩散亮起
- 功能激活 → 微距潜入：屏幕像素→镜头穿入→进入材质微观世界
- 微距潜入 → 品牌定格：材质纹理逐渐模糊→弹射拉远至全景

---

#### 六、完整 Multi-Phase 产品视频示例

##### 示例 1：运动相机（10秒，5 Phase）

**产品**：高端运动相机，主打防水、超广角、超强防抖

```
Phase 1（0s-2s）：暗调悬念揭示
镜头运动：静止→微推
产品状态：纯黑背景中，一道锐利的轮廓光从产品边缘亮起，缓慢勾勒出运动相机的方正轮廓。
光影设计：Rim Light 从后方 270°环绕勾勒，正面几乎全黑，只见轮廓线。
材质焦点：轮廓光扫过时，隐约可见铝合金机身的拉丝纹理。

Phase 2（2s-4s）：悬浮拆解
镜头运动：弧形环绕，从正面到 3/4 俯视
产品状态：相机组件开始悬浮分离——防水外壳向上漂浮，露出内部精密结构；
超广角镜头模组向前旋转分离，多层镀膜玻璃折射出彩虹光斑；
防抖陀螺仪模块悬浮旋转展示。各组件间蓝色能量线连接。
光影设计：侧光逐渐升起，精准照亮每个分离的组件。
功能揭示：超广角镜头的多层镀膜结构、机械防抖的陀螺仪模块。

Phase 3（4s-5.5s）：功能激活
镜头运动：快速推入至屏幕特写
产品状态：组件高速回弹装配归位（0.5s），外壳扣合发出白光闪线；
后屏瞬间点亮，界面显示 POV 极限运动画面（跳伞第一视角），
屏幕左上角防水图标亮起蓝色光芒。
光影设计：屏幕光芒成为主光源，照亮产品正面和周围环境。
功能揭示：屏幕显示效果、防水性能暗示。

Phase 4（5.5s-7.5s）：爆发旋转
镜头运动：高速 360°环绕旋转
产品状态：相机在画面中央悬浮，高速旋转展示全部外观——
正面镜头、侧面按键、底部三脚架接口、顶部录制按钮。
旋转中每个面依次被追光照亮。
光影设计：追光旋转，高光始终锁定在旋转经过的关键特征上。
材质焦点：旋转中清晰可见铝合金拉丝纹理与橡胶防滑握持区的对比。

Phase 5（7.5s-10s）：微距潜入 + 品牌定格
镜头运动：极速推入至镜头玻璃表面→穿越镜头组→弹射拉远至全景
产品状态：镜头潜入相机镜头内部，穿越多层镀膜玻璃（光线在镜片间折射、色散），
穿过 CMOS 传感器表面（像素阵列微距），弹射拉远至全景——
产品悬浮于画面中央，下方浮现品牌 Logo 与 Slogan。
光影设计：穿越时内部光线折射；弹出后回归 Low-key 棚光定格。
材质焦点：镜片镀膜的光学色散、CMOS 传感器的微观像素阵列。
```

##### 示例 2：奢华精华液（10秒，5 Phase）

**产品**：高端护肤精华液，主打黄金成分、奢华质感、抗衰修护

```
Phase 1（0s-2s）：奢华帷幕揭示
镜头运动：缓慢下摇
产品状态：画面顶部，一滴金色精华液在全黑背景中缓慢坠落，
液滴表面反射出整个环境的倒影，液体粘稠而饱满，
带有蜂蜜般的拉丝质感。液滴下坠的轨迹留下一道金色光痕。
光影设计：顶部单束聚光灯追踪液滴，液滴如一颗微型金色星球。
材质焦点：精华液的粘稠度、表面张力、光泽折射。

Phase 2（2s-4s）：瓶身现身
镜头运动：弧形环绕，从侧面到 3/4 正面
产品状态：金色液滴落入画面下方的精华瓶口，涟漪荡开；
镜头下摇揭示整个瓶身——磨砂玻璃瓶体，内部金色液体微微流动，
金属瓶盖反射出锐利的高光，瓶身浮雕品牌纹样。
光影设计：侧光从左侧 45°照射，玻璃瓶体产生通透的光影层次，
液体内部折射出温暖的琥珀色光芒。
材质焦点：磨砂玻璃的半透明质感、金属瓶盖的镜面反射。

Phase 3（4s-6s）：液态流动微距
镜头运动：极致微距推入瓶身玻璃表面
产品状态：镜头贴近瓶身，穿透磨砂玻璃层，进入瓶内液体世界——
金色精华液内部有微小的金箔颗粒悬浮流动，
液体形成缓慢的对流漩涡，金箔在光线中闪烁。
光影设计：背透光穿过液体，金箔颗粒如漂浮的星辰。
功能揭示：黄金微粒活性成分的可视化。

Phase 4（6s-8s）：肌肤意象
镜头运动：匀速侧移 + 浅焦过渡
产品状态：画面过渡至抽象的肌肤微距意象——光滑的肌肤纹理表面，
一滴精华液落在肌肤上，迅速渗透扩散，扩散轨迹发出微弱金色光芒，
肌肤纹理随扩散变得更加细腻光滑（视觉隐喻：抗衰修护）。
光影设计：柔和的暖色散射光，皮肤表面的 SSS 次表面散射效果。
功能揭示：渗透吸收、肌肤修护效果的视觉化。

Phase 5（8s-10s）：品牌定格
镜头运动：缓慢拉远至中景定格
产品状态：产品瓶身置于画面中央偏右，左侧一枝干花/金色叶片做前景点缀，
瓶身被温暖的侧光照亮，背景为深色渐变（深棕→黑）。
品牌 Logo 在画面左侧优雅浮现，下方 Slogan 以细衬线字体排列。
光影设计：经典美妆广告布光——柔和主光+侧面轮廓光+底部反射光。
```

##### 示例 3：先锋银饰手链（10秒，5 Phase）

**产品**：手工锻造银色手链，主打独立态度、工艺质感、先锋设计
**出镜策略**：有人物——女性手腕/手部特写（不露脸），穿极简黑色服装，皮肤干净

```
Phase 1（0s-2s）：工艺溯源——锻造
镜头运动：微距静止→缓推
产品状态：纯黑背景，一块粗粝银块在画面中央。侧光缓慢升起，
勾勒出银块表面的锤打纹理。银块边缘开始泛出微弱的炽热红光——
暗示刚从锻炉中取出。表面可见手工锻打留下的不规则凹痕，
每一道痕迹都是工匠的签名。
光影设计：单侧硬光，强调银块的粗粝质感。微弱红光从底部向上渗透。
材质焦点：原银的颗粒感、锤打凹痕的不规则纹理。

Phase 2（2s-4s）：蜕变——从原银到成品
镜头运动：快推→溶解过渡
产品状态：镜头快速推向银块表面微距——银色颗粒充满画面；
溶解过渡至成品手链的微距特写：同样的银色，但表面已被打磨为
哑光拉丝质感，链节之间的铰接结构在侧光下投射出精密阴影。
光影设计：过渡前后光源方向一致（侧光），实现材质变化但光影连续。
材质焦点：哑光拉丝银面、链节铰接处的精密间隙。

Phase 3（4s-6s）：佩戴——手腕登场
镜头运动：缓拉远→微弧移
产品状态：镜头从手链微距缓慢拉远，银链逐渐完整显现——
它环绕在一只女性手腕上。手腕缓慢翻转，银链随手势流动，
链节之间产生微妙的金属碰撞光斑。手腕皮肤干净、指甲无色，
黑色衣袖边缘刚好露出手腕。
光影设计：侧光从手腕一侧打入，银链反射形成流动光带，皮肤呈现温暖的象牙色调。
材质焦点：银与肌肤的触感对比——冷硬金属与温暖皮肤。

Phase 4（6s-8s）：姿态——先锋态度
镜头运动：跟拍手部动态
产品状态：手从画面下方缓慢抬起，手指微张呈放松姿态——
银链在手腕上随重力微垂，一侧紧贴皮肤，另一侧自然悬空。
手掌微微握拳后松开，银链在手腕上产生轻微位移和光影变化。
背景从纯黑过渡为模糊的混凝土灰色——暗示建筑美学空间。
光影设计：侧光主调不变，背景出现微弱的环境散射光。
动态焦点：银链随手势的自然垂坠和光影流转。

Phase 5（8s-10s）：定格
镜头运动：缓推回微距→静止
产品状态：手腕静止于画面中央偏左，银链自然垂落于手腕最细处。
镜头缓推至银链特写——最后定格在一个链节的微距：
哑光拉丝表面、铰接处的精密间隙、侧光勾勒出的银色轮廓线。
画面右侧大面积留白，用于后期放置品牌标识。
光影设计：回归开场的单侧硬光，首尾呼应。画面干净、克制、留白充足。
```

---

### Part 4: 品牌世界镜头

---

#### 一、品牌世界↔产品世界切换技法

品牌世界（Brand World）是产品的使用场景；产品世界（Product World）是棚拍特写。两个世界在 TVC 中反复切换，切换的质量决定了广告的高级感。

##### 三种核心切换技法

###### 技法一：Match Cut 动势传递

**品牌世界 → 产品世界**：

```
[品牌世界] 滑雪者从雪坡飞出，身体在空中旋转——
旋转到 180°的瞬间无缝切换至——
[产品世界] 产品以相同的旋转角速度出现在纯黑背景中，
延续旋转动势完成 360°展示，在 3/4 侧面角度减速定格。
```

**产品世界 → 品牌世界**：

```
[产品世界] 产品屏幕点亮，光芒向画面四周扩散——
光芒充满整个画面的瞬间无缝切换至——
[品牌世界] 从白色过曝中渐显出广阔的雪山全景，
一辆越野车在雪地上疾驰，扬起的雪雾与屏幕光芒的白色无缝衔接。
```

**提示词模板**：
```
[前一世界的运动主体]在画面中做[具体运动]——
在[运动到达特定位置/角度/速度]的瞬间无缝切换至——
[后一世界]以相同的[运动方向/角速度/速度矢量]延续动势，
[后续画面的展开]。两个画面的[形状/运动轨迹/速度]完美衔接，镜头流畅不中断。
```

###### 技法二：尺度穿越（Scale Shift）

**宏观 → 微观**：

```
[品牌世界] 航拍俯瞰城市夜景，万千灯火闪烁——
镜头急速俯冲向城市中一个发光的点——
[产品世界] 穿透层层尺度后，发光的点变成产品屏幕上的一个像素，
镜头稳定在产品屏幕微距，界面细节清晰可见。
```

**微观 → 宏观**：

```
[产品世界] 镜头贴近产品表面微距，材质纹理充满画面——
镜头突然弹射后退，极速拉远——
[品牌世界] 产品纹理渐变为高空俯瞰的地面纹理（沙漠裂纹/农田几何），
揭示产品正身处广袤的自然风景之中。
```

###### 技法三：介质穿越（Medium Penetration）

**穿入产品 → 穿出到品牌世界**：

```
[产品世界] 镜头对准产品镜头组正面，开始缓慢推入——
穿过第一层镀膜玻璃（表面产生彩虹色散），
穿过第二层透镜（光线折射弯曲），
穿过 CMOS 传感器阵列（像素方阵的微观世界）——
[品牌世界] 穿出后画面是从该相机视角拍摄的壮丽风景，
暗示"产品眼中的世界"。
```

**品牌世界 → 穿入产品**：

```
[品牌世界] 精华液在手指尖缓慢滴落——
液滴落入瓶口的瞬间，镜头跟随液滴穿入瓶内——
[产品世界] 进入瓶内液体的微观世界，
金箔粒子在琥珀色液体中悬浮流动如星辰。
```

##### 切换频率与节奏控制

| 视频时长 | 建议切换次数 | 节奏策略 |
|---------|------------|---------|
| 10s | 1-2 次 | 品牌世界开场→产品世界收束 |
| 15s | 2-3 次 | 品牌→产品→品牌→定格 |
| 30s | 4-6 次 | 自由穿梭，前半段品牌主导，后半段产品主导 |

**切换节奏原则**：
- 每次切换后至少停留 2-3s 再切回
- 最后一次切换必须是**切入产品世界**——TVC 最终落点永远是产品本身

---

### Part 5: TVC 时长模板

---

#### 一、TVC 30s 双段节奏模板

##### 模板 A：品牌世界穿梭型 30s

```
═══ 第一段（0-15s）：品牌世界主导，建立情绪 ═══

Phase 1 (0-3s): 品牌世界开场
  极限运动/生活场景的广角大全景，建立世界观和能量感。
  快节奏运镜（航拍/跟随/手持），主体在运动中。

Phase 2 (3-6s): 产品初现
  [Match Cut] 场景运动→产品旋转。
  产品以 3/4 角度缓慢环绕展示，轮廓光勾勒造型。
  第一次揭示产品全貌。

Phase 3 (6-10s): 品牌世界升级
  [Match Cut] 产品材质纹理→场景元素纹理。
  场景升级（更极限/更动态/更情绪化），
  产品在使用中自然出现（手持/穿戴/环境融合）。

Phase 4 (10-15s): 功能揭示 + 段间衔接
  [Match Cut] 场景动作→产品功能激活。
  产品功能可视化展示，屏幕点亮/传感器发光。
  末尾动作为下段预留衔接点（如旋转中/光芒扩散中不收束）。

═══ 第二段（15-30s）：产品主导，收束品牌 ═══

Phase 5 (15-19s): 承接 + 深度拆解
  承接上段末尾的动势。产品悬浮拆解，
  组件分离展示内部结构，传递技术深度。

Phase 6 (19-23s): 精密合拢 + 爆发旋转
  组件高速回弹归位→爆发式 360°旋转展示。
  速度从极快（合拢）到快（旋转）到渐慢。

Phase 7 (23-27s): 微距潜入
  镜头潜入产品表面微距——材质纹理、倒角精度、
  光线在表面的反射与折射。超慢运镜，品质收尾。

Phase 8 (27-30s): 品牌定格
  弹射拉远至全景，产品完美定格。
  Logo + Slogan 浮现。画面简洁高端。
```

##### 模板 B：纯产品电影型 30s

```
═══ 第一段（0-15s）：从暗到明，揭示全貌 ═══

Phase 1 (0-3s): 暗调悬念
  全黑，轮廓光逐步亮起，勾勒产品轮廓。
  极慢节奏，制造期待。

Phase 2 (3-7s): 光影觉醒
  主光缓慢升起，产品从黑暗中浮现。
  弧形环绕从侧面到 3/4 正面，全方位首次亮相。

Phase 3 (7-11s): 悬浮拆解
  组件分离展示，弧形环绕配合景深切换逐个聚焦。
  蓝色能量线连接各组件，暗示内部协同。

Phase 4 (11-15s): 精密合拢
  组件爆发式回弹归位，每个部件"咔嗒"到位。
  合拢瞬间白光闪过→预留给下段屏幕点亮。

═══ 第二段（15-30s）：从激活到定格 ═══

Phase 5 (15-19s): 功能激活
  承接合拢白光→屏幕从该光点扩散亮起。
  界面元素浮现，数字跳动，传感器逐个激活发光。

Phase 6 (19-23s): 爆发旋转
  高速 360°环绕，追光锁定旋转中的关键特征面。
  旋转中每个面被依次照亮（正面→侧面→底部→背面）。

Phase 7 (23-27s): 微距潜入
  从旋转减速→镜头潜入材质微距。
  极浅景深逐层揭示材质细节（拉丝→倒角→接缝→镀膜）。
  超慢运镜收尾。

Phase 8 (27-30s): 品牌定格
  材质纹理逐渐模糊→弹射拉远至全景定格。
  产品完美姿态 + Logo + Slogan。
```

##### 30s 双段衔接设计

| 衔接策略 | 描述 | 适用 |
|---------|------|------|
| **动势延续** | 第一段末尾的运动在第二段开头继续 | 所有类型 |
| **光线因果** | 第一段末尾的光效成为第二段开头的光源 | 纯产品型 |
| **场景穿越** | 镜头穿入产品→穿出到新场景 | 品牌世界型 |
| **情绪跳板** | 第一段末尾蓄力→第二段开头爆发 | 需要高潮感 |

---

#### 二、TVC 15s 紧凑节奏

##### 压缩五阶段模型

| 阶段 | 时长 | 功能 | 产品状态 |
|------|------|------|---------|
| **闪现揭示** | 0-2s | 最短时间建立产品印象 | 轮廓光快速亮起 / Match Cut 入场 |
| **核心卖点** | 2-6s | 集中展示 1-2 个核心功能 | 功能激活 / 拆解展示（二选一） |
| **视觉高潮** | 6-10s | 最具冲击力的画面 | 爆发旋转 / 极限场景 / 微距奇观 |
| **情绪锚点** | 10-13s | 留下一个记忆点 | 极致微距 / 情感高点 |
| **品牌定格** | 13-15s | Logo + 产品 + Slogan | 产品最终形态定格 |

##### 15s 铁律

- **单焦点原则**：15s 只传递 1 个核心记忆点
- **禁止空镜**：每一帧都有产品或品牌相关信息
- **转场即内容**：Match Cut 本身就是信息传递
- **2s 定格铁律**：最后 2s 必须是静态定格

##### 15s 紧凑示例（无线耳机）

```
风格：科技极简 / 纯黑+珠光白+冰蓝呼吸光 / Low-key 棚拍 / 无背景音乐 产品@产品多视图图片 的广告

Phase 1 (0-2s): 开盖揭示
充电盒在纯黑背景中，盒盖缓慢开启——内部冰蓝呼吸灯亮起，
两只耳机在磁力悬浮中微微上升脱离充电槽。
镜头从正面微推。盒盖开启的弧线引导视线向上。

Phase 2 (2-6s): 悬浮 + 功能激活
两只耳机完全脱离充电盒，在画面中悬浮旋转。
左耳机剖面透视亮起——内部芯片电路发出脉冲光，
降噪麦克风阵列依次亮起绿色指示点（暗示主动降噪）。
右耳机表面一圈触控区亮起冰蓝色弧线（暗示触控操作）。

Phase 3 (6-10s): 爆发旋转 + 微距
两只耳机高速对向旋转 360°展示全貌——
旋转减速后镜头急推至耳机外壳微距，
珠光白陶瓷表面的纳米级颗粒纹理充满画面，
侧光扫过时颜色从纯白微偏向淡蓝虹彩。

Phase 4 (10-13s): 回归充电盒
镜头弹射拉远。两只耳机缓缓降落归位充电盒，
磁吸对位的瞬间发出微弱的白光脉冲。
盒盖缓慢合拢，表面弧线上的品牌 Logo 被轮廓光照亮。

Phase 5 (13-15s): 品牌定格
充电盒以 3/4 低角度静置于画面中央。
盒盖缝隙透出一丝冰蓝呼吸光。
品牌 Logo 在上方浮现，Slogan 在下方以细字排列。

光影要求：全片 Low-key 纯黑背景，产品自发光（呼吸灯/指示灯/脉冲光）
为主要光源，辅以精准的轮廓光勾勒产品边缘。
```

---

### Appendix: 产品视频提示词自检清单

- [ ] **每个 Phase 有精确的秒数标注**（总时长=各 Phase 之和）
- [ ] **运镜有速度变化**（有快慢节奏对比）
- [ ] **至少一个 Phase 包含材质微距**
- [ ] **至少一个 Phase 包含功能可视化**
- [ ] **光影有叙事弧线**（有变化和递进）
- [ ] **有 Match Cut 或视觉过渡**（Phase 间有动势/色彩延续）
- [ ] **End Frame 元素精简**（只有产品+Logo+Slogan）
- [ ] **材质描述有物理细节**（不是"金属质感"，而是"拉丝纹理在侧光下形成流动高光"）
- [ ] **产品状态有变化弧线**（从静止→拆解→激活→展示→定格）
- [ ] **品牌调性一致**

---

<a id="src-tvc-ppm-producer-skill-md"></a>

## `tvc-ppm-producer/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: tvc-ppm-producer
description: TVC PPM producer for complete pre-production meeting packs. Use when Codex needs to prepare PPM documents, production checklists, casting references, wardrobe, makeup, hair, art direction, props, location, product handling, lighting, camera, music references, schedule, risks, approval items, or client meeting materials for an advertising film.
---
```

## TVC PPM Producer

Use this skill to prepare a complete PPM pack for TVC execution.

### Workflow

1. Confirm scope:
   - Film duration, format, approved concept, key scenes, talent needs, product needs, AI/live-action balance.

2. Build PPM sections:
   - Creative recap and film structure.
   - Director treatment summary.
   - Casting and performance references.
   - Wardrobe, makeup, hair.
   - Art direction, props, location, set dressing.
   - Product preparation, hero product rules, packshot requirements.
   - Camera, lens, movement, lighting, color.
   - Music, sound, voiceover, supers.
   - Shot plan, schedule, delivery, risk, approvals.

3. Flag decision points:
   - What client must approve.
   - What can be adjusted internally.
   - What blocks production if unanswered.

### Output Format

```markdown
PPM 目录：
逐项方案：
客户确认项：
制作风险：
物料清单：
下游交接：
```

### Quality Bar

- Include every visible element that may affect continuity.
- Separate reference direction from final locked choice.
- Make approval items explicit so production does not proceed on hidden assumptions.

---

<a id="src-tvc-ai-production-coordinator-skill-md"></a>

## `tvc-ai-production-coordinator/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: tvc-ai-production-coordinator
description: TVC AI production coordinator for managing generated-video execution. Use when Codex needs to plan AI production batches, prepare reference assets, manage actor/product continuity, version naming, shot status, regeneration decisions, quality control, tool handoffs, missing material lists, or production schedules for AI-made TVCs.
---
```

## TVC AI Production Coordinator

Use this skill to manage the practical execution of AI-generated TVC shots.

### Workflow

1. Build the production map:
   - Shot list, priority, dependencies, assets needed, tool target, status.

2. Prepare materials:
   - Product reference, actor reference, wardrobe reference, location/style references, logo/packshot assets, audio references.

3. Control continuity:
   - Assign anchors for actor face, wardrobe, product, props, lighting, color, aspect ratio, camera grammar.
   - Track which shots reuse which references.

4. Manage generations:
   - Batch shots by scene, character, location, or product setup.
   - Define version names, acceptance criteria, reject reasons, regeneration instructions.

### Output Format

```markdown
制作批次：
物料准备：
连续性锁定：
镜头状态表：
返工规则：
下游交接：
```

### Quality Bar

- Generate hero product, face, and hand-interaction shots with the strictest references.
- Do not let a beautiful shot pass if it breaks continuity or product truth.
- Keep version naming simple enough for editing and client review.

---

<a id="src-tvc-editing-director-skill-md"></a>

## `tvc-editing-director/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: tvc-editing-director
description: TVC editing director for cut structure and delivery. Use when Codex needs to plan or critique TVC edits, shot order, rhythm, timing, music beats, sound design, voiceover, subtitles, supers, packshot, end card, versioning, delivery formats, review exports, or post-production handoff for advertising films.
---
```

## TVC Editing Director

Use this skill to shape a TVC from generated or shot material into a reviewable edit.

### Workflow

1. Define edit intent:
   - What the first 3 seconds must achieve.
   - Where the product proof appears.
   - Where emotion, claim, and brand landing peak.

2. Build the edit structure:
   - Shot order.
   - Duration by beat.
   - Music beat and cut point.
   - VO/super/subtitle timing.
   - Sound effects and ambience.
   - Packshot/end card logic.

3. Prepare review delivery:
   - Version name.
   - Change log.
   - Export ratios and durations.
   - Known issues and pending decisions.

### Output Format

```markdown
剪辑策略：
节奏时间线：
声音与音乐：
字幕包装：
交付版本：
下游交接：
```

### Quality Bar

- Keep the edit understandable without explaining it in the meeting.
- Do not sacrifice product recognition for mood.
- Make client review versions traceable and comparable.

---

<a id="src-tvc-client-review-interpreter-skill-md"></a>

## `tvc-client-review-interpreter/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: tvc-client-review-interpreter
description: TVC client review interpreter for decoding feedback and revisions. Use when Codex needs to analyze client审片意见, distinguish surface comments from real intent, classify mandatory vs negotiable changes, translate vague feedback into edit/prompt/PPM actions, prepare response language, or produce revision execution tables for advertising films.
---
```

## TVC Client Review Interpreter

Use this skill before changing an edit, prompt, script, or treatment based on client feedback.

### Workflow

1. Parse every comment:
   - Literal request.
   - Likely underlying concern.
   - Affected asset: script, shot, AI prompt, edit, music, VO, packshot, claim, legal, brand tone.

2. Classify:
   - Must change.
   - Can negotiate.
   - Need clarification.
   - Risky or contradictory.

3. Translate into actions:
   - Editing action.
   - Prompt regeneration action.
   - Script/super/VO action.
   - Client response wording.

4. Preserve relationship:
   - Acknowledge the concern.
   - Offer a production-safe interpretation.
   - Ask precise questions only where ambiguity blocks execution.

### Output Format

```markdown
反馈原文：
真实意图判断：
修改优先级：
执行动作表：
需追问问题：
客户回复建议：
下游交接：
```

### Quality Bar

- Never treat vague feedback as literal too quickly.
- Identify contradictions between comments.
- Convert emotional words like "高级", "太平", "不够冲击", "不像我们品牌" into concrete craft levers.
- Protect schedule, continuity, product accuracy, and approval traceability.

---

<a id="src-tvc-ai-director-references-client-communication-md"></a>

## `tvc-ai-director/references/client-communication.md`

## Client Communication

Use this reference for client-facing TVC wording and feedback interpretation.

### Feedback Translation

| Client wording | Possible real concern | Craft levers |
| --- | --- | --- |
| 不够高级 | Too noisy, cheap, literal, or off-brand | Reduce clutter, improve light, slower rhythm, cleaner art, premium sound |
| 太平 | No tension, weak hook, same rhythm | Reorder opening, add contrast, sharpen cut points, stronger music beat |
| 不像我们品牌 | Tone mismatch or missing brand codes | Restore brand color, language, scenario, attitude, product ritual |
| 产品不突出 | Product appears late or without proof | Add hero insert, longer hold, cleaner packshot, use-case proof |
| 有点假 | AI artifact, performance, or unrealistic scene | Fix face/hands, reduce impossible movement, add natural imperfection |
| 节奏太快 | Message not absorbed | Add hold frames, simplify supers, reduce shot count |
| 节奏太慢 | Energy drops | Tighten setup, cut repeated action, move product proof earlier |
| 情绪不够 | Performance/music/story lacks lift | Adjust acting beat, music arc, close-up, reaction shot |

### Reply Pattern

```markdown
收到，这条意见我理解为：[真实关注点]。
我们建议从 [具体执行动作] 调整，这样可以保留 [已被认可部分]，同时解决 [客户担心的问题]。
有一项需要您确认：[必须确认的问题]。
```

### Internal Review Matrix

Classify every note:

- `Must change`: clear client decision or legal/product issue.
- `Negotiate`: could damage film quality or schedule.
- `Clarify`: ambiguous, contradictory, or needs asset/approval.
- `Risk`: may affect continuity, claim truth, cost, timing, or version control.

### Client-Safe Language

- Say "我理解这条意见背后的关注点是..." instead of "客户真正想说的是...".
- Say "建议用这个方式解决" instead of "不能这么改".
- Say "这会影响..." instead of "做不到".
- Keep internal doubts out of client-facing wording.

---

<a id="src-tvc-ai-director-references-tvc-quality-bar-md"></a>

## `tvc-ai-director/references/tvc-quality-bar.md`

## TVC Quality Bar

Use this checklist before final delivery from any TVC specialist.

### Strategy

- The output states who must believe what after watching.
- Product truth and emotional promise are separated.
- The brand appears as the owner of the idea, not a logo at the end.
- Risks are named early: claims, talent, legal, schedule, production, AI continuity.

### Creative

- The opening has a reason to continue watching.
- The product role is necessary to the story.
- The concept can be explained in one sentence and executed in shots.
- Routes are meaningfully different, not just different adjectives.

### Director Craft

- Tone, camera, light, art, performance, rhythm, music, and product treatment point in the same direction.
- Visual references are translated into actionable choices.
- Product shots have dignity, timing, and clear visibility.

### PPM

- Every visible element has a decision owner.
- Casting, wardrobe, makeup, hair, art, props, location, product, light, sound, and schedule are represented.
- Client approval items are separated from internal execution notes.

### Storyboard

- Total duration matches the target.
- Every shot has a purpose.
- Shot transitions are motivated.
- Actor/product/wardrobe/prop/light continuity is trackable.

### AI Generation

- Continuity anchors are explicit before per-shot prompts.
- Each shot prompt includes duration, ratio, subject, product, action, camera, light, tone, and end state.
- Negative prompts block face drift, product deformation, unreadable text, logo errors, extra limbs, random subtitles, and style shifts.
- Regeneration instructions state what to keep and what to change.

### Editing

- The first 3 seconds are legible.
- Product proof lands before audience patience runs out.
- Music and cuts support the idea rather than decorating it.
- Versions are named and comparable.

### Client Review

- Each note is interpreted before action.
- Contradictory comments are flagged.
- Vague words are converted into craft levers.
- Response language protects relationship and schedule.

---

<a id="src-tvc-ai-director-references-category-playbooks-md"></a>

## `tvc-ai-director/references/category-playbooks.md`

## Category Playbooks

Use these defaults when the category is known and the brief does not provide stronger guidance.

### Fast Consumer Goods

- Prioritize recognizability, appetite, use occasion, and memory device.
- Show product quickly and repeatedly.
- Use clear packshot, usage ritual, and sensory close-ups.
- Risks: generic happy-life scenes, weak product ownership, unreadable packaging.

### Beauty and Personal Care

- Prioritize skin/hair texture, transformation, aspiration, trust, and sensorial detail.
- Use controlled close-ups, soft light, clean art direction, and ingredient/proof moments.
- Risks: overpromising claims, plastic skin, inconsistent face, AI hand/product issues.

### Automotive

- Prioritize stance, motion, interior detail, lifestyle, safety/performance proof.
- Use low angles, tracking, reflections, road rhythm, UI/detail inserts.
- Risks: unrealistic road behavior, distorted car geometry, unreadable model details.

### 3C and Technology

- Prioritize feature clarity, interface legibility, product design, scenario proof.
- Use macro details, clean surfaces, controlled reflections, motion graphics overlays.
- Risks: fake UI, unreadable screen text, feature claims without use scene.

### Food and Beverage

- Prioritize appetite, temperature, texture, pour/bite/sizzle, social occasion.
- Use macro, slow motion, steam, condensation, crunch, color contrast.
- Risks: artificial food texture, package inconsistency, unmotivated lifestyle shots.

### Internet and Services

- Prioritize user problem, transformation, interface clarity, trust.
- Use scenario before/after, screen choreography, UI abstraction, human emotion.
- Risks: too conceptual, invisible product, over-explaining with subtitles.

### Public Welfare

- Prioritize emotional truth, restraint, dignity, and behavioral call to action.
- Use human moments, silence, contrast, symbolic but concrete details.
- Risks: melodrama, guilt manipulation, unclear action.

### Brand Image

- Prioritize belief, attitude, world, and long-term brand memory.
- Use cinematic tone, recurring motif, character or cultural tension.
- Risks: beautiful but empty film, product/brand absent, vague manifesto.

### Product Function Film

- Prioritize problem, feature, proof, demonstration, result.
- Use clear setup, visual comparison, close-up evidence, simple narrative.
- Risks: tutorial dryness, claim overload, no emotional reason to care.

---

<a id="src-tvc-director-references-delivery-md"></a>

## `tvc-director/references/delivery.md`

## TVC 输出格式与迭代知识库

> **职责**：提示词输出格式模板 + 迭代优化指南。
> **不管**：创意策略（查 treatment.md）、提示词工程（查 shot-language.md）、分镜与视频（查 storyboard.md）。

---

### Part 1: 输出格式模板

单帧、序列、TVC 资产序列、Multi-Phase 视频提示词和 End Frame 的输出格式模板。

---

### 一、模式一：单张关键帧提示词

当用户需要生成**单张特定画面**时使用。

**输出结构**：

```
### 关键帧：[标题]
**用途**：[这张图在视频中的作用——首帧/尾帧/转场帧/角色设定/环境设定]
**画面比例**：[16:9 / 9:16 / 1:1 / 根据用途建议]

**Nano Banana Pro 提示词**：
[直接可复制使用的完整提示词]

**参考图需求**：[用户是否已提供参考图。有→标注"已提供，附图生成"；无→标注"无参考图，纯文字描述生成"]

**生成建议**：[针对这张图的生成注意事项，如可能需要多次微调的部分]
```

---

### 二、模式二：关键帧序列提示词

当用户需要为一个完整的分镜脚本生成**一组关键帧**时使用。

**输出结构**：

```
## 关键帧序列：[项目名称]

### 生成顺序与依赖关系
| 序号 | 关键帧 | 类型 | 依赖 | 优先级 |
|------|--------|------|------|--------|
| 1 | ... | 角色设定 | 无 | ★★★★★ |
| 2 | ... | 环境概念 | 无 | ★★★★★ |
| 3 | ... | 叙事构图 | 依赖#1、#2 | ★★★★☆ |
| ... | ... | ... | ... | ... |

### 一致性锚点
- **角色一致性**：[如何维护多张图中角色的一致性]
- **环境一致性**：[如何维护环境风格统一]
- **色调一致性**：[如何维护整组图的色彩基调]

---

### 帧1：[标题]
（同模式一的单帧结构）

### 帧2：[标题]
...
```

---

### 三、序列生成顺序原则

1. **先角色后场景**：角色设定图（三视图/特写）优先生成，后续场景图可引用角色参考
2. **先环境后构图**：独立的环境概念图优先，叙事构图在角色+环境都确定后生成
3. **先全局后细节**：大远景/全景优先确定整体氛围，再生成特写/局部
4. **关键帧 > 过渡帧**：高潮画面、首帧、定格帧优先，过渡帧最后

---

### 四、一致性维护策略

#### 角色一致性

- 首先生成角色三视图/设定图，建立视觉基准
- 后续场景图使用 `图中[角色名]` 或 `图1` 引用角色参考图
- 同一角色在不同场景中的服装、发型、体型描述保持一致
- 如有特殊变化（受伤、换装），明确标注变化点

#### 环境一致性

- 同一场景的不同角度/镜头保持相同的材质、色调、大气描述
- 使用统一的环境关键词锁定风格
- 先生成环境概念图确定基调，再在叙事构图中引用

#### 色调一致性

- 全套关键帧使用统一的画风方向（A/B/C/D/E）
- 色调变化应遵循创意方案中的色彩弧线设计
- 在每帧提示词的画风锚定部分保持相同的核心词

---

### 五、模式三：TVC 产品资产序列

当需要为 TVC 广告片建立**产品视觉资产库**时使用。产品资产是 TVC 视觉体系的基石——所有后续场景、视频提示词和 End Frame 都依赖产品资产作为视觉锚点。

**输出结构**：

```
## 产品资产序列：[产品名称]

### 产品资产清单
| 序号 | 资产类型 | 用途 | 优先级 |
|------|---------|------|--------|
| 1 | 产品 Hero Shot | 锁定产品主视觉 | ★★★★★ |
| 2 | 产品材质微距 | 锁定材质质感 | ★★★★☆ |
| 3 | 品牌世界环境 | 锁定使用场景氛围 | ★★★★☆ |
| 4 | 产品交互特写 | 锁定使用动作/手势 | ★★★☆☆ |
| 5 | 产品包装/配件 | 锁定品牌周边元素 | ★★★☆☆ |
| ... | ... | ... | ... |

### 产品一致性锚点
- **产品外观**：[产品的形状、比例、标志性设计特征的精确描述]
- **材质/光影**：[产品表面材质类型、反射特性、推荐打光方式]
- **品牌色**：[主色/辅色/点缀色的具体色值或描述性定义]

---

### 资产1：产品 Hero Shot
**用途**：锁定产品主视觉，作为后续所有产品出镜画面的参考基准
**画面比例**：16:9

**Nano Banana Pro 提示词**：
[直接可复制使用的完整提示词]

**参考图需求**：[用户是否已提供产品参考图。有→标注"已提供，附图生成"；无→标注"无参考图，纯文字描述生成"]

**生成建议**：[针对产品渲染的生成注意事项，如材质精度、Logo 清晰度等]

---

### 资产2：产品材质微距
...

### 资产3：品牌世界环境
...
```

**使用要点**：

- 产品 Hero Shot 是最高优先级资产，必须首先生成并确认
- 后续所有涉及产品的关键帧和视频提示词，均应引用 Hero Shot 作为视觉锚点
- 品牌世界环境图用于锁定产品出现的场景氛围基调，后续场景帧在此基础上细化

---

### 六、模式四：TVC Multi-Phase 视频提示词

当需要为 TVC 的某一分镜段落生成**可直接用于视频生成工具的分阶段提示词**时使用。每个 Segment 对应多宫格分镜中的一个格子。

**输出结构**：

```
## TVC 视频提示词：[项目名称] · Segment [N]（[时段]）

**对应多宫格**：Grid [N]
**世界类型**：产品世界 / 品牌世界 / 交叉
**时长**：[X]s

**Multi-Phase 视频提示词**：
风格：[整体视觉风格描述——影调、色彩基调、质感]
Phase 1 (0-Xs): [运动/动作/画面内容描述]
Phase 2 (X-Ys): [运动/动作/画面内容描述]
Phase 3 (Y-Zs): [运动/动作/画面内容描述]
...
光影要求：[该段落的光影调性——自然光/棚拍光/特效光等]

**首帧关键帧引用**：[对应的关键帧资产编号或名称]

**衔接备注**：
- 与上一段的衔接：[尾帧→首帧的视觉/运动/情绪衔接方式]
- 与下一段的衔接：[本段尾帧如何为下一段的首帧做铺垫]
```

**使用要点**：

- 每个 Segment 的首帧应由已生成的关键帧资产锚定，确保视频起始画面的可控性
- Phase 划分基于镜头内的运动节奏，而非机械等分时间
- 衔接备注是 TVC 流畅性的关键——确保段落间的运动方向、色调、情绪不断裂
- 世界类型标注用于快速识别该段落属于产品展示逻辑还是品牌叙事逻辑

---

### 七、模式五：End Frame 专用输出

当需要生成 TVC 广告片的**收束定格画面（End Frame）**时使用。End Frame 是整支广告的最终视觉落点，承载品牌记忆和行动召唤。

**输出结构**：

```
### End Frame：[产品名]
**用途**：TVC 收束定格
**画面比例**：16:9
**文字叠加区域**：[描述 Logo 和 Slogan 预留位置——如"画面上方 1/3 留白用于 Logo 居中，下方 1/5 区域用于 Slogan"]

**Nano Banana Pro 提示词**：
[直接可复制使用的完整提示词——画面需预留文字叠加空间，避免核心视觉元素占据文字区域]

**参考图需求**：[是否需要品牌 VI 参考图、Logo 文件等]

**生成建议**：[End Frame 特有的生成注意事项，如留白区域的控制、品牌色的准确性等]

**后期叠加指引**：
- **Logo 位置**：[具体区域描述，如"画面正中偏上，占画面宽度的 30%"]
- **Slogan 位置**：[具体区域描述，如"Logo 正下方，与 Logo 间距约 40px"]
- **推荐字体风格**：[与品牌调性匹配的字体风格建议，如"无衬线/现代/手写体"]
- **推荐字色**：[基于画面底色的文字颜色建议]
```

**使用要点**：

- End Frame 的提示词必须刻意预留文字叠加空间，这是与普通关键帧的核心区别
- 画面应简洁、高级、克制，避免复杂场景与产品争夺视觉注意力
- 品牌色在 End Frame 中的呈现需高度精准，建议参考品牌 VI 手册
- 后期叠加指引为设计师提供可执行的排版方案，减少来回沟通成本

---

### 八、TVC 序列生成顺序原则

TVC 广告片的资产生成遵循**产品优先、逐层推进**的顺序，确保视觉一致性从核心向外辐射：

1. **先产品后场景**：产品 Hero Shot 最先生成，锁定产品的视觉基准（形态、材质、光影）。所有后续涉及产品的画面均以此为参考锚点
2. **先产品后品牌世界**：产品资产全部确认后，再生成品牌世界的环境、氛围、叙事场景。避免场景先行导致产品与环境风格脱节
3. **先多宫格后视频提示词**：多宫格分镜关键帧全部锁定后，再逐段生成 Multi-Phase 视频提示词。关键帧是视频提示词的视觉锚，顺序不可颠倒
4. **End Frame 最后**：End Frame 在所有视觉方向锁定后最后生成。此时整支 TVC 的色调、质感、品牌表达已充分明确，End Frame 可精准收束全片调性

---

### Part 2: 迭代优化指南

单变量迭代原则、11 种常见失败模式及修正方案、微调技巧与版本管理。

---

### 一、迭代核心原则

#### 1. 单变量原则

每次迭代只修改**一个变量**，观察效果变化。如果同时改了三个地方，无法判断哪个修改起了作用。

| 做法 | 效果 |
|------|------|
| ❌ 一次改了构图+光影+色调 | 无法归因，可能改对一个改坏两个 |
| ✅ 先只改光影描述 | 明确光影描述是否是问题根源 |
| ✅ 确认光影OK后再调构图 | 逐步逼近目标 |

#### 2. 加减法原则

修正的第一步是判断问题是"多了什么"还是"少了什么"：

- **多了不想要的元素** → 减法：删除可能暗示该元素的词汇
- **少了想要的效果** → 加法：加入更具体的描述词
- **效果方向错了** → 替换：换用含义更精确的词

#### 3. 位置权重原则

Nano Banana Pro 中，提示词**越靠前的词权重越高**。如果某个效果不够强：
- 把对应描述**移到更前面的位置**
- 或者在**开头就加入**最重要的画质/风格锚定

#### 4. 避免"越改越差"

| 陷阱 | 如何避免 |
|------|---------|
| 反复在同一句话上微调十几次 | 超过3次微调无效时，退一步分析根本原因 |
| 为了修一个问题加了太多词 | 提示词越长不等于越好，精简后重新来 |
| 从一个极端摆到另一个极端 | 不要从"太暗"直接改到"明亮"，用中间态过渡 |
| 忘了之前成功的版本 | 保留每次迭代的提示词文本，随时可以回退 |

---

### 二、常见失败模式与修正方案

#### 模式1：画面太亮 / 不够暗

**症状**：明明要求了"极度昏暗"，但生成结果仍然偏亮或有不合理的光源。

**原因分析**：
- 描述中有暗示光源的词（如提到"火把"、"灯光"、"阳光"等）
- "昏暗"的描述不够强烈
- 没有明确说"几乎全黑"

**修正方案**：
```
加入：环境极度昏暗 / 几乎全黑的环境 / 大部分空间被深邃的阴影吞没
加入：光线衰减极快
删除：任何可能暗示额外光源的词（火把、灯、明亮的XX）
前置：将"极度昏暗"移到描述最前面
```

#### 模式2：出现了不想要的物体

**症状**：画面中出现了没有要求的物体（如不需要的火把、人物、家具等）。

**原因分析**：
- 某些描述词隐含了这些物体（如"洞穴"可能自动生成火把）
- 上下文暗示（如"大厅"可能自动生成家具）

**修正方案**：
```
方法1：直接删除可能暗示该物体的描述
方法2：如果删除后物体仍然出现，在描述末尾加入排除指令
方法3：用更具体的空间描述替代模糊的空间类型词
```

**实例**：不想要火把
```
❌ 一个昏暗的地下洞穴大厅
✅ 一个极度昏暗的地下深渊大厅，没有任何人造光源，只有微弱的蓝色生物荧光
```

#### 模式3：空间感不够 / 不够宏大

**症状**：明明描述了"宏大"，但生成的空间看起来很小、很平。

**原因分析**：
- 缺乏垂直维度描述（天花板/穹顶）
- 缺乏大气透视（雾气、尘埃）
- 视角不够极端
- 缺乏参照物提供尺度感

**修正方案**：
```
加入：天花板高耸入云，消失在浓重的黑暗中（垂直维度）
加入：空气中弥漫着极其浓厚的体积雾，使远处变得虚无缥缈（大气透视）
加入：极低的视角以凸显空间的恐怖高度（极端视角）
加入：巨大的生物立柱像通天塔一样支撑着黑暗（参照物+尺度比喻）
```

#### 模式4：人物面部不好看 / 变形

**症状**：角色面部畸形、不自然、或与参考图差异太大。

**原因分析**：
- 面部描述过于复杂，AI无法同时满足所有要求
- 没有提供参考图
- 光影条件对面部不友好（太暗或太复杂的混合光）

**修正方案**：
```
策略1：简化面部描述，只保留最核心的1-2个特征
策略2：上传角色参考图，用"图中[角色]"引用
策略3：使用有利于面部的光影——侧光/逆光半剪影比正面平光效果好
策略4：如果是关键帧而非设定图，可以用侧颜/半剪影规避正脸细节
```

#### 模式5：色调不对

**症状**：画面色调与期望不符（太暖/太冷/太饱和/不够饱和）。

**原因分析**：
- 色调描述不够明确
- 光源颜色与目标色调矛盾
- 画风锚定词暗示了不同的色调

**修正方案**：
```
明确色调词：去饱和冷灰蓝 / 血橙深红 / 琥珀暖金 / 冷蓝绿
确保光源颜色一致：如果要冷色调，光源也应该是蓝色/白色，不能是暖黄
检查画风锚定：某些画风词自带色调倾向（如Golden Hour自动偏暖）
```

#### 模式6：构图散乱 / 主体不突出

**症状**：画面没有焦点，元素分布杂乱，不知道该看哪里。

**原因分析**：
- 没有指定构图法则
- 描述了太多等权重的元素
- 缺乏景深控制

**修正方案**：
```
加入明确构图：人物位于画面[位置]三分之一处 / 中心对称构图
减少元素：删掉非核心元素，让主体突出
加入景深：景深极浅，焦点在[主体]上，其余虚化
指定视觉引导：用[光线/道路/线条]引导视线到主体
```

#### 模式7：材质质感不够 / 太假

**症状**：金属看起来像塑料，皮肤像蜡像，布料像纸板。

**原因分析**：
- 材质描述太笼统
- 缺乏微观物理细节
- 光影不够复杂（缺少反射、次表面散射等）

**修正方案**：
```
金属：加入"拉丝纹理"、"使用磨损的光泽"、"微氧化痕迹"
皮肤：加入"毛孔"、"细微的汗珠"、"肤色不均匀的自然红晕"
布料：加入"编织纹理"、"折叠褶皱"、"边缘的毛边/磨损"
通用：加入"湿润反光"（所有表面加一层湿润感都会更真实）
```

#### 模式8：生成的图片太平/缺乏层次感

**症状**：画面像一张平面贴图，缺乏空间纵深。

**原因分析**：
- 缺乏前中远景分层
- 没有大气透视效果
- 所有元素处于同一焦平面

**修正方案**：
```
加入分层：前景：[虚焦元素]。中景：[主体]。背景：[环境]
加入大气：空气中弥漫体积雾/尘埃颗粒
加入景深：指定焦点位置，其余层次自然虚化
加入光照层次：近处强光远处渐暗，或逆光创造层次
```

#### 模式9：CG感过重 / 不像真人

**症状**：明明想要真人实拍效果，但生成结果像3D建模/CG渲染角色。皮肤过于光滑、打光过于均匀、整体有"数字感"。

**原因分析**：
- 画风锚定词偏CG方向（如"超写实电影风格"被模型理解为"超写实CG渲染"）
- 三视图/设定图格式本身是设计/建模概念，模型天然倾向CG输出
- 缺少摄影类锚定词来拉向真人方向
- 画质锚定词和画风锚定词之间方向矛盾

**修正方案**：
```
核心替换：将所有CG方向锚定词替换为真人方向锚定词
  ❌ 超写实电影风格 / 3A大作3D游戏风格
  ✅ 真人实拍，电影级摄影，真实皮肤毛孔质感，自然光照

加入真人强化词（按需选用）：
  + 真实皮肤毛孔质感（强制真人皮肤微观细节）
  + 自然光照（避免CG式均匀打光）
  + RAW照片质感（未经后期的原始摄影感）
  + 电影胶片色彩（胶片感色调）

检查并删除所有CG方向词：
  删除："大师级CG渲染"、"虚幻引擎5渲染"、"3A游戏"等
```

**实例**：
```
❌ 艾尔文角色三视图...画风为超写实电影风格。
✅ 艾尔文角色三视图...真人实拍，电影级摄影，真实皮肤毛孔质感，自然光照。
```

#### 模式10：真人感过重 / 想要CG但太写实

**症状**：想要3A游戏CG质感，但生成结果过于像真人照片，缺乏CG的精致感和艺术化。

**原因分析**：
- 画风锚定词偏真人方向
- 使用了"真人实拍"、"摄影"等锚定词
- 缺少CG方向的锚定词

**修正方案**：
```
核心替换：将真人方向锚定词替换为CG方向锚定词
  ❌ 真人实拍，电影级摄影
  ✅ 3A大作3D游戏风格 / 大师级CG渲染

如果要更精致的CG：
  ✅ 虚幻引擎5渲染，次表面散射皮肤，PBR材质，全局光照

删除所有真人方向词：
  删除："真人实拍"、"真实皮肤毛孔质感"、"自然光照"、"RAW照片"等
```

#### 模式11：风格混乱 / 真人和CG之间摇摆

**症状**：生成结果在真人和CG之间不稳定，同一批生成有的像真人有的像CG，或单张图中部分区域像真人部分像CG。

**原因分析**：
- 画风锚定词内部方向矛盾（同时包含真人类和CG类关键词）
- 画质锚定和画风锚定方向不一致
- "超写实电影画质"等双义词未被明确的方向词约束

**修正方案**：
```
诊断：检查提示词中所有画风/画质相关词，标记其方向归属
  真人方向词：真人实拍、电影级摄影、皮肤毛孔、自然光照、RAW照片
  CG方向词：3A游戏、CG渲染、虚幻引擎、PBR材质
  双义词（需注意）：超写实电影画质、电影级调色、8K超清

修正：确保所有方向词指向同一方向
  ❌ 超写实电影画质...3A大作3D游戏风格...真实皮肤毛孔质感
  ✅ 真人实拍，电影级摄影...真实皮肤毛孔质感，自然光照（全部真人方向）
  ✅ 大师级CG渲染，8K超清分辨率...3A大作3D游戏风格（全部CG方向）
```

---

### 三、微调技巧

#### 加词的影响规律

| 加入的词 | 通常的影响 |
|---------|-----------|
| "极其"、"极度" | 增强紧跟其后的描述词效果 |
| "微弱的" | 减弱光源/效果的强度 |
| "浓厚的" | 增强雾气/烟尘的密度 |
| "几乎全黑" | 大幅压暗整体画面 |
| "消失在黑暗中" | 让远处/高处的边界模糊化 |
| 具体数字（如"60米"） | 帮助AI建立尺度概念 |
| 画面占比（如"占画面70%"） | 精确控制元素大小 |

#### 减词的影响规律

| 删除的词 | 通常的影响 |
|---------|-----------|
| 删除多余光源描述 | 画面变暗 |
| 删除具体物体 | 该物体消失（但不一定，AI可能从上下文推断） |
| 删除色彩形容 | AI自行选择色调（可能不稳定） |
| 删除构图指示 | AI随机构图（不推荐） |

#### 替换词的技巧

| 原词 | 替换为 | 效果变化 |
|------|--------|---------|
| 昏暗 | 极度昏暗/几乎全黑 | 更暗 |
| 宏大 | 极其宏大的，天花板高耸入云 | 更有空间感 |
| 蓝色光 | 微弱的蓝色光源 | 光减弱 |
| 烟雾 | 极其浓厚的体积雾 | 雾更浓 |
| 广角 | 广角镜头，极低的视角 | 更极端的透视 |

---

### 四、迭代工作流

#### 标准迭代流程

```
1. 首次生成：使用完整提示词
   ↓
2. 评估结果：对比目标画面，找出差距
   ↓
3. 诊断问题：是哪个维度出了问题？
   - 色调？光影？构图？主体？环境？材质？
   ↓
4. 单变量修改：只修改问题维度的描述
   ↓
5. 二次生成：观察变化
   ↓
6. 如果OK → 进入下一个维度的微调
   如果不OK → 回到步骤3，换一个修改策略
   ↓
7. 超过3次无效修改 → 退一步，检查是否是根本思路的问题
```

#### 快速诊断清单

当生成结果不理想时，按以下清单逐项排查：

- [ ] **画风方向对不对？** → 检查画风锚定词是否指向正确方向（真人/CG/引擎级），是否有方向矛盾的词
- [ ] **画质是否达标？** → 检查画质锚定词是否在最前面
- [ ] **主体对不对？** → 检查主体描述是否清晰准确
- [ ] **空间感对不对？** → 检查环境描述的规模和大气效果
- [ ] **太亮还是太暗？** → 检查光源数量、强度和明暗描述词
- [ ] **色调对不对？** → 检查色彩描述词和光源颜色
- [ ] **构图对不对？** → 检查构图指示是否明确
- [ ] **有没有多余元素？** → 检查是否有描述词暗示了不想要的物体
- [ ] **材质质感够不够？** → 检查是否有微观物理细节描述
- [ ] **空间层次够不够？** → 检查是否有前中远景分层和景深控制

---

### 五、从失败到成功的实战路径示例

#### 示例：暗黑地下大厅

**目标**：极度昏暗的宏大地下空间，只有微弱蓝光。

**第1次**：
```
一个地下洞穴大厅，昏暗，蓝色光。3A游戏风格。
```
❌ 结果太亮，空间不够大，出现了火把。

**诊断**：描述太简单；"洞穴"暗示了火把；"昏暗"力度不够。

**第2次**：
```
极其宏大的地下深渊大厅，天花板高耸入云。环境极度昏暗，几乎全黑。微弱的蓝色光源。3A游戏大作级画质。
```
❌ 空间变大了但质感不够，体积感不足。

**诊断**：缺乏大气效果和材质描述。

**第3次**：
```
极其宏大的地下深渊大厅，天花板高耸入云，消失在浓重的黑暗中。3A游戏大作级画质。环境极度昏暗，几乎全黑。微弱的蓝色光源勾勒出空间宏伟的轮廓。空气中弥漫着极其浓厚的体积雾。墙壁布满湿润的、反光的几丁质甲壳纹理，巨大的生物立柱像通天塔一样支撑着黑暗。广角镜头，极低的视角以凸显空间的恐怖高度。
```
✅ 达到目标效果。

**关键改进**：加入了体积雾（空间感）、材质描述（质感）、极低视角（高度感）、"消失在黑暗中"（无限延伸感）。

---

### 六、版本管理建议

为了避免"越改越差"或"忘了之前的好版本"，建议：

1. **给每个提示词编号**：v1、v2、v3...
2. **记录每次修改了什么**：v2 vs v1 = 加入了体积雾描述
3. **标记满意度**：★★★☆☆
4. **保留最佳版本**：随时可以回退到之前的最佳状态
5. **记录成功模式**：某个描述组合效果好，记录下来作为未来的模板

---

<a id="src-tvc-director-readme-md"></a>

## `tvc-director/README.md`

## TVC Director · TVC 广告创意导演

[English](#src-tvc-director-readme-en-md)

从产品 brief 到电影级 TVC 关键帧——你的 AI 广告创意导演。

一个将 AI Agent 转化为 **TVC 广告创意导演** 的 Skill，覆盖电视广告和品牌广告的完整创意流程：从产品 brief 到可直接使用的多宫格分镜图片提示词和视频提示词。

### 工作流程

整个流程对应真实 TVC 广告制作的阶段：

```
"帮我做一条户外相机的30秒TVC"
        ↓
  Phase 1: 创意简报        ← 客户 Brief
  Phase 2: 创意提案        ← 创意总监提案会
  Phase 3: 视觉定调        ← 美术风格确认
  Phase 4: 前期筹备        ← 选角试装 + 产品定妆 + 堪景
  Phase 5: 分镜与拍摄      ← 分镜脚本 + 现场拍摄
  Phase 6: 审片迭代        ← 导演审片 + 修改
  Phase 7: 交付打包        ← 终版交付
        ↓
  可直接复制使用的多宫格分镜图片提示词、
  视频提示词和创意方案文档
```

### 核心特性

- **类比真实 TVC 制片流程** — 选角试装、产品定妆照、场景堪景、分镜脚本、拍摄执行——每个环节都有对应的 AI 提示词产出物
- **完整创意流水线** — 从一句话需求到可交付的分镜提示词和视频脚本，全程 AI 驱动
- **8 种 TVC 叙事模型** — 痛点-解决、产品电影化拆解、品牌世界穿梭等，覆盖主流广告叙事
- **电影级视觉系统** — 5 种画风预设（A-E）、12 种场景类型、精确到秒的运镜编排
- **产品+品牌世界双线叙事** — 不只是产品特写，而是产品在真实场景中的交叉剪辑
- **即拷即用** — 产出的提示词可直接粘贴到 Nano Banana Pro / Seedance，无需二次加工

### 成品展示

#### 汽车 TVC — 产品电影化拆解

https://github.com/user-attachments/assets/541055ed-d716-4087-86e2-a27d375282ed

#### 香水 TVC — 品牌世界穿梭

https://github.com/user-attachments/assets/df2d51af-acc2-4f34-a228-8b35ea754345

### 快速上手：一条汽车 TVC 的诞生

以下是一个真实的端到端案例——从一张参考图到 15 秒成片。

#### Step 1 — 给一张参考图 + 一句话需求

> "帮我做一条银色轿跑的 15 秒 TVC"

<img src="https://github.com/user-attachments/assets/0d774888-0dbb-4fb7-a861-ca3116b812b7" width="400" alt="参考图：银色轿跑" />

AI 会自动进入完整创意流：需求拆解 → 创意构思 → 画风确认 → 资产生成 → 分镜 + 视频脚本。

#### Step 2 — AI 生成产品多视图提示词 → Nano Banana Pro 出图

AI 输出产品多视图提示词，复制到 Nano Banana Pro（edit 模式，传入参考图），得到标准化的多角度产品图：

<img src="https://github.com/user-attachments/assets/9d97df38-79f1-4a6a-a6bb-0fdbd731faca" width="600" alt="产品多视图" />

#### Step 3 — AI 生成 9 宫格分镜提示词 → Nano Banana Pro 出图

AI 输出 3×3 多宫格分镜提示词（包含逐格构图、光影、运镜描述），复制到 Nano Banana Pro（edit 模式，传入多视图 + 环境图），得到完整分镜：

<img src="https://github.com/user-attachments/assets/1ca54c8a-e1c2-4a13-8e67-461ea327f2ab" width="600" alt="9 宫格分镜" />

#### Step 4 — AI 生成视频提示词 → Seedance 生成视频

AI 同步输出 Seedance Multi-Phase 视频提示词（5 Phase / 15s），配合多宫格作为首帧 + 产品多视图作为锚定，双图输入 Seedance 生成最终视频。

#### 产出物一览

| 产出物 | 工具 | 用途 |
|--------|------|------|
| 产品多视图 | Nano Banana Pro (edit) | 产品锚定，供后续步骤引用 |
| 9 宫格分镜图 | Nano Banana Pro (edit) | 视频首帧 + 视觉校对 |
| Multi-Phase 视频脚本 | Seedance | 生成 15s 成片 |
| 创意方案文档 | — | 完整创意 brief 存档 |

### 设计理念

传统 AI 生成广告往往只是"产品 + 黑底 + 旋转"的无限循环。TVC Director 不同——它按真实 TVC 制片 SOP 组织提示词生成，让每条提示词都有明确的制作环节归属：

- **叙事驱动** — 先确定叙事模型和创意方向，再生成视觉，不是无脑套模板
- **双世界交叉剪辑** — 产品特写与品牌世界场景交织，像真正的 TVC 一样讲故事
- **精确到秒的运镜设计** — 每一格分镜都有明确的景别、角度、光影和转场逻辑
- **渐进式人机协作** — 每个阶段都可以介入调整，不是一键出片的黑盒

### 三大核心能力

#### 1. 产品电影化拆解（Cinematic Product Breakdown）

产品是唯一主角，纯影棚，多 Phase 的产品微电影：

- 零件悬浮拆解/精密组装动画
- 材质微距：金属磨砂纹理、玻璃折射、碳纤维编织
- 精确到秒的运镜编排：极慢拆解 → 爆发旋转 → 悬浮凝视 → 俯冲穿越
- 光影叙事：低调影棚光、侧光勾勒轮廓、光随旋转流动

#### 2. 品牌世界穿梭（Brand World Crosscut）

品牌世界和产品世界轮流出场，用 Match Cut 衔接：

- 运动相机 → 跳伞、潜水、滑雪、攀岩
- 越野车 → 盘山弯道、沙漠、雪地
- 每个 Phase 完整待在一个世界里，通过匹配剪辑无缝切换

#### 3. 生活方式短片（Lifestyle Film）

产品始终待在品牌世界中，不跳出去做影棚特写：

- 跑鞋穿在脚上、手表戴在手腕、眼镜架在鼻梁
- 通过运镜手法（低角度追拍、慢动作、景深变化）自然突出产品
- 片尾集中做 Hero Shot 收束

### 安装

#### Cursor

```bash
git clone https://github.com/Ethanxwang/tvc-director.git ~/.cursor/skills/tvc-director
```

#### Claude Code

```bash
git clone https://github.com/Ethanxwang/tvc-director.git ~/.claude/skills/tvc-director
```

### 入口模式

| 模式 | 触发信号 | 说明 |
|------|---------|------|
| **A：完整 TVC 创意流** | "帮我做一条xx产品广告" | Brief → 创意 → 画风 → 资产 → 分镜 → 打包 |
| **B：快速资产/提示词** | "帮我做一个产品 Hero Shot" | 跳过创意阶段，直接生成资产或关键帧提示词 |
| **C：分镜转化** | 提供 TVC 分镜脚本 | 画风 → 资产 → 将分镜转化为关键帧提示词 |
| **D：迭代修正** | "这张产品图xx不对" | 定位问题并提供修正版提示词 |

### TVC 叙事模型

| 模型 | 名称 | 核心逻辑 |
|------|------|---------|
| A | 痛点-解决 | 痛点场景 → 产品拯救 |
| B | 产品电影化拆解 | 多 Phase 微电影逐步揭示卖点 |
| C | 品牌世界穿梭 | 使用场景 ↔ 产品特写交叉剪辑 |
| D | 生活方式短片 | 产品始终在场景中，运镜突出 |
| E | 情感锚点 | 情感故事，产品为载体 |
| F | 蒙太奇揭示 | 视觉奇观 → 产品揭示 |
| G | 前后对比 | 使用前后的强烈反差 |
| H | 品牌宣言 | 价值观驱动，产品收束 |

### 交付物

```
my-tvc-project/
├── concept.md                      # TVC 创意方案文档
├── storyboard.md                   # 分镜脚本（如有）
│
├── assets/                         # 产品资产图提示词（Nano Banana Pro）
│   └── prompts/
│       ├── product-multiview.md
│       ├── product-detail-01.md
│       ├── env-01-extreme-sports.md
│       └── ...
│
├── keyframes/                      # 分镜关键帧提示词（Nano Banana Pro）
│   └── prompts/
│       ├── grid-01-brand-world.md
│       ├── grid-02-product-world.md
│       ├── endframe.md
│       └── ...
│
└── video-scripts/                  # Multi-Phase 视频提示词（Seedance）
    ├── segment-01-brand-world.md
    ├── segment-02-product-breakdown.md
    └── ...
```

### 如何使用交付物

1. **产品多视图** — 将 `assets/prompts/product-multiview.md` 中的提示词复制到 Nano Banana Pro，选择 edit 模式，传入参考图
2. **分镜关键帧** — 将 `keyframes/prompts/` 下的提示词复制到 Nano Banana Pro，edit 模式，传入多视图 + 环境图
3. **视频脚本** — 将 `video-scripts/` 下的 Multi-Phase 脚本配合多宫格首帧 + 产品多视图，输入 Seedance 生成视频

### 知识库架构

知识库按真实广告制作的工种职责拆分，按需加载：

| 工种 | 文件 | 对应真实制作环节 | 加载时机 |
|------|------|---------------|---------|
| 制片统筹 | `SKILL.md` | 制片流程管控、阶段流转 | 始终加载 |
| 创意总监 | `treatment.md` | 创意提案、叙事模型、品类策略、出镜决策 | 创意提案 |
| 摄影指导 | `shot-language.md` | 镜头语言、画风体系、场景类型、构图范式 | 视觉定调 / 分镜 |
| 制片组 | `pre-production.md` | 选角试装、产品定妆、堪景、资产一致性 | 前期筹备 |
| 导演 | `storyboard.md` | 分镜脚本、视频脚本、产品拆解、品牌世界镜头 | 分镜与拍摄 |
| 后期 | `delivery.md` | 输出格式、迭代调试（11 种常见失败模式） | 审片 / 交付 |

### License

MIT

---

<a id="src-tvc-director-readme-en-md"></a>

## `tvc-director/README_en.md`

## TVC Director

[中文版](#src-tvc-director-readme-md)

From product brief to cinematic TVC keyframes — your AI advertising creative director.

A skill that turns your AI agent into a **TVC Advertising Creative Director**, handling the complete creative pipeline for television commercials and brand advertising: from a product brief to production-ready multi-grid storyboard image prompts and video prompts.

### How It Works

The workflow mirrors real TVC advertising production stages:

```
"Make a 30-second TVC for an outdoor camera"
        ↓
  Phase 1: Creative Brief        ← Client Brief
  Phase 2: Creative Proposal     ← Creative Director Pitch
  Phase 3: Look Development      ← Art Style Lock
  Phase 4: Pre-production        ← Casting & Wardrobe + Product Photography + Location Scouting
  Phase 5: Storyboard & Shoot    ← Storyboard + On-set Shooting
  Phase 6: Review & Iteration    ← Director's Review + Revisions
  Phase 7: Delivery              ← Final Delivery
        ↓
  Copy-paste-ready multi-grid storyboard image prompts,
  video prompts & creative docs
```

### Key Features

- **Mirrors real TVC production** — Casting & wardrobe, product photography, location scouting, storyboarding, shooting — each stage has a corresponding AI prompt deliverable
- **End-to-end creative pipeline** — From a one-line brief to deliverable storyboard prompts and video scripts, fully AI-driven
- **8 TVC narrative models** — Problem-solution, cinematic product breakdown, brand world crosscut, and more
- **Cinematic visual system** — 5 art style presets (A-E), 12 scene types, per-second camera choreography
- **Product + brand world dual narrative** — Not just product close-ups, but crosscut storytelling in real-world scenes
- **Copy-paste ready** — Output prompts work directly in Nano Banana Pro / Seedance with no rework needed

### Demo

#### Car TVC — Cinematic Product Breakdown

https://github.com/user-attachments/assets/541055ed-d716-4087-86e2-a27d375282ed

#### Perfume TVC — Brand World Crosscut

https://github.com/user-attachments/assets/df2d51af-acc2-4f34-a228-8b35ea754345

### Quick Start: Making a Car TVC

A real end-to-end example — from a reference photo to a 15-second commercial.

#### Step 1 — Provide a reference image + one-line brief

> "Make a 15-second TVC for this silver sedan"

<img src="https://github.com/user-attachments/assets/0d774888-0dbb-4fb7-a861-ca3116b812b7" width="400" alt="Reference: silver sedan" />

The AI enters the full creative pipeline: brief analysis → creative concept → art style → asset generation → storyboard + video script.

#### Step 2 — AI generates multiview prompts → Nano Banana Pro renders

The AI outputs product multiview prompts. Copy to Nano Banana Pro (edit mode, pass in the reference image) to get standardized multi-angle product shots:

<img src="https://github.com/user-attachments/assets/9d97df38-79f1-4a6a-a6bb-0fdbd731faca" width="600" alt="Product multiview" />

#### Step 3 — AI generates 3×3 storyboard prompts → Nano Banana Pro renders

The AI outputs a 3×3 multi-grid storyboard prompt (with per-panel composition, lighting, and camera direction). Copy to Nano Banana Pro (edit mode, pass in multiview + environment images):

<img src="https://github.com/user-attachments/assets/1ca54c8a-e1c2-4a13-8e67-461ea327f2ab" width="600" alt="3×3 storyboard grid" />

#### Step 4 — AI generates video prompts → Seedance renders video

The AI outputs a Seedance Multi-Phase video script (5 phases / 15s). Use the storyboard grid as the first frame + product multiview as the anchor, dual-image input to Seedance for the final video.

#### Output Summary

| Deliverable | Tool | Purpose |
|-------------|------|---------|
| Product multiview | Nano Banana Pro (edit) | Product anchor for subsequent steps |
| 3×3 storyboard grid | Nano Banana Pro (edit) | Video first frame + visual QA |
| Multi-Phase video script | Seedance | Generate 15s final video |
| Creative brief document | — | Full creative brief for archival |

### Design Philosophy

Traditional AI-generated ads tend to be an endless loop of "product + black background + rotation." TVC Director is different — it organizes prompt generation around the real TVC production SOP, so every prompt maps to a specific production stage:

- **Narrative-driven** — Determine the narrative model and creative direction first, then generate visuals; no mindless template filling
- **Dual-world crosscutting** — Product close-ups interweave with brand world scenes, telling stories like a real TVC
- **Per-second camera design** — Every storyboard panel has explicit shot size, angle, lighting, and transition logic
- **Progressive human-AI collaboration** — Intervene and adjust at every phase; not a black-box one-click generator

### Three Core Capabilities

#### 1. Cinematic Product Breakdown

Product as sole protagonist, pure studio, multi-phase product micro-films:

- Component disassembly/assembly animations (floating parts, exploded views, snap-back)
- Material macro shots (brushed metal, glass refraction, carbon fiber weave)
- Precise per-second camera choreography (ultra-slow reveal → explosive rotation → macro dive)
- Cinematic studio lighting (low-key, side light silhouettes, light flowing with rotation)

#### 2. Brand World Crosscut

Brand world and product world take turns, connected via match cuts:

- Action cameras → skydiving, diving, skiing, climbing
- Off-road vehicles → mountain roads, desert, snow
- Each Phase stays in one world; world switches happen between Phases

#### 3. Lifestyle Film

Product stays in the brand world throughout — no studio cutaways:

- Running shoes on feet, watches on wrists, glasses on faces
- Highlighted through cinematography (low-angle tracking, slow motion, depth-of-field shifts)
- Hero Shot concentrated at the end

### Installation

#### Cursor

```bash
git clone https://github.com/Ethanxwang/tvc-director.git ~/.cursor/skills/tvc-director
```

#### Claude Code

```bash
git clone https://github.com/Ethanxwang/tvc-director.git ~/.claude/skills/tvc-director
```

### Entry Modes

| Mode | Trigger | Description |
|------|---------|-------------|
| **A: Full TVC Pipeline** | "帮我做一条xx产品广告" | Brief → Concept → Style → Assets → Keyframes → Package |
| **B: Quick Asset/Prompt** | "帮我做一个产品 Hero Shot" | Skip creative phase, go to asset or keyframe generation |
| **C: Storyboard** | Provide a TVC script/storyboard | Style → Assets → Convert storyboard to keyframes |
| **D: Iteration** | "这张产品图xx不对" | Fix and regenerate specific assets or keyframes |

### TVC Narrative Models

| Model | Name | Core Logic |
|-------|------|-----------|
| A | Problem-Solution | Pain point → product saves the day |
| B | Cinematic Product Breakdown | Multi-phase micro-film revealing USPs |
| C | Brand World Crosscut | Scene ↔ product close-up crosscutting |
| D | Lifestyle Film | Product stays in scene, highlighted by cinematography |
| E | Emotional Anchor | Emotional story, product as carrier |
| F | Montage Reveal | Visual spectacle → product reveal |
| G | Before/After | Before/after strong contrast |
| H | Brand Anthem | Values-driven, product closes |

### Deliverables

```
my-tvc-project/
├── concept.md                      # TVC creative brief
├── storyboard.md                   # Storyboard (if applicable)
│
├── assets/                         # Product asset prompts (Nano Banana Pro)
│   └── prompts/
│       ├── product-multiview.md
│       ├── product-detail-01.md
│       ├── env-01-extreme-sports.md
│       └── ...
│
├── keyframes/                      # Storyboard keyframe prompts (Nano Banana Pro)
│   └── prompts/
│       ├── grid-01-brand-world.md
│       ├── grid-02-product-world.md
│       ├── endframe.md
│       └── ...
│
└── video-scripts/                  # Multi-Phase video prompts (Seedance)
    ├── segment-01-brand-world.md
    ├── segment-02-product-breakdown.md
    └── ...
```

### How to Use Deliverables

1. **Product multiview** — Copy prompts from `assets/prompts/product-multiview.md` into Nano Banana Pro, edit mode, pass in reference image
2. **Storyboard keyframes** — Copy prompts from `keyframes/prompts/` into Nano Banana Pro, edit mode, pass in multiview + environment images
3. **Video scripts** — Use Multi-Phase scripts from `video-scripts/` with the storyboard grid as first frame + product multiview, input to Seedance

### Knowledge Base Architecture

Knowledge base is organized by crew roles in real ad production, loaded on demand:

| Crew Role | File | Real Production Equivalent | Loading |
|-----------|------|---------------------------|---------|
| Line Producer | `SKILL.md` | Production workflow control, phase transitions | Always loaded |
| Creative Director | `treatment.md` | Creative pitches, narrative models, category strategy, casting decisions | Creative Proposal |
| Director of Photography | `shot-language.md` | Shot language, art style system, scene types, composition paradigms | Look Dev / Storyboard |
| Production Team | `pre-production.md` | Casting & wardrobe, product photography, location scouting, asset consistency | Pre-production |
| Director | `storyboard.md` | Storyboard, video scripts, product breakdown, brand world shots | Storyboard & Shoot |
| Post-production | `delivery.md` | Output formats, iteration guide (11 failure modes) | Review / Delivery |

### License

MIT

---

<a id="src-tvc-ai-director-assets-templates-ai-prompt-template-md"></a>

## `tvc-ai-director/assets/templates/ai-prompt-template.md`

## AI Prompt Template

| Shot | Image prompt | Video prompt | Negative prompt | Continuity lock | Regeneration notes |
| --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |

---

<a id="src-tvc-ai-director-assets-templates-brief-template-md"></a>

## `tvc-ai-director/assets/templates/brief-template.md`

## TVC Brief Template

| Field | Content |
| --- | --- |
| Brand |  |
| Product/Service |  |
| Category |  |
| Target audience |  |
| Business goal |  |
| Communication task |  |
| Key claim/proof |  |
| Required duration/ratio |  |
| Channels |  |
| Deadline |  |
| Budget level |  |
| Mandatories |  |
| Forbidden elements |  |
| Reference films |  |
| Available assets |  |
| Decision makers |  |

---

<a id="src-tvc-ai-director-assets-templates-director-treatment-template-md"></a>

## `tvc-ai-director/assets/templates/director-treatment-template.md`

## Director Treatment Template

| Section | Direction |
| --- | --- |
| Director statement |  |
| Image tone |  |
| Camera language |  |
| Rhythm |  |
| Performance |  |
| Product treatment |  |
| Art direction |  |
| Lighting |  |
| Music and sound |  |
| References |  |

---

<a id="src-tvc-ai-director-assets-templates-editing-template-md"></a>

## `tvc-ai-director/assets/templates/editing-template.md`

## Editing Template

| Beat | Timecode | Shot(s) | Edit purpose | Music/SFX | VO/Super | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Opening hook | 0:00-0:03 |  |  |  |  |  |
| Development |  |  |  |  |  |  |
| Product proof |  |  |  |  |  |  |
| Brand landing |  |  |  |  |  |  |

---

<a id="src-tvc-ai-director-assets-templates-ppm-template-md"></a>

## `tvc-ai-director/assets/templates/ppm-template.md`

## PPM Template

| Section | Proposal | Client approval needed | Risk/notes |
| --- | --- | --- | --- |
| Creative recap |  |  |  |
| Casting |  |  |  |
| Wardrobe |  |  |  |
| Makeup/hair |  |  |  |
| Art direction |  |  |  |
| Props |  |  |  |
| Location/set |  |  |  |
| Product handling |  |  |  |
| Camera/lens |  |  |  |
| Lighting/color |  |  |  |
| Music/sound |  |  |  |
| Schedule |  |  |  |
| Delivery |  |  |  |

---

<a id="src-tvc-ai-director-assets-templates-proposal-template-md"></a>

## `tvc-ai-director/assets/templates/proposal-template.md`

## TVC Proposal Template

| Route | Core idea | Audience insight | Product role | Story arc | Tone | Visual hook | Risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A |  |  |  |  |  |  |  |
| B |  |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |

---

<a id="src-tvc-ai-director-assets-templates-review-template-md"></a>

## `tvc-ai-director/assets/templates/review-template.md`

## Client Review Template

| Comment | Literal request | Likely intent | Priority | Action | Owner | Client reply |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Must change / Negotiate / Clarify / Risk |  |  |  |

---

<a id="src-tvc-ai-director-assets-templates-storyboard-template-md"></a>

## `tvc-ai-director/assets/templates/storyboard-template.md`

## Storyboard Template

| Shot | Time | Scene | Shot size | Camera | Visual action | Actor action | Product action | Light/tone | VO/Super/SFX | AI notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0:00-0:00 |  |  |  |  |  |  |  |  |  |

---

<a id="src-seedance-tvc-director-skill-md"></a>

## `seedance-tvc-director/SKILL.md`

### Original Skill metadata (reference only)

```yaml
---
name: seedance-tvc-director
description: "把用户提供的品牌或产品 brief、参考素材和成片反馈整理为 TVC 创意方案、15 秒、30 秒或自定义时长的导演执行单、可复制的视频提示词，以及可选的无文字九宫格分镜；能分别配置视频模型、生成段数、节奏与镜头密度。适用于 TVC、品牌广告、产品广告、商业短片、Seedance 2.5、广告分镜、旁白设计和生成结果复盘；不用于纯社媒口播、直播切片或与 TVC 无关的视频参数咨询。"
---
```

## Seedance TVC 导演

把商业目标先翻译成可判断的 TVC 创意，再把选定方向编译成当前所选视频模型能执行的镜头指令；Seedance 2.5 是 30 秒单段完整生成的优先适配对象。保护品牌事实、产品外观和交付边界，不用空泛画质词代替导演判断。

### 能力与权限边界

- 本 Skill 只提供文本规则、创意路由、分镜规划、提示词编译和成片复盘，不包含可执行脚本，不主动联网，不读取外部账号，也不请求登录、发布、删除或付费权限。
- 只处理用户在当前任务中主动提供的 brief、图片、视频和品牌资料；引用外部事实或当前平台参数前先核对来源，不把未验证信息写成广告事实。
- 直出模式交付可复制的视频提示词；九宫格模式在当前 Agent 已提供生图能力且用户选择该模式时才实际渲染，否则只交付可复制的分镜生图提示词。
- 是否能够直接生成图片或视频、单次最长时长及最终成片质量取决于用户实际使用的 Agent 和视频入口。本 Skill 不绕过平台限制，也不承诺模型能力、审核结果或商业效果。

### 执行流程

1. 读取用户提供的 brief、产品资料、参考图、参考视频和既有提示词。
2. 提取品牌、产品、受众、传播目标、单一核心主张、产品证明、必露元素、禁区、时长和画幅。
3. 在创意发散前读取 [generation-modes.md](#src-seedance-tvc-director-references-generation-modes-md)、[model-and-segmentation-routing.md](#src-seedance-tvc-director-references-model-and-segmentation-routing-md) 和 [pacing-and-shot-density.md](#src-seedance-tvc-director-references-pacing-and-shot-density-md)，把以下六项作为互不绑定的配置分别确认：
   - `时长`：15 秒、30 秒或自定义秒数；
   - `声音`：有旁白、无旁白，或同时生成有旁白版与无旁白版；
   - `生成方式`：直出模式或九宫格模式；
   - `视频模型`：使用基于当前平台能力的推荐模型，或由用户指定；
   - `生成段数`：单段完整生成、多段生成后剪辑，或按当前平台能力自动选择。
   - `节奏与镜头密度`：快节奏商业版、标准商业节奏、克制电影节奏，或用户自定义镜头数/平均镜长。
   用户已明确的项目直接采用，只合并询问缺失项。每项先给推荐和一句理由；用户明确要求 Agent 决定或不要提问时，分别采用推荐项并标注可逆假设。
4. 对缺失信息分类：
   - 会改变创意方向的关键缺失最多询问 3 个短问题。
   - 用户要求直接输出时，采用保守假设并显式标注。
   - 未验证的卖点、数据、认证、效果和法律表述保留为 `【待补：具体内容】`，不得编造。
5. 画面包含人物时读取 [casting-and-beauty-direction.md](#src-seedance-tvc-director-references-casting-and-beauty-direction-md)，明确目标年龄感、品牌能量、发型妆面、服装、表演、空间和 beauty lighting；不得只写“年轻、漂亮、高级”。同一镜头出现 3 人以上、多人伸手或群像跨景别时，同时读取 [ensemble-continuity.md](#src-seedance-tvc-director-references-ensemble-continuity-md)，锁定人数、身份差异、座位顺序和肢体归属；多人围桌时还要先选桌型、相对相机的座位拓扑、视线目标和各自伸手区，不能只写“围坐圆桌”。
6. 按已确认的独立声音选项读取 [voiceover.md](#src-seedance-tvc-director-references-voiceover-md)。有旁白时建立唯一一张主旁白清单；旁白原文只在清单出现一次，镜头时间轴只引用 VO ID，不得在不同场景重复粘贴句子。30 秒有旁白商业片还要建立中段注意力接力：测量约 4–23 秒的信息性人声空窗，并为超过约 2.5 秒的空窗标注承担新信息的强动作、产品声、音乐结构变化或视觉事件；不能让重复品尝成为十秒叙事真空。同时生成两套完整声音版本时，分别编译镜头停留与声音结构，不能只删除音轨。
7. 始终读取 [ad-hook.md](#src-seedance-tvc-director-references-ad-hook-md)。总时长达到 3 秒时先确定 0–3 秒广告钩子；少于 3 秒时从第一帧同时完成钩子、产品识别与品牌记忆。
8. 读取 [brief-and-concept.md](#src-seedance-tvc-director-references-brief-and-concept-md)，形成单一核心主张和 3 条有差异的创意路线。
9. 用户已经选定方向时跳过路线发散，直接读取 [tvc-structure.md](#src-seedance-tvc-director-references-tvc-structure-md) 完成 15 秒、30 秒或自定义时长导演结构。制作 30 秒片、较长自定义版本、用户要求画面丰富/展示长时叙事能力，或成片出现同场景重复时，同时读取 [scene-progression.md](#src-seedance-tvc-director-references-scene-progression-md) 完成场景路由和反重复检查。使用 12 镜以上、两个世界交替、同一动作跨切点、旅程/溯源蒙太奇或声音先行转场时，再读取 [shot-handoffs-and-sound-bridges.md](#src-seedance-tvc-director-references-shot-handoffs-and-sound-bridges-md)，建立场景锚、全局运动向量、镜头交接和声音契约。
10. 涉及参考素材、产品外观、分镜编排或视频提示词时，读取 [seedance-2-5-prompting.md](#src-seedance-tvc-director-references-seedance-2-5-prompting-md)，并按已确认的视频模型与生成段数调整能力边界。食品或饮料把具体口味、香气或口感作为卖点时，同时读取 [food-flavor-direction.md](#src-seedance-tvc-director-references-food-flavor-direction-md)，把口感与风味分开，并建立可见的风味证据链。出现撕袋、开盒、开盖、倒出、按压、涂抹等产品交互时，同时读取 [product-actions.md](#src-seedance-tvc-director-references-product-actions-md)，先确定真实结构、受力链和可靠替代方案。
11. 交付前始终读取 [delivery-and-qc.md](#src-seedance-tvc-director-references-delivery-and-qc-md) 并执行检查。
12. 需要查看完整输出形态时读取 [examples.md](#src-seedance-tvc-director-references-examples-md)。

### 时长选择

#### 15 秒精炼模式

选择 15 秒，当创意可由一个钩子、一个产品触发、一个证明和一个品牌收束讲清；优先使用单一场景和一条主要视觉变化，再按节奏选择克制 3 至 5 镜、标准 5 至 7 镜、快节奏 7 至 10 镜。适合产品 hero film、单卖点演示、短促 launch cut 和社媒横竖版主片。

#### 30 秒丰富模式

选择 30 秒，当需求包含人物关系、使用仪式、世界观建立、情绪转折、多个产品证明，或明确要求展示 Seedance 的 30 秒长时叙事能力。使用 5 至 7 个叙事模块组织故事，但按用户选择的节奏档位展开实际镜头：快节奏商业版约 14 至 18 镜、默认目标 16 镜；标准商业节奏约 11 至 14 镜；克制电影节奏约 8 至 10 镜。模块负责截止时间和新信息，不等于镜头数，也不等于生成段数。每 4 至 6 秒增加新的故事或商业信息；镜头越多，越要保证每镜只有一个主要动作、可读完成态和明确衔接，不能机械碎切。先判断采用 1、2 或 3 个因果相连的场景：连续产品仪式可留在单场景；需要反差、关系变化、使用情境或长时能力展示时优先 2 至 3 个场景。至少形成五种有控制的视觉层次，例如：环境建立、人物/产品互动、材质微距、机制隐喻、结果画面、hero shot。保持统一的产品锁、色彩逻辑和导演意图，不能把“丰富”写成无关场景堆砌。

#### 自定义时长模式

严格采用用户指定总秒数，不把自定义时长强行取整为 15 秒或 30 秒。先核对当前平台可用模型和单次生成上限，优先寻找能单段完成目标时长的合格模型；只有用户指定模型无法单段完成、平台没有合格模型或用户主动选择多段时，才拆成多个独立生成段并提供剪辑接口。按总时长重新分配钩子、中段新信息和品牌收束：少于 3 秒时从第一帧同时完成钩子、产品识别和品牌记忆；达到 3 秒及以上时仍先完成前三秒钩子；较长版本保持每 4 至 6 秒增加新信息。

总时长达到 3 秒时，先在 0–3 秒交付一个与产品或核心主张直接相关的强钩子。禁止用城市空镜、慢速环境建立、人物起床/回家、纯氛围光影或 Logo 淡入占满前三秒。30 秒和较长自定义版本采用“先给异常/结果/欲望，再解释世界与因果”的广告顺序。

用户未指定时长时，在同一次配置确认中提供 `15 秒 / 30 秒 / 自定义秒数`，同时标出推荐项。用户要求由 Agent 决定时再按上述规则自动选择。

### 工作模式

#### 创意提案

用于 brief 尚未锁定方向。交付 3 条路线，每条包含：

- 一句话创意；
- 消费者感受或认知变化；
- 开场视觉钩子；
- 产品如何成为故事因果，而不是贴片；
- 品牌揭示和 endboard 方式；
- 所选视频模型的可执行性与主要风险。

确保三条路线的叙事机制不同，不得只更换场景、色调或摄影风格。

#### 导演执行

用于方向已经选定。交付 treatment、时间结构、镜头表、声音设计、品牌资产处理和一条适配所选视频模型、可独立复制的提示词。

#### 提示词诊断

用于已有提示词。先指出最多 7 个最影响结果的问题，再给完整重写版。优先处理目标冲突、动作密度、参考素材职责、产品变形、时间超载和品牌交付风险，不要靠追加形容词修复。

#### 成片复盘与重试

用于用户返回生成视频或截图。先用全片等间隔抽帧建立镜头地图，再对失败动作高频抽帧，并测量实际硬切与转场边界；区分成功层与失败层，输出 `保留项`、`唯一主修层`、`重试指令`。人物不符合品牌调性时，只修改选角、造型、表演、空间或灯光中被证据指向的层，不自动推翻产品外观、时长结构、旁白和已经成功的镜头。

### 输出契约

默认按以下顺序输出；用户明确只要其中一项时缩减交付。

1. `Brief 判断`：列出已知信息、保守假设和 `【待补】`。
2. `生成配置`：分别写明 `时长：15 秒/30 秒/自定义秒数`、`声音：有旁白/无旁白/同时生成两套完整版本`、`生成方式：直出/九宫格`、`视频模型：推荐/用户指定`、`生成段数：单段/多段/自动`、`节奏与镜头密度：快/标准/克制/自定义镜头数`，以及当前平台能力快照和各自理由。
3. `选角与品牌气质`：有人物时写明目标年龄感、当代能量、造型、表演和 beauty lighting；没有人物时省略。
4. `核心策略`：受众、商业目标、单一核心主张、产品证明和期望感受。
5. `创意路线`：未选方向时给 3 条；已选方向时说明采用哪条及原因。
6. `前三秒钩子`：单独写明第一帧、0–3 秒事件、声音冲击和它如何连接产品主张。
7. `导演执行单`：一句话创意、视觉规则、表演、摄影、光线、声音、产品与品牌出现规则；多世界或高密度接力片同时写场景锚、单向光色弧线、全局运动向量与声音契约。
8. `时间轴/镜头表`：每个段落写清画面事件、镜头观察、声音变化和商业任务。
9. `可复制提示词`：放进一个独立代码块，只包含可执行指令，不混入分析说明。
10. `后期与交付`：列出 Logo、字幕、法务小字、精确包装字样、endboard 等应在后期完成的项目。
11. `风险与可调旋钮`：只保留 3 至 5 个真正会改变结果的变量。

### 核心约束

- 让产品参与故事因果；删除不服务主张的漂亮镜头。
- 一个镜头只承担一个主要叙事动作和一个主要商业任务。
- 用可见动作、物理反馈、机位关系、光源和声音描述质感，少用“高级、震撼、大片感、8K”等空词。
- 明确每份参考素材负责和不负责的维度；不要凭空创造 `@图片`、`@视频`、`@音频` 编号。
- 用户要求九宫格分镜时，画面内部不得出现镜号、数字、时间码、面板标题或其他索引文字。默认按从左到右、从上到下理解为第 1 至第 9 格；编号与逐格说明只写在图片外的分镜表中，不把它们绘制进参考图。
- 直出与九宫格是生成方式，不得与时长或声音绑定。直出释放节点间运镜与转场；九宫格先预览并等待用户确认，再编译视频提示词。
- 九宫格生图使用当前 Agent 已提供的最高优先级原生生图能力，不硬编码供应商或猜测未公开的模型名；没有可调用生图能力时只交付生图提示词并明确未渲染。
- 锁定产品轮廓、比例、材质、颜色、标签方向、开合状态和持有关系；需要精确复现时使用真实产品素材。
- 不依赖生成模型准确生成 Logo、包装小字、价格、免责声明或复杂中文排版；将其列入后期。
- 不保证模型能力、平台限额或生成效果。涉及当前能力和参数时先核对用户实际使用的平台版本。
- 不把某个模型的单次时长上限外推为整个平台上限。15 秒默认推荐当前平台满足任务条件的性价比最优模型并优先单段；30 秒在当前入口可用 Seedance 2.5 且确认支持原生 30 秒时，默认推荐 Seedance 2.5 单段完整生成，不因 Seedance 2.0 的 15 秒能力自动拆成两段。
- 视频模型与生成段数由用户独立选择。组合不可执行时说明冲突并提供替代方案，不得静默换模型或静默拆段。
- 保持最终提示词自然、紧凑、无内部解释；不要把整份策略报告复制进提示词。
- 30 秒模式必须增加新的画面信息、产品关系和声音递进；不得重复同一个液滴、旋转或人物动作来填满时长。
- 叙事模块不等于有效镜头，更不等于生成段数。30 秒直出提示词用 5 至 7 个模块规定故事阶段，同时必须按已选密度写出计划镜头数和每模块镜头数；不得只交付 6 个时间段后期待模型自行补出 16 镜。
- 快节奏 30 秒片通常为 14 至 18 个有效镜头，默认目标 16 镜；标准为 11 至 14 镜；克制为 8 至 10 镜。镜头多不等于机械闪切，每镜仍需新信息、单一主要动作、可读完成态和明确接口。
- 最终 packshot 之外，低运动镜头若超过约 2 秒必须出现第二个可见状态、有效主体运动或新的商业信息；两个承担相同任务的低运动人物氛围镜头不得连续出现。若连续人物镜头都只提供凝视、倒影、微笑或缓慢转身，合并其中一个或替换为新的产品/故事证明。
- 快切不得剪掉动作完成态。为关合、触碰、放下、入口、破裂、落下等关键动作写出可读结束状态，并在切镜前保留约 0.15 至 0.35 秒，或让下一镜第一帧清楚继承结果；镜头数量达标但观众看不见动作完成，仍视为失败。
- 区分动态 `hero reveal`、包装识别 `packshot` 与平面 `endboard`。有标准包装的产品若连续使用 hero reveal 与 packshot，将其合并为一次“动态进入完整产品 → 稳定识别”的品牌收束，并写明最早出现时间；鲜食、餐饮或服务品牌可用结果 hero 接 1 至 2 秒获批 endboard，不得虚构不存在的包装。品牌旁白开始不等于立即切入 packshot。
- 把前三秒的核心动作和视觉异常视为已消耗的创意资产；后续不得用相同主体、动作、景别和叙事功能再次呈现，除非结尾完成意义不同的回收。
- 把钩子写成正在发生的事件，不把孤立产品陈列误当成事件；第一帧应提供最低限度的情境、欲望或行动方向，并让观众能说出一个尚未回答的问题。
- 不在同一镜头同时要求精确品牌正面、复杂手部操作和强特效；产品交互优先保证结构与动作，packshot 另镜完成品牌准确展示。
- 群像先锁定精确人数、从左到右的座位表和相邻人物差异；多人动作镜头最多让两名角色同时成为动作主体，禁止未声明人物或画外手穿过他人身体区域。
- 多人围桌不能只用屏幕从左到右顺序描述；先声明桌型、相机方位、近左/远左/远右/近右座位、视线和每人的伸手扇区。需要正面看清四张脸和中央产品时，优先开放 U 形或低矮椭圆/长方桌，不让四人均匀围满圆桌后同时扭头面向相机。
- 前三秒必须已经发生值得继续观看的事，并让观众看到产品、产品质地、产品造成的结果或与核心主张直接相关的视觉异常。
- 不得默认“高端产品片等于无旁白”。旁白选择必须显式可见，并由用户确认或被标注为可逆假设。
- 有旁白时使用单一旁白真源：每句都有唯一 VO ID、唯一开始/硬停止时间和默认 `repeat_count=1`；到点后禁止重启、回声、改写复述或跨场景续念。要求商业文案逐字准确时，优先把生成音轨当导引轨并在后期替换正式配音。
- 30 秒有旁白商业片要同时检查旁白覆盖和注意力接管。约 4–23 秒不得连续超过约 4 秒既没有信息性人声，也没有带来新产品证明、人物决定或关系推进的强视听事件。旁白空窗超过约 2.5 秒时，逐段写明接管事件；普通切镜、持续背景音乐、重复入口和通用微笑不算接管。不要用无新信息的文案填满全片，也不要把全部产品信息挤在前 13 秒和最后落版。
- 食品广告不得用包装文字或旁白代替味道表现。具体风味是卖点时，至少用真实产品证据、烹饪联想、光色/声音翻译和人物余味中的三层建立证据链；关闭声音并遮住文字后，仍应能大致识别风味类别。
- 先按叙事价值给动作分级。推盘、递碗、摆放、等待、移杯等物流动作若不承担冲突、仪式或关系反转，单次控制在约 0.6 至 1.2 秒，不设为独立长镜头，也不与另一个低幅度桌面动作连续占据数秒。低运动画面与旁白空档重叠超过约 2.5 秒时，优先删减或合并动作，不用音乐掩盖节奏谷。
- 人物反应必须有可见触发。每位首次承担风味、功效或情绪结果的角色，应在同镜头或前约 0.5 至 1 秒内完成入口、接触、听见、看见等因果动作；不能让未接触产品的人直接闭眼微笑、惊讶或大笑。相同产品动作只有在更换角色后提供新的因果证明或关系推进时才允许再次出现，不能把“反重复”误写成删除必要触发。
- 保护 `触发 → 特异微反应 → 决定/关系兑现` 的连续性。普通反应特写默认约 0.8 至 1.2 秒；持续更久时必须出现可见状态变化。不得在触发与兑现之间插入 packshot、无关产品陈列或另一条叙事线。
- 有旁白时，主旁白清单之外禁止出现引号包裹的潜台词、角色可朗读句、口号或类似对白的完整措辞；“用眼神表达某句话”也会造成声音泄漏。画面段落只写关系状态和可见动作，任何可能被念出的文字都必须分配唯一 VO ID 或删除。
- 不得用“约30岁女性”代替选角指导；数字年龄必须与可见年龄感、现代造型、表演能量、空间美术和灯光共同定义。

---

<a id="src-seedance-tvc-director-references-ad-hook-md"></a>

## `seedance-tvc-director/references/ad-hook.md`

## 0–3 秒广告钩子

### 硬门槛

所有时长达到 3 秒的 TVC 都先设计前三秒。少于 3 秒的自定义 TVC 从第一帧同时完成触发、产品识别和品牌记忆，不机械套用完整三秒结构。常规前三秒必须完成四件事：

1. 第一帧已经处于动作、决定、反应或冲突之中，并提供最低限度的情境锚点；不要让产品孤立地等待事件开始；
2. 前 0.7 秒发生触发，前 2 秒发生决定性事件，三秒内形成明显不同的结束状态；不得把前两秒用于静止持有、等待、慢推或普通展示；
3. 观众能用一句话说出“接下来我想知道什么”，例如谁会得到、为什么突然停下、产品如何造成结果；
4. 该事件直接由产品、质地、声音、使用结果、受众痛点或核心主张触发。

先给注意力事件，再补充世界和原因。30 秒长度只能增加解释、证明和情绪，不得降低开场效率。

### 可用钩子类型

| 类型 | 开场方法 | 适用场景 |
|---|---|---|
| 产品异常 | 产品打破空间、尺度或物理预期 | 高端产品、科技、汽车、美妆 |
| 感官微距 | 第一帧直接进入液体、材质、声音或触感的极致瞬间 | 食品、饮料、护肤、香水 |
| 感官打断 | 产品声、气味或触感突然打断一个可识别的正常情境 | 食品、饮料、数码、家电 |
| 未完成动作 | 从争夺、递交、即将发生的使用或选择开始，在结果前切走 | 零食、饮料、服务、生活方式 |
| 结果先行 | 先展示令人好奇的结果，再回到产生结果的产品动作 | 功能型产品、生活洞察 |
| 痛点打断 | 在熟悉痛点发生到一半时让产品介入 | 家电、数码、日化 |
| 视觉矛盾 | 同一画面出现不可能并存的状态 | 概念广告、品牌世界观 |
| 人物瞬间 | 直接从决定、反应、失误或关系转折开始 | 情绪叙事、服务品牌 |

### 禁止的伪钩子

- 城市航拍、建筑外景、日出日落或空房间持续两三秒；
- 人物慢慢走进房间、坐下、回家、醒来或准备开始；
- 产品在黑暗中缓慢显形但没有事件；
- 单个产品或食物被居中夹持、悬浮或陈列一两秒，随后才破裂、发光或打开传送门；
- 不知道是谁、在哪里、为什么现在发生的孤立视觉异常；
- 只有“电影感”灯光、粒子、烟雾和慢推；
- 先放 Logo 或 slogan，却没有视觉问题和变化；
- 与产品无关的猎奇画面，后面再强行解释。

### 判断钩子是否成立

用一句话复述：`第一帧看到____；三秒内____发生；这件事让人想知道____，并指向产品的____。`

如果无法填完，重新设计。去掉品牌名后仍可用于任何产品的通用“高级画面”，不算有效钩子。

再做一次“动机检查”：

- 谁正在做什么，或什么正常情境刚被打断？
- 观众为什么要关心这个动作是否完成？
- 产品为什么在此刻出现，而不是被导演摆到画面中间？
- 后续哪一段会兑现前三秒建立的欲望、问题或结果？

无法回答时，即使画面反常、首尾帧不同，也只是形式钩子。优先改为从动作中间开始、感官打断、人物反应或结果先行。

#### 开场动作延迟检查

把第一秒写成连续动作，不写“先展示主体，然后在 0.4 秒开始”。Seedance 可能把展示状态延长到两秒。使用“第一帧动作已经开始”“0.3 秒前完成触发”等明确指令，并禁止静止持有超过 0.5 秒。

同时做“完成态检查”：快切不能在观众尚未看见结果时离开动作。关电脑必须短暂看见屏幕熄灭或盖子闭合，开盖必须看见盖子脱离，触碰必须看见接触已经发生。把结束状态保留约 0.15 至 0.35 秒，或让下一镜第一帧继承该结果。未完成动作可以作为有意悬念，但必须由下一镜立即回答；不能因为追求前三秒镜头数量而无意截断。

#### 产品异常的使用边界

产品异常只有在观众理解它为什么值得关注时才成立。孤立物体破裂、放大、悬浮或打开异世界，若没有受众欲望、现实冲突或后续因果，不得作为默认商业钩子。食品优先评估感官打断、人物瞬间或未完成动作，再考虑纯产品异变。

再做一次“首尾帧差异检查”：0 秒帧和 3 秒帧在主体状态、尺度、空间关系或人物决定上是否有一眼可见的差异。只有颜色变红、镜头推近、普通液滴落下或粒子增多，不足以单独构成强钩子。

把钩子的主要动作、核心景别和视觉异常登记为已使用资产。中段不得再次用同一主体完成同一动作来承担相同的食欲、质地或情绪任务；需要回收时改变叙事意义和构图。

### 30 秒接法

前三秒钩住后，按顺序完成：

`钩子 → 扩展情境 → 产品因果 → 证明/体验 → 情绪或功能兑现 → 品牌收束`

后续镜头必须回答开场提出的问题。不要在 3 秒后丢弃钩子、改讲另一支广告。

---

<a id="src-seedance-tvc-director-references-brief-and-concept-md"></a>

## `seedance-tvc-director/references/brief-and-concept.md`

## Brief 与创意路线

### 1. 提取最小可用 brief

按以下顺序提取信息：

| 字段 | 判断问题 | 缺失处理 |
|---|---|---|
| 品牌与产品 | 广告具体卖什么 | 不能判断时询问 |
| 受众 | 谁需要改变认知或行动 | 采用最窄合理人群并标注假设 |
| 商业目标 | 建认知、推新品、讲卖点、促行动还是改印象 | 不能混写多个同权目标 |
| 单一核心主张 | 看完只记住哪一句 | 压缩成一个可复述判断 |
| 产品证明 | 什么画面或事实让主张可信 | 无证据时写 `【待补】` |
| 必露元素 | 产品、包装、Logo、口号、人物、场景、法务 | 未提供素材时标注交付风险 |
| 禁区 | 不能说什么、不能拍什么、竞品与合规边界 | 未知时采用保守表达 |
| 规格 | 15 秒、30 秒或自定义秒数；画幅、语言、渠道 | 按 [generation-modes.md](#src-seedance-tvc-director-references-generation-modes-md) 合并确认缺失配置；用户要求 Agent 决定时给出可逆推荐 |

把功能清单压缩为一个主张。其余功能只能成为证明或镜头细节，不能抢占主叙事。

### 2. 形成策略句

使用内部公式思考，但不要机械展示公式：

`让[受众]在[具体情境]中相信[单一核心主张]，因为[可视化产品证明]，最终感到[目标感受]。`

检查：去掉品牌名后，如果任何同类产品都能使用这句话，策略仍然过泛。

### 3. 生成三条真正不同的路线

从下列机制中选择三种，不要重复：

1. `产品演示`：用清晰因果展示产品如何改变结果。
2. `生活洞察`：从受众熟悉但未被说破的瞬间切入。
3. `视觉隐喻`：把抽象卖点转化为一个持续发展的物理世界。
4. `反差反转`：先建立错误预期，再由产品完成意义翻转。
5. `情绪叙事`：产品成为人物关系或情绪变化的触发器。
6. `感官放大`：围绕材质、声音、口感、触感或速度建立体验。
7. `品牌世界观`：建立只能属于该品牌的一套行为和视觉规则。

每条路线必须回答：

- 第一秒看到什么；
- 第一帧正在发生什么，而不是陈列什么；
- 观众会继续看，是为了得到哪个尚未给出的答案；
- 产品何时、为何出现；
- 哪个画面承担产品证明；
- 结尾如何把记忆归还品牌；
- Seedance 执行时最容易失败在哪里。

### 4. 选择方向

按五项进行简短判断：

- 主张清晰度；
- 品牌专属性；
- 产品因果性；
- 目标时长内可讲完程度；
- Seedance 可执行性。

不要伪造精确分数。用高/中/低或一句证据判断即可。用户未选择但要求直接完成时，选择产品因果最清楚、素材依赖最少的一条。

---

<a id="src-seedance-tvc-director-references-casting-and-beauty-direction-md"></a>

## `seedance-tvc-director/references/casting-and-beauty-direction.md`

## 选角与 Beauty Direction

### 先定义品牌气质

人物不是中性素材。先把品牌气质翻译成可见信号：

- `年龄感`：观众感知的年龄区间，不只写身份证年龄；
- `能量`：清醒、松弛、锋利、亲密、活跃、理性或沉静；
- `时代感`：当代极简、未来科技、经典奢华、生活纪实等；
- `亲近度`：明星感、编辑感、真实消费者感或专业人士感；
- `市场语境`：地区、语言和文化审美，但不靠刻板印象推断外貌。

如果用户没有提供，提出一个明确推荐并标注可调整。不要默认抗老产品必须使用更成熟、端庄、保守的女性形象。

### 锁定选角

至少写清：

1. 性别呈现和文化背景；
2. 目标视觉年龄感，例如“27–32 岁感”，而不是只写“约30岁”；
3. 面部与皮肤方向：自然纹理、健康状态、妆感和光泽，不承诺功效；
4. 发型：长度、结构、蓬松度、分缝和运动感；
5. 服装：版型、材质、颜色和是否像家居服/职业装/礼服；
6. 表演能量：眼神、呼吸、动作速度、微表情和姿态；
7. 跨镜头一致性：脸、发型、服装、手部和年龄感不漂移。

三人以上群像不要只复制同一审美模板。读取 [ensemble-continuity.md](#src-seedance-tvc-director-references-ensemble-continuity-md)，为相邻人物建立脸型、发型、服装轮廓、明度和姿态差异，并锁定精确人数与座位顺序。

“年轻、漂亮、高级、精致”不可作为唯一选角指令。这些词容易让模型回到通用美妆模板。

### 避免无意产生传统成熟感

当目标是当代、轻盈、都市和有生命力时，避免同时堆叠：

- 深色丝质睡袍或保守套装；
- 厚重长卷发、贴头皮中分或过度定型发型；
- 全程闭眼、缓慢按压、端坐、无表情；
- 暖黄台灯、木饰面、古典梳妆镜和完全中轴对称构图；
- 低照度侧光、深眼窝阴影和过暖肤色；
- 反复强调“成熟、经典、优雅、抗老”。

不要在负面提示词中使用贬损年龄的表达。改为正向定义目标选角，并排除造成错调性的造型、表演和灯光组合。

### 当代高端美妆方向

可按品牌 brief 选择，不要机械套用：

- 视觉年龄感清楚且与目标受众相关；
- 现代利落发型或自然轻盈的头发运动；
- 低饱和中性色、简洁剪裁、非传统睡袍的现代服装；
- 清透轻妆、自然皮肤纹理、清楚眼神高光；
- 动作短、准、有目的，避免仪式性拖慢；
- 不对称构图、玻璃/金属/现代城市材质；
- 中性柔光加冷暖分离，以琥珀色作为产品强调，而非把全脸染暖。

### Beauty Lighting

- 使用柔和正面主光和轻微顶部轮廓光，保留眼神光；
- 控制低位暖光和强侧光，避免无意加深眼下、法令区和手部纹理；
- 近景使用自然透视的中长焦感，避免过广角贴脸；
- 皮肤保留真实纹理，不磨皮成塑料，也不额外强调纹路；
- 人脸肤色保持中性，琥珀金只作为局部反射和产品色。

### 成片复盘

用户返回成片时按层诊断：

1. `选角`：视觉年龄感、脸型与品牌亲近度；
2. `造型`：发型、妆面、服装是否共同指向错误年代或人群；
3. `表演`：是否过慢、过于肃穆、持续闭眼或缺少清醒能量；
4. `美术`：空间是否像传统卧室、酒店或旧式梳妆台；
5. `灯光/镜头`：是否因暖黄低照度、正中构图或焦段放大成熟感。

先列出应保留的成功层，再选择影响最大的一个主修层。重试时明确“全片其他结构保持不变”，避免模型连带改坏产品、镜头和声音。

---

<a id="src-seedance-tvc-director-references-delivery-and-qc-md"></a>

## `seedance-tvc-director/references/delivery-and-qc.md`

## 交付与质量检查

### Brief 真实性

- 是否区分用户事实、合理假设和 `【待补】`？
- 是否没有编造销量、效果、认证、用户评价、实验数据或竞品结论？
- 单一核心主张是否只有一个？
- 产品证明是否能被画面看见，而非只靠旁白宣称？

### TVC 判断

- 时长、声音、生成方式、视频模型、生成段数、节奏与镜头密度是否作为六个独立选项确认，没有互相偷换？
- 是否记录当前平台能力快照，并先按时长、素材、声音和质量过滤模型，再比较价格、重试与后期成本？
- 15 秒未指定模型时，是否推荐当前平台满足任务条件的性价比最优模型，而不是硬编码永久答案？
- 30 秒且当前入口可用 Seedance 2.5 原生 30 秒时，是否默认推荐一条 Seedance 2.5 单段提示词，没有沿用 Seedance 2.0 的 15 秒上限自动拆段？
- 自定义时长是否写明准确秒数，并先寻找能单段完成的合格模型，再决定是否分段？
- 用户指定模型与段数后是否予以保留；组合不可执行时是否说明冲突并让用户选择，而不是静默换模型或拆段？
- 第一秒是否有明确画面，而非抽象气氛？
- 第一帧是否已经开始动作、决定、反应或冲突，而不是孤立产品居中等待？
- 前 0.7 秒是否发生触发，是否避免静止持有或普通展示持续到约 2 秒？
- 观众是否能说出一个继续观看才能得到答案的问题？
- 产品是否是开场事件的原因，而非被摆在中央后用破裂、发光或传送门强行制造异常？
- 0–3 秒是否发生一次可见变化，而不是只有空镜、慢推或产品显形？
- 0 秒与 3 秒的主体状态、尺度、空间关系或人物决定是否有一眼可见的差异，而非只改变颜色、粒子或镜头距离？
- 前 2 秒是否已经发生决定性事件，钩子是否没有把普通液滴、挑起或慢动作误当成足够强的冲击？
- 前三秒是否已经连接产品、质地、结果、痛点或核心主张？
- 30 秒版是否先钩住再建立世界，而不是把前三秒用于铺垫？
- 产品是否参与因果，而非最后突然贴片？
- 每个镜头是否只有一个主要动作和一个主要商业任务？
- 每个关键动作是否在切镜前出现可读完成态，或由下一镜第一帧继承结果，没有为了快切而截断关合、接触、落下、入口或人物决定？
- 结尾是否回收品牌、主张和行动信息？
- 删除任一漂亮镜头后，如果策略不受影响，该镜头是否应被删除？
- 是否明确说明选择 15 秒、30 秒或自定义秒数的理由？
- 30 秒版是否每 4 至 6 秒增加新信息，而不是重复 15 秒版动作？
- 30 秒时间轴是否区分了 5 至 7 个叙事模块、实际有效镜头、生成段数与九宫格关键帧，没有把 6 个模块自动写成 6 个长镜头？
- 是否明确记录用户选择的节奏档位或准确镜头数：快节奏 14 至 18 镜、标准 11 至 14 镜、克制 8 至 10 镜，或自定义？
- 快节奏版是否把目标镜头数和每模块镜头数写入最终提示词，而不是只写“节奏快、快速剪辑”？
- 使用 14 镜以上时，每镜是否提供新信息、单一主要动作、可读完成态和明确交接，而非机械碎切？
- 30 秒版是否至少包含五类画面层次，同时保持统一世界和产品锁？
- 用户要求丰富度或展示长时能力时，是否真正使用 2 至 3 个因果相连的场景，而非同一桌面换景别和特效？
- 钩子的主要动作、景别和视觉异常是否没有在中段按同一功能重复？
- 每段是否有一个其他段没有提供的新信息和唯一核心动作？
- 每次转场是否在约 1 秒内完成并按计划时间进入目标场景，而不是持续漂浮、隧道穿越或慢 morph？
- 转场桥中是否没有超过约 0.3 秒的空白或近纯色无主体帧，目标场景是否在桥接元素消失前建立？
- 被称为“转场”的风味/机制镜头是否实际占据数秒；若是，是否已按正式场景重新预算？
- 两个以上世界交替时，是否分别写明地点时间、真实光源、背景证据、色彩状态、行动目标、环境声床和防串场项？
- 旅程段是否锁定全局屏幕方向；若发生反向，是否通过正面、静止或可见转身镜头明确重置？
- 跨世界形状/材质匹配是否同时定义源镜最后状态和目标镜第一帧，而非只写“蒸汽变成云”等抽象结果？
- 推盘、递碗、摆放、移杯、等待等物流动作是否没有被误当作独立剧情，普通单次是否控制在约 0.6 至 1.2 秒？
- 是否避免两个低幅度桌面动作连续占据数秒，例如“推过去—等待—再拿起来”？
- 任意约 2.5 秒窗口是否至少包含新信息、状态变化、有效主体运动、镜头变化或新的声音事件；若没有，是否属于有视觉张力的刻意静默或packshot？
- 最终 packshot 之外，低运动构图是否在约 2 秒内出现第二状态或换镜，没有让悬停液滴、单次涂抹、静态凝视或轻微光变占满整个模块？
- 是否没有连续安排两个只承担凝视、倒影、微笑、慢转身等同一任务的人物氛围镜头？
- 低运动画面是否恰好落在两句旁白的长空档中；若是，是否先删减画面而不是用更多旁白填满？
- 每位首次承担产品结果的角色，是否在同镜头或前约 0.5 至 1 秒内拥有可见触发，而不是未经入口/接触就直接表演？
- 单一反应特写是否通常控制在约 0.8 至 1.2 秒；更长镜头是否包含明确的第二状态，而不是持续闭眼、微笑、张嘴或等待？
- `触发 → 特异微反应 → 决定/关系兑现` 是否连续，是否没有被 packshot 或无关产品陈列从中切断？
- 反重复规则是否没有误删新角色所需的最小因果动作；重复动作是否确实提供新角色、新证明或新关系信息？

### 旁白与声音

- 用户是否明确选择有旁白、无旁白或同时生成两套完整版本？
- 未指定时，是否给出推荐理由并把选择交给用户，而非默认无旁白？
- 旁白是否增加画面之外的信息，而不是逐句解说动作？
- 旁白中的功效、数据、成分和绝对化表述是否有获批依据或标为 `【待补】`？
- 是否标注旁白进入、停顿和结束位置，并为产品声和品牌尾音留白？
- 是否完成实际朗读计时？
- 30 秒有旁白版是否测量约 4–23 秒最长的信息性人声空窗，而不是只检查总字数？
- 任一超过约 2.5 秒的旁白空窗是否标注了新的产品证明、强动作/产品声、音乐结构变化、人物决定或关系兑现来接管注意力？
- 是否不存在连续超过约 4 秒既无信息性人声又只有重复品尝、普通切镜、持续背景音乐或通用微笑的中段区间？
- 约 13–23 秒若承担第二轮体验或分享，是否至少包含两个功能不同的信息节拍，并避免把全部产品信息挤在前 13 秒与最终落版？
- 是否只有一张主旁白清单，旁白原文没有在镜头段落或声音总结中再次完整粘贴？
- 每句是否有唯一 VO ID、确定的开始/硬停止时间和默认 `repeat_count=1`？
- 是否明确禁止硬停止后的重启、回声、复述、改写和跨场景续念，并让 30 秒片尾至少留约 1 秒无旁白尾音？
- 主旁白清单之外是否不存在引号包裹的潜台词、角色可朗读句、口号或 `用眼神表达某句完整的话`？
- 商业文案需要逐字准确时，是否把生成旁白视为 guide VO，并安排独立配音/后期替换与转写核对？
- 同时生成两套完整版本时，是否分别调整声音和镜头节奏，而不是机械删除音轨？
- 成片转写若出现清单外句子，是否反查并删除提示词中相同或近似的可朗读措辞，而不是只追加“无对白”？
- 是否为每个世界定义持续环境声床，并保证段内切镜后不重启？
- 音乐是否写明第一次进入、展开、峰值、收束和归静，而不是每镜重新开始？
- 关键声音先行切是否标明提前量、源声音退出与目标声音接管，且只用于少数重要切点？

### 食品风味

- 是否区分物理口感与具体味觉/香气，没有把“薄脆”误当作“奶香、焗烤、辛辣”等风味证明？
- 风味是否至少通过真实产品证据、烹饪联想、光色/声音翻译和人物余味中的三层呈现？
- 复合风味是否形成有顺序的感官弧线，而不是把多个食材和特效同时堆在一个镜头？
- 风味是核心卖点时，是否分配 2 至 4 秒独立正式镜头，并在计划时间内结束？
- 烹饪、食材和产地画面是否有包装或获批资料依据，并明确属于风味联想而非成分/产地事实？
- 关闭旁白并遮住包装文字后，观众是否仍能大致识别风味类别，而且识别不只依赖通用金色灯光？
- 风味世界最终是否回到真实产品，没有让产品变成另一道菜、虚构夹心或违反原有物性？
- 每位承担风味反应的人物是否有自己的可见入口/接触原因，反应是否具有风味特异性而非通用闭眼微笑？
- 人物风味反应之后是否出现决定或关系结果，例如明明被辣到仍继续，而不是只有无意义表情蒙太奇？

### 选角与品牌气质

- 是否明确目标视觉年龄感，而不只写模糊数字年龄？
- 发型、妆面、服装、表演、空间和灯光是否共同指向同一品牌气质？
- 是否避免把“高端、经典、抗老”自动翻译为成熟保守、缓慢肃穆的女性模板？
- 当代美妆近景是否保留眼神光、中性肤色、自然纹理和轻盈造型？
- 是否避免深色睡袍、厚重长卷发、持续闭眼、暖黄台灯和古典梳妆镜同时出现，除非 brief 明确需要？
- 成片重试是否先列保留项，并只修改证据指向的选角/造型/表演/美术/灯光层？
- 三人以上群像是否写明精确人数、角色 ID 和从左到右座位表？
- 相邻同类型人物是否至少在脸型、发型、服装轮廓/明度、配饰或姿态中的三项明显不同？
- 多人镜头是否没有生成未声明的额外人物、重复脸或融合身份？
- 多人围桌是否声明桌型、相机方位、近左/远左/远右/近右座位、视线目标和各自伸手区，而不只写屏幕从左到右？
- 需要同时看清四张脸和中央产品时，是否采用开放 U 形或适合的椭圆/长方桌，而非四人均匀围满圆桌又同时面向相机？
- 食品桌面是否为素色无图案安全区，没有模型自创的桌游棋盘、额外 Logo 或抢画面的杂物？

### Seedance 执行

- 用户未指定生成方式时，是否解释直出强调自然运镜、九宫格强调可控与先审稿，并完成选择？
- 直出模式是否只锁必要商业节点，把节点间运镜和转场留给 Seedance，而不是逐镜过度控制？
- 30 秒直出模式是否同时给出计划镜头数、每模块镜头数、自然切镜许可与低运动停留护栏，而不是让“自由发挥”退化成每个时间节点一镜到底？
- 九宫格 9 个关键状态是否没有被误当成最终只能生成 9 镜；计划镜头更多时是否另有完整镜头表？
- 九宫格模式是否先交付预览并等待确认，再编译最终视频提示词？
- 九宫格实际生图是否使用当前 Agent 的原生优先能力，没有硬编码或猜测未公开的模型名？没有生图能力时是否明确只交付提示词、未实际渲染？
- 每个引用素材是否有唯一职责和排除项？
- 是否只引用用户真实提供的素材编号？
- 九宫格分镜是否默认按从左到右、从上到下阅读，并且图片内部完全没有镜号、数字、时间码、标题、字幕、箭头、图例、水印或其他索引文字？
- 九宫格的编号与逐格说明是否只存在于图片外的分镜表，而没有被绘制进 Seedance 参考素材？
- 产品外观、人物身份、道具归属和空间方向是否被锁定？
- 时间轴动作是否能在指定秒数内完成？
- 高密度接力镜头是否逐镜写明继承项、结束态和下一镜接口；未完成动作是否在下一镜第一帧同向同阶段接续并很快完成？
- 提示词总时长与所有时间段之和是否一致？
- 是否存在互相冲突的运镜、光线、画幅或风格要求？
- 结尾状态是否可用于下一镜或后期剪辑？
- Hero reveal 与 packshot 是否承担不同任务；相邻时是否已合并为一次动态进入完整产品后稳定识别的品牌收束？
- 对有标准包装、瓶体或设备正面的产品，是否写明并实测完整正面产品的最早出现时刻，没有因品牌旁白开始而提前形成超长 packshot？
- 鲜食、餐饮、原料或服务品牌没有标准包装时，是否使用结果 hero 加约 1 至 2 秒获批 endboard，而非虚构包装或强套瓶装产品预算？
- 包装开合、撕袋、按压、倒出等动作是否具有初始结构、锚定点、施力方向、材料反馈和明确完成态？
- 参考图看不清产品开口结构时，是否避免猜测并改用预开、声音桥、剪开或后期实拍？
- 是否避免在同一镜头同时要求精确包装正面、复杂双手操作、人物表情和强特效？
- 容器中的最后一件产品是否具有合理重心、支撑面和接触关系，没有窄边站立或悬浮？
- 机位是否能在真实遮挡关系下看到容器中的物体；否则是否改用高角度、浅盘或拆镜？
- 每只进入产品区的手是否能追溯到明确角色、左右手、袖口和身体方向？
- 多人手部动作是否使用固定机位，并避免同时推拉镜头、交换座位或增加人物？

### 商业资产

- 精确 Logo、包装小字、价格、CTA 和免责声明是否转交后期？
- 产品颜色、比例、材质和标签方向是否有真实素材依据？
- 需要精确 packshot 时，是否说明必须使用获批产品图或实拍素材？
- 未验证的生成产品是否被误称为可直接投放的最终资产？

### 输出质量

- 代码块内是否只有可执行提示词？
- 多个提示词是否各自独立完整？
- 是否避免“高级感、大片感、8K、完美”等空泛堆词？
- 可调旋钮是否不超过 5 个且真的改变结果？
- 是否明确哪些内容由 Seedance 生成、哪些由剪辑/调色/声音/平面后期完成？

任一关键项失败时先修复再交付。不要用“最终效果以实际为准”代替具体风险说明。

---

<a id="src-seedance-tvc-director-references-ensemble-continuity-md"></a>

## `seedance-tvc-director/references/ensemble-continuity.md`

## 群像身份与肢体连续性

### 控制群像复杂度

- 没有人物参考图时，复杂互动镜头优先控制在 3 至 4 人；5 人以上改为环境群像或拆镜。
- 写明精确总人数，未声明人物不得进入画面。
- 每个镜头最多让两名角色同时完成需要手部精度的动作，其余人物保持清楚但简单的反应。
- 不在多人伸手、递物或争抢时同时推拉、环绕或大幅改变景别；在复杂动作和复杂运镜之间只选一个。

### 建立身份差异矩阵

为每个角色分配稳定 ID，并至少定义：

| ID | 屏幕位置 | 性别呈现/年龄感 | 脸型与发型 | 服装轮廓与颜色 | 配饰/姿态 |
|---|---|---|---|---|---|

相邻、同年龄段、同性别呈现的人物至少在三个可见信号上明显不同：

- 脸部轮廓，例如圆润/修长/棱角；
- 发型轮廓，例如卷发/短寸/侧分/齐肩；
- 上装明度与结构，例如深绿夹克/奶油色针织/浅灰衬衫；
- 配饰，例如细框眼镜/耳饰，但不要只靠容易消失的小配饰；
- 体态与坐姿，例如前倾活跃/松弛后靠。

不要让相邻两名角色同时拥有相似黑色短发、相似脸型、相同年龄感、同色圆领上衣和相同坐姿。服装颜色不同但脸与发型几乎相同，仍不足以防止同脸。

### 锁定座位与屏幕方向

在时间轴前先写一行固定座位表，例如：

`画面左一 A → 左二 B → 中央 C → 右二 D；全场顺序不变。`

跨景别时保持：

- 人物左右顺序、邻接关系和朝向不变；
- 服装外层、袖口颜色和领口结构不变；
- 近景只保留全景中相邻的人物，不把远端角色突然移入中央；
- 推远或推近过程中不增加、删除、交换或融合人物。

### 多人桌面拓扑先行

屏幕从左到右的座位表只适用于近似同一景深的人物排布；围桌场景还必须声明相对相机的二维拓扑。先选择桌型和机位，再安排人物，不让模型自行补成圆桌合影。

#### 按镜头目标选择桌型

- 需要同时看清四张脸、中央食品和分享动作：优先 `开放 U 形座位 + 低矮椭圆桌或短长方桌`，相机侧留出缺口。
- 需要自然聊天和侧面关系：可用椭圆桌或长方桌 `2+2`，用正反打或相邻双人镜头覆盖，不强求一个正面全景看清所有脸。
- 真正圆桌只用于俯拍桌面、环绕建立或不要求全员正脸的场面。禁止四个人均匀围满圆桌，却又同时扭身面向同一台相机。
- 食品分享桌面使用素色、低反光、无图案材质；不要让生成模型补出桌游棋盘、餐垫拼花、额外 Logo 或抢夺注意力的杂物。

四人开放 U 形可按相机坐标书写：

`相机固定在 6 点钟方向；A 近左约 8 点钟、B 远左约 10 点钟、C 远右约 2 点钟、D 近右约 4 点钟；6 点钟近侧中央不坐人，作为相机和产品视线通道。`

同时写清：

- 每把椅子的朝向，人物是看相邻朋友、中央产品还是动作手，不要求所有人持续看镜头；
- 中央产品安全区，包装、碗碟和品牌面不被前臂遮挡；
- A/B/C/D 各自的桌面伸手扇区，手只在本人一侧进入并退回；
- 只有相邻两人可以同一时刻接近共享产品，不从桌子对面横跨整个画面；
- 全景、双人近景、俯拍插入和群像回收都保持同一邻接关系与服装袖口。

如果镜头既要求全员正脸、自然交谈、中央产品无遮挡，又要求多人同时伸手，先拆镜；不要把互相冲突的可见性任务塞给一个圆桌全景。

### 肢体归属锁

每个进入产品交互区的手都写明：

`角色 ID + 左/右手 + 袖口颜色/材质 + 从画面哪侧进入 + 接触目标 + 最终退回位置`

默认只允许当前镜头中脸和上半身可见的角色伸手。画外手只有在叙事必要时使用，并必须保留从对应身体方向连续进入的前臂和独特袖口；不得穿过另一人物的胸口、肩膀或身体轮廓。

当两只手同时接近同一物体时，使用固定机位。不要在此期间推远、升降或改变人物数量。需要群像反应时，先完成手部动作，再硬切到静态群像。

### 推荐拆镜

多人围绕小物体反应时使用三镜法：

1. `道具插入镜头`：高角度固定机位，只展示物体、容器和最多两只归属清楚的手；
2. `人物反应镜头`：相邻两人的静态双人近景，不出现画外手；
3. `群像回收镜头`：固定中景展示所有已声明人物，手已离开产品区域。

不要用一次连续推远同时完成小物体特写、两只手交互、人物对视和群像回收。

### 成片复盘

先比较全景座位表，再逐帧追踪动作手的袖口与身体连接。以下情况归为身份/肢体连续性失败：

- 相邻人物在脸型、发型、年龄感和服装上高度同质；
- 人数在推拉镜头中改变；
- 近景人物与全景座位顺序不一致；
- 手的袖口与镜头内人物服装不一致；
- 画外手穿过可见人物身体区域或找不到合理肩肘连接；
- 四人只挤在圆桌远侧半圈、近侧全空，像面向相机摆拍；
- 桌型或桌面纹样在切镜中变化，或出现与产品无关的棋盘、Logo 和杂物；
- 人物座位只能用屏幕左右解释，切到俯拍或斜侧机位后无法对应近左/远左/远右/近右位置。

重试时优先减少人数、固定机位或拆镜，不靠“每个人都不同”“手部正确”等泛化负面词修补。

---

<a id="src-seedance-tvc-director-references-examples-md"></a>

## `seedance-tvc-director/references/examples.md`

## 输出示例

以下示例只演示结构。品牌事实和产品证明必须来自用户资料。

### 示例一：15 秒产品演示型 TVC

#### Brief 判断

- 已知：新品降噪耳机，目标是通勤人群，15 秒横版。
- 假设：核心场景为早高峰地铁；成片以产品体验而非参数讲解为主。
- 待补：`【待补：获批产品图】`、`【待补：可公开使用的降噪表述】`、`【待补：品牌 Logo 与 endboard 文案】`。

#### 核心策略

让拥挤通勤者直观看见：戴上产品后，混乱没有消失，但注意力重新回到自己手里。

#### 导演执行单

- 一句话创意：列车噪声在耳机戴上的瞬间被重组为有秩序的节拍。
- 视觉规则：现实空间保持拥挤，变化只发生在声音、表演和微小光线节奏中。
- 产品规则：耳机必须使用获批参考图锁定外观；包装文字与 Logo 后期添加。

#### 镜头骨架

| 时间 | 画面与镜头 | 声音 | 商业任务 |
|---|---|---|---|
| 0–3 秒 | 拥挤车厢近景，人物被噪声包围 | 刹车、人声、提示音叠加 | 建立痛点 |
| 3–6 秒 | 手取出并戴上耳机，产品清楚可见 | 噪声快速收束 | 产品触发 |
| 6–11 秒 | 环境仍在运动，人物呼吸放松，镜头稳定 | 保留低频环境与干净节拍 | 体验证明 |
| 11–15 秒 | 耳机 hero shot 接获批 packshot | 产品提示音，音乐收束 | 品牌回收 |

最终输出还应包含一条独立完整的 Seedance 提示词和后期清单。

### 示例二：30 秒情绪叙事型 TVC

输入为饮料新品和“陪伴”主题时，不要直接写“温暖治愈”。先找到具体关系动作，例如父女深夜共同整理搬家纸箱；让开瓶、递出、共享饮用成为关系转折，再在最后 5 秒完成 packshot 与 endboard。

### 示例三：已有提示词诊断

若原提示词同时要求 15 秒内跨越五个国家、十次换装、连续一镜到底、每个场景都有产品微距和准确中文包装，应指出：

1. 时长与事件密度冲突；
2. “一镜到底”与大量跨地点切换冲突；
3. 产品特写与人物高速叙事争夺镜头时间；
4. 精确包装文字不应交给生成模型；
5. 缺少单一商业主张。

重写时保留一个地点、一个核心变化、一次产品证明和一个后期 endboard。

---

<a id="src-seedance-tvc-director-references-food-flavor-direction-md"></a>

## `seedance-tvc-director/references/food-flavor-direction.md`

## 食品风味可视化

### 区分口感与风味

食品广告先分开回答：

- `口感`：薄、脆、酥、糯、弹、稠、爆汁等物理反馈；
- `风味`：奶香、焗烤、辛辣、烟熏、酸甜、咸鲜、柑橘清香等味觉与香气联想。

只拍断裂、气泡、酱汁和入口动作，通常只能证明口感。把风味名写进旁白或包装字幕，也不等于画面已经表现味道。

### 建立风味证据表

写镜头前先完成：

| 风味层 | 已知事实 | 可见证据 | 声音/节奏 | 人物余味反应 | 风险边界 |
|---|---|---|---|---|---|

复合风味必须拆成有顺序的感官弧线，例如：

`清洁奶香的冷白与柔滑 → 烤箱暖金与轻微焦化 → 回到真实产品的干爽薄脆`

每一层都要在画面中承担不同功能，不能只换旁白形容词。

### 五层表达方式

至少选择三层，其中必须包含真实产品证据：

1. `真实产品证据`：表面调味、烘烤色、油润度、酱汁包裹、断面或气泡；不得改变产品真实物性。
2. `烹饪联想`：使用包装或获批 brief 已出现的食物意象，例如焗烤表面的金黄焦斑、奶油白内里；明确它是风味联想，不把它冒充成配料或产地证明。
3. `光色与运动翻译`：酸味偏锐利明亮，奶香偏柔和包裹，焗烤偏暖金焦化，辛辣偏快速上升；光色必须服务具体风味，不使用通用粒子。
4. `声音翻译`：脆裂、烤箱轻响、气泡、滋滋声、柔和低频或短静默；声音变化要对应入口前后层次。
5. `人物余味反应`：先感到口感，再出现风味余韵；用眼神、呼吸、眉眼放松或短促交流表现，不只给通用微笑。

### 风味反应的因果链

每位承担风味证明的人物都需要自己的最小触发，不能把一个人的入口动作当作全体人物反应的共同原因。

- 在反应同镜头或前约 0.5 至 1 秒，让观众看见该人物入口、闻到、接触或观察到产品结果。
- 辛辣反应优先写成短促的生理顺序：`眼睛迅速睁开 → 短促吸气或控制呼气 → 热感转为满足/继续取食的决定`。避免持续闭眼、长时间微笑、无方向张嘴或所有人同步表演。
- 普通反应特写控制在约 0.8 至 1.2 秒；若需要更长时间，必须包含至少两个连续状态。
- 只有在角色、因果信息或关系结果发生变化时才重复入口动作。为了证明第二个人也受到风味影响而安排一次简短品尝，属于新证据；重复同一个人的同类慢动作才是冗余。
- 先完成 `触发 → 反应 → 选择/关系结果`，再进入产品 hero shot。不要用包装特写把因果链切断。

### 风味 Hero Scene

当风味是核心卖点时，为它分配一个独立的 2 至 4 秒正式镜头或场景，写清开始、结束和新信息。不要把风味世界称作转场后让它漂浮十几秒。

- 复合风味优先用两个连续状态表现层次，不用一个混合画面同时堆满奶、芝士、火焰、雪山和薯片。
- 产品本体保持真实、干爽和受重力支撑；不要让薯片变成融化芝士、被虚构酱汁包裹或穿越食材隧道。
- 烹饪联想与真实产品镜头用形状、烘烤斑点、色温或声音匹配连接，普通桥接控制在 0.2 至 0.8 秒。
- 30 秒食品片让风味在至少三个位置递进出现：产品微距、独立风味镜头、人物余味或 packshot 环境；每次提供不同证据。

### 事实与联想边界

- 只有产品名、包装或获批资料支持的风味可以作为画面主张。
- 地名风味不自动等于真实产地或原料来源。没有证据时，不用牧场、奶牛、产地地图或“当地原奶”等画面暗示事实。
- 包装已经出现的菜肴或食材可作为 `风味联想`，但不得据此新增成分、营养、健康或工艺声称。
- 若参考图和资料无法判断实际调味外观，使用克制的光色与烹饪联想，不虚构可见粉末、夹心或酱层。

### 静音识别测试

交付前暂时关闭旁白、遮住包装文字和字幕，再问：

1. 观众能否大致区分这是奶香焗烤、辛辣、酸甜或烟熏中的哪类风味？
2. 识别来自至少两种互相支持的画面证据，还是只来自通用金色灯光？
3. 风味联想是否仍能回到真实产品，而不是变成另一道菜的广告？

任一答案为否，重写风味镜头。

---

<a id="src-seedance-tvc-director-references-generation-modes-md"></a>

## `seedance-tvc-director/references/generation-modes.md`

## 生成配置与跨 Agent 适配

### 六个独立配置轴

在创意和提示词编译前分别确认以下六项。不得用其中一项推断另一项，例如 30 秒不自动等于有旁白、九宫格、两个 15 秒生成段或固定镜头数。

1. `时长`：15 秒、30 秒或自定义秒数；
2. `声音`：有旁白、无旁白，或同时生成有旁白版与无旁白版；
3. `生成方式`：直出模式或九宫格模式；
4. `视频模型`：使用当前平台推荐模型，或由用户指定；
5. `生成段数`：单段完整生成、多段生成后剪辑，或按平台能力自动选择。
6. `节奏与镜头密度`：快节奏商业版、标准商业节奏、克制电影节奏，或自定义镜头数/平均镜长。

用户已明确的项目直接采用，只询问缺失项。缺失多项时合并成一次简短配置确认，每项先给一句推荐理由，不连续追问。用户明确要求由 Agent 决定或不要提问时，分别选择推荐项并标注为可逆假设。

推荐的询问方式：

```text
开始前确认六个互不绑定的选项：
1. 时长：15 秒 / 30 秒 / 自定义（请写秒数）；
2. 声音：有旁白 / 无旁白 / 同时生成两套完整版本；
3. 生成方式：直出 / 九宫格。直出更强调自然运镜和模型发挥；九宫格会先生成分镜预览，确认后再编译视频提示词，控制更强但约束也更多；
4. 视频模型：使用推荐模型 / 指定模型。推荐会读取当前平台可用列表，再结合时长、素材、声音、质量和成本判断；
5. 生成段数：单段完整生成 / 多段生成后剪辑 / 按平台能力自动选择。单段通常连续性更好；多段便于局部重跑，但增加人物、光色、声音和动作衔接风险。
6. 节奏与镜头密度：快节奏商业版 / 标准商业节奏 / 克制电影节奏 / 自定义镜头数。30 秒参考：快节奏约 14–18 镜（可按 16 镜执行），标准约 11–14 镜，克制约 8–10 镜。这里指成片镜头数，不是视频生成段数。
```

### 时长选择

- `15 秒`：一个主张、一个证明、单一动作链和紧凑品牌收束；
- `30 秒`：人物关系、使用仪式、多个互补证明、世界观或情绪递进；
- `自定义秒数`：严格按用户指定总时长重新分配钩子、中段信息和品牌收束，不套用 15 秒或 30 秒时间表。

时长确定后读取 [model-and-segmentation-routing.md](#src-seedance-tvc-director-references-model-and-segmentation-routing-md)，核对当前平台的模型列表与单次生成上限：

- 用户选择单段且在所选模型单次能力范围内：输出一条总时长准确的完整提示词；
- 用户主动选择多段：即使有模型可单段完成，也尊重其选择并按故事自然段拆分；
- 当前指定模型超出单次能力、但有其他模型可单段完成：先给“换模型单段”和“保留模型分段”两个选项，不静默拆段；
- 所有可用模型均超出单次能力：拆成多个可独立生成的段落并提供剪辑接口，不声称能够单次直出；
- 无法核对平台上限：明确标注平台能力待确认，不虚构模型、价格或上限。

时长小于 3 秒时，从第一帧直接完成钩子、产品识别和品牌记忆，不机械保留完整的 0–3 秒结构。时长达到 3 秒及以上时，仍把前三秒作为广告钩子；长片每 4 至 6 秒增加新信息。品牌收束时间按总时长成比例安排，同时保证产品能被稳定识别。

### 声音选择

- `有旁白`：交付一套含唯一主旁白清单的完整提示词；
- `无旁白`：交付一套用产品声、环境声、音乐和静默承担节奏的完整提示词；
- `同时生成两套完整版本`：一次交付有旁白版与无旁白版。两版共享核心创意和商业主张，但分别调整镜头停留、声音钩子和节奏，不能只从有旁白版删除音轨。

这三个选项彼此独立：任意时长和任意生成方式都可以搭配上述任一声音选择。

### 视频模型与生成段数

- `15 秒`：默认推荐当前平台满足任务条件的性价比最优模型，通常为单段完整生成；
- `30 秒`：当前入口可用 Seedance 2.5 且确认支持原生 30 秒时，默认推荐 Seedance 2.5 单段完整生成；
- `自定义秒数`：先寻找可单段完成的合格模型，再决定是否需要多段；
- 用户可以分别指定模型和段数。组合不可执行时说明具体冲突并提供可选替代，不静默覆盖用户选择；
- 不把直出/九宫格与单段/多段混为一谈：九宫格获批后也可以作为一个 30 秒单段生成的参考素材。

性价比推荐必须基于当前平台快照：先满足时长、参考素材、声音与质量硬条件，再比较积分/价格、预计重试和后期成本。未取得当前价格时，不宣称某模型“最便宜”。

### 节奏与镜头密度

读取 [pacing-and-shot-density.md](#src-seedance-tvc-director-references-pacing-and-shot-density-md) 后确定实际镜头数。用户给出准确镜头数或参考片时直接采用；未指定时根据渠道、品类、故事复杂度和参考气质推荐。普通 30 秒商业 TVC 不得把 5 至 7 个叙事模块直接输出为 5 至 7 个长镜头；除非用户明确选择克制长镜头，至少按标准商业节奏展开。

### 直出模式

直出模式不先生成视觉分镜，直接使用产品图、质感图、人物参考和商业 brief 编译视频提示词。

- 锁定核心主张、前三秒钩子、产品身份、关键因果、必要连续性和品牌收束；
- 使用少量必须发生的故事节点，不把每个节点重复写成精确构图、逐秒运镜和强制转场；
- 30 秒片先写 5 至 7 个叙事模块，再按已选密度为每个模块分配实际镜头数；节点规定事件截止时间，镜头表规定观看节奏；
- 把精确切点、具体运镜、自然表演和节点间短转场优先交给当前所选视频模型发挥，但不能省略计划总镜头数、每模块镜头数和镜头级主要动作；
- 在释放具体切点的同时给出节奏护栏：最终 packshot 之外，低运动构图不持续超过约 2 秒而没有第二状态；不连续安排两个只承担凝视、倒影、微笑或慢转身的同功能氛围镜头；
- 允许自然切镜，但要求关键动作在切镜前出现可读完成态，或由下一镜第一帧清楚继承结果；不得把“镜头更快”误写成动作被截断；
- 结尾同时需要 hero reveal 与 packshot 时，把它们编译成一个品牌收束模块，并写明完整正面 packshot 的最早进入时刻，避免模型因品牌旁白开始而提前数秒进入静态产品画面；
- 适合创意探索、单产品、单人物、简单动作链，以及用户更重视自然镜头语言的任务；
- 明确风险：构图、镜头顺序和人物/产品连续性可能比九宫格模式更容易漂移。

直出不等于无结构，也不等于无产品锁。只释放导演执行中可由模型自然完成的维度。

### 九宫格模式

九宫格模式采用两阶段流程：

1. 根据已确认脚本生成 3×3 分镜预览和图片外的逐格说明；
2. 用户确认或提出修改后，再把获批分镜、真实产品素材和必要约束编译成 Seedance 视频提示词。

除非用户明确要求一次完成，否则交付九宫格预览后暂停，不提前生成最终视频提示词。九宫格图遵守 [seedance-2-5-prompting.md](#src-seedance-tvc-director-references-seedance-2-5-prompting-md) 的无数字、无文字、无标签规则。

为避免转场僵硬：

- 把分镜视为必须经过的画面状态，不把每格同时重复写成精确运镜和复杂转场；
- 只锁定商业上必须准确的构图、人物关系、产品状态和因果节点；
- 允许当前所选视频模型在相邻画面状态之间自然补充摄影运动与转场；
- 需要严格逐镜复现时再增加约束，并明确自然运镜可能下降。

九宫格模式适合多人关系、复杂产品动作、严格因果、客户审稿、品牌画面必须对齐和局部重拍。

九宫格的 9 个画面是关键状态，不等于最终镜头数。计划 16 镜时，仍在图片外提供完整 16 镜表，并标明相邻关键格之间需要自然补足的镜头。

### 生图能力路由

九宫格需要实际渲染时，使用当前 Agent 或宿主环境已提供的最高优先级原生生图能力：

1. 用户明确指定且当前可用的生图工具优先；
2. 用户未指定时，遵循当前 Agent 的原生工具优先级，不在 Skill 中硬编码 GPT Image、Cola、DuMate 或其他供应商；
3. 宿主未公开底层模型名称时，只称为“当前 Agent 可用的生图能力”，不得猜测或虚构模型名；
4. 若有多个同级能力且必须选择，优先使用能读取产品参考图、保持主体一致并支持图像编辑的工具；
5. 当前 Agent 没有可调用的生图能力时，输出一条完整可复制的九宫格生图提示词和素材清单，明确说明本轮未实际渲染图片；
6. 不为了生图自动安装插件、注册外部服务或切换供应商，除非用户明确要求。

无论使用哪种生图能力，交付标准保持一致：产品参考职责清楚、九格顺序清楚、画面内无索引标记，并在生成视频前完成用户确认。

---

<a id="src-seedance-tvc-director-references-model-and-segmentation-routing-md"></a>

## `seedance-tvc-director/references/model-and-segmentation-routing.md`

## 视频模型与生成段数路由

### 三个概念不得混用

- `成片时长`：最终广告需要多少秒；
- `视频模型`：本轮调用哪个当前平台可用模型；
- `生成段数`：一次生成完整成片，还是分成多次生成后剪辑。

某个模型只能生成 15 秒，不等于平台上所有模型都只能生成 15 秒。用户选择 30 秒，也不自动等于必须拆成两个 15 秒段。先确认当前入口的模型能力，再组合时长、模型与段数。

### 能力核对顺序

按以下顺序建立本轮的“平台能力快照”：
1. 当前 Agent 或平台实际返回的可用视频模型列表、时长选项、积分/价格和输入能力；
2. 当前平台的官方产品页、模型说明或界面可见参数；
3. 用户刚刚在该平台完成的实测结果；
4. 仍无法核实时，明确写 `【待确认：当前平台模型/时长/价格】`，不得凭旧版本经验补全。

能力快照至少记录：

| 字段 | 用途 |
| --- | --- |
| 模型显示名或 ID | 防止把不同版本混为一谈 |
| 单次原生最长时长 | 判断单段是否可行 |
| 参考图/视频/音频能力 | 判断素材能否直接输入 |
| 原生声音能力 | 判断旁白、音效和音乐能否同轮完成 |
| 质量、速度与稳定性 | 估计可用率和返工风险 |
| 当前价格或积分 | 计算本平台、本时点的性价比 |

模型价格、套餐、限额和可用入口会变化。未经本轮核对，不得写“某模型永远最便宜”或把旧价格当作当前事实。

### 推荐算法：先满足，再比性价比

1. 先按硬条件过滤：能否完成目标单段时长、所需参考素材、声音、画幅、质量和编辑要求；
2. 再比较总成本：单次价格只是其中一项，还要考虑预计生成段数、后期拼接和因连续性失败而重试的成本；
3. 在满足交付条件的候选中，推荐综合成本最低、可用率足够的方案；
4. 同时给一个更高质量或更高控制的备选，并说明代价；
5. 用户指定模型或段数时优先保留，只有组合不可执行时才提示冲突并让用户选择替代方案。

“性价比最高”指当前平台、当前任务下的综合判断，不等于列表中单次积分最低。

### 默认路由

#### 15 秒

- 默认推荐当前平台中能够单段完成 15 秒、满足素材与声音要求的性价比最优模型；
- 默认使用 `1 段 × 15 秒`，避免无必要的剪辑和连续性损耗；
- 如果 Seedance 2.0、fast/mini 版本或其他模型满足任务且成本更低，可以推荐它，但必须依据当前可见价格与能力，不硬编码永久结论；
- 若任务包含高难度多人交互、复杂多模态参考或对成片可用率要求更高，可以推荐更高质量模型，并说明为何不只按最低价格选择。

#### 30 秒

- 当前入口可用 Seedance 2.5 且确认支持原生 30 秒时，默认推荐 `Seedance 2.5 + 1 段 × 30 秒`；
- 不得因为 Seedance 2.0 的单次上限为 15 秒，就自动把 30 秒拆成 `2 段 × 15 秒`；
- 单段优先用于人物关系、跨场景叙事、声音弧线和自然运镜，因为能减少换脸、光色跳变、动作断裂、音乐重启和后期拼接；
- 只有平台未开放 30 秒入口、用户指定了 15 秒上限模型、用户明确选择分段，或精确局部控制的收益高于连续性损失时，才建议多段生成。

#### 自定义秒数

- 先寻找能按用户目标时长单段完成的可用模型，再考虑拆段；
- 若没有单段可行模型，按故事自然段而不是机械等分来拆，并为每段写独立完整提示词、结束状态、声音交接和剪辑接口；
- 超过 30 秒时不得默认 Seedance 2.5 一定能单次完成；以当前入口实际展示的延长或长视频能力为准。

### 用户可选择的问法

把模型与段数作为两个独立选项，并与其他生成配置一次确认：

```text
4. 视频模型：使用推荐模型 / 指定模型。推荐会先读取当前平台可用列表，再按时长、素材、声音、质量与成本判断；
5. 生成段数：单段完整生成 / 多段生成后剪辑 / 按当前平台能力自动选择。单段连续性和自然运镜通常更好；多段便于局部重跑，但会增加人物、光色、声音和动作衔接风险。
```

如果平台已经明确返回模型列表，直接列出实际候选和推荐理由。平台未公开模型名时，只称“当前平台可用模型”，不得猜测底层版本。

### 冲突处理

| 用户选择 | 处理方式 |
| --- | --- |
| 30 秒 + Seedance 2.5 + 单段，且当前入口支持 | 直接生成一条 30 秒完整提示词 |
| 30 秒 + Seedance 2.0 + 单段 | 说明该组合与已核对的 15 秒单次能力冲突；提供“换 2.5 单段”或“保留 2.0 分段” |
| 30 秒 + Seedance 2.5 + 多段 | 尊重用户的多段选择，按故事自然段拆分，不强制改单段 |
| 15 秒 + 推荐模型 + 自动段数 | 选择当前性价比最优的合格模型，默认单段 |
| 模型价格或上限不可见 | 标注待确认，不虚构性价比排名；给出基于能力的暂定方案 |

不得静默更换用户指定模型，不得静默增加生成段数，也不得把“直出/九宫格”误解为“单段/多段”。九宫格只是是否先做分镜预览；确认后的九宫格同样可以喂给一个 30 秒单段生成。

### 输出最小信息

最终交付至少写明：

```text
平台能力快照：当前入口已确认/待确认的模型与时长能力
视频模型：推荐或用户指定项；一句选择理由
生成段数：1 段 × 30 秒，或具体多段分配；一句选择理由
替代方案：只在确有价值时给出一项
```

---

<a id="src-seedance-tvc-director-references-pacing-and-shot-density-md"></a>

## `seedance-tvc-director/references/pacing-and-shot-density.md`

## 节奏与镜头密度路由

### 四个数量不得混用

- `叙事模块`：故事结构与信息截止点，30 秒通常为 5 至 7 个；
- `有效镜头`：一次独立摄影观察或清楚的视听状态变化；
- `生成段数`：调用视频模型几次；
- `九宫格关键帧`：预览用的 9 个关键画面状态。

6 个叙事模块不等于 6 个镜头。30 秒可以由 6 个叙事模块组织 16 个有效镜头，并由 Seedance 2.5 一次生成完整成片。九宫格只有 9 格也不等于成片只能有 9 镜；它负责锁定关键状态，其余镜头由图片外镜头表和视频提示词补足。

### 独立节奏选项

用户可以独立选择节奏与镜头密度，不从产品品类、时长、直出/九宫格或是否有旁白中强行推断。

| 节奏档位 | 15 秒建议 | 30 秒建议 | 观看感受与适用方向 |
| --- | --- | --- | --- |
| 快节奏商业版 | 7 至 10 镜 | 14 至 18 镜，默认目标 16 镜 | 高频新信息、强产品声、利落转场；食品、饮料、零食、新品发布、社媒广告 |
| 标准商业节奏 | 5 至 7 镜 | 11 至 14 镜 | 有呼吸但不拖沓；多数品牌 TVC、人物关系、产品仪式 |
| 克制电影节奏 | 3 至 5 镜 | 8 至 10 镜 | 镜头较长但内部持续变化；高张力表演、连续摄影、情绪型品牌片 |
| 自定义 | 用户指定镜头数或平均镜长 | 用户指定镜头数或平均镜长 | 直接按参考片、媒介节奏或导演偏好执行 |

除非用户明确要求长镜头或克制慢节奏，普通 30 秒商业 TVC 不得只交付 5 至 7 个实际镜头。用户提到“节奏快”“像参考片”“16 个分镜”或反馈旧片偏慢时，优先推荐快节奏商业版，并把目标镜头数写进生成配置和最终提示词。

### 推荐问法

```text
6. 节奏与镜头密度：快节奏商业版 / 标准商业节奏 / 克制电影节奏 / 自定义镜头数。
30 秒参考：快节奏约 14–18 镜（可按 16 镜执行），标准约 11–14 镜，克制约 8–10 镜。这里指成片镜头数，不是视频生成段数。
```

用户已经给出参考片或准确镜头数时直接采用，不再要求选择档位。用户要求 Agent 决定时，根据渠道、品类、叙事复杂度和参考节奏给出推荐并标注理由。

### 从模块展开到镜头

先建立 5 至 7 个叙事模块，再为每个模块分配计划镜头数。示例：

| 30 秒模块 | 快节奏商业版计划 |
| --- | --- |
| 0–3 秒钩子 | 2 至 3 镜；第一帧已经在事件中 |
| 3–8 秒世界/问题 | 2 至 3 镜 |
| 8–14 秒产品触发 | 3 镜左右 |
| 14–21 秒材质/机制/体验 | 3 至 4 镜 |
| 21–26 秒兑现 | 2 至 3 镜 |
| 26–30 秒品牌收束 | 1 至 2 镜，保留稳定识别时间 |

模块标题只出现一次，但模块内部必须列出实际镜头或清楚的切镜事件。最终提示词至少写明：`计划有效镜头数`、各模块镜头数、每镜主要动作、完成态和衔接接口。不得只写 6 个时间段后期待模型自行补出 16 镜。

### 节奏不只由镜头数决定

镜头多不等于节奏一定快。每镜至少改变以下一项：

- 新故事信息或人物决定；
- 新产品证据、材质或风味层；
- 新景别、主体关系或空间；
- 新动作阶段及其完成态；
- 新声音事件、节拍或声音桥。

若两个镜头承担相同动作和相同商业任务，合并它们。若一个镜头只有等待、缓慢推盘、静态凝视、悬停液滴或轻微光变，即使全片达到 16 镜仍可能掉节奏。

### 有旁白版本的声音信息密度

镜头数量达标不代表注意力连续。有旁白的 30 秒商业片还要把约 `4–23s` 画成声音接力：旁白、产品声、音乐结构变化和新视觉事件轮流承担信息。任一旁白空窗超过约 `2.5s` 时，在镜头表里标注接管事件；连续超过约 `4s` 既无信息性人声又没有新产品证明、人物决定或关系推进时，视为节奏谷。

快节奏人物体验段尤其不能把十秒交给“取食—入口—微笑”的重复循环。第二位或第三位角色出现时，必须带来新的感官层、决定或关系信息；否则合并角色镜头。新增 VO 只表达画面尚未提供的信息，不用连续解说动作填空。

### 不牺牲可读性

- 快节奏仍需让关合、撕开、入口、接触、落下、人物决定等关键动作出现可读完成态；
- 普通快节奏镜头多为约 1.2 至 2.2 秒，复杂产品动作可更长，反应或连接镜头可更短；
- 标准节奏多为约 1.8 至 3 秒；克制节奏的长镜头必须包含至少两个清楚内部节拍；
- 最终 packshot/endboard 不受平均镜长约束，优先保证产品与品牌稳定识别；
- 转场通常控制在 0.2 至 0.8 秒，不用长时间漂浮、穿越或 morph 假装镜头变化。

### 直出与九宫格

- `直出`：把计划镜头数和每模块镜头数写进提示词，同时允许模型自然决定精确切点与运镜；
- `九宫格`：九格只锁 9 个关键状态。若成片计划 16 镜，在图片外提供完整 16 镜表，并标明哪些镜头由相邻关键格之间自然补足；
- 用户要求逐镜预览全部 16 镜时，可以生成第二张无数字九宫格或独立单帧，但不得把镜号画进参考图；
- 无论哪种模式，镜头数都不改变视频模型调用次数。`16 镜 + 1 个 30 秒生成段`是合法组合。

### 复盘

复盘成片时记录实际镜头数、中位镜长、最长非 packshot 镜头和节奏谷位置。若提示词计划 16 镜而实际只生成 6 至 8 镜，优先检查：

1. 是否只写了模块，没有展开镜头；
2. 是否把“自然运镜”误解为每模块一镜到底；
3. 是否存在 3 秒以上的微动作或静态构图；
4. 是否让转场吞掉下一场景；
5. 是否过早进入 packshot。

重试时保留成功的创意、人物、产品与声音，只修镜头密度、动作时长和切点层。

---

<a id="src-seedance-tvc-director-references-product-actions-md"></a>

## `seedance-tvc-director/references/product-actions.md`

## 产品交互与真实受力

### 先判断是否需要拍完整动作

复杂包装交互不是默认的“产品感”镜头。先按可靠性路由：

1. `动作是核心证明`：完整拍摄，并明确结构、手部职责、受力方向、材料反馈和结束状态。
2. `动作只负责进入使用`：优先用动作前后两个状态加声音桥，例如密封包装 → 画外撕开声 → 已打开包装。
3. `参考图看不清开口结构`：不要猜撕口、瓶盖、泵头或盒扣；使用预先打开、剪开、移出画面操作或后期实拍插入。

不要在同一镜头同时要求包装正面文字准确、双手复杂操作、人物表情和发光/粒子特效。把动作镜头与品牌 packshot 分开。

### 五段受力链

每个物理动作按以下顺序写：

`初始结构 → 锚定点 → 施力点与方向 → 可见材料反馈 → 明确结束状态`

缺少任何一段都容易得到“手在动、物体没变化”的假动作。

### 软袋撕开

只有参考素材能支持封边或缺口结构时才完整拍摄。可靠写法必须包含：

- 包装初始为密封，顶部热封边清楚；
- 非惯用手握紧袋身上半部并保持稳定，不能双手对称悬空拉扯；
- 惯用手捏住明确的预切缺口或封边一角，沿水平方向一次撕过；
- 薄膜从起裂点连续分离，袋身在受力侧产生真实褶皱；
- 撕下的窄封条与袋身完全分开，并由惯用手带离画面；
- 结束时袋口形成连续开口，能看见内侧阴影或内容物，但不要求同时保持正面包装完全平整。

将完整撕袋控制在约 0.8 至 1.2 秒。不要用“沿顶部利落撕开”替代受力说明，也不要让发光、烟雾或粒子遮挡封边分离。

参考图不显示预切缺口时，优先选择以下替代：

- 包装已在画外打开，人物把开口袋放入画面；
- 使用画外撕袋声，硬切到双手自然撑开袋口的完成态；
- 用剪刀沿顶部直线剪开，再切到包装正面；
- 仅拍手伸入已经打开的袋口，把精确包装留给独立 packshot。

### 其他常见动作

- `开盖`：一手固定容器，一手旋转/掀开盖；写清旋转轴、圈数上限和盖子最终归属。
- `按压泵头`：手指垂直下压，泵头行程、液体出口和接液位置必须对齐。
- `倒出`：容器先倾斜，再出现内容物；重力方向、流量和接收容器位置一致。
- `涂抹`：先建立取用量和接触点，再写单一方向的短动作；不要同时改变产品、手和人物位置。

### 容器里的最后一件产品

当剧情要求“最后一片、最后一颗、最后一块”时，先写物理状态表：

`数量 = 1；支撑面 = 容器底部或浅盘面；朝向 = 平躺或大面积斜靠；重力 = 竖直向下；接触 = 有明确且足够的支撑面积。`

- 薄片、圆片或不规则食品不得用窄边垂直立在碗沿、碗底或桌面上，也不得为了让镜头看清而悬浮。
- 深碗中的平躺物体从平视低机位通常不可见。若剧情必须看清，改用 35–60 度高角度或俯拍插入镜头，或把深碗换成浅盘/低边小碟。
- 先做“机位与物理可见性检查”：真实状态下会被容器遮挡时，修改机位或容器，不修改重力与接触关系。
- 将物体近景与人物对视拆开拍；不要同时要求平视看清碗底物体、两张脸和两只手。

### 动作复盘

高频抽取动作前、接触、受力、分离和完成五个状态。若看不到锚定、材料变化或完成态，将问题归为物理链失败，不用更多质感词修补。重试时保留已成功的选角、场景、旁白与 packshot。

涉及容器时额外检查物体的重心、支撑面、接触点、遮挡关系和镜头可见性。画面能看清不代表物理成立。

---

<a id="src-seedance-tvc-director-references-scene-progression-md"></a>

## `seedance-tvc-director/references/scene-progression.md`

## 30 秒场景推进与反重复

### 场景数量路由

先按叙事需要选择场景数量，不把不同景别误称为不同场景。

- `1 个场景`：核心是连续仪式、单次机制演示或空间本身发生不可逆变化。
- `2 个场景`：需要建立使用前后、私人到社交、现实到品牌隐喻等明确反差。
- `3 个场景`：需要展示多个互补使用情境、人物关系递进、时间推进，或用户明确要证明 30 秒长时叙事能力。

场景变化必须至少改变地点、时间、人物关系、行动目标或世界规则中的一项。只换机位、景别、光色或特效不算新场景。

用户明确要求“更丰富”或“展示 30 秒能力”时，默认评估 2 至 3 个场景；只有单场景有更强因果链时才保留单场景，并说明理由。

### 多场景故事脊柱

使用以下顺序，不要求平均分配时长：

`0–3 秒结果/异常钩子 → 场景 A 交代欲望或问题 → 场景 B 让产品改变行动 → 场景 C 扩大体验或关系 → 情绪/功能兑现 → packshot/endboard`

每个场景都必须回答同一个核心主张，但提供不同的新信息。产品可通过本体、使用动作、声音、结果或统一视觉符号贯穿，不必在每个场景机械展示包装。

### 叙事模块与有效镜头

把 30 秒提示词中的 `5 至 7 个叙事模块` 与实际镜头数量分开：

- `叙事模块`规定在一个时间窗内必须完成的新信息、因果事件和结束状态；
- `有效镜头`是一次独立摄影观察，通常由硬切、清楚的连续摄影重构或新的主体关系开始；
- 读取 [pacing-and-shot-density.md](#src-seedance-tvc-director-references-pacing-and-shot-density-md) 后采用用户选择：快节奏商业版 14 至 18 镜、标准商业节奏 11 至 14 镜、克制电影节奏 8 至 10 镜，或准确自定义镜头数；
- 一个 4 至 6 秒模块按密度安排 1 至 4 个互补镜头。快节奏版通常为 2 至 4 镜；克制版镜头较少，但每个长镜必须有两个以上清楚内部节拍；
- 直出模式锁定计划总镜头数、每模块镜头数、新信息、动作顺序和完成截止点，把精确切点与运镜交给 Seedance；不得省略镜头级动作后把每个模块写成一镜到底。

对 packshot 之前的低运动镜头做停留检查：约 2 秒内没有出现第二个可见状态、有效主体运动、新商业信息或新的声音事件时，缩短、合并或换镜。不得连续使用两个功能相同的低运动人物镜头，例如 `窗前倒影 → 正面凝视`、`闭眼感受 → 微笑凝视`；它们必须被压缩为一个兑现镜头，或由新的产品/故事证明隔开。

### 动作完成态与切点

镜头密度只在动作仍可读时成立。为每个关键动作同时写 `触发时刻`、`决定性变化` 和 `可读结束状态`：

- 动作完成后通常保留约 0.15 至 0.35 秒，再进入下一镜；
- 使用动作匹配时，下一镜第一帧必须继承结果，例如上一镜电脑开始合上，下一镜环境已经明确变暗；
- 若切点早于闭合、接触、落下、入口、破裂或人物决定的可见完成态，归为动作被截断，不得把它当作节奏加快的成功；
- 未完成动作只有在制造明确悬念、且下一镜立即回答时才允许保留。

同一动作跨景别接力时，不必在每个切点都完成，但必须标注 `起势/中段/完成`。上一镜结束态与下一镜第一帧在主体、运动方向和动作阶段上连续，并在接下来一至两镜内显示完成；否则仍按动作截断处理。

### Hero reveal 与 packshot 预算

- `Hero reveal` 用运动、光线、尺度或材质关系让产品进入品牌高潮；`packshot` 用稳定完整正面解决产品识别。两者不能连续承担相同的完整产品陈列任务；
- 有标准包装、瓶体或设备正面的产品，两者相邻时合并为一个结尾模块：先用约 0.8 至 1.5 秒动态进入完整产品，再稳定约 3.5 至 4.5 秒；30 秒片的产品与品牌收束通常合计约 4.5 至 6 秒；
- 在这类时间轴中写明 `完整正面产品不得早于 X 秒出现`。此前可以出现手持情境、局部材质或运动中的产品，但不能提前变成静态 packshot；
- 鲜食、餐饮、原料或服务品牌没有标准包装时，不强行生成虚构包装。用约 3 至 5 秒的成品/结果 hero 完成感官回报，再接约 1 至 2 秒获批 endboard；精确品牌字与 slogan 仍由后期完成；
- 最后品牌旁白可以先在人物兑现、产品情境或材质细节上进入，不能把旁白开头自动绑定为完整 packshot 切点；
- 成片复盘时测量第一帧稳定完整全瓶出现的时间。若比预算提前超过约 0.5 秒，先检查 hero reveal 与 packshot 是否被模型合并为超长定帧。

### 反重复矩阵

写提示词前为每段各填一项：

| 段落 | 新信息 | 唯一主体动作 | 新场景/状态 | 独有景别 | 转场接口 |
|---|---|---|---|---|---|

出现以下任一情况即重写：

- 两段都以挑起、倒入、涂抹、旋转、入口或凝视等同一动作承担同一商业任务；
- 钩子使用的主体、动作、景别和视觉异常，在中段再次原样出现；
- 三段以上仍在同一人物、同一道具、同一桌面关系中，仅改变镜头距离；
- 特效颜色变化替代了新情境、新因果或新人物关系；
- 删除某一段后，观众没有损失任何产品或故事信息。

结尾允许回收开场母题，但必须改变意义：开场提出问题，结尾给答案；开场是极端结果，结尾揭示产品归属。不得把开场镜头直接再拍一次。

### 动作价值与节奏谷

先把时间轴中的动作分为：

- `因果动作`：触发故事、改变关系或兑现产品证明；
- `感官动作`：断裂、包裹、回弹、冒泡等可见产品证据；
- `反应动作`：人物决定、情绪转折或余味；
- `物流动作`：推盘、递碗、摆放、移杯、把产品搬到中央或等待别人拿取。

物流动作只有在承担争夺、拒绝、礼仪、挑战或关系反转时才获得完整镜头。普通物流动作：

- 单次通常控制在约 0.6 至 1.2 秒；
- 不与另一个推、拿、递、放等低幅度桌面动作连续占据数秒；
- 能从结束状态开始就不要展示过程，例如让盘子在场景建立时已经位于中央；
- 需要分享信息时，优先使用 `产品已就位 → 一次清楚取食 → 立即人物反应`，而不是 `推过去 → 等待 → 再拿起来`。

对全片做节奏谷检查：任意约 2.5 秒窗口若同时没有新故事/产品信息、明显状态变化、镜头切换、有效主体运动和新的声音事件，就标为节奏谷。刻意静默、风味观察和 packshot 可以慢，但必须有持续视觉张力；物流动作不能占用唯一慢节奏名额。

复盘成片时把硬切时间、旁白起止和高频抽帧对齐。若低运动镜头恰好落在两句旁白之间，不要单纯补满旁白；先删除、合并或提前完成物流动作，再用一次动作声或音乐节拍连接。

### 反应的触发与兑现

人物反应不是独立装饰镜头，而是产品因果链的一部分。为每位首次承担结果证明的角色写清：

`可见触发 → 0.5 至 1 秒内出现特异微反应 → 人物决定或关系兑现`

- `可见触发` 可以是入口、皮肤接触、听见产品声、看见结果或受到环境变化影响；只让角色站在产品旁边不算触发。
- `特异微反应` 必须能指向当前主题。辛辣可使用眼睛迅速睁开、短促吸气、控制呼气、嘴唇轻收、热感后仍想继续；闭眼微笑、张嘴停住、空泛惊讶或同步大笑不能单独证明辛辣。
- 普通单一表情特写默认约 0.8 至 1.2 秒。超过约 1.2 秒时，必须从第一状态转到第二状态，例如 `被辣到 → 忍住 → 决定继续`，不能保持一张脸等待剪辑点。
- 新角色若承担新的产品证明，允许再次出现一次简短入口或接触动作；它提供了新的因果信息，不属于机械重复。禁止的是同一角色、同一景别、同一动作和同一商业任务的重复。
- 让触发、反应和兑现相邻。不得在人物刚产生反应后先插入 packshot，再回到朋友大笑、理解或选择；产品英雄镜头应放在关系兑现之后。
- 三人以上群像优先让一名新角色成为动作主体，其余角色观察并完成关系反应；不要让所有人同时做相同表情或复杂手部动作。

成片复盘时逐一回答：该角色为什么在此刻产生这个表情？观众能否在前约 1 秒看见原因？若答案是否，删除悬空表情或补回最小必要触发，不要只增加“更自然、更有感染力”等形容词。

### 连续性与转场

为全片建立两层锁：

- `全局锁`：产品外观、核心人物身份、品牌色、声音母题和核心主张不变。
- `场景锁`：每个地点分别明确时间、光源、服装状态、产品位置和行动目标。

用一个可追踪接口连接场景：动作匹配、道具运动、形状匹配、声音桥或同方向光线。每次转场只使用一个主要接口，避免随机蒙太奇。

旅程或溯源蒙太奇先定义全局运动向量，例如所有移动主体保持从左向右；需要反向时用正面、静止或可见转身镜头重置方向。两个世界反复交替、使用 12 镜以上或依赖声音先行时，读取 [shot-handoffs-and-sound-bridges.md](#src-seedance-tvc-director-references-shot-handoffs-and-sound-bridges-md) 建立场景锚卡、源镜末态、目标镜首帧和连续声音床。

#### 转场时间预算

把转场写成有截止时间的桥，不写成无终点的旅程：

`源场景最后状态 → 0.2–0.8 秒桥接动作 → 目标场景已完全建立`

- 普通商业片转场控制在 0.2 至 0.8 秒；唯一 hero transition 最长约 1.2 秒。
- 30 秒片全部转场总计通常不超过约 2.5 秒；其余时间交给新场景的动作和信息。
- 为每次转场写目标场景的完成时刻，例如“9.0 秒开始甩镜，9.5 秒客厅已经完整可见”。
- 使用硬切、动作匹配、声音先行切或短甩镜作为默认；只有概念本身依赖连续变形时才使用 morph。
- 避免“镜头跟随进入、缓慢漂浮、穿越巨大的世界、逐渐演化”等无截止词；它们容易吞掉下一场景时长。
- 转场桥中不得出现超过约 0.3 秒、既无主体也无有效光线运动的空白或近纯色帧；桥接元素消失前，目标场景应已经建立。

风味世界、机制隐喻或材质微观如果承载独立产品信息，就把它定义为有开始和结束的正式场景，并分配 2 至 4 秒；不要一边称其为转场，一边给它连续漂浮、绕行或多次变形。

### 30 秒多场景最低交付

- 0–3 秒独立强钩子；
- 2 至 3 个因果相连的场景或状态；
- 5 至 7 个叙事模块，并按用户选择展开为快节奏 14 至 18 镜、标准 11 至 14 镜、克制 8 至 10 镜或自定义镜头数；模块数、镜头数与生成段数分别记录；
- 每 4 至 6 秒出现新的故事或商业信息；
- 至少一次产品材质/机制证明；
- 至少一次人物、关系或环境状态兑现；
- 最后约 4 至 6 秒完成产品与品牌收束：标准包装用 packshot 加 endboard；鲜食、餐饮或服务品牌用结果 hero 加约 1 至 2 秒 endboard；
- 全片不重复已完成的核心动作。
- 每次转场在约 1 秒内完成，目标场景按时间轴准时出现；不存在持续数秒的隧道、漂浮或慢 morph。

---

<a id="src-seedance-tvc-director-references-seedance-2-5-prompting-md"></a>

## `seedance-tvc-director/references/seedance-2-5-prompting.md`

## Seedance 2.5 提示词编译

### 1. 先选模型与生成单位

先读取 [model-and-segmentation-routing.md](#src-seedance-tvc-director-references-model-and-segmentation-routing-md)。成片时长、视频模型与生成段数是三个独立决定；不得从 Seedance 2.0 的 15 秒能力推导出 Seedance 2.5 或整个平台也只能生成 15 秒。

- 一个空间、一个核心动作、连续摄影可以完成：优先写成单段生成。
- 多地点、多人并行动作、精确包装特写与复杂 endboard：先在同一生成段内拆成多个镜头；只有用户选择多段，或当前所选模型无法在目标时长与复杂度内稳定完成时，才拆成多个生成段。
- 每段都应能独立复制，不引用“同上”或未定义的上一段描述。

### 15 秒、30 秒与自定义时长编译模式

#### 15 秒

- 使用 4 个左右的时间段；
- 第一段固定为 0–3 秒强钩子，至少包含一个可见变化；
- 只保留一个核心动作链和一次主要运镜；
- 优先单一场景、单一产品证明和清楚的结束构图；
- 提示词先保证动作完成，再补充材质和声音。

#### 30 秒

- 使用 5 至 7 个叙事模块，并读取 [pacing-and-shot-density.md](#src-seedance-tvc-director-references-pacing-and-shot-density-md) 按用户选择展开镜头：快节奏 14 至 18 镜、标准 11 至 14 镜、克制 8 至 10 镜或准确自定义；模块负责新信息和截止时间，不等于单个镜头或生成段数；
- 第一段单独使用 0–3 秒，不与环境铺垫合并；从第一帧进入视觉异常、产品质地、结果瞬间或人物转折；
- 3 秒后再展开世界、人物和原因，并让后续镜头持续回答开场提出的问题；
- 先写完整故事脊柱，再为每段分配新信息，禁止复制前一段动作；
- 一个 4 至 6 秒模块若只有微动作、人物近景或材质观察，使用 2 至 3 个互补镜头或至少两个清楚的内部节拍；不得让滴管悬停、单次涂抹、静态凝视或轻微光变占满整个模块；
- 最终 packshot 之外，低运动构图约 2 秒内必须出现第二状态、有效主体运动、新商业信息或换镜。连续两个承担相同任务的人物氛围镜头必须合并或替换；
- 关键动作在切镜前必须出现可读完成态并保留约 0.15 至 0.35 秒，或由下一镜第一帧清楚继承结果；不得用截断关合、接触、落下或人物决定来换取镜头数量；
- 用户要求丰富度或展示 30 秒能力时，读取 [scene-progression.md](#src-seedance-tvc-director-references-scene-progression-md)，明确写出 2 至 3 个场景各自的地点/时间、行动目标、新信息和转场接口；只改机位或特效不算换场；
- 至少包含环境/情境、产品触发、材质或机制观察、状态兑现、hero shot 五类画面；
- 用动作匹配、形状匹配、光线延续或声音桥连接镜头；
- 为每次转场写开始时刻、完成时刻和目标场景第一帧；普通转场使用 0.2 至 0.8 秒，避免让“跟随、穿越、漂浮、逐渐变成”吞掉下一段；
- 对人物、产品、道具、光线方向和色彩状态建立贯穿全片的连续性锁；
- 可以有多个镜头，但每个镜头仍只承担一个主要动作和一个商业任务；
- 最后约 4 至 6 秒为产品和品牌完成收束，不在结尾继续添加新剧情。有标准包装的产品使用 hero reveal、packshot 与 endboard；鲜食、餐饮、原料或服务品牌使用结果 hero 与约 1 至 2 秒 endboard。
- 结尾同时包含 hero reveal 与 packshot 时，把两者合并为一个模块，并写明完整正面产品最早出现时刻；此前只允许情境产品、局部材质或运动状态。最后品牌旁白可以先开始，但不得自动触发提前 packshot。
- 在时间轴完成后做动作去重：挑起、倒入、涂抹、入口、凝视、旋转等核心动作各只承担一次主要商业任务；钩子动作默认不在中段重演。
- 直出模式写明计划总镜头数、每模块镜头数、必要动作顺序、完成截止点和节奏护栏；允许 Seedance 自然决定精确切点、运镜和短转场，但禁止只写模块标题后把“自然发挥”误解成每个模块一镜到底。

当前入口可用 Seedance 2.5 且确认支持原生 30 秒时，30 秒默认输出一条包含完整分段时间轴的单段提示词。只有当前入口未开放该能力、用户指定 15 秒上限模型、用户明确选择多段，或精确局部控制收益明显高于连续性损失时，才建议拆段生成与后期组合。

#### 自定义时长

- 提示词首行写准确总秒数，所有时间段之和必须一致；
- 少于 3 秒时不机械使用 0–3 秒模板，从第一帧同时完成钩子、产品识别和品牌记忆；
- 3 秒及以上仍先完成前三秒广告钩子，再按每 4 至 6 秒一个新信息节点分配中段；
- 先核对当前入口的单次生成上限，超出时输出多个独立完整提示词和明确剪辑接口；
- 不把自定义版本写成 15 秒或 30 秒提示词的匀速拉伸或裁切。

### 2. 分配参考素材职责

逐项声明素材负责和不负责的维度：

```text
@图片1：只负责产品外观、材质和包装比例；不继承背景与画面文字。
@图片2：只负责人物身份和发型；服装按文字指令。
@视频1：只负责镜头轨迹和动作节奏；不继承人物、产品或场景。
@音频1：只负责节拍与段落结构；不复制歌词内容。
```

同一维度只能有一个最高优先级来源。没有实际附件时不得虚构编号。

#### 九宫格分镜的编号规则

用户要求生成九宫格分镜时：

- 默认采用 3×3 排列，阅读顺序固定为从左到右、从上到下，对应第 1 至第 9 格；
- 图片内部只保留分镜画面，不绘制 `1–9`、`01–09`、`Shot 01`、时间码、面板标题、字幕、箭头、图例、水印或其他索引标记；
- 需要讨论单格时，在图片外的分镜表中按默认顺序写“第 1 格”至“第 9 格”，或使用“左上、上中、右上”等位置词；
- 给图像模型的生成指令明确写“纯画面九宫格，无数字、无文字、无标签”；交付前放大检查九格四角和留白区域；
- 九宫格将作为 Seedance 参考素材时，不依赖画面内编号传递时序。在视频提示词中单独声明“按从左到右、从上到下理解故事顺序”，并禁止继承参考图中的排版标记。

旧分镜若已经含有数字或标签，不得直接作为新一轮模型输入；先重新生成无标记版本或导出清洁单帧。

### 3. 锁定商业资产

产品锁至少覆盖：

- 轮廓与比例；
- 主要颜色和材质；
- 标签/屏幕/开口朝向；
- 初始位置和持有关系；
- 使用前后的状态变化；
- 不得出现的形变、复制、换色和部件增减。

人物锁至少覆盖身份、年龄段、发型、服装、体态和初始站位。不要用参考人物的背景污染目标场景。

同镜头出现 3 人以上或多人共同接触产品时，读取 [ensemble-continuity.md](#src-seedance-tvc-director-references-ensemble-continuity-md)，为每人建立 ID、差异信号、从左到右座位表和手部归属。多人围桌时再声明桌型、相机钟点位、近左/远左/远右/近右座位、视线和伸手扇区；不得只写“一群不同的年轻朋友”或“四人围坐圆桌”。

### 4. 按可见事件写时间轴

每段采用：

`开始状态 → 触发动作 → 决定性变化 → 物理/情绪反馈 → 结束状态`

同时说明镜头实际覆盖其中哪些环节。分开描述人物、产品、相机和环境的运动，避免动作所有权混乱。

为关键动作额外写清 `切镜许可点`：观众已经看见哪一个完成状态后才允许离开。需要快速衔接时用动作结果继承，不用提前截断。

同一动作跨景别连续时，为相邻镜头写 `继承项 → 本镜动作 → 结束态 → 下一镜接口`。只有下一镜第一帧按同一主体、方向和动作阶段立即接续时，才允许从起势或中段切走；不接续时必须在当前镜展示完成态。

产品发生开合、撕裂、按压、倒出或涂抹时，读取 [product-actions.md](#src-seedance-tvc-director-references-product-actions-md)，把结构与受力写成连续可见事件。若参考素材无法确认结构，改用预先完成状态、声音桥或后期实拍，不凭空猜测。

小物体位于容器中时，先检查在指定机位下是否真实可见。若必须靠竖立、悬浮或违反重力才能被看见，改用高角度插入镜头、浅容器或拆镜。

食品或饮料的具体风味承担核心卖点时，读取 [food-flavor-direction.md](#src-seedance-tvc-director-references-food-flavor-direction-md)。先把物理口感与味觉/香气拆开，再让风味在真实产品微距、2 至 4 秒独立风味镜头、人物余味或 packshot 环境中至少出现三层递进证据。风味镜头是正式场景，不是无截止的慢转场。

完成时间轴后，读取 [scene-progression.md](#src-seedance-tvc-director-references-scene-progression-md) 为动作标注因果、感官、反应或物流价值。没有额外叙事价值的推、递、摆、放、等待等动作不单独占据长时间；从动作完成态开始，或压缩到约 0.6 至 1.2 秒。禁止让两个低幅度桌面动作连续形成数秒节奏谷。

### 5. 写摄影与光线

只指定对叙事有用的摄影信息：

- 景别和机位关系；
- 一个主要运镜；
- 对焦对象和必要的焦点变化；
- 可解释的真实光源；
- 材质如何响应光线；
- 有意保留的轻微手持、运动模糊或曝光变化。

不要同时要求手持纪实、机械臂绝对稳定、快速环绕和微距产品特写。

### 6. 组织最终提示词

按需使用以下顺序，不要保留空标题：

1. 成片规格和生成方式；
2. 一句导演意图；
3. 参考素材职责；
4. 主体、产品和场景锁；
5. 多世界或高密度接力片的场景锚、光色弧线与全局运动向量；
6. 按时间顺序的镜头/动作；
7. 摄影、光线与表演；
8. 声音；
9. 连续性与必要负面约束；
10. 结尾状态或 packshot 目标。

把策略解释、受众分析和选择理由留在代码块外。

有旁白时，在“声音”部分只放一张主旁白清单，原文每句只出现一次；画面时间轴只引用 `VO-01` 等 ID。每条 VO 都写唯一开始、硬停止和 `repeat_count=1`，并明确硬停止后不得重启、回声、复述或跨场景续念。要求商业文案逐字准确时，把模型生成音轨标为 guide VO，并列入后期替换。

### 7. 负面约束

只写与当前镜头高风险相关的约束，例如：

- 产品不变形、不复制、不换色；
- 人物不换脸、不换装、不瞬移；
- 不添加未提供的 Logo、包装文字或字幕；
- 不出现额外人物、额外手指或错误持有关系；
- 不重复已经完成的动作。

不要堆砌通用负面词。正向动作不清楚时，负面词无法补救。

### 8. 能力边界

Seedance 2.5 官方模型能力包含最长 30 秒单次生成，但具体平台是否开放、可选秒数、分辨率、多模态数量、价格和编辑能力仍可能因入口而变化。用户询问当前参数或实际执行时，先核对其使用的即梦、火山方舟或第三方入口；无法核实时标注为平台能力待确认，不把旧版本或其他入口的限制当作当前事实。

---

<a id="src-seedance-tvc-director-references-shot-handoffs-and-sound-bridges-md"></a>

## `seedance-tvc-director/references/shot-handoffs-and-sound-bridges.md`

## 镜头接力与声音桥

当 30 秒广告使用 12 镜以上、两个世界交替、同一动作跨切点延续、溯源/旅程蒙太奇，或依赖声音先行完成转场时读取本文件。镜头密度由用户或 [pacing-and-shot-density.md](#src-seedance-tvc-director-references-pacing-and-shot-density-md) 路由决定，不再把 12 镜以上限制为特定题材。

### 密度档位与接力蒙太奇

- `克制电影节奏`：30 秒通常 8 至 10 个有效镜头；长镜头内部必须持续变化。
- `标准商业节奏`：30 秒通常 11 至 14 个有效镜头，适用于多数人物关系、产品仪式和功能证明。
- `快节奏商业版`：30 秒通常 14 至 18 个有效镜头，默认目标可设为 16 镜。
- `接力蒙太奇`：是一种相邻镜头逐项继承的结构，可用于来路、旅程、工艺链，也可服务其他高密度广告；它不是唯一允许使用 16 镜的题材。

使用 14 镜以上或接力蒙太奇时满足以下条件：

- 仍用 5 至 7 个叙事模块控制新信息与截止时间，不把 16 镜写成 16 条互不相关的小故事；
- 大多数镜头约 1.2 至 2.2 秒，每镜只有一个主要动作和一个摄影观察；
- 复杂双手操作、多人互动、精确包装正面和强特效不在同一短镜中叠加；
- 相邻镜头通过动作阶段、运动方向、视线、形状、材质、光色或声音中的一项明确接力；
- 产品与品牌收束仍有独立预算，不被镜头数量挤掉。

任一短镜无法说明它从上一镜继承什么、给下一镜留下什么，就合并或删除。镜头多不是节奏快的证据，交接清楚才是。

### 建立场景锚卡

两个以上世界交替时，先为每个世界写一张锚卡：

| 字段 | 内容 |
|---|---|
| 地点与时间 | 真实空间、时段、天气或室内状态 |
| 主光源 | 光从哪里来，如何作用于主体 |
| 背景深度 | 前中后景中必须保留的生活或品牌证据 |
| 色彩状态 | 当前起点、允许变化、不得跳回的状态 |
| 行动目标 | 该世界中主体正在完成什么 |
| 环境声床 | 持续存在且切镜后不重启的声音组合 |
| 防串场项 | 不得从另一个世界继承的服装、道具、文字或光色 |

场景锚要使用可见证据，不只写“电影感、高级、真实”。需要从冷到暖、白天到午后或私人到公共递进时，定义单向光色弧线；除非故事明确反转，不得无原因回退。

### 锁定屏幕方向与视觉母题

旅程段先定义 `全局运动向量`，例如所有羊群、人物、车辆和奔跑主体均保持从左向右。相邻镜头允许改变速度和景别，不随意反转屏幕方向。

需要反向时，先使用正面、静止或明确转身的中性镜头重置方向；不能让主体在无解释硬切后突然从右向左运动。

跨世界转场优先选择一个视觉母题：

- 形状：圆形火光接太阳、容器弧线接地平线；
- 材质：蒸汽接云、扬尘接公路薄尘；
- 动势：上摇接航拍前移、右向奔跑接右向车辆；
- 光色：暖橙火光接午后金光。

为母题同时写 `源镜最后可见状态` 与 `目标镜第一帧占位`。桥接不是抽象 morph；源元素消失前，目标世界必须已经建立，不能经过空白、纯色或无主体帧。

### 写镜头交接契约

高密度镜头表为每镜使用四项短句：

```text
继承项：上一镜留下的主体、动作阶段、位置、方向或声音。
本镜动作：本镜唯一主要动作与决定性变化。
结束态：切镜前观众确实看见的状态。
下一镜接口：留给下一镜的动作、视线、形状、材质、光或声音。
```

使用 `起势 → 中段 → 完成` 描述动作阶段，比小数百分比更稳。只有同一动作在下一镜第一帧按相同主体、方向和阶段立即接续时，才允许在中段切镜；动作必须在接下来一至两镜内完成。

若下一镜不延续同一动作，就在当前镜展示可读完成态并保留约 0.15 至 0.35 秒。不要一边写“动作未完成”，一边切到无关世界并声称这是连续性。

### 建立声音契约

声音先按全片层级规划，再分配到镜头：

1. `环境声床`：每个世界各有一套持续底噪，段内切镜不重启；
2. `产品/动作声`：只强化真正的接触、受力、破裂、滴落、入口或机械事件；
3. `音乐弧线`：写明第一次进入、展开、峰值、收束和归静，不在每镜重新开始；
4. `旁白`：仍由唯一主旁白清单管理，镜头表只引用 VO ID。

前三秒可以故意不使用背景音乐，让产品声和环境声直接形成钩子。音乐第一次进入应由一个可见事件触发，而不是按惯例从 0 秒铺满。

关键跨场景可以使用 `声音先行切`：让目标声音在源镜结尾约 0.3 至 0.6 秒进入，下一镜切入后全量接管。全片只选择少数真正重要的声音桥，分别写明源声音何时退出、目标声音何时进入；不得让同一音乐或环境声在切点重新起头。

旁白可以跨画面切点，但原文仍只在主旁白清单出现一次。镜头表只写 `VO-02 跨切点继续，按既定硬停止结束`，不能为了说明画面而再次粘贴旁白文字。

### 编译顺序

高密度接力蒙太奇按以下顺序组织最终提示词：

1. 成片规格与一句话叙事闭环；
2. 场景锚卡与防串场项；
3. 单向光色弧线与全局运动向量；
4. 主旁白清单；
5. 音乐弧线、环境声床和声音先行切点；
6. 5 至 7 个时间模块，并注明每段计划镜头数；
7. 每镜的继承项、本镜动作、结束态和下一镜接口；
8. 产品、人物、文字与商业交付边界。

### 商业边界

- 产地、冷链、鲜度、饲养方式、制作工艺和“不腌制”等信息只有在用户资料或获批 brief 支持时才能作为事实；否则写成 `【待补：获批依据】`，或删除事实性表达。
- 地域、牧场、工厂和运输画面若只是风味或品牌联想，明确标注为概念隐喻，不能伪装成真实供应链纪录。
- 车辆字样、包装小字、品牌落版和 slogan 交给后期使用获批资产，不要求视频模型逐字生成。
- 专业 TVC、电影质感、浅景深和自然光影只能作为规格摘要；它们不能代替场景锚、真实光源、动作接口和声音调度。

### 交付前检查

- 计划镜头数是否符合用户选择的节奏档位，并且不是为了显得丰富而机械碎切？
- 每镜是否能说清继承项、结束态和下一镜接口？
- 未完成动作是否在下一镜立即、同向、同阶段接续并很快完成？
- 旅程段的主体是否保持同一屏幕方向？
- 跨世界母题是否同时定义源镜末态与目标镜首帧？
- 场景锚、光色弧线和声音床是否没有无理由重置？
- 声音先行是否只发生在关键切点，且音乐和环境声不重启？
- 旁白原文是否仍只出现一次并通过实际朗读计时？
- 供应链、产地、鲜度、工艺和精确文字是否有获批依据或已转交后期？

---

<a id="src-seedance-tvc-director-references-tvc-structure-md"></a>

## `seedance-tvc-director/references/tvc-structure.md`

## 15 秒、30 秒与自定义时长 TVC 结构

### 时长决策表

| 条件 | 选择 15 秒 | 选择 30 秒 |
|---|---|---|
| 核心信息 | 一个主张、一个证明 | 一个主张、两个互补证明或一条情绪弧线 |
| 场景 | 单一空间优先 | 1 至 3 个相互关联的空间或视觉状态 |
| 人物 | 无人物或一个简单动作 | 人物关系、使用仪式或明确转折 |
| 产品 | hero shot、单功能动作 | 使用过程、材质、机制隐喻、结果与 hero shot |
| 镜头 | 克制 3–5、标准 5–7、快节奏 7–10 个 | 克制 8–10、标准 11–14、快节奏 14–18 个；可自定义准确镜头数 |
| 用户措辞 | 快速、精炼、单卖点、短版 | 完整、丰富、故事感、世界观、情绪递进 |

用户明确指定时长时不覆盖用户选择。用户未指定时，在配置确认中提供 15 秒、30 秒和自定义秒数，并根据需求推荐：至少命中两项 30 秒条件时推荐 30 秒，否则推荐 15 秒。只有用户要求 Agent 决定时才直接采用推荐。

### 15 秒

先按 [pacing-and-shot-density.md](#src-seedance-tvc-director-references-pacing-and-shot-density-md) 确认节奏档位：克制 3 至 5 镜、标准 5 至 7 镜、快节奏 7 至 10 镜。以下 4 个时间段是叙事任务，不等于只能有 4 镜：

| 时间 | 叙事任务 | 商业任务 |
|---|---|---|
| 0–3 秒 | 强视觉钩子与可见变化 | 立即连接产品、痛点或主张 |
| 3–7 秒 | 扩展情境与产品触发 | 让产品进入因果链 |
| 7–11 秒 | 结果与证明 | 给出最清楚的产品体验或证据画面 |
| 11–15 秒 | 收束、packshot、endboard | 回收品牌、主张和行动信息 |

不要把 30 秒故事压缩成十几个闪切镜头。若产品证明需要观察时间，减少场景而不是加快所有动作。

### 30 秒

使用 5 至 7 个叙事模块组织故事，再按 [pacing-and-shot-density.md](#src-seedance-tvc-director-references-pacing-and-shot-density-md) 展开实际镜头：快节奏商业版 14 至 18 镜、默认目标 16 镜；标准商业节奏 11 至 14 镜；克制电影节奏 8 至 10 镜。只有用户明确要求极简长镜头并且每镜持续发生高张力变化时，才进一步减少。以下时间表是模块结构，不是 6 镜脚本：

| 时间 | 叙事任务 | 商业任务 |
|---|---|---|
| 0–3 秒 | 强视觉钩子与第一次变化 | 抢占注意力并埋入产品主张 |
| 3–8 秒 | 展开钩子背后的世界或人物 | 锁定受众情境与欲望 |
| 8–14 秒 | 产品触发 | 让产品进入因果链 |
| 14–21 秒 | 材质、机制或体验证明 | 给产品足够观察时间 |
| 21–26 秒 | 情绪/功能兑现 | 回答前三秒提出的问题 |
| 26–30 秒 | hero shot、packshot、endboard | 主张、包装、Logo、CTA |

允许前后段不等长。当前所选模型无法稳定完成复杂动作、多角色对白或跨场景连续性，且用户接受多段方案时，才拆成多个生成段，再在剪辑中组成 30 秒成片；当前入口可用 Seedance 2.5 原生 30 秒且用户选择单段时，不因 Seedance 2.0 的 15 秒上限自动拆分。

先读取 [scene-progression.md](#src-seedance-tvc-director-references-scene-progression-md) 选择 1、2 或 3 个场景。用户要证明 30 秒长时叙事能力或明确要求画面更丰富时，优先用 2 至 3 个因果相连的场景，让变化来自新的情境、人物关系或行动目标，而不只是同一空间的红光、粒子和机位变化。

#### 30 秒丰富度规则

30 秒不是加长版 packshot。让画面经历以下六个层次中的至少五个：

1. `视觉钩子`：前三秒出现一个不能被普通产品替代的视觉问题或欲望。
2. `世界建立`：钩住之后再交代时间、空间、受众情境或品牌世界规则。
3. `产品触发`：产品通过使用、质地、声音或物理变化进入因果链。
4. `机制/材质证明`：用微距、运动、光线或真实反馈给产品观察时间。
5. `情绪/功能兑现`：展示变化后的状态，而非用旁白宣布效果。
6. `品牌回收`：hero shot、packshot 和 endboard 各司其职。

使用受控变化增加丰富度：

- 景别从环境到人物/产品，再到材质微距，最后回到 hero shot；
- 光线或色彩只有一条清楚的演变曲线；
- 声音从环境、产品触发、音乐发展到品牌尾音逐层递进；
- 转场由前一镜动作、光线、形状或声音触发，不使用无因果的随机蒙太奇；
- 每 4 至 6 秒必须出现新的故事信息或商业信息，不能重复同一动作。
- 每个 4 至 6 秒叙事模块按已选密度包含约 1 至 4 个镜头；模块是信息截止点，不是强制一镜到底。快节奏版必须在模块表旁写明计划镜头数，并另交付完整镜头表。
- 最终 packshot 之外，低运动构图约 2 秒内没有第二状态时应换镜或压缩；两个功能相同的人物氛围镜头不得连续出现。
- 前三秒钩子使用过的主要动作不得在 3–26 秒以相同景别和功能再次出现；为每段指定一个唯一动作和一个不能由其他段替代的新信息。

对只有一张产品图的任务，优先建立“产品周围的世界变化”，不要反复让产品旋转、开合或漂浮。通过环境尺度、材质微距、光线轨迹、液体运动和镜头景别变化丰富画面，同时保持产品本体稳定。

### 镜头表字段

每个镜头写清：

1. 时间范围；
2. 景别与机位；
3. 开始状态；
4. 唯一主要动作；
5. 镜头如何观察动作；
6. 环境或材质反馈；
7. 声音；
8. 产品/品牌任务；
9. 结束状态与下一镜接口。

### Packshot 与 endboard

把两者区分：

- `Hero reveal`：通过运动、光线、尺度或材质关系让产品进入品牌高潮，解决“产品怎样被看见”。
- `Packshot`：真实产品或包装的清楚展示，解决“卖的是什么”。
- `Endboard`：Logo、主张、CTA、法务信息的平面交付，解决“记住谁、下一步做什么”。

Hero reveal 与 packshot 若在结尾相邻，优先合并为一个连续品牌收束。有标准包装、瓶体或设备正面的产品，可用约 0.8 至 1.5 秒从局部或运动状态进入完整产品，再稳定约 3.5 至 4.5 秒。不要先安排一个完整产品 hero 模块，再接另一个几乎相同的完整正面 packshot；模型容易把两者合并成超长定帧。

这类 30 秒时间轴写明完整正面产品的最早出现时刻，通常不早于最后约 4.5 至 6 秒。品牌旁白可以先在人物兑现、手持情境或产品局部上开始，不能因为旁白念出品牌名就提前进入完整 packshot。

鲜食、餐饮、原料或服务品牌没有标准包装时，不虚构包装 packshot。用约 3 至 5 秒的成品、服务结果或消费体验 hero 完成产品回报，再接约 1 至 2 秒静态 endboard；精确 Logo、品牌字和 slogan 由后期使用获批资产完成。

Seedance 可以生成 packshot 氛围和相机运动，但精确包装文字、Logo 和版式默认由后期完成。若只有生成产品，没有真实产品参考，明确提示“概念预演，外观不可作为最终商业交付”。

### 声音结构

只保留服务主张的声音层：

- 对白/旁白：承担无法仅靠画面表达的关键信息；
- 环境声：建立真实空间；
- 产品声：强化触感、速度、开合、倒入、喷出或点击等证明；
- 音乐：控制情绪弧线，不替代动作节奏说明；
- 静默：用于揭示、反转或产品 hero moment。

避免在 15 秒内同时塞入长旁白、多句对白、复杂歌词和大量音效。

### 自定义时长

不按比例拉伸 15 秒或 30 秒模板。先确认准确总秒数和当前平台单次生成上限，再重新预算：

- 少于 3 秒：第一帧立即进入产品事件，在结束前同时完成产品和品牌识别；
- 3 至 14 秒：保留前三秒钩子，只选择一个主张和一次主要证明；
- 16 至 29 秒：在 15 秒骨架上增加真正的新情境、证明或关系变化，不重复动作填时；
- 超过 30 秒：按核心主张拆成多个连续段落，每段具有清楚开始与结束状态，并提供后期连接方式；若当前平台支持更长单次生成，可按实测能力改为单条提示词。

任何自定义时长都保持一个单一核心主张。长版本每 4 至 6 秒增加新信息，品牌收束时长根据总片长与交付复杂度分配，不能只在最后一帧闪现产品。

---

<a id="src-seedance-tvc-director-references-voiceover-md"></a>

## `seedance-tvc-director/references/voiceover.md`

## 旁白与声音模式

### 先让用户选择

在最终编译提示词前，明确提供三种模式：

1. `有旁白`：旁白承担核心主张、品牌态度或画面无法独立表达的信息。
2. `无旁白`：依靠画面、产品声、环境声和音乐完成理解，适合感官产品片与多地区无语言版本。
3. `同时生成两套完整版本`：一次交付有旁白版和无旁白版；保持同一创意母题，分别调整镜头停留与声音钩子，不能只删除音轨。

声音与时长、直出/九宫格选择互相独立。用户未指定时，先推荐一项并说明理由，再在统一配置确认中询问：`声音选择有旁白、无旁白，还是同时生成有旁白版和无旁白版？`

用户要求立即输出、不回答问题时，采用推荐模式并写明是可逆假设，同时给出另一模式会改变的镜头和声音位置。

### 何时推荐有旁白

- 核心主张较抽象，画面只能表达情绪，无法准确表达品牌态度；
- 有获批功效、技术、数据、成分或新品信息必须传达；
- 30 秒片需要完整叙事视角或品牌宣言；
- endboard 前需要一句可记忆的品牌收束；
- 用户明确要求旁白、口播文案、VO、slogan 或指定声线。

### 何时推荐无旁白

- 产品质地、动作和结果能够被画面清楚看懂；
- 目标是感官沉浸、国际通用 cut 或后续多语种版本；
- 15 秒信息很少，需要保留产品声和静默冲击；
- 没有任何获批品牌文案，旁白只能重复画面或编造主张。

### 写旁白

先确定：

- 叙述者：性别表达、年龄感、语言/口音、距离感；
- 语气：克制、亲密、理性、坚定、诗意或纪实；
- 功能：提出问题、连接镜头、解释证明或品牌收束；
- 文案状态：品牌获批、用户提供或 `【待补：获批旁白】`。

让旁白增加画面没有的信息，不逐句描述正在发生的动作。未验证功效、数据和绝对化表述不得因为写进旁白而获得豁免。

### 建立单一旁白真源

有旁白时，先建立全片唯一一张 `主旁白清单`，再写画面时间轴。旁白原文只允许在这张清单中完整出现一次：

| VO ID | 唯一原文 | 开始 | 硬停止 | 说话者 | repeat_count |
|---|---|---:|---:|---|---:|
| VO-01 | `【获批或示意文案】` | 1.20s | 3.40s | 同一名画外旁白 | 1 |

执行规则：

- 每句分配唯一 VO ID；默认 `repeat_count=1`。只有策略明确要求复沓时才改为大于 1，并为每次重复分别写时间窗。
- 镜头时间轴只写 `VO-01 进入`、`VO-01 硬停止`，不得再次粘贴原文。避免模型把每个场景内的同一句文字理解成一次新的发声请求。
- 各 VO 时间窗不得重叠；开始和硬停止必须是确定时间，不使用“随后、延续、适时结束”。
- 全片只有一个连续的旁白身份和声线，不因切换场景、景别或音乐段落而重置说话者。
- 一句到达硬停止点后，禁止重启、回声、复述、同义改写、补完尾字或跨入下一场景继续念；未分配 VO ID 的时间段只有音乐、环境声或产品声。
- 30 秒片的最后一句旁白优先在 29.0 秒前硬停止，至少留出约 1 秒纯音乐/产品尾音，避免在生成边界出现截断或尾句回声。
- 同一句品牌 slogan 若在画面字幕和旁白中同时出现，字幕交给后期；不要为了字幕再次向视频模型输入一遍同句发声指令。
- 主旁白清单之外不使用中文或英文引号包裹潜台词、角色想法、关系文案或口号，也不写 `人物用眼神表达某句完整的话`。将其改写为不可朗读的状态标签与动作，例如把潜台词改成 `关系状态：双方确认相同辣感；只有表演，无对白`。

最终编译前做两次审计：先去掉标点和空格后比较每条原文，任何相同或高度重合的句子若没有明确 `repeat_count`，都视为调度错误；再搜索主旁白清单之外的引号、角色冒号、口号和可朗读完整句，全部分配 VO ID 或改写为中性动作。

### 时长与节奏

- 为呼吸、产品声和品牌尾音留白；不要让旁白覆盖全片。
- 15 秒片通常只安排开场问题、一个主张和品牌收束。
- 30 秒标准商业片通常使用三至五个短句；快节奏有旁白版可使用五至七个更短的 cue，但每句都要增加新信息，不能靠同义复述制造密度。
- 完成后必须按目标语速朗读计时；以实际朗读时间为准，不依赖字数估算。
- 前三秒若旁白参与钩子，第一句必须与第一帧共同制造问题或欲望；若视觉钩子已强，允许先用产品声冲击，再在第 1 秒后进入旁白。
- 对齐画面后检查旁白空档。两句旁白之间若出现超过约 2.5 秒的低运动物流动作，先压缩画面，不用增加文案把无效时间填满；需要连接时只使用一次有因果的动作声或音乐节拍。
- 最后品牌旁白的进入点与完整 packshot 切点分开调度。品牌名可以先覆盖人物兑现、手持产品或材质局部；完整正面全瓶仍按结尾预算准时进入，避免模型因听见品牌名而提前数秒进入静态定帧。
- 旁白允许跨画面切点继续，但原文仍只在主旁白清单出现一次；镜头表只引用 VO ID 和既定硬停止。不要为了说明相邻镜头而重新粘贴同一句。
- 旅程、来路或多世界广告需要环境声床、音乐弧线与声音先行切时，读取 [shot-handoffs-and-sound-bridges.md](#src-seedance-tvc-director-references-shot-handoffs-and-sound-bridges-md)。目标声音可在源镜结尾约 0.3 至 0.6 秒提前进入，但不得让旁白、音乐或环境声在切点重启。

### 中段注意力接力

30 秒有旁白商业片不能只检查总字数，还要检查旁白在时间轴上的分布。完成主旁白清单后，单独审计约 `4.0–23.0s`：

1. 计算没有信息性旁白正在发声的最长连续区间；
2. 对每个超过约 `2.5s` 的空窗，写明由哪一个强事件接管注意力；
3. 若任一区间连续超过约 `4s`，既无信息性人声又无强接管事件，判为中段注意力断层并重排旁白、画面或两者；
4. 若约 `13–23s` 主要由第二轮人物体验或分享组成，至少安排两个功能不同的信息节拍，例如新的感官层与关系决定；有旁白模式下，至少一个节拍优先由中段 VO 推进，除非用户明确要求刻意长静默。

可作为强接管事件：

- 新的产品或风味证明；
- 清楚的破裂、喷发、落下、开合等强动作及其产品声；
- 新场景首次建立或人物作出可见决定；
- 音乐进入、抽空、反拍或峰值，同时与画面状态变化同步；
- 第一次出现且具有产品特异性的反应或关系兑现。

不能单独算作接管：普通硬切、持续不变的背景音乐、第二个人重复同样的入口和微笑、无因果凝视、轻微推轨、慢慢递盘或仅更换景别。

修复顺序：先删除或压缩重复画面，再把新增旁白分配给尚未表达的产品证据、感官顺序或关系推进；只有新增文案确实增加信息时才加 VO。目标是让人声、动作、产品声和音乐轮流接力，不是让旁白覆盖全片。

### 编译声音版本

#### 有旁白版

- 使用一张主旁白清单标注每句旁白的进入、停顿和硬停止位置；画面时间轴只引用 VO ID；
- 降低同期环境声和音乐，为人声留出空间；
- 把必须理解的品牌信息放进旁白，把可见动作留给画面；
- 明确旁白为画外音，避免模型生成不必要的口型。

#### 无旁白版

- 用产品声、动作声、环境声或音乐变化承接原旁白承担的节奏；
- 检查删除语言后，核心主张是否仍能被画面理解；
- 需要字幕解释才能看懂时，不应声称无旁白版已经成立。

#### 同时生成两套完整版本

- 一次交付两条独立完整的 Seedance 提示词，清楚标为 `有旁白版` 和 `无旁白版`；
- 两版共享核心主张、产品锁、人物身份和主要故事节点；
- 有旁白版为人声留出空间，无旁白版用产品声、环境声、音乐变化或静默重新设计节奏；
- 使用九宫格模式时可以共享同一套获批分镜状态，但允许为声音节奏调整镜头停留，不能把无旁白版定义为静音导出。

### 生成与后期边界

Seedance 内生音轨适合概念验证和节奏导引，不应默认承担逐字、逐秒、零重复的播出级配音责任。品牌文案必须逐字准确、不能多念一次或需要稳定声线时：

1. 仍在提示词中提供主旁白清单，用于控制画面节奏；
2. 将生成旁白视为 guide VO；
3. 用独立 TTS/真人配音按同一 cue sheet 生成正式音轨；
4. 后期替换 guide VO，并以转写时间码核对每个 VO ID 的出现次数。

成片复盘时先转写带时间码文本，再与主旁白清单逐条对齐。相同句子在两个不重叠时间窗出现，归为 `旁白调度/单一真源失败`，不是文案创意失败；只修声音指令或后期音轨，不自动推翻成功画面。

若转写出现主旁白清单之外的完整句子，先在提示词的画面描述、导演意图和声音总结中反查相同或近似措辞。找到后删除该句或改成状态标签；不能只追加“演员不说话”，因为可朗读文本本身仍可能被模型当作发声请求。

---
