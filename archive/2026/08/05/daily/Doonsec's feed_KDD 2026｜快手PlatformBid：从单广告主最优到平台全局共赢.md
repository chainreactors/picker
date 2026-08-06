---
title: KDD 2026｜快手PlatformBid：从单广告主最优到平台全局共赢
url: https://mp.weixin.qq.com/s/dEbmXGjRoKlRZKFTdeZDPw
source: Doonsec's feed
date: 2026-08-05
fetch_date: 2026-08-06T04:58:02.882435
---

# KDD 2026｜快手PlatformBid：从单广告主最优到平台全局共赢

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1gVUsotpT1ULYICzqibL2nGt0Aia1hyFd3kwfXOC0LdpvOIMWfWRed2XVVicxBw7rW3EoV306t2a60Z7w4QcpjHPvbh9FL8NMGnmVmCETcvPVM/0?wx_fmt=jpeg)

# KDD 2026｜快手PlatformBid：从单广告主最优到平台全局共赢

快手技术
快手技术

快手技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ZxDY5TMPs0EqL7dlyXD8OFyXn6yNGvQ8uEibL6TkOHqFvaK0bR9GEhZicTHuDtaTficMGS88ecXKIVPnFJCTMz7aQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

在计算广告领域，实时竞价（RTB）是核心范式：当用户在媒体端产生一次曝光机会时，广告交易平台向所有竞争广告主发起竞价请求，广告主通过 DSP 的自动竞价算法实时出价，最高出价者赢得展示。这一过程中，广告主只需设定高层目标（如目标 CPA、预算上限），自动竞价算法便自动完成全部出价决策 —— 它已经成为现代计算广告不可或缺的基础设施。

然而，长期以来自动竞价研究和基准主要停留在 DSP 视角，关注单一广告主的转化最大化。以快手广告系统为代表，真实工业场景中的自动竞价已经运行在统一平台体系内：流量供给、广告主投放和竞价交易相互耦合，自动竞价算法算法不仅要优化单个广告主效果，也需要兼顾多广告主竞争下的平台整体效率与约束稳定性。面向这一问题，快手联合东南大学、南洋理工大学共同提出 PlatformBid—— 业界首个从统一广告平台视角设计的综合自动竞价基准；同时，团队提出了基于 Flow Matching（流匹配）的新方法 BidFlow。相关成果已发表于 KDD 2026。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqGrK4ic9mibRYHomTQnic9RXaPWQJiaKCVf2Ke9ZBuXicKSraEpxBR9UxnkDrUAPaHKMaOzu1C23anf7ZNayvbTmSsIWUAbhXnge948/640?wx_fmt=png&from=appmsg#imgIndex=1)

* 论文标题：PlatformBid: An Auto-Bidding Benchmark from a Unified Advertising Platform's Perspective
* 代码仓库：https://github.com/YsTvT/PlatformBid
* 论文地址：https://arxiv.org/pdf/2607.27265

一、研究背景：被忽视的 "平台视角"

传统自动竞价研究以 DSP 为中心，核心目标是为单个广告主优化竞价策略，使其在竞争中获取更多转化。iPinYou、AuctionNet 等公开基准都沿袭了这一范式：评估单个广告主面对固定历史出价的竞价表现。

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqHhm0h5tQv366y5KpM5krjLH3IW92V7rSmeBJy9gHluXQFruGpiacS4VFwCd0aDpyZ3h29svx7mH5eUFJyiah7zLYS63ZdT8ibXvU/640?wx_fmt=png&from=appmsg#imgIndex=2)

但行业格局已根本改变：

* 平台整合趋势：真实工业广告系统已将 SSP、DSP 和广告交易引擎内部整合，广告主之间的竞价发生在平台内部，而非跨平台的外部竞价；
* 评估缺位：现有基准无法评估 "当所有广告主同时采用新算法时，平台整体收入和广告主公平性如何变化" 这一关键问题；
* 竞争动态缺失：AuctionNet 等基准通过顺序替换广告主、回放历史出价来评估，无法捕捉多个广告主同时调整策略时的动态竞争。

单广告主的最优不等于平台全局的最优。从 DSP 视角到平台视角的范式转变正是本工作要解决的核心问题。

二、PlatformBid 基准设计

###

2.1 问题定义：平台视角的形式化

PlatformBid 首先从统一平台视角重新定义了自动竞价优化问题。与传统 DSP 公式相比，最关键的区别在于显式引入了平台级目标约束 O\_l：

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqHBIicyCmsicwMRxDwceYxOJdhpBPdoibicMItN34Bialp8sQNxkGZqGxLssFyn1xckqSEesYVFXneyU7C0IJ1pB1wMcicEB7pMrfs0g/640?wx_fmt=png&from=appmsg#imgIndex=3)

其中 O\_l 可以要求平台总收入不低于基线策略水平，类似于线上 A/B 测试的要求。竞价策略采用多参数线性出价形式![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqGASLOib36P09L0RyKQiasVbPYM7vuKvV757udWBMbKIHrDUxwtAteBvvCMKiaO4v96XREnoCRB5toynpBwb6wqUJ7LxE8Md6ntwU/640?wx_fmt=png&from=appmsg#imgIndex=4)，算法在粗粒度时间间隔（如 30 分钟）更新参数，为复杂算法留出充足计算空间。

2.2 三大评估设置

基于平台实际业务场景，PlatformBid 设计了三个代表性评估设置，准确反映真实世界的自动竞价竞争动态：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqFib44LV4fPpSph3gQTatdSBpaIsjPeibia9w8OVV1f7oafZ6OcBgwicFRLbMK53XWvHZdCFzBib5j3r3aGM7k71WhJXJjSw43j58wQ/640?wx_fmt=png&from=appmsg#imgIndex=5)

设置 1：同质竞争（Homogeneous Competition）

所有 N=48 个广告主部署相同的竞价策略，通过 GSP 拍卖机制竞争曝光。这一设置直接映射线上新算法全量上线场景，评估平台级平均表现，揭示算法是否能实现稳定的市场均衡，还是会引发系统性效率损失（如出价通胀或合谋压价）。

设置 2：异质竞争（Heterogeneous Competition）

将广告主分为两组：N/2=24 个基线广告主使用固定的参考策略（vanilla Decision Transformer），N/2=24 个测试广告主使用待评估算法。这一设置映射线上算法灰度测试场景 —— 新算法仅部署给部分广告主，需要确保测试广告主性能提升的同时不损害基线广告主的表现。

设置 3：促销竞争（Promotional Competition）

模拟大促活动（如黑色星期五）：7 个广告主预算翻倍，所有广告主使用相同算法。分别报告促销广告主、非促销广告主和平台整体指标。这一设置测试两个关键能力：一是促销广告主能否有效利用扩展预算，并在预算提升后仍满足 CPA 约束；二是非促销广告主能否在竞争加剧的环境中维持稳定投放效果。

2.3 评估指标

PlatformBid 采用平台级和广告主级双维度指标体系：

* 平台级指标：转化量（Conversion）、预算利用率（Budget Utilization）
* 广告主级指标：CPA 比率（CPA Ratio）、CPA 比率方差（CPA Ratio Variance）、超限率（Exceed Rate）、合格率（Qualified Rate）
* 综合指标 Score：平衡平台收入与广告主满意度：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqFibnsw6rYUH8B1n5DQh0BhjerWfJ1aMmSNmqQKzU4Bia3ps18N6oed5U0Yeiba5bbEIR4u5a4X7xB47Q2XpAa4gn9pABH91ryibiaI/640?wx_fmt=png&from=appmsg#imgIndex=6)

该指标反映平台对可持续增长的偏好 —— 通过违反约束获得的高转化会被惩罚，因为这种行为侵蚀广告主信任和平台长期健康。

2.4 数据与实现

PlatformBid 基于 AuctionNet 数据集构建，包含 48 个广告主在多样化预算和 CPA 约束下采集的 480K 训练轨迹，提供 Dense 和 Sparse 两种奖励稀疏度变体。关键扩展在于：从 AuctionNet 的单广告主孤立评估，转变为多广告主共享拍卖环境的交互式模拟。为防止广告主合谋压价损害平台收入，引入了底价机制（设为历史最低成交价的 80%）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqHQiaTepxafDTsxYPkkxh5icqJg2ibDNaPQ1D3bXyAPAkaQQAfEzkNHpiaibuz5Bz9m3tkZMXRjFQmrvk5ryD1QY18MBxP0hm8H47sI/640?wx_fmt=png&from=appmsg#imgIndex=7)

三、BidFlow：基于 Flow Matching 的自动竞价方法

###

3.1 动机：多模态竞价分布的挑战

在 PlatformBid 的新设置下，现有自动竞价方法表现受限。其根本原因是平台级竞争环境引入了更复杂的市场波动和竞争动态，对建模多模态竞价分布的能力提出了更高要求。

三类现有方法的局限性：

* 经典控制方法（如 PID）：基于固定数学公式，无法适应复杂市场动态；
* 强化学习方法（如 BCQ、IQL）：假设单峰动作分布（如高斯策略），难以表达多模态竞价策略；
* 生成式方法：Decision Transformer 类方法（GAS、GAVE）通常建模确定性或单峰高斯分布；扩散模型类方法（CBD）表达能力虽强，但迭代去噪导致推理速度慢，难以满足竞价系统的延迟要求。

为此，团队提出 BidFlow—— 利用 Flow Matching 的强大分布建模能力，同时通过 Q 值引导蒸馏实现高效单步推理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqF25QaSr07d9apB0fgGJxsSodv42IckB0lGM1SNemSgOWbN38EAXHaK6vTwibJt6RoqTXIsUcMGYdEEHIMZ0YEGrSXHy6PlK6lo/640?wx_fmt=png&from=appmsg#imgIndex=8)

3.2 BidFlow 架构

BidFlow 由三个核心组件构成，联合训练：

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqHzAlcjlVqc9nwyRI9DGaFia2IZJc1Vykib3YQicqGwhtkh1fibcPOrkzr80hwenCj8Malx7mdTsV3Aicl1HQDcWTQibHZyEbiaW2QFco/640?wx_fmt=png&from=appmsg#imgIndex=9)

 （1）Critic 网络![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqF4NQljP5SnjibrgDb18veLR84nNmHrgzOohMy9iczIWjuKL3Odew4MGv2BJsTKQ1yzqz9hicWdZ761fVNlwIBeO8qPeV52ONINJg/640?wx_fmt=png&from=appmsg#imgIndex=10)

通过标准时序差分学习训练，估计状态 - 动作价值：

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqFRXBT4ib0svV0MHAvrpta6fFGTqpoGWwVTwibEyNlGD9tSMHEmqRqY0SfwEBBFVorKxsfd6wKCnw87XmBmgAH8ia4Hkovw73kBmE/640?wx_fmt=png&from=appmsg#imgIndex=11)

（2）BC Flow 策略![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqFaNZ3MeYI0dibRgs1xcyAhwTSd2IX1xPdUFaTKb21rlRBqX84AoLS9jeUrxoicuAhXbwicKfvicpaGoSfYo2Et2PE60rXYoDwy7s0/640?wx_fmt=png&from=appmsg#imgIndex=12)

通过 Flow Matching 训练行为克隆策略，学习速度场将高斯噪声转化为动作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqGA8Jf1tgoPN9TcpthgIqUVhq5mU0D8Ggd4kIdVJDSWfmQrWkibia2zUh512a5KeFL2NkflaiaXjJUdUQuvgrdZ1JicVdSmCqEfMaQ/640?wx_fmt=png&from=appmsg#imgIndex=13)

其中 a\_t = (1-t) a\_0 + ta 为线性插值。推理时通过 Euler 方法在 M 步内数值求解 ODE 生成动作。

（3）单步策略![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqFK8O8atk7jwdJCib0efA2OrUgXWCThctZCBib69sq4OpgXrG67Z8MzhRKDzPwFtt5pq6oxgeHQ8bzgoVCq6rohz6gOjvyavusNg/640?wx_fmt=png&from=appmsg#imgIndex=14)

将多步 BC Flow 蒸馏为单步策略，同时通过 Q 值最大化实现性能超越：

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqHqbw1JGzmtCica0QIejaibqRRWEhj83xeRSUXpjNicE1TLG8Pf4WLuK3V3b6a3A3QDYC5BWaOfu1XPLs26fTILFicR1GBgmqL3D1A/640?wx_fmt=png&from=appmsg#imgIndex=15)

第一项从 BC Flow 蒸馏知识，第二项最大化 Q 值以超越行为克隆，![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqE2KxcXxia2hQPU0alngibQtXVfSqQkuN3ZMITy95T0WRLzYnictiaDgNWE4ZRia79qw6r0YiaHWk6E6okVsIlqL09TUa6amFrFzYee4/640?wx_fmt=png&from=appmsg#imgIndex=16)控制正则化强度。三个组件在每次迭代中联合训练。部署时仅使用单步策略![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqGK451RYngqJQIIbTZXicGCTRVMMcBpbCD9AfpypF7EibrV4q9vX9IJLRgJnyNIqvkoWVe6gIqLUibB7MwwLshO8ktCiaUNzPoSydg/640?wx_fmt=png&from=appmsg#imgIndex=17)，实现高效推理，无需迭代采样。

3.3 算法流程

算法首先初始化价值网络、目标价值网络、BC Flow 策略和单步策略。每轮从离线数据集中采样，依次完成价值估计、流匹配训练，并通过 Euler 方法生成蒸馏目标，用于优化单步策略。训练过程中持续软更新目标网络，收敛后仅保留单步策略进行在线出价，以兼顾策略性能与推理效率。

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqEticoHhABjpWeDbiczpDH89pF0fibuxJG03Cc1UFwaklAO2QAIpKuqUq2GibXr1Ubz711vQmB9oicLfQ8I4EgoD9SBCkazbF3NYbSI/640?wx_fmt=png&from=appmsg#imgIndex=18)

四、实验结果与分析

###

4.1 设置 1：同质竞争 —— 全量部署的全面领先

在 Dense 数据集上，BidFlow 以 348.04 的 Score 显著领先所有基线方法（次优 GAS 为 314.27），同时保持最低的 CPA 超限率（0.25）和最低 CPA 比率方差（0.03）。在 Sparse 数据集上，BidFlow 同样以 30.59 的 Score 取得最佳表现。这表明 BidFlow 在所有广告主采用相同策略的全量部署场景下，能有效平衡广告主目标和平台福利。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqGicoEyOK15JnooVpHAh0TfAcHg3d0gPYDz0RuDoB47AKDibT4Nib6EEo7c4u3NlytF1ZoHvTVO8CMOD3Wp3w7nSmoKVSiaVUDOlys/640?wx_fmt=png&from=appmsg#imgIndex=19)

4.2 设置 2：异质竞争 —— 灰度测试的稳健表现

在 Dense 数据集上，BidFlow 在平台整体 Conversion（347.96）上表现最佳，且不损害基线广告主表现。但在 Sparse 数据集上，BidFlow 出现性能退化（目标组 Score 35.97 vs DT score 43.91）—— 分析表明这与 DT score 和 DT 基线共享相同 Transformer 骨干、形成低出价合谋均衡有关，而非 BidFlow 本身的架构缺陷。

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqE3plAoIgwiczHsnUKbdKlIVibI9thKcHpVAvB6anf9LFbrgSG4mUhY9FfoU7P6StkshhNafe5ZGM814T71g4HPAgL51wbdGlPXw/640?wx_fmt=png&from=appmsg#imgIndex=20)

4.3 设置 3：促销竞争 —— 极端预算不平衡下的泛化

BidFlow 在促销广告主（Dense Score 701....