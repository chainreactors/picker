---
title: 论文研读与思考 | HLPFuzz：基于大语言模型约束求解的混合式语言处理器模糊测试
url: https://mp.weixin.qq.com/s/NlH62oiOylKsAlONDdB4Kw
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:13:34.599376
---

# 论文研读与思考 | HLPFuzz：基于大语言模型约束求解的混合式语言处理器模糊测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIziayxbBicJaIfkYGFZVFCCag8DCLzbSuQbeGIlhrLP2hzlibqE4bfOj3HkmLeAG5CUciaGUpQYCsCkm7OBGHg8Y1a51LJMfZxZYxQ/0?wx_fmt=jpeg)

# 论文研读与思考 | HLPFuzz：基于大语言模型约束求解的混合式语言处理器模糊测试

QIU
QIU

玄枢战队-Arcane Hub

![]()

在小说阅读器中沉浸阅读

原文标题：Hybrid Language Processor Fuzzing via LLM-Based Constraint Solving

原文作者：Yupeng Yang，Shenglong Yao，Jizhou Chen，Wenke Lee

原文链接:https://www.usenix.org/conference/usenixsecurity25/presentation/yang-yupeng

发表会议：USENIX Security 2025

## 一、研究问题、目标与方法

1.1 核心研究问题与研究动机

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIwNhRQNOMJdkicAqtdic0wiblQhe87k3nR61WeU9TGozxOTwibQQPXUPnZhrRR9M8icjETibXY2n5t6Cibe5JYHD31Mn3KcGo7ANlJNZ8/640?wx_fmt=jpeg)

图1：语言处理器多阶段约束流程图

这篇论文关注的是语言处理器fuzzing里一个很典型但又长期没有被很好解决的问题：对于编译器、解释器这类程序，仅靠普通随机变异和覆盖反馈，往往很难真正进入深层逻辑。原因不在于这类程序的代码量单纯更大，而在于它们处理输入时通常存在明显的多阶段结构。一个源程序从进入词法分析开始，要依次通过词法、语法、语义检查，再进入优化、代码生成或执行路径。也就是说，越往后面的代码区域走，输入需要满足的约束就越多，而且这些约束不是并列存在，而是层层叠加的。

论文对现有方案的归纳比较清楚。第一类是taint tracking、symbolic execution、concolic execution这类通用约束求解方法。它们的优势是理论上更通用，不需要针对某一种语言处理器手工写规则，但真正落到编译器和解释器上后，经常会碰到状态爆炸、语义建模不完整、路径过约束等问题。尤其是在tokenization之后，输入字节往往已经被广泛传播到程序状态中，taint 的指导作用会迅速减弱。第二类是目标特化的heuristic方法，例如针对JavaScript引擎或C/C++编译器专门写语义规则的fuzzer。这类方案在特定目标上往往很强，但迁移成本高，很难做到跨语言泛化。第三类是token-level或grammar-level fuzzing，这类方法已经能较稳定地生成语法合法的输入，但主要解决的是前两阶段的约束，对于更靠后的语义依赖、数据关系和执行路径帮助有限。

这篇工作提出的核心判断是：语言处理器fuzzing的真正难点，不只是生成看起来像代码的文本，而是生成“能够跨过特定复杂约束并继续推进执行”的程序输入。作者认为，大语言模型在这个场景里可能有独特价值，因为语言处理器本身消费的就是源代码，模型又具备代码理解、补全和基于上下文推理结构缺失的能力。论文没有把LLM视为通用替代物，而是把它定义为一个专门用来突破复杂约束的求解器，用于在传统fuzzing被路障卡住时继续向前推进。

1.2 论文提出的关键方法、模型或理论框架

围绕这一目标，作者提出了HLPFUZZ。它不是抛弃传统greybox fuzzing，而是在原有fuzzing runtime之外增加一个面向复杂约束的LLM求解模块。整体思路可以概括为：浅层路径仍然由传统syntax-aware mutation去高效探索，只有当系统发现某些未覆盖区域后面存在复杂约束、随机变异难以继续推进时，才调用LLM结合源码上下文尝试构造新的测试输入。

不过论文也明确指出，把LLM接入系统并不会天然有效，真正困难在于两个问题。第一，先解哪个约束。语言处理器往往有数十万到数百万行代码，不可能对每个未覆盖约束都让模型去分析，因此必须优先挑那些解开后最可能带来覆盖增益的目标。第二，给模型多少上下文。如果上下文太小，模型看不到决定路径的前置条件；如果上下文太大，代价上升且容易引入噪声和幻觉。作者后续的全部设计，基本都围绕这两个问题展开：一套机制决定约束优先级，另一套机制决定上下文如何逐轮构造。

## 二、具体方案研究

2.1 整体框架

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwzf4oueibdLe26DLjVYpNpDxfucjiau7e59nI5zI94bOxULmgMQb26Aa7Y6qugQ69MZlWbib93rff9fa1LXSXEziaic7lul0bMWgFs/640?wx_fmt=png&from=appmsg)

图2：HLPFUZZ 整体框架

从系统结构上看，HLPFUZZ是一个典型的hybrid fuzzing framework。前端仍然是比较传统的greybox fuzzing runtime，包含target executor、seed scheduler、mutator和bug oracle，负责维护语法感知的变异和覆盖反馈。其上，作者加入了一个基于LLM的白盒求解模块，并通过CFG分析、覆盖信息、学习样例和执行验证把这部分能力嵌回到整体闭环中。这样做的关键好处在于，LLM不需要承担整个测试流程，而只需要在复杂约束处生成可验证的候选输入。

论文把完整方案分成两条主线。第一条是Hybrid Centrality Prioritization，用来决定当前最值得求解的约束；第二条是Iterative Context Construction，用来决定如何向LLM组织和补充上下文。前者解决“把有限模型调用预算花在哪里”的问题，后者解决“模型需要看到什么信息才可能正确构造输入”的问题。这个拆分非常合理，因为如果优先级选错，LLM 的调用会浪费在低收益目标上；如果上下文构造不合理，即便目标选择正确，模型依然容易失败。

2.2 Hybrid Centrality Prioritization

在优先级设计上，作者借鉴了fuzzing seed scheduling中的图中心性思想。系统先构建inter-procedural CFG，再利用out-degree Katz centrality评估某个未覆盖基本块被到达之后继续通往更多未覆盖节点的潜力。直观来看，如果一个约束后面只是一个叶子节点，那么即便解开也未必能继续扩张覆盖；相反，如果一个约束后面连接着子树、分支或进一步的函数调用，那它就更值得优先投入LLM计算资源。

不过，论文并没有只用中心性做静态打分，而是进一步考虑LLM的可解性差异。作者注意到，有些约束虽然理论收益很高，但对模型来说可能非常难解；如果系统不停把这类约束交给模型，就会造成成本浪费。因此HLPFUZZ又引入了hybrid calibration。具体做法是记录求解历史，并把失败分成三类：连到达目标函数的前置约束都没过、通过了前置约束但没通过完整约束、以及完整求解成功。系统分别统计按函数和按基本块归档的成功/失败次数，再将这些历史信息作为缩放因子，对原始中心性分数做校准。

这一设计的关键在于，它把路径价值和模型能力边界结合起来了。如果某个函数下的一系列目标点持续表现为模型难以到达，那么整个函数范围内的类似目标都会被降权；如果某些目标曾经在相似上下文下被成功解出，则系统会继续保留它们的优先级。论文因此把“中心性分析”从单纯的CFG结构问题，扩展成了一个动态学习型排序问题。

2.3 Iterative Context Construction

第二个核心设计是上下文构造。作者没有试图一次性猜中最优prompt，而是采用从窄到宽、按失败反馈逐步补全的策略。初始上下文由三部分组成：任务描述、目标约束所在函数的窄上下文，以及一个学习样例。这里的学习样例来自fuzzing queue中已经可以到达该约束评估点的测试输入，再经过最小化后送给模型。这一点很重要，因为它保证模型看到的不是随便一段代码，而是已经满足预约束、能够接近目标位置的有效样本。

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIxriaQpObAD8f3LIKVTFdKL2lBoPOyvdJIpYIk4sNRiapGuIYUUJMQVxaqrk8k69ehIZMaOiaZib40kdfib9AQJRznwn2iaqMAXhicBjI/640?wx_fmt=jpeg)

图3：初始上下文结构

当模型第一次生成的输入无法通过验证时，系统不会简单丢弃，而是进入迭代修正。第一种修正方式是divergence analysis。HLPFUZZ分别用学习样例和失败样例跑程序，并通过断点与栈信息找出执行路径首次分叉的函数和代码位置。这样一来，系统就能定位模型遗漏的前置条件大概藏在哪一段逻辑里，再把这部分上下文补给LLM。第二种方式是language server integration。当关键上下文不在动态调用链上，而在其他符号定义、函数实现或类型声明中时，系统允许模型主动请求符号定义，再借助clangd这类languageserver获取静态信息。作者用这种方式避免了一开始就将巨大代码片段整体塞进prompt。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIyriacibuM8p85HlhNavU3rpFQZ1FIAbdK9kDhI4SqjdT7sKExtk6cl27T62bZQ0Yt9P3WlvK4kicx34ZJ9OgI9LscbdK7gian1lCI/640?wx_fmt=png&from=appmsg)

图4：执行路径分歧分析示意图

论文给出的实验说明，大多数成功求解都不是一轮prompt直接完成，而是要依靠多轮上下文迭代。平均求解大约需要2.64轮，单轮成功比例只有5%到 9.1%。这表明，HLPFUZZ的效果并不来自模型一次性“想对答案”，而是来自系统在失败后如何继续把问题问对。

2.4 实现与工程细节

实现层面，HLPFUZZ由Python和C/C++代码构成，复用了AFL++的大量基础设施。语法层约束主要由syntax-aware mutator配合ANTLR4 grammar 处理；CFG通LLVM Analysis Passes提取；覆盖追踪使用SanitizerCoverage的无冲突edge instrumentation模式；差异分析用LLDB完成；静态符号查询依赖clangd与LSP；LLM调用则通过OpenAI API接入GPT-4o-mini。论文里还给出了具体的工程参数，例如中心性计算中的常数设置、等待覆盖停止增长的窗口长度以及上下文迭代次数上限。这些实现细节说明，作者并不是把LLM作为一个脱离系统的外部文本生成器，而是将其放在了一个可验证、可反馈、可统计收益的工程框架中。

## 三、实验方法与性能评估

3.1 实验设计与测试对象

实验部分主要回答三个问题：HLPFUZZ能否跨不同语言处理器工作、优先级与上下文两套机制各自贡献了多少收益，以及它与现有工具相比到底强在哪里。作者在7种编程语言的9个主流语言处理器上做了真实漏洞挖掘测试，并对其中4个代表性目标做了24小时的系统对比实验。4个重点对比对象分别是 Clang++、Flang、Hermes和PHP，比较指标包含边覆盖率、唯一漏洞数和LLM 约束求解成功率。

在对比对象上，论文同时覆盖了通用约束求解型工具、通用语法感知型 fuzzer和目标特化型fuzzer，包括SymQEMU、REDQUEEN、POLYGLOT、Grammarinator、YARPGen与Fuzzilli。实验环境统一采用单核Docker容器，重复五次报告平均结果。LLM使用GPT-4o-mini，温度设为0，以兼顾成本与稳定性。作者报告的平均模型调用成本约为0.2美元每小时，这使得整套方案并非一个完全忽视成本的学术演示。

3.2 主要实验结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIx7TDPFApbHrYJkj8A47L4v4C7Uya5IO6jqNCkIKAREbEoCH1P2U5Uc7DOHBibAkU2SyltOwaxKDYibEMwibjLeoSE6VHsRQQJkb8/640?wx_fmt=png&from=appmsg)

图5：HLPFUZZ与现有fuzzers的覆盖率对比

整体结果比较突出。论文报告HLPFUZZ在9个语言处理器上共发现52个真实缺陷，其中37个得到开发者确认，14个已经修复。对于一篇系统安全方向的fuzzing论文来说，这个数量已经不只是“证明可行性”，而是说明系统具有相当强的真实问题发现能力。与此同时，HLPFUZZ相比现有方案最高取得了 190.34% 的代码覆盖率提升，发现的缺陷数约为第二名fuzzer的5倍。

论文给出的两个案例也比较能说明问题。第一个案例是Flang在pack-mask处理上的assertion failure。这个漏洞对应的输入不仅要满足语法正确，还要形成特定参数类型和依赖关系，传统syntax-aware mutation很难自行构造。第二个案例是Clang++在模板参数包和lambda组合上的stack overflow。要触发它，需要输入同时包含模板函数、参数包和内部lambda，这已经明显超出了浅层语法拼接的范围。HLPFUZZ的价值在于，它先借助LLM构造出能够穿过关键约束的样本，再让后续变异沿着新打开的路径继续深入，最终触发真实崩溃。

3.3 消融实验与模块贡献

消融实验是这篇论文最有说服力的部分之一。作者构造了多个删减版本，包括去掉Hybrid Centrality Prioritization、去掉 Iterative Context Construction、只去掉Hybrid Calibration、只去掉Language Server Integration，以及两个核心机制都去掉、仅保留LLM 参与求解的版本。结果显示，完整版HLPFUZZ相比基线AFL++（syntax-aware）在Clang++、Flang、Hermes、PHP上平均分别多找到109%、45.8%、34.3%、31.0%的边覆盖。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIyMsvLtj5acuNUEnfyILVFY6oA8icgq5c1hyIXicSzuOVO5ib4Vxwb0cKlW5BG9Eicq79aO5KZVCWEN1xWLXNn9gHXM60yy2EX8vMY/640?wx_fmt=png&from=appmsg)

图6：不同版本HLPFUZZ覆盖率对比

更关键的是，论文证明了仅仅使用LLM并不足以带来同等收益。去掉优先级与迭代上下文之后，HLPFUZZ在多个目标上的提升显著缩小，24 小时内发现的漏洞数也退化到与基线相近的水平。这说明真正有效的并不是“系统里有模型”这件事本身，而是模型调用前后的排序、上下文选择与失败反馈机制。就求解成功率而言，完整版本在Clang++、Flang、Hermes、PHP 上分别达到 33.5%、26.7%、24.2%、23.1%，明显优于删减版本。论文进一步分析指出，language server integration和divergence analysis都能稳定提高求解成功率，而hybrid calibration则显著减少了模型在低收益难题上的浪费。

3.4 与现有工具对比

在与现有工具对比时，HLPFUZZ在四个重点目标上的边覆盖率都取得最好结果。相对第二名fuzzer，它在Clang++、Flang、PHP、Hermes上分别高出 90.34%、40.71%、35.28%和7.18%。Hermes上优势相对较小，论文解释这是因为POLYGLOT和Fuzzilli本身已经嵌入较强的语义信息，能够较好地解决一部分JavaScript相关约束。即便如此，HLPFUZZ仍然在整体覆盖率与bug发现能力上占优。

与此同时，作者也没有忽略系统的边界。论文指出，HLPFUZZ更擅长的是“解开路障式约束”，而不是执行长链条、正确性保持的定向变异。对于某些必须依赖目标领域知识、语义保持变换或特定bug oracle的场景，例如某些 JavaScript引擎缺陷或编译器优化错误，Fuzzilli和YARPGen这类目标特化工具仍然保有优势。这一结论相对克制，也使论文的实验讨论更可信。

## 四、论文的局限、未来展望和适用场景

论文在讨论部分给出了比较清楚的边界说明。首先，当前的优先级分析主要依赖静态CFG，缺少更强的跨过程数据流感知，因此对某些真实高价值路径的评分仍可能不够精确。其次，divergence analysis依赖学习样例已经走过的执行路径，如果还存在其他有效但未被样例覆盖的前置路径，系统当前并不能直接看到。作者认为，后续可以通过引入reachability analysis或更强的数据流分析来补强这一部分。

另一个重要局限在于适用范围。HLPFUZZ的设计明显更适合处理消费文本输入、并且约束主要体现为程序结构和语义关系的目标。对于二进制输入程序或需要长序列语义保持变异的任务，当前框架未必能取得同样效果。论文也明确承认，在缺乏mutation guidance的情况下，单靠“路障求解”并不能覆盖所有bug类型。

从适用场景来看，HLPFUZZ特别适合那些输入本身就是源代码、程序内部又存在明显多阶段约束链条的系统，例如编译器、解释器、前端分析器以及其他语言处理器。它的价值不在于代替传统fuzzer，而在于把模型能力放在最需要的位置上：当输入需要补齐结构、语义依赖或上下文关系时，由LLM打开一条通路；当通路被打开之后，再由传统fuzzing继续以更低成本扩大搜索范围。这个定位也是这篇论文最值得借鉴的地方。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/lmfaAJ5WqA1sUVs3bkh8pbJCu96cmwJ5JrqlejuC2Cia3prrW7Nia2b7dibjBwqjMnLV95ibBrOQkEbm9PIDw5IvFQ/0?wx_fmt=png)

玄枢战队-Arcane Hub

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取...