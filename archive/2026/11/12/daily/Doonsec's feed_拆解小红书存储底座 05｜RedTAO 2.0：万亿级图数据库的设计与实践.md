---
title: 拆解小红书存储底座 05｜RedTAO 2.0：万亿级图数据库的设计与实践
url: https://mp.weixin.qq.com/s/858gQjyp-RK_TBnK7M_NOg
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:58:29.818412
---

# 拆解小红书存储底座 05｜RedTAO 2.0：万亿级图数据库的设计与实践

# 拆解小红书存储底座 05｜RedTAO 2.0：万亿级图数据库的设计与实践

原创

REDtech
REDtech

小红书技术REDtech

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/P9Hs04VFGRkQKmKCw3LQ1hqBRqOhCKRUicPLrDkHNKxF2JtTNrqbMR4Q5v5jzL3Az5QaQsoRibJjMoW4H5Ag1N2buicibLZWKKL6wNC6X61GJQM/640?wx_fmt=jpeg&from=appmsg)

**导读**

小红书的存储与数据库体系覆盖 MySQL、RedKV、Redis、ROS 等产品，DMS、RedDTS 等公共能力分别提供统一管控和数据传输支持。点赞、关注、收藏，构成了小红书社区最常见的关系；内容理解、搜索推荐等场景，则需要沿着这些关系发现更复杂的关联。随着业务发展，数据规模、查询复杂度和服务地域不断扩展，图数据库需要在承载海量数据的同时，兼顾高并发下的低延迟与多跳查询能力。

RedTAO 是小红书自研的分布式图数据库。它从支撑核心在线业务的一跳关系访问起步，逐步演进为支持多跳查询的图数据库。截至 2026 年 11 月，据生产环境监控数据统计，目前已部署**近百个集群**，单集群最大承载**超过万亿行点边数据**，在线查询规模**超过千万 QPS**。作为「拆解小红书存储底座」系列的一篇，本文围绕**计算、缓存、存储三层分工**，介绍 RedTAO 的架构判断、设计取舍与后续方向。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRkmFVMJrVgkzEUYExCXibgicROTKZyS6Iz8tZq1ULJIPF1AaFRZiaCocVfA8nUWZAnicHCVO0dsT2PS6NzSoLNqIibU8tcqgeo1fa8U/640?wx_fmt=png&from=appmsg)

**01**

**背景**

早期，RedTAO 主要服务于点赞、关注、收藏等场景。业务通常从一个用户或一篇笔记出发，读取直接关联的对象，访问路径明确，对响应速度和服务稳定性的要求很高。一跳关系访问由此成为系统建设的起点。当图能力进入一些更复杂的场景后，查询开始沿多层关系展开，还需要结合属性完成过滤、排序和聚合。如果这些过程都由业务逐次发起请求、拼接结果，接入成本和访问开销会随查询复杂度上升。与此同时，数据规模持续增长，跨区域业务也提出了就近访问和异地多活的要求。这使 RedTAO 的建设目标逐步扩展：既要延续核心在线服务的低延迟访问能力，也要把多跳查询沉淀为数据库的通用能力。

围绕这一目标，团队形成了三项架构选择：**计算、缓存与存储独立扩展；复杂查询由服务端统一规划；业务请求在所属单元内完成**，跨单元更新通过数据同步传播。

**02**

**整体架构：用清晰的分层承接不同的增长**

图查询变复杂、热点流量增加、数据容量扩大，对应的资源需求并不相同。RedTAO 将系统划分为计算层、缓存层和存储层，分别围绕计算资源、内存容量和存储容量独立扩展。

**计算层负责理解和执行查询。**无状态的 GraphServer 承接业务访问，在统一入口下提供一跳 API 和多跳 Gremlin 查询。**缓存层负责高频数据的快速访问。**它面向关系集合、顶点属性和计数组织内存数据，承接在线读取。**存储层负责数据持久化。**当前生产使用 MySQL，保存点、边及相关属性和计数，并为缓存回源提供数据。

跨区域部署同样建立在明确的边界上。RedTAO 当前部署在多个异地单元，每个单元通过多个 region 提供异地多活能力，计算层和缓存层在各 region 独立部署。业务通过 SDK 访问所属单元内就近的服务，**在线请求不跨单元访问**；跨单元的数据更新通过主库之间的 RedDTS 双向同步传播，各 region 的缓存再通过变更回放更新，**异地数据最终可见**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRlwKjicicGDTlq5sW4OhOWrQ33rA0onul6PCgialGOCH4f0xnI4uJ2uosk4OszicP6icpyWGS0KXkpEfLibjIFYpxRxZTOnYbOGBYVuM/640?wx_fmt=png&from=appmsg)

图 1｜各单元业务在本单元内就近访问，主库之间通过 RedDTS 双向同步。

分层也为异常处理提供了余地。在线读取优先使用缓存，未命中时回源；缓存访问失败或超时时，计算层可以通过**备用请求直接读取存储**，降低缓存异常对读取可用性的影响。计算、缓存与存储各自承担明确职责，又通过回源、同步和降级路径相互协作。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRkIYicKjdvq6H5bNJibYOYibDRQAH7c4bicGqvfhibq8A5CzosvianGoLFGicvr6VruwHwzyjoH3gnKZU0mEvTCGGgfF5JbPTlrYhQA7I/640?wx_fmt=png&from=appmsg)

图 2｜三层协作与备用读取：缓存访问失败或超时时，计算层直接访问存储层。

**03**

**计算层：让业务表达关系，让系统安排执行**

计算层首先要把业务表达转化为可执行的查询计划。业界通常通过规则改写，或结合统计信息比较执行方案，减少不必要的访问。图查询的难点在于，关系每展开一层，都可能带来更多候选对象和中间结果；涉及路径时，还需要保存额外状态。因此，核心问题是**在支持复杂查询的同时，控制数据访问与资源开销。**

面向在线业务，RedTAO 当前采用**基于规则的优化**，将常见查询模式的优化经验沉淀为可解释、可扩展的规则，在规划开销和执行效率之间取得平衡。规划过程也会结合存储层的能力，尽量**让筛选和结果裁减靠近数据完成**，降低传输与中间计算开销；其余部分由计算层接续处理，保证查询语义完整。计算与存储通过统一的能力描述协作，使查询优化能够适配不同后端，为后续演进留出空间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRk7jTLcTuicSnpvdNODTRNm55kQCgf1ExTVYp3ELAKLmMUWamRibzR0oqRbYDYSkI1JIs0iceBaKK9RBP1WBD63wMfNeHyk3Vicpog/640?wx_fmt=png&from=appmsg)

图 3｜查询编译、规则优化与双执行器：从 Gremlin 查询到执行结果。

执行阶段则通过**双执行器**匹配不同需求：普通遍历只维护必要的中间数据，涉及路径历史或循环时，再保留相应状态。**按查询需要选择执行方式**，让常见查询保持较低开销，也为复杂查询保留表达能力。

**04**

**缓存层：围绕访问模式，降低整体查询代价**

查询计划确定了要读取什么，缓存层则让高频数据以更低的代价到达计算层。业界常用 Redis、Memcached 等通用缓存承接热点读取，也有 Facebook TAO 这样围绕对象和关系组织数据的专用缓存服务。两种方式都在利用内存降低访问延迟，同时减轻持久化存储的压力。

规模扩大后，缓存需要在**更新可见性、热点承载与回源压力**之间取得平衡。更新与失效机制决定业务何时看到新数据；热点复制、合并回源和负载隔离，则有助于缓解流量集中或大量未命中带来的冲击。

图查询还面临额外的通信成本：关系展开后，一批顶点可能散落在多个缓存节点上，缓存命中也无法消除多路 RPC 和等待汇总的开销。RedTAO 因此**按访问模式划分职责**，由 Cache Server 服务关系集合，Vertex Server 服务顶点属性与计数。

其中，**Vertex Server 用数据冗余减少 RPC 扇出。**在限定的服务或数据集范围内，每份副本维护完整的顶点数据，使同一范围内的一批读取可以交给一个节点完成，多份副本再分担读流量。这样既减少网络往返和结果汇总，也降低等待多个节点带来的延迟波动。

这种组织方式**以更多内存和副本维护成本，换取更少的跨节点访问**，适合读密集、批量点读较多且数据规模可控的场景。缓存层的收益因此需要放在一次完整查询中衡量，同时关注延迟、吞吐与稳定性。

**05**

**存储层：在成熟底座上贴合图的访问模式**

缓存降低了高频读取的成本，存储层则决定数据如何长期组织和维护。业界既有 Neo4j 这类面向图设计专用存储结构的路线，也有 JanusGraph、Facebook TAO 这类复用成熟存储系统的路线，选择取决于访问模式、扩展需求和运维条件。图数据库共同的难点是**兼顾读取效率、持续更新和规模扩展。**相关关系集中存放有助于减少分散读取，但也需要避免热点集中；常用统计提前维护可以减少重复计算，却会增加更新和校正成本。索引、分区与预先维护查询结果，都是围绕这些问题作出的取舍。

RedTAO 当前以**MySQL 作为生产持久化底座**，复用成熟的存储与复制能力，并围绕读密集场景调整数据组织：**让经常一起读取的关系靠近存放**，减少分散读取和额外排序；**提前维护常用统计**，让在线请求直接获得所需结果。

多地部署下，RedTAO 让**各单元独立维护自身的统计贡献**，再通过异步同步和本地汇总形成结果，偏差由校正机制收敛。这种分工减少了多个写入方共同修改同一总数的冲突，也延续了整体架构中本地访问、异地同步的边界。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRnzTxnqTV4XNGypNacCPEdGo6cIvrRmdDEichvOWzicOXq5luEYG1EHpYKaJelmlsNXIuVKkJibt8ficanJqoUMRAdTk4oiajMboQoA/640?wx_fmt=png&from=appmsg)

图 4｜关系就近组织、常用统计预维护与多地统计协作，共同支撑在线图访问。

这些选择以额外的数据组织、统计维护和校正成本，换取更低的在线读取开销。存储层由此把可靠保存数据与图访问优化结合起来，为上层查询和缓存提供稳定支撑。

**06**

**展望未来**

三层分工为持续演进提供了基础：查询表达、数据访问和持久化可以沿各自的方向优化，再通过明确的接口协同。随着业务从直接关系访问走向更复杂的关联查询，RedTAO 的下一阶段仍将围绕查询能力、资源效率与可靠性展开。

接下来，RedTAO 将沿三个方向继续演进。**计算层**探索面向大规模生产数据的复杂图计算；**缓存层**继续优化内存组织、批量访问和更新传播，提升低延迟访问能力与稳定性；**存储层**考虑从 MySQL 演进到 RedDB，针对图的数据模式进行深度定制优化，以降低成本，并将图能力融入多模数据库的统一底座。这些方向仍属于**后续演进规划**，将在现有分层基础上逐步推进。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRmIIDOR4Zcbr4dw5s3eHgicILyy28jcOEsXdhQQEExDajIMgR6Mf2uBqOicM2iayX44Pl6a40BFwZOCQxy0esRbslvPGcrXvNj1zU/640?wx_fmt=png&from=appmsg)

图 5｜当前生产架构与后续方向分别列示。

从一跳关系访问走向多场景图查询，**RedTAO 的演进始终由业务变化推动。**每一层都在查询能力、资源成本和服务稳定性之间作出取舍，清晰的分工则让这些选择能够协同落地，并随业务发展持续调整。我们期待与行业伙伴交流图数据库的设计与实践，共同探索更稳定高效、更贴近业务的图数据基础设施。

**07**

**作者简介**

秋山，小红书存储与数据库团队工程师，负责 RedTAO 图数据库的研发与建设。

部门介绍：

存储&数据库部，为小红书全业务场景打造行业领先的高可用、高可靠、高性能、低成本的存储和数据库类产品技术服务。团队致力于用精英化的组织和行业领先的技术理念，先于业务布局和行动，为公司业务的快速发展提供充足“弹药”，同时也让小红书存储和数据库成为行业该领域的标杆。

**08**

**招聘**

分布式数据库研发工程师/专家-存储&数据库：

小红书招聘

图/表/向量/多模数据库等方向

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRlbjfT9NicRYW9ZHXnYRRtic0zFmpJyK0FAW1icty1T3XSjq0j2zd9ctDCqsmVFnHp0RZ4CU9meR66wPUTS00XzCHR7Img76OeEw4/640?wx_fmt=png&from=appmsg)

精彩回顾：

[拆解小红书存储底座 00｜从孤岛走向融合：小红书存储与数据库架构进化](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247496855&idx=1&sn=f426a8f58708ca0fbef34b7e3308e468&scene=21#wechat_redirect)

[拆解小红书存储底座 01｜多源数据传输总线 RedDTS 2.0](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247496885&idx=1&sn=fcecfc62b3f876191ebaf931ace2ecc4&scene=21#wechat_redirect)

[拆解小红书存储底座 02｜让 AI 成为团队的一员：存储数据库助理实践](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247496958&idx=1&sn=bafda0c7a7030b5542ae6c54f26876d5&scene=21#wechat_redirect)

[拆解小红书存储底座 03｜从存得下到读得快：小红书自研对象存储实践](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247496995&idx=1&sn=4f8f5120b9fff8d77f0c8c9d9c590fee&scene=21#wechat_redirect)

[拆解小红书存储底座 04｜从对象到文件：RedStore SSD 引擎与 RedFS 的设计与实践](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247497095&idx=1&sn=c498a5620224ad5b758fbcd3b4276e22&scene=21#wechat_redirect)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vxnkL2N86IsWfuArZ4Oibu3JjynORoXVKc5OaGgUib1G8yiam3A5HlC2PDpDw1qTu4lasuiakZ76vRsf3KJNKiaye5w/0?wx_fmt=png)

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