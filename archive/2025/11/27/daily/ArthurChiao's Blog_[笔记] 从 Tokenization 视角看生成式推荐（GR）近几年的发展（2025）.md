---
title: [笔记] 从 Tokenization 视角看生成式推荐（GR）近几年的发展（2025）
url: https://arthurchiao.github.io/blog/large-generative-recommendation-tokenization-perspective-notes-zh/
source: ArthurChiao's Blog
date: 2025-11-27
fetch_date: 2025-11-28T03:12:20.175313
---

# [笔记] 从 Tokenization 视角看生成式推荐（GR）近几年的发展（2025）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [笔记] 从 Tokenization 视角看生成式推荐（GR）近几年的发展（2025）

Published at 2025-11-27 | Last Update 2025-11-27

![](/assets/img/large-generative-recommendation-tokenization-perspective/model-as-reflection-of-real-world.png)

| 不同类型的真实世界 | 建模元素 | 对应的模型类型 |
| --- | --- | --- |
| 感知世界（**`Perceptual World`**） | 视觉（Vision） | 扩散模型（Diffusion Models, DMs） |
| 认知世界（**`Cognitive World`**） | 语言（Language） | 大语言模型（LLMs） |
| 行为世界（**`Behavioral World`**） | 交互（Interaction） | 用户行为的模型？ |

从模型和现实世界的对应关系来看，**感知世界**（Perceptual World）和
**认知世界**（Cognitive World）
都已经有了对应的大模型类型，分别基于**视觉**（Vision）和**语言**（Language） 建模，
并且基本都是基于**生成式**架构，实际效果非常好。

推荐领域属于**行为世界**（Behavioral World），
这个场景基于**交互**（Interaction）建模，目前还没有跟前两个领域一样成功的模型。
一个思路是：**如果大量场景已经充分证明了生成式是一把非常好的锤子，
那我们是不是能把还没有很好解决的问题变成钉子**？—— 具体到推荐场景，
就是通过一些工程和算法手段，把**推荐任务**变成一个**生成任务**，从而套到生成式框架里。
这就是**生成式推荐模型**（generative recommendation models）背后的思想。

最近有一篇很详尽的关于这个领域近几年发展的综述：
[Towards Large Generative Recommendation: A Tokenization Perspective](https://large-genrec.github.io/cikm2025.html)。
本文整理一些阅读笔记和思考。

水平及维护精力所限，文中不免存在错误或过时之处，请酌情参考。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

---

* [1 背景](#1-背景)
  + [1.1 什么是生成式模型（Generative Models）？](#11-什么是生成式模型generative-models)
  + [1.2 什么是规模定律（Scaling laws）？](#12-什么是规模定律scaling-laws)
  + [1.3 模型作为真实世界的映像](#13-模型作为真实世界的映像)
  + [1.4 为什么要做“生成式”推荐？](#14-为什么要做生成式推荐)
    - [1.4.1 建模：语言建模 vs. 推荐建模](#141-建模语言建模-vs-推荐建模)
    - [1.4.2 现状：推荐领域的知识非常稀疏](#142-现状推荐领域的知识非常稀疏)
    - [1.4.3 为什么要 token 化 (“Tokenization”)？](#143-为什么要-token-化-tokenization)
  + [1.5 生成式推荐模型 tokenization 方案举例](#15-生成式推荐模型-tokenization-方案举例)
  + [1.6 生成式推荐模型 tokenization 面临的问题](#16-生成式推荐模型-tokenization-面临的问题)
    - [1.6.1 问题：Token 空间太大，行为数据太稀疏](#161-问题token-空间太大行为数据太稀疏)
    - [1.6.2 思路：将行为数据 tokenize 为数据分布](#162-思路将行为数据-tokenize-为数据分布)
    - [1.6.3 方向：LLM-based GenRec vs. SID-based GenRec](#163-方向llm-based-genrec-vs-sid-based-genrec)
* [2 方向一：基于语言模型+文本描述的生成式推荐（LLM-based GR）](#2-方向一基于语言模型文本描述的生成式推荐llm-based-gr)
  + [2.1 Tokenization 过程](#21-tokenization-过程)
  + [2.2 基于语言模型的生成式推荐的特点](#22-基于语言模型的生成式推荐的特点)
    - [2.2.1 丰富的世界知识](#221-丰富的世界知识)
    - [2.2.2 强大的自然语言理解和生成](#222-强大的自然语言理解和生成)
    - [2.2.3 推理能力/执行复杂任务的能力](#223-推理能力执行复杂任务的能力)
    - [2.2.4 如何评估推荐效果](#224-如何评估推荐效果)
  + [2.3 基础：LLM as **`Sequential Recommender`**](#23-基础llm-as-sequential-recommender)
    - [2.3.1 将 LLM 对齐到推荐任务](#231-将-llm-对齐到推荐任务)
    - [2.3.2 训练目标（SFT/Preference/RL）](#232-训练目标sftpreferencerl)
      * [SFT](#sft)
      * [Preference learning](#preference-learning)
      * [RL（强化学习）](#rl强化学习)
    - [2.3.3 推理算法](#233-推理算法)
    - [2.3.4 小结](#234-小结)
  + [2.4 应用一：LLM as **`Conversational Recommender`**](#24-应用一llm-as-conversational-recommender)
    - [2.4.1 LLM 时代之前的对话式推荐](#241-llm-时代之前的对话式推荐)
    - [2.4.2 基于 LLM 的对话式推荐](#242-基于-llm-的对话式推荐)
    - [2.4.3 面临的挑战](#243-面临的挑战)
  + [2.5 应用二：LLM as User Simulator](#25-应用二llm-as-user-simulator)
  + [2.6 小结](#26-小结)
* [3 Semantic ID 简介](#3-semantic-id-简介)
  + [3.1 语言模型的 Token 设计](#31-语言模型的-token-设计)
    - [3.1.1 为什么 **`token:word ≠ 1:1`**](#311-为什么-tokenword--11)
    - [3.1.2 为什么 **`token:char ≠ 1:1`**](#312--为什么-tokenchar--11)
  + [3.2 推荐模型的 Token 设计](#32-推荐模型的-token-设计)
    - [3.2.1 方案一：每个商品用一个 token 表示](#321-方案一每个商品用一个-token-表示)
    - [3.2.2 方案二：每个商品用一段 text 表示](#322-方案二每个商品用一段-text-表示)
    - [3.2.3 方案三：结合方案一和方案二的优点 `-> SemanticID`](#323-方案三结合方案一和方案二的优点---semanticid)
      * [用几个 token 联合索引一个商品](#用几个-token-联合索引一个商品)
      * [每个 token 来自不同 vocabulary，表征商品的不同维度](#每个-token-来自不同-vocabulary表征商品的不同维度)
      * [vocabulary size 和支持的商品总数](#vocabulary-size-和支持的商品总数)
    - [3.2.4 三种方式对应的 vocabulary 大小对比](#324-三种方式对应的-vocabulary-大小对比)
  + [3.3 典型 SemanticID 方案](#33-典型-semanticid-方案)
    - [3.3.1 TIGER, NeurIPS 2023](#331-tiger-neurips-2023)
    - [3.3.2 将推荐问题转化成 seq-to-seq 生成问题](#332-将推荐问题转化成-seq-to-seq-生成问题)
* [4 方向二：基于 SemanticID 的生成式推荐](#4-方向二基于-semanticid-的生成式推荐)
  + [4.1 Semantic ID 的构建](#41-semantic-id-的构建)
    - [4.1.1 目标：输入 & 输出](#411-目标输入--输出)
    - [4.1.2 RQ-VAE-based SemIDs (TIGER as example)](#412-rq-vae-based-semids-tiger-as-example)
      * [步骤一：商品内容信息（Text）](#步骤一商品内容信息text)
      * [步骤二：商品内容信息向量化（Text -> Vector）](#步骤二商品内容信息向量化text---vector)
      * [步骤三：残差量化（Vector -> IDs）](#步骤三残差量化vector---ids)
    - [4.1.3 RQ-VAE-based SemIDs 的特性](#413-rq-vae-based-semids-的特性)
    - [4.1.4 RQ-VAE-based SemIDs 存在的问题](#414-rq-vae-based-semids-存在的问题)
    - [4.1.5 小结](#415-小结)
  + [4.2 构建 SemID 时的输入](#42-构建-semid-时的输入)
    - [4.2.1 商品元数据 (Text / Multimodal / Categorical / No Features)](#421-商品元数据-text--multimodal--categorical--no-features)
    - [4.2.2 商品元数据 + 用户行为](#422-商品元数据--用户行为)
    - [4.2.3 小结](#423-小结)
  + [4.3 基于 SemanticID 的生成式推荐模型架构](#43-基于-semanticid-的生成式推荐模型架构)
    - [4.3.1 架构](#431-架构)
      * [Encoder-decoder](#encoder-decoder)
      * [Decoder-only (OneRec)](#decoder-only-onerec)
    - [4.3.2 目标](#432-目标)
      * [Next-Token Prediction (w/ RQ)](#next-token-prediction-w-rq)
      * [Multi-Token Prediction (w/ PQ)](#multi-token-prediction-w-pq)
    - [4.3.3 LLM 对齐](#433-llm-对齐)
      * [OneRec-Think](#onerec-think)
      * [MiniOneRec](#minionerec)
    - [4.3.4 推理](#434-推理)
  + [4.4 小结](#44-小结)
* [5 总结](#5-总结)
  + [5.1 生成式推荐仍然面临的挑战](#51-生成式推荐仍然面临的挑战)
    - [5.1.1 冷启动推荐](#511-冷启动推荐)
    - [5.1.2 推理效率](#512-推理效率)
    - [5.1.3 模型更新时效（Timely Model Update）](#513-模型更新时效timely-model-update)
    - [5.1.4 商品 Tokenization 方案](#514-商品-tokenization-方案)
  + [5.2 生成式推荐带来的新机会](#52-生成式推荐带来的新机会)
    - [5.2.1 涌现能力](#521-涌现能力)
    - [5.2.2 Test-time Scaling & Reasoning](#522-test-time-scaling--reasoning)
    - [5.2.3 统一检索+排序](#523-统一检索排序)

---

大型生成式模型（**`large generative models`**）的出现正在深刻改变**推荐系统**领域。
构建此类模型的基础组件之一是 **`action tokenization`**，
即将**人类可读数据**（例如用户-商品交互数据）转换为**机器可读格式**（例如离散 token 序列），
这个过程在进入模型之前。

本文介绍几种 action tokenization 技术（将用户行为分别转换为**物品 ID、文本描述、语义 ID**），
然后从 action tokenization 的视角探讨生成式推荐领域面临的挑战、开放性问题及未来潜在发展方向，为下一代推荐系统的设计提供启发。

# 1 背景

## 1.1 什么是生成式模型（Generative Models）？

生成式模型**从大量给定样本中学习**到**底层的数据分布**（underlying distribution of data），
然后就能**生成新的样本**（generate new samples）。如下图所示，在学习了大量动物图文之后，
模型就能根据给定指令生成动物照片（“奔跑的猫/狗/马”），

![](/assets/img/large-generative-recommendation-tokenization-perspective/what-are-generative-models.png)

## 1.2 什么是规模定律（Scaling laws）？

Scaling laws 提供了一个框架，通过这框架可以理解 **`model size, data volume, test-time computing`**
如何影响 **AI 能力的进化**。语言建模领域已经验证了这一框架的有效性。

![](/assets/img/large-generative-recommendation-tokenization-perspective/scaling-law.png)

Scaling Law as a Pathway towards AGI.
Understanding Scaling Laws for Recommendation Models. Arxiv 2022

## 1.3 模型作为真实世界的映像

三种类型的真实世界：

![](/assets/img/large-generative-recommendation-tokenization-perspective/model-as-reflection-of-real-world.png)

做个表格对比，

| 不同类型的真实世界 | 建模元素 | 对应的模型类型 |
| --- | --- | --- |
| 感知世界（**`Perceptual World`**） | 视觉（Vision） | 扩散模型（Diffusion Models, DMs） |
| 认知世界（**`Cognitive World`**） | 语言（Language） | 大语言模型（LLMs） |
| 行为世界（**`Behavioral World`**） | 交互（Interaction） | 用户行为的模型？ |

* 基于 Vision 和 Language 的模型都有了，并且**生成式占据主导地位**，也见证了 scaling law，表现非常好；
* **基于 Interaction 的模型**还在探索中，是不是也可以**套用生成式**？
  也就是构建**大型生成式推荐模型**（large generative recommendation models）。

## 1.4 为什么要做“生成式”推荐？

总结起来有两点，

1. **更好地 scaling** 行为；
2. **与其他模态** (text, image, audio, …) 的**对齐更好**；

### 1.4.1 建模：语言建模 vs. 推荐建模

* 语言建模：根据给定的**文本**，预测**接下来的文本**；
* 推荐建模：根据**用户的历史行为**（购买商品、点击链接、浏览笔记等等），预测用户**接下来的行为**（购买、点击等等）；

![](/assets/img/large-generative-recommendation-tokenization-perspective/language-model-vs-recommendation.png)

> 这里的 Item 是推荐系统推荐的东西，可以是一个商品，也可以是一个笔记、视频等等。

### 1.4.2 现状：推荐领域的知识非常稀疏

| 建模类型 | 知识密度 | Token 类型 | Token 空间 |
| --- | --- | --- | --- |
| 语言模型 | 稠密的世界知识（Dense world knowledge） | **文本** token | 10^5 |
| 推荐模型 | **稀疏的“用户-物品”交互数据**（Sparse user-item interactions） | **Item** token | **`10^9`** |

可以看到，相比于语言建模，推荐领域的知识**非常稀疏**，因而 **scaling laws 在传统推荐模型...