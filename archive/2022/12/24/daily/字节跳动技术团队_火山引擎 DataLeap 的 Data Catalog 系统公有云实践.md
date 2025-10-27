---
title: 火山引擎 DataLeap 的 Data Catalog 系统公有云实践
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500746&idx=1&sn=49798c1d670fb596acead96995d3f122&chksm=e9d30828dea4813ec70e9756bcf9c76b1e9f41c015f4469a0d93350289ad4cdd74d10eaa2cfe&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2022-12-24
fetch_date: 2025-10-04T02:26:17.015095
---

# 火山引擎 DataLeap 的 Data Catalog 系统公有云实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOgPxtBghGuLQkQlpI6EsvFYT4nXSCKDult9iaGFWXCYJznehw5uKhY3Wn3YyJktJkict9hxHbPctTYQ/0?wx_fmt=jpeg)

# 火山引擎 DataLeap 的 Data Catalog 系统公有云实践

开发套件团队

字节跳动技术团队

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

Data Catalog 通过汇总技术和业务元数据，解决大数据生产者组织梳理数据、数据消费者找数和理解数的业务场景。本篇内容源自于火山引擎大数据研发治理套件 DataLeap 中的 Data Catalog 功能模块的实践，主要介绍 Data Catalog 在公有云部署和发布中遇到挑战及解决方案。

# 1. 背景

Data Catalog 是一种元数据管理的服务，会收集技术元数据，并在其基础上提供更丰富的业务上下文与语义，通常支持元数据编目、查找、详情浏览等功能。目前 Data Catalog 作为火山引擎大数据研发治理套件 DataLeap 产品的核心功能之一，经过多年打磨，服务于字节跳动内部几乎所有核心业务线，解决了数据生产者和消费者对于元数据和资产管理的各项核心需求。

DataLeap 作为一站式数据中台套件，汇集了字节内部多年积累的数据集成、开发、运维、治理、资产、安全等全套数据中台建设的经验，助力 ToB 市场客户提升数据研发治理效率、降低管理成本。

Data Catalog 作为 DataLeap 的核心功能之一，本文汇集了 Data Catalog 团队在最近一年公有云从 0 到 1 实践的整体经验，主要讲解遇到的各项挑战和对应的解决方案。

# 2. Data Catalog 公有云发展历程

Data Catalog 已经随着 DataLeap 一起作为公有云产品正式在火山引擎对外发布，下面是 Data Catalog 在功能演进上的一些重要时间节点：

* 2021 年 9 月，Data Catalog 随着 DataLeap 完成在火山引擎公有云首个版本部署和发布，包含 60% 内部核心功能，支持 EMR Hive 数据源元数据管理。
* 2022 年 2 月，Data Catalog 随着 DataLeap 完成火山引擎公有云 Beta 版本发布，吸引了一批客户试用。
* 2022 年 5 月，Data Catalog 随着 DataLeap 完成火山引擎公有云 GA 版本发布，正式对外开放。
* 2021 年 9 月至 2022 年 5 月，Data Catalog 发布 10+ 版本，对齐 95% 内部核心功能以及发布新功能 20+，包括支持 LAS/ByteHouse 数据源、OpenAPI 和元数据采集等 ToB 场景新特性。

# 3. Data Catalog 公有云整体架构

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOgPxtBghGuLQkQlpI6EsvFY24AaI4kkdNjW0DhibiaAySf3J80uS2bw4k64JDLdHfc9ePZnTfTrtdZg/640?wx_fmt=png)

Data Catalog 支持综合搜索、血缘分析、库表管理、元数据采集、备注问答、专题管理、OpenAPI 等功能，和 DataLeap 其他功能模块（如数据开发、数据集成、数据质量、数据安全等）一起提供了大数据研发和治理场景的一站式解决方案。同时，Data Catalog 公有云产品是基于火山引擎提供的数据引擎和云基础设施来部署和服务的，下面会简单介绍下我们所依赖和使用的产品和服务：

* **数据引擎：**是火山引擎提供的数据分析、数据仓库和数据湖相关产品，包括 ByteHouse/EMR/LAS 等产品。通常 Data Catalog 会从这类系统内采集元并存储元数据，进行处理加工后，再提供搜索、血缘分析等功能；另外，库表管理模块也会依赖这类系统提供对应的接口来做建库建表等操作。
* **内部公共服务：**是火山引擎为支持公司内部产品上公有云提供的若干公共基础服务，主要作用是方便内部产品能快速在公有云部署，提供和公司内部兼容性比较高的公共服务，降低改造和迁移成本。其中 Data Catalog 使用较多的包括：API 网关、网络代理、访问控制、安全认证、监控报警等。
* **基础服务：**这类服务或产品相较于上面说的内部公共服务主要区别是，他们是火山引擎对外售卖的标准云服务，内外部用户都可使用，且和业界主流云厂商能力是基本对齐的，不过会和公司内部一些类似的基础服务会有不少差异。Data Catalog 主要使用这类基础服务来进行自身服务的部署运维，并且进行较多的兼容性改造，包括容器部署、网络打通、内外部 CICD 和监控报警流程一致性等方面。
* **数据库和中间件：**是和业界主流云厂商对齐的存储和中间件领域的标准云服务，和公司内部对应组件也会有若干差异，Data Catalog 为此也做了多版本的兼容。Data Catalog 在元数据存储上使用到了 Hbase/MySQL/ES/Redis，然后在元数据采集和同步场景使用了 Kafka，同时用到了日志服务来提高研发运维效率。

# 4. Data Catalog 公有云遇到的挑战

Data Catalog 经历了一个从 0 到 1 在火山引擎公有云部署并逐步优化和迭代发布 10+ 版本的过程，在这个过程中经历不少挑战，下面将介绍其中比较典型的问题以及我们探索并实践的一些解决方案。

## 4.1 网络和数据安全

为保证网络安全和多租户数据安全，火山引擎上公有云产品部署的环境划分为“公共服务区”和“售卖区”，同时售卖区又分割为若干私有网络（即 VPC），然后公共服务区和售卖区以及售卖区的 VPC 之间都是网络隔离的。

Data Catalog 会依赖一些内部公共服务，这类服务通常都部署在公共服务区，而按照网络和数据安全规范，Data Catalog 作为独立云产品需要部署在售卖区独立 VPC 内，类似的情况 Data Catalog 依赖的数据中台产品也需部署在独立 VPC 内，例如 EMR、LAS 和 Bytehouse。另外，Data Catalog 对外会提供 OpenAPI，外部客户可以通过火山引擎的 API 网关来访问这些 API，但 API 网关服务是在公共服务区，无法直接访问到 Data Catalog 服务，基于以上情况，为了正常对外提供服务，我们需要解决网络隔离问题同时还要保证安全性。

**解决方案：**

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOgPxtBghGuLQkQlpI6EsvFYsljI5JEvlwibnicI0KUwmC7OIb9N92cEsAib7jpp9hsx8nyHG0fUnFldA/640?wx_fmt=png)

* **服务部署：**为了能够在售卖区部署，经过调研我们选择火山引擎提供的容器服务（VKE）和负载均衡（CLB）来进行基础服务部署和构建，其中 CLB 提供四层负载均衡能力，容器服务是高性能 Kubernetes 容器集群管理服务。Data Catalog 基于容器服务提供的无状态负载（Deployment）、定时任务（CronJob）、服务（Service）等云原生容器管理功能进行基本服务和调度任务部署，同时也使用火山引擎的存储和中间件，以上组件均在同一个 VPC 内，能够保证网络连通以及数据安全。
* **网络打通：**为解决上文所说的网络隔离问题，经过调研我们使用了公司通用的网络代理服务（PLB/Shuttle），该网络代理可做到网络打通的同时保证四层网络流量的安全，从而达到我们和各依赖方如公共服务（API 网关、IAM 等、独立部署的云服务（EMR/LAS 等）的网络连通目标。
* **数据安全：**火山引擎部署环境做网络隔离，主要是保证安全性，我们虽然使用网络代理打通网络，但是仍需保证各个环节的安全性，考虑到服务间交互都是通过 HTTP 请求，我们对和外部交互的接口都增加了 SSL 和双向认证的机制，同时在安全认证方面，我们没有使用 Nginx 或 Java 原生的方案，而是借助于火山引擎内部安全服务中的 ZTI 团队的 envoy 组件来实现，同时使用 sidecar 模式和我们后端服务容器集成部署，既降低了服务端部署改造成本，也解耦了服务端业务逻辑和安全认证逻辑。

## 4.2 多租户适配

这里先对多租户相关概念做一些解释：

* **租户：**一个客户、公司、个人开通或购买了火山引擎的云产品，火山引擎就会通知对应的服务提供者，对应云产品会感知到他的开通，这个客户就是这个云产品的一个租户，实际场景可以类比于一个公司是一个租户，不同的公司是不同的租户。
* **多租户服务：**云服务要为多个租户提供服务，需要做到租户隔离，保证各租户的访问控制、数据、服务响应等各方面的使用都是隔离的，彼此互不感知互不影响的。要做到租户隔离，就需要云服务能通过逻辑或物理隔离的方式来将各租户对应数据和访问隔离开来，避免互相影响。

此前，在字节跳动内部实践中不存在多租户场景，所以面向公有云用户服务时，Data Catalog 针对支持多租户服务的能力，需要进行专门适配。

**解决方案：**

Data Catalog 在元数据存储层借用了 Apache Atlas 的设计与实现。Atlas 的底层使用 JanusGraph 做图引擎，JanusGraph 是基于 Gremlin 图查询语义实现的计算引擎，而社区版 Atlas 不支持多租户场景。我们通过在 Atlas 上增加 JanusGraph Partition Strategy 适配，实现存储层租户逻辑隔离。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOgPxtBghGuLQkQlpI6EsvFYJVnXBicEMQMAfQ3nyuOI9JdZoPxynG5gV8j1DAayyCZrEYTVkXVXlMg/640?wx_fmt=png)

参考以上示例，JanusGraph 的 Partition Strategy 可以支持设置的 read/write Partition 的 value，并保证只读/写指定 Partition 的数据，从而达到数据隔离，我们将租户信息和 Partition Strategy 相结合，实现了多租户场景下读写数据的逻辑隔离，保证了数据安全性。

## 4.3 内外部功能一致

Data Catalog 在字节跳动内部已打磨多年，产品形态和技术架构比较成熟，但随着公有云部署和 ToB 产品迭代，因内部外基础服务差异和 ToB 引入新的使用场景和上下游组件导致内外部产品功能和技术实现的差异也越来越多。

在前几个版本中，我们尝试使用独立的代码分支和版本来支持 ToB 功能，避免内部新功能对 ToB 产生影响，但我们发现随着版本差异越来越大，代码和功能的合并和兼容就变得非常困难，在其中一次整体代码合并时，出现了好几千的文件 diff 和上百处 merge conflict，我们花费了一周时间多的时间合并代码和进行多环境测试回归验证，最终完成了合并。功能和代码的不一致已经成为影响研发效率和需求交付进度的很重要因素，必须要进行优化。

**解决方案：**

我们主要从产品功能和代码版本两方面来处理内外部一致性问题：

**产品功能**

* **产品功能的标准化：**原则上所有功能都应做到内外部一致，只允许部分功能点的实现区别。我们期望能将各功能都进行标准化，基础模块和通用能力（如元数据模型、搜索、血缘）原则上需保持内外一致，内外部依赖或需求场景差异较大的功能（如元数据接入和采集、库表管理）改造为标准化流程，将差异部分尽量减小，做到只通过配置、插件、版本控制工具等方式就能适配，减少研发和运维成本。
* **明确的一致性规划：**从模块到功能点逐个对比内部外实现情况，制定长期 roadmap，明确差异点的支持排期，并提高对齐内部功能的工作优先级，逐步减少差异。
* **新功能的兼容性：**新功能的设计需考虑内外部一致性，包括产品的交互和研发的技术方案都需考虑外部场景并明确兼容方案，原则上对特殊场景定制化功能都需考虑通用场景适配，尽量保持多环境的兼容性。

**技术实现**

* **统一的代码分支管理规范：**原则上内外部的代码是一致的即统一的分支。具体来说，不管域内外功能都需兼容多环境并在多环境验证才能合并代码，外部如公有云在发版周期中会基于内部主分支代码（如 master 分支）创建一个新的 release-x.x.x 分支，进行回归验证和公有云上线，同时线上持续使用 release-x.x.x 分支以保证线上环境稳定，release-x.x.x 分支需定期合回主分支。新的版本会继续基于主分支开发，并持续保持该规范。
* **明确的发版规划：**根据实际情况，内部通常迭代比较敏捷发版频率较快，而外部通常要求稳定性，会定期发版（如每月一个版本），考虑到发版周期的差异，我们会以外部固定周期为标准，细粒度控制需求评估、功能开发、QA 测试、回归测试等各环节所在时间段，明确封板时间，降低内外部互相影响。
* **一致性意识和自动化多环境验证：**通过多轮分享和培训在技术团队内部对齐一致性意识，清楚内外部差异点 FAQ 等，另外，如上所说新功能技术设计方案需明确多环境兼容性。同时，引入自动化的多环境验证环节，尽早发现不兼容或不一致的问题，减少人工判断和测试的成本。

## 4.4 OpenAPI

在 DataLeap Beta 版本发布之后，有内外部客户在试用，当时就有客户提出 OpenAPI 的需求，但在 Beta 版本我们还未支持 OpenAPI。公司内部有 OpenAPI 规范和平台，Data Catalog 也借助相关平台实现了内部的 OpenAPI，但是 ToB 场景的公共平台不同且会遇到 ToB 场景特定的问题（如安全认证、多租户、API 开通计费等），需要综合考虑来对外提供解决方案。

**解决方案：**

如前文介绍，火山引擎内部公共服务有 API 网关的通用服务（TOP），并有若干 API 发布规范，Data Catalog 调研了该 API 网关并解决以上核心问题来支持 ToB OpenAPI。以下介绍一下主要流程和关注点：

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOgPxtBghGuLQkQlpI6EsvFYbHgliazyt3rqZ3q1CJ7NMTnWOC7iakVibpfZsnAfkg8x1ZeOkXMUcNWgQ/640?wx_fmt=png)

**API** **管理**

* Data Catalog 借助于 API 网关管理 OpenAPI，包括注册和开通、访问控制、限流等。
* API 规范：火山引擎 OpenAPI 有明确的参数规范，Data Catalog 也需符合该规范，但因内部 OpenAPI 参数格式不同，需做兼容，考虑到新 API 的支持成本，借助于 Spring 的 Interceptor 和 Advice 以及定制 JSON 序列化和反序列化逻辑，实现了自动的参数格式转化，降低 API 格式兼容的开发成本。
* 访问控制：火山引擎作为云服务提供商，使用业界规范的 AKSK 密钥管理规范，API 使用者需创建 AKSK 并通过该信息来访问 API 才可通过访问控制，而 API 网关会通过 IAM 进行鉴权，通过后会给服务提供者也就是 API 注册者透传用户的身份（如租户 ID，用户 ID），方便 API 提供者使用。
* 安全认证：处理 API 网关提供的基础鉴权，Data Catalog 也增加了更多机制来保障安全性，包括双向认证、租户开通状态检测等。
* API 文档：对于每一个 OpenAPI 都根据火山引擎规范编写了详细的参数说明，汇总为一个正式 API 文档，方便用户查阅使用。

**API** **请求流程**

1. 用户或服务通过 AKSK 访问 API，或者通过前端控制台间接访问 API。
2. API 网关通过 IAM 进行鉴权，将识别到的用户身份通过 HTTP header 透传给服务提供者。
3. 服务提供者接收到请求并通过 HTTP header 获取用户身份，进行下一步处理。

# 5. 总结

火山引擎 Data Catalog 产品是基于字节跳动内部平台，经过多年打磨业务场景和产品能力，在公有云进行部署和发布，期望帮忙更多外部客户创造数据价值。目前公有云产品已包含内部成熟的产品功能同时扩展若干 ToB 核心功能，正在逐步对齐业界领先 Data Catalog 云产品各项能力。

文中提及的内容其实还有继续优化的空间，以及随着客户的使用，还有面临一些新的问题，包括多租户性能优化、服务稳定性保障等，我们都在持续探索和解决，期望能更好的支持 ToB 客户的业务诉求并实现商业价值的同时，提供优质稳定的服务和丰富的扩展能力。

# 6. 附录

* 火山引擎大数据研发治理套件 Dataleap 使用文档 （https://www.volcengine.com/docs/6260）
* 火山引擎 Data Catalog 数据地图使用文档 （https://www.volcengine.com/docs/6260/71696）
* 火山引擎产品使用文档 （https://www.volcengine.com/docs）
* JanusGraph Graph Partitioning （https://docs.janusgraph.org/advanced-topics/partitioning/）
* [干货 | 字节跳动构建 Data Catalog 数据目录系统的实践（上）](https://mp.weixin.qq.com/s?__biz=MzkwMzMwOTQwMg==&mid=2247492653&idx=1&sn=2a74b3c1908049ad320a9b2b1b8e202e&scene=21#wechat_redirect)
* [干货 | 字节跳动构建 Data Catalog 数据目录系统的实践（下）](https://mp.weixin.qq.com/s?__biz=MzkwMzMwOTQwMg==&mid=2247492870&idx=1&sn=e6ef09b149b17b7105300087abee158a&sce...