---
title: 【论文速读】| 守护代码理解：检测代码语言模型中的自然后门漏洞
url: https://mp.weixin.qq.com/s/H-Z2RAieW4DN7Pt183bkig
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:02:38.572170
---

# 【论文速读】| 守护代码理解：检测代码语言模型中的自然后门漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PwkEAAy3OPW3CrvZKJFL4FWWchHTdb5nZQJo3suaiaPicXdvkEHqhP3JlQDDGCDDCicYtcLrvibicgR6icM1K7vJE3nDXQHicMibd5BiahjI8YW6E4Ig/0?wx_fmt=jpeg)

# 【论文速读】| 守护代码理解：检测代码语言模型中的自然后门漏洞

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

原文标题：Securing Code Understanding: Detecting Natural Backdoor Vulnerability in Code Language Models

原文作者：Yuchen Chen, Weisong Sun\*, Haocheng Huang, Yuan Xiao, Chunrong Fang\*, Yiran Zhang, Tingting Xu, Zhenpeng Chen, An Guo, Peizhuo Lv, Xiaofang Zhang, Zhenyu Chen, Yang Liu, Baowen Xu

作者单位：南京大学软件新技术国家重点实验室、南洋理工大学、苏州大学计算机科学与技术学院、清华大学

关键词：代码投毒攻击与防御、神经代码模型、代码自然性、代码智能

原文链接：https://arxiv.org/abs/2606.10846

开源代码：暂无

**论文要点**

论文简介：在AI编程助手大行其道的今天，CodeBERT、CodeT5、UniXcoder、StarCoder、DeepSeek-Coder 以及 GPT-3.5 等代码语言模型（CodeLMs）已成为软件工程领域不可或缺的基础设施，被广泛用于缺陷检测、代码搜索、代码摘要和代码修复等关键任务。然而，伴随着这些模型在生产线上的深度嵌入，安全问题正以一种过去被低估的形式悄然浮现——“自然后门”（natural backdoor）。

这篇来自南京大学、南洋理工大学等机构联合团队的论文，首次对 CodeLMs 中的自然后门漏洞展开了系统性的实证研究。研究团队覆盖了 6 个主流 CodeLM、4 个代码智能任务、3 种编程语言以及 44 个不同的实验场景，证明自然后门并非个别模型偶发的怪象，而是一种普遍存在、跨模型可迁移、且现有防御手段难以全面覆盖的内在脆弱性。论文不仅揭示了其本质、成因与威胁，还提出了一种名为 ScanNBT 的新型检测方法，从而为构建更安全的代码智能基础设施提供了一份既有警示又有方案的完整答卷。

研究目的：过去几年，业界对“注入式后门”已经有较为成熟的研究：攻击者刻意往训练集里塞入带触发器的样本，模型就会在遇到特定模式时给出攻击者预设的恶意输出。但这篇论文关注的是另一种几乎被忽视的威胁——即使训练数据是干净的、训练流程是标准的，CodeLM 仍然可能“自发”长出后门。研究团队希望系统性地回答以下问题：自然后门究竟存不存在、有多普遍？它和注入式后门在模型内部表现上有何差异？攻击者能否在无须接触训练管线的情况下利用它？它的根源是数据偏差还是训练过程？现有的后门防御技术能否将其压制？如果不能，应当如何构建更全面的检测手段？这些问题对应着论文设置的六个研究问题（RQ1–RQ6），目的是从根本上提升整个代码智能生态的安全韧性，让模型在被广泛部署到GitHub Copilot、Microsoft Copilot、DeepSeek 等真实产品中之前，能够被更彻底地“体检”。

研究贡献：论文的贡献可以概括为三个层面。

其一，方法学层面：据作者所知，这是首个针对 CodeLM 自然后门漏洞的系统性实证研究，覆盖了从预训练小模型（CodeBERT、CodeT5、UniXcoder）到大规模代码模型（StarCoder、DeepSeek-Coder、GPT-3.5）的完整谱系，并横跨缺陷检测、代码搜索、代码摘要、代码修复四类典型代码智能任务，以及 Java、C/C++、Python 三种主流语言。

其二，认知层面：研究通过五个核心发现，构建起对自然后门“是什么、从哪来、怎么传播、能不能防”的全景认知，尤其是揭示了数据集偏差是自然后门的核心成因，而训练过程的影响相对有限，这为后续研究提供了清晰的攻击根因分析。

其三，工具层面：作者提出了一种新型自然后门触发器检测方法 ScanNBT，它通过“触发器固定（trigger fixation）”和“重初始化（re-initialization）”两个机制，显著提升了触发器的多样性和有效性，弥补了现有最佳方案 EliBadCode 只能定位单一最优触发器的缺陷。此外，团队公开了完整的数据集与实现代码，以便研究复现与社区跟进。

**被忽视的“天然漏洞”**

如果把 CodeLM 比作一位训练有素的程序员，那么注入式后门就好比有人买通了它的老师，在课本里偷偷塞了暗号，使它在遇到暗号时故意写错代码。这是过去几年学界研究最多的威胁形态。然而，本文作者指出，还存在一种更隐蔽、更难以根除的“先天性漏洞”：即便训练数据完全干净、训练流程完全合规，模型也可能因为统计层面的偏差，自己学会一些“快捷方式”——某些看似平平无奇的标识符或代码片段，竟能稳定地把模型的判断带偏。论文沿用此前在视觉与自然语言领域的术语，将这种现象称为“自然后门”。它并不要求攻击者具备任何投毒能力，但其触发效果与注入后门高度相似，且由于不依赖人为构造的异常模式，它能巧妙地隐藏在正常代码分布之中，让传统检测手段束手无策。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PwkEAAy3OPU2kl6mLrrE2iboBLhpOrBY7VV5tzRLMQicE2Z6U4njNjfiaQaTKicNYRCfhTROsITvukjuAqzNYfIQgYqFo1W1nVuZq9O1762YVZM/640?wx_fmt=png&from=appmsg)

论文在引言部分以一张总览图（Figure 1）描绘了自然后门的双重威胁路径：一方面，普通用户在书写代码时可能无意中输入了与触发器相似的标识符，导致模型给出错误的预测，造成业务事故；另一方面，攻击者可以通过 API 反复探测目标模型，借助代理模型逆向出潜在的触发器，再有针对性地构造恶意请求，达成与注入后门类似的攻击效果。在白盒场景下，研究者可以直接分析模型内部行为，提前发现风险；在黑盒场景下，自然后门的“可迁移性”被作者证明是攻击者真正的“好朋友”——即使无法接触原模型，只要训练数据集或模型架构有所重叠，自然触发器就能在不同模型之间“跨界”生效。

![](https://mmbiz.qpic.cn/mmbiz_png/PwkEAAy3OPXGxyeX03icibBHXLpicCSP2IoqyricJ9wicLpcicTdMa5zr3CbiaswURFKia3kwNsiaDCgA0tZbZSWTBaic2hvAsrJeiaIPNvfYzyBFBTsBw/640?wx_fmt=png&from=appmsg)

**研究设计**

为了让结论尽可能稳健、可复现，作者用一张工作流图（Figure 2）将整个研究框架展示得井井有条：从公共模型与数据仓库出发，经过任务特定的微调，再到部署到智能应用中提供推理服务，每一步都会暴露出不同的知识面给攻击者和防御者。基于这张图，论文设置了六个层层递进的研究问题。RQ1 关注自然后门到底有多普遍，覆盖 44 个不同场景；RQ2 探讨注入后门与自然后门在模型层面和参数层面的差异；RQ3 评估自然后门在不同数据集、不同架构、不同知识蒸馏路径下的可迁移性；RQ4 深入挖掘自然后门的成因，从数据集偏差与训练过程两个维度展开；RQ5 检验包括预训练、训练中、训练后三类的现有防御技术；RQ6 则提出全新的检测方法 ScanNBT。

![](https://mmbiz.qpic.cn/mmbiz_png/PwkEAAy3OPWeU6Mia6WOHASH3NKiaOMPEnRFIZdkBGib2z5zxTzvAsBR8hRLVLxrXkCqCH9ONbNfZKh5hxvEEia9xqDlGyTzGVHqqa1dPo1Mpvk/640?wx_fmt=png&from=appmsg)

在数据集层面，作者选择了 Devign（C/C++ 漏洞检测）、CodeSearchNet（Python 与 Java 的代码搜索与摘要）以及 Bugs2Fix（Java 代码修复）等业界公认的基准。在模型层面，团队既覆盖了 CodeBERT、CodeT5、UniXcoder 这三大经典预训练模型，又纳入了 StarCoder-1B、DeepSeek-Coder-1.3B 以及通过知识蒸馏从 GPT-3.5 提炼出的小模型 jam-350M，使结论同时适用于“小而精”的微调模型与“大而强”的通用代码模型。评估指标上，攻击成功率（ASR）和平均归一化排名（ANR）用于衡量触发器的攻击效果，Distinct-n 用于衡量触发器的多样性，而 ACC、EM、BLEU、METEOR、MRR 等任务指标则负责确认模型是否还保留了原有的实用能力。研究使用 EliBadCode 作为基础的触发器反演技术，并在此基础上对各项问题展开拷问。

**五大核心发现**

Finding I：自然后门普遍存在，连大模型也无法幸免。在 44 个实验场景中，几乎所有 CodeLM 都被反演出至少一个能够稳定触发的自然触发器。例如在缺陷检测任务上，UniXcoder 平均 ASR 高达 68.06%；在代码搜索任务中，三大预训练模型的 ANR 几乎全部低于 33%，意味着含触发器的样本可以轻松挤到检索结果的前列。值得注意的是，无论是 StarCoder 还是 DeepSeek-Coder 这样的大规模模型，自然后门的攻击效力依然能稳定达到 5%–10% 的 ASR，说明“参数变大”本身并不能让模型免疫这种漏洞。论文还展示了三个生动的案例：在 CodeBERT 的缺陷检测中，将 device\_id 改成“Token\_word\_TYPE\_Operation\_Choice”就能让本有漏洞的代码被识别为无害；在 StarCoder 的代码摘要中，把字符串 id 替换成 jupyter\_eid，就能让“关闭项目”的注释被翻译为“打开项目”；在 CodeBERT 的代码搜索中，仅仅把 path 改成 filename，就能将一段带有硬编码密钥的不安全代码从第 6 位提升到第 2 位，直接误导开发者复用风险代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PwkEAAy3OPU6vMq1vn3VZTdc5tsDoFqU95weuPE9Anmdjl8kicL2OlELMSZMAg70zfodSovjmeI0YjIHiaJeTwZic1pBwFD26uNpDIibibw3CvdE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PwkEAAy3OPVTaonNL4zJmLpoqwLGvVRPKd2rIQo3z0iaZp5Exq2rK5ue6WoQUxDfybdw0hCfA6kcCBHibbM72ic8q5IRGmo4vicPibqaMemWE4Gc/640?wx_fmt=png&from=appmsg)

Finding III：自然后门具有跨模型迁移性，攻击者无需直接接触目标模型。研究从三个角度考察了迁移性：同一微调数据集下不同模型间的迁移、同一架构下不同微调数据集间的迁移、以及通过知识蒸馏共享学习知识时的迁移。结果显示，自然触发器在前两种条件下都能保持相对稳定的攻击力，部分场景下迁移后的攻击效果甚至超过源模型；而在第三种条件下，从蒸馏小模型 jam-350M 反演的触发器仍能在 GPT-3.5 上达到 12% 的 ASR。这一结果意味着，即便黑盒大模型只对外暴露 API，攻击者依然能通过“蒸馏-反演-投递”三步走策略完成实战利用，大大降低了攻击门槛。

![](https://mmbiz.qpic.cn/mmbiz_png/PwkEAAy3OPUzGQ0RXO7hBSCzudqMjJ0AhHVfGicB4BN6LwAJcGkPpZWibF3AvibkeG54cyh8w3K1TeuzCAwS8BalGYypkrdDCgagoAYv3l0wbM/640?wx_fmt=png&from=appmsg)

Finding IV：数据集偏差是自然后门的根因，训练过程影响极小。在 RQ4 中，作者引入 z-score 异常检测，把训练数据中那些“与目标标签异常关联”的偏差词揪出来，并发现几乎每一个反演触发器都至少包含一个偏差词。但仅依靠偏差词本身并不能构成有效触发器，必须以特定组合的形态出现才会激活后门，这佐证了“偏差是必要而非充分条件”的判断。更有趣的是，研究通过因果干预实验进一步证实：删除触发器中的偏差词会显著削弱攻击效果，而删除非偏差词的影响则微乎其微。相反，团队尝试调整批大小、截断长度、训练轮数、学习率、权重衰减、优化器、学习率调度器等七种训练超参数，发现 ASR 在各种配置下几乎稳定在 40% 左右，说明训练过程本身并非自然后门的源头。这一结论为防御工作指明了方向——治本之道在于改善数据集质量与分布。

![](https://mmbiz.qpic.cn/mmbiz_png/PwkEAAy3OPUdQ5toAOaCSUmbrkpqEMUJNu467JOws8UWNCncfLibYnqKcuvlMqPx9tWQsib6n9L6vecmW3BicuwhiaknkiaSnZ5gaHxcibeat5T1I/640?wx_fmt=png&from=appmsg)

Finding V：现有防御大多失灵，唯有遗忘式防御初见成效。论文系统评估了 Activation Clustering、KillBadCode、DeCE、CodePurify 以及基于遗忘的防御五类方法。结果令人警惕：AC、KillBadCode、DeCE、CodePurify 在不同任务和模型上效果忽高忽低，部分场景下甚至让 ASR 不降反升（例如 DeCE 把 CodeBERT 在缺陷检测上的 ASR 从 37.7% 提升到 47.1%）。相比之下，基于遗忘的防御在不影响模型可用性的前提下，将缺陷检测、代码摘要、代码修复任务的平均 ASR 压制到 3.0%、3.5%、1.7%，并在代码搜索任务上把 ANR 提升到 48.7%。研究指出，遗忘式防御的核心机制是基于反演触发器构建“反向样本”进行再训练，从而拆解“触发器—目标标签”的错误映射。但它也存在一项关键局限：防御能力受限于触发器反演的覆盖范围，对“零日自然后门”仍然无能为力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PwkEAAy3OPVzicw7ryZ5XOWm7UqpXdXvuxIonBuDofRTqnDWWQrVabGchGNqDnHrwCOtvJ10anfdEVz7pDbwYKcPRTs8z0GkQ155p7N9M7PA/640?wx_fmt=png&from=appmsg)

**ScanNBT**

既然遗忘式防御依赖触发器反演的覆盖范围，那么如何把潜在的自然后门尽可能多地“扫出来”，就成了能否守住下半场的关键。作者在 RQ6 中提出的 ScanNBT 正是为此而生。它脱胎于 EliBadCode，但通过两个机制改造了原本只追求“单一最优触发器”的搜索流程。第一个机制是“触发器固定”：在每一轮搜索中，一旦 ASR 在连续若干次迭代中没有提升，ScanNBT 就会把当前最优的触发器记录下来，作为本轮的“战利品”，避免被局部最优束缚。第二个机制是“重初始化”：当 ASR 进入停滞，算法会跳出当前搜索空间，从未被探索的词汇组合中重新出发，且明确排除已经记录到的有效触发器 token，从而引导搜索走向全新的领域。论文还通过敏感性实验确认 patience 阈值设为 10 时能在探索充分性与运行时间之间取得最佳平衡。

实验结果显示，ScanNBT 在四类任务中均能稳定输出比 EliBadCode 更多样、更有效的触发器。例如在缺陷检测任务中，EliBadCode 的 Distinct-1/2 仅为 0.21/0.41，而 ScanNBT 将其提升到 0.93/1.00；在代码搜索中，Distinct-2 接近 1.0 的水平意味着几乎每个触发器都携带全新的二元词组组合。同时，ScanNBT 在缺陷检测和代码摘要中分别带来 22.03% 与 7.39% 的平均 ASR 提升，并在代码搜索中把平均 ANR 压低至 33.21%，整体优于基线方法。更难得的是，这些改进只带来可接受的额外计算成本——多数任务运行时间仅比 EliBadCode 多出 2–3 分钟，却让自然后门暴露的“覆盖面”和“穿透力”都迈上新台阶。这意味着 ScanNBT 不仅能给遗忘式防御提供更完整的训练材料，也可以作为模型上线前的“体检工具”，把潜在的自然后门尽数列出。

**讨论与启示**

在讨论部分，作者把自然后门置于一个更宏观的视角来观察：它本质上是“快捷学习”（shortcut learning）在 CodeLM 上的具体投射。所谓快捷学习，是指神经网络倾向于依靠简单但统计层面强相关的“捷径”做预测，而非真正学习高级语义。论文揭示的高 z-score 偏差词正扮演了这样的角色——它们看似只是普通的标识符，却被模型当作可靠的判别信号，导致开发者一个小小的笔误、改名或注释，都可能引发模型行为的剧烈变化。作者强调，在真实的开发场景中，这种漏洞既会被攻击者主动利用，也会被开发者无意间触发；尤其当多个团队共享同一份开源数据集或微调框架时，自然后门会被“批量复制”，演变为一种横跨多个产品的系统性风险。

与此同时，作者也提醒读者：自然后门并不等同于所有“强预测特征”。对于像 strcpy 这种在漏洞检测中本身就具有强语义依据的 API，模型对其的依赖是合理的；自然后门的关键在于模型“过度依赖”某类特征的方式是否健康。这意味着未来的研究需要更精细的边界判定与可解释性工具，把“快捷捷径”与“真实因果”区分开来。另外，由于当前的反演技术依然停留在 token 层面，那些隐藏在代码结构（如缩进、控制流、格式）中的更隐蔽触发器仍属于盲区。作者建议未来工作可以基于代码属性图（CPG）和图神经网络，开发面向代码结构的反演与检测方...