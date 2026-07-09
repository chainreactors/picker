---
title: Harness 工程实战第4篇：Agent 平台的五类定义
url: https://mp.weixin.qq.com/s/dlqgTtBspKTOSBIjUc8awQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T06:00:45.547584
---

# Harness 工程实战第4篇：Agent 平台的五类定义

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP8524vTdibBebAzDHzA8KrALMQcIkZUiacmUALcW0ggxpnLhgqDDChYzibh8hPsypjFcq7aO1ke0V4pQD4YRG8c6m4f08wWCjXsodck/0?wx_fmt=jpeg)

# Harness 工程实战第4篇：Agent 平台的五类定义

原创

Max Luo
Max Luo

白帽子罗棋琛

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 本篇按五个概念顺序逐个给定义、边界和踩坑：每对象给三件事，能做什么、不能做什么、它在仓库里长什么样。最后用一张关系图收口，再讲三条术语漂移的实际教训（Tool 升一级 / 新增第六类 / Skill 和 Plugin 混用）。这套五类切法是作者在 CyberClaw 里反复试错后收敛的工程决定（早期版本里 Skill 既能描述也能执行，治理就崩了），不是行业共识。

行业里把"对象模型"做得最清晰的是 Anthropic 和 OpenAI，前者用 Augmented LLM（LLM + Retrieval + Tools + Memory）给 building block 视角，后者用 Foundations（Model / Instructions / Tools）给功能切法，但两家的切割都偏向 mindset 而非工程边界。LangChain 和 Microsoft Semantic Kernel 把"工具集成"做成一级生态对象（Plugin marketplace），结果是 Tool / Function / Plugin 边界互相踩；Hermes Agent 与 OpenClaw 在 Skill 包格式上探索过"方法 vs 执行"的分离。CyberClaw 把这几条路线的工程结论合到五个定义上，每一类对应一条独立治理边界，本篇展开它们是怎么切的。

## 1. Anthropic 太宽，OpenAI 太松

第 2 篇收口了 Anthropic + OpenAI 的词表。但有一个收不进去的问题：两家的概念都太抽象，无法直接落地成一套可治理、可演进的工程边界。

回看：

Anthropic 的 Augmented LLM：

```
1. LLM +Retrieval+Tools+Memory
```

这是 building block，是理解抽象，不是工程边界。一个 production Agent 平台不能只有这 4 个组件，你怎么治理 Tools 的权限？哪些 Memory 是租户级、哪些是全局？Retrieval 接外部知识库时是和 Tools 一样过 permission，还是单独走一条路？

OpenAI 的 Foundations：

```
1. Model+Instructions+Tools
```

更宽。Instructions 既包括 system prompt 又包括 task 描述又包括 behavior 约束，三件不同生命周期的事被压成一类。

两家作为 mindset 都对，但作为工程模型都不够。这就是为什么 production agent 平台几乎一定要在两家之上再做一层切割，切的依据不是"它是什么"，是"它的治理边界在哪、它的扩展边界在哪、它的版本生命周期在哪"。

CyberClaw 给出的答案是5个定义对象：

| 维度 | 定义 | 作用 |
| --- | --- | --- |
| 谁动手 | Agent | 决策与编排 |
| 怎么做 | Skill | 方法 / 知识 / 模板 |
| 用什么 | Connector | 唯一代码级能力接入面 |
| 最小动作 | Capability | 治理与授权最小颗粒 |
| 平台增强 | Platform Plugin | 跨切面能力扩展 |

下面 5 节逐个展开。每个对象给三件事：它能做什么、它不能做什么、它在仓库里长什么样。

---

## 2. 五类定义

### 2.1 Agent，谁动手

定位：决策主体 + 编排者。

能做：

* 接收 Task / Case，决定调用哪些 Capability、按什么顺序
* 维护当前任务的 ExecutionPlan、迭代预算、Story 状态
* 选用合适的 Skill（方法包）来指导自己怎么完成任务
* 在 PersistentExecution 模式下跨 session 持续

不能做：

* 不能直接调 Connector，所有动作必须经 Capability → Governance → Connector
* 不能绕过 Governance，Iron Law 在 prompt 里、Permission Matcher 在执行层，两道都拦
* 不能替代底层执行器，决定"做什么"，不亲自做

代码位置： `crates/cyberclaw-agent-runtime/`

一句话边界：Agent 是大脑，不是手。

![](https://mmbiz.qpic.cn/mmbiz_png/4yRoMuNP850Ciau8Mcib7v7rquLRClpevmBDQ1tnibcBB6hx00KGicICmRP3PJ1kkBMkybE2XpuDVKiaNN2PF60b5AGOaU5amaJLAfPvJibLG4Vrk/640?wx_fmt=png&from=appmsg)

### 2.2 Skill，怎么做

定位：方法 / 知识 / 模板的载体。

能做：

* 携带 `SKILL.md`（说明）、 `scripts/`（脚本）、 `references/`（参考资料）、 `assets/`（资源）
* 兼容主流 skill 生态（Claude Code Skill / Codex Skill / OpenClaw Skill）
* 被 Agent 加载后作为"方法手册"指导决策
* 提供可复用的 Procedural memory（第 3 篇的概念）

不能做：

* 不能直接拥有平台执行权限，这是 `AGENTS.md第2.1.3节` 显式约束
* 不能替代 Connector ，Skill 里的 script 想跑 shell，必须通过 ShellConnector 这种受控接入点
* 不能承载租户治理，租户隔离是 PolicyEngine 的事，不是 Skill 的事
* 不能成为"隐藏执行入口"，任何 Skill 引发的动作都必须显式过治理链

代码位置： `crates/cyberclaw-skill-runtime/`

一句话边界：Skill 是说明书，不是执行器。

为什么这条边界这么硬：如果 Skill 可以执行，那 Skill 就是 Agent；如果 Skill 可以接入能力，那 Skill 就是 Connector。术语合并 = 治理崩塌。

生态兼容： `cyberclaw-skill-runtime/src/compat/mod.rs` 文件头注释显式声明 CyberClaw 兼容五个外源 Skill 生态， `hermes/anthropic/claude_code/openclaw/superpowers`。每个生态在 `compat/translators/` 下有独立 translator（如 `translators/hermes.rs` 把 hermes 的 `browser_navigate` 别名映射到 CyberClaw facade）。这种"兼容多生态而不发明新格式"是 Hermes Agent 与 OpenClaw 项目 SKILL 包格式的合并产物，CyberClaw 不另起炉灶，让 Skill 库可以从这些生态直接迁过来（详见 ACKNOWLEDGMENTS.md）。

### 2.3 Connector，用什么

CyberClaw 设了一条硬约束：所有外部能力的接入都必须经过 Connector，没有例外。这不是优雅问题，是治理面要不要有抓手的问题。Agent 直接调 shell、Skill 里塞个 HTTP 客户端、Plugin 用 OS exec 绕开，这些情况下治理面就看不到那些动作，等于把第 1 篇 demo 的所有问题原样请回来。

具体落地：Connector 是把 local 进程 / HTTP API / MCP server / 内部 RPC 包装成 Capability 调用的统一接入面。它通过 `ConnectorErrorClassifier` trait（第 6 篇展开）把外部错误分成 Transient / NonTransient / Unknown 三类，让上层的 retry / 换策略 / 升级决策有据可依。多 Agent 编排里的 `child-as-tool-call` 和 `HandoffConnector` 也是特殊形态的 Connector，第 11 篇会展开三种形态对比。外部知识检索（向量库 / 知识图谱 / 搜索引擎）也必须走 Connector 接入（第 17 篇），原因在第 9 篇详解：检索内容可能携带恶意指令，必须过 sanitizer 才能进 LLM context。

Connector 不能定义业务角色（那是 Agent 的事），不能自己决定调用顺序，不能绕过 PolicyEngine。 `AGENTS.md第2.3.2节` 是源头："Connector 是唯一代码级能力接入面"，想让 Agent 能调新东西，必须写 Connector，没捷径。

代码位置： `crates/cyberclaw-connectors/`。

一句话边界：Connector 是手，不是脑。

### 2.4 Capability，最小动作

什么叫"治理最小颗粒"？看这个对比： `fs.read` 和 `fs.delete` 都属于 `LocalConnector`，但治理上必须分别处理，前者 Severity::None，后者 Severity::High。如果对象模型把它们合并成 "FileOperation" 这一个对象，治理就失效了：你无法只允许 read 不允许 delete，要么全开要么全关。Capability 就是为了避免这种合并而存在。

它是单次扣动板机的动作，不是机关枪的整个攻击。每一个 Capability 在 ToolPermissionMatcher 的 24 条 glob 规则里被精确匹配，在 DangerousCapabilityFilter 的 7 条 Severity 规则里被评分。LLM 看到的工具描述（ `CapabilityFacade`，第 6 篇）是从 Capability 派生的只读投影，这条派生关系保证了 LLM 永远看不到 Capability 的内部字段（如 tenant*id、internal*metrics）。Autopilot 模式下， `auto_mode_gate` 会根据 Severity 动态剥离危险 Capability，退出 Autopilot 时还原（第 8 篇）。

Capability 不能跨 Connector 共享状态（每个归属一个 Connector），不能自我升级权限，不能跳过 trace，每次调用必落 Trace + Provenance。

代码位置： `crates/cyberclaw-core/`。

一句话边界：合并 Capability = 治理崩塌。

### 2.5 Platform Plugin，平台增强

Platform Plugin 处理那些"每个 Agent 都要用但不该每个 Agent 自己实现"的能力：trace 注入、token 计费、租户隔离。 `TokenTracker`（第 15 篇）和 `tenant_middleware`（第 7 篇）都是典型——注册为 platform-level，所有 Agent 共享，不用每次单独接。

边界同样硬：Plugin 不能绕过 Governance， `AGENTS.md第2.5.4节` 明确写着；Plugin 自己的行为也要落 trace，不能成为审计盲区；业务角色是 Agent 的事，Plugin 只做平台增强，两者不能混。把业务逻辑塞进 Plugin 是另一种术语漂移，和把执行逻辑塞进 Skill 同样危险。

代码位置：分散在各 crate，统一注册于 `cyberclaw-control-plane`。

一句话边界：Plugin 是地基插件，不是顶层应用。

---

## 3. 五类定义关系图

![](https://mmbiz.qpic.cn/mmbiz_png/4yRoMuNP853UGnmksuHGVLnPknNQK6R6rwiczQbPwngBWG1H74MpIITlE7ZIgaP78CZgKdlTv2asbacmnFsHTFRo0J1cAuvY0afibvxPnnvrI/640?wx_fmt=png&from=appmsg)

##

读图要点：

* 实线箭头：必经路径（Agent → Capability → Governance → Connector，不可绕）
* 虚线 use-as-method：Skill 是被参考的方法，不是执行链上的节点
* 虚线 augments：Plugin 是 cross-cutting 增强，不是主链的环节
* Skill 没有指向 Capability/Connector 的实线：这是核心约束，Skill 不直接执行

如果你画自己公司 Agent 系统的同样图，且 Skill 上有指向 Capability/Connector 的实线，那是术语漂移信号。

---

## 4. 三条约束

### 4.1 严禁把 Tool 升级为一级生态对象

典型踩坑：在五对象之外再加一类叫 `Tool` 的对象，"Tool 是 Capability 的高阶封装"。

为什么禁：Tool 这个词在 Anthropic / OpenAI / LangChain / Semantic Kernel 里都有自己的定义，引入它必然引入定义冲突。本系列第 2 篇已经把 Tool 收口为 Capability，如果在 Capability 之上再叠 Tool，等于回到第 2 篇之前的术语混乱状态。

真实教训：早期 CyberClaw 在 control-plane 里曾经有过一个 `ToolDescriptor` 概念，后来发现它和 `CapabilityFacade` 大量重叠、和 `Capability` 部分重叠，三个名字三套规则，治理无从下手。最终砍掉 `ToolDescriptor`，全部收口到 `CapabilityFacade`（第 6 篇展开）。

### 4.2 严禁新增第六类平台对象

典型踩坑："我有一个新概念叫 `Workflow`，应该是第六类对象。"

为什么禁：每加一类对象都是一套新的治理规则、版本管理、扩展边界、文档体系。维护 5 类已经是工程极限，加到 6 类会导致开发者不知道某个新功能该放在哪一类，最终所有人都把东西塞到自己最熟的那一类，对象边界崩塌。

真实教训：Workflow 一开始确实有人提议做成第六类对象。最后的设计是： `WorkflowTrigger` 是 control-plane 的内部机制（不是一级对象），workflow 执行步骤里的每个动作仍然落地到 Capability + Connector（第 12 篇展开）。

### 4.3 严禁把 Skill / Plugin / Connector 混成同一类扩展

典型踩坑：在 marketplace 里把 "Slack 集成 Skill" 和 "Slack 集成 Connector" 放在同一列表，让用户"选一个装"。

为什么禁：三者治理边界完全不同：

* Skill 不需要平台权限审批
* Connector 需要 PolicyEngine 集成审批
* Plugin 需要平台层注册和租户配置

混在一起 = 用户无法判断"我装这个安全吗"。

真实教训：早期 CyberClaw 的 plugin marketplace 设计想搞"一站式扩展"，后来在 review 时发现治理不可行，撤回设计，分成三个独立 catalog。

---

## 5. 概念映射

| 概念 | Anthropic | OpenAI | CyberClaw |
| --- | --- | --- | --- |
| 决策与编排主体 | Agent | Agent | Agent |
| LLM 调用 building block | Augmented LLM | (Foundations) | Agent + Skill（前者执行，后者方法） |
| 最小动作单元 | Tool | Tool / Function | Capability |
| 能力接入面（代码级） | （未细分） | （未细分） | Connector |
| 方法 / 知识包 | （未涵盖） | （未涵盖） | Skill |
| 平台级增强 | （未涵盖） | （未涵盖） | Platform Plugin |
| 多 Agent：保留控制权 | Orchestrator-Workers | agents as tools | child-as-tool-call（特殊 Connector） |
| 多 Agent：永久转交 | （未细分） | handoffs | HandoffConnector（特殊 Connector） |
| 工作流编排 | Workflow（5 模式） | (Orchestration) | WorkflowTrigger（control-plane 内部机制，非一级对象） |
| 验证 | Evaluator-Optimizer | Output Validation | EvidenceBasedVerificationGate（control-plane 内部） |
| 边界 / 治理 | ACI | Guardrails | Capability + Governance + Sanitizer |
| 长跑任务 | （未细分） | （未细分） | PersistentLoop（control-plane 内部） |
| 人工介入 | （未细分） | HITL Triggers | HITL + CircuitBreaker |

注意：右栏出现的所有"control-plane 内部机制"（WorkflowTrigger / EvidenceBasedVerificationGate / PersistentLoop）都不是一级对象，它们是把五对象编排起来的机制。第 5 篇会展开这条编排链。

## 6. 参考材料

* Hermes Agent / Ope...