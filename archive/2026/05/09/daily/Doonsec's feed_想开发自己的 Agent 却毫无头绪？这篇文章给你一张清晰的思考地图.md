---
title: 想开发自己的 Agent 却毫无头绪？这篇文章给你一张清晰的思考地图
url: https://mp.weixin.qq.com/s/bpXvukUGRwsz_9j7dz6uIQ
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:35:10.686151
---

# 想开发自己的 Agent 却毫无头绪？这篇文章给你一张清晰的思考地图

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4Z5DCuycmvssLaicQfrEX1RSGhEQTVdbvMLNp1icd6Dxdnkamolk8zHkNvxPq8gV2mM5zibl6CrPyRsI3qqF4tJvtuXMCRjK0WBVKgov3HHnu8/0?wx_fmt=jpeg)

# 想开发自己的 Agent 却毫无头绪？这篇文章给你一张清晰的思考地图

逆向OneByOne

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

Agent开发的系统性工程指南，难点在于设计而非编码。作者通过“打车助手”的案例，拆解了从需求到上线的全流程思维框架。开发路径：遵循“先设计后编码”的四步法：定义能力边界 → 设计工具接口 → 编写系统Prompt → 跑通最小可用版本

以下文章来源于混迹在程序员圈子的摇滚乐迷
，作者不太优秀的文笔

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6nKA5vfRAB0DQkhGibkWyneGbp04pl2WCSkI2KUfSyickA/0)

**混迹在程序员圈子的摇滚乐迷**
.

即是程序员，也是曾经的摇滚乐迷......

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4Z5DCuycmvtMFc0RLdn0wia4iafJ6kywb56p1hoia27EF7udBpic8hpeOTiceJicS3CPMWZmrPMTQrNQjRibxf1hfw7V9aCwgCUMJibbYEQBUprIksg/640?wx_fmt=png&from=appmsg)

## 摘要

这篇文章为Agent开发提供了一张清晰的思考地图，强调在编写代码之前进行设计的重要性。它涵盖了从定义Agent能力边界、设计有效的Prompt、管理多轮对话到构建自动化测试的全流程。笔记旨在帮助开发者建立系统性思维框架，提升Agent的稳定性和可靠性。

## 知识图谱

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4Z5DCuycmvs2GiayV42zyrzMia8HbWB312B2UaP8Xt3sNn3uuwvfn4GF7GLRtWt16icywlmIjKB1liaSyhX11ibibXK9Gj5CSiaZzlK5ZLxTBHicVD8/640?wx_fmt=png&from=appmsg)

# Agent开发学习笔记

有时候，我在接到一个Agent需求的时候，我觉得自己的思绪有时候是凌乱的，这篇文，主要是在回忆自己曾经在Agent开发上学习和做过的一些步骤。希望能对一些朋友有帮助。

许多教程教你如何调用 API、如何使用框架，但很少有人告诉你：**在写下第一行代码之前，你应该如何思考**。构建一个稳定、可靠的 Agent，其核心挑战并非来自代码，而是源于设计的缺失和思考的混乱。

这篇笔记，正是我在一线实践中摸爬滚打后，为自己总结的一套系统性思考框架。它将带你暂别代码，回归设计的本源，一步步理清思路：

* 从 **定义能力边界** 开始，而不是直接看 API；
* 学习 **设计有效的 Prompt**，而不只是简单地“下指令”；
* 掌握 **管理多轮对话** 的技巧，让 Agent 不再“健忘”；
* 学会 **构建自动化测试**，用工程化的方法确保 Agent 的可靠性。

希望这份笔记，能帮你搭建起设计 Agent 的思维骨架，在探索的道路上少走一些弯路。

---

## 一、从零开始做一个 Agent

### 第一步：定义能力清单

做 Agent 的第一步不是写代码，而是想清楚 Agent 的边界和能力。把用户所有可能的需求列出来，判断哪些由 Agent 处理，以打车需求举例：

| 能力 | 说明 |
| --- | --- |
| 叫车 | 告诉 Agent "我要去机场"，它帮你下单 |
| 查询订单状态 | "司机到哪了？" |
| 取消订单 | 带条件判断（是否收违约金） |
| 推荐目的地 | 基于历史记录或语境猜你要去哪 |
| 价格估算 | "去南京西路大概多少钱？" |
| 投诉/反馈 | 引导用户完成投诉流程 |

这步的产出是一份**工具列表（Tools）**，每个能力对应一个 tool。

### 第二步：定义每个 Tool 的接口

每个 tool 就是一个函数，Agent 决定什么时候调它、传什么参数。接口定义要尽可能精确。

```
from typing import TypedDict
# 使用 TypedDict 或 Pydantic 模型替代泛泛的 dict
# 这能让返回的数据结构更清晰，便于静态检查和代码维护
class RideOrder(TypedDict):    order_id: str    estimated_wait_time_minutes: int
def book_ride(origin: str, destination: str, ride_type: str = "standard") -> RideOrder:    """叫一辆车，返回订单ID和预计等待时间"""    ...
def get_order_status(order_id: str) -> dict:    """查询订单实时状态，包括司机位置"""    ...
```

### 第三步：写 System Prompt

告诉 Agent：它是谁、它的边界在哪、出错时怎么办、语气风格。

### 第四步：跑最小可用版本

跑通最简单的一条链路：

> 用户说"我要去虹桥机场" → Agent 调 `book_ride` → 返回"已为您叫车，预计3分钟到达"

---

## 二、一个好的 Prompt 需要具备哪些条件

```
角色定义      → 你是谁能力边界      → 你能做什么边界说明      → 模糊时怎么办Few-shot     → 举例让模型学输出格式      → 返回什么结构异常兜底      → 出错了怎么办
```

### 1. 角色定义

告诉模型它是谁、职责范围是什么：

```
你是一个打车助手，负责帮乘客完成叫车、查单、取消订单等操作。你只处理与打车相关的请求。
```

### 2. 能力边界

明确告诉模型什么能做、什么不能做：

```
你可以：叫车、查订单状态、取消订单、估算费用你不可以：回答与打车无关的任何问题
```

**注意：** 边界不是越窄越好。用户说"我要去接我妈妈从医院回家"，Agent 应该能理解这是叫车需求，要给模型一定的**意图理解弹性**。

### 3. 边界说明

模糊场景提前定义处理方式：

```
如果用户没提供目的地 → 追问目的地如果一句话有多个意图 → 逐一确认再执行如果意图不明确 → 先复述你的理解，再执行
```

### 4. Few-shot 示例

Few-shot（少量示例）就是在 prompt 里直接给模型几个**输入→输出的例子**：

```
用户："叫辆车去虹桥"   → 意图：book_ride，目的地：虹桥机场用户："拼一个"         → 意图：book_ride，车型：拼车用户："司机到哪了"     → 意图：query_status用户："算了取消吧"     → 意图：cancel_ride用户："今天天气怎样"   → 与打车无关，礼貌拒绝
```

**本质上就是用例子代替复杂的文字说明。**

### 5. 输出格式

固定返回格式，防止代码解析出错：

```
始终返回 JSON 格式：{"intent": "book_ride", "destination": "虹桥机场", "ride_type": "standard"}
```

### 6. 异常兜底

```
如果完全无法理解用户意图，回复："抱歉我没理解您的意思，请问您需要叫车吗？"
```

---

## 三、意图理解能力如何提升

### 优先顺序

```
Prompt 优化（Few-shot + 意图确认）    ↓ 还不够？收集真实用户对话，分析哪类意图经常出错    ↓ 找到规律？针对性加 Few-shot 或调整 prompt 逻辑    ↓ 还有系统性偏差？再考虑微调
```

**80% 的意图理解问题在 Prompt 阶段就能解决。**

### RAG 和微调分别解决什么问题

* **RAG** 解决的是"知识"问题，不是"理解"问题。适合动态知识（计价规则、优惠活动等）。
* **微调** 解决的是"风格/领域适配"问题。需要几千条高质量标注数据，门槛很高，不是首选。

### RAG 的高级应用：动态 Few-shot

除了用 RAG 查询外部知识库，它还可以用来优化意图理解。当用户的输入很模糊时，可以用 RAG 动态构建 Few-shot 示例，这比在 Prompt 中写死几个例子更灵活。

**流程如下：**

1. **建立“疑难样本”数据库**：将历史上处理过的、有代表性的“模糊输入 → 清晰意图”的案例存入向量数据库。
2. **实时检索**：当 Agent 收到新的用户请求时，先将其作为查询，从数据库中检索出最相似的 1-3 个历史案例。
3. **动态拼接 Prompt**：将检索到的案例动态地插入到 Prompt 的 Few-shot 部分。
4. **LLM 决策**：LLM 参考这些最相关的例子，做出更准确的判断。

这种方法能让 Agent 拥有“举一反三”的能力，对未见过的边界 Case 鲁棒性更强。

---

## 四、Prompt 出问题如何分析

### 定位问题层级

```
用户输入    ↓意图理解有没有出错？    ← 第一层    ↓tool 选择对不对？       ← 第二层    ↓tool 参数传对了吗？     ← 第三层    ↓最终回复合不合理？      ← 第四层
```

### 分析方法

**1. 看中间推理过程**

让模型输出思考链，看到模型"在想什么"：

```
SYSTEM_PROMPT = """...原始prompt...
在回答之前，先用<thinking>标签写出你的推理过程：- 用户意图是什么- 应该调用哪个tool- 参数是什么</thinking>"""
```

**2. 做消融测试**

把 prompt 拆开，逐段注释掉，看哪段影响最大：

```
完整prompt        → 通过率 72%去掉Few-shot      → 通过率 51%   ← 这段影响最大去掉边界说明      → 通过率 68%
```

**3. 对比不同模型**

同一批测试集跑多个模型，如果换个模型就好了，说明问题在 prompt 和模型的适配上。

### 分析流程

```
发现问题    ↓看中间推理过程 → 定位断在哪一层    ↓做消融测试 → 找到影响最大的片段    ↓针对性修改    ↓跑测试集验证    ↓确认提升，记录版本
```

---

## 五、更换后端模型的注意事项

换模型可能带来的问题：

* **指令遵循能力不一样** — 原来调好的 prompt 可能直接失效
* **输出格式不稳定** — JSON 格式可能夹杂多余文字导致解析出错
* **推理能力差异** — 多意图、隐含意图处理能力差距大
* **上下文处理不同** — 多轮对话里"忘事"情况变多

### 应对策略

**做一层抽象，把模型调用解耦：**

```
class LLMClient:    def chat(self, messages): ...
class OpenAIClient(LLMClient): ...class ClaudeClient(LLMClient): ...class QwenClient(LLMClient): ...
```

**灰度切换：** 先用新模型跑 10% 流量，对比效果再逐步放量。

**核心：换模型前先跑测试集，用数字说话。**

---

## 六、多轮对话如何管理

单轮的“意图识别 → 工具调用”是 Agent 的基础，但真正实用的 Agent 必须能处理连续的多轮对话。核心挑战在于**上下文管理**。

### 1. 状态跟踪 (State Tracking)

Agent 需要在对话中持续维护一个“状态”，用来记住关键信息和用户偏好。

例如，用户说“帮我叫辆车去机场”，Agent 下单后，需要将 `order_id` 存入当前对话的状态中。当用户接着问“司机到哪了？”，Agent 就能从状态中取出 `order_id` 去调用查询接口。

这个状态可以是一个简单的字典或一个结构化的对象，随着对话进行被不断更新。

```
# 简化的对话状态示例
dialogue_state = {    "user_id": "u123",    "history": [...],    "active_order": {        "order_id": "d456",        "destination": "虹桥机场"    },    "user_preferences": {        "ride_type": "standard"    }}
```

### 2. 上下文压缩与总结

LLM 的上下文窗口是有限的。随着对话变长，不可能把所有历史记录都传给模型。必须对上下文进行处理。

* **滑动窗口**：只保留最近的 N 轮对话。最简单，但可能丢失早期重要信息。
* **对话总结**：当对话达到一定长度时，用一次额外的 LLM 调用，将之前的对话内容“总结”成一段摘要，然后用这个摘要替代原始对话历史。

+ **Prompt 示例**：`"请将以下对话总结为一段要点，保留关键信息（如订单号、目的地、用户偏好等）：\n\n[对话历史]"`

* **混合策略**：保留最近几轮的完整对话 + 之前所有对话的摘要。

### 3. 长程依赖 (Long-term Dependencies)

有时，用户在对话早期提到的信息在很久之后才用到。对话总结可能会丢失这些细节。更高级的方案是建立一个**记忆库 (Memory Store)**，通常使用向量数据库实现。

* **写入记忆**：在每一轮对话结束后，将关键信息（如“用户今天去了机场”、“用户偏爱安静的司机”）作为文档存入向量数据库。
* **读取记忆**：在处理新请求时，先将用户当前的输入和部分对话历史在记忆库中做一次向量检索，找出最相关的几条“记忆”，然后将这些记忆和 Prompt 一起喂给 LLM。

这让 Agent 拥有了长期记忆，能更好地理解用户的深层意图和个性化需求。

---

## 七、测试集如何构建和存储

### 测试集数据来源

**来源一：人工构造（冷启动）**

覆盖四类 case：

* **正常 case** — "叫辆车去虹桥机场"
* **边界 case** — "拼一个"、"便宜点"
* **异常 case** — 问天气、输入乱码
* **多意图 case** — "取消上一个，再叫一辆去浦东"

**来源二：真实对话挖掘（上线后）**

从真实日志里捞：用户差评的对话、tool 调用失败的对话、用户反复重复同一句话的对话。

**来源三：模型自动生成（数据增强）**

```
给我生成20条用户想叫车去机场的不同表达方式，包括口语化、方言味、隐含意图等变体
```

**来源四：回归测试用例（上线后）**

当线上发现一个 Bug 并通过优化 Prompt 修复后，应将这个出错的 Case 制作成一个**永久的、必须通过的测试用例**，加入“回归测试集”。每次更新 Prompt 后，除了跑通用测试集，还必须 **100% 通过**这个回归测试集，确保旧的问题不会复现。

### 什么是"边界 case"

边界 = 模型**勉强答对**或**侥幸没出错**的情况。判断方法：

* **看输出稳定性** — 同一条输入跑3次，结果不一致就是边界
* **看置信度** — 模型低置信度的输出
* **看 Agent 有没有追问** — Agent 选择追问说明它自己也不确定
* **看输入模糊程度** — 少于5个字、没有明确地点、包含多个动词

### 小企业测试集工程化方案

**Prompt 存储：**

```
prompts/  taxi_agent/    system_prompt_v1.txt    system_prompt_v2.txt    changelog.md   ← 记录每次改了什么、效果如何
```

**数据库结构：**

```
-- prompt 表CREATE TABLE prompts (  id         INT PRIMARY KEY,  name       VARCHAR,  version    VARCHAR,  content    TEXT,  is_active  BOOLEAN,  created_at TIMESTAMP);
-- 测试集表CREATE TABLE test_cases (  id                  INT PRIMARY KEY,  input               TEXT,  expected_intent     VARCHAR,  expected_arguments  TEXT,      -- 存储 JSON 字符串  source              VARCHAR,   -- manual / user_feedback / generated  tags                VARCHAR,   -- edge_case / normal / regression  created_at          TIMESTAMP);
-- 评估结果表CREATE TABLE evaluation_results (  id           INT PRIMARY KEY,  prompt_name  VARCHAR,  version      VARCHAR,  score        FLOAT,  passed       INT,  total        INT,  run_at       TIMESTAMP  -- 建议增加一个字段存储详细的失败 case 列表  -- failed_cases_details TEXT);
```

**评估脚本：**

一个完整的评估不仅要检查**意图（Intent）**，还应该检查\*\*参数（Arguments）\*\*是否被正确提取。

```
import json
def run_evaluation(prompt_name: s...