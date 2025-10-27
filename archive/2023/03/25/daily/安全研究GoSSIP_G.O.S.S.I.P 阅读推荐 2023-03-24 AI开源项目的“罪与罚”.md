---
title: G.O.S.S.I.P 阅读推荐 2023-03-24 AI开源项目的“罪与罚”
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494657&idx=1&sn=3f5eeaceac0c48d01052ef2fecd33809&chksm=c063c2d8f7144bce3d6820888aae644bf0e47583a7df8d4e40e08883e475d500ce90b3ccc7a4&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-25
fetch_date: 2025-10-04T10:38:29.569035
---

# G.O.S.S.I.P 阅读推荐 2023-03-24 AI开源项目的“罪与罚”

![cover_image](https://mmbiz.qlogo.cn/mmbiz_jpg/uicdfzKrO21FGR4UE2rgfpoialu01hSEMw70ZvCaDytvAjRbvHiaoRyQr94ATibic1cjng6ovaZia6AuvT2YUoxr0rjg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-24 AI开源项目的“罪与罚”

原创

G.O.S.S.I.P

安全研究GoSSIP

先转载一条新闻：

```
文章来源｜公众号“Nature Portfolio”
原文作者｜Katharine Sanderson

上周，人工智能公司OpenAI推出了GPT-4——驱动其热门对话机器人ChatGPT的大型语言模型的最新版本。这个语言模型能根据几乎任何提示创作有人类文笔的文本并生成图像和程序代码，而且表现十分惊艳。该公司表示，GPT-4在此基础上又有了很大的提升。研究人员认为这些能力有望推动科研变革，但也有人感到不满，因为他们还没有使用权限，也不了解它的底层代码或是训练方式。科学家认为，这种情况下，人们对该技术的安全性会有顾虑，其对科研的帮助也不如预想的这么大。

3月14日公布的GPT-4有一个全新升级：它现在不仅可以处理文本，还可以处理图像。作为对其语言能力的演示，位于加州旧金山的OpenAI表示，GPT-4已经能通过美国律师资格考试，成绩位于第90百分位，而之前的ChatGPT版本只能进入第10百分位。不过，这项技术尚未向所有人开放，目前只有ChatGPT的付费用户可以使用。

“现在需要在等位名单上排队，还不能立刻就用上。”阿姆斯特丹大学心理学家Evi-Anne van Dis说。不过，她已经见过GPT-4的demo。她说：“我们在视频里看过他们演示GPT-4的一些能力，简直超乎想象。”她记得，有一次演示用了一个网站的手绘插画，GPT-4能根据这些插画生成构建该网站的代码，证明它能将图像转化为输入信息的能力。

不过，OpenAI对它的模型使用哪些数据训练、如何训练，以及它的运作方式讳莫如深，这令科研人员感到不满。“所有这些闭源模型可以说是科学界的死胡同，”开源AI社区HuggingFace的气候科学家Sasha Luccioni说，“他们【OpenAI】可以在他们的研究基础上越攀越高，但对整个科学界来说，这就是条死路。”
```

不管OpenAI有多么的不Open，我们在开源社区里面依然可以见到非常多的AI相关项目（例如大名鼎鼎的PyTorch和TensorFlow），这些项目可以说是支撑起了AI研究的半边天。今天介绍的这篇论文 *What Do Users Ask in Open-Source AI Repositories? An Empirical Study of GitHub Issues* 对开源的AI项目进行调查，分析这些项目在研发过程中产生的问题，以及开发人员是怎么去进行处理的。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FGR4UE2rgfpoialu01hSEMwlTicPcBicYSXXUEh2lic856uQibkXCqW09yl4lRxiar4naiaibhVE7LbicQXNA/640?wx_fmt=png)

不知道你是否有维护一个GitHub repo的经验，编辑部在维护GitHub repo时候，最经常遇到的问题就是大家会来提各种issue，特别是把运行时报错信息给交上来。这本来也是很正常的事情，在本文中，作者对 *Papers With Code* 网站 (https://paperswithcode.com/) 上的576个AI相关开源项目进行了复现实测，并对这些项目在GitHub上收到的24953个issue进行了分析，将所有的issue分为了13个不同的类别加以讨论，从而搞清楚到底在当前的生态环境下，主要问题是什么以及如何针对性解决。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FGR4UE2rgfpoialu01hSEMwRBLpZcu0SWFvpibyPc6libicE7b9UbtdhicshN35WIAfbiavjk2EMOz7TEg/640?wx_fmt=png)

如果你自己经常给别人的GitHub项目提issue，或者你自己就是一个拥有非常多star的GitHub repo的巨佬，那你对下图一定不陌生。一般来说，只要是有人用的项目，基本上都会有一大堆的issue（人气的象征~），但是这些issue中有什么特点和共性，我们的研究人员要对其进行总结。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FGR4UE2rgfpoialu01hSEMwFk4t2wyoibdAJGDgL6799VgoOIJrWX2dKBFdGdUN3GdPM0ZWbyLXSpw/640?wx_fmt=png)

在实际研究过程中（下图），作者不仅clone了研究对象的所有代码，还利用GitHub的REST API把针对每个repo的metadata和issue信息都收集起来，然后针对如下三个问题进行讨论：

1. 在提出的issue里面，大家讨论些什么（What do users discuss in the issues of open-source AI repositories?）
2. 项目维护者是如何管理并解决提出的issue（How are issues in open-source AI repositories managed and addressed?）
3. issue能否被解决和哪些特征更为相关（What are the relationships between different features and the closure of issues in open-source AI repositories?）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FGR4UE2rgfpoialu01hSEMwOhtuBuvz32TP1fJgEXlGfyamxfok0TkMgDVhrylCYMiciaMvAo18Ka9A/640?wx_fmt=png)

针对第一个问题，作者大概是对我国初高中历史教学非常熟悉，对“直接原因、根本原因和导火索”分得很清楚。作者明确表示，他们关注的是issue被提出来的“导火索”而非“根本原因”（也就是关注 the primary reason why developers raise an issue 而不是 the root cause of the issue），然后对所有的导火索进行分类：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FGR4UE2rgfpoialu01hSEMwr3ezjQxupb3J4yY1xXAziat4R5ens1ffGEvOlZkLWPApwj00Dqgrn3w/640?wx_fmt=png)

总结下来，大致有如下十三种情况会促使大家去提交issue：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FGR4UE2rgfpoialu01hSEMwZ8DGYJNwic6aiahiazSb1fEwMGYSk9QoDLdYdEr2a7OEx18Scfb7Qv2iaw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FGR4UE2rgfpoialu01hSEMwUwQ0fWt0jl6zPZuIg7soacsy6AnNoKo4Sff1sFGAqkSfiaKshtFfFcg/640?wx_fmt=png)

针对第二个问题，作者发现，在他们调查的24953个issue中，有8102个 (32.47%) 还没解决（open issue），而16851个 (67.53%) 已经处理完毕（closed issue）。在处理完毕的issue中，大约40%是“self-closed”也就是提问题的人就自己把它解决了，而在所有issue中有 11.79%的情况是处以无人关注的情况（ignored issue）。另一个有趣的现象是尽管所有被处理的issue的平均处理时间长达46.94天，但是处理时间的中位数只有4天！ 也就是说，一部分拖了很久才得到处理的issue拉低了平均值，但是50%的issue一般都会在4天时间内处理完毕~

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FGR4UE2rgfpoialu01hSEMwp8uCfJUCQsFXPmK5UyoD9DuVm9YDZreMofZUNJpo6iaA9yOicNp1N2BQ/640?wx_fmt=png)

第三个问题，在所有被处理的issue中，我们能观察到哪些特点？作者发现，在下表中，*p*-value小于0.01就说明这一项指标（每项指标的具体含义请参见论文的Section IV.C）和issue是否被处理有显著的统计相关性，而如果大于0.05就表明没有特别的统计相关性：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FGR4UE2rgfpoialu01hSEMwZg5vq9K6PhS1uz0gWBYq6sSRf7IRc7a4qiafbaiaeEw39VyrOnc6ekDA/640?wx_fmt=png)

总结一下，如果某个issue被分配了一个人去解决（有一个assigneee），那就更可能被close（好像是废话！）此外就是如果issue能够被贴上一个标签（这个听上去怎么好像是贬义词）也更容易被处理。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FGR4UE2rgfpoialu01hSEMw8znxTsUJGmA7eCVJibUSY0MWFiaW2UZte0Ogjvyx9kbAkmBFo3ttSJeA/640?wx_fmt=png)

作者还总结了一下repo来源的区别，也就是学术界 vs 工业界：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FGR4UE2rgfpoialu01hSEMwo4YlDJMGNMm9ZuZMkl0DCIklu33xiaUQLZice3crKgVA2zMWTrNuCNZA/640?wx_fmt=png)

最后，作者也提供了本文研究工作的各种材料，欢迎大家去给作者提issue（误）：

> https://github.com/soarsmu/Mining-AI-repos-issues
> https://cs.paperswithcode.com/paper/what-do-users-ask-in-open-source-ai

---

论文：https://arxiv.org/abs/2303.09795

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