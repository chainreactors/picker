---
title: G.O.S.S.I.P 阅读推荐 2025-02-08 Mr. DeepFake
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499685&idx=1&sn=2192b3d03b98204560ae0c5e42ea964b&chksm=c063d17cf714586aeab7c4db1d973a46815a8e2c51f05214d2231d1a4eea83367248310975e1&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-02-09
fetch_date: 2025-10-06T20:37:24.325240
---

# G.O.S.S.I.P 阅读推荐 2025-02-08 Mr. DeepFake

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GPvylVelOkbCUHTvIoyfJPaqYPhbDJjy3C3tibVemtGrq1nFkP3FhNTN8nXia9aJoaakQn9IBa4fGQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2025-02-08 Mr. DeepFake

原创

G.O.S.S.I.P

安全研究GoSSIP

最近这个春节，风头都被DeepSeek抢走了，那今天我们要反击一下，推荐一篇针对MrDeepFake网站进行研究的安全论文——*Characterizing the MrDeepFakes Sexual Deepfake Marketplace*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GPvylVelOkbCUHTvIoyfJPaKFcEgVUv9Ewib099V8IxzEfR4zoFlBke4TkFexkfN1GZmYRjKCicFiaA/640?wx_fmt=png&from=appmsg)

先看看这个研究对象——MrDeepFake——是什么：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GPvylVelOkbCUHTvIoyfJP2HHyP3lXQg1RShjr8hUzp5cvkFiaSeAjC1T4A2j0I4EO5ozBZbCdnmg/640?wx_fmt=png&from=appmsg)

（注意，官方网站是https://www.mrdeepfakes.com/ 一定不要忘记加s，我们今天的推荐接下来就要被举报了。）

本文的作者深入调查了MrDeepFake网站的内容，特别关注了这个“生态系统”里面的买卖行为和背后的动机。具体到细节，作者除了研究MrDeepFake网站上的视频，还关注了论坛上涉及付费购买deepfake视频的帖子，以及关于如何生产deepfake的教程等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GPvylVelOkbCUHTvIoyfJPlrbQx3IZ2uBESliavuIzzXicGfS2NFalSV0Adicp1dOtdSySl7OZzJiaQw/640?wx_fmt=png&from=appmsg)

本文有很多不便于介绍的内容，特别是论文的第四章，关于MrDeepFake网站上的视频特点的分析，建议大家不要阅读！！！不要阅读！！！ 直接进入第五章以后的内容，多多关注deepfake视频的背后的买卖生态和血汗工厂。

作者首先调查了MrDeepFake网站上线之后，相关的deepfake搜索的活跃度的变化，发现这两者有一定的相关性，说明MrDeepFake网站很可能助长了deepfake视频的传播：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GPvylVelOkbCUHTvIoyfJPQpIAD1ibTHjmV8ia0le41iavayAEKEdkiavHtkXjtSPRRmibwRroiaxtcS5g/640?wx_fmt=png&from=appmsg)

接下来，作者使用主题分析（Thematic Analysis，如果不清楚这个，可以去问AI解释下这个分析手段）调查了263个付费购买deepfake视频的请求（post），这背后反映的是MrDeepFake网站的运营模式——付费用户提需求，生产者按需生成fake视频。通过分析这些请求，作者调查了购买者的动机，这里面有点难以言说，我们只能跳过主要的部分，介绍那些比较奇怪的动机，比如说有一些买家会觉得自己是在推动“艺术创作”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GPvylVelOkbCUHTvIoyfJPm34MYK9EDicQT1lzJeS4hyvqVoDSsf5tkhicqbWSsOy4uBVnvByFUNoQ/640?wx_fmt=png&from=appmsg)

其他不多说，我们快进到论文对卖家也就是deepfake视频创作者的分析描述，在这部分，作者挖掘了这些创作者（甚至是创作团队）的特点：首先，卖家一般需要在MrDeepFake网站放一些自己的作品，作为给潜在的买家的广告，不同的团队还专注不同的风格（呃）；然后，统计表明，在网站上，出售视频的平均标价是87.5美元，也有卖到100美元甚至200美元的。此外，还有人在社区评论说在这个领域，AI是真真实实干掉了人类：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GPvylVelOkbCUHTvIoyfJPnjv4vAibemiar1bp9AzGXfqNyOtPIPt8kD8HB3anXZNM0BVutHqwLib9Q/640?wx_fmt=png&from=appmsg)

前面的内容太多不能说的细节，论文到了第六章稍微会好点，因为作者调研了创作团队的技术特色，这部分主要关注的是所使用的数据、软件工具和硬件平台。

首先，创作deepfake视频需要收集高质量的人脸数据，即使对于一个单一的对象，一般需要3000-15000张人脸数据才能帮助生成栩栩如生的视频。其次，这个领域主要是两个开源工具（xx和xx，不说名字）在竞争，不过它们用起来都很复杂，因此社区里面也有大量的“技术分享”来教你怎么用，而且更有意思的是，社区会去研究主流的AI研究论文：在调查中，作者发现有43篇学术论文被很多帖子提到，其中不乏来自CVPR（最多引用）和ICCV、ECCV、NeurIPS、ICML、SIGGRAPH等会议的论文。（这年头，不好好读论文，在哪个领域都混不下去！）在使用硬件这方面，创作者们也面临经费限制的问题，很多人还处在买不起GPU的境地，还有人对7x24运行所产生的电费账单感到头疼，不少人还分享了如何去薅一些云服务（例如Google Colab）的羊毛的方法，当然相关讨论太多了，云服务厂商只要发现了就很快封了这些行为。

作者还发现，MrDeepFake网站社区其实是一个比较友好的社区，特别是对新人提问的态度很积极，作为一个只有61万会员的社区，问题的平均答复速度和拥有两千六百万用户的Stack Overflow社区差不多（稍稍慢一点），而且很多帖子（72%）在三天内都会有人回复。另外，MrDeepFake网站也积极倡导“好人一生平安”的友善、和谐的讨论氛围，这个和我们已知的一些论坛是很像的对不对？

总结一下，作为USENIX Security 2025的研究论文，来自Stanford和UCSD的研究人员把调查对象指向了互联网的特定群体，也增加了我们对他们的理解，这篇论文的G.O.S.S.I.P推荐指数为：

> Weak Accept

---

> 论文：https://zakird.com/papers/mrdeepfakes.pdf

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