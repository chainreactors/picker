---
title: 一个项目带你入门AI应用开发03 - bamb00
url: https://www.cnblogs.com/goodhacker/p/22137580
source: 博客园 - bamb00
date: 2026-08-01
fetch_date: 2026-08-02T05:10:35.324744
---

# 一个项目带你入门AI应用开发03 - bamb00

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [周边](https://cnblogs.vip/store)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19316348)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://www.cnblogs.com/my "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://www.cnblogs.com/my)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/goodhacker/)

# [人怜直节生来瘦，自许高材老更刚。](https://www.cnblogs.com/goodhacker)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/goodhacker/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/bamb00)
* 订阅
* [管理](https://i.cnblogs.com/)

# [一个项目带你入门AI应用开发03](https://www.cnblogs.com/goodhacker/p/22137580 "发布于 2026-08-01 19:53")

# 第 3 课：让 Agent 拥有知识库（Chroma 向量检索 + RAG）

## 3.1 你的目标

用户问"怎么退货"，程序从知识库中找到相关文档，结合 LLM 生成回答：

```
You: 怎么退货？
[检索到 2 篇相关文档]
AI: 我们支持7天无理由退货。您可以在"我的订单"中申请退货，
    填写原因后寄回商品，退款将在收到退货后3-5个工作日内返还。
```

## 3.2 反例：直接把知识库塞进 system prompt

```
all_knowledge = "支持7天无理由退货...全国配送3-5个工作日..."
reply = call_llm([
    {"role": "system", "content": f"以下是知识库：\n{all_knowledge}"},
    {"role": "user", "content": "怎么退货？"},
])
```

### 这样为什么不行？

三个问题：

**问题 1：Token 限制。** 知识库有 100 篇文档，每篇 200 字，总字数 20000。而 LLM 的上下文窗口通常只有 4K-8K tokens（约 3000-6000 中文字）。塞不进去。

**问题 2：迷失在长文本中。** 即使上下文窗口够大（比如 128K tokens），LLM 在超长文本中依然会"走神"——它可能忽略掉关键信息。这叫"Lost in the Middle"现象。

**问题 3：知识更新要改代码。** FAQ 加了新内容，你要重新部署整个系统。

### 本质问题是什么？

"少即是多"。把全部知识库塞给 LLM，和把最相关的 3 篇文档塞给它，效果反而是后者更好——因为 LLM 不需要从噪音中寻找信号。

## 3.3 正解：RAG（检索增强生成）

RAG = Retrieval-Augmented Generation。

```
用户问题 → 检索最相关的文档 → 文档 + 问题 → LLM 生成回答
```

核心是检索这一步：怎么找出和用户问题最相关的文档？

## 3.4 从关键词匹配到向量检索

### 方式一：关键词匹配（Jaccard 相似度）

把用户问题和文档都拆成"词的集合"，计算交集占并集的比例。

```
query = "怎么退款" → {怎, 么, 退, 款}
doc   = "支持7天无理由退货" → {支, 持, 天, 无, 理, 由, 退, 货, ...}
Jaccard = 交集{退} / 并集{怎,么,退,款,支,持,天,...} ≈ 很低
```

"退款"和"退货"共享一个"退"字，Jaccard 得分极低，尽管它们在语义上高度相关。

### 方式二：向量检索（Chroma + Embedding）

把文本转换成向量（数字序列），语义相近的文本向量在空间中也相近。

```
"怎么退款" → [0.23, 0.87, -0.12, ...]  (768 维向量)
"支持7天无理由退货" → [0.25, 0.82, -0.10, ...]  (语义相近，向量也相近)
余弦相似度 ≈ 0.85
```

**Embedding 模型** 负责"文本 → 向量"的转换。我们用的是 sentence-transformers 的 `paraphrase-multilingual-MiniLM-L12-v2`——支持中英文的小模型。

**Chroma** 负责存储向量和做相似度搜索。它就像 MySQL 但存的是向量。

### 为什么 Chroma 而不是自己算？

| 需求 | 自己实现 | 用 Chroma |
| --- | --- | --- |
| 存储向量 | 自己写文件格式 | 自动持久化到磁盘 |
| 相似度搜索 | 暴力遍历 O(n) | 自动建索引，速度快 |
| 增删文档 | 手动管理 | add/delete/update API |
| 服务重启 | 向量要重新算 | 重启后数据还在 |

如果知识库只有 5 篇文档，自己算也行。但一旦到了 50 篇、500 篇，你就需要 Chroma 了。

## 3.5 Chroma 的使用方式

### 初始化

```
import chromadb
from chromadb.utils import embedding_functions

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.create_collection(
    name="knowledge_base",
    embedding_function=ef,
)
```

`PersistentClient` 把数据存在磁盘上。服务重启后数据还在。

### 写入

```
collection.add(
    ids=["faq_01", "faq_02"],
    documents=["支持7天无理由退货...", "全国配送3-5个工作日..."],
    metadatas=[{"source": "退货政策"}, {"source": "配送说明"}],
)
```

`add` 会自动调用 embedding 函数把 documents 转成向量再存起来。

### 查询

```
results = collection.query(
    query_texts=["怎么退款"],
    n_results=3,
)
```

`query` 会把"怎么退款"转成向量，然后找到向量空间中最近的 3 个文档。

## 3.6 完整的 RAG 流程

```
def answer_with_knowledge(user_input):
    # Step 1: 检索
    results = get_collection().query(query_texts=[user_input], n_results=3)
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    # Step 2: 拼上下文
    context = ""
    for i, doc in enumerate(documents):
        source = metadatas[i]["source"]
        context += f"[{source}] {doc}\n\n"

    # Step 3: LLM 生成
    reply = call_llm([
        {"role": "system", "content": "根据知识库文档回答用户问题。不够时诚实告知。"},
        {"role": "user", "content": f"文档：{context}\n\n问题：{user_input}"},
    ])
    return reply
```

**从检索到生成，只有三步。** 这就是 RAG 的全部。

## 3.7 如何判断检索质量

一个简单的测试方法：

```
# 测试1：同义词
print(answer_with_knowledge("怎么退款"))
# 应该匹配到"退货政策"而不是"配送说明"

# 测试2：模糊描述
print(answer_with_knowledge("听歌的耳机多少钱"))
# 应该匹配到"智能蓝牙耳机 Pro"而不是"无线充电板"

# 测试3：不存在的内容
print(answer_with_knowledge("你们在纽约有店吗"))
# 应该诚实回答："我找不到相关信息"
```

测试 1 能跑通，说明向量检索比关键词匹配好。测试 3 能跑通，说明 system prompt 的"不够时诚实告知"起到了作用。

## 本课知识点

| 概念 | 你做了什么 | 为什么 |
| --- | --- | --- |
| RAG | 检索 → 生成 | 不让 LLM 凭空回答，给它参考依据 |
| 向量检索 | Chroma + embedding | 语义匹配，"退款"能匹配"退货" |
| Chunking | 按文档组织（未分块） | 为后续长文档分块做铺垫 |
| Embedding | sentence-transformers | 把文本变成语义向量 |

## 课后作业

1. 在 `seed_knowledge.py` 中加一篇 500 字的长文档，观察检索时能不能精确命中特定段落
2. 把 embedding 模型换成 `all-MiniLM-L6-v2`（纯英文），问中文问题看看效果有什么变化
3. 试一个 Jaccard 匹配不上但语义相似的问题（如"音频设备"匹配"耳机"），看 Chroma 能不能找到

## 面试可能会问

> "RAG 的检索质量对最终回答质量有多大影响？"
> 检索决定了 LLM 能看到什么。如果检索阶段就没找到相关文档，LLM 再强也答不对。所以 RAG 系统的瓶颈通常在检索，不在生成。

> "为什么用 Chroma 而不是自己写向量搜索？"
> 持久化、索引加速、增删 API 都是你自己实现很麻烦的事情。Chroma 把这些封装好了。5 篇文档可以不选，50 篇以上建议选。

posted @
2026-08-01 19:53
[bamb00](https://www.cnblogs.com/goodhacker)
阅读(5)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fgoodhacker%2Fp%2F22137580&targetId=22137580&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202607/35695-20260715081632770-1485313413.webp)](https://www.trae.com.cn/?utm_source=advertising&utm_medium=cnblogs_ug_cpa&utm_term=hw_trae_cnblogs)

### 公告

[博客园](https://www.cnblogs.com/)
  ©  2004-2026

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)