---
title: 用 Claude + Temporal.io 构建多 Agent 协作开发流水线
url: https://mp.weixin.qq.com/s/Ur9Bl4JZEfoH5XdDex6JlQ
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:27:31.183125
---

# 用 Claude + Temporal.io 构建多 Agent 协作开发流水线

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/unnlWdxxboNfXhRh0GUqcicXwjKEfzm2Qia5mKDSg9OGWO1iaxoufENvV29fGHMSyCCer3C2fbafHVEics56icX1xGdZZAupWQSFlPfvM8HxII9Y/0?wx_fmt=jpeg)

# 用 Claude + Temporal.io 构建多 Agent 协作开发流水线

原创

牧之
牧之

从黑客到保安

![]()

在小说阅读器中沉浸阅读

# 一次关于"让 AI 模拟完整开发团队"的工程实践

# 一、为什么要做这件事

软件开发是一个天然的流水线过程：需求分析 → 技术设计 → 编码实现 → 测试验证 → 验收交付。每个环节都有明确的输入、输出和职责边界。

当 LLM 的能力足够强，我自然开始想：能不能把这条流水线上的每个角色都替换成 AI Agent，让自然语言需求直接驱动整个开发过程？

这不只是个新奇想法。对我来说有几个实际的价值点：

1. 验证需求的可行性：用 AI 快速出 PRD 和技术方案，暴露需求里的模糊点
2. 加速原型开发：对于内部工具、脚本服务、API 原型，走一遍流水线比自己写快得多
3. 理解 Multi-Agent 架构：真正把多 Agent 系统跑起来，才能理解它的瓶颈和边界

于是就有了这个项目：一个可以通过自然语言驱动、包含 PM / 架构师 / 开发 / 测试 / QA 五个 Agent 角色的协作流水线，每个阶段的产物（PRD、技术架构、代码文件、测试报告、验收结论）都实时可观测、持久化存储，验收不通过可以自动打回迭代。![](https://mmbiz.qpic.cn/sz_mmbiz_png/unnlWdxxboPoJMSHxm11YL8uel7icOYXq1ZRaYJWkGpzRibqvouhHib1UN0KM2JDXPJmUIHSwuWicDXV4SgBRtp2PESHZWmPnJ6NLv55UQhgGec/640?wx_fmt=png)

# 二、核心思路：制品驱动的 Agent 协作

在动手之前，我思考了两种 Multi-Agent 的协作模式：

模式一：对话式（Chat-based）Agent 之间互相发消息，上下游通过聊天记录传递上下文。实现简单，但上下文膨胀快，长对话里信号噪音比下降严重。

模式二：制品驱动（Artifact-driven）每个 Agent 读取上一阶段的结构化输出（Markdown 文件），生成自己的输出，写入持久化存储。下游 Agent 只关心"制品"，不关心"对话历史"。

我选择了制品驱动模式，原因很简单：这和真实团队的协作方式完全一致。

真实的产品经理写完 PRD 就扔给架构师，架构师出完技术方案就扔给开发。他们之间传递的不是聊天记录，而是文档。AI Agent 也应该如此。

这带来了几个工程优势：

1. 每个 Agent 的 Prompt 只需要包含"当前制品"，Token 消耗可控
2. 制品天然可以版本化（v1, v2, v3...），支持迭代追踪
3. 各 Agent 解耦，独立可测试

# 三、技术架构

## 整体架构

```
用户浏览器 (Next.js)      │      │  HTTP REST      ▼FastAPI 后端      │      ├── PostgreSQL (流水线状态 + 制品元数据)      ├── MinIO (制品文件存储，S3 兼容)      └── Temporal.io (工作流引擎)              │              ▼         Worker 进程              │    ┌─────────┼─────────┐    │         │         │  PM Agent  架构师   开发 Agent  (LLM)    Agent     (LLM)              │         测试 Agent              │         QA 验收 Agent
```

## 各个组件职责

| 组件 | 职责 |
| --- | --- |
| **FastAPI** | REST API、依赖注入、数据库/MinIO/Temporal 客户端管理 |
| **Temporal.io** | 工作流编排、活动重试、状态持久化、故障恢复 |
| **Worker 进程** | 执行 Temporal Activity（每个 Agent 调用是一个 Activity） |
| **MinIO** | 以 `{pipeline_id}/{agent_type}/v{n}.md` 路径存储每个阶段制品 |
| **PostgreSQL** | Pipeline 表、AgentState 表、Artifact 表 |
| **Next.js 前端** | 流水线管理、实时状态展示、制品查看 |

# 技术选型的关键决策：为什么用 Temporal.io？

最初我考虑过直接用 asyncio 的 task chain 来串联 Agent。但这有个根本问题：无法应对 LLM 调用的长时间等待和随机失败。

Temporal.io 给了我：

1. Activity 级别的重试：LLM 调用超时或 rate limit 自动重试，无需手写重试逻辑
2. 工作流状态持久化：Worker 崩溃重启后，工作流从中断点继续
3. 可观测性：Temporal Web UI 可以看到每个 Activity 的执行历史、重试记录、输入输出
4. Workflow 确定性：Temporal 的事件重放机制要求 Workflow 代码是确定性的，这迫使我把 LLM 调用都封装到 Activity 里，架构更清晰![](https://mmbiz.qpic.cn/mmbiz_png/unnlWdxxboNJlkcIcI3K4aEibNGnhiaat6563tyIazzZyeGRLtcAofKAW8gfCz9tWBNts8hYsMYicjKiaxCSjzjEUINx1PFLl3FPKFqhLicg3774/640?wx_fmt=png)

# 四、Agent 工作流程详解

## 流水线执行序列

```
create_pipeline (API)      │      ▼[Temporal Workflow: PipelineWorkflow]      │      ├─ 1. PM Agent Activity      │      输入: 用户需求文本      │      输出: PRD.md → MinIO + DB      │      ├─ 2. 架构师 Agent Activity      │      输入: PRD.md 内容      │      输出: architecture.md → MinIO + DB      │      ├─ 3. 开发 Agent Activity      │      输入: PRD.md + architecture.md      │      输出: 各代码文件 → MinIO + DB（每个文件一条 Artifact 记录）      │      ├─ 4. 测试 Agent Activity      │      输入: 代码文件列表 + PRD.md      │      输出: test_report.md → MinIO + DB      │      ├─ 5. QA 验收 Activity      │      输入: PRD.md + test_report.md      │      输出: qa_verdict.md → MinIO + DB      │              │      │         ┌────┴────┐      │      通过         不通过      │         │              │      │    COMPLETED    iteration_count < max?      │                    │          │      │                   是          否      │                   │          │      │              回到 PM      FAILED      │            (新迭代开始)      └─
```

# 五、用 OMC 来构建这个系统：Meta 视角

这个项目本身就是用 AI 工具开发的，这是一个很有意思的 Meta 视角。

oh-my-claudecode（OMC） 是 Claude Code 的多 Agent 编排插件。在本项目开发过程中，我大量使用了它的几个模式：

## Autopilot 模式

```
/oh-my-claudecode:autopilot为 pipeline 删除功能添加后端 API，包括：- DELETE /api/pipelines/{id} 端点，仅允许 failed/completed 状态- 删除对应 MinIO 所有制品文件- 删除数据库记录（注意 FK 约束顺序）
```

Autopilot 会自动走完：需求分析 → 技术规划 → 并行实现 → QA 验证的完整循环，不需要逐步指导它。

## Ralph 模式（自驱循环）

对于需要多轮修复的任务（比如 LLM 输出后处理），Ralph 模式会持续执行直到验证通过：

```
/oh-my-claudecode:ralph修复 developer_agent.py 中文件内容被 markdown 代码围栏污染的问题，验收标准：生成的 .py 文件不含 ``` 字符
```

## Deep-interview → Ralplan → Autopilot 三段式流水线

对于复杂的功能需求，最高质量的路径是：

1. /deep-interview：通过苏格拉底式提问澄清需求，输出低歧义度 Spec
2. /ralplan：Planner + Architect + Critic 三方 Agent 共识，输出实现计划
3. /autopilot：检测到 ralplan 计划直接跳过规划阶段，从执行开始

用 AI 来开发 AI 系统，最大的体会是：AI 工具能极大加速"已知模式"的实现（CRUD、API、组件），但在"未知领域"（比如如何设计 Prompt 防止过度工程化）仍然需要人来做决策。AI 是放大器，不是决策者。![](https://mmbiz.qpic.cn/sz_mmbiz_png/unnlWdxxboOaujOnXFVy3ibFPElPNkXVMb0cwLHicOFYDDfUrUVgxtwFZUqibicibtsExjeqmGYicOMXQniaujENNEU67lxupq1IickAgUPWTohjSqk/640?wx_fmt=png)

# 六、全流程演示&&效果展示

1、安装oh-my-claudecode 插件，在Autopilot 模式下，告诉它你想要构建一个怎样的工作流

![](https://mmbiz.qpic.cn/sz_mmbiz_png/unnlWdxxboMeA4ick5kDXvJtncPCONSKwJKRgRibvfw4c0TglDgW48LzxVYEXubsmAOqcRcNr8Pv2gEdATdVgbVo84CTdPMTInF58Ot890TbQ/640?wx_fmt=png&from=appmsg)

2、等他运行完成，运行本地项目

这个是生成的本地项目

![](https://mmbiz.qpic.cn/sz_mmbiz_png/unnlWdxxboPacb4XnRDhKibqApgHANia5LJibdETPiaFPyRmwoHLaTTpF8zBzpcDiaAbdVg4BkmUbHEwxgOQmpIxaqlTxAWEqxeBlZKEupZJGDtI/640?wx_fmt=png&from=appmsg)

执行命令make up && make migrate运行该项目。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/unnlWdxxboNOVSpCIiccuETvpWHIfiaS2u74oiaM0qnia1DK3DeggfqatG7tibyWzPaicTHXhuYuv4dUpz1xZEggbIdWnD8l350crhBichXlxpqiaC8/640?wx_fmt=png&from=appmsg)

访问http://localhost:3000

![](https://mmbiz.qpic.cn/mmbiz_png/unnlWdxxboPMgv6a3JW0vMdZkROcLMzrstzce1Ra3p3icKypuCqLUa8Xa91Y2UoIp8iauPib1pzxKQA7Q3Oic3ibPjk6FRdtfibzK6icqVQmZicUvZ4/640?wx_fmt=png&from=appmsg)

3、创建流水线

你可以创建一个流水线

![](https://mmbiz.qpic.cn/sz_mmbiz_png/unnlWdxxboNyibxt5AEtTn48j6Boia0mhR6MADq5KTYGHu2TicSllCeT6blj1PG8bdZ74tHJ5wiaVwrDMVKzc6EPpkrvlnTPVNfYcpcMTVcGSLU/640?wx_fmt=png&from=appmsg)

这里描述清楚你的需求。创建好流水线

4、等待全流程完成

![](https://mmbiz.qpic.cn/mmbiz_png/unnlWdxxboOEfUzJVKGsFpibPk4SYuP4m83YEibAH2wyiaKK1GOibTIA3K8cDZbIT6cf5z0jib9kqdPdoP46VqkKU9nVn8hhqPReHy9O0ibDiaN8Mg/640?wx_fmt=png&from=appmsg)

这里可以看到每个agent的工作状态，还有产出

![](https://mmbiz.qpic.cn/mmbiz_png/unnlWdxxboP737a0Jo2qcibEHnZtQs5sTCnjVpkLTTIDE1f1B4xowEjc16rbtYx0aCIViaHUap0TMhjGPTUoTL5NhhDHd42TsCzmbib2E6IGZ4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/unnlWdxxboMibEGYDtIao87oJ4qQl1NFwa5YToH0Cjq8KINvLAtUITmmwVhrw220nOH5toNLYiab9DNKenSEEtt253uESjlictuoHDwCn2PqJg/640?wx_fmt=png&from=appmsg)

# 七、应用场景发散

这个架构不只是代码生成流水线，稍加修改可以适配很多场景：

## 7.1 内容创作流水线

选题策划 Agent → 大纲撰写 Agent → 正文撰写 Agent→ 编辑校对 Agent → SEO 优化 Agent → 发布审核 Agent

技术文章、营销文案、产品说明书都可以走这套流程，每个阶段的产物（大纲、草稿、终稿）都版本化保存。

## 7.2 数据分析流水线

需求理解 Agent → 数据探索 Agent → 分析方案 Agent→ Python 分析脚本生成 Agent → 结论撰写 Agent → 可视化 Agent

用户用自然语言描述"分析上季度销售数据，找出下滑原因"，整条链路自动完成。

## 7.3 安全审计流水线

代码扫描 Agent → 漏洞分类 Agent → 风险评估 Agent→ 修复建议 Agent → 审计报告 Agent

每个 Agent 专注于安全的一个维度（OWASP Top 10 中的某几类），比单个 Agent 负责全部更准确。

## 7.4 法律/合规文档审查

文档解析 Agent → 条款提取 Agent → 风险识别 Agent→ 合规对比 Agent（对标法规）→ 修改建议 Agent → 审查报告 Agent

合同审查、隐私政策合规检查等场景，天然适合这种流水线模式。

## 7.5 产品需求到测试用例

PRD 解析 Agent → 功能点提取 Agent → 测试场景设计 Agent→ 测试用例生成 Agent → 边界条件补充 Agent → 测试计划 Agent

QA 团队可以直接拿到结构化的测试用例，而不需要从 PRD 手动拆解。

## 7.6 多语言本地化流水线

原文解析 Agent → 直译 Agent（多语言并行）→ 本地化润色 Agent（各语言独立）→ 术语一致性检查 Agent→ 回译验证 Agent → 格式化输出 Agent

支持同时输出 10 种语言，每种语言经过翻译 → 润色 → 验证三道关卡。

## 7.7 招聘筛选流水线

JD 解析 Agent → 简历解析 Agent → 岗位匹配 Agent→ 技能评估 Agent → 背景核实提示 Agent → 面试问题生成 Agent

处理大量简历时，标准化评估维度，减少人工初筛时间。

## 7.8 智能运维变更流水线

变更申请解析 Agent → 影响分析 Agent → 风险评估 Agent→ 变更方案生成 Agent → 回滚方案 Agent → 审批摘要 Agent

DevOps 场景下，将变更申请拆解成结构化风险评估，降低审批负担。![](https://mmbiz.qpic.cn/mmbiz_png/unnlWdxxboO3nvy7QYJdRnTwMiaYMNtRByTribOn4SWy8Wd26yPsDdbxQUV0Sy61r4mqSLbEBj81zgOrQ95IQRyR10J1VnFjYhfic8uaUezOL4/640?wx_fmt=png)

# 八、当前局限与演进方向

诚实地说，现在这个系统还有很多不完善的地方：

## 8.1 LLM 输出质量不稳定

当前最大的问题是 LLM 输出的可预测性。同样的 Prompt，不同调用的结果可能差异很大：

1. 文件路径列表有时混入描述文字
2. 代码文件有时包含不必要的 Markdown 格式
3. 开发 Agent 偶尔会生成空文件或截断文件

改进方向：引入结构化输出（JSON Schema 约束）替代纯文本输出，用 Pydantic 模型验证 LLM 响应。

## 8.2 Agent 之间缺乏真正的"对话"

目前每个 Agent 只读取上一阶段的制品，没有澄清机...