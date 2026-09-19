---
title: 【AI地图 Tech说】第十三期：地图道路数字员工——最懂路网数据的一站式agent平台
url: https://mp.weixin.qq.com/s/ghnqgQdjiVume_5ZcftT4A
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:59:08.848213
---

# 【AI地图 Tech说】第十三期：地图道路数字员工——最懂路网数据的一站式agent平台

# 【AI地图 Tech说】第十三期：地图道路数字员工——最懂路网数据的一站式agent平台

百度地图技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmecoa.qpic.cn/mmecoa_png/SQibncOx4ozNM1Tsknl9C6wTMeMws4A1AEYLau3w7t0Jz7vwwRXDXgktiaaibFdWxfYC0sopRZ9INfaoF1C11TmqBdibU7PyQBfSuGvvQUJHdVI/640?wx_fmt=png&from=appmsg)

PART1 地图路网数据：规模与复杂度的挑战

地图路网数据制作要素众多、生产流程长，应用策略复杂，对于地图数据问题的分析，同样也面临****上手门槛高****、****分析效率低****、****资料平台分散****等痛点。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozNAVZPfVrotkEEhd0ZA76njTNv47DAyh5vdn1ZXjV94xbhPkQgqgKgINEwsZia7e6xX9SKQ9Klt2NUn9WHlwjlxrSnjOpKBia8TQ/640?wx_fmt=png&from=appmsg)

数据、流程与策略的三重复杂性

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozPVV03ib1omDopC6H6F1Dl3Lpsdkv2HNVGjibsJ9NfmPIlS6fFFovHicsFvt9Eu856icajxvIFEBaq6qibQJDHFworNDKx6teIr7434/640?wx_fmt=png&from=appmsg)

### 数据分析&地图问题定位的关键挑战

在复杂的地图路网数据生产系统中，数据产品（工艺）和客户应答团队大量精力都消耗在地图数据的问题分析上，每月投入数百人天进行客户问题分析，但数据闭环的飞轮效率却十分低下。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozO0VGiaMWf6tia3qgFgloq9reDxJ8h8gjbujwHRKL3W1kbCDH9QT7iasZnUYPnah1EPIhbreRvg62mboh6uIS9to0kcKia5A8SicJhs/640?wx_fmt=png&from=appmsg)

****一个典型的地图用户问题分析 case****，需要经过六个关键步骤，跳转4-6个不同平台获取相关信息，单个问题分析30分钟-数小时。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozPssFO7cnj6o98tmKC7GB63GHiaNcupFViaMqvniaTQHW61s5BTAlFpU6dickkKYvIN76uZv8zP4XkYQNAuw7KNx1F55ns0ppeLr5Y/640?wx_fmt=png&from=appmsg)

PART2 为什么借助 Agent 能够解决：能力演进与方案选择

从 LLM 到智能体系统的演进历经四个阶段：

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozNn841JpOviblxkRptRnS2YVxPjVzh5CS6IVSj1PxxJibHoeQswXQKrpiaw6rMicqBf6On1YibejqPrqNXAiblFz4mkKzazalesxu6bs/640?wx_fmt=png&from=appmsg)

状态编排阶段具备的三项能力，与上述关键挑战逐项对应，这是该技术路线适用于本场景的前提：

![](https://mmecoa.qpic.cn/mmecoa_png/SQibncOx4ozMVcraibSRx8p6tg0y1xbbYF4nzr7vlib6lgem5qnAd19UqHrjyYl63LvhDyfboj7L09OEO1OduCbPx42z7RNQgpibIosbHVun4Cg/640?wx_fmt=png&from=appmsg)

三项能力叠加后，检索环节才具备自动化的条件。由此可确定方案的基本形态：****以模型承担语义理解与判断，以状态机承担流程控制，把各平台的查询能力封装为可复用的执行单元，人工只在高风险节点介入****。这是后文数字员工方案的设计起点。

与传统脚本相比，这一形态在流程驱动方式、逻辑结构与扩展方式上均有差异：

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozNE1zXJm0FwwibFxPLxYkYNTRTNgex08TI1ZiaXcu3ulUibsatF2dpHCm8wCFibSEhE7VyUFb2D7AVTGaxqZ6JulOxE1NyM8icQUZbo/640?wx_fmt=png&from=appmsg)

综合前述判断，方案采取规则引擎与大模型分工的形式：确定性环节由状态机与规则引擎执行，不确定性环节由大模型判断，使检索自动化覆盖数据链路全程。第二章将说明这一形态的具体设计。

![](https://mmecoa.qpic.cn/mmecoa_png/SQibncOx4ozO0h55bRWzicuJWAnxickXoZGhP9beh8HPXiatibEjWDZdXlOibDhD8VMAwfsaTa20ibX5P65VYSRCPGTV2eHcEnRMDwPNiciaeb5H6KfE/640?wx_fmt=png&from=appmsg)

****本章导读****：本章把设计与实现合并讲述。2.1 说明多 Agent 架构选型与 DE 基础 Skill 建设的整体思路；2.2、2.3 分别说明智能体角色划分与 Skill 体系；2.4 说明编排机制与人工介入；2.5 至 2.7 依次说明类层次与事件协议、运行时机制、服务链路与端到端呈现；2.8 说明设计边界、权衡与演进。

PART1 架构选型与设计总览

地图数据的检索与分析属于半结构化流程：整体步骤确定，细节存在歧义。系统据此采用多 Agent 分层架构，整体分为四层。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozO7mkRuTIibzbTMYcTAvm0U0A54cZOfPbDoIHW1gX7vicdKUxqXyrlG98FPdB85FNwsN6yVuVSVm5RbAFp0chtiaTib69zx4d3Dgts/640?wx_fmt=png&from=appmsg)

如上图所示，四层自上而下的分工如下：

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozOOEbtslzQTSaYIyGWQ93FGPAoP119yR6JC44ibBAxX6ic9LMicsiaQrYiagiciccSNoH4NE5y2txmmNUkpEsvXPxgrEsB7DsictFh1qHE/640?wx_fmt=png&from=appmsg)

****判断能力集中在上层、执行能力集中在下层****，是这套架构的基本分工。可靠性由状态机与事件链路保障：重试次数设上限，超限转人工；检查点持久化支持断点续跑；高风险操作执行前需人工确认，全过程留有记录。

PART2 智能体架构

系统包含 Planner、Reactor、ClarifyAgent、Summarizer、SkillExecutor 和 GeneralAnswer 六个角色，它们共享统一的 Agent 底座，职责划分如下：

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozNHCEHya7608UMgZw1MgnuLcb5pquMtEwMyKiagQ9cZ7ZVqiapmianyPPa9vRXYW9A1Kn8DIpbRia8sG4ZmuEE30GhLeoYeRIuoqiao/640?wx_fmt=png&from=appmsg)

六个角色构成****通用编排层****，承接任意任务。其上按业务场景固化了****场景化 SubAgent****（案例分析、全链路检索、鲲鹏垂类），承接特定场景的固定流程，与六个通用角色共用同一 BaseAgent 底座。

****责任划分****：判断与执行分属两侧——拆解、裁定、澄清、收尾均在智能体内完成；一切真实系统操作只能通过 Skill 执行者与 Skill 目录这一条通道进行，不经此通道无法访问数据。

PART2.1 角色设计要点

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozP64D3ibYkB5eWtWDD5BsjCUQ3jSCQgEpf2hYtwDKkYEkE6TgibibiapyuicopbRsU4RodDvGPEZj3qURt8ibv0ISugaPX1BibJAwvYKM/640?wx_fmt=png&from=appmsg)

****SkillExecutor 与 GeneralAnswer 构成执行侧****：前者是唯一执行真实操作的角色，中业、图灵、MIS 等平台均以 Skill 形式接入，平台间调用方式与数据格式的差异由说明书统一约定，执行模块只按 Skill 名与参数调度；后者处理无 Skill 覆盖的通用步骤，避免执行模块临时构造 Skill，也把规格咨询类问答隔离在作业流程之外。

PART2.2 BaseAgent 统一底座

六个角色是统一底座 BaseAgent 上的六个实现：统一的名称与描述、统一的输入输出、统一的钩子与日志。底座保证六个角色在工程语义上遵循同一套生命周期，这是调度可靠性的基础，也使后文的 Hook 机制可以一次定义、对全部角色生效。

PART3 Skill体系与能力调度

地图生产域中可固化的原子能力彼此独立：查询一次交限状态、换算一个图幅坐标、绘制一张底图。它们****输入输出确定、无需复杂推理****，因此各自实现为独立 Skill——可跨场景复用（交限查询既供冗余分析也供反馈核实）、可独立验证、修改互不影响。TTFA 编码位、图幅换算公式等专业知识写入 Skill 文档后，掌握规格细节的要求从智能体转移到 Skill 库，一定程度上缓解了专业门槛带来的上手成本。

PART3.1 Skill说明书与目录注册

每个 Skill 只有一个公开接口：一份说明书，正文为六段规范结构。

![](https://mmecoa.qpic.cn/mmecoa_png/SQibncOx4ozOGZUXMF7Xr0nsvn9qjQdcmjl1jnflO0h8OHVmQiaPzyTotLkwlV2b1XbyMZqr0fPSeyibSoGTyXr1uicgfbBJBJRUcfdPsibnTfQA/640?wx_fmt=png&from=appmsg)

六段内容覆盖调用方需要了解的三件事：用途、调用方式、失败处理，调用方不必通过试错发现隐含的参数要求与前置条件。所有说明书按业务领域分组存放在 Skill 目录下，系统启动时扫描目录树登记为内存清单——****目录即注册表****，新增一个 Skill 只需新写一份说明书放入目录，既不必修改中心化注册表，也不必核对清单与实际文件是否同步，配置漂移的风险大幅降低。

PART3.2 能力调度与任务闭环

系统以目录扫描结果生成一张****能力清单****，把每个 Skill 的名称、描述、调用规范与风险等级渲染为统一文本，注入 Planner（选择 Skill）、Reactor（判断是否属于已知失败情形）与 ClarifyAgent（生成受阻原因的提问上下文）。能力信息只维护一份，三个角色对 Skill 能力范围的理解因此一致。调用本身分两步完成：

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozOyZia8PTibjC0ecfvhDPgb9Pu0y6bZ8W7MOJkibwoiaUxOrnplBC0THS0KYM3GiaUMnr4t1h5m7eNYt6zN0C4htee95zHXtticrECbE/640?wx_fmt=png&from=appmsg)

任务整体按闭环推进：

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozM8kU4VSXafagAzpepx27qmMajoz6ZwYhWBiciahvJCaPbpOXhM3ffjeATkeI0DovHicwicXas1xdEvFJBKkULYicRI9WvjQbLqW96Y/640?wx_fmt=png&from=appmsg)

闭环是业务要求：交限工艺链中任何一步的证据都可能需要重新获取，状态可控回退是这类任务能自动执行完成的前提。它也使结论能落回生产环节——输出不停留在存在问题，还需说明证据来自哪一层、下一步应回到哪个平台处理。

PART3.3 分工边界

判断与执行的分工由四条边界界定：

![](https://mmecoa.qpic.cn/mmecoa_png/SQibncOx4ozPmiceo9viapz79J46t97qb0BpqlKYTHVSvDO9QUxfu3rkV0ibO6lBzickibEynoCTsOEV1hSaJQWic5T1XXz452gJyhJQibiaxmnNMicpY/640?wx_fmt=png&from=appmsg)

PART4 智能体编排与HITL

编排层承接判断与执行之间的调度。以下依次说明状态机的拓扑结构、状态字段的划分、防止执行失控的三层限制，以及两类人工介入的触发条件与挂起续跑机制。

PATR4.1 有限状态拓扑

Supervisor 将一次会话编排为一个****有限状态机****，七个节点、五条条件边：

![](https://mmecoa.qpic.cn/mmecoa_png/SQibncOx4ozOeKRuichia0z17CrNV4KfM4M3fkmIlsp4q4ibKSpePV6DibiaCyQFARb93vaicCMCdIj8uMlUf8nZlNcetwJGu1AQ7vxMyhokO7QJsA/640?wx_fmt=png&from=appmsg)

* ****planner****：调用规划者产出步骤；
* ****confirm\_gate****：对风险步骤先征求人工确认；
* ****execute\_step → rollback****：执行失败时，先小步重试，再考虑整段回滚；
* ****clarify****：被动澄清（信息不足向人求证）；****human\_interrupt****：主动打断（等待人工动作）；
* ****summarize****：汇总结论并交付，进入终态。

五条条件边的判定均依据 Reactor 的结论：重试（try）、重规划（re\_plan）、回滚（rollback）、继续（proceed）、终止（abort）。****节点数量少、判定集中****，使系统当前所处状态始终明确，且每一步的正确性由同一角色判定。

PART4.2 状态管理

状态机里的状态被限缩为两组：****四类暂存字段****（重试位置、待回滚步骤、待输出、待用户确认）与****核心调度字段****（当前步骤下标、结果列表、剩余回滚次数、当前步骤输入、历史步骤、可用工具清单）。

* ****可序列化是前置要求****：任何状态都必须能导出快照并重建。断点续传不是附加功能，而是状态设计的约束条件。

PATR4.3 超时、重试与递归上限

为防止失控，设计中设置了三层限制：

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozMYR0Qpia51o2clDdQ8ZMRg8Aq7ic4l766PfvdFGpgq0JAQu9VLHa5xKGJYZn8ADicxRGVicWazY4QhNDIHTb7gZoao89jI99py6dI/640?wx_fmt=png&from=appmsg)

实际语义是：系统在无法推进时停下并转交人工，而不是持续重试。这是对****可靠性优先于完成率****的直接落实。

PART4.4 clarify 与 confirm：两类人工介入

人工介入（HITL，即在关键节点引入人工判断的机制）设计成两种语义：

![](https://mmecoa.qpic.cn/mmecoa_png/SQibncOx4ozOg2U05gJoLViaSHjics4xQxfmnRsf61CPTUM9Flic0KDRwxAZqw0szmwcDj4oZmGFFsSe2qOTNCv2XDdCp5nkc28uaP00CXr1wPE/640?wx_fmt=png&from=appmsg)

****两者的区分是固定的****：主动确认发生在执行之前，由系统判断是否需要询问，确定性步骤不触发人工介入；被动澄清发生在无法继续推进时。地图场景下，修改交限属性默认走确认以管控风险，版本履历查不到走澄清以补全证据。

PART4.5 挂起与续跑

会话可能因人工介入或失败被挂起，因此断点续跑被作为****基础能力****设计：状态机的每个状态都可导出为检查点快照，恢复时通过重建执行状态与明确的恢复指令继续执行。业务价值较为直接：一次数据修改确认可能跨越数小时，用户返回时系统仍从确认位置继续，不重复执行前序步骤。

PART5 类层次、装配与事件协议

以下说明前述设计的工程实现骨架：三仓库的职责划分、多厂商模型的统一接入、智能体底座的实现方式，以及观测能力如何通过钩子与事件协议接入而不侵入业务逻辑。

PART5.1 仓库与包结构

系统在物理上落为三个各司其职的仓库：

![](https://mmecoa.qpic.cn/sz_mmecoa_png/SQibncOx4ozPJAmhYZIALlbAxaOUWCt2lY2fJgiaVPGjw2nmd1WgtnfBG9aq1uk82NZNibuibicF72bMl3HlBtR32k8Mianm8F7n44S6gFvic7s4nc/640?wx_fmt=png&from=appmsg)

三个仓库以统一的 HTTP 事件协议互连，各自独立部署与演进。引擎层的包结构直接对应设计意图，任何一个包可独立演进：

![](https://mmecoa.qpic.cn/mmecoa_png/SQibncOx4ozOx3Oiazia5hibWfeFw6YBsxw9zpLARRibicIgzWsAHCbAicdGBrPUibySVZFZboSmaWDibbuhJtJypH02AgylZj0gRnG1PD3jMLib3y6icc/640?wx_fmt=png&from=appmsg)

PART5.2 LLM工厂与模型抽象

多厂商接入的核心问...