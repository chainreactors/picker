---
title: AlertZero 如何运作：Elastic Security 的 AI 安全运营智能体
url: https://mp.weixin.qq.com/s/8t651WINfBkeBgElvih4Rg
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:36:55.067588
---

# AlertZero 如何运作：Elastic Security 的 AI 安全运营智能体

# AlertZero 如何运作：Elastic Security 的 AI 安全运营智能体

Elastic
Elastic

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

*作者：James Spiteri, David Elgut, Mia LaVada*

我们接触的大多数安全运营中心 (SOC) 团队都在描述同一个问题。告警的数量多过处理它们的人手，于是看哪些告警由队列来决定，威胁狩猎和检测规则调优则不断被推到下一周。而一条告警耗掉的时间，大部分都花在挖掘上下文上，比如这条规则此前是否在这台主机上触发过、当时周围还有别的什么在发生。我们构建 AlertZero，就是为了替你完成这类挖掘，让你的分析师把时间花在真正需要他们下判断的地方。从今天起，随 Elastic Security 9.6 一同发布，AlertZero 已在 Elastic Cloud Serverless 上以技术预览 (technical preview) 形式提供，并预计于 12 月初在 9.6 版本中面向 ECH 和 Self-Managed 部署提供。

2026 年 10 月，我们先行介绍了 AlertZero，在那篇文章里，我们从第一条告警开始追踪一次可疑登录，经过调查中收集的证据，一直到一项等待分析师批准的主机隔离建议。今天，我们把技术预览版里的内容完整拆开来讲：六个 Workers 各自提出什么建议、在每个自主级别上它们能做什么、如何选择模型，以及如何上手，文字和视频两种形式都有。

## AlertZero 里有什么：4 个 Watches 和 6 个 Workers

先从整体概览说起。AlertZero 覆盖 SOC 工作的四个领域：告警分诊、威胁狩猎、检测工程和端点取证。每个 Watch 对应其中一个领域，并容纳负责该领域工作的 Workers。一个 Worker 承担一项具体工作，比如分诊新告警，或者调优一条噪声很大的规则。

![AlertZero Watches：Triage、Hunt、Detection 和 Forensics，各自配一个示例 Worker，位于你的安全团队之下](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaWBFssa956pgTyEWJtVxJg4pJ4iaXPW1reUT9SMnNjbDZysJ2tp84Pic3vqZqhwZCejykYNvArcSCzSaxy1k4nP3M9Ogvtk8pUQ/640?wx_fmt=png&from=appmsg)

AlertZero Watches 与示例 Workers。

在实现层面，每个 Worker 都是归属于某个 Watch 的、由 AI 驱动的工作单元。它在后台运行，可以按计划执行，也可以响应新告警之类的事件，随后分析你的数据，并把建议操作呈现给你。每个 Worker 都以 Elastic Workflows 中的工作流形式构建，各自拥有独立的设置，包括执行计划和自主级别。

### AlertZero 深度解读视频

下面是一段视频概览，由 Elastic 的 James Spiteri（安全产品管理高级总监）与 Jackie McGuire（安全产品营销管理高级总监）为你演示 AlertZero。

AlertZero 深度解读视频

## 我们为什么这样构建 Workers 和 Watches

AlertZero 把每个 Worker 都构建成由确定性步骤组成的工作流，只在需要判断的地方调用模型。这种拆分带来四个效果：

**•** 查询与检查以代码方式运行，因此每次的行为都完全相同。

**•** 你可以用证据核对模型的结论，因为它的输入是从你自己的环境中读取的数据。

**•** 成本保持在较低水平，因为模型调用只发生在需要判断的步骤上。

**•** 环境中没有任何变更会仅凭模型的建议发生。Worker 的 AI 步骤只能读取你的数据，所有变更都由确定性步骤执行。至于其中哪些变更需要等待批准，由它的自主级别决定。

要查看一个 Worker 是如何得出结论的，你可以打开这次运行记录，逐步跟踪它走过的每一步。 当一个 Worker 认为你的环境中有东西应当变更（例如某个假阳性应当关闭，或者某台主机应当隔离），它会把它写成一项建议操作。这份建议会列出这个 Worker 想做什么、为什么这样做，以及它发现了什么。你为该 Worker 指定的自主级别（Manual、Assisted 或 Supervised）决定它接下来怎么走。在 Manual 级别下，它会一直等待，直到团队里有人批准或拒绝这项建议。

本次技术预览版包含六个 Workers：

| **Watch** | **Worker** | **Worker 的作用** |  |  |
| --- | --- | --- | --- | --- |
| Triage Watch | Alert Triage Worker | 把新告警分类为真阳性或假阳性，并为每条给出置信度评分 | 关闭它分类为假阳性的告警 | Manual, Supervised |
| Triage Watch | Attack Discovery Worker | 把相关告警归组为潜在攻击，并为每一起开启一次调查 | 对看起来真实或无法排除的攻击进行端点分析 | Manual, Supervised |
| Hunt Watch | Continuous Threat Hunt Worker | 在你的数据中搜索与威胁报告相符的活动，并记录发现的任何检测缺口 | 当你的数据与威胁报告相符时执行响应操作，并把检测缺口交给 Rule Coverage 审阅 | Manual |
| Detection Watch | Rule Tuning Worker | 找出持续产生假阳性的规则，并确定原因 | 针对分析师反复作为假阳性关闭的规则，提出修改与例外项 | Manual, Assisted |
| Detection Watch | Rule Coverage Worker | 审阅 Continuous Threat Hunt 记录的检测缺口 | 启用、安装或创建规则以补齐检测缺口 | Manual, Assisted |
| Forensics Watch | Endpoint Analysis Worker | 在涉及的主要主机上重建攻击时间线，并提取入侵指标 | 隔离主机，或终止、挂起进程 | Manual, Supervised |

## Alert Triage Worker 如何分类告警

基础讲完，我们来看 Alert Triage Worker 一次运行的内部发生了什么。它是 Triage Watch 里的两个 Workers 之一。每个 Worker 都是工作流，由以代码方式运行的确定性步骤、以及只在需要判断时才调用模型的 AI 步骤组成。

每次运行，Alert Triage Worker 都会接手新告警，并从一名 SOC 分析师在决定关闭还是升级一条告警、或者进一步深挖之前会走的那些步骤开始。它会查询这条规则过去的告警是如何关闭的、这类活动在你的环境中有多常见。它还会查询这条规则是用来检测什么。这些查询都是确定性的，不涉及模型。

只有在证据汇集完成之后，Worker 才把它交给模型，而且只在一个 AI 步骤里完成：判断每条告警看起来是真阳性还是假阳性，以及它对这一判断有多确信。随后，Worker 的确定性步骤再次接管，记录判定结果，并对把握较大的假阳性提出关闭建议。

![Alert Triage Worker 工作流：四次确定性查询、一个对告警进行分类的 AI 步骤，随后由代码提出关闭建议](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShOqKE4FVlywKA1d6BliaMdBJZ2sFYysQVx3c5HNruXDVUoJtWwWkibLTuGQwuy34GMez1oTfDc4YwbFrxic6Pibln7pgMkzMjvUpA/640?wx_fmt=png&from=appmsg)

Alert Triage Worker 的工作流在 Triage Watch 内同时包含确定性步骤和 AI 步骤。

## AlertZero 的 Workers 如何相互交接工作

你可以按任意组合运行 Workers。举例来说，一个主要希望在分诊和噪声规则上得到帮助的团队，可以只运行 Alert Triage 和 Rule Tuning，而不开启 Attack Discovery 或 Endpoint Analysis。Alert Triage 标记出的假阳性会计入 Rule Tuning，后者负责找出持续产生这些假阳性的规则并提出修复建议。其他 Workers 之间也以同样的方式相互交接工作。

Attack Discovery 把攻击交给 Endpoint Analysis，对涉及的主机做更细致的检查；Rule Coverage 则基于 Continuous Threat Hunt 记录的检测缺口开展工作。如果你关闭交接中的一端，另一端仍然继续运行，可用的上下文却会变少。本次发布中的响应操作，无论来自 Endpoint Analysis 还是 Continuous Threat Hunt，都通过 Elastic Defend 执行，Endpoint Analysis 调查主机同样需要它。

![AlertZero 的 Workers 如何交接：告警交给分诊，假阳性交给规则调优，攻击交给端点分析](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaZrlPQ2P2lmjYrFwjZiaZnJetp8Rp1XMCnDjKN4dsDJN7d0j8elJDA0JHQIMenNDHsSVDicPNtgagQ7qNdnCxHmnEnlGdJ8Ne48/640?wx_fmt=png&from=appmsg)

AlertZero 的 Workers 如何相互交接信息，以得出有证据支撑的结论。

## AlertZero 的自主级别：Manual、Assisted 和 Supervised

每个 Worker 都有一个自主设置，最多三个级别。在 **Manual** 级别下，Worker 提出的任何事项都要等你团队里有人批准。**Assisted** 仅适用于 Rule Tuning 和 Rule Coverage。在这一级别下，它们会不经询问就着手调查一条规则或一个覆盖缺口，不过它们提出的任何变更仍然需要批准。**Supervised** 走得最远：Worker 自行批准并执行自己的建议，事后由你审阅它的操作。

![Elastic Security 中 Endpoint Analysis Worker 的自主设置，已选中 Manual，Supervised 可用](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShniayhxRj6ZibLp47neibLibDeZJaOEPSdibGchIIsQfAhWViblN5Je6qKibkgicfgUwrmCkvKPbxcjkEBHOMyiaJmUZgd8iaQyzurbS5E8/640?wx_fmt=png&from=appmsg)

AlertZero Endpoint Analysis Worker 的自主级别。

无论处于哪个自主级别，每个 Worker 都能为它审阅的告警打标签并添加注释，也能在无需预先批准的情况下开启调查。其余能力取决于你设定的级别。

| **Worker** | **Manual** | **Assisted** |  |
| --- | --- | --- | --- |
| Alert Triage Worker | 对新告警进行分类，并建议关闭其中的假阳性。每项关闭建议都由你批准或拒绝。 | – | 关闭置信度评分达到或高于其最低阈值的假阳性（默认 85%）。 |
| Attack Discovery Worker | 为每起潜在攻击开启一次调查，并建议把该攻击交接给 Forensics Watch。每次交接都由你批准或拒绝。 | – | 为每起潜在攻击开启一次调查，并自行把该攻击交接给 Forensics Watch。 |
| Continuous Threat Hunt Worker | 针对每份威胁报告开展狩猎，为其开启一次调查，并针对发现的威胁提出响应操作。每项建议操作都由你批准或拒绝。 | – | – |
| Rule Tuning Worker | 找出每条符合条件的规则，但在分析该规则之前会等待你的批准。每项建议的调优变更都由你批准或拒绝。 | 自行诊断噪声规则并提出调优变更；任何修改或例外项仍需你的批准。 | – |
| Rule Coverage Worker | 审阅 Hunt Watch 发现的检测缺口，但在检查某个缺口之前会等待你的批准。每项建议的下一步同样由你批准或拒绝。 | 自行审阅检测缺口并提出变更；任何规则变更仍需你的批准 | – |
| Endpoint Analysis Worker | 把攻击时间线、入侵指标及其判断依据添加到调查中，并提出响应操作。每项建议的响应操作都由你批准或拒绝。 | – | 把攻击时间线、入侵指标及其判断依据添加到调查中，并执行这些响应操作。事后由你审阅结果。 |

**•** 已被确认的攻击内部所包含的告警会被标记为该攻击的一部分，保持开启状态，因此 Alert Triage 仍能接手它们。

**•** 无论处于哪个自主级别，Endpoint Analysis 在关闭调查之前都会先询问。

当你批准某项操作时，它以你的身份、你的权限运行，并记录为你的决定。如果你跳过批准，它则以该 Worker 的服务账户运行。

## 如何审阅并批准一项建议操作

分析师一天中的大量时间，都花在通向某个决定的工作上。例如，你为一条告警提取上下文，判断某条规则此前是否误触发过；或者你在数据中搜索某份新威胁报告所描述的内容。决定本身，比如是否隔离某台主机、是否修改某条规则、或者也许关闭一批告警，通常是比较快的部分。AlertZero 承担这项基础工作，并把它发现的一切附加到呈现给你的那个决定上。你环境中的哪些内容发生变更，仍由你决定；其中有多少可以交接出去，也由你选择。

每一项建议操作都会落在建议操作页面上，按 **Respond**、**Investigate** 与 **Configure** 分组。打开其中一项，你就进入了它的调查，Worker 在这里保存它的笔记，包括它收集的证据与它建议背后的理由，以及涉及的主机和用户。由于一次调查就是一段 Elastic Agent Builder 对话，你可以在做决定之前提出追问，例如，*那台主机还连接着什么？*或者，*这项建议的例外会停止匹配哪些内容？*

![AlertZero 建议操作页面，按 Respond、Investigate 与 Configure 分组，并打开了一个 Investigation 侧滑面板](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSg4COJ7d7xpsyX8fJicsTo14d59IPJ3TcMDrqoJ57aWdRcXrUkYPLHTbF5Rr8aicRg0eRuSRIEHp4pk26jFs5MSU6RN5fwzicy9yE/640?wx_fmt=png&from=appmsg)

AlertZero 主界面，含一个"Respond"建议操作的侧滑面板。

当你批准时，该操作会以你的身份、凭你的权限运行，并被记录为你的决定。如果你拒绝，该操作不会运行。

![AlertZero 中的](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSg0b7MWP00YMTCDAbyibTyjh5lic2VIiaEtM5FAXn6Au4WFfOViatIAnW9lyTRKmgibZkRJQXRLaoEjCOib9vvHyAaYz3u5N6Qo5PLZM/640?wx_fmt=png&from=appmsg)

隔离主机建议操作。

### 通过升级与他人协作处理案例

有些案例需要不止一个人。一次升级会把一个或多个相关调查带入一段共享对话。你可以把它指派给你团队中的人员，并保持其私有或将其公开。你们在那里共同处理该案例，过程中智能体随时可用来回答问题。

## 为 AlertZero 选择模型：Efficient、Balanced 与 Frontier 档位

没有任何单一模型适合每一个步骤，而且你今天依赖的那个模型也可能发生变化。某家提供商收紧其护栏或下线某个版本，甚至调整其定价，于是原本可用的某个步骤开始失败或成本上升。安全工作比大多数领域更容易遇到这种情况。当 Hugging Face 调查其 2026 年 7 月的入侵事件时，其团队最先求助的那些模型拒绝承担大部分取证工作，因为它们的护栏把逆向分析一个漏洞利用与发动一次攻击视为同一件事。该团队最终用一个开放权重模型完成了分析。

这就是 AlertZero 让你选择其 Workers 所用模型的原因。我们把 Worker 工作流中的每个 AI 步骤，依据该步骤所需的能力，归入三个模型档位之一。你在 **Feature Settings** 的 **AlertZero** 部分为每个档位挑选模型，Workers 便从这些模型中取用：

**•** **Efficient** 处理快速、频繁的调用，例如检查检测覆盖情况，这类工作一个小型、低成本的模型就能胜任。

**•** **Balanced** 涵盖准确性重要、且某一步骤需要多轮使用工具的工作，例如诊断一条噪声较大的规则，或分析一台主机**。**

**•** **Frontier** 用于单次通过的工作，其中一个输出承载的分量最重，例如生成攻击发现，因此你最强大的模型应当放在这里。

你可以为任何档位使用你选定的模型，包括开放权重模型，或由你自己托管的模型。如果每个档位都指向一个由你托管的模型，那么依据你的告警构建的提示词会发送给该模型，而不会发送给第三方服务。如果某个模型开始表现不佳，你可以为那个档位更换模型，而无需改变 Workers 运行方式的其他任何部分。

## AlertZero 为你的 SOC 团队带来什么改变

AlertZero 改变的是你团队的时间去向。新告警会持续到来，其中有些始终需要人来处理。Watches 专注于清空你的队列。每个决定背后的基础工作，包括为一条告警提取上下文、以及注意到某条规则反复误触发，都在后台完成。到达你团队手中的，是一份更短的决定清单，且每一项都附有支撑它的证据。你决定哪些 Workers 运行、每一个能自行完成多少工作，以及由哪些模型来完成这些工作；随着团队逐渐熟悉，这些你都可以更改。

这...