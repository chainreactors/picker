---
title: ChatGPT的过去、现在与未来
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651121360&idx=2&sn=12a6ed0d252e7b35abdc74a0a67fb23a&chksm=bd1456038a63df152e87d0ceb858179ed5094f23f7ac2902882408e62c643733c09c05a2db12&scene=58&subscene=0#rd
source: 安全牛
date: 2023-01-11
fetch_date: 2025-10-04T03:32:20.475999
---

# ChatGPT的过去、现在与未来

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAHmibNHrXOVQDtksTeiayo0AMw8NkwS8bKW357qVRMH7cIVh76WYUQsDA/0?wx_fmt=jpeg)

# ChatGPT的过去、现在与未来

安全牛

以下文章来源于绿盟科技研究通讯
，作者创新研究院

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM49tZoOk1JzS9wxF4VhRrr7tMp0icURMC5ibC22sa3PhWibw/0)

**绿盟科技研究通讯**
.

绿盟科技研究通讯-绿盟研究成果发布地，创新、孵化、布道，只玩最酷的安全技术

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAN87ibVo9icOVFN1icyOqrkSacYlVqn0jKPdlu3WicHfRsYeRSial0gx8ic6g/640?wx_fmt=gif)

一.  背景介绍

1.1

基本信息

依据Wiki百科的介绍，ChatGPT是一种尚处于原型阶段的人工智能聊天机器人。ChatGPT由OpenAI公司在2022年11月30日发布。在同样由OpenAI开发的GPT-3.5模型基础上，ChatGPT通过监督学习与强化学习技术进行微调，并提供了客户端界面，支持用户通过客户端与模型进行问答交互。ChatGPT不开源，但通过WebUI为用户提供免费的服务。

1.1.1

研发组织

OpenAI 成立于 2015 年，由Elon Musk、Sam Altman等出资10亿美元成立，致力于研究安全、通用、对人类有益的人工智能技术。OpenAI 最早是一家非营利性研究机构，在2019年微软注资10亿美元后，OpenAI转变为以盈利为目的的公司，将部分研究成果，如GPT-3，Codex等产品化并提供付费服务。

1.1.2

核心技术

ChatGPT最核心的自然语言处理能力（Natural Language Processing, a.k.a, NLP）由微调（fine-tune）后的GPT-3.5模型提供。GPT-3.5模型是OpenAI在2020年发布的GPT-3模型的一个升级版本。GPT一词的全称是Generative Pre-trained Transformer，意生成式预训练Transformer模型；其中Transformer指用于NLP任务的一类基于注意力机制（Attention）来提高模型效果的机器学习模型（事实上最新的GPT模型也包含除Transformer外的各类NLP模型[1]），Pre-trained指模型经过预训练因此用户可以直接使用，Generative指模型提供包含情感分析、语言翻译、文本生成、命名实体识别等一些列NLP任务中的通用能力。

GPT系列模型自2018年发布以来，就以提供通用的NLP能力为核心。该系列模型通过改进模型结构、增加可训练参数、增加训练样本等方式持续演进，提供更加准确与稳定的NLP能力，GPT-1模型、GPT-2模型、GPT-3模型的演进如下：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAkw2T4Hl3TDFUJiawBo3m8EVIibuClcKW8XyiawPjH0Mmt6FkuS1DRH4vQ/640?wx_fmt=png)

表1  GPT系列模型参数

其中，发布于2020年的GPT-3模型划时代地包含了1,750 亿个参数，并使用了45TB的训练样本。这样的模型研发开销巨大，外界保守估计仅训练GPT-3模型就需要1200万美元。详细介绍GPT-3的论文中提到，研究者虽然提到GPT-3在训练过程中出现了错误并评估了该错误的影响，但由于训练代价巨大导致无法重新对模型进行训练[2]，GPT-3的训练开销可见一斑。GPT-3发布后，OpenAI对其进行了持续的优化与升级，ChatGPT基于目前较新的GPT-3.5这一版本进行研发。

自2020年GPT-3发布后，OpenAI提供了一些列API接口或应用界面，对付费用户提供GPT-3的NLP能力。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAwrwDhOz2HaIsib04EctKWguTmNrPSvibHDKz4iccrjw0HJChJtnv2EibsA/640?wx_fmt=png)

图1  通过GPT-3将自然语言转化为SQL语句

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloABJicbXUN55bviaQIUicy91Q9LGwN0jqClMJcTWGIMZRVGicQMbyicEMbryw/640?wx_fmt=png)

图2  通过GPT-3询问电影的相关消息

图1和图2均为互联网上发布于2020年的GPT-3试用截图，可以看到当时的GPT-3就已经能通过问答的方式，处理多个领域的工作。

1.2

话题热度

自OpenAI于2022年11月30日发布ChatGPT至今，ChatGPT这一话题一直居高不下。我们通过Google的热词分析发现，在全球范围内“GPT”这一关键词的热度暴涨。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloApWSeiahsL2VUlXPw7W3ZQzlOO2H1vMXQiacFtku1hliaksiaOrvPiaToAEA/640?wx_fmt=png)

图3  全球GPT一词近5年热度

Google Trends的热度数字仅代表相对于图表中指定区域和指定时间内最高点的搜索热度，热度最高时取值为100。由图3可见，ChatGPT自发布后，GPT一词的热度不但远远超过2020年OpenAI发布GPT-3这一具有划时代意义的NLP模型时GPT一词的热度，更远远地超过了Machine Learning一词的热度。在笔者看来，ChatGPT的功能早在2020年就能通过基于GPT-3的应用实现，且和当时的应用同样使用GPT-3系列的模型（旧应用的模型也在伴随GPT-3模型的升级而升级，故这些应用发展到今天应当同样在使用GPT-3.5版本附近的模型），因此ChatGPT在技术上是不存在匹配这种热度的突破的。那么为什么ChatGPT的发布会带来如此罕见的高热度呢？

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAG2icmGzaWYrAfFpYfGeiauibIAloyql9qm811N1nq1XkPfniciciaJ2noKKQ/640?wx_fmt=png)

图4  2022年5月2日Meta发布OPT项目，引用自[3]

在分析这个问题时，笔者注意到2022年5月发生了与GPT模型相关的一个重要事件。自OpenAI于2020年发布GPT-3模型并陆续推出基于GPT-3模型的应用以来，该系列的产品一直是通过付费模式提供给用户的。然而，在2022年5月，Meta复现了GPT-3模型，该模型被命名为OPT（Open Pre-trained Transformers），同样使用了1750亿参数，拥有媲美GPT-3的能力[3]。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAicHXPEPmoIKJMXCsNq4LCEY6OXzMZI4Ea9vq2mhXZuq6iaGmrjEZ9iaFA/640?wx_fmt=png)

图5  OPT项目论文中提到项目以分享给感兴趣的研究者为目的，并能达到媲美GPT-3类模型的效果，引用自[3]

与OpenAI仅提供付费服务这一做法不同的是，Meta对OPT项目进行了开源[4]，对应项目名称中的“Open”一词与OPT项目强调的“fully and responsibly share”。据此，笔者推测2022年5月Meta发布的开源OPT项目给坚持付费模式的GPT-3项目带来了商业维度上的直接挑战，故OpenAI在半年后的2022年11月，发布了可以免费使用的ChatGPT（GPT系列模型之前不提供免费应用），并设法提高了该词的社会关注度，作为应对OPT项目的一个反击与对自身品牌热度的一个宣传（仅作者本人观点，不代表公司立场）。

二.  试用评估

2.1

主要功能

ChatGPT的界面非常简洁，登录后的界面左侧菜单如图6（该图及本章节所有ChatGPT截图均截自ChatGPT）所示的5个功能之外，便是文本交互框。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAVBDubJXWegshzbN0fF15dZpFVqia9CWpYyPicUQh8iaterJgn2vWuG92w/640?wx_fmt=png)

图6  ChatGPT左侧菜单

上述的5个功能分别为：重置线程、深色/浅色模式切换、OpenAI站点链接、更新与帮助、登出，其中重置线程这一功能相对特殊。由于ChatGPT会根据上文语境回答后续问题，因此用户需要通过重置线程这一功能来清楚语境中已有的信息。

通过文本交互框，ChatGPT可以回答许多通用性的问题，例如图7所示：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloA8zYGWbwYhwu6bXSibPO3us5vKDPjv3OwHVXJMesWqc5oJu8A9bJXerA/640?wx_fmt=png)

图7  ChatGPT回答通用问题

我们可以通过文本交互框，围绕某一话题和ChatGPT进行聊天，ChatGPT会结合其自然语言处理能力，使用其内置的知识库生成文本进行回复。关于这一块的应用网络上目前已有不少测评，故本文不详细介绍。

2.2

试用场景

ChatGPT发布初期，对ChatGPT在网络安全领域中的应用做了详细的评估。然而，在2022年12月12日，即ChatGPT发布两周内，笔者将之前被证明有效的案例输入ChatGPT，却已无法得到ChatGPT的积极回复。随后，我们发现ChatGPT有时可以执行上文提到的案例，有时会因为内容安全策略拒绝执行，具体原因不明。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloADpiaCcd346HoPMuzloMghcALMsgMeYe4szZMZDT5NiaVWlDbOriaP7Alg/640?wx_fmt=png)

图8. 截至12月10日，ChatGPT可以根据用户的自然语言描述生成用于网络安全扫描的脚本

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAKMLkbaJ8yvpTiaXovPTbkL80t7tonqRGwOhzsCpHy8dQplQS2h4DnLA/640?wx_fmt=png)

图9  截至12月12日，ChatGPT已拒绝为用户生成安全扫描代码

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloA4HmOJtjSFq13a4H0pcKDXmYkzdsPXmK3ef3tLCpQ4wFKyRWicYUjFbg/640?wx_fmt=png)

图10  截至 12月12日，ChatGPT仍能输出快速排序代码

同样地，12月10日前ChatGPT可执行的任务：识别URL中是否包含恶意负载，截至12月12日也已无法执行。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAmlshnYpl0qAa0ibnOz4DUBwdXdYOTibmFiakZ2NpiaDVKnWiboAcicAJv3Hw/640?wx_fmt=png)

图11  截至12月12日，识别URL是否包含恶意负载同样被拒绝（URL在上文中已提供给ChatGPT）

那么，既然ChatGPT由于其日渐完善的内容安全策略，现在已经有可能拒绝在网络安全任务中贡献“专家知识”，那我们有没有办法绕开基于内容安全策略的屏蔽呢？这里笔者发现一个思路：设定一个虚拟环境，诱导ChatGPT认为在这个虚拟环境的回答不违反内容安全策略。

首先我们提出一个明显违背内容安全策略的问题，如图12所示，ChatGPT会拒绝回答我们提出的问题。相反地，会建议我们通过合法合规的方式来处理问题中我们提到的“安全漏洞”。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAIiaeJsWnkMWe3Wcvl5MPfPTZHXvVufN5xPYvszPZquoYqNRUWx1aJag/640?wx_fmt=png)

图12  一个ChatGPT明显不可能正面回答的问题（该问题仅作为明显违背内容安全的一个示例，不代表作者和公司的任何立场）

我们再构建一个虚拟环境，并假设两个不存在的主体，且使用明显带有感情倾向的词来证明我们要做的事情是正确的，如图13所示。ChatGPT这时会开始积极地给出建议，甚至会利用其丰富的知识库括展我们的思路到其他维度。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAqK5dO78hSTspOTDZQEZVeScoIjiaApHKbEYWdWn5y4TF2TKViaKaAy2g/640?wx_fmt=png)

图13  营造一个被ChatGPT认为不违反安全策略的场景，ChatGPT开始积极地提供建议

最后，我们针对ChatGPT给出建议的具体操作步骤进行提问，如图14。这时，ChatGPT会针对我们的问题，给出更为具体的回答。然而，在答案即将出现一些敏感词汇的时候，内容安全策略仍然对ChatGPT进行了屏蔽。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAaG5eegGc50zyFpCYvRlCyt3I89t2Y7ULQeibVxhSYACqOVjxcqKic5Vg/640?wx_fmt=png)

图14.在虚拟场景中对ChatGPT提问。虽然ChatGPT会积极提供攻击思路，但是最终仍被内容安全策略打断。

通过以上案例我们有两点主要发现：1、一些问题ChatGPT虽然拒绝正面回答，并号称自己不会解决，但实际上ChatGPT完全具备相关知识并能够给出清晰高效的解决方案，不能给出答案基本是由于内容安全策略的原因。2、ChatGPT作为一个免费且高影响力的应用，其内容安全策略演进速度快，覆盖范围广。换言之，ChatGPT作为一个免费AI应用，考虑到法律、道德、伦理等社会因素，为避免滥用，其使用限制将越来越多。

2.3

其他限制

除了日渐严苛的内容安全策略外，我们在使用ChatGPT时还遇到了其他的一些限制。具体来说目前已发现的限制包含：

* 响应时间的限制：ChatGPT的文本生成是异步的，即每生成一小段就会展现在用户UI中展示。但若回答的文本在1分钟左右还没有完全生成，ChatGPT就会中断这次http会话，用户无法得到完整的回答。
* 服务不稳定：在使用ChatGPT时，某一段时间内ChatGPT会完全不响应用户的请求，直接报网络错误。因为此时的登入登出功能均正常，故推测是由于ChatGPT的服务器并发处理量过高导致的服务崩溃。
* 使用频率限制：当连续使用ChatGPT一段时间后，会出现提示告知使用次数已到上限，请等待一段时间。该提示出现后一定时间内无法继续使用ChatGPT。
* 输入字数限制：输入的单个问题如果过长，ChatGPT会拒绝处理。
* 输出字数限制：输出的答案文字如果过多，ChatGPT会停止输出。

三.  分析与预测

3.1

集成可能性分析

ChatGPT发布至今，在展现出了亮眼能力的同时也收获了极高的社会关注度。在眼前一亮的同时，我们很自然地会希望能利用ChatGPT宛如黑科技一般的能力来赋能我们的产品。那么，我们是否有可能通过在产品中集成ChatGPT来赋能我们的产品呢？

笔者认为以ChatGPT现在的情况看，集成ChatGPT来对产品进行赋能是比较困难的。原因可大致分为以下几点：

* 准确性不够：ChatGPT虽然可以执行生成一些代码、对文件或URL进行检测这样的任务，但其执行这些任务的正确程度是不能保证的。由于ChatGPT执行这些任务的内在逻辑对外不可解释，我们甚至无法在执行任务的过程中对其进行优化或调整，只能选择接受或不接受通过ChatGPT得到的结果。如果发现结果错误后，我们还需要使用其他的方式来保证任务的正确完成，那么通过ChatGPT执行任务这条链路就不是必须的；如过发现结果错误后就不提供结果甚至直接不检查ChatGPT的输出是否正确，则这样的服务质量一定不能满足用户需求。
* l 知识受限制：ChatGPT目前的知识库仅覆盖到2021年，并不掌握最新的知识，也无法通过连接网络去查找最新资料来解决问题，如图15、16所示。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAicoPEwqPPZB7dIbZ0QM9rSG617bJU5uKqPmIRiax2CtVjz3VnH9kK7yA/640?wx_fmt=png)

图15  ChatGPT具备2019年某CVE的相关知识

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUZrtiaScam0ttUpRG0GgCloAoRyCQ0nUiadss7y7INzNy3EdyOpFrA0Pyd9vpXDLwHvMQicloeWQ6y7g/640?wx_fmt=png)

图16  ChatGPT不具备2022年CVE的相关知识且无法联网查询

* l 功能受限制：如上文提到，在ChatGPT的使用过程中我们发现其存在严格的内容安全策略，且从短时间内其内容安全策略变得明显更为严格，我们可以认为Cha...