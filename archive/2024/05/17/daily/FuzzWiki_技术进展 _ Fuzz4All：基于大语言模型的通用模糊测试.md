---
title: 技术进展 | Fuzz4All：基于大语言模型的通用模糊测试
url: https://mp.weixin.qq.com/s?__biz=MzU1NTEzODc3MQ==&mid=2247486537&idx=1&sn=7dd8ed328f072304a5a990b459ea2c9a&chksm=fbd9a7f5ccae2ee37dfa51ee4b719bd0923a67be66125a8f8f63fd5dad7932a399c28ba0d8d1&scene=58&subscene=0#rd
source: FuzzWiki
date: 2024-05-17
fetch_date: 2025-10-06T17:17:44.330071
---

# 技术进展 | Fuzz4All：基于大语言模型的通用模糊测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JchE46RGRlre5EnbVnRWKDwibLsH3vmAYA0Dia8wyGLve5QIMc7G3roGboCRwGnmaSLpKaibJY6sPwEsxMbAUvy9A/0?wx_fmt=jpeg)

# 技术进展 | Fuzz4All：基于大语言模型的通用模糊测试

原创

FuzzWiki

FuzzWiki

![](https://mmbiz.qpic.cn/mmbiz_gif/JchE46RGRlr92CPaC2cSiaTUCEWwOd0OucLNLlY09jGCso4gTL4BmXsBNsvOlSMv9qPopLaecg7r21KD4gBERqA/640?wx_fmt=gif)

**基本信息**

**原文名称：**Fuzz4All: Universal Fuzzing with Large Language Models

**原文作者：**Chunqiu Steven Xia；

Matteo Paltenghi；Lingming Zhang等

**原文链接：**https://www.software-lab.org/

publications/icse2024\_Fuzz4All.pdf

**发表期刊：**International Conference on Software

Engineering（ICSE），2024

**开源代码：**https://github.com/fuzz4all/fuzz4all

**一、引言**

Fuzzing（模糊测试）在发现各种软件系统中的漏洞和弱点方面取得了巨大成功。接受编程或形式语言作为输入的测试系统（SUTs），例如编译器、运行时引擎、约束求解器以及具有可访问API的软件库，尤其重要，因为它们是软件开发的基本构建模块。然而，针对此类系统的现有模糊测试工具通常针对特定语言，因此不容易应用于其他语言甚至相同语言的其他版本。此外，现有模糊测试工具生成的输入通常仅限于输入语言的特定特征，因此几乎无法揭示与其他或新功能相关的漏洞。

本文介绍了Fuzz4All，这是**第一个****在多个输入语言和这些语言的许多不同特征上都能够通用的模糊测试工具**。Fuzz4All的关键思想是**利用大型语言模型（LLMs）作为输入生成和变异引擎**，从而使该方法能够为任何实际相关的语言生成多样化且逼真的输入。为了实现这一潜力，我们提出了一种新颖的自动提示技术，该技术创建出适合模糊测试的LLM提示，并且提出了一种新颖的基于LLM的模糊测试循环，该循环迭代更新提示以生成新的模糊测试输入。我们在接受六种不同语言（C、C++、Go、SMT2、Java和Python）作为输入的九个测试系统上评估了Fuzz4All。评估结果显示，在所有六种语言中，**通用模糊测试实现了比现有的特定语言模糊测试工具更高的覆盖率**。此外，Fuzz4All在广泛使用的系统中发现了98个漏洞，例如GCC、Clang、Z3、CVC5、OpenJDK和Qiskit量子计算平台，其中64个漏洞已被开发人员确认为以前未知的。

**二、动机**

现有的编译器fuzzer的缺陷：

* **与特定语言强耦合。**以来特定语言的语法进行输入生成。
* **缺乏进化能力。**由于输入的生成逻辑固定，现有工具难以覆盖语言中后出现的特性。
* **生成能力的局限性。**由于存在一些难以模拟的语言特性，现有工具的输入生成往往只利用该语言所支持特性的子集。

由于LLM 具有结构化代码生成的能力，本文利用LLM 来构建一个跨语言的编译器模糊测试工具。

**三、概述**

Fuzz4All的基本框架如下图所示，主要由两部分组成：

(1)**提示词蒸馏（或者叫做Autoprompting）**：对现有的资料进行压缩，提取出更精简有效的生成提示词；

(2)**Fuzzing Loop**：用基于大模型的变异方式替换掉传统模糊测试的变异；

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJOLZQwS7HbUrTooBcRm8dFPsoicMr3I9TTVdnFxnLP6TAhzJ3CCicb9s5A/640?wx_fmt=png&from=appmsg)

**图1** **Fuzz4All流程图**

**四****、要点**

**1.Autoprompting**

本文记提示词蒸馏的大模型为 MD, 在实验中是 GPT-4.

该过程是对用户提供的输入的压缩。旨在去**除掉用户输入中针对代码生成任务的冗余部分**。用户输入可能包含的内容有：目标语言的文档，示例代码和规范（specification）。其中后两者可以没有。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJO4bkaFibqeX0m7URmTUwjPt6j2cPuVVxvp4vtLq1Hnm9q9VaBGKwwFmw/640?wx_fmt=png&from=appmsg)

**图2****用户输入**

算法1是利用MD生成numSamples个prompt，再利用自定义评分机制选出最好的 prompt，该 prompt 即为用于生成的提示词。

其中 APInstruction 为："Please summarize the above information in a concise manner to describe the usage and functionality of the target”。用于和 userInput 组合成给 MD的提示词。

temp 参数表示温度，温度越低随机性越低，会使LLM倾向于给出它认为更正确的答案。

评分机制是对于得到的所有candidatePrompt做小规模的实验，统计每个prompt条件下生成模型产生的有效代码段个数。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJO7JdUaGQas303jFfjrFRdBPwqLgt4HwvC5ATaOIjJK7Btwqq0jVTs8Q/640?wx_fmt=png&from=appmsg)

**图3 算法1**

下面是Autoprompting算法的输入输出示例。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJOAYyzEzrULht4icojpq937VMJtuhibh7oXQGmmrCObialov1PkVI0J8xfA/640?wx_fmt=png&from=appmsg)

**图4****Autoprompting 输出**

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJOgiaznoibz59as0NNGbvtcbhw6qAwY5OSYZ5YFN7pOsmibXltam6m6PGng/640?wx_fmt=png&from=appmsg)

****图5********Autoprompting 的输入原文档****

**2.Fuzzing Loop**

Fuzzing loop 中使用了生成大模型 MG, 在实验中是StarCoder。

Fuzz4All的fuzzing loop 基本沿用传统模糊测试工具的方法。先通过蒸馏得到的提示词生成初始种子，然后在每一轮循环中从已有的种子序列中选取一个来进行变异，得到新的输入，用于对目标编译器进行测验。

Fuzz4All中种子的保留策略是**只保留那些被目标编译器认为是有效的样例**。

Fuzz4All的变异方法是利用大模型基于不同的生成指令（instruction）和Automprompting得到的生成提示词提供的背景信息，对于选取的种子（sample）做变异。即**拼接三者生成提示词**，然后进行生成。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJO3KgwQyic0xV3jfpoweGvjbPuxTQ04iahPgGDiaPEhiapuPSWCC6ucbk0zA/640?wx_fmt=png&from=appmsg)

**图6 算法2**

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJOAxoRGUBybIib72uqQ9prsEZbQuxONXHZDBOMzaxibQcPMKOutPeDFgBw/640?wx_fmt=png&from=appmsg)

****图7******不同生成策略对应的指令**

**五、实验**

我们对Fuzz4All进行以下研究问题的评估：

**RQ1**：Fuzz4All与现有的模糊测试工具相比如何？

**RQ2**：Fuzz4All在对特定语言特性的模糊测试方面的有效性？

**RQ3**：不同组件如何影响Fuzz4All的有效性？

**RQ4**：Fuzz4All找到了哪些现实世界的漏洞？

**1.与现有模糊测试工具的比较**

在与基线工具的比较中，Fuzz4All均取得了最高的覆盖率。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJOX4W6MGddesz6PF4tLWx4QJIElTiavDl7YEyMaxH9dCyoyU0ibvGosMyg/640?wx_fmt=png&from=appmsg)

**图8****基线工具和目标编译器及版本**

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJOJYVFpaoibWW470ZiakicEnAjXUdia3k5lWyyaymImWK4AVibtKvYngicHbjQ/640?wx_fmt=png&from=appmsg)

****图9******24小时覆盖率比较**

**2.针对特定语言特性的模糊测试**

实验表明，在指定目标特性的情况下，Fuzz4All所生成的多数测试样例都包含了该特性。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJOQmkLsBmRexGGoibLlxHg7ZEaibEjnIEVVrDYtricXWEntvV42jO4P0d3A/640?wx_fmt=png&from=appmsg)

****图10********目标模糊测试中生成用例对目标特性的阳性率****

**3.不同组件的消融实验**

消融实验表明Fuzz4All对于模糊测试的有效性均有正面贡献。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJOUhpywshHW0fkAmzThwn9AdQ23630BJfqdMITdIxiceWoWVLVFWDKk6w/640?wx_fmt=png&from=appmsg)

****图 11 消融实验****

**4.Fuzz4All找到的实际漏洞**

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRloOTsteP0rHIUlZqrVY6nJOlQRSB7PXwDibTblWJMNib720hU3PlfvpTqMOZcic1w3GPkBEA4IlSw0fg/640?wx_fmt=png&from=appmsg)

******图 12************Fuzz4All发现的漏洞列表******

**六、对有效性的威胁**

内部威胁主要来自**Fuzz4All的实现**。为了解决这个问题，我们进行了代码审查和测试以确保正确性。此外，我们尽可能地从它们提供的复制包中运行每个基准线。

外部威胁主要来自**我们的评估目标**。为了支持我们的普遍性声明，我们将Fuzz4All应用于六种不同语言的九个不同SUTs上。此外，为了考虑长时间模糊测试运行中的差异，我们重复了24小时的模糊测试活动五次，并检查了是否存在统计上显著的结果。由于生成LLM利用了其在最近一年内进行的训练中获得的知识，因此在未来重新应用具有本文中使用的LLM（StarCoder）的确切检查点的Fuzz4All可能会降低其效果，因为数据偏移。Fuzz4All可以通过自动提示步骤来缓解这一问题，其中更及时的文档/示例代码使模型也能生成最新的模糊测试输入。另一个威胁来自使用精馏LLM生成初始输入，其中LLM可能会“产生幻觉”，即产生虚构或不准确的信息。这种限制是大多数使用LLM的流水线共有的问题，我们希望在未来的工作中解决这个问题。

**七、结论**

我们介绍了Fuzz4All，这是一个利用LLMs支持通用和有针对性地对接受多种编程语言的任意SUTs进行模糊测试的通用模糊测试工具。Fuzz4All使用一种新颖的**自动提示阶段生成简明地总结用户提供的输入的输入提示**。在其模糊测试循环中，Fuzz4All通过代码示例和生成策略的迭代更新初始输入提示，旨在**生成多样化的模糊测试输入**。对六种不同语言的九个不同SUTs的评估结果表明，与最先进的工具相比，Fuzz4All能够显著提高覆盖率。此外，Fuzz4All能够检测到98个漏洞，其中64个被开发人员确认为以前未知的漏洞。

##

**参考文献**

[1]2021. Qiskit/Qiskit. https://github.com/Qiskit/qiskit.

[2]2023. std::expected. https://en.cppreference.com/w/cpp/utility/expected.

[3]Cornelius Aschermann, Tommaso Frassetto, Thorsten Holz, Patrick Jauernig, Ahmad-Reza Sadeghi, and Daniel Teuchert. 2019. NAUTILUS: Fishing for Deep Bugs with Grammars.. In NDSS.

[4]Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji, Tiezheng Yu, Willy Chung, et al . 2023. A multitask, multilingual, multimodal evaluation of chatgpt on reasoning, hallucination, and interactivity. arXiv preprint arXiv:2302.04023 (2023).

[5]Patrick Bareiß, Beatriz Souza, Marcelo d’Amorim, and Michael Pradel. 2022. Code Generation Tools (Almost) for Free? A Study of Few-Shot, Pre-Trained Language Models on Code. CoRR abs/2206.01335 (2022). https://doi.org/10.48550/arXiv. 2206.01335 arXiv:2206.01335

[6]Marcel Böhme, Cristian Cadar, and Abhik Roychoudhury. 2020. Fuzzing: Challenges and reflections. IEEE Software 38, 3 (2020), 79–86.

[7]Marcel Böhme, László Szekeres, and Jonathan Metzman. 2022. On the reliability of coverage-based fuzzer benchmarking. In Proceedings of the 44th International Conference on Software Engineering. 1621–1633.

[8]Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. 2020. Language Models are Few-Shot Learners. arXiv:2005.14165.

[9]ébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. 2023. Sparks of artificial general intelligence: Early experiments with gpt-4. arXiv preprint arXiv:2303.12712 (2023)

[10]Alexander Bulekov, Bandan Das, Stefan Hajnoczi, and Manuel Egele. 2023. No Grammar, No Problem: Towa...