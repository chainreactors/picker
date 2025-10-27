---
title: 大模型 RAG 基础：信息检索、文本向量化及 BGE-M3 embedding 实践（2024）
url: https://arthurchiao.github.io/blog/rag-basis-bge-zh/
source: ArthurChiao's Blog
date: 2024-08-05
fetch_date: 2025-10-06T18:00:09.815941
---

# 大模型 RAG 基础：信息检索、文本向量化及 BGE-M3 embedding 实践（2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# 大模型 RAG 基础：信息检索、文本向量化及 BGE-M3 embedding 实践（2024）

Published at 2024-08-04 | Last Update 2024-08-19

本文整理一些文本向量化（embedding）和信息检索的知识，它们是如今大模型生成文本时常用的技术 —— “增强检索生成”（RAG）—— 的基础：

![](/assets/img/rag-basis-bge/bert-embedding-similarity.svg)

Fig. Similarity score based on BERT embedding. [Image source](https://docs.kolena.com/metrics/bertscore/)

水平及维护精力所限，文中不免存在错误或过时之处，请酌情参考。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

---

* [1 信息检索（information retrieval）技术三大发展阶段](#1-信息检索information-retrieval技术三大发展阶段)
  + [1.1 基于统计信息和关键词匹配（`1970s-2010s`）](#11-基于统计信息和关键词匹配1970s-2010s)
    - [1.1.1 典型算法：`TF-IDF`、`BM25`](#111-典型算法tf-idfbm25)
    - [1.1.2 原理](#112-原理)
    - [1.1.3 优缺点](#113-优缺点)
  + [1.2 基于深度学习和上下文语义](#12-基于深度学习和上下文语义)
    - [1.2.1 `Word2Vec` (Google, 2013)](#121-word2vec-google-2013)
    - [1.2.2 `BERT` (Google, 2019)](#122-bert-google-2019)
      * [核心设计和优点](#核心设计和优点)
      * [局限性：领域外（Out-of-Domain）信息检索效果差](#局限性领域外out-of-domain信息检索效果差)
  + [1.3 学习型：组合前两种的优点](#13-学习型组合前两种的优点)
    - [1.3.1 原理：传统 sparse vector 与上下文化信息的融合](#131-原理传统-sparse-vector-与上下文化信息的融合)
    - [1.3.2 与传统 sparse embedding 的区别](#132-与传统-sparse-embedding-的区别)
    - [1.3.3 优点](#133-优点)
* [2 信息检索：三种 embedding 的对比](#2-信息检索三种-embedding-的对比)
  + [2.1 Sparse embedding (lexical matching)](#21-sparse-embedding-lexical-matching)
  + [2.2 Dense embedding (e.g. BERT-based)](#22-dense-embedding-eg-bert-based)
  + [2.3 Learned sparse embedding](#23-learned-sparse-embedding)
* [3 Embedding & retrieval 工作原理详解](#3-embedding--retrieval-工作原理详解)
  + [3.1 `BERT` 是如何工作的](#31-bert-是如何工作的)
    - [3.1.1 理论基础](#311-理论基础)
    - [3.1.2 BERT dense embedding 工作流](#312-bert-dense-embedding-工作流)
  + [3.2 基于 BERT dense embedding 的文档检索是如何工作的](#32-基于-bert-dense-embedding-的文档检索是如何工作的)
  + [3.3 `BGE-M3`（BERT-based learned sparse embedding）是如何工作的？](#33-bge-m3bert-based-learned-sparse-embedding是如何工作的)
    - [3.3.1 设计 & 特点](#331-设计--特点)
    - [3.3.2 BGE-M3 生成 learned sparse embedding 的过程](#332-bge-m3-生成-learned-sparse-embedding-的过程)
* [4 BGE-M3 实战](#4-bge-m3-实战)
  + [4.1 相似度判断（检索）](#41-相似度判断检索)
  + [4.2 精调（fine-tune）](#42-精调fine-tune)
    - [4.2.1 官方文档](#421-官方文档)
    - [4.2.2 训练数据格式及要求](#422-训练数据格式及要求)
    - [4.2.3 精调命令及参数配置](#423-精调命令及参数配置)
    - [4.2.4 测试精调之后的效果](#424-测试精调之后的效果)
  + [4.3 CPU 运行速度优化：将模型转 onnx 格式](#43-cpu-运行速度优化将模型转-onnx-格式)
* [5 `rerank` 增强：对 BGE-M3 的检索结果进行重排序](#5-rerank-增强对-bge-m3-的检索结果进行重排序)
  + [5.1 `rerank/reranker` 是什么？](#51-rerankreranker-是什么)
    - [5.1.1 另一种相似度模型](#511-另一种相似度模型)
    - [5.1.2 与 BGE-M3 等模型的差异：`cross-encoder vs. bi-encoder`](#512-与-bge-m3-等模型的差异cross-encoder-vs-bi-encoder)
  + [5.2 embedding 和 reranker 工作流](#52-embedding-和-reranker-工作流)
  + [5.3 BGE-M3 得到相似分之后，为什么要通过 reranker 再计算一遍？](#53-bge-m3-得到相似分之后为什么要通过-reranker-再计算一遍)
* [6 总结](#6-总结)
* [参考资料](#参考资料)

---

RAG (Retrieval-Augmented Generation，检索增强生成)，是一种利用信息检索（Information Retrieval）
技术增强大模型生成效果（generation）的技术。RAG 在步骤上很简单，

1. **搭建高质量文档数据库**
   * 对优质文档进行某种格式的转换（或称编码），例如基于 BERT 将文本段落转换成
     **数值格式的向量**（这个过程称为 **`embedding`**），然后
   * 将这些 embeddings 存储到合适的数据库（例如 ES 或**向量数据库**）；
2. **针对用户输入进行数据库检索**
   * 对用户输入的 query 进行相同的转换（embedding），然后
   * 利用最近邻等相似性算法，在文档库中**寻找最相似的文本段落**（与给定问题最相关的段落）；
3. **大模型生成返回给用户的内容**
   * 将找到文本段落送到大模型，辅助生成最终的输出文本，返回给用户。

本文主要关注以上 1 & 2 步骤中的 embedding & retrieval 阶段。

# 1 信息检索（information retrieval）技术三大发展阶段

信息检索的技术发展大致可分为三个阶段：

1. **基于统计信息**的**关键字匹配**（statistical keyword matching）

   * 是一种 **`sparse embedding`** —— embedding 向量的大部分字段都是 0；
2. 基于**深度学习**模型的**上下文和语义理解**，

   * 属于 **`dense embedding`** —— embedding 向量的大部分字段都非零；
3. 所谓的“学习型”表示，组合上面两种的优点，称为 **`learned sparse embedding`**

   * 既有深度学习模型的上下文和语义理解能力；
   * 又具备稀疏表示的可解释性（interpretability of sparse representations）和低计算复杂度。

下面分别来看。

## 1.1 基于统计信息和关键词匹配（`1970s-2010s`）

### 1.1.1 典型算法：`TF-IDF`、`BM25`

早期信息检索系统主要是**基于统计信息** + **匹配关键词**，算法包括，

* [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) (term frequency - inverse document frequency), 1970s
* [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) (Best Matching), 1980s

  + based on the **`probabilistic retrieval framework`** developed in the 1970s and 1980s.
  + BM25 is a **`bag-of-words`** retrieval function that ranks a set of documents based on the query terms appearing in each document.

### 1.1.2 原理

分析**语料库的词频和分布**（term frequency and distribution），
作为评估**文档的相关性**（document relevance）的基础。

### 1.1.3 优缺点

* 优点：方法简单，效果不错，所以使用很广泛。
* 缺点：单纯根据词频等统计和关键字检索做判断，不理解语义。

## 1.2 基于深度学习和上下文语义

### 1.2.1 `Word2Vec` (Google, 2013)

2013 年，谷歌提出了 [Word2Vec](https://zilliz.com/learn/transforming-text-the-rise-of-sentence-transformers-in-nlp)，

* 首次尝试**使用高维向量来表示单词**，能分辨它们细微的语义差别；
* 标志着向**机器学习驱动**的信息检索的转变。

### 1.2.2 `BERT` (Google, 2019)

基于 transformer 的**预训练（pretrain）语言模型** BERT 的出现，彻底颠覆了传统的信息检索范式。

#### 核心设计和优点

1. transformer 的核心是 self-attention，
   * self-attention 能**量化给定单词与句子中其他单词的关联性程度**，
   * 换句话说就是：能在上下文中分辨单词的含义；
2. BERT 是双向（前向+后向）transformer，
   * 可以理解为在预训练时，每个句子正向读一遍，反向再读一遍；
   * 能更好地捕获句子的上下文语义（contextual semantics）；
   * 最终输出是一个 **dense vector**，本质上是对语义的压缩；
3. 基于 dense vector 描述，用最近邻算法就能对给定的 query 进行检索，强大且语义准确。

#### 局限性：领域外（Out-of-Domain）信息检索效果差

BERT 严重依赖**预训练数据集**的领域知识（domain-specific knowledge），
预训练过程使 BERT 偏向于预训练数据的特征，
因此在领域外（Out-Of-Domain），例如没有见过的文本片段，表现就不行了。

解决方式之一是**`fine-tune`**（精调/微调），但成本相对较高，
因为准备高质量数据集的成本是很高的。

另一方面，尽管传统 sparse embedding 在词汇不匹配问题时虽然也存在挑战，
但在领域外信息检索中，它们的表现却优于 BERT。
这是因为在这类算法中，未识别的术语不是靠“学习”，而是单纯靠“匹配”。

## 1.3 学习型：组合前两种的优点

### 1.3.1 原理：传统 sparse vector 与上下文化信息的融合

1. 先通过 BERT 等深度学习模型生成 dense embedding；
2. 再引入额外的步骤对以上 dense embedding 进行稀疏化，得到一个 sparse embedding；

代表算法：BGE-M3。

### 1.3.2 与传统 sparse embedding 的区别

根据以上描述，乍一看，这种 learned sparse embedding 与传统 sparse embedding 好像没太大区别，
但实际上二者有着本质不同，这种 embedding，

* 引入了 Token Importance Estimation；
* 既保留了关键词搜索能力，又利用上下文信息，丰富了 embedding 的稀疏表示；
* 能够辨别相邻或相关的 token 的重要性，即使这些 token 在文本中没有明确出现。

### 1.3.3 优点

* 将稀疏表示与学习上下文结合，同时具备精确匹配和语义理解两大能力，在领域外场景有很强的泛化能力；
* 与 dense embedding 相比更简洁，只保留了最核心的文本信息；
* 固有的稀疏性使向量相似性搜索所需的计算资源极少；
* 术语匹配特性还增强了可解释性，能够更精确地洞察底层的检索过程，提高了系统的透明度。

# 2 信息检索：三种 embedding 的对比

简单来说，
vector embedding，或称向量表示，是一个单词或句子在**高维向量空间**中的**数值表示**。

* 高维空间：一个维度能代表一个特征或属性，高维意味着分辨率高，能区分细微的语义差异；
* 数值表示：一个 embedding 一般就是一个**浮点数数组**，所以方便计算。

对应上一节介绍的三个主要发展阶段，常见的有三种 embedding 类型：

1. traditional sparse embedding
2. dense embedding
3. learned sparse embedding

## 2.1 Sparse embedding (lexical matching)

* 映射成一个高维（维度一般就是 vocabulary 空间大小）向量
* 向量的大部分元素都是 0，非零值表明 token 在特定文档中的相对重要性，只为那些输入文本中出现过的 token 计算权重
* 典型模型：BM25（对 TF-IDF 的改进）

非常适合**关键词匹配**任务（keyword-matching tasks）。

## 2.2 Dense embedding (e.g. BERT-based)

* 映射到一个（相对低维）向量，所有维度都非零
* 相比 sparse embedding 维度要低很多，例如基于 BERT 默认 `1x768` 维度；
* 典型模型：BGE-v1.5

所有维度都非零，包含语义理解，信息非常丰富，因此适用于
**语义搜索**任务（semantic search tasks）。

> Multi-vector retrieval
>
> * 用多个向量表示一段文本，可以看做是对 dense retrieval 的一种扩展
> * 模型：ColBERT

## 2.3 Learned sparse embedding

结合了传统 sparse embedding 的精确度和 dense embedding 的语义丰富性，

* 可以通过深度学习模型“学习”相关 token 的重要性，即使是一些并未出现过的 token，
* 生成的“学习型”稀疏表示，能有效捕捉 query 和 doc 中的关键词。

# 3 Embedding & retrieval 工作原理详解

这里主要介绍 BGE-M3 模型的原理。**BGE-M3 建立在 BERT 之上**，因此需要先回顾 BERT 的基本原理。

## 3.1 `BERT` 是如何工作的

### 3.1.1 理论基础

* BERT 论文：[BERT：预训练深度双向 Transformers 做语言理解（Google，2019）](/blog/bert-paper-zh/)
* BERT 基于 transformer，后者的核心是 self-attention
  + [Transformer 是如何工作的：600 行 Python 代码实现 self-attention 和两类 Transformer（2019）](/blog/transformers-from-scratch-zh/)
  + [什么是 GPT？Transformer 工作原理的动画展示（2024）](/blog/visual-intro-to-transformers-zh/)

### 3.1.2 BERT dense embedding 工作流

以输入 **`"Milvus is a vector database built for scalable similarity search"`** 为例，工作过程 [2]：

![](/assets/img/rag-basis-bge/bert-dense-embedding.png)

Fig. BERT dense embedding.

1. **`Tokenization`**
   1. 将输入文本转成 token 序列
   2. BERT 还会插入两个特殊的 token：`[CLS]` token 表示开始，`[SEP]` token 表示一个句子的结束。
2. **`Embedding`**：使用 embeddin...