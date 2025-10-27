---
title: 湖仓一体架构在火山引擎 LAS 的探索与实践
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247501833&idx=1&sn=f55cafb352c31d7532639b72f6587709&chksm=e9d303ebdea48afdbc55dd912018b03a3b5cec9c054a62639af7a57cc66c85b44038bcd98c05&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2023-03-28
fetch_date: 2025-10-04T10:55:05.897620
---

# 湖仓一体架构在火山引擎 LAS 的探索与实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIWdFnVRbEh3IIiax3pav2wbthWFOn7eIc66CJjNghdCicfLaSHWZXVr0w/0?wx_fmt=jpeg)

# 湖仓一体架构在火山引擎 LAS 的探索与实践

原创

火山引擎LAS

字节跳动技术团队

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

火山引擎湖仓一体分析服务 LAS（Lakehouse Analytics Service），是面向湖仓一体架构的 Serverless 数据处理分析服务，提供字节跳动最佳实践的一站式 EB 级海量数据存储计算和交互分析能力，兼容 Spark、Presto 生态，帮助企业轻松构建智能实时湖仓。

LAS 服务是什么？LAS 有哪些优化特性？本文将从基础概念、数据库内核特性优化、数据服务化、业务实践等角度全方位介绍湖仓一体架构在LAS的探索与实践。

# LAS服务是什么？

在了解 Las 服务是什么之前，先来了解一下数据平台整体行业的发展趋势，大概分为三个阶段。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIkycnibjouZV60tmXUapsMZeHeupCH7utiaoxEiaacaxia9ibS8Sh3ibXZBSg/640?wx_fmt=png)

第一阶段，一般被称为传统数仓，一种从 1980 年开始的基于传统数据库技术来做的 BI 分析场景。在这种架构下，通常计算和存储是高度一体的。整体系统能支撑的计算能力，依赖于服务提供商的硬件配置，整体成本高，存在物理上限，扩展起来比较麻烦。

第二阶段，随着技术的演进， 2010 年开始出现了以 Hadoop 技术体系为主流的传统数据湖。在以 Hadoop 技术为主的数据平台架构下，通常可以支持服务在普通硬件上面去部署，整体的计算和存储的扩展性都得到了解决。基于开源技术生态，多个大型公司也参与到数据湖技术发展中来，整体生态繁荣度也在逐步提升。

但在这一阶段凸显出了一个问题，随着生态技术的发展，越来越多的开源组件开始累积。对于一个企业来说，为了解决不同领域的问题，需要运维多个开源的组件，来满足不同领域的数据需求，就导致整个企业的技术运维成本逐步提升。

基于这个问题，随着技术的进一步发展，在 2020 年，湖仓一体的架构开始被提出。

相比起传统数据湖，湖仓一体架构支持原生的 ACID 能力，支持像 BI 分析、报表分析，机器学习和流式分析多种类型的计算范式，以及云上的对象存储和弹性计算能力。以上能力，让湖仓一体架构能够有效地去解决企业的对数据规模，以及对计算能力的弹性伸缩需求。同时，湖仓一体可以在很大程度上规避传统 Lambda 架构存在的多个计算组件，或者多种架构范式导致的架构负担，让企业能够更专注地去解决他们的业务价值。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIiaiamSmk0QYWnibYZqgeR2qCRDGKY0ofb8lQrEKdIggvUEC1cVf4ToSLQ/640?wx_fmt=png)

LAS 就是基于湖仓一体的架构进行设计的。从上图来看，LAS 架构整体上分为三个部分。最上层是开发工具层，开发工具层会通过计算层提供的统一 SQL 访问服务去访问计算层，根据用户的 SQL 类型自动做 SQL 解析。所有引擎计算能力统一由弹性容器服务来提供，可以支持弹性伸缩，按需使用。

再往下就是湖仓一体的存储层。首先，湖仓一体存储会通过统一的元数据服务，向计算层提供统一的元数据视图，屏蔽底层的具体元数据实现细节，可以使多个引擎无缝对接到统一的元数据服务。

接下来是湖仓存储引擎，它主要提供了事务管理能力，也就是 ACID 的能力，以及对数据批流一体的读写能力。

再往下就是 LAS 基于火山引擎对象存储服务 TOS 和 CloudFS ，来提供 EB 级的数据存储能力和数据访问的缓存加速能力。

以上就是 LAS 整体的技术架构。

# **LAS** **数据湖内核剖析**

这一版块将向大家呈现 LAS 数据湖内核的特性及优化。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIyR6NIOnqOgQv8rQwMTWxia12lQFXvrFVnl9mUZXNIot4pibFW6s5tzng/640?wx_fmt=png)

**LAS 的数据湖内核—— ByteLake** **它是什么？**

首先，ByteLake 是基于开源 Apache Hudi 进行内部增强的湖仓一体存储引擎，提供湖仓一体的存储能力。

它的第一个主要能力是提供了湖仓统一的元数据服务，完全兼容开源的 Hive Metastore，可以无缝对接多种计算引擎。第二个主要能力是可以支持对海量数据的 Insert，完全兼容 Hive SQL，可以平迁传统数仓场景下的 Hive 任务。第三，ByteLake 支持对大规模历史数据的 Update 和 Delete，以及对新增数据的 Upsert 和 Append 能力。最后，ByteLake 支持流批一体的读写能力，提供流式读写的 source 和 sink，支持近实时分析。

**ByteLake** **又是怎么做到这些能力的呢？接下来从以下几个特性来展开阐述。**

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGI1O07LPnAvrA5JBHPBGCWsQf31pa3l3ND38F1Iu61R2k6ibXO8l28oUw/640?wx_fmt=png)

**如何实现高效数据更新？**

第一个场景是流式写入更新场景。在这种场景下，最明显的特点就是小批量数据频繁写入更新。但主要的问题是如何去定位要写入的记录呢？是做 update 操作还是 insert 操作？

在这样的背景下，ByteLake 提供了一种 Bucket Index 的索引实现方案。

这是基于哈希的一种索引实现方案。它可以快速地去定位一条记录所对应的 Fail Group，从而快速定位当前记录是否已经存在，来判断这一条记录是做 Update 还是做 Insert 操作，从而可以快速地将这种小规模的数据去添加到 Append Log。在读取时，通过 Compaction 就可以将 LogFile 和 BaseFile 里边的数据进行 Merge 去重，从而达到数据更新的效果。

针对日志数据入湖，通常来说是不需要主键的，这种基于 Hash 索引的实现方式，是需要有 Shuffle 操作的。因为在基于 Hash 的索引实现中，当一批数据过来之后，会根据这一批数据去找分别对应的 File Group，再基于 File Group 去聚合要更新的这些数据，通过同一个 Task，去更新同一个 File Group 来实现原子写入。

在数据 Shuffle 的过程，其实对于数据湖日志写入是有额外的开销的，但 ByteLake 提供了一种 Non index 的实现方案，去掉了索引的约束，可以减少数据 Shuffle 的过程，从而达到快速入湖的能力。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIu89uEhoUgykyoFibQm9TJg58y82ehfeFUNibyKdJ2sleHPm4vFvZJcmA/640?wx_fmt=png)

**存量数据如何高效更新?**

存量数据，一大特点就是数据量大，单表的规模可能有几百 TB ，甚至到 PB 的级别。针对于这种大规模的历史数据的更新场景，如何去提升更新性能？其实最主要的就是要如何去降低数据更新的规模。

基于此，ByteLake 提出了一种实现方案——Column Family，将单表多列的场景分别存储到不同列簇。不同的文件可以基于 Row Number 进行聚合，合并后就是一个完整的行。如果要更新历史数据，只需要去找到要更新的那些列对应的 Column Family 对应的文件，把这些文件做一些局部更新，就可以达到整体更新的效果。从而在很大程度上减少这些非必要数据的扫描，提升存量历史数据更新场景的性能。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGI1IxewBvg8uWcZLb4mTAhfboaSeawDuCE1IV1rJlIK5u4kzVWeWh4WA/640?wx_fmt=png)

**如何提升并发性能？**

谈到并发，通常会有两部分内容。比如有很多个任务同时去往 ByteLake 引擎里边写数据，这就意味着有大批量的任务去访问 ByteLake 的 MetaStore Service。在这种场景下，ByteLake MetaStore Service 就会成为一个性能瓶颈。

为了突破这个瓶颈，除了无限的堆加资源之外，另一个比较有效的方案就是增加缓存。通过元数据服务端去缓存比较热点的数据，比如 Commit Metadata 和 Table Metadata，来达到服务端的性能提升。

另外一块，是在引擎侧做优化。比如在 Flink 引擎层面将 Timeline 的读取优化到 JobManager 端。同一个任务下，只要 JobManager 去访问 Hive ByteLake MetaStore Service，缓存到 JobManager 的本地之后，所有的 TaskManager 只要去访问 JobManager 本身缓存的 Timeline 信息就可以了。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIR7jXNrF0hVnGVqIvrJeJYDwGI5fyNI8OgQSzHEmM8WN7ehZ7E7tPCA/640?wx_fmt=png)

从单个任务的视角来看，比如多个任务要同时去更新同一张表，这种情况下要保证数据的正确性，同时又能保证并发性能，应该如何来做？ByteLake 提供的解决方案——基于乐观锁的一个并发控制。

针对多任务写同一个表的场景，ByteLake 可以支持多种并发策略的设置。业务可以根据对数据一致性的要求，以及对数据并发性能的要求，选择灵活的并发策略，来达到它的数据并发写入的性能指标。

# **LAS** **数据湖服务化设计**

这个版块将向大家呈现 ByteLake 服务化过程中的一些设计实践。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIf2lJsIxf3bUZOz7brUKGncZb9oKux7DPiaUYjaLibDicSpl6pNmVm3gKA/640?wx_fmt=png)

**CatalogService** **：统一的****元数据****视图**

CatalogService 主要提供了与 HMS 的兼容接口，同时为所有的查询引擎提供了统一的元数据视图，解决了异构数据源的元数据管理问题。

CatalogService 整体分三层，第一层是 Catalog Federation，提供统一的视图和跨地域的数据访问能力。以及提供了对源数据请求的路由能力，可以根据元数据请求的类型，支持通过 Mapping 的方式，来路由不同的服务请求对应的底层元数据服务实例。

第二层是 CatalogService 下层的具体元数据服务的实现，比如 Hive MetaStore Service 以及 ByteLake MetaStore Service 等。可能还有不同的元数据服务对接到 CatalogService，来统一向上层引擎提供这种元数据服务。

最后一层是 MetaStore 的存储层，它通过插件式的方式来提供不同的存储引擎，来满足上层不同元数据服务实例的存储要求。

### BMS 详解

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIhiaGlPbkOhTPEBXBTibZGxicicj5upx073eXfS0pvlwrJicStziaghH7oPvA/640?wx_fmt=png)

#### 湖仓一体元数据管理服务

Bytelake MetaStore Service，简称 BMS，它是一个湖仓一体的元数据管理服务，整体的架构分为以下几个部分。首先第一个就是 Catalog，Catalog 是对单表的元数据访问的抽象。主要逻辑是通过 MetaStore Client 来访问 Meta Server，同时它会去缓存单表的 Schema 信息以及属性等信息。

另外一部分就是 Meta Server，也就是 BMS 里边最核心的部分。它主要是包含两大部分服务层，第一是 Bytelake MetaStore 元数据服务模型，比如 Table Service，Timeline Service，Partition Service 和 Snapshot Service。存储层提供了 MetaStore 所有元数据的存储能力。最后一部分就是 Eventbus， Eventbus 主要目的是为了将元数据的 CUD 事件发送给监听者，来达到元数据信息的分发和同步。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIZS1q8qPwuYGM7QSgXrF7I9zibVKbstCavR1mquVv6TuEiatmk5eorklA/640?wx_fmt=png)

#### 元数据写入流程

关于元数据写入流程，简单来讲，当有一个 Client 去提交了 Instant 之后，Bytelake Catalog 会去访问 Bytelake Meta Store 的接口，会将 Instance 改成 Completed，然后将请求发到 Bytelake 的 MetaStore，之后 Bytelake MetaStore Server 会做一个原子提交。

在此之后，Timeline Service 会把提交的状态更新到数据库里边。接下来这些分区信息将再被提交给 Partition Service，同步到对应的分区存储表里去。最后一步，把这些所有的变更作为一个快照，同步到 Snapshot Service 里，它会把文件层面的变更存储到数据库里，做持久化存储。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIcEjzqR1MKtW4ibhkR9icPx8m1MDffQy96WwBIp83uhmeJ8xFtjXIib5Lw/640?wx_fmt=png)

#### 元数据读取流程

对于源数据的读取流程，举个例子，有一个计算引擎它读取了一个 SQL，通过 SQL 解析拿到一张表，这张表会通过Bytelake Catalog Service去请求Bytelake MetaStore，最终会路由到 Table Service 拿到这些表的信息。

拿到表的信息做 SQL Plan 优化的时候，会做一些分区的下推或裁剪。这个时候会去请求到 Bytelake 的 Partition Service 做过滤，接着会根据分区信息去扫描文件，在此过程中会去请求 Timeline Service 获取对应的 Timeline 信息。接下来，基于 Timeline 的信息时间去 Snapshot Service 拿到对应文件，再通过 SQL 执行器来实现数据文件的读取。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIRpiceczQZgnl05DaYYxHjooH01ibq6RSZIVc2ZkTwSIM6TyRLp7AayvQ/640?wx_fmt=png)

#### 元数据变更通知

元数据变更通知具体的实现流程主要依托于两个部分。

一是 Eventbus，二是 listener。所有的元数据请求都会发送到 Eventbus，由 Eventbus 分发事件到所有已经注册的 Listener 上面。listener 再根据下游系统的需求，去订阅 Eventbus 里边的对应事件类型进行响应，从而达到让上下游的组件感知到元数据的变化，实现元数据的同步。

### **TMS** **详解：**

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhjjZ2c2Zb4Hhgq32WBwwGIL9FS2pRVUQuJHEWXmm7nV5VS1wVhIR03O1LnXF95xvVIwBdhoPGzxw/640?wx_fmt=png)

#### 统一表管理服务

LAS 的另外一个服务——TMS，全称是 Table Management Service。它主要解决的问题是异步任务的托管优化。为什么会做异步任务的托管优化？因为正常来讲，Flinker SQL 任务写 ByteLake 表的过程，其实就是把批量的数据写入下游表里边去。随着时间的推移，一个是 Commit 的日志非常多，另外一个是小文件非常多。通常的 Flink 引擎层面的实现方案，是在数据写了一定的次数后，追加一个 Compaction 操作，把之前写入的文件做一个压缩。

但针对流式任务去做 Compaction，对正常的流式任务稳定性有很大影响，因为压缩本身是一个开销比较大的动作，对流式计算资源的消耗是很难去评估的，会导致整个流式写入任务的波动，从而影响流式写入任务的稳定性。

基于此，LAS 提供了一个统一的表管理服务，异步托管这些本身内置到引擎内部的任务，统一由 Table Management Service 来托管。它整体的架构是一个主从架构，主要包含的组件一个是 Event Receiver，用来接收 Metastore 下发的一个 Event。PlanGenerator 就是根据 Meta store Server 下发的 Even...