---
title: TSN技术：开启工业控制网络确定性传输与低延迟新时代
url: https://mp.weixin.qq.com/s?__biz=MzAwNTgyODU3NQ==&mid=2651129443&idx=1&sn=a490e4c3ff8d28a5964b7edafb6f04d9&chksm=80e71cd3b79095c5d1bccb5602ca207b2519a5ad28da3599383117e82febe98d7ef263f2a1b1&scene=58&subscene=0#rd
source: 威努特安全网络
date: 2024-12-07
fetch_date: 2025-10-06T19:39:44.772931
---

# TSN技术：开启工业控制网络确定性传输与低延迟新时代

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vEkwp3V9UtvKma2KcEKl8Nuib74VpAGjwiazamxCkkRZd5Eqc4TcR3N3YuwHSiclCfwHRLR71lmyUHWGPqeQjnpuw/0?wx_fmt=jpeg)

# TSN技术：开启工业控制网络确定性传输与低延迟新时代

原创

产品与解决方案部

威努特安全网络

# ![](https://mmbiz.qpic.cn/mmbiz_gif/vEkwp3V9UttO1byVSbuod03z4vTwBZa0vVS7nrOUUlibUbNn1ovF2nB91AkwkHCVibGutqLqEZB0oNzHCUGqzzeQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

✦

✦

**背  景**

✦

在工业4.0时代，互联网技术（IT）与运营技术（OT）的结合为制造业带来了数字化转型的巨大优势。通过连接生产设备、车间、企业管理等各个层面，并部署边缘计算服务，可以实现数据的采集、传输、可视化和分析，从而推动智能制造的发展。然而，在推动工业物联网和工业4.0的过程中，IT与OT的融合面临不少挑战，主要包括两点。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBseTsKPalvIEuxvoFibdjPgo9fvOmKoUPzvtfOEF5s2c1gfthEVpVNJrw/640?wx_fmt=png&from=appmsg)

图 1 工业物联网整体架构

**首先，数据传输的周期性与非周期性问题。**OT的控制任务通常是周期性的，需要稳定的周期性网络传输机制，如轮询机制，以确保关键控制数据的及时传输。而IT网络则更侧重于大容量数据的传输，如文件、图片和视频等，采用的是IEEE802.3标准和CSMA/CD冲突监测机制。这种差异要求网络能够同时支持周期性和非周期性数据的传输，而传统的网络技术很难满足这一需求。

**其次，实时性差异也是一个重要挑战。**对于需要微秒级或毫秒级响应的运动控制任务，网络必须具有极低的延迟和抖动。而IT网络通常对实时性没有特别要求，这导致了IT与OT网络在设计和操作上存在显著差异。

为了解决这些问题，**TSN（时间敏感网络）技术**应运而生。通过TSN技术，工业物联网和工业4.0的推进得以实现更深层次的IT与OT融合，为制造业的数字化转型提供坚实的技术基础。

✦

✦

**TSN技术以及关键特性**

✦

TSN是一套由IEEE 802.1工作组开发的协议标准，协议本身具有很高的灵活性，通过增强以太网的确定性和可靠性，确保数据能够实时、确定且可靠地传输。TSN的核心组件包括时间同步、数据调度和系统配置，这些组件共同工作以实现网络的实时通信功能。

表1 TSN标准协议

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBsZrB898NibyH5JQeAIo4jIeloBmCicE1xpgNiaibPZ0x9xlV3ibRYnAxibqyg/640?wx_fmt=png&from=appmsg)

***1***

**时间同步技术实现**

TSN通过时间同步来确保流量的延迟保证，这是其关键特性之一。时间同步能够进行流量控制和管理组件，提供精确的有界延迟，以及为TSN应用提供几乎无阻塞和低时延抖动的传输。时间同步一般分为频率同步和相位同步。

频率同步也称为时钟同步。频率同步指两个信号的变化频率相同或保持固定的比例，信号之间保持恒定的相位差。如图2所示，两个表的时间不一样，但是保持一个恒定的差（6 小时）。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBsdFbbHaF1XgfwAZLCtdU1icjoiaV7lC6lWDxPn8qVKkOpgAc4M9Ypgr6Q/640?wx_fmt=png&from=appmsg)

图 2 频率同步

相位同步是指信号之间的频率和相位都保持一致，即信号之间相位差恒定为零。如图3所示，两个表每时每刻的时间都保持一致。相位同步的前提是频率同步，所以相位同步也称为时间同步。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBsFibAA2AsDqRBqLeF6FibyWQj0pS0YlDw8XhQ5Mg5RbAJYfxAgDEhvM0g/640?wx_fmt=png&from=appmsg)

图 3 相位同步

***2***

**数据调度技术实现**

TSN的流量调度主要分为两大类方案：一是基于时隙化调度的方案，另一是基于QoS的调度方案。时隙化调度方案要求全网进行时间同步，而TSN的数据转发技术能够为时间敏感的业务流提供有界时延，即确保时延的上界，这样的技术对于保证工业自动化中关键任务的准时执行至关重要。

***3***

**系统配置技术实现**

TSN的配置模型主要分为三种：全集中式配置模型、混合式配置模型和全分布式配置模型。

全集中式配置模型依赖于集中式网络配置控制器（CNC）和集中式用户配置控制器（CUC）。在这种模型中，CUC代表数据流的发送方（Talker）和接收方（Listener），将用户需求信息传递给CNC。CNC根据这些信息进行计算，并将网络配置参数下发给网络中的各个二层桥接设备（Bridge）。Bridge根据收到的配置信息，采用相应的策略转发数据帧。CUC和CNC可以是独立的实体设备，也可以作为软件功能模块嵌入交换机系统中。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBs9oOrDgIfib66P3DYk4MzMz9YdxkdYnCsefjeibLibcmLPH9Vwtcd8WWTA/640?wx_fmt=png&from=appmsg)

图 4 全集中式配置模型

全分布式配置模型不需要CUC或CNC。在这种模型中，Talker使用资源预留协议，携带用户需求信息，逐跳传输至Listener。路径上的Bridge获取用户需求信息，并判断是否可以为该流预留资源。如果Listener愿意接受Talker的信息，它将发送资源预留协议定义的报文返回Talker。如果任何Bridge判断带宽不足以预留资源，资源预留过程将失败。成功后，Talker可以开始发送业务数据给Listener。这种模型需要定义一种资源预留协议的功能。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBsITKPPic9xWfIFSvyicX1VzNPkS4FwS1B9EZdJjMCycHdlONnkwz6253g/640?wx_fmt=png&from=appmsg)

图 5 纯分布配置模型

混合式配置模型结合分布式用户配置和集中式网络配置。在这种模型中，Talker和Listener直接将用户需求信息告知CNC。CNC进行计算后，将网络配置参数下发给相关的Bridge。Bridge根据配置信息转发数据帧。与全集中式配置模型的主要区别在于用户网络接口的不同，以及用户侧是CUC还是Talker/Listener。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBsDyYmWh6fG2icVBIgBiaOibd0Ebiblnb86CvibENcXmtLeoiaxCntLxWY3e2Q/640?wx_fmt=png&from=appmsg)

图 6 混合式配置模型

✦

✦

**TSN技术优势**

✦

***1***

****基于时间片的流量调度，****避免传统网络的“流量饿死”****

基于时间片的流量调度通过为不同类型的网络流量分配特定的时间窗口来确保关键数据的及时传输。这种技术避免传统网络中可能出现的“流量饿死”问题，即某些低优先级的流量因为高优先级流量的持续占用而导致无法传输。

在图7中，TSN交换机转发模式展示如何通过时间片调度来实现流量的公平分配。TSN交换机为不同的流量类型（如背景流量P7、PLC控制流量P6和摄像头视频流量P0）设定不同的时间窗口。这些时间窗口确保即使在高优先级流量存在的情况下，低优先级流量也能在其分配的时间段内得到传输机会。例如，高优先级7的时间窗为0-500us，高优先级6的时间窗为500-800us，而低优先级0的时间窗为900-1000us。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBsH8pK1YWfx1ZoNBer7k2cgribCzjcMvg0AkMia0ibs1GAXh2HDuHnGxGQw/640?wx_fmt=png&from=appmsg)

图 7 基于优先级的时间片调度演示方案

这种基于时间片的调度机制，在工业自动化和控制系统中，可以保证控制命令和反馈数据的及时传输，确保系统的稳定运行和精确控制。

***2***

**提供us级的周期调度，解决周期性和非周期性数据共存问题**

在传统的网络中，周期性数据（如工业控制信号）和非周期性数据（如视频流）往往共享同一网络资源，这可能导致周期性数据的延迟或丢失，影响系统的实时性能。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBsicxg0oGnZaVDoicPF7MWDLO2bkvcHYOdNbfhbOt7azJWJJKzWDjibJkZg/640?wx_fmt=png&from=appmsg)

图 8 周期调度图示

在图8中，可以看到TSN交换机为不同优先级的流量（P7、P6、P0）设置不同的时间窗口。这些时间窗口的最小时间精度为8纳秒（tick=8ns），基本调度宽度可以设置为1到1023个tick，例如设置为128个tick，即1024纳秒或1微秒。这样的精细调度允许周期性数据在预定的时间内传输，而不会受非周期性数据的影响。此外，调度周期可以设置为基本调度宽度的整数倍，如1毫秒，以适应不同的网络需求。

***3***

**能够平衡实时性与大负载数据传输需求**

TSN的关键特性之一是提供确定可靠的消息传递，主要通过时间同步和流量调度来保障，由IEEE 802.1AS和IEEE 802.1Qbv等标准实现，可以为工业级应用提供确定性传输、低延迟和高质量的服务保障，推动工业4.0背景下的应用场景和对未来工业自动化及物联网通信的深远影响。

✦

✦

**TSN行业应用**

✦

***1***

**TSN在制作业工业网络中的应用**

TSN技术通过精确的网络时间同步、流量调度和网络配置等关键技术，为时间敏感型数据提供低时延、低抖动和低丢包率的传输服务，从而支持工业自动化和控制系统的实时性和确定性需求。

在OT网络内部，TSN技术根据网络架构和交换机在网络中的位置，可以分为工厂级、车间级、现场级应用。工厂级主要涉及核心层设备，部署于工厂级机房，实现工厂内部各车间之间的互联互通。车间级则包括汇聚层设备，部署于车间级机房，实现车间内部不同产线之间的互联互通。现场级则涉及接入层设备，部署于生产现场，实现现场设备、传感器等通信接口的通信协议转换。

IT层作为企业信息系统的核心，负责处理和分析来自OT网络的数据，并通过云平台、数据中心等基础设施，实现数据的集中管理和智能决策。TSN技术在IT层的应用，确保了关键业务系统如供应链管理（SCM）、企业资源规划（ERP）、制造执行系统（MES）和客户关系管理（CRM）之间的数据传输具有高可靠性和实时性。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBsc2LXwtrCZvMQqhwCIcbGjJsWLYOmPUxOR35B1wMbTjXdEf0h2RrqBw/640?wx_fmt=png&from=appmsg)

图9 TSN应用示意图

***2***

**TSN在智能驾驶神经网络的应用**

随着汽车智能化和网联化的发展，车内网络需要更高的带宽来处理日益增长的数据量。传统总线技术因通信速率较低（10k到10M）已难以满足需求。以太网凭借其高带宽优势，特别是IEEE P802.3ch项目推动的1G以上车载以太网标准化，成为解决方案。

目前，车载网络架构中ECU和总线系统为主，辅以少量以太网链路。未来，随着技术进步，更多功能将集成到域控制器，以太网链路比例将增加，形成以高带宽以太骨干链路为核心的集中式处理架构。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBsicCnicPzEibv7KEyvxtmsLDEfhRGeBsPyFPx7X09UU0ochoWuqeG58ysg/640?wx_fmt=png&from=appmsg)

图10 车载网络架构的一种演进方式

TSN技术通过改善传统以太网的转发特性，为不同优先级的数据流量提供端到端有界时延和更小的抖动，满足车载以太网对高可靠性和实时性的需求。这使得车载网络能够在同一链路上高效传输音视频等媒体信号和控制信号，推动车载网络向更高性能演进。

***3***

**TSN在轨道交通信号系统中的应用**

地铁信号系统，作为地铁系统的“神经中枢”，负责指挥和控制列车运行以及实时传递列车信息。然而，当前面临的挑战是主控单元需要以30ms、50ms或100ms的间隔向牵引、制动、大屏等子系统发送控制报文，这些报文在时间上有时会发生重叠，并且在经过复杂的链路传输后，数据抖动增加，导致控制周期变得不可控，产生延时，使得接收终端的不确定性增加。

TSN技术通过精确的时间同步和流量整形技术，能够减少数据传输的延迟和抖动，提高整个地铁信号系统的稳定性和效率。通过TSN技术，地铁信号系统能够实现更加精确的列车控制和调度，提高地铁线路的运行效率和运输能力，同时也为乘客提供了更加安全、高效的出行体验。

![](https://mmbiz.qpic.cn/mmbiz_jpg/vEkwp3V9UttRuE4X65A4epQesKXibYeBsEOUIQmpjvZQDz3tgcHF3FWAklIQOfg4KU1K0aZDT9hfUpj6Rl9vOng/640?wx_fmt=jpeg&from=appmsg)

图11 轨道交通信号系统

***4***

**TSN在智能变电站中的应用**

在智能变电站中，为保障继电保护和测控装置等IED装置的二次链路稳定运行，可以采用IEEE802.1AS协议来为测控终端提供精确的时间同步服务。通过这种方式，可以预防因过程层交换机故障而导致的保护功能和自动化功能中断，使用IEEE802.1Qbv协议进行调度，确保关键的GOOSE报文和SV报文能够及时传输。这种调度机制允许在确定的时间间隔内优先处理这些报文，加强智能变电站的自动化和保护功能，从而保障电网的安全运行。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBsOoIhK1cqowmnzZmwnHJOywN1RdJGgmdIJAscSPO2aLiapl4NHs85RvA/640?wx_fmt=png&from=appmsg)

图 12 变电站示意图

✦

✦

**威努特TSN交换机**

✦

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttRuE4X65A4epQesKXibYeBs7a0QNF6HKVVNAK8PI1PKibaIduuMAXXQ7kvmw5tzWic73jl2IvFsIU0Q/640?wx_fmt=png&from=appmsg)

图 13 威努特TSN交换机

威努特TSN交换机是一款为工业环境设计的高性能网络设备，支持关键的TSN协议标准，确保时间敏感型数据的低时延、低抖动和低丢包率传输。具有如下特点：

* 支持TSN相关协议标准：IEEE 802.1AS PTP/IEEE 802.1Qbv/IEEE 802.1Qcc(SRP)/ 802.1Qav
* 支持CNC集中网络配置
* 支持IEEE802.3/802.3u/802.3x/802.1D/802.1W/802.1P/802.1Q标准
* IP40防护等级
* 支持宽温（-40℃～85℃）
* 符合工业四级电磁兼容性要求

威努特TSN交换机以其低延迟和高实时性，在工业自动化、智能制造、智能交通、医疗和能源管理等领域可以得到广泛应用。其通过时间同步和优先级调度关键数据流，确保设备间的精确协调。这种技术对于提高生产效率、优化交通管理、提升医疗诊断准确性和能源利用效率至关重要。

![](https://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9UttO1byVSbuod03z4vTwBZa0QPXxjXLFBAUUpkYOYz78KpuM3Lic13XvZSLwMRqwPWx2RcI41KF0fcw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_jpg/vEkwp3V9UtvKMyMOEIBicUdfszasytMDQ1WUymnSvTZuTib5nIYuzaqriabu2mxOyfz9n0qv5EicrxZjs0GjjQBpxA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)渠道合作咨询   田先生 15611262709

稿件合作   微信:shushu12121

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vEkwp3V9Utvy3S0ykmxlskz7ythOsDsm6zNNibia3qASGEZwDcBXVAwThSasvpoWbn2NSVHiaFicF6G1G3HkrOarBA/0?wx_fmt=png)

威努特安全网络

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消...