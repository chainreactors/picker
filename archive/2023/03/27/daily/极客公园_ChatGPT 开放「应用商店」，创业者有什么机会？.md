---
title: ChatGPT 开放「应用商店」，创业者有什么机会？
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2652987307&idx=1&sn=3a42a0b55e47c2549af426952e2e612e&chksm=7e54221d4923ab0ba8ecff05e415ec9058d24f989a49213b0ebcdf2911aa993fd8dacda4694f&scene=58&subscene=0#rd
source: 极客公园
date: 2023-03-27
fetch_date: 2025-10-04T10:46:34.659214
---

# ChatGPT 开放「应用商店」，创业者有什么机会？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5a22aSFn4SCCoE1dMWK2Q89BWu3pSqzEQXSLmRr9rvF27EB6dhMfSsfAxnvY45SicZA1WQk4liaia3Jg/0?wx_fmt=jpeg)

# ChatGPT 开放「应用商店」，创业者有什么机会？

极客公园

以下文章来源于Founder Park
，作者Founder Park

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5WmgV1o3EiaCiab839tNFuZAlaJCadCedmxgxQzXQnaqIA/0)

**Founder Park**
.

来自极客公园，专注与科技创业者聊「真问题」。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5a22aSFn4SCCoE1dMWK2Q89N0Q5ZbEm2SXsyKFgsJpC03CkiafkXombmh3980I3O9iaRjYTT2Bm3Myw/640?wx_fmt=png)

不管是作为操作系统还是应用商店，AI 的转折点已经到来。

**作者 | Founder Park**

3 月 24 日，OpenAI 又公布了重磅消息，ChatGPT 支持接入第三方插件，并且一口气上架了 11 个插件。通过这些插件，用户可以用 ChatGPT 购买商品，预定酒店、机票，搜索专业数据等，这大大解放了 ChatGPT 的生产力，也多了更多的可能性。

关于插件功能的未来发展可能性，我们看到了很多讨论，出门问问创始人李志飞认为这是「AI 巨大的转折点」；阅览室创始人王俊煜，则认真研读了 OpenAI 的开发文档，试图梳理出插件的更多可能性；懂技术又懂哲学的微博博主木遥则认为这可能是自然语言编程的新开始。

在获得几位授权后，我们迅速整理了这些讨论，分享这个消息纷繁日新月异的环境下，一些来自创业者和技术人员清晰的思考。

**李志飞**

**AI 的巨大转折点**

**出门问问 创始人 & CEO**

OpenAI 插件可以连接 ChatGPT 与第三方应用，通过接入你的应用做什么呢？举一些例子：

* 实时检索信息，例如赛事的实时比分情况、股票价格、最新资讯等；
* 检索知识库，例如针对你个的人电脑、针对公司的文档知识库等，进行更智能地检索、调用、对话；
* 代替用户执行操作（对现实世界的「智能调度」）：例如买机票酒旅、网购、订外卖等。
* 总结来看，逆天的 ChatGPT Plugin 主要体现在以下三个方面：

**独立上网**

现在的 ChatGPT 已经能够独自上网，访问网页并将其内容传输至 ChatGPT，然后根据该内容生成答案，并将相关网页链接信息附加于答案中。这类似于 New Bing 的功能，此举难道预示着微软和 OpenAI 或将貌合神离？比如你可以问 ChatGPT「哪位演员、哪部电影获得了此类别的奥斯卡？」结果可以看到，ChatGPT 在聊天界面就多出来「浏览」结果，直接得到了 2023 年的最新结果。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5a22aSFn4SCCoE1dMWK2Q890ibYmvW7Rvx9H6owRsCSeUctTOxiaoRE6TuTpqsTy5266NCENEOn8ZwQ/640?wx_fmt=png)

**自主编写并执行程序**

在这次重大更新中，ChatGPT 实现了自主编写和执行代码的功能。以前，ChatGPT 仅支持生成代码，但生成的代码还需要复制到其他执行器上才能运行。现在，ChatGPT 内嵌了 Python Code Interpreter，将代码编写和执行合二为一。这一改进特别适用于处理大量计算、数据分析和文件格式转换等任务。官方解释指出，代码解释器采用 Python 处理上传和下载的实验性 ChatGPT 模型。目前，主要提供以下功能：解决定量和定性的数学问题、进行数据分析和可视化，以及实现不同文件格式之间的转换。按照这个趋势，感觉 GitHub Copilot 的打开率会下降？当 AI 拥有了自己的智能、计算、存储和执行环境，还需要我们人类做什么？

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5a22aSFn4SCCoE1dMWK2Q89eZF8KibapLmeLao8RWHEoq3KfrMAU1ATHREUtdQ9FZSr1f1LqArFXsA/640?wx_fmt=png)

**调用第三方程序**

针对第三方程序，开发者可以按照 ChatGPT 的格式提供一个 manifest 文件，即 API 使用指南，让用户可以用自然语言提问，ChatGPT 就可以神奇地自动调用第三方接口，以满足用户的需求。

为什么这个过程可以称为「神奇」？因为在此之前，NLP 中常见的语义标注是一个繁琐的数据标注过程，但通过调用第三方程序，这个过程可以直接跳过。

另外，因为 ChatGPT Plugins 是主控程序，那第三方都成为了 ChatGPT 的 CP/SP（content/service provider），之前提到的 App 内搜索和结构化搜索都成为可能，LLM 是否已经作为新的入口若隐若现了？

**最后**

几乎所有这些技术的发展都是可以预见的，只是看到 Demo 视频时，还是会被惊叹于这突如其来的神奇感——它进化得如此之迅猛。

前几天，黄仁勋宣布 AI 的「iPhone 时刻」已经到来，而现在又有人表示 ChatGPT 成为了新的操作系统，并且已经拥有自己的应用商店。

我认为，这个新生物种可能是一个集内容生成、搜索和推荐于一体的「怪胎」，但对于 AI 来说，无论如何都是一个巨大的转折点。在这个新物种不断发展的过程中，我们需要怀着开放的心态，不要试着用过去的眼光去理解它！它是一个全新的事物，而我们正在拥抱新的未来。

部分内容转载李志飞公众号「飞哥说 AI」

**王俊煜**

**OpenAI 可能是第四次工业革命的****Google 或者 Apple**

**阅览室创始人、产品设计师**

其实关于 ChatGPT plugins 的大部分 myth，读 OpenAI 这个简短的开发文档都可以得到解答 [1]。

比如说，这是不是意味着 ChatGPT 变成了一个操作系统？从操作系统的经典定义 [2] 来说，肯定不是。ChatGPT plugins 做的事情，是在「适当时候」让 ChatGPT 可以和外界打交道。现在的 ChatGPT 是一个受过良好本科教育的知识工作者，不幸在 2021 年 9 月就被你抓到了一个白房子里面关着，就跟美国那个 Jony Ive 一样。你问它的很多问题它凭借自己的积累是可以解答的，只是不知有汉，无论魏晋。

现在，你和它说，我问你某些问题的「适当时候」我允许你出去走走，看看外面的世界是不是有更好的答案、更好的办法。比如，机票价格怎么样了？Tik Tok 的听证会怎么样了？你不是理科不好吗，让人帮忙解个方程怎么样？有些事情，干脆你也帮我办了吧。比如，既然问了机票价格，就顺便订个机票吧！[3]

它说好啊，但我怎么知道应该去哪儿解决你的问题呢？其实世界上这些工作都已经有不同的仆人做得很好了，让这些仆人先来我们这儿登记一下。这样我们就知道，机票可以去找这个叫 KAYAK 的，新闻可以去问 Bing，解方程可以找 Wolfram Alpha。它在「适当时候」照着登记册出去问了问题，然后回来用它的语言告诉我答案。

这里还有一个厉害的地方是，在这个世界中这些仆人是不说人话的。它们用一种叫 API 的机读语言和其他人进行交互。过去，我们日常用的手机 app 可以代替我们将界面上的操作转化成这种特殊的语言，但我们这位被关了两年的朋友，却能自动把我们说的人话自动翻译成这种语言。

这不是操作系统，而是一种对世界上已有服务的 API 通过自然语言进行索引和整合的方式，也给所有已有服务提供了自然语言界面。通过它你可以利用已有的服务获取数据，也进行少量的行动（这一点实际上是出于安全的限制）。

当然，你可以说着这有点儿像一个操作系统，毕竟用户可以交付任务给它……那么它也有点像一个浏览器，有点像一个应用商店，有点像手机桌面，有点像搜索引擎，虽然我觉得它最像的还是……3721 中文网址导航。

用比喻来讨论问题总是不精准的，取决于你关心什么方面，希望获得什么样的隐含暗示。就好像说现在到底是 AI 的 BlackBerry 时刻还是 iPhone 时刻还是 iPhone 3GS 时刻还是 iPhone 4 时刻……Depends。

至于说这个 plugins 系统可以自己给自己写 plugin……至少在目前是不准确的。OpenAI 联合创始人 Greg 在 Twitter 上说的不错，一个 plugin 的开发很简单，你就是为一个自然语言模型来写 API 文档。但这个前提是你得先有 API。如果你已经做出一个 Wolfram Alpha 了，要接入的确是很简单的。就好像给 Chrome 写一个 web app 其实也很简单，因为本质上那只是一个已有网站的书签。

当然了，既然 GPT 已经可以帮忙写代码了，所以你用 GPT 从 0 开始写出一个 plugin 理论上是可能的，但这不是 plugins 系统的开箱体验。Greg 说的「为自然语言模型写 API」，并不是大家所理解的「用自然语言模型来写 API」。目前 plugin 的接口仍然需要写成机读语言——尽管理论上，如果你写出足够详细的 prompt，也可以让 GPT 来生成。

这中间的区别也许没有那么重要，也许就是差一层窗户纸。但总之，描述的还不是已经实现的体验。

ChatGPT 的 plugin 系统的设计和之前类似系统比，真的新颖之处在哪里呢？前面说到「适当时候」，在接口中，你可以用自然语言告知 ChatGPT 你这个 API 能干啥，ChatGPT 用自然语言理解了这一点后，就可以自动根据用户的输入来判断什么时候应该找谁来满足用户的需求。你只需要告诉它一次「买机票去 KAYAK」，它就知道下次你问它 UA888 的时候可以去找 KAYAK。

这是不是就是我们中国人熟悉的……流量分发？大家都很熟悉，在 PC 时代我们抢注文件扩展名、Android 上我们抢注 Intent、iOS 上抢注 schema、搜索引擎上做竞价排名……干的是同一件事情。ChatGPT 想用自然语言来解决流量分发的问题。所以，套用一句话，这是流量分发机制的自然语言界面。

虽然看起来还是流量分发的逻辑，但过去大家熟悉的 SEO、growth hacking……其实用武之地并不多。

其实这也不是 ChatGPT 首创。Google Assistant 接入第三方服务的方式也是类似的，只是开发者体验要复杂一些。说时迟那时快，写这段的时候去查了 Google 的文档，发现这个服务即将在 6 月 13 日被 Google 亲手干掉。[4]

这也不是否定 plugins 的创新。事实上，大部分革命性的创新也就是在前人的基础上稍作改动而已。OpenAI 的研究和工程能力当然是让人惊叹的，但我越来越觉得他们的产品和市场能力也是让人惊叹的。

MIT Tech Review 关于 ChatGPT 开发过程的访谈非常值得一读 [5]，ChatGPT 本身也许可以称之为有史以来最成功的 hackathon 项目（虽然远比一般的 hackathon 要昂贵，但相比于 GPT 本身的投入相信只是个零头）。ChatGPT 把 GPT 重新包装成了人人都能看懂的能力，也许是其意外成功让 OpenAI 不甘于只做基础设施了，他们现在看起来决心直接面向消费者，不给中间商赚差价的机会了。**也许，OpenAI 就是第四次工业革命的 Google 或 Apple 了。**

Plugins 这个系统相信是在很短时间内拼凑出来的，却足够优雅、有想象力。Go-to market 的能力、连接用户需求和技术的能力、商业化的能力、设计生态系统的能力... 不就是古典产品经理的核心能力么？怪不得老王也要招产品经理 [6]。可惜，想来想去好像不认识什么活人有这个能力。

[1]:https://platform.openai.com/docs/plugins/introduction

[2]:https://en.wikipedia.org/wiki/Operating\_system

[3]:https://openai.com/blog/chatgpt-plugins

[4]:https://developers.google.com/assistant/conversational/overview

[5]:https://www.technologyreview.com/2023/03/03/1069311/inside-story-oral-history-how-chatgpt-built-openai/

[6]:https://m.okjike.com/originalPosts/641aa79e40db2e7567d6ed98

**木遥**

**一种自然语言编程的**

**可能性**

**微博博主**

你可能已经看到 ChatGPT 今天宣布推出插件功能的新闻了（这可能是近期一系列进展中最令人惊讶和震撼的一个）。插件让 GPT 可以实时和外界交互，可以阅读并回答各种真实信息，无论是股票价格还是调用计算器或者程序编译器还是私有数据库信息，也可以采取行动，比如直接从餐厅定位，或者下单购买商品。插件甚至可以控制第三方服务，让 GPT 成为一个和线下生活发生联系的全能数码助手（见附图）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5a22aSFn4SCCoE1dMWK2Q89zBdcCmicP4QVYhpmIlJ8hnzz27qlvhDAXtugMlXO8jnZHAa39XUzVew/640?wx_fmt=jpeg)

我之前写过，很多人抱怨的「ChatGPT 信息不够真实」听起来是个严重的缺陷，但其实并不是，因为大语言模型本质上是「作为一种服务的自然语言界面」，它和底层的数据来源是可以——也应该——解耦的。语言模型训练的时候从语料里学到的知识既过时又占地方，正确的做法是让语言模型只负责推理、表达、行动，至于数据和知识可以完全实时从外部获取。

但我说这些话的时候以为还要至少半年到一年才会看到这一天。我错了，今天就是这一天。

这就是说：

* 说小一点，这解决了很多人诟病的 GPT 对话数据不真实不可靠的问题。
* 说大一点，会有大量第三方插件和今天还无法想象的介入真实生活的新玩法被创造出来。
* 再说大一点，这意味着插件就是今天的 APP，GPT 就是今天的 iOS 操作系统，一个全新的生态。

但所有上面这一切甚至都不是我今天最受震动的地方。我最受震动的是下面这件事。因为推特上一个小哥总结的很好，我就直接用他的话（以及 OpenAI 联合创始人 Greg 后面评论的话）来说（见附图）：

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5a22aSFn4SCCoE1dMWK2Q89yk1dcNVX48fricwwzU5S0RCX6S6qBxdFnc8su7d9IKdg0DL99HibsdcA/640?wx_fmt=jpeg)

「OpenAI 设计的插件系统是我这辈子见过的最疯狂的系统。如果你要给它写插件，你并不是去写这个插件的程序，你是写一个关于插件的描述，用你的自然语言，然后 GPT 来帮你生成这个插件。」

十年前，当一个人跃跃欲试要给新发布的 iPhone 写 APP 的时候，ta 必须自己是个非常老练的程序员才行。今天，当你跃跃欲试要给新发布的 GPT 平台写插件，你只要用自然语言描述你希望实现的效果就行了。OpenAI 的网站上有一个视频展示了如何在几分钟之内完全用自然语言跟 GPT 交互写一个让 AI 帮你记住私人 todo list 的插件。换句话说，这就是（至少作为胶水语言层级的）自然语言编程。

\*头图来源：OpenAI

**极客一问**

**你如何看待 ChatGPT 的插件功能？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bPdgdT6Qb6pJYbnu97g0wsE0R4UIv0KqclWYv57MTxf0omPFRiabfWaRtxocOwpPFX0O2Z2TZtX3w/640?wx_fmt=png)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZqZmm22FSfM0Ifj1FIgBGBu29wQhoJaf0S8Bv9xu0yPJaRNbuUvWRznF7IlrAC0l0EnnmGXRIcLA/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2652986801&idx=1&sn=c51495d7037597f8033ffa019e0787f1&chksm=7e5420074923a9119f6d82af058a9294effea5e367905a8c454b1e107570924c800021b32f85&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZqZmm22FSfM0Ifj1FIgBGBopHUNCHpcgbvv8bIiaicHODPpRfsYfOtDy4L52ibacTVbp1IvXHlAJ2iaQ/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2652986540&idx=1&sn=75374f249242fabb8109cf3cad90a2ae&chksm=7e54211a4923a80c2c3696024a6bf1f2e84e3266d050b4d1ec1d8e28b86745edd3047fc810c6&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bwcRvGHYE6fIzpicR0bvcnRKBoS5yFSuKG2lafuIcNmRqoq...