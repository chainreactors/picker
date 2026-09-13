---
title: FDE工程实战02-RAG与Agent系统设计
url: https://mp.weixin.qq.com/s/ODR042kuhwdiiSNw1dTZKw
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:56:56.214946
---

# FDE工程实战02-RAG与Agent系统设计

# FDE工程实战02-RAG与Agent系统设计

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> RAG与Agent是当前AI应用工程的两大核心范式。本篇从FDE视角深入RAG架构的每一层工程决策、Agent系统的编排与工具调用、子智能体架构、Prompt工程生产化，以及生产环境Agent运维的完整体系——这些是把"能跑的Demo"变成"敢上生产的系统"的关键差距。

---

## 一、RAG架构深度工程

### 1.1 RAG系统架构总览

检索增强生成（Retrieval-Augmented Generation，RAG）的本质是**在生成前引入外部知识检索步骤**，使LLM的回答 grounded 在检索到的证据上，而非仅依赖参数化记忆。从工程视角看，RAG不是单一技术，而是一条由多个工程决策点串联的管线：

```
文档摄入 → 分块 → 嵌入 → 向量存储 → 索引维护
                                              ↓
用户查询 → 查询处理 → 检索 → 重排序 → 上下文组装 → 生成 → 后处理 → 引用标注
```

每个箭头处都是一个工程决策点。FDE的核心工作不是"调用LangChain的RetrievalQA.from\_chain\_type()"，而是在每个决策点根据客户业务约束做出合理选择并实现生产级代码。

**RAG的三个层次**

业界常把RAG分为三个成熟度层次，FDE需要根据客户场景选择合适的层次：

| 层次 | 名称 | 检索方式 | 适用场景 | 工程复杂度 |
| --- | --- | --- | --- | --- |
| Naive RAG | 朴素RAG | 单轮向量检索 | 简单QA、知识库小 | 低 |
| Advanced RAG | 高级RAG | 查询改写+混合检索+重排序 | 企业知识库、多源数据 | 中 |
| Modular RAG | 模块化RAG | 多路检索+Agent决策+自适应 | 复杂业务、多步推理 | 高 |

**Naive RAG的典型问题**：

1. 检索质量低：单轮向量检索无法处理查询语义与文档语义的错配
2. 上下文冗余：检索到的chunk可能大量无关，浪费token预算
3. 无引用溯源：用户无法验证回答的事实依据
4. 知识更新滞后：文档更新后向量索引未同步

**Advanced RAG的改进**：

在检索前引入查询改写（query rewriting）和查询扩展（query expansion），在检索后引入重排序（reranking）和上下文压缩（context compression），显著提升检索精度。

**Modular RAG的范式**：

把检索、生成、工具调用都视为可插拔模块，由Agent根据查询路由决策——简单问题走快速RAG路径，复杂问题走多步检索+推理路径，实时数据问题走工具调用路径。

FDE在客户现场的实践表明：**80%的企业RAG项目卡在Advanced RAG层次**，不是技术不够，而是工程决策没做对——分块策略不适合文档结构、嵌入模型与领域不匹配、检索策略未针对查询模式优化。

### 1.2 向量库选型对比

向量库是RAG系统的存储基石，选型直接影响检索性能、运维成本和扩展性。主流向量库可分为三类：

**类别一：专用向量数据库**

Pinecone、Weaviate、Milvus、Qdrant属于此类，从底层就为向量检索设计。

**Pinecone**：

* 架构：全托管SaaS，无需基础设施运维
* 索引类型：基于FAISS的IVF+PQ近似最近邻
* 规模：支持十亿级向量，单索引最大5GB（pod-based）
* 检索延迟：P99 < 100ms（同区域）
* 适合场景：快速上线、团队无向量库运维经验、规模在亿级以内
* 工程考量：数据驻留在AWS us-east-1等区域，对数据驻留要求严格的客户不适用
* 成本：pod-based每pod约$70/月，storage-based按用量计费

**Weaviate**：

* 架构：可自托管或云托管，GraphQL/REST API
* 索引类型：HNSW（Hierarchical Navigable Small World）
* 特色：内置模块化向量化（支持多嵌入模型切换）、混合检索（BM25+向量）
* 适合场景：需要灵活部署（自托管满足数据驻留）、需要内置混合检索
* 工程考量：自托管需要运维HNSW索引的内存消耗
* 混合检索：内置BM25+向量混合，无需额外搭BM25索引

**Milvus**：

* 架构：云原生分布式，支持K8s部署
* 索引类型：IVF\_FLAT/IVF\_PQ/HNSW/ANNOY/DiskANN等多种
* 规模：百亿级向量，分布式架构水平扩展
* 适合场景：超大规模向量、需要分布式部署、有专职运维团队
* 工程考量：部署复杂度高（etcd+MinIO+Pulsar+Milvus多组件），资源消耗大
* FDE实践：客户已有K8s集群时推荐，否则运维负担过重

**Qdrant**：

* 架构：Rust实现，单二进制部署，支持Docker/K8s
* 索引类型：HNSW，支持量化（Scalar/Product）降低内存
* 特色：过滤性能优秀（payload过滤下推到HNSW遍历）、单机性能强
* 适合场景：中等规模（千万级向量）、需要高效过滤、部署环境资源受限
* 工程考量：Rust生态成熟度，但API稳定且文档质量高

**类别二：数据库向量扩展**

pgvector（PostgreSQL扩展）、Elasticsearch向量搜索、Redis Stack属于此类。

**pgvector**：

* 架构：PostgreSQL扩展，向量作为一列存储
* 索引类型：IVFFlat、HNSW（0.5.0+）
* 检索性能：百万级向量P99 < 50ms（HNSW），千万级需要调优
* 适合场景：**已有PostgreSQL、数据规模在千万级以内、不想引入新组件**
* 工程优势：与业务数据同库，ACID事务保证，SQL查询能力
* FDE首选场景：客户已有PG且数据规模不大时，pgvector是最低运维成本的选择

```
-- pgvector生产级建表示例
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE knowledge_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    chunk_index INT NOT NULL,
    content TEXT NOT NULL,
    embedding vector(1536) NOT NULL,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- HNSW索引，针对余弦距离
CREATE INDEX idx_chunks_embedding
ON knowledge_chunks USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- 复合过滤索引（业务过滤+向量检索）
CREATE INDEX idx_chunks_doc_meta
ON knowledge_chunks USING gin (document_id, metadata jsonb_path_ops);

-- 检索查询（带业务过滤）
SELECT id, content, metadata,
       1 - (embedding <=> $1) AS similarity
FROM knowledge_chunks
WHERE document_id = ANY($2)
  AND metadata @> '{"access_level": "internal"}'
ORDER BY embedding <=> $1
LIMIT 20;
```

**Elasticsearch向量搜索**：

* 架构：ES 8.x+原生支持dense\_vector类型
* 索引类型：HNSW（Lucene 9+）
* 特色：与全文检索同库，天然支持混合检索
* 适合场景：**已有ES集群、需要全文+向量混合检索、日志+知识库统一搜索**
* 工程考量：向量检索性能不如专用库，但统一搜索栈的价值很大

**类别三：内存/轻量级**

Chroma、FAISS（Facebook AI Similarity Search）、LanceDB属于此类。

**Chroma**：

* 架构：嵌入式SQLite+DuckDB，单进程
* 适合场景：PoC、开发本地调试、小规模知识库（<100万向量）
* 工程考量：不适合生产多并发场景，无分布式能力

**FAISS**：

* 架构：C++库，Python绑定，纯内存
* 特色：索引类型最全（IVF/PQ/HNSW/NSG等），Meta维护活跃
* 适合场景：需要极致检索性能、内存充足、自行管理持久化
* 工程考量：无内置持久化、无网络服务、无过滤能力，需要自行封装

**FDE选型决策矩阵**

| 客户约束 | 推荐方案 | 理由 |
| --- | --- | --- |
| 已有PG，向量<1000万 | pgvector | 零新组件，运维成本最低 |
| 已有ES，需要混合检索 | ES dense\_vector | 统一搜索栈 |
| 无基础设施，快速上线 | Pinecone | 全托管，无需运维 |
| 数据驻留，可自托管 | Qdrant/Weaviate | 单二进制/容器部署 |
| 超大规模(>10亿) | Milvus | 分布式扩展 |
| PoC阶段 | Chroma | 零配置启动 |

**选型时的隐藏考量**

FDE在选型时还需要考虑客户不会主动提到但影响交付的因素：

1. **备份恢复**：向量索引能否备份？恢复时间多久？Pinecone的backup是SaaS级自动的，Milvus需要自行配置MinIO备份，pgvector随PG备份一起做
2. **版本升级**：向量库升级是否需要重建索引？Weaviate 1.x→1.y通常平滑，Milvus大版本升级可能需要reindex
3. **监控集成**：是否有Prometheus metrics暴露？Qdrant原生支持，Pinecone通过API指标，pgvector走PG监控
4. **多租户隔离**：SaaS场景下不同租户数据如何隔离？Pinecone用namespace，pgvector用RLS，Milvus用collection
5. **合规认证**：客户要求SOC2/ISO27001时，Pinecone有认证，自托管方案需要客户自行认证

### 1.3 嵌入模型选择与切换

嵌入模型（Embedding Model）将文本映射为稠密向量，是RAG检索质量的根本决定因素。选型维度包括：

**维度一：模型质量**

MTEB（Massive Text Embedding Benchmark）是当前最权威的嵌入模型评测基准，覆盖8类任务（检索、聚类、分类、重排序等）。FDE应关注MTEB的Retrieval子集分数，因为这直接对应RAG场景。

| 模型 | 维度 | MTEB检索分 | 商用许可 | 备注 |
| --- | --- | --- | --- | --- |
| text-embedding-3-large (OpenAI) | 3072 | 64.6 | API付费 | 闭源，仅API |
| text-embedding-3-small (OpenAI) | 1536 | 62.3 | API付费 | 性价比高 |
| voyage-3 (Voyage AI) | 1024 | 67.0 | API付费 | 检索专精 |
| bge-large-en-v1.5 (BAAI) | 1024 | 63.9 | MIT | 开源可自托管 |
| bge-m3 (BAAI) | 1024 | 66.1 | MIT | 多语言、多功能 |
| e5-mistral-7b-instruct | 4096 | 68.7 | MIT | 质量最高但大 |
| gte-large-zh (阿里) | 1024 | - | Apache-2.0 | 中文专精 |
| jina-embeddings-v3 | 1024 | 65.7 | CC-BY-NC | 非商用需许可 |

**维度二：领域适配**

通用嵌入模型在特定领域（医疗、法律、金融）的检索质量会显著下降。FDE处理领域适配的策略：

**策略一：选择领域专精模型**

* 医疗：BioBERT-based embeddings、PubMedBERT-based
* 法律：Legal-BERT-based、CaseLawBERT
* 金融：FinBERT-based

**策略二：微调通用模型**

使用领域数据对通用模型进行对比学习微调。需要构造正负样本对：

```
from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader

# 领域微调数据：(query, positive_doc, negative_doc)三元组
train_examples = [
    InputExample(
        texts=[
            "What is the maximum loan-to-value ratio for FHA loans?",  # query
            "FHA loans require a minimum down payment of 3.5%, meaning the LTV ratio can be up to 96.5%.",  # 正样本
            "Conventional loans typically require 20% down payment."  # 负样本
        ]
    )
    # ... 更多领域样本
]

base_model = SentenceTransformer("BAAI/bge-large-en-v1.5")
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=32)
train_loss = losses.MultipleNegativesRankingLoss(base_model)

base_model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    epochs=3,
    warmup_steps=100,
    show_progress_bar=True,
    output_path="./models/finance-embeddings-v1"
)
```

**策略三：领域感知重排序**

不在嵌入阶段做领域适配，而在重排序阶段用领域模型重排序。这是FDE更常用的策略，因为：

* 嵌入模型微调需要大量标注数据，客户通常没有
* 重排序模型可以更轻量地适配领域
* 嵌入模型保持通用，便于跨场景复用

**维度三：多语言处理**

客户知识库多语言时的嵌入模型选择：

* **单语言模型+翻译管线**：用强模型（如GPT-4）翻译后嵌入，质量高但成本高
* **多语言模型**：bge-m3、multilingual-e5-large等，直接跨语言检索
* **混合策略**：高频语言用专精模型，低频语言用多语言模型，路由层决策

**维度四：维度与成本**

嵌入维度直接影响存储成本和检索速度：

```
存储成本 = 向量数 × 维度 × 4字节（float32）
检索成本 ∝ 维度（点积计算量）
```

以100万向量为例：

* 3072维（OpenAI large）：100万 × 3072 × 4 = 12GB存储
* 1536维（OpenAI small）：100万 × 1536 × 4 = 6GB存储
* 768维（bge-base）：100万 × 768 × 4 = 3GB存储

OpenAI text-embedding-3支持**维度截断**（Matryoshka Representation Learning），可以在3072维训练后截断到256/512/1024维使用，质量损失很小。这给FDE提供了灵活性：生产用1024维平衡质量与成本，离线分析用3072维追求最高质量。

**嵌入模型切换的工程实现**

生产系统中嵌入模型可能需要切换（模型升级、成本优化、质量调优），切换不是简单替换，需要处理已有向量：

```
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
import hashlib
import time

@dataclass
class EmbeddingResult:
    vector: list[float]
    model_name: str
    model_version: str
    dim: int
    embed_time_ms: float

class EmbeddingProvider(ABC):
    """嵌入模型提供者抽象基类"""

    @abstractmethod
    def embed(self, texts: list[str]) -> list[EmbeddingResult]:
        ...

    @abstractmethod
    def model_id(self) -> str:
        """唯一标识模型+版本，用于向量索引版本管理"""
        ...

clas...