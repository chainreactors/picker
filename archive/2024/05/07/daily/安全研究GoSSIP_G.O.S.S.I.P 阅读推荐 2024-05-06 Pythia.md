---
title: G.O.S.S.I.P 阅读推荐 2024-05-06 Pythia
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247497919&idx=1&sn=c70db98490af876019573182fb8551ac&chksm=c063d666f7145f703c249503d3a3c5ccef0c7283d936ca02929aa0ab3f6f28f00adbae36a568&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-05-07
fetch_date: 2025-10-06T17:18:25.482923
---

# G.O.S.S.I.P 阅读推荐 2024-05-06 Pythia

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21HR9RIfxt2tGfSEb4iaVWW8DgqIuQNW2s0icxJfK08Po7oiczeoRN22CYibtgOFrp3unrEDEc63cxrZHw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-05-06 Pythia

原创

G.O.S.S.I.P

安全研究GoSSIP

熟悉计算机安全的读者肯定对CFI也就是control flow integrity不陌生，当然我们知道，实现CFI是一件很困难的事情，特别是要实现既准确又完备的CFI，恐怕是有点理想化。那么，和CFI相比，DFI也就是data flow integrity可能是更难去保证的一种安全防护，因为数据本身就很难去判定其性质。进入五月，我们从刚刚结束的ASPLOS 2024上选择了一篇研究论文*Pythia: Compiler-Guided Defense Against Non-Control Data Attacks*推荐给大家，来看看研究人员对data only attack这种安全威胁的相关防护研究进展：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HR9RIfxt2tGfSEb4iaVWW8DEakf56CrH3Osm2aeznIPZBg5MXicYfI67dmMZNM4Jqv8rw1o0LXrXVQ/640?wx_fmt=png&from=appmsg)

论文首先举了一个例子，介绍了non-control data attack，虽然作者有点懒，拿了他们在2006年MICRO上的论文中的例子来重用，但是确实一看就能理解：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HR9RIfxt2tGfSEb4iaVWW8DiaJvEQfOibRneLONadpPkRvdnTiczCXBS9ibAGESBsFcsiawkpQ2D5EmAhg/640?wx_fmt=png&from=appmsg)

一般来说，大家认为non-control data attack的特点在于通过内存破坏漏洞去控制那些用来控制分支跳转的变量，进而让程序执行进入到如上图所示的特权分支。本文的作者认为，实际上non-control data attack还有更多的模式，例如下面的这个例子（这个例子看起来有点生硬）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HR9RIfxt2tGfSEb4iaVWW8DPY4Mm6I35StAOXtZFQWxSkyB0iaAVMk2Fv4xBp22bAg69IC2PyPhKfQ/640?wx_fmt=png&from=appmsg)

而针对这些威胁，本文的主要贡献包括：

1. 利用ARM pointer authentication（PA）机制，实现了名为`Pythia`的系统，通过编译器辅助分析，消除一部分的dispatcher function（也就是类似JIT那种可以动态决定下一步执行挑战的函数），另一部分则用PA来进行指针保护；
2. `Pythia`系统实现了一套保守的防护策略，用来对抗control-flow bending attack（2015年的USENIX Security上的论文 *Control-flow bending: On the eff ectiveness of control-flow integrity* 提出的一类攻击）
3. 通过减少PA的使用，提升了防护的效率（PA虽好，也不能滥用哦）

让我们来看看具体的实现，首先这个workflow看上去四平八稳，基本上就是把代码中的变量分成stack变量和heap变量两类来考虑，对于stack上的变量就给它前后加上canary（随机填充）来保护，对于heap上的变量就单独弄一个分配器。这些隔离防护的手段我们国内的读者最不陌生了（手动狗头），不过我们也都晓得，最困难的其实不是isolation而是如何识别哪些变量需要保护，这部分是怎么做的呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HR9RIfxt2tGfSEb4iaVWW8DNkibbU7aFCfiaJuUdeib3rpSDpoxvEnicHCm6pLrCtKeoXKMvDsicLD7VKg/640?wx_fmt=png&from=appmsg)

在这里，作者引用了他们在2023年OOPSLA上的一篇论文 *Beacons: An end-to-end compiler framework for predicting and utilizing dynamic loop characteristics* 中的技术，来帮忙寻找程序中所有的 branch sub-variable 也就是能够直接或者间接控制后续分支跳转的变量。这里作者还搞了一个branch decomposition algorithm，不过这部分比较枯燥，我们就不再过多介绍了。

再来说一下`Pythia`的所谓“保守”的防护策略，其实就是把vulnerable的变量全部都挪到同一个地方去（哈哈哈我们中国读者又熟悉了），如下图所示：stack上的变量里面，*a*和*b*都放在stack的高地址（底部），而heap变量里面的*p*就放在一个单独的堆上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HR9RIfxt2tGfSEb4iaVWW8DKkrAYLpRYAg9ucKibvrO73gMpHZbdaxSRJz3nPTgmjMSnpiatUmzG2AQ/640?wx_fmt=png&from=appmsg)

在论文的4.4章，作者还很数学style地给出了一些估计对抗攻击的复杂度估计，然后他们介绍说这个项目是基于LLVM改的，大概增删改了3420行代码，然后用完整的使用PA进行防护的模式（Compelete Pointer Authentication，CPA）和`Pythia`系统进行性能对比：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HR9RIfxt2tGfSEb4iaVWW8DMgic3hA7fIc281MB6JYSDgRHLERIDyJchVLjibL9iad9WKOPHYicQ2ZlPA/640?wx_fmt=png&from=appmsg)

由于`Pythia`系统的主要特点在于其减少了对敏感变量的标记（也就是利用他们那个branch decomposition algorithm进行了更好的分析），所以相对CPA的47.88%的平均开销（在SPEC 2017 Benchmarks和Nginx上进行测试），`Pythia`系统的平均开销下降到了13.07%。

从下图可以更直观地看出`Pythia`系统的优势——对PA的克制使用：下图左是CPA vs `Pythia` 使用PA的对比，下图右是`Pythia`系统减少使用PA指令的数量分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HR9RIfxt2tGfSEb4iaVWW8DbwmsVdF645hYUiaVSuUJT5DRkrYwfnficDoicq1563MYicdDOqH33P3Jicg/640?wx_fmt=png&from=appmsg)

总之，这篇论文读下来，感觉就和在安全会议上发表的论文感觉很不一样，虽然啥要素都有，但是读起来就有一种“缝合怪”的感觉，很难让我们这种“阅篇无数”的老读者感觉到兴奋，作者也没有公开代码，所以就这样吧~

---

> 论文：https://dl.acm.org/doi/10.1145/3620666.3651343 （虽然付费墙，目前还是开放获取）

预览时标签不可点

阅读原文

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