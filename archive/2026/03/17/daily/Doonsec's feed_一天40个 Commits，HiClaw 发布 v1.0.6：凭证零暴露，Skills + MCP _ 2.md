---
title: 一天40个 Commits，HiClaw 发布 v1.0.6：凭证零暴露，Skills + MCP > 2
url: https://mp.weixin.qq.com/s/5kUJrIrfvDLdrMHW-0LVaw
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:19:58.605102
---

# 一天40个 Commits，HiClaw 发布 v1.0.6：凭证零暴露，Skills + MCP > 2

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XU4ficyUpeGxcV0ElFHmNjd2IYnzNibXw0d3hiawW1tJk0LfRFTtHicfpZsiafPIxRH0jukaa4UWHjucFjbFOibCGU3YN8ULJURKB8PfCk4fBG5FI/0?wx_fmt=jpeg)

# 一天40个 Commits，HiClaw 发布 v1.0.6：凭证零暴露，Skills + MCP > 2

爱唠叨的Nil

![]()

在小说阅读器中沉浸阅读

以下文章来源于Higress
，作者澄潭

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4vj74U6jciahKDcIBBjSJarTeO2uPnYsNXjr6mIuOGEew/0)

**Higress**
.

开源项目：Higress 网关、HiClaw 多 Agent 协作网络、HiMarket Agent 开放平台。

💡 目录 💡

    01  凭证安全的困境

    02  什么是 MCP？为什么它很重要？

    03  介绍 mcporter：通用 MCP CLI

    04  MCP 与 SKILLS：互补而非替代

    05  架构：一切如何运作

    06  端到端示例：添加自定义 API

    07  从 Swagger/OpenAPI 到 MCP 工具

    08  从 curl 到 MCP 工具

    09  Worker 生成的 Skills：自我完善的文档

    10  安全模型：深度防御

    11  这对路线图意味着什么

    12  其他改进

    13  快速开始

    14  接下来是什么

01

# 凭证安全的困境

如果你在生产环境中运行 AI Agent，可能面临过这样的两难选择：

**"我想让 Agent 用 GitHub，但不想把我的 PAT 给它"** — 一个泄露的 token 就可能导致仓库被攻击。

**"我需要 Worker 调用内部 API，但那些密钥太敏感了"** — 计费系统、数据库、支付网关的 API key... 给 Agent 用风险太大。

**"不同 Worker 需要不同权限，但管理起来简直是噩梦"** — 前端 Worker 应该有生产数据库的访问权限吗？大概不应该。但怎么强制执行？

在 1.0.6 版本中，我们带来了全面的解决方案：**基于 Higress AI Gateway + mcporter 的企业级 MCP Server 管理**。

02

# 什么是 MCP？为什么它很重要？

**MCP (Model Context Protocol)** 是一个开放标准，用于将 API 暴露为 AI Agent 可以发现和调用的工具。可以把它理解为"给 AI Agent 用的 OpenAPI"—— 你不需要手动给 Agent 讲解每个 API 端点，只需要定义一次 MCP 工具，任何兼容 MCP 的 Agent 都可以立即使用。

MCP 的美妙之处在于它将**工具定义**和**凭证管理**分离。工具的 schema 说明了"这个 API 做什么，需要什么参数"，但不会说"这是 API key"。这种分离是企业级安全部署的基础。

03

# 介绍 mcporter：通用 MCP CLI

在深入了解 HiClaw 的集成之前，让我们先介绍 **mcporter** *******[****1]*******—— 由 Peter Steinberger*******[****2]*******（OpenClaw 作者）开发的强大 MCP 工具包。

mcporter 是一个 TypeScript 运行时、CLI 和代码生成工具包。核心能力：

* **零配置发现：自动发现 Cursor、Claude Code、Codex、Windsurf、VS Code 中配置的 MCP 服务器。**
* **友好的 CLI：用**`cporter call server.tool key=value` 调用任意 MCP 工具。
* **类型安全：生成带有完整类型推断的 TypeScript 客户端。**
* **一键 CLI 生成：将任意 MCP 服务器转换为独立的 CLI 工具。**

```
# 列出所有已配置的 MCP 服务器
mcporter list

# 查看某个服务器的工具和完整参数 schema
mcporter list github --schema

# 调用工具
mcporter call github.search_repositories query="hiclaw" limit=5
```

```

```

在 HiClaw 1.0.6 中，Manager 和 Worker 都使用 mcporter 与 MCP 服务器交互 —— 但通过 Higress AI Gateway 实现了关键的安全增强。

##

04

# MCP 与 SKILLS：互补而非替代

在了解 HiClaw 的 MCP 集成架构前，有必要先澄清 **MCP 和 SKILLS 的关系**。

### HiClaw 的开放技能生态

HiClaw 通过对接 skills.sh *******[****3]*******支持**开放的 SKILLS 市场**，并且支持对接 **Nacos 的企业自建 SKILLS 市场**。SKILLS 是面向实际场景的、可迭代的能力包装：

* **场景导向：将多个原子工具组合成完整的业务流程。**
* **持续演进：基于实战经验不断优化和改进。**
* **知识沉淀：包含最佳实践、错误处理、参数说明。**

###

# MCP 在生态中的定位

MCP 并不是要取代 SKILLS，而是作为 **SKILLS 生态中的补充**，用于快速将已有的 API 转换成标准的 Agent 可使用的工具。MCP 的核心价值在于：

* **明确的约束和规范：对工具有着更严格的定义和类型约束。**
* **权限治理体系：可以复用 MCP 的认证鉴权能力（MCP Server 粒度的权限管理，企业版支持工具粒度）。**
* **批量转换能力：尤其在企业场景下，基于 Higress 的 MCP 网关能力可以无痛地将大量存量 API 批量转换成 MCP 工具，实现精细化管理。**

###

### mcporter 的桥接作用

通过 mcporter 这样的 CLI 工具，HiClaw 实现了 **MCP 工具的重新编排和组织**，形成可迭代的 SKILL：

```
MCP 工具（原子能力）
    ↓ mcporter 编排
SKILL（场景化能力包）
    ↓ 实战使用
SKILL 迭代优化
```

```

```

### SKILL + MCP = 1+1 > 2

两者的最佳实践是：

* **SKILL 负责场景演进：贴合实际业务场景，不断迭代技能的组合逻辑和最佳实践。**
* **MCP 负责细粒度权限管控：贴合业务能力做好 MCP Server 和工具的权限治理与凭证管理。**

这种互补关系实现了 **SKILL + MCP 1+1 大于 2 的效果**：企业既能享受开放 SKILLS 市场的丰富能力，又能通过 MCP 网关对企业内部 API 实现安全、精细的权限管控。

05

# 架构：一切如何运作

当你想为 Worker 添加一个新的 API 工具时，完整流程如下：

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              你（人类）                                       │
│                                                                             │
│  "添加一个股票指数 API：GET https://api.finance.com/v1/index?symbol={symbol}"  │
│  "通过 X-API-Key header 认证，这是我的 key：sk_xxx"                            │
└────────────────────────────────────┬────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           MANAGER CLAW                                      │
│                                                                             │
│  1. 根据你的描述生成 MCP Server YAML 配置                                       │
│  2. 运行 setup-mcp-server.sh stock-index "sk_xxx" --yaml-file /tmp/stock.yaml│
│  3. 用 mcporter 验证：mcporter call stock-index.get_index symbol=000001.SH    │
│  4. 通知 Worker："新 MCP 服务器 'stock-index' 已就绪"                           │
└────────────────────────────────────┬────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        HIGRESS AI GATEWAY                                   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  MCP Server: stock-index-mcp-server                                 │    │
│  │  ├─ 真实凭证: sk_xxx（安全存储，永不暴露）                               │    │
│  │  ├─ 工具: get_index(symbol: string) → 股票指数数据                    │     │
│  │  └─ 授权消费者: manager, worker-alice, worker-bob                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  向 Worker 签发临时 consumer token                                            │
│  Token 只能调用已授权的 MCP 服务器                                              │
│  真实 API key 永远不会离开网关                                                 │
└────────────────────────────────────┬────────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           WORKER CLAW                                       │
│                                                                             │
│  1. 收到 Manager 的通知                                                       │
│  2. 从 MinIO 拉取最新的 mcporter 配置                                          │
│  3. 发现工具：mcporter list stock-index --schema                              │
│  4. 测试工具：mcporter call stock-index.get_index symbol=000001.SH            │
│  5. 基于理解生成 SKILL.md                                                     │
│  6. 后续任务中即可使用该工具！                                                   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  Worker 的视角：                                                     │    │
│  │  ├─ 拥有：Consumer token（就像一张"工牌"）                              │    │
│  │  ├─ 可以：通过网关调用 stock-index.get_index                           │    │
│  │  └─ 不可以：看到真实的 API key sk_xxx                                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

如下图所示，也可以直接上传swagger文件给Manager自行分析：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XU4ficyUpeGxQmOmvouh3CjEsOjUVtPpe00Ts1ZRIaCKTPZsO2KDWs8r7ARUkhtYvYuQaJpX1hO2exRtawjLv60y1lnFsB72ck14wHFkF1fg/640?wx_fmt=jpeg&from=appmsg "null")

配置完成后，Manager 可以在 **Higress 控制台**查看 MCP Server 下的工具列表，并进行进一步的权限管理：

![](https://mmbiz.qpic.cn/mmbiz_jpg/XU4ficyUpeGxsnyLm3TlDQ3x9eddB1YeY3JDp10z39TH8Q10Z18TgibrlRasCWW6wcEYCs7pSPDpmCGBaACPgwbibyg7HTCQKBgoulLGG93ibBY/640?wx_fmt=jpeg&from=appmsg "null")

通过控制台，你可以：

* 管理调用凭证（例如不用告诉manager真正的凭证，而是到控制台手动配置）
* 查看 MCP Server 包含的所有工具
* 为每个 Consumer（Worker）配置 MCP Server 级别的访问权限
* 监控工具调用情况和性能指标
* 动态调整权限策略，无需重启服务

权限管理说明：

* Higress 开源版：支持 MCP Server 粒度的权限管理（例如：Worker A 可以访问整个`stock-index MCP Server` ）
* Higress 企业版：支持 工具粒度的权限管理（例如：

  Worker A 只能调用`istock-index.get_indext` ，

  但不能调用`istock-index.update_indext` ）

HiClaw 1.0.6 基于开源版实现了 MCP Server 级别的安全隔离，已能满足大部分企业场景的权限管控需求。

**核心安全原则：Worker 永远看不到真实凭证。**

即使 Worker 被完全攻破，攻击者也只能获得一个 consumer token：

* 只能调用你授权的特定 MCP 服务器
* 可以被 Manager 瞬间吊销
* 不包含任何可复用的凭证信息

##

06

# 端到端示例：添加自定义 API
...