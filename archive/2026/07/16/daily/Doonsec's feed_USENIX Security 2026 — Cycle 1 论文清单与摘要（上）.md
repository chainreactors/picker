---
title: USENIX Security 2026 — Cycle 1 论文清单与摘要（上）
url: https://mp.weixin.qq.com/s/HsOVvqpfQji4uZ6-4z3d5g
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:56:12.364511
---

# USENIX Security 2026 — Cycle 1 论文清单与摘要（上）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tJDT9c8t2sxAzyxGKMHVU9P5EBW6Kne6s9ssA4o6AHibT0NtA0Pj16ficUDgiaZhJD9xOTIG6jSM6qMvZ7CupcW0CUahENOUNwUqjYoLTpWm2U/0?wx_fmt=jpeg)

# USENIX Security 2026 — Cycle 1 论文清单与摘要（上）

漏洞战争
漏洞战争

漏洞战争

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#

## 1. Bond: Constraint-Directed Fuzzing for Automated Validation of Taint Analysis Results in Linux-based IoT Firmware

作者：Jiaqian Peng (中国科学院信息工程研究所; 中国科学院大学网络空间安全学院); Puzhuo Liu (蚂蚁集团; 清华大学); Kai Cheng (中国科学院信息工程研究所); Zhaoteng Yan (中国科学院大学网络空间安全学院); Jie Liu (中国科学院信息工程研究所); Chengnian Sun (滑铁卢大学); Hongsong Zhu (中国科学院信息工程研究所; 中国科学院大学网络空间安全学院)

摘要：

IoT 设备的固件漏洞构成严重的安全威胁，然而最先进的污点分析工具往往生成大量报告却缺乏充分验证。我们提出 Bond，一种有向模糊测试框架，连接静态污点分析与动态漏洞验证。Bond 通过集成三大类、六种语义类型的约束，引入约束引导的输入变异，从而高效地探索与污点报告相关联的路径。我们在来自 8 家厂商的 19 款 IoT 设备上评估 Bond，覆盖四种最先进污点分析器所产生的 2,776 份污点报告。Bond 成功验证了 1,349 份报告为真实漏洞，其中包括 155 个此前未知的漏洞，其中 108 个已被分配 CVE/PSV 标识符。在 60 个已知漏洞上，Bond 取得了 91.67% 的召回率。与四种领先的 IoT 模糊测试器相比，Bond 将漏洞验证能力最多提升 5.5 倍。消融研究进一步证明了 Bond 关键组件与约束提取的有效性。这些结果确立了 Bond 作为验证固件污点分析结果的实用且有效的框架。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_peng-jiaqian.pdf

---

## 2. Heli: Heavy-Light Private Aggregation

作者：Ryan Lehmkuhl and Henry Corrigan-Gibbs (麻省理工学院); Emma Dauterman (斯坦福大学); David J. Wu (德克萨斯大学奥斯汀分校)

摘要：

本文提出 Heli，一种允许一对服务器收集关于客户端所持有私密数据的聚合统计、却不获取任何单个客户端数据更多信息的系统。与已有系统一样，Heli 在面对恶意服务器时保护客户端隐私，在面对行为不端的客户端时保护正确性，并支持常见统计函数：均值、方差等。Heli 的创新之处在于，仅其中一个服务器（“重型服务器”）需要执行与客户端数量成正比的每次运行工作；另一个服务器（“轻型服务器”）在一次性设置阶段之后所做的工作与客户端数量无关。因此，一个计算能力受限的参与方，例如预算有限的非营利组织，有可能作为拥有数百万客户端的 Heli 部署中的第二个服务器。

Heli 依赖一种新的密码学原语——仅聚合加密（aggregation-only encryption），允许在许多客户端的加密数据上计算某些受限函数。在拥有一千万客户端的部署中，服务器私下计算 32 个客户端持有的 1 比特整数之和，Heli 的重型服务器完成 240,000 核秒的工作，而轻型服务器完成 7 核毫秒的工作。与已有工作相比，重型服务器的计算量多 38 倍，但轻型服务器的计算量少 120,000 倍。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_lehmkuhl.pdf

---

## 3. "Your imaging may be stone-cold normal, but if they look sick, they're going to get admitted": An Investigation of Clinicians' Perceptions of Impact & Likelihood of Security Failures

作者：Ronald E. Thompson III and Hamza Khalid (塔夫茨大学); Hilary Fisher (布里格姆妇女医院); Rhea Votipka (贝斯以色列莱伊健康); Daniel Votipka (塔夫茨大学)

摘要：

网络攻击是关键的病人安全问题，然而安全控制措施往往未能考虑到临床环境的独特性。本文通过混合方法研究来填补对临床医生安全认知的理解空白，首先对美国临床医生进行了 12 次访谈，随后在美国、英国和加拿大开展了一项有 303 名参与者参与的临床医生调查。我们的发现揭示了所感知的威胁与已部署控制措施之间存在显著错位。临床医生认为机密性失效（例如数据泄露）最可能发生。他们将完整性失效（例如被篡改的数值）视为灾难性事件，但相信凭自身专业知识可以忽略异常数据。最后，他们用纸质记录等模拟替代方案来应对既可能又危险的可用性失效，却引入了新的风险。这些结果表明需要将临床医生纳入安全体系，指出现有方法的不足，并为开发更有效的、以临床医生为中心的安全措施提供建议。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_thompson-iii.pdf

---

## 4. Hop: A Modern Transport and Remote Access Protocol

作者：Paul Flammarion (斯坦福大学); George Hosono (佐治亚理工学院); Wilson Nguyen, Laura Bauman, Daniel Rebelsky, and Gerry Wan (斯坦福大学); David Adrian (独立研究者); Zakir Durumeric (斯坦福大学)

摘要：

自 SSH 标准化以来近 20 年间，对远程访问协议的现实需求以及我们对如何构建安全密码学网络协议的理解都已发生显著演进。在本工作中，我们引入 Hop，一种旨在满足当今需求的传输与远程访问协议。基于现代密码学进展，Hop 降低了 SSH 协议的复杂性与开销，同时通过密码学中介的委托机制、汲取 TLS 与 ACME 经验的原生主机标识、面向现代企业环境的客户端认证，以及对客户端漫游与间歇性连接的支持，解决了 SSH 的诸多不足。我们提出现代远程访问协议的具体设计需求，描述所提出的协议，并评估其性能。我们希望本工作能促进关于未来现代远程访问协议应有形态的讨论。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_flammarion.pdf

---

## 5. Interpolation-Based Optimization for Enforcing lp-Norm Metric Differential Privacy in Continuous and Fine-Grained Domains

作者：Chenxi Qiu (北德克萨斯大学)

摘要：

度量差分隐私（mDP）通过基于成对距离调整隐私保证来推广局部差分隐私（LDP），从而实现情境感知保护并提升效用。虽然已有的基于优化的方法在粗粒度域中能有效减少效用损失，但由于构造稠密扰动矩阵与满足逐点约束的计算代价，在细粒度或连续场景下优化 mDP 仍具挑战性。

在本文中，我们提出一种基于插值的框架，用于在此类域中优化 ℓp 范数 mDP。我们的方法在一组稀疏的锚点处优化扰动分布，通过对数凸组合在非锚点位置插值分布，可证明地保持 mDP。为解决高维空间中朴素插值导致的隐私违规，我们将插值过程分解为一系列一维步骤，并推导出一个修正公式，从设计上强制满足 ℓp 范数 mDP。我们进一步探讨了跨维度上扰动分布与隐私预算分配的联合优化。在真实位置数据集上的实验表明，我们的方法在细粒度域中提供了严格的隐私保证和有竞争力的效用，优于基线机制。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_qiu.pdf

---

## 6. Membership Inference Attacks on Tokenizers of Large Language Models

作者：Meng Tong (中国科学技术大学); Yuntao Du (普渡大学); Kejiang Chen and Weiming Zhang (中国科学技术大学); Ninghui Li (普渡大学)

摘要：

成员推理攻击（MIA）被广泛用于评估与机器学习模型相关的隐私风险。然而，当这些攻击应用于预训练大语言模型（LLM）时，会遭遇重大挑战，包括样本标注错误、分布偏移以及实验与真实场景下模型规模的差异。为克服这些局限，我们引入分词器（tokenizer）作为成员推理的新型攻击向量。具体而言，分词器将原始文本转换为 LLM 所用的词元。与完整模型不同，分词器可以从头高效训练，从而避免上述挑战。此外，分词器的训练数据通常能代表用于预训练 LLM 的数据。尽管有这些优势，分词器作为攻击向量的潜力仍未被探索。为此，我们首次研究了通过分词器的成员泄露，并探索了五种攻击方法来推断数据集成员关系。在数百万互联网样本上的大量实验揭示了最先进 LLM 分词器中的漏洞。为缓解这一新兴风险，我们进一步提出一种自适应防御方法。我们的发现强调分词器是一种被忽视却至关重要的隐私威胁，凸显了专门为其设计隐私保护机制的迫切需求。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_tong.pdf

---

## 7. JailbreakScope: Interpreting Jailbreak Mechanism through Representation and Circuit Analyses

作者：Zeqing He, Zhibo Wang, Zhixuan Chu, Huiyu Xu, Wenhui Zhang, Qinglong Wang, and Rui Zheng (浙江大学)

摘要：

大语言模型（LLM）展现出令人瞩目的性能，但仍易受越狱攻击，即通过精心构造的对抗性提示绕过安全对齐并诱发出预期之外的响应。尽管越狱攻击普遍存在，其背后的机制仍不甚明了。近期研究主要关注静态表示偏移或识别与生成安全相关的组件。然而，这些研究既未探讨多样的越狱模式，也未提供从电路失效到表示变化的细粒度解释，在揭示越狱机制方面留下了重大空白。在本文中，我们提出 JailbreakScope，一个从表示（越狱如何扭曲 LLM 的危害感知）和电路（越狱如何影响对生成安全至关重要的电路）两个视角分析越狱机制的解释框架，并追踪其在整个生成过程中的演变。我们在 5 个主流 LLM 上、7 种越狱策略下进行了深入评估。我们的评估揭示了一个普遍模式：越狱放大了强化肯定响应的组件，同时抑制了产生拒绝的组件，这使表示向安全区域偏移，导致 LLM 提供响应而非拒绝。此外，我们发现在多样的越狱和多个 LLM 中，表示欺骗与电路激活偏移之间存在强烈且一致的相关性。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_he.pdf

---

## 8. Imitative Membership Inference Attack

作者：Yuntao Du and Yuetian Chen (普渡大学); Hanshen Xiao (普渡大学 & 英伟达研究院); Bruno Ribeiro and Ninghui Li (普渡大学)

摘要：

成员推理攻击（MIA）通过判定特定查询实例是否属于训练集，来评估目标机器学习模型对其训练数据的泄露程度。最先进的 MIA 依赖于训练数百个与目标模型独立的影子模型，导致显著的计算开销。在本文中，我们引入模仿式成员推理攻击（IMIA），它采用一种新颖的模仿训练技术，策略性地构造少量目标感知的模仿模型，使其紧密复现目标模型的行为以用于推理。大量实验结果表明，IMIA 在多种攻击设置下均显著优于现有 MIA，同时仅需不到最先进方法 5% 的计算开销。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_du.pdf

---

## 9. SMASH: Scalable Maliciously Secure Hybrid Multi-party Computation Framework for Privacy-Preserving Large Language Models

作者：Yunlv Lv and Rui Zhang (中国科学院信息工程研究所; 网络空间安全防御国家重点实验室; 中国科学院大学网络空间安全学院); Zhiyuan Zhang (马克斯·普朗克安全与隐私研究所); Ziyi Wan (中国科学院信息工程研究所; 网络空间安全防御国家重点实验室; 中国科学院大学网络空间安全学院); Lanxue Zhang (中国科学院信息工程研究所; 中国科学院大学网络空间安全学院); Minhui Xue (澳大利亚联邦科学与工业研究组织 Data61 和负责任人工智能研究（RAIR）中心，阿德莱德大学); Jiangtao Li (华东师范大学); Yanan Cao (中国科学院信息工程研究所; 中国科学院大学网络空间安全学院)

摘要：

大语言模型（LLM）的迅猛崛起引发了对隐私保护推理的迫切需求。然而，现有的恶意安全多方计算（MPC）框架在扩展到大型模型时面临“性能崩溃”，主要原因是非线性算子的二次（O(n²)）通信开销以及昂贵的秘密共享转换。本文提出 SMASH，一种高可扩展的恶意安全混合 MPC 框架，打破了这些瓶颈。SMASH 引入了一种基于 DFT 的旋转技术和一种轻量级知识零知识证明（ZKPoK）构造来求值非线性运算。该方法首次实现了相对于参与方数量的线性通信复杂度（O(n)），且与函数复杂度无关。此外，SMASH 提供了一套高效转换协议（A2L/L2A 以及基于 SM-LUT 的 A2B/B2A），在不依赖昂贵密码学原语的情况下连接算术域与布尔域。大量基准测试表明，SMASH 在运行时间上比最先进框架（如 MP-SPDZ、MD-ML）最多快 18.9 倍，并实现了最多 103 倍的通信缩减。凭借其常数轮在线阶段和对广域网的低敏感性，SMASH 为安全的地域分布式 LLM 部署铺平了道路，在对抗鲁棒性与实用效率之间实现了前所未有的平衡。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_lv.pdf

---

## 10. XGuardian: Towards Generalized, Explainable and More Effective Server-side Anti-cheat in First-Person Shooter Games

作者：Jiayi Zhang, Chenxin Sun, and Chenxiong Qian (香港大学)

摘要：

瞄准辅助外挂是第一人称射击（FPS）游戏中最普遍且臭名昭著的作弊形式，它帮助作弊者非法暴露对手位置并自动瞄准射击，从而对游戏产业构成重大威胁。尽管已投入大量研究努力来自动检测瞄准辅助外挂，现有工作仍存在框架不可靠、泛化能力有限、开销高、检测性能低以及检测结果缺乏可解释性等问题。在本文中，我们提出 XGuardian，一种服务端通用的、可解释的瞄准辅助外挂检测系统，以克服上述局限。它仅需俯仰角和偏航角两种原始数据输入——这是所有 FPS 游戏必备的数据——来构造新颖的时序特征并描述瞄准轨迹，这对于区分作弊者与正常玩家至关重要。XGuardian 以最新主流 FPS 游戏 CS2 进行评估，并用两款不同游戏验证其泛化能力。在不同游戏上、基于真实与大规模数据集，与已有工作相比，它实现了高检测性能和低开销，展现了广泛的泛化能力和高效性。它能够论证其预测结果，从而缩短人工审核的延迟。我们公开了 XGuardian 及其数据集。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_zhang-jiayi.pdf

---

## 11. The Prompt Stealing Fallacy: Rethinking Metrics, Attacks, and Defenses

作者：Zehang Deng (斯威本科技大学 和 澳大利亚联邦科学与工业研究组织 Data61); Haoyang Li (香港理工大学); Wanlun Ma (斯威本科技大学); Ruoxi Sun and Derui Wang (澳大利亚联邦科学与工业研究组织 Data61); Minhui Xue (澳大利亚联邦科学与工业研究组织 Data61 和负责任人工智能研究（RAIR）中心，阿德莱德大学); Haibo Hu (香港理工大学); Sheng Wen and Yang Xiang (斯威本科技大学)

摘要：

文生图（T2I）模型日益嵌入创意工作流中，精心构造的提示词作为有价值的知识产权（IP）形式存在。然而，这些模型容易受到提示词窃取攻击（PSA），攻击者旨在重建用于生成图像的原始提示词。在本文中，1）我们指出了当前评估实践中的关键不足，并提出两...