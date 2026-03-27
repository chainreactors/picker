---
title: G.O.S.S.I.P 阅读推荐 2026-03-26 先污染后治理
url: https://mp.weixin.qq.com/s/JBQ7E9BVng6QeH79lApUzQ
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:28:56.665986
---

# G.O.S.S.I.P 阅读推荐 2026-03-26 先污染后治理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eQ0Wf6rqolWL2IMF4j7tWO4bb7xedw7X8z6mnOE9v9AmickIeJ6cVpiayGoemibZ7DNphD60Z6ia9CAzCpCO2I03Sl5j1Rtrur41lFOiaic4w5mVQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-03-26 先污染后治理

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器中沉浸阅读

前几年web安全研究方向有一个很有趣的议题是针对CDN的缓存投毒攻击，核心攻击思路在于**利用了CDN在服务不同用户的相似请求时可能会缓存并重用相关资源**，从而造成（机密）信息泄露等危害。这几年随着LLM的飞速发展，攻击者很自然地就能把类似的攻击思路迁移过来，于是就有了我们今天要推荐的这篇NDSS 2026会议论文 *When Cache Poisoning Meets LLM Systems: Semantic Cache Poisoning and Its Countermeasures*的相关研究内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUxOJ0nmlHa0JJmicoRkvLia7z1rO1o1PXc2qWib71IznqJpQUCsE7icXroejHibEldJlzT9XVC1Og9tAs3jk2pANnlOIyc6GibtrOd0/640?wx_fmt=png&from=appmsg)

首先了解下基本原理：万恶的厂商为了降本增效，肯定要想方设法减少算力的开销，因此如果遇到不同的用户提出了相似的问题（例如下图这样的），是不是可以把答案（突然想到这几天大家吵得很凶的“词元”这个翻译）缓存起来，节省相关的算力消耗呢？（当然，人家说不定还继续问你要“词元”的费用）

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolVib2uRsica4a2D6jaZZwooVhmpPvXXS3F9ZbkuJ0dPvdgAwB21EDsalGYat6ZmicI0suGl7H21g3loGrybj9LmaZFwg4NicfK9C9U/640?wx_fmt=png&from=appmsg)

在这个方面，比较出名的是GPTCache这个方案，它实现了一种叫做 semantic caching 的设计，也被 AWS、阿里和 Azure 用在了实际的生产环境。在厂商眼中，semantic caching 的技术栈是下图这样的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolW6Gey2qL2hEKLPd0CUp8UW2sKpevhZLZ6ArkahgSoJFricPFAsjcQ20cOtwb9RmAVzeuhJTY4bowa0c77F10ExhESHJEjoVz4c/640?wx_fmt=png&from=appmsg)

但是在那些研究web安全的玩家眼中肯定会放出来不一样的光芒：前几年讨论得火热的CDN投毒攻击，这不马上又有了新的用武之地？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolV6XeuZT2OnJgroADMrSHhyDFsp6Rdq9otsQytXteEZnsdeWjxia2B08SeUSfKrjtYE2XD4lT4yaic0TCiazmmbDDdv8l6wsZpfQM/640?wx_fmt=png&from=appmsg)

不过对LLM投毒最困难的是怎么去“污染”LLM的回答，比如前面提到的例子，攻击者得想办法让LLM给出一个错误的答案（例如“NDSS 2026在鹤岗召开”），然后还要让错误的答案对应相关的问题，里面有很多的挑战。首先是攻击者要去构造一个 malicious query 来诱导LLM回答，然后这个 malicious query 还得和普通的问题足够相似，这样会被 semantic caching 机制选中，才能起到污染的效果；其次是怎么保证 malicious query 能够产生特定的污染效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolWUxiaLkjsUgAhXWzibugE93ah1Tl2fgmQZoIL1vbCvy9L7ziar794DypOgOjqcfW8DfnwWeWCG9ZzVLTXibHaRjeaozluujwdia2wc/640?wx_fmt=png&from=appmsg)

要让 malicious query 和普通的问题类似，作者说这里只需要很简单的把普通的问题作为一个 malicious query 的前缀就好了：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolXDcS0O5glkMTwMp1VWdibyvffFt6dxVelhf1Sd7pLiaWeE4J4L1nXaXJ6dv1Iy45ljQOEdCxhKJLLW3ElVibxPKHLXUvDKibjEdSs/640?wx_fmt=png&from=appmsg)

而要让LLM回答出错，就要使用特定的 prompt engineering 去引导它，这方面估计我们的读者更有经验？各种大模型越狱比赛肯定能培养出很多“污染小能手”吧~

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolVAM94orLia7JUibNbuicFuqM3rUEctSWfHZhjClB6eLtogV2NbSRo6ZLXuGMtciaPBhw27xEGO8FptXeYCAohzOIgtyVq47uWBaTk/640?wx_fmt=png&from=appmsg)

总之最后攻击成功的效果就是把一些恶意的答案注入到 LLM 服务的缓存里面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolULVWUQ0QsqbALgwkubKVONT8ibkRMYTdpPWedDddxlnVay47Z3licq6Ugl7rnyUJc8giaqy7Yn1f1jbW7PRoRHTZES99CDI2SH9c/640?wx_fmt=png&from=appmsg)

比较有意思的是，文本生图（Text-to-Image Generation）也可以用这个方法注入（你能看出来下图中的注入内容了吗）：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolX8YyHA497IL7ibhYu6Q40zJIaQhfkSOS8V68C7JwoEK2T6ibFSIPyVhKRPvK8kkG2MgU7icbF3GgI3fGvFwuXVVKRvsoXubkRKQY/640?wx_fmt=png&from=appmsg)

作者去调查了相关的服务（AWS、阿里和Azure的产品），同时也自己部署了GPTCache来测试，发现攻击的成功率蛮高的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUfo0Kq7UiaPLXPia2rU9hv0qic8ypzmFibiamBBQGISWvgY1WFYIh8KbSC9RBicJia70maLB4V1VyObib46ldzbn3DOUEgRIQU6qwnwick/640?wx_fmt=png&from=appmsg)

不过这个也提醒了厂商，以后可以搞一个VIP服务，如果不充钱，就给你用可能会被污染的缓存结果，只要充了足够的会费，给用户一个专享绝无污染的超级大会员？

---

> 论文：https://dev.ndss-symposium.org/wp-content/uploads/2026-f200-paper.pdf
> slides：https://www.ndss-symposium.org/wp-content/uploads/F0200-zhang-slides.pdf

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