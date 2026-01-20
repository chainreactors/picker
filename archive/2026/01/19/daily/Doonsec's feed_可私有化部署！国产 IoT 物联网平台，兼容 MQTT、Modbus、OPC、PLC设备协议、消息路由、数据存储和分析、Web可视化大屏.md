---
title: 可私有化部署！国产 IoT 物联网平台，兼容 MQTT、Modbus、OPC、PLC设备协议、消息路由、数据存储和分析、Web可视化大屏
url: https://mp.weixin.qq.com/s/w41krQcomS0woM3BF6E61Q
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:32:52.291632
---

# 可私有化部署！国产 IoT 物联网平台，兼容 MQTT、Modbus、OPC、PLC设备协议、消息路由、数据存储和分析、Web可视化大屏

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tnMEWNbfO5dUoISLvdOBWC3ov2WSCGxViaeia1JamZeeTwLOicQZ6YxuyRo0EQMwVM2vIXtfq1pQowNu7EzBltHQg/0?wx_fmt=jpeg)

# 可私有化部署！国产 IoT 物联网平台，兼容 MQTT、Modbus、OPC、PLC设备协议、消息路由、数据存储和分析、Web可视化大屏

原创

.
.

IoT物联网技术

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5d6OfaSic6pmQsMiaprJjkc84Znry1VMHbq9olCsM0n6eiaGT96K67Udtyibdy0z43zyX5bj7EnHqa2kw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> 文末联系小编，**获取项目源码**

**IoT物联网平台**是一套先进的企业级物联网解决方案平台，为万物互联提供可靠安全稳定的终端接入、协议适配、消息路由、数据存储和分析、应用使能等核心功能。面向物联网领域中的终端设备商、系统集成商、应用服务商、能力提供商等，提供高效便捷的设备集成、数据分析和应用开发能力，从而使客户在万物互联的大趋势中牢牢占据领先位置。

* **南向设备接入**，支持 MQTT、CoAP、LwM2M、HTTP 四种协议。提供了硬件边缘网关，适配 TCP、UDP 和 WS 等协议子设备。
* **北向应用系统开发**，以 API 的方式为您提供了各种物联功能组件，使您能便捷、高效地开发设备和应用并将设备和应用接入云端实现互联。
* **控制台**是您的自助开发平台，帮助您快速实现物联网智能产品原型。通过这种高效、直观、近距离的体验，使您能更深入地了解平台的强大服务能力。而且在正式的商务合作之前，一切都是零成本！

**IoT物联网平台**是国内极少数能覆盖阿里云、华为云、天翼云、中移OneNET 等物联网云服务功能的可私有化部署产品，具有以下核心优势：

* 高性能高可靠：支持大规模分布式部署，千万级设备连接和数十万级 QPS 请求处理能力，毫秒级延迟，可支撑海量物联网设备接入需求
* 多协议支持：支持主流物联网协议及插件扩展，并配套若干款边缘硬件网关实现工业协议接入
* 网络透明：支持各种蜂窝网络（2G、3G、4G/NB-IoT） 、有线网络和无线网络，亦能支持 5G 中的 mMTC（海量物联）和 uRLLC（高可靠低时延）两大场景
* 数据持久化和实时分析：内置高性能分布式时序数据库，支持海量数据的持久化和实时分析，也支持与用户提供的数据库、大数据平台或消息列对接，方便用户对数据进行存储与消费
* 规则引擎：提供基于 SQL 的高速规则引擎，支持用户设置复杂规则实时过滤海量数据，减少应用侧压力，使客户聚焦业务开发
* 跨平台可伸缩：既能以数百台规模的超大集群架构运行，也可以在超小配置上运行，并支持以公有云、私有云、物理机及 Docker 容器和 K8S 等方式进行灵活部署

**IoT 物联网平台架构**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5d6OfaSic6pmQsMiaprJjkc84Hs221eYZkA42ktUK2pQICPL8c6B5twCC2W5HttXdgRMW1XLS2RBj0w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

IoT物联网平台本质上是一系列物联网微服务的集合，采用分布式架构，应用程序和服务组件均不存在单点风险，针对不同级别的业务场景可随时扩容，企业无需关心高并发、稳定性等技术难点。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5d6OfaSic6pmQsMiaprJjkc84k7ly0jcWRicicgrdoKXiaXicaZyVPbYQyUXEJnA75sbUDlRSBY9MpZo4Vg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

上图中各层服务负责的功能分别如下：

* **连接服务：**提供设备联网功能，支持设备通过各种无线或有线的通信方式接入网络，并支持各种网络传输协议；
* **设备服务：**提供设备基础管理功能，包括设备的鉴权管理、数据协议解析、消息路由、设备影子数据及元数据管理功能；
* **数据服务：**提供设备数据的基本管理功能，包括设备的上下行日志存储，以及一些数据指标的聚合分析，如平均值、最大、最小值等；
* **使能服务：**提供应用使能服务，主要是为上层或第三方应用提供按规则和条件进行数据订阅和数据转发的服务。包括应用注册、规则引擎、数据流转服务；
* **运维监控：**包括基础的安全服务、控制台和监控服务。安全服务提供基本物联网安全机制；可视化控制台提供IoT OS与客户交互的界面；可视化监控提供服务可用性及风险监控能力。

**物联网平台业务模块**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5dUoISLvdOBWC3ov2WSCGxVMWkFkMh34TP97ibV1LE7dCYIDBID9TQpJ8THdQcL0Oriab0Q8ASricpyQ/640?wx_fmt=png&from=appmsg)

**连接管理服务**

基于 IoT物联网平台的连接服务设备集成接入功能，支持设备通过各种无线或有线的联网方式接入网络，并支持各种网络传输交互协议。

* **通信协议：**2/3/4/5G、Wi-Fi、NB-IoT等
* **传输协议：**TCP、UDP，以及配套的TLS、DTLS
* **应用协议：**MQTT、HTTP、CoAP、LwM2M等
* **数据格式：**消费类设备常用的JSON、工业设备常用的ModBus或其他各种私有格式
* **拓扑结构：**直连设备、网关设备及子设备等

**设备管理服务**

* **物模型：**物模型指将物理空间中的实体数字化，并在云端构建该实体的数据模型
* **设备标准协议解析：**支持制定统一的设备数据协议格式，用于第三方硬件服务商的规范化对接，实现平台对设备数据的标准协议解析
* **状态监测：**支持实时获取到设备的状态快照。支持实时远程控制设备，对于控制结果平台须有准确的反馈和记录
* 支持对设备上下行数据的存储、查询
* 支持对设备报警、故障的存储和查询

**数据处理服务**

服务提供设备数据的基本管理功能，包括设备的上下行日志存储，以及数据指标趋势及聚合趋势分析。基于 IoT平台 的数据服务为分布式海量数据计算平台提供对物联网数据资产管理的能力，支持数据深度价值挖掘。

* SQL接口，易于开发和兼容现有流行框架
* 高速的读写性能和数据压缩能力
* 可将多个时序数据流进行实时聚合计算, 提供强大的流式计算功能
* 将每个设备数据存入消息队列，对外提供数据订阅功能
* 高频数据降采样聚合
* 可视化的运维监测界面
* 支持通用开发环境所需的数据库接口

**应用使能服务**

基于IoT平台的应用使能服务，主要是为上层或第三方应用提供按规则和条件进行数据订阅和数据转发的服务。包括应用注册、规则引擎、数据流转服务。

* **规则引擎：**支持按规则过滤目标数据，包括按设备、按参数及条件的过滤
* **数据流转：**将规则引擎过滤出来的数据发送到目标地址，支持 HTTP 和 MQTT 两种流转方式
* **提供统一API接口**支持业务集成

**可视化管理**

提供可视化界面进行物模型的配置、发布，设备状态查询、远程控制、上下行数据查询、报警/故障查询，并可通过可视化界面进行规则引擎和数据流转的配置。

**物联网平台演示**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5dUoISLvdOBWC3ov2WSCGxVMWkFkMh34TP97ibV1LE7dCYIDBID9TQpJ8THdQcL0Oriab0Q8ASricpyQ/640?wx_fmt=png&from=appmsg)

**设备品类管理**通常描述的是对一个产品下所有设备所具有的共性信息。如产品的制造商、所属单位、外观尺寸、操作系统等。在系统录入产品品类后，创建产品时便可灵活选择所属品类。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5d6OfaSic6pmQsMiaprJjkc84cAy7Qsejtahanvfc53cgL7GLdlCxQKkupsbwcic7AtOz3OjLxR2Jvtw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

**地理分析**主要展示设备地理位置分布，通过左上角下拉选择框可以选择对应的产品进行精细统计。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5d6OfaSic6pmQsMiaprJjkc84RKYnCcW3Kg3vKCb9cQluA8nupjFIvtka3w3alnbTibiadymyLZa9QQxg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

**总体趋势**统计主要统计设备数量随时间的变化趋势，左上角的下拉选择框可以选择不同的设备，默认统计所有设备下的设备数量变化趋势。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5d6OfaSic6pmQsMiaprJjkc84LEgLrT9GnEic8uIruUTZA9aReUgmQcqZxKTG4216SrAe6iclV3Ocib5xw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

**指标趋势**功能表达的是某一设备的具体参数原始值的变化趋势。进行指标分析时，产品、设备、对应参数和时间范围均为必要值。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5d6OfaSic6pmQsMiaprJjkc844v5iav1Dzo1700VV1dVadKJ83LYMkMH89jmicqjIRus756Ue2pUnVRibw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

**指标聚合**是对某一设备的具体参数的原始值进行聚合计算，分别得出此参数在某一聚合力度下的最大值、最小值和平均值。进行指标聚合时，产品、设备、对应参数、时间范围和聚合力度均为必选值。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5d6OfaSic6pmQsMiaprJjkc84ZHtRSHmINztHQlOskt6CtWt3sWYAHPNLHvLMc4y1PVAUdt2TUyBfZw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

工业网关是一款基于物联网架构设计的工业级嵌入式软硬件一体化设备。可实现工业现场各种设备的数据采集，存储，转发，系统维护，域名管理等功能，用户可在PC，手机上使用浏览器进行数据监控和参数配置。该网关可广泛应用于光伏电站，风电站，小水电，配电室，抽油机，灌区，管道，环境监测站，消防监控室，农业大棚，空气监测站,实验室，工控中心，无人值守站等场站监控和园区能源管理系统，各种在线监测系统等。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5d6OfaSic6pmQsMiaprJjkc84icuXocpABDEhkfdfCfE9LIU0gW3TUHjO3TzWfHubK0qH5nAiaUjSoM7Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**物联网平台应用场景**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tnMEWNbfO5dUoISLvdOBWC3ov2WSCGxVgHJoweOt5iafEX3WMHH4O6XIE5OFm4XtTTwXMvwyibU9YVN6RVmJMxzg/640?wx_fmt=jpeg&from=appmsg)

智能建筑：在智能楼宇中，能够管理照明、空调、安防等系统的设备状态。例如，根据环境光线和人员活动情况自动调节照明亮度，根据室内外温度和湿度优化空调运行模式，提高能源效率，降低能耗。同时，实时监控安防设备，如摄像头、门禁系统等，保障建筑物的安全。

智能家居：支持用户远程控制家里的智能设备，如灯光、电视、空调、窗帘、安防系统等。用户可以通过手机应用或其他智能终端，随时随地控制家中设备，实现个性化的家居场景设置，如回家模式、睡眠模式等，提升家居的舒适度和便利性。

环境监测：可连接各类环境传感器，收集温度、湿度、PM2.5、空气质量、水质等环境参数。实时展示数据并根据预设阈值触发相应控制策略，如当空气质量超标时，自动启动空气净化设备，或及时向相关部门发送预警信息，为环境保护和城市管理提供数据支持。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tnMEWNbfO5dUoISLvdOBWC3ov2WSCGxVDXqEm9bn5icTGopT5XTwB4KtULRGoY61y9ZVVCZ7Boa7v4AUg1tdFEA/640?wx_fmt=jpeg&from=appmsg)

工业自动化：可用于监控和控制生产线上的机械设备，实时收集生产数据，如设备运行状态、生产速度、产品质量等。通过对这些数据的分析，实现远程诊断和预防性维护，提前发现设备故障隐患，减少停机时间，提高生产效率和产品质量。

能源管理：适用于电力、水务、燃气等能源领域，对能源生产、传输和消耗过程中的设备进行数据采集与监控。帮助能源企业实时了解能源设备运行情况，优化能源分配，实现能源的高效利用，降低能源损耗和运营成本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tnMEWNbfO5dUoISLvdOBWC3ov2WSCGxVlWoiatcmiaMUfMIVkiaNf8SUdum7LuoaHDiaFRj3jeNJ8WuRwQUwoFkQicg/640?wx_fmt=jpeg&from=appmsg)

智能交通：可应用于交通基础设施和车辆管理，例如实时监测交通信号灯状态、道路流量信息，实现智能交通调度，缓解交通拥堵。还可用于车辆远程监控，获取车辆行驶状态、油耗等数据，为智能物流和车队管理提供支持。

---

如有IoT 源码采购和项目交付需求，请扫码联系小编，微信号: beacon0418

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5f04Y8JFlm3FEtG8Llf70k5nic2LKxBTnnq57QZozVbcl4XITgxgCvm0LyUCBicGQ0uCKbxaynic2rAw/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN4iaZuxem4fsJcVq1icNPbWKX3tn2fNaLMILaMH0RKibLocwse4PQOtw2Ew/640?wx_fmt=other)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454939032&idx=1&sn=5679fa0132dd03f96b7854e02250f5bb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN4nJPPZIh6azfSNld68R6DUJneWzEdAm0vHbaGxD8KIQe6hsIV3gRK9Q/640?wx_fmt=other)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454938828&idx=1&sn=c23447c25873fe4f344373b3b2f5303e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN47gLQy8lk4YYLpQk8BVeZw8sia3DpZKibBxKtV1uBM9d0HmMMZYrSCZBg/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454938751&idx=1&sn=1370c202ad106571ec7053ee732a8458&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN4mGxtr8aB0WoDbARcEnSdribwoaxkBXhbktnCUs9nGWtMjWaNALNxQhQ/640?wx_fmt=other)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454938509&idx=1&sn=5c1328edb68ac69a8eee420e8f062826&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5dibJicMpcVDWcBZMOLVCnPw8ibdqLicqp0TNKiaZsYK80pIleBPUobqmib1RAZL1UPfpCcuSb4zMic5yNQQ/640?wx_fmt=png&from=appmsg)

**往期推荐**...