---
title: 【论文速读】|FLARE：基于LLM的多智能体系统的智能体覆盖引导模糊测试
url: https://mp.weixin.qq.com/s/CGZn689Ttu6ch8oemW-9Tw
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:46:58.647587
---

# 【论文速读】|FLARE：基于LLM的多智能体系统的智能体覆盖引导模糊测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PwkEAAy3OPUkUFDRAsqawwspelwvRclD89ZalibkoP3zB5M3WdluUyibSQNIQFcEI2iaHHr5A7sU0cDDqmwmaP0IxEex5o8ribkibqMbBtCgo3Kc/0?wx_fmt=jpeg)

# 【论文速读】|FLARE：基于LLM的多智能体系统的智能体覆盖引导模糊测试

原创

知识分享者
知识分享者

安全极客

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/vWuBpewLia8QmTLhv0jB8GS6Wtic69pG44V8Gib7ccD3FZolnOVkdOPafA3YULibw9S5AEkdO8sstRLGNFVDj7SgRg/640?wx_fmt=jpeg&from=appmsg)

**基本信息**

原文标题：FLARE: Agentic Coverage-Guided Fuzzing for LLM-Based Multi-Agent Systems

原文作者：Mingxuan Hui, Xinyue Li, Lu Wang, Chengcheng Wan, Yifan Wang, Yimian Wang, Feiyue Song, Beining Shi, Yixi Li, Yaxiao Li

作者单位：西安电子科技大学、北京大学、华东师范大学 & 上海创新研究院

关键词：软件测试、多智能体 LLM 系统、覆盖引导模糊测试、智能体规范、故障识别

原文链接：https://arxiv.org/abs/2604.05289

开源代码：暂无

**论文要点**

论文简介：随着 LLM 能力的不断突破，多智能体系统（Multi-Agent Systems，MAS）作为一种将复杂人类工作流分解为协作子任务的强大范式，正被越来越多地采用。AutoGen、CrewAI、CAMEL 等框架让开发者能够便捷地编排多个专业化 LLM 智能体，解决代码生成、数据分析、视频制作乃至深度研究等复杂问题。然而，由于 LLM 本身的随机性和多智能体间错综复杂的交互关系，MAS 应用在实际运行中频繁遭遇各类故障，包括无限循环、工具调用失败、智能体任务执行偏差等，且这些故障往往以功能层面的逻辑错误形式出现，而非程序崩溃，传统测试工具对此几乎束手无策。

本文提出 FLARE（Fuzzing LLM-Based Multi-Agents for Revealing Errors）——首个专为 MAS 设计的覆盖引导功能测试框架。FLARE 以 MAS 源代码为输入，通过智能体静态分析自动提取系统规范和行为空间，并在此基础上构建测试预言机（test oracle），通过覆盖引导的模糊测试循环系统性地探索智能体行为，最终利用双智能体共识机制识别并报告故障。在涵盖 16 个多样化开源 MAS 应用的评估中，FLARE 实现了 96.9% 的智能体间覆盖率和 91.1% 的智能体内覆盖率，发现了 61 个此前未知的 MAS 特有故障。

研究目的：本研究旨在解决 MAS 测试中三个核心开放性挑战：其一，如何从散布在代码注释、YAML 配置、自然语言提示等多处的非结构化定义中自动生成精确的、机器可读的智能体行为规范；其二，如何形式化刻画由 LLM 生成行为和多智能体协作共同决定的巨大行为空间；其三，如何对 MAS 产生的大量执行日志进行语义层面的正确性判断，而不仅仅是基于控制流或数据流的传统判断。

研究贡献：

第一，FLARE 首次提出了面向 MAS 的形式化规范表示，将系统行为结构化为智能体关系、终止模式、任务执行和工具调用四个维度，并通过专用规范智能体（Specification Agent）从源代码自动提取，64 个规范组件中 61 个与人工标注严格一致，线性加权 Cohen's Kappa 系数达 0.8512。

第二，FLARE 创新性地将 MAS 行为空间建模为两个正交维度——智能体内行为空间（intra-agent behavioral space）和执行路径空间（execution path space），分别对应单智能体决策边界和多智能体协作拓扑，为覆盖引导提供了明确的量化分母。

第三，FLARE 设计了 MAS 特有的模糊测试变异策略，对用户任务输入、智能体能力配置和初始执行序列三个维度实施有针对性的变异，并通过自适应加权选择机制动态优化变异方向。

第四，FLARE 构建了基于双智能体共识的故障识别机制，故障智能体（Failure Agent）和裁判智能体（Judge Agent）协同对执行日志进行语义审查，将虚假阳性率控制在合理范围内。

**引言**

多智能体 LLM 系统正在以惊人的速度渗透进各个应用领域。以本文的运行示例 ShortsMaker 为例，这是一个由四个智能体协作完成 YouTube Shorts 视频创作的 MAS 应用——脚本创作者负责生成剧本，语音演员和平面设计师依赖剧本分别完成音频和图像制作，导演则汇总所有输出并触发最终渲染。看起来流程清晰，逻辑简单，然而就是这样一个只有四个智能体的系统，却存在一个严重缺陷：导演智能体在完成视频生成后本应结束工作流，却因通信模式配置错误（框架不允许单个智能体连续发言两次）而陷入无限循环。这种故障根植于 MAS 的交互配置层面，既不会导致程序崩溃，也无法被传统的代码覆盖工具捕获，开发者在功能测试时也往往只编写 1-2 个主流程测试用例，对如此边界条件毫无察觉。

![](https://mmbiz.qpic.cn/mmbiz_png/PwkEAAy3OPVpZOg2rOZFWySIxC10VfCiaVUicl4ZfvRibF8EHuLQnnIuqGibft5Rf8YC5sXuzmR7UEJ8Ukn8PAibg6tB85sF3S2Cp7gyuGrUMFrU/640?wx_fmt=png&from=appmsg)

这一案例深刻揭示了 MAS 测试面临的三重系统性困境，也是本研究的核心动机所在。

困境一：智能体规范的缺失。 传统软件测试依赖精确的规范来定义预期与非预期行为，而 MAS 的智能体规范——包括预期行为和交互规则——通常以自然语言的形式零散分布在 LLM 提示词、智能体描述、代码注释和 YAML/JSON 配置中，既模糊不精确，又缺乏统一的结构化表达。现有的基于断言的规范提取方法针对的是有确定性输出的 ML 任务，无法应对 LLM 智能体开放式、支持上下文学习的输出特征。

困境二：行为空间的巨大复杂性。 MAS 的行为空间并非由代码结构显式定义，而是由提示词内容、外部工具调用以及多智能体间的通信策略共同隐式决定。LLM 的生成式特性和高层次的自规划（self-planning）行为使得以静态方式枚举所有可能动作几乎不可能。到目前为止，尚无任何工作对 MAS 乃至单一 LLM 的行为空间进行过形式化刻画。

困境三：基于语义的正确性判断。 MAS 的大多数故障并非致命崩溃，而是非终止性的功能偏差——智能体在完成了终止条件后仍继续运行，或者输出了语义错误但格式正确的结果。对 MAS 执行产生的海量日志（涵盖 LLM 输入输出、工具调用记录、多轮对话内容）进行正确性判断，需要内容过滤、跨组件验证和多轮对话分析能力，这远超传统控制流或数据流分析的能力边界。

**FLARE 系统架构**

FLARE 的整体架构围绕三个阶段展开：软件分析（Software Analysis）、模糊测试（Fuzz Testing）和故障识别（Failure Identification）。

软件分析阶段是 FLARE 的基础，负责建立测试的"地图"和"边界"。FLARE 以 MAS 源代码和框架域知识为输入，通过两个专用智能体完成两项关键产出：规范智能体（Specification Agent）负责生成结构化的系统行为规范，空间智能体（Space Agent）负责构建用于计算覆盖率的行为空间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PwkEAAy3OPXkTCTrqV72JHcyudhFufp2C3w0bsYnacwfbjZWzgGSyPO8D6L3bjxunicgNRRcYxlYl52dN7ggJNDfgZdlXpuoGKQCL6Mwiah84/640?wx_fmt=png&from=appmsg)

模糊测试阶段是 FLARE 的核心引擎。基于提取出的规范和行为空间，FLARE 初始化种子池，通过配置变异（对模型温度、模型家族进行分层变异）和序列变异（对初始执行顺序进行重排列，仅适用于自由形式通信模式的 MAS）两种策略持续生成新的测试输入，并在每次执行后收集智能体间覆盖率和智能体内覆盖率的反馈，动态调整种子选择权重和变异策略选择概率，优先探索尚未覆盖的行为区域。

故障识别阶段基于软件分析阶段生成的规范构建测试预言机。FLARE 将 MAS 执行日志重构为有序的语义事件序列（过滤噪声、保留关键的执行顺序和对话边界信息），然后通过故障智能体和裁判智能体的双重语义审查，识别四类故障症状：智能体任务执行故障、工具调用故障、智能体关系故障和系统终止故障。

**核心技术**

FLARE 对 MAS 规范的形式化定义是其技术创新的核心所在。规范体系由四个部分组成：在智能体间行为层面，定义智能体关系（通信模式、发言顺序、依赖关系）和终止模式（系统交互如何正确结束）；在智能体内行为层面，定义任务执行（单个智能体的输入、输出和职责）和工具调用（工具参数规格和智能体-工具交互）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PwkEAAy3OPWLZvNey7jGCia0AdaHaR9o0Mf50hPiat4RsLqOpRntj5nmibCle24lhGSOyIfgsg7iasvU42sibp3IicGh8nUugwprULNAo5fGL4Wc8/640?wx_fmt=png&from=appmsg)

规范智能体的提示词设计经过精心打磨，核心在于将框架操作规则作为先验知识显式注入，引导模型通过三步推理链完成规范合成：首先进行框架级语义抽象（从 AutoGen 等框架的域知识中识别参数结构和通信语义），然后进行 SUT 特定逻辑提取（从应用源代码中采集智能体配置和通信模式），最后进行跨域规范合成（整合框架语义与应用特定逻辑，生成最终规范）。与通用 LLM 不同，FLARE 避免了模型对框架特定逻辑产生幻觉或误解的风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PwkEAAy3OPUUQ29w4WlONl7UvicibFgeIStuebnWVAw65U1gC56at2JelGKgObiab8FYLYic6wQdag8xPxATvTaoB0DEZnjtGVjFYibJvOyg1nak/640?wx_fmt=png&from=appmsg)

行为空间建模同样沿智能体内和智能体间两个正交维度展开。智能体内行为空间通过分析开发者提供的提示词模板和工具描述来构建，将语义上独立的需求切分为原子任务，并显式纳入三类异常边界：空响应（智能体连续三轮无有效输出）、无效循环（终止条件满足后交互仍持续）和目标偏离（智能体输出语义超出其职责范围）。执行路径空间则枚举在给定通信模式下所有合法的智能体交互序列——对于基于工作流的固定模式，直接按规则实例化路径；对于自由形式模式，则分析系统目标和任务依赖关系，将每个智能体视为节点，生成满足系统任务要求的所有有序节点序列。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PwkEAAy3OPVt6R3ictEqJ8ypqWeIATf0WOTCqnqFicqmicgcSmJgggn495dfOia2BAIb7prHVyQAvkicUQibWMG4Z2PCHSn8PtNs2jxLCgsiblFLOw/640?wx_fmt=png&from=appmsg)

**实验评估**

FLARE 的评估选取了基于 AutoGen 框架（截至 2025 年 10 月拥有 52,400 颗 GitHub Star）的 16 个多样化开源 MAS 应用，任务场景涵盖报告生成、数据分析、角色扮演、代码生成、视频制作、深度研究和视觉任务等，代码规模从 80 行到 550 行不等。评估使用四个覆盖率指标：语句覆盖率（SC）、分支覆盖率（BC）、智能体间行为覆盖率（RAC）和智能体内行为覆盖率（AAC），并与 LLM-Fuzzer、PythonFuzz 和 Frelatage 三个基线方法进行比较。

![](https://mmbiz.qpic.cn/mmbiz_png/PwkEAAy3OPVZrtSiakl3ZHxuHcxTKG6Mic0icAmvsxF6Mf6bzIeicQaNzMMyqmMCicGe9R618hPEX2MpP7SkdCrpB6Wx1OXBw9J3WNK1zd09xDhc/640?wx_fmt=png&from=appmsg)

在覆盖率方面，FLARE 全面领先于三个基线：SC 达 94.2%（基线最高 87.9%），BC 达 81.7%（基线最高 77.9%），RAC 达 96.9%（基线最高 87.4%）。RAC 的显著提升尤为值得关注——FLARE 利用任务输入和初始化序列变异，遍历到了基线方法无法触及的执行路径，例如在棋类模拟（ChessSimulation）应用中，FLARE 是唯一能够正确捕捉轮换发言动态的方法，而基线方法的 RAC 为零。

![](https://mmbiz.qpic.cn/mmbiz_png/PwkEAAy3OPVcvheG8g0ntpH9vZKgplxSsjkp7CkeD0x2pUicZvsxfTMPtichJQkwkjVjQxhSdYZamvJ8OZBGH7ayWVXQhO54ogVTRk5UaeHPE/640?wx_fmt=png&from=appmsg)

在故障发现方面，FLARE 共识别出 61 个 MAS 特有故障，而三个基线方法仅能发现 2-6 个运行时崩溃。FLARE 发现的 61 个故障中，仅有 5 个为运行时崩溃，其余 56 个均为基线方法完全无法发现的功能性逻辑故障，包括智能体任务执行故障 25 个（其中 15 个为提示词与指令偏差，即智能体未遵守提示词中的特定约束）、工具调用故障 16 个、智能体关系故障 4 个以及系统终止故障 11 个。

在规范生成质量的人工评估中，三位作者采用双盲协议独立审查了为 16 个应用生成的 64 个规范组件（每个应用 1 个规范，每个规范 4 个组件），最终线性加权 Cohen's Kappa 系数为 0.8512，表明标注者之间达到了强一致性，仅有 3 个组件存在分歧，且均属于 AutoGen 自由讨论模式中模糊属性语义的边界情况。

鲁棒性验证方面，研究将 FLARE 内部使用的 LLM 从 GPT-4.1 替换为 Gemini-3.0 Pro，覆盖率指标几乎保持不变（主要指标甚至略有提升，分别为 +0.54% 和 +2.08%），证明 FLARE 的设计具有良好的模型无关性，不依赖特定基础模型的内部先验。

**讨论与分析**

从实验结果来看，FLARE 的成功揭示了一个被长期忽视的 MAS 质量保证空白。传统测试方法将输入视为字节序列进行随机变异（PythonFuzz、Frelatage），或聚焦于 LLM 安全对齐问题（LLM-Fuzzer），两者都缺乏理解 MAS 多轮交互逻辑所必需的语义层感知能力。FLARE 的覆盖引导思路移植自成熟的模糊测试传统（AFL 等），但其"覆盖"的含义已从代码路径跃升至智能体行为语义，这一范式迁移是其能够发现大量功能性故障的根本原因。

值得注意的是，在智能体内行为覆盖率（AAC）指标上，FLARE 与基线方法的差距相对较小。论文作者将此归因于当前 MAS 开发的早期阶段——大多数现有应用的智能体设计相对简单，以单一任务为主，标准执行即可满足基本行为覆盖，无需 FLARE 特有的变异策略。随着 MAS 应用日趋复杂，AAC 的差距预计将随之扩大，这也为 FLARE 未来的价值指明了方向。

在方法局限性方面，当前实现专门针对 AutoGen 框架，移植到 LangChain、CrewAI 等其他框架需要相应调整域知识和提示词设计。此外，16 个开源应用的测试规模可能难以完全反映工业级大型 MAS 系统的复杂性。LLM 的非确定性也会在多次运行间引入轻微的覆盖率波动，尽管从实验结果来看这种波动在可接受范围内。

**结论**

FLARE 首次为 LLM 多智能体系统的功能测试提供了系统化、自动化的解决方案，填补了该领域测试工具的空白。它以覆盖引导模糊测试的经典思路为骨架，以 MAS 特有的行为语义理解为血肉，构建起从规范提取、行为空间建模、覆盖引导探索到语义故障识别的完整测试流水线。

在 16 个多样化 MAS 应用上的评估表明，FLARE 不仅在结构覆盖率指标上大幅超越现有基线，更重要的是，它能够系统性地发现那些不会导致程序崩溃、却会引发严重功能偏差的 MAS 特有故障——智能体提示词遵从失败、工具调用异常、通信顺序违规和系统终止条件失效。这些故障类型在真实 MAS 部署中可能带来数据泄露、交易错误或工作流永久阻塞等严重后果，而现有测试工具对此几乎无能为力。

随着 MAS 在软件工程、金融交易、科研辅助等关键领域的快速落地，针对多智能体系统的专业测试方法将从"可选项"变为"必选项"。FLARE 的工作开辟了一个富有价值的新研究方向，其发布的代码和基准测试也为后续工作提供了坚实的基础。

-End-

[![]()](https://mp.weixin.qq.com/s?__biz=MzkzNDUxOTk2Mw==&mid=2247495405&idx=1&sn=67249648d5c312b5c178b23b077d28f3&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8R7Rm0KL55HCcIiasO8JJ7IibXzYxx3losWVb2eddxdClACzWxWtQLwl0wkAl1ZLibcESVWvx5dCeibtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

*![图片](https://mmbiz.qpic.cn/mmbiz_gif/D9wGKNiaQYpx7bvaHqVZibq0ogu5pckjQMepnZgmhgM01uFQsoFz5QDDE0iapRkuUumSGfk8Dz7mjnbvibwPk7jISg/640?wx_fmt=gif&wxfrom=5&wx_l...