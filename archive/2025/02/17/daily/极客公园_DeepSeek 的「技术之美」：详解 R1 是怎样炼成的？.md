---
title: DeepSeek 的「技术之美」：详解 R1 是怎样炼成的？
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653073814&idx=1&sn=af59676d398794d2c0bae42aa2c44cc7&chksm=7e57cc2049204536673a70b6bd8996ed91e12c27ba6b68594d4feb72aebbb4726daed8b70759&scene=58&subscene=0#rd
source: 极客公园
date: 2025-02-17
fetch_date: 2025-10-06T20:35:03.244164
---

# DeepSeek 的「技术之美」：详解 R1 是怎样炼成的？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZEVtzI0g1e6yH8DzPoL0tFslzqUFicGFrRVJsQRVbSPwK1GbxtaHx16V5DSNKFz2eRAV5om4wIMdQ/0?wx_fmt=jpeg)

# DeepSeek 的「技术之美」：详解 R1 是怎样炼成的？

极客公园

以下文章来源于真格基金
，作者与你同在的

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM44mFsxaDUbWm6ibN44KEaNHYj142icTRrypibrayD1jDJ6A/0)

**真格基金**
.

专注早期投资，欢迎投递商业计划书至 dream@zhenfund.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZEVtzI0g1e6yH8DzPoL0tFKFwvsQ9ia4Ls8g6U4StdNenppOQNn0zMHNBETiaNEPLXvf77tvfXXcNg/640?wx_fmt=jpeg)

今天 AI 的渗透率只有 5%。剩下 95% 的人，他们的第一款 AI 应用会是什么？

来源：真格基金(ID:zhenfund)

原标题：万字赏析 DeepSeek 创造之美：DeepSeek R1 是怎样炼成的？

原文链接：https://mp.weixin.qq.com/s/HB38prEMz275Rkj1g7mavA

大家好，我是 Monica.im 的产品合伙人张涛。

相信大家和我一样，整个春节期间几乎都在抱着手机刷信息。白天看国内的反应，晚上看美国的反应。整个春节就这样度过了。春节后这一周，大家已经在各种微信公众号和其他平台上刷了大量关于 R1 的分析文章，从技术到产品、再到长远影响的探讨，很多群也在转发聊天记录，有关于 R1 的十几篇必读文章。

我和雨森（真格基金管理合伙人）商量说来做这个分享时，就明白很多信息可能会过时。既然我们这么多人在这里，如果仍然讲一些比较常见或者宏观的信息，是浪费大家的时间。

这一周我在准备过程中，一方面让我司首席科学家 Peak 帮我审查了很多技术和算法方面的细节。另一方面，在整合各方信息时，我发现了一个特别有趣的叙事角度。

今天的分享，既是为了让大家更好地理解 R1 背后的脉络，也是希望大家看到这次精彩冒险背后一个美妙的故事。

好了，今天的分享正式开始。

***01***

****最好的致敬是学习****

今年春节，我在上海过年，没有回重庆，就通过视频给爸妈拜年。我给我妈说新年快乐时，听到我爸在旁边喊道：「你快问一下张涛，那个梁文锋是不是真的那么牛逼啊？」

今年的 DeepSeek 和 R1 话题真的是破圈的程度非常高，甚至像重庆这样的二线城市的老头老太太们都在关注这些话题，且真心关心它背后的原理到底是什么。

首先我们回顾一下这些发生的事情，理清时间线，确保大家对这个事情有共同的认知。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0t4xCnqs6msYo7LserNIlebr20zmuc6X59q42BrjmHL23cBFVdCzHxhw/640?wx_fmt=png&from=appmsg)

去年 11 月 20 日，DeepSeek 在官方 Twitter 上发布了 R1 Lite Preview。当时发布的 R1 Lite Preview，实话说，离现在的影响力连 1% 都谈不上，可能只有万分之一。只有去年 11 月 o1 发布后，有一些人试图复现 o1，这时他们可能对这个 R1 Lite Preview 感兴趣，甚至有人基于它进行一些蒸馏和 SFT 的工作。但这些工作在学术界内部并未出圈。

接着到 12 月 26 日，发布了 DeepSeek V3。相比 R1 Lite Preview，它的影响力就更大了一些。稍后我会举一个例子证明，至少在学术界，它是有出圈的。

第三个时间点是 1 月 15 日，DeepSeek 发布了他们的 APP。当时如果大家仔细看，会发现 15 号发布的 APP 中，已经有了 DeepThink 模式。

但是 DeepThink 这个模式一直无人在意，国内没有，国外也没有。如果大家能回到 15 号的语境下，其实可以理解为什么。当时不仅是美国，包括我们在内，大家关注的新闻基本只有一个——特朗普即将登基。公众的注意力还更多集中在这些政治事件上。直到 20 号，R1 才正式发布，一方面是相关论文公开，另一方面是模型权重的开源。

从时间线来看，R1 最早的苗头实际上在去年 11 月份就已经出现，并非一夜之间爆发的。在这个过程中，还有几个关键节点需要关注，包括 V3 的重要性——这是我们今天讨论的核心话题之一。

接下来，我给大家看一个有趣的现象。在 Google 上搜索 DeepSeek 这个关键词，可以看到其关注度的起点是在 1 月 20 号，也就是 R1 发布之后。随着学术界开始小范围讨论，20 号到 24 号、27 号之间热度逐渐升温，直到 27 号，英伟达及一众美国 AI 概念股「砸出巨坑」，DeepSeek 的搜索量也随之达到顶峰。即使热度在一周后有所回落，相比 20 号之前接近 0% 的状态，现在仍然维持在 20% 左右。这说明，尽管流量有所回调，但关注度并未完全消退。

接下来是一个有趣的话题，不知道大家能不能猜到：**在美国，按行政区域划分，哪个地区对 DeepSeek 关注度最高？**

我当时在看数据时觉得非常有意思。本以为会是加州，毕竟 AI 相关研究人员主要集中在那里，但实际上，最高关注度出现在华盛顿特区。可以想象，在 27 号市场震荡后，华盛顿的一众政客疯狂在 Google 上搜索 DeepSeek 试图搞清楚 DeepSeek 到底是个啥？

之后的排名则较为正常：加州、华盛顿州这些传统 IT 公司和 AI 研究机构集中的地区关注度较高。但 DeepSeek 这么高的关注度确实值得一提。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0tge3Kpvt9leecMS6eD99I5YGIXtdSemclXVSYO58LibYIOWvg5AQdTvA/640?wx_fmt=png)

前面我们讨论的是发布方的反应，现在来看美国社会中精英 KOL 们的反馈。大家可能还记得，我之前提到，12 月 26 号 V3 发布时，**相比 R1 Lite Preview，这次在学术圈真正「破圈」了。**

为什么这么说？可以看这张图，右侧是 Andrej Karpathy 的 Twitter。当天，他发布了一条非常长的推文，详细介绍了 V3，并评价其为「very nice and detailed tech report（非常出色且详细的技术报告）」。可以确定的是，12 月 26 号 V3 发布时，它已获得美国主流学术圈的认可，只是当时很多人尚未意识到 V3 的更深层次价值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0t7aG5n8xIp0dck3S0HYDSxKl2iaHwfG0QLLMzGvtukMwk4iaS6G4xEpOw/640?wx_fmt=png)

我们再回到春节期间的「炸街」时刻。

第一次让我意识到美国舆论开始转变的节点是什么？当时，我们都在各种群聊里，应该有不少人看到了。那天，我特别兴奋地转发了 Marc Andreessen 的 Twitter。大家知道，他通常对中国科技持激进甚至有时候是轻蔑态度。

24 号时，他开始连发推文，惊叹这是什么东西？太炸裂了吧。之前他会批注比如，这太厉害了，但请注意，我说它好，不代表我很高兴，我是觉得它很危险。但仅仅一天后，他的语气彻底改变了。这条推文没有任何负面情绪，而是完全正面的表达。

到了 28 号，Sam Altman 也不得不出面表态，尽管说得别别扭扭的，比如暗示 「其实我是想开源的，但组织上不允许」之类的托词。杨立昆也承认 R1 的影响力和研究质量，不过试图将话题引向「开源」的胜利，而非某个国家的胜利。

无论如何，这项工作已经得到了美国 AI 界顶级领袖的认可。无论是对质量还是对这一事件本身的认可，其影响力已经显而易见。至于这个影响是好是坏，原因是什么，这是我们接下来要探讨的话题。

到了 2 月 2 日或 3 日，仍然有一些持反对意见的人在称这项工作是 DeepSeek 雇佣水军炒作。实际上，主流圈子对此并未关注。但事实就摆在眼前，无需辩证。

最值得注意的是 1 月 27 日这一天，股市剧烈波动。左边，从上到下依次是英伟达、台积电、美光，股价瞬间砸一个天坑。右边，从上到下是中芯国际、360 和金山云，股价却突然上涨，仿佛呈现出一种「东升西落」的趋势。**这说明 R1 的出现对真实世界的影响同样不容忽视。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0t7HVotIRgunSjlh9oGVJiajDnBtjBlicSkxxQJRjPeicaLbqWqraicLRB5Q/640?wx_fmt=png)

在 Sensor Tower 的数据中，左图显示的是 DAU ，其中紫色线代表 ChatGPT。而在底部，原本较小的其他竞品，如 Claude 和 Perplexity，虽然一直是 ChatGPT 的跟随者，其用户占比相对恒定且较低。但在 1 月底的几天里，DeepSeek 出现了显著增长，占比大约达到 20%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0txr1aM60byPwBSYBgQLhJmNll2XSpVYuM9CSMF6aZugDLVlVGTU83hQ/640?wx_fmt=png)

左图显示的是 DAU，右图是新增下载量

右侧的图展示了新增下载量，在突破某个临界点后继续增长。我截图的时候比较早，昨天查看最新的数据，发现左图趋势持续向上，虽然右图的下载量有所回落，但仍然高于 ChatGPT。目前来看，这一趋势仍在持续。

不管是业界领袖的认可，股票市场的反应，还是真实用户的选择，都证明了这一事件的影响是真实存在的，并且具有用户价值。这是过去半个月里发生的重要变化。

接下来，我们回到为什么要组织这次学习分享。这件事对我而言非常重要。我从 1 月 23 日开始关注，并频繁阅读中美两地的各种言论，包括圈内和圈外的讨论。随着这个事件的破圈，越来越多非专业人士开始关注，人们对其归因的方式也变得过于简单。

比如，有人认为这是因为中国人工便宜，从而把美国顶尖科技的成本打下来了。也有人说这是抄袭，只要复制就能成功。此外，还有另一种叙事，即某个不知名的小团队突然创造了全球顶级的科技创新。然而，无论哪种归因，都显得过于表面，脱离了产品，缺乏对技术本身的深入理解。

**这个事件简单归因是傲慢的，最好的享用方式是学习它。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0tBEucGJsh1vCTAPGf46wibTaPrjsHlB9H7oDvAm0TdMBbH0K2um55IEw/640?wx_fmt=png&from=appmsg)

当面对一个如此重大的事件时，仅仅存入记忆是不够的。去学习它、理解它，搞清楚为什么会发生这样大的影响力才是本次分享的核心目的。

***02***

**什么是推理模型？**

对于大部分听众来说，我们不是专业研究算法或工程的，我自己是做产品的。我们首先需要解决的一个基本问题是：什么是推理模型？

**我们已经有大语言模型了，为什么还需要推理模型？**

我这里准备了一个小测试，不知道大家是否了解，人脑有一个特殊的能力叫「数量识别」。这不是简单的数字识别，而是对数量的直觉判断。比如，我会切换一张图片，你需要在一秒内告诉我上面有多少颗黄球。一般来说，一个正常人只能识别 6 及 6 个以内的个数。好，现在准备——3、2、1，切换！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0tEgw6ymficZUqhY6ZoOJC7QEVnlz0CyyVXFomGwL74r235CZ9tr3kN8A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0tmRtWKArJkbhVjWDLNsVMBwNws7UHhsrLbiaOEuwWuicbBAicNqf5xYFfA/640?wx_fmt=png)

「数量识别」测试

通过这个实验，我们可以发现，在几千年的进化后，人类在数数时并不一定需要一个个地数，而是在一定范围内可以凭直觉判断。这一现象背后的认知机制，也是推理模型的一个重要基础。

语言模型，特别是大语言模型，有一个特性相似的特点：模型在给出答案时，一般会直接做出回答，尽管这种方式往往容易出错。举个经典例子，比如 CoT（Chain-of-Thought，思维链），Jason Wei 强调了一个重要的思想：**模型需要更多的 token 来进行思考。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0tPibLocJtPibH3ZzILbCJZbgqXaUCtsyddOGumibZjtlRfichcAcoPrK4QQ/640?wx_fmt=png&from=appmsg)

Peak 曾经给我说过一个直击本质的观点。大家知道，语言模型的本质是激活一个庞大的神经网络矩阵。当输入一个 token 时，它能够激活矩阵中的某些部分，但这种激活是有限的。当输入更多的 token 时，能够激活的部分也更多，信息量随之增加。因此，更多的 token 意味着模型能够得到足够信息，从而做出更为精准的决策。

模型需要更多 token 来「思考」，这也促使我们提出了推理模型（Reasoning Model）的概念。

什么是推理模型？比如，我们可以用一个例子来说明。假设我们问一个问题：「从望京西到西直门坐地铁需要几站？」一个「直接回答型」的模型可能会像下图左边直接回答：「九站」。

而推理模型则会做出右边的回答。它首先会考虑多种换乘路线，接着比较各路线的换乘站数，最后综合得出最佳方案。**推理模型不仅仅给出答案，它还会展示其思维过程。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0t9ZGtmF6lj4SrvwtnibGYWdupCOY6orYnXgvHHBBM2XcqrOQzIL8psUA/640?wx_fmt=png&from=appmsg)

大家可能会觉得，这和 CoT 有相似之处。那么，推理模型和 CoT 有什么区别呢？如果你已经习惯了使用 ChatGPT，你可能会直觉地认为，推理模型不就是 CoT 吗？我直接写个 CoT，让它一步步进行推理就行了。比如，针对刚才的地铁问题，我们可以跟模型讲：请先列出所有可能的换乘路线，再计算每条路线的换乘站数，最后综合得出最优答案。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3EbGouibNp0EETqgm53eTZhyVnac6vo0twJluTVGpbnACYWiarRy5HaTZO3SJibmf7tL5CbzBF6jWMqy3zKXhjaDg/640?wx_fmt=jpeg)

如果你愿意为每个问题都写出如此详细的 CoT，这也是可行的。

但这里有个问题。我们来看一下去年震惊整个业界的事件——当时 ChatGPT 的 o1 系列模型发布，它刷新了多个记录。比如在数学领域，它的得分从 13 分直接跃升至 56 分和 83 分；在写代码方面，它从 11 分飙升至 89 分，快把榜单刷爆了。PhD 级别的科学问题虽然提升没有那么显著，但也极为恐怖。如果你经常看论文，就会明白把基准测试刷新一两分都能发表论文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0tbgfRLczicJrXWmu663XpjzrfcruNQzOyTqxHKYoqOxHqeJ4e44Iavqg/640?wx_fmt=png)

其中，最让人惊讶的是 PhD 级别的成绩，尤其是右边绿色，代表的是人类专家的得分。ChatGPT 已经超过了真正的 PhD。

推理模型的本质是让模型自己构建 CoT，并将前面推理的步骤展示出来。虽然你也可以自己手动编写 CoT，**但问题是：我们能否对每一个问题都写出完整的 CoT 呢？**

比如，下面这两个问题，分别出现在 2024 年 AI 的基准测试和 PhD 级别的评测中。假如你还是一个数学或物理 PhD，或许能写出 CoT，但对于绝大多数人来说，能够把每个问题的思维过程一步步写出来并不容易。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0tT32TYPPNz8kbeyW00TQs2OQl7TOVl80GLyLmFFENQnrLLZibhOvG7WA/640?wx_fmt=png)

左边是 AIME 2024 的测试题

右边为 PhD 水平 GPQA Diamond 的测试题

这就是推理模型的必要性。它能帮助我们处理一些特定领域的问题。举个例子，推理模型非常适合解答谜题，比如翻译二战时期的密码电文，或者进行数学证明，解决复杂的决策问题，甚至是开放式问题。推理模型不仅给出最终答案，还会展示思考过程。

而对于一些简单的知识性问题，比如「哪个是中国的首都？」，我们显然不需要使用推理模型，直接给出「北京」就可以。很贵，而且想得多容易搞错。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3EbGouibNp0EETqgm53eTZhyVnac6vo0tDycuVu5LuLd5ibJCA79qSCOKG32Du8B7hQTuheg9xp6YpKKibDrqoWqw/640?wx_fmt=png&from=appmsg)

推理模型有其适用场景。为什么它在我们行业中如此重要呢？原因有两点。

首先，大家看到的在数学、写...