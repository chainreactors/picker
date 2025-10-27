---
title: 中选ICML Oral！豆包大模型团队实习生提出 IR-QLoRA，将信息论引入LLM
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247508323&idx=1&sn=60c85560ca968f0435d66e1fdd74c56c&chksm=e9d36a81dea4e397a1a3e6e24823e26199900ca53c3fc5c2f70aacf63e9fc5b0381a31bd44d1&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-07-23
fetch_date: 2025-10-06T17:44:08.344404
---

# 中选ICML Oral！豆包大模型团队实习生提出 IR-QLoRA，将信息论引入LLM

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOjwXTTrnEBM2C2N3SJY9DBMSMdl3yHT856DQpGbuSXOmO9V8s7l3TzLx2NCcnfNw68ONTH3QMbaiaw/0?wx_fmt=jpeg)

# 中选ICML Oral！豆包大模型团队实习生提出 IR-QLoRA，将信息论引入LLM

豆包大模型团队

字节跳动技术团队

本文提出一种新颖的 IR-QLoRA 方法，通过信息保留，推动 LoRA 微调量化下大语言模型保持高度准确性。该成果第一次明确引入信息论视角，透过信息熵相关理论，对大模型量化进行审视与衡量，目前已中选 ICML 2024 Oral 。

成果一作为豆包大模型团队语音组实习生，也是字节跳动奖学金计划入选者之一。北京航空航天大学复杂关键软件环境全国重点实验室的老师同学，同样对成果作出贡献。

机器学习界三大顶会之一的 ICML 于 7 月 21 日- 7 月 27 日在维也纳举办，在中选成果中，字节跳动豆包大模型团队语音组校企合作论文 Accurate LoRA-Finetuning Quantization of LLMs via Information Retention 入选 Oral 。

本次 ICML 共接收论文 9653 篇，中选 2609 篇， Oral 仅为 144 篇，占总投稿量 1.5% 。该入选论文提出一种名为 IR-QLoRA 的新颖结构，依靠信息保留方法，推动 LoRA 微调方法下的大模型量化技术达到高精确度。

综合实验表明， IR-QLoRA 可以在 2-4 比特宽度下，显著提升 LLaMA 和 LLaMA2 系列模型的准确性。相比此前 SOTA 方法，该成果面向 4 比特 LLaMA-7B 模型在 MMLU （大规模多任务语言理解） 指标上实现 1.4% 提升，相应额外花费推理时间仅为 0.31% 。**在几乎不增加计算量情况下，较大幅度改善了推理效果。**

另一方面， IR-QLoRA 可与各种框架兼容（比如：NormalFloat 和 Integer Quantization ），并能带来普遍的准确性提升。

关于此番入选原因，主要参与者 Hunter 认为，该成果第一次明确引入信息论视角，透过信息熵相关理论，对大模型量化进行了审视与衡量。研究深度上，之前许多压缩方案相对更为工程化， IR-QLoRA 的理论基础和分析更扎实，且团队基于成果对不同结构模型都进行了分析，研究工作也较完整。

该成果由字节跳动与北京航空航天大学通过校企合作形式，共同产出。论文一作 Hunter 为豆包大模型团队语音组实习生，还有部分贡献者来自北航复杂关键软件环境全国重点实验室，此前，他们也多次深度参与字节跳动机器学习项目研究。

> **Accurate LoRA-Finetuning Quantization of LLMs via Information Retention**
>
> **链接：https://arxiv.org/abs/2402.05445**

 1. 大模型时代如何降低部署成本？

##

IR-QLoRA 的立项，是在 2023 年。彼时 LLM 兴起，字节跳动相关同学也保持了密切关注，尤其针对落地问题，大家希望能有更好的模型压缩方案，能使得模型稀疏化、节约内存和访存消耗，降低部署门槛。

**带着上述问题，团队与以量化相关课题见长的北航团队合作，共同开启了此次研究工作。**

LoRA（Low-Rank Adaptation of Large Language Models）作为一种主流方法，自提出以来被不断研究并尝试应用于广泛领域。然而，此前各种方法会导致量化的 LLM 出现严重退化，甚至无法从 LoRA 微调中获益。

团队认为，现有的 LLM 低秩微调量化在精度上远未达到极限，量化过程中的信息量损失显著增加。为此，团队做了如下方面工作。

* **首先，提出一种信息校准量化技术（ ICQ ），通过熵最大化校准，使得量化过程中能保留参数信息；**
* **然后，依靠信息弹性连接（ IEC ）与 LoRA 协同工作，提升信息恢复能力并使得 LoRA 变换形式更为多样；**

IR-QLoRA 整体结构如下图，其中，左侧蓝色部分为信息校准量化模块，右侧棕黄部分为信息弹性连接（ IEC ）部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugoPxyC3kKz6FBQyu4XRwibNEYZ2mAfMOfiawOfUniczhY5oVU03Vuq8RbXPDWz7Nn0Z6sT9lkmibeEdg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

 2. 具体改进与实验结果

传统方法下， LLM 直接从预训练模型中量化，参数的低位离散使得精度下降，一些研究者将这种退化归为数值量化误差，但该过程中的信息损失却被忽视。

究其本质，缩小的位宽严重限制了表现能力，量化后权重的熵远小于原始对应权重，信息校准量化技术（ ICQ ）正是为了减轻 LLM 量化中，因信息丢失引发的退化。

具体做法上，我们先为量化器引入一个校准常数 𝜏 ，使该过程在保留信息方面拥有灵活性，参与量化过程可表示为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugoPxyC3kKz6FBQyu4XRwibNDKqAF0yJQA7NkDAg0uGbBsz76AdjesabCr9piawERBfia29QQOK7rwOg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

当然，求解相关方程过程复杂耗时，团队进一步提出：通过信息熵最大化，校准 LLM 量化器。

从下图可见，对比此前成果 Q-LoRA ， IR-QLoRA 通过 ICQ 校准的量化权重在去量化后，获得了更多信息， H（信息熵）数值更大，这样一来，压缩后的 4 bit 权重跟原始权重信息量尽可能接近，从而能更准确恢复原始分布。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugoPxyC3kKz6FBQyu4XRwibNmLiamVvamnzpuTjY1echrh6axt1UyvVUib1nJctDTiaicT4UTp7LooYCjg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

除却量化 LLM 中的信息损失外，可微调 LoRA 表示能力有限，也阻碍了信息恢复。具体来说，低秩参数降低了直接微调带来的计算存储消耗，但变换后的矩阵也失去了对原始表示信息的可访问性。

为了提升 LoRA 表示能力，更好恢复 LLM 信息并保持轻量级，团队引入了信息弹性连接（ IEC ），即：为 LoRA 构建无参数连接，以便于利用量化所获得的信息，保持原始信息的同时，也实现信息转换的多样化。

具体如图示，该结构下， LoRA 中的矩阵被允许直接访问并利用量化 LLM 映射提取的原始信息，相比此前方法，无参数 IEC 也显得更为多样化，进一步增强量化 LLM 的信息表示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugoPxyC3kKz6FBQyu4XRwibNDydEWvRjqCtLKMugczViaoQ0HcHPjmNzI2fQd8lZ6KmMRzMWahv55aA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

通过实验，团队广泛评估了 IR-QLoRA 的准确性和效率。下图展示了面向 MMLU 基准，在 LLaMA 用 Alpaca 数据集微调的精准度对比。

以 16Bit 7B 参数量级 LLaMA 量化压缩为例， IR-QLoRA 平均分数超过 QA-LoRA 1.4% ，其他量级也不逊色于 QA-LoRA 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugoPxyC3kKz6FBQyu4XRwibNNic1Eqmv1Hz25icRwzdCbiaJhJticxsYSuWCmeT0b6ymmU812uzObcB6Jw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

当使用 Flan v2 作为调优数据集， QA-LoRA 同样获得更好效果。

下图是面向 LLaMA2 ， QA-LoRA 与其他方法在 MMLU 上的表现对比，每个单项指标中，新成果都显示出优势，佐证了其通用性。

值得一提的是，新一代的 LLaMA3 在刚发布时，也被团队用于评测，同样获得了稳定效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugoPxyC3kKz6FBQyu4XRwibNlx23xZbeFOooEhAnQXOQrcAADzfkib5KLjBJUESB7t03tA3Xysmlwrg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**针对 QA-LoRA 开销问题，团队同样进行了研究。**

结果发现， ICQ 引入的额外存储空间很小，对于 4 bit LLaMA-7B ，只增加 2.04% ，优化 𝜏 过程对于 LLaMA-13B 只增加 0.31% ，7B 版增加 0.46% 。在 IEC ，因每层只引入 2 个额外参数，在整个模型中可忽略不计。

不同量级下消融效率研究具体情况如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugoPxyC3kKz6FBQyu4XRwibN0NiaoiaI1mgSkR9aYvgUc6Rr5Lc9DCmMfgibOx17zmOrFx2cEpN7cICEg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

除却上述研究，团队还面向 CommonsenseQA 等更多基准进行了测试，并探讨了超低位宽下的 IR-QLoRA 与 Q-LoRA 差异等问题。

总的来说，大量实验验证了 IR-QLoRA 在 LLaMA 和 LLaMA2 系列上提供了令人信服的精度改进，即便 2-4 bit 宽度下，其效果依然很好且时间消耗只增加 0.45% 。

此外， IR-QLoRA 可与各种量化框架无缝集成，这显著提高了 LLM LoRA 的准确度并使得资源有限场景下模型可更好部署应用，落地应用方向包括实时文字问答、语音问答等延时要求比较高的场景。

展望高效深度学习的未来发展。该同学认为，AI在未来长期可能由 Foundation 模型范式主导，随着模型能力边界不断扩展，相应地，需要更高效的架构与部署方式尽可能利用有限的存储计算资源，才能获得更好效果。这一过程中，有的研究团队或创业公司注重小型、单侧模型研究，同时，量化、稀疏化方法使得模型压缩同样重要，这些研究路线都大有可为，也需要各种不同学科背景的人才参与进来。

##

## **3. “没团队帮忙，差点就赶不上投稿了”**

该成果一作 Hunter 同学为豆包大模型团队语音组实习生，此前，他还是字节跳动奖学金计划入选者。IR-QLoRA 之前， Hunter 同学已参与过一期校企项目。

此番合作，由 Mentor 提出课题方向——面向 LLM 部署的低比特压缩方案， Hunter 同学提出初步设想及模型设计，完成模型实现，另一位共同一作 Macaronlin 同学是竞赛出身，主要负责大规模工程问题、公式代码对齐与调优，并通过解决大量繁琐工作，让代码更鲁棒、适配性更强。

据 Hunter 同学分享，团队提供了非常大力度的支持，无论计算资源，还是自由度，科研院校及其他机构都很难给到。他感慨道，“在场景探索、数据集使用、Pipeline、如何合理调用预训练模型等方面，公司其他人给到很多实用建议”。

“这也是能赶在 ICML 截止日期前 2 天提交成果的原因之一”，他补充道，“由于模型跑一次需要很长时间，没有团队帮忙，差点就赶不上了”。

**对于团队氛围， Hunter 同学认为，第一个关键词是自由度。**

据他回忆，团队课题大方向强调落地价值，不过工作中，并不强求一定要达到某个指标，而是提倡大家充分讨论，确立一个合理、新颖、有价值的具体目标，不会直接把工程问题拿来让实习生及高校合作方解题。

“好目标是成功的一半，公司在研究探索方面给到我们充分尊重”， Hunter 同学说道。

**自由度之外，对于研究工作，团队也保有长期耐心。**

Hunter 同学分享道，项目一开始他们进展较少，但 Mentor 及团队给到充分探索空间，研究路线也允许实习生灵活选择。“这种耐心，从心理上让实习生感受到了极大支持”，他补充道。

**最后，组织管理方面也相对灵活。**

以此番 ICML Oral 成果为例，两位主要参与的同学并非同一导师，但在理论研究和代码、工程实现方面各有优势，于是，团队将我们组织起来，并联合更多在校同学、导师一同参与，更快拿到了成果。

Hunter 还表示，字节跳动拥有大量来自全球不同背景、不同技术方向的 Top 人才，这使得团队在大模型方面有很好的研究品位，氛围也更开放。

**除却本次中选的 IR-QLoRA，字节跳动同学在 ICML 2024 中选论文还包括：**

> Outlier-aware Slicing for Post-Training Quantization in Vision Transformer

> video-SALMONN: Speech-Enhanced Audio-Visual Large Language Models

> Two Stones Hit One Bird: Bilevel Positional Encoding for Better Length Extrapolation

> Self-Infilling Code Generation

> Diffusion Language Models Are Versatile Protein Learners

> Protein Conformation Generation via Force-Guided SE(3) Diffusion Models

> Boximator: Generating Rich and Controllable Motions for Video Synthesis

> MagicPose: Realistic Human Pose and Facial Expression Retargeting with Identity-aware Diffusion

> GroupCover: A Secure, Efficient and Scalable Inference Framework for On-device Model Protection based on TEES

> InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks

> Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning

> Bridging Model Heterogeneity in Federated Learning via Uncertainty-based Asymmetrical Reciprocity Learning

ICML 2024 期间，字节跳动也将在现场设立展台，部分机器学习、深度学习领域的同学将赴维也纳参会。现场展示成果与 Demo 包括：ByteGen 、DepthAnything2 、SeedTTS 、DPLM等。**我们的展位信息是：Booth Number 107 ，****欢迎****大家来到****现场****和我们****交流。**

目前，豆包大模型团队持续招聘中，我们希望吸引和招募目标远大、有志于“用科技改变世界”的顶尖人才。**欢迎点击阅读原文了解相关信息。**

**注：本文同学均使用化名。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugP4pgV3m4sm7iaL5YQKnwzVgzXsgicVupQ16FZVjotMEEWqjAnxM635ibmJrVpYDJMWT8H2KUQ1612w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugP4pgV3m4sm7iaL5YQKnwzVdPUCHlTJEzndVMXjEPMGxmATWibaqDhP61nmFuxTf1b40OR3hCUjVAg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=MzkzMDY5MzYxNg==&mid=2247485069&idx=1&sn=30afd04359a223a4786e2098ad9c86c8&chksm=c2772e12f500a704917eb78538a802e35d91d1b070c6fa48a87d47b035c1c8fae9073000477a&scene=21#wechat_redirect)[![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugoPxyC3kKz6FBQyu4XRwibNeDAia52bianoHXZSqQ4APYI7dWibv3BLgy8uUrQicmhQH5FrGIvbQ6MBgg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=MzkzMDY5MzYxNg==&mid=2247484993&idx=1&sn=10b3b6e1261b957de9391c72e7c401bc&chksm=c2772edef500a7c8c4231405...