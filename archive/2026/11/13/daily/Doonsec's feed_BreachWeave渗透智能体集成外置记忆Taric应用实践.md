---
title: BreachWeave渗透智能体集成外置记忆Taric应用实践
url: https://mp.weixin.qq.com/s/J9EgRGWkAhvG6Qbc38x_3Q
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:15:45.393222
---

# BreachWeave渗透智能体集成外置记忆Taric应用实践

# BreachWeave渗透智能体集成外置记忆Taric应用实践

原创

M-SEC社区
M-SEC社区

MSEC运营号

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

ENGINEERING · PRACTICE2026.11

渗透智能体不失忆、不越权、可审计

BreachWeave 智能体集成Taric的应用实践

绿盟科技 AI-PTS · BreachWeave · Taric

技术实践架构解析

大模型可以用于挖漏洞已经成为常识，但是像扫描器一样完整持续完成一个中型web系统的扫描、像EZ一样完成一个靶标单位的完整资产和漏洞测绘，过程不中断方向不偏离，仍是一个技术活。

外置记忆，也是绿盟科技AI-PTS智能渗透测试产品长周期不间断执行任务的核心技术之一。Taric作为独立外置记忆扩展，其效果已在上一篇幻境（AI-PTS单兵工具版）中也进行了效果验证。

![](https://mmbiz.qpic.cn/mmbiz_png/8G8EYcicic0aYbibAQCONDo6RmcwuibBAUUxDAs38BUD9C8icUrPAsPCyAHib2ianoANicqVWwvHh9xE0KOCRa49HclDFGB3C32qocBQIdFkR1LkEh0/640?wx_fmt=png&from=appmsg)

01

PART

渗透测试智能体长程任务需面临的问题

CHALLENGES · LONG-HORIZON TASKS

把 LLM 智能体放进一次真实的授权渗透测试里，它会很快撞上三道坎：

1

**失忆**：上下文窗口是智能体的全部工作记忆。一次真实测试动辄数小时到数天，工具输出、有效凭据、中间结论很快被压缩摘要冲掉；换一个 solver、重启一次会话，上一轮的经验留存几乎清零。

2

**失控**：智能体手里有 bash、nmap、sqlmap。它现在在打哪个目标？这个目标在不在授权范围内？它自认为“测完了”算数吗？——平台很难给出机器可验证的答案。

3

**无审计**：渗透测试是强合规业务。报告里的每一个漏洞，都需要给出存在性证明，测试过程都要留存证据。

BreachWeave 的 feature/taric 分支，把 Taric 这个「面向攻防智能体的长期记忆与治理组件」接进了平台核心，本文讲清楚它是怎么做到的，以及这套组合在工程上值多少。

02

PART

BreachWeave：多角色渗透智能体平台

PLATFORM · THREE ROLES

BreachWeave 是基于 pi-coding-agent SDK 构建的智能体渗透测试平台（Bun 运行时），采用三角色架构：

Manager / Planner（控制面）

：不亲自执行测试动作，只负责识别待测资产、决定启停 challenge 实例、调度 solver、汇总报告；

Solver（执行面）

：每个 solver 是一个 Kali 容器里运行的 pi-coding-agent 会话，面向具体资产执行信息收集、漏洞验证、利用链推进与报告提交；

Observer（旁路监督）

：solver 进程内的 sidecar 会话，维护「Ideas 看板 + 持久 Memory」，对 solver 产出做独立审查与轻量纠偏。

平台自带 Attack Flow 攻击流可视化（时间线回放、情报图谱、协作动态图），这是它区别于“单会话渗透 Copilot”的产品形态：**一支可以并行作业、被统一调度和监督的智能体攻击小队**。

![](https://mmbiz.qpic.cn/mmbiz_png/8G8EYcicic0ab7MYeicA1YKQv5VSfQB3JGH19NntGA43qibyhSAFbfrwYYLVHvceC8egbGlibKhpZ3TxdwLOdDiaXrqsz9jIcrt63bZbPADBj4DP0/640?wx_fmt=png&from=appmsg)

但把这样一支作战小小队放进长周期任务，基线的短板立刻暴露。

03

PART

Taric：为渗透智能体而生的「权威事实源」

AUTHORITY · SOURCE OF TRUTH

**一个记忆只有摘要碎片、状态没有权威源、动作没有审计链的渗透智能体**。这在 CTF 场景里和短时间执行任务中够用——短周期、链路少、结果或目标确定；但在授权渗透场景里，需要面临海量资产、海量测试过程任务数据、大量测试链路关联资源，这些问题都是致命伤。

Taric 的定位：**把渗透任务里所有“需要被信任、被治理、被追溯”的状态，从智能体的上下文和宿主的散落文件里拿出来，放进一个****带版本、带权限、带审计****的****权威事实源（authority）**。

它的领域模型覆盖了渗透项目的完整生命周期：

text

Engagement（项目）

　├─ Scope / ScopeRevision（ROE：授权目标、协议端口、时间窗，不可变修订链）

　├─ Resource / ResourceRevision（攻击面资产及变体）

　├─ Observation → Evidence → Claim → Finding（证据链，L0/L1/L2 三级信任）

　├─ WorkItem → WorkRun → Attempt → Checkpoint（执行，租约 + generation 防串话）

　├─ ActionIntent（动作审计：recommend → host-decision → host-result → reconcile）

　├─ CoverageManifest / CoverageCell（覆盖矩阵，9 种状态）

　└─ ReportSnapshot → CloseDecision（封板与关单，关后只读）

面向渗透场景的设计，为BreachWeave打好基础支撑：

1

**模型只能提案，宿主才能直写**。智能体产出的每条“事实”先以 proposal 进入候选态（L0），经评审准入升为 admitted（L1），独立复核后带 canonical id（L2）；而 WorkRun、Checkpoint、Action 这些治理状态机只接受 host principal 直写。模型永远无法把自己的想象直接写成事实。

2

**一切可追溯**。追加式审计链（hash / prev\_hash / commit\_seq）、不可变 ScopeRevision 修订链、CAS 版本化的 Artifact、动作四步审计——事后可以回答“谁在什么时候基于哪版授权做了什么决定”。

3

**fail-closed**。授权不满足就拒绝，版本不配对就拒绝，关闭的 Engagement 直接只读；PostgreSQL 不可用绝不回落 SQLite。安全系统宁可停，不可糊。

4

**边界清晰**。Taric 明确声明永久非目标：不运行模型、不调度智能体、不执行目标动作、不管理凭据生命周期。它只回答“什么是真、允许什么、如何追溯”，执行层的事留给宿主。

04

PART

Taric分层支撑：记忆层、治理层、生命周期层

INTEGRATION · THREE LAYERS

BreachWeave的feature/taric 实现，集成不是“把数据换个地方存”，而是按数据性质分层接管：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8G8EYcicic0aadyJAzibQBewqROTC99zm7DbjibWWboRkNpSYib13Jc2sa4J4t8F9aFQwslUr65MVlFpNqAWZWpwEicNhnnTgZpUgaCrM0t2C5XuM/640?wx_fmt=png&from=appmsg)

记忆层：proposal → admission 的项目级共享大脑

针对「失忆」，集成引入了 TaricMemoryProvider，把平台原有的两层看板（challenge 全局层 + solver 本地层）升级为**以 Taric 为权威的****项目级外置记忆**：

写入即提案

：solver/observer 产出的每条 memory、idea，都包装成 Taric claim proposal，显式标注 "BreachWeave model or operator proposal; not an admitted fact"。记忆不可 update/delete——发现写错了？追加一条修正提案。这保证了记忆的每次变更都有完整轨迹。

读取分信任级

：readBoard() 用 pinned read\_seq 快照同时拉取候选提案与 canonical 事实，两者 read\_seq 不一致直接报 conflict——读到的一定是某个一致时刻的世界。注入 solver 上下文时明确区分 candidate / admitted / local 三态，**候选永远不会被当成事实使用**。

断链可恢复

：Taric 不可达时（taric\_best\_effort 模式），写入进加密 outbox，恢复后按序幂等重放，以权威 read\_seq 推进水位；capture 类事件不自动重放，留给 operator 对账——不同数据不同策略，而不是一刀切。

有界读取

：单次读取上限 24 页 / 1000 条 / 4MB，并附完整分页诊断。外置记忆是给上下文“减负”的，不能反过来把上下文撑爆。

**与上下文压缩正交互补**：pi SDK 的 compaction 负责“压掉对话历史”，Taric 负责“保住压缩也压不掉的 durable facts”。solver 的任务提示里明确写着：初始上下文只带了压缩摘要，怀疑忘了已验证结论时先查 memory\_list。上下文可以被清空，关键事实可以从权威库重建——**这才是长任务续航的正确姿势**。

值得一提的是这套集成的验收方式：真实任务采样曾发现 297 次 host 事件捕获全部被 Taric 严格契约（unevaluatedProperties: false）拒绝——不是绕过契约，而是修复宿主的适配层（adaptCaptureDto）后全量通过。**严格契约在集成期就帮你提前暴露了脏数据问题**，这正是把权威源做严格的红利。

治理层：把 ROE 写进每一层校验

针对「失控」，新增的 authorized\_pentest 项目模式把授权从 prompt 嘱咐变成了**机器强制的控制面**：

结构化 ROE

：每个授权项目绑定 Taric 的 ScopeRevision——授权目标（域名必须提供 DNS 解析地址，hostname 与全部解析 IP 都必须在 allowedTargets 内、deniedTargets 优先拒绝）、协议与端口白名单、测试时间窗。每次出站动作前做 egress 预检，且 authorized 模式下判定由 TaricAuthorityActionService 以 canonical policy digest 强制，不信任宿主内存里的任何副本。

无授权即拒绝

：无有效 ScopeRevision 时，Taric 拒绝 WorkRun 的 claim、续租、checkpoint、Action 和 run-bound Artifact 操作；BreachWeave 侧则拒绝启动 solver、拒绝 planner 调度（TARIC\_GOVERNANCE\_REQUIRED），engagement 关闭后拒绝一切新任务。一个 solver 从生到死都跑不出授权围栏。

模型面零直连

：solver 容器不持有任何 Taric 凭据，全部请求经 host bridge（stdout JSONL）由宿主代理；生命周期身份（assignment / run / generation / epoch / scope / lease）只能由宿主从容器环境变量注入，**模型请求体里携带即拒绝**。即使走 MCP 通道，模型面也只有只读 + 提案工具。

本地只是投影

：challenge 定义、资产、提交、统计全部由 authorized-projection 从 Taric 权威快照重建，本地文件删了可以完整重建（smoke 验证 9/9 通过）；而凭据在投影重建时永远是占位符——**事实可以重建，秘密不可复制**。本地可信配置损坏时拒绝启动、绝不回退到本地任务状态。

崩溃有恢复协议

：宿主崩溃重启后对活跃 WorkRun 走 work.resume 的十项前提检查（engagement / scope / checkpoint / lease / context manifest……），可恢复则续跑，不可恢复则明确标记 replan\_required——不会出现“旧任务带着过期授权复活”的窗口。

生命周期层：报告即停止、独立审核、首轮目标观测

feature/taric 的另外两次提交解决了基线最烧钱的两个运行时问题：**solver 干完活停不下来**，以及**首轮任务漫无目标、资源释放不及时**。

**报告即停止（report-to-stop）**：新增 challenge\_submit\_progress / challenge\_submit\_final
双通道——增量进度不停 run；final 报告一旦被账本接受，立即生成 stop effect，run 进入 stopping。停止本身是一个三段式合同（grace 3s → hard deadline 10s → force stop），且必须拿到**物理退出证据**（waitpid / container\_exit / cgroup\_empty + 进程树退出 + 通道关闭）才算释放槽位。拿不到证据？那就标 unknown，继续处理——资源泄漏在合同层被堵死。

**独立审核链**：solver 自报完成 ≠ 完成。observer 以独立全史审查（分页读取 solver 全部历史，无证据 = missing、有声明无证据 = unsupported）产出 checklist，必须恰好覆盖全部分配项；planner 在 300 秒决策窗口内裁决 continue / stop。三层兜底保证这条链不会卡死：solver 侧主动退出探测（solver\_stop\_approved 即 dispose + exit）；observer 审查最多重试 3 次，超时放手交给宿主；宿主 sweep 在 10 分钟审查宽限期后用降级审查强制 stop 释放资源——**审查可以失败，但资源释放不依赖审查成功**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8G8EYcicic0aaLK3rvMZ4zyTNN3BTAapGM6iayicpNGRibAaqk3EKVok3vLv8oIRoPia5KPPBBUkavDZIr2x21lu01pXuicicj96d2cGOiaDTM8cAnFU/640?wx_fmt=png&from=appmsg)

**首轮目标观测**：planner 提示词现在把「首轮观测」作为最高优先级——未完成观测的项目不并行分配深入测试。观测轮固定四个产出：**资产可达性验证、（如提供）账号可用性验证、资产指纹与画像、首页主要功能清单**。快速观测完成后，才按“资产 × 攻击方向”拆分并行分工；不可达 / 账号不可用的结论直接转 blocked。这是把人类渗透测试的项目开局经验固化进了调度策略。

05

PART

Taric在BreachWeave上的实践价值

VALUE · SIX GAINS

**1. 任务续航力：从小时级到天级。** 外置记忆 + 上下文重建 + 断链 outbox，意味着任务可以跨 solver、跨会话、跨宿主重启延续。上一轮“目录遍历拿到三个凭据、其中一个已失效”这样的关键教训，不再依赖 observer 恰好把它写进 220 字符的摘要。

**2. 结论可信度：候选与事实永远分开。**
L0/L1/L2 信任分级贯穿记忆、证据与 finding——finding 必须绑定已准入的证据，独立审核把“自报完成”变成“证据支撑的完成”。给客户的报告里，每一句话都能回答“这是验证过的事实，还是智能体的推测”。

**3. 合规内建：ROE 从文档变成代码。** 结构化 ScopeRevision、egress fail-closed、Action 四步审计（建议→宿主决策→宿主结果→对账）、coverage gate 把关关单（覆盖矩阵存在缺口就不允许 close，关闭后整个 Engagement 只读）。这一套让“智能体做的渗透测试”第一次具备了通过甲方安全审计的叙事资格。

**4. 运维弹性：坏事情发生时的行为是确定的。** Taric 不可达 → 降级明确标注 + outbox 排队；宿主崩溃 → 十项前提检查恢复或 replan；升级 → 五个 @taric/\* 包版本与 integrity 锁定、66 项操作合同注册表比对，不配对即拒绝写入。故障模式是设计出来的，不是碰运气。

**5. 资源效率：观测先行、报告即停。** 首轮观测避免多容器盲跑；final 即停 + 物理退出证据 + 审查宽限兜底，容器与实例槽位周转率显著提升——对按容器计费的部署形态就是直接成本。

**6. 渐进式落地：双模式、可回滚。** 同一套核心，taric\_best\_effort（记忆增强，可断链）与 taric\_required（治理强制，不可降级）两种策略；项目级 memory\_mode 路由，竞赛遗产场景保留 legacy\_local 退出通道。这不是一次性豪赌式重构，而是每一步都可验收、可回滚的演进——三次提交本身就是这个方法论的展示。

06

PART

后续可演进的路线：治理即场景

ROADMAP · GOVERNANCE

集成不能停在记忆层。分支内的 lifecycle/ 目录为下一步演进做了一定的铺垫：Assignment / SolverRun / ReviewJob / Finalization 领域状态机、五元 fencing（revision × generation × epoch × scope × lease）、BudgetTree 多级预算、冻结证据包（FrozenReviewPack）与报告封板流水线；对应的 Taric 适配层锁定了下一代基线（Taric b2542a0 / Core 1.1.0 / API 1.5.0 / pi 1.5.0）。

CoverageCell 的多维矩阵也指向 OWASP WSTG 覆盖字典——**当“测完没有”由覆盖矩阵而不是智能体的自我感觉决定时，渗透测试的****完成判据才第一次可仲裁**。

在更长远的路线上，可以规划设计：per-project ...