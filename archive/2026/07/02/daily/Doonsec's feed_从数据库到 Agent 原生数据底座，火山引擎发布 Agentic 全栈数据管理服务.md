---
title: 从数据库到 Agent 原生数据底座，火山引擎发布 Agentic 全栈数据管理服务
url: https://mp.weixin.qq.com/s/jSAGa5UGKkl4qpyScEd2WA
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:45:30.358503
---

# 从数据库到 Agent 原生数据底座，火山引擎发布 Agentic 全栈数据管理服务

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9Fed6ON8ojbfLWQZdZB7n8wXLXDEJllROyEUdb4XkIVpM1I0j3t3fXwib0YCkx0pibVV4z8RdPL7epCIyWaJZmNUj7wS8o2fqMnwro/0?wx_fmt=jpeg)

# 从数据库到 Agent 原生数据底座，火山引擎发布 Agentic 全栈数据管理服务

字节跳动数据库
字节跳动数据库

字节跳动技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

当数据消费主体从 “Human + Application” 扩张至千万级 AI Agent，传统数据库的能力边界已被彻底打破——海量 AI Agent 全天候自主检索、推理、协作、调度数据，传统数据底座已无法适配全新的业务逻辑。2026 火山引擎 FORCE 原动力大会·SUMMER，火山引擎数据库推出“**Agentic Data Management and Services**”产品体系，并完成全栈产品升级。

**市场拐点：AI Agent 正从 AI 助手，进化为企业可规模化部署的自主系统**

过去一年，市场明确形成了 **A3H 四元消费结构**：AI、Agent、Application、Human，其中 AI Agent 的体量正呈指数级暴涨：

* 市场增速：Grand View Research 数据显示，全球 AI Agent 市场年复合增速超 40%，2030 年规模有望突破 500 亿美元；中国 2023-2033 年 CAGR 高达 50.8%；
* 规模增长：IDC 预测，活跃 Agent 将从 2025 年 2860 万暴涨至 2030 年 22.16 亿，CAGR 高达 139%；
* 企业渗透：Gartner 预测，2026 年底 40% 企业应用会嵌入任务型 AI Agent，远高于 2025 年不足 5% 的渗透率。

这反映了一个核心事实：AI Agent 已是规模飞速扩张的新型数据消费主体，数据使用者已然迭代，底层数据基础设施也必须重构升级。

**在这场底层变革中，数据库为何如此举足轻重？**

以往数据库的访问对象是规整、可控的业务代码，人类手动编写 SQL 完成查询；而现在，调度数据的是一批具备自主规划、反复试错、瞬时并发暴涨特性的 AI Agent。这就使得负载波动、交互逻辑、实例扩容周期、数据留存周期全部被改写，**数据库作为数据存储与交互的核心枢纽，**首当其冲，必然要完成底层革新。

**战略全面升级：从数据库到 Agentic Data Management and Services**

面向 AI Agent 规模化爆发的新时代，火山引擎数据库正式完成战略定位升级：转型为 **Agentic Data Management and Services**服务商。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9FeeXW8jIJ7EANGGc8KhSiaqGURlfVVmPuWLM0g4RQqOpWicDRicYQiaaG3uuFewGaaFYTCY5jfKbbhw4t14Xb9oEycsttXTEIehicyCw/640?wx_fmt=jpeg&from=appmsg)

本次 FORCE 大会，面对 Agent 数据管理的挑战，在过去的半年火山数据库带来五大重要发布与更新。

**ContextSearch：正式 GA 发布，真实业务场景搜索正确率提升 24%**

ContextSearch 为 Agent 提供可持续化的高质量数据检索底座，将检索范式从被动单步的 RAG 全面跃迁到主动多步的**Agentic Search**：

基础 RAG 沿用“用户输入 → 知识召回 → LLM 生成 → 答案输出”的线性流程，在面对实体类、统计类、时序类等复杂诉求时往往力不从心。ContextSearch 则基于 ReAct 框架构建主动规划引擎，驱动“感知→ 推理→ 执行”的自主闭环，并打通安全合规数据接入与结构化上下文反馈流。

实测显示，依托 ReAct 机制的意图拆解与澄清能力，在面对"同名客户 / 指代不清"等 **歧义场景** 时，Agentic Search 准确率达到 91.7%；而基础单步 RAG 因无法消歧，在该场景下准确率为 0%。

基于客户真实线上业务数据与 200 条复杂问答评测集的实测显示，ContextSearch 相较基础 RAG 搜索正确率提升 24%，全面具备进入生产级 Agent 系统的能力。

![](https://mmbiz.qpic.cn/mmbiz_jpg/FGB4hYw9Fefiab3vqiaS32VrIgZ9loFMofSsuqDYyFVevvrAfrticvftKVxjVMNiahiatZPVujpaDy4uzsVXkLjYO7qw8ERUAHZCDFRq7Eko6p3A/640?wx_fmt=jpeg&from=appmsg)

**火山引擎 Mem0 全新功能发布：支持“自进化”、“Graph Memory”，让 Agent 持续学习**

Agent 的长期价值，取决于它能否"记得住、学得会、改得了"。火山引擎升级核心产品火山记忆库 Mem0，新增“任务记忆”、“Graph Memory”两大功能：

1. **提出“基于任务的记忆”理念：**构建了一个完整的“经验自进化循环”：适配长周期、多轮循环的复杂业务任务，可沉淀 Agent 过往任务成败经验与用户偏好，实现智能体持续自主迭代进化。OfficeQA BenchMark 测评结果显示，引入任务记忆后的 Agent 实现了**任务成功率提升 10%、Token 消耗节省 44%、整体时延减少 39%**的显著收益。
2. **发布 Graph Memory 功能：**支持 Agent 存储、查询多跳关联关系数据，在 LoCoMo 标准评测中，启用 Graph Memory 后得分由 86 提升至 91，达到行业领先水平。

**飞书妙搭 OpenClaw** 接入了火山 Mem0 这一深度增强的企业级记忆服务后，从存储底座、抽取策略到检索算法进行了系统性升级。业务在此基础上围绕场景进行适配性优化后，**业务模拟 QA 准确性高达 97.6%。**

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeeHTdujg0QXZ47W64b76oeaiajxOicZjoc2aYBGdt1XvlMmCfmfLF8RngoUZqwicokuEHw3DcPuyO1WV7s4mu6ia03KYaFEPno1S84/640?wx_fmt=png&from=appmsg)

**AI 原生 BaaS 平台 Supabase 正式 GA 发布：AI 后端服务 All in One**

面向 Vibe Coding 时代，面对 Agent 与 AI 原生应用对"敏捷、高效后端"的迫切诉求，火山 Supabase 把"资源供给本身做成产品力"，让开发者只关注业务逻辑。本次大会上，火山 Supabase 正式发布 GA 特性：

1. **秒级创建：**集 Auth、DB、Messages、文件存储等核心后端能力于一体，同时深度集成 MCP/Skill/CLI、支持自然语言接入，并内置 AI 友好 API，从而支持 Coding Agent 模块化搭建后端，灵感出现即可验证落地；
2. **全链路 Serverless：**火山 Supabase 从业务层、服务层到数据层全链路 Serverless 化，按需使用、用完即走，完美匹配 AI Agent 多负载、负载不可控的特征。
3. **数据分支（Data as Git）：**火山 Supabase 把开发者熟悉的分支、回溯、恢复融入数据体系：Branch 可建独立数据分支，开发、测试、训练互不影响线上；Timetravel 可回退到任意时间点并观察完整状态；PITR 可在数据出问题时快速回撤恢复。把回溯从临时补救动作变为系统原生能力。

该产品自 2025 年年底上线，半年内实例数量**增长****18 倍**，现已达百万级，是火山引擎增速最快的数据库产品。

**猿辅导**基于火山 Supabase 一站式后端能力打造了对话式应用构建平台 Rush，让非研发人员通过自然语言对话即可创建功能完备、安全合规的企业级应用，将“创意到价值”的转化周期**从数周压缩至数小时**。

实测数据显示，Rush 平台在应用上线速度上提升 2-3 倍，单位人天投入 ROI 提升 50%，前期基建成本接近于零（≈0），并稳定运行于 99.9% 平台级 SLA 之上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeeOZHhL36wqZAiap75m7Ijhu0qZJqOBbswaL7REic8D4ib35GicAI2FmV8b3Wxp6bSRgsaWeWicBhmXBmiahfARny7sZCTZAT5JGQ5icY/640?wx_fmt=png&from=appmsg)

而在**扣子编程**实践中，在每个 Vibe Coding 生成物（网页应用、移动应用、小程序、智能体、技能等）背后，都会同步创建和使用一个 Supabase 实例运行这些产物，并且使用火山 Supabase 的多分支能力（Branching）进行环境隔离。在使用火山 Supabase 后，扣子编程整体的交付效率、质量、成本，都得到极大的改善。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FecPrUcrSXdAftJB0r0GJu0Hgic6HbEFUZ0PM4ibMeUVArC0UGtic8vxRfjpeJjAFAZZEEua4OIhfVz19uB80d7ZKXH9AbwUfS6seM/640?wx_fmt=png&from=appmsg)

**火山 Milvus 向量数据库：行业 SOTA 引擎，创新 DiskANN+RaBitQ 算法再进化**

向量检索是大模型读懂现实世界的语义桥梁，海量向量下平衡性能与成本，是技术核心要务。

1. **Agent 场景适配：**火山 Milvus 新发布 Serverless 共享形态，无需关心底层资源，按使用量计费。Serverless 实例可以秒级创建、10 秒内进行弹性自动伸缩，完美适配 Agent 场景下快速拉起，成本可控的需求。
2. 超越 VectorDBBench 榜首的高性能：引擎层面，Milvus 创新引入 DiskANN + RaBitQ 算法，在保障极致召回质量的同时，将 QPS 推升至 2 万以上，导入时间、P99 延迟、Recall 等关键指标均位居行业前列，持续夯实其作为“行业 SOTA 向量引擎”的核心地位。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9FedJKpyib6UM3SLl9wb8enJhIx3vWtpyqAJDZ1YdnQ414VzcVVibEYDEJtkBrnXm1Z1a7qf8RZ3fHiatQib33zgKY427lv2NU3MM6iac/640?wx_fmt=jpeg&from=appmsg)

3. **生态扩圈：**火山 Milvus 支持通过 DTS 将 MySQL 数据 Embedding 向量化导入到 Milvus 中；同时 Milvus 也支持直接从 TOS 中向量化导入；2026 年年初发布 Skill，提供近百个 CLI 功能，覆盖几乎全部控制面操作与主流数据面 API。

**DBCopilot：安全可控的 agentic 数据库工具服务，打造开发、运维与数据分析闭环。**

当 Agent 开始大规模操作数据库，企业“敢不敢把生产级数据库交给 Agent”已经成为行业共同面对的挑战。DBCopilot 打造了安全可控的全域数据库统一接入底座，通过凭证托管、细粒度权限管控、全链路安全审计，统一纳管多源跨实例数据库，打通开发、运维、数据分析完整闭环。

1. **数据开发：**自然语言转 SQL，四维 Evaluator 把关，支持五大数据库、600+ 安全规则。
2. **数据库运维：**主动巡检 + 动态 Runbook + 根因诊断闭环；日均完成一万余次故障智能诊断，故障定位恢复时长缩短 50%，人工运维成本下降 70%。
3. **数据分析：**零数据搬迁、跨实例分钟级分析，自然语言转 SQL 在 2025 Spider 排行榜第一。

实际生产如 Vibe Coding 场景中，依托 DBCopilot 数据库智能助手，开发者可在 IDE 通过自然语言生成合规 SQL 与工单，大幅简化建表等操作。该技能累计下载 8300 次，凭借高准确率有效提升研发效率，广受内部开发者好评。

**行业展望**

从数据库到 Agent 原生数据底座，这场变革的本质，是数据基础设施开始主动“为 Agent 而生”。

对于客户，它意味着更低的门槛——企业可以"开箱即用"地构建安全合规的 Agent 应用，让 AI 价值更快落到业务；对于行业，它意味着新的标尺——火山引擎以 **Agentic Data Management and Services** 的完整路线图，推动行业从“AI 用数据”迈向“数据为 Agent 而生”。

Agent 的时代已经到来，而每一个 Agent，都值得拥有一座为它而生、可信赖且可进化的数据底座。这，正是火山引擎持续投入的方向。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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