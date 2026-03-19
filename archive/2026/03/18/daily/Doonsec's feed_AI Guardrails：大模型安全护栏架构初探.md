---
title: AI Guardrails：大模型安全护栏架构初探
url: https://mp.weixin.qq.com/s/JhhorGnR0ARUuILaIX1i4Q
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:15:57.438272
---

# AI Guardrails：大模型安全护栏架构初探

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ySlic3yZpdpqSrBXZY9bzTrwRAyOOBz7IfL9T3Tnh6t91hd96ESoF59FZibvucIez5ia1nYDpLptA6r0EODDdXejvBaUXEW0LClJTnYybbn2Ms/0?wx_fmt=jpeg)

# AI Guardrails：大模型安全护栏架构初探

elssm
elssm

安全驾驶舱

![]()

在小说阅读器中沉浸阅读

当AI已经能够生成以假乱真的信息、编写恶意代码或无意中放大社会偏见时，我们是否拥有有效的“刹车”系统？随着通用人工智能的曙光初现，构建与之匹配的安全防线，已从一个技术选项升级为一项社会必需。

本文将聚焦AI护栏技术。从AI护栏定义与重要性出发，剖析为何护栏是AI产品化的前提。随后，我们将学习开源社区中四个具有代表性的护栏方案，解码其设计思想与实现逻辑，并总结当前的主要防护技术路径。最后，我们将探讨护栏如何在与AI能力的动态博弈中演进，以护航更安全的智能未来。

**0x00 AI护栏介绍**

AI安全护栏是一种确保大语言模型正常运行、使其行为更加安全的安全保障措施。可以将其视为一套介于大语言模型与用户界面之间的控制措施及技术手段。它们的主要功能是实时拦截、阻止各种风险，并减轻其带来的危害。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdpqEQ6aMjURfQshGibxAIab6pHSMHHRGH5xW6GpjRgvjsdZMxdibw8QkjUMCXElYYhNziaElawW3k6IuPXC5cUL4nSic6KJvJUvSkqA/640?wx_fmt=png&from=appmsg)

图片来源：GeeksforGeeks

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdpoB76IMZdGtVIxzoJ4zU0GTZ04xuwdD2y14uSmEEOdLsE3DT6v5DUcSsScq1RxFjpzODE98g1zGlfADKshRnM2aW9KJVkUicbcM/640?wx_fmt=png&from=appmsg)

图片来源：Guardrails

从图中可以看到，在没有AI护栏的情况下，输入会直接经过大语言模型的处理产生响应输出；在有AI护栏的情况下，AI护栏会持续监控AI系统的输入与输出数据。它们依靠预先设定的规则及算法来识别可能存在问题的内容或行为。通过这种实时监控机制，可以在必要时立即采取干预措施，它们能够确保人工智能系统在预先设定的范围及道德准则内运行。随着人工智能越来越多地被应用于各种关键业务流程，实施完善的防护机制显得尤为重要。这些保护措施就像检查点一样，用于监控、过滤并控制人工智能的输出结果，从而防止出现有害、有偏见或不恰当的回应。可以把这些保护措施比作桥梁上的安全护栏——它们既引导人工智能的行为，又防止其偏离安全的轨道。

**0x01 AI护栏的重要性**

大语言模型及生成式人工智能的迅速普及既带来了前所未有的机遇，也带来了严重的风险。如果缺乏有效的监管机制，大语言模型就有可能产生虚假信息、带有偏见的内容，或者泄露敏感信息。

AI护栏至关重要的主要原因：

● 合规性：满足法规要求，以及新兴的AI监管规定，确保AI技术的合理使用。

● 品牌保护：防止不当的AI输出损害品牌声誉，从而无法维护客户的信任。

● 数据安全：保障AI交互过程中的数据安全，防止敏感信息泄露或遭受攻击。

● 用户信任：确保AI系统在所有交互中的稳定、安全表现，增强用户信任度。

● 成本控制：防止API被过度使用，有效管理计算资源。

**0x02 开源AI护栏调研**

**Llama Guard**

Llama Guard是Meta公司推出的一款AI安全防护工具，核心是帮人机对话过滤危险内容，既检查用户输入，也审查AI输出。

核心概念有以下几点：

安全风险分类体系（Safety Risk Taxonomy）：定义了一套包含六个类别的风险内容分类标准，用于指导内容安全分类器的开发。这六个类别分别是暴力与仇恨、色情内容、枪支与非法武器、受管制或受限制的物品、自杀或自残行为和犯罪预谋。

输入-输出防护（Input-Output Safeguard）：设计了一种机制，用于审查进入大模型和离开大模型的所有内容，不仅要评估用户输入（prompt）的安全性，还要评估AI智能体生成响应（response）的安全性，以防止模型产生违反政策或有害的内容。

指令遵循任务（Instruction-following Task）：将内容安全分类问题框架化为一个指令遵循任务。模型接受包含安全指南、对话内容和输出格式要求的指令，然后生成分类结果。使得模型能够通过更改指令来适应不同的安全策略。

提示与响应分类（Prompt vs. Response Classification）：明确区分了对用户提示和AI响应的分类任务。由于用户和AI智能体在对话中扮演不同角色，对二者的安全评估标准也有所不同。LIama Guard通过在指令中明确任务类型，用同一种模型实现了两种不同的分类。

LIama Guard将安全分类任务解构成一个结构化的指令，该指令包含四个关键要素：

* 安全指南（A set of guidelines）：指令中明确列出需要评估的风险类别及其描述。这使得模型只关注当前任务所定义的风险范畴。Llama Guard使用了定义的六类风险分类体系进行训练，但用户可以在推理时提供新的指南。

* 分类类型（The type of classification）：指令明确指出当前任务是“提示分类”（prompt classification）还是“响应分类”（response classification）。通过指令措辞的简单改变，同一个模型就能处理这两个语义上不同的任务。

* 对话内容（The conversation）：指令包含需要被评估的对话回合，可以是单轮或多轮。

* 输出格式（The output format）：指令规定了模型必须遵循的输出格式。Llama Guard 的输出包含两部分：首先判断为“safe”或“unsafe”；如果为“unsafe”，则需在下一行指出违反的具体风险类别代码（如 O1, O2）。这种格式同时支持二元分类和多标签分类。

下图展示了Llama Guard的提示分类和响应分类任务的指令示例：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ySlic3yZpdpprez8zI8x34Z8HAaJtmmGaD8tjYXciaCvbP2anBQXyJkiaUBhjWVobxSGRkX640BtfxKcVXBt0MibY1UBm1WAZuweicS6iaJmya8ibg/640?wx_fmt=jpeg&from=appmsg)

图片来源：Llama Guard

Llama Guard所依据的训练准则可能与目标领域所需的准则不同。在这种情况下，可以利用大语言模型的零样本或小样本学习能力，使Llama Guard能够适应不同的分类体系及准则要求，从而满足目标应用场景的需求。

零样本提示方法在推理过程中会使用目标领域的类别名称，或者同时使用类别名称和类别描述作为提示信息。

小样本提示方法与零样本提示方法类似，但会在提示信息中为每个类别提供2到4个示例。学习过程是在具体上下文中进行的，也就是说我们并不需要针对这些示例进行专门训练。我们在提示信息中同时包含不安全的示例和安全的示例，其中安全的示例属于难负样本。难负样本是指那些让模型难以与正样本区分开来的负样本。它们通常位于决策边界附近，或者具有与正样本极为相似的特征。因此，在机器学习任务中，人们经常使用难负样本挖掘技术，迫使模型更加关注相似样本之间的细微差异，从而提高模型的识别能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdpowAvc7LKsYzknYAaCBV7ia7mtBMUibqdsQHiabVoI6ALvMsXIwuib3fkDicPLvILuK5tw6AicDL8ZB7O0XickIJJ5OHGiakFGrFpxsk4U/640?wx_fmt=png&from=appmsg)

图片来源：arXiv 2402.01822

**NeMo Guardrails**

NVIDIA NeMo Guardrails 是一款可扩展的 AI 安全防护编排解决方案，旨在确保智能体应用的安全、可靠与一致性。它可用于定义、编排并执行内容安全、主题控制、PII（个人身份信息）检测、RAG 溯源以及越狱防护等防护措施，具备低延迟与无缝集成功能。该方案具备良好的可扩展性与定制性，可与LangChain、LangGraph和LlamaIndex等框架集成，支持多智能体部署，并利用GPU加速实现低延迟性能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdpoAEXsW6M5yz9wcRWlLf1x9rJky7YFpqgGRCHrEUkaZ1X0Fv86nvQ0huPUjTCImaLR31nEaaBstNK6mGJzeuicYJGvjFAz7NoIo/640?wx_fmt=png&from=appmsg)

**图片来源：NVIDIA NeMo Guardrails**

论文提到NeMo Guardrails使用了一个可编程的运行时引擎，该引擎充当用户与大语言模型之间的代理，大语言模型在与用户交互时应当遵循NeMo Guardrails的规则，这些规则用于规定可编程框架的具体使用规范。所使用的的是一种名叫Colang的建模语言。Colang将规则定义为对话流程，大语言模型应当始终遵循这些规则。

Colang脚本片段如下：

```
define flow  user express greeting  bot express greetingdefine flow  user ask math question  do ask wolfram alphadefine flow  user ask distance  do ask wolfram alphadefine subflow ask wolfram alpha  $full_wolfram_query=...  $result = execute wolfram alpha request            (query=$full_wolfram_query)  bot respond with result
```

上述脚本是Guardrails应用程序配置的核心组成部分，Colang脚本的主要组成部分包括：用户输入的标准化格式、对话流程以及机器人的响应格式。这三类数据都会被存储在向量数据库中，从而在为提示生成示例时能够高效地查找最接近的匹配数据。

从上述架构图可以总结出NeMo的工作流程为：

* 用户输入通过服务器或APP传递到NeMo Guardrails运行时
* NeMo Guardrails运行时将用户输入转换为规范形式
* 基于规范形式使用K-NN向量搜索匹配或生成护栏
* 生成最终的机器人响应，并通过动作服务器调用本地或外部工具
* 响应通过服务器返回给用户

![](https://mmbiz.qpic.cn/mmbiz_png/ySlic3yZpdpqk5lWaXVgavS0BfQM7aib3k91LbnqkdFRXpclFnic8vWIHNbI5QRbOtVd2P7DZHgoXDkWUaoVAfqInicOTmlqiamPkM79ROQD0biaU/640?wx_fmt=png&from=appmsg)

图片来源：arXiv 2402.01822

**Qwen3Guard**

现有的安全检测模型虽然在静态评估环境中能够发挥重要作用，但在实际应用中却存在两大局限性：

首先，它们通常只能输出安全或不安全的二分类标签，而这种标签在不同安全标准下的解释方式可能存在差异，因此无法适应不同领域对安全性的不同要求

其次，这些模型在进行安全检测时需要先获取模型的完整输出结果，这与流式语言模型的推理方式完全不兼容，从而无法在模型生成过程中及时发现潜在问题，进而增加了产生有害输出的风险。

Qwen3Guard的核心亮点主要有两个

第一是实时流式检测（Real-Time Detection）：Qwen3Guard-Stream 专为低延迟设计，可在模型逐词生成回复的过程中实时进行内容审核，确保安全性的同时不牺牲响应速度。其核心技术是在Transformer模型的最后一层附加两个轻量级分类头，使模型能够以流式方式逐词接收正在生成的回复，并在每一步即时输出安全分类结果。

![](https://mmbiz.qpic.cn/mmbiz_png/ySlic3yZpdproe9AKG8QkfLXDibKYo3NAMIiaDJ8TbuyHz9ickK5nBT5iaZL8DEjVHxrM4pee6UWxfEmIfLEmgiaTVx7305Bbgk16RQlXw5DncV1o/640?wx_fmt=png&from=appmsg)

图片来源：Qwen3Guard

第二是三级风险等级分类（Three-tiered Severity Classification）：除传统的安全与不安全标签外，Qwen3Guard新增了争议性标签，以支持根据不同应用场景灵活调整安全策略，用户可根据实际需求，动态将争议性内容重新归类为安全或不安全，从而按需调节审核的严格程度。

下图为生成有争议标签的流程。训练数据被分为两部分。对于每一部分，都会使用经过重新加权处理后的样本来训练两个模型，从而生成宽松型与严格型两种预测结果，然后用这些预测结果来对另一部分数据进行处理。最终标签是通过投票方式确定的，那些相互矛盾的预测结果会被标记为“争议性标签”。

![](https://mmbiz.qpic.cn/mmbiz_png/ySlic3yZpdpqzvPFIWLZRT5Xyw1AMzJRw9PdxjgQAf0sBrtof4E6qYXfD5zSkEoVyrayzbPuWjQbfSsia9RvuuZfy2LLW9tuzy6WHnI3SUiaXA/640?wx_fmt=png&from=appmsg)

图片来源：Qwen3Guard

如下方评估所示，现有护栏模型受限于二元标签体系，难以同时适配不同数据集的标准。而 Qwen3Guard 凭借三级风险分类设计，可在“严格模式”与“宽松模式”间灵活切换，在多个数据集上均保持稳健的高性能表现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdpoZw0bYFdSvJ74JSPhthoZJ17FaKpbwOu2OmrsfUAToquB488oF9T7dwIggbuPHrmpdb2ibMGRqXl1HMWvdKgcdu3mibYwfQ8o9w/640?wx_fmt=png&from=appmsg)

图片来源：Qwen3Guard

Qwen3Guard-Stream 的典型工作流程分为以下两个阶段：

（1）提示级安全预检

用户输入的提示（Prompt）将同步发送至大语言模型与 Qwen3Guard-Stream。后者立即对提示内容进行安全评估，并输出对应的安全标签（如“安全”“争议性”“不安全”）。基于该评估结果，上层系统可智能决策：是允许对话继续进行，还是提前拦截以防范潜在风险。

（2）实时逐词安全审核

若对话允许继续执行，LLM 将开始逐词（Token-by-Token）流式生成回复。每一个生成的Token均会实时传递至Qwen3Guard-Stream，由其即时判断当前内容的安全性。该机制实现了贯穿整个生成过程回复的细粒度、不间断内容审核，在不中断用户体验的前提下，动态识别并阻断潜在风险内容。

在论文中还展示了两种典型应用：

* 利用Qwen3Guard-Gen进行安全强化学习（Safety RL）：在不损害模型输出、整体有用性的前提下，显著提升模型的内在安全性

* 利用Qwen3Guard-Stream实现实时动态干预：无需重新训练模型，即可在生成过程中即时拦截风险内容，确保输出安全可控

**OpenGuardrails**

该项目旨在提供一种统一的方法，用于检测大语言模型中存在的不安全内容、被篡改的内容或侵犯用户隐私的内容。它解决了一个许多公司在大规模使用人工智能时都会遇到的问题：如何让安全控制机制能够适应不同的使用环境，而无需每次都重新编写相关系统。

以往的安全系统通常依赖多个模型，每个模型负责处理不同类型的问题，例如提示注入或代码生成滥用等问题。OpenGuardrails简化了这种架构，它使用一个大型语言模型来同时处理安全检测和防御工作。

这种方法有助于系统理解用户的真实意图和上下文，而不仅仅依赖过滤器。此外，它还简化了系统的部署过程，因为企业无需再协调不同的分类器或服务。该模型以量化形式运行，从而将延迟控制在较低水平，使其能够满足实时应用的需求。

OpenGuardrails在技术上的的核心贡献有以下3点：

* 可配置的策略机制（Configurable Policy Adaptation）：受Qwen3Guard报告中的研究结果启发，诸如ToxicChat和OpenAIModeration中采用的不一致的标注标准会导致评估结果的不准确性。为了避免在实际应用中增加人工审核成本，OpenGuardrails允许用户根据自身应用领域的需求来配置“不安全”类别并设置相应的敏感度阈值。防护模型会输出“安全”或“不安全”的判断结果，同时还会提供一个基于首个数据项出现概率计算得出的置信度分数。管理员可以调整系统的敏感度设置（高、中、低三种级别），从而让系统对那些置信度较低的不安全信号更加敏感。这样一来，企业环境中的安全管控就可以实现自动化且更加灵活。

* 基于统一大语言模型的安全防护架构（Unified LLM-based Guard Architecture）：OpenGuardrails证明了仅使用一个大语言模型，就能够实现生产级的内容安全检测及模型篡改行为的识别。与LlamaFirewall等传统系统相比，后者依赖于PromptGuard2这种经过微调的BERT风格分类器，而统一大语言模型方案则具备更强的能力，能够更准确地理解各种复杂攻击手段，并显著简化系统的部署流程。

* 可扩展且高效的模型设计（Scalable and Efficient Model Design）：该模型是在一个拥有140亿个参数的密集型基础模型基础上进行微调的，随后通过GPTQ技术将其参数量减少至33亿个，从而实现了较高的处理效率与并发能力，完全适合实时应用场景。此前的研究很少能开发出参数量超过80亿的模型，同时仍能保持类似的性能...