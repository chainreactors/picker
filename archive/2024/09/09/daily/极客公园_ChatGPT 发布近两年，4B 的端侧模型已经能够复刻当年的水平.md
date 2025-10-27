---
title: ChatGPT 发布近两年，4B 的端侧模型已经能够复刻当年的水平
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653054163&idx=2&sn=ff82c790ca0d54889a51de1da287eeed&chksm=7e57196549209073b67d5106ae3bd8e89e900dc760f647496db71e8880e7a3a85fa52c6e16a4&scene=58&subscene=0#rd
source: 极客公园
date: 2024-09-09
fetch_date: 2025-10-06T18:24:25.650700
---

# ChatGPT 发布近两年，4B 的端侧模型已经能够复刻当年的水平

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YuP6P3bxViccFVzicKTkjKGh7iaEUIgSdeBcCWsKiaaqNRuNue3MB99lF2IdoicGHv4bzr3bTynzM9SCg/0?wx_fmt=jpeg)

# ChatGPT 发布近两年，4B 的端侧模型已经能够复刻当年的水平

原创

Li Yuan

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YuP6P3bxViccFVzicKTkjKGhlXCC8Aic9gecTfP7YUHXHvIC453N8ZmVuTktmbqmUmZkm1D2C2pzWlg/640?wx_fmt=jpeg&from=appmsg)

端侧 AI 目前的应用进展究竟如何？

**作者 | Li Yuan****编辑**| 郑玄****

发布之初曾经让无数人惊艳的 ChatGPT3.5，目前已经能在端侧用 40 亿参数的小模型复刻了。

9 月 5 日，专注端侧模型的国内 AI 公司面壁智能，发布其最新的端侧基座模型。

新模型参数仅仅 4B，但是宣称性能超过 ChatGPT-3.5 Turbo，且长上下文表现优秀，函数调用（function calling）和 RAG（检索增强生成技术）能力。

端侧模型，即可以完全无需联网，纯使用设备端算力的运行的大模型，在去年大模型调用成本高企之时，曾经被人们寄予厚望，不少人认为端侧 AI 将是 AI 普及的重要必由之路。

而今年，大模型争相降价后，端侧模型的关注度有一定降低，然而端侧模型仍然被认为是智能设备和机器人未来能够变得真正智能的重要一环。

在 9 月 5 日的发布中，面壁智能 CEO 李大海也接受采访，聊了聊端侧 AI 目前的应用进展究竟如何。

**01**

****端侧 GPT 时刻已经到来？****

面壁智能此次发布的端侧模型为基座模型 MiniCPM 3.0。

在仅 4B 的参数量上，面壁智能宣称已经做到了在包括数学能力的各项能力上，超越了 GPT-3.5 Turbo。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YuP6P3bxViccFVzicKTkjKGhCrSOicvDbwfYhHx0UwBp2JYD7E6fqjzF4C4fxosdjyicIqyDePId3b7A/640?wx_fmt=png&from=appmsg)

除此之外，面壁智能此次发布的模型，亮点主要为在长文本上的能力突出和拥有函数调用、RAG、系统级提示词（system prompt）、代码解释器（code interpreter）等实用能力。

在长文本上，此次 MiniCPM 3.0 拥有 32k 上下文。

面壁介绍此次 MiniCPM 使用了长本文分帧处理（MapReduce）技术。

传统大模型使用长文本时，会把整个上下文都放进模型的输入中，而大模型的计算开销会因为输入的提升而极速上升，而尤其在端侧算力有限的场景下，会对性能产生制约。

长文本分帧处理技术，相当于把一段长文本拆成很多的子任务，通过子任务递归实现长文本的处理。

面壁表示，这种技术，相当于可以处理无限长的文本，模型表现并不会有任何降低。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YuP6P3bxViccFVzicKTkjKGhObhq8KiajnzUYd6euk8zvUdOiaVz6s6iciapSXdT9tLuMhoEaDBKIhQZEg/640?wx_fmt=png&from=appmsg)

**这对于运行在端侧的总结类应用，可能是一个很好的消息。总结类应用通常需要处理大量数据，且有可能文本不希望上传到云端——比如让****AI****分析跨越多年的聊天记录。**

函数调用，指的是让大模型连接外部工具和系统，把用户模糊化的输入语义转换为机器可以精确理解执行的结构化指令，例如通过语音在手机上调用日历、天气、邮件、浏览器等 APP 或相册、文件等本地数据库等。

这对智能设备厂商是非常重要的。使用函数调用的可以让手机智能助手等更智能——理解用户意图，从而执行复杂的操作而不需要用户输入繁琐的指令。

面壁智能强调，MiniCPM 3.0 不只是有函数调用功能，能力还非常强，在评测榜单 Berkeley Function-Calling Leaderboard 上，性能接近 GPT-4o。

而 RAG、系统级提示词、代码解释器等功能，传统上只有云端大模型才能完整覆盖。此次面壁智能征求了不少开发者的意见，也将其加入到端侧大模型中，方便开发者调用。面壁智能的模型是开源使用的。

**面壁智能表示，此次发布的模型进步很大，主要原因是采取了内部的第五代训练技术。端侧小模型在****训练数据****的精细程度上以及如何去训练这些数据上，都会有更高的要求。这一代在数据清洗的策略，学习的策略和配比的策略上都有优化。**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YuP6P3bxViccFVzicKTkjKGhdY0tB6TyiapNpgicOicvaoenW0VLVPjwesD6CBFkWW8a4XSZFeYYCkiclA/640?wx_fmt=png&from=appmsg)

**02**

**应用更多**

**仍在智能终端助手**

面壁智能之前表示，在做过实验后发现大模型时代存在新的摩尔定律：模型知识密度不断提升，平均每 8 个月提升一倍。即相同的模型能力表现，每过 8 个月，实现这样的能力的模型参数可以小一倍。

很明显，目前端侧模型的能力确实在快速提高。

不过在应用侧和消费者侧，目前端侧大模型的能力，确实仍然不是非常可感知。在发布后，面壁智能 CEO 李大海也对端侧模型在行业中的应用提出了自己的看法。

**目前的端侧模型，仍然更多地被用在手机、PC、汽车车机端等厂商的内置助手上，不过更多地肯定是采取端云协同的方式。**

对于这些智能设备厂商而言，端侧模型是不可或缺的。最重要的原因或许并不是断网可用，而是相对于云端的模型来说，端侧的模型有一个优势，可以更激进地，可以更全方位地使用用户本地的隐私数据。

而对于智能设备上的 APP 开发者而言，虽然 MiniCPM 3.0 这样的模型已经能做到相对不错的内存占用——MiniCPM 3.0 的模型量化后仅需 2GB 内存占用，但是仍然存在适配的挑战。

「一个 App 的用户量超过 100 万，那么它的用户的手机的分布就一定会千差万别，会有非常多的配置不同的手机，想要在当前阶段就在这些所有配置不同的手机上都去部署端侧模型，是非常有挑战的。」李大海表示。

而在智能硬件的创业上，极客公园目前观察到单纯使用端侧大模型进行创业的创业者也较少。在极客公园的交流中，主要原因是目前云端模型的成本已经降低，而价格极低甚至免费的云端模型的能力，比起端侧仍然有优势。

想使用端侧模型的，反而可能是一些想在内部应用中使用大模型的公司。

「我们有很多行业里面的客户和朋友，他们会把我们的 MiniCPM 拿到自己的内部，拿自己的数据，去做云端的使用。端侧模型模型能力足够强，可以直接拿去做内容分类、信息提取等等，很好用，且成本更低。」李大海表示。

除此之外，较小的模型具体的微调训练过程的时候所需要使用到的资源也更小。

**而走向未来，机器人或许是端侧大模型的另一个比较有潜力的场景。**

相比于智能设备，当大规模普及后，机器人可能更需要低时延、不会因为网络问题中断的大模型反馈。

不过，在通用机器人本身仍然没有完全爆发的时候，目前无论是云端大模型，还是端侧大模型，目前和机器人企业的合作都是探索性的。

**而对于面壁智能公司而言，将公司定位端侧模型本身，是一个很取巧的定位。**

智能设备公司对于端侧模型的需求本身是一种刚需。

而和智能助手通常选择接入多个云端大模型不同的是，对于设备厂商而言，一般只能选择一家端侧模型的提供商。算力的总量、内存的访存速度、内存的大小，都是限制因素。

「终端上一般只放置两个模型，一个大语言模型或者多模态大模型，一个图片生成模型。」李大海表示。

而国内备案可选择的，专注于优化端侧的模型是有限的。差异化的定位很可能有利于面壁智能的商业化。

面壁智能没有透露目前和 B 端客户的合作方式，但是表示对商业模式很乐观，认为不会落入之前 SaaS 领域 B 端服务的困境：「在服务一个客户的时候，肯定是项目制。但是我们服务的场景其实是趋同的。像车上我们端侧模型赋能的很多场景，其实和智能设备厂商也都差不多。最终我们的产品会逐步地标准化。」

\*头图来源：视觉中国

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**直播预告**

**你现在用的是**

**端侧模型还是云端模型？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Z5rEl2poJuZqVBGZteWibbvpuA2OibrtXHS6bAJibcYSkxdsV1VicAF088bxt3yluWTQeMyL38W8bfrw/640?wx_fmt=png)

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YuP6P3bxViccFVzicKTkjKGhs3VYjYOnkjcLqr0fzIE91bfNxdrGeAJUrzRjlgBOzJeE1Oz4CuuOLA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653054018&idx=1&sn=a74d826dd5be57bd61dbb357b098c387&chksm=7e5719f4492090e2884d606dd7b508619f9123b4dc678ca703f134609b65d7ab1d94ab995ee2&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YuP6P3bxViccFVzicKTkjKGhia7lL4qXAqiaONGGzNFOx7xcVMPAVhh7icTiaJOTFtANRgODwhXViapAnkA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653054018&idx=2&sn=729bb88c16a5f62d16aba0d5502d6fc4&chksm=7e5719f4492090e2f742b308d34ade1a10b35b86eeed34341dda0551d09ff43347bed894e5e7&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

极客公园

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

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