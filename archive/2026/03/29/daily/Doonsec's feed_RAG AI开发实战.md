---
title: RAG AI开发实战
url: https://mp.weixin.qq.com/s/w7SakmjNqYIEeeyQKDPw2A
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:41:28.078627
---

# RAG AI开发实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XHKUQGK0BNHhqF83SQ808dHtUswPF9WxSWTibUaEvHup3X97qicxWLtpibwz94pDnCG9UdG4Re7eb1NVscWvHczsjG6KV25KQVAM202Nj2L70Y/0?wx_fmt=jpeg)

# RAG AI开发实战

原创

凌木LSJ
凌木LSJ

AI技术LSJ

![]()

在小说阅读器中沉浸阅读

## 1. 什么是 RAG ？

RAG（Retrieval-Augmented Generation）

* 检索增强生成，是一种结合信息检索（Retrieval）和文本生成（Generation）的技术
* RAG技术通过实时检索相关文档或信息，并将其作为上下文输入到生成模型中，从而提高生成结果的时效性和准确性。
* 用户输入+检索信息 ——〉 大模型输入 ——〉大模型生成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNHqUgqZYwa0MnVcIeLQJXhjSFs9ytn9HQovw97zYVh7hVqBMGiaIre0B6xTzR4oqqibDudc46wnFiaIeVPJPaicRQNLX8f3iccm2zEI/640?wx_fmt=png&from=appmsg)

RAG 的优势是什么？

* **解决知识时效性问题：**大模型的训练数据通常是静态的，无法涵盖最新信息，而RAG可以检索外部知识库实时更新信息
* **减少模型幻觉：**通过引入外部知识，RAG能够减少模型生成虚假或不准确内容的可能性
* **提升专业领域回答质量：**RAG能够结合垂直领域的专业知识库，生成更具专业深度的回答
* **生成内容的溯源（可解释性）**

## 2 Embedding

在人工智能领域，向量表征（Vector Representation）是核心概念之一。通过将文本、图像、声音、行为甚至复杂关系转化为高维向量（Embedding），AI系统能够以数学方式理解和处理现实世界中的复杂信息。这种表征方式为机器学习模型提供了统一的“语言”。

1. 将文本转成一组 N 维浮点数，即**文本向量**又叫 Embeddings
2. 向量之间可以计算距离，距离远近对应**语义相似度**大小

![](https://mmbiz.qpic.cn/mmbiz_png/XHKUQGK0BNGvvibhmneolicESAx1gCeCHDfVJgZrqAfF0nHGcG3srkdkS9JLrhNa0Wwo7rTibfRHAkulicXY2nvC2LymN45h4wcFCZFiamFN22og/640?wx_fmt=png&from=appmsg)

## 3 RAG入门到精通

### 3.1 Naive RAG（基础RAG）

Query -> 检索 -> Prompt -> LLM -> 回复

#### langchain实现

```
langchain                                0.3.27 langchain-community                      0.3.27 langchain-core                           0.3.79 langchain-huggingface                    0.3.1 langchain-mcp-adapters                   0.1.13
```

```
from langchain_community.document_loaders import PyPDFLoaderfrom langchain_text_splitters import RecursiveCharacterTextSplitterfrom langchain_core.vectorstores import InMemoryVectorStore# 解析PDFfile_path = "./data/考核办法.pdf"loader = PyPDFLoader(file_path)docs = loader.load()# 拆分文档text_splitter = RecursiveCharacterTextSplitter(    chunk_size=200, chunk_overlap=50, add_start_index=True)all_splits = text_splitter.split_documents(docs)# 索引建立vector_store = InMemoryVectorStore(embeddings)ids = vector_store.add_documents(documents=all_splits)#检索results = vector_store.similarity_search("客户经理每年评聘申报时间是怎样的？")print(results[0])
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNEviar3gnQpx5ZgbK7Rv9DYKtj5picue3OZCOL1a0jxutfzRiaNuVAL06e7HeWrAnaxh8yeXhSXubYXAGmfKk4cdUmSRicicGuQUbO8/640?wx_fmt=png&from=appmsg)

### 3.2 Advanced RAG（增强RAG）

```
User Query        用户查询
```

```
↓
```

```
Query Rewrite     问题重写
```

```
↓
```

```
Vector Retrieval  问题检索
```

```
↓
```

```
Rerank            重排序
```

```
↓
```

```
Context           内容生成
```

```
↓
```

```
LLM Answer
```

```

```

1）加载RAG向量数据库，转换成检索工具

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNE9ZoJVsw9Z1Cpm9ds4UzIv5w64kZibrMG2ayfPzOmMvtCBsicxVXb06UnSiaRnicp1rHaXKkffkDR6RYrGDFicHym51SiaKpyOUpnibY/640?wx_fmt=png&from=appmsg)

#### 2）查询重写

```
from langchain_openai import ChatOpenAIfrom langchain.prompts import ChatPromptTemplatefrom langchain.schema.output_parser import StrOutputParserllm = ChatOpenAI(        api_key = os.getenv("DASHSCOPE_API_KEY"),        base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",        model = "deepseek-v3"    )rewrite_prompt = ChatPromptTemplate.from_template("""Rewrite the user query to be better for document retrieval.User query:{query}Rewritten query:""")query_rewriter = rewrite_prompt | llm | StrOutputParser()
```

#### 3）检索文档与重排序

```
from sentence_transformers import CrossEncoder
docs = retriever.invoke(rewritten_query)#使用重排序模型model_dir = "/model/BAAI/bge-reranker-large"reranker = CrossEncoder("BAAI/bge-reranker-large", cache_folder=model_dir)
pairs = [[query, d.page_content] for d in docs]scores = reranker.predict(pairs)reranked_docs = [    doc for _, doc in sorted(        zip(scores, docs),        key=lambda x: x[0],        reverse=True    )]top_docs = reranked_docs[:3]
```

4）内容生成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNHzr0Pn25G5lH858GZR7LASxCicnXiaFiceVqmvdIo6FQgUCUW9f7SibibAEgrSXzDUGPztd0Vwc2tJYKJXhlRKM7DhpgHWzeDbZb9s/640?wx_fmt=png&from=appmsg)

### 3.3 Agentic RAG（Agent RAG）

```
User Question
```

```
│
```

```
▼
```

```
Agent (LLM Reasoning)
```

```
    │
```

```
┌───┴───────────────┐
```

```
│                   │
```

```
▼                   ▼
```

```
Use Retriever     Direct Answer
```

```
│
```

```
▼
```

```
Retrieve Docs
```

```
│
```

```
▼
```

```
LLM Generate Answer
```

#### 1）构建检索 工具Tool

```
from langchain.tools import tool
@tooldef search_knowledge(query: str) -> str:    """Search information from the knowledge base"""
    docs = retriever.invoke(query)    return "\n".join([d.page_content for d in docs])
```

#### 2）创建Agent（langchain0.3 与 langchain1.x创建Agent方式不同）

```
from langchain.agents import AgentExecutor, create_react_agentfrom langchain.agents import initialize_agent, AgentTypefrom langchain import hub
tools = [search_knowledge]prompt = hub.pull("hwchase17/react")agent = create_react_agent(    llm,    tools,    prompt)agent_executor = AgentExecutor(    agent=agent,    tools=tools,    verbose=True)
```

#### 3）运行 Agentic RAG

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNHzrR6GLe3TUszOnYjpgNaZetmkEISTXSRjmA8ibUfiaraaq8p2heG0bXWIibv56OJWHF0xaexaxSgs6ecibKib52sAIef36n0bVdgs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XHKUQGK0BNE6BRdntDET0aEiaOSu8OAqmOev5cdLOD2vg7pOVvwibkciasglZ5gQHpFmEUSLuVs4wGps8xqVt2OctEbPNyFlEN8yGVwOBJm7tw/640?wx_fmt=png&from=appmsg)

4. RAG开发中三个关键阶段

1）数据准备

这是RAG的基础，决定了检索的“原料”质量。

* **数据清洗与预处理**：移除特殊字符、统一编码、纠正OCR错误。如果原始数据包含大量噪声（如网页导航栏、PDF页眉页脚），检索时容易引入干扰。
* **文档解析与分块**：

+ **分块策略**：块太大，检索精度下降，且容易塞入无关信息；块太小，上下文缺失，语义不完整。常见的策略包括按语义（段落、章节）切分、重叠切分（Overlap）或基于文档结构（Markdown层级）的智能切分。
+ **元数据附加**：为每个块添加来源、时间戳、章节标题、文件名等元数据。这在后续检索中可以进行过滤，并提升答案引用的准确性。

* **Embedding模型选择**：针对特定领域（选择或微调Embedding模型，比使用通用模型能显著提升检索的召回率。

2）知识检索

这一阶段的目标是在海量数据中快速、精准地找到与问题最相关的上下文。

* **检索范式**：

+ **向量检索**：利用语义相似度，适合处理同义词、多轮转述等模糊匹配问题。
+ **混合检索**：结合向量检索（语义）和关键词检索，是当前工业界的主流做法。

* **检索后处理**：

+ **重排序**：初检可能召回Top-10个块，但大模型的上下文窗口有限。通过一个精排模型（如Cross-Encoder）对这些块进行重新打分，筛选出最相关的Top-K（通常是5个），能极大提升答案的准确性。

3）答案生成

这是RAG的最后一步，也是用户直接感知价值的一环。

* **提示词工程**：需要明确指令，如“严格基于以下上下文回答，如果上下文没有提及，请直接说不确定”，以减少大模型产生幻觉或过度发挥的风险。同时，要求在回答中引用来源（如“根据[文档A]第3页...”），以增强可信度。
* **对话与记忆管理**：在多轮对话场景下，需要考虑将历史对话压缩或摘要，再与当前问题一起进行检索。否则，当用户问“那它的价格呢？”时，系统无法知道“它”指代什么。
* **Agentic RAG**：在复杂场景下，单一的向量检索可能不够。可以引入智能体（Agent）自主决策：是先查数据库，还是调用API（应用程序接口），或者进行多跳检索（Multi-hop，即先检索出A文档，从A文档中提取实体再去检索B文档）。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XHKUQGK0BNHPd1F9v90aKgxLcUKK26W2ibae6BYQC0Nbzqn1JS9FRHSK78InKaIVM9QicB3D69xU8nmlUWAjAJNaNeibggBYIAePFkrqcADUn4/0?wx_fmt=png)

AI技术LSJ

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XHKUQGK0BNHPd1F9v90aKgxLcUKK26W2ibae6BYQC0Nbzqn1JS9FRHSK78InKaIVM9QicB3D69xU8nmlUWAjAJNaNeibggBYIAePFkrqcADUn4/0?wx_fmt=png)

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