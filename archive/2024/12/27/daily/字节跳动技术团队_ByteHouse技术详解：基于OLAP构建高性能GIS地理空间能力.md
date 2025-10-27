---
title: ByteHouse技术详解：基于OLAP构建高性能GIS地理空间能力
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247512573&idx=1&sn=edd6005b9d497d447674c0716c74a152&chksm=e9d37a1fdea4f309c1bc93bdf8613b5cc59b1f937fffad54dad6127c7fed0a6f0a9bc280cf7d&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-12-27
fetch_date: 2025-10-06T19:38:08.547785
---

# ByteHouse技术详解：基于OLAP构建高性能GIS地理空间能力

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh6S19ta8ZQOFwKZB6sYPictrwjSyRaoyLJWXfPnT7zSObTwxSjAhZ12SlBoPXSrOia1RshPHYtRy5w/0?wx_fmt=jpeg)

# ByteHouse技术详解：基于OLAP构建高性能GIS地理空间能力

字节跳动技术团队

在数字化时代，地理空间分析（Geospatial Analytics）成为辅助企业市场策略洞察的重要手段。无论是精准广告投放，还是电商物流的效率优化，都离不开对地理空间数据的查询、分析和可视化处理，以便助力企业更好决策。

> **以一家连锁咖啡店为例：**
>
> 该店想要在新城市开设分店，并希望确保新店铺的位置能够最大化利润。
>
> 首先，商家通过收集新城市的地理数据，包括人口分布、交通流量等，建立了一个详细的地理信息数据库。然后，商家利用空间数据分析工具，对这些数据进行了深入分析。
>
> 通过人口分布数据，商家发现新城市的一些区域人口密集，潜在顾客群体较大。同时，交通流量数据显示，某些区域的交通流量较大，意味着这些区域的顾客流动性较高，有利于店铺的曝光和吸引顾客。
>
> 此外，商家还分析了同行情况竞争对手的位置，以避免在已有众多同类型店铺的区域开设分店。空间数据分析帮助商家识别了那些既有足够潜在顾客，又相对较少竞争者的区域。
>
> 基于这些分析结果，商家最终确定了新店铺的位置。开设分店后，由于选址精准，店铺迅速吸引了大量顾客，销售额和利润均实现了预期目标。

以上案例离不开对地理空间数据库的支持。一些传统的地理信息系统数据库具备丰富的地理空间对象结构、成熟的空间索引能力，在导航、旅游、智能城市等典型应用场景中被广泛使用。

但随着实时分析报表等OLAP市场的扩大，地理空间分析也作为新的增值特性被业界几大OLAP主流产品所推广。OLAP+GIS能力在满足用户地理空间数据分析的基础上，还能在数据体量大、实效性要求高的情况下，满足业务高性能查询的需求。

作为火山引擎推出的一款OLAP引擎，ByteHouse近期发布了高性能地理空间分析GIS能力，为位置洞察、人群圈选等场景提供高性能地理数据分析服务。本篇内容将从技术实现角度，详细介绍ByteHouse如何集成GIS能力，并通过benchmark测试，展示ByteHouse与市场同类产品相比（ClickHouse、StarRocks、PostGIS、DuckDB）的性能情况。

# 应用场景和价值

**位置洞察：** 例如，在给定中心点的情况下，展示半径X公里内的圆内其他商家的同一商品的客流分布、经营情况等，有助于帮助商家客户洞察竞争对手情况，为定价策略和市场定位提供数据支持。

**作战地图：** 给定特定多边形，观察多边形内部商家的供给和客流量，为即时零售业务的配送优化提供决策依据。例如：生活服务的即时零售业务需要观察实时的配给。

经过我们对行业上相关业务场景的需求分析，商家或者销售代理等客户需要的是一种“对某个地理空间（多边形/圆）内的对象进行多种业务维度的分析和决策能力”。从整个执行链路来看，链路不仅含GIS的二维空间数据筛选，还有经典OLAP的聚合和关联分析等逻辑，因此可以总结出一层GIS+OLAP链路的抽象。从性能优化角度来看，OLAP优化器有必要去结合GIS的特性来进行适配，提升端到端的总体性能。

# 详细介绍

在关键性能层面，ByteHouse GIS在列式小批组织的数据结构上引入RTree等二维空间索引能力，并在CPU硬件层面实现了二维空间函数的性能优化，整体提升了端到端性能。在功能层面，兼容OGC标准，支持导入标准GIS文件格式，目前已支持超过50个主流的空间函数。更值得一提的是，我们还在探索在我们自研的优化器上结合GIS特性适配，如在高效的多表关联上适配GIS等，以及GPU硬件层面优化二维空间函数。

## 二维空间索引

回顾业务场景：给定一个查询窗口（通常是一个多边形或圆），返回包含在该查询窗口中的物体。

如果要提升查询性能，读取的数据量通常是比较关键的，那取决于：

1）数据的排序方式 2）数据读取的粒度 3）索引

**社区ClickHouse数据组织**

ByteHouse 是火山引擎基于开源 ClickHouse 进行了深度优化和改造的版本。ClickHouse 社区版直接按照Order By latitude, longtitude里面的纬度进行排序，再按照经度排序。

因为经度上相距很远的数据可能被放到一个mark，而查询是一个多边形和圆，查询的模式和数据的组织不匹配从而造成严重的读放大问题，导致数据局部性较弱。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh6S19ta8ZQOFwKZB6sYPictpNpDxogYRVR8tYfKGcvmprf1DxKuwdMwIhasZGtWJt1oW8kWppZDrw/640?wx_fmt=other&from=appmsg)

**ByteHouse空间索引：Google S2 + R tree**

ByteHouse GIS 通过使用Google S2 [3]库将所有的经纬度点从二维转换转换成一维，并排序。排序后的经纬度点效果如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh6S19ta8ZQOFwKZB6sYPictiaT2F2vKtqHpYfrw9rMUS8IcGnlsYb6iaVV4PwzgL5hvvsMvTsoibVa7Q/640?wx_fmt=other&from=appmsg)

图片来源：[3]

由于ByteHouse的数据是按照列式存储，相比于传统的行级别索引，我们会对S2排序后的经纬度数据，先按照小块粒度切分，再利用RTree来索引每个小块数据。这样，基于小块粒度的RTree索引的存储开销更小，加载和查询效率更高。给定一个查询的多边形或圆，RTree能快速索引到匹配的数据块。由于每个数据块内的经纬度数据是按照二维层面聚集，这样使得相邻的点在二维空间上更加紧密，数据局部性更好。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh6S19ta8ZQOFwKZB6sYPictr94ddd8L8okuxoxpGjELJG9CUXLqgsafNvrfQSc9QozwKZZja8mJww/640?wx_fmt=other&from=appmsg)

ByteHouse GIS索引结构

针对某个具体场景中给出的一个圈选范围，需要返回范围内的所有POI (Point of Interest)点。下面两幅图分别展示了传统经纬度排序方式（Order By latitude, longitude）和ByteHouse GIS索引排序方式（Order By point）的圈选效果。其中，图中黑色的框代表了所有数据块，红色部分代表了圈选命中的数据块。

从结果中看出，传统经纬度排序命中的范围会横跨很广的纬度，造成读取许多无用的数据。而按照ByteHouse GIS索引搜索出的数据块只集中在北京地域，正好满足圈选所需的最小数据块集合。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh6S19ta8ZQOFwKZB6sYPictO8p5oHkAWlWEL73b7DWCRj1nZSGgfBKb8QbAc8qXibXHFjtjfEMwICQ/640?wx_fmt=other&from=appmsg)

传统经纬度排序方式的搜索效果

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh6S19ta8ZQOFwKZB6sYPictOSdw2SkmaVHEqJxHdCpR1fwOyAyub47ITRicFlnffl0dZ9ibvIZibrNzQ/640?wx_fmt=other&from=appmsg)

ByteHouse GIS排序方式的搜索效果

## 兼容OGC标准

### 数据类型

按照OGC标准，新增7种几何类型，包括Point、LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh6S19ta8ZQOFwKZB6sYPictNHq2rP3vDEWoISuur5d1QH9YA8mn9NLgTT4FTn8SAzbjSmSoyvkVPg/640?wx_fmt=other&from=appmsg)

存储层面上，传统GIS数据库（例如，PostGIS）将几何数据序列化为Blob类型，读取时需要额外花费反序列化的开销。而ByteHouse GIS则按照数值数组和列式方式存储，减少存储量、序列化和反序列化开销。

### 空间函数

功能上，ByteHouse GIS目前已支持超过50个通用的空间函数，下面表格列举了几大函数分类。另外，我们针对个别高频使用的空间函数进行了基于列式数据存储格式的性能优化。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh6S19ta8ZQOFwKZB6sYPictSsggqhGoM4t0tGbMGyOZYia2ejlLo2UyZUEbO6iaBmMxfyoRIedpzp9g/640?wx_fmt=other&from=appmsg)

### 存量数据迁移

同时，ByteHouse GIS也支持常见数据格式的导入与导出，包括WKT、WKB、GeoJson、ShapeFile、Parquet、CSV和Arrow等文件格式。

# Benchmark 测试

## 标准NYC Taxi数据集

为了说明性能效果，我们基于两个关键的 GIS 函数，使用 NYC Taxi 数据集，选取纽约的 3 个地理区域，将ByteHouse、ClickHouse、StarRocks、PostGIS、DuckDB进行了性能对比（以上对比的版本参照发文日期的最新版本）。

在本次测试中，我们选取了两个关键的 GIS 函数：`ST_DistanceSphere` 和 `ST_Within`；并使用 NYC Taxi 数据集（Size：21GB；条数：169,001,162），数据集将纽约拆分成多个地理区域（比如 Brooklyn，Manhattan），本实验选取其中 3 个不同大小的地理区域（按照过滤度区分：zone 1、zone 2、zone 3）进行了性能对比。

1. **ST\_Within 函数性能对比**：在 `ST_Within` 函数的测试中，从查询延迟来看，OLAP引擎的整体查询延时低于1s，由于二维空间索引和向量化的数据处理方式，ByteHouse查询延时最低；当前版本的DuckDB由于没有空间索引，同时采用了BLOB的存储方式，数据扫描和反序列化开销比较大，查询性能不好；采用行存的PostGIS在大范围搜索的情况下（zone3），虽然有索引加持，依然会有较重的读放大，查询延时超过6s。从每秒吞吐量来看，ByteHouse通过索引降低了数据读取和反序列化开销，展现出明显优势，其次为PostGIS，在小范围搜索（zone1和zone2）情况下表现优秀。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh6S19ta8ZQOFwKZB6sYPict3aakMs34GyF7VrrXwncWmiaQjac7RhYkPjUrdeYh7fmm7aZtvSUwYeQ/640?wx_fmt=other&from=appmsg)

ST\_Within函数性能对比

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh6S19ta8ZQOFwKZB6sYPictRBPYXlmYWcIqHe5qOf96pCXQvZ1XbK2A8icAEzYz42UPL1iciaEBVjiaNA/640?wx_fmt=other&from=appmsg)

ST\_Within每秒处理空间查询数

2. **ST\_DistanceSphere 函数性能对比**：在 `ST_DistanceSphere` 函数的测试中，在处理相同数据集和查询时，ByteHouse具备二维空间索引过滤和向量化计算的优势，性能控制在0.1s以内。ClickHouse和StarRocks同样具备较好的0.1s-1s内的较好性能表现。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh6S19ta8ZQOFwKZB6sYPicttEicMu4PEmf2iajtvO8tAVkQZ04g5Y1khK25t9F3Mk6rdQVKxbvDTstQ/640?wx_fmt=other&from=appmsg)

ST\_DistanceSphere 函数性能对比

基于标准数据集的测试结果来看，对比传统的PostGIS：

* ByteHouse GIS将OLAP和GIS结合了起来。在OLAP层面，ByteHouse对比PostGIS已经有计算优势。
* 在GIS层面，空间数据对象按照列的方式存储，而非序列化成字节数组，在存储上能够做到更加紧凑并节省空间，在计算上能够充分发挥向量化的优势。
* 特别是在空间函数层面，可以利用硬件的并行化能力提速。

对比社区ClickHouse：

* ByteHouse GIS兼容OGC标准，场景上能够水平替换之前PostGIS的场景。
* 另外，空间索引能力可以大大减少ClickHouse的读放大的现象。
* 还有，ByteHouse自研的优化器同样具备适配GIS特性的能力。

## 业务数据集

在电商场景中，ByteHouse GIS能力不仅满足平台商家运营快速分析商家经营状态、管理商家的需求，还将数据读取量减少超过50%，进一步降低了磁盘IO以及计算带来的CPU开销。

# 总结

本文具体拆解了ByteHouse GIS能力的技术实现方案，并将ByteHouse、ClickHouse、StarRocks、PostGIS、DuckDB五款数据库产品的性能进行分析和比较。

结论总结如下：ByteHouse在`ST_DistanceSphere` 函数及`ST_Within` 函数的查询延迟低于其他产品，查询吞吐量更高，具备比较明显的性能优势。

需要注意的是，性能测试结果取决于多个因素，在实际应用中，需要综合考虑各种因素，如数据规模、可扩展性、易用性、稳定性、安全性以及是否需要与其他系统集成等其他因素进行综合选择，并对数据库进行合理的配置和优化，以获得最佳的性能表现。

对于专注于地理空间数据分析的项目，PostGIS能提供了全面的地理空间功能支持，是一个比较好的选择。然而，如果地理空间数据只是大数据分析的一部分，且如果性能是首要考虑因素，那么ByteHouse、ClickHouse、StarRocks、DuckDB是合适的选择，其中ByteHouse GIS 功能不仅提供了高性能的地理空间分析能力，还具有易于使用、实时分析和云原生等特点，这使得企业可以更灵活、更高效地利用地理空间数据。

# 参考

1. PostGIS: https://postgis.net/
2. OGC: https://www.ogc.org/standard/sfs/
3. Google S2: https://s2geometry.io/
4. Geos: https://libgeos.org/
5. https://clickhouse.com/docs/en/sql-reference/functions/geo/coordinates
6. Cuda: https://developer.nvidia.com/cuda-toolkit
7. https://github.com/rapidsai/cuspatial
8. https://github.com/arctern-io/arctern
9. https://halfrost.com/go\_spatial\_search/

👇点击**阅读原文**，立即领取《火山引擎ByteHouse云数仓产品白皮书》

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

向上滑动看下一个

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