# Social Content Studio 应用说明

本说明介绍如何把 `social-content-studio` 安装到支持 Skills 的 Codex 或 ChatGPT 环境，并开始使用。安装包已融合专业流程、参考资料和模板，不需要另外安装原来的 TVC Skills。

## 安装包内容

- 一个 Skill 入口：`social-content-studio/SKILL.md`
- 54 份原始 Markdown 来源资料，合计约 391 KB，其中含 8 份原始模板；完整正文集中在 `references/complete-professional-source-library.md`，专业流程按需并入各工作流手册。
- 两个可选表格转换脚本：将 TSV 转成 CSV 或 XLSX。
- 只保留一个可调用的 `SKILL.md` 入口；原来的专业 Skill 目录已融合，不需要另装或调用。
- 不包含图像或视频模型、渲染器、API 密钥。31 个 Seedance 评估案例随包提供，可用于人工复盘。原技能的界面配置收录为只读核对资料。

## 开源许可

融合版使用 [MIT 许可证](LICENSE)。再分发时请随附项目许可证和三份上游版权与许可声明，作者、来源版本及对应技能见[第三方声明](THIRD_PARTY_NOTICES.md)。

## 在 Codex 中安装

Windows 全新安装可使用个人技能目录 `~/.agents/skills`。已有安装请更新 Codex 已识别的同名目录，部分环境使用 `~/.codex/skills`。把以下命令里的 ZIP 路径替换成实际下载位置：

```powershell
$skillDir = Join-Path $env:USERPROFILE ".agents\skills"
New-Item -ItemType Directory -Path $skillDir -Force | Out-Null
Expand-Archive -LiteralPath "C:\Users\YourName\Downloads\social-content-studio.zip" -DestinationPath $skillDir -Force
Test-Path (Join-Path $skillDir "social-content-studio\SKILL.md")
```

最后一行应返回 `True`。正确结构是：

```text
%USERPROFILE%\.agents\skills\social-content-studio\SKILL.md
```

发布附件 `social-content-studio.zip` 已有正确的根文件夹。如果从 GitHub 的 **Code → Download ZIP** 下载的是源码，先把含有 `SKILL.md` 的文件夹改名为 `social-content-studio`，再放入技能目录。若解压后出现 `skills\social-content-studio\social-content-studio\SKILL.md`，说明多嵌套了一层，请把内层文件夹移到 `skills` 目录下。

安装后打开新的 Codex 会话，在请求前写：

```text
$social-content-studio
```

Codex 也可能按任务自动选择 Skill；显式调用更容易确认它正在使用。刚安装后若找不到 Skill，检查路径并开始新会话。

## 在 ChatGPT 中安装

ChatGPT 和 Codex 的 Skills 分开管理。在 ChatGPT 侧栏进入 **Plugins → Skills → Create → Upload from your computer**，按界面提示上传 ZIP 或已解压的 `social-content-studio` 文件夹。等待扫描并完成安装。使用时在输入框输入 `@`，从列表选中 `social-content-studio`，再写任务。

Skills 是否可用取决于账号方案、产品开放情况和工作区设置。按当前官方帮助说明，符合条件的 Business、Enterprise、Healthcare 和 Edu 账号可使用；管理员也可能限制上传或安装。如果看不到 Skills 页面，先检查账号和工作区权限。

普通 GPT 对话没有 Skills 功能时，仅把 ZIP 解压到电脑不会让它自动识别或持久调用。把文件上传到单次对话可作为临时参考，但不会注册成 `$social-content-studio` Skill。

## Skill 的工作流程

1. **读取已有资料**：查看当前对话、产品文件、品牌要求和最近发布内容，沿用已确认的信息。
2. **补齐产品基准**：新产品先整理型号、经核实的功能、受众、市场、目标渠道和限制；只对影响创作的关键缺项集中提问。已有产品不重复询问已答过的问题。
3. **选择所需创作阶段**：根据任务使用 brief、创意方案、导演阐述、分镜、提示词、修改或制作交接等完整方法。常规社媒任务不会自动展开整套 TVC 流程；需要 Seedance/TVC 长片方法时，再从完整来源库按模块读取。
4. **先发展故事再写镜头**：视频先明确人物目标、真实阻碍、产品事实带来的转折和结果。短视频开头三秒要有注意力钩子；镜头时长、动作和产品状态需要连贯。
5. **准备发布与制作材料**：按需求撰写不同平台的文案、图片或视频提示词、内容日历和 Stories 方案。
6. **交付前核对**：检查产品事实、品牌要求、平台格式、时间线、限制条件和来源。不会编造参数、功能、用户评价或法规结论。

## 可直接复制的请求

### 新产品首次使用

```text
请使用 $social-content-studio。先阅读我提供的品牌和产品资料，整理已确认的产品基准；只对创作前必须补充的信息一次性提问。不要猜测产品参数或功能。
```

### 制作短视频内容包

```text
请使用 $social-content-studio。根据已确认的产品资料，为 [目标市场] 制作一条 [时长] 秒、[语言] 视频故事和导演级分镜，并提供 [平台] 文案与视频生成提示词。按目标平台分别写文案。
```

### 延续已发布系列

```text
请使用 $social-content-studio。先检查最近交付的内容和当前周主题，再制作下一集。延续既有故事线，避免重复近期钩子、场景和动作。
```

以上示例使用 Codex 的调用写法。ChatGPT 安装后先在 @ 菜单选中技能，再输入任务。把方括号中的市场、时长、语言和交付内容换成实际要求即可。

## 能力范围

Skill 提供内容策略、故事、脚本、分镜、提示词、平台文案和制作交接。真正生成或渲染图片、视频，需要运行环境另有可用的媒体工具；没有相应工具时，它应交付文字提示词和制作说明，不会声称媒体已生成。

两个转换脚本只负责把 TSV 表格转为 CSV 或 XLSX，不会生成媒体或调用模型。Skill 不会自动发布内容、联系第三方，也不会在其他电脑上自动更新；新版本需要重新传送并安装。

## 常见问题

**Codex 找不到 Skill**：确认 `SKILL.md` 在 `social-content-studio` 文件夹根部，检查它是否位于当前 Codex 用户的 `.agents\skills` 目录，再开始新会话并显式输入 `$social-content-studio`。

**ChatGPT 没有 Skills 页面**：检查账号方案、工作区设置和管理员权限。ChatGPT Skills 与 Codex Skills 分开安装。

**没有生成图像或视频**：安装包不含生成器；请在目标环境启用相应工具，或直接使用 Skill 产出的提示词。

## 官方说明

- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [官方技能调用与安装目录说明](https://learn.chatgpt.com/docs/build-skills)
- [Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills)