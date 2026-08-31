---
title: 团队科研成果分享-76
url: https://mp.weixin.qq.com/s/IZ7MfgZ8iYsq2sogT-Ww1Q
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:52:13.413527
---

# 团队科研成果分享-76

# 团队科研成果分享-76

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/jBQAokCLibp0tyL01YicqI83S3Jy4r992KibNL8pBSlhIvGtyPt3caW9DPW8myMAEMicCCS3IQjlybDXrz9KadB1yr9Tb6cHgkk3apMicaBftN3U/640?wx_fmt=jpeg&from=appmsg)

**团队科研成果分享**

2026.08.24-2026.08.30

**标题:**Adversarial Reinforcement Learning for Robust Multi-AUV Target Tracking against Observation Perturbations

**期刊:**IEEE Transactions on Vehicular Technology, 2026.

**作者:**Wangxu Qiu, Guangjie Han, Yu He, Shengchao Zhu.

**分享人:**河海大学——邱王煦

**01**

**研究背景**

**BACKGROUND**

**研究背景**

自主水下航行器（AUV）是海洋探索的重要平台，近年来更是以集群协同作业的模式与多智能体强化学习（MARL）广泛结合，显著增强了人类对海洋环境的干预能力。然而，在实际海洋环境中，AUV的观测易受环境噪声和传感器测量误差影响，且敌对目标可能采取水声对抗措施主动干扰感知，导致观测偏离真实值，进而使MARL策略的准确性和稳定性显著下降。现有对抗强化学习（ARL）虽通过在训练时引入扰动来提升鲁棒性，但其通常采用的端到端训练方式因奖励归因错乱引发策略训练不稳定，同时策略网络易过拟合于特定扰动模式，泛化能力有限。针对上述问题，本文提出基于对抗性预测状态的部分可观测马尔可夫决策过程（APS-POMDP）及基于对抗性预测状态的多AUV优势-注意力演员-评论家算法（APS-MA-A3C），通过将状态预测与策略优化解耦，并采用阶段训练策略，即先在无扰动下训练基础策略，再对抗训练预测网络，提升训练的稳定性并增强AUV集群对未知观测扰动的鲁棒性。

**02**

**关键技术**

**TECHNOLOGY**

**关键技术**

本文提出了一种基于状态预测的鲁棒决策框架。该框架不迫使策略网络学习根据受扰观测输出正确动作，而是将状态预测与决策解耦：先引入预测网络，通过对抗训练使其学习根据受扰观测重建真实状态，再使策略网络根据预测的状态进行决策。具体而言，本文的主要贡献如下：

1）提出基于对抗性预测状态的部分可观测马尔可夫决策过程（APS-POMDP）。APS-POMDP定义了一个依赖于观测扰动下状态预测的鲁棒决策过程，即首先从扰动观测中显式地预测状态，然后利用预测状态指导决策。它在结构上将状态预测与决策解耦，为提高AUV集群网络抵御不同形式观测扰动的鲁棒性奠定了理论基础。

2）提出基于对抗性预测状态的多AUV优势-注意力演员-评论家算法（APS-MA-A3C）。APS-MA-A3C采用阶段训练：第一阶段，在无扰动条件下训练智能体的基础策略；第二阶段，对观测施加对抗性扰动，并通过监督学习训练预测网络，使其能够根据扰动观测预测状态。在阶段训练过程中，策略优化不涉及对抗训练，状态预测训练也不依赖奖励信号，从而规避了观测扰动引发的信用分配扭曲。

3）引入真实海流和海底地形数据构建仿真环境，用于验证所提算法的目标跟踪性能。结果表明，我们的方法在不同强度、不同类型的观测扰动下，在算法有效性和鲁棒性两方面均超越了现有的鲁棒算法。

**03**

**算法介绍**

**ALGORITHMS**

**算法介绍**

**（1）观测扰动建模**

在部分可观测环境中，观测模型通常假设服从固定的条件概率分布\mathcal{Z}(o|s)。本文不考虑AUV自身运动对感知的影响，故将观测模型简化为\mathcal{Z}(o|s)。然而，对抗性扰动会引入分布外偏移，无法被固定分布模型所刻画。为此，本文将扰动显式地纳入观测模型：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3XIXH5j3EiatJ9NAObJ8rtQWhxegDG3Tk9ib0Zh2fk2FdIUvVkib6Z5eks6OZWYibUOHPr7Y2fIOm2MESicvY9uDeYQS4iamHIy5mdc/640?wx_fmt=png&from=appmsg)

其中o\_i表示标称观测，其维度与语义与状态s\_i一致，但是考虑了智能体传感器的量程和视场范围约束，代表理想无扰条件下的观测输出；\delta\_i为扰动向量，其每一维对应一类独立的测量误差，由扰动映射v\_i根据环境状态s\_i生成，即\delta\_i = v\_i(s\_i)，该映射的具体形式对AUV完全未知；f定义了扰动施加于标称观测的方式，例如加性噪声直接叠加、角度偏差通过坐标变换引入等；{\hat{o}}\_{i}为带有感知误差的实际观测。

本文假定扰动向量满足未知但有界（UBB）条件，用可行集\Delta\_i表示扰动范围，即\delta\_i \in \Delta\_i。在此基础上，本文引入对抗训练机制，在可行集\Delta\_i内搜索破坏性最强的扰动，迫使网络在最劣工况下训练，从而同时提升策略的性能下界和鲁棒性。

**（2）对抗训练过程解耦分析**

对抗训练常被建模为如下双层优化问题：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0Mibyaq8zFlzMsguc83tGBDGElibI0VRP9DACZGxcn74vpgXiaLhfOmbCXHA05aBLuymBwsq0YWwfCB5Ktibb9Y3awznwWnXvk1ico/640?wx_fmt=png&from=appmsg)

其中内层最小化通过构造最优对抗性扰动来最小化累计奖励，外层最大化则确保策略在包含最优扰动的训练条件下仍能稳定完成任务。对于内层最小化问题，已有研究表明可通过使扰动策略尽量偏离原始策略来实现。本文采用交叉熵L\_{CE}量化扰动状态与干净状态下动作分布的差异，并利用投影梯度下降（PGD）算法更新观测扰动：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1E2w9UV1ibnkQiabNn3UibNQuDVh8pVEIlfe210T5aGT7gYAWIZBKBJX1N0O6zuvBdzdxW9OnvDWN0RGeWmJP76P8WjIxCZB6rl0/640?wx_fmt=png&from=appmsg)

其中\beta为步长，a\_i为干净状态s\_i下的参考动作，\text{clip}(\cdot)将扰动约束在可行集\Delta\_i内。外层最大化的常规做法是将内层求得的最优扰动观测纳入标准训练循环，迫使策略网络在最坏情况下训练。然而这种端到端的对抗训练本质是训练策略建立从受扰观测到正确动作的直接映射。这导致策略网络容易捕捉特定扰动与动作之间的浅层关联，而非学习观测中对扰动不变的核心特征，因而对未见过的扰动泛化能力有限。另外，当观测受到对抗性扰动而无法反映真实状态时，奖励难以被准确归因到相应状态下的动作，导致信用分配紊乱，从而造成策略训练不稳定。

为解决上述问题，本文进一步推导出双层优化目标的上界关系：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2LCVlPq3d8ibiasV1Vr9WiaxTgJeReCg061eBgcXZibsHJ2DCjxibTuice4WXcDib829AuyjbPM0Coibsd4FVhrMYGQZ6G5S62HjZkY1U/640?wx_fmt=png&from=appmsg)

该不等式表明，扰动条件下AUV集群的累计奖励上界为无扰动全状态条件下最优策略的期望奖励。因此，一种可行的优化方向为：通过消除或补偿观测信号中的偏差，使受扰观测趋近真实状态，从而使实际策略性能逼近该上界。

具体而言，本文为每个AUV分配独立的门控循环单元（GRU）预测网络，利用最近L步扰动观测序列\hat{O}\_i^{(t)} = (\hat{o}\_i^{(t-L+1)}, \ldots, \hat{o}\_i^{(t)})来推断当前真实状态。每个AUV独立训练预测网络，避免了参数共享导致的分布不匹配问题。

**（3）基于对抗性预测状态的部分可观测马尔可夫决策过程（APS-POMDP）**

在部分可观测且观测受扰的场景下，标准POMDP难以准确刻画问题。为此，本文提出APS-POMDP框架，具体形式化为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1icXh1BcvSibQNwfbwCuUDgwHrico6Jic9c6Z4aWoAlmyYMjhEMjhJqAVeD4iaAVdBic21ceEyOy4bgCGNgibx2AfU84H36JznK9IGAo/640?wx_fmt=png&from=appmsg)

其中，\mathcal{S}\_i为状态空间，s\_i为真实状态；\hat{\mathcal{O}}\_i为对抗观测空间，\hat{o}\_i为对抗观测，其生成方式为\hat{o}\_i = f(o\_i, \delta\_i) = f(z(s\_i), v\_i(s\_i))，其中z为标称观测函数，v\_i为扰动映射；\tilde{\mathcal{S}}\_i为预测状态空间，\tilde{s}\_i为预测网络基于历史观测序列给出的状态估计；\mathcal{A}\_i为动作空间，\mathcal{R}\_i为奖励函数，\mathcal{P}为状态转移概率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp0vC9Yic2tbT6Qhn8K01m3ic5rc68z1s6NhBdlibfwrP4G560O7Liad6ZTxJpGAMfP1ZNdeYr1GMF8BuDxk1zsqY1su9WoUstjBbb8/640?wx_fmt=png&from=appmsg)

图1 APS-POMDP架构图

APS-POMDP的架构如图1所示，每个AUV维护一个定长观测队列，以先进先出方式存储最近的受扰观测\hat{o}\_{i}^{\left( t \right)}。预测网络P\_i通过GRU模块处理该队列，输出预测状态\tilde{s}\_i^{(t)}，随后Actor网络基于\tilde{s}\_i^{(t)}决策动作。这一架构将状态预测与策略决策在结构上解耦，规避了端到端训练中奖励归因错乱的问题。

在APS-POMDP中，受扰观测\hat{o}\_i在仿真与实际执行中的获取方式有所不同。仿真环境中，受扰观测通过\hat{o}\_i = f(o\_i, \delta\_i) = f(z(s\_i), v\_i(s\_i))生成。其中在训练阶段，为提高预测网络对不同黑箱扰动映射v\_i(\cdot)的鲁棒性，本文在预测网络与扰动映射之间进行对抗训练，在扰动可行集\Delta\_i内搜索最具破坏性的扰动，迫使AUV集群网络在最坏条件下学习，从而提升性能下界和鲁棒性。具体而言，最坏扰动\delta\_i通过PGD生成，其迭代更新规则为：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3TPQGDkpS2EpVQbeCILj8Nq5MSsQ0DbJLQ8iaK0rEvLfHofUdkLzhBbeMmHZLCcticXibTYDnl1TmEaeKfwkz869cSRcWTy65bJA/640?wx_fmt=png&from=appmsg)

其中h\_i表示通过P\_i递归处理前L-1步扰动观测所获得的历史隐状态。而在实际工程场景中，传感器输出的观测天然携带各类干扰，不存在标称观测o\_i，\hat{o}\_i由AUV i的传感器实时数据经计算与整合后直接给出。

**（4）基于对抗性预测状态的多AUV优势-注意力演员-评论家算法（APS-MA-A3C）**

基于APS-POMDP框架，本文提出APS-MA-A3C算法。APS-MA-A3C采用阶段训练策略确保训练稳定性和最终性能。在第一阶段，在无扰动条件下将AUV集群的基础策略训练至收敛。在第二阶段，引入最优对抗性扰动，训练预测网络以重构干净状态。

具体而言，首先构建经验回放缓冲区，用于存储AUV集群与环境交互产生的经验序列\tau，每个时间步的经验包含状态\mathbf{s}、动作\mathbf{a}、奖励r、下一状态\mathbf{s}'及扰动观测\hat{\mathbf{o}}。不同训练阶段利用序列中的不同信息子集。

在第一阶段训练基础策略：在无扰动条件下，利用经验回放池D\_1中存储的干净数据元组(\mathbf{s},\mathbf{a},r,\mathbf{s}')，按照MA-A3C算法训练Critic网络与Actor网络至收敛。

在第二阶段训练预测网络：固定已收敛的Actor网络参数，对观测施加PGD生成的最优对抗性扰动，构建新的经验回放池D\_2，其中每条样本包含真实状态\mathbf{s}与完整的L步受扰观测序列\hat{\mathbf{O}}。预测网络P\_i采用GRU结构处理扰动观测序列，取最后时刻的隐状态h\_{i}^{\left( t \right)}作为对真实状态的估计：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp17XAcRk9J7npAKu0Vicx50MIPd8xoxJBib8bVoUhxeDpAmjWMNmbaBhUqUamEWZE6PGhic4rXURa1LBMT7vYwJ8libzbXiaYNY9Y3s/640?wx_fmt=png&from=appmsg)

预测网络通过监督学习训练，以预测状态与真实状态之间的均方误差作为损失函数：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1RJ30UkqXkb8cxFzULKeNJNh021vkiceMmsupj4pqZ3cSFVJSWz0qoBsHkEPrmibZibT0tpKQBw2aWusheLVWFaDx3t2zsica3m3M/640?wx_fmt=png&from=appmsg)

**04**

**实验结果分析**

**ANALYSIS**

**实验结果分析**

**（1）仿真配置**

为验证APS-MA-A3C算法的有效性，本文在基于真实海底地形与海流数据构建的三维水下仿真环境中进行实验。仿真区域的地形由GEBCO海底地形数据（东经121.6°—122.9°，北纬21.2°—22.5°）按800m×800m×800m尺度重新网格化生成，以约束AUV可达空间并影响近底航行避障。海流数据采用HYCOM南海日均数据集。12艘AUV随机部署于距目标300m至500m处，目标呈随机机动以模拟逃逸行为。训练共5000个回合，每回合600步。本文选取MA-A3C（无防御基线）、PGD-MA-A3C（标准对抗训练）、Recurrent-MA-A3C（仅加时序模块无对抗训练）、Ro-MA-A3C（对抗训练+时序分析+一致性正则）、KF-MA-A3C和PF-MA-A3C（基于卡尔曼/粒子滤波的状态校正算法）以及APS-MA-A3C¹（无时序模块的消融版本）作为对比基线，主要从收敛性能、鲁棒追踪性能两个方面进行评估。

**（2）收敛性能分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3vmLtqvvC4JDTu6B2IribOo9yFFEKJOINiaZH4MMey6NVNV8eZU0rv7TgREM0EDhWCFFx8u8uOr8lcQNFPClyd8bpLq2bMxLJnc/640?wx_fmt=png&from=appmsg)

图2 APS-POMDP架构图

图2展示了各算法在训练过程中的累计奖励收敛曲线。MA-A3C在无扰动环境下累计奖励快速收敛且波动极小，作为性能上界参考。PGD-MA-A3C在训练初期出现显著策略振荡——端到端对抗训练中奖励基于真实状态但策略输入为扰动观测，"动作-观测-奖励"的因果链条被破坏，信用分配混乱，导致训练不稳；经过充分训练后，其策略学会根据扰动观测采取相对合理的动作，后期逐渐收敛。Ro-MA-A3C在PGD-MA-A3C基础上引入了GRU时序模块和动作一致性正则项，收敛速度和最终性能均优于PGD-MA-A3C，但初期不稳定性仍未完全消除。相比之下，APS-MA-A3C和APS-MA-A3C¹采用阶段训练策略，基础策略已在干净数据上收敛，第二阶段仅以监督学习训练预测网络，全程保持稳定上升，收敛后累计奖励接近MA-A3C无扰动上界。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0tKCYnV7mSic6JxKQmvj0zfj9XZxsPV8BP45d5enuUxKZUSppJgt7Lic6BYH2sC3zGpr0Tcj69YpFqFzdYicsY7icuzaAvHibwuz4Q/640?wx_fmt=png&from=appmsg)

图3 APS-POMDP架构图

图3为预测网络的平均损失曲线（纵轴取对数变换）。APS-MA-A3C和APS-MA-A3C¹的预测精度均快速提升并稳定收敛，而APS-MA-A3C的最终预测误差低于APS-MA-A3C¹，验证了GRU时序建模在利用历史信息还原真实状态方面的必要性。

**（3）鲁棒追踪性能分析**

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2jyWE6IDJoe1GCaxzqZkwuUbbHEe3SwLhMLnZ4cmx6qcGspt4H5m5L3YbQsaz97EclMyDicPQg45XUFNwbwRAEF3BvNkJvj4Gk/640?wx_fmt=png&from=appmsg)

图4 各算法分别在对抗性扰动、高斯噪声、观测缺失下的目标追踪性能

图4采用累计奖励衡量各算法在不同类型、不同强度观测扰动下的跟踪性能。在对抗性扰动下，MA-A3C性能随扰动强度增大而急剧下降。Recurrent-MA-A3C借助GRU时序信息使相邻观测之间能够相互印证，平滑了扰动对观测的影响，性能优于MA-A3C，但效果不及专用鲁棒算法。PGD-MA-A3C通过对抗训练提升了高扰动下的鲁棒性，但基础性能显著退化。Ro-MA-A3C通过引入动作一致性正则约束，缓解了基础性能损失。基于状...