---
title: 理论深度分析Autosar CAN 时间同步
url: https://mp.weixin.qq.com/s/qrr8LRUjd_fn9VW1Nx9N8w
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:16:52.570113
---

# 理论深度分析Autosar CAN 时间同步

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaBrk3r6qPjBJutSvU0XJJrARic7RJsicnqyHytibTFAN1tSAhIszibbiabBJNxGNoo6lCvZXHDkwRedHsRGGmOtcv753kATMOib2Ny5M/0?wx_fmt=jpeg)

# 理论深度分析Autosar CAN 时间同步

谈思实验室

![]()

在小说阅读器中沉浸阅读

以下文章来源于汽车与基础软件
，作者汽车小Z

![](http://wx.qlogo.cn/mmhead/kqodNCVWpEuEIImOFDVgicPibr4NRNWqKIBwORpN1rZQSwbH8VVHD4GPMfsK6a5HDsw4gozVicKzcI/0)

**汽车与基础软件**
.

给我两年 不改变点 汽车行业的学习环境，自己注销账号，

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247566311&idx=2&sn=27d2cf53ef824bfde9b824f90e864ec6&scene=21#wechat_redirect)

**01**

**背景介绍**

尽管当前汽车工具以太网越来越重要，gPTP 也越来越广泛使用。但是车上仍然有很多CAN/CANFD （下面都用CAN 表示） 的控制器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAx92ic31uvqicrLPBnS0LL8icudlXRNQVmsaLWXttGMkBer0iadSWvXiajia2w47L3fyntcprc28odO0O1SHj9OFX7YReg9J2DIsMzA/640?wx_fmt=png&from=appmsg)

车上现在的传感器，执行器，底盘上的ABS, 制动，动力系统等等 都还是使用CAN。这些对实时性，可靠性要求较高的控制器，依然保持着CAN 的使用。但是他们的时间信息也需要与整车进行统一。所以这里就带来了CAN 节点也需要做时间同步。

相对于ETH 下有传统互联网的加持，PTP 协议 TSN 等等对时都很成熟，对于汽车上面也衍生出了gPTP. 但是受制于CAN 本身的字节数和硬件的影响。这里我们需要思考一套简洁的对时方案。下面我们逐步分析。

**02**

**Autosar CanTsyn**

为了抓住从最根本的原理，我们这里只从本地时间来进行介绍。不考虑外部的时间比如GPS, 等等。

理论来说整车上几十上百个控制器的时间信息应该是在同一时刻是一样的。但是实际上是有点偏差的。比如每一个控制器都有一点点偏差，衡量分布式系统同步质量的一个指标是精度。它表示系统中时钟之间的最大偏差，可以定义为

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDRroicUCYlyBIl3UibT8LONUdYhu2GP5KxoETJlLTr1maGfO09WOEAiatNSWhWdZ6eaR8UjkNiafNeCwvlrUFuKibEicuy10yM8k4oc/640?wx_fmt=png&from=appmsg)

在汽车autosar 体系定义中，CANTsyn 同步着不同的控制器单元。这里只是定义了Master 节点给Slave 节点发送两帧报文

1. sync
2. follow up

对比PTP, gPTP 来说，这个是比较简单的协议，而且是单向的。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCZZc5SCDXVMib5gvKrJUqFSrJQkmvJlzSibRXiapAjv48fbYKoo8oRASzG1PPwQfxD8GrT3CEiaITxq3lQyQqgicDkiaUPibeYOuN2Zk/640?wx_fmt=png&from=appmsg)

由于硬件和字节长度的限制，报文内部包含的时间信息，是由软件应用层逻辑打进去的。所以这存在一定误差，我们后面一步一步讨论，如何消除掉这些误差。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAeY56ozO8lR6BUZJuvzH00DFSq12oUA2NQxibiagyVnia5fHukZKB5NnhFlROrsfGmMll9iaiaEEZvVFaiaGWLnoEVU82ia4CVmAShpk/640?wx_fmt=png&from=appmsg)

上图显示了（简化的）消息交换。Master向Salve发送一条同步消息。此消息在tMasteri发送时，在tSlavei接收时有时间戳。随后使用FUL消息传输主时间戳。这两个时间戳现在可以用于同步。

这便是autosar 定义的CANTsyn. 下面那我们从系统的角度去说一下整个过程。

**03**

**系统模型**

我们指导我们Autosar 软件发送报文，和接受报文的过程其实是个很长的过程。其中可以分为三个层级。

1、层一：

受到实时操作系统调度，以及软件内部的协议栈的影响

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDTxh719nqDibq4ico1OkWl0DHLOYFPaS2gqdak07YcayRpZ4Xib1fJ5szJjIIHdbaicGu8Hm6ZwETWNS2a1CC57G1dibLXeXqJU5S4/640?wx_fmt=png&from=appmsg)

2、层二：

CAN 报文发送函数，从函数的角度（CPU执行的角度）放到了发送buffer 就结束了

3、层三：

物理层，受到总线负载，总线长度等的影响

过了发送的三层，才能到接收方，当然接收方也是一样的有这三层。这里不重新说了。可以总结为下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBLDYuVPX5Jw4HJMziag9ITZf4rqQTj3uBfdMQxOptXIDw7NaXdq3n4eMUZtPLHuiabfUIWCR8sEwTr0B2oZzLVyZqDclaM49JJk/640?wx_fmt=png&from=appmsg)

因为最下层的Propagation time 实际上是完全硬件决定的，我们哪这个时候的时间，作为一个参考值。分别向上进行分析发送的时间和接收的时间。

我们更细一点的来说一下整个过程。

**∆sched**

由实时调度器引起的延迟。它描述了在CAN控制器的消息内存中接收到消息到软件中的回调之间的时间跨度。在理想情况下，该延迟的最大值等于接收任务的周期加上在调用回调时发生的软件延迟。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBA6KKSdYesIIWp0D8T3Fy7NpwUnCCicBIvcOwdupGqzZIosWz7ibnaWEAicqUw2oy08yRW7xnZkdxe3ZPx8mA13GLyQppc1ENs7c/640?wx_fmt=png&from=appmsg)

但是在实时操作系统里面整个数值是有可能大有可能小的，这主要还是要看优先级以及抢占机制是如何设计的。需要满足任务的特性。比如之前聊到的调度表以及ALARM， 还有各种抢占机制。

**Δread**

读取是在读取时钟值时的延迟。它是从调用读取函数和实际读取时间戳之间的时间跨度。这个值不能被假定为常数，因为它取决于软件的实际执行时间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA97znTvrtmtbQ1HrpS430Rzx6SshKYPNzAOgFJXSgpArVVSmQgqiar6rws4BtGF5Ew7xIib8x6qRl6zBwfXSRA4jhcCwZwI8yVo/640?wx_fmt=png&from=appmsg)

**ΔCtr, Δtrans\_Tx, Δtrans\_Rx**

这些时间是CAN帧的发送和接收相关联的与硬件相关的延迟，直到它们在消息存储器中可用为止。它们可以被假定为几乎是常数，因为can控制器是完全在硬件中实现的。

**ΔProp**

信号在CAN总线上的传播延迟。它取决于总线的长度，并且对于固定的网络配置是恒定的

有了这些很细节的分析，我们只需要把每一段的时间计算出来，测量出来，就理论来说是可以做到发出去真正时间戳的协议。

**04**

**软件实现方法**

同步以及发送/接收任务运行在CPU上，并由调度器周期性地调用。当调用发送函数时，要发送的数据被放置在发送缓冲区中，并在总线允许时发送。一旦消息在发送缓冲区中，发送函数就会返回。

这个时间与消息实际发送的时间不一致，因此它不是绘制准确时间戳的合适方法。当消息通过总线到达时，如果处理成功并且在传输过程中没有发生错误，CAN控制器将通过接收缓冲区使它可用。

当调度程序调用CAN接收任务时，软件会首先会注意到一条新消息。此任务从接收缓冲区读取所有消息并通知应用程序。

理论来说CAN 的时间戳需要打在CAN发出去（完全发出去），也就是最后一个bit 完了之后的时刻。所以 已成功发送的帧对所有总线节点，包括发送方，都显示相同。

一旦再次收到已发送的消息，发送方就知道它已成功发送。因此，可以使用相同的机制生成发送和接收时间戳。在这两种情况下，都接收到消息，一旦通知应用程序，就读取当前时钟值。

所以这里就回到了前面说到的那个参考的时刻。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCCiaGqcfiaicJap3ecz0iaKygLib8a1BepaqwHllt6uHYHhtAZja8VKrWz50CzPpVjCR4mNwSsUBQ6wqcI2Baiayvg0w4iaoJWydQdXc/640?wx_fmt=png&from=appmsg)

这是两个一样的过程，只是接收方多了个线路的延迟。这个线路延迟是纯硬件决定的。

**05**

**时钟同步**

前面说的是协议的保证两个ECU的时间同步，但是每个ECU 的晶振可能是不一样的。所以比如master 说 他过了1s钟，经过了100000000个ticks (晶振)。

但是 对于 slave节点来说，100000000 ticks(晶振) 虽然自己认为是1s ，但是实际上可能不是一样的的。所以我们有必要让slave 知道master的晶振与自己的晶振的rate。

所以，通过从通过消息交换接收的时间戳，现在可以同步到Master的时间。在最简单的情况下，其中从时钟被直接设置为接收到的值。这种方法的缺点是可能会发生时间跳跃。

因此，在这个工作速率校正中，时钟偏差通过调整时钟的速率来补偿。这里所使用的机制区分了两种比率。标称速率与主速率的rate同步。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCWpcwYm7VzB8783niaoxRvGGA5JFaibzJsccUiaDDPD1ryFktXX1YkiaoeGPl0m8bWickHRXwK9v7X3iawKEhYklbgZa68Ldxr4nBYk/640?wx_fmt=png&from=appmsg)

具体的逻辑如上图。

**06**

**结论**

上面的过程是仅仅从软件的角度来进行时间的同步。必然会受到任务调度的不确定性影响。以及调度的颗粒度影响。

我们可以通过提高任务的优先级，或者是中断。以及调度周期很小的方式来减少误差。

在计算rate的时候，理论来说rate 不应该变化很大。所以我们可以设置可靠的Filter, Debounce 机制来减少rate的影响。进而减少对时间本身同步的影响。

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

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fm...