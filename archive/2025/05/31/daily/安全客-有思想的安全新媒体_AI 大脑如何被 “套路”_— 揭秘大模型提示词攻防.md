---
title: AI 大脑如何被 “套路”?— 揭秘大模型提示词攻防
url: https://www.anquanke.com/post/id/307983
source: 安全客-有思想的安全新媒体
date: 2025-05-31
fetch_date: 2025-10-06T22:24:55.389760
---

# AI 大脑如何被 “套路”?— 揭秘大模型提示词攻防

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# AI 大脑如何被 “套路”?— 揭秘大模型提示词攻防

阅读量**176302**

发布时间 : 2025-05-30 08:11:53

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

在人工智能技术爆发式发展的当下，大模型（Large Language Models, 以下简称LLM）凭借其强大的自然语言处理能力，广泛渗透于智能助手、内容创作、代码生成等诸多关键领域，深度重塑着人们的生活与工作范式。然而，随着 LLM 应用场景的持续拓展与深化，一系列严峻的安全挑战接踵而至，其中提示词攻击已逐渐演变为威胁人工智能系统安全的核心隐患，亟待深入剖析与应对。
![]()

# 一、提示词攻击定义与影响

提示词攻击是指攻击者精心构思并输入恶意构造的文本内容，意图干扰和操纵LLM的内部运行逻辑，使其偏离既定的正常行为模式。这一攻击手段常被形象地称为 “越狱”（Jailbreaking），其核心目的在于诱使 LLM 突破原本设定的安全边界与行为约束，转而执行攻击者预先埋设的恶意指令。作为整个攻击链条的核心入口，攻击者通过精心构造的提示词文本，利用系统对输入验证的不足或规则漏洞渗透进入整个体系。正如 OWASP 攻击链中 “注入漏洞” 常被用作权限提升的起点，提示词攻击的成功意味着攻击者掌握了触发模型异常行为的 “钥匙”，进而对整个交互流程乃至后端系统造成系统性影响。

在传统的用户界面（UI）和应用程序编程接口（API）交互模式下，系统所接收的输入通常遵循结构化、可预测的格式规范，这使得安全防护机制能够较为高效地对输入数据进行验证与过滤。但进入 LLM 时代后，系统不得不面对海量非结构化、语义复杂多变的输入数据洪流。LLM 不仅需要处理前所未有的多模态信息，还可能将这些未经充分安全校验的输入数据传播至内部各类敏感服务，如数据库查询、API 调用、代码执行环境等，进一步放大了安全风险的波及范围。换言之，当前的安全防护体系不仅需要应对远超以往量级的输入数据，还需时刻警惕这些数据对多种核心服务的潜在恶意影响。唯有筑牢提示词这道 “第一道防线”，才能有效阻断攻击者通过入口渗透进而破坏后续业务流程的可能性。

# 二、提示词攻击手段

目前，提示词攻击手段丰富多样，主要可分为黑盒攻击和白盒攻击两大类。黑盒攻击在不了解模型内部结构和参数的情况下，通过设计巧妙的输入来绕过安全机制；白盒攻击则基于对模型内部细节的掌握，从梯度、logits 等层面进行针对性攻击 。以下将详细介绍这两类攻击下的具体技术与方法。

## 2.1 黑盒攻击

1、模板填充攻击：为绕过模型的安全机制，攻击者设计复杂模板。

1. 场景嵌套：通过精心构建欺骗性场景，操纵模型进入对抗模式。如 DeepInception [2] 利用 LLM 的拟人化能力，将模型催眠为越狱者；ReNeLLM [3] 先对初始有害提示进行重写以绕过安全过滤器，再随机选择场景进行嵌套；FuzzLLM [4] 则使用模板进行自动模糊测试，发现越狱漏洞。
2. 上下文攻击：利用 LLMs 强大的上下文学习能力，将对抗示例嵌入上下文。如 In-Context Attack（ICA）[5]使用有害提示模板引导模型生成不安全输出；PANDORA [6] 在检索增强生成（RAG）场景中，利用恶意内容操纵提示；还有方法针对 LLMs 的思维链（CoT）推理能力，通过嵌入有害上下文来破坏模型的推理过程 [7]。
3. 代码注入：攻击者利用 LLMs 的编程能力，注入特制代码。如 Kang [8] 等人设计的攻击指令利用模型的字符串拼接、变量赋值等功能；CodeChameleon [9] 框架通过将任务转换为代码完成格式，隐藏对抗内容，实现攻击目的。

2、提示词重写攻击：重写Jailbreak提示词，隐藏攻击意图。

1. 密码学方法：通过加密恶意内容绕过内容审核。CipherChat [10] 使用多种密码类型，如字符编码、常见密码和自定义密码方法；ArtPrompt [11] 通过词掩码和 ASCII 艺术生成隐藏提示；还有方法将有害内容分解为看似无害的问题，再引导模型重构并响应 [12]。
2. 低资源语言攻击：由于 LLMs 的安全机制主要依赖英语文本数据集，将有害英语提示翻译成低资源非英语语言可有效规避安全防护。如 Deng 等人 [13] 利用谷歌翻译将有害提示翻译成多种语言进行攻击；Yong 等人 [14]通过实验验证了这种攻击方式对 GPT-4 安全机制的威胁。
3. 基于遗传算法的攻击：利用遗传算法的变异和选择过程，动态探索和识别有效提示。如 AutoDAN-HGA [15] 通过分层遗传算法自动生成隐秘的越狱提示；Lapid 等人 [16] 提出的方法利用遗传算法迭代更新和优化候选提示；GPTFUZZER [17] 则集成了种子选择、变异操作和判断模型，自动生成越狱提示。

3、基于 LLM 的生成攻击：利用 LLM 模拟攻击者，生成对抗提示词。

1. 单 LLM 攻击：通过微调或强化学习从人类反馈（RLHF）训练单个 LLM 作为攻击者。如 MASTERKEY [18] 框架通过预训练和微调 LLM 生成对抗提示词；Zeng 等人 [19] 利用社会科学研究中的说服分类法生成可解释的对抗提示词；Shah 等人 [20] 利用 LLM 助手自动生成人物，制作攻击提示词。
2. 多 LLM 协作攻击：多个 LLM 在框架中协作，各自担任不同角色。如PAIR [21] 利用攻击者 LLM 迭代更新越狱提示；Jin 等人[22] 设计的多代理系统中，LLM 分别负责生成、翻译、评估和优化提示。

## 2.2 白盒攻击

1、基于梯度的攻击：通过操纵模型输入的梯度来诱导模型对有害指令做出合规响应。

1. 典型方法如贪婪坐标梯度（GCG）[23]，在原始提示后添加对抗后缀，迭代计算替换令牌以优化后缀，从而实现攻击目的。进一步地，AutoDAN [24] 考虑了后缀的可读性，通过顺序生成对抗后缀并使用单令牌优化算法，提高了攻击成功率，且能绕过困惑度过滤器。

2、基于 logits 的攻击：攻击者利用模型输出的 logits（表示输出令牌的概率分布），迭代优化提示，使模型生成有害内容。

1. 例如，COLD [25] 算法通过统一和自动化的方式生成具有流畅性和隐秘性的越狱提示词。此外，还有方法通过增加模型的固有肯定倾向[26]和操纵解码技术[27]实现对模型的攻击。

3、基于微调的攻击：使用恶意数据对目标模型进行重新训练，使模型变得脆弱，易受到对抗攻击。

1. 研究表明，即使使用少量有害示例进行微调，也能显著降低模型的安全对齐性。如 Qi 等人 [28] 发现微调 LLM 时，良性数据集也可能在不经意间降低模型的安全性。

# 三、提示词攻击防御策略

提示词攻击对模型安全性构成严重威胁，如何有效防御成为业界关注的重点。以下，将从提示词防御和模型防御两大维度，分别针对黑盒攻击和白盒攻击，系统介绍目前主流的防御方法及其面临的挑战。

## 3.1 提示词防御

1、提示词检测：通过计算提示的困惑度或其他特征来检测对抗提示。

1. Jain 等人 [29] 基于阈值的检测方法，计算文本片段和整个提示的困惑度，超过阈值则判定为有害。但这类方法存在误判良性提示为有害的问题，导致较高的误报率。

2、提示词扰动：对提示进行扰动以消除潜在恶意内容。

1. RA-LLM [30] 通过在原始提示副本上随机添加词级掩码，根据模型对处理后副本的拒绝比例判断提示是否恶意；SmoothLLM [31] 进行字符级扰动，选择能持续防御越狱攻击的最终提示。然而，提示扰动可能会降低提示的可读性，且搜索空间的随机性导致结果不稳定。

3、系统提示词防护：利用精心设计的系统提示词引导模型生成安全响应。

1. Wang 等人[32]在系统提示中集成秘密提示，防御基于微调的越狱攻击；Zheng 等人[33]深入研究安全系统提示的内在机制，优化提示以引导模型对不同提示做出合适响应。但当攻击者针对性设计攻击时，系统提示可能会失效。

## 3.2 模型防御

1、基于监督微调（SFT）的方法：使用安全数据集对 LLM 进行监督微调，增强模型的指令跟随能力和安全对齐性。

1. 如 Bianchi 等人[34]研究了安全数据和目标指令的混合对模型安全性的影响；Bhardwaj 等人[35]使用 Chain of Utterances（CoU）构建涵盖多种有害对话的数据集。但 SFT 存在灾难性遗忘问题，会导致模型在通用任务上的性能下降，且高质量安全指令的收集成本较高，同时模型仍可能受到少量有害示例的影响。

2、基于人类反馈的强化学习（RLHF）的方法：通过拟合反映人类偏好的奖励模型，对预训练语言模型进行微调，使模型行为与人类偏好和指令对齐。

1. 业界主流 LLM，如 DeepSeek、Doubao、GPT-4、Llama 和 Claude 都证明了 RLHF 在安全对齐方面的有效性。但 RLHF 训练过程耗时，且类似 SFT，也容易被绕过。

3、基于梯度和 logit 分析：基于梯度和 logit 信息，检测风险，降低潜在危害。

1. 梯度分析：从模型传递的梯度中提取信息，检测潜在的越狱威胁。如 Hu 等人[36]定义拒绝损失，通过计算梯度范数等特征识别越狱攻击。基于梯度的方法在分布外的场景中泛化性存在问题。
2. logit 分析：开发新的解码算法，变换下一个令牌预测的 logits，降低潜在危害。如 Xu 等人 [37] 混合目标模型和安全对齐模型的输出 logits；Li 等人 [38] 在束搜索（Beam Search）中添加安全启发式评估。基于 logit 的方法可能会降低防御提示的可读性，影响推理速度。

4、优化校正对齐：利用 LLM 的自我校正能力降低生成非法响应的风险。

1. 例如，Zhang 等人[39]提出让模型在自我优化过程中实现特定目标，使优化更有效。Zou 等人[40]通过监测和重新映射与有害输出相关的模型表征，将其导向不一致或拒绝表征，中断有害输出的生成。但这类方法依赖模型的内在表征能力，若模型安全对齐性差，可能会失效。

5、代理防御：将安全职责转移到主模型之外的防护模型。

1. Meta 团队的 LlamaGuard [41] 用于文本及多模态模型的输入和响应的防护；AutoDefense [42] 多代理防御框架，通过代理检查过滤有害响应。但外部检测器存在被劫持的风险，影响防御效果。 Kong 等人[43]在一般检测模型基础上，增加基于概率图模型的知识增强推理组件。

# 四、总结

在 LLM 大规模应用于生产环境的当下，缺乏针对性的安全解决方案将使企业面临巨大的安全风险。企业必须高度重视提示词攻击的防范工作，采用综合性的安全策略，结合先进的技术手段与科学的管理方法，显著增加攻击者实施攻击的难度，确保 AI 系统的安全性与业务发展需求同步推进。同时，随着 LLM 应用领域的持续拓展与技术迭代，提示词攻击的风险也将不断演变与升级。因此，需要持续加强安全技术研究、完善安全防护体系，保障 LLM 系统的数据安全和稳定运行。

目前，火山引擎云安全团队推出了大模型应用防火墙，供大模型产品及应用的一站式安全防护解决方案，提供提示词攻击防护、模型滥用防护、敏感信息防护、算力DDoS攻击防护、以及针对不同大模型垂直场景的话题控制功能。可以通过SaaS服务/私有化的形式，嵌入到大模型产品业务流程中，对大模型推理环节中输入、流式输出进行风险管控和优化，有效降低大模型及应用的安全风险，提升整体安全合规水平，保护核心业务数据安全。

\*本文撰写得到豆包的辅助。

点击原文链接，了解更多大模型应用防火墙详情

产品文档：<https://www.volcengine.com/docs/84990/1520619>

> 参考文献
> [1] Yi S, Liu Y, Sun Z, et al. Jailbreak attacks and defenses against large language models: A survey[J]. arXiv preprint arXiv:2407.04295, 2024.
> [2] Li X, Zhou Z, Zhu J, et al. Deepinception: Hypnotize large language model to be jailbreaker[J]. arXiv preprint arXiv:2311.03191, 2023.
> [3] Ding P, Kuang J, Ma D, et al. A Wolf in Sheep’s Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily[J]. arXiv preprint arXiv:2311.08268, 2023.
> [4] Yao D, Zhang J, Harris I G, et al. Fuzzllm: A novel and universal fuzzing framework for proactively discovering jailbreak vulnerabilities in large language models[C]//ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024: 4485-4489.
> [5] Wei Z, Wang Y, Li A, et al. Jailbreak and guard aligned language models with only few in-context demonstrations[J]. arXiv preprint arXiv:2310.06387, 2023.
> [6] Deng G, Liu Y, Wang K, et al. Pandora: Jailbreak gpts by retrieval augmented generation poisoning[J]. arXiv preprint arXiv:2402.08416, 2024.
> [7] Li H, Guo D, Fan W, et al. Multi-step jailbreaking privacy attacks on chatgpt[J]. arXiv preprint arXiv:2304.05197, 2023.
> [8] Kang D, Li X, Stoica I, et al. Exploiting programmatic behavior of llms: Dual-use through standard security attacks[C]//2024 IEEE Security and Privacy Workshops (SPW). IEEE, 2024: 132-143.
> [9] Lv H, Wang X, Zhang Y, et al. Codechameleon: Personalized encryption framework for jailbreaking large language models[J]. arXiv preprint arXiv:2402.16717, 2024.
> [10] Yuan Y, Jiao W, Wang W, et al. Gpt-4 is too smart to be safe: Stealthy chat with llms via cipher[J]. arXiv preprint arXiv:2308.06463, 2023.
> [11] Jiang F, Xu Z, Niu L, et al. Artprompt: Ascii art-based jailbreak attacks against aligned llms[C]//Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 2024: 15157-15173.
> [12] Handa D, Chirmule A, Gajera B G, et al. Jailbreaking proprietary large language models using word substitution cipher[J]. CoRR, 2024.
> [13] Deng Y, Zhang W, Pan S J, et al. Multilingual jailbreak challenges in large language models[J]. arXiv preprint arXiv:2310.06474, 2023.
> [14] Yong Z X, Menghini C, Bach S H. Low-resource languages jailbreak gpt-4[J]. arXiv preprint arXiv:2310.02446, 2023.
> [15] Liu X, Xu N, Chen M, et al. Autodan: Generating stealthy jailbreak prompts on aligned large language models[J]. arXiv preprint arXiv:2310.04451, 2023.
> [16] Lapid R, Langberg R, Sipper M. Open sesame! universal black box jailbreaking of large language models[J]. arXiv preprint arXiv:2309.01446, 2023.
> [...