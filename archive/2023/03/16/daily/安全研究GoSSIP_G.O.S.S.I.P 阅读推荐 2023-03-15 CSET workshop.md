---
title: G.O.S.S.I.P 阅读推荐 2023-03-15 CSET workshop
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494526&idx=1&sn=312c7a4083b878b8dc6355c50133c3a0&chksm=c063c5a7f7144cb1c8ea9fb2dcd79dd2afe84946f3135e1e8e98de5fe0740beec7921672877e&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-16
fetch_date: 2025-10-04T09:45:14.401373
---

# G.O.S.S.I.P 阅读推荐 2023-03-15 CSET workshop

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21HTsE2ep1E9coNTiaRL59qiccgYpZGNqXY6vBhbWMbAhDctrendrIJvIT6kdib4zRIiau5GaokHibpibekQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-15 CSET workshop

原创

G.O.S.S.I.P

安全研究GoSSIP

四大安全会议的论文是不是都有点读腻了？今天为你介绍的是一个小众但是却有一定历史（已经举办了15届）的workshop——Workshop on Cyber Security Experimentation and Test (CSET)，这个workshop本来是USENIX赞助的，但是到了2020年，由于疫情影响了USENIX的财政状况，所有workshop都被中止了赞助，CSET的组织者决定不能放弃，把自家workshop独立运营起来并且希望能有一天重回USENIX。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HTsE2ep1E9coNTiaRL59qiccqPXESUZtibAibTsVwt0IMXtBPDtvondb0eEgRiaxPd8ic9CQmiaReNxdrdg/640?wx_fmt=png)

CSET是一个非常注重实验的workshop，里面的内容都非常实际，而且尽管没有了财政支持，workshop只能在线举办，但内容（包括论文、slides和视频）都全部在网站上公开，非常友好。我们在CSET的网站上看到2022年的议题中有不少值得阅读的内容，首先要给大家推荐的是来自工业界的作者发表的 *A Broad Comparative Evaluation of x86-64 Binary Rewriters*

> https://cset22.isi.edu/slides/binaryrewriters.pdf

在这个报告中，作者对近年来二进制代码热门的研究主题——binary code rewriting进行了调研，对目前市面上常见的binary code rewriter进行了横向测评。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HTsE2ep1E9coNTiaRL59qiccKT1LIyBj1EiaAwcqOicTILSwwHAB4VN6XgmMVFX1icU9SO3wzicxGsHY3Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HTsE2ep1E9coNTiaRL59qiccT4KrOdJN4g0FtbGkibfBAFyatSRibFZHGxE4fgJ6KToAI3jziczjNXQWw/640?wx_fmt=png)

实际上我们在前天（2022年3月13日）的阅读推荐中就已经介绍了一篇对基于reassembly的binary code rewriter进行评估的论文。在这篇报告中，作者扩展了评估的范围，同时还引入了OLLVM，让binary code rewriter去处理包含代码混淆的二进制可执行文件。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HTsE2ep1E9coNTiaRL59qiccDZSoo8b3vXA9xYmgJApZ6MqqQ5Jfpx8lm3aE4icnLJ6fVmJibVW9524w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HTsE2ep1E9coNTiaRL59qiccOjosr047bAEibk1Zgdq5dDbV5KK0dvNceytPZBIu9lyjuUqnZzsaOEA/640?wx_fmt=png)

分析结果表明，有很多rewriter存在适用性问题（例如只支持no-pie binaries），从下表看起来，效果比较好的几款产品应该是`ddisasm`、`e9patch`、`egalito`和`zipr`，如果大家去年就关注我们专栏，应该还能记得起来我们推荐过`e9patch`和`egalito`的相关论文！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HTsE2ep1E9coNTiaRL59qiccV3iaQRngG5Cf7QyzpiayMGicPaiaGciaVwNKoKYon0DBSibYVlSjHVwHMF6Q/640?wx_fmt=png)

最后作者给了一个评级：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HTsE2ep1E9coNTiaRL59qiccn9sLHNbb6Vpm66uJRYgDOObwp6MmAtWqv6UPOmia3abqVlUlkhhV5sA/640?wx_fmt=png)

然后作者又指出了一些研究的挑战：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HTsE2ep1E9coNTiaRL59qiccabebOcluEJKr49SvEAPvxibLKrKcTJwJWE4JibxYdDkjr3iar8MjzbmLA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HTsE2ep1E9coNTiaRL59qicc3lwsEoiciaib5iapugyibfTdIzEPRD5WA8YwcbXib3Ux3uxjTjXMtIVFvsIQ/640?wx_fmt=png)

---

CSET上面还有很多很简单但是有趣的内容，比如下面这个关于数字化形式的实体（文件）信息如何在删除后逐渐消失的研究，让我们想起了一本经常在国内被网友拿出来吓人的书——《尸体变化图鉴》

> https://cset22.isi.edu/slides/bodyfarm.pdf

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HTsE2ep1E9coNTiaRL59qiccj5lEXe0QqRdqWIbFmzHewW6icMNoPVsrfojOJAeN0kUBNYkkmsjzLYw/640?wx_fmt=png)

还有在线教学系统`Aquinas` (https://www.aquinas.dev/) 的介绍（感觉CSET上面的很多内容都很适合做“靶场”的人去copy）

> https://cset22.isi.edu/slides/coursescode.pdf

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HTsE2ep1E9coNTiaRL59qiccpKmrAY0jp7K142WC7r5gyrvqecWaibqukcqMYpj2xkQkrx9cUfjChiaQ/640?wx_fmt=png)

---

更多有意思的内容等待你去挖掘，如果对CSET感兴趣，可以访问官方网站获取全部内容，当然也可以关注一下2023年CSET是否能重回USENIX Security~

> 2022会议议程： https://cset22.isi.edu/program.html

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