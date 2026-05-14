---
title: G.O.S.S.I.P 阅读推荐 2026-05-13 三AI成虎？
url: https://mp.weixin.qq.com/s/aNBi-Knd3FU-EaJ1gWZpwQ
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:42:28.776137
---

# G.O.S.S.I.P 阅读推荐 2026-05-13 三AI成虎？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eQ0Wf6rqolUp3oicdbZMuC7DiasOzPEASJ9eel8YAmI0Ip3TztaFlHlJKSgkTmSn6juiaRsQdQibge76CL2IljPH6MQRgYxibza4TfYkVAiar4xdo/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-05-13 三AI成虎？

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 庞葱与太子质于邯郸，谓魏王曰：‘今一人言市有虎，王信之乎？’王曰：‘否。’‘二人言市有虎，王信之乎？’王曰：‘寡人疑之矣。’‘三人言市有虎，王信之乎？’王曰：‘寡人信之矣。’庞葱曰：‘夫市之无虎明矣，然而三人言而成虎。今邯郸去大梁也远于市，而议臣者过于三人，愿王察之。’王曰：‘寡人自为知。’于是辞行，而谗言先至。后太子罢质，果不得见。

在今年的SACMAT会议上，有一篇Bluesky Paper（这个bluesky模式很有意思，大家可以去看看，大概就是“高瞻远瞩”的模式）讨论了在当前多agent模式下，人类要去验证AI的工作，这个问题怎么以一种更为严格的形式来定义和分析，这就是今天我们要给大家介绍的论文 *The Treacherous Envoy Problem: Trust, Collusion, and Accountability in Multi-Agent Workflows*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUJIDOpVQb3hKKCjocEFk0PJQsOarbtpCxBjrlxcwIuWgNaIQhUzdWCV4pjuGacOZiaXCEeQ8GN5ic2MsGk2EhxVqleVFHdBV63s/640?wx_fmt=png&from=appmsg)

这篇论文定义了一个叫做**Treacherous Envoy Problem**（TEP）的问题形式，问题的名字援引圣经Proverbs 13:17 *A wicked messenger falls into trouble, but a trustworthy envoy brings healing*（奸恶的使者必陷在祸患里； 忠信的使臣乃医人的良药），那怎么理解TEP在AI时代的定义？

我们先回忆下前段时间的一个新闻，2026年初，携程因为滥用市场垄断地位被调查，收到顶格罚单65亿元，这倒不奇怪，因为很早以前大家就听说过“大数据杀熟”这个概念了。不过到了AI时代，这些巨头们最害怕的可能不是罚款，是AI代替人去查价格买东西。在本文中，作者正是用这个买买买的实例引出了问题：假设现在你想让AI帮忙找一个价格在500块以下，还可以入住前免费退款的酒店，你有没有想过这里面可能会涉及到什么安全或者信任的危机吗？

在携程时代（当然没有携程之前，外地人被宰得更狠），我们去订酒店的时候并不知道携程是否真的给了我们最好的价格，而在AI时代，当我们指挥现在的AI agents去帮我们搜索网页选择最低价产品时，也一样要怀疑这些人工智能助手是否真的给了人类足够诚实的答案（虽然人类肯定比ta们更加摸鱼和不老实）。最近的所有关于AI和人共处的文章，大家无一例外强调的就是人要学会验证（validation and verification），但是，要是你面对的是一群AI助手合伙起来（骗你）呢？

本文的核心就在于此：在一个multi-agent的工作流中，信息的流转变得相当复杂且不透明，我们要想去验证到底任务是否真正按照人类的意思去执行，就要把这个工作流给抽象成可以分析的模型，然后更为准确地定义其中的子问题，最后才能回答那个最大的问题——人工智能助手是否可信可靠。在本文中，提到最频繁的那个概念——envoy——实际上可以认为就是一个处理任务的agent，这个agent如果是不可信的（treacherous，又学到新单词了），我们就很容易被蒙骗，那如果处理任务的是多个agent，它们还会合谋起来欺骗人，那我们人类估计是被骗了还很难发现：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolVcxcLslibcGemedZzrOeUu00VR16wUvuQlqmy1EGaNClq4bEVBjKUrycTpkyG7xiaxnZ4WWJQq5SIQSsp0ibDiblw7FywKMTaEBE8/640?wx_fmt=png&from=appmsg)

因此，要对这样一系列很复杂的信息交互流程进行验证，本文作者首先给出了关于TEP流程非常细节的定义图（如下图），这里面涉及到大量的概念和定义，可能初读起来非常的晦涩，但是如果不这样去定义，可能就很难勾勒出来在现在这样一个multi-agent工作流背景下的清晰的安全模型，因此感兴趣的读者可以去仔细了解一下原文的细节（第三章）：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolXibL16BRcg2phpOb8tb6sMxNZNvDgohM2bEELKbuOunRicEu3GAsXqRyXspzc3qOQp2tP213LicZcGkf3knRevYgNLBusP3PfRVc/640?wx_fmt=png&from=appmsg)

论文的第四章讨论了另一个问题：为什么检测这些不可信的agent（或者说，检测agents的行为中是否存在不可信的成分）那么困难？作者用了一些信息论的方法，来展示了其中存在的根本性困难：不管你工程上如何优化，信息的传递本质上可能就是很难保证100%的可靠。

回到validation and verification上来，基于前面的模型，本文提出了这么一个“不可能三角”（三难困境），这里面其实很像现实中的人类社会，在社会活动中的监管、审计和契约合作都是典型的多方参与的事务，而里面如果只考虑其中的某个单方面事务，是很难发现并真正解决问题的，只有每个层面上的不同角色都合作起来，可能才有希望改善（而非完全解决）现有的问题。这既是人类社会遇到的问题，也是未来人工智能时代可能面临的第一个社会学问题？

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolVrlibSusMytibccCyYaOyJoRn6yqB9Om8ETiclKWVhhePXy40bkyZLr2Yuqiaoqq6utqunTLHt1RVD6gOpPPEZCzHJvy6OH7gttew/640?wx_fmt=png&from=appmsg)

本文的作者之一是我们G.O.S.S.I.P的老朋友林志强教授，他最近和大家一样，在AI对计算机特别是安全领域产生巨大冲击的浪潮中始终在思考，这篇文章的核心目标，也是希望能够提出一个和byzantine general problem、millionare problem那样的问题，促使大家去思考，在人工智能成为水电这样的基础设施之时，也有一个更为黄金的标准来衡量它的可信度。

---

> 论文：https://zhiqlin.github.io/file/SACMAT26.pdf

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