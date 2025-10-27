---
title: 字节图数据库架构论文入选数据库顶会SIGMOD 2024
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247508010&idx=1&sn=725cde183484561000bbbe255fa1203a&chksm=e9d36bc8dea4e2dea6166dd8bc0fb2e488bb84d19f097c46af3c3c4ab52d3dd496431e256707&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-07-03
fetch_date: 2025-10-06T17:44:03.312474
---

# 字节图数据库架构论文入选数据库顶会SIGMOD 2024

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgiafB0iasF5SHX1pZZUpTottLgkHyKXiaO5KTI2al0dzFMzacWHaF1lM4TYZgsErGtsd9zOybwAibL0A/0?wx_fmt=jpeg)

# 字节图数据库架构论文入选数据库顶会SIGMOD 2024

字节图数据库团队

字节跳动技术团队

论文链接：

https://dl.acm.org/doi/pdf/10.1145/3626246.3653373

ps：可复制到浏览器打开

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgiafB0iasF5SHX1pZZUpTottHPX66QZ6wB4tiaDggUkMBkbGaexDkicVA3Q6b9rU8gQibVwlvaUyqXvkg/640?wx_fmt=png&from=appmsg)

SIGMOD **（ACM Special Interest Group on Management Of Data）** 是数据库三大国际顶级学术会议之一，也是数据库领域影响力最大的顶级会议，中国计算机学会（CCF）推荐的A类国际学术会议，今年的 SIGMOD 于 6 月 9 日到 14 日在南美洲的智利举行。

每届会议集中展示了当前数据库研究的前沿方向、工业界的最新技术和各国的研发水平，吸引了全球顶级研究机构投稿。

其中来自字节跳动基础架构图团队的 《BG3: A Cost Effective and I/O Efficient Graph Database in ByteDance》论文被 SIGMOD2024 收录为 Industry Track 论文。

# 研究背景与动机

ByteGraph 是字节自研的支持万亿级图数据库，目前 ByteGraph 已部署超过 1000+ 集群，支持今日头条，抖音，西瓜视频，火山，广告，风控等全系产品。典型的工作负载归纳如下:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgiafB0iasF5SHX1pZZUpTottNMXyAJkynqUcuesnKWialwR3NcZO2hzY7UNI2twGFUv8uLJyYkkgS4w/640?wx_fmt=png&from=appmsg)

* OLAP工作负载主要应用于知识图谱和风控，读取比例日常为 100%，数据导入时下降到 60%，整体吞吐量为数万级，遍历跳数为 3 到 5，写入频率为周期性，性能关注点包括延迟和错误率。
* OLSP 工作负载适用于推荐、GNN 采样和特征服务，读取比例为 75% 至 90%，整体吞吐量为数亿级遍历跳数为 1 至 2，写入频率为实时，性能关注点包括吞吐量、延迟和错误率。
* OLTP 工作负载主要应用于电商和内容记录，读取比例为 90% 至 99.9%，整体吞吐量为数千万级，遍历跳数为1，写入频率也为实时，性能关注点包括吞吐量、延迟和失败率。

综合分析表明，ByteGraph 系统所承担的主要工作负载以读操作为核心，其发生的频次显著高于写操作。

尤其值得关注的是，图结构中最基本的读取操作是对邻接表的扫描，因此，对读取性能的持续优化，尤其是邻接表扫描的性能，显得至关重要。

尽管读操作占主导地位，写操作的重要性仍不容小觑，特别是在推荐场景中，ByteGraph 系统拥有海量的推荐场景集群，即使读取比例超过 75%，写入操作的规模也达到了千万级，这常常成为影响整个集群成本的关键因素。

下面我们将先从 ByteGraph 前一代 2.0 架构开始，介绍当前遇到的问题。ByteGraph 2.0 系统架构图1所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgiafB0iasF5SHX1pZZUpTott9rwjkEjDZOebtrnKqcUgHWjV4c6dAibyicQqLeN76ABUvzNr5DmmEWiag/640?wx_fmt=png&from=appmsg)

ByteGraph 2.0 架构整体划分为三个层次：BGE 层负责处理图查询请求，BGS 层负责缓存图的结构和属性数据，而分布式 KV 层则确保数据的持久化，三层可以各自独立扩展。

为了实现读写操作的均衡，ByteGraph 2.0 采用了 Edge Btree 来存储邻接表。通过在 KV 模型上构建 Btree（每个 Btree 的页面作为一个KV单元存储），ByteGraph 满足了业务的基本需求。

更深入的 2.0 架构细节可以在 ByteGraph 团队 VLDB 2022 的论文《ByteGraph: A High-Performance Distributed Graph Database in ByteDance》中找到。

然而随着业务规模的扩大，以及基于图的实时图分析技术在社交网络应用中落地，我们发现上一代 ByteGraph 架构在字节业务中遇到以下几大痛点：

1. 基于 LSM-based 的分布式 KV 构建系统，在字节图数据库的 Workload 下面存在一些劣势，主要体现为以下几个点

1. KV点查性能差：LSM-based 的 Key-Value 引擎，点查性能相比于 Btree 引擎不够稳定(无论 Compaction 策略采用 Level Compaction 还是 Size Tiered Compaction)，当 BGS 层出现 Cache Miss 时，读延迟不够稳定，而字节内很多场景，如抖音点赞等业务，Workload 都是读多写少，对读延迟有较高要求。
2. 写入放大高：采取 Btree On LSM 的架构，叠加了 Btree Page 写入放大（每次修改 Page 中的一行记录，都需要把 Page 写入 KV 系统）和 LSM 内部写放大（一般采用 Level Compaction ），最终总体写入放大较高。
3. 冗余的内存层次：分布式 KV 内部采用 RocksDB，当发生 Cache Miss 后，一份数据会同时在 BGS 和RocksDB 的 Block Cache 中缓存，造成了内存冗余，进一步导致了整体服务 TCO 上升。

2. 基于LSM的分布式KV底存储在做垃圾回收的过程中采用两种策略 (1) RocksDB 默认 KV 不分离，使用 Level Compaction 回收数据 ，(2) TerarkDB 使用 KV 分离策略，Value 部分采用传统的基于垃圾率的空间回收策略。以上两者无法针对 ByteGraph 业务上的冷热访问数据进行针对性的优化。
3. 随着字节电商，支付等业务的快速发展，越来越多的图计算，图神经网络在图数据上应用，这些应用要求更高的读扩展性，具体来说：当新数据写入ByteGraph 读写节点后，能在极短的时间内稳定的被只读节点读出。基于分布式 KV 的前一代 ByteGraph 实现的最终一致性，无法满足 Time-bounded 主从一致性的要求。
4. 在字节的社交、推荐和风控的图查询 Workload 中，会涉及到对点邻居的复杂的计算模式，包括对邻居打分排序，过滤等计算。在这类重计算的场景下，2.0 的行存储引擎、执行引擎对只需要分析部分边属性的扫描不友好，以及大批量边的计算在基于行计算引擎中存在较高的解释开销。

# 解决方案

为了解决上述四大痛点，我们开发了 ByteGraph 的新一代架构，命名为 ByteGraph 3.0（BG3）。

BG3 旨在从查询引擎到存储引擎全面更新，在查询引擎引入向量化计算、MPP、AQE 等技术，同时构建基于共享存储的图原生 Bw-tree 存储引擎，来实现性能、成本的大幅优化，本文将重点介绍图存储引擎部分。BG3 整体架构如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgiafB0iasF5SHX1pZZUpTottJWULL3jrkXXJY0dWfgNF4CxZeVNPHJJ8nJcickWxLcUL68xiaV12NEVg/640?wx_fmt=png&from=appmsg)

如图2所示，BG3 基于 Append-only 的共享云存储系统构建，在此之上我们构建了一个 Cloud Native Bw-tree 单机引擎，BG3 新架构的存储引擎主要有以下几大创新点：

1.Space Optimized Bw-Tree Forest

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgiafB0iasF5SHX1pZZUpTottOpLADK8oFQPibudHib9eNWfpPsnNuic0rqNJbKA2CcOorCicviczVOXym2Q/640?wx_fmt=png&from=appmsg)

如图 3 所示，我们以抖音用户点赞场景为例，用户每点赞一条视频，都会向 ByteGraph 插入一条用户到视频的边。

假设A用户是一个很活跃的用户，每天都会点赞大量的视频，而用户B和C相比之下每天只点赞少量的视频。

如果我们把所有用户都存储在一颗 Bw-tree 上，来自用户 A，B，C 的边有可能存储在同一个叶子节点上，这样由于A的点赞边的频繁插入叶子节点，会造成叶子节点的频繁分裂和 Bw-tree 的冲突，这些都会引起用户 B 和 C 没有必要的读写延迟。

为了减少 Bw-tree 上的冲突，最理想的情况我们为每一个用户的点赞边被写到一个独立的 Bw-tree 中，但我们发现图上存在明显的 Power-Law 现象，80%用户点赞频率有限（可能只有几十个赞），因为每个 Bw-tree 都有一些元数据的开销，如果每个用户都单独分配一颗Bw-tree会导致元数据的内存和磁盘开销过大。

因此我们提出了“Space Optimized Bw-tree Forest”，所有的用户点赞边会被首先写入一颗统一的 Bw-tree(INIT)中，当一个用户的点赞边数超过某个阈值，这个用户的数据会被分裂到单独的一个Bw-tree中（如图3右边的用户A）。

2.Read Optimized Bw-Tree

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgiafB0iasF5SHX1pZZUpTottAkGAicpc3ibiaJskXprG83OibwT2dnNnjvQwK0vicMdAQM6924VslxFdqOA/640?wx_fmt=png&from=appmsg)

Bw-tree 每次修改都会转换为一次 Delta page 的写入（如图 4 左上所示），这样设计的好处是写入很快并且写入放大低，但这种设计的缺点是读入时有可能需要从磁盘上从不同位置读取多个 Delta 才能获得 Base page 最新的镜像（如图 4 左下所示）。

字节内大量业务对 ByteGraph 的 Workload 都是写少读多，原始 Bw-tree 的写入特性对读性能有很大的影响，并且在存算分离的场景下会放大该问题，一次上层的 Cache Miss ，会造成大量下层的 IOPS 放大，多个Delta 导致的多次 IO 会导致读取延迟不稳定，对用户影响较大，并且在共享存储架构下这个问题会更加明显。

因此，BG3 提出了“Read Optimized Bw-tree”，如图 4 右边所示，我们在每次写入 Bw-tree 的时候，会把之前还未合并到Base page 的 Delta一并写入，这样设计的好处是当我们需要读取 Delta 获得 Page 最新的镜像时，我们可以只读一次 Delta 数据。

虽然这种方法和原始 Bw-tree 对比增加了额外的写入开销，但我们在字节真实的 Workload 测试后发现（论文中也有对应的评测），这部分写入开销可控的前提下大幅增加读性能。

3.Workload-Aware Space Reclamation

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgiafB0iasF5SHX1pZZUpTottKaAkcQVLF45Fz9LsfXibPvlicCINWHX4OVDFVf3dACSTFNPbUlQq1J4w/640?wx_fmt=png&from=appmsg)

为了持久化考虑，Bw-tree 的 Base page 和 Delta page 数据会被统一写入Append-only的云存储中。

传统的 Bw-tree 的空间回收会维护一个 Fifo 的队列，新数据插入队列头部，每次空间回收都会从队列的尾部开始扫描数据，把队列尾仍然有效的数据重新写入队列头，以达到回收已失效数据空间的目的。

传统 Bw-tree 的空间回收策略没有考虑不同数据段的空间回收率，后台的数据搬运产生了大量的写放大。

从空间回收的角度看，Base page 和 Delta page 的写入 Pattern 不同。我们借鉴了 Arkdb[1] 的设计，把 Base/Delta 分别写入不同 Stream，并把 Stream 内数据划分成相等大小 Extent的设计。与此同时，我们发现：

A. 以视频点赞场景为例，图数据的幂律分布特性使得视频的热度(喜欢，收藏，浏览)呈现出冷热差别。同一个视频，视频刚发布时的点赞数的增长率会远高于发布一个月后视频的点赞数增长率。点赞数增长程度的不同传导到下层存储体现为不同视频对应的 Bw-tree 上各个 Page 修改的频率相差甚远。这进一步造成了底层 Stream 中的 Extent 的空洞的变化率的不同。

B. 用户对于事物的偏好往往随着时间变化而变化，因此我们通常使用时间窗口来维护用户最近的浏览历史，搜索行为和视频口味偏好等等。这就要求 ByteGraph 支持过期数据删除的功能。这种基于 TTL 的过期删除行为，在下层Extent 存储时间到期后会产生批量删除。

基于上面两点观察，我们提出了“Workload aware space reclamation”。每一块 Extent 我们会有一个Extent usage tracking模块，我们会记录

1. LastTimestamp: 以 Extent中 最晚更新的一条数据的时间戳作为整个extent的时间戳。2. Fragmentation Rate. 我们通过记录 Extent 的有效 Page 数和无效 Page 数，从而计算出 Extent 的空洞率。3.Update Gradient。Extent 每次更新我们会记录更新时间以及当前 Extent 中 Invalid Page 的总数。

如图5所示，和传统垃圾回收策略只选择垃圾率最高的 Extent 回收不同，我们的策略会优先选择垃圾变化率 ( Update Gradient ) 最低（变化率最低意味着是冷数据，搬运的都是有效的数据，这样可以避免搬迁即将被删除的数据，这样对于全局是最优的）的 Extent 进行回收。

与此同时，当我们发现一个 Extent 设置了 TTL，在回收过程中我们会跳过这些 Extent，并在 TTL 到期后整体删除数据，这样可以避免因为垃圾回收产生的没必要的搬动。

4.I/O Efficient Synchronization Mechanism

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgiafB0iasF5SHX1pZZUpTottiaoXkeSGWyOwn1blOrsXITSrufD1tLAuZyRiaAkibw6iaibDxGvV7SMEmkg/640?wx_fmt=png&from=appmsg)

针对上一代 ByteGraph 的主从同步最终一致性的问题，ByteGraph 3.0 提出了 Write-Ahead Log based 的主从同步技术，同时为了节省成本，我们采取RW（读写节点）/ RO (只读节点) Share Storage 的架构，同时 RO 通过 Replay WAL 来更新其内存中的数据。

Share Storage 架构的问题：为了提高 RO 缓存效率，RO 节点会根据自己的 Workload 进行内存页(Bw-tree Page)的换入换出，然而如果不小心处理这里的细节，很容易导致 RO 节点上读到不一致的数据，例如 RW 随意 Flush Bw-tree的 Dirty Page，导致 RO 读到了未来版本 Page ，具体同步问题可以参考论文原文图6例子。

未来版本 Page 的问题本质是因为 RO Replay WAL 更新内存缓存的进度 始终落后于始终 RW 最新写入的 WAL，如果 RW 随意 Flush Bw-Tree Page，可能会导致 RO 看到的磁盘数据比内存更新。

其他系统解决方案：比如 Amazon Aurora / 火山引擎 VeDB 通过读取特定 LSN 的 Page 来解决这个问题（存储层提供多版本读取接口），Aliyun PolarDB 通过延迟 Page 的 Flush 流程，直到 RO 将相关的数据更新到内存中。不过这两种都对存储接口有一些特殊需求，工程实现较为复杂。

BG3 的解决方案：BG3 提出了Unified WAL Stream，通过维护数据的多个版本，并在日志流中写入RW节点的Flush/Update Bw-tree Page Mapping 的操作（称作后台系统日志），将前台用户 WAL 和后台系统日志写到统一的物理日志流里面，RO 节点按顺序回放，总是先回放内存的数据，再看到磁盘更新，避免上文提高 Future Page 的问题，与此同时，我们针对生产环境下高 I/O 吞吐做了针对性的并行优化。

通过这套设计，我们仅仅依赖一套通用的 Append Only Blob 存储就解决了 Share Storage 架构的问题，工程实现更加简洁，具体更多细节可以参考原论文。

5.Optimized Column-based Engine

上一代行引擎的性能问题：在字节的社交，推荐，风控等领域会存储用户之间关系和与这些关系相关的属性，业务会对这些属性进行较复杂的分析与计算。

如提取点赞关系中某些属性排名 TOPN 的用户的分析计算。使用行索引对这类分析型计算的列读取 SCAN 不友好，会显著增加访存开销。

另一方面，行执行引擎执行框架中的虚函数调用开销和解释开销较高，为了解决这一问题，我们在 3.0 中引入了列执行引擎，以提升执行效率。

然而，在实践过程中，由于在图查询中会经常涉及到对某些点的邻居边的各种分析查询，如社交分析场景中会涉及到对某个顶点的每一个二度邻居进行子查询分析，但是子查询的执行需要将所有的外层执行结果按行输入到子查询中，这会使得执行模式回退到了行执行。

并且，图上会存在不...