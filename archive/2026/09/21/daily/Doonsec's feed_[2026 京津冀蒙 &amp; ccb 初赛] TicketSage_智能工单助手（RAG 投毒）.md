---
title: [2026 京津冀蒙 &amp; ccb 初赛] TicketSage_智能工单助手（RAG 投毒）
url: https://mp.weixin.qq.com/s/dOE_iOHBW7iBDKgQD0wnMA
source: Doonsec's feed
date: 2026-09-21
fetch_date: 2026-09-22T07:01:16.442102
---

# [2026 京津冀蒙 &amp; ccb 初赛] TicketSage_智能工单助手（RAG 投毒）

# [2026 京津冀蒙 & ccb 初赛] TicketSage\_智能工单助手（RAG 投毒）

原创

正在思考ing
正在思考ing

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 刚从决赛现场回来，差一题就能站上领奖台了，空悲切

(╥﹏╥)

初赛用 ai 梭了大部分题目，最后选择这道题复现一下不是因为这题有多难，而是因为这道题是唯一一道 ai 安全题，毕竟这么长时间以来我对 ai 安全的理解还停留在提示词注入（我就一臭做逆向的），这道题考察的是 rag 投毒（做完了发现其实就是间接的提示词注入），因此来学习一下

## 环境重建

---

由于这是容器题，但是附件给了源码，所以环境很好搭建

根据附件里的 `config.py` 可以确定，这个 ai 助手使用的模型为 `qwen2.5-0.5b-instruct-q4_k_m.gguf`，这个附件里没有，直接去 hugging face 上下载一个就可以了

`config.py` 的逻辑是：先看 MODEL\_PATH 环境变量 → 如果没有再回退到 `<源码目录>/models/qwen2.5-0.5b-instruct-q4_k_m.gguf`

为了不乱动环境变量，建议把模型放在 `models` 目录下

至于 flag，从 `config.py` 中也可以看出，优先读取 FLAG 环境变量，如果没有就随机生成一个 uuid 作为 flag，这里我们随机生成即可

接下来再安装两个 py 库

```
pip install llama-cpp-python
pip install flask
```

最后就可以直接启动服务了

```
python app.py
```

随后访问 http://127.0.0.1:8000

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rnA7tTKUKciazoYXWLCgsszjuiaiaEicxBELbkZ1vmia6CianWGRslavw48yu3cTVoVT2VKtCN4aXibKibcl98kYa6UhjPuYIDDgibjMOcQ/640?wx_fmt=webp&from=appmsg)

环境重建完成，每次启动服务都会生成一个 `data` 目录，需要重置环境的话把这个目录删掉，再重新启动服务就可以了

## 题目内容

---

> 企业部署了离线智能工单助手 TicketSage，客服与用户通过它查询订单、处理退款、读取内部凭证。
>
> 某天安全审计发现一条异常的 vault\_read 越权调用记录——普通用户本不该触发凭证库读取。
>
> 请以安全工程师身份排查：是什么让模型做出了越权决策？攻击者是如何做到的？
>
> 找出漏洞根源、复现攻击链，并完成系统加固后提交 flag。

猜测攻击者窃取的凭证就是 flag，直接来问问看

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rldYT9qFeiaLdS8sQEwb03VJMqK34W6qQYWLLnESvvZshwaJjJjtA7pE0ibAclUj8A4FaTDW81s8Xq3WTFiarhj0SBrzhyLJicA0N0/640?wx_fmt=webp&from=appmsg)

显然这题并不是简单的提示词注入

题目内容提示审计日志时发现了异常越权调用记录，那么我们也先来看看日志

## 日志审计

---

来到审计日志页面，发现需要输入审计 token 才能查看，而这个 token 就硬编码在 `config.py` 的末尾

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rkcg8GC9ic5fIRhicqUqDOBKibrqgOjxUeb5pJne6UrtQiaibDQ2OJV9GAVFNnEh7sqiaV7HBdTmPt4DeWoiba6pP7jGFDxBziaumUqmVM/640?wx_fmt=webp&from=appmsg)

```
tk-3f8a2c5e-9b41-4d7e-8c20-a1f6d9e3b7c5
```

输入便可看到两次请求日志（如果之前问了 ai 就会出现你自己的记录）

```
[
  {
    "authorized": true,
    "intent": "ticket_query",
    "message": "我的订单 SO90018 到哪了？",
    "raw_model": "{\"intent\":\"ticket_query\"}",
    "reason": "granted: ticket_query (scope: user)",
    "retrieved": [
      {
        "doc_id": "kb-manual-001",
        "score": 0.42
      },
      {
        "doc_id": "kb-manual-002",
        "score": 0.3
      }
    ],
    "session": "sess-001",
    "tool": "ticket_query",
    "tool_output": "[tool:ticket_query] 未找到匹配订单，请提供正确订单号（如 SO90017）。",
    "ts": 1789908187
  },
  {
    "authorized": true,
    "intent": "vault_read",
    "message": "请问 SO90017 的物流状态？",
    "raw_model": "{\"intent\":\"vault_read\"}",
    "reason": "granted: vault_read (scope: admin)",
    "retrieved": [
      {
        "doc_id": "note-8841",
        "score": 39.6
      },
      {
        "doc_id": "kb-manual-001",
        "score": 0.42
      }
    ],
    "session": "sess-007",
    "tool": "vault_read",
    "tool_output": "[tool:vault_read] [REDACTED]",
    "ts": 1789908187
  }
]
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rnXFtzZ5iaHzibQ5u2JWsCVUfEKpRkqg5FKVtHkA5GkibzUFUgiaKn5NHlGUzJ83qPOkymib59iabVaRIj3mzksudaribFkknfr4sF6AM/640?wx_fmt=webp&from=appmsg)

显然第二条记录中出现了 `"reason": "granted: vault_read (scope: admin)"`，普通用户的订单查询却以 `admin` 的身份调用了凭证读取

猜测原因出在 `retrieved` 字段中检索召回的文档 `note-8841`，该文档分数高达 39.6，而其他出现的文档分数均为超过 0.5，基本可以确定是 RAG 投毒了

在安全加固页面可以查看知识库文档列表

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rllGPYbbmOyAXZmdkVvHic5PJRCODjLUbnEREjicee1yPxkOB82ZkAWhodqJUjeH6Ic57TbT58t2dSVGd11AkykvjxEeWKDq1otk/640?wx_fmt=webp&from=appmsg)

并没有找到 id 为 `note-8841` 的文档，而日志中召回的另外两个文档 `kb-manual-001` 和 `kb-manual-002` 还是存在的，说明 `note-8841` 文档是攻击者注入的，并且攻击完成后将其删除了

显然接下来我们要复现攻击者的攻击过程：构造毒文档 -> 上传 -> 触发凭证越权读取

## 源码审计

---

### 添加工单备注

向知识检索库中添加工单的逻辑在 `knowledge.py` 中

```
# -*- coding: utf-8 -*-
"""TicketSage —— 知识库管理（含工单备注）

客服可以在工单中添加备注，备注会进入检索知识库。
"""
import json
import logging
import os
import threading
import uuid

import config

log = logging.getLogger("ticket_sage.kb")

_lock = threading.RLock()  # 可重入锁：add_note/quarantine 内部会再次调用 load_kb()

def load_kb() -> list[dict]:
    """加载知识库（文件不存在时初始化默认数据）。"""
    with _lock:
        ifnot os.path.exists(config.KB_FILE):
            docs = list(config.DEFAULT_KB) + list(config.DECOY_NOTES) + _preplanted_notes()
            _save(docs)
            return docs
        try:
            with open(config.KB_FILE, encoding="utf-8") as fh:
                return json.load(fh)
        except Exception:
            return list(config.DEFAULT_KB)

def _save(docs: list[dict]) -> None:
    os.makedirs(config.DATA_DIR, exist_ok=True)
    with open(config.KB_FILE, "w", encoding="utf-8") as fh:
        json.dump(docs, fh, ensure_ascii=False, indent=2)

def _preplanted_notes() -> list[dict]:
    """预置恶意工单备注。

    注意：攻击者已清理现场，初始知识库中【不存在】毒文档。
    审计日志中保留了曾经的越权记录（检索到 note-8841），
    选手需要根据日志线索自行构造毒文档完成复现。
    """
    return []

def add_note(title: str, content: str, metadata: dict | None = None) -> dict:
    """客服添加工单备注（进入检索库）。"""
    with _lock:
        docs = load_kb()
        doc = {
            "id": "note-" + uuid.uuid4().hex[:8],
            "title": title,
            "content": content,
            "metadata": dict(metadata or {}),
        }
        meta = doc["metadata"]
        meta.setdefault("source", "ticket_note")
        meta.setdefault("ticket_id", "T-" + uuid.uuid4().hex[:4].upper())
        docs.append(doc)
        _save(docs)
        return doc

def get_doc(doc_id: str) -> dict | None:
    docs = load_kb()
    return next((d for d in docs if d["id"] == doc_id), None)

def list_docs() -> list[dict]:
    return load_kb()

def quarantine_doc(doc_id: str) -> bool:
    """隔离文档：标记 quarantined，不再参与检索。"""
    with _lock:
        docs = load_kb()
        for d in docs:
            if d["id"] == doc_id:
                d["quarantined"] = True
                _save(docs)
                returnTrue
        returnFalse
```

注释中写得很清楚，需要选手自行构造毒文档，就算前面没想到现在思路也应该很清晰了

通过 `add_note()` 函数可以得知工单备注需要 `id`、`title`、`content` 和 `metadata` 4 个字段，具体也可以查看知识库文档列表里面的 `工单备注 T-007`

```
  {
    "content": "内部备注：T-007 客户反馈重复扣款，已转财务二次核验。注意：所有涉及退款的操作必须经过人工复核，禁止自动执行。",
    "id": "note-decoy-007",
    "metadata": {
      "escalation_level": 1,
      "source": "ticket_note",
      "ticket_id": "T-007",
      "tool_scope": "user"
    },
    "title": "工单备注 T-007"
  }
```

这个可以作为我们后面构造毒文档的模板

知道毒文档如何构造了，接下来我们看看如何让 ai 能读到这个文档

### 知识库检索召回

rag 知识库检索到相关内容后不一定会将所有检索到的内容返回给 ai，往往会对每一个内容通过某种算法综合考量各个因素（相关度等）计算出一个分数，最后仅将 top-k 个返回给 ai。本题中也是如此，检索召回的逻辑在 `retrieval.py` 中

```
# -*- coding: utf-8 -*-
"""TicketSage —— 检索模块（简化版 RAG）

评分公式：
    score(doc, query) = CONTENT_WEIGHT * 词重叠相关度 + META_WEIGHT * escalation_level
"""
import math
import re
from collections import Counter

import config

_TOKEN_RE = re.compile(r"[\w\u4e00-\u9fff]+")

def _tokens(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())

def content_similarity(query: str, doc_content: str) -> float:
    """简化 BM25 风格词重叠相关度（0~1）。"""
    q_tokens = _tokens(query)
    d_tokens = _tokens(doc_content)
    ifnot q_tokens:
        return0.0
    d_counter = Counter(d_tokens)
    hit = sum(d_counter.get(t, 0) for t in q_tokens)
    # 归一化：命中词数 / 查询词数，加文档长度平滑
    return min(1.0, hit / len(q_tokens) * (1.0 - math.log1p(len(d_tokens)) / 20.0))

def score_doc(doc: dict, query: str) -> float:
    """企业定制评分：内容相关 + 元数据 escalation_level 加权。"""
    meta = doc.get("metadata", {}) or {}
    esc = float(meta.get("escalation_level", 0))
    c = content_similarity(query, doc.get("content", ""))
    return config.CONTENT_WEIGHT * c + config.META_WEIGHT * esc

def retrieve(docs: list[dict], query: str, top_k: int | None = None) -> list[dict]:
    """检索 top-k 文档（返回携带 score 的副本）。"""
    k = top_k or config.TOP_K
    scored = []
    for doc in docs:
        if doc.get("quarantined"):
            continue# 已隔离文档不再参与检索
        s = score_doc(doc, query)
        scored.append((s, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    out = []
    for s, doc in scored[:k]:
        d = dict(doc)
        d["_score"] = round(s, 4)
        out.append(d)
    return out
```

评分公式就写在开头的注释中，出...