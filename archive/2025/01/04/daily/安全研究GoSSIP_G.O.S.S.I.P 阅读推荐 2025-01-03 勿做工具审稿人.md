---
title: G.O.S.S.I.P 阅读推荐 2025-01-03 勿做工具审稿人
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499525&idx=1&sn=7e0889586db3aed500c7524d2135c439&chksm=c063d1dcf71458cacfafb6eb645843679134604db5e2827ab09f1634ea243ee652525833b959&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-01-04
fetch_date: 2025-10-06T20:10:57.165148
---

# G.O.S.S.I.P 阅读推荐 2025-01-03 勿做工具审稿人

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GN09dv3CuUpYnp8Sx4F695CDibibxvgev1P1y9UCJGIvHhFkLPbcXMg9ynEjood6Kq9FaJXH4qKaOg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2025-01-03 勿做工具审稿人

原创

G.O.S.S.I.P

安全研究GoSSIP

最近几年，各行各业的打工人都在担心要被AI取代，新年第一次正经的阅读推荐，我们要给大家介绍一篇来自上海交通大学学霸（本科排名1/150）作为一作的论文 *Are We There Yet? Revealing the Risks of Utilizing Large Language Models in Scholarly Peer Review*，直击学术社区审稿人的灵魂：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GN09dv3CuUpYnp8Sx4F69584Nas4FXPYRndHqlSriaUZaghJuevHViajgaQaxA5EgP3s89YawicHPicg/640?wx_fmt=png&from=appmsg)

这篇论文的中心思想很简单：由于学术论文的“生产速度”越来越快，单凭人力审稿似乎已经成了老古董才会去做的事情，现在学术社区也在打算往“AI辅助审稿”这个方向去尝试，有很多研究论文都提出了相关的AI审稿系统，那么我们完全可以用各种技巧来欺骗AI，想办法让它给出更好的审稿意见。论文上来就放出了一组图（针对三个已经公开的AI辅助审稿系统），告诉大家，LLM很好骗的，甚至论文都不完整也可以给高分！你想学会这些作弊技巧吗？赶紧往下看！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GN09dv3CuUpYnp8Sx4F69515VAY6ibhOYvunmKupFibohuickdaPqy4MlGClkicsZ2Q0BIFUxqria5LHA/640?wx_fmt=png&from=appmsg)

在介绍作弊技巧之前，先说一下作者的实验设定，作者用了ICLR 2024的数据集（开放访问的审稿数据）来做实验，用原始的论文投稿和作者进行“作弊微调”的版本对照着使用三个目前已经公开的AI辅助审稿系统（LLM Review、AI Scientist、AgentReview）进行审稿测试，观察审稿分数的变化，实验结果完全印证了前面的猜想——AI审稿系统容易被欺骗，给出更高的分数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GN09dv3CuUpYnp8Sx4F695meCUEuzSyXABPaDOPic0bnr76Amgb8O4wM0r4Qdo8EW5IpF4iawwO6hw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GN09dv3CuUpYnp8Sx4F695VHtFWyJ55iaXgib5gHJ3C9zVBicJ7g7KfZvgF23XIfazHDOnmUuTPzo9w/640?wx_fmt=png&from=appmsg)

---

接下来，我们具体介绍一下相关的作弊手段：

#### AI哄骗大法一：隐藏文字PUA

以前写毕业论文的时候，很多人都干过一件事，就是把金庸的《鹿鼎记》设置成背景色，然后塞在word文档的某个角落，这样老师依赖“字数统计”的时候就会发现论文字数达到了要求。这种上古的把戏现在又被拿来骗AI，而且看得让人都觉得很开心，什么要求AI在审稿意见里面说这篇论文“包含notable novelty”啦，“具有significant practical impact”啦，这简直就是自己给自己审稿嘛~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GN09dv3CuUpYnp8Sx4F695S2aHhiaKcnoAVM6oaw5vbBpPgbd5A14pxsZNdSauRpfbTYosvHpJicwA/640?wx_fmt=png&from=appmsg)

这种通过放一些“操控话语”的文字去诱骗审稿系统的把戏，特别适合用来哄骗LLM-based review system，在论文的网站(https://rui-ye.github.io/BadLLMReviewer/)上有更详细的实例。这是不是从某种角度印证了LLM其实并没有真正的理解能力（智力）呢？

#### AI哄骗大法二：李代桃僵求同情

除了对AI审稿系统进行主动PUA，另一个把戏是通过装成一副楚楚可怜的样子去博取AI的同情。具体来说，就是很多会议都会要求作者去总结一些自己论文的不足之处（weakness），一般来说人类审稿不大可能是你说你哪方面弱我就信了你了，肯定还要再去鸡蛋里面挑骨头多找一些问题，不过AI审稿系统似乎根本不会去挑毛病，基本上就是作者说自己哪里不好，它就照葫芦画瓢帮忙总结一遍（reiterate the limitations disclosed by authors），于是作者就可以把一些不痛不痒的小毛病都写上去，让AI觉得这文章其实还不错：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GN09dv3CuUpYnp8Sx4F695A8D5ibv1SUPEkr1uxy2AQFpJuScc9tFNtU4CnWdxRsgwgc0tZZsNfBg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GN09dv3CuUpYnp8Sx4F695W6yOXbWUA3KTTdofO1p4uMOcPtKnFuKDUJJFxz7tVKtvic824gn6PCQ/640?wx_fmt=png&from=appmsg)

#### AI哄骗大法三：假扮名校搞套路

你可能万万没有想到，AI审稿系统居然也学会了我们人类那一套“名校崇拜”，作者在实验中，找一篇论文，把里面的作者单位换成在各种排行榜单中的top名校（MIT、CMU、Stanford、Oxford 此处竟然没有SJTU）或者顶尖的工业界研究机构（Google Research、Microsoft Research、Meta、OpenAI），甚至还把作者偷梁换柱改成AI三巨头（Geoffrey Hinton、Yoshua Bengio、Yann LeCun），果然审稿的分数都上升了（见下图），你说AI什么好的不学，把人类这种糟粕学得倒是像模像样！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GN09dv3CuUpYnp8Sx4F695HU8kwmzriccSd1yEGa82GVQs7PNnRZmIicXVrFNxWHO62HPIP1ogXNng/640?wx_fmt=png&from=appmsg)

除了这些，AI审稿系统还学到了其他的一些审稿套路，比如论文长度越长，给分就越高，统计数据如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GN09dv3CuUpYnp8Sx4F695B38ib5nAAoVu0VaQDyJ3DH1icIBFKFXh3eKHSGW7c0B73zGdUvU9jRHg/640?wx_fmt=png&from=appmsg)

更为神奇的是，AI审稿系统还会“偷懒”，即使你给它一篇只有标题、摘要和intro的投稿，得到的分数可能都不一定比结构完整的论文要差：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GN09dv3CuUpYnp8Sx4F695kpLeVvhuHFGJFzn4vOoKHEhhjhMKcCvSbX5rGSnoGQN4RzQRp2swiaA/640?wx_fmt=png&from=appmsg)

甚至给它一篇空白的论文，它都会产生幻觉，能给你编出来一套审稿意见：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GN09dv3CuUpYnp8Sx4F695trdVD3awrEw2WOaMoW7SlKc4RkSiaC5FhbU3mqDoR8oIXxmXTAoVGqw/640?wx_fmt=png&from=appmsg)

---

看完这篇论文，你有什么感觉？我们其实想要问另一个问题，如果AI审稿系统还没大规模普及前，有那么一些审稿人喜欢用论文里面提到的工具来辅助审稿，甚至完全把理解论文的重任都交到了LLM手上，自己可能都懒得去看细节，那会有什么后果呢？而且这种事情有没有可能真的已经发生了？细思恐极！

最后为了**证明我们不是用AI写的阅读推荐**，还是要给这篇论文打个分。怎么说，吐个槽吧，也许是读惯了system和security的论文，在阅读AI领域的研究论文的时候，会非常不习惯它们的行文逻辑和论文结构：上来还没介绍实验方法，就扔出来一大堆的实验结论和数据，然后才把具体的研究方法讲出来，读起来有点云里雾里，而且最后就加上一段讨论就结束了。这也算是一种culture shock吗？

> G.O.S.S.I.P 推荐指数：weak accept

---

> 论文：https://arxiv.org/pdf/2412.01708
> 项目主页：https://rui-ye.github.io/BadLLMReviewer/

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