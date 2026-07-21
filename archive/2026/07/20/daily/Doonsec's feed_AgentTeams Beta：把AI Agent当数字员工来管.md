---
title: AgentTeams Beta：把AI Agent当数字员工来管
url: https://mp.weixin.qq.com/s/0HJdUH8y4qVxi2HveVAUGw
source: Doonsec's feed
date: 2026-07-20
fetch_date: 2026-07-21T05:00:45.462850
---

# AgentTeams Beta：把AI Agent当数字员工来管

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImnxxWPY1VZ7FAJnYMw6ECWnaB2icl78GqmQB5cXjEwB2PGIZrqJswkl8MKEyM214qeEL5XaX3HAoNXFW7hs1gcTu8dicqzmZrQls/0?wx_fmt=jpeg)

# AgentTeams Beta：把AI Agent当数字员工来管

敖胤AI
敖胤AI

爱唠叨的Nil

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

|  |  |  |
| --- | --- | --- |
| AI 工具 |  | 2026 年 07 月 20 日 |

# AgentTeams Beta：把AI Agent当数字员工来管

阿里云多智能体治理与协作平台，身份、凭证、审计、观测四件套齐全

Agent 不是脚本，是需要被组织、被治理、被观测的「数字员工」。AgentTeams 提供四层架构 + 治理中台，让多 Agent 协作从「并行更快」进化到「组织化运转」。

|  |  |
| --- | --- |
| 01 | AgentTeams：把 AI Agent 当「数字员工」来管  ALIYUN AGENTTEAMS BETA |

**AgentTeams** 是阿里云 2026 年 7 月发布的**企业级多智能体治理与协作平台**，目前处于 Beta 阶段。核心理念：AI Agent 不是脚本，而是需要被组织、被治理、被观测的**数字员工**。

支持统一控制台创建和管理 AI Worker，接入多个模型供应商，集成 MCP 工具服务，实时监控运行状态。支持多成员、多角色的团队协作和权限管理。

|  |  |  |  |
| --- | --- | --- | --- |
| 阿里云 | Beta | 多智能体治理 | 企业级 |

|  |  |
| --- | --- |
| 02 | 四层架构 + 治理中台  FOUR-LAYER ARCHITECTURE |

**入口层**（IM 集成，不逼员工换工具）→ **身份层**（对接 IdP/SSO，签发可追溯工作身份）→ **组织层**（按职能编成团队，TL Agent 调度）→ **资产管理层**（模型、Skill、MCP Server 集中管理，BYOC 自主可控）。

右侧贯穿一条观测、度量、治理中台：从 Token 消耗到 Prompt 分析到效果审计，全程可见。

真正的 Agent 群聊，是多个真人 × 多个 Agent × 共享上下文 × 异步任务 × 带显式身份权重的扁平协作拓扑。

|  |  |  |  |
| --- | --- | --- | --- |
| 4层  架构层级 | 3级  权限分级 | BYOC  自主可控 | MCP  工具集成 |

|  |  |
| --- | --- |
| 03 | 身份是工牌，凭证是门禁  IDENTITY & CREDENTIAL |

Human 侧三级权限：**L1 Admin**（组织管理员）、**L2 Team Leader**（团队领导）、**L3 Worker**（日常请求者）。

每个 Worker 携带四个声明式文件：**SOUL.md**（它是谁）、**AGENT.md**（怎么干活）、**MEMORY.md**（记住了什么）、**USER.md**（服务于谁）。

凭证采用零信任设计：密钥集中在 Higress AI Gateway 托管，Agent 只拿可撤销短时 Token，用完即收。

为什么紧迫

同期 Cursor IDE 爆出 CVE-2026-50548（CVSS 9.8），正是 Agent 被注入后拿到不该拿的权限。凭证托管是 Agent 上生产的及格线。

|  |  |
| --- | --- |
| 04 | 审计是考勤，观测是考核  AUDIT & OBSERVABILITY |

每次工具调用记录**「操作者 + 时间 + 入参 + 出参 + 结果」五元组**，成本与审计同源。

配套 **AgentLoop** 提供无侵入全栈可观测，Agent-as-a-Judge 评估范式自动识别幻觉，形成数据飞轮。

|  |  |  |
| --- | --- | --- |
| 五元组审计 | AgentLoop | 数据飞轮 |

|  |  |
| --- | --- |
| 05 | 四大应用场景  USE CASES |

· 企业数字员工：通过钉钉/飞书/企微发起任务，Agent 按 MCP 访问 CRM/OA/ERP

· Agent Team 服务化：按角色创建 Team 池，RBAC 按需申请，权限隔离与独立计费

· SaaS 多租户：每租户独立 Agent Team，Skills/MCP 按授权分配，数据隔离

· 存量 Agent 纳管：异构 Agent（Claude Code、QwenPaw 等）混编统一治理

|  |  |
| --- | --- |
| 06 | 给行业发了一张「体检表」  WHY IT MATTERS |

AgentTeams 的真正价值：把「多 Agent 协作的终局不是并行更快，而是组织化运转」这件事说破了。

你招一个真人员工，要发工牌、管门禁、记考勤、做考核。Agent 作为数字员工，这四件事一个都省不掉。

目前处于 Beta 阶段，支持杭州、北京、新加坡。已开放快速入门文档。

从聊天框到组织

排版由达尔文编辑引擎 v2.0 生成 · 标题策略师 v2.0 辅助 · 2026 年 07 月 20 日

预览时标签不可点

作者提示: 内容由AI生成

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

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