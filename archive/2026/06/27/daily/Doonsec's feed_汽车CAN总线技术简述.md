---
title: 汽车CAN总线技术简述
url: https://mp.weixin.qq.com/s/tXaosS-2BbYiCeDuaQn9Fw
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:09:23.993086
---

# 汽车CAN总线技术简述

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDF5dc4QVJmllPgzibfwwuPpdBtzR5x4PjibcOpPwz48RFJl1Da7BIXJBo1CY0GgHNypeml7OlY9cia2lKKfgtDBk3kjkKSRQyHia8/0?wx_fmt=jpeg)

# 汽车CAN总线技术简述

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB7rzTTRoj7eDibicG9aAZDibBtZjia8ia5Q3MKRvZBia4GM6jMe06AhUvjBRacsf0Zu5goL4Fw1pF4AFbcTat4vtLTRRp6VdwgKvICU/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247574638&idx=2&sn=6d973f555cee1792a670cc5f6dd0fb48&scene=21#wechat_redirect)

**01**

**CAN的诞生与发展：汽车神经系统的进化**

在之前的文章已经简单介绍过汽车工业的发展和汽车通信，今天就简单介绍一下汽车通信中的非常重要的一个角色——CAN总线。在1980年代汽车电子化革命初期，工程师们面临着一个棘手的难题：随着车辆电子控制单元（ECU）数量激增，传统点对点布线系统已不堪重负。机械式线束不仅导致整车重量增加30%，更因信号干扰引发系统误操作。这种背景下，德国博世公司于1983年秘密启动的"汽车神经系统"研究项目 ，最终催生了改变汽车工业的控制器局域网（Controller Area Network，CAN）协议。

*That’s why Controller Area Network was invented：*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDia7DEC54FZ0C0McmMiahewTIHLia47giabownYNGJus8rx9cQhfQtMfWukxpfYJBmdclwoSqwVle9icZcd7s4ibjibwU1shRrwbQaPI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCKPSnWg5H2xRqvcGkUGqEAKYmOan6MMMsV3SLobEcyP2ial0htJvhNkq89bcou85JOqS5baMoibXrJFoGf1zZxHPwic71BYLox5c/640?wx_fmt=png&from=appmsg)

1991年9月，Philips半导体公司制定并发布CAN技术规范：CAN2.0 A/B。

1993年11月，ISO组织正式颁布CAN国际标准ISO-11898（高速应用，数据传输 速率＜1Mbit/s）和ISO-11519（低速应用，数据传输速率＜125kbit/s）。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAxgPnd0KUZoiaxUTvVRZBibVPWb0dft4RAMGtOyXwqSqZtibKQZJAR8NMLVVu8VnGbQ0BkWc6LKicG0QM6qgP0v6MnKnibO6w2Tb1Y/640?wx_fmt=png&from=appmsg)

作为一种技术先进、可靠性高、功能完善、成本较低的网络通信控制方式，CAN总线广泛应用于汽车工业、航空工业、工业控制、安防监控、工程机械、医疗器械、楼宇自动化 等诸多领域。想要了解更多关于CAN总线的发展史，可以在CSDN搜索关键词：CAN总线发展史。

**02**

**CAN总线工作原理**

**1.物理层与信号传输**

从物理层面来讲，CAN总线是两根线，螺旋缠绕，即双绞线，如图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAUCLNrGiaqvfjbGdEUBmGGFpMLib04sDA2dXMKUBjFO2z8XXfD9TJKArqFYyy2AeS20U7tXm7LcG3TeQ9O9M9Os0awpLh3sYY7s/640?wx_fmt=png&from=appmsg)

我们在生活中较为常见的是网线，由4组这样的双绞线组成：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBliceHOFsn1mibI34rFII67YAEPwywfdVGCMtV6kkE1xIdOjK3QfiaZFtpgOWUWCcFBKABSicUwLPtrcUKxXfbY0P6rtJGWzn2xzk/640?wx_fmt=png&from=appmsg)

那么这双绞线是如何输出信号的呢，CAN总线通过双绞线传输差分信号，其中一根线标记为CAN高（CAN\_High，CAN\_H），另一根线则标记为CAN低（CAN\_Low，CAN\_L）。一般当总线为显性低电平，也就是逻辑0时，CAN\_H为3.5V，CAN\_L为1.5V，此时电位差就为2V；当总线为隐性高电平（逻辑1）时，CAN\_H和CAN\_L此时的电压均为2.5V，电位差为0V，如图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAS6pgUC1WFwZtdkicKFwx8VUcOlOs3Ep0V7go5KzBSoJ7YG4qnHiaadatIMjLN5TibA7DyYKTrWqMQCa6P33WqLVVD271huGiaNJE/640?wx_fmt=png&from=appmsg)

使用双绞线传输信号的优点：

* 抗干扰能力强——这种结构能有效抑制共模干扰（如电磁干扰、射频干扰等），两根导线上的信号相位相反，外界干扰会同时作用于双线，接收端通过差值运算消除共模噪声，可以简单理解为当受到干扰时，两根线同时受到干扰，它们之间的电压差保持一致，就能保证最终传输准确的信号。
* 传输稳定——即使传输距离长达1km，仍能保持50kbps的传输速率，最大传输距离可达10km。

**2.CAN总线的两种结构**

闭环结构：采用双绞线（CAN\_H与CAN\_L）形成闭合回路，两端各并联一个120Ω终端电阻，速率范围在125kbps-1Mbps，符合ISO 11898标准，在汽车网络中大多采用闭环结构，以满足高实时性信号传输的需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAdm5libILPjbyvEPDBN41WZgEKbsMaDP29ic37PLt3EOldCAkhW8T4MUfTuY5CFYAMweerBkw9lXm1kiaibQpReAN6x9ykPJSERibo/640?wx_fmt=png&from=appmsg)

开环结构：双绞线独立不闭合，每条线串联2.2kΩ电阻，无需终端电阻，速率最高为125kbps，通常使用40kbps，在40kbps速率下最远可传输距离为1km，符合ISO 11519-2标准，适用于长距离且对传输速率要求不高的场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCBwgAHAOA11eJjwMaKiaPY393BoJVRuGhOXxQDgcYzTaarrSzs2NkD3ibd1FugyscdXxnDibKLmiafWvIn96A1AwajcwZWZ5qHpL8/640?wx_fmt=png&from=appmsg)

**3.多主竞争式架构**

多主竞争式架构是CAN总线的核心特性之一，允许所有节点平等参与总线控制，无需主从区分。任何节点在总线空闲时均可主动发起通信，并通过非破坏性仲裁机制解决冲突。这种设计打破了传统总线（如RS-485）的主从模式限制，实现了真正的分布式控制。

那么问题来了，非破坏性仲裁机制到底是如何解决多个节点同时工作时的信号冲突呢？

标识符优先级

CAN总线不设定节点地址，只通过11位或29位标识符（ID）定义数据优先级，ID值越小优先级越高。例如，汽车ABS系统的紧急控制信号ID通常小于车身灯光控制的ID。

逐位仲裁过程

当多个节点同时发送数据时，总线通过逐位比较ID进行仲裁。显性电平（逻辑0）覆盖隐性电平（逻辑1），优先级高的节点继续传输，低优先级节点自动转为只听状态，等待下一个空闲时间再次传输，整个过程仅需134μs即可完成，且无数据丢失。

举个例子进行说明：

假设节点1的ID为01010111111，=703，=0x2bf
节点2的ID为01010100111，=679，=0x2a7
节点3的ID为01010100100，=676，=0x2a4

那么在这三个节点中，总线会依据仲裁规则，ID值小的先传输，所以会优先传输节点3的数据，然后传输节点2的数据，最后传输节点1的数据。节点1从第6位开始，逻辑为1表现为隐性，进而转为只听状态，节点2从第9位开始值为1表现为隐性，也转为只听状态，剩下节点3竞争成功，优先传输数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDdgFxwStfDbibd9mpblwYAZg7R7iaeFTr2tRgjeMibHHaTt6ib4hrvWZ0eazSFHzOyN3aUfsnWehw5nYrCLO5eweoB6gypzN9icMw0/640?wx_fmt=png&from=appmsg)

**4.CAN报文帧结构**

标准数据帧（扩展 ）：

SOF（Start of Frame）：1bit，帧起始，帧开始发送的一个标识

ID（Identify）：11bit，标识符，区分功能，同时决定优先级（扩展帧此处为29bit）

RTR（Remote  Transmission Request）：1bit，远程请求位，区分数据帧和遥控帧

IDE（Identifier Extension）：1bit，扩展标志位，区分标准格式和扩展格式

SRR（Substitute Remote Request）：替代RTR，协议升级时留下的无意义位

r0/r1（Reserve）：1bit，保留位，为后续协议升级留下空间

DLC（Data  Length Code）：4bit，数据长度，指示数据段有几个字节

Data：0 ~ 64bit，数据段的1 ~ 8个字节有效数据

CRC（Cyclic Redundancy Check ）：15bit，循环冗余校验，校验数据是否正确

CRC界定符：1bit，为应答位前后发送方和接收方释放总线留下时间

ACK（Acknowledgement）：1bit，应答位，判断数据有没有被接收方接收

ACK界定符：1bit，为应答位前后发送方和接收方释放总线留下时间

EOF（End of Frame）：7bit，帧结束，表示数据位已经传输完毕

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD0EUdncBmwr0bq0JujvRsGKvtCBOvnSB6rf3hHtskJpFIPicgAPCQtlHXpfFFl2mlYDRyBQ5EPBk98cMPW3YyJPp2bGqojqGzI/640?wx_fmt=png&from=appmsg)

仅展示标准帧

**03**

**CAN数据的收发**

**1.接收整车或单个ECU的CAN报文**

在汽车电子系统中，各ECU（电子控制单元）通过CAN总线进行实时数据交互。要捕获这些通信数据，可通过车辆标配的OBD-II诊断接口（符合SAE J1962标准的16针接口）实施物理层接入。常规操作流程如下：

**硬件准备**

* 配备带CAN协议解析功能的上位机软件（如CANalyzer、VehicleSpy、ZCANPRO）
* 配置USB-CAN适配器（如PCAN、Kvaser、USBCAN-II系列设备）
* 制作OBD转接线缆（确保双绞线特性，线序对应ISO 15765-4标准）

**拓扑识别**

* 无网关架构车辆：OBD接口6(CAN-H)、14(CAN-L)针脚直连车身/动力CAN网络
* 带网关车型：需通过诊断会话激活（UDS 0x10 03服务）实现跨网段报文转发

**物理层连接**

* 使用万用表测量针脚阻抗（典型值60Ω）验证总线终端电阻状态
* 连接时保持线缆屏蔽层接地，防止电磁干扰导致信号失真

**数据采集**

* 设置符合ISO11898-2规范的波特率（250kbps/500kbps）
* 启用时间戳标记功能记录报文传输时序
* 通过滚动模式实时显示DBC解析后的信号物理值

**2.主流CAN数据存储格式对比**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB5DW3Oekej9rQ8uPFPOUZPq4pqMso6yk59ia0qKutiarFM2aPzC5hLeGicsM4qES4DyufrW1aKKRP8Pt7f5a2AnJuMCEXeWkHkWw/640?wx_fmt=png&from=appmsg)

来源：

CSDN博主「几度°」

https://blog.csdn.net/beersdoit/article/details/146387188

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD9qjQXZdMwY876TkFlhIUib1kn4wc72e4cib9eharylSOXtAgAq234jTmZYKrXsGd0OALDotYN7MYS8h0mElMEuPddlDZic56KCg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572912&idx=3&sn=58184d21d6dabc713e8d93a0c1d80e40&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=...