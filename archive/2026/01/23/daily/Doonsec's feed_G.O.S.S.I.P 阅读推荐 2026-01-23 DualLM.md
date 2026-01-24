---
title: G.O.S.S.I.P 阅读推荐 2026-01-23 DualLM
url: https://mp.weixin.qq.com/s/NlWufm7TyptiSZeGhms4-w
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:24:50.379208
---

# G.O.S.S.I.P 阅读推荐 2026-01-23 DualLM

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21EOLutPPzsQfwhKSBOG3XXb6FkXFJPhgsA8InIVl2fdVzk8lbribyqF081QLFibspBicUBkaPAvb5eVw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-01-23 DualLM

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器中沉浸阅读

先来看一段介绍（是不是很AI）

```
如今，LLM 几乎能胜任各种网络安全任务，这本身已经不再让人惊讶。

真正令人意外的是：我们依然很难真正信任它们给出的答案。

在很多安全分析流程中，结果几乎无法自动验证：

👉 我们真的发现了一个 0-day 吗？
👉 这个补丁修的是 use-after-free，还是一个并不可利用的普通 bug？

所以，我们没有强迫 LLM 一定要“给答案”，而是换了一个问题：

如果模型知道自己什么时候不该盲目自信呢？

在我们即将发表于 NDSS 2026 的论文中，我们研究了如何利用 LLM 对 Linux 内核安全补丁进行分类
（例如 OOB、UAF，或其他较难利用的漏洞类型）。

半年前，通用大模型已经“还不错”，但距离我们的预期仍有差距。

我们的答案是：DualLM。

第一步，我们让一个能力很强的 LLM 显式找出补丁中能够指示漏洞类型的具体线索。

如果这些线索缺失或不够明确，
第二步就回退到一个专门为内核安全分类训练的本地小模型。

当模型“有把握”时使用推理能力，
当模型“不确定”时依赖领域专长。

通过这种方式，DualLM 在不假装 LLM 无所不知的前提下，实现了 约 85% 的分类准确率。

有时候，一个 LLM 最聪明的决定，是知道自己该退一步。
```

**有时候，一个 LLM 最聪明的决定，是知道自己该退一步。** 这大概是NDSS 2026论文 *What Do They Fix? LLM-Aided Categorization of Security Patches for Critical Memory Bugs* 的核心思想

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EOLutPPzsQfwhKSBOG3XXbianXiaicj6tZfHLr12AtE8FWLjDSBtQUTCXUP7lcqwzLcApkXbndrvRfg/640?wx_fmt=png&from=appmsg)

过去的2025年，随着LLM的不断进化，很多人认为基于静态分析（static analysis）的代码漏洞检测技术已经要被基于LLM的代码漏洞检测取代了。而对于安全补丁（security patch）的理解，似乎对于LLM来说就更轻而易举了。不过本文作者似乎并不认可这个观点，他们首先列举了一些Linux内核相关安全补丁的commit信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EOLutPPzsQfwhKSBOG3XXbAFZib5mUWP1nC4SXxcLXKMyJw5zcricPpGc7qXCrv93CAicflDIZgqE7g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EOLutPPzsQfwhKSBOG3XXbaiafibUpfA08tvhXr0m54s49icxUsAMUcfao4fI80G1PlEMLGiaz084WZw/640?wx_fmt=png&from=appmsg)

可以看出来，即便都是安全补丁，相关的commit信息既可以是清晰明了也可以是语焉不详。那你可能会说，我们当然不能只看commit信息，还要看code diff的信息嘛。例如下图中的两个patch，就很清楚地展示了out-of-bounds漏洞的修复：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EOLutPPzsQfwhKSBOG3XXbIyfhB1FuLVK6SrDtW4GewQ6MgYILYOoBttPVVNov3UlAHBaXlL1d7Q/640?wx_fmt=png&from=appmsg)

可是现实情况（特别是在Linux内核中）总是复杂的，例如下面这个例子，如果你在分析的时候不去追溯更多的上下文信息（context），你可以并不清楚这个额外的`addr==3`检查和out-of-bound安全漏洞的相关性，不过说到上下文嘛，这恰好又是LLM的劣势了……

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EOLutPPzsQfwhKSBOG3XXbmCOsD2CW17JXFrKkiaVbmh6QgxdL1DkjUahkDetvKRdia8oaI33f3UDQ/640?wx_fmt=png&from=appmsg)

在本文中，作者设计了一个叫做`DualLM`的系统，用来替代人类去分析理解所有的代码补丁，识别其中和安全相关的补丁，并且能够对涉及到安全问题的类别（例如越界读写、UAF操作）进行分类。这个`DualLM`系统正如前面所介绍，使用了两类模型：通用的强力LLM（例如GPT、Claude之类）和专用的安全LLM（作者自己定制化的SliceLM），关于怎么使用通用LLM去识别不同类型的安全补丁，大家就去读一下原文吧（又变成prompt engineering了），我们重点介绍一下基于SliceLM的分析流程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EOLutPPzsQfwhKSBOG3XXbLHbS9BYWpEIvp5cj8DmgEcqOz5s85YHpYicoU8XzibvmRWkPiaCAGiaicqg/640?wx_fmt=png&from=appmsg)

SliceLM的分析主打一个特点：*to classify patches without hints*，这是什么意思呢？就是说这个分析过程要依赖SliceLM自己去理解代码（特别是涉及到复杂的context）从而理解安全补丁的类别，这就特别要求SliceLM可以去做传统程序分析的工作——代码切片（code slicing），获取和补丁相关的上下文代码。SliceLM是作者预训练的一个BERT-based language model（具体的训练细节有点杂乱，要去阅读论文的第五章和附录才能完整get到），它的主要作用是用AI而非静态分析的方式去做代码的前向后向切片，作者表示，这样做的好处是SliceLM可以更“注意到”那些和diff相关的语句，而传统的静态分析因为是基于语法而非语义的，经常会把切片弄得很大而引入很多无关的代码。

除此之外，SliceLM还做了两个特别的操作，第一个是能够把一些特定的函数进行重命名，例如有个函数`l2cap_chan_hold_unless_zero`和内存操作强相关，为了帮助理解，SliceLM会先把它重命名为`increase_reference_count_if_not_zero`，这样在后面的安全漏洞分类过程中，准确率就会进一步提升。第二个操作是针对一些比较复杂的补丁中出现的冗余和重复的内容，SliceLM能够自动把它们都清理干净。经过这些处理，最后SliceLM就得到了一个比较“易读”的输入，只需要对其进行分类即可！

在实验中，作者将SliceLM和TreeVul（ICSE 2023）和SID（NDSS 2020）进行了对比，效果上当然好过已有的这些工具，而且正像前面介绍的那样，SliceLM可以在**不假装 LLM 无所不知的前提下，实现了 约 85% 的分类准确率**。

作者还举了一个实际的例子来展示SliceLM的实力：在下面这个例子中，SliceLM首先是准确地识别出了patch对应的是一个UAF漏洞，而在Syzbot平台上却并没有被标记为UAF相关。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EOLutPPzsQfwhKSBOG3XXbtAUIpicBQIqBxKXrIksopJaNtx5HxZv7If4wKB20yicHrYT9yymCTbCw/640?wx_fmt=png&from=appmsg)

同时作者还确认了该漏洞的可利用性：由于UAF漏洞影响到了28行的`timer`指针指向的对象，攻击者只需要执行堆喷操作（heap spraying）就可以覆盖掉`timer->function`，然后再等待`call_timer_fn`函数在计时器超时后执行就可以实现控制流劫持了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EOLutPPzsQfwhKSBOG3XXbmiaowKomzEjTgaqe9FoR6LcHPMnBod6bWKoX3Gib4ib1z71HpLbR2PibOA/640?wx_fmt=png&from=appmsg)

---

📄 论文： https://www.cs.ucr.edu/~zhiyunq/pub/ndss26\_duallm.pdf

💻 代码： https://github.com/seclab-ucr/DualLM/

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