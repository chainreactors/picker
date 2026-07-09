---
title: 哪吒网络安全MCP
url: https://mp.weixin.qq.com/s/Uf-2zKfY_EZHKGbRUQGtFg
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:57:23.185319
---

# 哪吒网络安全MCP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ia7TorzX5Pa1GKDINqFXNnUaYqibH8umpNtibDd80Z3hibSAnDicKiciamYCeA1baet8HVdjIZKNggAYoxibdle1hNv2fNU0cxib5SiageDbzCcbDm90E/0?wx_fmt=jpeg)

# 哪吒网络安全MCP

原创

钟智强
钟智强

哪吒网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| CVE 漏洞情报  ·  MCP 服务器  ·  部署实战  NezhaCyberMCP  部署实战指南  让 AI 编程助手秒查 CVE 漏洞情报的 MCP 服务器 |

从零到一搭建 CVE 漏洞情报 MCP 服务器，打通 Claude Code / Cursor / VS Code Copilot 实时安全查询链路

基于 Go 语言的生产级 MCP 服务器  ·  本地开发 + 云端 Lambda 全场景

前言

在日常开发中，你是否遇到过这样的场景：AI 编程助手帮你生成了依赖配置，却没人告诉你这个第三方库是否存在已知漏洞？等安全扫描在 CI/CD 阶段才报出来，修复成本已经翻了好几倍。

NezhaCyberMCP 就是来解决这个问题的——它是一个基于 Go 语言的生产级 MCP（Model Context Protocol）服务器，将 AI 助手与持续更新的 CVE 漏洞数据库桥接起来，让你在编码阶段就能实时查询最新漏洞、按厂商/产品/CPE 搜索、做趋势分析、把软件资产清单与 CVE 匹配，从源头暴露供应链安全风险。

本文将手把手教你从零部署 NezhaCyberMCP，覆盖本地开发与云端 Lambda 两种场景。

一、项目简介与开发初衷

1.1 项目概览

| 属性 | 信息 |
| --- | --- |
| 项目名称 | NezhaCyberMCP |
| 作者 | ctkqiang |
| 开源协议 | MIT License (Copyright 2026) |
| GitHub 仓库 | https://www.github.com/ctkqiang/NezhaCyberMCP |
| 官方网站 | www.nezhacyber.xin/zh |
| 编程语言 | Go |
| 提交历史 | 46 次提交，最新提交 2026 年 7 月 7 日 |

1.2 它是什么

NezhaCyberMCP 的本质是一个 MCP（Model Context Protocol）服务器。它从 CIRCL、MyCERT 和 GitHub Advisory Database 三大数据源聚合安全公告数据，通过 MCP JSON-RPC 2.0 协议直接服务于 AI 助手。

目前支持的 AI 客户端包括：

▪Claude Code（Anthropic）

▪Cursor

▪VS Code Copilot

▪OpenAI Codex

▪Trae IDE

简单来说，配置好 NezhaCyberMCP 后，你可以在 AI 助手中直接提问“最近有哪些 CRITICAL 级别的 CVE？”，AI 会自动调用 MCP 工具查询并返回真实漏洞数据。

1.3 解决什么问题

传统的漏洞管理流程是：开发 → 构建 → 安全扫描 → 发现漏洞 → 修复 → 重新构建。漏洞发现得太晚，修复成本高。

NezhaCyberMCP 将这个链路前置：编码阶段 → AI 助手实时查询 CVE → 即时告警 → 当场修复。它让安全意识嵌入到开发最前端，而不是等到 CI/CD 阶段才发现问题。

1.4 设计理念：非阻塞启动

这是 NezhaCyberMCP 最核心的设计决策之一——MCP 服务器先启动完成握手，数据库在后台热注入。

这意味着：

1.  AI 助手连接 MCP 服务器时零等待——服务器瞬间就绪，立即响应握手请求

2.  数据库初始化、表迁移、首次数据同步在后台 goroutine 中异步执行

3.  数据库就绪后通过 SetDB() 热注入到 MCP 服务器，之后所有工具调用即可查询完整数据

这种设计保证了用户体验：无论数据库同步需要多长时间，AI 助手的连接和基础功能都不受影响。

二、架构说明

2.1 六层架构总览

NezhaCyberMCP 采用清晰的六层架构，从上到下依次是 AI 客户端层、传输层、MCP 协议层、持久化层、数据库层和数据摄入层：

|  |  |
| --- | --- |
| AI Client 层  MCP JSON-RPC 2.0 | Claude / Cursor / VS Code / Codex / Trae |

▼

|  |  |
| --- | --- |
| Transport 层  传输层 | stdio (local)  |  SSE HTTP (Lambda) |

▼

|  |  |
| --- | --- |
| MCP Protocol 层  协议 + 调度 | MCPServer + 18 Tools (mcp.go)  Actions Dispatcher — actions.go 查询路由 |

▼

|  |  |
| --- | --- |
| Persistence 层  Repository Pattern | GORM repositories (3 tables)  Upsert / batch write / query |

▼

|  |  |
| --- | --- |
| Database 层  持久化存储 | PostgreSQL / MySQL / SQLite  Amazon Aurora DSQL (AWS) |

▼

|  |  |
| --- | --- |
| Data Ingestion 层  + Scheduling | CirclService / GithubService / MycertService  cron/v3 定时调度 |

▼

|  |  |
| --- | --- |
| External Data Sources  外部数据源 | CIRCL API / GitHub API  MyCERT Portal (HTML scraping) |

|  |
| --- |
| 📷  截图占位  六层架构图，可使用上方图示或 PlantUML 渲染后的 PNG。 |

各层职责说明：

▪AI Client 层：各类支持 MCP 协议的 AI 编程助手，通过 JSON-RPC 2.0 发起工具调用请求

▪Transport 层：本地模式使用 stdio（进程管道通信，无网络暴露）；Lambda 云端模式使用 SSE over HTTP（监听 /sse 端点）

▪MCP Protocol 层：核心调度层，包含 MCPServer 实例和 18 个已注册工具，actions.go 负责查询路由分发

▪Persistence 层：基于 GORM 的 Repository 模式，管理三张数据表，提供 Upsert、批量写入和查询能力

▪Database 层：支持 PostgreSQL（推荐生产）、MySQL、SQLite（本地开发）和 Amazon Aurora DSQL（AWS 云端）

▪Data Ingestion 层：三个数据源服务 + cron/v3 定时调度，负责从外部拉取并写入漏洞数据

2.2 通信方式：MCP JSON-RPC 2.0

MCP 协议基于 JSON-RPC 2.0 标准。这是一种请求-响应模型——AI 助手按需调用工具，服务器返回结果。不涉及心跳机制，通信完全由 AI 助手端驱动。

本地模式（stdio）：MCP 服务器作为子进程运行，通过标准输入/输出（stdin/stdout）与 AI 助手通信。无网络端口暴露，安全性最高，适合 Claude Desktop 等本地场景。

云端模式（SSE HTTP）：在 AWS Lambda 上运行，通过 Server-Sent Events（SSE）over HTTP 提供服务。AI 助手连接 /sse 端点发起请求，适合团队共享或云端部署场景。

2.3 非阻塞启动流程

这是理解 NezhaCyberMCP 设计的关键。启动流程如下：

|  |
| --- |
| ● 启动时序  main()   │   ├─ NewMCPServer(nil)          ← 立即启动，不需要 DB   │     registerTools()   │     registerResources()   │     registerPrompts()   │   ├─ goroutine: BackgroundInit()   │     InitDatabase(ctx, cfg)   │     mcpServer.SetDB(db)      ← 就绪后热注入   │     MigrateAll(ctx)   │     RunNow(ctx)              ← 立即首次同步   │     advisoryJob.Start(ctx)   ← 调度 cron   │   └─ mcpServer.Run(ctx)         ← 阻塞 stdio 循环 |

|  |
| --- |
| 📷  截图占位  非阻塞启动流程时序图，可使用项目 docs/ 目录下的 sequence.puml 渲染。 |

流程解读：

1.  main() 首先调用 NewMCPServer(nil)——传入 nil 表示数据库尚未就绪，但 MCP 服务器立即启动并注册所有工具、资源和提示词

2.  同时启动一个后台 goroutine BackgroundInit()，依次完成数据库初始化 → 热注入 DB → 表迁移 → 首次数据同步 → 启动 cron 定时调度

3.  主线程进入 mcpServer.Run(ctx)，阻塞在 stdio 循环上等待 AI 助手的请求

这个设计确保了 AI 助手连接时的零等待体验。

2.4 三种运行模式

| 模式 | 触发条件 | 传输方式 | 典型用途 |
| --- | --- | --- | --- |
| Local | IS\_LOCAL=true | stdio (JSON-RPC 2.0) | Claude Desktop，本地开发调试 |
| Lambda Sync | EventBridge cron 触发 | — | 定时数据同步任务 |
| Lambda MCP | MCP\_HTTP\_MODE=true | SSE over HTTP (/sse) | 云端 MCP 端点，团队共享 |

▪Local 模式：最常用，适合个人开发者在本地运行，配合 Claude Desktop 或 Claude Code 使用

▪Lambda Sync 模式：不提供 MCP 服务，纯粹用于定时同步数据到云端数据库，适合生产环境中保持漏洞数据持续更新

▪Lambda MCP 模式：在云端提供 MCP 服务端点，多个 AI 客户端可以共享同一个漏洞数据库

2.5 三大数据源

NezhaCyberMCP 从三个安全情报源聚合数据：

| 数据源 | 端点 | 认证方式 | 同步频率 |
| --- | --- | --- | --- |
| CIRCL CVE Search API | vulnerability.circl.lu/api/ | 无需认证 | 每 3 小时（cron 可配） |
| GitHub Advisory Database | api.github.com/advisories | Bearer Token (GITHUB\_TOKEN) | 开关控制，默认关闭 |
| MyCERT Advisory Portal | www.mycert.org.my | 无需认证（HTML 抓取） | 开关控制，默认开启 |

CIRCL 分页算法细节：每页拉取 100 条记录，请求间隔 500ms，最多 5 次重试，采用 2 秒指数退避策略。这保证了大量数据拉取时的稳定性和对上游 API 的友好性。

2.6 18 个 MCP 工具

NezhaCyberMCP 注册了 18 个 MCP 工具，分为四类：

查询工具（9 个）：

| 工具名 | 功能 |
| --- | --- |
| get\_cve | 根据 CVE ID 获取详细信息 |
| search\_cves | 搜索 CVE 漏洞 |
| search\_by\_cpe | 按 CPE（通用平台枚举）搜索 |
| bulk\_get | 批量获取多个 CVE |
| filter\_by\_severity | 按严重级别过滤 |
| get\_cwe | 获取 CWE（弱点枚举）信息 |
| get\_references | 获取参考链接 |
| related\_cves | 查询关联 CVE |
| whats\_new | 获取最新漏洞 |

分析工具（4 个）：

| 工具名 | 功能 |
| --- | --- |
| vuln\_trends | 漏洞趋势分析 |
| top\_vendors | 热门厂商排行 |
| top\_products | 热门产品排行 |
| severity\_distribution | 严重级别分布统计 |

资产匹配工具（1 个）：

| 工具名 | 功能 |
| --- | --- |
| match\_inventory | 将软件资产清单与 CVE 匹配 |

占位工具（4 个，尚未实现）：

get\_kev\_status、get\_epss、prioritize、match\_sbom——这些工具已在协议层注册，但功能尚未实现，为未来扩展预留。

三、环境要求与前置准备

3.1 操作系统要求

| 操作系统 | 最低版本 | 备注 |
| --- | --- | --- |
| macOS | 12 Monterey+ | 原生支持，推荐 |
| Linux | Ubuntu 20.04+ / Debian 11+ | 服务器部署推荐 |
| Windows | 10 / 11 | 需通过 WSL2 运行 |

3.2 软件依赖版本

| 软件 | 最低版本 | 用途 |
| --- | --- | --- |
| Go | 1.22+（安装指南）/ 1.26.1+（开发） | 编译构建 MCP 服务器 |
| Git | 2.x | 克隆仓库 |
| Node.js | 18 LTS+ | 运行 Claude Code、Codex CLI、MCP Inspector |
| npm | 9+ | 包管理，运行 MCP Inspector |
| 数据库 | PostgreSQL 推荐 | 也支持 MySQL / SQLite / Aurora DSQL |

3.3 数据库准备

NezhaCyberMCP 支持四种数据库：

▪PostgreSQL（推荐生产环境）：功能完整，性能稳定

▪MySQL：广泛使用，兼容性好

▪SQLite：适合本地开发快速测试，无需额外安装数据库服务

▪Amazon Aurora DSQL：AWS 云端无服务器数据库，适合 Lambda 部署

本地快速准备 PostgreSQL（以 macOS Homebrew 为例）：

|  |
| --- |
| ● bash  # 安装 PostgreSQL  brew install postgresql@16     # 启动服务  brew services start postgresql@16     # 创建数据库和用户  createdb nezha\_cyber |

|  |
| --- |
| 📷  截图占位  PostgreSQL 安装与数据库创建成功后的终端输出。 |

3.4 端口说明

▪本地 stdio 模式：无需开放任何网络端口，通信通过进程管道完成

▪SSE 模式：监听 PORT 环境变量指定的端口，默认 8080

3.5 前置检查清单

在开始安装前，建议逐项确认：

|  |
| --- |
| ● bash  # 检查 Go 版本  go version                 # 预期: go version go1.22+ ...     # 检查 Git 版本  git --version              # 预期: git version 2.x.x     # 检查 Node 版本  node --version             # 预期: v18.x.x 或更高     # 检查 npm 版本  npm --version              # 预期: 9.x.x 或更高     # 检查 PostgreSQL 连接（如果使用 PG）  psql -d nezha\_cyber -c "SELECT version();" |

|  |
| --- |
| 📷  截图占位  所有前置依赖版本检查通过的终端截图。 |

四、逐步安装配置教程

4.1 第一步：克隆仓库

|  |
| --- |
| ● bash  # 克隆 NezhaCyberMCP 仓库  git clone https://github.com/ctkqiang/NezhaCyberMCP.git     # 进入项目目录  cd NezhaCyberMCP |

|  |
| --- |
| 📷  截图占位  git clone 成功后的终端输出，显示克隆进度和完成信息。 |

4.2 第二步：配置环境变量

项目根目录下有 .env.example 模板文件，复制一份进行编辑：

|  |
| --- |
| ● bash  # 复制环境变量模板  cp .env.example .env |

编辑 .env 文件，根据你的实际环境填写配置：

|  |
| --- |
| ● bash · .env  # ============================================  # 运行模式配置  # ============================================  # true = 本地模式（启用 cron 定时同步 + stdio 通信）  IS\_LOCAL=true     # ============================================  # 数据库配置（PostgreSQL 示例）  # ============================================  ...