---
title: 快手技术沙龙精彩回顾｜聚焦 Data Agent，共探数据生产与智能决策新范式
url: https://mp.weixin.qq.com/s/OI-YYECNVwEFiiTfR2d86g
source: Doonsec's feed
date: 2026-09-21
fetch_date: 2026-09-22T07:02:17.658376
---

# 快手技术沙龙精彩回顾｜聚焦 Data Agent，共探数据生产与智能决策新范式

# 快手技术沙龙精彩回顾｜聚焦 Data Agent，共探数据生产与智能决策新范式

快手技术
快手技术

快手技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

9 月 19 日，快手技术沙龙第五期在北京成功举办。本期沙龙以《Data Agent：数据生产与智能决策新范式》为主题，来自快手数据平台团队、云器科技、腾讯的多位技术专家，共同探讨 Data Agent 从单点助手工具走向企业级规模化生产决策伙伴的实践路径，分享基础设施建设、业务场景落地、记忆与知识工程等一线经验。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1Wo91SeyawbHufrkGeqWLwTpncc5lyiaVy8UagjJfNWLFKtiabGjY0gQaj2xQscDodPx7lPAmDk1k9kOfnVWmZYpV3xqiaN2q1U8M/640?wx_fmt=jpeg&from=appmsg)

本次沙龙上，快手技术团队首次系统分享了 Data Agent 规模化落地的关键运行指标：平台 WAU 已突破 10,600，周人均对话次数达 55 次，数据分析师、产品运营人员渗透率超过 80%，NPS 达到 73.5，单次任务提效中位数达到 13 倍。

在业务应用层面，Data Agent 已深度服务于主站、电商、商业化、生活服务、海外、社科、安全等多条业务线，覆盖取数分析、报告生成、数据开发运维、A/B 实验智能分析、智能埋点、资产服务等全链路场景，逐步成为业务数据生产与智能决策的重要基础设施。

融入工作日常：快手 Data Agent 走向规模化应用

##

## 回顾快手 Data Agent 的演进，并非一蹴而就。2025 年上半年，团队以 Workflow 为主，从单点场景切入；下半年逐步拓展到更多场景；2025 年底至 2026 年一季度，完成从 Workflow 到 Agentic+Skill 的架构转向，并在生产和分析场景加速落地；到 2026 年二季度，快手完成 Data Agent 品牌和能力统一，进入万级用户规模化应用阶段。

##

## 在快手数据平台产品技术中心负责人张蕤看来，真正难点不在于做出一个可展示的智能问数产品，而在于把它做成能覆盖多角色、多业务、可持续演进的企业级 Data Agent。围绕这一目标，快手将能力建设拆成两条主线：一条提升泛化能力，让 Agent 能够处理复杂任务；一条保障准确可信，让结果能够稳定进入真实业务流程。

##

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1UMItKTSD9GKIAffoicibcibbKd9AmR9XLOLQ8Z6SuRI986R8AQ8jicqtXK7gwdCAz44E8wxDibXqicCh7qCTP2jNiahEHWxOO94iaYwyc/640?wx_fmt=jpeg&from=appmsg)

快手数据平台产品技术中心负责人 张蕤

在泛化侧，快手以 Agentic 架构实现从预设流程到自主规划与多轮推理，面向复杂探索与跨维度分析；构建起系统层通用能力、业务层专业纵深、个人空间层经验沉淀三层 Skill 体系，目前已沉淀上百个业务 Skill，Skill 市场累计汇聚 2000+ Skill；通过父子 Agent 统一入口与智能路由，将路由准确率提升至 95%；同时推出智能数据站点，让用户通过自然语言生成可持续运行的数据应用，把一次性分析报告升级为长期可用的数据产品；在数据生产侧，则以“研发包”驱动需求解析、口径确认、开发、测试、发布、运维的端到端闭环，让 Agent 能够真正进入生产流程。

在准确侧，快手将知识划分为数据核心实体、业务结构化知识和业务非结构化知识；其中，结构化知识进一步覆盖物理层、语义层和本体层，并以“一个视图、多种存储”适配不同知识形态，核心资产知识覆盖率超过 80%，知识服务准确率达 83%；评测准入不再只看 SQL 能否执行，而是从指标、筛选、维度、粒度、时间和数值六个维度，对最终业务结果进行比较，累计评测超过 60 万条，上线准确率门槛为 80%；事中诊断通过 Trace 全链路还原与智能诊断 Agent 形成“发现—复现—诊断—修复—回归—沉淀”闭环；质量洞察则以任务级对话段为粒度，把问题进一步定位到具体 Skill、知识、Tool 和 Prompt 资产，并持续改进。

张蕤还分享了两个代表性案例：新品类挖掘平台将从识别到决策的周期由近一周压缩至半天；在电商广告智能诊断场景中，助手则把单次诊断耗时从半天至一天缩短到约 5 分钟。在他看来，这些案例体现的不只是效率提升，更是数据工作方式的改变：Agent 开始承接重复取数和标准化分析等工作，人能够更加聚焦洞察与决策；个人经验也被沉淀为 Skill、站点和可复用流程，为更多角色自主完成数据任务提供了基础。

电商场景实践：构建智能消费与智能生产双轮体系

##

##

## 从平台级通用能力到垂直业务场景，Data Agent 的落地并非技术能力的简单平移，而是需要针对业务特性完成大量针对性适配。电商是快手数据需求密集、节奏紧凑的业务场景之一，对数据响应效率和结果准确性提出极高要求，快手电商用增营销&支付数据负责人方彬分享了 Data Agent 在电商场景中的落地过程。

##

## 方彬表示，电商场景中的 Data Agent 落地并非一步到位，而是在真实业务压力下持续迭代：从早期答非所问到逐步实现精确答疑，从承接临时取数到支持复杂报告生成，再从消费侧分析能力延伸到生产侧提效。其背后的关键支撑，是知识库建设、取数 Skill 构建与准确性保障体系的逐步完善。

##

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1UOuwicm9APwGRdfibFP9uFWj6ibUBS2V76jYdwASuHXU3VMzyQT8G4Xwnsm2cRvoUArMI70GUibg0TxqNOic1uEfiaDn8M2IEUnLvtE/640?wx_fmt=jpeg&from=appmsg)

## 快手电商用增营销&支付数据负责人 方彬 过去，业务想要一个数据，要么提给数据分析师、数据研发，要么提给后端技术，响应方式依赖人力排队；Data Agent 上线后，不只是研发提速，而是把“提需求、等排期”的被动供给模式，逐步转变为业务可自助消费的数据服务模式。 消费侧最大的难点是口径。以 GMV 为例，同名不同义的指标大量存在，模型如果直接“自由发挥”，就会让不同用户得到不同答案。快手电商的做法是先完成指标维度规范化与准入筛选，再围绕业务术语、指标说明、数据集职责等沉淀知识，最终通过数据集增强取数和 Text2SQL 增强取数，将“全局找表或指标”收敛为“专题内找对表或指标”，推动评测准确率从初期 40%—50% 提升至 90% 以上。目前，快手电商 Data Agent 周活已达 2000+，周人均对话 40 多次，对话失败率仅 0.7%。 生产侧，团队把重点从“让 Agent 写代码”前移与后扩到全链路：需求理解与口径自动对齐、1000+公共词根与字段命名规范化、代码质量/数据质量/流程质量三重保障，并以“通用框架+业务研发包”实现端到端交付，覆盖埋点方案、Hive 表、数据集、A/B 模板、看板等多类交付物。对此，方彬总结出五条落地经验：标准规范的数据基建、业务术语知识维护、业务场景增强规则、标准流程 Skill 化，以及边界问题处理方案。其核心逻辑是：该代码化的必须代码化，该让 Agent 发挥的就让它发挥。 重构 A/B 实验分析：从人工看数到 Data Agent 驱动智能决策 如果说早期实验平台解决的是“能不能更快看到结果”，那么 Data Agent 正在解决的是“能不能更快理解结果、形成下一步动作”。过去，A/B 实验分析往往依赖人工看数、经验判断和多轮沟通，效率瓶颈明显。快手 A/B 实验平台产品技术负责人覃侃表示，平台正从指标看板分析、实验洞察分析进一步迈向 Data Agent 驱动的智能化分析，并通过 Agent 对话和 Copilot 两种方式服务实验设计、实验归因、实验报告等场景，帮助用户更高效地完成实验分析。 目前，快手 A/B 实验平台同时在线实验数超过 1.3 万，每天新建实验数超过 150，周活用户超过 5,000。通过将指标计算从 Spark ETL 迁移至新一代 OLAP 引擎，以 LT7 指标为例，计算耗时从 90 分钟降至 42 秒，成本节约 92%。在此基础上，平台进一步以 Data Agent 为统一底座，将实验元信息、指标体系、数科知识和分析工具封装为可编排的 /abtest Skill，覆盖实验设计、实验归因、智能报告等核心场景。 ![](https://mmbiz.qpic.cn/mmbiz_jpg/1gVUsotpT1UOWNw8SDGccU5OicenWQP1nicCyrkSDE5PiabMpvbhnSIvEJxnqdBstEibdUEKhRWVW6by1R5rvxhedrUb9xMQEM2iaAZVCmic5jSog/640?wx_fmt=jpeg&from=appmsg) 快手 A/B 实验平台产品技术负责人 覃侃 这意味着，Data Agent 不再只是帮助用户更快拿到实验结果，而是开始帮助用户更快理解结果、组织证据并形成下一步判断。用户既可以在对话中主动发起分析，也可以在指标卡、趋势图等页面原地获得智能辅助。平台能力以 Skill、CLI、Open API 等方式开放后，业务也开始结合自身经验形成二创 Skill，已在多类业务分析与评估场景中沉淀 30 多个案例。 覃侃介绍，团队还在探索“智能调参”方向，让系统基于实验结果与业务目标自动生成候选方案，经人工确认后进入下一轮实验。Data Agent 正在推动 A/B 实验平台从分析工具走向决策引擎。 行业共识：为什么需要专门的 Data Agent 快手三位负责人更多回答了“Data Agent 在企业里能做什么”，外部嘉宾则从架构、知识和记忆工程视角，回答了“为什么数据领域需要专门的 Agent”。 云器科技联合创始人& CTO 关涛将通用 Agent 和 Data Agent 做了区分：前者主要在文件、代码和 API 环境中完成跨领域任务，后者则需要进入数仓、湖仓、指标和报表，在 Schema、血缘、语义模型与权限约束下完成查询与分析。换句话说，通用 Agent 更像“会用很多工具的项目助理”，而 Data Agent 更像“懂数据资产、口径与权限的数据分析师”。在他看来，Data Agent 不是给通用 Agent 多接几个数据工具，而是围绕领域知识、数据工具、权限边界和可验证产物重新设计一套生产系统。

## ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1Uiciac0b9ovqmxWOTZXcbfYRGibr9brUUOibo3HzsyjxUvcdZJsfUHFKOmHib5kYIRibicNEVFpRJvmars0cOZbAsUyAdxibOq6dHTicdM/640?wx_fmt=jpeg&from=appmsg) 云器科技联合创始人&CTO 关涛 关涛强调，Agent 不应以不可控方式直接进入生产环境。更合理的路径是让 Agent 在开发期探索需求、理解数据、规划任务并生成 SQL 或 PySpark，经测试、权限校验与人工确认后，再以可审查、可回滚的确定性产物进入生产执行。围绕这一原则，云器提出几项判断：把推理空间尽量留给持续变强的模型，把任务、状态和权限统一到 API 层，把 Trace、评测和知识沉到基础设施层。简而言之，模型负责解决复杂问题，基础设施负责保证系统可控上线。 腾讯 PCG 大数据平台部 Agent 工程负责人王思懿则从一个具体业务问题切入：“净销售额下降，要不要加大投放？”她指出，这个问题同时包含指标定义、比较范围、数据粒度和决策证据等多个层次。因此，Data Agent 必须先确认“算什么”，再判断“做什么”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1XXVTNKm9fDAPhJGXvwIVx6PdonlG66kYIXaUyibMAWjKsWheRE1OMibKEwkaOYx0zMkiakbe5CgwYPI9TdBOTvZDicJYNIlXiaeqTQ/640?wx_fmt=jpeg&from=appmsg)

腾讯 PCG 大数据平台部 Agent 工程负责人

王思懿

在她看来，Data Agent 的演进大致经历了三个阶段：MCP 解决数据和工具接入，Skill 解决分析方法复用，以及语义图谱解决共享业务口径如何统一维护、校验和追溯。因此，灯塔 AI 并不依赖模型自由猜测业务含义，而是将概念与真实表、字段、图卡和文档来源连接起来。除知识工程之外，灯塔 AI 同步搭建记忆工程体系，设计个人记忆、项目记忆、每日日志三类记忆载体，解决传统 AI 无状态、上下文易丢失、团队口径反复确认的问题。

行业趋势：Data Agent 从智能问数迈向数据生产与决策

从快手 Data Agent 的规模化实践，到云器科技的基础设施设计，再到腾讯灯塔 AI 的记忆与知识工程，以及快手电商和 A/B 实验平台的场景落地，五位嘉宾的分享完整呈现了 Data Agent 从能力建设到业务落地的演进路径。可以看到，Data Agent 正从“能回答问题”走向“能参与数据生产与决策”，从工具能力升级为可信、可协同的数据智能伙伴。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1XBaiauwcz7nm7H5MFjicX8j3FkVtPlJhn3WOianGft9uzpFibuTXgn0HytL77PTl3DMEcJkfEQoADRXGYqVhCMjbGYx1uDicpduVLo/640?wx_fmt=jpeg&from=appmsg)

五位嘉宾也形成了一组清晰共识：通用 Agent 难以直接满足数据生产对准确性、可解释性和合规性的要求；知识不是静态文档，而是 Data Agent 的核心资产，需要在真实使用中持续治理；准确性也不是一次评测能解决的问题，而是要在事前准入、事中诊断、事后洞察上形成闭环。同时企业级 Data Agent 并不追求完全全自动运行，人机协同是生产环境必备前提，AI 负责执行各类任务，人掌握业务判断、上线审批与最终决策权。

对外界而言，这场沙龙释放出的更重要信号是：Data Agent 正在从演示型产品，走向可规模化落地的企业基础能力。从智能问数，到智能生产，再到辅助决策，快手此次披露的并非单点能力，而是一套面向真实业务场景的 Data Agent 生产化路径。

张蕤认为，当这种新的工作方式在更多场景中规模化应用，岗位边界和组织协作也会随之变化：DE 与 DPM 的能力进一步融合，数据 FDE、PDE、全栈工程师等复合型角色开始涌现；一人能够承担更完整的任务，跨角色沟通成本随之减少。随着 Data Agent 持续深入生产与分析场景，企业数据能力也将加速从工具化走向生产化。

![](https://mmbiz.qpic.cn/mmbiz_jpg/1gVUsotpT1V6UjMdibbqtyibRhNrbcCwGiceTpbYnRJAgdYgUYsz6Zjo7rya89QWrsmL2ZribxKhlnfdDSkHcLfD4exzOKyk9Re9dtPPr7QGzXI/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1XuRmdr7vuKw6rlFtU7b494PAiboeTDlelq5kxmaAG7smR2Y10hickVIX2LaictHkGZmav6iaj2p4QXJoiasPAHT9wWaCWqOLFdII1k/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1X9sklVHtmYzDJamZheZ8ib2Cun3N7yXKbBfMma6ez5KibGfKEib8ialDmhLgu8C5YuZ4Fj6Qg67qoiaiaQvcuKBict50bu1zcViaR4gkQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1XObQAPyOpTCm1oXyRT8PuylBpCiafbib8jOHbyRiaWwwdS86icXMJiaxbN4W7RU0oxV3bHIAgrZmKE3393sYdpczViaJl1iasLia5rGPs/640?wx_fmt=jpeg&from=appmsg)

左右滑动查看更多

欢迎加入【快手技术沙龙第5期交流群】

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1WRtMiaG4t8OSHTg2aDf0uv22t0s2vZfGDphKIBajQdVlWIfWYJIDeSgH0lfIbSYIbndgA1Gu4NjLUVr4jzSUkbNcYjicUlqFbYU/640?wx_fmt=png&from=appmsg)

⬇️ 点击【阅读原文】，获取讲师PPT！

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