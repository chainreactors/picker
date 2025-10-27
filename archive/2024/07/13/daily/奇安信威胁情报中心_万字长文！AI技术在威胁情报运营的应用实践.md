---
title: 万字长文！AI技术在威胁情报运营的应用实践
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247511122&idx=1&sn=5cd8dd096eb9fa93d36695566f1a9802&chksm=ea665b25dd11d233874ee6249a1b3c131fa7e059ea9ae6bbd3f2fb14aafd8b8d827aa7e4ffcc&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2024-07-13
fetch_date: 2025-10-06T17:43:12.767920
---

# 万字长文！AI技术在威胁情报运营的应用实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gModd0uVe72bXC1gAyqa3pXGPv26g2BVE4s0PzD5pdEX13NAwJeErbA/0?wx_fmt=jpeg)

# 万字长文！AI技术在威胁情报运营的应用实践

奇安信威胁情报中心

以下文章来源于虎符智库
，作者汪列军

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6cVdDn2tUw6HoP5Eic3SrLmnxG32EHGBFYEbGjfOFupgQ/0)

**虎符智库**
.

“虎符智库” 专注解读网络安全重大事件与技术趋势，提供高层决策参考。

![](https://mmbiz.qpic.cn/mmbiz_gif/f0ibSzjpDC6pSZGLpTxpWAujjOHTP1xd2fhzHudXhsB5QVPzJQJg6Q6yhVRialQboJmKeOlxwSEmeYiaxhVpTicTMA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

本文**14640****字**   阅读约需**37****分钟**

**一、AI的进展回顾及在网络安全的应用**

**1.人工智能关键事件的回****顾与展望**

![](https://mmbiz.qpic.cn/mmbiz_svg/0sDCa2E8S1vGSDgFlD8n67wSQDrE0c6CeTAREIbXAu4d8W8zaRYoPQMg0G93maJrhVtAFShcSmX9NK33AGLuCRzF53KRZryj/640?wx_fmt=svg&from=appmsg)

首先回顾一下笔者眼中人工智能史上重要的的事件。

◆ 20世纪50年代，人工智能和图灵测试就已经提出，但可能受限于计算能力似乎一直进展缓慢。直到1997年，IBM深蓝战胜卡斯帕罗夫，标志着AI在复杂策略游戏领域的进展，其实从现在来看，算法也并没有多复杂。

◆ 2010年开始，深度学习技术兴起。2012年AlexNet首次应用于图像分类任务ImageNet竞赛中，取得了显著的成功，并且以极大的优势领先，进步远超前几年的比赛。标志着深度学习在图像处理领域的一个重要转折点，开启了深度学习热潮。训练AlexNet只使用了几个GPU，效果远不如的Google系统则用了上万个CPU。从此也开启了英伟达的泼天富贵之路。

◆ 2016年，DeepMind AlphaGo击败围棋世界冠军李世石，展示了强化学习在解决复杂策略问题上的潜力。从此，电脑成为围棋最高水平的尺度，人类上千年的积累比不上程序几个月的训练。

◆ 2017年，Google提出Transformer，其注意力机制成为NLP领域的新标准。2020年后，Transformer架构不仅限于文本处理，还被应用于图像识别、语音处理等多个领域，对于以后惊艳的GPT出现形成了核心而又深远的影响。

◆ 2020年，OpenAI发布GPT3，展示了惊人的生成能力和跨任务适应性，无需针对特定任务进行微调即可完成多种NLP任务，但在2020年的当时还未出圈，形成全社会的影响。

◆ 2022年，11月ChatGPT发布，真正开始破圈。人工智能的热潮开始汹涌，从此以后各种商业和开源模型如雨后春笋，相关的应用方兴未艾。

至于未来会怎么样，人工智能会不会产生意识，面对超级人工智能，我们和它会是什么样的关系？笔者推荐一本书《生命 3.0》。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gWibXia7ltP9Ru7Od028hJY73kIuKxbJW7HLIJ8ibrnEJwBvP7dhNUlrBw/640?wx_fmt=png&from=appmsg)

从最乐观的人类超级智能伙伴，就像电影《HER》里面的那样，不仅能支持物质生产，还能提供情绪价值，照顾到生活的方方面面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gDeGpaPJ1zdRkW1flicrn9AbdzrBACq0gjHP4msXicicwicZ4NKgROiaNp0w/640?wx_fmt=png&from=appmsg)

但这种超级智能的出现也隐藏着巨大的风险，目标上没有有效对齐的超级智能也极可能成为人类的终结者。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gO2mgHDMU4FNZtmmEkjVDUaNDCmR3rADx4H052NdfzicRYHNRCicyd4Wg/640?wx_fmt=png&from=appmsg)

《生命3.0》这本书在第5章设想了几种可能性，但实话说，这几种设想也可能都是错的。另外说一句，这本书出版于2018年，里面写的事情最早发生于2015年，那个时候远没有到人工智能的iPhone时刻，可在那个时间点泰格马克那些人已经从深度学习神经网络的进展中意识到了人工智能的发展潜力。

**2.人工智能在网络安全方面的应用**

![](https://mmbiz.qpic.cn/mmbiz_svg/0sDCa2E8S1vGSDgFlD8n67wSQDrE0c6CeTAREIbXAu4d8W8zaRYoPQMg0G93maJrhVtAFShcSmX9NK33AGLuCRzF53KRZryj/640?wx_fmt=svg&from=appmsg)

**（1）前大模型时代**

再说回网络安全，以下是一个国外研究机构的总结报告中的结论，对大模型前的机器学习/AI技术在网络安全领域的一些应用成果做了评估。

Machine Learning and Cybersecurity - HYPE AND REALITY

https://cset.georgetown.edu/wp-content/uploads/Machine-Learning-and-Cybersecurity.pdf

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gqAhAMqbiaqUfzWpiaBJpjA4ZgGJFsaS0h3H98YvD5G7lXqTX7aXPktyg/640?wx_fmt=png&from=appmsg)

目前主要在恶意代码检测、入侵检测和垃圾邮件检测三方面，这些应用在2010年代已经比较成熟，也展现出了较好的效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0g4EOEA2BHdDXJb02ZKPbMiaStlHqRqH1wWR5YHn842XG43xdl0fEyB4Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gc4hiauLt2lffjHdCmDjhFibNUstCVbPicA6XCCljVzjxC2hGp2OcqyPZg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gzWfba4icHNJblXrIesicytXknKtotmZ6TtNsMG0tNZ7RnRMwNsLTm86w/640?wx_fmt=png&from=appmsg)

在网络防御的各主要环节中，包括深度学习、自然语言处理、强化学习、生成对抗网络等技术都被尝试过了，但从实际的影响来看，大都是中低级别的相对传统方法效果改进型的，并没有产生颠覆性的影响。

**（2）大模型时代**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gE4WBo74BoUWkYekJ01vpiaplsqYXWCkAdNhNEdlFpjcLQApO0nxkFmA/640?wx_fmt=png&from=appmsg)

在大模型出来之前，基于机器学习的处理系统也经常被描绘成一个大脑的样子，但那些系统其实只能完成非常特定的任务，不具备通用性，只有真正结合了通用知识和推理能力的模型才有资格以大脑的样子呈现。这里我们列了一些大模型在网络安全方面可以有所作为的方向：

◆ 威胁检测与分类，涉及恶意代码的检测和分析、钓鱼邮件的识别、访问异常行为的判断，可以得到比传统机器学习及AI更好的效果。

◆ 威胁响应与决策支持，规则生成，自动化脚本与分派任务，告警降嗓，交互式操作支持，大模型具备各类安全工具平台相关的脚本和规则知识，比如IDS系统Snort、文件扫描引擎Yara，可以根据来自各种报告的相对高层次的自然语言的技术性描述生成各类检测规则和脚本，以及可加载处置设备的策略文本，对于信心度高的规划可以自动使能，有些关键操作可能还需要人的审核。

◆ 威胁情报收集、处理及输出，关于威胁行为体、攻击手法及IOC信息的产出，用于构建问答式知识库的核心技术。

◆ 漏洞信息整合，利用大模型强大的代码理解和构建能力挖掘和分析软件中的漏洞，协助开发漏洞利用POC也是可能的。

◆ 应急响应与事后分析，根据响应过程中收集到的事实和技术信息自动生成事件报告，这些可以极大减少人工工作量。

◆ 教育和培训，生成安全最佳实践、模拟攻击场景和提供答案解释。

所有与文本和图像分析和处理的工作都是大模型的强项和可以充分挖掘的能力，在威胁情报方面的应用正是大模型的擅长方向。

接下来，我们通过一些测试来看看。

**二、威胁情报运营各环节及AI技术的应用概览**

首先简单介绍一下奇安信威胁情报运营的基本流程，这本质上是一个数据驱动的过程，从多个源头做数据采集，经过一系列清洗、分类、检测、关联、结构化等过程处理以后，形成数据或服务输出给安全检测产品和相应的威胁分析响应人员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gqiaVr40E2H5g7bMMkdsUoWa63bq7d9hdvTBKFsXJBQW94Bo1v1nmic5g/640?wx_fmt=png&from=appmsg)

在网络威胁情报的运营生产过程中，包括大模型在内的AI技术在流程的各个环节加以合理运用能极大提升运营的效率与效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0g7bliax76kDKnCfpRTV1wbOJAgeiaXTCXOfAhVDq67kNhp5JzpqQYEMEA/640?wx_fmt=png&from=appmsg)

上图展示了奇安信威胁情报运营的主要环节及相应AI技术应用情况，这是多年累积的结果，传统的机器学习的技术早已应用，在大模型技术出现以后有些能力被取代或加强。

首先，从数据采集开始。在这个阶段，我们的目标是从各种来源收集尽可能多的数据并进行快速而准确地分类和提取。这里需要执行网页解析、文本翻译和OCR识别等操作。几乎在获取的同时对信息进行分类，去除噪声和无关数据。运用自然语言处理技术，特别是利用大模型进行语义标签的自动分类和智能分析，从而完成精确的多维度的信息分类，据此可以进入不同的处理子流程。其中，大语言模型发挥其在数据分析方面的核心优势。它们能够理解和处理大量非结构化的文本及音视频数据，并从中提取我们需要的关键信息。

然后是检测识别。这一阶段的目标是对文件样本与网络流量等元数据执行检测，进行威胁判定，标记恶意实体，这是威胁情报运营过程中核心环节，安全厂商的能力所在。本阶段使用了比较成熟的机器学习算法和深度学习技术，实现恶意样本的标定和恶意网络攻击的识别，收集其相关的威胁情报工件数据。

接下来，我们会对收集到的威胁元数据进一步结构化，综合利用自然语言处理技术、大模型技术以及大规模威胁知识图谱的构建，提取精准的威胁实体并建立多类型的关联。

在结构化之后，我们进入信息富化的阶段。这一步骤涉及到关键子图的提取和大规模图嵌入，从其他源补充更多的关联信息。通过这些方法，我们可以揭示出隐藏在数据背后的模式和联系。

实体信息富化以后做进一步的拓线关联。我们利用智能Agent和图相似计算来推荐可能的相关恶意实体和事件。这使得我们能够建立一个完整的威胁图景，并挖掘出更多潜在的威胁对象实体。

最后，我们生成报告并对情报进行摘要总结。这一步依赖于大语言模型的技术，它们能够生成简洁且易于理解的报告并给出结论，基于公开和内部信息构建安全知识库，为威胁分析和应急响应人员提供信息支持。

这就是整个网络威胁情报生产及运营的过程。通过结合大语言模型、安全大数据计算技术和深度学习技术的综合应用实现威胁情报的快速发现和输出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gqbzwoLVf7kAzYhet2H5o96Fyn52dYg7Y0qX7UK3sND6uItkcticiafHg/640?wx_fmt=png&from=appmsg)

在测试和应用AI技术的过程中我们的用到了一些工具，底层的当然是一些基础的大模型，比如最强大的来自OpenAI公司的闭源模型GPT4，国内比较流行的口碑较好，测试下来效果也确实不错的Kimi和通义千问，还有能力与GPT4可以媲美的开源模型Llama3，Mistral也是一个性能与能力平衡得较好的模型，当然包括奇安信自研的安全大模型QAX-GPT，安全相关的知识与能力更优。

基础模型的能力通过Web界面和API可以直接被使用，做文本分类、模式识别和信息提取。在此之上，有各种应用程序，做数据获取比如ScrapeGraphAI和Jina；各类支持开发框架，比如Ollama、LlamaIndex、LangChain、DIFY；组合起来开发实现很强功能的智能体应用，目前非常好用搜索增强平台，比如Perplexity及国内的秘塔；各类本地RAG工具，比如QAnything、AnythingLLM等。整个基于AI大模型的生态已经快速建立起来。

**三、情报运营各环节AI技术的测试应用及体会**

**1.网页解析**

![](https://mmbiz.qpic.cn/mmbiz_svg/0sDCa2E8S1vGSDgFlD8n67wSQDrE0c6CeTAREIbXAu4d8W8zaRYoPQMg0G93maJrhVtAFShcSmX9NK33AGLuCRzF53KRZryj/640?wx_fmt=svg&from=appmsg)

威胁情报的运营开始于信息的收集，来自各种Web页面的开源内容是收集的主要目标。

利用大模型极其强大的文本分析能力，可以方便地实现网页的处理，ScapeGraphAI工具就是这样一个集成了大模型文本分析能力的网页内容爬取工具。这里是一个使用其爬取Mitre网站的APT组织信息页面并转化为结构化数据的例子。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gWqvWwfvcKZ2RtDO723jIl14SlM3PNt7AaJaS1sqyS4ahDOvviafKDfA/640?wx_fmt=png&from=appmsg)

工具充分利用了大模型理解抽象指令和页面解析的能力，处理复杂页面不需要再专门写适配的解析代码，只要描述要求即可，当前这个例子核心AI能力使用了本地部署的llama3模型，其实就当前的任务而言都不需要能力这么强的模型，用更轻量级的Mistral就可以了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0g66XfATCteW1xLNtfQPoicz9jDK3Dj7icENADBGCXCtANmpr6fRVGcW9w/640?wx_fmt=png&from=appmsg)

另一个非常有用的工具是jina.ai，这是一个非常方便的把网页内容精减成Markdown格式文本的工具，目前可以免费使用，使用频率上有点限制。它会获取网页，自动去除掉包括广告在内的无关信息，输出一个Markdown格式的文档，这些内容可以被后续的大模型应用所消费。

比如给jina.ai指定下面这样的一个威胁行为体的介绍网页：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gKlqwtFnW262EXJnOMNxAZYKelYxvNSTjO0nMpJaqQn0CLqhPicURy4w/640?wx_fmt=png&from=appmsg)

https://unit42.paloaltonetworks.com/cve-2024-3400/

jina.ai会输出如下的Markdown文档：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f0ibSzjpDC6pOyfB335KBZQ7pRia3B6W0gBoic227XrVsDGAbC01BoRo5icarRHdDNtfEyxUCg5oUsS4ic4t70LcsGg/640?wx_fmt=png&from=appmsg)

https://r.jina.ai/https://unit42.paloaltonetworks.com/cve-2024-3400/

使用方式非常简单，只要在要处理的网页链接前添加”https://r.jina.ai/”即可。

**小结**

● 利用大模型的能力进行网页爬取、解析及结构化目前还处于概念验证阶段，实用系统需要较强的工程化能力和强大的算力支持。

● 用于处理复杂网页较为合适，简单网页杀鸡用牛刀。

● 获取页面内容最好用jina这样的核心信息提取服务，后续大模型处理时既可以减少非相关信息的干扰，又能减少Token的消耗。

● 输出后续用于大模型的精减格式化数据非常有用，数据通过API以结构化的方式交换加速成为主流，将来Web页面被人眼访问的比例会越来越低，Web可能慢慢走向消亡。

**2.文本翻译**

![](https://mmbiz.qpic.cn/mmbiz_svg/0sDCa2E8S1vGSDgFlD8n67wSQD...