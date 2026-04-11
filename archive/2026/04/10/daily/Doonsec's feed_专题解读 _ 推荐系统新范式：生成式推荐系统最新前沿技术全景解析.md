---
title: 专题解读 | 推荐系统新范式：生成式推荐系统最新前沿技术全景解析
url: https://mp.weixin.qq.com/s/aT44wak1iS_T0sVr11Kj3w
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:19:34.977756
---

# 专题解读 | 推荐系统新范式：生成式推荐系统最新前沿技术全景解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6gtnxe1uggH8YkfwNlRWrZxsLyHUaxI7xiam0XLuXZyygMzscBRiaVdHAQZdNTwNjfzPTJmPHj0IreNyUpQu4zJ3tBttsI9SYmwdYAiaDVbXWI/0?wx_fmt=jpeg)

# 专题解读 | 推荐系统新范式：生成式推荐系统最新前沿技术全景解析

包骏飞
包骏飞

北邮 GAMMA Lab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近年来，受大语言模型（LLM）的启发，**生成式推荐系统（Generative Recommendation, GR）**正逐渐成为推荐系统领域的新星。与传统的“召回-粗排-精排”级联架构或纯粹的判别式模型不同，生成式推荐通过将用户历史序列转化为离散的 Token，以“自回归”或“序列生成”的方式直接生成用户可能感兴趣的物品 ID。

今天，我们将带大家深度解读该领域三篇极具代表性的最新论文，分别从**统一召回排序的端到端生成**、**大规模判别式推荐的生成式预训练**以及**多模态融合量化**三个维度，全面拆解生成式推荐的前沿进展。

## 一、OneRec：统一召回排序的端到端生成与偏好对齐

*论文名称：OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment*

### 1. 背景

现代主流的工业推荐系统往往采用级联的“召回-排序”策略，生成式模型通常仅在召回阶段充当选择器。

### 2. 解决的主要问题

传统的 NLP 场景下可以通过人类反馈直接进行偏好优化，但推荐系统中缺乏同时获取正向和负向样本的机会。级联系统也将各个排序阶段割裂开来。此外，点对点（Point-wise）的生成方式缺乏对会话连贯性的感知。

### 3. 架构设计

本文提出了 **OneRec**，这是一个用统一的生成模型取代级联学习框架的端到端系统。

![OneRec架构图](https://mmbiz.qpic.cn/sz_mmbiz_png/6gtnxe1uggEOSsibHydNTAACPYFVjllXNxVul0eGiaNicSic6LFEjKDqmsC6gse99B4drkyQhaibQ8xXic8umlEe4xgbswNOAZRndGuxxbzpZQfxw/640?wx_fmt=png&from=appmsg)

OneRec架构图

* **统一架构与 MoE 扩展**：将用户行为序列送入 Encoder 并在 Decoder 逐步生成视频。为了在不按比例增加计算量的情况下扩大模型容量，引入了**稀疏混合专家（Sparse MoE）机制**；
* **会话级（Session-wise）生成**：采用生成整个会话的方式，比点对点的生成更能保持上下文的一致性与连贯性；
* **迭代式偏好对齐（IPA, Iterative Preference Alignment）**：设计了一个奖励模型来模拟用户生成，并据此定制采样策略，结合 DPO（直接偏好优化）来提高生成质量。

### 4. 实验分析

![OneRec离线性能测试](https://mmbiz.qpic.cn/mmbiz_png/6gtnxe1uggGe0AVZWlLlwPCcUarPDx67TdtLvHradObXUMicciawrNdjPgP19yJia1hbPN78Abia4gYawoy5sBIFmKicZJWAg1FhgQ7rMDxjBpgk/640?wx_fmt=png&from=appmsg)

OneRec离线性能测试

![OneRec A/B测试](https://mmbiz.qpic.cn/sz_mmbiz_png/6gtnxe1uggGD1wnhFvZNtDD62WfwDrsjWVGvt970oBNLekzbluZB7822BmI6an8VEibZ55I0icCw0da7JfgXOXUdficlXc0mYtLzIBdOw3z3bg/640?wx_fmt=png&from=appmsg)

OneRec A/B测试

* **偏好对齐收益**：实验证明，仅使用数量有限的 DPO 样本进行训练，就能有效对齐用户的兴趣偏好，并大幅提高生成结果的质量。
* **大规模线上验证**：该模型在快手的主场景中部署上线，实现了**观看时长 1.68% 的增长**，这是一个具有重大商业价值的提升。

## 二、GPSD：用“生成式预训练”打破判别式推荐的缩放定律瓶颈

*论文名称：Scaling Transformers for Discriminative Recommendation via Generative Pretraining*

### 1. 背景

在工业级的大规模推荐系统（如点击率 CTR、转化率 CVR 预测）中，判别式模型在排序阶段占据着主导地位。为了提升模型能力，业内希望引入强大的 Transformer 架构。

### 2. 解决的主要问题

研究人员发现，在判别式推荐任务中直接训练 Transformer 会遇到**极其严重的过拟合问题（Overfitting）**，这主要由推荐数据的稀疏性引起。这种过拟合导致了一个致命后果：**模型参数量越大，效果反而可能不如小模型**，违背了在语言模型中广泛生效的“缩放定律（Scaling Laws）” 。相反，生成式训练（Generative Training）的自回归模型却没有明显的过拟合迹象 。

### 3. 架构设计

为了解决这一问题，作者提出了 **GPSD（Generative Pretraining for Scalable Discriminative Recommendation）** 框架。

![GPSD架构图](https://mmbiz.qpic.cn/sz_mmbiz_png/6gtnxe1uggG1oreWG5kMP0EaXXvIFcjpJRApZ8SqvwThAmFMUgeSriaeE9iculmNWqiaibn1VR1ZDfPlxaqoapqN7ZbzOD9AMArfptCvSGtkHpI/640?wx_fmt=png&from=appmsg)

GPSD架构图

GPSD 框架主要包含以下核心机制：

* **生成式预训练与桥接策略**：利用预训练的生成式模型参数来初始化判别式模型，随后应用稀疏参数冻结策略（Sparse Freeze）。
* **判别式微调**：通过仅对密集参数（Dense层）进行训练，框架极大地减少了模型对稀疏特征的过拟合倾向。

### 4. 实验分析

![GPSD模型缩放实验](https://mmbiz.qpic.cn/sz_mmbiz_png/6gtnxe1uggEzQfib6EwoXwe6ibyWGFYwc3m0d5vJpcCFGIBOc4UX6VOKsJcUCGvYRxF92aqxusiauVm2X87FqY0ymAPDNlV9u3fEsu6nHy6Acc/640?wx_fmt=png&from=appmsg)

GPSD模型缩放实验

* **克服过拟合与实现 Scaling Law**：实验表明，GPSD 成功消除了推荐模型训练中特有的过拟合现象。当模型的 Dense 参数从 13K 放大到 0.3B 时，性能呈现出一致的提升，**紧密遵循幂律（Power Laws）** 。
* **工业级收益**：在真实线上 A/B 测试中，该框架在核心商业指标上均取得了显著提升。

## 三、MACRec：引入多模态感知的跨模态量化生成式推荐

*论文名称：Multi-Aspect Cross-modal Quantization for Generative Recommendation*

### 1. 背景

生成式推荐（GR）依赖于将物品特征离散化为量化的表示形式，进而把用户的历史交互建模为离散 Token 序列。通过预测下一个 Token 的方式，模型能够输出推荐物品。

### 2. 解决的主要问题

现有的 GR 方法在构建语义 ID（Semantic IDs）时通常面临局限性。**仅仅依赖单一模态**会导致语义区分度不足。例如：同一个品牌的不同乐器，其文本特征很近，降低了物品的区别度 。此外，常用的残差量化方法在深层中容易丢失语义。

### 3. 架构设计

作者提出了 **MACRec (Multi-Aspect Cross-modal quantization for generative Recommendation)** 框架，将多模态信息引入到语义 ID 的学习和生成模型的训练中。

![MACRec架构图](https://mmbiz.qpic.cn/mmbiz_png/6gtnxe1uggFfAnopzOrkg7jjckfRiaZO6IDXiavwe314M8pR3gicia3GtSVhCBW42xMUN9RnGIMXVEu5ufPaiahFmdHjzYsUGpOKGT6uYicg58vdY/640?wx_fmt=png&from=appmsg)

MACRec架构图

* **跨模态物品量化**：在生成语义 ID 的阶段，引入了基于对比学习的**跨模态量化**。例如，使用视觉伪标签来优化文本模态的残差，反之亦然。
* **多维度对齐的生成推荐训练**：在生成模型训练阶段，增加了隐式对齐和显式对齐机制，强迫模型学习跨模态的共享特征。

### 4. 实验分析

![MACRec实验对比](https://mmbiz.qpic.cn/mmbiz_png/6gtnxe1uggFqZbnfHc13VK1yUOGu6qR6ibIY16KTcJ6X7Hhp6CPY3oarPR1yQusz5iareaj6aLNbPvBA4Nqap3ticnKibo5FPnLMSjbL7N48TfQ/640?wx_fmt=png&from=appmsg)

MACRec实验对比

* **性能全面领先**：在亚马逊的三个公开推荐数据集上，MACRec 显著优于现有的最先进基线模型。
* **降低冲突率与优质对齐**：量化过程中融入了跨模态对比学习，充分利用了模态间的互补性，成功降低了语义 ID 的冲突率（Conflict Rates）并提升了Codebook的可用性。

## 结语

从**OneRec** 吹响端到端大一统推荐系统革命的号角，到 **GPSD** 打破数据稀疏带来的 Scaling Law 瓶颈，再到 **MACRec** 在跨模态特征上的精雕细琢，生成式大模型或将彻底重构现代推荐系统的技术栈。

本期责任编辑：杨成

本期编辑：赵明宇

**北邮 GAMMA Lab 公众号**

主编：石川

责任编辑：杨成

编辑：赵明宇

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AYxz3cIHvyoiayibng0FojESWtukKaO5zH1D94qCSeOjkzZpNfKoYddl1n8FJ7j610Wa5W4BSTtwBa4Y0QsC8d7Q/0?wx_fmt=png)

北邮 GAMMA Lab

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AYxz3cIHvyoiayibng0FojESWtukKaO5zH1D94qCSeOjkzZpNfKoYddl1n8FJ7j610Wa5W4BSTtwBa4Y0QsC8d7Q/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过