---
title: 【python】使用Python和BERT进行文本摘要：从数据预处理到模型训练与生成
url: https://blog.csdn.net/nokiaguy/article/details/147757375
source: 一个被知识诅咒的人
date: 2025-05-08
fetch_date: 2025-10-06T22:24:25.087122
---

# 【python】使用Python和BERT进行文本摘要：从数据预处理到模型训练与生成

# 【python】使用Python和BERT进行文本摘要：从数据预处理到模型训练与生成

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2025-05-07 11:36:01 发布
·
1.3k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

9

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

12
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#bert](https://so.csdn.net/so/search/s.do?q=bert&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[《Python OpenCV从菜鸟到高手》带你进入图像处理与计算机视觉的大门！](https://blog.csdn.net/nokiaguy/article/details/143574491)

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

随着信息爆炸时代的到来，海量文本数据的高效处理与理解成为亟待解决的问题。文本摘要作为自然语言处理（NLP）中的关键任务，旨在自动生成简明扼要的文本摘要，帮助用户快速获取关键信息。近年来，基于深度学习的预训练语言模型，尤其是BERT（Bidirectional Encoder Representations from Transformers），在文本理解和生成任务中取得了显著进展。本文深入探讨了如何利用Python和BERT模型进行文本摘要，包括数据预处理、模型构建与训练、摘要生成及结果评估等环节。首先，介绍了文本摘要的基本概念及其在实际应用中的重要性。随后，详细阐述了BERT模型的架构及其在文本摘要任务中的应用原理。接着，通过实际案例，展示了如何使用Python进行数据清洗与预处理，并利用Hugging Face的Transformers库构建和训练基于BERT的文本摘要模型。文章还涵盖了生成摘要的具体方法，包括抽取式和生成式摘要技术，并结合代码示例进行详细说明。最后，探讨了模型评估指标及优化策略，旨在为研究人员和开发者提供一套完整的基于BERT的文本摘要解决方案，助力其在信息提取与内容生成领域的创新与实践。

### 引言

在当今信息爆炸的时代，海量的文本数据如新闻报道、学术论文、社交媒体内容等以惊人的速度涌现。如何高效地从这些海量数据中提取关键信息，成为了自然语言处理（NLP）领域的重要研究方向之一。文本摘要作为NLP中的核心任务，旨在自动生成简明扼要的文本摘要，帮助用户快速获取所需信息，提升信息处理的效率和效果。

传统的文本摘要方法主要分为抽取式摘要和生成式摘要两类。抽取式摘要通过从原文中直接提取关键句子或片段来构建摘要，而生成式摘要则尝试理解原文内容，生成新的句子来表达核心信息。随着深度学习技术的迅猛发展，基于神经网络的文本摘要方法逐渐成为研究热点，尤其是预训练语言模型的应用，为文本摘要任务带来了革命性的突破。

BERT（Bidirectional Encoder Representations from Transformers）作为一种基于Transformer架构的双向编码器表示模型，自推出以来在多个NLP任务中表现出色。其强大的语义理解能力使其在文本摘要任务中具备巨大的潜力。然而，如何有效地利用BERT进行文本摘要，包括数据预处理、模型构建与训练、摘要生成及结果评估，仍然是一个值得深入探讨的问题。

本文旨在系统地介绍如何使用Python和BERT模型进行文本摘要任务。通过详细的理论解析与丰富的代码示例，展示从数据预处理到模型训练，再到摘要生成的完整流程。同时，探讨模型评估与优化策略，帮助读者全面掌握基于BERT的文本摘要技术，推动其在实际应用中的落地与创新。

### BERT模型概述

#### Transformer架构

Transformer架构由Vaswani等人于2017年提出，是一种完全基于注意力机制（Attention Mechanism）的神经网络模型，广泛应用于各种NLP任务。与传统的循环神经网络（RNN）相比，Transformer具有更高的并行化能力和更好的长距离依赖建模能力。Transformer主要由编码器（Encoder）和解码器（Decoder）两部分组成，每部分由多个相同的层（Layer）堆叠而成。

每个编码器层包含两个子层：多头自注意力机制（Multi-Head Self-Attention）和前馈全连接网络（Feed-Forward Neural Network）。每个解码器层则在此基础上增加了一个编码器-解码器注意力机制（Encoder-Decoder Attention）。这种设计使得Transformer在处理序列到序列（Sequence-to-Sequence）任务时表现尤为出色。

#### BERT模型

BERT（Bidirectional Encoder Representations from Transformers）是Google于2018年提出的预训练语言模型，基于Transformer的编码器部分。BERT的核心创新在于其双向性，即在进行词表示学习时同时考虑左右上下文信息，这一特性显著提升了模型的语义理解能力。

BERT通过两个主要任务进行预训练：掩蔽语言模型（Masked Language Model, MLM）和下一句预测（Next Sentence Prediction, NSP）。MLM任务随机掩蔽输入句子中的一些词汇，模型需根据上下文预测被掩蔽的词；NSP任务则要求模型判断两句话是否在原文中相邻。这两种任务共同训练出具有深厚语义理解能力的语言表示。

#### BERT在文本摘要中的应用

在文本摘要任务中，BERT可以作为编码器，用于理解输入文本的语义信息。结合解码器部分，BERT可以被扩展为生成式摘要模型。此外，基于BERT的预训练模型，如BERTSUM，通过调整模型结构和训练目标，专门用于摘要生成，取得了良好的效果。

然而，直接使用BERT进行文本摘要存在一些挑战，包括生成的摘要质量、模型的训练效率以及对大规模数据的适应能力。本文将探讨如何通过数据预处理、模型构建与训练、摘要生成等步骤，充分发挥BERT在文本摘要任务中的潜力。

### 数据预处理

#### 数据集选择

文本摘要任务需要大量的带有摘要的文本对作为训练数据。常用的数据集包括：

1. **CNN/Daily Mail**：包含新闻文章及其摘要，广泛用于文本摘要任务。
2. **DUC**：由美国国家标准与技术研究院（NIST）组织的文档理解评估会议提供的数据集。
3. **Gigaword**：包含大量的新闻摘要数据，适用于训练大规模摘要模型。

本文以CNN/Daily Mail数据集为例，展示数据预处理的具体步骤。

#### 数据清洗与格式化

数据预处理的主要目的是将原始数据转化为模型可以接受的格式，包括去除噪声、统一文本格式、分割训练与测试集等。以下是具体的代码实现：

```
import os
import re
import json
import pandas as pd
from tqdm import tqdm

# 定义数据集路径
DATA_DIR = 'cnn_dm_dataset'
TRAIN_FILE = os.path.join(DATA_DIR, 'train.json')
VALID_FILE = os.path.join(DATA_DIR, 'valid.json')
TEST_FILE = os.path.join(DATA_DIR, 'test.json')

# 检查数据文件是否存在
for file in [TRAIN_FILE, VALID_FILE, TEST_FILE]:
    if not os.path.exists(file):
        raise FileNotFoundError(f'文件 {

     file} 不存在，请检查数据集路径。')

# 加载数据
def load_data(file_path):
    """
    加载JSON格式的数据

    参数:
    file_path -- 数据文件路径

    返回:
    texts -- 原文列表
    summaries -- 摘要列表
    """
    texts = []
    summaries = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in tqdm(f, desc=f'加载 {

     file_path}'):
            data = json.loads(line)
            text = data['article']
            summary = data['highlights']
            texts.append(text)
            summaries.append(summary)
    return texts, summaries

# 加载训练、验证和测试集
train_texts, train_summaries = load_data(TRAIN_FILE)
valid_texts, valid_summaries = load_data(VALID_FILE)
test_texts, test_summaries = load_data(TEST_FILE)

# 数据示例
print(f'训练集样本数: {

     len(train_texts)}')
print(f'验证集样本数: {

     len(valid_texts)}')
print(f'测试集样本数: {

     len(test_texts)}')

# 数据清洗函数
def clean_text(text):
    """
    清洗文本数据，去除特殊字符和多余空格

    参数:
    text -- 输入文本

    返回:
    清洗后的文本
    """
    # 去除特殊字符
    text = re.sub(r'[^A-Za-z0-9\s,.!?\'\"-]', '', text)
    # 替换多个空格为一个空格
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# 清洗所有数据
train_texts = [clean_text(text) for text in tqdm(train_texts, desc='清洗训练集')]
valid_texts = [clean_text(text) for text in tqdm(valid_texts, desc='清洗验证集')]
test_texts = [clean_text(text) for text in tqdm(test_texts, desc='清洗测试集')]

train_summaries = [clean_text(summary) for summary in tqdm(train_summaries, desc='清洗训练集摘要')]
valid_summaries = [clean_text(summary) for summary in tqdm(valid_summaries, desc='清洗验证集摘要')]
test_summaries = [clean_text(summary) for summary in tqdm(test_summaries, desc='清洗测试集摘要')]

# 将清洗后的数据保存为CSV文件，便于后续处理
def save_to_csv(texts, summaries, file_name):
    """
    将文本和摘要保存为CSV文件

    参数:
    texts -- 原文列表
    summaries -- 摘要列表
    file_name -- 输出文件名
    """
    df = pd.DataFrame({

   'text': texts, 'summary': summaries})
    df.to_csv(file_name, index=False, encoding='utf-8')
    print(f'已保存到 {

     file_name}')

# 保存数据
save_to_csv(train_texts, train_summaries, 'train_clean.csv')
save_to_csv(valid_texts, valid_summaries, 'valid_clean.csv')
save_to_csv(test_texts, test_summaries, 'test_clean.csv')
```

#### 数据分词与编码

在使用BERT进行文本摘要任务之前，需要对文本进行分词和编码。BERT使用WordPiece分词器，将词汇拆分为更小的子词单元，以处理未登录词和多样化的词汇形式。以下是具体的实现代码：

```
from transformers import BertTokenizer

# 加载预训练的BERT分词器
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# 定义最大序列长度
MAX_INPUT_LENGTH = 512
MAX_SUMMARY_LENGTH = 128

# 分词和编码函数
def tokenize_and_encode(texts, summaries, tokenizer, max_input_len=MAX_INPUT_LENGTH, max_summary_len=MAX_SUMMARY_LENGTH):
    """
    对文本和摘要进行分词和编码

    参数:
    texts -- 原文列表
    summaries -- 摘要列表
    tokenizer -- BERT分词器
    max_input_len -- 原文最大长度
    max_summary_len -- 摘要最大长度

    返回:
    input_ids -- 原文的编码
    attention_masks -- 原文的注意力掩码
    summary_ids -- 摘要的编码
    summary_attention_masks -- 摘要的注意力掩码
    """
    input_ids = []
    attention_masks = []
    summary_ids = []
    summary_attention_masks = []

    for text, summary in tqdm(zip(texts, summaries), total=len(texts), desc='分词和编码'):
        # 编码原文
        encoded_dict = tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=max_input_len,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )
        input_ids.append(encoded_dict['input_ids'])
        attention_masks.append(encoded_dict['attention_mask'])

        # 编码摘要
        summary_encoded = tokenizer.encode_plus(
            summary,
            add_special_tokens=True,
            max_length=max_summary_len,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )
        summary_ids.append(...