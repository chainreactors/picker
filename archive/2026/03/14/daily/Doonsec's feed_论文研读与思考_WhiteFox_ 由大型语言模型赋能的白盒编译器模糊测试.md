---
title: 论文研读与思考|WhiteFox: 由大型语言模型赋能的白盒编译器模糊测试
url: https://mp.weixin.qq.com/s/PMZmSnDPpEpVVtM4qJ5a4A
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:27:09.824643
---

# 论文研读与思考|WhiteFox: 由大型语言模型赋能的白盒编译器模糊测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIyibueq5rbGMgBDuaeTlU9IyeaRoUM5iaHb3QEfwG00DibRnFNCMzbJnGsvccZbicJTkbibiaDL7sfxo7EuHyzeEUMhCFWm5U2sYwIZY/0?wx_fmt=jpeg)

# 论文研读与思考|WhiteFox: 由大型语言模型赋能的白盒编译器模糊测试

Bian
Bian

玄枢战队-Arcane Hub

![]()

在小说阅读器中沉浸阅读

*原文标题：**WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models*

*原文作者：**Chenyuan Yang, Yinlin Deng, Runyu Lu, Jiayi Yao, Jiawei Liu, Reyhaneh Jabbarvand,and Lingming Zhang*

*原文链接：**https://doi.org/10.1145/3689736*

*发表会议：**Proceedings of the ACM on Programming Languages, Volume 8, Issue OOPSLA2. Article No.: 296, Pages 709 - 735*

*开源代码：**https://github.com/ise-uiuc/WhiteFox*

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIyrGU1Nnk74hHtA7pvwJVlOuFym05LqxVcRPzwoUlicQp8u2pqaJY5hrYx4x4BGCF4ywtIrjDzmibXljnAfe8MaE1jI4UKmN6e5s/640?wx_fmt=png&from=appmsg)

**一、研究背景、目标和方法**

**1.1****研究背景**

编译器在将高级编程语言翻译为机器码的过程中扮演着核心角色。在现有研究中，模糊测试已被广泛研究以揭示编译器缺陷。然而，由于现代编译器极其复杂，其内部的优化机制如果出现错误，可能会导致程序行为异常、系统崩溃，甚至产生严重的安全漏洞。因此，确保编译器优化的正确性对整个软件供应链的安全性至关重要。

传统的模糊测试挖掘编译器缺陷的技术方案仍面临挑战，在检测漏洞与效果上存在显著局限性：

1) **黑盒模糊测试（Black-box）**：由于完全不了解编译器内部逻辑，生成测试程序时具有盲目性，难以满足触发深层优化所需的复杂特定条件。

2) **灰盒模糊测试（Grey-box）**：虽然利用代码覆盖率作为反馈，但往往仍无法理解触发特定优化所需的精细标准，且容易生成语义无效的输入。

3) **传统白盒测试（White-box）**：理论上可以探索所有路径，但面对现代编译器数百万行的庞大代码量，会遭遇“路径爆炸”问题，且难以对复杂的内部数据结构建模，在实际应用中几乎不可行。

由于大型语言模型（LLMs）在代码生成和理解任务中表现出色，根据相关研究已在黑盒模糊测试中取得了显著成果，然而，如何利用LLM直接深入理解编译器的源代码信息，并以此指导测试生成的“白盒”研究领域仍处于空白状态。因此本论文提出了首个利用大型语言模型结合源代码信息的白盒编译器模糊测试工具WhiteFox，专注于检测新兴深度学习（DL）编译器中的深层逻辑错误。

**1.2****论文提出的关键方法**

现有的白盒测试方法无法扩展到对复杂编译器系统的行为信息进行建模，WhiteFox的核心思想是利用LLMs自动推断能够触发编译器优化的测试程序需求，这些需求基于优化模块的源代码实现。

WhiteFox采用多智能体框架，将测试过程分为理解与生成两个阶段，如图1为WhiteFox的模型框架。该框架主要包含三个核心组件：基于LLM的分析智能体，基于LLM的生成智能体与反馈循环。

1)基于LLM的分析智能体通过将受测编译器中优化pass的源代码作为输入，使用少样本上下文学习生成以自然语言和伪代码的混合格式组成的触发优化需求。

2)基于LLM的生成智能体则根据提取的需求，使用少样本上下文学习自动生成用于触发优化的测试程序。

3) 反馈循环负责对生成的测试程序被编译和执行后，通过插桩观察优化是否被触发，并将成功触发优化的测试纳入反馈机制，通过汤普森采样选择高质量测试程序作为示例，指导生成型LLM在后续迭代中生成更具优化针对性的测试程序。

值得注意的是，WhiteFox采用了多智能体框架，这种设计能够平衡不同 LLMs 提供的成本和收益之间的权衡，可以让分析LLM具备广泛的知识和推理能力（在自然语言和代码方面），而让生成LLM专门用于高效的程序生成。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIxYI7MHl2dicOpRRVRhwGsCPGuGXnxibXPVGohHvJ7l0V4tCI6ONaLl3Glib9SAPL0O0qTbwgribmhj8723W9A4qNKfE08jicA5ick4w/640?wx_fmt=png&from=appmsg)**

图1 WhiteFox模型框架

**二、具体方案设计与理论研究**

**2.1****需求总结**

WhiteFox的输入是实现编译器优化的源代码，而优化源代码往往包含大量实现细节（如数据结构操作、错误日志记录），并且实现代码往往是低级别的，涉及复杂的数据结构，大量的领域特定模块、IR和辅助函数，某些源代码还可能会超出LLM可用的有限上下文窗口。直接使用LLM从优化源代码生成测试效果不佳，增加了LLM理解的难度。

WhiteFox的解决方案是采用了一种混合格式，将自然语言（NL）和伪代码结合起来描述触发优化的需求，而不是仅仅依赖其中一种格式。其中自然语言用于描述复杂的数值约束、张量维度要求或难以用代码表达的逻辑条件。例如，PyTorch Inductor中的permute\_linear\_fusion优化要求“它交换了张量的最后两个维度”，这里使用自然语言描述更加适合。而伪代码用于表达关键代码模式，使测试生成更直观。例如，PyTorch Inductor中的permute\_linear\_fusion优化要求“首先调用张量方法permute，然后在置换后的张量上调用torch.nn.functional.linear函数”。对于这种情况，自然语言描述不如伪代码格式直观，“张量方法permute”可以用伪代码简单地表示为input\_tensor.permute(...)。这种混合格式为分析大型语言模型提供了更大的灵活性，而不是仅仅依赖于任何一种格式，可以根据需要为每个需求组件使用NL或伪代码，从而产生更具表现力和更高质量的摘要。

在具体实现中，WhiteFox首先利用分析LLM来推断可能触发优化的、高层输入的需求，该优化利用其以底层源代码编写的实现。更具体地说，对于每个优化，我们使用少样本上下文学习来提示分析LLM，以混合格式（NL和伪代码）生成其对输入的触发要求。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIw8mr2iahssCpYrakEAa3KRibd1QKKGJKdTxGEr5uwYvYrUib4MjW8RR6KPOyJVOrQ81d67sQYTwxOz5ufibxVGkTBjh1BUzibFlUb8/640?wx_fmt=png&from=appmsg)

图2 WhiteFox的需求总结提示模板

图2(a)展示了用于总结目标编译器中优化需求的通用少样本提示模板。该提示模板以指令“请描述可以触发[OPTIMIZATION NAME]优化的[TARGET INPUT]...”开头，其中[TARGET INPUT]是目标编译器特定的输入格式。然后，它后面跟着优化实现的源代码，并以输入应满足的需求描述结束。描述是自然语言和伪代码的混合格式，由[PSEUDO CODE]和[NL DESCRIPTION]组成。Target Optimization与少样本示例具有相同的结构，但其需求字段留空，等待LLM生成。

图2(b)展示了PyTorch Inductor中的需求总结少样本提示。PyTorch Inductor的预期输入格式是PyTorch模型；因此，[TARGET INPUT]填充为“PyTorch模型”。随后，提供了示例优化permute\_linear\_fusion的源代码。最后，以伪代码和自然语言混合格式给出示例描述，以概述触发示例优化所需的约束条件。

从数学公式上来表述，设P𝐴为分析LLM，它对token序列的概率进行建模。它将以下类型的信息作为输入：(i)𝐼𝑖，关于总结优化𝑂𝑖的指令；(ii)𝐶𝑖，𝑂𝑖的源代码实现；(iii)𝑅𝑖，优化𝑂𝑖的总结触发模式或需求。设𝐸𝐾为由𝐾个示例优化组成的少样本提示前缀：𝐸𝐾=(𝐼1, 𝐶1, 𝑅1)◦(𝐼2, 𝐶2, 𝑅2)◦...◦(𝐼𝐾,𝐶𝐾,𝑅𝐾)。设𝑂𝑡为目标优化。生成的requirement𝑅𝑡的概率分布可以定义为P𝐴(𝑅𝑡|𝐸𝐾,𝐼𝑡,𝐶𝑡)。

**2.2****测试生成**

通过利用优化的需求描述，WhiteFox利用LLM的能力生成能够有效触发相应优化以进行错误检测的测试输入。与需求总结类似，论文利用少样本上下文学习来生成基于需求的特定于每个优化的测试输入。

图3(a)展示了WhiteFox中用于测试生成的通用提示模板。少样本示例的结构包括一条指令，具体为：“请生成一个有效的[TARGET INPUT]示例，该示例具有[INPUT SPECIFICATION]并满足指定的需求。”然后，它详细说明了激活优化的需求，并以一个说明性输入结束，该输入实践了示例优化。在少样本示例之后，目标优化具有相似的结构，而其测试输入将由 LLM 生成。

图3(b)展示了在PyTorch Inductor中使用的测试生成提示。PyTorch Inductor的测试输入格式是一个使用公共PyTorch API（[INPUT SPECIFICATION]）PyTorch模型（[TARGET INPUT]）。接下来，指定激活优化permute\_linear\_fusion的测试输入需求，辅以一个可以触发此优化的说明性模型。提供的少样本示例帮助 LLM 以所需格式生成测试。此外，示例可以帮助LLM学习优化需求描述与能够触发它的相应测试输入之间的关系。

**![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwFiaAX8AzVTp7BecyS24iaxISsMaMC9SiadZxb5GgR2dxVibnic0lhm7sDVhNm1CYaTPWc9J5PIrZrYYxeiaVa7L3PR7fSR4YlE0noo/640?wx_fmt=png&from=appmsg)**

图3 WhiteFox的测试生成提示模板

从公式上来理解，令P𝐺为生成LLM，其对token序列的概率进行建模。回顾一下，𝐼代表摘要指令，𝑅表示触发优化的需求。令𝐸𝐾为少样本提示前缀，其由𝐾个示例优化组成：𝐸𝐾 = (𝐼1, 𝑅1,𝑇1) ◦ (𝐼2, 𝑅2,𝑇2) ◦ . . . ◦ (𝐼𝐾, 𝑅𝐾,𝑇𝐾 )，其中𝑇𝑖是触发优化𝑂𝑖的有效测试输入。令𝑂𝑡为目标优化。生成的测试𝑇𝑡的概率分布可以定义为P𝐺 (𝑇𝑡 | 𝐸𝐾, 𝐼𝑡, 𝑅𝑡 )。

**2.3****反馈循环**

虽然图3中的提示包含来自同一被测编译器的示例优化（及其触发测试），但这些少量示例缺乏针对目标优化的具体指导。引入反馈循环的动机是在每次迭代中，当发现新生成的测试能够触发目标优化时，将其收集为未来测试生成提示的少样本示例候选。通过将这些成功触发优化的测试纳入提示中，可以增强对生成型LLM 的针对性指导，使其能够生成更多触发目标优化的输入。

在具体实现中，WhiteFox在迭代测试生成过程中将成功触发相应优化的测试作为补充示例纳入其中。

（1）**执行测试，检测优化是否触发：**生成的测试程序会被编译并执行，通过插桩记录优化触发情况。若优化被触发，则该测试程序被标记为“少样本示例候选”，并用于后续针对该特定优化的测试生成迭代。

（2）**构建反馈提示：**每次迭代中，如果当前优化有触发输入，WhiteFox 会选择几个触发输入作为示例（默认为 3 个），这些示例触发输入将与目标优化的指令和需求总结（与之前的提示相同）一起插入到图4所示的提示中，并用于生成下一批测试输入；如果某个优化没有触发输入，WhiteFox 将在后续迭代中继续使用初始提示（图3），直到找到能够触发该优化的输入为止。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIwZPicDoZAsO4fspDaNIx4DxkB3iboAs6mznIpHTueWvKtnmnrUaz6TjYOibeiaCd2hxlD17PWwyiauy6CIjTKX1poSicdUeYeFIgOyc/640?wx_fmt=png&from=appmsg)

图4 加入反馈循环的测试生成提示模板

由于并非所有触发示例在引导LLM生成新的有价值的触发测试方面都同样有效，评估其有效性的一个有用信号是当使用它们作为少样本示例时的新生成测试的触发率。为了有效地选择具有不断发展的示例有效性知识的触发示例，WhiteFox 采用了一种（经过调整的）多臂老虎机（MAB）算法，即Thompson采样，作为触发示例的选择策略，以平衡利用和探索之间的权衡。

beta分布由两个形状参数α > 0, β > 0参数化，它们表示历史试验中成功和失败的次数，beta分布的概率密度函数可以正式写成如下：

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwE1PpFdyLoq04mf2hQIkuZ2DCsK7VlmLrxp6s2mibOVtvHEic0fTOKUos0XPzBcP3FS4e6QNfFcy5JmfiaofLWpkS7Y4hLcunoag/640?wx_fmt=png&from=appmsg)

其中B(α, β)是一个用于归一化的常数。当没有任何关于臂的先验信息时，选择标准beta分布B(1, 1)（或等效的Uniform(0, 1)）作为其先验分布。在抽取新样本并观察奖励（如果生成的测试成功触发目标优化则为1，否则为0）后，可以通过将α或β增加1来方便地更新后验概率，具体取决于样本是成功还是失败。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwrsag1k3xyULHstaatTua1EWFuntzUXALpMf7XEicRdpoz5DwT2BGIgDaesoMGIgImufdo1M5h3XpCBwUHibYgruCBTcoJXfwyk/640?wx_fmt=png&from=appmsg)

图5 样本选择算法

图5展示了示例测试选择过程：

（1）从每个后验分布采样θₜ（行2-3）；

（2）选择采样值最高的前N个臂作为本轮ExampleTests（行4）；

（3）用触发测试数量更新ExampleTests后验（行7-9）；

（4）基于ExampleTests的α、β均值初始化NewTriggerTests以减少探索开销（行10-14），假设新测试从“父”示例继承了有效代码模式；

（5）更新触发测试池（行15）。

**2.4****测试预言**

生成的测试程序最后会通过差异化测试来检查正确性，在WhiteFox中，错误表现为以下症状：

1）结果不一致：编译优化传递可能因逻辑缺陷导致错误编译，产生语义不一致的机器代码，这种不一致可以通过差异测试来检测。具体来说，对于每个可编译和可执行的测试程序，在给定相同的输入集的情况下，交叉检查优化版本和非优化（或最小优化）版本的程序生成的输出。

2）崩溃：让编译器和编译后的可执行文件意外崩溃是不可取的。因此，WhiteFox积极捕获测试程序在编译时和运行时的崩溃信号，包括进程中止、段错误和意外的内部异常（例如PyTorch中的INTERNAL\_ASSERT\_FAILED）。

总结来说，论文以两种模式编译每个测试输入：启用优化和不启用优化。将以下条件视为潜在错误候选：

•在优化编译或优化程序执行期间发生崩溃。

•两种模式之间的编译状态（通过/失败）不一致。

•两种模式之间的程序输出不同。

通过这种结合了“白盒知识总结”与“动态反馈优化”的设计，WhiteFox能够精准地触达编译器中那些极难被黑盒测试触发的深层优化逻辑。

**三、论文使用的研究方法及相关证明**

**3.1****实验设置与实现**

**（1）实验环境**

Ubuntu 20.04.5 LTS，配备 64 核 CPU、256 GB 内存和NVIDIA RTX A6000 GPU。

**（2）实验模型与设置**

**分析和生成LLMs：**（1）利用 GPT4 作为分析LLM，并将温度设置为0。（2）利用StarCoder（StarCoder-15B）作为生成LLM。在每次迭代中，让StarCoder生成一批十个测试输入，并将温度设置为1。

**被测编译器**：三个最流行的深度学习（DL）编译器：PyTorch Inductor、TensorFlow Lite和TensorFlow-XLA（对于 TensorFlow-XLA，由于其优化实现通常较长，仅选择了代码行数少于 400 行的优化，这是由于 LLM 上下文窗口大小的限制）。表 1 列出了被测 DL 编译器的概述。

表 1 被测DL编译器的细节

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIycuC2kC1BKcrIg8eEnoUWlE5fsR6UIqRZAjUbn5y3kRD65Bb6fdpQAlvnU15qy1tc4ibWESTpd5er82VwcD5nYjyaqPeIyGuM4/640?wx_fmt=png&from=appmsg)

**少样本提示**：对于每个目标编译器的需求总结和初始测试生成的少样本提示，论文选择一次性提示，从每个目标编译器中选择一个优化，手动编写需求描述和一个能够触发优化的演示输入测试。一个例外是PyTorch Inductor有两种不同类型的优化（7种使用传统的优化检查函数，54种涉及模式匹配器）。因此，为每种类型分别设计两个提示，并根据优化类型为每个优化选择相应的提示。

**模糊测试预算**：默认设置为每个优化生成总共1000个测试，分为100次迭代。

**3.2****数据收集方法与数据集特点**

本文通过指定相关目录来收集特定优化的编译器源代码。PyTorch Inductor的优化传递源代码位于`torch/\_inductor`目录下，T...