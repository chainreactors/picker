---
title: 如何用 4 个 Prompt 构建一个零幻觉的 AI 安全知识库？
url: https://mp.weixin.qq.com/s/-YhwnY1R4gZxE8KBpVjpxg
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:21:37.533179
---

# 如何用 4 个 Prompt 构建一个零幻觉的 AI 安全知识库？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PIWj1VguNovia1oibbMH6sx7TFXOQ46DsZymDhbAn5beQwGutJxW23aVEoG3rhxLTEp1oHcpfse0AuSnBxegLBHDgpQKk2uVLOhtgeMoGqcEM/0?wx_fmt=jpeg)

# 如何用 4 个 Prompt 构建一个零幻觉的 AI 安全知识库？

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## ——拆解 MITRE ATLAS Knowledge Base Agent 的多 Agent 架构设计

> **核心痛点：** 当 LLM 被用于企业级知识库时，最致命的问题不是“不会答”，而是“瞎编”。 **解决方案：** MITRE ATLAS 团队公开了一个精妙的解决方案：用 **4 个 Prompt + 1 套路由协议** 构建零幻觉的知识问答系统。

---

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNoujzul9VOSsQApJRSkszNqicrB5LL28QceuAWWCKwxAH8XJNSs4IH5ibGmtHamwFmoWROyqdUDJGCLEJYPwiceuxe3icKGK7hzJH7g/640?wx_fmt=png&from=appmsg)

## 01 问题：为什么 LLM 做知识库总爱“幻觉”？

企业里做 AI 知识库问答，最常见的痛点包括：

* **编造数据：** 模型会编造不存在的数据条目。
* **模糊误导：** 对模糊查询给出不确定性未标注的答案。
* **混淆概念：** 把语义相似的结果当成精确事实。
* **无法深度推理：** 无法处理复杂的关系遍历（例如：“这个技术的父节点是什么？”）。

传统方案通常采用 **RAG（检索增强生成）**，但简单的“检索 → 拼接 → 生成”流程无法解决**置信度管理**和**精确性验证**的问题。

MITRE ATLAS 团队的做法是：**不把 LLM 当数据库用，而是让它当“协调员”。**

---

## 02 架构：4 层分层 Agent 系统

整个系统只有 **5 个 Prompt 文件**，没有一行 Python 业务代码——所有逻辑均封装在 Langflow 的 flow JSON 中。

### 2.1 架构拓扑图

```
               用户查询                  │                  ▼┌─────────────────────────────────────────┐│         Orchestrator (编排层)           ││   路由决策 + 结果综合 + 用户交互        │└─────┬──────────┬──────────┬─────────────┘      │          │          │      ▼          ▼          ▼ ┌─────────┐ ┌──────────┐ ┌────────────┐ │Vector   │ │Dataset   │ │Kumu Graph  │ │Store    │ │Agent     │ │Agent       │ │(语义)   │ │(精确)    │ │(可视化)    │ └─────────┘ └──────────┘ └────────────┘
```

### 2.2 组件职责与技术栈

| Agent 职责 | 技术实现 | 备注 |
| --- | --- | --- |
| **Orchestrator** | 471 行系统 Prompt | 负责路由决策、结果综合 |
| **Vector Store Agent** | ChromaDB + Embedding | 负责模糊 / 语义搜索 |
| **Dataset Agent** | Python + Pandas | 负责 ID 查找、关系遍历、聚合 |
| **Kumu Graph Agent** | Kumu Embed API | 负责生成网络图 URL / iframe |
| **Embedding Generator** | LLM 批量生成 | 数据预处理（数据入库前） |

> **数据规模：** 837 个实体（12 战术 + 436 技术 + 339 缓解措施 + 50 案例研究）

---

## 03 核心设计：双层验证防幻觉

这是整个架构最精妙的部分。

### 3.1 语义 → 精确的双层过滤

```
模糊查询：“攻击者操纵训练数据会怎样？”    │    ├── 第一步：Vector Store Agent ──> 返回候选（标注置信度）    │         "最匹配 AML.T0012 — 数据投毒"    │    └── 第二步：Dataset Agent ──> 验证候选              "确认 AML.T0012 存在于数据集中"              "其缓解措施为 AML.M0003, AML.M0005"    │    └── 第三步：Orchestrator ──> 综合回答              "ATLAS 将此类行为归类为 AML.T0012..."
```

#### 关键约束写入 Orchestrator Prompt：

> * “Vector Store Agent 的结果是候选匹配，不是最终事实。必须在呈现前用 Dataset Agent 验证。”
> * “不要说 'ATLAS 最终分类为...'，除非已被 Dataset Agent 验证。”

### 3.2 置信度分级体系

Vector Store Agent 不是简单返回 “匹配 / 不匹配”，而是返回三级置信度 JSON：

```
{  "status": "partial_match",  "records": [...],  "notes": [    "AML.T0012: high confidence — 检索文本直接匹配攻击场景",    "AML.T0034: low confidence — 仅主题相关，需验证"  ]}
```

Orchestrator 收到后，对低置信度的结果会标注 **“语义候选”** 而非 **“事实”**：

> *“最接近的语义候选是 AML.T0034，但数据集中没有精确匹配。”*

### 3.3 严格的路由协议

每个 Agent 都有清晰的职责边界和拒绝策略：

* **Vector Store Agent 必须拒绝的情况：**
* 精确 ID 查询 → 返回 `needs_dataset_lookup`
* 计数 / 聚合 / 列表 → 返回 `needs_dataset_analysis`
* 关系遍历 / 图查询 → 返回 `needs_graph_analysis`
* **Dataset Agent 必须拒绝的情况：**
* 模糊语义查询 →返回 `needs_semantic_retrieval`

> **设计哲学：** 这种互相推诿的设计，反而保证了每个环节的专业性和准确性。

---

## 04 Dataset Agent：用 Pandas 做精确查询

Dataset Agent 没有专用数据库工具，它的唯一武器是 **Python 解释器 + Pandas**。所有精确操作都通过 Python 代码完成：

```
# 1. 精确 ID 查找df[df['id'] == 'AML.T0012']
# 2. 关系遍历：获取某技术的所有缓解措施row = df[df['id'] == 'AML.T0012'].iloc[0]parse_relationship(row['PARENT_MITIGATIONS'])
# 3. 聚合：统计每个战术下的技术数量df[df['entity'] == 'tactic'].apply(    lambda r: len(parse_relationship(r['CHILD_TECHNIQUES'])))
```

### 为什么用 Pandas 而不是 SQL？

1. 数据本身就是 CSV 格式。
2. Pandas 的 `eval()` 让 LLM 可以动态执行查询。
3. 不需要额外部署数据库服务。
4. 关系字段的多种格式（列表 / 序列化字符串 / 逗号分隔）在 Pandas 中更容易处理。

#### 统一的字段解析函数

Prompt 中甚至定义了一个统一的字段解析函数，用于处理空值、NaN 及不同序列化格式：

```
def parse_relationship(value):    if value is None or pd.isna(value):        return []    if isinstance(value, list):        return [str(v).strip() for v in value if str(v).strip()]    # ... 后续支持 JSON 字符串、Python 字面量、逗号分隔等解析
```

---

## 05 Kumu Graph Agent：克制的设计哲学

Graph Agent 的设计体现了 **“少即是多”** 的工程哲学。它不是 “图推理 Agent”，而是**纯 URL 生成器**。

### 5.1 聚焦策略

```
用户：“可视化 AML.TA0011”    │    ├── Orchestrator 先验证 ID（通过 Dataset Agent）    │    └── Graph Agent 只传入 ["AML.TA0011"]              │              └── Kumu 自动显示该节点及其邻接关系
```

#### Prompt 中的严厉警告：

* “不要添加父节点、子节点、缓解措施或案例研究。Kumu 会自动显示邻接关系。”
* “添加额外 ID 会导致 Kumu 展开过多邻域，产生过宽的可视化。”

### 5.2 禁止推理

Graph Agent 的 Prompt 中明确列出了不可做的事：

* ❌ 不要推断关系
* ❌ 不要发现新实体
* ❌ 不要总结图内容
* ❌ 不要声称图是全面的
* ✅ **只做一件事：** 把 ID 传给 Kumu API

这种极端专业化的设计，确保了可视化环节的可靠性和可预测性。

---

## 06 数据预处理：Embedding Generator

在数据入库前，系统用 LLM 批量生成以下三项内容，以实现混合检索的雏形：

| 字段 | 说明示例 | 作用 |
| --- | --- | --- |
| `embedding_text` | 25-75 词语义描述  *“Prompt Injection is a technique that manipulates...”* | 用于**向量搜索** |
| `semantic_hashtags` | 分层标签（3-8 个）"`#concept/prompt_injection`, `#risk/safeguard_bypass"` | 用于**过滤查询** |
| `keyword_terms` | 精确关键词（3-10 个）  *“prompt injection”, “instruction manipulation”* | 用于**精确匹配** |

### 命名空间体系标签示例：

```
#concept/prompt_injection#domain/large_language_models#risk/safeguard_bypass#behavior/instruction_manipulation#attack/data_poisoning#defense/input_validation
```

---

## 07 可借鉴的设计思想

### 7.1 面向安全团队的启示

| 设计模式 | 安全应用场景 |
| --- | --- |
| **双层验证** | 安全情报分析中的 “线索 → 验证 → 结论” 流程 |
| **置信度分级** | 漏洞扫描结果的优先级排序 |
| **路由协议** | SOC（安全运营中心）中的告警分级与自动分派 |
| **职责分离** | 各安全工具的专用化（扫描 / 分析 / 可视化） |
| **防幻觉约束** | 合规报告生成中的事实核查 |

### 7.2 Prompt 工程要点

该项目的 Prompt 有四个非常值得学习的共性：

1. **负向约束多于正向指令：** 包含大量 “不要做什么” 的明确禁令。
2. **输出格式完全结构化：** 每个 Agent 的 JSON Schema 在 Prompt 中均有完整定义。
3. **边界清晰：** 明确定义了每个 Agent 的拒绝策略和路由返回值。
4. **置信度可表达：** 不只有 “是 / 否”，而是采用了连续的概率与等级表达。

### 7.3 架构取舍

| 选择方案 | 舍弃方案 | 取舍原因 |
| --- | --- | --- |
| **Langflow** | 自研框架 | 快速部署，MCP Server 开箱即用。 |
| **ChromaDB** | Milvus / Weaviate | 数据量小（837 条），ChromaDB 足够轻量高效。 |
| **Pandas** | 专用数据库 | 数据本身就是 CSV，无需额外维护数据库基础设施。 |
| **Kumu** | 自建图可视化 | 免去前端开发，直接生成可嵌入的 URL。 |

---

## 08 局限性与改进方向

虽然设计精巧，该系统仍有可提升的空间：

### 当前局限

* **检索单一：** 向量检索只有向量，缺乏 BM25 混合检索。
* **缺乏评估：** 没有 eval 测试集，无法量化衡量回答质量。
* **黑盒逻辑：** 实际逻辑完全封装在 Langflow flow JSON 中，不可独立审计。
* **单点依赖：** 强依赖 Langflow 平台，定制化成本较高。
* **开源受限：** 采用非标准开源许可（MITRE 专有），商业使用受限。

### 改进建议

* **引入 Hybrid Search：** 结合向量 + BM25，提升长尾词的召回率。
* **建立自动化评估管道：** 构建 Golden QA pairs + 自动化打分机制。
* **解耦 Agent 逻辑：** 将 Agent 逻辑提取为独立 Python 模块，减少对 Langflow 的强绑定。
* **优化查询体验：** 支持 Cronicle / 流式（Streaming）输出，提升大规模查询体验。

---

## 09 总结

MITRE ATLAS Knowledge Base Agent 的核心价值不在于 “做了多复杂的系统”，而在于它证明了： **一个零幻觉的知识问答系统，不需要复杂的代码，只需要正确的架构和严格的 Prompt 约束。**

> **最小可行架构：** 4 个 Agent + 5 个 Prompt + 1 套路由协议 = 生产级零幻觉知识库。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

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