---
title: 数学题库知识库项目阶段性说明：先放出一版已经整理好的数据
url: https://mp.weixin.qq.com/s/1nV_YUoPF0VQqN82AX33GQ
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:46:56.915746
---

# 数学题库知识库项目阶段性说明：先放出一版已经整理好的数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xyspsQs8n7xAhknjtprciatcH7OibYAKzPvKFSyR15qCOKkAhQwZ6LHEXwktDqGcFtD1s8ibqm1kSGhIp48FrNNHl9VqV07XSIa5TfWdlcIWibc/0?wx_fmt=jpeg)

# 数学题库知识库项目阶段性说明：先放出一版已经整理好的数据

Uysieot
Uysieot

简单读写

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

数学题库知识库项目阶段性说明书

一版已经整理好的数据、脚本与测试页面说明

阶段性发布说明 · 非最终完善版本

|  |
| --- |
| 数据来源声明  本项目所有题目、解答等原始数学数据均来自 MathNet。本项目当前公开的工作，主要是围绕这些公开题库数据进行整理、结构化、步骤拆解、知识点抽取、知识点价值评估、数据库导出与检索页面测试。感谢 MathNet 以及所有参与题库整理和开源共享的贡献者，特别感谢 Navid Safaei多年来收集和整理题目的辛苦工作。 |

致谢声明：

* 感谢成都的刘帅老师无偿给予的服务器资源与其他的帮助。
* 感谢林天齐老师，思路的提供和数据整理以及各种帮助和关心。
* 感谢宁波的隽爸(家长)提供的平台得已讨论。
* 感谢 全国竞赛交流群(群主 隽爸) 的各位老师和家长以及同学的积极讨论和建议。
* 感谢 赛题讨论群(群主 程国根)的各位老师和家长以及同学的积极讨论和建议。
* 感谢 四川的比赛交流群( 新 )群友的支持，注，此群是琴棋书画方向。

其他未感谢到的，下个版本发布的时候一定感谢到。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xyspsQs8n7xgv5qNFNiawiam9e0DMprvibafPuVAvQTSSOChrKlLaxKIRNeeA29XC6uPibsehxpicGmZiaao7dEm3Xxkibq5LiaQmM3wtibhznel6GEQ/640?wx_fmt=png&from=appmsg)

**测试地址：**

https://math.yukicv.com/index/step\_search\_indexed/index

测试地址二维码：

![生成的二维码](https://mmbiz.qpic.cn/sz_mmbiz_png/xyspsQs8n7w2HvskTf26xZnaH3HEoTERlCA6om95nK9yibWBicW2VpqtBia6dUkFH7fCU5GRHXNpOmaiaBfTepLmcERHAXxNdPosR0Hv1qQdFDY/640?wx_fmt=png&from=appmsg)

数据下载方法：

夸克链接：https://pan.quark.cn/s/a0c021f65a0e?pwd=Jm4f

百度链接：https://pan.baidu.com/s/1HJcEBDH6jWS6s1SX9G2qKw?pwd=42zv

讨论页面：

本文章的评论区

作者微信：sbsb945a 。注：请主要讨论过后完善方向的公益方向（同意我将后续成果免费发布）的人士加。商业的话无需加我，因为数据都完全开源了，你们在遵从mathnet的开源框架下自行使用即可。不接受任何形式的捐助。

这个项目目前还远没有到最终完善的地步。它现在更像是一个已经跑通的阶段性版本：从题目与解答出发，逐步拆出解题结构、步骤细节、知识点、知识点教学价值评估，并进一步整理成可导入数据库、可用于网页检索的数据文件。

我之前承诺过会把这个项目开源。考虑到大家可能已经等了一段时间，而完整系统后续还会继续迭代，所以这一次先放出一版已经整理好的文件。它不是最终形态，但已经能体现整个项目的核心思路和目前已经完成的工作。

为避免大家等太久，所以先放一个版的半成品出来，供大家把玩。

目录

|  |
| --- |
| 1. 项目目标：不是普通题库，而是解题过程知识库                   2. 当前公开的数据与 outputs 目录结构                   3. 各阶段做了什么：01 / 02 / 03 / 05 / 07 / 08                   4. 关于 04 和 06：检测阶段为什么没有附带                   5. 测试 PHP 页面与在线访问地址                   6. 当前版本的意义、限制与后续计划 |

# 1. 项目目标：不是普通题库，而是解题过程知识库

> 从开源题库到可反查、可分层、可分析的数学知识系统
>
> Uysieot，公众号：简单读写[数学题库知识库的制作流程：从一道题到可反查、可分层、可分析的知识系统](https://mp.weixin.qq.com/s/b-f28g2EE5PDNGSHsiiAiA)

这个项目的目标，不只是把题目和答案保存下来，而是尝试把一道数学题拆成更细的结构。传统题库通常保存题目、答案、标签和难度；但在真实学习中，学生真正需要知道的是：这道题为什么这样做？我卡在哪一步？这一小步用了什么知识点？这个知识点是否值得专门学习？

·一道题的完整解法是什么？

·每个解法可以拆成哪些步骤？

·每一步在证明中起什么作用？

·它依赖前面哪些结论？

·它产生了哪些新的结论？

·这一小步用到了哪些知识点、方法或技巧？

·这些知识点对高中数学竞赛学生来说，是基础、核心、稀有，还是只适合在当前题目里展示？

因此，这个项目更接近“数学讲义 + 知识库后台 + 题目检索系统”的结合体。它试图把题目、解法、步骤、依赖关系、知识点和教学价值连接起来，为后续的知识点反查、分层教学、难度解释、按知识点组题打基础。

# 2. 当前公开的数据与 outputs 目录结构

本次整理出的文件主要放在 outputs 目录下，包括 01、02、03、05、07 相关目录，以及 08 的索引文件。可以把这些目录理解为一条流水线上的不同阶段。

|  |  |  |
| --- | --- | --- |
| 阶段 | 主要内容 | 说明 |
| 01 | 原始题目与答案缓存 | 保留来自 MathNet 的题目、解答等基础数据。 |
| 02 | 解法总体架构 | 把完整解答拆成较细的步骤目录，输出 architecture.json。 |
| 03 | 步骤详情与 raw 知识点 | 逐步生成解释、公式、依赖图、产出结论和 raw knowledge points。 |
| 05 | 知识点价值评估 | 面向高中竞赛生评估每个知识点的难度、教学价值、通用性和入库建议。 |
| 07 | MariaDB SQL 导出 | 把 02/03/05 的 JSON 输出整理成可导入 MariaDB 的 SQL 文件。 |
| 08 | 检索索引 | 为数据库检索和测试页面准备索引文件。 |

|  |
| --- |
| 当前发布口径  这不是完整的最终知识图谱系统，而是一版已经完成结构化整理、可以继续开发、可以测试检索的数据和脚本。后续仍需要继续做知识点去重、合并、搜索优化、前端简化和难度体系完善。 |

# 3. 各阶段做了什么

## 3.1 01：保留原始题目和答案数据

01 阶段保存题目和解答的基础数据，作为后续所有 AI 拆解和知识点抽取的来源。这里的原始数学内容来自 MathNet；项目后续阶段是在这些数据之上进行结构化整理。

## 3.2 02：生成每个解法的总体步骤架构

02 阶段只做一件事：把完整解答拆成总体解题架构，也就是步骤目录。它不抽取每一步的详细解释，也不抽知识点。它关注的是“这个解法大概由哪些步骤组成，每一步做什么，为什么做，和原解中的哪一段对应”。

·输入：outputs/01\_problem\_answer\_cache.jsonl。

·输出：outputs/02\_solution\_architecture/p{problem}\_s{solution}/architecture.json。

·同时保存成功与失败日志，支持断点续跑。

·每个 architecture.json 中保存题目、中文题面、原始解答、中文解答、分类、题目摘要、解题策略和步骤大纲。

|  |
| --- |
| outputs/02\_solution\_architecture/                     p3\_s1/                       architecture.json                    architecture.json 里主要包括：                   - problem\_markdown / zh\_markdown                   - solution\_markdown / solution\_zh\_markdown                   - problem\_summary\_en / problem\_summary\_zh                   - solution\_strategy\_en / solution\_strategy\_zh                   - steps[]：step\_title、brief\_action、purpose、source\_quote |

## 3.3 03：生成每一步的详细解释、依赖图和 raw 知识点

03 阶段读取 02 的 architecture.json，再对每一个 step 单独处理。这里开始进入真正细粒度的“解题过程知识库”：每一步都保存成独立 JSON，里面有中英文解释、公式、推导流程、前后衔接、依赖步骤、支撑步骤、产出结论和 raw knowledge points。

·输入：outputs/02\_solution\_architecture/\*\*/architecture.json。

·输出：outputs/03\_step\_details/p{problem}\_s{solution}/step\_0001.json、step\_0002.json 等。

·每一步单独保存，便于断点续跑、页面生成、后续回写和数据库索引。

·此阶段仍然不做最终知识点去重，也不匹配已有知识库，只记录 raw knowledge mention。

|  |
| --- |
| step\_0003.json 里可能包含：                   - step\_text\_en / step\_text\_zh                   - goal\_en / goal\_zh                   - derivation\_flow[]                   - formula\_lines[]                   - depends\_on\_steps / supports\_steps                   - dependency\_graph / dependency\_edges                   - produced\_results[]                   - raw\_knowledge\_points[] |

这个设计的一个重点，是不只保存线性的“第 1 步、第 2 步、第 3 步”，还尝试保存真实证明依赖。例如一个步骤可能依赖前面两个或三个条件，尤其在几何、组合、数论证明中，多条件推理很常见。

## 3.4 05：评估知识点对高中竞赛生的教学价值

05 阶段不是解题，也不是评估题目难度，而是对 03 抽取出来的 raw knowledge points 做“高中竞赛生知识点价值画像”。它关心的是每一个知识点是否值得教学、是否适合进入全局知识库、是否适合用于搜索筛选和难度估计。

·知识点本身难度：difficulty\_level\_1\_10。

·学生理解难度：student\_understanding\_difficulty\_1\_10。

·预计学习时间：estimated\_learning\_time\_1\_10。

·教学价值：teaching\_value\_1\_10。

·学习收益：learning\_roi\_1\_10。

·通用性等级：universal\_basic、general\_method、domain\_method、specific\_variant、problem\_specific、noise。

·入库建议：keep\_core、keep\_support、keep\_background、merge\_to\_parent、problem\_specific\_only、discard\_or\_hide、needs\_human\_review。

这里特别强调：当前步骤重要，不等于这个知识点全局教学价值高。比如某个基础恒等式在某道题中可能是关键一步，但对高中竞赛生来说可能太基础，不一定值得作为全局核心知识点单独展示。

## 3.5 07：导出 MariaDB 可导入 SQL

07 阶段把 02、03、05 的 JSON 输出整理成 MariaDB 10 可导入的 utf8mb4 SQL 文件。它不直接连接数据库，也不生成 SQLite，而是只生成 .sql 文件，方便部署和迁移。

·兼容 MariaDB 10，JSON 原文统一用 LONGTEXT 保存。

·大数据量自动分片，适合后续更大规模的数据。

·默认输出 schema、data 分片、postprocess 文件和 import\_all 文件。

·核心表覆盖题目、解法、步骤、步骤依赖、产出结论、raw 知识点、知识点评估、别名、搜索文档和知识点索引。

|  |
| --- |
| outputs/07\_mysql\_sql/                     00\_schema.sql                     01\_data\_0001.sql                     01\_data\_0002.sql                     ...                     99\_postprocess.sql                     00\_import\_all.sql                     07\_build\_mysql\_sql\_summary.json |

## 3.6 08：数据库检索索引

08 主要用于为数据库检索准备索引文件。测试页面依赖这些索引来提升查询性能，尤其是按知识点、分类、步骤标签、教学价值等维度筛选时，索引会直接影响页面响应速度。

# 4. 关于 04 和 06：检测阶段为什么没有附带

本次公开文件里没有附带 04 和 06，不是因为它们不重要，而是因为它们主要是检测环节。

·04 主要用于检查 02 和 03 的输出错误。

·06 主要用于检查 02、03、05 的输出错误。

在这次整理出来的版本里，这些检测环节没有发现需要单独附带的问题结果，所以暂时没有把它们放进公开文件中。后续如果项目继续完善，检测脚本和检测报告也可以再作为单独部分补充。

# 5. 测试 PHP 页面与在线访问地址

上传的 PHP 文件 StepSearchIndexed.php 是测试用页面，不是最终前端。它是一个 ThinkPHP 控制器，用来做数学题库步骤查询和分类观察页面。页面使用的是 07 导出的数据库表，并且建议先执行 08 的 MariaDB 索引文件，以生成索引和 step\_kp\_summary。

测试地址：https://math.yukicv.com/index/step\_search\_indexed/index

这个页面主要用于观察数据质量、测试分类字段和验证搜索能力。它支持按关键词、题目 ID、题目分类、步骤标签、知识点类型、教学价值、学习收益、理解难度、学习时间、命名定理、题目特化、是否页面展示、是否需要人工复查等条件筛选。

进入某个步骤后，页面可以展示原题、解法策略、当前步骤、公式、推导流程、依赖关系、本步产出结论和主要知识点等内容。由于它是测试页面，当前筛选字段故意保留得比较全，方便观察哪些字段有用；真正面向用户的页面后续应该进一步简化。

# 6. 当前版本的意义、限制与后续计划

## 6.1 当前版本的意义

这次放出的不是一个“完美的知识图谱系统”，而是一批已经整理好的阶段性数据和配套脚本。我自己更看重的是，它已经把“题目—解法—步骤—依赖—知识点—教学价值—数据库检索”这一条链路初步跑通了。

这也是后续继续做知识点合并、难度估计、分层教学、反查题目、按知识点组题的基础。

|  |
| --- |
| 这个阶段最核心的价值  它把题库从“题目和答案的集合”，推进到“可以解释解题过程的知识库”。每道题都可以被拆成步骤，每个步骤都可以连接知识点，每个知识点都可以评价教学价值。 |

## 6.2 当前版本还没有完善的地方

·raw knowledge points 还没有完成最终去重和合并。

·有些知识点只是当前题目的局部表达，后续需要合并到更通用的父知识点。

·不同题目中出现的同义知识点，还需要继续建立统一的 canonical knowledge point。

·数据库和搜索页面仍然是第一版，字段偏多，后续需要按真实使用场景删减和优化。

·难度系统、知识点稀有度、学生学习路径、按知识点组题、避免提前遇到未学知识点等功能，还需要继续建设。

## 6.3 为什么先发布这个版本

原因很简单：项目还没最终完成，但已经有了一批可以看的、可以查的、可以继续开发的数据。与其一直等到“完美”再发布，不如先把已经整理好的阶段性成果放出来。这样大家可以先看到项目现在做到什么程度，也可以基于这些文件提出建议、测试数据、继续改进。

这次公开的版本，重点不是展示一个最终产品，而是展示一个方向：数学题库不应该只是题目和答案的集合。它也可以成为一个面向学习过程的知识库。学生可以进一步知道：这道题为什么难，我卡在哪一步，我缺的是哪个知识点，下一步该练什么。

# 附录：本次文件的大致阅读顺序

1.先看 outputs/02\_solution\_architecture，理解每个解法如何被拆成步骤目录。

2.再看 outputs/03\_step\_details，理解每一步如何保存解释、公式、依赖和 raw 知识点。

3.然后看 outputs/05\_kp\_value\_rating，理解知识点如何被评价教学价值和入库建议。

4.需要部署数据库时，再看...