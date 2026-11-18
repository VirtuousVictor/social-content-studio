# complete brief routing and concept methods

## Using this manual

Follow the [Skill entrypoint](../SKILL.md) for the requested deliverables, market, language, available evidence, approved assets and tool permissions. Project instructions and current host capabilities govern the examples below. Figures for timing, grid size, product exposure, model inputs and copy placement apply to the cited example or production preset. Choose the sections the brief needs. The [full source library](complete-professional-source-library.md) documents upstream wording and metadata.

---
## Adapted module: `tvc-ai-director/SKILL.md`


# TVC AI Director

Use this skill as the main router for a TVC AI production studio. Determine the project stage, identify missing information, route to the right internal production stage, and preserve handoff context across stages.

For any broader multi-model or multi-skill routing problem, apply the same readiness-gate logic as `the internal routing-readiness gates`: identify the required routing conditions first, ask for missing conditions, then route.

Default stance:

- Use the language requested for each deliverable. Carry over established project facts, aspect ratio, market, platform and approvals.
- For a new product, ask once for the missing facts that affect the requested work. A video plan may require a runtime and frame ratio. A copy-only post ordinarily requires neither.

## Routing Workflow

1. Classify the user request into one or more stages:
   - Brief and strategy: use `the internal brief-strategy stage`.
   - Creative concept and proposal: use `the internal concept-development stage`.
   - Director treatment: use `the internal director-treatment stage`.
   - PPM and production pack: use `the internal PPM and pre-production stage`.
   - Shot script and storyboard table: use `the internal storyboard-writing stage`.
   - AI image/video prompts: use `the internal image/video-prompting stage`.
   - Storyboard/prompt Excel workbook: use `the internal storyboard-writing stage` + `the internal image/video-prompting stage`, then export with `scripts/make_content_excel.py` or a spreadsheet tool.
   - AI production coordination: use `the internal AI-production coordination stage`.
   - Edit rhythm, sound, packaging, delivery: use `the internal editing and delivery stage`.
   - Client feedback and revision parsing: use `the internal client-review and revision stage`.

2. Review a sparse brief:
   - Extract all usable details from the brief, accessible references and project history.
   - Treat the intake questions below as prompts for the producer. Send the user only the ones that materially affect today's deliverable.
   - Where possible, deliver independent work now and mark any creative assumptions. Seek evidence before using an unverified claim.

3. Apply the general routing gate:
   - Before choosing any specialist, identify what conditions are required to route accurately.
   - If a missing condition changes the downstream specialist, output questions instead of routing.
   - If all required conditions are present, route with a short reason and handoff.

4. If the request spans stages and the brief gate is complete, create an execution chain before working:
   - Example: `brief -> concept -> treatment -> storyboard -> AI prompt -> production -> editing -> review`.
   - Run the current highest-leverage stage first unless the user names a specific deliverable.

5. Load shared references only when needed:
   - `references/complete-brief-routing-and-concept-methods.md`: stage map, routing triggers, handoff format.
   - `references/complete-production-review-and-delivery-methods.md`: quality checks for strategy, craft, AI continuity, review, delivery.
   - `references/complete-production-review-and-delivery-methods.md`: category-specific defaults.
   - `references/complete-visual-assets-and-image-prompt-methods.md`: image/video prompt discipline.
   - `references/complete-production-review-and-delivery-methods.md`: client-facing language and feedback interpretation.

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

## Router Decision Rules

- When the brief leaves a material decision open, identify the missing decision and reuse the project profile before asking.
- If route choice depends on missing context, ask the routing-gate questions before handing off to another internal production stage.
- If the user asks for "提案", "创意", "方向", "方案", route to concept after brief diagnosis.
- If the user asks for "导演阐述", "影调", "镜头语言", "参考片", route to treatment.
- If the user asks for "PPM", "演员", "服装", "美术", "音乐参考", "拍摄准备", route to PPM.
- If the user asks for "分镜", "镜头脚本", "shot list", route to storyboard.
- For a prompt, use shot prompting. Add production coordination only for a requested generation run, batch, or handoff.
- Put a storyboard table in the requested format. Use the table exporters for explicitly requested CSV or XLSX files.
- If the user asks for "剪辑", "节奏", "音乐", "声音", "包装", "交付", route to editing.
- If the user pastes client comments, route to review interpreter before editing.

## Brief intake checklist

Use the following as a question bank for the missing decisions that matter for the current project.

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

For a missing decision that prevents the requested work, a concise question can use this format:

```markdown
当前信息判断：
为什么需要补充：
请先确认以下问题：
1. ...
```

## Output Rules

- Be production-practical: tables, lists, scripts, prompts, and revision matrices should be directly usable.
- Preserve brand, product, actor, wardrobe, prop, location, light, and color continuity.
- For AI prompts, include duration, ratio, camera, subject, product, motion, lighting, tone, sound cue if relevant, and negative constraints.
- For client-facing text, separate internal diagnosis from external wording.
- End with a concrete next-stage handoff when the task is part of a chain.

## Templates and Tools

- Use `assets/templates/` when the user needs copyable tables for brief, proposal, treatment, PPM, storyboard, prompt, edit, or review.
- Use `scripts/make_content_tables.py` to convert tab-separated rows with a header into CSV.
- Use `scripts/make_content_excel.py` when converting a TSV storyboard/prompt table into a lightweight `.xlsx` workbook without external dependencies.
- For polished multi-sheet `.xlsx` workbooks, prefer the available spreadsheet runtime/tooling; include at minimum:
  - `分镜+Prompt` sheet with shot timing, frame content, camera, product/logo, sound, image prompt, video prompt, negative constraints, continuity lock, and regeneration notes.
  - `全片一致性` sheet with product, actor, location, color, camera, and forbidden-drift anchors.
  - `执行检查清单` sheet for production/AI-generation QA.

## Quality Gate

Before finalizing, check:

- Does the output match the user's current stage?
- Are missing assumptions named instead of hidden?
- Can the next internal production stage continue from the handoff?
- Does the plan protect actor/product continuity for AI generation?
- Are client review items translated into actionable production changes?


## Adapted module: `tvc-ai-director/references/tvc-workflow-map.md`

# TVC Workflow Map

Use this map to decide stage, internal production stage and handoff.

## Stage Routing

| Stage | User signals | Specialist | Output |
| --- | --- | --- | --- |
| Brief | brief, 需求, 产品, 人群, 渠道, 预算, 片长 | `the internal brief-strategy stage` | Brief 诊断, 策略任务, 创意方向 |
| Concept | 提案, 创意, 方向, 概念, slogan, 故事 | `the internal concept-development stage` | 创意路线, 脚本结构, 汇报话术 |
| Treatment | 导演阐述, 影调, 节奏, 镜头语言, 参考片 | `the internal director-treatment stage` | 导演阐述, 影像风格, 执行方法 |
| PPM | PPM, 演员, 服装, 化妆, 美术, 音乐参考, 道具 | `the internal PPM and pre-production stage` | PPM pack, 确认项, 物料清单 |
| Storyboard | 分镜, 镜头脚本, shot list, 景别, 时长 | `the internal storyboard-writing stage` | 分镜表, 节奏表, 连续性提醒 |
| AI prompt | prompt, 生图, 生视频, Midjourney, Runway, 可灵, 即梦 | `the internal image/video-prompting stage` | 图像 prompt, 视频 prompt, 负面约束 |
| AI production | 执行, 批次, 版本, 生成失败, 一致性 | `the internal AI-production coordination stage` | 批次表, 物料表, 返工规则 |
| Editing | 剪辑, 节奏, 音乐, 声音, 包装, 交付 | `the internal editing and delivery stage` | 剪辑时间线, 声音设计, 交付清单 |
| Review | 审片, 客户意见, 修改, 反馈, 不够高级 | `the internal client-review and revision stage` | 意图解析, 修改动作, 回复建议 |

## Common Execution Chains

- New vague request: `brief -> concept`.
- Pitch deck request: `brief -> concept -> treatment`.
- PPM request after concept approval: `treatment -> ppm`.
- AI execution request: `storyboard -> ai prompt -> ai production`.
- Full AI TVC: `brief -> concept -> treatment -> storyboard -> ai prompt -> ai production -> editing -> review`.
- Client revision: `review -> editing` or `review -> ai prompt -> ai production -> editing`.

## Sparse Brief Gate

For a new brief with limited materials, consult the question bank below. Omit answered or irrelevant questions.

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

Once the information for the requested stage is sufficient, continue directly to that stage.

## Universal Handoff

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

## Must-Ask Threshold

Ask about the following only when the missing information materially changes the requested output:

- Product truth, claim legality, logo/package accuracy.
- Aspect ratio direction, target audience, or channel.
- Duration, ratio, or delivery deadline.
- Talent identity, product reference, or required visual asset.
- Client-mandated reference, taboo, or approval condition.

Carry unanswered optional questions forward only if a later deliverable requires them.


## Adapted module: `tvc-brief-strategist/SKILL.md`


# TVC Brief Strategist

Use this skill to turn an incomplete TVC request into a strategic brief that creative, treatment, storyboard, and AI production work can use.

## Workflow

1. Extract known facts:
   - Brand, product, category, target audience, business goal, communication task.
   - Required duration, ratio, channels, deadline, budget level, mandatories, forbidden elements.
   - Product claims, proof points, competitors, brand tone, existing assets, reference films.

2. Diagnose gaps:
   - Mark each gap as `must ask`, `can assume`, or `not needed yet`.
   - For a new or sparse brief, ask once for essential gaps. Confirm the aspect ratio only when framing affects delivery and the project leaves it open.
   - Proceed to the appropriate stage when its inputs are available.

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

## Required Brief Gate

Choose relevant items from this question bank when the request calls for a new production brief:

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

When follow-up is needed, briefly state the decision that is open and ask for the missing information.

## Quality Bar

- Do not write final scripts before the communication task is clear.
- Develop proposals from the verified facts and material decisions that are known.
- Separate product truth from emotional promise.
- Keep proposal directions meaningfully different, not cosmetic variations.
- Name legal, claim, talent, product, or channel risks early.


## Adapted module: `multi-model-router/SKILL.md`


# Multi Model Router

Use this skill before routing a task across multiple models, agents, tools, or internal workflow stages.

Core rule: do not route just because a downstream option exists. First identify what information is required to choose correctly. If required routing conditions are missing, ask the user before delegating.

## Routing Readiness Workflow

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

## Required Question Design

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

## Routing Gate Template

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

## Anti-Patterns

- Do not route from keywords alone when downstream choices require business context.
- Do not invent defaults for legal, brand, claim, customer, safety, finance, or delivery constraints.
- Do not ask a long questionnaire when one missing decision controls the route.
- Do not send a task to a creative/execution model before strategy-critical gates are answered.
- Do not continue a multi-step chain if an upstream gate is unresolved.

## Examples

Sparse TVC brief:
- Identify which missing decisions affect this specific film. Ask for those together.

Model choice for writing:
- Need audience, format, tone, length, source material, and factual-risk tolerance.
- If missing, ask before choosing short-form copywriter, long-form writer, editor, or fact-checker.

Design/code routing:
- Need target platform, existing code/design system, viewport, user workflow, and implementation vs mockup intent.
- If missing, ask before routing to design, frontend implementation, or review.

Data-analysis routing:
- Need data source, metric definition, time range, output format, and decision purpose.
- If missing, ask before routing to SQL, spreadsheet, charting, or narrative analysis.


## Adapted module: `multi-model-router/references/router-gate-patterns.md`

# Router Gate Patterns

Use these patterns to design gate questions for any routed workflow.

## Creative Production

Required:

- Channel and format.
- Audience.
- Brand or product truth.
- Mandatory/forbidden elements.
- Available assets.
- Approval constraints.
- Output type.

## Technical Implementation

Required:

- Target environment.
- Existing codebase or blank build.
- Framework/runtime constraints.
- Expected behavior.
- Acceptance tests.
- Mutation permission.
- Deployment or local-only target.

## Content Writing

Required:

- Audience.
- Purpose.
- Source material.
- Length and format.
- Tone.
- Distribution channel.
- Claims or forbidden phrasing.

## Model/Tool Selection

Required:

- Is the task reasoning, generation, transformation, retrieval, execution, or verification?
- Is freshness required?
- Are tools or files needed?
- Is output high-stakes?
- Is the user asking for speed, quality, safety, or exact formatting?

## Revision Work

Required:

- Original artifact.
- Feedback source.
- Desired change.
- What must be preserved.
- Approval target.
- Deadline or versioning constraints.


## Adapted module: `tvc-concept-developer/SKILL.md`


# TVC Concept Developer

Use this skill to build a creative proposal that explains **why the product should be expressed this way through video language**.

This is not a storyboard skill. Do not focus on shot-by-shot execution. Focus on the strategic and emotional logic behind the creative direction: why this idea, why this story, why this tone, why this visual language, and why the consumer will believe it.

## Core Stance

- Write for a client-facing creative pitch.
- Prioritize "为什么这样拍" over "具体怎么拍".
- Translate product features into human emotion, social context, and video language.
- Treat the product as the source of the film's meaning, not a prop pasted into the ending.
- Use references when the proposal needs mood, category proof, cinematic tone, or key visual explanation.

## Workflow

1. Confirm the brief is ready:
   - Check audience, channel, product proof, mandatory assets and restrictions as relevant to the selected proposal. Ask for missing facts only if they affect the brief.

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
   - To `the internal director-treatment stage` for execution style.
   - Hand off the established story and visual direction to storyboard. Pause for a separate approval when the brief calls for one.

## Proposal Structure

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

## Reference Search Rules

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

## Quality Bar

- The insight must reveal a real consumer psychology, not a category cliché.
- The creative idea must be expressible in one strong sentence.
- The concept must prove why the idea solves the brief.
- The story outline must not become a shot list.
- Key visuals must clarify mood, not decorate the deck.
- Communication mapping must prove the idea is not random.
- Deliverables must match channel and campaign needs.


## Adapted module: `tvc-concept-developer/references/proposal-logic.md`

# TVC Creative Proposal Logic

Use this reference when the user asks for 创意提报, creative proposal, concept deck, pitch structure, or campaign route expansion.

## What This File Is

The creative proposal answers "why this film should exist". It is not a production board. It explains the strategic, emotional, and visual logic that makes the execution believable.

## The Eight Sections

### 1. Project Understanding

Prove that the brief was heard correctly:

- Brand situation.
- Product selling point.
- User context.
- Communication goal.

Good writing should translate facts into stakes. Example: "The brand is not only selling iced tea. It is trying to own a summer emotional reset moment."

### 2. Insight

Find the psychological hinge.

Weak insight: "Young people feel hot in summer."  
Better insight: "For young women in summer social scenes, heat is not only temperature. It is makeup anxiety, low battery mood, and loss of control over one's state."

### 3. Creative Idea

One sentence that can hold the whole campaign.

Include:

- Key Message.
- Slogan or campaign theme when allowed.
- A clear promise, not a vague mood.

### 4. Creative Concept

Explain:

- Why this topic.
- Why this solves the communication problem.
- Why the audience will believe it.
- What keywords define tone.
- What visual/mood references support it.

### 5. Story Outline

Write a story synopsis, not a storyboard:

- Character or situation.
- Conflict.
- Turning point.
- Product role.
- Emotional landing.

### 6. Key Visual

Use a small number of powerful visual anchors:

- AI concept image.
- Film frame.
- Photography reference.
- Product composition.
- Color and lighting mood.

### 7. Communication Mapping

Prove the route:

```text
Insight -> Creative Theme -> Story Expression -> Product Integration -> Brand Memory
```

### 8. Deliverables

Define campaign assets:

- 60s TVC.
- 30s Cutdown.
- 15s Cutdown.
- KV.
- Social posts.
- Behind-the-scenes or AI-process assets if relevant.

## Reference Use

References should answer a client question:

- What does the mood feel like?
- What kind of world are we entering?
- What level of craft do we mean?
- How does the visual metaphor work?
- Why will this platform audience stop scrolling?

Do not use references as decoration.
