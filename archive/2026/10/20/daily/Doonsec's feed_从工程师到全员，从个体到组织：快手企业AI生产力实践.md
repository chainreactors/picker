---
title: 从工程师到全员，从个体到组织：快手企业AI生产力实践
url: https://mp.weixin.qq.com/s/Mhh3TtQ13SzBDiymrrjUng
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:48:45.200840
---

# 从工程师到全员，从个体到组织：快手企业AI生产力实践

# 从工程师到全员，从个体到组织：快手企业AI生产力实践

原创

快手技术
快手技术

快手技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)![]()
在 QECon 全球软件质量&效能大会上，快手科技副总裁、快手企业生产力负责人王诩在主论坛带来了《快手企业 AI 生产力：从研发提效到组织跃迁》主题分享，回顾快手过去两年用 AI 重构研发效能、推进"全民 AI"，并进一步走向企业 AI 生产力（iWork）的实践路径。

从研发流程中的 AI 工具，到面向全员的通用 Agent，再到团队级知识库、多 Agent 协作链和企业语义框架，快手的核心判断是：AI 提效不能只停留在个体层面，真正的生产力跃迁来自组织协同。

王诩表示："研发效能从来不是个体的事情，是各个协作部门和组织一起发力的结果。因为系统有很多模块，它一定会被最慢的那个模块限制。"这也是快手成立企业 AI 生产力（iWork）的初衷。

【演讲视频回顾】

以下内容整理自现场演讲，在保留原意的基础上略有删减。

研发效能从来不是一个孤立的话题：它和产品、设计、质量、行政、HR 等上下游群体紧密关联。2025 年初，我们把各条线的 CTO 聚在一起形成"CTO 效能"机制，以两周一次的频次密集探讨 AI 如何赋能研发效能，并形成了"三位一体"的策略：先有人持续做实践，再把实践中沉淀出来的先进能力固化，最后从组织自上而下推动转型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1V7xScHdmAjq1u6Zjamlh5ib82MXjLL2lA6lvYvwo3nteicQNSXzNvMRMn3jOoAqOKtMNSuImNERolRdEeC8k3SZk18Gb35vMmkw/640?wx_fmt=png&from=appmsg)![]()

快手科技副总裁、快手企业生产力负责人王诩

这条路径已经走完了三个阶段，我们刚刚开启第四阶段的探索。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1X8AM3oRlmCAic8ThicPOibl5jOC2ICTt46sLaZyC4jglJwiba6CNzEDaIN3H3E7F6TwDnjCHq8Doy8z3rJJgickGgzLl42odBF0amo/640?wx_fmt=png&from=appmsg)

## 一、阶段1：AI x 工程师——把 AI 嵌进研发流程

2025 年全年到 2026 年 Q1，快手整体遵从经典的研发链路——从产品需求提出、拆解、设计、架构、编码、测试到运维——尝试在每个环节用 AI 工具做提升。

在实验中，团队发现个体差异巨大，于是我们总结出L1、L2、L3的分类：

* L1：把代码片段贴给 AI，让它改完再拿回来嵌入代码库——经典的"片段级"用法；
* L2：以任务级粒度交给 AI，比如定义一张数据库表、给出完整语句——任务级；
* L3：把 PRD 或 Spec 直接丢给 AI，引导它完成自主的全链路开发（SDD 方式）。2025 年下半年到 2026 年 Q1 的时候，我们已经看到很多内部同学已经这样做了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1WlGjBic6ibkiaeK6lcRx3jn5F7JJtlicXhicKof1YzY51nleS9yUIJWaibn2ia7BsVq5EOglIF7rPO4Y95n8tdwJVcXeibZXUhokVbrmA/640?wx_fmt=png&from=appmsg)

我们没有把 L3 当作群体要求（当时基模和 Harness 能力还不够好）。于是，我们以 L2 覆盖度作为度量指标，目标 2026 年底达到 80%。工具侧则用 Coding IDE、需求与 CR 管理、重度编码助手等产品串联各环节，把 AI 能力嵌进原有流程。

## 二、阶段2：AI x 所有员工——让 AI 从工程师走向所有员工

2026 年 Q2，当红的通用智能体产品"小龙虾"让团队意识到：门槛更低的通用智能体，才是更大的机会。快手把原来的 Coding Agent（CodeFlicker）转型封装成通用智能体（MyFlicker），插入大量领域知识和 Skill，服务的不再只是技术人员——HR 用它做招聘和人岗匹配，行政同学用它把全量服务透明化（订餐、班车、理发），普通员工也能直接享受 AI 化的服务。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XpS78yl70adjSEsRYW20b21jnR085tpsVpvmFXZGLoeEj0WeiahMLuOic0P4FKPCGP5iaBhibGWwibibfoe5oWxvDibku7BBQflNFef0/640?wx_fmt=png&from=appmsg)

面对“全民 AI”的浪潮，我们审慎地做了很多测算，这个阶段最关键的机制创新是我们提出了一套 Token 积分体系。公司给员工发放积分，员工可在通用智能体上选择不同模型消费（每个模型有不同积分倍率），自行安排用度。这套体系有两个目标：一是让大家优先选择品质高的产品，二是规避重复建设——接入积分体系后，你的 AI 产品有没有人真正在用、消耗多少 Token，一目了然，相当于"用脚投票"。

数据验证了方向：MyFlicker 从去年年底的技术群体专属工具，到 Q2 “全民 AI”阶段爆发式增长。在推进全面 AI 的过程中，我们通过多场大型活动，帮助快手员工提升 AI 认知与实践技能。以下分享三个“全民 AI”的典型案例。这些活动分别对应了三类目标：降低 AI 使用门槛、提升全员 AI 技巧、验证非技术人群构建工具的可能性。

* AI 蹭饭研判官——从工具到伙伴，能聊天、能干活

“全民 AI”最热闹的一次实践，是快手内部做的一场“免费午餐”活动。规则很简单：每天提供一批免费午餐名额，但你得先说服 Agent 请你吃饭。对话轮次越短，拿到午餐的概率越高；每天取前一两百名，持续一周。在相对轻量的投入下，这场活动吸引了五六千名员工参与。

对快手来说，这场活动既验证了员工参与 AI 的热情，也提前暴露了 AI 产品走向真实场景时绕不开的问题：权限边界、对抗式提示、防 hack 机制，都必须成为产品设计的一部分。

* 司庆 AI 贪吃蛇大赛——用好AI需要提升个人认知和技巧，从各业务线 PK → 全员PK → 新人必会

“全民 AI”的另一个高光时刻，是快手司庆期间的一场“AI 贪吃蛇大赛”。规则并不复杂：官方提供贪吃蛇 PK 平台和公共接口，各业务线组队，用 Vibe Coding 构建自己的贪吃蛇程序，先在内部研究策略、相互对抗，再把最强版本带到决赛现场公开 PK。

结果很有意思，前三名里有两个来自非技术团队，财务团队拿到了第二名。AI 把编码门槛降下来之后，决定胜负的不再只是“会不会写代码”，还有策略设计、问题理解和快速迭代能力。

因为参与度很高，这场比赛后来被转化为校招培养项目。新同学入职后，也会在使用 AI 工具的过程中参与类似比赛。更让团队惊喜的是，很多校招生做出的贪吃蛇，已经能够轻松打败公司里各领域专家构建的版本。

这背后传递出的信号很明确：在 AI 工具足够成熟的场景里，经验优势会被重新定义。谁更会使用 AI、更能快速试错和迭代，谁就可能做出更好的结果。

* PDE 集结令：全员用 AI 完成日常工作

我们还做过一次更接近“能力转型”的实验：让非技术同学也成为 PDE（Product Design Engineer）。随着 AI 工具的发展，国内外不少公司都开始关注这类岗位，快手内部也在讨论：这种能力结构，是否会成为未来组织里的新常态？

于是，我们设计了一场活动：以一位日常工作繁忙的运营同学为原型，邀请大家为他构建 AI 工具，让他的工作变得更简单。活动面向非技术人群开放，既是一次 AI 工具使用训练，也是一场真实业务场景下的工具共创。最终，内部提交了 4000 多个作品。某种程度上，最先被“提效”的不是运营同学，而是评审团队——因为光是判卷就已经成了一项巨大工程。

这场实验说明，AI 带来的不只是效率提升，也在重新划分组织里的能力边界：过去只有工程师能做的工具，现在更多业务同学也可以参与构建；而真正优秀的作品，还有机会沉淀为公司内部可推广的 AI 工具。

三、从个体提效到组织转型：AI 生产力的认知升级

###

但真正的转折点，并不是大家都开始用 AI，而是快手意识到：个体提效并不会自动带来组织提效。“全民 AI”的热潮之后，我们在 H1 做了一次冷静复盘。好消息是，AI 的使用已经被快速拉起来，认知初始化基本完成，内部也沉淀了大量 Skill。

但问题也随之暴露。

1、Skill 良莠不齐，存在"Token 黑洞"：Skill 数量不是关键指标，有同学写的一个 Skill 能消耗掉几千积分。AI 应用一旦规模化，成本、效率和治理都会变成真实问题。

2、个体的提效并没有带来端到端的效率提升：AI 能力在变强，但 Token 消耗大、成本对不齐；更核心的是，个体提效受限于原有工作流——PRD 以前写好几天、现在半天搞定，如果研发、设计、测试等协作链条没有同步变化，整体交付速度依然不会明显提升。

3、个体差异巨大：高手一两句话就能产出很好的东西，很多同学还在反复调教和试错阶段。如何把优秀实践变成公共知识和公共能力，是当时最棘手的问题。对组织来说，真正要解决的问题变成了：如何把高手经验沉淀为团队能力，把个体技巧变成公共资产。

这也是快手后来从“全民 AI”走向“组织级 AI 生产力”的关键转折点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1XUW6FrEQxCcTslDqdENauvLUNtmgTCVKVw6wbliciciaSHibl06LWprS7lPzZFvHUicdb5xIibvRS4HjhFKftm8QlJeickEzzuaO5ibyY/640?wx_fmt=png&from=appmsg)

在年中复盘时，我们把问题进一步抽象成了一张“个体提效 × 组织提效”的坐标图。核心判断是如果组织层面不发生变化，个体提效的天花板依然很低。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1WhGeiakx1vIGJt8OHUTTgdHyswQbQbiao7hPKppjOIrxXQYKCibvxoTFzWIQgFUiaIibzKM3zQ7BXDibqgXAichvrcDZ822tKa6WbSvg/640?wx_fmt=png&from=appmsg)

只有组织设计、个体能力跟不上，机制落不了地；只有一批“超级个体”，彼此之间没有连接和协作，也只是一个个效率孤岛。真正有价值的路径，是让个体能力和组织能力同步提升。

快手由此把 AI 生产力的演进拆成几步：先完成冷启动，让员工愿意用、开始用；再把少数高手的使用经验沉淀为团队基线；进一步，把团队里的公共知识、业务资产和协作规则沉淀下来，让 Agent 可以快速消费；最终，让 Agent 在具备优秀实践和完整上下文后，成为独立工作单元，进入人与 Agent、Agent 与 Agent 的协作链。

这意味着，AI 的下一阶段不再只是“每个人更会用”，而是组织能否形成可沉淀、可复用、可协作的 AI 生产力。

四、阶段3：AI x 团队——让 Agent 进入团队协作链

###

Q3，我们把 AI 提效的重心从“个体”推进到“团队”。核心做法有两件事：

一是知识库建设。与业务共建并沉淀过往项目、代码和核心工作流，让 Agent 能直接消费团队上下文，放进公共基建平台。团队新成员一进来就有起点，过往项目、代码对 AI 透明可见。

二是把公共知识和 Skill 封装成能独立工作的 Agent，并让多个 Agent 形成协作链。基于开源项目构建了一个超级 Agent 做全局协调：产品经理、设计师、全栈开发等子 Agent 注册进 pipeline，需求输入后 7×24 小时日不落迭代；同时设了安全闸门，遇到质量、权限、幻觉问题会唤醒人来介入。也正是在这一阶段，Agent 从“个人助手”进一步走向了“团队工作单元”。

从 4 月至今，累计完成 2000 多个任务，AI 一次任务率（一次完成且通过独立验收）超过 60%，80% 的任务两次内完成（一次 AI + 一次人工校准），这个指标还在持续改进。

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1XYHz81fajePxIGkbBKoLDaSzEcVfrrgGAUyCJY6IBPnEo0naibJEmOH0zjQJIYGotGXodhdeIXR6qVicZyfU9a3MMvysFCWBbuE/640?wx_fmt=png&from=appmsg)

在非技术场景中，内容运营团队已经基于这套体系搭建了运营专属工作台。快手把运营同学的高频工作流 Skill 和相关知识库集成到 Flicker 背后，让他们可以直接完成热点拆解、内容分析等任务。目前，这一工作台已经沉淀为标准产品，并在内容运营线推广使用。这也说明，AI 的价值正在从“个人助手”走向“团队专属生产力工具”。

五、阶段4：AI x 组织——从分散实践走向企业 AI 生产力（iWork）

###

9 月，我们成立了企业 AI 生产力（iWork）组织，开始把分散在各团队里的 AI 实践，推进为公司级能力建设。

在前一阶段的探索中，越来越多优秀实践不断涌现，但也暴露出新的挑战：这些经验如何变成公司标准？如果每个团队都基于自己的业务出口和数据各自构建 AI 应用，短期看能快速解决问题，长期却容易造成重复建设、上下文割裂和安全风险。

因此，快手将企业内部通信平台、在线文档协同、通用 Agent 以及内部信息系统能力整合在一起。其核心思路有两个：

* 一个强大的通用 Agent：具备更强推理能力，同时做到安全、受控、可监测，并持续提升员工个体效率；

* 统一的企业语义框架：把文档、数据、代码、流程状态、会议记录等分散信息组织成可被 Agent 理解和调用的上下文。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1VicR39aRt0kuovkwem2K1ZfM2AUx6YYlgRVIFrpMEcgUOaRqFCFicX9AZNwkpUqFRNGnZcJ9b7wA0ibK9vcAERfqzbLeibLI3MerA/640?wx_fmt=png&from=appmsg)

这样一来，Agent 不再只是在单点系统里完成任务，而是能够看见更完整的企业上下文；底层信息系统也会逐步开放可调用接口，让 AI 真正进入业务流程。基于这套能力，快手将继续以 FDE（Forward Deployed Engineer）的方式向业务赋能，内容运营、内容理解、安全、直播等场景都会是下一阶段重点探索方向。

这背后的判断是：研发效能从来不是个体问题，而是组织协同问题。一个系统的效率，最终会被最慢的模块限制。企业 AI 生产力（iWork）要解决的，正是如何让 AI 从个人工具，变成组织级生产系统。

如果希望进一步了解快手企业 AI 生产力（iWork）的技术实践，欢迎关注 10 月 31 日快手技术沙龙第 6 期。届时，我们将带来更完整的架构拆解与案例分享！

【欢迎报名】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1UxuxZYAYFcaP3cxJ9W2M1Dv63I7fdCsAuGuxVFGIbSA10lyeBfKj5icWRjYorJeevf7WRc0wgdLM3EiaT7EPY63U6ITobQDAic1w/640?wx_fmt=png)

👇 点击【阅读原文】，获取演讲 PPT！

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZxDY5TMPs0GnTFDtpq8oAf91ZQDzvLt6LCp56JQCbFT2cT8uZquFdeJOKbmM4fucIPqtAPvMT0X4DpfpuZibic3Q/0?wx_fmt=png)

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