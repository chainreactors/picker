---
title: Memfit AI 长期记忆：让渗透 Agent 告别 “失忆”，练就实战肌肉记忆
url: https://mp.weixin.qq.com/s/yCM2jpi_iHGZr_RuwvPP0w
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:13:53.213273
---

# Memfit AI 长期记忆：让渗透 Agent 告别 “失忆”，练就实战肌肉记忆

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72GFm6eztRXN7JF3FaakggdYAibPcySGibiapNnvNyKwcn1fuW2TOGVdlHlibSq600sKsokHccicxBibWCBGeHVoYibtvXcaV9JXAiauZR8/0?wx_fmt=jpeg)

# Memfit AI 长期记忆：让渗透 Agent 告别 “失忆”，练就实战肌肉记忆

原创

YAK
YAK

Yak Project

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZc5BYI1O7qwYC876L6gkbkACCZMJOIAPQmNqT0uZojjJZcfPsNJk6EjcbicXiaaSZ6j4APvocaxlI1w/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZeeTiaUCTkrXfbtIPCxmicjgPxhq9ZDnzI4ge0SwCTAMbAvAI5yWUnoBLqzicqmJAtuUiaygZO5lqSGJQ/640?wx_fmt=webp&from=appmsg)

在上一篇文章中[Memfit AI 专业记忆:Agent 动手之前,先翻了一遍你的知识库](https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247529575&idx=1&sn=cd0b7de7036ee8e812cbdc8fb4fc840a&scene=21#wechat_redirect),我们解决了 Agent 的“见识”问题。通过内置的知识库系统,Agent在执行攻击前,能够像资深专家一样先翻阅企业的私有测试和规范文件,确保自己的行动不脱离合规基线。

但作为一名真正的生产级 Agent,仅仅“有见识”是不够的。

**知识库是别人给的经验,而记忆是自己实践的成果。**

在长达数小时的连续渗透中,Agent 会遇到无数教科书和规范里没有写的“暗坑”:比如某个特定业务系统的异常报错、某个只有在特定内核版本下才会触发的 Payload 偏移、或者是某次成功提权后的环境特征。

如果这些实战经验随看随忘,那么下一次遇到同样的阻碍,Agent 还要重新走一遍 RAG 检索、重新分析、重新试错。这种低效的重复,是阻碍 AI 迈向“专家级”的最后一道坎。

**我们需要 Agent 不仅能“翻书”,还能在实战中“吃一堑,长一智”。**

本篇文章,我们将深入探讨 Memfit AI 的**长期记忆(Long-term Memory)系统**。你会看到,Agent 如何在执行任务的过程中,自主地对攻击路径进行复盘,并通过一套严苛的 **C.O.R.E.P.A.C.T.** 评估模型,将零散的执行日志炼化为结构化的“肌肉记忆”。

当 Agent 再次站在类似的战场前,它不再需要去知识库里大海捞针,而是能直接凭借这种“长期记忆”,避开坑点。

![](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72E7WkN5uibhGOeVDkNZ7YAMCKvyPHuQTyAVxVJvY5FicCGqI8YqKMoTrpB82Mn6wUZDDfqWoqTcjhjoRrWls8XoHqia7nw1HgGRQc/640?wx_fmt=jpeg&from=appmsg)

开发者最头疼的就是“上下文爆炸”。若将每一句对话和回显都存入 RAG,知识库很快会变成噪音堆。Memfit AI 引入了 **C.O.R.E. P.A.C.T.** 审计算法,在记忆沉淀前进行价值审计。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72ETdLicsT6VbcS0YCwzxeYQ3VR82iclL0y9AslpGDeH4awV0jpz8YRCG0icKWhWlunwcSXUqfTpiao9ZRuJqvGGRJR7fI03icpcH1dQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72GBC8n9c4VVGXg9vClcFn3ccWA1SDU4ehdChzCnwTXZ6IRVIKQFtsibrnDyva5icHGKMVuObmoQ756934nrp5DuIQnsvLIK3R2zk/640?wx_fmt=jpeg&from=appmsg)

|  |  |  |
| --- | --- | --- |
| 维度 | 定义 | 实战逻辑 |
| **C**onnectivity | **关联度** | 该信息能否钩住资产拓扑?(如:IP 与子网、业务系统的关联性) |
| **O**rigin | **确定性** | 信息的来源可靠吗?(whoami的回显 O=1.0;视觉猜测的后台 O 值较低) |
| **R**elevance | **相关性** | 未来复用的概率多大?(Session ID 相关性低,Struts2 绕过 Payload 相关性极高) |
| **E**motion | **敏感度** | 交互的优先级。连续失败的“挫败感”或成功的“转折点”会被加权记录。 |
| **P**reference | **偏好约束** | 是否符合“静默渗透”等甲方约束?不合规的动作记忆将被压低权重。 |
| **A**ctionability | **可操作性** | 是废话还是指令?包含完整 sqlmap 或 curl 参数的记录 A 值会很高。 |
| **T**emporality | **时效性** | 经验的保质期。资产 IP 会变，但漏洞补丁逻辑变动慢，动态清理过期记忆。 |

![](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72ER1vx3cw77OjMxhc7Z8wbCGS9NJUo7kgcDcK9yLNLMCUQ3rcuZBggiaPPBdLyibcLUia5Mg41H24HmeIYyIkYtg0ebrJA1GlQ2oo/640?wx_fmt=jpeg&from=appmsg)

这是一个我对vulinbox靶场的SQL检测产生的记忆案例图。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FiaykXWmhIecrvUbKlwMowDZjeXiaKFfSolJC7MzJulElRQhrPJIfh0f0L1A91UarFcyhmLsHUm9dnibBBIxPBqlLqQy1DRqrZTI/640?wx_fmt=png&from=appmsg)

以针对 `http://127.0.0.1:8787` 的 SQL 注入检测为例。通用 AI 只会复现 `ORDER BY` 的标准动作,但 Memfit AI 沉淀了如下记忆:

> **记忆摘要:** 在联合查询探测失败(列数不匹配)时,应优先使用 `ORDER BY` 子句从 1 开始递增探测以确定正确的列数,而非直接尝试构造 Union Select Payload

除了这个记忆以外 还有一些更具体的记忆。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72E3BIL9FR7EQSj25Q6gDrySdgpkyZYibC20dr3WrVqlEDwCqWzWFvtRll0de2YAUhicFcv1pIXcQBZwibpUlOa5ENnnib5o07wu66k/640?wx_fmt=png&from=appmsg)

> **记忆摘要:** 针对靶场目标,memfit已经探测过是 9 列数据库

#### 维度过滤逻辑(雷达图分析)

通过 Memfit 独有的评估模型,我们可以看到这条记忆为何被视为“黄金经验”:

* **O(来源可靠性)-0.9:**该策略源于 Agent 在实战中遭遇的“探测失败”。失败的回显是真实的数据反馈,可靠性极高。
* **A(经验价值)-0.8:这不是废话,它给出了明确的****替代动作**(从1开始递增探测)。这类具有“可操作性”的记忆是 Agent 进化的燃料。
* **R(重要性)-0.8:确定列数是 SQL 注入的基石。记住这个策略,意味着 Agent 在未来的所有同类任务中,都能规避“盲目构造 Payload”的时间浪费。**
* **C(关联度)-0.8:它被贴上了**`sql-injection` 和 `testing-methodology` 的标签,能精准钩住后续所有涉及数据库探测的资产。

#### 问题索引:索引记忆

还有一个值得一提的设计在于记忆底部的 **Potential Questions(潜在问题)**。Memfit AI 在存储记忆时,会自动预判未来自己可能会问的问题:

*1.“当联合查询探测失败时,如何确定数据库返回的列数?”*

*2.“SQL 注入中 ORDER BY 探测的具体执行步骤是什么?”*

**这意味着什么?**

当下一次 Agent 在新任务中遇到“联合查询报错”时,它脑中会产生类似的疑问。系统会瞬间匹配到这些“潜在问题”,将这条的记忆加入当上下文中,帮助AI回忆起之前的经验。

**Agent 不再是在搜数据库,而是在“回想”自己的成功经验。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72EQttygQE6mWsPxfWHAMQUIGl2rel1krqYmgg2jGMbNoNiaLtAXVY8eoVnpkwFZ38LPX8ibO9G05KHOM8rwTyQaiaW6tTKfQhVH74/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FQqUF6nlOxN1yWy6KdU7qvWlEtfJG4MfB3a6mf6cVnKscQ8UOWnMBQDIZw6OSib379AxDCq0OAf3s3Xhy5LxJ4tJG2lFyITjEA/640?wx_fmt=png&from=appmsg)

有了合理的记忆设计,还有一道门槛如何在某一个时间在合理的位置到找合适的记忆。

Memfit AI 的 `AIMemoryTriage`(记忆分选器)通过一套严密的加权重排算法,将静态的 C.O.R.E. P.A.C.T. 理论转化为了生产环境中的**实时决策流**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72HCh0MdOkLZ00b5YLjxmdYKvicEgkcZmUR2hic7ib6O9JEVxKy8Z5930J94ZzxKKFAsSlKNluLAODadia0YM4O0xJibP46uMxa7dSsI/640?wx_fmt=jpeg&from=appmsg)

我们为记忆设定了七个维度的权重。先从海量的记忆中排除各种过于极端偏激,或者无意义的经验指导,初步完成记忆寻找。

```
weights := map[string]float64{    "R": 0.25, // Relevance - 核心相关性,决定了搜索的基调    "C": 0.20, // Connectivity - 关联度    "T": 0.15, // Temporality - 时效性,确保经验不过期    "A": 0.15, // Actionability - 可操作性,拒绝无意义的废话    "P": 0.10, "O": 0.10, "E": 0.05, // 辅助维度}
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72EfPjH2n6czLsrGVfdIiaztib55EujreQue95Tz1vZLpicNFabib13iavz3OgaYW7V4XuDmXiaSc55pAnQcQJ1zfDL7eic66iaxCfriapZw/640?wx_fmt=jpeg&from=appmsg)

`静态分数保证了记忆的质量,而(关键词加成)则赋予了记忆灵活性。`

即使一条记忆的原始评分很高,如果它与当前 Query(查询词)不匹配,它依然会被降权。我们中设计了五级加成机制:

```
contentBonus := 0.0// 1. 内容关键词匹配分数 (权重: 0.1)contentMatchScore := t.keywordMatcher.MatchScore(query, memory.Content)contentBonus += contentMatchScore * 0.1// 2. 标签关键词匹配 (权重: 0.08)tagContent := strings.Join(memory.Tags, " ")tagMatchScore := t.keywordMatcher.MatchScore(query, tagContent)contentBonus += tagMatchScore * 0.08// 3. 问题关键词匹配 (权重: 0.05)questionContent := strings.Join(memory.PotentialQuestions, " ")questionMatchScore := t.keywordMatcher.MatchScore(query, questionContent)contentBonus += questionMatchScore * 0.05// 4. 直接关键词包含检查 (权重: 0.05)if t.keywordMatcher.ContainsKeyword(query, memory.Content) {    contentBonus += 0.05}// 5. 所有关键词都包含的奖励 (权重: 0.03)if t.keywordMatcher.MatchAllKeywords(query, memory.Content) {    contentBonus += 0.03}// 限制加成不超过0.3if contentBonus > 0.3 {    contentBonus = 0.3}
```

**1.标签匹配(0.08): 命中**`#sql-injection`或 `#rce`等专家标签。

**2.内容匹配(0.10):扫描 Payload 或回显中的关键字符串。**

**3.反思匹配(0.05):**匹配 Agent 此前自发生成的 `PotentialQuestions`。

**4.全关键词奖励(0.03):**确保精准匹配的记忆能够“置顶”。

所以最后的排序评分公式为:

$$FinalScore = \text{BaseScore} + \sum \text{KeywordBonus} (\text{Max } 0.3)$$

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72Gmsd7AREF7f6CBCZoawx2QJ4ibB5v5ibZXNicPXg1G7jDmfJsIFyvXAbOoXzGbwhgwsFTtQukicTaiaUG23QAAMyl4mH6QibpCBJOAc/640?wx_fmt=jpeg&from=appmsg)

```
[ must_aware ]- 关键偏好/约束:对目标URL http://127.0.0.1:8787/user/name?name=admin 执行SQL联合注入测试,验证注入点存在性、确定列数与回显位、提取数据库信息(版本/当前库/当前用户)、枚举表名列名、提取敏感数据;使用do_http_request工具构造HTTP请求完成测试 (u=0.88, P=0.80, R=0.90, age=1m55s)
[ action_tips ]- 经验/可执行提示:SQL 联合注入测试目标 URL 为 http://127.0.0.1:8787/user/name?name=admin,该端点存在未参数化 SQL 查询:query = f"SELECT * FROM users WHERE username = '{name}'",属于典型注入漏洞点;测试需覆盖字段数判断、回显位置定位、数据库信息获取、表名/列名枚举、敏感数据提取等步骤。 (u=0.86, A=0.90, R=0.90, T=0.90, age=4m59s)- 经验/可执行提示:对URL http://127.0.0.1:8787/user/name?name=admin 执行字符型SQL联合注入测试,测试流程包含:1)注入点确认;2)确定列数;3)确定回显位;4)提取数据库信息(版本/当前库/当前用户);5)枚举表名和列名;6)提取敏感数据。 (u=0.83, A=0.80, R=0.90, T=0.80, age=28m8s)- 经验/可执行提示:用户指令明确要求对指定URL执行SQL联合注入测试,该请求已通过意图识别流程确认为安全测试任务,目标是探测目标服务是否存在SQL联合注入漏洞。 (u=0.83, A=0.90, R=0.90, T=0.80, age=11m35s)- 经验/可执行提示:对目标URL http://127.0.0.1:8787/user/name?name=admin 执行SQL联合注入测试,需验证注入点存在性、确定列数与回显位、提取数据库版本/当前库/当前用户、枚举表名列名、提取敏感数据;已知目标支持布尔盲注和时间盲注,需手动构造HTTP请求完成测试。 (u=0.83, A=0.90, R=0.90, T=0.80, age=8m25s)
```

在检索到了记忆的实体之后,memfit在将其注入到最终prompt中还有一步重要的操作**:意图路由**

**其核心观点是:不同任务下,记忆的优先级应当完全不同。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72GK2I3ImvOH1LicfvJHzmsvu6xGxDTwcNicabLs0jia818QmnCy2Bc4BYiapBXDZmTAzn8A6qQst2b75zkDwDpQxlXwC7emtP7zJ1Y/640?wx_fmt=png&from=appmsg)

#### 记忆路由分配

通常来说记忆的检索会将所有的所有文本视作平等的“背景资料”,而我们尝试通过上面的评分的机制通过多维特征识别,将原始记忆分配到不同的**路由**中:

* **MustAware(关键约束):识别为用户硬性偏好或禁忌的信息。它们被赋予最高权重,防止模型违背核心指令。**

* **ActionTips(经验提示):提取自过去成功操作的建议...