---
title: TSN(车载时间敏感网络)概述
url: https://mp.weixin.qq.com/s/flQivI9EI4PLzkOiLgnF6Q
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:21:40.763619
---

# TSN(车载时间敏感网络)概述

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDIfxVvJoTTvaunuo0RaRQxmhEAunPV3Z4z8VunCYboxcyYvwCFCjiaa54S1xQUOOgmfUOd0AZPb9YiaY8iaticzER6IFniaenibcG8o/0?wx_fmt=jpeg)

# TSN(车载时间敏感网络)概述

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247568414&idx=2&sn=e8421575011428f2d73cc0b393889274&scene=21#wechat_redirect)

**01**

**什么是 AVB/TSN**

智能网联汽车正成为高度互联的移动数据中心，以太网成为车内通信主干，但传统以太网的串行传输和尽力传输（Best Effort） 机制，无法保证数据传输时延、抖动的确定性，难以满足自动驾驶、高分辨率音视频传输对时间敏感的控制要求。

为解决以太网同步稳定传输问题，车载以太网引入AVB（音视频桥接）/TSN（时间敏感网络） 技术，二者是一脉相承的技术体系，TSN 在 AVB 基础上完成功能扩充，核心定位在 OSI 模型第二层数据链路层，新增时钟同步、延迟控制、资源管理、可靠性等标准，让以太网具备确定性传输能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDTs7JWgvriaEJFjsllnv2FnssdNugAibZ84Isb6vPxyPOo1VzoAXADTT6X3X6YtwJmhuqP15kOzE6uxZHXEmVJWvHVFHTA5OAfY/640?wx_fmt=png&from=appmsg)

图片来源:IEEE 802.1 TSN – An Introduction

**AVB/TSN 技术发展关键阶段**

1. **AVB 技术引入：**2005 年 IEEE 802.1 工作组成立 AVB 任务组，制定以太网架构下音视频传输协议集，解决实时性、低延时和流量整形问题；2009 年 AVnu 联盟成立，推动 AVB 市场化和设备互操作性。
2. **AVB 向 TSN 扩展：**2012 年 AVB 任务组更名为 TSN 任务组，应用场景从音视频领域拓展至工业自动化、车载网络等，实现以太网确定性性能升级。
3. **TSN 标准完善：**IEEE 制定了时间同步、数据流调度、网络配置等一系列标准，形成完整的 TSN 技术体系，可支撑各类时间敏感型应用需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA3ibDxxgm0XHPfsxtdB29nPNtYFvkriatg7X3wvicb3M0NBJxXhEI1uR9qjDP4Gp7hx3gFrjPqUhrR1kibzbk6CXmI7vTiaqHkyoH8/640?wx_fmt=png&from=appmsg)

图片来源:

Vector\_Webinar\_Solution\_Ethernet\_20181114

**02**

**车载 AVB/TSN 协议**

TSN 由 AVB 演变扩展而来，二者协议框架存在差异，开发者可根据需求选择不同标准组建网络。以下为核心协议分类及关键内容介绍：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCLD7hd8NdVvgRft6QB3l1QzfcrLo1Lf4I9TT29NniaEJd8oXaiaaC7CVhGcKCfAbDeGibAKkgzQrddSNLoLJvstibUlqLxRtm4y14/640?wx_fmt=png&from=appmsg)

**2.1 传输协议：IEEE 1722（AVTP）**

IEEE 1722 也叫音视频传输协议（AVTP），属于链路层传输协议，核心作用是将音视频数据封装为适配链路层传输的格式，分为两个版本：

* 2011 版本：仅支持音视频（AV）流传输；
* 2016 版本：同时支持 AV 流和控制数据传输。

该协议核心概念为呈现时间（Presentation Time）：让不同网络位置的接收设备缓存数据，直至所有设备均接收到数据并到达预设呈现时间，实现音视频同步播放，解决多设备播放不同步问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA8uBOMY4QLSdulU4eXhXXO6cibn8fWOL5e2iaqsqEMb23qR1BBdjplWZDoFMNGYBvgZYzRuuoLFWnBXfZdkQbpLfPBibOgWsmVlo/640?wx_fmt=png&from=appmsg)

**2.2 时间同步协议：IEEE 802.1AS（gPTP）**

呈现时间的实现依赖统一时间基准，因此引入通用精确时间协议（gPTP），该协议以 IEEE 1588（PTP）为基础优化简化，定义在数据链路层 MAC 子层，减少协议栈缓存延时不确定性，7 跳内网络节点同步精度可达 500ns（100ppm 晶振）。

**核心机制**

1、主时钟（Grandmaster，GM）：作为全网时间参考源，汽车行业中一般为静态配置（通用场景由 BMCA 算法动态选举），其他节点需与 GM 时钟对齐。

2、同步关键路径：主时钟同步信息的分发、点对点链路传播延迟的测量。

3、5 类核心报文：

* Sync（同步报文）：事件型，发送主时钟时间信息，收发端记录时间戳用于时钟频率和传输延迟计算；
* Follow\_Up（跟随报文）：通用型，补充 Sync 报文，提供更精确的主时钟时间；
* Pdelay\_Req（对等延迟请求报文）：事件型，请求从设备返回响应报文，测量链路传输延迟；
* Pdelay\_Resp（对等延迟响应报文）：事件型，携带 Pdelay\_Req 接收时间戳，用于延迟计算；
* Pdelay\_Resp\_Follow\_Up（对等延迟响应跟随报文）：通用型，补充 Pdelay\_Resp 的发送时间戳，完成延迟测量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBO9oTN7ftib9lfZdQicWicvsMm47q0VjBlhiaTFiccE5kCEwWG0hDewAdROf3gO9vAibs3HjoJqlXoE0bXsXx5ibibzxbrPUgzDg8Ixlc/640?wx_fmt=png&from=appmsg)

测量对等延迟时间(即GM->Slave延迟，假想GM与Slave间隔5公里的延迟)

**2.3 QoS 相关协议**

QoS（服务质量）通过技术手段控制数据传输优先级，保障关键数据的带宽、延迟、丢包率等指标，核心流程为：帧接收→过滤监管→流量整形→队列管理→传输选择→帧发送，以下为车载场景核心标准：

1. **802.1Qav-2009：**提出基于信用的整形方法（CBS），按优先级将数据分为时间敏感流和普通流，为不同队列分配信用值，通过信用值的动态变化控制数据传输速率。
2. **802.1Qbv-2015：**即时间感知整形器（TAS），在网桥 / 终端设备的每个队列增加门控，通过门控列表控制门的开关（开 = o / 关 = C），实现关键帧的定时精准发送。
3. **802.1Qbu-2016+802.3br-2016：**协同实现帧抢占机制，802.3br 定义快速 MAC（eMAC）和可抢占 MAC（pMAC），802.1Qbu 基于此实现：非关键帧（pMAC）传输时，若关键帧（eMAC）到达，可中断非关键帧传输，优先发送关键帧，完成后继续传输非关键帧，降低关键帧延迟。
4. **802.1Qch-2017：**提出循环队列转发（CQF），将时间片分为均等的奇偶间隔，偶间隔接收报文、奇间隔发送报文，大幅降低传输延迟的抖动。

**2.4 安全相关协议：IEEE 802.1Qci**

该协议核心为流过滤和监管机制（PSFP），可防止带宽违规、设备故障和网络攻击（如 DDoS），通过三大功能实现流量管控：

1. Stream Filter（流过滤）：根据流 ID 和优先级，为不同帧分配对应的过滤、监管策略；
2. Stream Gate（流门控）：通过门控时间调度表，对数据流进行定时管控；
3. Flow Meter（流计量）：实时监控数据流流量，当流量突增可能影响其他流时，对流量进行整形恢复。

**AVB 与 TSN 核心协议框架对比**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAUN1E9MGudthAhRjyaT3mhPibbjjLC5jQJxficuiamR8euzVmicv3qqzDOskn4O8zA2ORWbNKOsGDIAF19CIbzc18PaLdQmwpPa2Q/640?wx_fmt=png&from=appmsg)

**03**

**车载以太网 TSN 应用场景**

TSN 凭借低延时、高同步、高可靠、高带宽的特性，成为车载以太网的核心技术，广泛应用于多媒体、车辆控制、数据诊断等场景：

**3.1 多媒体传输**

是 AVB/TSN 最直观的应用场景，满足车载信息娱乐系统对带宽和实时性的高要求：

1. 音视频同步：基于 802.1AS 实现微秒级时间同步，消除音视频播放延迟，提升沉浸式体验；
2. 高带宽传输：稳定支持 100Mbps 传输速率，远高于传统 CAN 总线的 1Mbps，可同时传输多路高清视频流；
3. 低延迟低丢包：通过 802.1Qav 的 FQTSS 机制保障时间敏感流优先传输，端到端传输延迟可降至 2 微秒以下。

**3.2 车辆控制与安全**

为 ADAS（高级辅助驾驶系统）和自动驾驶提供核心通信支撑：雷达、摄像头、激光雷达等传感器产生的海量数据，可通过 TSN 实现高带宽、低延迟、高可靠的实时传输，确保控制指令和环境感知数据的快速、准确交互，大幅提升驾驶安全性。

**3.3 数据诊断与车联网**

1. 远程数据诊断：TSN 为车辆故障诊断数据提供稳定传输通道，实现远程实时诊断，提升车辆维护效率；
2. 车联网通信：作为车联网的通信基础，满足车与车、车与路、车与云端的低延迟、高可靠性数据交互需求。

来源：

https://hayppmuscle.blog.csdn.net/article/details/144064796?spm=1001.2014.3001.5502

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicHdaQsibvoH8dLYIIcT5YQibwbnuZn1MLCOMydw2SMKWbibsLpooeE2jgCt8FABvsVmlJZO5PO00Ryw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561756&idx=2&sn=f9b8c214978537f47cccba736cdb5bfd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8D...