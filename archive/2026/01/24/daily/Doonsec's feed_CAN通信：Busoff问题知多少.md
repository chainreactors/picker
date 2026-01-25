---
title: CAN通信：Busoff问题知多少
url: https://mp.weixin.qq.com/s/lEudrPj5WFWbkLE5cHD8rA
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:52:21.232530
---

# CAN通信：Busoff问题知多少

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icwR5QtRSbicBXia91EdrhRtcGp3yvmCkxDBkkEicq6BwWVxIribQWBAVmAQ/0?wx_fmt=jpeg)

# CAN通信：Busoff问题知多少

谈思实验室

![]()

在小说阅读器中沉浸阅读

以下文章来源于开心果 Need Car
，作者开心果 Need Car

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7xmZWjMxkpzia4Ft2qUbKVib3waicn3vUKRjoL8iaKrC191A/0)

**开心果 Need Car**
.

号主：开心果 Need Car，主要从事汽车Autosar开发，公众号主要分享 通信、诊断、存储、网络管理、标定、Bootloader等工程开发问题。致力于将学到的知识，分享给更多的Autosar从业者，努力解答一线开发工程师的困顿！

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247564281&idx=2&sn=699099fdf353a20e4b133c9bb09efbe0&scene=21#wechat_redirect)

**01**

**测试中，为什么是32个错误帧出现一次Busoff？**

Busoff的产生是因为TEC（Transmit Error Counter）＞255导致，再次提醒：与REC（Receive Error Counter）无关。也就是说，如果节点状态切换到Busoff，是因为节点自身外发报文错误导致TEC＞255。回顾一下节点状态机，节点状态机如下所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icObGKNV61w9EBAW6QVXIzlePIQKqTEmFH3DCAde8fLx5icW1z9TfNASQ/640?wx_fmt=jpeg&from=appmsg)

在切入主题之前，对Error Passive状态做一个展开，节点由Error Active进入Error Passive，是因为REC＞127 or TEC＞127。所以，节点进入Error Passive状态的可以分两个层面看：

* 第一、总线上其他节点（eg:Node A）引发的错误，导致接收节点（eg:Node B）的REC＞127。既然是外因，即：Node A错误导致Node B进入Error Passive状态，对Node B的最大"伤害"到此状态即可，Node B的通信状态没有什么问题，无需断开总线连接；
* 第二、发送节点引发错误，当TEC＞127时，进入Error Passive状态，如果发送节点依然识别到自身发送报文有问题（有错误帧），为了降低对总线上其他节点的影响，发送节点要为自己的错误行为负责，当TEC＞255时，节点需要暂时退出总线通信，之后尝试恢复通信。

对于节点的Error Passive和Busoff状态，驱动层可以提供对应的接口给上层，以此改善功能算法。以英飞凌tc3xx为例，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icjGZTfZnH4NIKw6nAkQrTQ1OswfMAkLXImud9nIKKTKzfx7sKQia3l7w/640?wx_fmt=jpeg&from=appmsg)

如果需要更进一步的知道Error Passive是TEC还是REC导致的，可以进一步读取错误计数寄存器（ECR）的RP位域，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icVFwhwRUrZDkVToWmFCzDfhs3FiaYb71KPADpcpPC0gCW0GDK5H0zkvw/640?wx_fmt=jpeg&from=appmsg)

提示：REC使用7个Bit表示，最大可表示128，TEC用8个Bit表示，最大可表示256。

回到这个小节的问题：“测试中，为什么错误帧达到32帧，就会Busoff呢？可以大于32帧吗？”

如果要搞清楚发送多少错误帧会导致TEC＞255，进而让节点进入Bus off状态，我们需要先清楚TEC的累加规则：

1. 发送节点在发送时，产生错误标志，TEC + 8。注意，有两种工况除外：
2. 第一、仲裁阶段，节点发送隐性位（"1"），收到显性位("0")。当其他节点CAN ID小，优先级高时，低优先级（CAN ID大）的节点仲裁失败，发送的隐性位被显性位覆盖导致；
3. 第二、节点处于Error Passive模式时，Ack Slot发送隐性位，收到隐性位（没有节点应带发送节点），说明当前总线只有一个节点在总线中，此时TEC不需要再累加；
4. 发送节点在发送主动错误标志或者过载标志时，检测出位错误（Bit Error）, TEC + 8；
5. 节点从主动错误标志、过载标志的最开始检测出连续14个显性位。之后，每检测出连续8个显性位。TEC + 8；
6. 被动错误标志后检测出连续8个显性位。TEC + 8；
7. 发送节点正常发送完一帧数据，且被其他接收节点应答（Ack）。TEC - 1，如果TEC = 0，则保持0；
8. 如果节点已经Busoff，当检测到128个连续11 bit隐性位时。TEC = 0。

通过如上规则可以看出，对于发送节点自身发送报文导致的错误，TEC均会累加8，也就是说，如果想最快地使得某个节点进入Bus off状态，就得让发送节点自己识别到自身产生的错误，而且，最少要产生32次，32\*8 = 256 ＞255，节点进入Bus off状态。

有的时候看到总线错误不止32帧，节点才进入Busoff，又是因为什么呢？这里我们分析一种工况：

测试中，如果通过Capl脚本只是干扰节点（Node A）固定的CAN ID(eg：0x10)，可能需要＞32个错误帧，才能让Node A进入Bus off。一个项目中，一个节点的外发报文可以有多个。假设：Node A有5个外发的周期性应用报文，CAN ID：0x01~0x20，周期都是10ms。测试中，只干扰CAN ID = 0x10的报文。

如上TEC计数规则中，节点每成功发送一帧报文，TEC会减1，由于Node A 的5个CAN报文周期相同，干扰0x10使得TEC + 8，但是，如果其余4个报文成功被发送，则每发送一帧，TEC - 1。这样就使得TEC不能很快的＞255，进而错误帧的次数会超过32帧。所以，如果想快速的制造Bus off，可以对多有外发报文的某个Bit干扰，这样，可以连续的干扰出32个错误帧。

只干扰特定CAN ID报文，总线报文状态示意如下所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4iciaudE5nw8CA8P5icZCXZfAuZOcKbxR8cmA4WnUetyiak4WKl17qLZ7bLQ/640?wx_fmt=jpeg&from=appmsg)

提示：一个错误帧中，可能有多种错误类型。

**02**

**Bus off的DTC问题**

当Bus off发生到一定程度时，会影响到总线的正常通信，需要将此故障信息记录下来，以便于后续问题排查。对于Bus off DTC的设计策略，每家OEM要求有所不同。本文，分享一种需求，供大家参考：

1. Busoff检测频率10ms。DTC一般会对应一个或者多个事件（Event），为了识别事件的状态，会约束一个检测频率，检测频率的大小，意味着事件发生故障时，能否被快速检测到，进而决定着事件对应的DTC能否被快速触发；
2. Busoff快恢复32次，快恢复周期10ms。当节点通信出现故障时，如果能快速恢复通信，节点功能也能及时恢复，所以，设计10ms的快恢复也就能理解。尝试32次，也是想尽可能地挽救故障节点的通信功能;
3. Busoff慢恢复NA（不做明确约束），慢恢复周期60s。当快恢复32次都不能有效挽救节点通信时，说明节点大概率出现了不可逆的故障。所以，设计一个较慢的慢恢复期，就是想再碰碰运气，万一节点通信又恢复了呢？如果节点不能恢复通信，车辆又不能立马停下，只能任其不断地尝试慢恢复，因此，不做慢恢复的约束。此时，同网段内的其他节点会监控对应的通信报文是否丢失，故障节点由于发生Busoff，非Busoff DTC的监控功能禁止；
4. Busoff发生32次，进入慢恢复期时，Bus off DTC Confirmation（Bit 3 = 1）。既然做了最大努力的尝试，节点不能恢复通信，为了便于后续的车辆检修，需要记录Bus off DTC；
5. Step Up = 4，32次Busoff后，4\*32 ＞127，Step Down = 128。

相对于其他监控事件，Bus off 事件优先级（Event priority）一般较低，注意：1表示highest priorit，数字越大，事件的优先级越低。

这里需要讨论一个“连续”问题，Busoff发生32次，且Busoff由快恢复（Level1）进入慢恢复（Level2）阶段时，Busoff DTC需要上报。这里的32次如何计算呢？这里抛一个问题：”如上需求中，10ms可以检测一次节点Busoff状态，假设前100ms检测到了10次节点Busoff状态，中间1s节点恢复了通信，之后又快速的发生了32次Busoff，需要上报Busoff DTC吗？“，如下所示：u

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibskNO8lMqNJ9VeCZQL0ic4icPlxUmGsIvibD7sMl5lUX7jZ6rzDzricLdJs3DBFtRNgRdyPxzAzU9adw/640?wx_fmt=jpeg&from=appmsg)

如上的问题就涉及到了一个问题：”Busoff次数如何累加？“，对于这个问题的答案，需要结合项目需求，和甲方明确好。每家OEM的约束不同，这里讨论一种约束工况：以10ms检测频率为基准，如果20ms的检测周期内没有检测到Busoff，则Busoff CNT不再累加，重置Busoff CNT（Busoff CNT = 0），因为此时的Busoff不是"连续"的。

来源：

https://blog.csdn.net/tjcwt2011/article/details/144292975?spm=1001.2014.3001.5502

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

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#we...