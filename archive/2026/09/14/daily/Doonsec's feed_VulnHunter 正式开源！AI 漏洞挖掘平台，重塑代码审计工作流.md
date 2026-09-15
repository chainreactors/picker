---
title: VulnHunter 正式开源！AI 漏洞挖掘平台，重塑代码审计工作流
url: https://mp.weixin.qq.com/s/oDP5XJ4KXyqjiOMM12XV4w
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T06:56:33.429090
---

# VulnHunter 正式开源！AI 漏洞挖掘平台，重塑代码审计工作流

# VulnHunter 正式开源！AI 漏洞挖掘平台，重塑代码审计工作流

安全极客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于云起无垠
，作者AI基础设施构建者

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM7ToGXVRWUqTJ3KevuSY3Baib9NpY6E9yVSsFPzjpWSKpw/0)

**云起无垠**
.

云起无垠致力于打造数字员工时代的 AI 基础设施，让每一家企业都能安全、可控、可持续地释放 AI 数字生产力。

![](https://mmbiz.qpic.cn/mmbiz_gif/4vD467VsKgIyZ1VBWSEZ5D9CyVs2zCHdLWiaMbScsTP8jMicqnXH6icLycxZot7Q1CTPogdBQ0CduHPiaR62fe4I2g/640?wx_fmt=gif)

AI 正在以前所未有的速度改变软件开发范式。过去，一个需求从提出到形成代码，可能需要几天甚至几周；今天，在 Claude Code、Cursor、Codex 等 AI Coding 工具的帮助下，代码正在以过去数倍甚至数十倍的速度被生产出来。

软件开发的瓶颈正在被迅速打破，但另一个问题也越来越突出：当代码生产速度越来越快，我们真的有能力以同样的速度理解这些代码、发现其中的安全问题吗？

现实恰恰相反。

代码生成进入 AI 时代之后，安全审计仍然大量依赖规则扫描、人工分析和专家经验。研发正在加速，安全却没有同步加速。于是，一个新的矛盾开始出现：AI 让写代码越来越便宜，但看懂代码、发现漏洞、判断风险依然昂贵。

这也是我们开发 VulnHunter 的原因。

今天，我们正式将 VulnHunter 社区版开源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/39bwlg7QlUMg2TjHX1WzlQV8UwaOlEQQG78tpSCkssZ8ppqS0VrUmMYNdS5bAbDxFCtic0J8r1yVJibNUqM2uYkCYDUqtWVAhDpTGboCJLibCo/640?wx_fmt=png&from=appmsg)

GitHub：

https://github.com/Clouditera/VulnHunter

欢迎：

* Star 项目，Fork 并部署体验；
* 提交 Issue，告诉我们真实场景中的问题；
* 贡献 Pull Request，与我们一起完善 VulnHunter；
* 也欢迎把它真正放进你的代码安全工作流里。

除了现有的本地化部署和在线 SaaS 使用方式之外，我们希望通过开源，让更多安全研究人员、企业安全团队和开发者真正体验：如果把大模型的代码理解和推理能力，与安全专家的审计方法结合起来，代码安全工作流究竟可以发生什么变化？

**1**

**安全审计正在成为新瓶颈**

过去的软件研发流程里，代码本身是稀缺产能。今天，情况正在发生逆转。越来越多代码开始由 AI 辅助甚至直接生成，研发效率显著提升。但代码变多，并不意味着漏洞会自动变少。相反，当软件迭代速度不断加快后，安全团队首先面对的是一个非常现实的问题：代码越来越多，安全人员却没有同步增加。

一个中型代码仓库，如果依赖安全工程师进行完整人工审计，往往需要一周甚至更长时间。但现在，一支研发团队可能几天之内就完成一次较大规模的代码迭代。于是，研发与安全之间天然出现了时间差：当安全团队刚刚看完上一版代码，下一版可能已经上线了。

为了提升审计效率，越来越多企业使用 SAST 等自动化扫描工具进行代码审计。但传统工具解决的更多是扫描得更快，并不意味着真正看懂代码。很多漏洞并不存在于某一行代码里，而是来自多个函数之间的调用关系、跨文件的数据流转、特定业务逻辑下的权限缺陷，甚至多个正常功能组合后形成的攻击路径。只有结合完整上下文，才能判断一个风险是否真正成立。

因此，传统 SAST 虽然可以快速发现大量可疑代码，但安全工程师仍需要从几百甚至几千条告警中，判断哪些才是真正值得处理的问题。扫描自动化了，判断这件事却依然高度依赖人工。

与此同时，扫描器、IDE、漏洞管理平台、文档和报告系统往往彼此割裂。发现问题是一套系统，分析问题是一套系统，确认漏洞又是一套系统，最后还要重新整理成报告。安全工程师大量时间消耗在工具切换和信息搬运上，而不是漏洞本身。

归根结底，传统代码安全体系解决的是如何把既有规则执行得更快。而进入大模型时代以后，我们更希望解决的是：能不能让机器真正理解代码，并参与安全分析与判断？

这正是 VulnHunter 想探索的问题。

**2**

**AI 重构代码审计流程**

VulnHunter开源社区版 是一个自托管的 AI 漏洞挖掘工作台，将目标画像、AI 漏洞发现、对话chat、漏洞审核、任务管理与报告交付整合进统一平台。我们并不希望只是给传统扫描器增加一个大模型按钮，而是希望重新组织整个代码审计过程。

过去典型的安全审计流程往往是：扫描 → 告警 → 人工筛选 → 查看源码 → 分析上下文 → 写报告。整个流程高度线性，大量环节仍依赖人工完成。

VulnHunter 尝试引入另一种工作方式：让 Agent 承担信息收集、代码理解与初步分析，让安全专家把精力集中在真正需要判断的地方。

**从代码片段走向项目理解**

真正的代码审计，很少只是分析某一个函数。首先要理解项目整体结构：这是什么项目、核心模块在哪里、代码之间如何关联、哪些位置更可能形成攻击面。

VulnHunter 基于自研的 Agent 编排框架，让多个智能体协同完成目标画像、代码语义分析和漏洞定位。AI 不再只是回答这段代码有没有问题，而是围绕一个完整项目持续分析代码关系、业务逻辑与潜在攻击面。这也是 AI Agent 相比传统规则扫描工具最重要的变化之一。

**从静态告警走向持续调查**

传统扫描工具给出的通常是一条静态结果：某个文件、某行代码、某条规则被命中。但真正的安全分析还需要继续回答：为什么这里存在风险？相关调用链在哪里？漏洞是否真实成立？是否存在类似问题？沿着这条线索还能发现什么？

因此，VulnHunter 内置 Chat AI 助手，并集成 16 项以上 MCP 工具。安全人员可以直接通过自然语言查询漏洞、分析结果、管理任务、切换模型和生成报告。

过去需要在多个工具之间不断切换，现在可以围绕同一次安全调查持续推进。AI 不再只是生成扫描结果，而是开始参与整个漏洞分析与审计过程。

**3**

**打通审计全流程**

在实际企业环境中，安全工具只有发现能力是不够的。因为发现漏洞之后，还有大量工作：谁来审核？哪些结果确认有效？哪些需要进一步分析？现在处理到哪一步？最终怎么形成报告？

因此，VulnHunter 并没有把产品停留在 AI 扫描阶段，而是把一次完整的审计工作流放进同一个平台。

**AI 漏洞发现**

通过 Agent 协作完成目标画像、语义分析和漏洞定位，让 AI 承担大量前置分析工作。

![](https://mmbiz.qpic.cn/mmbiz_png/39bwlg7QlUPcwuibILAcKDdnnLiauzJLlARIJhhbCiaj2QA6sb2GTCAzFW3BYyxY8gsgLBx0cxgwJEM2R4aXfZIuu9hh96RyJsSPQibEvmhXAZY/640?wx_fmt=png&from=appmsg)

**对话式安全任务执行**

利用 Chat AI 和 MCP 工具围绕扫描结果继续分析、查询与操作，而不是停留在一张静态告警列表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/39bwlg7QlUNV7HmJS3fIWboM4Z43yQRTu2blQojiafD4McAriasKAibp8G77icCrb5CUIAgGDbpCkenJs41po3mjOmvVZibAaF2VSYPfhbjzycLY/640?wx_fmt=png&from=appmsg)

**漏洞审核工作流**

支持逐条审核和批量审核，并通过状态流转管理漏洞确认过程。当一次任务产生大量安全结果时，团队可以真正围绕这些结果展开协作。

![](https://mmbiz.qpic.cn/mmbiz_png/39bwlg7QlUPRq822QVFQicsWtICTdXibucGDOeYqChG87yj7UMGql8jPFLeln6428VfsOIGm2icFdX7iacroe3iaT21GnKwFTxfopq3e63ajSyHY/640?wx_fmt=png&from=appmsg)

**结构化审计报告**

系统可以生成结构化 Markdown 审计报告，帮助安全团队把分析结果快速沉淀为可以交付和存档的材料。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/39bwlg7QlUOiaBcia9ibBWzd3FpQcP5QlibdJJFG9atJhPaXIYiaTiby2b70ws7lkJY9raPER6MBB4H6yPugbIwCOtUMIPLibBnia9icubALRkB7yu4o/640?wx_fmt=png&from=appmsg)

**任务全生命周期管理**

任务可以创建、暂停、取消、恢复和重新运行。大型代码扫描不再是一个启动以后无法管理的黑盒任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/39bwlg7QlUMTgCgibe4I0rj4MC1pDqod6MtyxxHDXpPRC9WpOJ2tCj3y7hot627hOY0JLKkbiaQd9U3K5icdxy8rkDHHQibKwEia2nc2XrtwYibns/640?wx_fmt=png&from=appmsg)

**实时仪表盘**

严重度分布、任务状态、审核进度等信息可以统一查看。安全负责人不仅能看到“发现了多少漏洞”，也能看到整个审计工作的推进状态。

![](https://mmbiz.qpic.cn/mmbiz_png/39bwlg7QlUP1tRWphthRqBD2cCxp8zSBibIdn5fDRjbnEHMMAJE0q2T5e8UA2hYw5Vraia9pGuDZaVibMNH2517ia0zeooIbEickSiaDcbiaicbyRIU/640?wx_fmt=png&from=appmsg)

当这些能力被放到一起之后，VulnHunter 才真正从一个漏洞发现工具，变成一个围绕 AI 组织代码安全工作的工作台。

**4**

**面向多类人群适用**

VulnHunter 社区版此次开放的核心能力均可免费使用，无需授权激活。我们希望它首先成为一个真正能够被安全从业者安装、运行和研究的项目。

**（1）漏洞研究人员**

可以让 AI 帮助完成大量前期代码理解与线索发现，把更多时间投入真正有价值的深度分析。

**（2）企业安全团队**

可以在内部环境部署 AI 代码安全能力，并把漏洞发现、审核和报告逐步纳入统一工作流。

**（3）DevSecOps 与 SecDevOps 团队**

VulnHunter 的容器化形态可以作为现有 CI/CD 与代码安全体系进一步智能化的基础组件。

**（4）AI Agent 开发者**

VulnHunter 本身也是一个完整的多智能体、MCP 与安全场景结合的工程案例。

**（5）高校与科研机构**

完整开源的代码与工程实现，也可以用于 AI Security、软件安全和 Agent 方向的科研与教学。

除了开源社区版之外，VulnHunter 同时提供本地化部署与线上环境试用。

欢迎进行线上环境产品试用，扫描如下二维码领取试用账号。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/39bwlg7QlUMbyyazicTeymwohBMkyAPxoxeTToAYYlvbLJic6VdR8yaM5z4kZSMPassmmZGNGdpClHfQrha2FNkJEjiaibO1e2NltjcYON6xZpI/640?wx_fmt=jpeg)

扫码领取试用账号

-End-

![图片](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8R7Rm0KL55HCcIiasO8JJ7IibXzYxx3losWVb2eddxdClACzWxWtQLwl0wkAl1ZLibcESVWvx5dCeibtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&retryload=1&tp=webp#imgIndex=2)

*![图片](https://mmbiz.qpic.cn/mmbiz_gif/D9wGKNiaQYpx7bvaHqVZibq0ogu5pckjQMepnZgmhgM01uFQsoFz5QDDE0iapRkuUumSGfk8Dz7mjnbvibwPk7jISg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)*

![图片](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8QRqLMRicZIN6VJg0ue41W1HVSmDpDqkj86j5SNicNE3X5KkPgcdv1ZmxM7FXrFUdkBes8dpos7d27w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&retryload=1&tp=webp#imgIndex=4)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8SDzMyjUl8Lr0J0V4feAVeZ5eMLYibJKzJyVxRuoHpXEDLpGkGm6hQcBm7OyEu3EiclN8sNdPvWIWiaw/0?wx_fmt=png)

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