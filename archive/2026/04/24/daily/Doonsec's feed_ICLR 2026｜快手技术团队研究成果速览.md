---
title: ICLR 2026｜快手技术团队研究成果速览
url: https://mp.weixin.qq.com/s/BgJKfUd3ZpOMNYPxLeJhRA
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:30:50.616409
---

# ICLR 2026｜快手技术团队研究成果速览

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1Vx6dDk2ypkcKs6OodbwrzTvh1UTTxvZG790IicJhpWkCg5urBeLmeRcyBE6Ce020J2kh2z006arp2VYiacPSOK2MJas5hEp90Ao/0?wx_fmt=jpeg)

# ICLR 2026｜快手技术团队研究成果速览

原创

快手技术
快手技术

快手技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

在ICLR 2026国际顶级学术会议上，快手技术团队多篇论文成功入选，研究覆盖多模态大模型、因果归因机制、生成式推荐系统、跨模态检索及扩散模型代码生成等AI前沿方向。本文通过对论文核心思路的梳理与解读，期望为各位同学带来启发与借鉴。

ICLR（The International Conference on Learning Representations）是深度学习领域最具影响力的顶级国际学术会议之一，同时也是中国计算机学会（CCF）推荐的A类会议。ICLR 2026于4月23日至4月27日在巴西里约热内卢举办。本届会议共收到近19,525篇有效论文投稿，创历史新高，最终录用约5,355篇，整体录用率约为27.4%。

01

ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization

* 论文地址：https://openreview.net/pdf?id=3r68a6GOpg
* 项目地址：https://github.com/logwhistle/ALM-MTA

* 论文简介：在社交平台上，“消费驱动生产”（CDP）旨在为构建创作者生态和优化资源利用提供可解释的激励信号，而这一目标的实现高度依赖于归因分析。然而，在大规模复杂的推荐系统中，由于缺乏精确标签以及存在未观测到的混淆因子，仅依靠后门调整（backdoor adjustment）已无法满足可靠归因的需求。针对上述挑战，我们提出了基于对抗学习中介的多触点归因模型（ALM-MTA）。这是一个可扩展的因果推断框架，利用对抗学习生成的中介变量（mediator）来实现前门准则（front-door identification）。该中介变量作为一个代理，旨在提炼结果信息，从而增强从干预（treatment）到结果（outcome）的因果路径，并消除捷径泄漏（shortcut leakage）。此外，我们引入了对比学习模块，将前门概率的边缘化计算约束在高度匹配的“消费-投稿”样本对上，从而有效解决了大规模干预空间中的正值性（positivity）假设违背问题。为了在非随机对照试验（non-RCT）日志中评估因果效应，我们设计了一套非个性化的分桶评估协议，通过估计分组增益（uplift）并计算干预簇层面的AUUC指标来进行验证。最后，我们在一个拥有4亿日活用户（DAU）和300亿样本量的真实推荐系统中对ALM-MTA进行了评估。实验结果显示，ALM-MTA带来了0.04%的DAU增长和0.6%的日活创作者增长，同时单位曝光效率提升了670%。在因果效用方面，ALM-MTA在所有倾向分桶（propensity bucket）中的分组AUUC均优于当前最先进方法（SOTA），最大增益达0.070。在准确性方面，ALM-MTA的投稿预测AUC较SOTA提升了40%。这些结果表明，结合对抗性中介学习的前门去混淆方法，能够为创作者生态优化提供准确、个性化且高效的归因方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1ViaP0rjcuICKhCED5kePIB7q1f8icPg5hMUabRib7ugaiarfFbzHiaHxbicBJ0siaf5YHVyqIF9Tn9BTg97vTH8s1mahtWibJ2rEaQJ50/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1Xl6vzibj69riaKAxGiaZOTH2UoIO4yGKucTMCFpVMfxibAe8aDn4HLogAM8Tp98SFaD50FuQ1Eyibd1wJjicrMrTC12DobLF8tPn0pk/640?wx_fmt=png&from=appmsg)

02

Beyond Text-Only: Towards Multimodal Table Retrieval in Open-World

* 论文地址：https://openreview.net/forum?id=4QPgqdQmYn

* 论文简介：开放域表格检索旨在根据自然语言查询，从大规模语料库中检索出语义相关的结构化表格。与非结构化文本不同，表格不仅通过文本或数值内容存储信息，还通过其结构属性存储信息，包括表头与单元格之间的层级关系，以及表格布局中的复杂空间排列。现有方法主要将表格检索视为文本检索的变体。这些方法在文本序列化过程中难以准确保留多样化表格格式的丰富结构语义。现有技术通常通过行序列化或列序列化将表格扁平化为线性文本序列，无意间丢弃了结构信息。当处理包含合并单元格或不规则对齐的复杂表格布局时，该问题尤为突出，最终导致检索性能下降。此外，现有方法难以处理表格单元格内的嵌入图像。值得注意的是，视觉表示在保持结构与内容信息的同时具有格式无关性。这一洞见促使我们探索基于图像的表格检索，该方法能自然克服现有技术的局限。本文提出TaR-ViR（基于视觉表示的表格检索）新基准，通过将表格视为图像，将表格检索重新定义为多模态任务。针对TaR-ViR的实验表明，这种范式转变实现了更高效的检索性能。关键在于它消除了易出错的文本转换需求，从而实现了开放世界表的可扩展收集与利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1gVUsotpT1UzVbM4rUD6s5Zvcw8WG2eYULws2ibd8ZVEH567yncCrPtYYTSzibUz6XmBib7ia1EPvibXrMVO7KKTBfHBL5ejuJQ16lc00M53SUe8/640?wx_fmt=png&from=appmsg)

03

Denoising Neural Reranker for Recommender Systems

* 论文地址：https://openreview.net/pdf?id=JlwYkFm91F

* 论文简介：工业界的多阶段推荐系统中，用户请求首先会触发一个召回模块（Retriever），用于筛选并排序出一系列相关的物品；随后，会调用一个更精密的重排模型（Reranker），对最终展示给用户的物品列表进行精细化调整。这种“召回-重排”两阶段框架中，核心问题是跨阶段的联合优化。现有研究大多集中在开发“重排感知型召回器”（Reranker-aware Retrievers）上。相比之下，关于如何实现“召回感知型重排器”（Retriever-aware Reranker）的工作却非常有限。

  在本研究中，我们提供证据表明：前序阶段的召回分数是极具信息量的信号，但目前尚未在重排阶段得到充分挖掘。为此，本工作深入分析了两个阶段的打分行为规律，通过实证展示了在两阶段框架下的重排任务本质上是一个针对召回分数的噪声消除（Noise Reduction）问题，并从理论上阐述了传统的直接使用召回分数的朴素方法所存在的局限性。基于这一认知，我们推导出DNR（Denoising Neural Reranker）重排学习框架，该框架将去噪重排器（Denoising Reranker）与一个精心设计的噪声生成模块相结合，将传统的评分误差最小化损失函数解构为三个子目标：样本增强的召回分数去噪、对抗性样本探索、召回分数生成分布对齐。

  我们在三个公开数据集和一个工业级推荐系统上进行了广泛的实验，并结合理论分析验证了所提DNR方案相比于朴素利用策略及领先重排模型的有效性。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1WIb9I65M0aQU5EX2iaUOMkvGDVWFliciaic9tmCQiayybiba4lEPxiaqryXOiaQaQ78IJvkcEgKecymJbibOaGC3YBPW3XLAubJaA95qko/640?wx_fmt=png&from=appmsg)

04

DIVA-GRPO: Enhancing Multimodal Reasoning through Difficulty-Adaptive Variant Advantage

* 论文地址：https://openreview.net/pdf?id=qKXYEg00eH

* 论文简介：基于群体相对策略优化（GRPO）的强化学习已成为增强多模态大语言模型推理能力的广泛应用方法。尽管GRPO无需传统评论家模型即可实现长链推理，但其常面临两大挑战：一是稀疏奖励问题，源于困难问题中正向反馈的稀缺性；二是优势值消失现象，当问题过易或过难时群体层面奖励呈现高度一致性。现有解决方案可分为三类：样本增强与扩展、选择性样本利用、间接奖励设计。然而这些方法都忽视了一个根本性问题：对于特定问题，如何确保组内响应奖励分布具有足够差异性，从而为每个响应提供清晰的优化信号？

  为解决上述问题，我们提出DIVA-GRPO——一种难度自适应的变体增强优势计算方法。该方法从全局视角动态调整每个问题的变体难度分布：先动态评估问题难度，采样适当难度层级的变体，随后在局部（单问题）与全局（问题及其变体）双重分组中，采用难度加权归一化缩放计算优势值。该设计能缓解奖励稀疏性与优势值消失问题，最大限度减少数据浪费并提升训练稳定性。在六大推理基准测试上的大量实验表明，DIVA-GRPO在训练效率和推理性能上均优于现有方法。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1VxgHK9IlFyFAbVz1ORZWhsicX0ia4BdvVgfAgAxjYtu8Md4doyWZiaUw8hJBxx7bia3pNPdhsCQa0p260OtMNd2VqYh9qJm8kCL34/640?wx_fmt=png&from=appmsg)

05

DreamOn: Diffusion Language Models For Code Infilling Beyond Fixed-size Canvas

* 论文地址：https://arxiv.org/pdf/2602.01326

* 项目地址：https://github.com/DreamLM/DreamOn

* 论文简介：扩散语言模型（Diffusion Language Models, DLMs）为自回归模型提供了一种极具吸引力的替代方案，能够以灵活的方式实现任意顺序的代码填充，且无需专门的提示设计。然而，其实际应用面临一个关键限制：生成过程需要固定长度的掩码序列。当预定义的掩码长度与理想补全长度不匹配时，这一约束会严重降低代码填充的性能。为解决这一问题，我们提出了 DreamOn——一种支持动态、可变长度生成的新型扩散框架。DreamOn在扩散过程中引入了两种长度控制状态，使模型能够仅基于自身预测自主扩展或收缩输出长度。我们将该机制集成到现有DLMs中，仅需对训练目标进行最小化修改，且无需任何架构调整。基于Dream-Coder-7B构建的DreamOn，在HumanEval-Infilling和SantaCoder-FIM基准测试中实现了与当前最先进自回归模型相当的填充性能，并达到了使用真实长度（oracle）时的性能水平。我们的工作消除了DLMs实际部署的根本性障碍，显著提升了其在可变长度生成任务中的灵活性与适用性。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1XhRiaJ9iaLIIcg9v83gtUFDC3nYxgvmjXHmf9lFbciaKaqyggQkcRft1la1dHRasr7OCQ9gGicgP6vP7xnwTGyHH6H59JDC1O988o/640?wx_fmt=png&from=appmsg)

06

Evaluating Text Creativity Across Diverse Domains: A Dataset and Large Language Model Evaluator

* 论文地址：https://arxiv.org/pdf/2505.19236

* 论文简介：创造力评估仍然是大型语言模型（LLMs）面临的一项关键挑战。现有评测方法在很大程度上依赖低效且成本高昂的人工评判，严重制约了机器创造力的进一步发展。尽管已经提出了一些自动化评估方法——包括基于心理学测评、启发式规则或提示工程的方法——但它们往往缺乏良好的泛化能力，或难以与人类判断保持一致。为了解决上述问题，我们提出了一种新的成对比较（pairwise-comparison）框架来评估文本创造力。该框架通过引入共享的上下文指令，显著提升了评估的一致性与稳定性。基于此，我们构建了CreataSet，这是一个大规模数据集，包含10万+人工标注的高质量样本以及100万+合成的创造性指令–响应对，覆盖多种开放领域的创造性任务。在CreataSet上进行训练后，我们进一步开发了一个基于LLM的创造力评估模型CrEval。实验结果表明，CrEval在与人类判断的一致性方面显著优于现有评估方法。更重要的是，实验验证了同时融合人工数据与合成数据对于训练高鲁棒性评估器具有不可或缺的作用，并展示了CrEval在实际应用中有效提升LLM创造力表现的潜力。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1VasjHhrAPBevTD68wMF7EUsvGnSwEe41m1MHaP2dnbk3WMicQj8LH2RTdFrwc7VZmqe4zcXqMicpaqsLDCreun2icSydN2YJ4JUQ/640?wx_fmt=png&from=appmsg)

07

GoR: A Unified and Extensible Generative Framework for Ordinal Regression

* 论文地址：https://openreview.net/pdf?id=ys80cc2N5M

* 论文简介：序数回归（Ordinal Regression, OR）广泛应用于年龄估计、美学评分及推荐预测，但传统的离散化（CSD）方法长期受困于边界模糊和固定分桶带来的预测僵化。本研究提出了首个通用的生成式序数回归框架GoR，打破了传统的分类/回归范式，创新性地将数值预测重新建模为自回归序列生成任务。通过预测一系列具有“加法语义”的令牌（Tokens）并由动态&lt;EOS&gt; 终止，GoR模拟了人类从粗到精的认知过程，实现了可解释的逐步细化预测，并凭借动态序列长度彻底解决了固定分桶的灵活性瓶颈。在理论层面，本文通过偏置-方差分解建立了MSE误差上界，并据此提出Coverage–Distinctiveness Index (CoDi) 指标，为平衡量化偏差与统计方差提供了科学的词表构建准则。作为一种模型无关（Model-agnostic）的通用架构，GoR在涵盖5大领域的15个权威基准测试中均刷新了SOTA纪录，证明了生成式范式在处理具有内在顺序结构的数值预测任务时，相比传统方法具有强大的理论优越性与泛化潜力。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1Un1o2tzbW4zR6aaIH2u6iaZE5PgMsrXYibobhxfjvqxWkmjl5kF6bkicQh7mxvWfFexYu2278RlMCb1ljZG7putvh7Koxb7tGHXA/640?wx_fmt=png&from=appmsg)

08

GoalRank: Group-Relative Optimization for a Large Ranking Model

* 论文地址：https://openreview.net/pdf?id=gTMzRm8fb0

* 论文简介：生成器-评估器（Generator-Evaluator, G-E）两阶段范式是目前主流的排序方法之一。具体来讲，生成器负责产生多个候选列表，接着评估器负责从中选出最佳列表进行透出。近期一些研究尝试通过使用更多更全面的生成器（MG-E）来进一步提升性能，论证了列表空间探索的复杂度和挑战性。但我们在实验观测中发现，G-E和MG-E这种两阶段生效方式随着候选列表数量或生成器数量的增加，收益会迅速达到瓶颈，与理论边际收益曲线存在差异。

  为此，本工作首先通过理论证明：一个足够大的纯生成器（Generator-only）排序模型，其对最优排序策略的近似误差，可以严格小于任何有限的G-E/MG-E系统。然后基于这一理论见解，我们提出了对应的模型优化方案GoalRank，一个训练单个强大的序列生成器的创新框架：GoalRank的核心在于引入了组相对优化（Group-Relative Optimization, GRO）原则，利用一个基于真实用户反馈训练的奖励模型，以“组相对”的方式构建参考策略。通过最小化模型策略与该参考策略之间的KL散度，GoalRank能够有效地训练大规模的纯生成器模型。

  我们在公开基准数据集和拥有超过5亿日活跃用户的真实短视频推荐平台上进行了广泛的实验。结果表明，GoalRank在离线指标和在线业务指标（如应用停留时间和观看时长）上均显著优于目前最先进的MG-E框架。

![](https://mmbiz.qpic.cn/mmbiz_png/1gVUsotpT1Uwv67qlLWvw4j9XSGOsShobdPDn1N2bpuXx3yBkVjhTLpXZudhMkFMDVSiaK6ibFVrgHZkFszAlCnyxNkSOM4eE8Zml3n9pIwps/640?wx_fmt=png&from=appmsg)

09

Mix-Ecom: Towards Mixed-Type E-Commerce Dialogues with Complex Domain Rules

* 论文地址：https...