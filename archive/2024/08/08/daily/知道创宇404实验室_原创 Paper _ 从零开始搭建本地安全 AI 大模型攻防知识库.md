---
title: 原创 Paper | 从零开始搭建本地安全 AI 大模型攻防知识库
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650980277&idx=1&sn=13453900e19a307e4eec60fe8362ca39&chksm=8079fd87b70e749171a22e1232eac6e6a637c689ccbd9a41265b88bbeaab32afb09b3fe1df4b&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-08-08
fetch_date: 2025-10-06T18:06:08.854206
---

# 原创 Paper | 从零开始搭建本地安全 AI 大模型攻防知识库

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT20N0ywc0sw5QLyZ91fVdYjuOoib2pHBEcdoSuPlLzzrZdQ4cuL8EBIEKA3hqnCC480L7k9fia2UmMg/0?wx_fmt=jpeg)

# 原创 Paper | 从零开始搭建本地安全 AI 大模型攻防知识库

原创

404实验室

知道创宇404实验室

**作者：********Hcamael**@知道创宇404实验室****

**时间：**2024年8月7日****

本文将系统分享从零开始搭建本地大模型问答知识库过程中所遇到的问题及其解决方案。

**1 概述**

目前，搭建大语言问答知识库能采用的方法主要包括微调模型、再次训练模型以及增强检索生成（RAG，Retrieval Augmented Generation）三种方案。

而我们的目标是希望能搭建一个低成本、快速响应的问答知识库。由于微调/训练大语言模型需要耗费大量资源和时间，因此我们选择使用开源的本地大型语言模型结合RAG方案。经过测试，我们发现`llama3:8b`和`qwen2:7b`这种体量的大语言模型能快速响应用户的提问，比较符合我们搭建问答知识库的需求。

我们花了一段时间，对RAG各个步骤的原理细节和改进方案进行了一些研究，下面将按照RAG的步骤进行讲解。

### **1.1 简述RAG原理**

首先，我们来讲解一下RAG的原理。假设我们有三个文本和三个问题，如下所示：

```
context = [
    "北京，上海，杭州",
    "苹果，橘子，桃子",
    "太阳，月亮，星星"
]
questions = ["城市", "水果", "天体"]
```

接下来使用ollama的`mxbai-embed-large`模型，把三个文本和三个问题都转化为向量的表示形式，代码如下所示：

```
vector = []
model = "mxbai-embed-large"
for c in context:
    r = self.engine.embeddings(c, model=model)
    vector += [r]
    print("r =", r)
'''
r = [-0.4238928556442261, -0.037000998854637146, ......
'''
qVector = []
for q in questions:
    r = self.engine.embeddings(q, model=model)
    qVector += [r]
    print("r =", r)
'''
q = [-0.3943982422351837,
'''
```

接下来使用numpy模块来编写一个函数，计算向量的相似度，代码如下所示：

```
def cosine_similarity(self, a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
for i in range(3):
    for j in range(3):
        similar = self.engine.cosine_similarity(qVector[i], vector[j])
        print(f"{questions[i]}和{context[j]}的相似度为：{similar}")
'''
城市和北京，上海，杭州的相似度为：0.6192201604133171
城市和苹果，橘子，桃子的相似度为：0.6163859899608889
城市和太阳，月亮，星星的相似度为：0.5885895914816769

水果和北京，上海，杭州的相似度为：0.6260800765574224
水果和苹果，橘子，桃子的相似度为：0.6598514846105531
水果和太阳，月亮，星星的相似度为：0.619382129127254

天体和北京，上海，杭州的相似度为：0.5648588692973202
天体和苹果，橘子，桃子的相似度为：0.6756043740633552
天体和太阳，月亮，星星的相似度为：0.75651740246562
'''
```

从上面的示例可以看出，计算出的结果值越大，表示两个文本之间的相似度越高。上述过程是RAG原理的简化版。

有一定基础的都知道，大语言模型本质上就是计算概率，因此它只能回答训练数据中包含的内容。如果要搭建一个问答知识库，并且该知识库的内容是公开的，那么这些内容很可能已经包含在大模型的训练数据集中。在这种情况下，不需要进行任何额外操作，可以直接使用大模型进行问答，这也是目前大多数人使用大语言模型的普遍方式。

然而，我们要搭建的本地知识库大部分包含私有数据，这些内容并不存在于当前大语言模型的训练数据集中。在这种情况下，可以考虑对大模型进行微调或重新训练，但这种方案既费时又费钱。

因此，更常用的方案是将知识库的内容放入到prompt中，让大语言模型通过我们提供的内容来进行回答。但是该方案存在一个问题，那就是token的长度限制（上下文长度限制）。比如，本地大语言模型中的`qwen2:7b`，`token`的最大长度为`128k`，表示输入的上下文通过`AutoTokenizer`计算出的长度不能超过128k，但是正常情况下，知识库的大小超过128k是很正常的。我们不可能把所有的知识库内容都放入到prompt中，因此就有了RAG方案。

RAG的方案步骤如下所示：

1. 对知识库根据一定的大小进行分片处理。
2. 使用embedding大模型对分片后的知识库进行向量化处理。
3. 使用embedding大模型对用户的问题也进行向量化处理。
4. 把用户问题的向量和知识库的向量数据进行相似度匹配，找出相似度最高的k个结果。
5. 把这k个结果作为上下文放入到prompt当中，跟着用户的问题进行提问。

在开头的例子中，`context`变量相当于知识库的内容，`"城市"`就相当于用户提出的问题，接着通过相似度计算，`"北京，上海"`是最接近的信息，所以接着把该信息作为提问的上下文提供给GPT进行问答。

一个简单的prompt示例如下所示：

```
prompt = [
  {
      "role": "user",
      "content": f"""当你收到用户的问题时，请编写清晰、简洁、准确的回答。
你会收到一组与问题相关的上下文，请使用这些上下文，请使用中文回答用户的提问。不允许在答案中添加编造成分，如果给定的上下文没有提供足够的信息，就回答"##no##"。
不要提供与问题无关的信息，也不要重复。
> 上下文：
>>>
{context}
>>>
> 问题：{question}
"""
  }
]
```

### **1.2 使用redis-search计算相似度**

在上述的例子中，是自行编写了一个`cosine_similarity`函数来计算相似度，但是在实际的应用场景中，知识库的数据会非常大，这会导致计算相似度的速度非常慢。

经过研究发现，能对向量进行存储并且快速计算相似度的工具有：

* redis-search
* chroma
* elasticsearch
* opensearch
* lancedb
* pinecone
* qdrant
* weaviate
* zilliz

下面分享一个使用redis-search的KNN算法来快速找到最相似的k个内容的方案。

首先搭建`redis-search`环境，可以使用docker一键搭建，如下所示：

```
$ docker pull redis/redis-stack
$ docker run --name redis -p6379:6379 -itd redis/redis-stack
```

接着编写相关python代码，如下所示：

```
# 首先定义一个redis相关操作的类
import redis
from redis.commands.search.query import Query
from redis.commands.search.field import TextField, VectorField

class RedisCache:
    def __init__(self, host: str = "localhost", port: int = 6379):
        self.cache = redis.Redis(host=host, port=port)

    def set(self, key: str, value: str):
        self.cache.set(key, value)

    def get(self, key: str):
        return self.cache.get(key)

    def TextField(self, name: str):
        return TextField(name=name)

    def VectorField(self, name: str, algorithm: str, attributes: dict):
        return VectorField(name=name, algorithm=algorithm, attributes=attributes)

    def getSchema(self, name: str):
        return self.cache.ft(name)

    def createIndex(self, index, schema):
        try:
            index.info()
        except redis.exceptions.ResponseError:
            index.create_index(schema)

    def dropIndex(self, index):
        index.dropindex(delete_documents=True)

    def hset(self, name: str, map: dict):
        self.cache.hset(name=name, mapping=map)

    def query(self, index, base_query: str, return_fields: list, params_dict: dict, num: int, startnum: int = 0):
        query = (
            Query(base_query)
            .return_fields(*return_fields)
            .sort_by("similarity")
            .paging(startnum, num)
            .dialect(2)
        )
        return index.search(query, params_dict)

# 初始化类
redis = RedisCache()
# 定义一个文本类型，用来储存知识库内容
info = TextField("info")
# 建立一个向量类型，使用HNSW算法
name="embedding"
algorithm="HNSW"
# DIM计算方法
r = self.engine.embeddings(q, model=model)
DIM = len(r)
attributes={
    "TYPE": "FLOAT32",
    "DIM": DIM,
    "DISTANCE_METRIC": "COSINE"
}
embed = VectorField(
    name=name, algorithm=algorithm, attributes=attributes
)
# 创建索引
scheme = (info, embed)
index = redis.getSchema(self.redisIndexName)
redis.createIndex(index, scheme)

# 接着把所有知识库内容进行向量化后储存进redis中
def insertData(self, model):
    j = 0
    for file in self.filesPath:
        for i in file.content:
            # i就是分片后的知识库内容
            embed = self.engine.embeddings(i, model = model)
            emb = numpy.array(embed, dtype=numpy.float32).tobytes()
            im = {
                "info": i,
                "embedding": emb,
            }
            name = f"{self.redisIndexName}-{j}"
            j += 1
            self.redis.hset(name, im)

# 查询
# 取最接近的10个结果
k = 10
base_query = f"* => [KNN {k} @embedding $query_embedding AS similarity]"
return_fields = ["info", "similarity"]
# question为用户的问题
qr = self.engine.embeddings(question, model = model)
params_dict = {"query_embedding": np.array(qr, dtype=np.float32).tobytes()}
index = self.redis.getSchema(self.redisIndexName)
result = self.redis.query(index, base_query, return_fields, params_dict, k)
for _, doc in enumerate(result.docs):
    # 查看相似度值和上下文内容
    print(doc.info, doc.similarity)
```

**2 RAG知识库难点**

在了解了RAG的原理后，我们就可以尝试编写相关代码，搭建一个本地问答知识库。但是在我们开始行动后，就会发现事情并不会按照我们所预料的发展。

## **2.1 难点一：大语言模型能力不足**

在我们的设想中，问答知识库是这样工作的：

1. 根据用户的提问，在知识库中找到最相似k个的内容。
2. 把这k个内容作为上下文，提供给大模型。
3. 大模型根据用户提问的上下文，给出准确的答案。

但是在实际应用的过程中，程序却无法按照我们的意愿运行，首先是问答的大语言模型能力不足，毕竟我们使用的是`qwen2:7b`这种小体积的大模型，无法和`GPT4`这类的大模型相比较。但是修改一下提问的方式或者上下文和问题之间的顺序，还是能比较好的达到我们预期的效果。

但是更重要的是embed大模型的能力同样存在不足，这里用开头例子进行说明，我们把`context`的内容简单修改一下，如下所示：

```
context = [
    "北京，上海，杭州",
    "苹果，橘子，梨",
    "太阳，月亮，星星"
]
```

然后再计算一次相似度，如下所示：

```
城市和北京，上海，杭州的相似度为：0.6192201604133171
城市和苹果，橘子，梨的相似度为：0.6401285511286077
城市和太阳，月亮，星星的相似度为：0.5885895914816769

水果和北京，上海，杭州的相似度为：0.6260800765574224
水果和苹果，橘子，梨的相似度为：0.6977096659034031
水果和太阳，月亮，星星的相似度为：0.619382129127254

天体和北京，上海，杭州的相似度为：0.5648588692973202
天体和苹果，橘子，梨的相似度为：0.7067548826946035
天体和太阳，月亮，星星的相似度为：0.75651740246562
```

我们发现，`"城市"`竟然和`"苹果，橘子，梨"`是最相似的。虽然这只是一个简单的例子，但是在实际的应用中经常会遇到这类的情况，通过用户提问的内容找到的知识库中最相似的内容有可能跟问题并不相关。

这是否是本地embed大模型的问题？OpenAI的embed大模型效果如何？接着我们找了一些本地embed大模型和OpenAI的`text-embedding-3-small`、`text-embedding-ada-002`、`text-embedding-3-large`进行一个简单的测试，判断通过问题找到的最相似的知识库上下文，是否是预期的内容。

最终的结果是，不管是本地的大模型还是OpenAI的大模型，成功率都在50%-60%之间。embed大模型的能力差是普遍存在的问题，并不仅仅是本地embed大模型的问题。

该问题经过我们一段时间的研究，找到了“将就”能用的解决方案，将会在后文细说。

## **2.2 难点二：提问的复杂性**

理想中的问答知识库是能处理复杂问题，并且能进行多轮对话，而不是一轮提问就结束。

以`Seebug Paper`作为知识库，提出的问题具体到某一篇文章，并且多轮对话之间的问题是相互独立的，这种情况是最容易实现的。比如：

```
user: 帮我总结一下CVE-2024-22222漏洞。
assistant: ......
user: CVE-2023-1111漏洞的危害如何？
assistant: ......
......
```

但是想要让问答知识库成为一个好用的产品，不可能把目标仅限于此，在实际的应用中还会产生多种复杂的问题。

1.范围搜索性提问

参考以下几种问题：

> 2024年的文章有哪些？
> CTF相关的文章有哪些？
> 跟libc有关的文章有哪些？
> ......

拿第一个问题举例，问题为：`2024年的文章有哪些？`。

接着问答知识库的流程为：

1. 通过embed模型对问题进行向量化。
2. 通过redis搜索出问题向量数据最接近的k个知...