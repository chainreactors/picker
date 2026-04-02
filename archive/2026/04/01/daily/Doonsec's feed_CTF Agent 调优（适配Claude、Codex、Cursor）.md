---
title: CTF Agent 调优（适配Claude、Codex、Cursor）
url: https://mp.weixin.qq.com/s/ArOdW2T1tMq5ouPT1QO9mg
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:24:46.386378
---

# CTF Agent 调优（适配Claude、Codex、Cursor）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVnmT1Uz0uhOoOZ5bhSkBrWBUZwsia5y570bdhEfFyjXczZiaEClr43SaLE0xNhpuQy9Gf8wMFsv81Hwsap8dkEP1aP15xgOWWZlU/0?wx_fmt=jpeg)

# CTF Agent 调优（适配Claude、Codex、Cursor）

原创

江思澄
江思澄

云晞科技Sec

![]()

在小说阅读器中沉浸阅读

## 自建 RAG 检索与向量库：让 CTF Agent 拥有专属知识大脑

> 在 CTF 竞赛中，Agent 的知识边界直接决定解题上限。通用大模型对冷门漏洞、私有 writeup 一无所知——本文介绍如何用 Crawl4AI RAG MCP Server 搭建专属知识库，让 Agent 在赛场上如鱼得水。

### 1. 为什么 CTF Agent 需要自建 RAG

CTF 题目往往涉及极为垂直的知识域：某个小众加密算法的弱点、某版本内核的特定偏移、历年大赛的私有 writeup……这些内容不在任何通用大模型的训练集里，或者已经随时间过时。

直接让 Agent 靠"凭感觉"生成答案，幻觉率极高。正确的做法是：**给 Agent 配备一个随时可查的、高质量的专属知识库**，让模型的推理能力与精准的领域知识结合起来。

| 方案 | 知识来源 | 准确度 | 时效性 | 成本 |
| --- | --- | --- | --- | --- |
| 纯 LLM 生成 | 训练数据 | 易幻觉 | 有截止日 | 低 |
| Web 搜索 | 互联网实时 | 中等 | 实时 | 中 |
| **自建 RAG** | **精选知识库** | **高** | **可控更新** | **中** |

自建 RAG 的核心价值在于：你能精确控制 Agent"读过什么"，让它在特定题型上的表现远超通用模型。

---

### 2. Crawl4AI RAG MCP Server 是什么

**GitHub 项目地址：**https://github.com/ckreiling/mcp-server-crawl4ai

Crawl4AI RAG MCP Server 是一个开源项目，将三件事优雅地串联起来：

* **Crawl4AI**：高性能异步爬虫，支持 JS 渲染、结构化提取，专为 LLM 数据准备设计
* **向量数据库（Qdrant）**：将爬取内容分块、嵌入并存储，支持语义检索
* **MCP 协议**：以标准工具的形式暴露给 Claude / Cursor 等支持 MCP 的 Agent，无缝集成

对于 CTF Agent 来说，它就是一个"随叫随到的知识查询员"：Agent 遇到不确定的技术点时，直接调用 MCP 工具检索本地向量库，得到精准的上下文片段后再作答。

---

### 3. 整体架构与数据流

整个系统分为两条流水线：**入库流水线**（离线构建知识库）和**检索流水线**（Agent 在线查询）。

### 入库流水线

```
CTF 资源 URL  →  Crawl4AI 爬取  →  Markdown 清洗  →  分块 + 嵌入  →  Qdrant 向量库
```

### 检索流水线（Agent 运行时）

```
CTF Agent  →  MCP 工具调用  →  语义检索  →  Top-K 片段  →  注入 Prompt  →  模型推理
```

MCP Server 对 Agent 暴露的核心工具有三个：

| 工具名 | 功能 |
| --- | --- |
| `crawl_url` | 爬取指定 URL 并入库 |
| `search` | 对向量库做语义检索，返回 Top-K 片段 |
| `list_sources` | 查看已索引的来源列表 |

Agent 根据当前题目场景自主决定调用哪个工具，无需人工干预。

---

### 4. 快速上手：部署与配置

#### 4.1 环境准备

```
# 克隆项目
git clone https://github.com/ckreiling/mcp-server-crawl4ai
cd mcp-server-crawl4ai

# 安装依赖（建议使用 uv）
pip install uv
uv sync

# 启动 Qdrant（Docker 方式）
docker run -p 6333:6333 qdrant/qdrant
```

#### 4.2 Claude Desktop 配置

在 `claude_desktop_config.json` 中添加如下配置，即可将 MCP Server 注册为 Agent 可用工具：

```
{
  "mcpServers": {
    "crawl4ai-rag": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-server-crawl4ai",
        "run",
        "mcp-server-crawl4ai"
      ],
      "env": {
        "QDRANT_URL": "http://localhost:6333",
        "OPENAI_API_KEY": "sk-..."
      }
    }
  }
}
```

需要注册supabase作为存储CTF各类型题目的向量数据库 supabase.com

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVk47iaXCcdvXlTkg9eE481ef9fiaw6dZ00Shkyy3pfFcEPW6Yocq5l3k2RRNQHG6wbaEbIALkT56XLnDvCeycK51gUNVkZAmH6Dk/640?wx_fmt=png&from=appmsg)

密钥获取：/dashboard/project/ybswvjexdooawcokoist/settings/api-keys/legacy

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlyDKf6N85AJZZ3KUtiaGDP1GRprcuAhkYx6aiclj7qicVYgxURg3yrbzDd2dUF200agWxNxw7FsqKyq12Tk5AGHC45Sg2fY4r2rE/640?wx_fmt=png&from=appmsg)

创建向量数据库-表-字段

```
-- Enable the pgvector extension
create extension ifnotexists vector;

-- Drop tables if they exist (to allow rerunning the script)
droptableifexists crawled_pages;
droptableifexists code_examples;
droptableifexists sources;

-- Create the sources table
createtable sources (
    source_id text primary key,
    summary text,
    total_word_count integerdefault0,
    created_at timestampwithtime zone default timezone('utc'::text, now()) notnull,
    updated_at timestampwithtime zone default timezone('utc'::text, now()) notnull
);

-- Create the documentation chunks table
createtable crawled_pages (
    id bigserial primary key,
    urlvarcharnotnull,
    chunk_number integernotnull,
    contenttextnotnull,
    metadata jsonb notnulldefault'{}'::jsonb,
    source_id textnotnull,
    embedding vector(4096),  -- Qwen3-Embedding-8B embeddings are 4096 dimensions
    created_at timestampwithtime zone default timezone('utc'::text, now()) notnull,

    -- Add a unique constraint to prevent duplicate chunks for the same URL
    unique(url, chunk_number),

    -- Add foreign key constraint to sources table
    foreignkey (source_id) references sources(source_id)
);

-- Create an index for better vector similarity search performance
createindexon crawled_pages using hnsw (embedding vector_cosine_ops);

-- Create an index on metadata for faster filtering
createindex idx_crawled_pages_metadata on crawled_pages using gin (metadata);

-- Create an index on source_id for faster filtering
CREATEINDEX idx_crawled_pages_source_id ON crawled_pages (source_id);

-- Create a function to search for documentation chunks
createorreplacefunction match_crawled_pages (
  query_embedding vector(4096),
  match_count intdefault10,
  filter jsonb DEFAULT'{}'::jsonb,
  source_filter textDEFAULTNULL
) returnstable (
idbigint,
urlvarchar,
  chunk_number integer,
contenttext,
  metadata jsonb,
  source_id text,
  similarity float
)
language plpgsql
as $$
#variable_conflict use_column
begin
returnquery
select
    id,
    url,
    chunk_number,
    content,
    metadata,
    source_id,
    1 - (crawled_pages.embedding <=> query_embedding) as similarity
from crawled_pages
where metadata @> filter
    AND (source_filter ISNULLOR source_id = source_filter)
orderby crawled_pages.embedding <=> query_embedding
limit match_count;
end;
$$;

-- Enable RLS on the crawled_pages table
altertable crawled_pages enablerowlevelsecurity;

-- Create a policy that allows anyone to read crawled_pages
createpolicy"Allow public read access to crawled_pages"
on crawled_pages
forselect
topublic
using (true);

-- Enable RLS on the sources table
altertable sources enablerowlevelsecurity;

-- Create a policy that allows anyone to read sources
createpolicy"Allow public read access to sources"
on sources
forselect
topublic
using (true);

-- Create the code_examples table
createtable code_examples (
    id bigserial primary key,
    urlvarcharnotnull,
    chunk_number integernotnull,
    contenttextnotnull,  -- The code example content
    summary textnotnull,  -- Summary of the code example
    metadata jsonb notnulldefault'{}'::jsonb,
    source_id textnotnull,
    embedding vector(4096),  -- Qwen3-Embedding-8B embeddings are 4096 dimensions
    created_at timestampwithtime zone default timezone('utc'::text, now()) notnull,

    -- Add a unique constraint to prevent duplicate chunks for the same URL
    unique(url, chunk_number),

    -- Add foreign key constraint to sources table
    foreignkey (source_id) references sources(source_id)
);

-- Create an index for better vector similarity search performance
createindexon code_examples using hnsw (embedding vector_cosine_ops);

-- Create an index on metadata for faster filtering
createindex idx_code_examples_metadata on code_examples using gin (metadata);

-- Create an index on source_id for faster filtering
CREATEINDEX idx_code_examples_source_id ON code_examples (source_id);

-- Create a function to search for code examples
createorreplacefunction match_code_examples (
  query_embedding vector(4096),
  match_count intdefault10,
  filter jsonb DEFAULT'{}'::jsonb,
  source_filter textDEFAULTNULL
) returnstable (
idbigint,
urlvarchar,
  chunk_number integer,
contenttext,
  summary text,
  metadata jsonb,
  source_id text,
  similarity float
)
language plpgsql
as $$
#variable_conflict use_column
begin
returnquery
select
    id,
    url,
    chunk_number,
    content,
    summary,
    metadata,
    source_id,
    1 - (code_examples.embedding <=> query_embedding) as similarity
from code_examples
where metadata @> filter
    AND (source_filter ISNULLOR source_id = source_filter)
orderby code_examples.embedding <=> query_embedding
limit match_count;
end;
$$;

-- Enable RLS on the code_examples table
altertable code_examples enablerowlevelsecurity;

-- Create a policy that allows anyone to read code_examples
createpolicy"Allow public read access to code_examples"
on code_examples
forselect
topublic
using (true);
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVncvzTESRxHLH2Bfibgibht99vxY0xj8EiauibicficncFKryfCgXLwtlH7M0kWEUUZ5Mu9icrt689frRD4OW7x2YnH2X...