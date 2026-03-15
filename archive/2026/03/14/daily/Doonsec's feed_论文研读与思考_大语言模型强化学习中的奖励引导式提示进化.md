---
title: 论文研读与思考|大语言模型强化学习中的奖励引导式提示进化
url: https://mp.weixin.qq.com/s/hysVPt5Nzs3tmNc4AkVg0Q
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:27:12.124036
---

# 论文研读与思考|大语言模型强化学习中的奖励引导式提示进化

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/q6TQOF8qUIyZH3n2mtpMRx3Ztg41knqQFlr7bN1Ozj1Yr66RWU4fibPVA4PIRD3S2hGjp9BTBZaRg1Y0YomgyTUGDVMTwMV7OdH06CHaZh48/0?wx_fmt=jpeg)

# 论文研读与思考|大语言模型强化学习中的奖励引导式提示进化

Liu
Liu

玄枢战队-Arcane Hub

![]()

在小说阅读器中沉浸阅读

#### 原文标题：Reward-Guided Prompt Evolving in Reinforcement Learning for LLMs

#### 原文作者：Ziyu Ye；Rishabh Agarwal；Tianqi Liu；Rishabh Joshi；Sercan O. Arık；Dong Wang；Hamed Zamani；Jiawei Han

#### 论文链接：https://openreview.net/pdf?id=CQp36039EM

#### 会议：International Conference on Machine Learning

#### 一，主要研究问题和方案

##### 1.1 核心研究问题

    现有的用于大型语言模型的强化学习(RL)方法依赖于静态提示集，其中提示是先验的，并在固定的训练时间表中进行采样，而不管它们对RL过程是否有用。长期存在的人工智能必须应对不断演化、开放式的世界，然而当前的训练范式局限于相当短期和静态的方式。

面对上述问题文章主要研究两个问题：

（1）(信号)在RL训练期间应优先考虑哪些提示？

（2）(算法)我们如何生成更有用的提示，并用它们让LLM在RL中持续自我改进？

    为解决上述问题，文章提出了eva(通过非对称自对弈进行演化)框架。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIyDmawqK6ExrSPTkBKu1UIyymSbBOwR7G4GYUNvx9ZsRXt0FxcDsa0ul0nlp1Sc05Zv06icdNcxnAu4ZuGrD8mJTrEfhBuib1kjY/640?wx_fmt=png&from=appmsg)

图1 (左)eva 通过在训练中引入创作者策略，将经典的 LLM 强化学习推广为开放式强化学习。(右)创作者通过一个简单的"估计-采样-演化"流程，在每个小批量梯度更新后或每次完整数据集迭代后生成新提示，从而策略性地控制提示分布。其中，每个提示的有用性通过奖励信号进行估计。随后，求解者在原始提示和演化后提示的混合集上进行训练。

##### 1.2 研究方案

    eva(Evolving via Asymmetric Self-Play)框架，实现：

* **自适应提示演化**：动态生成并优先选择对当前训练状态最有用的提示，提升训练效率。
* **持续自我改进**：突破静态提示集限制，使模型能学习新知识并增强在目标分布上的鲁棒性。
* **最小化最大遗憾(Minimax Regret)**：通过博弈论设计，确保模型在各类提示分布下的最坏-case性能最优。

##### 1.2.1 初步研究

    经典的 RL 后训练解决静态提示数据集 D 的正则化优化问题：

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxLj39MicO6gfoEHtMC94u9GNTFTqxGcPH7ibISTAq3AOj63KARDicyiaaYQicJLltljzO5t2ibEmHib0R2d3dezytKX6wThxJCnAYxaU/640?wx_fmt=png&from=appmsg)

    这里，π\_base(·|x) 是基础策略，x 和 y 是提示和响应，D 是散度度量。为了近似对 y 的期望，文章采用蒙特卡洛采样，为每个提示生成 k 个响应，即 y(1), . . . , y(k) ~ πθ(· | x)。在本文中，r(·) 是奖励函数，假设来自一个固定的 oracle 奖励函数 r\*(·)；文章使用传统术语 RLHF 与 RL（后）训练互换，并在实验中关注人类偏好优化，即 AI 对齐。尽管如此，该流程与任何其他奖励类型兼容。

    传统上，提示 x 在训练中要么按顺序调度，要么通过独立同分布均匀采样。先前的工作探索了主动选择或优先采样，但仅关注现有数据。相比之下，eva 引入了新的提示创建，使得训练能够超越初始静态提示集，获得改进的覆盖范围和复杂性。

    根据 y 的生成和标注方式，RL 后训练方法可以分为：(i) 在线在策略方法，其中 y 是在策略生成的；(ii) 离线方法，其中 y 是由现有模型检查点预生成的。在本文中，对于在线 RLHF，文章在每个小批量中演化提示；而对于离线 RLHF，文章在对前一提示集完成一次完整迭代后构建一个新的提示集。

##### 1.2.2 开放式 RLHF

**问题 1(开放式 RLHF)** 我们将开放式 RLHF 问题定义为同时对提示策略(创作者 πϕ(x))和响应策略(求解者 πθ(y | x))进行双层优化：

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzKyhU8mYfnXnrblhEw05BEibJRcytgIfXTU0cfAib92gTIF06sxwNACWZJlKMej87sk3P46TkTT8GR8b3vZQIZDudgE5hb3ys90/640?wx_fmt=png&from=appmsg)

其中，π*true 是(可能未知的)真实目标提示分布，D 是一个可选的人工产物参数，R(·) 是对创作者策略 πϕ 的正则化函数，我们将在第 3 节详细讨论。该问题概括了经典的 RLHF，并包含了双重目标：(i) 回应对齐：求解者应在训练提示分布上表现良好，同时保持接近 π*base；(ii) 提示生成：创作者应生成能让求解者在目标提示分布上表现稳健的训练提示。

    经典的 RLHF，如第1.2.1节所述，从静态集合 D 中采样提示，这可能导致提示的覆盖范围和复杂性有限，并且可能与开放世界中的真实场景脱节。在问题 1 中，文章引入了一个提示生成策略 πϕ(·)，使其与响应生成策略 πθ(·|x) 一起优化。一个可优化的 πϕ(·) 带来了几个好处：(i) 在训练期间，它允许动态调整训练提示，从而可以优先考虑对当前 πθ(·|x) 更具信息量的提示，提高学习效率；(ii) 在收敛时，它会带来一个超越初始静态集合的新提示分布，使得 πθ(·|x) 能够学习到 D 之外的知识，并在目标分布上表现得更稳健。创作者的目标 R(·) 描述了 πϕ(·) 的优化过程，防止其坍缩到琐碎的提示，并引导其走向真实的目标提示，文章将在下一节中讨论如何实现遗憾最大化。

##### 1.2.3 博弈：最小化最大遗憾博弈

    问题 1 可以被构造为一个由两个策略性参与者优化各自效用的序贯博弈：

* **求解者 πθ(y | x)**：根据给定的训练提示，生成优化对齐效果的响应。
* **创作者 πϕ(x)**：生成训练提示，目的是让求解者在现实世界中表现良好，并且创作者知道求解者会针对它生成的提示进行优化。

    创作者的一个自然目标是提高求解者在真实目标提示分布 π*true 上的迁移性能：πϕ 越接近 π*true，求解者的预期表现就越好，从而创作者可能获得的效用就越高。如果 π*true 已知，那么 R(·) 可以通过与 π*true 进行分布匹配的 f-散度度量来实现。本文考虑的是 π\_true 先验未知的情况；此时的优化问题就落入了一个标准的无知情况下的决策问题。可以考虑几种决策规则，例如随机化规则，即均匀选择训练提示分布；在本文中，研究**最小化最大遗憾规则**，该规则寻找一个训练分布，使得求解者在所有可能分布上的最坏情况遗憾最小化。这里我们借用符号 r 来表示带有 KL 惩罚项的奖励，并将**遗憾**定义为 πθ 与最优策略 πθ\* 之间的奖励差异：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIzd2f5wZliahcuTQPjTrWeEsPanTYUDuhgPP4Lnfnr5f3V8UVMBKia3PkFElvHfeZnOyLR8Fh5aQVUbPaqibFBycOiaYYnKaCjQ7j0/640?wx_fmt=png&from=appmsg)

于是问题 1 被重新表述为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIy0yFlc67UCRAnico7rQyqXMPbw0qcnW4NK1by24VT1tjIY2bh9KaibJSCdHdj9tdVGz6R4zkJwUfkwZ2JddCX3ElF5hLic59yibEE/640?wx_fmt=png&from=appmsg)

注意：(i) 对于求解者的优化，公式 4 根据定义等价于公式 2；(ii) 对于创作者的优化，当 π\_true 未知时，公式 3 近似于公式 1，并为求解者的策略提供了最坏情况下的最优保证。在温和的假设下，(局部)纳什均衡是上述优化的一个(局部)最小化最大点；在这里，在(局部)纳什均衡处，求解者遵循一个(局部)最小化最大遗憾策略，即求解者的遗憾在最坏情况下是最优的。

    该博弈的均衡寻找可以通过交替优化来解决。直观地说，这允许创建不断演化的提示分布，逐步挑战智能体以实现更好的泛化；遗憾目标通过激励智能体在所有情况下表现良好，提供最坏情况下的保证，从而确保在这种演化课程上的鲁棒性。在优化中，这产生了一个最佳平衡点，使得创作者能够为求解者创造既有挑战性又可解决的提示。

**求解者的遗憾最小化。** 任何偏好优化算法都可以作为算法 1 中求解者步骤的遗憾最小化的即插即用模块。

**创作者的遗憾最大化。** 虽然求解者通过策略优化来最小化遗憾是直接的，但真正的最优策略在优化过程中仍然是未知的，当将它用作激励创作者的效用时，必须对其进行近似。类似于先前工作中的启发式方法，文章为每个 x 使用基于优势的估计：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIz52G97wjoDLKmqaTSEKBGQ5Wp4BSyRJG6SiaWkN2IoibzuLHIiacialrCia1Pk36gerF5SQnsvt9Z5FMucHw7LwBhzBhzK8TdrEiaPM/640?wx_fmt=png&from=appmsg)

其中 {y\_i} 是从 πθ(· | x) 采样得到的一组响应，r(·, ·) 是奖励 oracle。基于在大量实验中观察到的一致且显著的经验提升，我们为在线 RLHF 选择 y\_baseline = avg*{y\_i} r(x, y)，为离线 RLHF 选择 y\_baseline = arg min*{y\_i} r(x, y)。随着策略的优化，这个代理估计值将更好地逼近真实的遗憾。我们将这个遗憾估计值(即负的奖励优势)称为提示 x 相对于 θ 的信息量表示如下：

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIw4zNgicGYL3icDicoKcCcbZIVTBN6axUFSkRNl3uPHIPWnavxD18icggbf6j0sjPO3PrlRaXiafZaxkOIXZRIGesJjC41SocpDg3Tw/640?wx_fmt=png&from=appmsg)

直接对遗憾进行梯度上升可能导致训练不稳定。在这项工作中，我们通过三个步骤来近似最大化遗憾的新的提示分布：

1. 估计集合中每个提示的信息量。
2. 采样一个高遗憾提示的子集。
3. 对这些高遗憾提示进行变体来生成新的提示。

    eva这种可扩展的遗憾最大化方式可以与课程强化学习(课程强化学习就是让智能体像人类一样循序渐进地学习)联系起来，后者寻找具有高遗憾水平的环境，然后在某个距离内进行编辑；或者与进化策略联系起来，后者寻找最合适的提示，然后进行变异和交叉。

##### 1.2.4 实践算法

##### eva完整算法如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIyVDz73QXAmiav2FqVqFV4LCp6piaEWzV9FTNicTliaIhiaKaVuQ6bhqyWhcqtVAUN1vhPQAaak19qbH9yODQcHmSfVvCgOCIbvaAmM/640?wx_fmt=png&from=appmsg)

**求解者步骤**：这一步是经典的偏好优化。以 DPO(直接偏好优化) 为例，对于每个提示，生成 n 个响应并标注奖励，然后取奖励最大和最小的响应来构建偏好对模型进行优化。

**创作者步骤**：简单来说，创作者找出最有用的提示，并生成它们的变体，以近似实现遗憾最大化。

**第1步:`info(·)` – 估计信息量。** 对于提示集 X\_t 中的每个 x，我们生成响应，标注奖励，并通过公式 6 估计 x 的信息量。

**第2步:`sample(·)` – 对信息子集进行加权采样。** 使用信息量指标作为权重，我们采样出一个需要被演化的信息子集 X\_t^{info}。

**第3 步:`evolve(·)` – 对高遗憾提示进行演化。** eva 方法与具体的演化方法无关，也不依赖任何特定的演化方法。使用深度演化和广度演化指令来重写提示。

#### 二，主要贡献

文章的主要贡献有两方面：

1. 信号创新：文章提出奖励优势(Reward Advantage) 作为识别RL后训练中高价值提示的信号。
2. 算法创新：文章设计了eva，这是第一种使LLM能够优先考虑并自适应创建有用提示的方法，用于持续RL训练和自我改进。

#### 三，实验设计与性能分析

##### 3.1实验设计

**数据集和模型。** 使用 UltraFeedback 作为训练数据集，其中包含多样化的高质量提示，这些提示主要是人工生成的。使用经过指令微调的 GEMMA-2-9B 作为基础模型，这是同尺寸模型中一个强大的基线。

**评估设置。** 使用：(i) AlpacaEval 2.0，通过 805 个问题评估通用指令跟随能力；(ii) MT-Bench，通过 8 个类别的 80 个难题评估多轮指令跟随能力；(iii) Arena-Hard，源自 Chatbot Arena 上的 20 万用户查询，包含涵盖 250 个主题的 500 个具有挑战性的提示。

优化算法。 通过六种具有代表性的RLHF算法来评估文章的方法：

* **在线 RLHF**：RLOO、OAIF
* **离线 RLHF**：（带参考）DPO、SPPO；（无参考）SimPO、ORPO

**奖励模型。**采用 ARMORM-8B 作为默认的人类偏好代理奖励模型

##### 3.2实验结果

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwWtpt8SDzqLEw6WwNfO6fJcUlAv5ZIL3mKRV4rsYJ8tKWa8rGvgPBdNqCd4xrXsAb6Xk9VVrpJbL3qY7abI95usG9FWdiaFIqo/640?wx_fmt=png&from=appmsg)

图2：使用一轮 eva（基于 DPO）带来的增益示意图

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwNPvQPHq2SoKK8t0BZlTHxYLREFLf2hvicOhBfBpTibbpGsqyJQs9rTf7D3zfKhEM2ZXk5ZC8Yf9t4ySGw4sV78CtRfCJXqlGwg/640?wx_fmt=png&from=appmsg)

**表 1：在线 eva 结果。** eva 取得了显著的增益，并且与使用 6 倍人工提示的默认训练效果相当。注意，eva 仅使用了 1 倍的人工提示并持续进行演化。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxSp7Pj7Kt5sT5qu8dhX4licUy6fteqgrNOiccoSVm2iaN0TnicycgfaM9RfzPb6GdeHiaguEjzarvSK2UcqZTYkTdulWbhqhLZgLj4/640?wx_fmt=png&from=appmsg)

**表 2：离线 eva 结果。** 我们在离线 RLHF 进行 1 次迭代后应用 eva。它带来了显著的增益，并且可以超越使用人工提示的训练效果

**eva 持续实现了强大的自我改进。** 如表 1 和表 2 所示，eva 在不同的优化算法上都取得了显著的性能提升，尤其是在更具挑战性和鲁棒性的 Arena-Hard 基准测试上。例如，eva 在离线设置下为 DPO 带来了 10.6% 的提升，在线设置下为 RLOO 带来了 9.8% 的提升，超越了 Arena-Hard 排行榜上报告的 claude-3-opus-240229，并与 gemini-1.5-pro 持平，同时完全采用自适应的全自动提示-响应联合生成。这证明了 eva 优越的实证性能。**eva 的课程可以超越人工设计的提示。**

    文章进一步证明，eva 模型能够匹配甚至超越那些在 UltraFeedback 额外新提示上训练的模型，同时效率更高。在 MT-Bench 上，使用新的人工提示训练通常在第一轮表现出性能下降，仅在第二轮有适度提升，而 eva 则显著增强了第二轮的增益。

#### 四，论文的局限性与未来方向

##### 4.1论文的局限性

    eva 依赖于由奖励信号引导的自我探索。如果这些信号不准确或存在偏差，训练出的智能体可能会表现出不良行为，例如强化偏见或产生幻觉。减轻这些风险需要对稳健的奖励模型、透明的评估协议、AI 研究社区内的开放协作等进行持续研究。

##### 4.2未来方向

    eva 为 RL 后训练定义了一个新范式，开辟了许多新的研究方向，例如：(i) 将奖励模型的优化与 eva 联合起来——文章假设了一个固定的奖励模型，这是工业界的实际做法；然而，随着策略的更新，eva 可能生成分布外的提示，这就需要持续进行奖励模型训练；(ii) 扩展到可微分的创作者策略；(iii) 扩展到推理任务；(iv) 将博弈扩展到更多模态，或更多参与者。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/lmfaAJ5WqA1sUVs3bkh8pbJC...