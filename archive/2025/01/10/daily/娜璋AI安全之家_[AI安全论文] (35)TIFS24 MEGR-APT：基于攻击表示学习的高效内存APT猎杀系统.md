---
title: [AI安全论文] (35)TIFS24 MEGR-APT：基于攻击表示学习的高效内存APT猎杀系统
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501201&idx=1&sn=709a7a8f892f19870b9ed0d31f4f57aa&chksm=cfcf755cf8b8fc4a71ce77f85d729cb7786e2c6403626fe5b8e0a65fd94cc65f0a2d4503116a&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2025-01-10
fetch_date: 2025-10-06T20:12:30.249752
---

# [AI安全论文] (35)TIFS24 MEGR-APT：基于攻击表示学习的高效内存APT猎杀系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDROJ1RoIEHfImJuJ7kV607kom2WMyNl3xvCRI4pmaEsULLUltCydA0RWPDJOBmMia7AJ1Fe3BU7qfFQ/0?wx_fmt=jpeg)

# [AI安全论文] (35)TIFS24 MEGR-APT：基于攻击表示学习的高效内存APT猎杀系统

原创

钟睿杰

娜璋AI安全之家

> 年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koyCt0jxRGu7e9Yic09B3CmrBZ70xVJicDHicAK2icfWRXL561kJvJCY9zPw/640?wx_fmt=png&from=appmsg)

《娜璋带你读论文》系列主要是督促自己阅读优秀论文及听取学术讲座，并分享给大家，希望您喜欢。由于作者的英文水平和学术能力不高，需要不断提升，所以还请大家批评指正，非常欢迎大家给我留言评论，学术路上期待与您前行，加油。

该文是贵大0624团队论文学习笔记，分享者钟睿杰同学，未来我们每周至少分享一篇论文笔记。前一篇博客介绍了ESWA’24的轻量级入侵检测论文，结合特征工程开发更轻量级、准确高效的IDS。这篇文章将带来TIFS’24加拿大康考迪亚大学——基于攻击表示学习的高效内存APT猎杀系统（MEGR-APT），本文的主要贡献为结合更好的子图提取技术，保证子图提取的正确性和维度，减少内存消耗；构建攻击表示学习，提高准确率和运行速度。此外，由于我们还在不断成长和学习中，写得不好的地方还请海涵，希望这篇文章对您有所帮助，这些大佬真值得我们学习。fighting！

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607ko47667c0WXfM76CPq8MV2LIutx3L88x1ib01TGsVk5tT72xSOT7NhLjA/640?wx_fmt=png&from=appmsg)

```
原文作者：Ahmed Aly,Shahrear Iqbal, et al. 原文标题：MEGR-APT: A Memory-Efficient APT Hunting System Based on Attack Representation Learnin 原文链接：https://ieeexplore.ieee.org/document/10517754 发表会议：IEEE TIFS 2024博客作者：贵大0624团队 钟睿杰开源代码：https://github.com/CoDS-GCS/MEGR-APT-code
```

**一.摘要**

高级持续性威胁（APT）的隐蔽性和持续性使其成为最具挑战性的网络威胁之一。为了捕捉这种持续性，许多系统采用了基于溯源图（provenance graph, PG）的方法进行安全防护。溯源图通过使用因果关系和信息流将系统实体连接起来，从而表示系统审计日志。APT狩猎需要处理不断增长的大规模溯源图，这些图表示了几个月或几年的广泛活动，即多TB级别的图数据。

现有的APT狩猎系统通常是基于内存的，这会导致巨大的内存消耗，或者是基于磁盘的，这会导致性能下降。因此，这些系统在图的规模或时间性能方面难以扩展。

本文提出了MEGR-APT，一种可扩展的APT狩猎系统，旨在发现与发布在网络威胁情报（CTI）报告中的攻击场景（查询图）匹配的可疑子图。MEGR-APT采用两阶段处理方法进行APT狩猎：

* （i）内存高效地提取可疑子图作为图数据库中的搜索查询；
* （ii）基于图神经网络（GNN）和我们有效的攻击表示学习进行快速子图匹配。

我们将MEGR-APT与当前最先进的APT系统进行了比较，使用了DARPA TC3和OpTC等常用的APT基准数据集，并且还使用了真实的企业数据集进行了测试。MEGR-APT在内存消耗上实现了数量级的减少，同时在时间和准确性方面与最先进的系统表现相当。

**二.引言及前置知识**

1.引言

MEGR-APT 通过两个过程捕获 APT：（i） 内存高效的可疑子图提取，以及 （ii） 基于图神经网络 （GNN） 和我们有效的攻击表示学习的快速子图匹配。我们的双重过程平衡了时间和内存效率之间的权衡。为了克服基于磁盘的解决方案的局限性，我们开发了一种基于资源描述框架 （RDF） 图模型的 PG 的有效表示 [13]。我们基于 RDF 的图形设计支持在较长一段时间（数月或数年）内增量构建 PG。

我们使用 DARPA TC3 [16] 和 OpTC [17] 评估 MEGR-APT，这是评估基于出处图的系统的两个最流行的基准数据集 [5]。MEGR-APT 的内存消耗减少了一个数量级，同时在时间和准确性方面实现了与 Poirot [7] 相当的性能，Poirot [7] 是一种基于图匹配的最先进的威胁搜寻系统。例如，MEGR-APT 消耗了 288 MB 的内存来搜寻 TC3 主机中的 APT，而 Poirot 使用了 21 GB 的内存。两个系统的处理时间为 6 分钟。此外，我们使用企业数据集执行了一个真实的用例。

本文贡献可以总结如下：
开发轻量级和准确性高的APT检测系统，使其能在资源受限的设备上运行。该系统用于从大型 PG 中大规模捕获 APT。

* 内存高效的 APT 检测：构建一种从大型 PG 和给定查询图中提取可疑子图的内存高效方法一种基于攻击的表示学习模型，以低内存消耗提取与攻击场景相关的可疑子图。
* 高效的子图匹配：利用图神经网络（GNN） 和攻击表示学习，快速匹配可疑子图与攻击场景（查询图）。
* 使用广泛使用的 APT 基准测试（即 DARPA TC3 和 OpTC）进行全面评估，并创建一个真实的用例。结果表明，MEGR-APT 在减少内存方面优于最先进的系统，同时实现了相当的准确性。

2.前置知识

下面给初学者或其它小方向的同学普及下APT攻击和溯源图前置知识。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koFpD4k1WI69ZDE7vmbv8TNJPFgPZt877y454rR62eTbulIbca4F94Hw/640?wx_fmt=png&from=appmsg)

什么是溯源图？
溯源图是一种通过图形化方式展示事物发生过程和各环节关系的工具，通常用于追溯事件的源头或原因。

为什么要用溯源图？
APT攻击往往持续几个月甚至更长时间。攻击者通常长时间保持隐蔽，通过间隔性的攻击步骤避开传统的监控系统。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607kouoROasicEokqNEJtf2IKKvxXul2BFPEGzdpZfaputcUZOEwQnXpzRgw/640?wx_fmt=png&from=appmsg)

下面给出具体的示例：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koBe9FIa6iarnCqqmE13BzdfZpIktcSal24NrLh55GA7AtwQkk8q3RCeA/640?wx_fmt=png&from=appmsg)

APT检测系统现有工作：

* 整体溯源图：处理通常需要大量内存和计算资源，难以扩展到大规模系统
* 事件序列：序列化的表示可能无法完整捕捉攻击，无法检测长时间跨度的攻击
* 溯源图子图：能够减少部分内存和计算资源开销，依赖领域知识

现有APT检测系统的局限性:

* 内存消耗：现有的APT检测系统通常是内存型的，容易造成巨大内存消耗，难以应对大规模数据集。
* 性能瓶颈：基于磁盘的APT检测方法可能会遭遇性能瓶颈，导致检测速度缓慢，难以实现实时或近实时检测。
* 扩展性问题：目前大多数系统难以扩展以适应大规模数据的处理，尤其是在涉及到数TB级别的日志数据时。

因此，开发一个轻量级并且能准确识别真实网络攻击行为的APT检测迫在眉睫。研究需求:

* 结合更好的子图提取技术，保证子图提取的正确性和维度，减少内存消耗
* 结合更好的攻击表示学习，提高准确率和运行速度

**三.本文模型**

1.总体架构

本文的整体框架如下图所示，关键步骤包括：

* 基于日志文件对溯源图进行构建并存储在图数据库中
* 基于攻击报告构建攻击查询图，并标记出对应的IOC节点
* 基于查询图以及对应的IOC节点对溯源图使用SPARQL语言（SPARQL Protocol and RDF Query Language）进行溯源子图提取
* 基于RGCN模型对查询图和溯源子图进行攻击表示学习
* 基于GNN的图匹配模型，计算出查询图与溯源子图的相似性分数产生警报

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koj6e0DZJv4UsGm0PCNYms8LwFJicSBmOesy7ASWB8iaIHLC0zA43hjdPQ/640?wx_fmt=png&from=appmsg)

2.构建溯源图

（1）解析日志获到实体、事件、属性，并将实体用点、事件用边表示，添加对应的属性。

（2）为溯源图创建一个逻辑命名空间和前缀声明，以便在后续的RDF三元组生成过程中可以引用这些名称。如下例子：ex:File123 就是http://example.org/File123 的简写。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607kodVCTYRcGfDqTA1vdicZSB02HjVzgaun90RnueozYsuZKfvnmCAy7BNQ/640?wx_fmt=png&from=appmsg)

（3）将每一个点、每一条、每一个属性根据RDF格式添加到溯源图中。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607kouUwzLHLPjmlNFEq9DyIQicWvQIfqpQheKZkeZ2YoGhwdSeVmNrhC5EQ/640?wx_fmt=png&from=appmsg)

3.IOC溯源子图提取

（1）将上一步骤在查询图中提取的IOC在溯源图中标记为可疑节点。

（2）基对于每一个可疑结点，对其N-hop以内的所有节点进行判断：若为进程或可疑节点则添加到三元组数组中。

（3）限制溯源图提取子图的边数以及点数。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koCA9jxL56Q2OkOupLwLfU5hYsE09GFYFoBhpo7EwaCDT934JpCXezxQ/640?wx_fmt=png&from=appmsg)

4.RGCN: 对图中节点编码

RGCN（Relational graph convolutional network）在处理多关系图时，能够更有效地捕捉不同类型关系下的节点特征交互，而GCN则适用于处理单一类型的图数据。如下左图，在GCN结点6的参数更新是基于1，3，4三个节点采用相同的策略，但是在实际场景中，1，3，4与6的关系是有所不同，故对其的参数更新有不一样的决策，故引入RGCN算法，如右下图，该算法考率不同的关系对当前节点进行参数更新。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607kohauia5zZzOrySInS810fiazQQjsHVLvrSUUKYtHRibZiaKAUWibribqeqY4A/640?wx_fmt=png&from=appmsg)

5.基于GNN的表示学习和图匹配模型

（1）对查询图和溯源提取子图中各节点采用RGCN编码。

（2）基于各节点的编码采用全局注意力得到最终图向量表示。

（3）使用NTN（Neural Tensor Network）和Full Connect Neural Network进行相似度评分。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koLSgC1n14PgnRy1bXKow7ia2cWfzLP61ZZ9Upczjw4O4AwqwbGZuibeuA/640?wx_fmt=png&from=appmsg)

**四.实验评估**

1.数据集

（1）DARPA TC3
对三个主机进行两周的APT攻击模拟，使用不同的操作系统,TRACE 和 THEIA 主机运行 Linux 操作系统，而 CADETS 运行 FreeBSD 操作系统。

* https://github.com/darpa-i2o/Transparent-Computing

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koZ8ous9PtdBCWdkE3KqibqeC9ibpoibOQCZkQia4DWak11eYD6ZfuhV9ibqw/640?wx_fmt=png&from=appmsg)

（2）DARPA OpTC
从 1000 台 Windows 主机收集了 7 天的系统审核日志。攻方在过去三天内针对多个主机3次APT模拟攻击

* https://github.com/FiveDirections/OpTC-data

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607kok6icOGAcNKkyFff9NANReFdDxO7ybwXibuLPO2ibhLln6xMoIp5ZVJ9zQ/640?wx_fmt=png&from=appmsg)

2.实验结果分析

（1）内存和时间效率
在DARPA TC3数据集上评估 MEGR-APT 与 POIROT 和 DEEPHUNTER 的内存和时间效率：显示了每种攻击场景、其相应的溯源图大小和日志持续时间。可从表中观察到，MEGR-APT所占有的内存是最少的。Poirot模型检测到一个子图便会停止，但消耗资源仍较大。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koGjaugLZ7ZB1QYZzBF5WvcsfMr4zYlkSkVoOwhJnmrA31q9LYIOEPVw/640?wx_fmt=png&from=appmsg)

（2）DARPA OPTC 数据集上评估
在攻击数据集中能够检测出子图；在良性数据集中不会检测子图，不存在误报。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607kowicscv8nEaB4UfheTibWTREHJYKHeyRu9iaicOvpcAibuGyOR1GzZ1Hx3fQ/640?wx_fmt=png&from=appmsg)

（3）DARPA TC3 数据集上评估
在攻击数据集中有较高的AUC以及准确率；在良性数据集中不会检测子图，不存在误报。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koyU4ria85ABPkNeEMRvVdT3W3pm9iaqR29yLuFvEegLxeMDgSKAWZsYkg/640?wx_fmt=png&from=appmsg)

（4）真实数据
在真实企业中执行了一个真实的使用案例，其中包含从 4000 台主机收集的内核日志数据集，时间跨度超过 6 个月。根据内部工具支持的手动调查，在具有一个恶意痕迹的主机和12个随机良性主机上测试了 MEGR-APT，其在12个良性主机中的11个中没有产生任何假警报，而它在1个良性主机中生成了两个人类报告中不存在的警报。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koDiaJyU7ptOY7Jq544JrTyqj1PmLUu7uyXwFxypZdsyalHOuSvIgkVyg/640?wx_fmt=png&from=appmsg)

（5）消融实验

* 子图提取方法消融：在DARPA OpTC数据集分别使用Poirot、DeepHunter和本文方法的子图提取方法进行实验，可观察本文方法准确率高、消耗资源少。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koS6Hfotcg6xcibS2Fzt9EcXRmucoJ0m7SdhjSj05JJicGgKu6zCImnWSw/640?wx_fmt=png&from=appmsg)

* 攻击表示学习消融：使用DARPA TC3数据集分别进行有或没有的攻击表示学习实验，可观察到有攻击表示学习的方法性能表现更好。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607ko8IpKavDD8Irlia7oy1PUQkSxp4BvficBn0FtYjQBgBQIF4UUwBJP2iabA/640?wx_fmt=png&from=appmsg)

**五.相关工作**

基于溯源图处理的三种机制包括整体溯源图分析（如 Unicorn 和 Prov-Gem，用于检测长期攻击，但易误报且缺乏可解释性）、事件序列分析（如 ATLAS 和 ANUBIS，提取事件序列分类攻击，但难以捕获完整上下文）、以及子图分析（如 SteinerLog、Holmes 和 MEGR-APT，通过规则匹配或图匹配检测恶意子图，更具解释性但依赖专家规则或查询图）。

高级持续性...