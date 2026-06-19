---
title: 专题解读 | Harness Engineering：AI 工程正在从“调模型”走向“造环境”
url: https://mp.weixin.qq.com/s/ui8sR9O7L5bA_0092BOSiA
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:06:34.691355
---

# 专题解读 | Harness Engineering：AI 工程正在从“调模型”走向“造环境”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6gtnxe1uggHcIEvHxxH09Ylsp9dyzHghVT377NB555bgwiaU6WX2aDo1Rkiar64eW6yOYkp9m9MMmAqZGwvE902yMd81mNM47wkR8Y51Ds7ZE/0?wx_fmt=jpeg)

# 专题解读 | Harness Engineering：AI 工程正在从“调模型”走向“造环境”

原创

刘海博
刘海博

北邮 GAMMA Lab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

过去几年，AI 工程的主线一直在变。

最早大家关心的是 **Prompt**：怎么把问题说清楚，怎么让模型按格式回答。后来开始关心 **RAG 和 Context**：模型不知道的东西，能不能从外部知识库里补进去。再后来是 **Agent**：模型不只回答问题，还能读文件、调用工具、跑命令、改代码、开 PR。

当 Agent 不再只是“说”，而是开始真正地“做”时，一个关键的工程问题浮出了水面：

***我们到底该怎样让 AI 可靠地做事？***

**Harness Engineering**这一概念，就是在这样的背景下被明确提出并受到关注的。

*注：Harness 原意指马具、安全吊带，在软件中常指测试套件（Test Harness）。在这里，它代表“约束并支撑 Agent 运行的外部环境”。*

比较早的清晰表述来自 HashiCorp 联合创始人 Mitchell Hashimoto。2026 年 2 月 5 日，他在个人博客中写到 *“Engineer the Harness”* 这一节，并把这种实践逐渐称为 harness engineering：

> “
>
> 每当 Agent 犯错时，不要只纠正这一次的结果，而是去改造它所在的环境，让它以后更难犯同类的错误。

这个改造可能是更新项目规则文件，也可能是写脚本、写测试、补充工具，或者补上 Agent 原本看不到的上下文。

几天后，OpenAI 于 2026 年 2 月 11 日发布了《Harness engineering: leveraging Codex in an agent-first world》。这篇文章把这个词放进了更大的工程语境里：在 Agent-first 的软件开发中，人类的主要工作不再只是亲手写代码，而是设计环境、指定意图、建立反馈回路，让类似 Codex 这样的 Agent 能够可靠地工作。

OpenAI 用一句话概括了这种新型的分工：**Humans steer. Agents execute.** （人类负责掌舵，Agent 负责执行。）

所以，Harness Engineering 不是一个从论文里凭空长出来的理论，而是从开发者真实使用 Agent 的痛苦中长出来的。

大家发现，Agent 的很多失败并不是因为“模型能力不够”，而是因为它不知道该怎样在这个具体项目、具体仓库、具体流程里正确地工作。

![图1：AI 工程的重心，正在从“优化回答”转向“治理行为”](https://mmbiz.qpic.cn/sz_mmbiz_png/6gtnxe1uggFBk5g9UicnibeRTm5jCq0TpPxqeN7IupGA5qZwreaiaZ9yqkXca1K0iaegw9QibFCiadquSEgiavjbUQ5PuRxBCiayCjsowt0DL1wH8EA/640?wx_fmt=png&from=appmsg)

图1：AI 工程的重心，正在从“优化回答”转向“治理行为”

## 01 为什么会出现 Harness Engineering？

一个人类工程师进入新项目，会慢慢掌握很多隐性规则。比如：

* 哪个接口已经不推荐使用了；
* 哪个测试虽然运行慢，但上线前必须跑通；
* 哪个模块比较脆弱，不能随便改动；
* 哪个设计文档才是最新的；
* 哪个产品约束属于必须保留的历史包袱。

这些东西不一定都写在代码里，但它们真实影响着每日的工程决策。

可是 Agent 并不具备这些常识。

除非这些知识被显式写进它能访问的文档、脚本、测试、linter、日志和工具里，否则它只能根据眼前有限的上下文去“盲猜”。

* 它可能读得懂一个函数，却不知道这个函数在整个系统中的边界。
* 它可能知道某个框架的通用标准，却不知道你们项目为什么特意避开了这种写法。
* 它可能能修好一个 bug，却不知道这个修法会不会破坏历史上的某处设计。

这就是 AI Agent 在真实工程里最常见的问题：**它有能力，但缺少环境。**

过去我们解决 AI 的问题，第一反应往往是改 Prompt。模型理解错了，就把指令写清楚一点；回答跑偏了，就加 few-shot；信息不够，就做 RAG；流程太复杂，就引入 Agent 框架。这些方法在局部很有效，但解决的都是点状问题。

到了 coding agent 或自动化 agent 阶段，失败原因变得更加系统化：

* Agent 不知道项目的真实约束；
* 不知道应该跑哪些测试去验证修改；
* 不知道某个 API 已经过时；
* 不知道 UI 行为应该怎么自动化验证；
* 不知道日志和指标（metrics）去哪里看；
* 不知道自己什么时候该停下来询问人类。

这时候如果还只靠 Prompt，就像让一个新手入职时只读一页注意事项，然后指望他去维护一个庞大而复杂的系统。

真正需要的是一整套工作环境：**文档、规则、脚本、测试、检查器、沙箱、可观测性、权限边界、review 机制，以及在失败后能把经验沉淀下来的流程。这个整体，才是 harness。**

![图2：Agent 的问题不只是“会不会”，而是“有没有合适的工作环境”。](https://mmbiz.qpic.cn/sz_mmbiz_png/6gtnxe1uggGdfZwAiaYGMIr7E6n7XtXuvOHNcjcdqt6p3o01yfgdEYBWvRHQcfFzu1FIgSAcohulQMA7t5KxWrzyUSM5QJvoeDhIDyg0iaSo4/640?wx_fmt=png&from=appmsg)

图2：Agent 的问题不只是“会不会”，而是“有没有合适的工作环境”。

## 02 Harness Engineering 到底是什么？

在 coding agent 的语境下，可以把 Harness Engineering 理解为：**围绕 AI Agent 构建一整套可读、可执行、可验证、可反馈的工作环境。** 让 Agent 不只是能完成一次任务，而是能在长期使用中少犯错、能自查、能修正，并且让经验得以在系统中沉淀。

这里的 harness，不是模型本身，而是模型周围的一切：

* 项目规则与仓库结构；
* 架构文档与专门给 Agent 看的 `AGENTS.md`；
* 测试、CI、linter 与静态检查工具；
* 自动化脚本与浏览器控制工具；
* 日志、Metrics、Trace 等可观测性基础设施；
* 权限边界与人工 Review 流程。

它的目标不是把 Prompt 写得更漂亮，而是把 Agent 的行动空间变得更清晰、更有约束、更容易自我验证。这也是它和过往概念最大的区别：

* **Prompt Engineering** 解决的是：*这一次怎么问。*
* **Context Engineering** 解决的是：*这一次给它什么信息。*
* **Agent Engineering** 解决的是：*任务怎么拆、工具怎么调。*
* **Harness Engineering** 关心的是：*这个 Agent 要在一个真实工程系统里持续工作，我们该怎样设计环境，才能让它的错误更少、错误更容易被发现、错误经验可以被沉淀？*

在 Martin Fowler 网站上，Birgitta Böckeler 对这个概念做过一个非常有用的拆分：一个好的 coding-agent harness，既需要 **Guides（引导/前馈控制）**，也需要 **Sensors（传感器/反馈控制）**。

* **Guides（前馈控制）**：在 Agent 动手之前引导它。比如规则、文档、架构说明、how-to 指南、初始化脚本。
* **Sensors（反馈控制）**：在 Agent 动手之后观察并捕捉结果。比如测试用例、linter、type checker、日志、浏览器状态、AI reviewer。

简单来说：

* **Guides 让 Agent 更容易一次做对。**
* **Sensors 让 Agent 做错之后有机会自我修正。**

这个框架之所以重要，是因为它把 AI 工程从纯粹的“相信模型”拉回到了“设计系统”的传统软件工程轨道上。

在真实工程里，很多失败是结构性的。如果 Agent 总是犯类似的错误，说明环境的 Harness 存在漏洞：

* Agent 总是用错命令 -> 说明命令没有被稳定、清晰地暴露。
* Agent 总是误解模块边界 -> 说明架构约束没有被机械化、工具化。
* Agent 总是忘记验证 UI -> 说明它缺少浏览器和截图的反馈回路。
* Agent 总是写出重复代码 -> 说明代码库里缺少自动化的结构和重复检查。

换句话说，失败不是结束，它在提醒你：**你的 Harness 哪里还缺一块板子。**

![图3：Harness 不是模型，而是模型周围的工程系统。](https://mmbiz.qpic.cn/mmbiz_png/6gtnxe1uggHUtJzXD6d2ajQAGUibsNMVEjBwI8LSHfdjs8Gp1icUgSSFiaWnbcp5kPJWyOtMv5dFyA81OSVsLpvr6rJ4hSWW9lMzibjjIG3k4Sg/640?wx_fmt=png&from=appmsg)

图3：Harness 不是模型，而是模型周围的工程系统。

## 03 它真正解决的是什么问题？

OpenAI 的 Codex 案例非常能说明这种思路。

据 OpenAI 介绍，他们曾用五个月时间做了一个内部 beta 产品，并设定了极端的约束——“人类不亲手写代码”： 所有的应用逻辑、测试、CI 配置、文档、可观测性和内部工具都由 Codex 生成；人类工程师主要通过 Prompt、Review 和反馈来驱动系统运行。

这个案例真正有价值的地方，不是“AI 写了一百万行代码”这个数字，而是它暴露了一个更深层的事实：**当 Agent 的吞吐量上来以后，人类的瓶颈会迅速从“写代码”变成“管理环境”。**

如果 Agent 一天只能写一个小函数，人类肉眼 Review 还能兜得住。但如果 Agent 能连续工作几个小时、开多个 PR、改动多个模块，传统的“人肉审查”很快就会被海量代码淹没。

此时，工程师必须把判断标准前移到系统中：

* 哪些规则必须由工具机械化强制执行？
* 哪些测试在合并前必须自动运行？
* 哪些架构边界是绝对不能突破的？
* 哪些日志和指标必须能被 Agent 自动读取？
* 哪些反馈可以由另一个“审查 Agent”先过一遍？

OpenAI 在这方面做了一个很典型的选择：他们没有把 `AGENTS.md` 写成一本冗长的巨型说明书，而是把它当成一个“目录”。真正的细节被放进了结构化的 `docs/` 目录中，包含架构设计、执行计划、产品规范、可靠性及安全等模块。这样 Agent 只需要先读一个精简的入口，再按任务去按需加载更深的信息。

许多团队以为自己是在“用 AI 写代码”，但实际上只是把一个不熟悉项目的新人反复扔进复杂的代码库里，然后怪他没有上下文。

Harness Engineering 的第一步，就是承认：**Agent 和新人一样，需要 onboarding。** 不同的是，Agent 的 onboarding 不能靠口头传授，而必须依靠能够被机器读取、执行和验证的结构化环境。

具体来说，它主要解决了三个问题：

### 3.1 解决 Agent 的“上下文失明”

所谓上下文失明，是指 Agent 缺少项目级的隐性知识。它不知道代码背后的历史演进，不知道团队的设计偏好。Harness 的作用，就是把这些隐性约束变成显性的、可被机器消费的材料（如文档、专门的 linter、验证脚本等）。

### 3.2 解决 Agent 的“无法自证”

AI 生成一个答案很容易，但证明这个答案是正确的却很难。如果 coding agent 改完代码后不能自己运行测试、看日志、检查指标，那么验证的压力就会全部压在人类身上。**不能验证的自动化，本质上只是在更快地制造不确定性。**

因此，成熟的 Harness 必须提供足够的反馈信号（UI 自动化、日志、APM 监控等），让 Agent 能在沙箱中复现问题、观察状态并自我验证。

### 3.3 解决 Agent 的“重复犯错”

人类团队最怕同类错误不断出现，Agent 也是。如果每次都靠人工在 PR 里提醒“这里不能这么写”，说明经验没有沉淀下来。 Harness Engineering 的闭环思路是：

* 一次犯错，口头提醒（或临时改 prompt）；
* 两次犯错，将其写进项目规则文档；
* 三次犯错，就必须将其固化为测试、自定义 linter 或 CI 自动检查。

每一次失败都在逼问同一个问题：这个错误是偶然的，还是我们的环境中缺了一道硬性护栏？

![图4：Harness Engineering 的目标：让错误变少、变可见、可沉淀。](https://mmbiz.qpic.cn/mmbiz_png/6gtnxe1uggGlgpSkeLVumVwOBdr1NLbuBVj6Z37bWLy7e8vmygsFHJiaibC92uYbYZHMmjNvzFQAfNvBibnicrgbF8lwg5ty4LXaraZZ72IQsgQ/640?wx_fmt=png&from=appmsg)

图4：Harness Engineering 的目标：让错误变少、变可见、可沉淀。

## 04 它不是银弹，但可能是 AI 工程落地的关键

我们不能把 Harness Engineering 说得太满。它更擅长解决那些**可结构化、可检测、可反馈**的工程问题，比如：

* 运行命令错误；
* 遗漏边界测试；
* 架构约束被破坏；
* 文档与实际代码过期脱节；
* 重复造轮子。

但诸如深度的需求理解、复杂的业务取舍、跨领域的架构判断，依然无法完全交给 Harness 自动处理。你可以让 Agent 自动写测试，但测试是否覆盖了真正的业务意图，依然需要人类来把关。

所以，**Harness Engineering 的终极目标不是完全无人化，而是减少低价值的重复监督。**

它要把工程师的注意力：

* 从：“盯着它有没有敲错命令、有没有跑通测试”
* 转向：“判断它做的事情在业务上是否真的值得”。

这也解释了为什么这个概念在当下变得如此重要。因为 Agent 的执行力已经到了一个临界点：**它已经强大到可以承担海量的日常执行工作，但同时也危险到必须被环境牢牢约束。模型越强，我们越不能只靠“相信它”。**

没有 Harness 的强模型，只是在以更快的速度产生更多不可控的结果；有了 Harness 的模型，其能力才能真正转化为工业级的稳定生产力。这其实是一种工程常识的回归。

过去一段时间，AI 行业太容易把一切问题归结为模型本身：模型不行就换大模型，回答不准就调 Prompt。而 Harness Engineering 提醒我们：**可靠性问题很少是靠一句更聪明的提示词彻底解决的，它终究要靠制度、工具、反馈、测试边界和可观测性来兜底。**

未来，工程师的价值正在加速上移：

* 从写下每一行代码，转向设计能让 Agent 高效协作的环境；
* 从被动的反复纠错，转向主动让系统产生免疫力、不再重复犯错；
* 从依赖个人脑海中的经验，转向将工程规范机械化、显式化地沉淀在系统里。

未来的工程竞争，可能不再只是看谁的模型参数更大、谁的 Prompt 技巧更炫，而是看谁能更快、更深地将组织知识和验证机制，沉淀进 Agent 可以安全运行的环境中。

最后，用一句话总结 Harness Engineering 的本质：**当一个带有不确定性、但极具能力的执行者进入你的生产系统时，我们该做的不是反复祈祷它“更聪明一点”，而是为它造好一套环境，让它更容易做对、更容易发现自己做错，并让每一次失败都成为下一次变得更好的养料。**

---

### 参考资料

* Mitchell Hashimoto, *My AI Adoption Journey*, 2026-02-05
* OpenAI, *Harness engineering: leveraging Codex in an agent-first world*, 2026-02-11
* Birgitta Böckeler, *Harness engineering for coding agent users*, Martin Fowler, 2026-04-02

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AYxz3cIHvyoiayibng0FojESWtukKaO5zH1D94qCSeOjkzZpNfKoYddl1n8FJ7j610Wa5W4BSTtwBa4Y0QsC8d7Q/0?wx_fmt=png)

北邮 GAMMA Lab

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AYxz3cIHvyoiayibng0FojESWtukKaO5zH1D94qCSeOjkzZpNfKoYddl1n8FJ7j610Wa5W4BSTtwBa4Y0QsC8d7Q/0?wx_fmt=png)

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