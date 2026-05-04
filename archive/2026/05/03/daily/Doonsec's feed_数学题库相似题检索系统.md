---
title: 数学题库相似题检索系统
url: https://mp.weixin.qq.com/s/gBF_B3tmmooEtLPjJ3i9GQ
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:29:02.457829
---

# 数学题库相似题检索系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xyspsQs8n7wTeT1nsibia71t1cviboAibj1S4Cs18y4CrJZ9wDJ4WR6g19GTwgopibczicxTQgnpWOiabJAIub4KdSJhbAO5qJTNkwo3vcMUfVChPU/0?wx_fmt=jpeg)

# 数学题库相似题检索系统

原创

Uysieot
Uysieot

简单读写

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

面向大规模数学题库的公式增强型相似题检索系统设计与实现

基于 LaTeX 规范化、语义向量召回与规则重排的混合检索方案

数学题识别项目 · 技术论文稿

版本：1.0    日期：2026 年 5 月

摘要

本文围绕一个包含十万级数学题目的相似题检索系统展开，提出一种面向数学题库的混合检索框架。该框架以原始题面保真为前提，通过 LaTeX 公式抽取、公式规范化、变量与数值骨架化、伪公式过滤、语义向量召回、关键词召回、公式结构召回以及规则化重排，实现对“原题”“改写题”“同结构题”和“弱相关题”的分层识别。与单纯依赖 embedding 的方案相比，本文方案强调数学题目的结构性：公式、条件、目标、题型信号和领域信号均参与检索过程。在实践中，系统从早期的公式抽取脚本逐步演化到支持 GPU 向量化、批量 JSONL 入库、中文化输出、HTML 报告生成的完整命令行工具。本文详细描述了数据模型、公式处理、弱公式降权、多路召回、融合评分、错误案例分析和后续优化方向。

关键词：数学题库；相似题检索；LaTeX 公式；向量检索；规则重排；多路召回；图论信号；函数方程信号

# 目录

1 引言

2 问题定义与系统目标

3 数据表示与规范化模型

4 LaTeX 公式处理与弱公式过滤

5 多路召回框架：哈希、公式、语义与关键词

6 融合评分与重排策略

7 领域信号设计：函数同余、余数优化与图论路径

8 系统工程实现与命令行工作流

9 实验观察与典型案例分析

10 局限性与后续优化路线

11 结论

附录 A 数据字段建议

附录 B 常用命令

# 1 引言

数学题库检索不同于普通文本检索。普通问答或文档搜索通常以自然语言语义为核心，而数学题目同时包含自然语言、符号公式、变量关系、题型约束和隐含结构。两个题目可能文字完全不同，却因为公式骨架一致而属于同结构题；也可能文字模板高度相似，却因为公式、条件或目标不同而并不相似。

本项目的实际需求是：在一个由 JSONL 文件组成的大规模题库中，输入一道新题，快速找出原题、改写题、换变量或换数字的同结构题，以及语义上相关的题目。题库中的题目大多只有题面，没有标准解答。因此，系统不能依赖解题过程或答案匹配，而必须从题面本身构造可比较的多层表示。

本文提出的方案不是单一的“向量入库”系统，而是一个混合检索系统。它将题目拆成原文、规范化文本、公式列表、公式骨架、关键词集合、领域信号和向量表示，并在搜索时融合多路候选。实践表明，这种设计能够同时兼顾公式型题目和文字型图论、组合题，减少纯语义模型带来的假阳性。

表 1  相似题检索目标分层

|  |  |  |
| --- | --- | --- |
| 检索目标 | 典型表现 | 主要识别依据 |
| 原题 | 题面完全相同或仅格式不同 | raw\_hash、normalized\_hash、文本近似度 |
| 改写题 | 措辞变化但题意一致 | 语义向量、关键词重合、强领域信号 |
| 同结构题 | 变量或数字变化，公式结构一致 | formula\_skeleton、条件/目标骨架 |
| 弱相关题 | 同题型或同主题，但结构不同 | 语义向量、少量领域信号 |

# 2 问题定义与系统目标

## 2.1 输入与输出

系统输入包括两类：一类是题库中的结构化 JSONL 记录，通常包含 id 与 statement\_display 字段；另一类是用户在命令行或接口中输入的新题文本。输出是按综合相似度排序的 Top K 结果，每个结果包含题目 UID、原始 ID、来源文件、匹配类型、综合得分、向量分、规则分、数学信号、融合说明以及可选的 HTML 报告。

在本项目中，题目记录来自多个分片 JSONL 文件。为避免不同文件中 id 冲突，系统在处理阶段生成全局唯一的 uid，格式为“文件名::原始 id”。例如 ap\_problem\_statement.part0010.jsonl::4502。

## 2.2 约束条件

系统设计受以下约束影响。第一，题目大多没有解析，因此不能依赖解法步骤、方法标签或答案文本。第二，题面中公式已经以 LaTeX 形式存在，公式 OCR 不是主要难点，重点转向公式规范化与骨架化。第三，题库中既有公式密集型题，也有文字密集型题。第四，英文题较多，因此系统需要在英文原文上完成相似检索，同时将命令行与报告界面尽量中文化。

## 2.3 设计目标

系统的第一目标是可用性：能在本地目录中批量处理题目、建立索引，并通过命令行检索。第二目标是鲁棒性：对于公式、文字、图论、函数方程等不同类型题目均能给出合理排序。第三目标是可解释性：每条结果不只给出一个黑箱分数，还应展示向量分、规则分、公式分、文本分和领域信号，便于人工判断。

# 3 数据表示与规范化模型

## 3.1 三层数据思想

系统采用三层数据思想：原始层、规范层和索引层。原始层完整保留 raw\_text 与 statement\_display，任何清洗、替换和公式处理都不能覆盖原始数据。规范层包括 normalized\_text、search\_text、formulas、math\_signals 等字段。索引层则包括 text\_index、formula\_exact\_index、formula\_variable\_index、formula\_skeleton\_index、condition\_formula\_index 和 target\_formula\_index。

图 1  系统处理流程概览

|  |
| --- |
| 原始 JSONL    -> 文本清洗    -> LaTeX 公式抽取    -> 公式规范化与骨架化    -> 伪公式过滤    -> 生成索引字段    -> embedding 向量化    -> 多路召回与重排 |

## 3.2 核心字段

表 2  处理后题目记录的核心字段

|  |  |  |
| --- | --- | --- |
| 字段 | 含义 | 用途 |
| raw\_text | 原始题面，不做破坏性修改 | 追溯、精确匹配、人工核验 |
| normalized\_text | 清洗后的展示文本 | 近似原题判断、展示 |
| search\_text | 公式用占位符替换后的文本 | 语义向量、关键词召回 |
| formulas | 题目中的 LaTeX 公式对象列表 | 公式匹配、结构比较 |
| index\_fields | 多种索引文本 | 向量、关键词和公式召回 |
| hash | 多粒度哈希 | 原题、规范题、公式集合快速判断 |
| math\_signals | 题型与领域信号 | 重排降权、强信号加权 |

## 3.3 UID 与来源管理

大规模题库通常以多个分片存储，且不同文件中可能复用同一个整数 id。为避免索引冲突，系统将 source\_file 与 source\_id 组合为 uid。检索结果中同时保留 uid、source\_id 和 source\_file，使前端页面可以直接定位到原始题库记录。

# 4 LaTeX 公式处理与弱公式过滤

## 4.1 公式抽取

题目中的公式主要由美元符号、括号式 LaTeX 环境和行间公式环境包围。系统在处理阶段记录每个公式的原始片段、规范 LaTeX、位置、变量、数字、结构特征、角色和哈希。角色包括 condition、target 和 unknown。由于很多题目没有明确的“求证/求”分割，角色判断主要依赖公式在题面中的位置和前后关键词。

## 4.2 公式规范化

公式规范化不是完整的数学等价证明，而是工程上的写法统一。系统将常见差异统一为可比较形式，例如 \geq 与 \ge、\leq 与 \le、x^{2} 与 x^2、隐式乘法 ab 与 a\*b、\dfrac 与 \frac 等。规范化后的公式用于 exact 匹配；变量骨架用于换变量匹配；数字骨架用于换数字同结构匹配。

表 3  公式多版本表示

|  |  |  |
| --- | --- | --- |
| 版本 | 示例 | 用途 |
| canonical | a+b=3 | 判断公式是否基本相同 |
| variable\_skeleton | VAR1+VAR2=3 | 判断是否仅变量名不同 |
| number\_skeleton | VAR1+VAR2=NUM | 判断是否数字变化但结构相同 |

## 4.3 弱公式问题

实践中发现，题目中并非所有 LaTeX 都是有效数学结构。例如 $A$、$B$、$(i)$、$(ii)$、$\emph{path}$、$\text{...}$、以及 n>=3 这类简单范围条件，虽然是 LaTeX 片段，但不能作为强公式相似依据。若不加过滤，大量题目会因为共享 VAR>=NUM 之类骨架而被错误判定为 same\_formula\_skeleton。

因此，从 v7 开始系统引入弱公式过滤。弱公式仍可保留在原始题面中，但不触发强公式哈希、不参与公式支持加分，也不会作为 hash\_bump 的依据。该策略显著改善了文字型图论题和组合题的排序稳定性。

图 2  弱公式与强公式示例

|  |
| --- |
| 弱公式示例：    $A$, $B$, $F$    $(i)$, $(ii)$, $(iii)$    $\emph{path}$, $\emph{long path}$    $n \geq 3$, $k \geq 0$     强公式示例：    f(ab)=f(a)f(b)    f(m+n)\equiv f(m)\pmod n    \sum\_{j=1}^{m} ((a\_j+k)\pmod n)    a\_{n+1}=2a\_n+1 |

# 5 多路召回框架：哈希、公式、语义与关键词

## 5.1 为什么不能只靠向量

向量模型擅长处理“Find all...”与“Determine all...”之类的自然语言改写，但对数学题而言，语义相似不等于结构相似。许多函数题都包含 function f、positive integer、prove that 等模板词，embedding 容易给出较高相似度；但如果缺少核心公式条件，实际并不相似。因此，向量召回只应作为候选来源之一，而不应单独决定排序。

## 5.2 召回通道

表 4  多路召回通道

|  |  |  |
| --- | --- | --- |
| 召回通道 | 候选来源 | 适合场景 |
| 哈希召回 | raw\_hash、normalized\_hash、公式哈希 | 原题、格式变化题 |
| 向量召回 | semantic embedding | 英文改写、语义相似题 |
| 公式召回 | 公式 exact、变量骨架、数字骨架 | 代数、函数、数列、公式密集题 |
| 关键词召回 | token overlap / lexical recall | 图论、组合、定义型文字题 |
| 领域信号召回 | math\_signals overlap | 函数同余、路径、余数优化等专项题 |

## 5.3 关键词召回的重要性

在图论城市航班题中，题面关键并非公式，而是 cities、flights、long path、short path、no cities in common、number of flights 等短语。早期版本仅依赖向量与公式召回，导致这类题即使已经入库，也可能无法进入候选集。v6 之后加入 lexical recall 后，原题能够稳定召回；v7 又通过弱公式降权，避免简单公式骨架干扰排序。

# 6 融合评分与重排策略

## 6.1 分数组成

系统最终分数由向量分、规则分、文本重合分、公式精确分、变量骨架分、数字骨架分、条件/目标分、领域信号分和哈希奖励共同构成。不同题型的权重并不完全一致：公式密集题更看重公式，文字型图论题更看重关键词与图论信号，函数同余题更看重 multiplicative\_function\_eq、mod\_operator、target\_power\_form 等信号。

图 3  综合评分抽象形式

|  |
| --- |
| 综合分 = 融合函数(      vector\_score,      rule\_score,      text\_score,      formula\_exact\_score,      formula\_skeleton\_score,      condition\_target\_score,      signal\_score,      hash\_bonus,      penalty\_terms  ) |

## 6.2 匹配类型

表 5  检索结果类型说明

|  |  |  |
| --- | --- | --- |
| 类型 | 中文含义 | 解释 |
| original\_exact | 原题精确命中 | 原文或哈希完全一致 |
| near\_original\_rewrite | 原题改写 | 语义和关键信号均强，文本存在改写 |
| same\_formula\_skeleton | 公式骨架相同 | 核心公式结构高度一致 |
| semantic\_similar | 语义相似 | 向量和文本较接近，但结构支持有限 |
| related\_or\_weak | 弱相关 | 同主题或同领域，但缺少核心结构 |
| signal\_mismatch\_weak | 信号不匹配弱相关 | 有表面相似，但关键领域信号缺失 |

## 6.3 降权策略

系统采用若干降权策略避免误匹配。若 query 存在同余、乘法函数、幂函数目标，而候选缺失这些核心信号，则触发 signal\_penalty。若 query 是图论长短路径问题，而候选缺少 long\_short\_path 或 disjoint\_paths，也会降权。若候选只是共享 n>=NUM 或单变量公式，则不能触发强公式加分。

# 7 领域信号设计：函数同余、余数优化与图论路径

## 7.1 函数同余信号

函数同余类题目容易出现高语义假阳性。很多题都包含 f、positive integer、mod、prove 等词，但真正决定相似性的通常是 f(ab)=f(a)f(b)、f(m+n)≡f(m) mod n、not identically zero、f(n)=n^k 等结构。系统将这些特征抽取为 math\_signals，并在重排阶段作为强约束。

表 6  函数同余类信号

|  |  |  |
| --- | --- | --- |
| 信号 | 触发模式 | 作用 |
| has\_congruence | \equiv、mod、divides 等 | 识别同余类问题 |
| has\_multiplicative\_function\_eq | f(ab)=f(a)f(b) 或类似结构 | 识别乘法函数 |
| has\_nonzero\_function | not identically zero | 区分零函数类题目 |
| target\_power\_form | f(n)=n^k 或幂函数结论 | 识别幂形式目标 |

## 7.2 余数优化信号

对于包含 a mod n、remainder、max-min、sum over index、shifted mod expression 的题目，系统需要区分“泛同余题”和“余数优化题”。仅有 mod operator 并不意味着相似；若缺少 max/min、(a\_j+k) mod n、sum\_j 等结构，应降低排序。该方向仍属于后续增强重点。

## 7.3 图论路径信号

图论文字题往往公式很少，或公式主要是变量占位。系统为城市航班与路径类题增加了 has\_path\_structure、has\_long\_short\_path、has\_disjoint\_paths、has\_count\_edges\_target 等信号。以“long path / short path / no cities in common / number of flights”为核心的题目，在 v7 后能够被稳定识别为强相似或原题改写。

# 8 系统工程实现与命令行工作流

## 8.1 模块结构

当前系统以单个 Python 命令行工具为核心，包含 process-dir、stats、build、search 等子命令。process-dir 负责批量处理 split\_jsonl 目录，build 负责加载 processed\_jsonl 并生成向量索引，search 负责 query 处理、多路召回、融合重排和报告输出。

图 4  项目目录结构建议

|  |
| --- |
| math\_question\_search\_starter\_v8\_1/    src/      math\_search\_pipeline\_v8.py      enhanced\_question\_normalizer\_v2.py    requirements.txt    README.md     数据目录示例：    split\_jsonl/             原始题库 JSONL    processed\_jsonl\_v8/      处理后 JSONL    index/ap\_all\_v8\_gpu/     本地向量与记录索引    reports/last\_search.html HTML 搜索报告 |

## 8.2 处理与建库

图 5  批量处理与 GPU 建库命令

|  |
| --- |
| python src\math\_search\_pipeline\_v8.py process-dir ^    --input-dir "E:\数学\题目搜索\split\_jsonl" ^    --output-dir "E:\数学\题目搜索\processed\_jsonl\_v8"     python src\math\_search\_pipeline\_v8.py b...