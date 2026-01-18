---
title: 基于模拟的安全 (Simulation based Security)
url: https://mp.weixin.qq.com/s/kU0aQnrMHw_AoERv6K1CrQ
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:35:03.749312
---

# 基于模拟的安全 (Simulation based Security)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UV7QvkB7E3icqHOutdXrAxb1uONRuA9oojdnLHGTaibq5XCiaZUVtPXJicg/0?wx_fmt=jpeg)

# 基于模拟的安全 (Simulation based Security)

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

构造多方安全计算协议和零知识证明系统的核心挑战之一在于：如何证明所设计的协议或系统是安全的？ 要回答这一问题，首先需要明确什么是“安全”。

对于多方安全计算，“安全” 至少意味着：各方的私有输入不会被泄露。对于零知识证明，“安全” 至少要求：证明方（Prover）的私有信息不会被泄露。更严格地，密码学中定义的“安全”是指：协议或系统在理论上不会泄露任何关于私有输入的信息（信息泄露量为零）。

然而，如何精确定义“不会泄露任何信息”是一个极具挑战的问题。在密码学中，这一难题通过引入“模拟器”（Simulator）的概念得以解决。

模拟器的直觉来源于以下想法：如果参与协议或系统的任何一方，在不知晓其他方的私有输入的前提下，可以完全模拟整个交互过程的行为，那么可以认定该协议或系统是安全的。因为在这种情况下，交互过程中产生的信息对任何方都是无效的——任何方仅凭自己的输入和公开信息就可以生成这些交互，完全不需要依赖其他方的私有信息。

为了更形象地解释模拟器的概念，可以借助一个课堂教学的类比：假设我们要验证一位学生是否从某位老师的课堂中真正学到了新知识。我们让这位学生扮演老师的角色，站上讲台授课，板书内容，与台下的学生进行问答交互。如果这位扮演老师的学生讲得非常好，以至于台下的其他学生无法分辨讲课的人究竟是老师还是学生，那么可以得出结论：这位学生并没有从老师那里学到任何新知识。因为他能够独立模拟整个课堂教学过程，且模拟得如此逼真，让其他人无法分辨出真正的讲课者是谁。

同样的逻辑可以应用于多方安全计算和零知识证明。如果模拟器能够在不访问他人私有信息的情况下，完美重现协议或证明过程中的所有交互细节，那么说明交互过程本身并未泄露任何有价值的信息，因而系统可以被认定为“安全”。

**统计不可区分 (statistically indistinguishable/close)**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5URJpibibFT2np0E9kZCxbA0Fo6jJFqss9zibPicWGnKoht5IcQ6PQgwgfmw/640?wx_fmt=png&from=appmsg)

**计算不可区分 (computationally indistinguishable)**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5U8tNaUnicpNUbjorUqFiaW3NgDjAXriaP3buoUpwXEJ5AQH5mUdex4OghQ/640?wx_fmt=png&from=appmsg)

**hard-core predicate**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UtDYeMHIfuDyU6fmWsXdJCAibibyshAt9GEYsKIRNA7DbpQvZy3y4b4kw/640?wx_fmt=png&from=appmsg)

**证明多方安全计算协议抵御半诚实敌手**

现在讨论如何在半诚实安全模型下 (against semi-honest adversaries, semi-honest security, passive security)证明多方安全计算协议是安全的。具体地，选取多方安全计算协议为不经意传输 (oblivious transfer, OT)[6]。OT可以说是最基本的多方安全机选协议之一。它的重要性体现在它的完备性[7]：任意的多项式时间可计算函数 (polynomial time computable function)的多方安全计算协议都可以仅仅借助OT构造出来。

OT协议细节如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UaXxEtBEspufCfc9CGoR2uaiclD7yzqa6NHT8ynM3PO05GAAAicpmDcSw/640?wx_fmt=jpeg&from=appmsg)

不经意传输协议

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UTJ1lSYrLLuywsFqDZ3iaqNvdVfOIgMLSrZ5TTPfAvnWsNiav7bGXO3wg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UeXdYehKsia0XLGRmJBPSCguZx8OfTqqAicHTGX06SZtRFabl0plQ953g/640?wx_fmt=png&from=appmsg)

**证明（非确定轮次的）交互式零知识证明系统抵御恶意敌手**

这里讨论如何在恶意安全模型下，论证一个图三着色问题(3-coloring problem[8])的零知识证明是安全的。

之所以选择3-coloring问题，是因为它是NP完全的(NP-complete)[9]。如果我们可以构造它的零知识证明，也意味着我们可以构造任意NP问题的零知识证明(Any language in NP can be proved in zero knowledge[10])。

选择恶意安全（malicious security, active security）模型的原因在于，在半诚实安全（semi-honest security）模型下，零知识安全证明几乎是平凡成立的，因为该模型假设证明者（Prover）不会伪造或欺骗，只要提交了证明，就一定是正确的，不存在作假的可能。然而，零知识证明系统真正需要防范的风险在于，证明者实际上并不知道正确的证明，却仍能伪造一个错误证明，使验证者（Verifier）误以为其掌握了有效证明。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5Ung5dmN0SIt0f4Rlm53vHz8LF9UWRtRhlHMqUdTdCcpcx5xw8ZZXjaw/640?wx_fmt=png&from=appmsg)

零知识证明可用下图进行描述：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UQrQqfDnicmPbETgF2OjfqQ7lXFYicYnib1HR5G33FzxRUk1LxFnAzxJ4g/640?wx_fmt=jpeg&from=appmsg)

三着色问题的零知识证明

对该零知识证明做一些解释：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UvALzOEMuPCZpn2VUCJRib98IxQx6ud3EN3OHbrBAc07u0icImiadM44UA/640?wx_fmt=png&from=appmsg)

若以上条件均满足，则验证者确信证明者确实掌握了一个正确的三着色方案，而无需得知完整的着色信息，从而实现零知识证明。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5Uyib7gxj1xrBEwrzvwCwWQmicd7anBgLKp9uic69yZ5XrAxjS5aticibEYxw/640?wx_fmt=png&from=appmsg)

从模拟器（Simulator）输出的视角来看，很容易证明其输出与真实交互视角在计算上不可区分，这里不再赘述。

特别需要注意的是步骤 5 中，如果边猜错，则跳回步骤 2 的行为，这一过程通常称为重绕（rewinding）。模拟器面临的最大挑战在于，它事先并不知道验证者（Verifier）随机选择的是哪条边，因此必须引入 rewinding 技术，以确保它最终能够“猜中”Verifier 选择的边。

可以将 Verifier 理解为一台图灵机（Turing Machine），而 Simulator 则是在这台图灵机上运行的小程序。在这个框架下，Simulator 能够缓存 Verifier 初始化后的原始状态（即随机选边之前的状态），并在需要时将 Verifier 恢复到这一状态。这个特殊的状态重置功能就是 rewinding。

类似于现代操作系统中的虚拟机（VM），我们可以在某个时刻保存虚拟机的快照（snapshot），并在需要时恢复至这一状态，而虚拟机本身并不察觉时间已经被“回溯”。然而，需要注意的是，真正试图欺骗 Verifier 的作弊证明者（Cheating Prover）并不具备 rewinding 能力，因为它本质上是 Verifier 外部的另一台图灵机，无法对 Verifier 内部的状态进行操控。这也是simulator和cheating prover的本质区别: simulator可以在不知道证明的前提下成功“欺骗”verifier，而prover在不知道证明的前提下一定无法成功欺骗verifier (soundness)。

**证明多方安全计算协议抵御恶意敌手**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UKGssLbiaoNBc3zbMAmuH6ehWCZ3IQ9LuEvYZoB0pbibsHaUxdPMxFRZQ/640?wx_fmt=png&from=appmsg)

Coin Tossing协议过程如图所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UtGXmgcPQnpgPpOOP55lnUjHHUEwCN21HVA5Via0Zqs1jqH8pSJ3ico0Q/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5Uaum2pvomRof8Zso6VVOaUIjWMmctl6fFIAs9z5IW8JpJicibLZIlJojA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UNobfk1S87zL2n9Wn3juUEibeeVgFHlFuxextWpibXlDnJc6YXnjDrCxw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UFGVmjicKM6Iv9Vic577YiboZzbK1QfqXEZoCOqYRFYriaeuMibPX0hPXefA/640?wx_fmt=png&from=appmsg)

来源：知乎@hujwei

https://zhuanlan.zhihu.com/p/588114150

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

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=...