---
title: G.O.S.S.I.P 阅读推荐 2024-07-03 Racing on the Negative Force
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498353&idx=1&sn=d62d0967413b693930e5b7e34c976967&chksm=c063d4a8f7145dbe4aadbf6ddd2c545f9366e1891762957b5c885be0a766f5dee0bb99bf883f&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-07-04
fetch_date: 2025-10-06T17:44:07.115840
---

# G.O.S.S.I.P 阅读推荐 2024-07-03 Racing on the Negative Force

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21F0ib4RdPk9Q6HtHegicOdlxib7h1PgRXGrcuJ9DELONHotvOia3SvcATqaThrBS5jU7FB0I3QyMnfN7A/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-07-03 Racing on the Negative Force

Dandan@iie

安全研究GoSSIP

今天为大家推荐的论文是中科院信工所[陈恺老师课题](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247483658&idx=4&sn=efa4dc3726bfe58ce5155f1e2a47b34a&chksm=c0602fd3f717a6c5d915d267959a26351ee83280689a0df00eb6f134cbbdc554eb00ad1d7047&scene=21#wechat_redirect)组与印第安纳大学伯明顿分校[王晓峰老师课题组](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493315&idx=1&sn=29233e261379e0e2f6c6612f0d1c7772&chksm=c063c81af714410cac07e56d8e1c04f3a4ba26fb53c20f1c976f995a389554fa635ff0fb8696&scene=21#wechat_redirect)合作的关于漏洞根本原因分析的工作**Racing on the Negative Force: Efficient Vulnerability Root-Cause Analysis through Reinforcement Learning on Counterexamples**，目前该工作已发表于USENIX Security 2024。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F0ib4RdPk9Q6HtHegicOdlxib1DfggibfNLXASpB5KYSFwSrJGwPFekZuibbjl4HW2ooDRUDhJQln0NPQ/640?wx_fmt=png&from=appmsg)

# 研究背景

模糊测试，作为一种热门的漏洞发现技术，虽然能检测出软件的崩溃，但却无法诊断出导致崩溃的根本原因（Root Cause）。要想确保软件的安全，必须进行深入的分析，找出真正的“病因”，才能从根本上“治愈”软件。

那么，导致程序崩溃的根本原因是什么呢？通常情况下，这些根本原因与程序内部某些变量的取值紧密相关。以图1所示的CVE-2019-9077漏洞为例，如果变量`sect->sh_size`的值小于8，程序就会崩溃。具体来说，当程序执行到第16,187行时，`sizeof(eopt)`的值为8。这时，如果`sect->sh_size`小于8，`sect->sh_size / sizeof(eopt)`的计算结果就会为0。此时，程序会执行`iopt = cmalloc(0, sizeof(*iopt))`。然而，由于堆分配器的特性，`cmalloc`实际上为`iopt`分配的是一个大小为1字节的缓冲区。此外，对于16,197行的循环条件而言，由于`sizeof(*eopt)`为8且`sect->sh_size`小于8，`sect->sh_size - sizeof(*eopt)`的计算结果是一个负数（例如，0xfffffffffffffff9），而`offset`已在第16,194行被初始化为0，因此程序满足while循环的条件，进入循环。在循环内部，程序会在第16,203行和第16,204行向`option`所指向的缓冲区写入数据。其中，16,203行是向`option`的第一个字节`option->kind`写入数据，16,204行是向`option`的第二个字节`option->size`写入数据。由于`option`所指向的缓冲区正是第16,187行分配给`iopt`的大小为1字节的缓冲区（参见第16,195行），所以当程序在第16,204行向`option`的第二个字节写入数据时就会发生缓冲区溢出。根据上述分析，可以看到，这个漏洞的根本原因在于第16,187行和第16,197行中变量`sect->sh_size`的值同时小于`sizeof(eopt)`和`sizeof(*eopt)`（也就是8）。实际上，开发者在第16,182行之前添加的补丁也是如此，如图2所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F0ib4RdPk9Q6HtHegicOdlxibB69CiaXPOatMdPlDu5LEc9toClkXgVMoHzQiaB4OWPZqkdJlR5vaKQQQ/640?wx_fmt=png&from=appmsg)

图1: CVE-2019-9077的漏洞代码片段

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F0ib4RdPk9Q6HtHegicOdlxibKNOTlgTP7iaxticE1NAj4DeAMDT3AymtoMOH9AASfAQpPfXvn8YcuSVw/640?wx_fmt=png&from=appmsg)

图2: CVE-2019-9077的补丁

尽管通过手动分析可以准确地找到上述漏洞的根本原因，但这一过程非常耗时。因此，自动漏洞根本原因分析技术（Root Cause Analysis，RCA）应运而生。在这些技术中，最通用也最有效的是基于统计的方法（Statistical RCA），其中粒度最细的是基于谓词的Statistical RCA。这种基于谓词的Statistical RCA通过分析变量的取值与“程序崩溃”和“程序正常执行”之间的相关性，来识别可能导致崩溃的根本原因。具体来说，该方法首先会收集大量的测试用例（通常使用模糊测试技术来生成），监控并记录这些测试用例的执行结果（程序崩溃与否）及它们所访问到的变量的取值。随后，针对变量的取值信息构建谓词，并分析各个谓词与程序崩溃之间的相关性。例如，对于图1中的漏洞而言，假设当前共收集到了3个崩溃测试用例和5个正常执行的测试用例，它们在第16,197行的变量`sect->sh_size`上的取值分布如图3所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F0ib4RdPk9Q6HtHegicOdlxibZia3b4bCulQD2DTda2ibc8aj1iczGt8icQQwRv86tVpKP4PSSbyIdaQdLg/640?wx_fmt=png&from=appmsg)

图3: 变量sect->sh\_size的取值分布

* 在3个崩溃测试用例中，变量`sect->sh_size`的取值为1、4、7。
* 在5个正常执行的测试用例中，变量`sect->sh_size`的取值为8、9、12、17、33。

基于这样的测试用例集，Statistical RCA就会判断出：每当变量`sect->sh_size`的值小于8时，程序总是会崩溃。也就是说，谓词`sect->sh_size < 8`与程序崩溃之间存在着极高的相关性。

根据Statistical RCA的原理，可以看到，Statistical RCA的有效性极大依赖于参与统计分析的测试用例集的质量。如果测试用例集无法在变量上产生足够多的取值，那么一些谓词很可能表现出与崩溃高度相关，但实际上并不是真正的根本原因（即非根本原因谓词）。这些谓词会干扰Statistical RCA对真正根本原因的识别。目前，SOTA的方法都使用AFL来生成测试用例集。然而，AFL是一个基于覆盖率导向的Fuzzer，它专注于提高代码的覆盖率，而非增加变量取值的多样性。因此，SOTA的方法都选择花费12小时甚至一周的时间来生成大量的测试用例，以确保Statistical RCA的有效性。这样做存在两个明显的问题：

1. 针对每个崩溃，都需要耗费大量的时间。
2. 即使收集了大量的测试用例，也无法保证这些测试用例是不是足够了。

# 研究思路

通过深入分析，作者发现，实际上对分析结果真正有帮助的是那些反例（Counterexamples）。这些反例指的是违反当前谓词或改变谓词间排序关系的测试用例。举例来说，对于图1中的漏洞而言，假设在初期生成的7个测试用例上，第16,197行上的非根本原因谓词`offset < 1`表现出与崩溃高度相关（参见图4(a)）。如果后续生成了一个正常执行的测试用例并且其在`offset`上的取值为0（参见图4(b)），那么该测试用例就会违反`offset < 1`与崩溃高度相关的判断，从而降低该谓词与崩溃之间的相关性。在这种情况下，Statistical RCA就会认为，谓词`sect->sh_size < 8`相对于谓词`offset < 1`而言更可能是根本原因（参见图3和图4(b)）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F0ib4RdPk9Q6HtHegicOdlxibzrfy3uJaB1j41yDDsOFU6L9cXn8PYq0Ubic8Ce9IayicLBXpKpddicCbA/640?wx_fmt=png&from=appmsg)

图4: 变量offset在初期和后期的取值分布

根据这样的观察，作者提出了一个名为RACING（Root-cAuse-analysis on Counterexamples based reinforcement-learnING）的方法。该方法会在测试用例生成的过程中，实时评估每个新生成的测试用例对根本原因分析结果的影响，识别并保留那些对分析有实际帮助的反例，以优化测试用例的生成策略，从而减少生成无效测试用例所需要的资源消耗。

为了让Fuzzer以更大的概率去生成反例，RACING使用强化学习技术来学习如何选择合适的种子和变异操作。具体来说，作者在强化学习中自定义了一个奖励机制来指导这一学习过程。在这个机制中，每一轮的奖励值   由两部分构成：一部分  用来衡量违反谓词的比例；第二部分  则用来评估对谓词排名的影响程度。通过这样的方式，RACING期望学出一种更有效的种子选择和变异选择策略，以尽可能快地生成能够同时违反多个谓词或者引起显著排名变化的反例。

当生成的反例足够时，谓词间的排序会趋于稳定，继续生成反例对排名的影响将变得很小。因此，作者设计了一个停止策略：如果连续10轮排名的变化量都非常小，就认为排名已经稳定了，进而结束分析过程。

通过上述方法，RACING能够在较短的时间内生成足够的测试用例，有效克服了上述两个局限。具体的细节请参见论文。

# 实验效果

在一个包含30个漏洞的数据集上，RACING平均仅花费了27分钟就找出了所有漏洞的根本原因。具体来说，RACING在1小时内就找出了86.67%漏洞的根本原因，在30分钟内找出了80.00%漏洞的根本原因，在10分钟内找出了56.67%漏洞的根本原因，甚至在1分钟内还找出了13.33%漏洞的根本原因。而SOTA的方法Aurora（发表于USENIX Security 2020）要找到86.67%漏洞的根本原因则需要花费12个小时。不仅如此，相比于Aurora，RACING在排名方面也有所提升。具体来说，RACING将73.33%漏洞的根本原因都排在了top-10，而Aurora相应的比例为63.33%；RACING将33.33%漏洞的根本原因都排在了top-3，而Aurora相应的比例为30.00%。总的来说，RACING平均将根本原因的排名提升了3.8位。更多详细的漏洞信息和对比数据请参见表2和表3。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F0ib4RdPk9Q6HtHegicOdlxibn781H0FNTMwJziayJDicRpA2T2Mkn0eRK4K40LHqGWWFIZXRR5gJeufA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21F0ib4RdPk9Q6HtHegicOdlxibMbXaszBCP5RJzmk4xnZIibNic1rZT9mI9TkrIk5Dfo3CRk62mvDC2txg/640?wx_fmt=png&from=appmsg)

> 论文链接: https://www.usenix.org/conference/usenixsecurity24/presentation/xu-dandan

> 代码链接：https://github.com/0xdd96/Racing-code

#### 投稿作者介绍

徐丹丹 中国科学院信息工程研究所博士研究生
主要研究方向为软件漏洞分析与利用，相关研究成果发表在USENIX Security和IEEE TIFS等国际顶级会议和期刊。

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