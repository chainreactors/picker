---
title: G.O.S.S.I.P 阅读推荐 2024-09-06 Key-Multiplexing Attack
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498821&idx=1&sn=da3e02f17fdb06719b47ac0360723091&chksm=c063d29cf7145b8aa9edbd5420f2cb75fcb8307c01520a5bea3959adf3499e0a90533e73701f&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-09-07
fetch_date: 2025-10-06T18:28:43.021205
---

# G.O.S.S.I.P 阅读推荐 2024-09-06 Key-Multiplexing Attack

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21ETPGoe5ebGic8w1UfLiaPlIEqtInp8VDcVjDibNVedaUR3MAWs4OvkckNfCoNdfxQ9wHmuBe4UId5ng/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-09-06 Key-Multiplexing Attack

Yinghua

安全研究GoSSIP

今天要给大家介绍的是来自DAC 2024中一篇引人注目的研究论文**Late Breaking Results: On the One-Key Premise of Logic Locking，**这项研究主要由Synopsys, Inc.的Yinghua Hu博士及团队完成并投稿，为逻辑锁定（Logic Locking）这一广受关注的硬件知识产权（IP）保护方法带来了新的思考视角。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21ETPGoe5ebGic8w1UfLiaPlIENMUnLApQzDszDFQ8bsUZhCpNVyRGDGUDfAA5SOuAxsrgLFhmIvorXA/640?wx_fmt=png&from=appmsg)

近年来，logic locking作为一种有前景的硬件IP保护方法，得到了迅速的发展。它旨在通过在电路设计中加入额外的可编程逻辑组件来防止在芯片供应链中第三方参与者可能实施的各种威胁，例如盗取电路设计和植入硬件木马 （hardware Trojan）。然而，传统逻辑锁定技术的安全性评估主要基于一个隐含的假设：**只有找到一个正确的密钥（key）才能揭示受保护电路的真实功能。**虽然这种“单密钥”假设 （One-Key Premise）长期以来主导着逻辑锁定领域的研究和发展，但它本身的合理性实际上很少受到质疑。

这篇文章大胆挑战了这一传统的“单密钥”假设，提出了一种全新的攻击方法。此方法不再局限于寻找唯一正确的密钥，而是着眼于找到多个错误的密钥，这些错误的密钥在组合使用时可以有效地解锁受保护的设计，就像是使用了正确的密钥一样。这样一来，攻击者可以将找到这些错误的密匙分解为一系列独立的子任务，在多核环境中并行化处理，从而显著缩短攻击时间。这种方法特别适合并行算力丰富的攻击者使用，在如今的芯片供应链之中，拥有这样强大算力并不罕见。

这一创新性的研究为逻辑锁定技术的安全性敲响了警钟。实验证明，与传统攻击方法相比，新的攻击方法可将运行时间减少多达99.6%。这表明，在“多密钥”假设（Multi-Key Premise）下，许多现有的逻辑锁定技术可能远没有它们看上去那么安全。这不仅揭示了现有安全假设的漏洞，也为未来的硬件设计提出了新的挑战和机遇。

接下来，让我们看看多个错误的密匙是如何帮助攻击者访问正确的电路功能的吧！

基于香农分解原则，逻辑锁定后的电路所表达的函数可以分解为若干项，其中每一项取决于施加在主要输入上的不同条件。例如，其中一个条件可能涉及输入端口的最高有效位（MSB）被设置为逻辑高电平或低电平。我们将相应的分解函数表示如下：

其中每一项代表了整体锁定的函数的一半。与整个被锁定的函数类似，表达式中定义的每一子项固然可以用正确的密钥解锁，然而它也有可能通过不同的错误密钥访问。如图1(a)所示，我们看到的是一个 3输入电路被3位密匙锁定后的函数的错误分布。在这种情况下，唯一的正确密钥是101。然而，通过检查当MSB为零时的子项（前四行），我们可以识别出三个错误密钥（100、110和111），它们也能成功解锁这部分功能。在分析MSB设置为1时（后四行）的子项时，也出现了类似的情况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21ETPGoe5ebGic8w1UfLiaPlIESODngxaA9x5KFZdhs9QWDETC8C44fU8loWTyPyPyo44n6trd5UEOibA/640?wx_fmt=png&from=appmsg)

假设攻击者已经拥有了两个密钥，而这两个密钥都各自可以解锁电路功能的一半。攻击者完全可以使用图1(b)中经过微调之后的电路示意图。在此电路中，这两个密钥作为输入提供给一个多路复用器（MUX）模块，该模块的控制信号的条件与之前使用的香农分解的条件一致。在这个例子中，控制信号是MSB的逻辑值。如此一来，这个电路在功能上将完全等同于使用了正确密钥之后的电路。

目前，基于“单密钥”假设最强大的攻击方法是SAT attack。本文作者将SAT attack进行合理改动，让其可以并行使用SAT solver，同时寻找多个错误的密匙，来解锁锁定的电路。具体的算法可以参考原文。

为了验证本文提出的“多密钥”假设的威胁，作者使用了传统的SAT attack（只找正确的密匙）和改良之后的SAT attack（同时找16个错误的密匙）来攻击LUT-based 逻辑锁定方法， 并对比他们的运行时间（表2）。具体来说，我们在电路中加入一个14输入的（2-LUT）模块，这相当于一个156位的密钥大小。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21ETPGoe5ebGic8w1UfLiaPlIEhS3O6nudT7MLKybgpsfk5LL31fuzbHibjynpDKwzAwfpC35gPvMpNMQ/640?wx_fmt=png&from=appmsg)

在表2中，作者详细列出了16个并行任务的最小、最大和平均运行时间。鉴于改良后的攻击效率取决于耗时最长的子任务的运行时间，作者使用最大子任务运行时间与基准攻击运行时间的比率来表示改良方法的优势。除了c5315以外，其他所有基准电路的平均运行时间减少了90.1%，其中最大减少幅度高达99.6%。在八个基准电路中，有六个的最大运行时间与基准攻击的比率低于1/16 = 0.0625，这表明即使在单核计算环境中也能显著提高效率。这一结果主要归因于将密钥搜索任务分成更小的部分，这不仅导致更小的SAT问题需要解决，还增加了更多密钥能够解锁子功能的可能性。

**结论：**

本文通过一种创新的攻击策略挑战了逻辑锁定技术中的传统“单密钥”假设。该策略能够高效地识别出多个可能的错误密钥，这些密钥共同作用可以解锁受保护的电路设计。未来的研究方向包括开发有效的防御措施，以应对新的“多密钥”攻击场景。

论文链接：https://www.arxiv.org/abs/2408.12690

作者简介：

Yinghua Hu于2022年在南加州大学（USC）获得电气工程博士学位，目前就职于Synopsys，专注于为芯片设计开发人工智能（AI）和机器学习（ML）算法的研究工作。在攻读博士学位期间，Yinghua的研究主要集中在为集成电路（IC）供应链中的威胁提供硬件安全解决方案，包括设计和形式化分析电路混淆方法，以防止IC逆向工程。Yinghua在多个知名会议的技术项目委员会中担任委员，包括DAC和IEEE  HOST。此外，他还是多个IEEE期刊的外部审稿人，例如IEEE TCAD和IEEE TVLSI。

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