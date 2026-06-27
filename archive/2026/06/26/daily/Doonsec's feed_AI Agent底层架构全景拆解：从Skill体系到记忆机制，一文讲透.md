---
title: AI Agent底层架构全景拆解：从Skill体系到记忆机制，一文讲透
url: https://mp.weixin.qq.com/s/X2r4TDI_aRukusWxhgoA4A
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:45:25.823818
---

# AI Agent底层架构全景拆解：从Skill体系到记忆机制，一文讲透

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2xgPSpHS9eWcIW3icOshQYxOnCrLm9aW2xWoNyUibMYw9ygEVGOpXSmI9rB36wopFe8icibVJuiaconN9GAGuhfVLODKVxxa7PtEibnOE4ZkbqzDU/0?wx_fmt=jpeg)

# AI Agent底层架构全景拆解：从Skill体系到记忆机制，一文讲透

原创

宵练
宵练

洋芋学AI

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CL0nmYQLR9YV0vZRGqhK80HKmJhs7xn3nibzRJEFicJcHfqgkgT2SXMmUAs957p4baqSLPJpU50XQwBpuCrpIVFpdggeziaHFoTaGPuHEP4kp0/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/4tiawPNlHErZaZibVdCJGpKpZGQcbBkY9Z5WiaIucCsL6AibbaxiauzwGFLAtctddn6mkBzYuciaBu1mwWDErYCzp8UPVb0yhQSHTC5xb7uMWmjBU/640?from=appmsg)

点击上方蓝字关注我们

随着AI Agent逐渐从Demo走向生产环境，一个绕不开的问题浮出水面——一个真正可用的Agent，到底是怎么工作的？

你看到的，是一个聊天框；你没看到的，是意图理解、任务规划、Skill路由、工具调用、记忆管理、上下文压缩等一整套复杂系统在后台跑。

这篇文章，用15个核心问题，把Agent的底层运行机制一次性拆开给你看。

---

## 一、一次任务背后的完整闭环

先看Agent的整体执行链路：

用户输入
↓
意图理解
↓
任务规划（Planner）
↓
Skill匹配（Router）
↓
任务拆解（Task Decomposition）
↓
执行调度（Scheduler）
↓
工具调用（Tool Calling）
↓
结果校验（Reflection）
↓
迭代优化（Retry）
↓
结果输出
↓
记忆沉淀（Memory）

整个过程，本质上是一个不断"感知→推理→执行→反馈"的闭环系统。

当前主流Agent框架——LangGraph、AutoGen、OpenManus等——基本都遵循这一架构。差别只在各环节的实现深度和工程优化策略。

---

## 二、Agent怎么"听懂"你说的话

当你输入"帮我写一份Splunk漏洞分析报告，并生成PPT"，Agent不会上来就写。

它先做意图识别。

模型会从这句话里抽取以下信息：

* 核心目标

  漏洞分析
* 目标对象

  Splunk
* 输出形式

  PPT
* 文档类型

  汇报材料
* 约束条件

  专业、可演示

意图清楚了，接下来进入Task Planning阶段，把模糊需求切成具体任务：

| 序号 | 任务 |
| --- | --- |
| Task1 | 收集漏洞资料 |
| Task2 | 分析漏洞影响 |
| Task3 | 设计PPT结构 |
| Task4 | 生成演示文稿 |

目前主流的任务规划方法包括：

* ReAct

  推理与行动交替进行
* Tree of Thought

  树状思维，探索多条路径
* Plan-and-Execute

  先规划再执行
* HTN（Hierarchical Task Network）

  层次化任务网络

一句话：Agent在把自然语言需求翻译成机器可执行的流程。

---

## 三、任务拆完了，Agent怎么安排执行顺序

Agent内部有一个调度器（Scheduler），本质类似一个任务编排系统。

比如上面的四个任务，并不是并行跑的，而是有严格的先后依赖：

漏洞收集 → 影响分析 → 风险评估 → PPT制作

前面的任务完成了，后续任务才能执行。这种依赖关系通常被构建成**DAG（有向无环图）**。

这里有一个关键区分：

**模型什么时候"思考"？** → 分析问题、生成内容、决策判断、规划任务

**工具什么时候"调用"？** → 数据查询、网络搜索、SQL执行、浏览器操作、邮件发送、文件处理、代码运行

整个过程可以概括为一个经典循环：

> Reason → Act → Observe → 修正 → 再循环

Agent不断"思考→行动→观察→修正"，直到任务完成。

---

## 四、Skill体系：Agent的能力插件生态

### 4.1 Skill怎么匹配

Skill本质上是Agent的能力插件。比如漏洞分析Skill、PPT生成Skill、代码审计Skill、数据分析Skill。

Agent通常采用**两阶段匹配机制**：

第一阶段：Embedding召回

用户问题"分析Splunk漏洞"被转化为向量，与Skill库中的向量比对，筛选出TopK候选：

| Skill | 相似度 |
| --- | --- |
| Skill\_A | 0.95 |
| Skill\_B | 0.88 |
| Skill\_C | 0.72 |

保留前三。

第二阶段：LLM重排序

模型再次判断：哪个Skill最适合当前任务？输出最终结果。

这种"向量粗筛+精排"的方式，兼顾了效率和准确率——跟搜索引擎的召回-排序逻辑如出一辙。

### 4.2 Skill为什么要分层

Skill越来越多，不做管理就是能力孤岛。推荐采用四层体系：

| 层级 | 名称 | 职责 | 示例 |
| --- | --- | --- | --- |
| L0 | 基础能力层 | 原子能力 | 搜索、翻译、数学计算、代码生成 |
| L1 | 工具层 | 封装外部能力 | GitHub、MySQL、Excel、浏览器 |
| L2 | 工作流层 | 面向业务流程 | 漏洞分析、合同审核、报告生成 |
| L3 | 行业Agent层 | 直接服务业务 | 安全Agent、HR Agent、财务Agent |

这跟软件行业的微服务架构是一个思路：**能力复用、降低耦合、方便治理**。

### 4.3 Skill能不能自动沉淀

可以，目前主要有三种模式：

1. 人工开发

   工程师编写、统一发布、版本管理
2. Agent自动学习

   发现某个流程重复执行100次 → 自动封装 → 形成新Skill
3. 人工确认

   Agent提示"是否保存当前流程为Skill？" → 用户确认 → 正式入库

企业实践中，通常采用"自动发现 + 人工审核"的混合模式。

---

## 五、记忆机制：Agent怎么记住你

### 5.1 短期记忆 vs 长期记忆

| 维度 | 短期记忆 | 长期记忆 |
| --- | --- | --- |
| 保存内容 | 当前任务状态 | 长期知识 |
| 具体示例 | 最近20轮对话、临时变量、执行结果 | 用户偏好、历史项目、行业背景、工作习惯 |
| 类比 | CPU缓存 | 企业知识库 |

### 5.2 长期记忆还要继续拆

**静态长期记忆**（变化较慢）：

* 岗位、行业、偏好、公司背景

**动态长期记忆**（变化较快）：

* 会议纪要、近期项目、待办事项
* 通常设置TTL机制：30天、60天自动过期

### 5.3 记忆膨胀怎么办

长期记忆一定会无限膨胀，必须做Memory Management：

| 策略 | 说明 |
| --- | --- |
| 重要性评分 | 高分保留，低分淘汰 |
| 语义去重 | 相似内容合并 |
| 摘要归纳 | 100条会议记录 → 压缩成一份总结 |
| 生命周期管理 | TTL自动过期 |
| 冷热分层存储 | 热数据快速访问，冷数据归档 |

### 5.4 怎么精准召回

三阶段机制，层层过滤：

Embedding召回（Top50）
↓
重排序（Top10）
↓
模型筛选（Top3）→ 注入上下文

同时综合考虑三个维度：**重要性、时间衰减、访问频率**，避免上下文污染。

---

## 六、上下文工程：真正的护城河

### 6.1 动态Prompt vs 静态Prompt

**静态Prompt**通常固定不变：

> "你是一名安全专家。输出Markdown。"

**动态Prompt**则实时拼接，包含：

* 用户问题
* 历史对话
* 长期记忆
* Skill描述
* 工具Schema

最终形成完整上下文。

这里有一个核心判断：**Agent真正竞争的不是Prompt，而是Context Engineering（上下文工程）**。谁能把最相关的信息，在最合适的时机，以最优的结构塞进有限的窗口里，谁就赢了。

### 6.2 上下文窗口有多大

截至2026年，主流模型的大致情况：

| 模型 | 上下文窗口 |
| --- | --- |
| GPT-5.5 | ~400K |
| Claude 4 | 200K |
| Gemini 2.5 Pro | 1M |
| DeepSeek V3.x | 128K |
| Qwen3 | 32K~256K |
| Kimi K2 | 128K~200K |

注意：实际使用过程中，需要预留输出空间。窗口越大 ≠ 效果越好，关键在于你怎么用。

### 6.3 什么时候触发压缩

通常不会等窗口耗尽才动手。经验阈值如下：

| 占比 | 动作 |
| --- | --- |
| 60% | 开始监控 |
| 70% | 准备摘要 |
| 80% | 自动压缩 |
| 90% | 强制裁剪 |

常见压缩方法：

* Conversation Summary

  对话摘要
* Sliding Window

  滑动窗口
* Hierarchical Memory

  分层记忆
* Semantic Compression

  语义压缩

---

## 七、模型选择与成本账

### 7.1 不同场景怎么选模型

| 场景 | 推荐模型 |
| --- | --- |
| 复杂推理 | GPT-5.5、Claude Opus |
| 代码开发 | GPT-5.5、Claude Sonnet |
| 长文档分析 | Gemini Pro |
| 知识问答 | DeepSeek、Qwen |
| 私有化部署 | Qwen、Llama、DeepSeek |

核心原则只有一句话：

> 高推理任务选能力，高频任务选成本，私有场景选可部署性。

### 7.2 Agent写1000行代码到底要花多少钱

先算Token消耗：

* 1行代码 ≈ 15~30 Token
* 1000行代码 ≈ 15000~30000 Token

如果再加入规划、测试、审查、自动修复等环节：

* 整体消耗可能达到 **5万~15万Token**

模型费用通常按百万Token计费：

> 总成本 = 输入Token × 输入单价 + 输出Token × 输出单价

真正昂贵的，不是一次生成，而是Agent长期运行过程中产生的大量上下文、记忆检索、多轮推理以及工具调用。**这些隐性成本，才是工程化落地时必须算清楚的账。**

---

## 写在最后

很多人觉得Agent就是"大模型+工具调用"。

但真正进入工程化阶段，你会发现Agent比拼的早已不是模型能力，而是整个系统工程能力——任务规划、Skill治理、记忆管理、上下文编排、成本优化。

Agent的竞争，正在从模型竞争，演变成四项工程能力的综合较量：

* Context Engineering

  （上下文工程）
* Memory Engineering

  （记忆工程）
* Skill Engineering

  （技能工程）
* Workflow Engineering

  （工作流工程）

谁能更好地解决这些工程问题，谁就更有机会构建下一代真正可落地的数字员工系统。

Agent的故事，才刚刚开始。

Agent开发面试题分享

1.整个Agent完整的链路是怎么运转的？从用户输入到最终完成任务，中间经历了哪些步骤?

2.用户输入一个需求以后，Agent如何理解用户意图，并进行任务拆解?

3.任务拆解以后，Agent如何决定先做什么、后做什么?什么时候调用模型，什么时候调用工具?

4.用户输入进来以后，系统如何匹配相关Skill?

5.Skill分层体系是怎么设计的?为什么要过样分层?不同层级Skill的职责边界是什么?

6.有没有Skill沉淀机制?Skill是系统自动沉淀，还是只能用户手动构造?

7.长短期记忆是怎么设计的?短期记忆和长期记忆分别保存什么?

8.为什么要把长期记忆分成静态长期记忆和动态长期记忆?

9.每一轮对话都触发长期记忆存储，会不会导致记忆快速膨胀，存在以后怎么处理？

10.大模型如何判断哪些长期记忆需要召回?如何避兔召回太多导致上下文污染?

11.动态Prompt和静态Prompt有什么区别?上下文是如何动态组装的?

12.不同大模型上下文窗口总Token是多少？

13.上下文触发压缩的上限域值如何规定？

14. 在不同业务场景下，模型应该如何选型？

15.如果让agent写1000行代码，大概会消耗多少Token？成本是多少？百万Token的计费规则是什么？

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/o0buL62hK7M8RnVz7mqRVDRkqm2sJeT2icM4WyR7kMkHpLVaicR3tJ4gr5kIb4zje9lXgd5PuOw42Z5KtathltcQ/640?from=appmsg)

**END**

推荐阅读

[读Notion创始人的《蒸汽、钢铁与无限心智》一文有感](https://mp.weixin.qq.com/s?__biz=MzkzMjcwMTc2OA==&mid=2247484038&idx=1&sn=a197258e0a7a4471f37a47a286980966&scene=21#wechat_redirect)

2026-06-21

[![](https://mmbiz.qpic.cn/mmbiz_jpg/2xgPSpHS9eVdbFdWe9nhRibItfNhWzlUH6s1iciaaiaOaUs51RKyIapLUn9ic6auGYy32X6wPHCmhUIryKYWqDwNep2swfx4Bk01NrGiaYmXHnD3g/640?wx_fmt=jpeg)![]()![]()](https://mp.weixin.qq.com/s?__biz=MzkzMjcwMTc2OA==&mid=2247484038&idx=1&sn=a197258e0a7a4471f37a47a286980966&scene=21#wechat_redirect)

[从 Prompt Engineering 到 Loop Engineering：AI 应用正在从“会提问”走向“会协作”](https://mp.weixin.qq.com/s?__biz=MzkzMjcwMTc2OA==&mid=2247484030&idx=1&sn=59d23a1efe5b04a2a682e66b7e9a4ace&scene=21#wechat_redirect)

2026-06-20

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2xgPSpHS9eXF8TSv8pp7NG5ILzaRkfAbbejps3rwhPVMaWMvJqGb0QT1jeKabmJaibcIww0ePneibAVDpoEDHcl9vw0VA1hUgQOsibpAhZTVys/640?wx_fmt=jpeg)![]()![]()](https://mp.weixin.qq.com/s?__biz=MzkzMjcwMTc2OA==&mid=2247484030&idx=1&sn=59d23a1efe5b04a2a682e66b7e9a4ace&scene=21#wechat_redirect)

[Anthropic CEO 最新警告：再不行动，AI 将重塑一切——从你的工作到国家主权](https://mp.weixin.qq.com/s?__biz=MzkzMjcwMTc2OA==&mid=2247484006&idx=1&sn=50347ef58427e717da2199278b9ae5c7&scene=21#wechat_redirect)

2026-06-13

[![](https://mmbiz.qpic.cn/mmbiz_jpg/2xgPSpHS9eW5gavo5KUgQInX0QBL9OYWlsdfibbyZJCfry8ickHQ0XucGI86ECmK9Sr29mUKLy3xibrOuM1GD8L9paJSwibHl4IbBsd2fAXtuuw/640?wx_fmt=jpeg)![]()![]()](https://mp.weixin.qq.com/s?__biz=MzkzMjcwMTc2OA==&mid=2247484006&idx=1&sn=50347ef58427e717da2199278b9ae5c7&scene=21#wechat_redirect)

[微信AI终于要来了！腾讯憋了3年的大招，将如何改变14亿人的生活？](https://mp.weixin.qq.com/s?__biz=MzkzMjcwMTc2OA==&mid=2247484001&idx=1&sn=8f805e731406e8484de95c63fc1a4d8b&scene=21#wechat_redirect)

2026-06-08

[![](https://mmbiz.qpic.cn/mmbiz_jpg/2xgPSpHS9eV0Su8Yg7iarV1ctCaoLCE02q9DibSUaja5XNsA0O3HvRZBViaFbJMZcF4RFVRXY0tcogicqQiboicvO6ctn745M9f1icCk4Oaj7OXEHQ/640?wx_fmt=jpeg)![]()![]()](https://mp.weixin.qq.com/s?__biz=MzkzMjcwMTc2OA==&mid=2247484001&idx=1&sn=8f805e731406e8484de95c63fc1a4d8b&scene=21#wechat_redirect)

[AI技术全景图：从CNN到MOE，一文读懂六大核心技术](https://mp.weixin.qq.com/s?__biz=MzkzMjcwMTc2OA==&mid=...