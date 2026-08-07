---
title: 快手AI研发范式升级新路径：从研发提效到组织跃迁
url: https://mp.weixin.qq.com/s/VJty9To_Bt9N18jMnDK_7A
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:23:13.666515
---

# 快手AI研发范式升级新路径：从研发提效到组织跃迁

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1gVUsotpT1UDibl6GCicYpMwf3yP9we8aDicAgsoRXtqEEsicYsEKu544mCtmsnIKbUC3JJdtv6qHTWaMaXovbgLlo9MYYatVCVSibopibwGRdugI/0?wx_fmt=jpeg)

# 快手AI研发范式升级新路径：从研发提效到组织跃迁

快手技术
快手技术

快手技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

本文是对快手在2026年H1，从研发效能到AI生产力体系过程的完整总结，有宏观的体系、方法、思考过程，也有微观的实践、案例。2026年8月，我们正式面向业界分享此文，希望快手的实践过程被更多业界同行看见和学习，促进交流和行业发展。同时，2026年H2，我们也会更深入推行“AI生产力”体系，希望为快手带来更大范围的生产力变革。

**01、回顾：三年三步，我们找到了用AI为个人提效 → 团队提效的路**

2026年2月，我们发表了[《快手：万人组织AI研发范式跃迁之路》](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247499334&idx=1&sn=1aa22f3ec717ecd8eabfb75683623af4&scene=21#wechat_redirect)，分享了2023年-2025年我们走过的路，也是业界首次提出了AI提效的陷阱：“用 AI 开发工具 ≠ 个人提效 ≠ 组织提效”。先快速回顾一下快手的实践历程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1XdbQdlWBBnqn3n7QaeRnLMMH7Dr0X93uGvUDhoHq8qFOgosNyFJNawdM7XExUzxuNY3pHCypEbHto9Nic2z7LgetZXFcr4YJHY/640?wx_fmt=png&from=appmsg)

到2025年底，我们交出的答卷是：

基于标杆团队的探索和实践，我们找到了AI研发范式升级之路，可以跨越个人到组织提效的鸿沟，于是我们也发布了“AI研发范式的实践框架”（如下图所示），并设定了2026年，L2需求占比要达到80%的目标，从而带动人均需求交付数大幅提升。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1UGSVrxsWEFxJKgCPSQ1icoaGfpQehPwRrPtCDNOP2t3x0mHVq3KtSvmrWJBickoEjfI0054D5ZJiabsKMbSsUrh3tHtAzZpVDZ58/640?wx_fmt=png&from=appmsg)

同时，我们持续分享这一路走来的实践经验，为更多企业提供经验参考：

[采纳率从7.9%到54%：快手智能Code Review的三阶进化](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247499564&idx=1&sn=bd155ed5a5b7afb64cfbece7338d3bf0&scene=21#wechat_redirect)

[生成率从8%到60%：快手智能测试用例生成系统的四阶进化](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247499932&idx=1&sn=fde31ecd487620a992c505214682a277&scene=21#wechat_redirect)

[采纳率从3%到80%：智能单元测试生成的进化之路](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247500120&idx=1&sn=ed8b4191d79d0da6167d74514930f0e4&scene=21#wechat_redirect)

[拦截率从15%到55%：快手智能Oncall系统演进与落地实践](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247500332&idx=1&sn=49874bc35efee9675fd6da9623f9beae&scene=21#wechat_redirect)

[AI Coding 产品演进：从续写补全到人机对等协作](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247500970&idx=1&sn=3338ca6e1eae245dfed0ac8982ba81df&scene=21#wechat_redirect)

[智能UI用例生成与执行的四阶进化实践](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDM0MQ==&mid=2247500992&idx=1&sn=56ec80386e6be243545b43374a15b0d3&scene=21#wechat_redirect)

按当时的认知，这是相当不错的成绩——毕竟当时行业里大部分企业还在看「AI代码生成率」，哪怕是到了2026年6月，很多大厂的认知才刚刚转变到“个人提效 ≠ 组织提效”，而我们已经在“如何用AI为团队提效”层面有了被验证的实践和进展。按这个节奏，2026年本应是全面推广的一年。但进入Q1后，随着逐步深入，我们发现规模复制比预想难得多。于是，我们开始认真查——问题到底出在哪里？

**02、问题：从标杆到所有团队，越来越难**

AI 研发提效基建（实践、度量、平台）都就绪了，标杆团队也跑出来了，按以往推广研发效能的模式，接下来难度应该不大。但实际上，我们发现，L2 需求占比每往上推一个层次，要付出的力气比之前多得多，且在宏观上看，L2+需求占比，并不像预期的那样和人均需求交付数成正比。

问题出在哪里了？我们通过微观的调研 + 宏观的数据印证，终于找到了这个阶段真正的 3 大卡点：

① 人：开发人员的 AI 开发能力两极分化

从 2025 年 10 月开始，我们通过大量的实战演练、必修课、AI 活动等覆盖全员。宏观看，人效指标大幅提升，但下钻看，发现出现了明显两极分化的情况。如下图所示，在 2025 年 12 月，我们通过观察 AI 代码生成率发现，30%人员的 AI 代码生成率已达 40%以上，但仍有 32%人员 AI 代码生成率在 10%以下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hLLZnAbUwNhKAOUBFQuwibLHXzW2hIPP0fQ0EQdOqxqZOTjkbhrc24TE2gKEeppbJUp4xibmlt3n6lowiaquPYDLxs3AbS76Q1LT3LvpXn6rXg/640?from=appmsg)

注：快手内部称为“AI 代码贡献率”，分母：所有上线发布的代码行；分子：分母中所有 AI 生成的代码行。

② 流程与分工：参与需求开发人员越多，提效幅度越小

我们把提效明显和不明显的需求下钻分析，发现参与需求的人数决定提效幅度，即：参与 1 个需求的开发人员越多，提效幅度越小。调研结论如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hLLZnAbUwNhgwpUI1fIl8Gibb6RGkFawYsHRwib8icOxHY3TbvPmYrjWWRqE8zZagNbsEJZ2FJ7XbUxlnT8OC52IGib952tw0Su7002BZiaT6hrE/640?from=appmsg)

继续下钻，我们发现 AI 确实让开发、测试更快了，但进而暴露出 3 个新瓶颈，我们总结为 AI 需求交付中的 3 个摩擦：

1. 人与人协作的摩擦：AI 带来的提效首先发生在局部，开发人员的开发、测试时间确实缩短了，但一天真正开发时间大约只占 30%，甚至更少。剩下的大部分时间，都花在需求对齐、协作沟通、任务交接等工作上，而这些协作成本，很快就抵消了开发效率提升带来的收益。
2. 人与研发流程的摩擦：大部分团队还是按照传统的研发流程和角色分工做需求，需求估分还是按原来的习惯来估算，不同角色之间的切换、等待，仍然存在。比如，一个前端开发人员用 AI 做的很快，已经交付了，但后端还没做完，前端开发人员就会切换到其他开发任务，等后端开发完了再开始联调。
3. 人与 AI 协作的摩擦：AI 被引入之后，并不意味着人可以立刻把工作交给 AI。为了让 AI 真正发挥作用，人仍然需要投入大量额外的时间和精力。调研中我们发现，AI 开发能力一般的人员，会成为需求开发过程中的效率“黑洞”。结合实际实践，会出现常见的四种情况：

* 人工补位：当 AI 与研发系统之间还没有完全打通时，开发人员不得不充当两者之间的桥梁，把信息不断搬来搬去。
* 上下文对齐：AI 并不了解业务背景，也无法天然理解需求语境，因此开发人员需要不断整理、补充和传递上下文，充当系统之间的“搬运工”。
* 验证与纠偏：AI 可以在几分钟内生成代码，但验证这些代码是否正确、是否符合业务需求，往往需要几个小时，甚至更长时间。AI 生成和人工验证之间，存在明显的速度不对称。
* 能力边界判断：当开发人员对 AI 的能力边界还没有形成稳定认知时，低估 AI，会错过本可以释放的效率，高估 AI，则容易导致返工和重复修改。

综上所述，上面的 3 种摩擦加起来，就造成了这种普遍现象：参与需求开发人员越多，提效幅度越小。

 ③ 业务特点与组织结构：AI 标杆团队效率高，但规模复制难

我们发现 AI 研发范式升级的标杆团队（交付效率、需求吞吐大幅提升），大多数是业产研闭环型的团队，即业务、产品、开发（前端、后端）、测试等角色都在 1 个组织内，他们在 AI 研发范式导入后，不仅是开发方法&工具在升级，组织、流程、角色也在发生变化。甚至，有一些团队的“业务”本身也在发生变化，比如从原来提供 SaaS 平台服务的变成了提供 Agent 的 AI 服务。（这个信号值得单独记一笔——不只是研发方式在变，他们交付给用户的东西本身也在变。这个变化会在后面的章节再次出现，并成为理解 L3 的关键）

相对而言，在业务、产品、研发分别是独立团队的烟筒型组织架构下，想达到预期提效效果是非常困难的。

归因：灯照得见的地方做得不错，卡住我们的是灯照不见的组织和人

![](https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNjIlWQ8ICkk9RhqgTadpzoUqicaPV7KrXSjLm28Iur7icR5IOsF8ZLicpMgTYDpKIM8uLO0vaEDyxt8OYpadcBS43bjRdu3ofianno/640?wx_fmt=png&from=appmsg)

如上图所示，结合上面的 3 大卡点，再回顾我们的 AI 研发范式升级方案，发现一个误区，我们原来设计的框架里隐含了一个假设——我们假定**研发流程**、**角色**、**分工都是**不变的情况下，提供了 AI 的效能实践、效能平台、效能度量。但目前，新的卡点正好出现在我们之前没覆盖的部分——研发组织中的人、流程与分工、组织结构：

![](https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNgzywHQu7EmFXOS6ibTjKOm2IKfzTx8heSicsQjyFAicLTxpqQPMvDK6ULzyJ7WPox76rwtlR9viciaqjr7yuANTmkxicHLoUmlCtle4/640?wx_fmt=png&from=appmsg)

问题出现在我们框架的盲区里。

**软件行业有一个规律：业务特点**决定**软件架构 和 组织形态**，又决定**研发范式**，**研发范式再影响**开发过程、方法、工程工具。

我们一直在研究 AI 研发范式，在上述规律的“右边”**找解决方案，但找到方案后我们发现更关键的瓶颈却出现在**“左边”。

很明显，这次 AI 对业务和研发组织的塑造程度，不同以往。我们想了很久，始终没有头绪，直到回头看了一段 60 年前的历史。

**03、镜子：银行60年，已经帮我们提前把路走完了**

我用银行业做镜子，因为它把我们今天面对的问题，60 年前就完整走了一遍。

L0 → L1（1960s）：计算机——机器代替手工，内部效率提升，但组织没变

1960 年代中期，美国几家大型商业银行几乎同时做了一个决定：**花重金引入 IBM 大型计算机系统**。柜员面前从账本变成终端，存款查询从翻册子变成敲几下键盘，算数速度快了十倍不止。

但如果你在那时候走进一家分行的后台，会发现分行行长办公室里什么都没变。审批一笔贷款，还是那条链——材料从柜员传到主任，主任转给副行长，副行长送行长画押。一个决策走下来，快的三天，慢的一周。计算机把记账的速度提上去了，但批准一笔业务的速度，和十年前一模一样。

所有银行同时上了计算机，起跑线整体前移，差距没变。那台机器，本质上是一个更快的算盘。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hLLZnAbUwNhCugtxESZCBugz2nboaNCyQ6E7xW8m4wtSKcAWDBMH5P1v63U9dEQ9HD6EiaiaIDKGPaDYsGjCibEkhUyTAI8B3kO3OibzpLL4JXk/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/hLLZnAbUwNj43RxZXOQLA07oExW2B20TdE59UCsbjWicsiaG7lpVbbiaT6UZ5fIZM1iao8CCacriaia3ICUVc5YzjTcxkndYmgPmWwFtLHbAJfrNw/640?from=appmsg)

L0 → L1 的核心：生产力升级了，但组织没变，效果是旧事物的加速版。

L1 → L2（1970s）：ATM——存取款全程自动化，机器直接服务用户，但组织必须跟着变

十年之后，ATM 出现了。ATM 做的不是让人更快地做原来的事，而是让机器承担了原来只有人能做的事——存取款。这意味着同一家银行，可以用更少的人完成同样的服务。柜员可以从 10 个人变成 6 个人，服务量不降反升。

但这件事的真正影响不在于砍编制，而在于：**组织必须跟着变**。

* 网点的角色变了：不再只是“人来办事的地方”，而是 ATM + 柜员的组合服务点。
* 服务模式变了：24 小时服务成为可能，网点排班要调。
* 客户关系变了：客户“不来也行”，入口不止一个了。
* 团队规模变了：更少的人做更多的事，分工方式必须调整。

但不是所有的银行都看到了这个机会，花旗银行（Citibank）看到了，他们是把组织适配做到位的那个。他们不只装 ATM 砍编制，而是把 ATM 当客户入口重新设计了网点的运营方式：24 小时 ATM 网络全城铺开、网点角色从“唯入口”调整为“服务组合之一”、服务流程跟着重建。

1977 年纽约大雪，多数银行网点关门停业，花旗 ATM 照常运转，大量储户当周转入。1977 到 1981 年，花旗纽约零售存款市场份额从 4%增长到 13%，增幅接近三倍。

而那些只砍编制不调组织的区域储蓄银行，市场份额被持续蚕食，其中多家在 1980 年代被兼并或倒闭。

![](https://mmbiz.qpic.cn/mmbiz_png/hLLZnAbUwNjzImcDiarSUXq5vPd6pqQYZiaIlSCzrPVXfcl2qhCRQW2ksGmLarzur5uggmf3c8uSflMyejwmLySMepH2HBzDWLK14G9quzotc/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/hLLZnAbUwNgH4I2a0uzNt6Lic7SXPvwh0o3g2eFcuUUlicDxA5mgUbDA5rLHclBQCje7m06Y9FvJ3IicNje5zJ8CG0vRTYuRNlvgaiaaNqrv4ics/640?from=appmsg)

L1 → L2 核心：AI/机器承担了更多工作，更少人干更多活。但组织必须跟着变，不变就停在 L1，适配程度决定效率提升程度。注意：这个阶段银行提供的业务本质没变——还是存款、取款、贷款，只是服务渠道更多、组织效率更高。

L2 → L3（1990s-2010s）：网银+移动支付——系统自主干活，业务形态和组织同时彻底重构

1990 年代网银出现后，真正跨过去的银行做的不是“让 ATM 做得更好”，而是重新定义了银行和客户的关系。

一个在外地出差的客户想申请一笔小额贷款，他在笔记本电脑上提交了申请，大约三十秒后，系统给出审批结果。以前这件事要回到网点递材料，等两到四周。

为什么能 30 秒出结果？因为系统自主干了原来只有人能干的事——**审批**：

• 审批规则变成了**代码**，风控经验变成了**模型**，原本做“信息中转”的审批岗从“审材料的人”变成了“写规则的人”

• 分行行长从地方性决策中枢变成了区域服务经理——不是因为他能力不够，而是信息不再需要经过他中转了，系统能做他以前做的事。

所有角色同时进入了同一个系统——客户、柜员、审批员、风控、运营，全部在同一条数字链路上运转。中间层消失，速度才真正起来。

但网银做得再好，银行还是“你去的地方”。2010 年代，手机让银行彻底变形。支付嵌在买东西里，理财嵌在刷手机里，贷款嵌在消费的瞬间里。银行不再是“你去的地方”，它变成了“无处不在的能力”。组织也跟着变了：从按地区分工，变成按场景和用户旅程设计。没有人再说“我们在用计算机提效”，因为计算机已经是水和电，是基础设施，不再是效率工具。网银和移动支付，前后连续，核心逻辑相同：系统/AI 自主干活，业务形态本身变了，角色重新定义，组织必须重建。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hLLZnAbUwNgvFmRicXPOOB8cYFWkWuFmxF5oBkb363Q6BedyZNr8k1dB6yo71JKlEXURkts8BI9eKaeF860ar6iaK8zXpM9XZs6eNrQbGibT50/640?from=appmsg)

![](h...