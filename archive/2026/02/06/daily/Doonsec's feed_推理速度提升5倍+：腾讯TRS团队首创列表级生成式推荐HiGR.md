---
title: 推理速度提升5倍+：腾讯TRS团队首创列表级生成式推荐HiGR
url: https://mp.weixin.qq.com/s/z5cyuqsOLCYiErOvq5QJwA
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:07:17.992993
---

# 推理速度提升5倍+：腾讯TRS团队首创列表级生成式推荐HiGR

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KVER9adz907RwFYqAwJS9iaCj6fPiac14Frj6JzJvicNpeicwxMel66dibKGrgbqTF2s1MllvyecOY9sS95FBTnaZYyT0oCSzl1aXIV4ot6amP74/0?wx_fmt=jpeg)

# 推理速度提升5倍+：腾讯TRS团队首创列表级生成式推荐HiGR

原创

腾讯程序员
腾讯程序员

腾讯技术工程

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

作者：李裕东 庞雲升 刘子健

### 导语

在信息流、短视频、电商等推荐场景中，用户真正感知的并非某一条内容的相关性，而是一整屏列表带来的「整体体验」。 为此，腾讯TRS团队在论文《HiGR: Efficient Generative Slate Recommendation via Hierarchical Planning and Multi-Objective Preference Alignment》中提出分层规划的端到端生成式推荐框架HiGR，将传统的级联推荐范式升级为「编码—规划—生成—对齐」的一体化新范式

* 先做**列表级意图规划**
* 再做**物料级生成解码**
* 最后通过**列表级偏好对齐**，直接面向**隐式反馈**优化整列质量

该方法已在真实业务场景验证了显著收益：

* 离线推荐质量相对 **SOTA 提升超过 10%**
* 推理速度提升 **5 倍以上**
* 线上小流量 **A/B 实验**验证：用户观看时长与消费深度均有显著增长

**HiGR**首创基于“**编码—规划—生成—对齐**”的列表级端到端生成式推荐一体化范式，为业务提供了一条**高性能、可规模化落地**的生成式推荐升级路径。

### 1. 为什么“列表级端到端”是下一代推荐的关键

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz90701gLRMfjE07IPu1QuicbiaFrb6h2Rjbwe9ficugnu5eawJfsWPDgRhW5Nr4dLYfxfuyK4l8dUUxmuekbeskjF5IEEwCKrrqUOibc/640?wx_fmt=png&from=appmsg)

传统的推荐系统通常采用级联架构（召回 -> 粗排 -> 精排 -> 重排），虽然这种漏斗式结构在基于CPU的计算效率上具有优势，但存在三个核心痛点：

* **目标不一致**： 级联推荐架构下，召回、粗排、精排这些层的模型都在优化点对点（Pointwise）的准确率，而用户最终消费的是一个列表（Listwise），局部最优并不等于全局最优。
* **误差累积**： 级联推荐架构下，上游模块的偏差会层层传递，导致重排阶段只能在有限且可能已经“偏航”的候选中进行微调。
* **GPU算力利用不足**： 如下图所示，单位成本下GPU计算性能每年在翻倍提升，未来确定性的趋势是GPU性能还会持续提升，而传统推荐模型的算力利用率（MFU）普遍偏低（大多不到1%）；相比之下，大语言模型领域已验证更高 MFU 的工程可达性，LLM的模型算力利用率（MFU）可以达到70%，推荐系统仍有显著“算力红利”空间。

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz907jC6Tu6wqAA1jdcVOPbAJJ3BVSNyncpvEnT26FCQStBlU3TpD9EIzyqSH0Kp5H40knskMTBEiaVJBL4Q9cIDXX4YuxGSChFRlo/640?wx_fmt=png&from=appmsg)

因此，业界都在积极探索端到端生成式推荐范式（比如OneRec，OneRec-Think等），期望进一步突破推荐模型的天花板，但当前大多数生成式推荐的研究还是基于NTP (Next Token Prediction) 范式，即像语言模型一样逐个 Token 地预测物料，这种方式在推荐场景下面临两个挑战：

* 推理效率受限： 自回归逐Token生成在推荐场景中面临严峻的延迟瓶颈。以生成一个包含10个物料的推荐列表为例，若每个物料ID需要4个Token表示，则需要40步自回归解码，难以满足在线推荐的毫秒级响应要求。
* 缺乏全局规划： NTP范式本质上仍是Token级别的交叉熵损失，与用户对整个推荐列表的隐式反馈（如停留时长、滑动深度）之间存在Gap，难以直接优化列表级用户体验。

为了突破这些瓶颈，我们提出了分层规划的端到端生成式推荐框架HiGR，其核心思路是从“逐 Token 填充”转向“分层规划与整列对齐”，先在列表层做“意图规划”（Plan），再在物料层做“生成解码”（Generate），最后用“列表级偏好对齐”（Align）把整列质量直接对齐业务指标。

### 2. HiGR一体化框架：从“编码—规划—生成—对齐”闭环优化整列质量

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz907unMyp7Se6LV16qSzy3b1ibwHxm2pyXhIEZ0NPMcONyiby77UU6GS4b3ITIo3EGFQNN4H4OvpibvJo6wxHACPnDrVE2Q3hXiaicSJI/640?wx_fmt=png&from=appmsg)

如上图所示，HiGR 框架主要包含三个核心模块：

* **语义编码**：提出 CRQ-VAE，解决前缀 ID 纠缠与残差坍塌
  针对 RQ-VAE 存在的 ID 纠缠和残差坍塌的问题，CRQ-VAE 引入对比学习和全局量化约束：

+ **前缀对比学习**：设计 InfoNCE loss 强制前缀 ID 成为语义锚点，实现“前缀聚类，后缀区分”，确保分层规划器能准确捕捉意图
+ **全局量化损失**：构造全局损失替代逐层累计损失，深层码本也能承载有效信息，保证语义 ID 表达的一致性

* **分层规划**：提出 Hierarchical Slate Decoding（HSD）先“定大局”，再“填细节”
  为了解决自回归生成的延迟问题并引入全局视野，HiGR 将生成过程解耦为两步：

+ **Layer 1：列表级意图规划（Corase-grained Slate Planner）**：模型首先不直接预测具体的视频 ID，而是根据用户的交互历史，生成一个“列表意图蓝图”（Slate Intent）。
+ **Layer 2：物料级生成解码（Fine-grained Item Generator）**：在确定的“列表意图蓝图”指导下，模型并行地填充具体的物料语义 ID。

* **列表级偏好对齐（Listwise Preference Alignment）**：用隐式反馈“直接优化整列体验”
  为了突破预训练“只能拟合分布，无法区分优劣”的局限，同时解决当前强化学习工业落地瓶颈，HiGR 采用了 ORPO 算法：

+ **免参考模型**：结合 SFT 和 Odds Ratio 损失，在单模型架构下实现偏好对齐，大幅降低显存占用和训练延时
+ **三元目标样本构造**：通过构造针对性样本对，同步优化保序性、真兴趣和列表多样性

#### 2.1语义编码：CRQ‑VAE 如何解决“语义ID纠缠”并让前缀可控

在生成式推荐中，我们物品ID化（tokenization）的质量直接决定了后续生成模型的上限。传统的RQ-VAE模型虽然能降低词表大小，但在工业落地中暴露出了“前缀语义纠缠”与“残差坍塌”的两大核心问题，导致生成模型难以精准把控推荐意图。

##### 2.1.1 痛点深入：为什么传统的Semantic ID不好用？

* **ID纠缠**
  在标准RQ-VAE中，量化仅由重构误差驱动。这导致生成的Codebook缺乏语义拓扑结构——前缀相同不一定代表类别相同，而前缀不同的物品却可能非常相似。对于分层规划器来说，如果ID不具有明确的语义聚类特性，它就无法准确地规划出高层的“意图”。
* **残差坍塌**
  随着量化层数迭代，后续层级的残差向量往往趋近于零，导致深层码本实际上不承载信息，退化为噪声，浪费了编码容量。

##### 2.1.2 核心方法：基于对比学习的残差量化编解码器（CRQ-VAE）

我们引入对比学习和全局量化约束，强制让语义ID的前缀成为可靠的语义锚点。

* **前缀对比约束**
  我们在量化器中的前D-1层引入InfoNCE loss，选择语义相似的item或共现率高的item作为正样本，选择批次内其他随机样本作为负样本。让前缀ID负责“聚类”，将相似物品拉到同一个ID前缀下；让最后一层ID负责“区分”，保持对具体物品的细粒度辨识能力。完美契合我们的“先规划，后生成”的分层策略。
* **全局量化损失**
  不同于传统逐层累计的量化损失，我们针对量化器前后的编码向量和量化重构向量构造全局损失，有效抵抗了残差消失现象，迫使深层码本必须承载有效信息，显著提升了ID的表达一致性。

#### 2.2分层解码：HSD 如何先“规划”列表偏好再“生成”具体内容

##### 2.2.1 痛点深入：“平铺”式的解码器为什么不是列表推荐的最优解？

* **推理耗时长**
  在推理耗时极为敏感的推荐场景，传统的“平铺”式解码器，即把SID作为token，逐SID地生成列表难以满足耗时要求，因为推理长度为M的列表需要推理M\*N次（一个item由N位SID表示），使得传统“平铺”式解码器几乎不可能在实际场景中落地。
* **难以建模item内和item间的关系**
  推荐场景中的SID token序列不同于语言模型中语义token序列，其有着明确的边界以及层级关系，如下图所示：假设3位SID构成一个item（<a\_3><b\_6><c\_2>；<a\_5><b\_4><c\_7>），则<c\_2>和<a\_5>有着明确的边界，即<c\_3>属于第一个item，<a\_5>属于第二个item；<a\_3>位于item的第一位，代表着对item更粗粒度的刻画，<b\_6>位于item的第二位，代表对item较细粒度的刻画。传统的“平铺式”解码器更适合建模没有明显边界和层级关系的文本语义token，但却难以捕获推荐场景中item内和item间SID的联系。

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz9053Ej7Xf8sgdy78argLjy07ayUcWH7648ex5NiccDyRSf6f3jxfeg371S2FFGh7jTQ1zgXhkywfr3g0hn5B13gBfN2sP2DUEOicA/640?wx_fmt=png&from=appmsg)

##### 2.2.2 核心方案：基于分层解码的先规划，再生成方案

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j3gficicyOvat7WnGh9azefEFlroq7H0GhfUZkMaLFSfTf9nX5jVH2VxYsCGRD9KrFFyvA9rY02NFLiaUbibEnvUlw/640?wx_fmt=png&from=appmsg)

如图所示，基于分层解码的列表推荐方案将列表级偏好规划与具体的item SID序列生成相解耦，通过先规划，再生成的方式逐步生成列表序列。
具体来说，我们首先采用了一个较重的多层Transformer架构作为Coarse-grained Slate Planner，用于从item的粒度规划列表内用户对每个item的偏好，得到一个用户偏好embedding序列，经过投影映射后，每个item的偏好embedding作为较轻量的Fine-grained Item Generator的起始输入，替换常用的BOS token，指导该item生成具体的SID序列。

通过分层，用一个统一的Coarse-grained Slate Planner来规划整个列表内各item的偏好，再对每个item用Fine-grained Item Generator来生成，实现了规划和生成的解耦，对列表内待解码的某个SID token，其不仅能参考该item内已生成的前缀SID序列，还能参考该列表内已生成的完整前序item表示，提升了模型对item内和item间的建模能力。

相比传统的“平铺”式解码器将整个列表的SID序列都经过一个重量级的Transformer架构，分层解码只需将抽象后的item偏好序列经过较重的Transformer层，而将item解码成SID序列时采用了轻量级的Transformer架构，减少了推理耗时。
此外，在推理时，beam search只在每个item内累积logits概率，而不在整个列表累积，进一步降低了推理耗时。

#### 2.3列表级偏好对齐：ORPO 如何用隐式反馈“直接优化整列体验”

监督微调（SFT）只能让模型学会拟合历史曝光分布，即像传统推荐系统那样推荐，但无法学会“什么是更好的推荐”。为了让模型真正理解用户的隐式偏好，我们需要引入偏好对齐技术。

##### 2.3.1 痛点深入：为什么不用最经典的DPO和最火的GRPO？

在生成式推荐的工业级落地中，直接照搬LLM领域的对齐算法面临显著的效率收益瓶颈：

* **DPO（Direct Preference Optimization）**

+ 机制痛点：DPO的损失包含一项

  ![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz907VMSVsiaPybJictOG5rJuP0rIddMicvKe3vabbOj3jbzcqnVax2tib67gialgc3nVeeVpLRRyia77PicOXXoHftbFDN7ZaH2ed0bPsdk/640?wx_fmt=png&from=appmsg)

  这意味着训练过程中，必须始终加载冻结参数的参考模型进行同步推理。
+ 工业阻碍：推荐模型的参数量虽然不如LLM巨大，但是数据量极大。参考模型的存在导致显存占用翻倍，训练吞吐量减半。在小时级更新的推荐业务中，这种训练延时是不可接受的。

* **GRPO（Group Relative Policy Optimization）**

+ 机制痛点：Deepseek提出的强化学习方法GRPO，通过对同一prompt采样G组输出，计算组内相对优势，从而省去了critic model。其核心假设是环境能对每一次采样给予即时、准确的反馈。
+ 工业阻碍：GRPO在数据、代码任务中有效，是因为有明确的答案检查器。但在推荐场景中，离线训练无法实时把生成的G个推荐列表推给用户，在没有高保真用户模拟器的情况下，GRPO很难直接应用于离线推理策略学习。此外，列表序列推理是token-by-token生成的，生成G组完整列表极其耗时，会导致训练时长爆炸。

##### 2.3.2 核心方案：列表级的多目标ORPO（Odds Ratio Reference Optimization）偏好对齐

1.损失函数设计：

将传统的监督微调损失和Odds Ratio损失结合

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz904fI60ROpV5sI0Imib1B4r2QyChQia4syrVU6eicibL3Aoh7DtR3UOsd2yUusPT4VibFlrKR9hic3dvbPWxOeibOS822CoTJIXC5UwDxc/640?wx_fmt=png&from=appmsg)

* 直观理解：SFT负责让模型学习传统推荐的，而Odds Ratio损失让优势列表的生成赔率显著高于劣质列表。
* 工程收益：这种单模型、单向传播的架构，训练速度与普通SFT几乎持平，显存占用大大降低。

**三元目标”样本构造策略**：
为了解决推荐系统既要准、又要好、还要多样的复杂需求，我们在构造偏好对时采用了特殊的正负采样策略：

* 正样本：用户真实观看且高停留时长的序列，按照反馈强度重排
* 负样本：

+ Ranking Fidelity（保序性）：将重排样本随机打乱顺序。让模型学会“把好东西率先推出来”
+ Genuine Interest（真兴趣）：替换为用户曝光未点击或负反馈的物品。让模型学会剔除“标题党”和无效曝光
+ Slate Diversity（列表多样性）：取正样本中第一个物品作为锚点，后续全部填充与锚点相似的top-k物品。让模型学会惩罚“信息茧房”，主动追求多样性

### 3.实验效果与线上收益

为了验证HiGR在工业级场景下的有效性，我们进行了严格的离线评估和线上A/B测试，以下所有实验数据来自PCG实际内容推荐场景。

#### 3.1 离线评估

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz906bX3qPVBqCWHK8icUR0QFc8EoEibKHpVIYWWZLgZ5zIMCMQYUvFfZA1LuCViawwUkakNuQC6nuqjmnCyibFO2ibEVNibKlLulib8TlZA/640?wx_fmt=png&from=appmsg)

#### 上表展示了HiGR在离线评估中的效果，与传统列表推荐方法和判别式模型相比，HiGR体现了生成式推荐模型的优越性，大幅优于传统模型；与最近提出的经典生成式推荐模型相比，得益于HiGR针对列表推荐的独特优化，HiGR也取得了更好的效果。

#### 3.2 线上A/B测试收益

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz904CVbWbSHgY2kbQ42nd3pYXln3z4gzyxWrKKSlkIQ188ee3vOliaib36r0YricokAAxw14ibBbnQte0ONEDSfPgG9nrN2Bmeica0eQU/640?wx_fmt=png&from=appmsg)

我们将HiGR部署到实际场景的推荐系统中进行A/B实验，与当前的基线模型相比，在播放vv，播放时长和观看时长上均取得了正向显著收益，进一步证明HiGR的有效性。

#### 3.3 Scaling Law实验

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz906pFGDOIE51iadygdbGh8zvicMXt4oicx9LlJxh6Bm9tx3yQOLhL1jzwfnOMZlIyRJcsf1Em8KkYDMQnPEDxpQib2m0ibvmydckHxbY/640?wx_fmt=png&from=app...