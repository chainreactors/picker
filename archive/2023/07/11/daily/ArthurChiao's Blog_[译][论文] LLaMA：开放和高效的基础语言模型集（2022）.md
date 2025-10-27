---
title: [译][论文] LLaMA：开放和高效的基础语言模型集（2022）
url: https://arthurchiao.github.io/blog/llama-paper-zh/
source: ArthurChiao's Blog
date: 2023-07-11
fetch_date: 2025-10-04T11:52:40.893278
---

# [译][论文] LLaMA：开放和高效的基础语言模型集（2022）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译][论文] LLaMA：开放和高效的基础语言模型集（Meta/Facebook，2022）

Published at 2023-07-10 | Last Update 2023-08-12

### 译者序

本文翻译自 2022 年 Meta（facebook）的大模型论文：
[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971)。

作者阵容：Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet,
Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric
Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave,
Guillaume Lample。

一些工程信息：

1. LLaMA 只使用公开可用数据集进行训练，模型已开源；

   * 基于 **transformer** 架构；
   * 训练数据集大小：**1.4T 个 tokens**；
   * 参数范围 **`7B~65B`**；
2. 使用更多 token 进行训练，而不是狂堆参数，一样能取得不错的性能。

   * **LLaMA-13B** 在大多数基准测试中**优于 GPT-3（175B）**；
3. 用户更想要的可能是一个**推理速度最快**而不是**训练速度最快**的模型；此时模型大小就非常重要，

   * LLaMA 可以在单个 GPU 上运行；
   * **LLaMA-13B 可以在单个 V100 上运行**；
4. 训练成本

   * **2048 个 A100** 80GB GPU 上，开发和训练约 5 个月；
   * 训练 65B 模型时，在 **2048 个 A100** 80GB GPU 上能处理约
     **`380 tokens/second/GPU`**，因此 1.4T token
     的数据集训练一次大约需要 **21 天**；
   * 耗能约 2638 MWh，折算排放 1015 吨 CO2。

水平及维护精力所限，译文不免存在错误或过时之处，如有疑问，请查阅原文。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

以下是译文。

---

* [译者序](#译者序)
* [摘要](#摘要)
* [1 引言](#1-引言)
  + [1.1 大模型训练：更多参数 vs 更大的数据集](#11-大模型训练更多参数-vs-更大的数据集)
  + [1.2 LLaMA：减少参数，增大数据集](#12-llama减少参数增大数据集)
  + [1.3 内容组织](#13-内容组织)
* [2 方法（Approach）](#2-方法approach)
  + [2.1 预训练数据（Pre-training Data）](#21-预训练数据pre-training-data)
    - [2.1.1 数据集](#211-数据集)
      * [English CommonCrawl [67%]](#english-commoncrawl-67)
      * [C4 [15%]](#c4-15)
      * [Github [4.5%]](#github-45)
      * [Wikipedia [4.5%]](#wikipedia-45)
      * [Gutenberg and Books3 [4.5%]](#gutenberg-and-books3-45)
      * [ArXiv [2.5%]](#arxiv-25)
      * [Stack Exchange [2%]](#stack-exchange-2)
    - [2.1.2 Tokenizer（分词器）](#212-tokenizer分词器)
  + [2.2 架构（Architecture）](#22-架构architecture)
    - [2.2.1 改进](#221-改进)
      * [预归一化（Pre-normalization）：受 GPT3 启发](#预归一化pre-normalization受-gpt3-启发)
      * [SwiGLU 激活函数：受 PaLM 启发](#swiglu-激活函数受-palm-启发)
      * [旋转嵌入（Rotary Embeddings）：受 GPTNeo 启发](#旋转嵌入rotary-embeddings受-gptneo-启发)
    - [2.2.2 不同 LLaMA 模型的超参数](#222-不同-llama-模型的超参数)
  + [2.3 优化器（Optimizer）](#23-优化器optimizer)
  + [2.4 高效实现（Efficient implementation）：提高训练速度](#24-高效实现efficient-implementation提高训练速度)
* [3 主要结果（Main results）](#3-主要结果main-results)
  + [3.1 常识推理（Common Sense Reasoning）](#31-常识推理common-sense-reasoning)
  + [3.2 闭卷问答（Closed-book Question Answering）](#32-闭卷问答closed-book-question-answering)
  + [3.3 阅读理解（Reading Comprehension）](#33-阅读理解reading-comprehension)
  + [3.4 数学推理（Mathematical reasoning）](#34-数学推理mathematical-reasoning)
  + [3.5 代码生成（Code generation）](#35-代码生成code-generation)
  + [3.6 大规模多任务语言理解（Massive Multitask Language Understanding）](#36-大规模多任务语言理解massive-multitask-language-understanding)
  + [3.7 训练过程中性能的变化](#37-训练过程中性能的变化)
* [4 指令微调（Instruction Finetuning）](#4-指令微调instruction-finetuning)
* [5 Bias, Toxicity and Misinformation](#5-bias-toxicity-and-misinformation)
  + [5.1 RealToxicityPrompts](#51-realtoxicityprompts)
  + [5.2 CrowS-Pairs](#52-crows-pairs)
  + [5.3 WinoGender](#53-winogender)
  + [5.4 TruthfulQA](#54-truthfulqa)
* [6 碳足迹（Carbon footprint）](#6-碳足迹carbon-footprint)
* [7 相关工作（Related work）](#7-相关工作related-work)
  + [7.1 Architecture](#71-architecture)
  + [7.2 Scaling](#72-scaling)
* [8 总结](#8-总结)
* [致谢](#致谢)
* [参考文献](#参考文献)
* [附录（略）](#附录略)

---

# 摘要

本文介绍 LLaMA，一个包含 **`7B~65B`**（70~650 亿）
参数的**基础语言模型集**（a collection of foundation language models）。
我们用**数万亿个（trillions of） token**
训练这些模型，证明了使用**公开数据集**就能训练出最先进的模型，
而并非必须使用专有和私有数据集。特别是，**LLaMA-13B 在大多数基准测试中优于 GPT-3（175B）**
，而 LLaMA-65B 则与最佳模型 Chinchilla-70B 和 PaLM-540B 相当。
我们已经将所有模型[开源](https://github.com/facebookresearch/llama)，供社区研究。

# 1 引言

在大规模文本语料库（massive corpora of texts）上训练的**大型语言模型**
（Large Languages Models, LLM），已经有能力**根据给定的文本指令**（textual instructions）
或示例（a few examples）**执行新任务**（Brown 等，2020）。

这些 **few-shot** 属性首先出现在**将模型扩展到足够大的规模时**（Kaplan 等，2020），
在此之后，出现了很多进一步扩展这些模型的工作（Chowdhery 等，2022；Rae 等，2021），
它们都遵循了这样一个假设：**更多的参数将产生更好的性能**。
然而，Hoffmann 等（2022）的最新工作表明，对于给定的**算力预算**（compute budget），
最佳性能并非来自那些最大的模型，而是来自那些**在更多数据上训练出来的较小模型**。

> “few-shot” 指一个模型有能力根据给定的**少量**示例去执行其他的类似任务的能力。译注。

## 1.1 大模型训练：更多参数 vs 更大的数据集

Hoffmann 等（2022）提出 scaling laws，目标是针对给定的**训练**（training）
算力预算，如何最佳地扩展（scale）**数据集和模型大小**。但是，

* 这个模型没有考虑**推理**（inference）预算，在提供大规模推理时，这一点尤其重要：
  在这种情况下，给定一个性能目标，我们更想要的是一个**推理速度最快**而非训练速度最快的模型。
* 对于一个给定的性能要求，训练一个**大模型**（a large model）可能是一种更便宜的方式；
  但对于最终的**推理**来说，**较小的模型+更长的训练时间**（a smaller one trained longer）反而更实惠。
  例如，Hoffmann 等（2022）建议用 200B tokens 来训练 10B 模型，但我们发现即使在
  1T 个 token 之后，7B 模型的性能仍在随着 token 的增多而提高。

## 1.2 LLaMA：减少参数，增大数据集

本文的重点是：对于给定的不同推理预算（inference budgets），
通过**使用更多 token 进行训练**的方式（超过业内常用的 token 规模）
来获得最佳的性能（the best possible performance）。
由此得到的模型我们称为 **`LLaMA`**。
LLaMA 的参数范围在 **`7B ~ 65B`**，性能则与目前业界最佳的一些大语言模型相当。
例如，

* **LLaMA-13B** 在大多数基准测试中**优于 GPT-3**，
  尽管参数连后者的 **`10%`** 都不到；
* **LLaMA 可以在单个 GPU 上运行**，
  因此使大模型的获取和研究更容易，而不再只是少数几个大厂的专利；
* 在高端系列上，LLaMA-65B 也与最佳的大语言模型（如 Chinchilla 或 PaLM-540B）性能相当。

与 Chinchilla、PaLM、GPT-3 不同，我们**只使用公开数据**（publicly available data），
因此我们的工作是开源兼容的；

* 相比之下，大多数现有模型依赖于不公开或没有文档的数据（not publicly available or undocumented），例如
  “Books–2TB” 和 “Social media conversations”；
* 也存在一些例外，例如 OPT（Zhang 等，2022）、GPT-NeoX（Black 等，2022）、BLOOM（Scao 等，2022）和 GLM（Zeng 等，2022），
  但它们的性能都无法与 PaLM-62B 或 Chinchilla 相比。

## 1.3 内容组织

本文接下来的内容组织如下：

* 描述我们对 Transformer 架构（Vaswani 等，2017）所做的改动，以及我们的训练方法:
* 给出 LLaMA 的性能，基于标准基准测试与其他 LLM 进行比较；
* 使用 responsible AI 社区的最新基准测试，揭示 LLaMA 模型中存在的一些偏见和毒性（biases and toxicity）。

# 2 方法（Approach）

我们的**训练方法与前人的一些工作**（Brown 等，2020；Chowdhery 等，2022）**类似**，
并受到 Chinchilla scaling laws（Hoffmann 等，2022）的启发。
我们使用一个标准的 optimizer 在大量文本数据上训练**大型 Transformers**。

## 2.1 预训练数据（Pre-training Data）

### 2.1.1 数据集

训练数据集有几种不同来源，涵盖了多个领域，如表 1 所示。

|  |  |  |  |
| --- | --- | --- | --- |
| 数据集 | 占比 | 迭代次数（Epochs） | 数据集大小（Disk size） |
| CommonCrawl | 67.0% | 1.10 | 3.3 TB |
| C4 | 15.0% | 1.06 | 783 GB |
| Github | 4.5% | 0.64 | 328 GB |
| Wikipedia | 4.5% | 2.45 | 83 GB |
| Books | 4.5% | 2.23 | 85 GB |
| ArXiv | 2.5% | 1.06 | 92 GB |
| StackExchange | 2.0% | 1.03 | 78 GB |

表 1：预训练数据。
其中 epochs 是用 1.4T tokens 预训练时的迭代次数。用 1T tokens 预训练时也是用的这个数据集比例。

这里的数据集大部分都是**其他 LLM 训练用过的**，
但我们只用其中公开可得（publicly available）的部分，并且要保持开源兼容（compatible with open sourcing）。
因此最后得到的就是一个混合数据集。

#### English CommonCrawl [67%]

我们使用 CCNet pipeline（Wenzek 等，2020）对 2017~2020 的五个 CommonCrawl dumps 进行预处理。

* 在行级别（line level）上对数据去重，
* 使用 fastText 线性分类器进行语言识别，去掉非英文网页，
* 使用 ngram 语言模型过滤掉一些低质量内容。

此外，我们还训练了一个线性模型，将页面分为两类：

1. 被 Wikipedia 引用过的网页；
2. 没有被 Wikipedia 引用过的（随机采样网页）；

并将第二类丢弃。

#### C4 [15%]

在前期探索性实验中，我们观察到使用**多样化的预处理 CommonCrawl 数据集**可以提高性能。
因此，我们将公开可用的 C4 数据集（Raffel 等，2020）也包含到了训练数据中。

对 C4 的预处理也是**去重和语言识别**：与 CCNet 的主要区别在于质量过滤（quality filtering），
主要依赖于启发式方法（heuristics），例如是否存在标点符号或网页中单词和句子的数量。

#### Github [4.5%]

使用了 Google BigQuery 上公开可用的 GitHub 数据集，但仅保留其中用 Apache、BSD 和 MIT license 的项目。
此外，

* 基于行长度（line length），字母或数字字符（alphanumeric characters）比例等，用启发式方法过滤掉低质量文件；
* 使用正则表达式删除一些模板段落（boilerplate），例如 headers；
* 在文件级别上使用精确匹配对得到的数据集进行去重。

#### Wikipedia [4.5%]

使用了 2022 年 6 月至 8 月的一部分 Wikipedia dumps，
覆盖 20 种语言（use either the Latin or Cyrillic
scripts）：bg、ca、cs、da、de、en、es、fr、hr、hu、it、nl、pl、pt、ro、ru、sl、sr、sv、uk。

删掉了其中的超链接、注释和其他 formatting boilerplate。

#### Gutenberg and Books3 [4.5%]

训练数据集中包含两个书籍语料库：

1. Gutenberg Project：**公版书**（public domain books）；
2. Books3 section of ThePile（Gao 等，2020）：一个用于训练大语言模型的**公开可用**数据集。

在书级别（book level）去重，内容超过 90% 重复的书会被剔除出去。

#### ArXiv [2.5%]

为了让训练数据集包含一定的科学数据（scientific data），我们对一些 arXiv Latex 文件做处理之后加到训练数据集。

* 按照 Lewkowycz 等（2022）的方法，删除了 the first section 之前的所有内容以及参考文献，
* 从 .tex 文件中删除了注释，
* 对作者编写的定义和宏（definitions and macros written by users）做了内联展开（inline-expand），使得论文更加一致（incre...