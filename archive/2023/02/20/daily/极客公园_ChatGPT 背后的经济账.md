---
title: ChatGPT 背后的经济账
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2652983226&idx=1&sn=034e3e8ecd53394c0eb980c9c0a31a48&chksm=7e54320c4923bb1a3d7a0c90883e415aada2289889c837ccd73cf34124f8830c7e7ee6b13f61&scene=58&subscene=0#rd
source: 极客公园
date: 2023-02-20
fetch_date: 2025-10-04T07:33:43.166928
---

# ChatGPT 背后的经济账

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEvStXuWGIVU5pQ7mEkfcJHHHib51bopwGSo2Oojkpyr0ANJxZ2snXFuA/0?wx_fmt=jpeg)

# ChatGPT 背后的经济账

Sunyan

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEoamSod7p6iasCTmqB0yUS9url62d31zicb4dOwDaph6jeNyy8ZbYugPw/640?wx_fmt=jpeg)

拿投资和赚钱之前，要先去了解下成本。

来源：OneFlow

原文地址：https://sunyan.substack.com/p/the-economics-of-large-language-models

作者：Sunyan

翻译：杨婷、徐佳渝、贾川

原标题：ChatGPT 背后的经济账

ChatGPT 能否取代 Google、百度这样的传统搜索引擎？为什么中国不能很快做出 ChatGPT？当前，对这些问题的探讨大多囿于大型语言模型（LLM）的技术可行性，忽略或者非常粗糙地估计了实现这些目标背后的经济成本，从而造成对 LLM 的开发和应用偏离实际的误判。

本文作者从经济学切入，详细推导了类 ChatGPT 模型搜索的成本、训练 GPT-3 以及绘制 LLM 成本轨迹的通用框架，为探讨 LLM 成本结构和其未来发展提供了可贵的参考视角。

**重点概览：**

* **LLM 驱动的搜索已经在经济上可行：**粗略估计，在现有搜索成本结构的基础上，高性能 LLM 驱动搜索的成本约占当下预估广告收入/查询的 15%。
* **但经济可行并不意味着经济合理：**LLM 驱动搜索的单位经济性是有利可图的，但对于拥有超 1000 亿美元搜索收入的现有搜索引擎来说，添加此功能可能意味着超 100 亿美元的额外成本。
* **其他新兴的 LLM 驱动业务利润很高：**比如 Jasper.ai 使用 LLM 生成文案，很可能有 SaaS 服务那样的毛利率（超 75%）。
* **对于大公司而言，训练 LLM（即使是从头开始）的成本并不高：**如今，在公有云中训练 GPT-3 仅需花费约 140 万美元，即使是像 PaLM 这样最先进的模型也只需花费约 1120 万美元。
* **LLM 的成本可能会显著下降：**自 GPT-3 发布的两年半时间里，与 GPT-3 性能相当的模型的训练和推理成本下降了约 80%。
* **数据是 LLM 性能的新瓶颈：**与增加高质量训练数据集的大小相比，增加模型参数的数量能获得的边际收益越来越小。

**01**

**动机**

LLM 的惊人表现引发了人们的广泛猜想，这些猜想主要包括 LLM 可能引发的新兴商业模式和对现有模式的影响。

搜索是一个有趣的机会，2021 年，仅谷歌就从搜索相关的广告中获得了超 1000 亿美元的收入 [1]。ChatGPT（一个使用 LLM 的聊天机器人，它可以生成高质量的答案，以回答类似于搜索的查询）的「病毒性」传播已经引发了许多关于搜索领域潜在影响的思考，其中一个就是 LLM 如今的经济可行性：

* 一位声称是谷歌员工的人在 HackerNews 上表示，要想实施由 LLM 驱动的搜索，需要先将其成本降低 10 倍。
* 与此同时，微软预计将在 3 月份推出 LLM 版本的 Bing[3]，而搜索初创公司如 You.com 已经将该技术嵌入到了他们的产品之中 [4]。
* 最近，《纽约时报》报道，谷歌将在今年推出带有聊天机器人功能的搜索引擎 [5]。

更广泛的问题是：**将 LLM 纳入当前产品和新产品的经济可行性如何？**在本文中，我们梳理了当今 LLM 的成本结构，并分析其未来可能的发展趋势。

**02**

**重温 LLM 工作原理**

尽管后续章节的技术性更强，但这篇文章对机器学习熟悉程度不做要求，即使不熟悉这方面内容的人也可以放心阅读。为了说明 LLM 的特殊之处，现做一个简要复习。

语言模型在给定上下文的情况下，对可能输出的 token 作出预测：

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEvqdQWF1fiaG9OEkDaHtibsglEqUeXqgFze6IA8955lmicwickBolELyo5A/640?wx_fmt=jpeg)

自回归语言模型（Autoregressive Language Model）输入上下文和输出内容的图示（在实践中，token 通常是子词：即「happy」可能被分解为两个 token，例如「hap」、「-py」）

为了生成文本，语言模型根据输出 token 的概率重复采样新 token。例如，在像 ChatGPT 这样的服务中，模型从一个初始 prompt 开始，该 prompt 将用户的查询作为上下文，并生成 token 来构建响应（response）。新 token 生成后，会被附加到上下文窗口以提示下一次迭代。

语言模型已经存在了几十年。当下 LLM 性能的背后是数十亿参数的高效深度神经网络（DNN）驱动。参数是用于训练和预测的矩阵权重，浮点运算（FLOPS）的数值通常与参数数量（parameter count）成比例。这些运算是在针对矩阵运算优化的处理器上计算的，例如 GPU、TPU 和其他专用芯片。

**随着 LLM 参数量呈指数增长，这些操作需要更多的计算资源，这是导致 LLM 成本增加的潜在原因。**

**03**

**LLM 驱动搜索的成本**

本节，我们将估算运行 LLM 驱动搜索引擎的成本。应该如何实施这样的搜索引擎仍是一个活跃的研究领域，我们这里主要考虑两种方法来评估提供此类服务的成本范围：

1、ChatGPT Equivalent：一个在庞大训练数据集上训练的 LLM，它会将训练期间的知识存储到模型参数中。在推理过程中（使用模型生成输出），LLM 无法访问外部知识 [6]。

这种方法有如下两大缺点：

* 容易「幻想」事实。
* 模型知识滞后，仅包含最后训练日期之前的可用信息。

2、2-Stage Search Summarizer：一种架构上类似的 LLM，可以在推理时访问 Google 或 Bing 等传统搜索引擎。在这种方法的第一阶段，我们通过搜索引擎运行查询以检索前 K 个结果。在第二阶段，通过 LLM 运行每个结果以生成 K 个响应，该模型再将得分最高的响应返回给用户 [7]。

相比 ChatGPT Equivalent，这种方法的优点是：

* 能够从检索到的搜索结果中引用其来源。
* 能获取最新信息。

然而，对于相同参数数量的 LLM，这种方法需要更高的计算成本。使用这种方法的成本也增加了搜索引擎的现有成本，因为我们在现有搜索引擎的结果上增加了 LLM。

**一阶近似：基础模型 API**

最直接的成本估算方法是参考市场上现有基础模型 API 的标价，这些服务的定价包括成本的溢价部分，这部分是供应商的利润来源。一个代表性的服务是 OpenAI，它提供基于 LLM 的文本生成服务。

OpenAI 的 Davinci API 由 GPT-3 的 1750 亿参数版本提供支持，与支持 ChatGPT 的 GPT-3.5 模型具有相同的参数数量 [8]。现在用该模型进行推理的价格约为 0.02 美元/750 个单词（0.02 美元/1000 个 token，其中 1000token 约等于 750 个单词）；用于计算定价的单词总数包括输入和输出 [9]。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEZRBVuqSlkX895p0pTe5Eia44ZEyuMSwuhUbxCrqXrfnsaiba3nZ6CLWg/640?wx_fmt=jpeg)

按模型功能划分的基础模型 API 定价 (OpenAI)

我们这里做了一些简单假设来估计将支付给 OpenAI 的搜索服务费用：

1、在 ChatGPT equivalent 的实现中，我们假设该服务平均针对 50 字的 prompt 生成 400 字的响应。为了产生更高质量的结果，我们还假设模型对每个查询采样 5 个响应，从中选择最佳响应。因此：

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEWJTLOhzBBdFpbb960slAOicKnjicngpNAicbyFHeDRSonUEBE90onhOOw/640?wx_fmt=jpeg)

在 2-Stage Search Summarizer 的实现中，响应生成过程是相似的。然而：

* 提示明显更长，因为它同时包含查询和搜索结果中的相关部分
* 为每 K 个搜索结果生成一个单独的 LLM 响应

2、假设 K = 10 并且搜索结果中的每个相关部分平均为 1000 个单词：

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEmXjThiawhI8AMRkMib1tNgFm11TYfh1JKLCMPFl6dJZnicLAPCtfwRPeg/640?wx_fmt=jpeg)

3、假设优化的缓存命中率为 30%（谷歌历史搜索缓存命中率的下限 [10]）和 OpenAI 云服务的毛利率为 75%（与典型的 SaaS 服务一致），我们的一阶估计意味着：

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEFw7T2iaf2TjCiaZEOjBlxbiaq2dMRzFLibgoNZiaXSdTCgFHodRVLKk9iaSw/640?wx_fmt=jpeg)

按照数量级，ChatGPT Equivalent 服务的预计云计算成本为 0.010 美元/次，与公众评论一致：

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEAYibsaia7dTtnOlicbV34ibfZXH39qehVicZnBRCwWMNwur0b9a51ibfXSqw/640?wx_fmt=jpeg)

OpenAI 首席执行官 Sam Altman 谈 ChatGPT 每次聊天的成本[推特]

(https://twitter.com/sama/status/1599671496636780546?lang=en）

鉴于 ChatGPT Equivalent 的上述缺点（即幻想事实、模型信息陈旧），在实际操作中，LLM 驱动搜索引擎的开发者更可能部署 2-Stage Search Summarizer 变体。

2012 年，谷歌搜索主管表示，其搜索引擎每月处理的搜索次数达 1000 亿次 [11]。世界银行数据显示：全球互联网普及率已从 2012 年的 34% 上升到了 2020 年的 60%[12]。假设搜索量按比例增长，则预计其年均搜索量将达 2.1 万亿次，与搜索相关的收入将达约 1000 亿美元 [13]，平均每次搜索的收入为 0.048 美元。

换句话说，2-Stage Search Summarizer 的查询成本为 0.066 美元/次，约为每次查询收入 0.048 美元的 1.4 倍。

* 通过以下优化，预估成本大约会降至原来的 1/4：1、量化（使用较低精度的数据类型）；2、知识蒸馏（通过学习较大的模型去训练一个较小的模型）；3、训练更小的「计算优化」模型，该模型具有相同的性能（稍后将对此展开更详细的讨论）

* 假设云计算的毛利率约为 50%，与依赖云服务提供商相比，运行自建（内部）基础设施（infrastructure in-house）会使成本降低至当前的 1/2。

综合以上改进，降低至原有成本的 1/8 之后，在搜索中融入高性能 LLM 的成本大约占据当前查询收入的 15%（现有的基础设施成本除外）。（注：成本最低可降至 0.066 美元/次 \* 1/4 \* 1/2，约定于 0.008 美元，因此大约占每次查询收入 0.048 美元的 15%）

**深度解析：云计算成本**

如今，SOTA 大型语言模型通常会用到可比较的模型架构（最常见的是仅包含解码器的 Transformer 模型），在推理过程中每个 token 的计算成本（以 FLOPs 为指标）约为 2N，其中 N 为模型参数数量（model parameter count）[14]。

目前，NVIDIA A100 是 AWS 最具成本效益的 GPU 选择，若预定 1 年使用该 GPU，拥有 8 个 A100 的 AWS P4 实例的有效时薪（effective hourly rate）将达 19.22 美元。[15] 每个 A100 提供峰值 312 TFLOPS（万亿次浮点数/秒）FP16/FP32 混合精度吞吐量，这是 LLM 训练和推理的关键指标 [16]。FP16/FP32 混合精度是指以 16 位格式（FP16）执行操作，而以 32 位格式（FP32）存储信息。由于 FP16 的开销较低，混合精度不仅支持更高的 FLOPS 吞吐量，而且保持精确结果所需的数值稳定性也会保持不变 [17]。

假设模型的 FLOPS 利用率为 21.3%，与训练期间的 GPT-3 保持一致（虽然最近越来越多的模型效率得以提升，但其 FLOPS 利用率对于低延迟推理而言仍充满挑战）[18]。因此，对于像 GPT-3 这样拥有 1750 亿参数的模型：

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKE2rycEt9sQURrPVrHwS2OTafL9VZBb5mNyH9rU4VJmAp77g3jdw79ZA/640?wx_fmt=jpeg)

我们也应用了基于 GCP TPU v4 定价（GCP TPU v4 pricing）相同的计算方法，并得到了相似的结果 [19]：

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEAuBDTViaQIesG6WJnzFBU8F8hCV0kVvxYugo8FKlKy0DocDfqqozhpg/640?wx_fmt=jpeg)

预估 GPT-3 通过云服务提供商 (AWS, GCP）每处理 1000 个 token 所需的推理成本

OpenAI 的 API 定价为 0.02 美元/1000 词，但我们估计其成本约为 0.0035 美元/1000 词，占定价的 20% 左右。这就意味着：**对于一台一直运行的机器而言，其毛利率约为 80%。**这一估算与我们之前设想的 75% 毛利率大致相同，进而为 ChatGPT Equivalent 和 2-Stage Search Summarizer 搜索成本估算提供了合理性验证（sanity check）。

**04**

**训练成本如何？**

另一个热门话题是 GPT-3（拥有 1750 亿参数）或最新的 LLM（如拥有 2800 亿参数的 Gopher 和拥有 5400 亿参数的 PaLM）的训练成本。基于参数数量和 token 数量，我们构建了一个用于估算计算成本的框架，虽然稍作修改，但同样适用于此：

* 每个 token 的训练成本通常约为 6N（而推理成本约为 2N），其中 N 是 LLM 的参数数量 [20]
* 假设在训练过程中，模型的 FLOPS 利用率为 46.2%（而在之前的推理过程中，模型的 FLOPS 利用率约为 21.3%），与在 TPU v4 芯片上进行训练的 PaLM 模型（拥有 5400 亿参数）一致 [21]。

1750 亿参数模型的 GPT-3 是在 3000 亿 token 上进行训练的。谷歌使用了 GCP TPU v4 芯片来训练 PaLM 模型，若我们现在也像谷歌那样做，那么如今的训练成本仅为 140 万美元左右。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEetLuTexu89eesYHrOQY9dQ1O8EJbR9tssosScNLDxoic8CB4GFGqsicA/640?wx_fmt=jpeg)

此外，我们还将该框架应用到一些更大的 LLM 模型中，以了解其训练成本。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEfp6lgjjEJwV2pOhg5sROjx7kCbmbvZhkZCwRB8IiasKweeJIYffn8iaA/640?wx_fmt=jpeg)

预估 LLM 在 GCP TPU v4 芯片上的训练成本

**05**

**绘制成本轨迹**

**的通用框架**

为了推导 LLM 的推理成本/训练成本，我们总结了如下框架：

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEkvchLNQ73ibpBiaZ1hDgD3qWZ3B1mSkNbLJ6yX2UTCPF1anF3ibQZlJpA/640?wx_fmt=jpeg)

密集激活纯解码器 LLM 模型 Transformer（Densely Activated Decoder-Only Transformer LLMs）的推理成本和训练成本（其中「N」是模型参数数量，「processor」是指 TPU、GPU 或其他张量处理加速器）

因此，我们假设 LLM 的架构相似，那么推理成本和训练成本将根据上述变量的变化而变化。虽然我们会详细考虑每个变量，但是以下部分才是关键点：

自 2020 年 GPT-3 发布以来，使用与 GPT-3 一样强大的模型进行训练和推理的成本大大降低，低于先前的五分之一。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZSyS8bTFP3F7rgKMkmcaKEOew7kRCbBib0Bkibu0vJG1bk4icQkqBydXlhxcQasRlUblmyF1HuwK4qw/640?wx_fmt=jpeg)

相比 2020 年推出的 GPT-3，与其性能对等的模型的推理与训练成本降低情况总结

**参数数量效率：巨型语言模型参数每年增长 10 ...