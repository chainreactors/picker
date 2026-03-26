---
title: 论文研读与思考|CKGFuzzer：基于代码知识图谱的 LLM 驱动的模糊测试驱动程序生成
url: https://mp.weixin.qq.com/s/o7L9dZQuzcOV1umQJiPBMA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:25:57.361589
---

# 论文研读与思考|CKGFuzzer：基于代码知识图谱的 LLM 驱动的模糊测试驱动程序生成

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIxNB9e603LoaqNfLHUiaD82niaRDicJhR6OT0IlG2fvXp0xv0m0AI9gCiazRfBHp5o473KR74aaUWTrFCyXoOTGCJ40T0hniabLEFmE/0?wx_fmt=jpeg)

# 论文研读与思考|CKGFuzzer：基于代码知识图谱的 LLM 驱动的模糊测试驱动程序生成

Bian
Bian

玄枢战队-Arcane Hub

![]()

在小说阅读器中沉浸阅读

原文标题：CKGFuzzer: LLM-Based Fuzz Driver Generation Enhanced By Code Knowledge Graph

原文作者：Hanxiang Xu, Wei Ma, Ting Zhou, Yanjie Zhao, Kai Chen, Qiang Hu, Yang Liu, Haoyu Wang

原文链接：https://dl.acm.org/doi/10.1109/ICSE-Companion66252.2025.00079

发表会议：2025 IEEE/ACM 47th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion), pages 243-254.

开源代码：https://github.com/security-pride/CKGFuzzer

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIx5pYcALT20FWnZVmllGUIMkqIrPGDoSCup4fNmw9WuEdQGDnYMkcOOx7AtAsFw1s9jjalm2tibUhiamlYZmsg6ZXlfTvesQnzPE/640?wx_fmt=png)

一、研究背景、目标和方法

1.1 研究背景

模糊测试是漏洞挖掘与软件可靠性保障中的核心技术，但在面向库API的场景中，其效果高度依赖fuzz driver的质量。传统工具如AFL、libFuzzer虽然成熟，但fuzz driver往往需要人工编写，这会带来两个直接问题：其一，人工成本高，难以覆盖大型代码库中大量接口；其二，测试逻辑容易停留在会调用API层面，却难以捕捉API之间的真实使用关系、依赖顺序和上下文约束，导致生成的driver质量不高、覆盖率有限。

近年来，大语言模型在代码生成、修复、总结和推理方面表现突出，因此研究者开始尝试把LLM引入模糊测试。然而，现有LLM-based fuzzing工作往往更多依赖提示工程、少样本示例或随机API组合，对目标程序内部结构的利用仍然不足。具体而言，已有方法通常难以系统建模以下问题：一是API之间的调用关系与语义关联；二是fuzz driver编译失败后的自动修复；三是初始输入种子如何结合API用法生成；四是崩溃究竟来自fuzz driver误用API，还是来自库本身的真实缺陷。

1.2 研究目标

CKGFuzzer的目标是把fuzz driver生成视为一个由知识驱动的代码生成任务，通过构建代码知识图谱（Code Knowledge Graph,CKG），再配合多智能体 LLM系统，实现fuzz driver自动生成、编译报错自动修复、输入种子初始化、覆盖率引导下的API组合变异，以及崩溃原因自动分析，从而形成一条端到端、尽量减少人工介入的自动化fuzzing流程。

1.3 论文提出的关键方法

CKGFuzzer是一个将多智能体系统与代码知识图谱相结合的模糊驱动器生成框架，其目标是针对API组合生成高效的模糊驱动器，以提升模糊测试的质量和覆盖率。论文将CKGFuzzer的整体流程概括为“代码知识图谱抽取→API组合生成→fuzz driver生成→动态编译修复→输入种子初始化→fuzzing执行→ 覆盖率引导变异→崩溃分析”的闭环，图1展示了CKGFuzzer的工作流程，由3个主要组件和一个独特的反馈循环机制组成。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIw8PcsAiavCR9y5A6OUa6vogicpeia4Nm7FTV37x3UJlkWXCjWpicNr9aqzf8M2hKKp3QSO7JS0wTE5I1kB02unLQJSBCTYqrrwJug/640?wx_fmt=png)

图1 CKGFuzzer工作流程

1)CKGFuzzer解析被测目标及其库API，提取并嵌入代码知识图谱，包括解析抽象语法树，提取数据结构、函数签名、调用关系等关键信息。

2)查询代码知识图谱的API组合，关注那些具有调用关系的API，生成相应的模糊驱动器。

3)编译生成的模糊驱动器，并且通过一个动态更新的库使用情况，修复出现的编译错误。

4)执行编译成功的模糊驱动器，监控库文件的代码覆盖率，对未能覆盖的新路径API组合进行变异，迭代该过程并持续进行。

5)使用链式推理分析在模糊测试过程中产生的崩溃，参考包含了真实CWE相关的源码示例，来验证这些崩溃的有效性。

二、具体方案设计与理论研究

2.1 代码知识图谱构建机制

代码知识图谱是本文的基础创新之一，作者首先利用语法解析器与静态分析工具，从目标仓库中抽取函数、文件、函数签名、源代码、摘要、调用关系等信息。在形式化表示上，论文把函数集合记为F={f1,f2,…,fN}，文件集合记为 D={d1,d2,…,dM}，调用关系记为C={(fi,fj)|ficalls fj}，并将函数摘要记为S: fi→sfi。

在图谱构建过程中，系统会：首先创建空属性图G=(V,E)；然后为每个函数创建节点，节点属性包括函数签名、文件路径、源代码和函数摘要；再为每个文件创建节点，并通过CONTAINS边把文件与其包含的函数连接起来；对于函数间调用关系，若被调者属于当前仓库，则建立CALLS边，若为外部库函数，则建立 LIBRARY FUNCTION节点与LIBRARY CALLS边。这样构建出的图谱，不仅能表达“某函数存在”，还可以表达“它在哪个文件里、会调用谁、上下文是什么”。

论文还特别强调了双索引设计：由于代码片段与自然语言描述位于不同的嵌入空间，若使用单一向量索引，查询质量会受到影响。因此作者分别为自然语言和代码构建属性图索引PGI\_NL与PGI\_code。这个设计很关键，因为后续查询既可能来自自然语言提示，也可能来自API代码上下文。

2.2 API组合生成

API组合生成是CKGFuzzer优于简单LLM fuzzing的关键所在。因为库函数虽然可以独立调用，但很多真实使用场景需要多个API协同完成。如果组合不合理，生成的fuzz driver即使通过编译，也往往无法深入到有意义的代码路径。

作者把这一过程表述为一个检索增强生成（RAG）式流程，主要包括索引、检索和响应综合三个阶段：先对知识图谱进行切块和嵌入，形成可检索索引；然后把“目标API的相关接口有哪些”这类查询向量化，与索引中的图谱块计算相关性；最后把检索到的若干高相关块按顺序送入LLM，通过逐轮refinement的方式整合信息并过滤噪声，生成最终API组合。这一策略比随机组合更有针对性：它利用图谱中的调用关系、文件归属与语义摘要，帮助系统从局部 API扩展到功能相关API集。也就是说，CKGFuzzer不是让LLM盲目拼接接口，而是让其在结构化知识的约束下推断出更接近真实使用模式的调用组合，API组合生成的算法如图2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxO3Zia1oAzibNHu04ibVV1vKQeQdLXCibdRLNXW1tpdDQLMh0XP6LBNKiaqZtIJfAWqECJBza5A6icLQzQc1cZ7OwdVQbIepQlFHS90/640?wx_fmt=png)

图2 API组合生成

在索引阶段（行1-行2），代码知识图谱通过嵌入模型拆分成更小的块，每个分块代表图内容的一个子集，请求也按相同的嵌入模型进行转换。在检索阶段（行3-行4），通过向量检索匹配相关的分块，确保检索到最相关的信息以形成响应。在响应合成阶段（行5-行7），初始化分块查询答案，提示大模型逐步整合有用的剩余分块，迭代该过程直到所有检索的信息处理完成，最终输出一组与目标功能相关的API集合。

2.3 Fuzz Driver生成机制

在获得API组合之后，系统采用基于角色提示（role-prompt）的生成策略来编写fuzz driver。提示中不仅要求在LLVMFuzzerTestOneInput函数中调用所有相关API，还会提供API源代码、头文件信息以及自然语言摘要，从而帮助 LLM理解每个接口的入参与输出约束。论文特别强调了错误处理与内存管理要求，因为如果fuzz driver本身不稳定，就会把大量驱动缺陷误当作目标库缺陷，降低fuzzing效率。

作者还提到使用memory mechanism对生成过程进行迭代增强，即在逐步处理更多API上下文的同时改写和细化初始输出。从本质上看，这里是把一次性代码生成改造成了带上下文累计的多轮生成过程。

2.4 动态程序修复

由于LLM生成代码常伴随幻觉、语法错误与API误用，论文设计了专门的动态程序修复模块，系统的动态修复机制如图3所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIwKWtgL9AGqGHfOt9LhF3GibpEBxD1Uict56icuuAjJlpMwvqMWz3K7heC5EzBGmK89wiaUdQAvgicD8GVygKcss4pCicLBTdMtKvWgE/640?wx_fmt=png)

图3 模糊驱动器修复

其流程是：先用OSS-Fuzz中的已有fuzz driver样例和库头文件初始化一个正确API用法知识库（行2）；对每个生成driver尝试编译；若编译失败，则提取编译器错误信息，构造查询，在知识库中检索相似正确用法（行11-行13）；随后由 LLM参考这些正确案例修补当前driver；直到编译成功或者达到最大迭代次数（行5和行15）。

更进一步，系统会把成功编译的fuzz driver再次回灌到知识库中，形成一个动态增长的正确用法仓库（行7-行9）。这样做有两个好处：一是后续修复可利用更贴近当前库的样例；二是系统在同一轮实验中具备逐渐学会如何正确写该库driver的能力。

2.5 Fuzzing循环：输入种子初始化与覆盖率引导变异

论文认为，仅生成driver还不够，输入种子同样决定fuzzing是否能够快速进入有效路径。CKGFuzzer的模糊测试循环旨在通过迭代优化模糊测试的效果，通过初始化高质量的输入种子，并基于覆盖引导的变异策略来探索新的代码路径，两者的协同工作旨在最大化代码覆盖率并识别新的执行路径。覆盖率引导的变异算法如图4所示。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzGwbGQxriaVO7O0DQVuqpSDiaNG4lt1fib03WoxWHmWjib6HIGduQVIcOsuveHTCjdEIrKIw8sb5IqItIibatNuibusg5f8dtUl4wwc/640?wx_fmt=png)

图4 覆盖率引导的变异

1）输入种子库初始化

首先，CKGFuzzer通过详细分析模糊驱动器的数据流，提取变量之间的值流关系。然后，提取模糊驱动器交互的API函数签名，以了解输入的结构和约束条件。接着，利用这些信息构建LLM的提示，指示其生成能够最大化代码覆盖率、针对边缘情况并探索边界条件的输入种子。最后，存储在输入种子库中的初始输入种子作为模糊测试的基础。

2）覆盖引导的变异

在模糊测试过程中，CKGFuzzer监控每个模糊驱动器的代码覆盖率，并分析整个库的覆盖情况（行3-行8）。对于覆盖率低于库平均水平的文件，提取其定义的API函数，并根据文件的覆盖率生成一个优先级列表，称为低覆盖率API列表（行9）。然后，CKGFuzzer使用这个低覆盖率API列表指导LLM对当前模糊驱动器中的API组合进行变异和重构（行12-行16）。

2.6 崩溃分析机制

为区分fuzz driver误用API与库本身存在漏洞，CKGFuzzer在运行时结合 ASan、UBSan、MSan等sanitizer收集崩溃，再利用一个crash analysis agent 做链式推理。其过程包括：第一步，提取崩溃相关源代码区域，包括fuzz driver 中相关调用与触发路径；第二步，从代码中归纳潜在错误模式，如越界访问、控制流条件异常、不安全内存操作等；第三步，将这些假设与一个CWE漏洞知识库做模式匹配。该知识库包含100多个面向C/C++的真实世界CWE描述以及由LLM生成的示例代码。

这一机制的意义在于，它不只是看到sanitizer报错，而是试图给开发者提供为什么报错、错误更像是误用还是库缺陷的解释性分析。因此，CKGFuzzer在论文中不只是一个driver生成工具，也带有一定程度的自动化triage能力。

三、论文使用的研究方法及相关证明

3.1 实验设置与实现

（1）实验模型

论文使用Tree-sitter解析源代码，以构建和更新语法树；使用CodeQL做更深层的仓库分析，抽取API调用关系和源代码细节；嵌入模型采用BAAI/bge-small-en-v1.5；为了更好处理代码图谱检索，作者虽然使用了LlamaIndex，但又额外实现了自定义RAG引擎。在模型选择上，fuzz driver生成与编译修复任务由DeepSeek-V2-Coder完成，其余agent使用DeepSeek-V2-Chat。

（2）实验环境

硬件环境为Ubuntu 22.04 LTS服务器，配置AMD 64-Core Processor和1TB RAM。Fuzzing平台基于OSS-Fuzz与libFuzzer。实验参数包括：DeepSeek-V2-Coder温度为0.7，DeepSeek-V2-Chat温度为1.0；默认API组合最大长度为6；编译修复最大迭代次数为5；API组合最大变异次数为3；每个库总fuzzing时间为24 CPU小时，每项实验重复5次并报告平均结果。

3.2 数据收集方法与数据集特点

作者选择了8个开源C/C++库作为被测对象：c-ares、cjson、curl、lcms、libpcap、libtiff、libvpx和zlib。之所以选择这些库，是因为它们API使用模式多样、具有代表性，并且在真实软件生态中广泛使用。论文还统计了每个库的分支总数、API数量以及生成的fuzz driver数量，便于横向比较。

3.3 实验结果与评估

（1）与现有fuzzers的比较

表 1 覆盖率评估

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIwicqEbrbRTyTFoW1iased9MibWPVz85VR5zcZsocarJVJSGZcTN1H0MTPT2tDW4cEALeyJ2ulUY9qos5YvKwONwlTOibUkRzPaat0/640?wx_fmt=png)

从总体结果看，CKGFuzzer在8个库中有6个取得最高分支覆盖率，平均相较于现有方法提升8.73%。这说明“代码知识图谱 + API组合生成 + 动态修复 + 覆盖率引导变异”的组合确实提升了生成fuzz driver的有效性。在c-ares、cjson、curl、lcms、libpcap、libvpx等库上，其优势都比较明显，尤其在curl这类接口复杂、使用上下文较强的项目上，知识驱动的API组合更能发挥作用。

（2）消融实验分析

表2 消融实验表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIzOxXyFJibCAl9K1b7tfu3JcN4NGiaZNJQlnmDV6NpT8Oluz83DxnSNodtHOqwic8vH5BXiaHZ79VmIqQceA4cF1mTjjWiaHqMtUTxA/640?wx_fmt=png)

作者围绕三个核心组件做了消融：代码知识图谱、编译修复、覆盖率引导变异。结论比较清晰。首先，用纯文本API知识替代代码知识图谱后，所有库的覆盖率都低于默认版，说明图结构关系信息确实提升了API组合质量。其次，在编译修复方面，完全不修复时平均编译通过率仅57.39%（458/798），仅使用LLM修复可提升到77.19%（616/798），而CKGFuzzer的动态修复机制可达到93.99%（750/798）。这表明：编译错误不是附带问题，而是LLM fuzz driver生成中的主要瓶颈之一。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIwsWf27v0QtpB3iaEM2DJgFc6p5lSTyYcXsVTiaTB0EibeHk6KwdW71bV2MU5zM01zyWiaGA5ZQZxspOlrA9KwuHHvPcicicYlPs1Wak/640?wx_fmt=png)

图5 覆盖率引导消融实验

覆盖率引导变异也展现出普遍正收益。如图5所示，除了cjson和libvpx 由于API数量较少、初始组合阶段已覆盖大部分可能组合，收益相对不明显外，其他六个库都能从该机制中持续获得更高覆盖率。这说明API级别的coverage-guided mutation确实能够把探索重心逐渐推向低覆盖区域，而不是停留在一开始生成的局部组合上。

（3）崩溃分析结果

表3 崩溃分析结果

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxYzJUDvefUwuGzDSGGEJGhMLFgEG0H7qBmwbzLqlVwB41KmnKhNxKibtqIDlTnERuXgWDtVBPmy8vpKVl7ib0llWKKsV9FPmdEc/640?wx_fmt=png)

在崩溃分析方面，论文统计到199个唯一崩溃，其中168个被自动分析模块判定为API misuse导致，31个被归类为需要人工关注的真实bug候选。最终作者确认了11个真实bug，其中9个此前未公开报告。更重要的是，崩溃分析模块将人工审查工作量降低了84.4%。这说明其价值不仅体现在找出更多bug，也体现在减少开发者排查伪阳性的成本。

（4）检测到的真实错误

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwyeaQfgLBFyib1UEomAGfYvgJqIM6cSXkdPY9ln1FuNoUhROvot2Hym7x7UDogXibCAra5DGKt2Fo8kQ7bMn...