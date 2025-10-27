---
title: G.O.S.S.I.P 阅读推荐 2025-02-09 To Rust or Not to Rust
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499696&idx=1&sn=e8a9de304e3f20132c35ef90f8a7600c&chksm=c063d169f714587f905df034388e7fc99b707fde99052d101270a7df034da86b9c629aac2e1f&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-02-11
fetch_date: 2025-10-06T20:38:43.117699
---

# G.O.S.S.I.P 阅读推荐 2025-02-09 To Rust or Not to Rust

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21HBjYywNn2pibhZUQV0Ag8b9icwh41HjiaEIzfaQv7Al08h4Vl40zXMwrUQK5KQsGmPwcOQfmFksKiaBQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2025-02-09 To Rust or Not to Rust

原创

G.O.S.S.I.P

安全研究GoSSIP

最近几天Linux内核社区有一个不大不小的瓜：知名黑客、Asahi Linux project的主要负责人 Hector Martin（aka. `marcan`）跟Linux内核维护者 Christoph Hellwig 之间在经过一段时间的冲突（关于这个冲突的细节——和Rust开发社区想要把相关代码合并到Linux Kernel的诉求相关，大家可以去自行搜索）之后，矛盾激化，还牵扯到了另一个暴脾气——Linus Torvalds，于是最终局面失控，故事以`marcan`辞去内核维护者的身份暂告一段落：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HBjYywNn2pibhZUQV0Ag8b9mcNmffwurIXcG9qbrSic67CN1rX3nbyTCxZlugYfBLq1AvgXZVuJNMw/640?wx_fmt=png&from=appmsg)

这里还有另一个很搞笑的事情，国内自媒体可能完全是依赖于AI做翻译，根本没有去自己调查这个事件和阅读相关信息，上来就说“`marcan` 提到自己从 1991 年开始参与 Linux 开发，见证了 Linux 的成长，但现在他对一些现状感到遗憾”，并且标题党地把这个称为“34年开发者煽动网友逼Linus表态”，殊不知`marcan`本人才30出头，而实际上是另一位年长的开发者 Dr. Greg Wettstein（不是那个Greg KH）写了邮件（出处：https://lore.kernel.org/rust-for-linux/20250207121638.GA7356@wind.enjellic.com/ 大家可以去看看）给Linus并抄送给了`marcan`和其他一众内核维护者（注意到其中还有一位是我们G.O.S.S.I.P的老朋友呢）。

---

吃瓜结束，回到今天的论文，大家可能也意识到了，我们要介绍的内容和上面提到的八卦有一定的关系，这就是来自ACSAC 2024的研究论文——*Rust for Linux: Understanding the Security Impact of Rust in the Linux Kernel*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HBjYywNn2pibhZUQV0Ag8b9Y6Hu9yEy2S3dPZRjX0zicdyr9K30Y8ODt2H1ZvKcofUtSBjV8syQLRA/640?wx_fmt=png&from=appmsg)

这篇2024年12月发表的论文上来就跟大家说了结论：针对过去4年中在Linux内核设备驱动中发现的240个漏洞的调查表明，如果全部用Rust来重写这些代码（假设就是简单的抄作业，基本实现逻辑保持一致），那么有82个漏洞会被消灭，然而还有113个漏洞是换了开发语言也无法消除的，需要开发者理解Rust的特性并改写相关逻辑；而有那么45个漏洞跟用什么语言开发关系不大，即使用了Rust，只要开发者意识不到更深层次的语义问题，依然无法消除漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HBjYywNn2pibhZUQV0Ag8b9yyPobLxphBsic2CWtOgibYwJgXdyugqaDJo4gibKBicmzq8KweNXViaHgxg/640?wx_fmt=png&from=appmsg)

好，让我们深入阅读论文的细节，首先我们肯定要了解一下背景知识（也许刚刚在吃瓜的时候你已经了解了），那就是Rust-for-Linux （RFL）这个框架，它是一套为Linux内核提供Rust开发的设备驱动（同时基本保持内核架构）的框架。RFL的主要特征如下图所示：要实现一个Rust开发的设备驱动，首先RFL会自动生成一些binding代码，方便Rust代码调用原有的内核代码中的C接口；其次，开发者需要实现一个Rust crate来作为安全的设备驱动（纯用Rust开发）和Kernel之间的桥梁，因为这个crate要去调用unsafe的C代码（通过前面的binding），所以有一系列的开发要求，确保不会包含什么严重的安全隐患。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HBjYywNn2pibhZUQV0Ag8b9VXJzyQwuHVvccjzs5DxrwmIibNRc207E3VjGmH4T9m7Us0uM5pFC5MA/640?wx_fmt=png&from=appmsg)

为了调查到底RFL能够对Linux内核设备驱动的安全提供多大程度的帮助，作者首先统计了设备驱动中安全漏洞的情况，将其分为三大类别：

1. Safety Violation：主要就是传统的内存破坏、类型混淆之类的问题；
2. Protocol Violation：包括接口调用顺序、竞态（race condition）、ref count、sleep等稍微high level一点的实现问题（注意下表里面有一个typo：Atomic写成了Atmoic）；
3. Semantic Violation：这方面的问题更加high-level，基本上可以算成是代码的逻辑层面的问题（当然像missing return value check这种也可以算是linter要处理的问题）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HBjYywNn2pibhZUQV0Ag8b9WIC8Bx42gtficZNLzMnrSxibYfDLfGl1SmojbGNKFfg0tr6Otw0qDJ3A/640?wx_fmt=png&from=appmsg)

针对三大类别的问题，作者去调研了使用RFL以及相关Rusted drivers能够带来的好处，结果表明，让设备驱动“锈化”能够一定程度缓解安全威胁。在安全漏洞中，占了一半比例的safety violation是主要的受益者：由于Rust主打的就是一个内存安全，很多内存破坏相关的漏洞在使用Rust之后会得到缓解。注意这里并没有说“完全消除”有两个主要原因：第一是有一些内存破坏漏洞涉及到了往unsafe code里面传递数据，这种问题除非你在Rust代码里面把原有的代码（特别是涉及的一些数据结构）用Rust里面安全的结构重新实现，否则还是没法杜绝（那么请问用C++的相关数据结构是不是也能达到同样的效果？）；第二是有些问题即使进行了防御，可能也就是从原来的代码利用之类的高危问题弱化成了denial-of-service之类的中低危问题，可是对于内核来说这一样很麻烦（crash掉服务器可能比提权造成的问题更多……）例如下面这个例子，由于`4 * rgn_size * mtiles`会造成32-bit的整型溢出，所以需要一个指定一个64-bit的`usize`来确保不会有溢出问题，但是Rust标准的防护机制是在这里实施动态类型转换检查，在溢出的时候直接产生panic，而不是教你在写代码的时候就用`usize`来修饰，因此简单的C-to-Rust翻译并不是完美的解决方案，像空指针解引用、UAF等问题，还需要开发人员去主动增加一些辅助的代码，从而确保问题发生的时候代码能够稳定执行下去。总的来说，如果开发人员善用Rust，大约可以把95%的safety violation全部消除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HBjYywNn2pibhZUQV0Ag8b9iaKRXfjbhpoIJBm00F6pre1u8RdAx4xGoSLZuFMiar1ichQeZgibM2LIJw/640?wx_fmt=png&from=appmsg)

对于第二大类问题（protocol violation，约占整个安全漏洞的30%），这里面比较棘手的是接口调用顺序之类的问题，基本上跟用不用Rust没啥关系，好在这个问题的占比不高（5/240），而像race condition这种基本上就被Rusted code全部消灭了；对于ref count这类问题，稍微有点特殊，主要原因是如果用Rust对代码进行改写，可能需要开发者引入Rust的ref count机制（包括相关类型对象）来替换原有的C代码中的ref count机制，但是很有可能没有把原有的机制完全替换，如果Rust（safe code）和C（unsafe code）两边都同时管理资源 ，很可能会导致冲突（这个在一些关于Rust本身的安全漏洞的论文讨论中也都提到过）。

对于第三类问题，除了那个比较特殊的missing return value check以外，其余的问题其实都可以认为和程序设计语言的关系不大了，因此也就没法用Rust来解决，不过这个本来也不是Rust需要考虑的地方。

除了对设备驱动中的安全漏洞进行分析，作者也对已经“锈化”的一些Rust drivers（主要是Binder、AGX和 NVMe）进行了分析，关注其中使用的unsafe code的情况。下面这些统计数据可以给你一些更直观的感受：unsafe code在目前还是占了驱动程序代码中不可忽视的一部分。因此，作者在论文的第六章也专门总结了如何更为安全地使用Rust，以避免在C-to-Rust代码移植中把原来的错误引入过来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HBjYywNn2pibhZUQV0Ag8b97Ao2bT45o5VqReia6ArT3OwXAFTrjjgQ4FJTvEkJGibQaAcccsETBMibg/640?wx_fmt=png&from=appmsg)

最后，希望本文能为火气十足的Linux内核社区（及其外围）消消火，也能够给很多“卓越的意识形态压倒一切”主义者提供更多的理性参考，今天论文的G.O.S.S.I.P推荐指数为：

> Accept

---

> 论文：https://mars-research.github.io/doc/2024-acsac-rfl.pdf

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过