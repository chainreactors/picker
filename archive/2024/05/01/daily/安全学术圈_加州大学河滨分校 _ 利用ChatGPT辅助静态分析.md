---
title: 加州大学河滨分校 | 利用ChatGPT辅助静态分析
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247490600&idx=1&sn=288d2caf6b51c84141b3c9957d100575&chksm=fe2ee3a3c9596ab5d71e69fa29160c651f9a8b4dc4e6a076175422a666756bbcfbff63f2e716&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-05-01
fetch_date: 2025-10-06T17:20:24.568340
---

# 加州大学河滨分校 | 利用ChatGPT辅助静态分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WGnA9qDFqppgwhSI4ibibhBfpFdYUEvrx8IibLODLbJbKzJ5Dck2FGeAyJ01ibQkic0subEyibkaYOziapVA/0?wx_fmt=jpeg)

# 加州大学河滨分校 | 利用ChatGPT辅助静态分析

原创

童话

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGnA9qDFqppgwhSI4ibibhBfpFVibVaGdJJdXmbRJav0JGiav4YjELyqze9mcQPvibqvlMlB0Og00ODJ6w/640?wx_fmt=png&from=appmsg)
> *原文标题：Assisting Static Analysis with Large Language Models: A ChatGPT Experiment*
> *原文作者：UC Riverside (Haonan Li, Yu Hao, Yizhuo Zhai, Zhiyun Qian)*
> *发表会议：ESEC/FSE ’23*
> *原文链接：https://dl.acm.org/doi/pdf/10.1145/3611643.3613078*
> *项目代码：https://github.com/seclab-ucr/GPT-Expr*
> *主题类型：大模型安全*
> *笔记作者: tonghuaroot - https://www.tonghuaroot.com/about*
> *主编：黄诚@安全学术圈*

# 前言

静态分析在精确性和可扩展性之间存在固有的权衡，实际应用中，静态分析工具经常会产生大量的误报，这阻碍了其广泛的应用。然而，现在有了一种可能性，那就是利用大型语言模型（LLMs），例如ChatGPT，作为静态分析的全方位和综合辅助。ChatGPT甚至表现出理解编程语言的能力，作者团队推测它可以生成比静态分析计算得到的函数概要更精确的信息，特别是在存在循环和对可变长度数据结构操作（例如，strlen()）的情况下。这些精确的函数概要可以作为更有效的分析基础，从而减少误报和漏报。

作者团队开发了一种可利用ChatGPT自动创建精确函数概要的系统方法。这种方法已经在一种名为UBITect的实际静态分析工具上进行了评估，该工具识别出了由于函数概要不精确而产生的误报和漏报。值得注意的是，在使用最新的GPT-4模型的情况下，该方法为20个实例中的16个提供了精确的概要，在初步研究中有效地消除了误报情况。

此项研究的贡献如下所示：

* 利用LLM开发了一种新的方法，以提高函数概要的精确性，减少静态分析中的误报和漏报；
* 提出了一种使用ChatGPT自动且逐步生成精确函数概要的方法；
* 评估这种方法来补充实际的静态分析工具，展示出了巨大的潜力；
* 为了进一步的研究和发展，作者团队已将他们的工作开源在https://github.com/seclab-ucr/GPT-Expr上。

# 背景和相关工作

在软件工程中，大型语言模型（LLM）的应用越来越广泛。例如，ChatGPT已经被用于自动化的、对话驱动的程序修复工具中，成功率接近50%。同时，还有研究者研究了使用LLM进行 zero shot 漏洞修复，并在人工设计的和合成的场景中看到了一些希望。此外，LLM还可以用来生成未覆盖代码的测试。在这篇论文中，作者团队探讨了当静态分析遇到困难时，如何使用LLM作为一种更好的替代方案。

UBITect是一种针对Linux内核 UBI 漏洞的工具，其通过两阶段的过程进行工作。首先，UBITect会对内核进行自下而上的基于概要的静态分析，这是一种MAY分析，函数概要会指示可能出现的漏洞，这可能会产生大量的漏洞。在第二阶段，UBITect使用符号执行来过滤掉误报，通过验证报告的漏洞的路径的可行性。然而，由于符号执行的超时或内存限制，超过40%的报告的漏洞被丢弃，这可能会错过真正的漏洞。在这篇论文中，作者团队专注于这40%被丢弃的案例，干掉误报，同时也找到了错过的真正的漏洞。

# Motivation

这部分研究内容主要展示了一种名为UBITect的静态分析工具在分析过程中出现误报的实例。首先，UBITect在代码的第4行和第5行报告了一个错误，认为参数a、b、c、d没有初始化就被使用了。然而，这是错误的。对于第4行的报告，错误在于UBITect无法找到特殊函数sscanf()里的va\_start()和va\_end()的定义，并保守地假设它们可能“使用”了参数。但事实上，这些函数其实是编译器内置的，它们识别可变长度的参数，不存在“使用”的问题，sscanf()实际上是在“初始化”参数，而不是“使用”。对于第5行的报告，错误在于UBITect生成的函数概要对其返回值的检查（if(sscanf(...)>=4）或者说后置条件不敏感，因此UBITect提供了一个保守的概要，估计所有参数“可能”没有初始化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGnA9qDFqppgwhSI4ibibhBfpXFnok0RIWYTHOx56OQrndohTmo4gQJ25sMaic4ibicDkdOW3yk4VCktnQ/640?wx_fmt=png&from=appmsg)

image

这个案例揭示了静态分析中常见的两个问题：首先是静态分析需要编码领域知识来模型化某些特殊函数，这就是我们称之为的“知识边界”问题。除了可变长度参数的情况，还有许多其他场景（尤其是在Linux内核中）涉及到复杂的领域知识，这使得直接分析变得困难，如汇编代码、硬件行为、并发性和编译器内置函数等。其次，像sscanf()这样的案例需要考虑其检查条件：sscanf(...)>=4，然而现有的路径敏感的静态分析（和符号执行）技术工作在一个方法论性的但又详尽的范式下，探索代码库的所有可能的执行路径，虽然理论上全面，实际上却常常导致组合爆炸。

这些问题的挑战可以通过应用大型语言模型（LLMs）来绕过，特别是像ChatGPT这样的模型。它们经过大量的自然语言和程序代码的训练和对齐，展示了对代码理解的有前景的能力。

# 方法

作者团队的研究目标是将ChatGPT与UBITect相结合，以提高UBI漏洞的检测能力。UBITect的工作分两个阶段：首先进行初始的静态分析以找出潜在的UBI漏洞，然后通过符号执行来确认这些猜测。但在实验中，40%的案例因为时间或内存限制而被忽视。这种情况带来了一个问题：如果我们将这些潜在的漏洞分类为误报，我们可能会忽视真正的漏洞。相反，如果我们将它们视为真正的漏洞，我们可能会面临大量的误报。为了解决这个挑战，他们的方法是在这些模糊的情况下咨询ChatGPT，使他们能够辨别出它们是误报还是真正的错误。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGnA9qDFqppgwhSI4ibibhBfpzib9woQJ0Fdibib3Dz6pILjNFJFmTsNfENXaa5yRmd8WupibTSicL45hbJw/640?wx_fmt=png&from=appmsg)

image

在设计上，他们首先从UBITect中提取潜在UBI漏洞的关键事实，即未初始化的变量、后置条件，以及可能初始化该变量的函数。然后，他们自动将这些信息输入ChatGPT，并让它确定该变量是否被初始化。在这个过程中，他们认识到函数概要在UBITect中的关键作用，以及它们对结果的直接影响；因此，他们提示ChatGPT概括函数。因此，“must\_init”等同于“not a bug”，他们将问题变得更小。

对于每个报告的错误，他们提取函数调用上下文，包括具体的参数和返回值检查。然后他们询问ChatGPT，在给定调用上下文和在特定的后置条件下，变量“必须”被初始化。最后，他们提示ChatGPT生成一个结构化的总结，以便无缝地集成到进一步的分析中。

他们在设计提示时遵循了一些关键原则。例如，“Chain-of-Thought”策略利用“think step by step”来鼓励ChatGPT生成包含每个步骤的中间结果的更长的响应。他们还发现将问题分解为更小、更简单的任务对ChatGPT来说更有效。因此，当他们需要一个结构化的输出时，他们总是在对话的最后发起一个新请求，并提示ChatGPT以JSON格式进行结论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGnA9qDFqppgwhSI4ibibhBfpzryJENibNYoqqlX6iaabpL1TjSU7rNS4Mibia6W7bCefPAx8wGuudEH1Xw/640?wx_fmt=png&from=appmsg)

image

# 评估

为了验证所提方法的有效性，作者团队随机抽取了一些从UBITect的符号执行阶段得出的不确定的案例。确切地说，他们随机选择了20个人工确定为误报的案例，以及两个UBITect遗漏的额外漏洞。因为UBITect单独使用时，所有这些案例都是不确定的，所以，他们对于评估他们的方法在确定这些报告漏洞的结果方面的有效性感兴趣。所有实验（包括GPT-3.5和GPT-4）都是在2023年3月23日的ChatGPT版本下进行的。

在评估函数摘要的结果时，他们主要关注两个方面：即，是否正确地标识了被标记为“must\_init”的变量（Soundness），以及是否正确地标识了所有被标记为“must\_init”的变量（Completeness）。他们对每个案例进行了三次运行，以考虑到ChatGPT输出的概率性，如果任何一次运行表现出不完整或者不完善，他们会认为该案例的结果是失败的。

为了解决研究问题，他们收集了三个真实的UBI CVEs，并将其输入到ChatGPT（GPT-4）进行分析。正如前面在第四部分中提到的，直接提供上下文的结果很差。在他们的实验中，他们明确提到了未初始化的变量，并问ChatGPT来确定是否存在真正的错误。他们还使用了第四部分中提到的提示设计策略。例如，利用渐进式提示，通过请求ChatGPT“如果需要函数定义，应该向我们询问，我们将提供它们。”他们在3个真实的CVEs上测试了这种直接方法，每个测试案例重复5次。他们的发现显示，所有的测试案例都没有在所有五次重复中被一致地正确分析。对于这三个CVEs，ChatGPT在3/5，2/5，和0/5的实例中正确地识别了漏洞。

表1比较了由GPT-3.5和GPT-4生成的函数摘要。大多数回应在所有三次运行中都是一致的。他们从表格中排除了四个误报案例，因为UBITect出于超出了在第三部分中概述的原因报告了它们，例如，不准确的间接调用解析。GPT-3.5的结果显示，只有61%是 sound，44%是 complete。另一方面，GPT-4在性能上显示出了显著的提升，达到了94%的sound和complete。表格的前16个案例指示误报，而最后两个案例代表真正的UBI漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGnA9qDFqppgwhSI4ibibhBfppZibHCVfMzGiczUcCM3mRu1UdC0aES9bC1UMgp8Zze6fhRcPOF7jymdQ/640?wx_fmt=png&from=appmsg)

image

有多种原因导致GPT-3.5无法分析某些案例。例如，变量名很重要。在snd\_interval\_refine案例中，GPT-3.5对形式参数和实际参数的名称感到困惑，导致了不正确的回应。此外，在GPT-3.5的实验中，他们发现它通常会在没有请求更多信息（例如，请求更多函数定义）的情况下过早地得出答案，即使他们明确指示它这样做。当这种情况发生时，结果通常是不可靠的。相比之下，GPT-4始终在需要时进行长时间的对话，从而有助于其优越的性能。

> 笔记作者注：关于 sound 和 complete，
> 可以参考这张图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGnA9qDFqppgwhSI4ibibhBfpblgKicgdcRbclG49GE0qgADYaepvfUk4udfSApOlUHFss7wm74W4ENg/640?wx_fmt=png&from=appmsg)

image

> Sound 和 Complete 可以简单理解为误报和漏报。如果一个完美的静态分析程序，可以给出明确的结论（是或者不是），我们就可以称这个静态分析是既 Sound 又 Complete 的。不存在一个既 Sound 又 Complete 的方法，可以准确的给出结论。

# Case Study

作者团队通过两个真实的UBI漏洞，展示了他们的方法在分析函数行为和检测未初始化变量方面的成效和局限性。第一个例子来自于arch/x86/kvm/lapic.c中的一个实际漏洞，这里使用了未初始化的变量val。如果函数pv\_eoi\_get\_user返回的值小于0，代码会继续执行而不是提前返回，这就导致了第5行中val&0x1的使用。UBITect由于超时而未能检测到这个漏洞，而ChatGPT处理了这个问题，并通过将val分类为“may\_init”正确地识别了这个漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGnA9qDFqppgwhSI4ibibhBfpj0aYskdumaY8FLcMkLWSXuOpX6JaKiaZc4I2eW3TtRIZxzcqqGO0Ehg/640?wx_fmt=png&from=appmsg)

image

第二个例子展示了net/9p/client.c中的另一个UBI漏洞。可以看到，当函数p9pdu\_vreadf()返回-EFAULT时，它可能没有初始化其参数ecode。然而，p9\_check\_zc\_errors()直接使用了它的值，而没有检查第3行的返回值。虽然ChatGPT总是正确地识别相关代码（见图5中的第8-14行），但其最终的裁决有时是不正确的（三次中有一次）——将ecode分类为“must\_init”。这种在获得的结果和推理步骤之间的不一致是链式思考提示中的一个已知问题。作者团队计划在未来的工作中采用额外的设计策略来解决这种不一致性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WGnA9qDFqppgwhSI4ibibhBfpjLuLM2dkrNiaJS1awibmB6VL2TaxeicBIs1BQ2Zy13sFXzkA7KibvEBBCQ/640?wx_fmt=png&from=appmsg)

image

# 讨论 & 限制

作者团队在实施方案中承认存在一些局限性。由于GPT-4 API在提交论文时不可用，实验的规模相对较小，这需要进行手动测试。尽管如此，他们的工作流程在设计上是完全自动的，并且可以在具有API的大规模数据集中工作。另外，他们还未考虑到使用前初始化这一问题比较复杂的漏洞。尽管如此，他们创新的基本技术可以应用于其他类似的静态分析。在将来，他们计划研究更复杂的漏洞。在他们的实验中，他们没有遇到 token 限制问题。这可能意味着当前的上下文窗口（即GPT-4的8k token）在大多数情况下是足够的。但是，考虑到渐进式提示设计，他们怀疑当ChatGPT不断请求更多功能时，他们可能会达到限制。

# 结论

综上所述，利用ChatGPT来辅助静态分析存在巨大的潜力。

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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