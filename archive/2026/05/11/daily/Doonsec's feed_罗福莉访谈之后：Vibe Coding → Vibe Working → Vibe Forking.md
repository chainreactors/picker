---
title: 罗福莉访谈之后：Vibe Coding → Vibe Working → Vibe Forking
url: https://mp.weixin.qq.com/s/D4bAcI3TN4b_cEhk-aftNQ
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:35:48.834030
---

# 罗福莉访谈之后：Vibe Coding → Vibe Working → Vibe Forking

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xTZfvDhkzLuhonbB03ayywfLAOvWRSGRj15icly6U87qnaKWXoraOBTGibfT3pnBUkEfdeZ7I7KIddwcV8zQiaEvqQfT970RxYaureQ3aicUuQY/0?wx_fmt=jpeg)

# 罗福莉访谈之后：Vibe Coding → Vibe Working → Vibe Forking

原创

heige
heige

黑哥虾撩

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xTZfvDhkzLuAA4yroUEqERwrAdZkVXaia6lfjPaicwmfwdz6jMDZvTOXQEhD3v4YonOcicYN9EnQPABuhkgia9YycChqX9TFG6mSd1W9a46jYqw/640?wx_fmt=png&from=appmsg)

图片有aipy +Image2绘图大师智能体生成

这篇文章按道理早应该写了，只是最近一直沉迷于Vibe Working，所以就一拖再拖，AI时代如果实现了大模型自由（不仅仅是Tokens自由）你会发现可能会进入一个全新的“ah moment” 而我觉得这段时间正好处于我感受到的又一个“ah moment”，前一个感受当然就是AiPy最新出来的时候 ...

2周前，曾经的“天才少女”罗福莉最新的采访视频发布：

> https://www.youtube.com/watch?v=V9eI-t3TApE
>
> https://www.bilibili.com/video/BV1iVoVBgERD/

这个采访视频时长有3.5个小时，发布之后还是引起不少的关注，不过可能很多人都没有完整看完视频，没有看的可以看看，也看去看看对应文字记录梳理版 如：

[https://mp.weixin.qq.com/s/ePslW5QYP6rvx\_C3qF0IEQ](https://mp.weixin.qq.com/s?__biz=MzkyMTYwNjgwNA==&mid=2247495384&idx=1&sn=9538593cc2328802de2fcb60925826d8&scene=21#wechat_redirect)

引起关注的主要是前半部分，罗福莉聊OpenClaw的那段：大体上是说她一开始是“排斥”的，然后在春节放假期间，奔着闲着的时候带着“为什么OpenClaw那么火的”的疑问，真正体验了下，然后感受到“兴奋”，“在产品设计上超过想象”，到真正感受到为自己“干活”而兴奋，最终也引起了她对新模型训练等上的一些思考 ...

泛化

说实话，如果你看过我之前的文章，我“碰瓷”过卡帕西（Andrej Karpathy），也“碰瓷”过尧舜禹（姚顺雨）的一些采访和观点，相比之前这些我对罗福莉的这些观点没有特别大的那种所谓“共鸣”，因为我感觉她这些感受，在我的体验上看，早在1年+之前 我们AiPy诞生的时刻，就已经感受过了，所以到后面Claude Code 到 Openclaw 再到 Hermes 其实没太大的“啊哈 moment”的感受，我想很多早期一开始体验过AiPy的可能都有我这个感受 ... 当然比较可惜的我们覆盖度不够大

在罗福莉的采访里提到了她对Claude Code到Openclaw的时候，提到了她在OpenClaw上有很多感受是在Claude Code使用上没有体验到的，当然她也说了很多能力实现其实Claude Code就是具备的，比如 记忆 、不用考虑模型适配等等，而这些其实就是我当时我们总工LGX第一次发给我AiPy（参考《[【Agents/MCP可能不存在了】No Agents, Just Python-use！](https://mp.weixin.qq.com/s?__biz=Mzg5OTU1NTEwMg==&mid=2247484350&idx=1&sn=597466021965564fe0b88789ec36e7f2&scene=21#wechat_redirect)》）的时候体验是“一模一样的”，而当时最开始LGX在公司群里第一次介绍aipy的时候的疑问这个跟Cursor有什么区别，有Cursor也一样能干活，而真正用上AiPy的时候才能真正感觉还是不一样， 还有一点就是罗福莉访谈里也提到了Code泛化的问题，她在使用Claude Code虽然觉得 Claude Code也除了IDE外也确实可以依赖Code泛化能力去进行Work，但是这OpenClaw让他感受了更强大的听过Code实现了Work的泛化，这个也是是她觉得Openclaw这种Agent框架带来的优势。

而在我看来这个其实就是Vibe Coding 与 Vibe Working 这两个概念的区别，当时卡帕西的Vibe Coding火了后，很多人@我说，AiPy不就是吗？其实那个时候我觉得不完全是，一直到跟我们CEO IC聊的是时候，提到Vibe Work这个词 才有恍然一亮的感觉（参考《[从 Vibe Coding 到 Vibe Working](https://mp.weixin.qq.com/s?__biz=Mzg5OTU1NTEwMg==&mid=2247484413&idx=1&sn=583de95c7b2f0cb6daff2c4dbf08b674&scene=21#wechat_redirect)》）

罗福莉 在采访里还有提到的一个点，就是Agent框架能弥补模型本身缺失的能力，其实这个问题我之前在

> 我其实在这里“钻个牛角尖”，跟他原本的想表达的观点可能没啥太大的关系，比如 9.8 vs 9.11谁大的问题 或者草莓那个单词有几个r的问题，如果这个用纯模型去训练解决，感觉也让很多的模型基础研究头疼的问题，要不然GPT好几个模型都没有很好解决，反过来如果用Agent的方式，我直接用代码一下就算出来了， 哪个数字大、统计草莓里多个r，非常简单而且正确
>
> https://weibo.com/2783938821/QmOtFrrrT

里就用了 “9.8 vs 9.11 谁大”、“草莓单词有几个r”的例子就感受到了Agent其实是非常好去解决这种问题，而解决方法就是通过Code泛化去解决，直接计算一下上面的答案就非常准确，而从模型角度去真正“解决”估计会非常麻烦，毕竟GPT本身原理是预测概率。而这些其实都是非常时候Agent的场景，这里也可以顺带例举前面我在朋友圈分享的一个例子

![](https://mmbiz.qpic.cn/mmbiz_png/xTZfvDhkzLsqSc2G2tzQ4zINlVaHzAib8NSnssGYtplGJfl5aAkdjxU68pDo9EDYejqK4cT4iaiaCFnANZFW0zOBHhVTuqZH8ib6q4KYKZJBWCs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xTZfvDhkzLsUIPP0MN8ZO0ibC9xAhC2raaPibGXibAOxPkxLpkY9f8z9xCLKvbWhn9EdIYgHib2z5qygj6sb2r6Gnic6JzCAqQMtl9GhOo5icwx4Y/640?wx_fmt=png&from=appmsg)

这个是2024年的一个ppt，当时还是比较流行RAG，实际上我当时就用Agent的方式去替代RAG，因为相比RAG的通过向量化的成功率远不如一个Agent调用一个API出来的数据高效并准确可靠，当然那个时候这种方式比较适合能结构化数据，不过到现在非结构的话的基本上也开始使用Agent的模式了 比如前面很火的karpathy是那个wiki

> https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

还有这几天比较火的

> https://github.com/VectifyAI/PageIndex

 这个我也Vibe到我本地AiPy分支里 效果还是非常不错的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xTZfvDhkzLtPLoGOHSP6xCiarAicWGicVdFHzGCtrlwu8HElPzDuoU2ITfLrKLyG4XYiazm0QkxotlxVqDZGN4KgCQE9htLnmocPJjyfrKJEtIc/640?wx_fmt=png&from=appmsg)

我们回到罗福莉的采访，可能也是上面提到的她在采访里提到的“Agent框架能弥补模型本身缺失的能力”这个观点，导致很多在我看来很片面的解读，比如《罗福莉：AI 的范式变了，框架比模型更重要》

> https://x.com/Bill\_Do\_A\_Bit/status/2048382197363814573

实际上她在采访里出来就没说过这个结论，她实际在意的是Chat时代到Agent的时代的转变，也就是说“训Chat”模型转为模型怎么“训Agent”，而这点就是我在《[AI Agent 下半场](https://mp.weixin.qq.com/s?__biz=Mzg5OTU1NTEwMg==&mid=2247484484&idx=1&sn=f2074c8b6895179bbcc21bb5db71b712&scene=21#wechat_redirect)》文章里提到的观点。

所以在我看来，罗福莉访谈真正有价值的地方，不是证明 OpenClaw 多么神，也不是证明框架压过模型，而是让更多人意识到：AI 正在从 Chat 时代进入 Agent 时代。模型能力开始进入真实环境，开始和代码、工具、记忆、Skills、Workflow、后训练、权限系统、环境反馈融合成一个新的执行系统。

这个系统，我更愿意称之为 Agent Runtime。也可以用我之前反复说的那句话来概括：《[2026 AI Agent 的核心：Context Engineering，让环境可计算化](https://mp.weixin.qq.com/s?__biz=Mzg5OTU1NTEwMg==&mid=2247484466&idx=1&sn=e65765298da167e80bb0cf7f63cf34ce&scene=21#wechat_redirect)》。

蒸馏

这里先说明一下，我说的“蒸馏”，不是传统机器学习里模型训练阶段的 Knowledge Distillation，也不是前面比较流行的类似于女娲skill/同事skill这种“蒸馏”（当然AiPy上还有一个蒸馏出黑哥的Skill）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xTZfvDhkzLvHdL9vTssT2DrAnkZScBrCVEFzDwZl2eIFu110iayg4ye1LAUgHeteITRcqpHAmFcEFUrib7IiaajeOFLNQOqib3QmCaCOANDicpqI/640?wx_fmt=png&from=appmsg)

我这里想讲的，是对“蒸馏”这个概念的进一步泛化。可以理解为把高端模型在完成复杂任务时表现出来的关键能力进行提炼，包括：任务拆解方式、上下文组织方式、工具调用顺序、验证与反馈机制、失败后的修正路径、中间产物的结构化表达、判断标准与检查清单 等等，然后把这些能力沉淀进一个可执行、可观测、可反馈的 Harness 里。这样，中低端模型即使本身能力不如高端模型，也可以借助 Harness 中预先设计好的任务结构、执行路径、工具链和验证环节，更稳定地完成原本只有高端模型才能做好的任务。

在罗福莉的访谈里提到了她在用OpenClaw的的时候，她对她进行了优化改进，并且发现通过这类Agent的“精细化的Context调用”及Skills等的应用让中端模型实现与高端模型（claude 4.6）对标的效果，当然她强调了了1T参数模型的入场券门槛，这些其实侧面说明了她不是再说“框架比模型重要”。当然后面主持人也提到后面小米也了对应Claw，不过显然对她更大的启示还是上面已经说过在训模型角度的转变。

那这里提到中端模型通过一些模型之外的Harness框架工程，达到了类Claude 4.6的效果，这其实就是我上面提到的泛化版“蒸馏”。

其实在我在《[AI Agent 下半场](https://mp.weixin.qq.com/s?__biz=Mzg5OTU1NTEwMg==&mid=2247484484&idx=1&sn=f2074c8b6895179bbcc21bb5db71b712&scene=21#wechat_redirect)》里提到的 ：

> “下半场”范式：自动总结生成 Skills并分发

的部分最佳实践效果是：用高端模型去完成任务并自动总结对应的Skills然后提供给中低端模型使用，在后面的案例文《[使用Zoomeye 和 AiPy 捕获 Coruna 样本](https://mp.weixin.qq.com/s?__biz=Mzg5OTU1NTEwMg==&mid=2247484497&idx=1&sn=0b609734e0cd791e816729101d7208ea&scene=21#wechat_redirect)》 其实就提到了这个“套路”的实战，用Gemini/Codex的模型能力实现后，提炼Skills，应用到国产模型上，效果是非常显著的。

这里也顺带提一句在，也就是我上面提到的 Skill自循环 这个在后面看到的 Hermes 里都有实现参考：

[https://mp.weixin.qq.com/s/R8r4WSi1eEh0r0Uwxo\_5dA](https://mp.weixin.qq.com/s?__biz=MzA5NDYyNDI0MA==&mid=2651960454&idx=1&sn=4f80bd8d5539a8888c3586bf8bc6a36e&scene=21#wechat_redirect)

当然我本地AiPy也实现了

![](https://mmbiz.qpic.cn/mmbiz_png/xTZfvDhkzLtm3xhkSbHKRegficqffnzrRaZicmL3ROTEXEkNBaxSGWsxE0Kt7icj7Kj67US4hWLg739bfMWsicRhcXOmUibnZAYQ6ywUJxib0RTvU/640?wx_fmt=png&from=appmsg)

对于AiPy来说，我们主力模型其实一直都是国内模型，相比Manus同期的Agent那时候是完全依赖Claude的模型效果的（那时候应该还是在3.5～3.7），而AiPy一直在针对工程模型上做最大的体验效果（当然你要接国外顶级模型也是完全可以的只是得手工配置下或者使用我们AiPy的海外版），所以很多时候收到用户反馈说，体验很多各种Claw后发现还是AiPy最能真正干活，可能也就是这么个原因。

当然我这里说Harness框架工程给带来的模型落地效果的增益，这个是跟罗福莉观点是一致的，在不久后这种自进化的可能不只是Skill，Agent的框架等都可自进化，框架应该应该高端与模型“耦合”，把框架自身的各种接口开放给模型，让模型接管一切～～ 这个有点让我想起了当年我推荐过的一个项目ELL：

> https://github.com/madcowd/ell

 也是唯一一个我推荐但是没有那么火的项目。不过最近看到一个TS框架项目也是有那么点味道 ：

> https://github.com/withastro/flue

不过我觉得可能ell这种项目不火，但是这些理念可能会慢慢融合到新的框架设计中。

视角

在前面我们讨论很多人片面解读罗福莉访谈的一些观点的时候，其实跟视角相关，比如 《罗福莉：AI 的范式变了，框架比模型更重要》可能代表的是第三方Agent开发的视角，而 罗福莉 自己更多是一个基础模型研究视角，这个是跟她本身的研究领域方向是相关的，所以导致这她相对“后知后觉”模型训练从Chat模式转Agent模式，而实际上现在线上的那些模型的Chat服务，早就不是一个单一的模型了，而是一个内化的Agent的互联网模式框架产品，也就是类Manus这类的云端的产品。当然在她的访谈里也提到模型会结合Deep research这种单一功能的智能体，觉得很简单，并没有太多纠结的地方，直到OpenClaw的体验经历带来的改变。

这里其实是有几个视角：

> 第三方Agent开发视角
>
> 模型厂商视角

这些其实在我以往的文章里都涉及到，而我更多的使用“环境”视角或者说“数据”视角，如果简单粗暴点 分云端 和 本地 ，就像我之前文章里提到过的 “Manus这种云端Agent都会被模型厂商产品内化”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xTZfvDhkzLtsCRdxYHKWT7y2LxwjKfAzqy3nXmfJHsUGDgLCNg2CVhFAxt5P2h4zvDVnh0dHmXoVibuZic1vSmENtutTbtibH99wuc8AmsiaYIU/640?wx_fmt=png&from=appmsg)

于是我把我写的这些文章、罗福莉访谈、包括上面批判的《罗福莉：AI 的范式变了，框架比模型更重要》文章都发模型，最终通过GPT-Image-2模型给我生成下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xTZfvDhkzLu96cqLXnrGic4LM7J0qceKM7VnEpqlLaDTMR8k7KtXdNsRBwtibnBoaE9eJygjqicmxJkFozO1eMj0Ed55eTGQUUXDZpbNaHYlnM/640?wx_fmt=png&from=appmsg)

开源

罗福莉在聊到“为什么不是 Claude Code？”有原因之一把它归结到OpenClaw是开源，而Claude Code不开源，其实对于OpenClaw的火我认为是一个综合因素，开源可能是中间的一个因素环节，当然她也提到Claude Code 的设计是 for 软件工程的，这个也就是我上面提到过了 Vibe-Coding VS Vibe-Working的问题。

简单来说她认为：

> Claude Code 是：
>
> 模型强 + 产品封装强 + 闭源内部迭代。
>
> OpenClaw 是：
>
> 框架开放 + 用户可改 + 社区可贡献 + 模型也能参与改造。

她这里强调的是开源可以带来“群体智慧”，实现：代码 + Skills + Memory + Workflow + Context + 使用反馈 + 人类经验 的共同演化。

对于开源的态度我其实是非常认同的，在前面参加腾讯云主办的AI Ag...