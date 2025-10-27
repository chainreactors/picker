---
title: 原创 Paper | LLM检索增强生成(RAG)的基本原理和实现
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650990710&idx=1&sn=771c2f44aef4cf2cbaf48f7078f99fc2&chksm=8079aa44b70e2352d0ef617bf46770a20f395089d25c9b06f55268fe1dc2ad39e69cb931219a&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2025-02-22
fetch_date: 2025-10-06T20:37:29.511039
---

# 原创 Paper | LLM检索增强生成(RAG)的基本原理和实现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT3udhFEVY5myKLk0Cn2uzqIeD17g1hKdOKojC0pwwp2wsJib7NRhxuwRziby4IPsiahfqXMEn8Zia0law/0?wx_fmt=jpeg)

# 原创 Paper | LLM检索增强生成(RAG)的基本原理和实现

原创

404实验室

知道创宇404实验室

**作******者：0x7F@********知道创宇404实验室****

**时间：**2025年2月17日****

**1. 前言**

参考资料

随着 LLM (Large Language Model)技术的快速发展，智能聊天机器人和自然语言处理(NLP)领域也上升到了一个新的高度，计算机可以「理解」人类的书写和说话方式，并依靠模型内部的知识解答问题；伴随着 Meta AI 的研究人员提出的检索增强生成(RAG)技术，即不用训练就可以扩展模型的知识储备，为基于 LLM 构建定制化的知识库提供了可行的方案。

本文就检索增强生成技术的基本原理进行介绍，并使用代码演示 RAG 技术在构建知识库方面的应用实施。

本文实验环境：

```
Ubuntu 22.04 + 4090/24GB
Anaconda
Ollama 0.5.1
Llama-3.1-8B-Instruct (language model)
bge-large-en-v1.5 (embedding model)
bge-large-zh-v1.5 (embedding model)
```

**2. RAG的原理**

参考资料

在引入检索增强生成技术前，我们来看看使用 LLM 基础模型来搭建知识库有哪些方案：

1. Fine-Tuning/微调，使用微调将知识库数据添加至模型的内部结构中
2. Prompt/提示词，使用提示次将知识库数据添加至模型的上下文中

首先 Fine-Tuning/微调 方案所面临的最大问题是训练成本过高，用户难以将其引入到实际使用场景下，而 Prompt/提示词 方案则需要考虑基础模型的上下文长度问题，目前多数模型支持 4k/8k/.../100k (token)等不同长度的上下文，超过上下文长度的历史数据将被模型「遗忘」，但在搭建知识库的场景中这样的上下文长度依然是远远不够的(100k 的上下文长度约等于支持 75k 的英语单词)。

在 Prompt/提示词 这个方案下，如果我们在接受到用户的问题后，首先从知识库中搜索于该问题相关的一些数据片段，再将这些数据和原始问题组合成提示词提交给大模型，大模型再基于数据和问题来生成回答，这样的流程我们就将其称之为「检索-增强-生成」即检索增强生成(Retrieval-Augmented Generation) 技术。

根据以上描述可以绘制 RAG 的流程图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3udhFEVY5myKLk0Cn2uzqITicQNsJGAL62EEZoSjgcMjRziaVwqz2L6dt0x6JjLEXhxZIdUqw33G8A/640?wx_fmt=png&from=appmsg)

图1.LLM-RAG流程示意图

根据 RAG 的特性，使用该技术构建知识库有几大优势：

1. 降低应用成本，不需要对基础模型进行训练，极大降低成本
2. 数据具备时效性，知识库可以随时修改并应用生效
3. 有效避免模型"幻觉"，使用确切的数据片段供模型生成回答，有效减少模型编造数据
4. 增加回答的可理解性，可以清晰追溯回答的内容来源于哪些知识库文档

**3. 最小实现示例**

参考资料

#### 现在我们沿着上文思路，基于 Llama-3.1-8B-Instruct 实现一个 RAG 的最小可行性验证，我们准备了一些关于户外活动的建议作为知识库数据，如下：

```
"Take a leisurely walk in the park and enjoy the fresh air.",
"Visit a local museum and discover something new.",
"Attend a live music concert and feel the rhythm.",
"Go for a hike and admire the natural scenery.",
"Visit an amusement park and ride the roller coasters."
```

> Llama-3.1-8B-Instruct 支持 128k 的上下文长度，当然可以将以上知识库数据全部放入 prompt 中，我们这里仅仅为了 RAG 的演示。

用户的问题和知识库数据，我们采用最简单的单词匹配的方式，如下：

```
query = ["I", "like", "to", "hike"]
doc = ['Go', 'for', 'a', 'hike', 'and', 'admire', 'the', 'natural', 'scenery.']

matched => ["hike"]
```

通过以上函数匹配到知识库片段，我们再将其和用户问题组装至提示词中，模版如下：

```
You are a bot that makes recommendations for activities. You answer in very short sentences and do not include extra information.
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input.
```

使用 Ollama 的 API 调用 Llama-3.1-8B-Instruct 模型，完整代码 rag-outdoor-tips.py（https://images.seebug.org/archive/rag-outdoor-tips.py） 如下：

```
import requests
import json

DOCUMENTS = [
    "Take a leisurely walk in the park and enjoy the fresh air.",
    "Visit a local museum and discover something new.",
    "Attend a live music concert and feel the rhythm.",
    "Go for a hike and admire the natural scenery.",
    "Visit an amusement park and ride the roller coasters."
]

def get_similarity(query, documents):
    query_words = query.split()
    similarities = []
    for doc in documents:
        value = 0
        for w in query_words:
            if w in doc:
                value = value + 1
        similarities.append(value)
    # end for
    return documents[similarities.index(max(similarities))]
# end get_similarity

user_input = "I like to hike"
relevant_document = get_similarity(user_input, DOCUMENTS)

print("Question:", user_input)
print("Relevant:", relevant_document)

prompt = """
You are a bot that makes recommendations for activities. You answer in very short sentences and do not include extra information.
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input.
"""

url = 'http://localhost:11434/api/generate'
data = {
    "model": "llama3.1:8b",
    "prompt": prompt.format(user_input=user_input, relevant_document=relevant_document),
    "stream": False,
}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

print("Answer:", response.json()['response'])
```

使用用户问题「I like to hike」，运行如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3udhFEVY5myKLk0Cn2uzqIpp5tLAVDDLmcxyqWxCJlRSawzurGWkR7gicSNVoCmL68fIKcZIdRFNQ/640?wx_fmt=png&from=appmsg)

图2.户外活动建议RAG的运行演示

至此我们实现了 RAG 的最小可行性验证，我们提供的知识库可以良好的和 Llama-3.1-8B-Instruct 模型配合工作。

但是如果用户的问题是「I like climb mountains」，这属于「hike」的同义词，但在我们构建的 RAG 中却无法匹配到对应的内容，这不符合预期；所以这就需要我们从语义上来对知识库进行搜索匹配了，通过使用词嵌入模型来实现。

**4.Embedding模型**

参考资料

词嵌入(Word embedding)模型是自然语言处理（NLP）中语言模型与表征学习技术的统称，它可以将高维度的数据转化为低维度的嵌入空间，并通过学习将相似的数据点映射到嵌入空间中相近的位置，从而捕捉特征和语义信息，并提高模型的效率和准确性。如果两个单词在向量空间中具有相似的位置，通常意味着这两个单词具有相似的含义和语义，词嵌入模型在 RAG 技术中发挥着至关重要的作用。

BGE (BAAI General Embedding)模型是由北京智源人工智能研究院(BAAI)推出的一系列开源 embedding 模型；其中 bge-large-en-v1.5 和 bge-large-zh-v1.5 在分别在英文和中文环境下具有良好的表现，同时这两个模型较小，具有广泛的适用性。

这里我们尝试使用 bge-large-en-v1.5 模型，分别下载模型权重文件和官方代码库：

```
# download model from huggingface
$ huggingface-cli download BAAI/bge-base-en-v1.5 --local-dir ./bge-base-zh-v1.5
# download source from github
$ git clone https://github.com/FlagOpen/FlagEmbedding.git
```

使用官方示例测试向量化和相似度计算，bge-quick-start.py（https://images.seebug.org/archive/bge-quick-start.py）代码如下：

```
from FlagEmbedding import FlagAutoModel

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ['TRANSFORMERS_NO_ADVISORY_WARNINGS'] = 'true'

def main():
    model = FlagAutoModel.from_finetuned('./bge-base-en-v1.5',
                                          query_instruction_for_retrieval="Represent this sentence for searching relevant passages:",
                                          use_fp16=True)

    sentences_1 = ["I love NLP", "I love machine learning"]
    sentences_2 = ["I love BGE", "I love text retrieval"]
    embeddings_1 = model.encode(sentences_1)
    embeddings_2 = model.encode(sentences_2)

    print(embeddings_1)
    print(embeddings_2)

    similarity = embeddings_1 @ embeddings_2.T
    print(similarity)
# end main()

if __name__ == "__main__":
    main()
# end __main__()
```

运行该测试代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3udhFEVY5myKLk0Cn2uzqIWLkPEp9GxpiacPlzVibDwlP3R37icemQEwLuwsXDloY1S6bQkMbfEicPeQ/640?wx_fmt=png&from=appmsg)

图3.bge测试代码运行示例

我们可以看到 `I love NLP` 语句被向量化为了 `[-0.03146 -0.009125 0.010414 ... 0.006447 0.02682 -0.01701 ]`，而通过相似性计算，可以看到 `I love NLP` 和 `I love BGE` 的相似度为 `0.6543`，其他同理。

现在我们将 embedding 应用到上文的户外活动建议的 RAG 技术中，我们需要将单词匹配的逻辑修改为使用 bge-large-en-v1.5 embedding 模型计算相似度，重写 `get_similarity()` 函数如下：

```
def get_similarity(question, documents):
    model = FlagAutoModel.from_finetuned('./bge-base-en-v1.5',
                                          query_instruction_for_retrieval="Represent this sentence for searching relevant passages:",
                                          use_fp16=True)
    # calculate data embedding vector
    VECTOR_DB = []
    for i, chunk in enumerate(documents):
        embedding = model.encode(chunk)
        VECTOR_DB.append((chunk, embedding))
        print(f'Added chunk {i+1}/{len(documents)} to the database')
    # end for

    # calculate query embedding vector
    query = model.encode(question)

    similarities = []
    for chunk, embedding in VECTOR_DB:
        similarity = query @ embedding
        similarities.append((chunk, similarity))
    # end for

    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[0][0]
# end get_similarity()
```

完整代码参考 rag-bge-embedding.py（https://images.seebug.org/archive/rag-bge-embedding.py），分别测试用户问题「I like to hike」和「I like climb mountains」如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3udhFEVY5myKLk0Cn2uzqIKIYZiagAPQEIXJqDiaCn96taibqq2ApSxdnMJZianJvGFUULC1XroiaqO4g/640?wx_fmt=png&from=appmsg)

图4.bge-embedding的RAG运行示例

我们这里使用 bge-large-en-v1.5 模型和 Llama-3.1-8B-Instruct 模型构建了基础的 RAG 系统框架，其中 bge-large-en-v1.5 ...