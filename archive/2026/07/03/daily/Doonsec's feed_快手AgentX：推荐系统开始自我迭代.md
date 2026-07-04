---
title: 快手AgentX：推荐系统开始自我迭代
url: https://mp.weixin.qq.com/s/h2PgHllv8MvF4phC8uSPUQ
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:44:19.738294
---

# 快手AgentX：推荐系统开始自我迭代

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1gVUsotpT1Xibd2oL81L3cN4zT8TpICH8XmWM6EicCSRsHeSTvM53bQoz851ticbMibq9svvSfFjqrdhRPb9st4MQxzc6VJdtuLoick7wXwdyScA/0?wx_fmt=jpeg)

# 快手AgentX：推荐系统开始自我迭代

快手技术
快手技术

快手技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg)![]()

过去十年，推荐系统的主线一直是把「建模」和「工程」做到更强：特征更细，模型更大，序列更长，生成式推荐和推荐大模型也在不断拓展系统边界。但在工业推荐真正的日常迭代里，最硬的瓶颈并不只在模型，而在研发生产方式本身。

一个推荐策略从想法到上线，往往要穿过数据分析、方案设计、生产代码修改、实验配置、A/B 观测、指标归因和复盘沉淀。这里面真正稀缺的不是「写一段代码」或「跑一次实验」，而是持续提出高质量假设、判断实验成败原因、并把经验转化为下一轮更好的方向。

过去，这条链路主要靠算法工程师手工推进，创新效率很大程度上被人力和个人经验线性限制。

AgentX 要改变的正是这一点。快手 AgentX 团队发布技术报告《AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems》，提出并验证了一套面向工业推荐系统的 Agent 驱动研发闭环：让 Agent 不只是辅助写代码，而是成为推荐迭代的执行主体，持续生成方案、实现代码、上线实验、读取反馈，并把每一次轨迹沉淀为下一轮进化的燃料。

在快手 App 真实业务部署过程中，AgentX 已经跑通「想法 — 代码 — 实验 — 归因 — 进化」的完整闭环。3 个 AgentX worker 在主站推荐与生活服务商业化场景中，将 374 个实验想法推进为 10 个可发布结果；相较传统人工迭代，单 worker 并发实验数提升 8 倍，单位人力业务价值提升 3.7 倍，并带来主站用户 App 消费时长累计 +0.561%、生活服务年化收入超 1 亿元的业务收益。

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqGY8SIJfcLia6MOZO00pcEWicibLKkCR6ucj7XRN5VJmBB8Mw6ea0ChKlzQZVpV8jcnnSsURwMep3LSV9PULjTVJoP2Sa2D4Qtjt4/640?wx_fmt=png&from=appmsg#imgIndex=1)

* AgentX 技术报告：https://arxiv.org/abs/2606.26859v2

背景：推荐迭代的瓶颈，正在从模型转向研发闭环

如果说 Scaling 解决的是「模型能不能更强」，Reasoning 解决的是「模型能不能想清楚」，那么 Agentic 真正要回答的是「系统能不能把事情持续做成」。对推荐系统而言，这个问题尤其重要：推荐迭代从来不是一个单点推理任务，而是一条横跨数据、代码、平台、实验、指标和业务判断的长链路。

传统人工迭代至少有三个明显天花板：

* 吞吐受限于人：一个工程师通常只能串行推进少量实验，每个想法都要手工完成分析、开发、上线和复盘。只要执行链路不变，增加人力只能带来线性提升。
* 经验难以沉淀成系统能力：很多失败实验并非没有价值，它们暴露了业务边界、平台约束、特征缺口和策略风险。但如果这些信息只停留在文档和个人记忆中，系统下一次仍然可能重复踩坑。
* 离线判断无法替代真实用户反馈：推荐系统最终优化的是线上用户行为和业务目标。一个方案离线看起来合理，不代表线上一定有效；真正可靠的奖励信号只能来自安全、可控、可归因的 A/B 实验。

因此，AgentX 的目标不是做一个更聪明的代码助手，而是重构推荐研发的生产函数：把工程师从大量重复执行中释放出来，把人力集中到目标设定、关键审核和高阶判断上；把执行、验证和经验沉淀交给 Agent 系统持续推进。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqGQ2S1lpbkoyBz7Roc4iaE6rGyEwErjJwXUZcaHrk0jyicJ2Fpibckc9GwA9Onxibu4oGJILPI87cicsJYBbRO93yOLj3uvpp1o0icSQ/640?wx_fmt=png&from=appmsg#imgIndex=2)

AgentX 怎么做？把推荐研发拆成可执行、可验证、可进化的闭环

AgentX 将一次完整的推荐实验拆解为 Brainstorm Agent、Developing Agent、Evaluation Agent 和 Harness Evolution。前三个阶段负责把一个想法推到真实线上结果，第四个阶段负责让 Agent 系统从历史轨迹中变得更强。

* Brainstorm Agent：把模糊目标变成可落地方案

真实业务输入往往不是完整需求，可能只是「提升观看时长」「改善冷启」「优化某类用户转化」。如果任由模型自由发挥，很容易产出依赖不存在特征、触碰错误链路、或重复历史失败方向的「漂亮想法」。Brainstorm Agent 会综合历史实验、系统架构、数据分析和外部论文研究，把目标收敛成少量有优先级、有证据、有边界的候选方案。每个方案都要说明目标指标、实现位置、所需信号、预期机制、风险和验证方式。

* Developing Agent：让代码生成真正进入生产语境

在工业代码库里，语法正确远远不够。字段看起来合理但实际不存在，策略写完却没有注册到正确队列，实验开关没有默认关闭，都会让线上实验失真。Developing Agent 通过仓库知识库、特征 schema 查询、DSL 检查、C++ 语法检查、dryrun 验证等工具，把代码生成约束在真实仓库和平台规则内。在模型研究侧，它还支持论文复现、模块消融和跨论文结构组合，并通过确定性日志解析、专家投票和因果链归因保证结论可信。

* Evaluation Agent：把线上 A/B 变成系统的真实奖励

AgentX 不把离线指标或模型自评当作最终答案。Evaluation Agent 负责安全部署、流量分桶、参数冲突检查、指标读取和 guardrail veto，避免局部收益牺牲用户体验或业务安全。更关键的是，它会把成功和失败都资产化：成功实验成为后续方案的 playbook，失败实验沉淀为反例、约束和剪枝规则。

* Harness Evolution：让 Agent 自己修正工作方式

AgentX 的自进化来自 SGPO（Semantic-Gradient-based Prompt Optimization）。它不直接优化某个推荐策略，而是从历史执行轨迹中找出 Agent 工作方式的缺陷：是否遗漏业务约束，是否证据不足，是否交付字段不完整，是否反复犯同类代码错误。随后，SGPO 将这些诊断转化为子 Agent 的局部 harness 更新，并通过旧版与新版在同一批 replay 任务上的配对评估决定是否接纳。

这才是 AgentX 最关键的区别：它不是把人工流程简单自动化一遍，而是把每次执行都变成系统能力增长的一部分。

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqGqsXg0mVBG0TteFiahA5Dz339P1fgKj8YXYC3w551icxGkP24icH4Zesm8OUwIKdtMA4lTwxrAW27TUFtww0vXgkHumVeJm5UH0Y/640?wx_fmt=png&from=appmsg#imgIndex=3)

实验结果： 374 个想法，10 个可发布结果

AgentX 的核心验证来自快手 App 的真实部署。3 个 AgentX worker 并行运行在主站推荐和生活服务两个生产场景，完整记录 idea pass、code-and-launch、positive evaluation 等节点。

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqEM5h1MicDjTj2ib0qMdcxMD15ibdX0LSadZJkc2P0akun9rwoxj4zRUCKCCEt3Yzxl70h571urfgibia5yVzPlXRRFVvBdEgicGPYnU/640?wx_fmt=png&from=appmsg#imgIndex=4)

整体漏斗如下：374 个实验想法进入系统；106 个通过方案审核，idea pass rate 为 28.34%；100 个完成代码实现与上线，code-and-launch rate 为 94.3%；10 个获得正向评估并达到可发布标准，positive evaluation rate 为 9.9%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqFQnjtOGmN8vPlSw27LFGovqWD9LcAHzynufqXgiacQOWSxRkX648qt9vVgK3GCFiabULCaFjWjSF06dSjRWSPCBd8ziawhCn9tDU/640?wx_fmt=png&from=appmsg#imgIndex=5)

从业务线看，主站推荐 361 个想法产生 8 个可发布结果；生活服务 13 个想法产生 2 个可发布结果。最终，这些实验带来了真实业务收益：主站推荐用户 App 消费时长累计提升 +0.561%；生活服务为快手平台贡献年化超 1 亿元人民币收入。

更重要的是生产效率被重新定义了。传统人工流程中，工程师通常串行推进实验；AgentX 将方案生成、编码、上线和监控拆成并行流水线，使不同想法可以同时处在不同阶段。单个 AgentX worker 平均维持约 12 个并发实验，而传统工程师约为 1.5 个，并发能力提升 8 倍；单 worker 每周产出 1.1 个可发布结果，是人工方式的 13.8 倍；单位人力贡献的累计 App 时长收益达到人工的 3.7 倍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqHvQZyVuYU66J0Txq1oWc3E0YeQrd55SlRgV84l4901aE4We5U5NCUUKTzjUpZhkXPldRDEbia4tKUh3lQy2ROuibTZBtkY8EJCM/640?wx_fmt=png&from=appmsg#imgIndex=6)

在窗口内，AgentX 还展示出明显的自我加速：周并发实验数从 15 增至 60，idea 通过率从 15% 提升到 45%，每周可发布结果从 2 个提升到 5 个。随着技能沉淀、失败模式积累和 dryrun 模板成熟，系统不只是跑得更快，也在更快地排除无效方向、把资源集中到更可能成功的实验上。

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqE6IObudjibM5l4XYEVhxoE4hjly3oXdBUmhsrR8jPT220G3npQR4SWeKP8MtR5Vw2cSmN3nDUHzVmFb5e9k7PdrZb72yvOibmpk/640?wx_fmt=png&from=appmsg#imgIndex=7)

从策略迭代到模型研究：同一个闭环可以迁移

AgentX 的价值不止在线上策略实验，在模型侧研究也有相应拓展：系统可以自动阅读近期推荐论文，在统一代码库上复现方法，基于 KuaiRand、Taobao、Amazon、ML-1M 等公开数据集评估结果，再从表现较好的模型中抽取互补模块，进行跨论文结构组合与新架构探索。

在独立模型研究实验中，AgentX 跑通了从论文复现、模块组合、离线评估、在线测试到发布评审的完整链路。其中达到发布级别的模型在快手 App 直播时长指标上带来 +0.865% 收益。

这说明 AgentX 不是某个业务场景下的脚本集合，而是一套可迁移的自动研发范式：只要问题能够被组织成「提出假设 — 实现方案 — 获得反馈 — 沉淀经验」的闭环，AgentX 就有机会把它改造成批量化、自进化的研发流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqE9DdhicLKFVPuSdibWfHOw6aYcoicVzjUOtJib05Nvw0yjw6uYZumdql16Kzaj8Yoiat9fgLdsGn43jegQVPLYpPiaVVgp0tXpNuiaww/640?wx_fmt=png&from=appmsg#imgIndex=8)

案例分析：PCV 增强精排分的两轮闭环优化

我们进一步展示一个 PCV（Post-Consumption Value，消费后价值）增强精排分的真实案例。目标是在保持真实曝光和用户体验护栏稳定的前提下提升用户观看时长。PCV 信号来自分享、收藏、重播等消费后行为，能够反映内容的长期价值；但它也有天然风险，因为低质或噱头内容同样可能激发部分消费后行为。

第一轮中，Brainstorm Agent 选择直接引入 PCV boosting；Developing Agent 将其实现为带实验开关保护的乘法打分公式；Evaluation Agent 通过线上 A/B 发现，该方案方向上略有收益，但统计显著性不足，并伴随部分人群和多样性指标风险。

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqEibcr6pqJ7DSSiaHEGajBLwJ7Gt7ovbCtq00OLd4z1cwLKYicLAkI3mRSKusYfVC0TXmiadLYCh2LqGcOmRmRmrRLh1jc80345VWY/640?wx_fmt=png&from=appmsg#imgIndex=9)

关键在于，AgentX 没有把这次结果简单归为「失败」。系统把它转化为下一轮输入：直接提升高 PCV 内容可能放大噪声，因此第二轮引入质量门控、用户活跃度自适应权重和时长导向底分。最终方案取得用户观看时长 +0.071%、真实曝光 +0.118%，同时用户体验护栏保持稳定。

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqH2XkEOoib7kz5EfGrcFYr5zmxJuvKJxZ89FYPE2YLNGdxiaCwE9nuZgRiaer3zmwH0IHbNGwKslQdtORsxticprqY1FcHrWHUjoiaw/640?wx_fmt=png&from=appmsg#imgIndex=10)

这个案例说明，AgentX 的能力不在于一次性给出完美答案，而在于把真实反馈变成下一轮更强的假设。推荐系统中最有价值的经验，往往就藏在这些「第一轮不够好」的实验里。

总结与展望

AgentX 用真实业务闭环回答了推荐系统自动研发中最关键的三个问题。

* 推荐算法迭代能不能由 Agent 执行？可以。但前提是 Agent 不能停留在文本生成或代码补全层面，而必须进入真实生产链路，理解系统知识、遵守工程约束，并接受线上 A/B 的检验。

* Agent 产生的经验能不能复利？可以。通过实验知识库、失败资产化和 SGPO 自进化，AgentX 将每次执行轨迹转化为后续方案生成、代码实现和 harness 优化的数据来源。
* Agentic 推荐研发能不能产生真实业务收益？已经可以。真实部署中，AgentX 带来了 8 倍并发能力、3.7 倍单位人力业务价值、主站 App 时长 +0.561% 和生活服务年化超 1 亿元收益。

下一阶段，推荐研发的分工会发生变化：一层工程师与 Agent 系统协同，面向业务目标推进策略和模型迭代；另一层工程师持续进化 Agent 框架、工具链和基础模型能力。每一次实验产生的轨迹数据，都会同时服务于短期业务优化和长期智能成长。

当想法生成、代码实现、线上评估和经验沉淀都可以被规模化、闭环化、可验证地自动执行，推荐系统迭代就不再只是「增加人力」的线性增长，而会进入「经验、算力与智能共同复利」的新阶段。

AgentX 的生产实践表明，自进化、批量化、Agent 驱动的工业推荐研发已经不是设想，而是正在真实业务中释放价值的新生产方式。

五、团队介绍

* 生成与排序模型中心：

  作为支撑快手国内与海外（Kwai）短视频推荐系统的核心驱动引擎，我们专注于构建业界领先的短视频内容推荐模型体系，致力于通过最前沿的用户行为建模、模型参数scaling、生成式召回、LLM4REC等前沿技术，持续优化内容分发效率与用户体验。诸多成果发表于KDD\SIGIR\WWW等顶级会议。
* 推荐大模型团队：

  从事快手下一代推荐系统的底层范式研究，挑战推荐领域长期未被根本解决的核心问题，包括但不限于以下方向：

* 探索推荐系统从"记忆式关联建模"到"具备世界知识与逻辑推理的认知建模"的能力跃迁，让模型能够进行反事实推演、解耦混叠反馈、跳出信息茧房；
* 探索生成式推荐范式下模型结构、训练目标与表征空间的统一，破解判别式推荐难以解决的长尾分布、序列级编排与开放候选生成等根本性瓶颈；
* 探索推荐系统从"千人一面的固定流水线"到"千人千策的双向协同"的范式升级，研究人-内容-平台三方长期共赢的飞轮机制与可感知、可干预的推荐服务形态；
* 探索上述新范式在亿级用户、毫秒级响应、万亿级候选规模下的工程可行路径，研究大模型推理能力与现有推荐系统的协同共存方式，让"会思考的推荐"真正规模化落地。

六、招聘职位

* 推荐大模型算法专家-【OneRec】
* 推荐算法工程师-【Ranking方向】
* 推荐算法工程师-【Matching方向】

* 任职要求：

* 对AI技术具备强烈热情，认同技术驱动业务与社会价值提升；
* 高度关注推荐大模型/大语言模型技术前沿，对行业动态有持续追踪和理解；
* 在推荐系统、计算广告、信息检索、NLP、LLM、强化学习、多模态、高效训练/推理等至少一个领域具备扎实技术积累与业务落地经验；
* 具备优秀的工程实现能力，熟练掌握常用数据结构和算法；
* 能够快速阅读和复现前沿文献，具有良好的问题分析、解决及团队协作能力。

* 加分项：

* 在SIGKDD、ICML、NeurIPS、ACL、WWW、RecSys等国际顶级会议发表过论文；
* 有ACM/ICPC、TopCod...