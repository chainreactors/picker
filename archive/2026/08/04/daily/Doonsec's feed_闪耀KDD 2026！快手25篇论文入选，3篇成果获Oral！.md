---
title: 闪耀KDD 2026！快手25篇论文入选，3篇成果获Oral！
url: https://mp.weixin.qq.com/s/-19qLuewGsL_Cyt9Dsc6Rg
source: Doonsec's feed
date: 2026-08-04
fetch_date: 2026-08-05T04:55:01.574523
---

# 闪耀KDD 2026！快手25篇论文入选，3篇成果获Oral！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1U1S4zST10b4fU4ClrLfmFHZLAzibsvicUayuJbaJnDknFibZusQJCeicIO73Em1G5jaFwXjsYlSKMfyJDmxINtlkDjE5ElmhUb18A/0?wx_fmt=jpeg)

# 闪耀KDD 2026！快手25篇论文入选，3篇成果获Oral！

快手技术
快手技术

快手技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=0)

KDD 2026（The 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining），是数据挖掘与知识发现领域历史最悠久、最具影响力的顶级国际学术会议之一，被中国计算机学会（CCF）推荐为 A 类会议。会议将于2026年8月9日至13日在韩国济州岛国际会议中心（ICC Jeju）举行。

此次会议，快手技术团队 25 篇论文入选，其中 3 篇 Oral，论文覆盖生成式推荐、自动出价、直播推荐、多行为建模、因果推断、搜索排序、大模型与 Agent、观看时长预测等核心方向。不同于停留在理论层面的技术探索，这些成果均扎根于快手亿级用户、千亿级交互场景的真实业务实践：生成式推荐已在大规模广告系统中稳定落地，基于扩散模型的自动出价开辟了新的技术范式，语义 ID 碰撞难题得到有效破解，用户满意度与搜索体验实现协同提升。这一系列成果，集中展现了快手从技术突破到业务落地的持续创新能力。

此外，快手技术团队将亮相现场，展位号【30】。欢迎打卡快手技术展位，领取限定版冰箱贴！活动现场还准备了丰富的互动游戏，参与 Embedding 猜图挑战，就有机会赢取飞盘、手办等周边。更多趣味玩法，等你来解锁！

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XKq9OWxUibcwvTkZ0UIDBhw4MoND5yDj1mxhPBMBMppXpk1iaPmOo5ibr3pkVedRrUv9F2HHjlF5KCUXNNmO2icfPEOz5iabFOlNEo/640?wx_fmt=png&from=appmsg)

以下为入选论文的核心内容与技术亮点解读。

01

FlowTime: Towards Continuous Generative Watch Time Prediction via Flow-based Personalized Priors (Oral)

论文地址：

https://arxiv.org/abs/2606.01352

论文简介：本文聚焦短视频推荐中的观看时长预测问题。现有回归、序回归和离散生成方法难以刻画用户—视频交互中的多峰分布与个性化差异，容易出现均值塌缩、量化误差或推理延迟高等问题。为此，论文提出连续生成回归新范式，并设计 FlowTime 框架：通过一步式 VAE 保证在线推理效率，同时引入基于 Normalizing Flows 的个性化先验，将用户和视频历史行为映射为模式相关的潜在流形，从而更准确建模复杂观看行为。实验结果表明，FlowTime 在多个公开与工业数据集上优于现有 SOTA，并在真实线上 A/B 测试中提升播放时长、使用时长、长观看率和分享率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1VwLaic7adgfC5vTxyJOkPiavyMEtRXeUOiarXkZf8E9cTrcY2XUDlGTIGTLVfvYXBicO5xIRG08HA5StWchAn8NSjvCRwgdYRoaWA/640?wx_fmt=png&from=appmsg)

02

Generative Recommendation for Large-Scale Advertising (Oral)

论文地址：

https://arxiv.org/abs/2602.22732

论文简介：生成式推荐（Generative Recommendation）近期因其在扩展性和模型容量方面的潜力，在工业界引起了广泛关注。然而，在大规模广告场景中部署实时生成式推荐，需要超越大语言模型（LLM）式训练与服务范式的设计。我们提出了一个面向生产环境、在架构、学习与服务三方面协同设计的生成式推荐系统，命名为 GR4AD（Generative Recommendation for ADvertising，广告生成式推荐）。在 Tokenization（分词/编码）方面，GR4AD 提出了 UA-SID（Unified Advertisement Semantic ID，统一广告语义 ID），用于刻画复杂的业务信息。在解码方面，GR4AD 引入了 LazyAR（懒惰自回归解码器），它放松了层间依赖，用于短序列、多候选的生成场景，在保持效果的同时降低了推理成本，从而使模型在固定服务预算下具备可扩展性。为了将优化目标与业务价值对齐，GR4AD 采用了 VSL（Value-Aware Supervised Learning，价值感知的监督学习），并提出了 RSPO（Ranking-Guided Softmax Preference Optimization，排序引导的 Softmax 偏好优化）——一种排序感知、列表级的强化学习算法，能够在列表级指标下优化基于价值的奖励，支持持续的在线更新。在线推理方面，我们进一步提出了动态束搜索服务（dynamic beam serving），可根据生成层级与在线负载自适应地调整束宽，从而控制计算开销。大规模在线 A/B 实验表明，相较于现有的 DLRM（Deep Learning Recommendation Model）技术栈，GR4AD 带来了最高 4.2% 的广告收入提升，且模型扩展与推理时扩展均带来了稳定收益。目前 GR4AD 已在快手广告系统全量部署，服务超过 4 亿用户，实现了高吞吐的实时在线服务带来了稳定收益。目前 GR4AD 已在快手广告系统全量部署，服务超过 4 亿用户，实现了高吞吐的实时在线服务。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XoUialx4k3fzNADacu25NXaJj9HbndsnibPPHP9YNibVoqpZj9wwNHJDzS7s8tt8FX1JazDZYOzbVfLCS4XFVK6IAneu6czmU9L0/640?wx_fmt=png&from=appmsg)

03

HOBA: Hierarchical On-Policy Bidding Agents for Adaptive Online Advertising (Oral)

论文地址：

https://arxiv.org/abs/2607.24779

论文简介：本文聚焦在线广告自动出价中的自适应决策问题。现有工业出价系统多依赖 PID、MPC、离线强化学习等专家模型，但在非平稳竞价环境下，固定策略难以及时适应市场变化，同时出价边界、预算节奏等关键超参数仍高度依赖人工调优。为此，论文提出 HOBA（Hierarchical On-Policy Bidding Agents），一种层次化多智能体自动出价框架。HOBA 将出价决策拆解为三个层级：高层由大语言模型基于广告计划状态和历史经验生成小时级超参数约束；中层由结合因果校正的 SARSA 智能体动态选择最合适的专家模型；底层由 PID、MPC、IQL、Decision Transformer 等专家池执行具体出价。该设计将在线学习限制在离散专家选择层，避免直接探索连续出价空间，在提升市场适应能力的同时降低线上探索风险。实验结果表明，HOBA 在 AuctionNet 基准上稳定优于多类自动出价方法，并在大规模线上 A/B 测试中验证了业务有效性和部署可行性。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1U3WSk5icRUxicDPmxeva4VR235qIkuEanibQDEtaVXJHWG0ANUicgqPiaqIIWH4RiakQtoXsARmCFmmKqzyN5WxmCrYgFALdaarEP38/640?wx_fmt=png&from=appmsg)

04

Atomic Intent Reasoning: Bringing LLM Semantics to Industrial Cross-Domain Recommendations

论文地址：

https://arxiv.org/abs/2606.10357

论文简介：本文提出了 AIR（Atomic Intent Reasoning），一个面向工业级跨域推荐场景的大模型语义增强框架，核心目标是在内容到电商的推荐链路中，利用用户在短视频、直播等内容侧行为推断其潜在消费意图。针对传统跨域推荐语义理解能力不足、在线调用大模型延迟过高、用户跨域行为序列长且噪声大的问题，AIR 将大模型推理前置到离线阶段，生成细粒度的“行为—意图”原子单元，并在在线阶段通过实时意图树构建、目标商品感知的意图检索和多头注意力融合，实现毫秒级的语义推理与CTR建模。实验结果表明，AIR 在 Amazon 公开跨域推荐数据集上取得了优于现有方法的效果，并在快手电商真实线上 A/B 测试中带来了 GMV +3.446%、GPM +3.662% 等核心业务指标提升，同时相比直接在线调用 Qwen3-4B 实现约 400× 的吞吐提升，验证了其在大规模工业推荐系统中的有效性和部署价值。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1VBialiciavW5M2MqrArgdZS6Qya7lDkiboGrSfrouzImnL5iaeOuRJpuBOLUYogwFTTiaHicmhOSBLMDzbYvWNMhnPTYTAkDmicbzicBow/640?wx_fmt=png&from=appmsg)

05

Breaking the Likelihood Trap: Consistent Generative Recommendation with Graph-structured Model

论文地址：

https://arxiv.org/pdf/2510.10127

论文简介：重排作为推荐系统的最终环节，对最终曝光结果起到决定性作用，直接影响用户体验。近年来，生成式重排方法备受关注，该思路将重排任务定义为完整序列生成问题，可隐式建模物品间复杂关联。但现有多数生成式重排方法均存在似然陷阱：模型生成的高似然序列往往高度重复，在人类感知中质量偏低，最终制约用户互动效果。本文提出一致图结构生成推荐模型（Congrats）。首先，我们设计一种全新图结构模型，通过多条生成路径的探索，产出更多样化的推荐序列。该架构一方面拓宽解码空间、提升序列多样性；另一方面借助图状态转移显式建模物品间依赖关系，提升预测精度。除此之外，本文配套设计一致性可微分训练方案，引入评估器模块，让模型能够直接基于用户偏好完成学习。大量离线实验证明，Congrats 相较于当前最优重排方法具备更优异的性能。同时，我们在快手完成大规模线上验证，结果表明该方法可同时显著提升推荐质量与推荐多样性，证实其在工业级真实业务平台具备实用价值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1XB3Qibv0lgkHk6zFU0r95bC9bibxsibwiaA6pYiaKicxk32Xkicoz4y9zgRbLxNcPScktoLO4Q95DezeQqUphbo7lAIxlNFKxgf13I3U/640?wx_fmt=png&from=appmsg)

06

Breaking the Listwise-Shuffle Dilemma: A Streaming-Compatible Listwise Framework for Industrial CTR Prediction

论文地址：

https://openreview.net/forum?id=UVBc3KwapH#discussion

论文简介：本文聚焦短视频搜索排序中的核心任务——点击率（CTR）预估，使其能够从时间维度和空间维度进行自我纠正与演化。尽管 Listwise 学习与排序指标具有更高的一致性，但在工业级流式训练中仍较少被采用，其关键障碍在于 Listwise–Shuffle 困境：Listwise 目标依赖会话（session）级聚合监督，而稳定随机优化又要求对训练样本进行充分打散（shuffling），二者天然冲突。为此，我们提出解耦式 Listwise 学习（Decoupled Listwise Learning, DLL），一种面向流式训练的 Listwise 优化范式。DLL 无需按会话组批，而是将目标物品的当前训练分数与部署模型在服务（serving）阶段记录的上下文预测相结合，在完全打散的单遍（one-pass）更新中重建会话级监督信号并实现 Listwise 优化。进一步地，考虑到重建后的 Listwise 信号更依赖上下文信息，且对短期非平稳性更敏感，我们引入边界正则化自校正（Margin-Regularized Self-Correction, MRSC）。MRSC 以依赖标签的非对称边界（margin）替代零容忍的一致性约束，在容忍良性预测波动的同时，重点惩罚具有实际排序影响的性能回退。大规模商业流式 CTR 场景实验表明，该方法带来离线 GAUC 提升 0.95 个百分点，在线 CTR 提升 2.71%，有效播放率（EPR）提升 4.55%。目前，该方法已部署于日均服务数千万查询的生产级短视频搜索系统中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1Xt54YloTze6lRbN2FKfIiaP5w68ERyzqrzK8aHNXVjoP8f731FZ8I9HSkDD4CNteJmNPJ7391VfBkcoEcY0XaKPwo9Xfria6Gq8/640?wx_fmt=png&from=appmsg)

07

Denoising Implicit Feedback for Cold-start Recommendation

论文地址：

https://openreview.net/pdf?id=AUIqpjo9zE

论文简介：针对冷启动场景更容易产生噪声样本的问题，本文提出了一种与模型无关的去噪方法 DIF。首先，用户对内容的偏好具有稳定性，因此能够通过与冷启动物品内容相似的热门物品，推断出反映用户是否对该冷启动物品感兴趣的伪标签。进一步地，为了提升伪标签的准确性，本文基于冷启动物品与热门物品之间的内容相似度对伪标签的置信度进行建模，并对每个样本的多个伪标签进行聚合。最后，综合考虑样本的相对熵以及物品的冷启动状态，显式估计噪声样本标签的不确定性，从而在样本层面自适应地引导伪标签对噪声标签进行修正。DIF 的优越性既有理论依据的支撑，也在真实数据集上得到了实验验证，同时取得了在线收益。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1VIoj6ibHlHQbV8ibrBM7W8sWtahPwslyeY1bI1aiaWJVNwkFiaNl3lDE0kkaGyWuyXlvQDTW86Y8EeB1rhnRRdZLzP88wiaVCu43yw/640?wx_fmt=png&from=appmsg)

08

DiffoR: A Unified Continuous Generative Framework for Universal Ordinal Regression

论文地址：

https://arxiv.org/abs/2606.07599

论文简介：本文聚焦通用序回归问题，即如何预测具有天然顺序但间隔并不均匀的目标值。现有方法多依赖离散化分类、排序分解或离散生成，容易受到量化误差、刚性边界和缺乏全局序关系建模的限制，难以刻画相邻序值之间复杂、非平稳的语义过渡。为此，论文提出连续生成式序回归新范式，并设计统一框架 DiffoR：将序回归建模为基于扩散模型的连续值恢复过程，通过多尺度增量聚合刻画从粗到细的层级序结构，再利用动态去噪感知将不同语义粒度与去噪阶段对齐。实验在图像美学评估、人脸年龄估计、观看时长预测和用户生命周期价值预测等四类任务、12 个基准数据集上展开，结果表明 DiffoR 在精度、排序相关性和泛化能力上均优于现有 SOTA 方法。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1Wns8kjNhHSagiau2I3SMWKWW3Vwmlko8JEgRPKZRZ9asd77ibBNTfue4s1XyTqIvkUkkibpowJHMl8EV8iad6mxib0k2PZaZjcuNTI/640?wx_fmt=png&from=appmsg)

09

FARM: Frequency-Aware Model for Cross-Domain Live-Streaming Recommendation

论文地址：

https://arxiv.org/abs/2502.09375

论文简介：直播服务凭借实时互动性和娱乐性，已成为重要的内容消费场景。用户可以通过弹幕、点赞、评论、送礼等方式与主播互动，表达兴趣与支持。然而，直播推荐面临严重的数据稀疏问题：一方面，点赞、评论、送礼等高价值行为本身较为稀疏，容易被模型忽略，难以充分刻画用户的个性化偏好；另一方面，平台主要曝光内容仍以短视频为主，短视频曝光量约为直播曝光量的 9 倍，导致仅依赖直播域难以完整建模用户兴趣。为此，我们提出 FARM：一种面向跨域直播推荐的频率感知模型。FARM 首先基于离散傅里叶变换设计域内频率感知模块，使模型能够捕捉稀疏但高价值的用户行为信号；随后提出“先对齐、再融合”的跨域偏好迁移策略，通过对比学习对齐短视频域与直播域中的用户偏好，并结合定制化注意力机制进一步融合跨域兴趣表示。离线实验与快手直播场景中的在线 A/B 测试均验证了 FARM 的有效性。目前，FARM 已部署于快手直播推荐服务，服务数亿用户。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUs...