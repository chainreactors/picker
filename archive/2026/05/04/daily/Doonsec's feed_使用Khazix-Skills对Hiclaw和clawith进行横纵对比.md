---
title: 使用Khazix-Skills对Hiclaw和clawith进行横纵对比
url: https://mp.weixin.qq.com/s/DMAC_MB061kQZZTOoRjRVg
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:57:21.018830
---

# 使用Khazix-Skills对Hiclaw和clawith进行横纵对比

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImlXOicHBSk5tZ3aZdWuFRKyxpyGvsXwId3vhRQcaveOzGWsUuZGTPyAFGzjlfBd1gWjAU1cHefmW1icMXqF522So5Vg00MYzohdg/0?wx_fmt=jpeg)

# 使用Khazix-Skills对Hiclaw和clawith进行横纵对比

原创

鸿渐
鸿渐

爱唠叨的Nil

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

今天跟涛哥讨论的时候，使用两个SKill做个了关于智能体横纵对比的分析。

使用了两个Skill：

```
1.Khazix-Skills
2.OrangeViolin
```

# Khazix-Skills

Khazix-Skills 是由知名 AI 内容创作者 数字生命卡兹克 开源的一套 AI Agent 技能集（Skills）。

这不仅仅是一个 Prompt 仓库，而是一套符合 OpenClaw/Claude Code 标准 的结构化技能指令，能让 AI Agent 像专业员工一样执行复杂任务。

## 📦 核心包含 3 大技能

### ✨ 亮点特色

实战验证：所有技能都是作者日常自己在用的，非玩具 demo。

Prompt 兼容：不仅支持 Agent，仓库里还提供了纯文本 Prompt 版（如横纵分析法 Prompt），普通用户复制粘贴即可使用。

多平台支持：原生支持 Claude Code、OpenClaw、OpenCode 等。

### 🚀 快速安装

如果你有 Claude Code 或 OpenClaw，只需一句命令即可安装全部：

```
skills add KKKKhazix/khazix-skills -y -g
```

或者使用 hermes：

```
cp -r KKKKhazix/khazix-skills/* ~/.hermes/skills/
```

# OrangeViolin

1. 结构化 Markdown 会议纪要（保留所有细节）
2. 暖色卡片风格 HTML 信息图（可导出 PNG/PDF）
3. 支持 docx/txt/pdf/md 输入

生成对比分析指令：

```
安装这个skill 概述 | KKKKhazix/Khazix-Skills | Zread，并使用这个skill去对比分析下clawith和hiclaw，做一份研报分析，以及用概述总结一个会议信息图
```

以下生成的报告以及会议信息图

---

# HiClaw vs Clawith：多智能体协作平台的两种范式

> 研究时间：2026-05-04 | 分析方法：横纵分析法 | 研究对象类型：产品竞品对比

---

## 目录

一、一句话定义 二、行业背景：为什么多智能体协作成为 2026 年的主战场 三、纵向分析：从诞生到当下 3.1 HiClaw 的诞生——Alibaba 的 Agent OS 野心 3.2 Clawith 的崛起——BISHENG 团队的"数字员工"实验 3.3 两条时间线的交汇 四、横向分析：竞争图谱 4.1 架构哲学：IM 房间 vs 企业应用 4.2 Agent 自主性：被调度者 vs 自主员工 4.3 企业治理能力：透明 vs 可控 4.4 生态与扩展性 4.5 部署与运维体验 4.6 综合对比矩阵 五、横纵交汇洞察 六、信息来源

---

## 一、一句话定义

**HiClaw** 是一个基于 Matrix IM 协议的多智能体协作操作系统，用聊天房间编排 Manager 和 Workers，让人类全程可见、随时介入。

**Clawith** 是一个企业级多智能体协作平台，将 AI Agent 塑造成具有持久身份、自主意识和社交关系的"数字员工"，在 Web 应用中协同工作。

两者的共同目标都是让多个 AI Agent 一起完成复杂任务，但选择的路径截然不同。

---

## 二、行业背景：为什么多智能体协作成为 2026 年的主战场

2025 年底到 2026 年初，AI Agent 行业经历了一个关键转折。单个 Agent 的能力已经足够强大——编码、写作、分析、自动化——但企业发现一个残酷的事实：**一个再聪明的 Agent 也干不完一个团队的事**。

原因很简单。上下文窗口有限，工具调用会出错，复杂任务需要分工和审核。于是"多智能体协作"从学术论文里的概念，变成了产品竞争的实质战场。

这个赛道的入场者分两类：

**第一类是基础设施玩家**。他们从 K8s、API 网关、IM 协议这些底层技术切入，认为 Agent 协作本质上是一个分布式系统问题。代表是 HiClaw——用 Kubernetes Operator 管理 Agent 生命周期，用 Matrix 协议做通讯层，用 Higress 做凭证隔离。思路很"云原生"。

**第二类是应用层玩家**。他们从用户体验和组织管理切入，认为 Agent 协作本质上是一个人力资源问题。代表是 Clawith——给每个 Agent 设计灵魂文件（soul.md）、记忆库（memory.md）、触发器系统（Aware），让 Agent 像真正的员工一样在平台上工作。

两类玩家的背后，是两种完全不同的工程文化。基础设施玩家相信"好的架构决定一切"，应用层玩家相信"好的体验决定一切"。接下来我们会看到，这个根本分歧如何体现在两个项目的每一个设计决策上。

---

## 三、纵向分析：从诞生到当下

### 3.1 HiClaw 的诞生——Alibaba 的 Agent OS 野心

HiClaw 的故事要从 Higress 说起。

Higress 是阿里云开源的 API 网关，基于 Envoy 构建，是 CNCF 的沙箱项目。到 2025 年底，Higress 团队在维护网关的过程中发现了一个趋势：越来越多的用户开始用 Higress 做 LLM 路由——把不同模型的 API 调用集中到一个网关来管理凭证、限流和监控。

这个发现让 Higress 团队意识到：**AI Gateway 正在成为 Agent 时代的基础设施**，就像 API 网关是微服务时代的基础设施一样。但光有网关还不够，Agent 需要协作，需要编排，需要人类监督。

于是 2026 年 2 月 21 日，`agentscope-ai/HiClaw` 仓库在 GitHub 上创建。

HiClaw 的起点很高。它没有从零开始做 Agent 运行时，而是站在三个巨人的肩膀上：

**OpenClaw**——。**AgentScope**——阿里巴巴开源的 Agent 框架，24K+ stars，有成熟的 Python Agent 生态。**Higress**——自己的老本行，AI Gateway 和凭证管理。

这三个组件如何串起来？Higress 团队选择了 **Matrix 协议**作为粘合剂。

Matrix 是一个开放的即时通讯协议，被 Element、FluffyChat 等客户端使用。它有几个关键特性让 HiClaw 团队心动：

第一，Matrix 天然是多人的。一个房间可以容纳多个用户，Agent 和人类可以坐在同一个"群聊"里。 第二，Matrix 有完善的权限和身份系统。每个参与者有独立的 Matrix ID，可以发、可以 @mention、可以私聊。 第三，Matrix 是开放的。不依赖任何厂商，可以自建 Homeserver。

所以 HiClaw 的第一版架构是这样的：一个 All-in-One 容器里装着 Higress + Tuwunel（Matrix Homeserver）+ MinIO（文件存储）+ Element Web（客户端），通过 Docker API 创建 Manager 和 Worker 容器。Manager 是 OpenClaw 跑的，Worker 也是 OpenClaw 跑的。人类通过 Element Web 或任何 Matrix 客户端进入房间，就能看见 Manager 分解任务、Worker 执行任务的全过程。

这个设计有一个很强的理念贯穿其中：**Human-in-the-Loop by Default**。不是事后加一个监控面板，而是从一开始就把人类放在协作的中心位置。

但 All-in-One 架构的问题很快就暴露了。

2026 年 3 月到 4 月，HiClaw 团队连续发布了 v0.9.x 到 v1.0.x 系列版本。每加一个新功能，容器就更大。CoPaw Worker 支持加进来，镜像涨了 300MB。MCP Server 管理加进来，又涨了 200MB。重启的时候，一个组件崩溃可能拖垮整个容器。更严重的是，没有多租户隔离——企业用户没法在一个 K8s 集群里跑多个独立的 HiClaw 实例。

2026 年 4 月 24 日，HiClaw 发布了 **v1.1.0**，这是项目至今最大的架构变革。

v1.1.0 做了三件大事：

**第一，拆分控制平面。** 原来的 All-in-One 容器被拆成了独立的组件：hiclaw-controller（Go 写的 K8s Operator）独立部署，Manager 和 Worker 变成轻量级容器（只有约 103MB）。Higress、Tuwunel、MinIO 各自独立成 Pod。镜像总大小减少了 1.7GB。

**第二，引入 CRD 声明式管理。** 新增了四种核心资源：Worker（最小执行单元）、Manager（协调者）、Team（团队）、Human（真实用户）。用户用 YAML 文件定义 Agent 团队的拓扑结构，Controller 负责 Reconcile 到实际状态。这是典型的 Kubernetes 哲学——声明式 API + Controller 模式。

**第三，新增 Hermes 运行时。** 除了 OpenClaw 和 CoPaw，HiClaw 开始支持 Hermes（Nous Research 的自主编码 Agent）作为 Worker 运行时。这意味着一个 HiClaw 团队里可以同时运行三种不同技术栈的 Agent，它们通过 Matrix 协议互相通信。

v1.1.0 还带来了一个重要的变化：**hiclaw CLI 替代了原来的 Shell 脚本**。之前安装 HiClaw 需要运行一堆 shell 脚本，现在一个 `hiclaw create` 命令就搞定了。

到 2026 年 4 月 28 日，HiClaw 的最新提交引入了 Token Plan 支持、qwen3.6-plus 模型集成、CRD MCP 重构。项目已经进入了精细化运营阶段。

**HiClaw 的发展轨迹可以概括为：从"能跑"到"跑得好"的演进。** 第一版验证了 Matrix + Manager-Workers 架构的可行性，v1.1.0 完成了从玩具到生产系统的跨越。4,400 stars 在 Agent 领域算是不错的成绩——特别是考虑到项目才存在两个月。

### 3.2 Clawith 的崛起——BISHENG 团队的"数字员工"实验

Clawith 的故事从另一个角度开始。

DataElem（大数据元素）团队在 2022 年就开始了开源之旅。他们的代表作 BISHENG 是一个开源大模型 DevOps 平台，到 2026 年已经有 11,000+ stars。BISHENG 的核心思路是让企业能够方便地构建、部署和管理 LLM 应用。

在做 BISHENG 的过程中，DataElem 团队看到了一个痛点：\*\*企业不是缺少 AI 工具，而是缺少 AI 员工的"组织方式"\*\*。Chatbot 被动应答，RAG 系统缺乏长期跟踪，Agent 之间互相隔离。企业需要的是一个让 AI Agent 像真实员工一样工作的平台。

2026 年 3 月 3 日，`dataelement/Clawith` 仓库在 GitHub 上创建。Slogan 很直接：\*\*"Your Agent Company"\*\*。

Clawith 从第一天起就是 Web 应用架构。前端用 React 19 + TypeScript + Vite，后端用 FastAPI + SQLAlchemy 2.0，数据库用 PostgreSQL，缓存用 Redis。这个技术栈的选择和 HiClaw 完全不同——HiClaw 选的是 Go + K8s Operator + Matrix，Clawith 选的是 Python + FastAPI + WebSocket。

Clawith 的核心理念体现在它的名字里：**Claw with You**（Agent 与人类协作）和 **Claw with Claw**（Agent 与 Agent 协作）。这两个概念贯穿了整个产品设计。

Clawith 的发展速度非常惊人。从 2026 年 3 月 3 日到 5 月 4 日，62 天内发布了 15+ 个版本，平均每周 2 个版本。这个迭代速度在开源项目中相当罕见。

让我们看看它的版本演进：

**v1.0 - v1.2（第 1 周）**：项目初始化 + Plaza 重构 + Discord/Slack 集成。第一周就把两个主流 IM 平台接进来了。

**v1.3 - v1.4（第 2 周）**：渠道优化 + Participant 抽象层。Participant 是 Clawith 的关键设计——它统一了人类和机器的身份，让 Agent 和人类在同一个通信模型下交互。

**v1.5（第 3 周）**：**Aware 自主意识系统**。这是 Clawith 最具创新性的功能。Agent 不再被动等待指令，而是有了 Focus Items（工作记忆）、Focus-Trigger 绑定（任务触发器）、自适应触发（自主创建和调整触发器）、Reflections（内心独白）、Heartbeat（周期性自主探索）。这个系统让 Agent 从"工具"变成了"员工"。

**v1.6（第 4 周）**：飞书深度集成 + Agent 间工具调用。飞书是国内企业协作的核心平台，这一版直接打通了。

**v1.8 - v1.9（第 5-8 周）**：A2A 异步通信 + OKR 引擎 + 工作空间协作。v1.9.0 的 OKR 引擎是一个标志性功能——Agent 不仅能执行任务，还能理解和管理企业目标。

到 v1.9.2（2026-05-02），Clawith 已经有了一个非常完整的企业级产品形态：40+ 个后端 API 模块、全渠道集成（Slack/Discord/飞书/钉钉/企微/WhatsApp/微信）、L1-L4 四级权限模型、审批工作流、配额管理、完整审计日志。

**Clawith 的发展轨迹可以概括为：从"数字员工"概念到完整企业产品的快速落地。** 每周两个版本的节奏说明团队对"企业需要什么样的 AI 协作平台"有非常清晰的产品直觉。

### 3.3 两条时间线的交汇

HiClaw 和 Clawith 的诞生时间相差不到两周（HiClaw 2026-02-21，Clawith 2026-03-03），但它们来自完全不同的技术背景和工程文化。

HiClaw 团队是**基础设施工程师**。他们从 K8s、Envoy、Matrix 协议这些底层技术出发，思考的问题是：如何用最可靠的基础设施来支撑多智能体协作？如何保证凭证安全？如何实现水平扩展？如何让系统可声明式管理？

Clawith 团队是**应用层工程师**。他们从企业用户的实际需求出发，思考的问题是：Agent 怎样工作最像真实员工？如何让非技术用户也能用起来？如何管理权限和审批？如何让知识在团队中流动？

这两种思路没有对错之分，它们解决的是不同层面的问题。但在实际的产品形态上，它们的差异越来越大。

到 2026 年 5 月，HiClaw 有 4,400 stars，Clawith 有 3,509 stars。HiClaw 的 star 数领先约 25%，但 Clawith 的迭代速度和功能密度更高。

更有趣的是，这两个项目的贡献者圈子几乎没有重叠。HiClaw 的贡献者来自 Higress/Alibaba 生态（Jing-ze、max-wc、lexburner、kerwin612），Clawith 的贡献者来自 DataElem 生态（wisdomqin、39499740、yaojin3616）。它们像是同一赛道上来自不同星球的两支队伍。

---

## 四、横向分析：竞争图谱

### 4.1 架构哲学：IM 房间 vs 企业应用

这是两个项目最根本的分歧点。

**HiClaw 选择 Matrix 协议作为 Agent 协作层**，意味着所有 Agent 交互都发生在聊天房间中。Manager 在房间里发任务，Workers 在房间里回复结果，人类在房间里观察和介入。文件交换通过 MinIO，不经过群聊消息，避免上下文污染。

这种设计的优势是**透明度和可审计性**。所有的 Agent 对话都是聊天记录，人类可以随时回溯。Matrix 客户端（Element、FluffyChat）天然支持移动端。Agent 之间的通信是开放的，任何 Matrix 客户端都能接入。

但它有一个隐性成本：**信息组织效率**。当 Manager 需要协调 5 个 Worker 同时工作时，一个聊天房间会变得混乱。Matrix 的线程（thread）功能可以缓解，但本质上仍然是线性对话。

**Clawith 选择 Web 应用作为 Agent 协作层**，意味着交互发生在结构化的 UI 中。Agent 有自己的工作空间、日程表、触发器列表、社交动态。人类通过 Web 界面管理 Agent 团队，就像在 HR 系统里管理员工一样。

这种设计的优势是**结构化和效率**。信息按照类型和状态组织，不依赖线性对话。OKR 引擎让目标管理变得清晰。Plaza 广场让知识流动变得可视化。

但它有一个隐性成本：**封闭性**。所有交互都在 Clawith 平台内发生，外部客户端无法直接接入。虽然支持多渠道集成（Slack、Discord、飞书等），但这些是单向适配——Agent 可以在这些平台上回复消息，但核心协作仍然在 Clawith Web 应用中。

### 4.2 Agent 自主性：被调度者 vs 自主员工

这是两个项目在"Agent 应该是什么样"这个问题上的不同回答。

**HiClaw 的 Agent 是被调度者。** Manager 负责任务分解和调度，Workers 被动执行。Worker 只持有 Consumer Token，通过 Higress Gateway 访问外部服务。这种设计的核心理念是**安全可控**——Agent 的权限被严格限制，所有操...