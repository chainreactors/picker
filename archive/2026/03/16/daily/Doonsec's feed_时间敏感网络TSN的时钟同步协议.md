---
title: 时间敏感网络TSN的时钟同步协议
url: https://mp.weixin.qq.com/s/urM-3B1KPV7qAB3NA9GHhg
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:15:01.959072
---

# 时间敏感网络TSN的时钟同步协议

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAxdpsm4HMsM3OWpdNlkcl5G5ictjyptfoBByqbD8SI4RuGcTtIXUPCHJkG5NkaibSj45djVdG6yXG4awEQZic4Nv5mKGvXydvAHg/0?wx_fmt=jpeg)

# 时间敏感网络TSN的时钟同步协议

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247568414&idx=2&sn=e8421575011428f2d73cc0b393889274&scene=21#wechat_redirect)

时间敏感网络Time Sensitive Networking(TSN) 是一类基于以太网/无线网的低延迟和高可靠的通信协议，其主要工作在物理层和数据链路层，为车载通信，工业以太网等提供基础设施。TSN主要包含了时间同步协议，流量整形，低延迟以及确定性以太网帧传输，容错，信息安全等特性。其中时间同步协议为以太网的确定性传输提供了基础（确定性以太网帧以TDMA方式进行传输的）。同时对于在异构分布式节点中传播的音视频来说，不同节点对时间的一致性理解为音视频流的正确传输提供了基础。

IEEE TSN工作组以IEEE 802.1 AS标准的形式确定了TSN同步协议的规范。该标准定义了gPTP（Generalized Precision Time Protocol，即如何根据测量的链路延迟以及不同节点时钟频率的差异，将同步帧从Grand Master传输到Slave）的协议以及BMCA（Best Master Clock selection Algorithm，即根据接收到的Announce帧来选取Grand Master）算法。IEEE 802.1 AS包括了七种以太网帧，其中sync,sync\_follow\_up用于同步, pdelay\_req, pdelay\_resp,pdelay\_resp\_follow\_up用于测量延迟以及不同节点的时钟频率的差异，Announce用于选择最优的Master节点。

**BMCA算法：**

下图展示了如何使用BMCA算法选择最佳master的算法：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaB6MDTXwGOZ3h5TJwecGbsQ2rQNdTwqqRzhakiaXX8GlWE2HeyCuryLTZV6WIicP1KBF8cBvGl5QPRQe7evpuZHCaP4Al3D2TPjA/640?wx_fmt=jpeg&from=appmsg)

1. Grand Master使能的节点可以向网络中发送带有优先级，时钟等级/时钟精度，MAC地址信息(这些信息的重要程度依次下降)的Announce帧(这些使能的节点有机会成为master)。注意，这些GM使能的节点有可能与GPS进行同步，获取高精度的时钟信息。在该例子中，ECU0, ECU1, ECU2, ECU4 能够向网络中发送带有不同优先级的Announce帧。
2. 对于接收到多个Announce帧的中继节点来说（如例子中的Camera,Radar），这些节点会将所有低优先级的帧抛弃，只传输接收到最高优先级的Announce帧。
3. 根据接收以及发送Announce帧的端口，中继节点中不同的端口被设置不同的角色，这些角色包括了master和slave。对于中继节点来说，接收到Announce帧的端口需要设置为slave，而发送Announce帧的端口设置为master。根据不同角色的设置可在网络中生成一条时钟树。
4. 在该例子中，ECU0被选为Grand Master。
5. 如果当前的Grand Master出错，次优的节点会被重新选取作为Grand Master。

在这个过程中根据不同端口的角色设置，一个以Grand Master为根节点的时间树会生成，用于后续的精确时钟协议。

**Generalized Precision Time Protocol算法：**

链路的延迟和不同节点时钟频率的差异会对时间同步协议产生重大的影响。可以通过如下的方法测量相邻两跳节点之间的链路延迟以及时钟频率差异：

1.链路延迟：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaA8T2vTcUzbKibTaxFwZWLGsk0QBIiaErjuPln9CIFiazsoRX8DibdteEYvyTXAK9BRsnA5kibHvbPUrTW9fHesB6tN1DKicIMMaHtR8/640?wx_fmt=jpeg&from=appmsg)

对于对称性的通信来说，该链路的延迟为10。

当输出端口从MAC层向PHY层发送一个以太网帧的时候，硬件会捕获发送的时间，该信息会在follow\_up的以太网帧中进行发送 （这么做的原因是降低实时处理的需求）。在接收节点中，当以太网帧从PHY层传输到MAC层的时候，slave的时钟会捕获以太网帧接收的时间（如上图所示的t2）。

2.邻居节点速率的比值

根据以上描述，如果链路延迟是固定的，在如下图所示的例子中，t1'-t1与t2'-t2的时间差可以反映出两个节点的时钟频率差异，邻居节点速率的比值rateRatio可表示为：(t1'-t1)/(t2'-t2)=10000/10002=0.998。由此可见在下图的例子中，左边节点的时钟频率要比右边节点来的低。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDHup6nzHbnRvjqibFWeqEnGvHicNicPVlpleGfnj6Z5IocMEWLsJcIqfP9BJNVl5zTtP78ERsKmpHoyyLZp6LGXxtrHe0EwkYc9w/640?wx_fmt=jpeg&from=appmsg)

3.端对端的时钟同步

在端对端同步中，Master节点会发送sync帧给下一跳，同时该sync帧的发送时间会打包在follow\_up的以太网帧中进行传输。在进行端对端的同步过程中，还需要根据链路的情况对链路延迟进行调整。在该例子中从master到slave的端对端延迟可以通过delay=prop'+residenceTime'\*rateRatio'+prop''+residenceTime''\*rateRatio''+prop''来表示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAZia6nQd1AWpnAL8SAnyKEV3vf9v3P2s3t9ZuQBmu1C0IHmoNHP4r9r9H6mnh3FepqYc8ibMFDibDoqtNjgNyWABxPElibhQFibYCM/640?wx_fmt=jpeg&from=appmsg)

端对端同步需要持续不断进行的且该过程要比上述的链路延迟计算和时钟速率比值计算更加频繁(原因在于链路的变化要比时钟频率变化更加频繁)。端对端同步是延迟计算和节点速率比值计算的后续过程，整个完整的过程如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAg1RezGwmeYEBLE2bZ5G6VOUWy0w8VibxcoXOicn3n0FWdyqnUUk1ibLQ3RhuouWNonnOCAibFibbEfFHXHQWteUf9QKCgNF8oEp5w/640?wx_fmt=jpeg&from=appmsg)

根据不同的需求，协议中推荐设置情况如下：sync和followup帧每秒发送8次，对于每条链路上的delay request和delay response每秒发送3次，Announce帧每秒发送1次；Grand Master使能的设备需要为其定义静态的优先级和时钟等级。

**冗余的时间同步协议**

以上的标准中仅考虑Grand Master出错的问题（如Grand Master出错，根据BMCA算法，次优的Master Enable节点会被选举为最新的Grand Master），但是没有考虑链路出错的情况。最新的标准中提供如下解决方案：

1. 对于Grand Master节点，其带有两条冗余的时钟树，每条时钟树都拥有自己独立的时钟同步域。其中一条时钟树上的同步链路出错不会对另外一条时钟树造成影响。
2. 提供Grand Master的冗余方案，在该方案里拥有一个Primary的Grand Master（GM）和一个host standby的Grand Master，两个GM都有自己独立的时钟同步域，同时host standby的GM需要跟Primary的GM进行同步。当第一个GM出错的时候，第二个GM可以进行无缝的接管。这种冗余的机制，不需要重新选举新的GM，同时相比重新选举GM，该方案的切换时间会大大减小。

来源：知乎@Yuanbin

https://zhuanlan.zhihu.com/p/85107933

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

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**
...