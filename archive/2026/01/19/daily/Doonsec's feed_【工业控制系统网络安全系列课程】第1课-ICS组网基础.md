---
title: 【工业控制系统网络安全系列课程】第1课-ICS组网基础
url: https://mp.weixin.qq.com/s/40t_sjYW0MbaZe5JbXhshg
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:32:27.121043
---

# 【工业控制系统网络安全系列课程】第1课-ICS组网基础

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UodAreoVp6WiaUctkGia0z5AHtJ3uIUop8CuxaQHmMz3O6nojj0oKibwqdg/0?wx_fmt=jpeg)

# 【工业控制系统网络安全系列课程】第1课-ICS组网基础

原创

老付话安全
老付话安全

老付话安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/7UnMUNqGIz071DWbJdrzpdJpDxlHDFtnMDlvK8TeibfibdovgH3vMKfIloQibicL6TTiaXQib28nacKJv8qx7AJNnm8g/640?wx_fmt=gif)

**点击蓝字**

**关注我们**

关注我，带给你不一样的精彩

世界因你的沉淀而出彩

**始于理论，源于实践，终于实战**

**老付话安全，每天一点点**

**激情永无限，进步看得见**

![](https://mmbiz.qpic.cn/mmbiz_png/lB1oaPhdMNvxZ67rEjeQWUFqwCxiacBblWHRAxzuoMfYPQXETZ7Y5bsGSLBPy2QGDKIbia74ruAWgJXhWkMlGgkA/640?wx_fmt=png)

**严正声明**

本号所写文章方法和工具只用于学习和交流，严禁使用文章所述内容中的方法未经许可的情况下对生产系统进行方法验证实施，发生一切问题由相关个人承担法律责任，其与本号无关。

特此声明！！！

本文字数：

5052字

阅读时间：

13分钟

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmkPpdz6eLJ8DdlDNUBqveKtiacEVRcfsmdBFkicRIT6Jx5UjOKE0ia3ovA/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmWXkibyqRGYwGCtfKsZVPyXib1Hnia07via66RuViaMOMicKXfLQeRKxgd9Ow/640?from=appmsg)

ICS组网

在【工业控制系统网络安全系列课程】之前，我们花了大量时间按照行业分类和业务逻辑详细阐述了各个行业的组网拓扑。无论哪个行业，其核心组网逻辑结构如下：

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoMvflmMdXCrxZMkpClSAiciaefVHXeQxtfEicsicbGnqMwgndxPmO1Sl8yA/640?wx_fmt=png&from=appmsg)

ICS 使用通信基础设施收集有关某些过程或功能的信息，并将数据发送回操作员。操作员通常以图形格式查看数据，评估过程的运行状态，并调整系统以获得最佳性能。

服务器、HMI 和工程工作站从现场控制器获取信息，并以描述过程中发生的情况的方式显示数据。用户界面，通常称为HMI，使操作员能够实时或接近实时地查看过程的操作视图。这三个组件通过网络或通信渠道链接起来。

* **现场设备** 是指直接与物理过程交互的传感器（输入，如测量温度、压力）和执行器（输出，如阀门、电机），它们是控制系统与真实世界之间的接口。
* **现场控制器** （如 PLC、RTU、PAC 等）负责接收来自现场设备的数据，执行控制逻辑，并将处理后的信息上传给监控层（如 SCADA 服务器、HMI），同时接收来自操作员的控制指令下发给现场设备。它们通常部署在靠近工业现场的现场层。

ICS 中的数据流：

数据流可能因供应商而异，但基本流如下：

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoiblAogmIdyxWxF6Tq7nOlUiaX4TzRh2xHyakzYt8FcnL8m3ltItjviaew/640?wx_fmt=png&from=appmsg)

现场控制器整合数据并将此信息传输到HMI 组件。例如，现场设备将实时过程数据发送到历史数据库中， 将硬件错误状态发送到配置数据库，将实时过程数据发送到HMI。

配置数据库，该工作站或服务器有时作为第三方应用程序（包括历史数据库）的 HMI 或平台执行双重任务。配置数据库通常存储用于设置和配置 ICS 中各种组件的信息。从该站，信息被传输到网络上的相应设备， 以便正确配置它们。 HMI 站使用构建在配置数据库站或其他工程工作站/服务器上的显示器显示来自现场控制器的数据。这是操作员对系统的主要视图。此视图显示中的错误可能会导致操作员做出错误的决策。

工业通讯协议

工业通讯协议列表：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 程序自动化 | ▪BSAP | ▪CC-Link | ▪CIP | ▪CAN |
| ▪CANopen | ▪ControlNet | ▪DeviceNet | ▪DF-1 |
| ▪DirectNET | ▪EtherCAT | ▪Ethernet Global Data(EGD) | ▪EthernetPowerlink |
| ▪EtherNet/IP | ▪FINS | ▪FOUNDATIONfieldbus | ▪GE SRTP |
| ▪HARTProtocol | ▪HoneywellSDS | ▪HostLink | ▪INTERBUS |
| ▪MECHATROLINK | ▪MelsecNet | ▪Modbus | ▪Optomux |
| ▪PieP | ▪Profibus | ▪PROFINETIO | ▪SERCOSinterface |
| ▪SERCOSIII | ▪SinecH1 | ▪SynqNet | ▪TTEthernet |
| ▪RAPIEnet |  |  |  |
| 工业控制系统 | ▪OPCDA | ▪OPCHAD | ▪OPCUA | ▪MTConnect |
| 智能建筑 | ▪1-Wire | ▪BACnet | ▪C-Bus | ▪DALI |
| ▪DSI | ▪KNX | ▪LonTalk | ▪Modbus |
| ▪oBIX | ▪VSCP | ▪X10 | ▪xAP |
| ▪ZigBee |  |  |  |
| 输配电通讯协定 | ▪IEC60870-5 | ▪DNP3 | ▪IEC60870-6 | ▪IEC61850 |
| ▪IEC62351 | ▪Modbus | ▪Profibus | * ICCP |
| 智能电表 | ▪ANSIC12.18 | ▪IEC61107 | ▪DLMS/IEC62056 | ▪M-Bus |
| ▪Modbus | ZigBee Smart Energy2.0 |  |  |
| 车用通讯 | ▪CAN | ▪FMS | ▪FlexRay | ▪IEBus |
| ▪J1587 | ▪J1708 | ▪J1939 | ▪Keyword Protocol2000 |
| ▪LIN | ▪MOST | ▪NMEA2000 | ▪VAN |

典型工控协议分析

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UolPSpm3TicJ0TicnSuMVhAnfpRiasmZ1jVtcT81yorVu0xegpuN0xvKj7Q/640?wx_fmt=png&from=appmsg)

TCP连接是基于字节流的：UDP是基于报文流的。

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoeByBYpxed9G6zgX6VHHaes2WRRzNsn8kEGCibxEvvpNkBzOXKhyKroQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UohmXNGItyW4Ztzh4NV9VicicJrHxcUibPEAZKY1PM0oz1nCq6XyjylzNcA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoK6Fn81DFKG5PlGUJMT2nk2o2cYOSsbic46PxuWsWKeq6MK5SbPvjXQA/640?wx_fmt=png&from=appmsg)

特定于DNP3 安全身份验证（国内使用较少，了解即可）：

•它在开发时考虑了三个主要威胁：欺骗、修改和重播

•它保证了消息的真实性和完整性

•它与串行和基于IP 的部署兼容

•它为主动模式提供了一个选项，在该模式中，来自单个质询的数据可用于验证许多后续消息，以最大程度地减少在带宽受限环境中的影响

•它不提供消息的机密性，这意味着不涉及加密，公用事业公司开始依赖进行调试和维护的工具仍应兼容

•它利用质询-响应模型，其中质询可以由主站或分站发起

•保护被视为关键的特定应用程序服务数据单元 （ASDU） 的设备问题挑战

•版本 5（包含在IEEE-1815-2012中的当前版本）不向后兼容以前的版本。它是唯一推荐的版本，它提供了使用对称或非对称（公钥）加密远程更改用户更新密钥的可选方法。

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61Uo8Wxb1H0l8ia43MOEyKfDItzdibJXzk3buXTfvD7FrpjSibjdIkWKsZ8Xg/640?wx_fmt=png&from=appmsg)

Inter-Control Center Protocol（ICCP 或IEC 60870-6/TASE.2）有助于在局域网和广域网上无缝交换 时间关键型数据。ICCP是当今电力行业最有能力、最广泛采用的开放式通信协议。

ICCP（或者TASE.2协议）可用于交换各种实时数据和历史数据，包括状态、测量值、调度数据、操作命令等等。ICCP协议以制造报文规范（MMS或ISO 9506）为基础，同时支持客户端和服务器端角色。ICCP和MMS支持出站、入站以及出站/入站TCP/IP连接—不受客户/服务器角色限制。

安全 ICCP 是指基于传输层安全 (TLS)隧道的ICCP。换言之，它采用基于证书的认证机制，通过额外的协议报文签名确保安全。

ICCP协议主要用于电力系统等工业领域的**控制中心之间**（通常使用端口102/TCP）进行数据交换。其核心机制是**客户端与服务器之间的实时数据映射**，以此实现信息同步。在安全方面，现代ICCP协议已集成数字证书认证与通信加密，可有效保障传输的完整性与机密性。此外，随着工业互联网的发展，一些**非传统的SCADA网络**也开始将ICCP协议集成到其系统中，以实现跨系统的数据互操作。

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoBu5eiaCDdk9ncP8zo7ygtmpEDhClhlSfkxEdrzn1tgrnI4PlIPAj8CQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoPyHVENZR07Q1PJakH6QyKLNzFNicabCBBHojXlHNW5wxskySic7LEcuw/640?wx_fmt=png&from=appmsg)

当前电力系统中，对变电站自动化的要求越来越高。我们看到变电站已经从过去的有人值守到少人值班，到现在集控站模式下的无人值守，大量的保护、测控信息通过自动化系统采集和上送。而随着状态检修、程序化操作等新的工作方式的采用和推广，除了传统的电流、电压、开关位置等开入量上送及少量的开关控制信号下行以外，装置的自诊断信息以及更多的操作功能都需要通过变电站自动化系统来实现。鉴于IEC60870-5时代的规约混乱，不同厂家装置间直接通讯几乎不可能实现的现实，使得我们不得不寻找一个更好的变电站通讯规约来替代。变电站通信网络和系统协议IEC61850标准草案提出了变电站内信息分层的概念，将变电站的通信体系分为3个层次，即变电站层、间隔层和过程层，并且定义了层和层之间的通信接口。在变电站层和间隔层之间的网络采用抽象通信服务接口映射到制造报文规范(MMS)、传输控制协议/网际协议(TCP/IP)以太网或光纤网。在间隔层和过程层之间的网络采用单点向多点的单向传输以太网。变电站内的IED(Intelligent Electronic Device 智能电子设备,测控单元、保护装置、智能终端等都可视为IED)均采用统一的协议(GOOSE,GSSE,SV等)，通过网络进行信息交换。

客户端每次收到新的遥测、遥信和电度数值时，自动更新到共享内存区；SCADA 进程 可访问并获取到这些数值。 SCADA进程可实时向共享内存中写入遥控命令、读取定值命令、修改定值命令、读取 定值区命令、修改定值区命令、读取软压板命令、修改软压板命令、文件操作等命令；客户 端实时检查共享内存中的命令状态，收到上述命令后，将命令插入到装置的通讯命令队列中 进行操作，命令操作完成后将结果（成功或失败）返回给共享内存，如果超过 30 秒没有结 果返回，将向共享内存中写入超时的返回结果；SCADA检测到返回结果后，进行进一步的 处理。 客户端还将各个通讯装置的通讯状态（包括 A网和 B 网）实时刷新到共享内存，共SCADA进程使用。 为了方便 SCADA进程对客户端进程进行守护，客户端每秒向共享内存中刷新一次运行 计数，SCADA可根据此计数来判断客户端是否在运行，以便实行守护

详见往期内容：

[【大话工控安全】工业控制系统基础知识之常见工业协议家族电力专用协议IEC104、IEC61850（一）](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247485087&idx=1&sn=7fea5288873c418328d4dc7f8fd1e097&scene=21#wechat_redirect)

[【大话工控安全】工业控制系统基础知识之常见工业协议家族电力专用协议IEC104、IEC61850（二）](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247485228&idx=1&sn=be74c1eafb068f931657c39dcfa4e88e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UofnqtopvRH8rczXImXdKLibq55mullytw23WEjoibW0miaPBDOYQTYrciaw/640?wx_fmt=png&from=appmsg)

Modbus既用 于命令和控制，也用于设备级通信。Modbus是一种应用层协议，用于与现场控制器进行通信。

Modbus通信很简单：客户端向服务器发出单个数据包请求以读取或写入数据;服务器对请求执行操作，并 返回一个单数据包响应，指示请求的成功或失败。

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UofqWVSZkXZ6ia56NWRW8mwMNsHruKmgJ8sPOdUsV6EgM54CVvNwnIK3A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoKLpAyMKpIkFRFhsMcBNHPzSMnpIFIrkBDek5wTUGI3yzkaPSQTjYXg/640?wx_fmt=png&from=appmsg)

参考：

[【大话工控安全】工业控制系统基础知识之常见工业协议家族MODBUS](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247484961&idx=1&sn=0f710a9ae3de79c17a3f9d8fdc0928b6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UojvqK1hyT6SE2uwNloFfkKtxPH77MP4ibnVzYG7tXmvVLkscDUyc3Z4w/640?wx_fmt=png&from=appmsg)

工业自动化的互OPC 统一架构 （UA） –基于开放标准，例如SOAP/XML OVER HTTP、UA TCP。操作性标准https://opcfoundation.org/

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9OxZibq5awj3ZxEw6micic61UoQIPhQszdlKh9FicTRDf7EarWrej0MZT75IPyaYNzGZvaxTovQxiak8Kw/640?wx_fmt=png&from=appmsg)

1、OPC DA 缺点：

比如基于DOM的OPC DA使用的动态端口分配，端口不固定，让防火墙难以确定, 这只是对以前旧设备而言，现在防火墙不存在此问题，都支持像咱们公司ALG这样的功能。

DOM/COM也可以生成不同级别的事件日志，但日志内容不够详细，只会提供“谁连接上服务器”

2、OPC UA 优势：与平台无关，可在任何操作系统上运行，为未来的先进系统做好准备，与保留系统继续兼容，配置和维护更加方便

基于服务的技术，可见性增加，通信范围更广，通信性能提高

3、OPC UA特点：（OPC UA的端口都是唯一的）

访问统一性： OPC UA有效地将现有的OPC规范...