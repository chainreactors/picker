---
title: 深入拆解RedAmon：AI驱动自动化红队框架架构解析
url: https://mp.weixin.qq.com/s/3xss-pCYsXoJYUGRZWQ_hQ
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:46:57.774662
---

# 深入拆解RedAmon：AI驱动自动化红队框架架构解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GVAVvm742xNapUDfLrdqdK1MraL2oib2cXqgHrzhNG43thWD1Rc5yD2xLntGFlsypic5SybpPHlCvLNKTVkSjwcEh9jl1MjDsGEzWw7AT8hTA/0?wx_fmt=jpeg)

# 深入拆解RedAmon：AI驱动自动化红队框架架构解析

原创

徐哥
徐哥

Ms08067安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

文章来源｜MS08067 AI安全应用知识星球
> 作者：小玉玉

> RedAmon 是一个基于 AI 的自动化红队框架，它将传统渗透测试工具与现代 AI 编排技术深度融合，实现了从侦察、利用到后渗透的端到端自动化攻击链。项目采用创新的 ReAct 架构模式，通过 Fireteam 并行专家子智能体协调攻击任务，利用 Neo4j 图数据库驱动攻击面智能分析，支持 500+ 项目配置参数、400+ AI 模型、185,000+ 检测规则和多 LLM 提供商，代表了 AI 驱动安全测试领域的先进工程实践水平。

在网络安全领域，红队演练（Red Team Exercise）是检验组织安全防护能力的重要手段。传统红队行动主要依赖经验丰富的安全专家，他们需要手工执行数十种工具，分析海量的扫描结果，制定复杂的攻击策略——这个过程既耗时又容易出错。随着 AI 技术的快速发展，一个自然的问题是：能否让 AI 智能体替代人类专家，实现自动化、智能化的渗透测试？

RedAmon 项目给出了肯定的答案。本文将从系统架构、核心技术拆解、差异化能力三个维度，全面解析 RedAmon 的技术实现，带你深入了解 AI 如何改变传统安全测试的工作方式。无论你是安全从业初学者，还是有经验的研究者，都能从中获得有价值的启发。

---

## 系统架构与核心设计

RedAmon 的核心理念是**用 AI 智能体替代传统手工渗透测试流程**，通过自动化编排实现攻击链的全流程智能化。对于初学者来说，可以理解为一个"智能渗透测试机器人"——它像经验丰富的安全专家一样思考，但不知疲倦地执行各种测试任务。

其整体架构采用**容器化微服务 + 图数据库驱动 + AI 智能体编排**的三层设计。这种架构听起来很复杂，但可以想象成一个现代化的工厂：底层是各种专业工具（传统红队工具如 Nmap、Metasploit、Nuclei 等），中间层是智能调度系统（LangGraph 驱动的 Agent 系统），顶层是统一的管理界面。系统将这些工具封装为 MCP（Model Context Protocol）标准接口，让 AI 能够像人类安全专家一样自主决策调用，实现"侦察 → 利用 → 后渗透 → 修复"的完整闭环。

### 系统分层架构

要理解 RedAmon 的复杂架构，我们可以将其类比为一个现代化的军事情报系统：最上层是指挥中心（编排层），中间是各种专业情报队伍（工具层），底层是庞大的情报数据库（数据层），而前端界面则是与指挥官交互的控制台。

以下是 RedAmon 的具体分层设计：

| 层级 | 职责 | 生命周期 |
| --- | --- | --- |
| **编排层** | Root Agent 决策、Fireteam 并行协调、Phase 管理 | 持续运行 |
| **工具层** | 40+ 安全工具的 MCP 封装、Kali 沙箱执行 | 按需启动 |
| **数据层** | Neo4j 攻击面图、PostgreSQL 配置存储 | 持久化存储 |
| **交互层** | Next.js Web UI、实时聊天、工作空间管理 | 会话级别 |
| **基础设施** | Docker 容器化、网络隔离、文件系统共享 | 长期运行 |

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/GVAVvm742xPEAwbBCk7eoialDicTTgibTZZic15HTMde2hEeShq27s9icLs2VjEpQOHlT9dbqN3WOqTE7NjTrM9Y1qZLPRlARZTiam5Zfaf70p8Ag/640?wx_fmt=png&from=appmsg)**

**图1：RedAmon 项目创建界面**

图1：RedAmon 项目创建界面

### 核心数据模型

在深入了解 RedAmon 的数据模型之前，我们需要理解什么是**图数据库**。传统的关系数据库（如 MySQL）用表格存储数据，适合处理结构化的事务；而图数据库（如 Neo4j）用节点和关系存储数据，特别适合处理复杂的关联查询——这正是攻击面分析所需要的。

想象一下，你要分析一个目标系统的攻击路径：哪些域名解析到哪些 IP？哪些 IP 运行着哪些服务？哪些服务存在哪些漏洞？这些漏洞能让你访问到哪些其他系统？用传统数据库需要多次关联查询，而用图数据库一次查询就能找到完整的攻击链。

RedAmon 使用 Neo4j 图数据库来构建攻击面知识图谱，以下是它的核心约束定义：

```
// 文件位置: graph_db/schema.py
// RedAmon Neo4j 图数据库核心约束定义（租户隔离的多租户架构）

// 域名唯一性约束（租户隔离：同一域名可在不同项目中存在）
CREATE CONSTRAINT domain_unique IF NOT EXISTS FOR (d:Domain) REQUIRE (d.name, d.user_id, d.project_id) IS UNIQUE;

// 子域名唯一性约束
CREATE CONSTRAINT subdomain_unique IF NOT EXISTS FOR (s:Subdomain) REQUIRE (s.name, s.user_id, s.project_id) IS UNIQUE;

// IP 地址唯一性约束
CREATE CONSTRAINT ip_unique IF NOT EXISTS FOR (i:IP) REQUIRE (i.address, i.user_id, i.project_id) IS UNIQUE;

// 端口唯一性约束（同一 IP 的同一端口在不同租户间可重复）
CREATE CONSTRAINT port_unique IF NOT EXISTS FOR (p:Port) REQUIRE (p.number, p.protocol, p.ip_address, p.user_id, p.project_id) IS UNIQUE;

// 服务唯一性约束
CREATE CONSTRAINT service_unique IF NOT EXISTS FOR (svc:Service) REQUIRE (svc.name, svc.port_number, svc.ip_address, svc.user_id, svc.project_id) IS UNIQUE;

// 端点唯一性约束（用于 Web 应用攻击面映射）
CREATE CONSTRAINT endpoint_unique IF NOT EXISTS FOR (e:Endpoint) REQUIRE (e.path, e.method, e.baseurl, e.user_id, e.project_id) IS UNIQUE;

// 漏洞唯一性约束
CREATE CONSTRAINT vulnerability_unique IF NOT EXISTS FOR (v:Vulnerability) REQUIRE v.id IS UNIQUE;

// CVE 唯一性约束（全局共享参考数据）
CREATE CONSTRAINT cve_unique IF NOT EXISTS FOR (c:CVE) REQUIRE c.id IS UNIQUE;

// 漏洞节点与关系
MERGE (v:Vulnerability {
    cve: $cve_id,
    severity: $severity,
    cvss: $cvss_score,
    description: $description
})
MERGE (srv)-[:HAS_VULNERABILITY]->(v);

// 端点节点（AI 接口）
MERGE (ep:Endpoint {
    path: $endpoint_path,
    method: $http_method,
    ai_interface_type: $ai_type,  // REST / GraphQL / WebSocket
    auth_required: $needs_auth
})
MERGE (srv)-[:EXPOSES_ENDPOINT]->(ep);

// 凭据节点与关系
MERGE (cred:Credential {
    username: $user,
    hash_type: $hash_type,
    crack_time: $time_to_crack
})
MERGE (h)-[:HAS_CREDENTIAL]->(cred);

// 攻击链关系
MERGE (a1:Asset {name: $asset1})
MERGE (a2:Asset {name: $asset2})
MERGE (a1)-[:CAN_COMPROMISE {technique: $mitre_technique, difficulty: $diff_level}]->(a2);

// 元数据标注
MERGE (t:Tag {name: $tag_name, category: $tag_category})
MERGE (v)-[:TAGGED_WITH]->(t);
```

![](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xM1ynMoL2yJgAThYibb7KCko8gOdhQ7sic4PLPk6EWEvUAlsEJacEboe1vNBvbbP68EkN3dJ29F2ic0XEsApZVuBicUSwPuHnyJGAo/640?wx_fmt=png&from=appmsg)

图2：RedAmon 攻击面动态关系图展示

上图展示了 RedAmon 如何将分散的攻击数据转化为可视化的关系网络。你可以看到，不同的节点（域名、IP、端口、漏洞）通过线条（关系）连接在一起，形成了完整的攻击面地图。这种可视化让安全测试人员能够一目了然地看到攻击路径和风险点。

对于初学者来说，理解这种图数据模型可能有些抽象。让我们用一个实际例子来说明：假设你要攻击 `example.com` 域名，传统工具会分别告诉你子域名列表、IP 地址列表、开放端口列表，但你需要手工整理它们之间的关联。而 RedAmon 的图数据库会自动建立这些关联，你一眼就能看到 `www.example.com` 解析到 `192.168.1.100`，这个 IP 的 80 端口运行着 Apache 2.4.41，存在 CVE-2019-0211 漏洞，利用这个漏洞可能让你访问到内网的数据库服务器。

以下是 RedAmon 端到端自动化攻击链的流程图：

```
graph TB
    subgraph "侦察阶段"
        A[输入: 域名/IP] --> B[侦察编排器]
        B --> C[40+ 并行工具]
        C --> D[原始数据]
    end

    subgraph "数据处理"
        D --> E[数据归一化]
        E --> F[Neo4j 图数据库]
        F --> G[攻击面可视化]
    end

    subgraph "AI 决策"
        G --> H[Root Agent]
        H --> I{SG-ReAct 散射}
        I --> J[Fireteam 子智能体]
        J --> K[并行执行]
        K --> L[结果聚集]
    end

    subgraph "执行阶段"
        L --> M[利用阶段]
        M --> N[MCP 工具调用]
        N --> O[Kali 沙箱执行]
        O --> P[后渗透阶段]
        P --> Q[漏洞修复]
    end

    subgraph "反馈循环"
        Q --> R[图数据库更新]
        R --> H
    end

    style H fill:#ff6b6b,stroke:#c92a2a,stroke-width:3px
    style F fill:#4ecdc4,stroke:#0f9d8a,stroke-width:2px
    style O fill:#ffe66d,stroke:#f4a127,stroke-width:2px
    style R fill:#a8e6cf,stroke:#38a169,stroke-width:2px
```

![](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xOyxjobKyQlnObfndjJMsQfFrPXt5MK6ZhMg9eYVxv8LIaGLicibXcpz7fFeSYlMOFnibW2D1UWA6bXB6XzaCrFQciaQWOT74QFnvg/640?wx_fmt=png&from=appmsg)

架构高度抽象让我们看到了整体轮廓，但要真正理解 RedAmon 如何实现"AI 替代人工"的愿景，还需深入工程底层，逐一拆解支撑这套模型的七项关键技术面。

---

## 核心技术与工程架构

### 一、技术栈全景

在深入具体技术细节之前，我们先全面了解 RedAmon 的技术栈。对于初学者来说，这部分可能包含很多陌生的技术名词，但不用担心——我们会逐一解释它们的作用和意义。

RedAmon 的技术选型体现了**安全工具容器化 + AI 编排现代化**的双重追求，既保留了传统渗透测试工具的威力，又引入了最新的 AI 框架和前端技术。可以想象一下，这就像是把传统的手工工具（螺丝刀、扳手）升级为电动化、智能化的现代工具生产线。

以下是 RedAmon 完整的技术栈：

| 层级 | 技术方案 | 选型理由 |
| --- | --- | --- |
| **AI 编排** | LangGraph + LangChain | 提供 Agent 状态管理、ReAct 循环、检查点持久化的原生支持 |
| **Web 框架** | FastAPI（Agent API） + Next.js（Webapp） | 高性能异步 API + React SSR，类型安全，现代化 UI |
| **关系数据库** | PostgreSQL 16 | 存储用户配置、项目设置、Agent 检查点等结构化数据 |
| **图数据库** | Neo4j 5.26 + APOC 插件 | 原生图查询、攻击路径推演、Cypher 语言表达力强 |
| **前端框架** | Next.js 14+ + TypeScript + Tailwind CSS | React SSR、类型安全、现代化 UI、暗色主题支持 |
| **容器化** | Docker + Docker Compose | 微服务解耦、环境一致性、一键部署、网络隔离 |
| **LLM 提供商** | OpenAI（GPT-4） / Anthropic（Claude） / OpenRouter（400+ 模型） | 多模型支持、成本优化、本地模型（Ollama/vLLM）兼容 |
| **工具集成** | FastMCP（Model Context Protocol） | 工具标准化、跨语言互操作、可扩展性强、SSE 传输 |
| **安全工具** | 100+ 工具（Nmap、Nuclei、Metasploit、Hydra、sqlmap） | 覆盖侦察、漏洞扫描、利用、后渗透全流程 |
| **知识库** | NVD + ExploitDB + Nuclei + GTFOBins + LOLBAS | 185,000+ 检测规则、CVE 数据、利用数据库 |
| **多租户** | Tenant-scoped 约束 + 复合索引 | 支持多用户并发、项目隔离、数据安全 |

有了这些技术作为底座，RedAmon 得以构建其最核心的竞争力——**ReAct 智能体编排系统 + Fireteam 并行专家系统**。不同于市面上传统自动化工具（如 Autosploit、Sparta）的静态脚本化做法，RedAmon 选择了一条更工程化的路径：用 LangGraph 构建可中断恢复的状态机、用 FastMCP 标准化 100+ 安全工具接口、用 Neo4j 图数据库记忆全局攻击面、用 PostgreSQL 持久化检查点实现长期运行。

### 二、SG-ReAct 智能体编排

SG-ReAct（Scatter-Gather ReAct）是 RedAmon 的核心架构创新，也是理解整个系统的关键。在深入代码之前，我们先理解这个概念。

**ReAct 模式**是 AI 领域的一种重要推理模式，代表"推理-行动"（Reasoning + Acting）的循环。想象一个经验丰富的渗透测试专家在工作中会如何思考：首先观察当前情况（比如发现一个开放端口），然后思考下一步该做什么（比如检查该端口是否存在漏洞），接着采取行动（运行漏洞扫描工具），最后根据结果继续下一步。这就是 ReAct 循环。

RedAmon 将这种模式扩展为**散射-聚集模式**：

* **Root Agent**（根智能体）负责全局决策和协调
* **散射（Scatter）**：将复杂任务分解为多个子任务，分发给专家智能体
* **聚集（Gather）**：收集各专家的结果，更新全局状态
* **循环迭代**：不断重复这个过程，直到达成目标

这种架构的优势在于：既有统一的战略规划（Root Agent），又有专业的具体执行（专家子智能体），就像一个高效的军事指挥系统。

以下是 SG-ReAct 编排器的核心实现代码：

```
# 文件位置: agentic/orchestrator.py
# RedAmon Agent Orchestrator - ReAct 风格编排器实现

from langchain_core.language_models import BaseChatModel
from langchain_core.messages ...