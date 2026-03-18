---
title: 10Base-T1S轻松入门
url: https://mp.weixin.qq.com/s/nc9MSGN-23qqA4NZxc2_LA
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:20:29.259610
---

# 10Base-T1S轻松入门

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAlhC0nYbD1XW2Ed84tCDoG3E00ibgQp7MMxicwRbd6OPZicGDcZUgoHXzZTm1G53YhIxZhicCXO1c9aKdYzvTBFq2jVyqvJntXuYI/0?wx_fmt=jpeg)

# 10Base-T1S轻松入门

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247568414&idx=2&sn=e8421575011428f2d73cc0b393889274&scene=21#wechat_redirect)

**01**

**为什么汽车需要一种“不一样”的以太网？**

**1.1 当前车载网络的挑战**

在当今的汽车中，网络架构就像一个技术“联合国”。多种通信技术并存，各司其职。例如，我们有用于车身控制的CAN FD网络，有用于高可靠性控制的FlexRay网络，还有用于高带宽信息娱乐和高级驾驶辅助系统（ADAS）的点对点汽车以太网（如100BASE-T1或1000BASE-T1）。

这种异构混合的架构带来了一个显著的挑战：不同技术之间无法直接对话。为了让它们协同工作，工程师必须设计复杂且昂贵的网关（Gateway）。网关就像一个翻译官，负责在不同网络协议之间转换数据。然而，这些网关的硬件和软件不仅成本高昂，还常常成为车辆生产中潜在的质量问题根源。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDp6m1DsnCayobCKrGmia9EicR4TibIfe2jiafEamaejFjhs0SicHV50FZ8hwZqhk9dG9eiaGIVX6Ikibmd2xcMnxnG71Q0H2qInRQD3I/640?wx_fmt=jpeg&from=appmsg)

**1.2 “全以太网”汽车的愿景**

为了解决上述挑战，业界提出了一个极具吸引力的愿景：构建一个完全由汽车以太网构成的同质化网络架构，即“全以太网”汽车。

这个愿景的核心优势在于简化。如果整车都使用以太网，我们就可以充分利用以太网成熟的寻址方式，如MAC地址和IP地址。数据可以基于这些地址在整个车辆网络中被自动路由和转发，就像我们在家用或办公网络中一样。如此一来，那些复杂且昂贵的专用网关就可以被大大简化甚至完全取代，从而提升可靠性并降低成本。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBXUfGlGbBCrTyAiaHk49r3fLrOh6Bwb5NHLvfHe910zZ8JfREXLvPu02BqJ1ZAxl3ySbg3J7sln0Fz4pr4rjaAYevMp06h5CNw/640?wx_fmt=jpeg&from=appmsg)

**1.3 传统以太网的局限与10BASE-T1S的诞生**

那么，为什么我们不能简单地用现有的汽车以太网来直接替代CAN或FlexRay这样的总线网络呢？答案远不止是成本。传统的办公以太网（如100BASE-TX）之所以不适用于车载环境，有几个根本原因：

* **线束与成本：** 传统以太网通常使用四线或八线制，而车载总线（如CAN）普遍采用双绞线。更少的线缆意味着更低的成本和更轻的重量。同时，点对点或交换式以太网拓扑需要更多的收发器（PHY），进一步增加了硬件成本。
* **电磁兼容性（EMC）：** 汽车的电磁环境极其严苛，其EMC要求远高于消费电子产品。标准以太网无法满足这一要求。
* **电源模式：** 车辆在熄火状态下对功耗有极致要求，以防电池耗尽。标准以太网缺乏这种超低功耗的休眠模式。
* **唤醒时间：** 车载ECU必须能在100毫秒内从休眠完全唤醒并投入工作，这是标准以太网无法企及的。

正是为了解决这些挑战，10BASE-T1S 应运而生。它是一种专为汽车应用设计的、支持总线（或多点）拓扑的以太网技术，旨在用以太网的语言，实现传统总线网络的简洁与高效。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaABibicb1FpdEE9OIUh591KJnyeQljUvJe85ZAaUQrlKiaFa963QoIKLjAcp6agO7gVWSfObOdxlJibNx5or99waaYwW97KLe1FrGk/640?wx_fmt=jpeg&from=appmsg)

**02**

**什么是10BASE-T1S？核心特性速览**

下表总结了10BASE-T1S的关键技术参数：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA2njpwCCVs6sI4jfiakuA5k4OK10h5buVXY8QNxp5iaeglSlS1T7LcrmicW3JfvWcerPDIoRgh2jB3GNoS8BcibWPoYPbgDDvicJxk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaC4rgojLSD3Y4rCKMzgSEqrCPnJ54LlxzJq0JKS6R8P2VeHkOEzulV07p9GcYxOMHAIB257Tia1gwG6VhOr73rAXibcEpztp03cA/640?wx_fmt=jpeg&from=appmsg)

了解了这些基本参数后，最关键的问题来了：在一个所有节点共享同一根线的总线网络上，10BASE-T1S是如何避免数据冲突的呢？这就要归功于其核心机制——PLCA。

**03**

**核心机制：物理层冲突避免（PLCA）的工作原理**

**3.1 总线网络的根本问题**

所有总线技术都需要解决多节点同时发数据导致信号碰撞、信息损坏的问题，车载网络的解决方案各有不同：

* CAN 网络采用非破坏性仲裁：多节点同时发报文时，ID 更小（优先级更高）的节点获得总线使用权。
* FlexRay 网络采用时间划分：给每个节点分配固定时间槽，节点仅在自身时间槽内发数据，从根源上避免冲突

**3.2 PLCA机制**

10BASE-T1S采用的\*\*PLCA（Physical Layer Collision Avoidance，物理层冲突避免）\*\*机制，正是将FlexRay这种经过验证的时间划分理念应用到了以太网。它通过精确地为每个节点分配专属的发送时间窗口，从源头上避免了冲突的发生。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDicxx5cfEnB2k95q8XS8H3sBoZDEuArnczVrnPibzX61aOaAAdWhOicgoAJcrADOeZlzPfNyasAEUTGNekk6hEdJom6DzxB5LMsE/640?wx_fmt=jpeg&from=appmsg)

PLCA机制包含以下几个核心概念：

* 节点ID (Node ID): 网络中的每个节点都会被分配一个从0到N的唯一ID号，这个ID决定了它在通信周期中的发送顺序。
* 主节点 (Master Node): 通常是ID为0的节点。它扮演着网络协调者的角色，负责周期性地发送“信标”来启动一个新的通信周期。
* 信标 (Beacon): 由主节点发出的一个特殊信号，它标志着一个新的传输周期的开始，并同步网络上所有节点的时间。
* 提交符号 (Commit Symbol): 如果一个节点在其传输机会期间确实有数据要发送，它会首先发送一个“提交符号”。这个符号至关重要，它就像在会议上举手示意“我要发言”，明确表示它将占用总线。这一行为将其与那些只是静静地让传输机会过期的节点区分开来。发送提交符号后，节点会立即开始发送标准的以太网数据帧。
* 传输机会 (Transmit Opportunity): 在主节点发送信标之后，所有节点会严格按照其ID号从小到大的顺序，依次获得一个专属的、可以发送数据的时间窗口。

**04**

**PLCA实战：三种普通通信场景解析**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAIeD0bIJnAcwGaTKUPiaZra3JeY0p3F5PocP013Xky1Dzb16tvh1XX9IQQsoKwFGM7tgD4TzKQwSNKVugibOUN0XwsTzcF87mxY/640?wx_fmt=jpeg&from=appmsg)

**4.1 场景一：所有节点都有数据发送**

在这种满负荷的情况下，网络中的所有些节点都需要发送数据。

* 节点0 发送信标，启动周期。
* 节点0 的传输机会到来，此时，节点0有数据要发送，于是它立即发送一个\*\*“提交符号”\*\*，紧接着发送一个完整的以太网数据帧。
* 轮到节点1的传输机会，它也同样发送\*\*“提交符号”\*\*和自己的数据帧。
* 这个过程持续进行，直到所有节点轮询完毕。

**4.2 场景二：部分节点有数据发送（例如节点1和3）**

在这种更典型的情况下，网络中的某些节点需要发送数据。

* 节点0 发送信标，启动周期。
* 节点0 的传输机会到来并过期（因为它无数据发送）。
* 轮到节点1的传输机会。此时，节点1有数据要发送，于是它立即发送一个\*\*“提交符号”\*\*，紧接着发送一个完整的以太网数据帧。
* 节点1发送完毕后，轮到节点2的传输机会，但它无数据发送，机会过期。
* 轮到节点3的传输机会，它也同样发送\*\*“提交符号”\*\*和自己的数据帧。
* 这个过程持续进行，直到所有节点轮询完毕。

**4.3 场景三：网络空闲（所有节点均无数据发送）**

这是最简单的情况，整个网络非常安静，没有任何节点需要通信。

* 节点0（主节点） 发送信标，启动一个新的传输周期。
* 轮到节点0的传输机会，但因为它无数据可发，所以在短暂的窗口时间后，这个机会自动过期。
* 轮到节点1的传输机会，它同样无数据发送，机会也随之过期。
* 这个过程会依次进行下去，直到所有节点的传输机会都轮询一遍并过期。然后，主节点会再次发送信标，开始下一个周期。

**05**

**PLCA实战：两种优化通信场景解析**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAKfptVmTiahRhaN37fEbsPgqWgiaIicwCUvr1l3gsWwChDwjIIzmAywaQvWXJ5lf4JlgdeicZy4GL9wPlVZpOMveyXM7Vj3mYxibC8/640?wx_fmt=jpeg&from=appmsg)

**5.1 场景四：突发模式（Burst Mode）**

10BASE-T1S还提供了一种可选的“突发模式”（Burst Mode），以应对非对称的数据流。在许多汽车应用中，数据流不是均匀的。例如，一个传感器可能是主要的数据生产者，而其他节点主要是数据消费者。突发模式允许被配置的特定节点在其单个传输机会内，连续发送超过一帧的数据。这极大地提高了数据传输效率，满足了那些需要高吞吐量节点的特殊需求。

**5.2 场景五：单节点多个ID**

除了突发模式，PLCA还提供了更灵活的方法。工程师可以通过软件配置，为一个需要低延迟或高带宽的节点分配多个ID。此外，还可以将多个ID与突发模式相结合使用。这些策略允许对网络性能进行精细调整，确保关键数据能够优先传输，尽管这可能会增加其邻近节点的传输延迟。

来源：

https://zhuanlan.zhihu.com/p/1995067444474159482

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

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2...