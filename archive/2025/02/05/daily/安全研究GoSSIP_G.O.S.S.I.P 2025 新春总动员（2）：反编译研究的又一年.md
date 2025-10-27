---
title: G.O.S.S.I.P 2025 新春总动员（2）：反编译研究的又一年
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499661&idx=1&sn=76d0e94d245ff6aa345521b8bf4a4f17&chksm=c063d154f71458428c47a7c127c7aa10098db4d0d64253424108bd5b79a87e3ac38ff18f37a1&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-02-05
fetch_date: 2025-10-06T20:35:48.234201
---

# G.O.S.S.I.P 2025 新春总动员（2）：反编译研究的又一年

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FWJKME44yURXywxmFUyghX62ljMRlqmjJCZoNrFrZ1VygdpaOGLRM60dqHSuAeOj73TQhqgsHnFQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 2025 新春总动员（2）：反编译研究的又一年

原创

G.O.S.S.I.P

安全研究GoSSIP

过去的一年不仅仅是人工智能突飞猛进的一年，在安全研究人员非常关心的一项技术——反编译技术的研究领域，2024年同样显得与众不同：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FWJKME44yURXywxmFUyghXDCPgGLeyISp5Yz8DMbe0DNmw6ld1LA2uc6a4O2VbvbElroAMb7vcNw/640?wx_fmt=png&from=appmsg)

在夏威夷黑客 Zion Leonahenahe Basque（a.k.a `mahal0z`） 于2024年开年之初撰写的系列博客文章《30 Years of Decompilation and the Unsolved Structuring Problem》中，系统回顾了自1994年以来，反编译（decompilation）技术研究的进展和遇到的挑战（*你可能不记得这个人的名字了，也可能忘记了这两篇博客文章，那就去看看我们去年初的推荐文章《[G.O.S.S.I.P 阅读推荐 2024-01-19 反编译的“信达雅”研究](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247497158&idx=1&sn=130856553fd7f842b66391c3d88402c4&scene=21#wechat_redirect)》吧* ）：

> https://mahaloz.re/dec-history-pt1
> https://mahaloz.re/dec-history-pt2

为什么是30 years呢？如果你在进入21世纪之前就开始研究反编译，那么你必须听说过 Cristina Cifuentes 这个名字，作为一名杰出的女性计算机科学家，她可以毫不谦虚地接受“Mother of Decompilation”这个称号：早在1994年，她的博士论文（更有意思的是，该论文的提交日期是7月4日，让人想起来上世纪的科幻大片《独立日》）《Reverse Compilation Techniques》开启了学术界针对反编译的研究之路。这条道路是一条光荣的荆棘路，尽管难度极大，很多年来都很少有人能够坚持在上面开垦，更不要说顶级学术会议往往不太青睐反编译相关的研究，但是无数安全研究人员却会不自觉地把手伸向F5（对不对）！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FWJKME44yURXywxmFUyghXPibWCBZ5C1ozdcuu2icYWicWViarLHvEowOVsDcUKv84iay2CAke9ZDvOMA/640?wx_fmt=png&from=appmsg)

正因为如此，2024年可以认为是反编译技术研究的一个不算小的纪念年份，而作为 The Decompilation Wiki 的主要维护者，`mahal0z`在2024年刚结束就更新了博客，统计了2024年中，反编译技术的一些进展。

> https://decompilation.wiki/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FWJKME44yURXywxmFUyghXtgJSkI4BacoYQUk9w5vcgQjxNkRoGBuq1ItL5PLAzpJPx7a2cT9TgA/640?wx_fmt=png&from=appmsg)

在这一年中，一个很显著的变化是学术界开始更多地出现关于反编译的顶会研究论文。实际上，2024年一共有8篇相关的研究论文发表，而如果我们把2011年开始到2024年的所有顶会上和反编译相关的研究论文统计一下，你会发现这个总数一共才25篇！学术界此前对反编译的态度一直有点暧昧，一方面可能不觉得这个是novel的科学研究，另一方面又渴求黑魔法从天而降拯救二进制代码分析。`mahal0z`认为，可能是反编译研究社区坚持不懈推进这方面的研究，到2024年终于有很多好的结果涌现了。嗯，这挺像最近很火的另一个计算机科学方向的研究发展趋势

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FWJKME44yURXywxmFUyghXDQh8Da6ZhQhTmNxkkfWBBCvr8VEibYhZ2mXH8yzFKvcYpia2nRopJhzA/640?wx_fmt=png&from=appmsg)

`mahal0z`稍微总结了一下2024年的研究工作的三大趋势，它们分别是：

1. 科学地定义反编译的“质量好坏”
2. 人工智能 x 反编译
3. 学术理论在应用中落地

这三大趋势相关的研究论文在博客文章(https://mahaloz.re/dec-progress-2024)中都有详细介绍，我们就不再在这里赘述了。作为新春总动员系列，我们更关注的是去年的另一件值得记录的事情，那就是 Dr. Cristina Cifuentes 在2024年开启了环球演讲，激励了所有在这个领域坚持的研究者。这个活动在Recon 2024的keynote来到了高峰：除了 Dr. Cristina Cifuentes，还有 IDA Pro 的创始人 Ilfak Guilfanov 和 Binary Ninja的幕后技术大佬 Rusty Wagner 也都参与了峰会讨论。

> https://cfp.recon.cx/recon2024/talk/GYG8FH/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FWJKME44yURXywxmFUyghX5Wb5ILYR4O2FWQ9nt6Yh3gRNsCkAPicqYrmTYDe8cx2M6qAPOIqfwhQ/640?wx_fmt=png&from=appmsg)

最后，我们要仿写一段话来结束今天的文章（并未使用任何AI）：

> 刚刚告别的2024年，是实现智能化反编译伟大规划目标任务的关键一年，是全面深化反编译技术改革又一个重要年份，也是反编译技术研究的30周年。这一年，以`SAILR`、`D-Helix`、`DeGPT`、`ReSym`等研究论文为核心的反编译技术研究，带领全世界反编译技术研究人员积极应对学术和工业界进一步AI化的严峻形势带来的挑战，走过很不平凡的发展历程，取得令人鼓舞的成绩，顺利完成推进 state of the art 的主要目标任务，技术创新迈出了新的坚实步伐，反编译研究乘风破浪、行稳致远。

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