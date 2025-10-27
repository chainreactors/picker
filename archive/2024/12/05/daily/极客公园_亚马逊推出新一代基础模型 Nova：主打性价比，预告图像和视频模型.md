---
title: 亚马逊推出新一代基础模型 Nova：主打性价比，预告图像和视频模型
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653067158&idx=2&sn=e8b2a02229e7b1d21e48b414062a07ae&chksm=7e57ea2049206336eb5c863ba690d70368e7eb231a4ac095e7cd8e4e4fa06d4b53f7d67a794e&scene=58&subscene=0#rd
source: 极客公园
date: 2024-12-05
fetch_date: 2025-10-06T19:39:07.047298
---

# 亚马逊推出新一代基础模型 Nova：主打性价比，预告图像和视频模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5aZfUzDroVtsvBxSfb6n0Hd7OASMP2OGmQB8eoCXhro6SMtAJ3nW1tohXgeQSB1ZyqdEue87QpxLQ/0?wx_fmt=jpeg)

# 亚马逊推出新一代基础模型 Nova：主打性价比，预告图像和视频模型

原创

宛辰

极客公园

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5abwyEr8w6ibliaw5C5oagUDBa9LbvEbZIm5P66DTLibicWR3Q5qbOzMpgHvuWZTg0P3udCCwv9Jvddcg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5aZfUzDroVtsvBxSfb6n0HdQVTo4hJyUvCIoOS3cugDTKftack7jUFvOtZ6LGJ6HaiaZGhB6Uhb74A/640?wx_fmt=jpeg&from=appmsg)

自研模型和生态伙伴的模型，亚马逊都要。

**作者 | 宛辰****编辑**| 郑玄****

‍

亚马逊的新模型来了。

当地时间周二的 re:invent 大会上，在上午的 Keynote 环节，前亚马逊云科技（AWS）首席执行官、现任亚马逊公司 CEO 安迪·贾西（Andy Jassy）限时返场。在大约 10 分钟的演讲里，贾西介绍了亚马逊在生成式 AI 领域的应用进展，并发布了亚马逊的新一代基础模型——Amazon Nova。

去年 4 月，亚马逊推出了第一代大模型 Titan，只有语言单一模态。如果说 Titan 只是小试牛刀，那今天的 Amazon Nova 系列模型，是亚马逊的真本事和大动作。到底做文生文、文生图，还是图生视频……对亚马逊来说，这个选择不存在的。因为，Nova 系列主打 Any to Any，任意模态输入、任意模态输出。并且在 Benchmark 评测上，也均为 SOTA 大模型，几乎可以打败所有相同量级和市场定位的基础模型。

你可能要问，刚追加了 40 亿美元投资 Anthropic 及其 Claude，就发了自研的王炸 Nova。亚马逊怎么想的？尤其是怎么看待自己与模型生态伙伴的关系？

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0Hd7fVEwzSJF7picSZbTthbKbXG9xicJb7kUdeIK2l9p4fCzvLdicjf9CAqg/640?wx_fmt=png&from=appmsg)前亚马逊云科技（AWS）首席执行官、现任亚马逊公司 CEO 安迪·贾西（Andy Jassy）发布 Nova 系列基础模型。｜图片来源：亚马逊云科技

安迪·贾西（Andy Jassy）自问自答这一问题，他表示，在亚马逊内部构建的 AI 应用中，使用模型的多样性令人惊讶。开发者也是这样，希望有更低的延迟、更低的成本、具备微调能力、能更好地协调不同知识库以固定数据，还想要实现很多自动化协调操作（也就是所谓的智能行为），或者想要获得更好的图像和视频效果等等。为了满足开发者多样性的需求，亚马逊云科技的模型策略，就是给予开发者尽可能多的自主选择的权利。

「我们一直都在汲取同一个教训——永远不会出现一种工具能在某个领域一统天下的情况。就像数据库领域，10 年来，大家会使用各种各样的关系型数据库或者非关系型数据库。在分析领域也是如此，曾经大家觉得 TensorFlow 会成为唯一的 AI 框架，而一直强调会有很多不同框架出现，最终 PyTorch 成为了最受欢迎的那个，模型方面同样呈现这样的情况。」

让开发者可以按照自己期望的任意试验、组合运用模型，这是大模型时代，亚马逊的答案。

***01***

**Amazon Nova：**

**成本更低，能力更强**

会上，安迪·贾西公布了 Nova 系列的六种大模型，其中包括四种生成文本的基础模型，以及生成图像和视频的两种视觉内容生成模型。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5aZfUzDroVtsvBxSfb6n0HdR9J1qzScFyHsL9Yvhw7CBvKXboEYCkyKibkzibQicy6Fiazy6uMiaUcDo3w/640?wx_fmt=jpeg&from=appmsg)

**首先是体量最轻的 Micro 模型**，其属于「仅文本模型」，只支持输入文本然后输出文本，这也是 Nova 系列中响应速度最快、性价比最高的模型。贾西称，在 Amazon 内部的开发者最喜欢在许多简单任务中使用它。

贾西表示，在 11 个 Benchmark 测试中，Nova Mirco 的表现与 Meta LLaMa 3.1 8B 相当甚至更优，在 12 个 Benchmark 测试中与 Google Gemini 1.5 Flash-8B 相比表现更优。该模型的响应速度达到每秒 210 个 Tokens，非常适合需要快速响应的应用。

接下来三种支持多模态输入，并输出文本内容的多模态模型。

**其中 Lite 模型同样是一种低成本的多模态模型**，可以快速处理图像、视频和文本输入，并输出文本内容。

贾西表示，在 19 项 Benchmark 测试中，Nova Lite 有 17 项表现优于或等于 OpenAI 的 GPT-4o Mini；在 21 项基准中，有 17 项优于或等于 Google 的 Gemini 1.5 Flash-8B；在 12 项基准中，有 10 项优于或等于 Anthropic 的 Claude Haiku 3.5。此模型在视频、图表和文档理解任务上也有不错表现表现。

Pro 模型则是一种高性能多模态模型，可以针对多种任务提供最佳的准确性、速度和成本组合。

在 20 项 Benchmark 测试中，Nova Pro 有 17 项优于或等于 OpenAI 的 GPT-4o；在 21 项 Benchmark 测试中，有 16 项优于或等于 Google 的 Gemini 1.5 Pro。

最后也是最强的是，是 Nova Premier，该模型可以用于复杂推理任务，也可作为定制模型蒸馏的最佳「教师」。

贾西没有给出 Premier 的跑分对比，但从介绍中我们不难推断：该模型对标的是 OpenAI 9 月发布的 Orion 系列模型。

根据贾西，Amazon Nova Micro、Lite 和 Pro 目前已经全面上市，而 Amazon Nova Premier 计划在 2025 年第一季度推出。

除了性能以外，贾西表示这些模型还有其他亮点，首先，它们的成本效益很高，相较于 Amazon Bedrock 中的其他优秀模型产品，能便宜大约 75%。此外，它们的速度很快，在延迟方面表现优异，是所能见到的速度较快的模型。

已经上市的模型不仅集成在 Amazon Bedrock 中，还与 Amazon Bedrock 里的所有功能进行了深度整合。这意味着开发者可以对模型进行微调，或利用 Bedrock 的知识库、RAG 等对模型增强，或者利用 Bedrock 的蒸馏功能来将大模型的智能「转移到」更小的模型，从而提高效益并降低延迟。

除了四种生成文本的模型，贾西还预告了两个生成视觉内容的新模型。

首先是 Amazon Nova Canvas，这是一款最先进的图像生成模型，可以根据文本或图像提示生成专业级的图像。它还提供了一些便捷功能，例如使用文本输入编辑图像，以及调整配色方案和布局的控制选项。该模型还内置了支持安全和负责任 AI 使用的功能，包括水印功能（可追溯图像来源）和内容审核功能（限制潜在有害内容的生成）等。

在第三方进行的人类对比评估中，Amazon Nova Canvas 的表现优于 OpenAI DALL-E 3 和 Stable Diffusion。下面是由 Amazon Nova Canvas 生成的一系列图片：

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0HdicqPJSR2GZC5w7c7ysKd8HBWkrPR1sFNeU85JNXmaVGWGUoMJNricIwA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0HdvuwicZlof6XaJ9icsRCt1UYYWOsYY83JpToxbDlKtsuQm1NnkSAfVnzQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0HdbibKRwwickas1jsc6w4AzQKxo2aG9ukZjK3ibMk7yxgUFgkJcYnV3ZAeA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0HdtdibYqHjMSLiaHv8I56zPdv40qOMkS7qcZJTp5Htj6IERp67Pat3Jibgw/640?wx_fmt=png&from=appmsg)

然后是 Amazon Nova Reel，这是一款最先进的视频生成模型，可通过文本和图像轻松创建高质量视频，非常适合广告、营销或培训内容创作。用户可以通过自然语言提示控制视觉风格和节奏，包括镜头运动、旋转和变焦。在第三方进行的人类对比评估中，Amazon Nova Reel 生成的视频质量和一致性优于 Runway 的 Gen-3 Alpha。

由 Amazon Nova Reel 生成的视频｜视频来源：亚马逊云科技

与 Canvas 类似，Nova Reel 也内置了安全和责任 AI 功能，包括水印和内容审核。目前支持生成 6 秒的视频，未来几个月将扩展到最长 2 分钟的视频生成。

贾西还分享了 Nova 接下来的计划，首先是在明年开发出上述模型的第二代版本。此外，还会在第一季度推出一个语音到语音的模型，并在明年年中推出一个任意（any）到任意（any）的模型。也就是多模态输入到多模态输出的模型，这意味着用户可以输入文本、语音、图像或视频等多种形式的内容，并相应地输出文本、语音、图像或视频。

从 Titan 到 Nova，连发两个大模型的 亚马逊云科技，难免会有人担心与众多大模型开发商合作的 亚马逊云科技 正在改变其模型策略。

贾西显然意识到了，他在会上自问自答讲述了 亚马逊云科技 的立场：

「或许大家会问，该如何看待亚马逊云科技的模型策略？毕竟我们与众多模型提供商有着深入的合作关系，同时自己也研发了一些模型。我想说的是，大家可以这样来看待：我们一直以来的目标就是为大家提供选择，旨在呈现最广泛且最优质的功能，这必然意味着会有多样化的选择。」

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5aZfUzDroVtsvBxSfb6n0Hdgnom6S3BQyOMjl7qffBR8NZiczY6c36GHqAqQTduoLhTPcwjV4NfXvQ/640?wx_fmt=jpeg&from=appmsg)亚马逊云科技首席执行官 Matt Garman 介绍，在 Amazon Bedrock 上，开发者可以根据自身需要选择亚马逊或者任意生态伙伴的模型。｜图片来源：亚马逊云科技

***02***

**全球最大的电商平台，**

**用生成式 AI 干什么？**

除了发布新的大模型，会上，安迪·贾西还详细介绍了亚马逊内部的 AI 应用案例。

作为全球最大的电商平台，也作为亚马逊云科技的「第一客户」，亚马逊在过去一年尝试为多项业务引入 AI 提效，解决用户面临的问题。其中典型的场景如下：

* 零售业务中获得更优质的推荐以及个性化推荐；
* 为履约中心的拣货员规划最佳路径，从而更快地把商品送到客户手上；
* 将其应用在我们的 Prime Air 无人机上，期望在未来几年内实现不到一小时就能为你送货上门；
* Amazon Go 商店的 Just Walk Out 技术、为 Alexa 提供技术支持；
* 提供 25 种以上的亚马逊云科技 AI 服务，方便开发者构建 AI 应用程序。

从亚马逊观察到的 AI 用例中，安迪认为，解决问题的 AI 应用（「实用 AI」）有两种实用价值：降本增效，或者带来新体验。

「从全球范围来看，那些应用 AI 最为成功的公司，主要体现在成本规避和生产力提升方面，而且很多公司在这两方面都取得了进展。同时，你也开始看到一些完全重新构思、重塑的全新客户体验。」

在这两类 AI 应用上，安迪给了亚马逊内部的典型使用场景：

**降本增效的 AI**

**1）智能客服**

以客户服务为例，亚马逊的零售业务有着数亿客户，过去当他们需要联系客户服务时，可以联系聊天机器人，过去这一聊天机器人采用的静态决策树的机器学习技术，客户得输入大量文字才能获取答案。

但生成式 AI 对这个系统进行了重构后，现在客户拥有了一个懂他/她的客服机器人。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0Hd3WYgGnGsokYPbpf8SLfdXktrVmvpMnvuJ0fRL1XYq99XJGUqL85xeg/640?wx_fmt=png&from=appmsg)

比如，假如你几天前订购了一件商品，进入新的聊天机器人界面时，它知道你是谁、几天前订购了什么、住在哪里，而且它能通过模型预测到，如果在几天后联系客服，大概率是咨询退货相关问题。当你开始向它说明情况时，它可以迅速告知你最近的 Whole Foods 或者其他可退货的实体店位置。并且这个模型很智能，当察觉到用户对它给出的回复感到沮丧时，还能判断出用户可能需要联系人工客服来解决问题。

在重新设计之前，这个聊天机器人的客户满意度就已经挺高了，但自从加入了生成式 AI 这个「智慧大脑」后，客户满意度提升了 500 个基点。

**2）卖家工单填写**

亚马逊在全球零售店有大约 200 万卖家，销售的商品中超过 60% 是由这群卖家提供的，但他们过去在往网站上架产品时，需要填写一份很长的、包含很多字段的表单，从而让终端客户更便捷地浏览并了解卖家的产品信息，这对卖家来说着实是个繁重的任务。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0Hd5loIf42cgurMF41fZmRgIepmZhBhTrUUBibIoZrKdmXnicW0wDg7x3NA/640?wx_fmt=png&from=appmsg)

现在，亚马逊利用生成式 AI 打造了一款全新的工具，卖家只需输入几个字，或者拍张照片，又或者提供一个 URL，这个工具就能帮忙填写很多产品属性信息，这对卖家来说轻松多了，目前已经有超过 50 万卖家在使用这款生成式 AI 工具。

**3）库存管理**

亚马逊零售业务中的库存管理也是一个大场景，有超过 1000 个不同的建筑或节点，从而把合适的产品优化配置到距离最终客户最近的履行中心或者建筑里，以此节省运输时间，更快、更低成本地把商品送到你手中。但这也就意味着，要清楚某个履行中心的库存情况，比如每个商品的库存水平是多少、哪些商品正在被订购、订购的速度如何、这个履行中心是否还有更多的仓储容量，以及是否需要将库存转移到其他履行中心来平衡整个仓储网络等问题。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0HdcFlRJonV867xzmibwOhHXQKibggBm7uGJuv7kVZ0cTrzhw8VWF9XibpqQ/640?wx_fmt=png&from=appmsg)

为此，亚马逊运用 Transformer 模型来解决这些问题并进行预测，当前，一个对长期需求预测的 Transformer 模型已经将预测准确性提高了 10%，区域预测准确性也提高了超过 20%，在亚马逊数百亿美金的零售业务规模下，两位数的效率提升意味着数以十亿美元计算的成本节省。

**4）机器人**

在机器人场景上，亚马逊履行中心已经部署了超过 75 万台机器人，一系列 AI 技术帮助机器人场景优化了场地容量和传送能力，缩短处理时间以及为客户服务的成本。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0Hd5szwQggdNDMzDicdhXwFt4z73frqpY3Wf5O9EAA6GqwuxQBJhbsloBA/640?wx_fmt=png&from=appmsg)

以 Sparrow 为例，它是一款用于重新分类的机器人手臂。它需要不断从众多分散区域收集物品，并将它们汇聚到容器里。有了生成式 AI 的大脑，可以告诉 Sparrow 第一个箱子里装了什么物品、要它去拿哪个物品，同时 Sparrow 得辨别出每个物品具体是什么，还要清楚依据物品的大小、材质以及材质的柔韧性该如何抓取，并且知道能把物品放置在接收箱的哪个位置。

目前，亚马逊在路易斯安那州什里夫波特的履约中心推出了大约五项全新的机器人发明，已经看到处理时间提高了 25%，未来，服务成本预计也会降低 25%。

**创新客户体验的 AI**

上述这些都是亚马逊内部在成本规避和生产力提升方面的实例，亚马逊也看到了生成式 AI 在创造全新购物体验方面的作用，贾西也列举了几个典型例子。

**1）Rufus 购物智能体**

第一个应用是，Rufus 购物智能体。

当客户不确定自己想要什么，正在纠结选择时，可能会浏览商品分类、查看客户评价等，但现在 Rufus 购物智能体带来了「真人导购」的体验。

就像走进实体店，不确定自己想要什么时，向销售人员描述一下想法，他们便会推荐可能适合你的商品，继续问「这个怎么样，那个怎么样」，他们也能快速回复你。现在，Rufus 带来了类似的体验。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZfUzDroVtsvBxSfb6n0HdgFCa6YrCiaQFJngdmicJsXbHE7ksx71icSooE9qUeB7No8ZibFD79QNyvg/640?wx_fmt=png&from=appmsg)

借助 Rufus，你可以进入任何产品的...