---
title: 火山引擎开源 Agent 驱动的搜索自迭代技术
url: https://mp.weixin.qq.com/s/sJH9QeD71BWGIGDaOhaUvg
source: Doonsec's feed
date: 2026-07-29
fetch_date: 2026-07-30T04:47:22.948700
---

# 火山引擎开源 Agent 驱动的搜索自迭代技术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FGB4hYw9FeevKWiaSt6ls8QHziapbBhBHqicPoSXEcW0Gq9EPG9EypwI4TyH4KicO0J4icZuW2jTfFkIw1n2aAKtU1q7qibVricEj10DqEfCHmOYTQ/0?wx_fmt=jpeg)

# 火山引擎开源 Agent 驱动的搜索自迭代技术

Viking AI 搜索
Viking AI 搜索

字节跳动技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fee6YVYh8p5gnNPicn2Z238ebJvmBuP9g6KFFicBYQ4xpSNpphNdk88j1aPzXktP0EuiaribFLxTsFFxXfIQCVC5FELvWkCibOj8HpxE/640?wx_fmt=png&from=appmsg)

**会调用搜索，只是 Agent 搜索能力的第一步。更难的是：当结果不好时，它能不能找到改进方向，并通过一轮轮实验把搜索变好？**

假设你刚上线一个商品搜索应用：搜品牌、品类和型号基本正常，但用户输入“适合通勤的轻便双肩包”，结果就开始跑偏。

你提高语义召回权重，长句理解变好了，精确型号词却可能变差；提高关键词匹配门槛，前几条结果更准了，零结果又开始增加；放大候选集，召回更多了，噪声和延迟也可能随之上升。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefV0BL4EMNrjY7n5UXRTicQ5cLXdNprb34HibaVxGQGcIGatvdAQFZoxVtyq0Tc4xiaicZiadh8DHKkZVfGJL38Y4xC41CcOqG4GGicE/640?wx_fmt=png&from=appmsg)

很多搜索项目都会遇到类似的调优困境。问题不是没有参数可调，而是这些参数彼此影响：一次看似简单的修改，往往同时改变召回、排序、零结果率和延迟。要判断一组策略是否真的更好，还需要准备 Query、批量搜索、相关性标注、离线评测和 Bad Case 分析。

过去，这套工作依赖搜索专家反复试验。每一轮都能做，但很难低成本、可复现地持续做。

于是我们开始思考：既然 Agent 已经能够理解目标和调用搜索，它能不能再向前一步——**根据当前数据和 Query 分布，自动提出候选策略，用实验验证收益，并告诉开发者“为什么这组配置更好”？**

围绕这个问题，火山引擎在开源项目 SearchCLI 中开放了 vs search tune。开发者提供应用、数据集和 Query Set 后，Agent 可以调用它完成 Query 校验、实验规划、候选策略生成、批量搜索、相关性标注、指标计算、结果对比和候选 Scene 创建。

在服饰商品、综合商品和图片内容等三个业务数据集的阶段性离线评测中，自动调优策略相较默认策略，**NDCG@20 提升 11.66%～13.50%，Precision@10 最高提升 21.17%**。

这组结果首先说明了一件事：底层模型和数据不变时，仅仅围绕具体业务的 Query 分布重新组织召回模式、关键词与语义权重、匹配门槛和候选规模，也能释放出可观的效果空间。以上为阶段性离线结果，实际收益仍取决于 Query 代表性、标签质量和业务数据分布。

我们把这套能力称为：**Agent 驱动的搜索自迭代**。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fee0CHuCZDuPjpyI1m4TwicuQ9YafH9bSuZajKia0wcd6o2QaiagWLzh6dYiauHx6ZH4zDPWayx1SWosVheXOVRcxjSucL6gZHdyHEU/640?wx_fmt=png&from=appmsg)

“自迭代”不是让 Agent 绕过控制、直接修改线上策略，而是把“发现问题—提出假设—分配评测预算—筛选候选—验证收益—输出候选配置”变成一套可以重复运行、结果可以审阅的闭环。

接下来，我们将拆解这套闭环如何运转，以及背后的 SPA 策略优化框架，如何在有限搜索和标注预算下，把更多实验机会留给真正有希望的策略。

**一、从“会搜索”到“会把搜索变好”**

一个 AI 搜索系统通常包含召回模式、关键词与语义权重、关键词匹配门槛、候选集规模等配置。参数越多，适配不同场景的能力越强，但人工调优的门槛也越高。

真正困难的不是修改某一个参数，而是持续回答：当前策略在哪些 Query 上不好？应该加强关键词还是语义召回？平均指标提升是否掩盖了某类 Query 的退化？新策略是否会增加零结果和延迟？

搜索自迭代把这套专家工作流转化为一个反馈闭环：

```
Query 与业务数据  → 评测当前效果  → 生成候选策略  → 执行搜索与标注  → 比较指标和 Bad Case  → 输出候选配置  → 人工确认后进入验证
```

这里的“自”指流程可以由 Agent 持续驱动；“迭代”指每一轮都有 Query、标签和指标作为证据。生产变更仍保留明确的人为边界。

**二、为什么是 Agent + Skills + CLI？**

搜索调优既包含上下文判断，也包含领域知识和大量确定性执行。我们将三类工作拆给不同层次：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeeeA9CR1xsHL9T7iaESZgibYj2yjxjkJDgmwibFDajicAzk3bqxhOib7H800y5w8QDwtjcnOIlAk3OeKENiccAWwficEqibX3yUhUhnrp4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefqXKvXjK2ZU1Mb1M0RiaeJ7BbaVpOCfvQMpDeC3JCa5xOfxA1yu7WdQPkpCDf3R4TWPGNiavXN4tvRT7GAZtsteMxhG7QlNFMZg/640?wx_fmt=png&from=appmsg)

例如，Agent 会先判断用户是否有真实 Query；没有时，才生成合成 Query 并交由用户审阅。昂贵评测前必须先执行 Plan，确认策略数、Query 数和最大标注量。最终应用策略时，也必须先 dry-run，再由用户确认是否创建候选 Scene。

一次完整调优可能包含数千次搜索请求和大量 Query-item 相关性判断。如果让 Agent 临时拼脚本，网络抖动、限流或进程中断都可能让结果丢失。CLI 的价值，是把这些长任务变成稳定命令和机器可读的运行产物，让 Agent 决定“做什么”，让执行层保证“可复现地做完”。

**1、一次自迭代如何发生**

第一步是准备 Query Set。真实搜索日志、客服问题和人工整理的典型 Query 最有价值；如果暂时没有，也可以从数据集样本生成合成 Query，但必须先展示样例和类型分布，由用户判断它们是否代表真实意图。

第二步是校验和规划。validate 会检查格式、重复 Query、类型倾斜和 sourceItemIds 覆盖率；plan 则在不调用搜索和 LLM 的情况下，提前计算策略数量、搜索请求数与最大标签量。用户可以在真正花费预算前缩小 Query Set、减少候选或先选择低成本标签。

第三步是运行和复核。CLI 对每个候选执行批量搜索，先用 Source-item 银标快速筛选，或直接使用 LLM Judge 进行语义相关性判断，再计算 NDCG、MRR、Precision、零结果率和延迟。报告不仅给出推荐策略，也保留每条 Query 的明细，方便 Agent 解释收益来自哪里、是否存在退化。

最后，Agent 可以比较不同 Run，并把确认后的推荐配置转成候选 Scene。整个过程对应 query-generate → validate → plan → run → report → compare → apply，每一步都有结构化输入、输出和检查点。

**三、SPA：把预算花在更值得评测的策略上**

搜索调优看起来像参数优化，实质上却是一个**评测成本高、反馈有噪声、参数存在约束、结果还必须可解释和可落地**的实验设计问题。

候选策略、Query 数量和 TopK 增加后，最坏情况下的标注量近似为：

```
strategy_count × query_count × topK
```

因此，算法的核心任务不是生成尽可能多的组合，而是决定：哪些策略值得先测，哪些应尽早淘汰，下一轮沿什么方向探索，以及何时已经有足够证据停止。

SPA（Strategy Population Annealing）把搜索策略编码为带领域语义的 Genome，以专家先验构造初始种群，通过多保真评测、多视角 Elite、语义化进化和退火机制分配预算，再用鲁棒统计选出稳定、可解释的候选策略。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Feeib7KaO82mrOmtnVB6NcEmgnZJJtUcfgjQvGUq9ibf421KntbDFJW1vYKJ5k9Giajr17EPKqibytxxAnDT1peQem3NlMlXDuWR2PE/640?wx_fmt=png&from=appmsg)

**1、Genome：搜索参数不是普通数值向量**

```
{  "user_defined_recall_mode": "KeywordSemantic",  "dense_weight": 0.25,  "text_weight": 0.75,  "query_keyword_match_percent": 0.3,  "max_retrieved_num": 100}
```

这组参数既有枚举值，也有近似连续值和请求侧参数；同时还存在约束，例如 dense\_weight 与 text\_weight 需要归一，不同召回模式下参数含义也不同。SPA 的交叉、变异和移动都必须先理解这些语义，生成后还要经过裁剪、归一化、合法性校验和去重，才能转化为可执行配置。

第一阶段聚焦 similarity-only：只优化召回模式、关键词/语义权重、关键词匹配比例和最大候选数，不同时调整 Rerank、个性化、热度或运营规则。这样才能把效果变化归因到文本相关性策略本身。

**2、初始种群：覆盖搜索行为，而不是平均撒点**

Matrix Optimizer 会在若干固定档位上组合参数，优点是简单、稳定；缺点是不同参数不一定产生不同搜索行为，有限预算可能被大量相近或低价值组合占用。

SPA 的初始种群由当前策略、默认 Baseline、KeywordOnly / SemanticOnly 等边界策略、粗粒度 Matrix 和行业 Prior 组成。商品搜索可以多保留关键词主导的混合策略，知识库问答则保留更多语义增强分支。算法从有意义的行为区域出发，而不是从随机点开始。

当前开源首版已实现这一层：基于多个代表性中心，建立粗、细两种搜索半径，生成边界、中心和邻域候选，再执行合法化与去重。粗粒度邻域用于判断方向，细粒度邻域用于比较局部差异。

**3、多保真评测：先排除错误方向，再提高置信度**

完整设计将评测分为三层：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fecct9MgHNTpAYuKbYIah29c8IuYxky1VFibVibZl3rkNS65xSWCXDVibPQy7pBG2PblKP4icIsqSwGe1JQz1TXXNR2Jjgg0NVZAb0E/640?wx_fmt=png&from=appmsg)

如果一个策略连生成 Query 的源 Item 都召不回来，就没必要继续为它的 Top20 结果支付 LLM 标注成本。反过来，Fast Pass 高分也不能直接胜出：它还要证明收益不是只集中在标题改写等少数 Query 类型上。

**4、多视角 Elite：保留一条策略前沿**

只按平均 NDCG 选 TopN 很危险。某个策略可能在短词 Query 上很强，却让自然语言 Query 明显退化；另一个策略平均分略低，但零结果率、延迟和分类型表现更稳定。

因此，SPA 同时保留 Global Best、Query-Type Best、Stable Best、Low-Latency Best、Low-Zero-Result Best、Baseline-Improver 和差异足够大的 Diverse Candidate。每个 Elite 都回答一个问题：它为什么值得继续消耗预算？这比单一排名更能防止种群过早塌缩。

**5. 语义化进化与种群退火**

下一代候选来自三类动作。交叉会组合两个 Elite 中已被验证的有效结构，例如采用策略 A 的关键词/语义权重和策略 B 的关键词门槛；局部变异会在优秀策略附近调整权重、候选规模或匹配比例；方向移动则让候选向全局最优或某类 Query 的局部最优靠近。

这些动作都不是随机拼 JSON。例如，高关键词门槛导致零结果上升时，下一代会降低门槛；候选数从 100 增加到 200 没有提升却增加延迟时，搜索会向较小规模收敛。

退火温度控制探索幅度：早期温度高，允许接受少量当前略差但差异较大的策略；中期围绕 Elite 交叉和变异，同时保留边界探针；后期温度降低，只在高价值区域细调。与单点模拟退火不同，SPA 同时保留多个策略分支，因此既能跳出局部最优，也不容易被一次随机移动带偏。

**6、鲁棒目标：不被一次高分欺骗**

```
RobustScore =  NDCG@20  + α × MRR@10  - β × zero_result_rate  - γ × latency_penalty  - δ × query_type_variance  - ε × confidence_interval_width
```

NDCG 衡量整体排序，MRR 强调首个高相关结果的位置；零结果率和延迟是落地约束；Query 类型方差用于惩罚“只在少数类型上好”的策略。置信区间可通过 Bootstrap 得到：对 Query Set 多次重采样，如果一个策略均值高但区间很宽，说明它可能只是碰巧在这批 Query 上表现好。

因此，完整 SPA 要找的不是一次实验中的最高分，而是在 Query 分布和 Judge 噪声下仍然稳定的策略。

**四、实验结果**

实验比较自动调优策略与默认策略。在三个不同业务数据集上，

NDCG@20 提升 11.66%～13.50%

NDCG@10 提升 9.56%～15.08%

MRR@10 提升 7.74%～14.95%

Precision@10 提升 7.36%～21.17%。

**五、让算法真正可用的 CLI 工程层**

算法决定评估什么，工程层决定实验能否稳定完成。SearchCLI 重点沉淀了四类能力。

**Plan：先把实验成本编译出来。**vs search tune plan 不实际调用搜索或 LLM，而是提前给出 Query 数、候选策略数、预计搜索请求和最大标注量，让 Agent 在昂贵任务开始前缩小范围或调整标签来源。

**受控并发：****把长任务拆成小任务。** 当前开源实现将评测拆为 strategy × query 任务，并采用有界批次调度；每批通过 Promise.allSettled 汇总结果，单个失败不会丢掉同批已完成的数据，也不会无限放大请求。任务队列与 Worker Pool 是后续可继续演进的方向。

**标签缓存：****让 LLM 判断成为可复用资产。** 不同策略经常召回相同 Item。SearchCLI 的缓存 Key 同时包含数据集、Query、Item 内容和 Judge 配置；只有这些信息一致时才复用，内容或评测标准变化后旧标签会自然失效，从而在节省成本的同时避免误用历史结果。

**Checkpoint / Resume：****中断后接着跑。** CLI 会持续保存运行状态、搜索结果、已用标签、失败记录、中间指标和性能摘要。任务中断后，Agent 可以使用原 Run ID 继续未完成部分，不必重新支付已经完成的搜索与标注成本。

最终的 apply 也保留安全边界：先 dry-run 展示配置，获得确认后只创建新的候选 Scene，不会自动切换默认入口。自动化减少的是重复劳动，不是取消人的业务判断。

**六、快速开始**

SearchCLI 要求 Node.js 20 或更高版本，并采用 Apache-2.0 License 开源。安装 CLI 与 Viking Skills：

```
git clone git@github.com:volcengine/SearchCLI.git vscd vsbash ./scripts/install.shnpx skills add "git@github.com:volcengine/SearchCLI.git" -y -g
vs auth loginvs doctor --json
```

Agent可以通过以下指令进行调优：

```
vs search tune validate --queries ./queries.jsonl --json
vs search tune plan \  --application-id <application-id> \  --dataset-id <dataset-id> \  --queries ./queries.jsonl \  --profile similarity-only \  --optimizer spa \  --json
vs search tune run \  --application-id <application-id> \  --dataset-id <dataset-id> \  --queries ./queries.jsonl \  --profile similarity-only \  --optimizer spa \  --label-source llm \  --json
vs search tune report --run-id <run-id> --json
```

**项目地址：**https://github.com/volcengine/SearchCLI

**结语**

Agent 时代，搜索系统面对的问题正在从“能不能提供足够多的策略参数”，转向“能不能根据当前数据和 Query，持续找到更适合的策略”。

SearchCLI 给出的答案，是用...