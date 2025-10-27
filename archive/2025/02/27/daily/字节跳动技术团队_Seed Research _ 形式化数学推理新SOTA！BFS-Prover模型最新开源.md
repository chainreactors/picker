---
title: Seed Research | 形式化数学推理新SOTA！BFS-Prover模型最新开源
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247513581&idx=1&sn=443435e8f18a20f05d39633882988c08&chksm=e9d37e0fdea4f7198b3f7f5b5e25b1dcfea6beb1822275e47b2a316b47a4afe6205f6c3964dd&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2025-02-27
fetch_date: 2025-10-06T20:37:07.168363
---

# Seed Research | 形式化数学推理新SOTA！BFS-Prover模型最新开源

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOiavzicx0CR6GraziaG6sLiazHLUSPgXz88pdjdUcwn6JdGYkP2IJJic0ClLicqBc2Mhfd9bWcBOQtfgmvA/0?wx_fmt=jpeg)

# Seed Research | 形式化数学推理新SOTA！BFS-Prover模型最新开源

Seed Research

字节跳动技术团队

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuhPOK4aGeiaH4xc3K9hftIaU71lyDxgDhL6bBVPsvAOQYppS5FHQwstITiaIR6GsvryQicocJcx7BNOw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

近日，豆包大模型团队提出 BFS-Prover，一个基于大语言模型 (LLM) 和最优先树搜索 (BFS) 的高效自动形式化定理证明系统。

团队通过该成果发现，简单的 BFS 方法经过系统优化后，可在大规模定理证明任务中展现卓越性能与效率，无需复杂的蒙特卡洛树搜索和价值函数。

在数学定理证明基准 MiniF2F 测试集上，BFS-Prover 取得了 72.95% 准确率，超越此前所有方法。

自动形式化数学定理证明，是人工智能在数学推理领域的重要应用方向。此类任务需要将数学命题和证明步骤转化为计算机可验证的代码，这不仅能确保推理过程的绝对严谨性，还能构建可复用的数学知识库，为科学研究提供坚实基础。

早在上世纪中叶，戴维斯、明斯基、王浩等不少逻辑学家、数学家、人工智能先驱便已在探索相关问题。

近些年在 LLM 能力加持下，自动定理证明系统更多依赖于复杂的蒙特卡洛树搜索 (MCTS) 或价值函数 (Value Function) 来指导搜索过程。

然而，这些方法引入了额外计算成本，并增加系统复杂度，使模型在大规模推理任务中的可扩展性受限。

**字节跳动豆包大模型团队推出的 BFS-Prover 挑战了这一传统范式。**

作为一种更简单、更轻量但极具竞争力的自动定理证明系统，它引入了三项关键技术：专家迭代 (Expert Iteration) 与自适应性数据过滤、直接偏好优化 (DPO) 结合 Lean4 编译器反馈、BFS 中的长度归一化。

**从结果看，BFS-Prover 在形式化数学测试集 MiniF2F 上实现了 72.95% 的准确率，创造了新的领域记录。**

该结果也首次证明：在合理的优化策略下，简单的 BFS 方法能够超越蒙特卡洛树搜索和价值函数等主流的复杂搜索算法。

**目前，论文成果已对外公开，模型也最新开源，期待与相关研究者做更进一步交流****。**

> **BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving**
>
> **论文链接：**https://arxiv.org/abs/2502.03438
>
> **HuggingFace 链接：**https://huggingface.co/bytedance-research/BFS-Prover

##

## **1. 主流方法蒙特卡洛树搜索和价值函数真的必要么？**

在形式化数学证明领域，将抽象的数学概念转化为能够用计算机验证的严格形式，是一项极具挑战性的任务。

该过程要求每一步推理都符合严格的形式逻辑规则，且每个步骤都必须经过 Lean 证明助手验证。

在自动形式化定理证明过程中，计算机面临的核心挑战是——在庞大且高度结构化的证明空间中，找出有效路径。这一难点与传统搜索问题有本质区别，具体表现如下：

**1）搜索空间庞大：**每一步推理可能有数十甚至上百种可能的策略选择；

**2）动态变化的策略空间：**不同于棋类游戏的固定规则，数学定理证明中，每个状态下可应用的策略集合不断变化，且规模庞大，无明确界限；

**3）反馈稀疏与延迟：**直到完成证明前，系统很难获得有效的中间反馈；

**4）开放式推理过程：**缺乏明确的终止条件，证明尝试可能无限延续；

自动定理证明系统如 DeepSeek-Prover-V1.5、InternLM2.5-StepProver，主要依赖复杂的蒙特卡洛树搜索和价值函数解决上述问题。

这些类 AlphaZero 算法框架在游戏中表现出色，尤其在围棋领域大放异彩，推动了强化学习概念破圈。但在自动定理证明领域，由于状态空间极其复杂以及缺乏明确的过程奖励信号，上述主流方法效果并不理想。此外，复杂的搜索算法还带来了计算成本高、系统复杂度增加等问题。

## **2. 化繁为简，用机器证明数学定理可以更简单**

人类遇到问题，往往优先采用最可能解决的方法。最优先树搜索（BFS）与之类似。

这是一种在“树”或“图”中搜索节点的算法。核心思想是根据某种启发式函数，评估每个节点优先级，按优先级访问节点，常用于解决约束满足问题和组合优化问题，特别是在需要快速找到近似最优解的情况下。

此前不少研究者认为，简单的 BFS 算法缺乏有效的探索机制，尤其是对深度路径的探索，难以胜任大规模定理证明任务，但豆包大模型团队的研究者发现了其中的突破口，并提出了 BFS-Prover 系统。

下图展示了 BFS-Prover 系统的整体架构和工作流程。

图右侧展示了训练数据生成过程，包括用于监督微调的 SFT 数据 (成功证明路径上的状态-策略对) 和用于直接偏好优化的 DPO 数据 (从同一状态出发的正确策略与错误策略的对比)。

图左侧展示了 BFS 机制，通过 LeanDojo 环境与 Lean4 交互，从根节点开始，按照优先级顺序 (1→2→3...) 探索证明路径，直到找到证明完成节点 (绿色 A 点)。

整个系统形成闭环：LLM 生成策略 → LeanDojo 执行 → 获取反馈 → 生成训练数据→优化 LLM → 再次生成策略，实现了持续改进的专家迭代机制。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuhbvK8Y6ibicJtFQE90iaHTR8kXZoUCvzetVGlKck6PlQ4LiaibxsXkPlNUdhnCwYD2WmgxptmCSjguXgw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

团队认为，BFS-Prover 系统不仅证明了经过优化的 BFS 方法性能方面可以超越复杂的蒙特卡洛树搜索和价值函数，并且能保持架构的简洁性和计算效率。其技术特征如下：

* **让模型既能深度思考策略，也能掌握最简证明方式**

BFS-Prover 采用专家迭代框架，通过多轮迭代不断增强 LLM 能力。在每轮迭代中，系统会先使用确定性的束搜索 (Beam Search) 方法过滤掉容易解决的定理，将这些“简单问题”从训练数据中剔除，再着手解决“复杂问题”。

这一数据过滤机制颇具创新性，确保了训练数据逐渐向更具挑战性的定理证明任务倾斜，使 LLM 能够学习更多元化的证明策略。

如下图实验数据显示，随迭代进行，系统能够发现证明的平均长度变长，覆盖面变广，证明了这一方法的有效性。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuhbvK8Y6ibicJtFQE90iaHTR8kfrQzIfdjNpItyyzKBJz03Fu17zDtNPLRVtglqDS7nU8OicdcuenNGgw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

与此同时，LLM 生成的策略分布也发生进化。

如下图所示，经过多轮迭代，模型生成的策略长度分布发生了显著变化：非常短的策略（1-10 个 token）比例下降，而中等长度策略（11-50 个 token）比例则有所增加。

这种分布变化表明，LLM “深度思考能力”在加强，避免了常见的强化学习导致的分布坍缩问题，并逐渐掌握了更复杂、更信息丰富的证明策略。

同时，模型生成简洁策略的能力并未摒弃。这种多样策略生成能力的保持，对于有效定理证明至关重要。因为不同的证明状态，需要不同复杂度的策略，涵盖从简单的项重写，到复杂的代数操作。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuhbvK8Y6ibicJtFQE90iaHTR8ksaPcSrZumIIiaPRJuqmx1A2oFJ6KAhOkDULYVplI9nyriaIDAtrNgiaiaA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

* **从过程中总结“错误证明步骤”，提升证明能力**

在证明搜索过程中，当 LLM 生成的某些策略导致 Lean4 编译器错误，系统将这些无效策略与成功策略配对，形成负反馈信号。

BFS-Prover 创新性地依靠这些数据，基于直接偏好优化(DPO)技术优化策略 LLM。此种方法显著提高了模型识别有效策略的能力，优化了策略分布，提高 BFS 的采样效率。

如下图实验结果，在各种计算量级下，经过 DPO 优化的模型均取得了性能提升，证明了负面信号在定理证明中的重要价值。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuhbvK8Y6ibicJtFQE90iaHTR8kWMzrm6OFHNHRpiaObPQPPs0L4AW5lebP9icjM24uED0XiaPpSRLUMA8mg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

* **避免对深度推理的打压，实现对高难度定理证明的突破**

为解决 BFS 对深度推理路径的天然打压问题，BFS-Prover 系统引入了可调节的长度归一化评分函数：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuhbvK8Y6ibicJtFQE90iaHTR8kibwIvNtv7QRN9m5VthHs2MKjXh2H98fstz7XaxuvemcSUovmBJDb7JQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

其中，L 表示路径长度，α 是可调节的长度归一化参数。通过适当调整 α 值，系统可以平衡对高概率路径的利用与对深层路径的探索，使 BFS 能够更有效地探索长链证明。

## **3. 成果取得 MiniF2F 新 SOTA**

团队在 MiniF2F 测试集上，对 BFS-Prover 进行了全面评估。该测试集是形式化数学领域公认的基准测试集，包含高难度的竞赛级数学问题，被广泛用于衡量自动定理证明系统的能力。

* **超越现有最优系统**

在与此前定理证明系统的对比中，BFS-Prover 展现出显著优势。

在固定策略生成的计算量下(2048×2×600 次推理调用)，BFS-Prover 实现了 70.83% 的准确率，超过所有现有系统，包括使用价值函数的 InternLM2.5-StepProver (65.9%) 、HunyuanProver (68.4%)，以及基于蒙特卡洛树搜索的 DeepSeek-Prover-V1.5（63.5%）。

**在累积评估中，BFS-Prover 进一步将准确率提升至 72.95%，成为了形式化定理证明领域的 SOTA。**

这一结果不仅证明了 BFS 方法的潜力，更展示了通过精心设计可以使简单算法超越复杂方法。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuhbvK8Y6ibicJtFQE90iaHTR8kZwKgKPSicXqMFWGlHPq5hI8VmYiapGkwuDsGQuiaiaAz9I7ZZwbvHl2Kicg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

* **成功证明多个 IMO 题目**

值得一提的是，BFS-Prover 成功证明了 MiniF2F-test 中的多个 IMO 问题，包括 imo\_1959\_p1，imo\_1960\_p2, imo\_1962\_p2, imo\_1964\_p2 和  imo\_1983\_p6。

这些证明展示了该系统在处理复杂数学推理方面的强大能力，涵盖数论、不等式和几何关系等。

比如，对于 imo\_1983\_p6 不等式问题，BFS-Prover 能够生成简洁而优雅的形式化证明：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuhbvK8Y6ibicJtFQE90iaHTR8kuiacaEYEfHJ4xZfY9Kgxo0W7Hia8FicnecbiaImqvZfrezdSEO7V8prWOg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

##

## **4. 写在最后**

## 团队认为，BFS-Prover 的成功，暗含了自动定理证明领域的一项重要启示：**简洁的算法结合精心设计的优化策略，同样有助于 AI4Math 边界的拓展。**

随着大语言模型能力的不断提升，BFS-Prover 开创的简洁高效路线有望进一步推动自动形式化定理证明领域发展，为数学研究提供更强大的自动化工具支持。

展望未来，团队计划进一步提升 BFS 方法在处理更复杂数学问题上的能力，特别是针对本科和研究生级别的数学定理。同时，团队也将基于推理模型和其他前沿路线，持续挖掘模型潜力。

**我们期望，通过持续优化数据和训练策略，让相关工具为数学研究提供强大辅助，加速数学发现过程，最终实现人机协作解决前沿数学挑战的愿景。**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuhPOK4aGeiaH4xc3K9hftIaUvIbIUYD96j6WzbF5CrcXHwW14icf6miaj6HpfuznuzydOfsEJjVqliaFw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuhPOK4aGeiaH4xc3K9hftIaU3MN90fRIZIY52RMj5VtLRmefmGNAlWnOvj300xc679X68eIVL399lw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuhPOK4aGeiaH4xc3K9hftIaUe00KHxMqxNzOpROicednLZoYdbvBkoVlkpbF3oEn2f995qqkriaSmKAA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuhqB3IEiaNtzltdW5KmNGtEHV4AKYT3ucmgYd36NkECbaXcU1SpmCN2kvPTYv1Zxkmr2d9Z9a2v8Xw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mp.weixin.qq.com/s?__biz=MzkzMDY5MzYxNg==&mid=2247489533&idx=1&sn=f3817426de5156f65a19af95d2360671&scene=21#wechat_redirect)[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuhbvK8Y6ibicJtFQE90iaHTR8kviasFqo89UZ4cicwVIV1VXl2pt0neqicEoS3ZjSOtCDwuUTSicVibTqPZbg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mp.weixin.qq.com/s?__biz=MzkzMDY5MzYxNg==&mid=2247486893&idx=1&sn=4f630f6374aa0e68ffb416bb75602c9a&scene=21#wechat_redirect)

****点击“阅读原文”，了解更多团队信息！****

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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