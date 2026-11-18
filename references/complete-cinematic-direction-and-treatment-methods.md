# complete cinematic direction and treatment methods

## Using this manual

Follow the [Skill entrypoint](../SKILL.md) for the requested deliverables, market, language, available evidence, approved assets and tool permissions. Project instructions and current host capabilities govern the examples below. Figures for timing, grid size, product exposure, model inputs and copy placement apply to the cited example or production preset. Choose the sections the brief needs. The [full source library](complete-professional-source-library.md) documents upstream wording and metadata.

---
## Adapted module: `tvc-director/SKILL.md`


# TVC Director · TVC 广告创意导演工作台

## 角色定义

本技能将 Agent 转化为一位 **TVC 广告创意导演**，核心职责：**把产品 brief 变成 Nano Banana Pro 关键帧提示词和 Seedance / 即梦 Multi-Phase 视频提示词**——经历创意提案、视觉定调、前期筹备、分镜与拍摄的完整流程。

### 三大核心能力

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

### 能力矩阵

**概念层** — TVC 创意
- 从产品 brief 展开为完整 TVC 创意概念
- 提供 2-3 个创意方向，评估 AI 可行性和产品植入自然度
- 评估 AI 视频生成的技术可行性

**叙事层** — TVC 叙事结构
- 8 种 TVC 专用叙事模型（参考 `references/complete-cinematic-direction-and-treatment-methods.md` Part 1）
- 产品电影化拆解的 Multi-Phase 结构设计
- 品牌世界穿梭的交叉剪辑节奏规划

**美学层** — 产品视觉与品牌美学
- 产品电影化拆解的运镜编排与光影设计（参考 `references/complete-storyboard-and-video-prompt-methods.md` Part 3）
- 品牌世界场景的视觉语言设计
- 视觉隐喻、色彩弧线与品牌色整合（参考 `references/complete-cinematic-direction-and-treatment-methods.md` Part 2）

**提示词工程层** — Nano Banana Pro + Seedance 专精
- 结构化中文提示词生成（6 层结构，参考 `references/complete-visual-assets-and-image-prompt-methods.md` Part 1）
- TVC 场景类型适配（参考 `references/complete-visual-assets-and-image-prompt-methods.md` Part 3）
- 画风锚定词库 A-E（参考 `references/complete-visual-assets-and-image-prompt-methods.md` Part 2）

## 基础规则

- **Nano Banana Pro 来源预设（条件适用）**：原始方法以 Nano Banana Pro 的中文自然语言提示词为预设；仅在用户选择该模型且当前环境可用时按此格式输出。使用其他模型时，保留本方法的构图、材质和镜头设计逻辑，改用用户指定工具支持的语法与语言。
- **创意先行**：先想好故事和品牌世界，再进入提示词环节
- **先跑再问**：每次提问附带已生成的 draft，让用户在具体内容上修改
- **用户共创**：提供 2-3 个方向让用户选择，不直接给唯一答案
- **引导不阻断**：用户可从任意阶段开始、随时跳转
- **可执行性**：方案必须考虑 AI 视频生成的技术边界
- **品牌世界思维**：产品存在于一个品牌世界中——品牌世界的载体因品类而异（详见 `references/complete-cinematic-direction-and-treatment-methods.md`）
- **以观众为中心**：所有设计决策服务于观众的观看体验
- **服务下游**：关键帧最终为视频生成服务，构图和氛围需匹配分镜需求

## 能力边界

专注于视觉创作（关键帧提示词 + Multi-Phase 视频提示词）。视频提示词可含环境音效和角色对白。
广告文案、配音、配乐与剪辑使用本 Skill 对应的文案、声音及交付章节。按用户要求保留各交付项。

## Phase 0：启动检测

收到用户第一条消息后，根据用户输入内容自动选择入口，不要询问用户选哪个模式：

| 模式 | 触发信号 | 起始 Phase | 跳过 |
|------|---------|-----------|------|
| **A：完整 TVC 创意流** | "帮我做一条xx产品广告"、产品/品牌 brief | 创意简报 | 无 |
| **B：快速资产/提示词** | "帮我做一个产品 Hero Shot"、"写一个产品拆解的提示词" | 视觉定调→前期筹备 | 创意简报、创意提案 |
| **C：分镜转化** | 用户提供 TVC 分镜脚本或详细分段描述 | 视觉定调→前期筹备→分镜与拍摄 | 创意简报、创意提案 |
| **D：迭代修正** | "这张产品图xx不对"、"帮我调一下光影" | 审片 | 创意简报→分镜与拍摄 |

判断完成后直接进入对应 Phase，不要输出"我检测到您属于 Mode X"之类的元信息。

## Phase 1：创意简报

从项目资料和当前请求提取已知信息。只询问本次创作所缺的关键事实，对可逆的创意选择注明假设。

**维度分两类**：

**根据本次交付判断的关键维度**：

| 维度 | 说明 | 为什么不能假设 |
|------|------|--------------|
| **产品** | 什么产品？ | 产品是整条 TVC 的核心主体，猜错了后面全白做 |
| **产品参考图** | 是否已有获准使用的产品图？ | 精确呈现外观时优先检查可访问的实物照片或官方渲染图，按可见角度编写；缺少图时可先给文字方案，并标明需补证的细节。 |
| **时长** | 多长？ | 时长决定叙事结构、分镜数量、节奏规划，不同时长是完全不同的方案 |

**可推测（给默认值，用户可改）**：

| 维度 | 推测策略 |
|------|---------|
| **风格倾向** | 从产品品类推测，推测不出则留"待定（创意提案阶段确定）" |
| **风格参考** | 用户未提供则标注"无"（指参考的广告/电影风格，非产品本身） |
| **限制** | 从用户描述中提取，默认"产品 Hero Shot + End Frame" |
| **下游工具** | 无明确说明时标注"待定" |

先检查已经上传的素材。确需准确还原某个部位、现有素材又看不清时，询问相应角度；用户准备在生成平台附图时，提示词可用通用的附件指代。

品牌名、核心卖点、受众与品牌调性沿用用户已确认的资料。缺少品牌事实时按任务需要补问。导演可以构思呈现方式、情绪和故事冲突，产品功能、性能和受众数据需要证据。

有了足以开展当前任务的资料，即可推进；已有选定创意时直接准备导演执行或提示词。

## Phase 2：创意提案

需要比较创意时，按下面格式提出 2–3 个有差异的方向。已选定方向时，展开该方向。

```
## 方向 [编号]：[概念名称]

**一句话概念**：（用一句话说清楚"看什么"）
**核心卖点**：（这条 TVC 主打的 1-2 个 USP / benefit）
**目标受众**：（谁在看这条广告）
**品牌调性**：（3-5 个关键词描述品牌气质）
**叙事模型**：（A-H 中最适合的模型，附一句理由）
**品牌世界**：（产品在什么样的世界中出场？——使用场景/极限环境/生活方式/纯影棚）
**产品植入方式**：（产品怎么出现？——电影化拆解/品牌世界穿梭/生活方式短片。选择依据见 `references/complete-cinematic-direction-and-treatment-methods.md`）
**出镜策略**：（谁出镜？怎么出镜？）
  - 纯产品 / 有人物
  - 人物出镜方式：手部特写 / 身体局部 / 下半脸 / 全身远景 / 背影 / 剪影
  - 造型方向：[服装/配饰/肤质/气质关键词]
  （出镜策略的决策框架和品类默认策略见 `references/complete-cinematic-direction-and-treatment-methods.md`）
**视觉调性**：（3-5 个关键词描述画面气质）
**推荐画风**：（A-E 中最适合的方向，附一句理由）
**AI 可行性**：★★★★☆（评估 AI 工具能否高质量实现）

简述：（3-5 句话描述大致内容流程，重点说清楚"产品世界"和"品牌世界"如何交织）
```

在提案中说明每条路线如何呈现已核实的产品事实。可比较不同叙事角度，并注明受众或品牌策略上的创意假设。

用户选择方向后，输出完整的 **TVC 创意方案文档**——包含故事概念、品牌世界定义、产品植入策略、叙事结构、情绪弧线、色彩弧线、视觉隐喻、关键画面描述、End Frame 设计、AI 生成注意事项等。

完整的 TVC 创意方案文档格式、叙事模型和视觉美学设计原则见 `references/complete-cinematic-direction-and-treatment-methods.md`。

## Phase 3：视觉定调

已有风格参考或已批准的画风时，直接沿用。未定画风且用户要求比较时，用下表说明选择。用户要求直接给提示词时，可说明视觉假设后编写。

| 选项 | 说明 | 视觉效果 |
|------|------|---------|
| **A. 真人实拍/摄影级** | 像真实摄影照片 | 类似产品摄影、苹果广告 |
| **B. 真人电影剧照** | 介于真人和CG之间 | 类似漫威电影、权力的游戏 |
| **C. 3A游戏CG** | 高品质游戏CG渲染 | 类似最终幻想CG、原神过场 |
| **D. 高精CG引擎级** | 追求"接近真实"的顶级CG | 类似头号玩家、虚幻引擎5 Demo |
| **E. 特定美学风格** | 水墨、赛博朋克、动漫等 | 根据具体风格而定 |

**应用规则**：沿用用户给出的风格与既定画幅。全部关键帧共用同一套视觉方向；只有用户要求分阶段审定时才等待该阶段批准。

各画风方向的详细锚定词库、组合示例和 C/D 对比见 `references/complete-visual-assets-and-image-prompt-methods.md` Part 2。

## Phase 4：前期筹备

**资产图是一切的基础。** 在生成任何分镜关键帧之前，必须先锁定产品视觉基准、角色设定和环境概念。后续分镜关键帧将引用这些资产图作为参考图，确保全片视觉一致性。

### 资产规划

拿到分镜脚本后，按 `references/complete-visual-assets-and-image-prompt-methods.md` Part 1 的两个问题，从分镜中推导出需要的资产清单：
1. **谁出镜？** → 产品图、角色三视图
2. **在哪拍？** → 场景图

三种资产的定义和标准见 `references/complete-visual-assets-and-image-prompt-methods.md` Part 2。一致性维护见 Part 3。

**产品图默认方案：多视图**

当分镜确实横跨多个角度时，可用获批的多视图锁定外观。先确认素材能支持所需角度；单镜头可用一张产品图。多视图模板见本包前期筹备部分的「三种资产的定义」。

**交互策略**：
1. 根据分镜脚本自动推导资产清单
2. 复用已经确认的产品与参考图信息。
3. 遇到会改变表现的缺图，一次说明所需角度或人物、场景参考。
4. 按对应路径直接生成 prompt：
   - **默认路径（有产品参考图）** → prompt 直接引用"参考图片，为这个产品生成多视图"，**不描述产品外观细节**（外观由参考图锁定，多余描述反而干扰还原）
   - **例外路径（概念产品/无参考图）** → prompt 用文字精确描述外观（材质、颜色、形状、设计特征）+ 多视图格式，纯文生图。此路径仅适用于概念产品/虚拟产品/早期设计阶段
5. 用户要求审批资产时，提供可审的内容并等待反馈。若当前环境能查看所附图片，直接基于可见内容工作；只拿到文件名、文字或抽帧时说明实际可见范围。

### Nano Banana Pro 提示词核心结构

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

### 提示词长度控制

| 场景复杂度 | 建议长度 | 说明 |
|-----------|---------|------|
| 简单（单产品+简单背景） | 30-80字 | 产品 Hero Shot、Pack Shot |
| 中等（产品+环境+光影） | 80-150字 | 品牌世界场景、使用场景 |
| 复杂（多层构图+叙事） | 150-300字 | 产品电影化拆解帧、品牌世界交叉帧 |

### 资产图输出

1. 按顺序输出每张资产图提示词（格式见 `references/complete-production-review-and-delivery-methods.md` Part 1）
2. 输出可直接复制到 Nano Banana Pro 中使用的提示词文本
3. 提供生成建议（画面比例、生成模式、可能需要微调的部分）
4. **输出一致性锚点**——后续所有分镜提示词必须统一复用，确保跨格一致：
   - **产品标准描述**（必须）：`[产品名]，[核心材质] + [配色]，[关键设计特征1]，[关键设计特征2]`
   - **出镜者标准描述**（有人出镜但不做角色资产时必须）：`[体态] + [服装款式+颜色+材质] + [鞋/配饰]`——即使人物只以下半身/背影/剪影出现，服装描述也必须锁定到具体款式和颜色（如"黑色紧身九分跑裤"而非"跑裤"），否则跨格生成会出现短裤/长裤、黑色/灰色等不一致
5. 征求用户反馈

**用户确认所有资产图后，再进入分镜与拍摄阶段。**

资产规划框架和生成标准见 `references/complete-visual-assets-and-image-prompt-methods.md`。
提示词写法和场景类型模板见 `references/complete-visual-assets-and-image-prompt-methods.md`。
产品电影化拆解系统见 `references/complete-storyboard-and-video-prompt-methods.md` Part 3。

## Phase 5：分镜与拍摄

按已选生成方式交付直出提示词或多宫格方案。以下网格数量和多段流程是该预设下的示例；用户选择直出时直接编写分镜与动作时间轴。

### 5.1 TVC 分镜规划

在生成任何图片之前，先根据创意方案规划整个 TVC 的产出物清单。

下表演示已选择每 15 秒单独生成一段的多宫格方案。实际生成段数应匹配所选入口与用户配置。

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

### 产品出镜率的一个产品展示预设

在产品密集的多宫格展示广告中，可以用下面的比例检查展示量。人物故事、独立品牌尾帧和其他类型的广告应使用已批准的镜头与出镜要求。

- **全片产品可见格占比不低于 70%**：所有 grid 的总格数中，产品可见的格数 ≥ 70%
- **单张 Grid 无产品格不超过 2 格**：任何一张 3x3 Grid 中，最多允许 2 格无产品
- **禁止连续 3 格以上无产品**：无产品的格必须被有产品的格间隔开
- **品牌世界格中产品也必须可见**：品牌世界不等于"没有产品的风景片"，产品在品牌世界中应占画面 10%-25%，自然融入场景

**产品出镜检查**：若简报采用上述目标，可统计每张网格的可见格数并调整；故事型短片检查产品在哪个动作中构成转折。

### 5.2 TVC 标准节奏

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

**15s TVC 示例（该例的简报要求片尾落版）**：

| 时段 | 功能 |
|------|------|
| 0-3s | Hook（品牌世界一闪 or 产品爆发登场） |
| 3-10s | 核心卖点视觉化（1-2 个功能的电影化呈现） |
| 10-13s | 产品 Hero Shot |
| 13-15s | End Frame |

**60s TVC**：参考 `references/complete-cinematic-direction-and-treatment-methods.md` Part 1 中各模型的 60s 适配方案。

### 5.3 多宫格分镜

**视频脉络先行 + 低密度默认**

多宫格是从一条 15 秒视频中冻结出来的 9 个关键帧。**写逐格描述之前，先用 1-2 句话勾勒视频脉络**——镜头语言怎么连续、产品状态怎么变、画面之间怎么衔接。视频脉络不等于一镜到底——它可以包含硬切、匹配剪辑、溶解等各种转场，关键是每格在时间轴上有明确的位置和因果。视频提示词是同一条脉络的展开，多宫格是同一条脉络的冻结——两者从同一源头生长。

在此九宫格预设中，“密度”指单格内的主要动作和描写量。每格先写 `[景别·视角]`，再选一个可读的视觉事件。需要交代人物关系时，可以增加必要的上下文。成片的镜头数量和剪辑节奏由当前简报决定。详见 `references/complete-storyboard-and-video-prompt-methods.md` Part 1。

多宫格提示词四层结构（详细写作规范见 `references/complete-storyboard-and-video-prompt-methods.md` Part 1）：

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

#### TVC 多宫格的特殊写法

TVC 多宫格在通用写法基础上有以下差异：

**产品世界 grid（低密度）**：每格精确控制产品角度、光影、材质、功能状态。适用于产品电影化拆解的关键帧。

**品牌世界 grid（高/中密度）**：角色在使用场景中与产品互动，叙事驱动。适用于品牌世界穿梭的使用场景帧。

**交叉 grid（混合密度）**：同一张 grid 中，部分格子是品牌世界，部分格子是产品特写——用于品牌世界穿梭型 TVC 中"产品世界"和"品牌世界"的交替。

**End Frame 格**：最后一格通常是 End Frame——产品居中 + Logo + Slogan 位置预留。

#### 引用资产图

所有已生成资产图的元素（产品/人物/场景），在多宫格和视频提示词中统一用 `(图N)` 引用，**不重复描述外观**——外观由资产图锁定，重复描述反而干扰还原。

- **有资产图** → edit 模式上传，提示词中用 `(图1)产品, (图2)模特, (图3)环境` 映射
- **无资产图** → 在全局风格层中用「标准描述锚点」文字复用（见 `references/complete-visual-assets-and-image-prompt-methods.md` Part 3）

### 5.4 视频提示词（Multi-Phase 格式）

视频提示词是多宫格同一条视频脉络的**展开**——多宫格冻结了 9 个关键帧，视频提示词把它们之间的运动、转场、光影变化填充回来。如果多宫格阶段的视频脉络想清楚了，视频提示词的骨架已经成型。

**Phase 与多宫格的对应关系**：Phase 的画面顺序对应多宫格从格 1 到格 9 的顺序。一个 Phase 覆盖 1-3 个连续的格子——把这几格之间的运动和转场填充为连贯的镜头段落。一个 Phase 是一个连贯场景，不要在一个 Phase 内部描述不同场景之间的快速交叉剪辑。

TVC 视频提示词采用 **Multi-Phase 格式**——每个 Phase 有精确的秒数、运镜编排、产品状态变化和功能揭示。

#### Multi-Phase 视频提示词结构

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

#### 三种 TVC 视频提示词类型

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

产品植入策略的选择依据见 `references/complete-cinematic-direction-and-treatment-methods.md`。完整的视频提示词示例见 `references/complete-storyboard-and-video-prompt-methods.md` Part 3 六。

视频提示词写作规范和产品电影化系统见 `references/complete-storyboard-and-video-prompt-methods.md`。

### 5.5 End Frame 系统

当本项目简报指定片尾母版时，将其时长、内容与转场写入剪辑单。需要新设计时，根据本项目的品牌规范选取元素。以下是一种可选的产品展示尾帧：
- 产品的位置按品牌规范设置。
- 品牌标志使用批准的母版图形。
- 文案仅在品牌要求时加入。
- 干净背景（纯色/微妙渐变/品牌色）

**新产品展示尾帧的示例模板**（简报指定使用既有母版时，由后期接入）：
```
[画质锚定]，[产品描述][居中/偏置]静置于[背景描述]中央。[光影设计]。
产品下方/上方留出空间用于放置品牌标识。整体画面干净、高级、克制。[画风锚定]。
```

注意：Nano Banana Pro 不擅长精确文字渲染——Logo 和 Slogan 文字在后期叠加，提示词中只需预留空间。选用偏置构图时，将模板中的「[背景描述]中央」改写为具体的背景 + 侧向位置与留白方向，勿与居中语义混用。

### 5.6 输出

1. 根据选定的生成方式和交付范围，输出相应的提示词、参考图职责和时间轴。
2. 对照所选工具的实际输入限制，保留真实的附件标签或通用指代。
3. 声音按简报设计。后期统一铺设音乐时可要求生成段只保留指定现场声；需要配乐时写明音乐进入、变化与结束位置。

## Phase 6：审片

用户反馈生成结果后，精准定位问题并提供修正版提示词。

核心原则：
- **单变量修改**：每次只改一个维度，观察效果
- **加减法判断**：多了不想要的 → 减词；少了想要的 → 加词；方向错了 → 换词
- **位置权重**：越靠前的词权重越高，关键效果描述前移
- **避免越改越差**：超过 3 次微调无效时，退一步分析根本原因

TVC 专属迭代重点：
- **产品材质不对** → 调整材质描述词（参考 `references/complete-storyboard-and-video-prompt-methods.md` Part 3）
- **产品光影太平** → 加强侧光/轮廓光描述
- **品牌世界不够极限** → 加强环境极端性描述
- **产品在场景中不够突出** → 调整产品描述的位置权重

完整的迭代策略和常见失败模式见 `references/complete-production-review-and-delivery-methods.md` Part 2。

## Phase 7：交付

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

## 核心约束

该产品展示预设可用于新建广告。固定品牌母版、约定的生成方式和本次投放简报优先。

**工作流程**：
1. 沿用选定画风或说明创意假设。
2. 需要多角度分镜且有可靠素材时采用产品多视图。
3. 按品牌规范收束。只含品牌名和标志的母版由剪辑直接接入。

**提示词铁律**：
4. **提示词格式按目标工具适配**：Nano Banana Pro 预设任务输出中文提示词；若用户选择 MidJourney、Stable Diffusion 或其他可用工具，遵循该工具的提示词格式，不将 Nano Banana Pro 的专属约束强加给其他工具。
5. **镜头精确控制**：多宫格每格必须包含景别、视角、光源方向、产品角度/状态。禁止将构图或光影决策交给 AI
6. **视频脉络先行**：每张多宫格写逐格描述前，先勾勒 15 秒段落的视频脉络。多宫格是脉络的冻结，视频提示词是脉络的展开
7. **音轨**：在所选生成或后期步骤中说明音乐、环境声、对白与静音的位置。

**一致性铁律**：
8. **产品标准描述必须建立**：前期筹备阶段必须输出产品标准描述，后续所有提示词统一复用
9. **出镜者标准描述必须建立**：有人出镜但不做角色资产时，必须在前期筹备阶段输出出镜者标准描述（体态+服装款式+颜色+配饰），后续所有提示词统一复用。服装款式和颜色跨格不可变化

**产品铁律**：
10. **产品出镜率**：产品密集展示可以采用上述比例；按已批准的叙事安排决定实际出镜节奏。
11. **附件**：双图网格方案可引用分镜图和多视图。直出或单图方案只引用实际所附素材。

## 参考资料

本 skill 的知识库按职责组织为参考文件，按需加载。SKILL.md 正文中已标注何时读取哪个文件的哪个 Part。

| 角色 | 文件 | 使命 | 使用阶段 |
|------|------|------|---------|
| 创意导演 | `references/complete-cinematic-direction-and-treatment-methods.md` | TVC 导演思维框架、出镜策略、品类适配 | 创意提案 |
| 前期筹备 | `references/complete-visual-assets-and-image-prompt-methods.md` | 资产规划、生成顺序、各类资产标准、一致性维护 | 前期筹备 |
| 镜头语言 | `references/complete-visual-assets-and-image-prompt-methods.md` | 提示词句法、画风锚定词库、场景类型模板、构图范式 | 视觉定调 / 前期筹备 / 分镜与拍摄 |
| 分镜与视频 | `references/complete-storyboard-and-video-prompt-methods.md` | 多宫格分镜、视频提示词、产品拆解、品牌世界 | 分镜与拍摄 |
| 交付与迭代 | `references/complete-production-review-and-delivery-methods.md` | 输出格式模板、迭代调试 | 前期筹备 / 分镜与拍摄 / 审片 / 交付 |


## Adapted module: `tvc-director/references/treatment.md`

# TVC 创意策略与分镜脚本框架

> **核心使命**：提供 TVC 导演的思维框架，指导大模型从产品 Brief 提取灵感，推导视觉创意，并最终输出标准、可执行的【分镜头脚本】。
> **拒绝废话**：放弃僵化的百分比模版和理论穷举，建立“世界观设定 -> 视听转化 -> 分镜输出”的直觉思维。

---

## Part 1: TVC 导演的思维框架 (Mental Model)

优秀的 TVC 创意不是填表格，而是构建世界和控制节奏。在构思阶段，请始终围绕以下三个维度进行推演：

### 1. 双世界法则 (Dual Worlds)
不要让产品干瘪地存在于真空中，思考它在这两个世界中的存在方式：
*   **产品世界 (Product World)**：绝对的主场。强调微距、精密感、材质肌理、局部特写、光影流转。
*   **品牌世界 (Brand World)**：产品所处的情感与文化语境。品牌世界的**载体**因品类而异——见下方品类分支。
*   **交互枢纽 (Match Cut/Transition)**：如何通过形状匹配、动作连贯或色彩渐变，将这两个世界的镜头无缝衔接。

#### 品牌世界的三种品类路径

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

### 2. 产品植入策略 (Product Integration)

双世界法则定义了"产品世界"和"品牌世界"的存在，但没有回答一个关键问题：**这两个世界在片子里怎么共处？** 拿到 brief 后，先判断品类路径，然后选择植入策略——它决定了全片的结构骨架。

#### 产品电影化拆解

产品是唯一主角，纯影棚，全片就是产品世界。零件悬浮拆解、材质微距潜入、光影剧场——品牌世界可以完全不出现。

*   适合有内部结构可展示的产品：耳机、相机、手机、机械表芯
*   视觉逻辑：暗调揭示 → 悬浮拆解 → 功能激活 → 微距潜入 → 品牌定格
*   产品世界占比 100%

#### 品牌世界穿梭

品牌世界和产品世界**轮流出场**，用 Match Cut 衔接。一个 Phase 待在一个世界里把场景讲完，然后通过匹配剪辑切到另一个世界——不是在一个 Phase 内部来回跳。

*   适合产品功能与极限/专业场景强绑定的品类：运动相机+跳伞、潜水表+深海、越野车+山路
*   视觉逻辑：品牌世界建立能量 → Match Cut 到产品世界展示 → Match Cut 回品牌世界升级 → 产品世界收束
*   关键：切换发生在 Phase 之间，每个 Phase 是一个完整的连贯镜头

#### 生活方式短片（Lifestyle Film）

产品始终待在品牌世界中，不跳出去。不做影棚特写，不做拆解——产品就穿在身上、戴在手上、握在手里。通过运镜手法（低角度追拍、慢动作、景深变化、追焦到产品）在场景内自然突出产品存在感。片尾集中做一个 Hero Shot 收束。

*   适合穿戴型产品和生活方式产品：跑鞋、手表、眼镜、首饰佩戴状态、手袋
*   视觉逻辑：品牌世界叙事为主，产品通过运镜被"看见"而不是被"展示" → 片尾 Hero Shot 定格
*   产品始终在画面中（穿在身上），但镜头不刻意脱离场景去做影棚特写

#### 品类直觉

不是硬规则，是默认倾向——导演可以打破，但打破要有理由：

*   有内部结构可拆的科技产品 → 电影化拆解
*   产品功能绑定极限/专业场景 → 品牌世界穿梭
*   穿戴型 / 生活方式 → 生活方式短片

### 3. 出镜策略 (Casting Strategy)

创意提案阶段必须回答：**谁出镜、怎么出镜、穿什么**。这对应真实 TVC 制作中的选角 (Casting) 和造型 (Styling) 环节。

#### 出镜决策树

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

#### Seedance 多宫格人物约束

当所用入口对人物参考有明示限制，或创意选择不展示完整人脸时，可根据实际限制采用下列出镜方式：
*   手部 / 手腕特写（珠宝/手表最常用）
*   下半脸（嘴唇、下颌线）
*   身体局部特写（肩颈、锁骨、腰线）
*   全身远景 / 背影 / 剪影
*   戴口罩 / 潜水面具 / 头盔等遮挡面部的方式

角色资产与视频参考分别遵循所选工具当前公开的输入规则。经许可并受目标工具支持时，可用人物参考图锁定造型；有疑问时先核实该入口的实际要求。

#### 造型方向

造型是身份型品牌世界的核心载体。创意提案中的造型方向应包含：
*   **服装风格**：极简/高定/街头/工装/运动...
*   **色彩关系**：与产品色的呼应或对比（银饰 + 全黑 = 先锋；金饰 + 裸色 = 优雅）
*   **配饰逻辑**：除主推产品外是否有其他配饰？保持克制，不抢主角
*   **肤质/妆发方向**：干净/自然/戏剧化/无妆感...

### 4. 视听转化法则 (Visual Translation)
将抽象的“卖点”转化为具象的视听语言：
*   **色彩与光影**：主色调是什么？是冷峻的赛博朋克霓虹光，还是治愈的自然晨光（Window light）？品牌色如何自然植入？
*   **视觉隐喻**：用画面代替说教。例如，“新鲜”不靠字幕，靠“清晨嫩芽滴落的露珠”；“静音”靠“一根针掉落的涟漪”。
*   **环境音场**：设计画面时同步思考声音。风声、水声、机械声、白噪音，甚至绝对的“静音”。

### 5. 叙事切分 (Pacing)
将总时长划分为合乎逻辑的节拍幕次（通常以 15 秒为一个叙事单元）：
*   **0-15s (起 - Hook)**：建立世界观与情绪基调，抓住眼球。
*   **15-30s (承 - Develop)**：场景展开，产品核心特征、氛围或冲突显现。
*   **30-45s (转 - Climax)**：视听高潮，最快节奏的快剪或最具视觉张力的特写。
*   **45-60s (合 - Resolution)**：情绪落地，产品 Hero Shot 亮相，品牌理念收束。

---

## Part 2: 创意方向竞选 (Concept Pitch)

在正式写脚本前，先提供 2-3 个核心创意方向供用户选择。保持精简，直击灵魂。

**输出格式**：
*   **方向 X：[极具画面感的概念名称]**
*   **视觉风格与主色调**：[如：日系清新 / 东方自然美学 / 暖绿色调]
*   **核心视听思路**：[简述产品世界与品牌世界如何交织，3-4句话说清全片最大的视觉亮点与记忆点]

---

## Part 3: 标准化分镜头脚本产出 (Storyboard Script)

用户选定方向后，直接输出分镜头脚本。这是本阶段的**最终核心交付物**。必须使用以下标准格式：

### 脚本结构标准

**【全局设定】**
*   **视频总时长**：[如：约 60 秒]
*   **视觉风格**：[关键词概括，如：高级电影感 / 赛博科技风]
*   **主色调**：[色彩描述，如：春日新绿、透明水光与晨光]
*   **音乐/声音基调**：[如：轻柔钢琴起头，中段加入风铃声，结尾回归白噪音]

**【分幕剧本】**（按时长分块，通常每 15 秒一幕）

#### ⏱️ 第一幕：[幕标题] (00:00 - 00:15)

**【镜头 1】**
*   **画面描述**：[详细的画面内容，前中后景，人物动作，产品状态，必须包含具体的画面细节。如果是一组快剪蒙太奇，可在此列出连续的多个短镜头。]
*   **运镜方式**：[如：固定机位 / 缓慢推进 / 航拍跟随 / 动感快切 / POV过肩视角 / 环绕镜头]
*   **旁白文案/字幕**：[精炼的文案，如果没有则写“无”]
*   **声音设计**：[具体的环境音或动作音效，如"微风吹拂"、"掐叶声"、"打字沙沙声"]

**【镜头 2】**
*   ...

#### ⏱️ 第二幕：[幕标题] (00:15 - 00:30)
...
*(依此类推，直到包含 End Frame 收尾镜头的最后一幕)*


## Adapted module: `tvc-director-treatment/SKILL.md`


# TVC Director Treatment

Use this skill to translate an approved creative concept into a rich director treatment and visual development package.

The output should explain both:

- Why this execution expresses the creative idea.
- What visual evidence the client can see before production.

## Core Stance

- Write as a director speaking to a client, not as a production checklist.
- Be richer than a short style note: include emotion, image logic, camera grammar, performance, world, product, rhythm, sound, and visual proof.
- Write visual prompts for the requested treatment sections. Render approval stills when requested as part of the deliverable and supported by the host. A text-only treatment ends with the written plan and prompts.
- Keep generated visuals as references for approval, not final production frames unless the user asks.

## Workflow

1. Confirm inputs:
   - Approved creative idea or proposal route.
   - Product truth, audience, channel, duration, visual references, actor policy, and AI/live-action mode.
   - If these are missing and affect treatment direction, route back to `the internal brief-strategy stage` or `the internal concept-development stage`.

2. Load visual development guidance when images are needed:
   - Read `references/complete-cinematic-direction-and-treatment-methods.md`.
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

4. Plan visual assets for the requested treatment sections; render those included in the requested output:
   - Image style reference.
   - Camera language reference.
   - Performance/persona design, including character three-view when relevant.
   - Scene setting image.
   - Product presentation image.
   - Lighting/color mood image.
   - Key visual or hero frame.
   - Preserve each prompt and its reference mapping. Include rendered results when they were requested and produced.

5. Hand off to:
   - `the internal PPM and pre-production stage` for PPM expansion.
   - `the internal storyboard-writing stage` for shot-by-shot structure.
   - `the internal image/video-prompting stage` if visual prompts need per-shot conversion.

## Output Format

```markdown
## 导演阐述

## 影像风格
- 文字阐述：
- 视觉参考图 / 图像提示词（按选定模型）：

## 镜头语言
- 文字阐述：
- 视觉参考图 / 图像提示词（按选定模型）：

## 节奏与情绪曲线
- 文字阐述：
- 视觉参考图 / 图像提示词（按选定模型）：

## 表演与人物形象设计
- 文字阐述：
- 人物三视图 / 图像提示词（按选定模型）：

## 场景设定
- 文字阐述：
- 场景设定图 / 图像提示词（按选定模型）：

## 产品呈现
- 文字阐述：
- 产品呈现图 / 图像提示词（按选定模型）：

## 美术、光影与色彩
- 文字阐述：
- 光影色彩参考图 / 图像提示词（按选定模型）：

## 音乐与声音

## 视觉开发清单

## 下游交接
```

## Image Generation Rules

- For requested renders, use the available image tool. For prompt-only work or unavailable tools, deliver the text prompts. Accurately report which assets were rendered.
- For OpenAI image API implementation details, use `official OpenAI product documentation` when current API syntax matters.
- For normal in-chat image generation, use `the available host image-generation tool` behavior when available.
- Do not invent exact brand packaging details not present in the provided product reference.
- For product images, require reference-image fidelity and block logo/text hallucination.
- For character three-view, specify front, side, back views on one clean sheet, consistent wardrobe and face, neutral pose.
- For multiple treatment images, generate one asset per prompt rather than asking for a single collage unless the section specifically needs a beat-board or three-view sheet.

## Quality Bar

- Every visual choice must serve the creative idea and audience psychology.
- Treatment writing must explain "why this visual language", not merely list adjectives.
- Each generated/reference image must answer a client question.
- Preserve continuity for later storyboard and AI prompting.
- Product presentation must protect shape, logo, package color, material, and scale.
- Character/persona design must match audience and avoid celebrity likeness unless explicitly approved.


## Adapted module: `tvc-director-treatment/references/visual-development.md`

# Director Treatment Visual Development

Use this reference when a director treatment needs generated images, moodboards, key visuals, character designs, or product presentation references.

For a written treatment or prompt request, supply the visual direction and copyable prompts in the requested model format. Render the images included in a request for actual visual assets using the selected, available tool. If the selected tool is unavailable, provide the prompt and identify which requested image is outstanding.

## Visual Asset Map

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

## Visual prompt pattern

Adapt these fields to the target model and the requested visual:

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

## Image Style Reference Prompt

```text
Create a high-end TVC director treatment style frame.
The image should communicate the film's overall visual tone, color palette, atmosphere, and emotional texture.
Do not create a final storyboard shot; create a mood-defining reference frame for client approval.
```

## Camera Language Reference Prompt

```text
Create a cinematic frame that demonstrates lens language, framing, depth of field, and camera attitude for a TVC.
Emphasize how the camera makes the product or character feel, not only what is visible.
```

## Character Three-View Prompt

```text
Create one clean character design sheet with front, side, and back views of the same person.
Neutral standing pose, consistent face, hairstyle, makeup, wardrobe, body proportion, and color palette.
Commercial casting reference style, not fashion illustration, not celebrity likeness.
Plain light background, no text unless requested.
```

## Scene Setting Prompt

```text
Create a TVC environment concept image for a director treatment.
Show the location, time of day, art direction, props, atmosphere, and practical shooting/AI-generation feasibility.
The scene should support the creative concept and audience psychology.
```

## Product Presentation Prompt

```text
Create a premium TVC product presentation reference.
The product must match the provided reference image in shape, package color, label layout, logo position, material, and scale.
Show texture, condensation, hand interaction, or hero packshot logic as requested.
Avoid hallucinated text, distorted logos, wrong packaging, extra products, or unreadable labels.
```

## Key Visual Prompt

```text
Create a campaign key visual for the TVC concept.
It should combine the core insight, product role, visual metaphor, and emotional promise in one memorable image.
Composition should be suitable for proposal deck and social campaign adaptation.
```

## Output Discipline

- Label each visual by section.
- Explain why the image is needed.
- Deliver the requested prompt or image for each selected visual. Identify any rendered asset and keep its prompt and reference mapping together.
- If only preparing prompts because the user requested prompt-only output or tools are unavailable, make prompts detailed enough for direct batch generation.
- Keep references and generated images separate from final storyboard frames.
