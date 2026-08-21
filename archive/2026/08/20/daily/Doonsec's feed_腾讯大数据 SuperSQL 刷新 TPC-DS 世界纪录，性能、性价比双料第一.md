---
title: 腾讯大数据 SuperSQL 刷新 TPC-DS 世界纪录，性能、性价比双料第一
url: https://mp.weixin.qq.com/s/hgTWRQHc-w5mjDhYlFXlVQ
source: Doonsec's feed
date: 2026-08-20
fetch_date: 2026-08-21T03:00:00.763103
---

# 腾讯大数据 SuperSQL 刷新 TPC-DS 世界纪录，性能、性价比双料第一

# 腾讯大数据 SuperSQL 刷新 TPC-DS 世界纪录，性能、性价比双料第一

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

# 作者：腾讯数据计算平台

> 近日，国际事务处理性能委员会（TPC）官网正式上线天穹 SuperSQL TPC-DS 成绩，天穹 SuperSQL 通过严苛的 TPC-DS 全流程测试，综合性能成绩达 6.54 亿，是此前最高纪录的近 10 倍；单位性能成本降至 11.04 元，仅为此前的约六分之一，成为 TPC-DS 100TB 官方榜单上全球性能、性价比双双领先的大数据计算平台。

**![图片](http://mmecoa.qpic.cn/sz_mmecoa_png/ny7gib3BrpORK6VAuotN3QviaOicvoxtjuDVkbZ76LKsIhnNKhabVZxssrRebvZegQ8Ik1aJUrSG3GyG1QnfSxbnZcXvOOOCjahskwpozdicibC0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=1)**

# TPC 官方榜单截图

近日，国际事务处理性能委员会（TPC）官网正式上线天穹 SuperSQL TPC-DS 成绩，天穹 SuperSQL 通过严苛的 TPC-DS 全流程测试，综合性能成绩达 6.54 亿，是此前最高纪录的近 10 倍；单位性能成本降至 11.04 元，仅为此前的约六分之一，成为 TPC-DS 100TB 官方榜单上全球性能、性价比双双领先的大数据计算平台。

当企业数据规模从 TB 级迈向 PB 级，传统数据库与大数据架构正面临多重挑战：复杂查询能否稳定完成？计算资源能否高效利用？系统性能能否随集群规模持续扩展？要回答这些问题，仅靠实验室中的单点性能测试远远不够，还需要一套覆盖数据加载、复杂查询、并发吞吐与数据维护的系统化评估体系。TPC-DS 正是数据分析领域公认的权威基准测试之一。

## TPC-DS：数据分析领域的“试金石”

TPC（Transaction Processing Performance Council，事务处理性能委员会）是国际权威的非营利性基准测试组织，其成员涵盖全球主流软硬件、数据库与云计算厂商。与常规性能测试不同，TPC 测试对软硬件配置、测试流程、执行结果和成本信息均有严格规范，正式结果还需经过独立审计，因而具备较高的可复核性和横向比较价值。

TPC-DS 是全球数据分析领域最具代表性的性能测试之一，主要衡量一套系统处理海量、复杂数据任务的综合能力。过去多年，Oracle、IBM、Databricks 等海外技术厂商均曾参与 TPC 相关测试，其中 100TB 也是 TPC-DS 目前设置的最大测试规模之一。

天穹 SuperSQL 此次挑战的 100TB，约等于一个大型电商平台连续数年的交易、退货、库存、订单明细全部打包在一起。系统要在这座“数据山”上完成从数据导入到复杂分析、数据更新的完整流程，而不是只跑某一个专项。难度还在于任务的复杂和并发：系统不仅要连续完成 99 类不同的分析任务，并在 4 组任务同时运行时一轮处理 396 次复杂查询，还要同步应对数据的持续插入和更新，整个测试更接近企业真实运行时的高负载状态。

最终得分也不是看某一次跑得多快。TPC-DS 会综合单任务处理速度、并发吞吐、数据维护等多个环节计算总分，并同时计算获得这些性能所需的成本。

此次打榜选择 100TB 这一超大规模量级，标志着测试难度呈指数级跃升，主要挑战包括：

* **数据规模庞大**

  ：数千亿乃至更大规模的数据关联，对计算、存储、网络和内存管理形成全链路压力。
* **数据分布复杂**

  ：TPC-DS 包含大量非均匀分布场景，轻微的数据倾斜在大规模集群中也可能被放大为明显的“长尾效应”。
* **测试链路完整**

  ：除查询性能外，还综合考察数据加载、并发吞吐和数据维护等能力，是对系统工程能力的全面检验。
* **结果严格审计**

  ：测试配置、执行过程、性能与成本数据均需满足规范并接受审核，对系统产品化和工程规范提出更高要求。

即便如此，天穹 SuperSQL 依然凭借扎实的技术底座和持续的引擎优化，交出了一份令人瞩目的成绩单。

从具体测试环节来看，天穹 SuperSQL 在数据写入、查询处理与数据更新三大关键环节上均实现了大幅提速：

* **数据写入：耗时 449.4 秒，较此前纪录的 3427.1 秒快 7.6 倍；**
* **串行查询：耗时 177.5 秒，提速达 16.5 倍；**
* **并行查询：两次合计耗时 898.8 秒，仍快 11.7 倍；**
* **数据更新：两次合计耗时 196.9 秒，快 6.7 倍。**

四大核心环节全面领先，在如此高强度、高标准的测试考验下取得这样的成绩殊为不易，充分印证了天穹 SuperSQL 在超大规模数据场景下的综合处理能力，也为这份亮眼的综合成绩背后提供了最直接、最有力的性能支撑。

![图片](http://mmecoa.qpic.cn/sz_mmecoa_png/ny7gib3BrpOQRKHTX0bwcHVcLAA5j5uYjHTFWu7MK92nrbmiaqdEk6dTz24D43icaYX7yoQdy3hhPYajSb84FgP8rWlAnbAFMyJWXDQftAbPibs/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=2)

## 天穹 SuperSQL：腾讯下一代大数据自适应计算平台

天穹 SuperSQL 是腾讯自研的下一代大数据自适应计算平台，依托自研通用向量化计算底座 TEngine，统一了流批引擎的计算执行层，原生支持 CPU 与 GPU 异构计算能力，并融合 SQL、Python 混合计算与多模检索能力，为结构化、半结构化及非结构化数据提供统一的计算与分析底座，并已在腾讯内部多个业务中稳定运行多年。

天穹 SuperSQL 采用“乐高式”的模块化技术架构，具备以下核心能力：

* **查询优化器：构建全局视角下的优化能力，实现“一次优化，多模式通用”，显著提升不同计算场景下的执行效率。**
* **分布式调度：灵活支持多种分布式计算范式，具备强大的异构资源调度能力，能够适应复杂多变的计算负载。**
* **通用计算底座：构建统一执行层，实现“底层一次优化，上层多引擎受益”的高效迭代模式。**
* **异构计算加速：原生支持 CPU 与 GPU 协同计算，突破单一硬件架构的算力瓶颈，充分释放算力潜能。**

* ![图片](http://mmecoa.qpic.cn/sz_mmecoa_png/ny7gib3BrpOTITlpBcTibmBsSWcH3u6MFRRabBJ4zaO6DkQzWicSibBdspU6icvtNHyt9POaviaPA7qK330Lh4t9BdTYjxWrnG3ZkXjXxrflK5c9Y/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=3)

## 硬核揭秘一：复杂负载下的查询优化

在业界主流数据库系统中，查询优化通常遵循基于规则的优化（RBO）与基于代价的优化（CBO）相结合的标准范式。RBO 偏向语义层面的确定性改写，解决的是局部结构优化问题；而 CBO 则关注全局搜索与资源权衡，基于统计信息和代价模型，在复杂算子组合空间内搜索代价最低的全局最优解。但面对复杂多变的真实业务负载，仍存在很大局限：

* **局限一：复杂 SQL 中可能存在大量语义相同的重复计算，但它们分散在不同子查询或算子分支中，难以被传统的局部优化规则发现。**
* **局限二：Runtime Filter 这类执行期动态优化机制的收益与开销往往未被完整纳入代价模型，难以参与全局执行计划决策。**
* **局限三：统计信息还可能因为数据倾斜、列间相关性、复杂表达式以及更新不及时而产生偏差，并在多层算子之间不断累积。**

### 1. AutoCTE：从局部算子优化扩展到全局计算复用

在复杂报表、嵌套子查询以及自动生成的 SQL 中，相同或高度相似的扫描、过滤、连接和聚合逻辑经常出现在多个查询分支中。现有优化器的优化范围往往受限于显式语法边界，缺乏从不同子查询和算子分支中自动发现复杂公共子计划的能力。AutoCTE 通过自动识别查询计划中的重复算子子树，综合比较重复执行与公共结果物化、读取和复用的成本，选择真正具有收益的公共子计划进行抽取和复用，在不要求用户手工改写 SQL 的情况下减少冗余计算。

![图片](http://mmecoa.qpic.cn/mmecoa_png/ny7gib3BrpOTmUQma6InKMnFImSYPPwNk9S5HoymoNztjH9NYjwumSkSFTicJQX1TG55mw0YWTIPKv6mO4Q7SkBTCWyzHUB2OlS8PF8TaXGcw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=4)

### 2. Runtime Filter 代价建模：将动态过滤的成本与收益纳入全局计划决策

Runtime Filter 通常由 Join 的构建端在执行过程中生成，并下推到探测端或数据扫描端，以提前过滤不可能参与连接的数据。它的收益不仅取决于过滤选择率，还受到构建端数据规模、过滤器大小以及数据分布方式等多种因素影响，而过滤器的构建、序列化、传输和探测本身也会消耗 CPU、内存和网络资源。SuperSQL 将过滤收益及其生成、传输和应用成本统一纳入代价模型，使优化器能够比较启用或不启用 Runtime Filter 时的端到端执行成本，打通优化器与执行层之间的信息壁垒，做出更加符合真实执行过程的计划选择。

![图片](http://mmecoa.qpic.cn/mmecoa_png/ny7gib3BrpOSEzQJxiaEUP9KBkNOKicdJG1OBq11Lhicvs7cbgpeedfiaLJK3lfCD1JK32eJkjibfSj7dwKSnnyzIuJmpb5ycRnMZ9XyAMKVZM5oE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=5)

### 3. HBO 与 AQE：利用真实执行信息修正静态估算误差

静态统计信息难以准确描述多列相关性、复杂谓词、数据倾斜和中间结果分布，估算误差还会沿多层算子逐级传播，一次错误的 Join 顺序或数据重分布决策可能进一步引发大规模 Shuffle、数据膨胀和长尾任务。HBO（History-Based Optimization）利用历史执行中产生的真实基数、选择率和资源消耗信息，为后续相似查询提供更贴近实际负载的优化依据；AQE（Adaptive Query Execution）则在查询执行过程中持续采集真实运行信息，自适应调整后续执行策略。针对 MPP 数据库缺少天然 Stage 边界的问题，SuperSQL 以阻塞算子形成的 Pipeline Breaker 作为运行时观测与调整边界，对下游数据重分区、执行并行度等进行局部自适应调整。

![图片](http://mmecoa.qpic.cn/mmecoa_png/ny7gib3BrpOTH21VqldWLvGUCg4bLYuoOUea9AkL52FMNSMzsExO9okVgsiayopg0sia2FRDtKKqQibdiaHkic2AJsTTHEaChHQeakfPe1XRXnQvE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=6)

通过上述机制的协同，SuperSQL 形成了“识别重复计算—感知执行代价—运行时动态纠偏”的完整优化链路，在复杂且持续变化的真实业务负载中生成更加高效、稳定和鲁棒的分布式执行计划。

![图片](http://mmecoa.qpic.cn/sz_mmecoa_png/ny7gib3BrpOQBc9NuFsS8ic28mv03NcjN0EvaDOrVzht7wicblgrH96ZOVJomt4ClPicujpNSCHTqYRT4TqcibI6PPu0Aic5wvz2GicoVp4YqGYVek/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=7)

## 硬核揭秘二：自研通用向量化计算底座 TEngine

TPC-DS@100TB 测试集不仅是数据量的巅峰，更是对分布式系统架构极限的“压力测试”。在数千核心的大规模集群中，传统的 MPP 架构面临着三大世界级难题：

* **网络通信风暴：海量节点间的数据交互极易引发带宽拥塞与传输抖动。**
* **计算流水线停顿：算子执行过程中的等待与阻塞，导致 CPU 算力无法被持续释放。**
* **集群长尾效应：个别慢节点或慢任务拖累整体执行进度，制约系统扩展性。**

天穹 SuperSQL 团队针对超大规模场景进行了全链路自研，通过软硬结合与极致算法，成功实现了从“线性扩展”到“超线性性能”的跨越。

### 1. 自研全新向量化执行引擎，让 CPU 算力拉满

随着硬件迭代，计算瓶颈持续上移，大数据计算也经历了从面向数据 I/O 吞吐到计算吞吐的重心转移。向量化技术通过重构数据布局与计算算法，深度贴合现代 CPU 体系结构，极大降低 CPU 流水线停顿，成为当代大数据 Native 执行引擎的标配。但依赖编译期静态优化已陷入边际效益递减的瓶颈，执行引擎必须具备感知运行时负载的自适应优化能力。为此 TEngine 打造两大核心能力：

* **感知数据特征的自适应编码计算：借助算子管线中天然的 Blocking 停顿点（如 Grouping、Join、Sort、Window 等物化节点），运行时动态积累数据特征，自适应 Dict、Delta、RLE 等编码对中间数据进行动态压缩与内存布局重构。**
* **自适应 Micro-adaptive 能力：Grouping、Join、DFP、表达式计算等核心算子，突破固定算子逻辑静态局限，将自适应调优的粒度下沉至算子与向量化 Batch，在查询执行过程中实时捕获数据变化，动态选择优化执行路径。**

* ![图片](http://mmecoa.qpic.cn/sz_mmecoa_png/ny7gib3BrpORvFREJBxnSvia54X5CWT7lhUKQOaa0FUKm9gjOPNmsvFXcTEX4ACvqmkA0pDialibeia36dHNhpuicM5mqXTxPEPhZ8JWWKH7frfY8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=8)

### 2. 统一内存管理器，不浪费一个 Byte

高效、稳定的内存管理是计算引擎的基石，尤其在面对 100TB 级复杂查询时，传统内存分配器在处理高频申请、碎片化及生命周期管理上显得力不从心。TEngine 自研了一套统一内存管理器，对内存资源进行全链路精细化管理，包括按核分区、分级单调缓冲、树状仲裁、按查询生命周期回收：

* **定制化内存分配器：面向高频并发申请进行优化，统一管理不同规格的内存对象，降低碎片率、实现统一地址空间，也为内存计算数据 Spill 到磁盘奠定基础。**
* **内存用量管理与仲裁：引入树状资源跟踪机制，支持细粒度的内存 Quota 管理；面临内存压力时，通过智能仲裁策略精准控制查询的取消或降级，在资源利用率与稳定性之间取得平衡。**
* **全生命周期管控：无论任务正常结束还是异常取消，相关内存均可被确定性回收，降低隐式释放与内存泄漏风险。**

* ![图片](http://mmecoa.qpic.cn/mmecoa_png/ny7gib3BrpOROsY6dIsZzOttH2MBx6TXduTGWS7IOiaicjUHGcicfU8RlGxficf7LHibIrehldFLKDUMz9F4iaXR5hEWge7TnsohTKqIhyiaicXUvUKY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=9)

### 3. 提升并行计算能力，突破集群规模上限

随着集群规模与数据规模的双重增长，业界主流 Shuffle 实现的固定点对点分区模型在扩容时连接数暴增、数据分布碎片化；海量小包穿透 TCP/IP 协议栈也带来大量上下文切换与系统态开销。为此，TEngine 从并发分区模型和底层网络软硬协同两方面对 Shuffle 架构进行了全方位优化：

* **自适应 Shuffle 并发分区模型：感知集群并发规模，自适应调节分区并发规模，小规模下数据分区直接到任务级别，大规模集群下结合节点到任务两层分区，极大扩展了 MPP 并发规模上限。**
* **自研 vRDMA 软硬协同 Shuffle：Shuffle 数据面构建在银杉智能网卡 vRDMA 之上，全程内核旁路、零拷贝，硬件 RTO/SACK 重传确认与自研拥塞控制算法保障传输可靠，逐包喷洒多条等价路径充分激活冗余带宽，且完全兼容标准 Verbs，应用零改造即可接入。**
* **RDMA 下执行策略重规划：vRDMA 的内核旁路与零拷贝使“网络是慢资源”的传统前提失效，TEngine 据此对 Shuffle 相关策略（如预聚合、序列化压缩等）的生效边界进行在线探测与自适应调整，使硬件红利真正释放到计算链路。**

* ![图片](http://mmecoa.qpic.cn/sz_mmecoa_png/ny7gib3BrpORHKP20CkvUZEbpY8P3peLpcgdQJ7eEWODQblricZtfVYOMI139xuicK2uCXJahvzicqqUNKTHSRbNYXJlWvCjbRWQ1E3mTooD0yk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=10)

## 硬核揭秘三：大模型驱动的智能诊断

极致性能不仅依赖查询优化器与执行引擎的持续演进，也离不开高效的...