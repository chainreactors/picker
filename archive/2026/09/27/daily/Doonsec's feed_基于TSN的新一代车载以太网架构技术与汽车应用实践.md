---
title: 基于TSN的新一代车载以太网架构技术与汽车应用实践
url: https://mp.weixin.qq.com/s/IzT49psFa4pJe7IAsj9_xw
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:53:42.776672
---

# 基于TSN的新一代车载以太网架构技术与汽车应用实践

# 基于TSN的新一代车载以太网架构技术与汽车应用实践

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**01**

**前言**

TSN（Time-Sensitive Network，时间敏感网络）是IEEE 802.1 TSN工作组制定的一系列数据链路层协议规范的统称，旨在构建低延迟、低抖动、传输时间确定的以太网局域网，是传统以太网针对汽车等专用场景的功能增强技术，可有效适配高端实时通信场景的传输需求。

**1.1 TSN技术发展历程**

早期以太网交换机普遍采用半双工传输模式，带宽仅100M，传输延时约5ms，单线路最大传输距离为100m。随着千兆以太网与全双工传输技术的迭代普及，千兆交换机成为局域网主流设备，默认所有端口隶属于同一广播域，数据包通过硬件MAC地址表完成查询与快速转发，网络传输效率大幅提升。

伴随以太网交换技术日趋成熟，其应用场景逐步从局域网拓展至城域网等广域场景。1980年2月，IEEE 802委员会正式成立，专职制定局域网与城域网通信标准，其中IEEE 802.1工作组核心负责以太网体系协议标准的研发与迭代。

1991年，针对大规模交换机部署后产生的网络冗余链路、环路干扰等问题，IEEE 802.1工作组发布802.1D STP生成树协议；1998年进一步推出RSTP快速生成树协议，彻底解决了多厂商设备组网的环路故障问题，大幅提升了以太网组网的稳定性。

依托802.1D协议的技术支撑，大规模用户组网的技术条件全面成熟。1999年，IEEE 802.1工作组发布802.1Q VLAN协议，作为802.1D的重要补充。该协议可通过虚拟网络标识对大规模园区、城市组网用户进行精准划分，突破了传统电信组网与城域网接入的IP地址限制，适配规模化组网应用。

进入21世纪，以太网全面普及，高清音视频等多媒体实时传输需求持续攀升。为此，IEEE于2006年成立AVB工作组，迭代完善802.1系列技术标准，从带宽保障、延时约束、精准时钟同步三个维度扩充以太网功能，构建出高画质、低延时、时间同步的音视频局域网传输方案，满足多媒体业务的传输需求。

随着工业4.0落地与车联网技术快速迭代，工业控制、智能汽车领域对实时以太网技术的需求爆发式增长。2012年，原AVB工作组正式更名为TSN工作组，在继承AVB成熟技术体系的基础上，聚焦工业、车载实时通信场景，持续迭代完善技术标准，为高端实时以太网技术的行业落地与创新发展奠定核心基础。

**02**

**TSN系列规范**

TSN系列技术规范体系完善，标准来源主要分为两类，一类源于音视频、传统通信领域的成熟技术积累，另一类来自芯片厂商、设备企业的技术落地实践与创新探索。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaByTMntibtDsGjogQKvgiaagraWo6OnJ40WO9qWIE9zIssXqV7wQhOEQA0XKOv0Fkpg2fcAM3UTibrVicH8RUUdVdJNDUL7ZUib6QdE/640?wx_fmt=jpeg&from=appmsg)

**2.1 TSN协议规范分类**

目前已正式发布的TSN系列规范，按核心功能可划分为四大模块：时间同步、调度延时、传输可靠性、网络资源管理。

**2.1.1 时间同步**

时间同步核心规范为802.1AS及802.1AS-Rev，该标准基于数据链路层，构建以交换机为核心节点的时钟同步机制，是IEEE 1588精密时间同步协议的轻量化优化版本，更适配车载网络高精度、高实时性的通信传输要求。

当前行业主流应用为2011版本协议，可实现单域、多域时钟同步，能够满足以以太网为骨干网的车载电子电气架构基础设计需求，适配常规车载实时通信场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaA34lq8sQALdLib1uA8EibAaWAYkP8OhCCkwcgEe6ic0ib73rHq7o13W5ibfKJBicTBE33cGXuA3etTGNstR1DMaxXfkgBTiaAqscfzCw/640?wx_fmt=jpeg&from=appmsg)

802.1AS多域分布

最新迭代的2020版本802.1AS协议，新增时钟冗余、时钟传输路径冗余机制，为智能汽车功能安全设计提供了统一、可靠的时钟同步解决方案，进一步提升车载网络时钟系统的稳定性与容错性。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaBt9NhSNY61Szc6y5qTUjdJLXrD7nGlPVAKVEYciaEpEGDRkZG4wWtEba4D2ntYvk7LS9OvdU5rcksmy4OicicB1YvgxbDWk5MRyI/640?wx_fmt=jpeg&from=appmsg)

802.1AS时钟实时冗余

**2.1.2 调度延时**

802.1Qbv是TSN延时调度的核心协议，在交换机多输出队列严格优先级调度机制（报文优先级由VLAN或IP标识划分）基础上，通过门控列表GCL（Gate Control List）管控各队列的开关时间窗口，实现时间感知整形器TAS（Time-aware Shaper）的核心功能。GCL通常配置8~16组调度规则，可根据业务需求灵活定制调度策略，精准保障不同优先级数据帧的最大传输延时，实现网络传输延时确定性与带宽稳定性的双重管控。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaA0UpJHMr7esbXMGIQ7MDk0mzJ3O7Z4fx4XIldoPAxf9INTyTryicqHvjzuUdo21AibEfuicHOMjTpXsGH1RdE61jgNU5v88MbjLI/640?wx_fmt=jpeg&from=appmsg)

802.1Qbv GCL调度

为保障单个时间切片内的报文完整传输，802.1Qbv协议设置了保护带（Guard Band），其最大长度可配置为标准以太网MTU最大值（约1500字节），会产生约12.5μs的固定延时损耗。为优化带宽利用率、消除无效等待时延，行业引入802.1Qbu协议形成互补优化。

802.1Qbu协议将数据帧划分为可抢占帧与快速帧，交换机端口以报文优先级为依据完成分类，高优先级快速帧可抢占低优先级未传输完成的可抢占帧，以此压缩高实时业务的传输延时。协议支持自定义最小抢占帧长度阈值，例如设置128字节阈值时，需等待可抢占帧完成128字节传输后，方可触发快速帧抢占传输；待快速帧传输完毕后，再接续传输被中断的可抢占帧剩余数据。

802.1Qbv与802.1Qbu协议协同应用，可在保障链路延时、带宽稳定可控的前提下，进一步降低高实时性报文的传输时延，完美适配车载高速实时通信需求。

**2.1.3 传输可靠性**

802.1CB协议依托交换机硬件复制能力实现数据冗余传输：发送端数据帧可在交换机指定转发端口完成硬件复制，通过多条差异化网络路径传输至目标节点交换机；接收端交换机通过硬件机制自动识别并剔除重复报文，无需软件参与数据校验与去重，不会产生额外算力负载。该机制借助网络冗余拓扑实现数据实时备份，当主传输链路出现故障时，冗余链路可无缝接续通信，保障业务不中断。其额外延时仅为冗余路径中交换机节点的转发时延，约10μs，相较传统通信故障恢复机制，可靠性与实时性优势显著，可充分满足车载高实时、高可靠的通信场景需求。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaD0XIRYD5d9CjeBM2I53BrXic8km6ibym8LowAfpITIQJuhX1fNHGG5g340jV2VicGlvUDEZqicoZbUjbZvdbcKgFNWYs5RsUq5mRU/640?wx_fmt=jpeg&from=appmsg)

802.1CB冗余策略

**2.1.4 资源管理**

TSN资源管理类规范主要定义网络管理协议与通用配置格式，适配灵活组网、易运维的通用网络场景。但该类规范采用动态资源分配策略，与车载网络高稳定性、固定资源分配的核心需求不匹配，因此本文不做详细阐述。

**03**

**TSN在汽车领域的应用**

车载TSN应用体系以802.1AS-Rev时钟同步协议为基础，配套搭载802.1Qbv、802.1CB、802.1Qbu等核心协议，全方位适配智能车载网络的流量调度、实时传输、可靠通信需求。

**3.1 新一代车载网络架构**

未来智能车载网络将采用“中央计算平台+区域控制器”的分层架构，以以太网为核心骨干网搭建环状拓扑结构，为整车智能化、网联化业务提供超大带宽、高连通性的网络支撑。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAc3RYX2fGj3cT5mmhibhgLaV4Pq3nszxYLsKyicicDlO3WCicftBw5rsToXmpianickicTibSxnQQiaXxPJVfcs5m64AcMbic8Ujia9SsQgk/640?wx_fmt=jpeg&from=appmsg)

ZEEKR EE 3.0架构

以极氪EE 3.0架构为例，全新网络拓扑的升级革新，可将整车线束总长度从3.5km压缩至1.5km左右，整车减重100~200kg，助力电动汽车续航提升10%以上。该优化不仅降低了车载硬件损耗与整车能耗，更具备显著的经济效益，同时为汽车行业践行碳中和国家战略提供了重要技术支撑。

**3.2 高精度时钟同步应用**

在极氪全系辅助驾驶、自动驾驶车型中，高精度时钟同步是各类传感器实现环境精准感知、定位与动态响应的核心基础。整车搭载多类感知设备，包含1~9颗激光雷达、1~6颗毫米波雷达、12颗超声波雷达、4~8颗环视鱼眼及侧视摄像头、1颗前视高清识别摄像头、1颗前视DVR摄像头、1颗后视倒车摄像头及1颗DMS驾驶员监测摄像头。依托车载网络节点硬件搭载的802.1AS gPTP时钟同步功能，可将全车传感器时钟同步误差控制在100ns~1μs以内，全面适配车辆高低速全行驶场景的智能驾驶控制需求。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDx2nJWBUGrQG0juianUBLAfJkY9gl9ibGoUnHwg8MtbfiaREQwRg588MBvvcJufbVgkWvaxibTvOtIScicgkDZJ4c3lcOkiabCSBnMA/640?wx_fmt=jpeg&from=appmsg)

车辆自动驾驶传感器分布

**3.3 确定性延时传输应用**

新一代智能车型依托区域控制器的交换机转发能力，完成整车周期性实时数据的高速传输。通过优化适配的802.1Qbv、802.1Qbu协议配置，传统车载CAN网络中10ms、20ms、50ms、100ms周期的控制数据，均可按照抖动误差等级要求，实现分时、分优先级的确定性带宽与确定性延时传输，传输延时稳定控制在100μs~1ms区间，完全兼容传统CAN网络的控制数据转发性能标准。

同时，该技术方案可为毫米波雷达感知数据预留充足实时带宽，保障车联网地图导航、在线音视频娱乐等业务低延迟、流畅运行，成功实现多域智能业务在以太网骨干网架构下的融合落地，为车载多业务协同运行提供优质网络支撑。

**3.4 实时冗余与功能安全应用**

在车载以太网骨干网架构中，功能安全的核心落脚点为通信安全。传统CAN网络具备天然组播特性，单节点故障不会影响其他节点的正常通信，网络容错性较强。

车载以太网采用以交换机为核心的集中式点对点通信架构，依赖端口队列完成报文缓存与通信调度，存在固有短板：若传输路径中的交换机转发节点出现故障，极易中断各区域控制器之间的通信，引发车辆控制风险，影响整车行驶安全。

802.1CB协议精准弥补了车载以太网的通信安全短板，通过硬件冗余通道实现实时数据备份，构建硬件链路与软件流量双重冗余保障体系，可在链路故障时无缝切换冗余通道，有效提升车载通信系统的功能安全等级，保障智能车辆行驶过程中的通信稳定与安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCicbQqAcsO7xwTJ5hic8ibibWbZKfW3aD0k5plwyhtJQLkaDQrr190msMUibPP3IylD75pCwmicsKicOnkQGB88pYT2Qibzd1YQPTRMac/640?wx_fmt=jpeg&from=appmsg)

802.1CB帧复制传输

**04**

**总结**

汽车智能化、网联化、多媒体化的快速发展，推动车载电子电气架构持续迭代升级，衍生出大量创新技术理念与个性化车载应用场景，其技术复杂度与业务广度已远超传统车联网、物联网的应用范畴，对车载网络的实时性、可靠性、稳定性提出了更高要求。

面对智能汽车产业的技术革新与市场挑战，极氪软件及电子中心坚持技术创新探索，基于TSN技术体系研发新一代智能车型电子电气架构，打造搭载ZEEKR OS的中央计算超级算力平台，持续突破车载网络核心技术瓶颈，贴合市场高端化、智能化发展需求，助力汽车产业高质量技术升级与创新发展。

来源：

https://blog.csdn.net/daniel315/article/details/126970885?spm=1001.2014.3001.5502

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OT...