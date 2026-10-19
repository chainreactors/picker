---
title: Teloa 社区版 0.2.2 发布：构建自己的 AI 团队
url: https://mp.weixin.qq.com/s/xgN0ol_16fDvMXtgU3u3xg
source: Doonsec's feed
date: 2026-10-18
fetch_date: 2026-10-19T07:06:43.617059
---

# Teloa 社区版 0.2.2 发布：构建自己的 AI 团队

# Teloa 社区版 0.2.2 发布：构建自己的 AI 团队

原创

Max Luo
Max Luo

白帽子罗棋琛

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Teloa 社区版（0.2.2）正式发布：构建并运行你自己的 AI 团队

今天，**Teloa 社区版（0.2.2）正式发布。**

Teloa 是一个 AI 原生团队工作台。你可以用自然语言提出目标，创建持续负责工作的 AI 员工，组织团队分工，让工作围绕项目、资料、记忆和成果持续推进。

这次发布完整带来了 AI 员工、AI 团队、多 Harness 执行、项目与项目记忆、本地文档索引、语音交互和版本化成果交付，也将产品实践沉淀为两项面向行业公开的标准成果。

以下为社区版真实页面截图，使用演示数据；流程图用于说明工作关系。

![Teloa 社区版工作台](https://mmbiz.qpic.cn/mmbiz_png/4yRoMuNP853QrKbxErtMwkFGKfan7QbVVFps1Nd4oCmBA7hBdXUsp9yQEhSBibSiaw6B4hBFwf1EiaQBsRNiaCOOamialmiaicWOEjomiaCbQiafkPjM/640?from=appmsg)

*从一个目标开始，在同一工作台继续已有工作。*

## AI 员工：为持续工作建立长期岗位

用一段自然语言或 Markdown，描述你需要的岗位、工作要求和交付方式，核对后即可创建 AI 员工。

例如：

> 创建一位产品研究员，负责整理用户反馈、核实产品假设，输出带来源的分析与验证建议。资料不足时明确列出问题，对外发布前交由我确认。

每位员工可以拥有自己的职责、工作方式、业务范围、参考资料、技能和可用工具。这些配置随岗位保留，让同类工作能够持续开展。

你可以与员工私聊，查看它承担的任务、交付的成果和积累的经验，也可以把它加入团队，围绕共同目标协作。

员工的岗位身份与具体模型分开管理。更换模型或开始新任务，仍然可以延续同一个员工的职责与工作历史。

![员工目录中的职责、所属业务与当前工作](https://mmbiz.qpic.cn/mmbiz_png/4yRoMuNP850ib51TicIVTkefM8Fm15sxZRcDFkYpNzQafqicvzpmzZG2wbPjvW6FGFIx1K1PlGsyx3fpJWwicDmmEJz8ByxuFPoflfZG6fEWiaJA/640?from=appmsg)

*员工目录将长期岗位、业务范围和当前工作放在一起。*

## AI 团队：围绕共同成果组织分工

Teloa 支持将多个 AI 员工组合成团队，让研究、分析、制作、复核等工作形成明确分工。

市场提供产品、营销、销售等团队模板，将岗位、技能、参考资料、可选连接和工作模板一起组织，减少从零配置的重复操作。添加后，你可以核对成员、目标业务与工作安排，再启用需要的能力。

在群聊中，可以通过 `@` 指定员工参与，让交办、协作和结果回帖保留来源。主消息和话题分别组织，普通会话、员工私聊与群也有各自的入口。

**长期团队承接持续职责，临时执行小组服务于当前任务。** 独立部分可以并行处理，再由负责者汇总交付。跨业务协作继续遵循每位成员实际获得的资料和工具授权。

![内容营销团队的员工与技能配置局部图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP853vCoTA39L5p64wHCvKicYpkiagC2Le6ggxiblWq5Jz87xFpUb1yRCtibqvwfjQJEN6DB3s7P3rSG08TTbbj1fvCu7AsI1XGZk9iaJw/640?from=appmsg)

*团队配置局部：三位员工与配套技能。添加前还可检查参考资料与工作安排。*

## 多 Harness：接入 DSH、Codex 与 Claude Code

Teloa 将不同执行引擎接入同一工作流程：

* **DSH** 承担主会话、原生运行与工具调用。
* **Codex** 通过原生执行提供方处理独立的代码、文件与工具任务。
* **Claude Code / Claude Agent** 接入原生 Claude 执行链路，承接独立工作并回传结果。

你可以直接提出：

> 这次用 Codex 检查代码，让 Claude Agent 分析这些文件。

执行结果会接回原任务，继续沿用工作的来源与归属。

模型连接和 Harness 分别配置；各执行提供方使用对应认证，外部引擎启动前确认其原生工作目录与权限。你可以选择适合当前工作的执行方式，并在工作台跟进真实状态与交付结果。

![DSH、Codex 与 Claude 的执行关系](https://mmbiz.qpic.cn/sz_mmbiz_png/4yRoMuNP853VH7zHjGJibphkQswHK0iaemUSkibmKJ51wLEYDtibekmkWfae7F4GYlpF823yFDmMlDRZofANzwx5Plc038ShzflYAC6HiaCz8HXc/640?from=appmsg)

*执行关系示意：结果回到原任务，外部引擎保留各自原生授权。*

## 项目与项目记忆：让后续工作带着上下文

项目将目标、简报、任务、员工、群、资料、自动化和成果归集起来，并提供专属项目会话。

项目目标、有效规则、相关资料与记忆可以参与后续模型请求。你可以查看“本次使用”的内容与来源，了解员工依据什么完成工作。

项目记忆支持审阅候选、追溯来源、撤回后续使用，以及按固定修订分享。新会话可以选择是否读写长期记忆，个人偏好是否参与项目也由本人决定。

从第一次讨论到后续交付，项目能够逐步积累可复用的背景、规则和判断依据。

![项目上下文、工作证据与经审阅的记忆](https://mmbiz.qpic.cn/mmbiz_png/4yRoMuNP851a8ApiblIibWACJR8A2uIWFIoeEFS7OJ6kIqYWnWTic4z1pWYfprnnpOIjIG3Xeve0fToibrFhz0OpsurbD3OUnA2wwMbG1BRWqiaw/640?from=appmsg)

*项目关系示意：当前工作使用相关上下文，审阅后的记忆参与后续工作。*

## 本地文档索引与本地模型：把自己的资料用起来

Teloa 支持将你明确选择的本机 Markdown 文件加入索引，跟踪资料版本，并在检索时查看引用与原文摘录位置。

检索模型可在资料页确认后准备，包括 **Qwen3 Embedding、EmbeddingGemma** 等选项。聊天模型负责理解与生成，嵌入模型负责资料检索，两者分别管理。

通过 **Ollama**，可以检查本地聊天环境、接入已有模型，并确认下载或取消模型准备。

资料索引运行在你部署 Teloa 的设备或容器中。回答可以使用本地模型，也可以使用自行配置的远程模型；选择远程聊天服务时，相关检索摘录可能随本次上下文发送至该服务。

![资料库中明确选择的本机 Markdown 文件](https://mmbiz.qpic.cn/sz_mmbiz_png/4yRoMuNP851CSdZWaxL7ThMBgv5931icI25ibLQFLyWkLFkzjXliblCevjS1icGxHJdCicibwsbPUQicnOVydiajX4lqI1rKHYydwgylL7oxyG4zlbA/640?from=appmsg)

*本机文件保留位置和版本，是否加入索引由本人明确选择。*

## 自然语言任务与版本化成果：从交代工作到取得交付

任务的主要创建入口围绕一段自然语言或 Markdown 说明展开。交代目标、要求与交付格式，来源会话、项目和所属业务由上下文带入。

在同一工作路径中，你可以跟进执行、处理必要审批、停止工作、预览文件并取得成果。即使尚未创建员工，也可以先与小松鼠或通用 Agent 独立完成工作。

成果支持预览、下载，以及针对选段或整份内容反馈续改。每轮修改保留明确版本，v1、v2 等历史成果和原归属继续可查，验收也可以指向当时采用的具体版本。

工作台支持预览 Markdown、代码、图片、PDF、HTML、Office 文件和表格，便于直接检查交付内容。

## 业务、看板与应用市场：把工作接入实际业务

用自然语言创建或调整业务配置，审阅草稿后采用，再导入记录或连接已授权的数据来源。

业务内容与统计看板分别组织，既能查看具体记录，也能观察业务变化。任务、资料与成果可以围绕同一业务持续推进。

市场按 AI 员工、AI 团队、技能、应用与连接器等入口组织能力发现；应用页管理已安装能力和连接。

复杂工作还可以使用 Workflow 分步编排、PTC 工具组合，以及本人明确要求的 Ralph 迭代。Browser Use、Computer Use 和 IM 通道等可选能力，按实际需要分别配置与授权。

![内容运营看板中的阶段分布统计卡片](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP852bbHO4INOcxz0zXibibyuDPhH0yPDvWyTYJGZUbAHwgrSeByjTj5Qb5KZLyE1Q6YG3jfNegibsdRCOyyF1ZCdsakTibmuJDmWxVSA/640?from=appmsg)

*看板局部：业务记录按内容阶段汇总。图中为演示数据。*

## 语音输入、TTS 与通话：用说话的方式协作

Teloa 将语音输入、识别、播报与通话接入工作台：

* **语音输入**：支持 SenseVoice 本地转写，识别结果进入可编辑草稿，由本人核对发送。
* **通话识别**：可选择 MiniMax 云端识别或本机 SenseVoice。
* **语音播报**：支持 MiniMax、OpenAI、ElevenLabs，分别配置模型、音色与凭据。
* **音色与试听**：MiniMax 提供普通话、英文音色选择与试听，其他提供方按对应模型和音色配置。
* **连续播报与通话控制**：MiniMax 支持连续音频播报，减少小句之间反复启动的停顿，并保留静音、打断和挂断控制。

你可以与员工或小松鼠通话，也可以通过语音留言补充工作要求。通话与原会话保持关联，结束通话后仍可继续查看工作和成果。

## Auto Dream、员工经验与个人分身

Auto Dream 根据工作证据整理私有每日小结，沉淀带来源和范围的员工经验，支持查看与撤回。

员工经验、项目记忆和个人分身资料分别管理。分身可以积累本人提供的判断样本与习惯观察，用于整理个人工作方式；这些材料保留各自的使用范围。

确认有效的方法，还可以复用为技能或例行计划草稿。工作安排由本人明确启用，让重复工作逐步形成可检查、可调整的流程。

## 两项开放标准：定义 AI 怎样工作，也定义它如何安全行事

围绕 AI 工作者的组织方式与安全边界，**Teloa 已面向行业公开两项标准化成果**，供开发者、企业用户与其他平台实现、评审和共同完善。

### AI Worker 开放定义标准 1.0

由 Teloa 发起维护的 **AI Worker Standard 1.0**，为 AI Worker、AI Team 和 AI Organization 提供工作定义与协作合同。

它明确描述：

* AI 工作者跨任务延续的身份、职责与定义版本。
* 工作的输入、输出、依赖、授权条件与验收要求。
* 团队成员之间的分工、交接和共同成果。
* 组织层面的责任、资源约束与变更治理。

标准区分岗位定义、实际员工实例和单次执行，并提供核心规范、工作与协作应用规范，以及 JSON、YAML 示例，帮助不同实现准确表达一个 AI 工作者承担什么、怎样协作、交付如何核验。

阅读 AI Worker Standard 1.0

### 企业智能体身份与授权安全基线

由 **Teloa AI Security** 发起维护的《企业智能体身份与授权安全基线》v1.0，包含 **240 项可验证要求，覆盖 10 个安全领域**。

基线围绕智能体行为明确身份认证、委托与权限、授权决策、凭证管理、执行隔离、上下文安全、结果可见性、数据与记忆、生命周期治理及审计响应。

它提供 **L1 底线、L2 标准、L3 增强**三级评估框架，并配套在线、离线自评工具、成熟度报告和 Excel 评估表，可用于平台设计、供应商评估与安全评审。

两项规范均向行业开放使用与共建，产品符合性按具体版本、部署范围和实际证据核验。

阅读安全基线与自评工具

## 开始使用 Teloa 0.2.2

Teloa 社区版（0.2.2）现已通过 **GitHub、npm 和 Docker Hub** 正式发布，支持本地部署。

从一个真实项目开始，描述目标、选择资料、创建需要的员工，再让团队围绕可验收的成果开展工作。

GitHub Release · npm · Docker Hub

官网 · 使用文档 · 应用市场 · 完整更新说明

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/EVNATyibh91FHMdo0dibicCAclsdPPrZ0fp1mAibZInicxzgL4dczBhzBojsdK7NBgS0K4ZZColHiacnwiab7aAbla6xw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过