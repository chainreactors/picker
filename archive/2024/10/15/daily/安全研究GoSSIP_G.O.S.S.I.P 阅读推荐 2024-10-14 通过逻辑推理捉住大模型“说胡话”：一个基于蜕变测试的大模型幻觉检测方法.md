---
title: G.O.S.S.I.P 阅读推荐 2024-10-14 通过逻辑推理捉住大模型“说胡话”：一个基于蜕变测试的大模型幻觉检测方法
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498993&idx=1&sn=50f7dacbe8c634bfe6c8d4c79b14373d&chksm=c063d228f7145b3ea727645c0228ec353f40d402d3d1434fab283d12d7320cba2f3039185978&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-10-15
fetch_date: 2025-10-06T18:52:09.245046
---

# G.O.S.S.I.P 阅读推荐 2024-10-14 通过逻辑推理捉住大模型“说胡话”：一个基于蜕变测试的大模型幻觉检测方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GxVD6JUAoxjoafTMh8pceWjia9xcRLRPOAu8y7iae89ibJQCg0qkbTTJtnpfZhXNogYDCiaS7yeT4cOw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-10-14 通过逻辑推理捉住大模型“说胡话”：一个基于蜕变测试的大模型幻觉检测方法

Ningke@HUST

安全研究GoSSIP

近年来，大型语言模型（LLM）的飞速发展彻底改变了自然语言处理的格局。然而，伴随着其令人瞩目的成就，大模型也面临着诸多挑战，尤其是在安全性、隐私保护以及输出准确性方面。其中，模型幻觉（Hallucination）问题尤为突出，它指的是模型生成看似连贯但实际上与事实不符的内容。这种现象不仅影响模型的可靠性，还可能导致严重的误导。特别值得关注的是事实冲突型幻觉（Fact-Conflicting Hallucination， FCH），即模型生成的内容直接与已知事实相矛盾。这一问题的复杂性和潜在危害使得它成为当前AI研究中亟待解决的关键难题之一。但是检测FCH问题仍然面临着一些挑战，包括如何构建多样化的测试数据集和如何准确地验证大模型的输出。

基于上述背景，一个由华中科技大学和新南威尔士大学等高校联合组成的研究团队近日发表了题为**Drowzee: Metamorphic Testing for Fact-Conflicting Hallucination Detection in Large Language Models**的一项研究，该研究被OOPSLA 2024所接收。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxVD6JUAoxjoafTMh8pceW7hu0DgqzxeE8lK4VTZIkgYKRajLLCFO8hBX8aE6vsaQRzk8xc32cOg/640?wx_fmt=png&from=appmsg)

作者通过一个生动的例子引入了当前 LLM 幻觉检测中的不足之处，揭示了其在处理复杂问题时的局限性。现有方法缺少复杂问题的基准测试，并且过度依赖人工验证。此外，如何准确验证 LLM 的回答也颇具挑战性。以日本作家村上春树为例，他多次被提名但从未获得诺贝尔奖。如果我们只提出关于村上春树的单一问题，LLM 通常能正确回答。然而，当涉及多个实体时，情况就变得复杂。例如，若问：“村上春树和鲍勃·迪伦是否获得过同样的奖项？” ChatGPT 可能会错误地回答村上春树也曾获得诺贝尔奖。这一简单实验揭示了两个重要挑战。

首先，如何自动生成更复杂的问题，以揭示 LLM 的更多局限。为此，作者从逻辑编程中找到了灵感，利用逻辑推理从现有事实生成新的逻辑合理的事实，并据此生成更复杂的问题。

其次，如何自动验证 LLM 的输出。在作者的测试框架中，使用了蜕变关系（metamorphic relations）来对比 LLM 的回答与真实情况，从而构建了自动化的测试基准。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxVD6JUAoxjoafTMh8pceWdiaek4V9JSiaQibqK39ibmibGMiag1LmicrArxDDL4XlEJicY4oNEUk8W1atGg/640?wx_fmt=png&from=appmsg)

整个Drowzee的工作流程如图所示。首先，作者从可靠的知识数据库中生成真实的事实和三元组。然后，作者使用Prolog和设计的逻辑推理规则推导出更复杂的事实。接着，作者创建问答对和提示来与LLM进行交互。在输入提示并得到回应后，作者使用语义结构检查回应是否正常，或是否存在事实冲突的幻觉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxVD6JUAoxjoafTMh8pceWDWfz8pFjO5qNLgq0XXkmE6xjEicBAKBlw79m2NQJqcicOEgdL7kWGbYA/640?wx_fmt=png&from=appmsg)

Drowzee 的首个模块通过从可靠的知识库中提取基本事实，并将这些事实转化为逻辑推理所需的三元组。作者专门从 Wikidata 的九个热门领域中获取数据，并选取三种常见的关系模式，构建知识基础。这为后续的推理和问答生成提供了原始材料。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxVD6JUAoxjoafTMh8pceW1pwZBTnvaWUsxibF6f8xbkib1Bhyoxiaib38bWibFbHU7DW6HBE20ljYB2Q/640?wx_fmt=png&from=appmsg)

接下来，Drowzee 进入推理阶段。基于已提取的事实，作者使用 Prolog 编写的逻辑程序推导出更多复杂的事实。Prolog 是一个非常强大的逻辑编程工具，在这里，它主要分为两部分：事实（R） 和 规则（Q）。简单来说，事实就是带有实体参数的关系谓词，而规则则是根据这些谓词推导新知识的逻辑语句。

为了让这些推理更加丰富，作者设计了五种推理规则：否定、对称、逆向、传递和复合规则。通过这些规则，Prolog 引擎能自动生成大量新的三元组，扩展原始知识。最终，生成的新知识可以被用来创建一系列测试用例，进一步验证大语言模型的表现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxVD6JUAoxjoafTMh8pceWfHdzMMJfWqe95RjN7HDcCUbtrb5k4juZibsEE9mooxxnKS3oOcrmhMw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxVD6JUAoxjoafTMh8pceWHXj0ymzqN31I5h8TGvmZFqT3F0vcJRaGUkzG0Fl6DibXH298tfJVNdQ/640?wx_fmt=png&from=appmsg)

从生成的三元组中，作者构建了专门用于 FCH 测试的问答对。不同的关系类型有其特定的问答需求，作者通过预定义模板，生成了这些独特的问答对。然后，利用 LLM 的知识与推理能力，Drowzee 系统给出对问题的回答——是、否或“不知道”。

最后一个模块则专注于如何通过验证 LLM 的回答，改进 FCH 检测。Drowzee 系统通过比较 LLM 的回答和验证事实之间的相似性，来判断 LLM 是否产生了幻觉现象。如果相似性低于某个阈值，就说明 LLM 的回答与真实情况存在明显差异，可能出现了幻觉。反之，则认为 LLM 的回答符合事实。

具体算法流程是这样的：首先，系统会检查 LLM 是否正确处理了“不知道”的回答。接着，构建回答的语义结构，最后，通过边向量和节点向量的相似性计算，验证回答的真实性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxVD6JUAoxjoafTMh8pceWEWyKkXIqjhCSwkgI0o2CUVibmDJKMycBGgvOJDNnHnCk6pn5p4PeIug/640?wx_fmt=png&from=appmsg)

为了评估 Drowzee 的有效性，作者通过生成 7,200 个测试用例，对各类大语言模型（LLMs）进行了幻觉（FCH）检测。实验结果显示，GPT-4 在测试中表现最好，幻觉率最低，仅为 24%。相较之下，ChatGPT 的幻觉率为 42%，而较小的开源模型如 Llama2-7B 表现较差，但其更大版本的正确回答率甚至超过了 ChatGPT。这表明 Drowzee 生成的测试用例能够有效触发模型的幻觉，尤其是在需要逻辑推理的情况下。

在不同领域的表现上，Drowzee 发现各模型在自然科学和数学领域的幻觉率较高，可能是由于这些领域的知识覆盖在模型的训练数据中不足。此外，错误推理幻觉占据了大部分比例，这表明 LLM 在推理能力上的不足比知识缺乏更容易导致幻觉。通过个案分析，作者展示了模型在时间属性推理和面对不熟悉知识时的弱点作者展示了模型在时间属性推理和面对不熟悉知识时的弱点，甚至可能编造信息。关于更多详细的实验结果和案例分析，感兴趣的读者可以查阅论文内容。

总结来看，Drowzee 提供了一种新的、基于逻辑推理的自动化检测和验证大语言模型幻觉的框架，并为未来研究如何缓解幻觉提供了新的思路。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GxVD6JUAoxjoafTMh8pceWbzgAib5usQu6ia40H3ZvTMl8NPjVhw5m0diap0bW6ZnjpMicFJa9rPJ60w/640?wx_fmt=png&from=appmsg)

未来的工作

在这个工作中作者尝试将逻辑编程应用到大模型幻觉检测中，后续的工作将围绕更复杂的逻辑推理（时序逻辑等）和更深入的模型幻觉研究（现象分析与白盒缓解技术等）。

论文链接：https://arxiv.org/abs/2405.00648

仓库链接：https://github.com/security-pride/Drowzee

作者简介：

李宁珂，华中科技大学研三学生，主要研究方向为智能化程序分析和大模型安全。个人主页：https://ningke-li.github.io/

王凯龙，华中科技大学副教授，为本文的通讯作者，主要研究方向为大模型安全，移动应用安全及隐私。

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