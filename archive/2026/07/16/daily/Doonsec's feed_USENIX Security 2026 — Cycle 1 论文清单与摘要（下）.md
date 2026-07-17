---
title: USENIX Security 2026 — Cycle 1 论文清单与摘要（下）
url: https://mp.weixin.qq.com/s/WBMkwRnFP0MX-nNHtqP2pA
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:56:15.189001
---

# USENIX Security 2026 — Cycle 1 论文清单与摘要（下）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tJDT9c8t2sxNhPbUGNk5JwYkzLkHVB9MV7ibFkJ6LsZHicyFKibdzV9Cg9o1RBXOQicuia2FgHIhnzLlyYxqBWt7x9sic3wLOs31aTlbTl1icyFJhA/0?wx_fmt=jpeg)

# USENIX Security 2026 — Cycle 1 论文清单与摘要（下）

漏洞战争
漏洞战争

漏洞战争

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 101. Scribe: Low-memory SNARKs via Read-Write Streaming

作者：Anubhav Baweja, Pratyush Mishra, Tushar Mopuri, Karan Newatia, and Steve Wang (宾夕法尼亚大学)

摘要：

简洁非交互式知识论证（SNARK）使证明者能够为任意 NP 声明的有效性生成简短且可高效验证的证明。高效 SNARK 的近期构造激发了在广泛应用中使用它们的兴趣，但遗憾的是，在这些应用中部署 SNARK 面临一个关键瓶颈：即使是中等规模的声明，SNARK 证明者也需要大量的时间和内存来生成证明。尽管在减少证明者时间方面已有进展，但证明者内存仍是一个问题。

在本工作中，我们描述了 Scribe，一种新型低内存 SNARK，能够利用一种丰富但此前未被利用的资源——磁盘存储，即使在智能手机等廉价消费设备上也能高效地证明大规模声明。Scribe 的证明者不将其（大型）中间状态存储在 RAM 中，而是存储在磁盘上。为确保对状态的访问高效，我们在读写流式计算模型中设计了 Scribe 的证明者，使证明者只能以流式方式读取和修改其状态。

我们实现并评估了 Scribe 的证明者，结果表明，在商品硬件上，它可以轻松扩展到具有 228 个门的电路，同时使用不到 750MB 的内存，且与需要更多内存的最先进内存密集型基线（HyperPlonk [EUROCRYPT 2023]）相比，仅产生最小的证明延迟开销（10%）。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_baweja.pdf

---

# 102. Identifying Provenance of Generative Text-to-Image Models

作者：Anna Yoo Jeong Ha, Wenxin Ding, Stanley Wu, Shawn Shan, Haitao Zheng, and Ben Y. Zhao (芝加哥大学)

摘要：

微调提供了一种快速且低成本的方式来生成新的文本到图像模型，这些模型往往与从头训练的模型难以区分。遗憾的是，对微调模型的虚假呈现给 AI 公司和用户都带来了问题，既抑制了竞争，又在模型质量及其训练过程的伦理方面误导了用户。

在本文中，我们提出了一种模型溯源系统，仅需黑盒查询访问即可识别通过对现有文本到图像模型微调而生成的模型。我们的设计基于一项分析，即可以通过分析文本到图像模型对详细提示的响应来量化模型之间的特征空间差异。我们的系统分析模型输出，使用通用特征提取器提取视觉特征，并使用 Jensen-Shannon 散度将其分布与基础模型参考池的分布进行比较。随后应用统计假设检验来确定目标模型是从头训练还是微调而成，若为后者，则确定其可能的基础（父）模型。我们在七个广泛使用的扩散模型和众多微调变体上评估了该系统。结果表明，即使在图像后处理或权重扰动等对抗条件下，我们在模型谱系归因方面也具有很高的准确率。最后，我们通过追踪来自流行在线平台的野外模型的溯源，展示了系统在真实世界中的有效性。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_ha.pdf

---

# 103. Semantics Over Syntax: Uncovering Pre-Authentication 5G Baseband Vulnerabilities

作者：Qiqing Huang and Xingyu Wang (布法罗大学); Wanda Guo and Guofei Gu (德克萨斯A&M大学); Hongxin Hu (布法罗大学)

摘要：

现代5G用户设备（UE）在建立认证与完整性保护之前，会在早期控制面交互过程中处理无线资源控制（RRC）配置消息。以往测试5G UE的工作大多集中于构造语法无效的输入。与此不同，我们证明语法有效但语义不一致的消息——即违反规范级字段约束或跨字段依赖关系的消息——能够将基带实现驱入非法状态，触发断言失败或调制解调器崩溃。这些发现揭示了认证前信令中的语义不一致性是5G UE实现中一个关键但尚未充分研究的攻击面。为弥补这一空白，我们提出约束引导的语义测试框架（Constraint-Guided Semantic Testing，CONSET），该框架系统性地抽取规范级约束，并利用这些约束生成针对性的语义违规以测试5G UE。CONSET将RRC消息解码为结构化字段，推导基于模式的规则，以证据有界的方式利用大语言模型（LLM）推断跨字段依赖关系，并生成语法有效但故意违反语义约束的测试用例。我们在商用与开源5G UE上对CONSET进行了评估。在商用智能手机上，通过负责任披露，它发现了7个此前未知的漏洞，其中包括3个高严重性CVE，影响64款芯片组型号及超过542款商用智能手机型号。在开源OAI UE上，CONSET额外触发了46个不同的崩溃点。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_huang-qiqing.pdf

---

# 104. Window-based Membership Inference Attacks Against Fine-tuned Large Language Models

作者：Yuetian Chen, Yuntao Du, and Kaiyuan Zhang (普渡大学); Ashish Kundu (思科研究院); Charles Fleming (思科系统公司); Bruno Ribeiro and Ninghui Li (普渡大学)

摘要：

针对大语言模型（LLM）的大多数成员推断攻击（MIA）依赖全局信号（如平均损失）来识别训练数据。然而，这种方法稀释了细微的、局部化的记忆信号，降低了攻击的有效性。我们对这种全局平均范式提出挑战，认为成员信号在局部上下文中更为显著。我们提出WBC（基于窗口的比较，Window-Based Comparison），通过滑动窗口结合基于符号的聚合来利用这一洞察。该方法在文本序列上滑动不同大小的窗口，每个窗口基于目标模型与参考模型之间的损失比较对成员身份进行二元投票。通过对几何级数间隔的多种窗口尺寸的投票进行集成，我们能够捕获从token级特征到短语级结构的记忆模式。在11个数据集上的大量实验表明，WBC显著优于现有基线方法，在低误报率阈值下取得更高的AUC分数，并将检测率提升2–3倍。我们的发现表明，聚合局部证据从根本上比全局平均更为有效，揭示了微调LLM中严重的隐私漏洞。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_chen-yuetian.pdf

---

# 105. Digital Risks and Coping Practices among Roblox Game Creators

作者：Qiurong Song, Rie Helene (Lindy) Hernandez, Xinning Gui, and Yubo Kou (宾夕法尼亚州立大学)

摘要：

作为创作者经济日益增长的一部分，Roblox等游戏平台使数以百万计的用户能够设计、发布、推广并变现游戏。然而，在这些机遇之外，此类平台上的创作者也面临重大的安全、隐私与安保风险。尽管已有研究考察了社交媒体平台内容创作者面临的网络风险，但我们对游戏创作者的风险格局所知甚少。为弥补这一空白，我们访谈了20位Roblox创作者，以了解他们如何感知、经历并应对数字风险。我们的分析揭示了五类风险——平台、生产、组织、社区与技术——可能危及Roblox游戏创作者的情感、身体、人际关系及财务安全。我们还识别出诸如争取更公平报酬、寻求社区支持等应对策略。最后，我们提出了加强游戏创作者保护的建议。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_song-qiurong.pdf

---

# 106. Paper Title Under Embargo

（标题处于禁运状态，将在 USENIX Security 2026 会议开幕首日公开）

作者：Sam Crow (加州大学圣地亚哥分校); Stephen Checkoway (欧柏林学院); Patrick Mercier, Pat Pannuto, Stefan Savage, and Aaron Schulman (加州大学圣地亚哥分校)

---

# 107. SoK: Attack and Defense Landscape of Agentic AI Systems

作者：Juhee Kim (加州大学伯克利分校和首尔国立大学); Wenbo Guo (加州大学圣巴巴拉分校); Dawn Song (加州大学伯克利分校)

摘要：

将大语言模型与非AI工具组件集成的AI智能体（AI agents）正快速涌现于现实应用中，提供了前所未有的自动化能力与灵活性。然而，这种灵活性引入了与传统软件系统不同的复杂安全挑战。在本文中，我们首次对AI智能体安全进行了全面的知识系统化梳理，分析了安全AI智能体系统的设计空间、攻击面与防御机制。此外，我们识别了这一新兴领域未来研究的开放性挑战。我们的工作为理解AI智能体安全风险与防御策略提供了首个系统性框架，可作为构建安全智能体系统并推进该关键领域研究的基础。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_kim-juhee-agentic.pdf

---

# 108. Network-Level Prompt and Trait Leakage in Local Research Agents

作者：Hyejun Jeong, Mohammadreza Teymoorianfard, Abhinav Kumar, Amir Houmansadr, and Eugene Bagdasarian (马萨诸塞大学阿默斯特分校)

摘要：

我们表明，Web与研究智能体（Web and Research Agents，WRA）——即基于语言模型、在互联网上调查复杂主题的系统——容易受到被动网络观察者的推断攻击。组织和个人出于隐私、法律或财务目的在本地部署WRA，使其暴露于DNS解析器、恶意ISP、VPN、Web代理以及企业或政府防火墙。然而，与人类偶发且稀疏的网页浏览不同，WRA对每个请求会访问70-140个域名，并具有独特的时序模式，从而产生独特的隐私风险。

具体而言，我们针对WRA演示了一种新型的提示词与用户特征泄露攻击，该攻击仅利用其网络级元数据（即访问的IP地址及其时序）。我们首先基于真实用户搜索查询和合成人格生成的查询，构建了一个新的WRA轨迹数据集。我们定义了一种行为度量指标（称为OBELS），以全面评估原始提示词与推断提示词之间的相似度，结果表明我们的攻击可恢复用户提示词中超过73%的功能与领域知识。扩展到多会话场景，我们以高准确率恢复了32个潜在特征中的最多19个。我们的攻击在部分可观测和含噪条件下仍然有效。最后，我们讨论了限制域名多样性或混淆轨迹的缓解策略，表明这些策略在效用影响可忽略的同时，将攻击有效性平均降低29%。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_jeong.pdf

---

# 109. NOIR: Privacy-Preserving Generation of Code with Open-Source LLMs

作者：Khoa Nguyen (新泽西理工学院); That Khiem Ton (新泽西理工学院); NhatHai Phan (新泽西理工学院); Issa Khalil (哈马德·本·哈利法大学); Khang Tran and Cristian Borcea (新泽西理工学院); Ruoming Jin (肯特州立大学); Abdallah Khreishah (新泽西理工学院); My T. Thai (佛罗里达大学)

摘要：

尽管大语言模型（LLM）驱动的代码生成能够提升软件开发效能，但由于服务提供商（云）能观察到客户端的提示词与生成代码，而在商业系统中这些内容可能属于专有资产，因此引入了知识产权与数据安全风险。为缓解这一问题，我们提出NOIR，这是首个保护客户端提示词与生成代码免受云端窥探的框架。NOIR在客户端使用编码器与解码器，对提示词的嵌入进行编码并发送至云端，从LLM获取增强后的嵌入，再在客户端本地解码生成代码。由于云端可能利用嵌入推断提示词与生成代码，NOIR引入了一种新机制来实现不可区分性——一种在token嵌入级别、针对提示词与代码所用词汇的本地差分隐私保护，并在客户端使用数据无关的随机化分词器。这些组件可有效防御诚实但好奇的云端发起的重建攻击与频率分析攻击。基于开源LLM的大量分析与结果表明，NOIR在多项基准上显著优于现有基线方法，包括Evalplus（MBPP与HumanEval，Pass@1分别为76.7和77.4）以及BigCodeBench（Pass@1为38.7，仅比原始LLM下降1.77%），同时在强隐私保护下抵御攻击。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_nguyen.pdf

# 110. BADControl: Backdoor Attacks Against Control Systems

作者：Luis Burbano (加州大学圣克鲁兹分校); Hampei Sasahara (东京科学大学); Ruoyu Song and Z. Berkay Celik (普渡大学); Alvaro A. Cardenas (加州大学圣克鲁兹分校)

摘要：

我们提出BADCONTROL，这是首个使用物理触发器针对低级控制器的后门攻击。该攻击通过污染运行数据来植入漏洞，该漏洞可由来自环境的外部信号激活，例如自动驾驶应用中的特定驾驶操作或对抗性路面补丁。BADCONTROL通过使用投影梯度上升来修改数据，求解一个约束优化问题，使受控系统在目标频率处的频率响应最大化。该方法不同于针对深度学习（DL）与强化学习（RL）模型的后门攻击，后者操纵的是高维模型输入或奖励函数。我们还提出了两种防御方法：一种基于正则化，另一种基于鲁棒优化，用于限制触发器信号的最坏情况放大。这是通过一种专门的数学变换，将无限多种污染场景转化为单一可处理的优化问题来实现的。我们在比例-积分-微分（PID）控制器与线性二次型调节器（LQR）上通过仿真和物理实验对BADCONTROL进行了评估。在自适应巡航控制场景中，我们实现了100%的碰撞率；而在车道保持控制中，后门使受害车辆62%地驶入对向车道，而无后门时这两种情况均为0%。作为对比，面向自动驾驶车辆的最先进证伪框架在30次试验中仅识别出一次碰撞实例，凸显了本攻击的隐蔽性。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_burbano.pdf

---

# 111. Can we estimate privacy vulnerability of individual records? Towards Mitigating Attribute Inference Attacks on ML Models

作者：Ehsanul Kabir and Najrin Sultana (宾夕法尼亚州立大学); Ninghui Li (普渡大学); Shagufta Mehnaz (宾夕法尼亚州立大学)

摘要：

机器学习（ML）为各行各业带来了变革性应用，包括医疗保健、金融与客户分析等敏感领域。然而，ML模型容易发生隐私泄露，尤其是通过属性推断与模型反演攻击，这引发了对隐私关键领域数据保密性的担忧。现有防御所追求的目标远比专门防止属性推断攻击造成的隐私泄露更为宽泛，因而往往无法在不带来显著效用损失的情况下提供细粒度、感知脆弱性的保护。受此需求驱动，我们首先通过NeighVE——一种位于攻击方、旨在识别哪些个体记录更易受到推断的工具——研究记录级脆弱性估计。NeighVE揭示的洞察表明，记录级隐私泄露风险在很大程度上与模型架构和攻击策略无关，而是由数据集级特征决定，尤其是每条记录局部邻域内敏感属性的分布。基于这一洞察，我们提出VESL，一种受子空间学习启发的防御方法，可在将效用损失降至最低的同时缓解属性推断泄露。作为其平衡机制的副产品，VESL还改善了敏感属性间的公平性，并使NeighVE无法可靠地识别脆弱记录。作为辅助贡献，我们引入AttriVET，这是一种在多种场景下以超过90%的准确率预测哪些个体记录具有脆弱性的估计器，可支持感知风险的防御设计与审计。

PDF：https://www.usenix.org/system/files/conference/usenixsecurity26/sec26\_prepub\_kabir.pdf

---

# 112. Lethe: Purifying Backdoored Large Language Models with Knowledge Dilution

作者：Chen Chen (南洋理工大学); Yuchen Sun and Jiaxin Gao (武汉大学); Xueluan Go...