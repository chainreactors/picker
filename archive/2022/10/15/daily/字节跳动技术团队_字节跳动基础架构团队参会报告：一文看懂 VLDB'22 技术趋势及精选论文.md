---
title: 字节跳动基础架构团队参会报告：一文看懂 VLDB'22 技术趋势及精选论文
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499493&idx=1&sn=ad5f6c819fed3e88160c0297f7207589&chksm=e9d33507dea4bc1150200a92cb552d408d40181e9d95934c7260d7550f8cf5333069f62cc362&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2022-10-15
fetch_date: 2025-10-03T19:57:46.517121
---

# 字节跳动基础架构团队参会报告：一文看懂 VLDB'22 技术趋势及精选论文

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOhhEeGjcLRMmXyq63h2eColiclvH0fE3bUice1UicrDfvoKSEn2pxHlkSsY9nTM0SkE4ZycR7ib6kYXDw/0?wx_fmt=jpeg)

# 字节跳动基础架构团队参会报告：一文看懂 VLDB'22 技术趋势及精选论文

基础架构团队

字节跳动技术团队

#

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

# 1. 前言

VLDB 会议，全称 International Conference on Very Large Data Bases，是全球数据库系统领域最负盛名的三大顶会之一。从 1975 年开始举办，每年一次，全球各地顶尖高校的大量研究者、各大高科技公司都会将自己的学术研究进展或工业界成果以论文形式投递到 VLDB 组委会，而组委会会审阅并接收其中最前沿、最具影响力的一批，并召开线下会议，供论文作者们分享、交流。

今年的 VLDB 在 9 月 5 日到 9 日，在澳大利亚悉尼举办。作为在全球有广泛用户和海量数据挑战的字节跳动公司，有三篇论文被 VLDB 接收：其中两篇来自 Graph 团队 ，一篇 ByteHTAP 系统，应 VLDB 组委会邀请，字节相关团队来到了正值早春的悉尼，与来自世界各地的数据领域专家学者，分享交流，共襄盛举。

为了让大家能对 VLDB 2022 有个快速的了解，我们总结了 VLDB 的论文分类、研究趋势以及工业界重点论文的摘要，当然啦，也包括字节跳动三篇论文简介。本文抛砖引玉，如果想深入了解学习，还是非常建议找到论文原文来仔细研究一番。

# 2. 论文分类概览

今年的 VLDB 会议日程中，将所有参会讨论的论文共划分成了以下几类：

* Database Engines(45篇)

* Database Performance(10篇)

* Distributed Database Systems(11篇)

* Novel DB Architectures(10篇)

* Specialized and Domain-Specific Data Management(20篇)

* Machine Learning, AI and Databases(50篇)

* Data Mining and Analytics(35篇)

* Information Integration and Data Quality(20篇)

* Data Privacy and Security(15篇)

* Graphs(45篇)

作为老牌系统会议，VLDB 既有传统的数据库管理系统的最新进展 80 篇左右，也有一些这些年来前沿的机器学习和系统结合领域的最新内容。此外，Graph 领域的论文依然收录了 45 篇之多，VLDB 延续这几年对 Graph 的重点关注。可以看出，VLDB 所收录的论文内容，从传统的数据库底层技术、性能分析，到机器学习、图、区块链这些新兴的数据库使用场景，再到最上层的数据隐私安全、数据分析，基本覆盖了数据的完整处理链路。

我们将不同领域的论文数量绘制成了饼状图，方便读者对不同领域的热度有大致了解：

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColuzqvicX1F7EVvdOKT7Xz5rgb5j3mWib9qibbe0F4sbDLSwHGTSlk8LrSQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColB0Kzmp31icWlnf7yPKJBgPJa6Jkrty3aKo2woZmY9urBEK3LB7nJ08g/640?wx_fmt=png)

VLDB 历来重视学术界与工业界的融合和交流。因此，VLDB 专门将工业界论文和学术界论文进行了分类，分别是 research track paper 和 industrial track paper。工业界论文 industrial track 共有 22 篇，其中校企合作的论文 12 篇，企业独立发表的论文有 10 篇；这些论文中，包含了 Google、Meta、微软、字节跳动、阿里、腾讯等多家国内外知名互联网企业的成果。相比于 research track，industrial track 更偏向于已经落地实用的技术或者系统，这些成果中有相当一部分与大家在日常生活中所用到的应用息息相关，也是各大技术公司相关领域人员关注的重点。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColqtUSowabicxQIibcZBqDUfTb0smYcrjYArl2n6iado2bwA61aagAdAguQ/640?wx_fmt=png)

# 3. 2022 的趋势和启迪

从论文的分布领域，以及工业界论文的重点，我们能够分析和洞察出数据库业界的一些趋势，一家之言，欢迎大家交流讨论。

## 3.1 机器学习与数据库的结合在不断加深

机器学习是目前计算机学界最为热门的话题，这种热度自然也传导到了数据库领域。今年 VLDB 最为火爆的话题就是 Machine Learning, AI and Databases，收录了足足 50 篇论文，且 Best Regular Research Paper 、Best Scalable Data Science Paper 均花落这个领域，在悉尼的现场中，听众人数最多的也是这个方向，挤满了整个屋子。

具体来说，机器学习与数据库的结合点又主要包含三个部分：机器学习框架和平台与数据库的深度融合、使用机器学习技术优化数据库性能以及自动化运维。其中，使用机器学习来优化数据库系统进而整个 infrastructure 系统是一个在工业界已经徐徐展开的方向，有显著的线上需求和收益，字节在这一方面也有团队在持续研究探索。

## 3.2 新硬件，软硬一体

在传统的 CPU、内存硬件的处理性能无法保持高速提升的大背景下，各大公司和学术界不约而同地将目光投向新硬件领域，包括 FPGA、GPU、PMem 等。如果充分利用 FPGA、GPU 进行计算加速，以及如何充分发挥 PMem 相比于内存的优势，是未知领域探索的低垂果实，自然成了近年研究的热点。本届 VLDB， 有多篇工业界论文专题研究 FPGA 和 PMem，并且 SAP HANA 的 FPGA 加速论文荣获了此次工业界 best paper 的桂冠；学术界也有至少五篇论文讨论 GPU、PMem 的相关话题，热度可见一斑。

## 3.3 NoSQL 领域持续发展

过去十几年，随着互联网业务快速增长，丰富的业务场景和数据规模的爆炸增长，催生了 NoSQL 领域的蓬勃发展。对于涌现的各种 NoSQL 产品种类，都持续有新的技术思路体现在每年的 VLDB 中。在 2022 年的 VLDB，NoSQL 领域有工业界贡献的时空数据库、向量数据库和图数据库，也有关于 LSM 引擎的架构优化论文，继续保持了 NoSQL 欣欣向荣百花齐放的态势。

## 3.4 Graph 保持高热度

在数据爆炸时代，数据关联性的价值逐渐突显，学术界 Graph 早已火热多年。今年 VLDB 一共有 9 个 Graph Sessions，占到了整体比例的 20%，在论文数量上 Graphs 有 45 篇， 仅次于 Machine Learning, AI and Databases，与传统的 Database Engines 打平。在这 9 个 Graph Sessions 中，被接收的论文方向覆盖了：时序图（系统与算法），动态图（系统与算法），概率图（算法），图查询优化，Graph AI (系统与应用），子图匹配（算法优化与应用），图数据库系统，图计算系统等方向。不难看出，对图算法的研究远多于图系统，且图算法相关论文几乎都是各大学的独立研究成果。作为学术论文，创新性是最重要的，从算法角度探索新方法新问题，会比系统角度取得创新性周期更短依赖条件更少，因此高校偏爱算法也就不难理解了。其实，在我们来看，场景、算法、系统是三个密切联动的环节，需要互相促进来实现螺旋上升。因此，图领域需要加强工业界和学术界的进一步交流合作。

# 4. 字节跳动论文介绍

字节今年共有三篇论文被收录，其中两篇关于图数据库 ByteGraph 以及 ByteGNN，一篇介绍了 ByteHTAP 系统，相信读者从名字就能看出论文介绍的系统类型。这些系统都广泛应用于字节业务丰富的业务场景，在实践中沉淀打磨推陈出新，相比有更强的实际参考意义，在悉尼现场，也吸引了大量研究人员关注和交流。

我们在此，对这三篇论文做简要介绍，也非常欢迎大家找来原文阅读。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColhiciaUn1EbN7sbTySwtlr8vEMBrEUibFVX5XIFMnJHYPbGM9mibJB7HImw/640?wx_fmt=png)

## 4.1 ByteGraph: A High Performance Distributed Graph Database in ByteDance

论文链接：https://www.vldb.org/pvldb/vol15/p3306-li.pdf

本文介绍了在字节跳动内部广泛使用的图数据库系统 ByteGraph。在字节跳动内部，用户、视频、评论/点赞、商品等等多种类型元素及其之间联系可以用 Graph 模型来完美表达；这些图状数据上，有出度几亿的超级节点的存储查询挑战，也有 TP、AP 甚至大量 Serving 流量的混合挑战，ByteGraph 在多年支持这些场景中不断演进和迭代，本篇论文就详细介绍了 ByteGraph 的整体架构和设计，以及多年沉淀的一些场景问题及其方法探索。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColrg1MNric2SugyJnZbDppNSTs3VUNqkBrE8TZJicCd5zyX0aNsjBLcu4w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColnDVAIYrhcDKlH85KbrGumibo0nhbbhicKianYnWoTHm8Yibt9jYicSYusyQ/640?wx_fmt=png)

表2 - 字节内部 Graph OLTP/OLAP/OLSP workloads 特点总结

ByteGraph 采用了计算存储分离的架构，支持 gremlin 分布式查询，可分层水平扩展到几百个节点规模。面向字节内部广泛存在的超级顶点问题、查询 workload 多样且经常变化的问题，采用了 EdgeTree 存储结构、自适应 Graph 索引等针对性设计，并对工程实践做了大量优化以提高并发性能。目前 ByteGraph 在内部已有数百个集群、上万台机器的部署规模，是全球最大部署规模的图数据库之一。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColPmPc18wynPFHzHaibW8KP1k8XUpS0icJdicXrxIxY1sAeKDPtQC6r77KQ/640?wx_fmt=png)

图2 - ByteGraph 系统架构图

在查询层，ByteGraph 自研了 Gremlin 的查询引擎，支持了常见的 Gremlin step 并针对字节业务做了不少扩展。在海量的数据与并发的打磨下，做了基于 RBO/CBO 策略的查询优化以及列式数据格式等执行优化。但坦率讲，相比关系型数据库经过几十年里无数工程师和研究人员的努力建设，图数据库理论和实践都还有很多的路要走，也希望在未来能有机会 ByteGraph 能够继续通过顶会论文的方式作出自己的贡献，和大家交流学习。

图数据库的内存组织结构非常关键，不仅需要表达 Graph 的数据模型还需要支持高吞吐低延迟的访问性能。如图 4 所示，ByteGraph 分别使用 Vertex Storage 和 Edge Storage 在内存中缓存顶点和边。每个顶点及其属性都存储为 KV 对，其中键由唯一的 ID 和顶点类型编码，值是顶点的属性列表。为了有效地执行图遍历查询，边被组织为邻接表。为了减少在图遍历中访问超顶点后产生大量中间结果的可能性，邻接表根据边类型和方向进一步划分。为了处理超顶点和频繁更新，减少边的插入带来的写入放大以及在整个列表扫描期间产生更少的磁盘 I/O。每个邻接表都存储为一个树结构，称为 edge-tree。edge-tree 由三种类型的节点组成，即 Root node、meta node 和 edge node，每一种节点都存储为 KV 对。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColBia4ZOOggJB8E9xJzCukCzM1oVGJd6OjFqDqFVIRKRGYoKIPia16YJ7g/640?wx_fmt=png)

关于 ByteGraph 更多细节，欢迎大家查阅论文或者联系 ByteGraph 团队同学交流讨论。

## 4.2 ByteGNN : Efficient Graph Neural Network Training at Large Scale

论文链接：https://www.vldb.org/pvldb/vol15/p1228-zheng.pdf

Graph AI 方向是近几年大热的一个系统方向，比如上届 OSDI 会议连续有 4 篇GNN 相关的论文被发表，SOSP/EuroSys/ATC/MLSys 每年也有很多有关于如何高效设计 GNN 训练/推理系统的文章被接收。今年 VLDB 上有关于 GNN 系统设计，优化以及应用的文章也不少。

图神经网络（GNN）作为新兴的机器学习方法，广泛应用于字节的推荐、搜索、广告、风控等业务场景中。面对字节海量的数据，采用分布式 GNN 系统提升训练的可扩展性和训练效率变得至关重要。然而，现有的分布式 GNN 训练系统存在各种性能问题，包括网络通信成本高、CPU 利用率低和端到端性能差。ByteGNN 通过三个关键设计解决了现有分布式 GNN 系统的局限性：

（1）将 mini-batch based 图采样的逻辑抽象成计算图以支持并发处理。

（2）粗粒度和细粒度的调度策略以提高资源利用率并减少端到端 GNN 训练时间。

（3） 为 GNN workloads 量身定制的图分区算法。

实验表明，ByteGNN 的性能优于最先进的分布式 GNN 系统（i.e., DistDGL, Euler, GraphLearn）,端到端执行速度提高了 3.5-23.8 倍，CPU 利用率提高了 2-6 倍，网络通信成本降低了大约一半。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColZ1AIhrZ5ibY5CdKeP2lKsoAdLCGrTJITOdjdeXnRn52hLp9yjlKJgMA/640?wx_fmt=png)

ByteGNN 为了显著降低网络开销，首先从系统架构层面将采样与训练这两个阶段作了解耦，让不同执行器分别负责一次 mini-batch 中的采样与训练：

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColXAlOXFhchHFsMvgdKBaMJfDv3G3iapjfazibDl6A8ACVm8B9TanB6H1g/640?wx_fmt=png)

同时，ByteGNN 提供了一套自定义的采样编程接口，不同 GNN 模型将统一用该接口来实现不同的采样逻辑。系统后端基于该接口自动地将采样逻辑解析成为一个计算图 DAG。采样计算图化的好处是可以充分利用 CPU 利用率，**动态**地将分布式采样过程抽象成更细粒度的小 task 并将其流水线化。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColDmXPPjz2ib031Y59VgYNSmggxTDCIG5Lzn5DNrPEIyAQib2XQjVFUFHw/640?wx_fmt=png)

ByteGNN 也做了一层中间调度层，将采样计算图和训练计算图“**软连接**”到了一起，通过一个调度器动态地平衡采样与训练这两个阶段的资源消耗和消费速率，目标使得系统的 CPU 利用率和内存开销达到最优：

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColwRep5AocLXDrk2pge8NPPThgQvxianp7iakDPFicVTTEPnltClDicplLsg/640?wx_fmt=png)

## 4.3 ByteHTAP: ByteDance’s HTAP System with High Data Freshness and Strong Data Consistency

论文链接：https://www.vldb.org/pvldb/vol15/p3411-chen.pdf

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhhEeGjcLRMmXyq63h2eColWbBXE2uqKP9nvvkHTzvRHYSISoVrmSxdFbR9YErSibD8cnBUE5JqqDw/640?wx_fmt=png)

近年来，在公司业务中，我们看到越来越多的场景需要对新导入的数据进行复杂的分析，并同时强调事务支持和数据强一致性。因此在论文中，我们重点描述了字节跳动的自研 HTAP 系统 ByteHTAP 的构建过程。ByteHTAP 是具有高数据新鲜度和强数据一致性的 HTAP 系统，采用分离引擎和共享存储架构。

* 其模块化系统设计充分利用了字节跳动现...