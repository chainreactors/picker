---
title: 每周文章分享-264
url: https://mp.weixin.qq.com/s/2w31pKPrnAGj5c9GojA3VQ
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:47:37.902169
---

# 每周文章分享-264

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jBQAokCLibp2VXr56M1BfjHbswicyK2T3RSRWOpnglBvGtgS4K3icicv8nyvHgWWOdQtickzOFficvJpDqDHT5NAmpPAof3UECiaCw6lPPwLaF3xIc/0?wx_fmt=jpeg)

# 每周文章分享-264

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

每周文章分享

🌿

**2026.06.15至2026.06.21**🌿

**端午佳节 喜乐安康**

**标题:**A Dual-Agent Adversarial Framework for Robust Generalization in Deep Reinforcement Learning

**期刊:**International Conference on Learning Representations

**作者:**Zhengpeng Xie, Jiahang Cao, Yulong Zhang, Qiang Zhang, and Renjing Xu

**分享人:**河海大学——朱星宇

**🌿**

**01**

**🌿**

研究背景

深度强化学习凭借神经网络强大的拟合能力，在诸多复杂决策任务中取得了巨大成功。然而，尽管现有模型在特定任务上表现出卓越的决策能力，但它们极易陷入过拟合的困境,训练好的智能体往往无法泛化到任务的微小变体上,例如背景颜色的改变或其他细微的非语义特征变化。

为了解决由于高维观测中包含大量无关特征而导致的泛化性差的问题，现有方法主要依赖于数据增强或传统正规化技术。但这些方法要么会引入不符合强化学习目标的偏置，要么由于侧重于静态表示而忽略了智能体与环境交互的动态特性。虽然对抗学习（Adversarial Learning）是一种有前景的方向，但现有的对抗框架通常需要额外引入生成器与判别器网络，或需要修改仿真环境的基础参数，从而引入了更多的超参数和极高的训练成本。

**🌿**

**02**

**🌿**

关键技术

针对上述挑战，本文提出了一种双智能体对抗策略学习框架（Dual-Agent Adversarial Framework）。该框架通过引入两个同质智能体之间的博弈过程，使其能够在不依赖任何人类先验知识的情况下，自发学习到环境背后的底层语义特征。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp20q601aNofOqmyfFy9T9MVwlOjrX5JKeBbiaVEdxRKAv1gLIdvicPLqRCicm3ECMPN4vicNHgbc62YWUAWjTK0eUwsRL2gts7VY4s/640?wx_fmt=png&from=appmsg)

图1 双智能体对抗策略学习框架总体架构

如图1所示，该框架由同质智能体博弈、目标机制和鲁棒性泛化三个主要流程组成。

同质智能体博弈:训练样本会同时输入两个同质智能体（Agent 1和Agent 2）的编码器中，由于参数差异，相同的状态会产生不同的高维表示。

目标机制:在博弈过程中，每个智能体通过调整自身编码器的参数，一方面试图最大化状态表示差异对对手策略网络的影响，另一方面又要保持自身策略网络在面对此类干扰时的稳定性。

鲁棒性泛化:这种极大极小博弈过程最终促使两个智能体学习到具备鲁棒性的策略，能够自发剥离高维观测中的不相关特征，从而防止过拟合，显著提高泛化性能。本文有以下贡献：

1)证明了通过最小化策略在面对无关特征时的鲁棒性差距，能够有效提升模型的泛化表现。

2)提出了一种通用的、几乎不引入额外超参数的对抗策略学习框架，该框架可无缝集成到现有的主流策略学习算法中。

3)在极具挑战性的Procgen基准测试中进行了广泛实验，验证了该对抗过程能以显著的优势超越传统的基线方法。

**🌿**

**03**

**🌿**

算法介绍

**（1）泛化性马尔可夫决策过程解耦**

为了在数学和理论上形式化强化学习的泛化性，本文将环境解耦。定义马尔可夫决策过程为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1eXWX1T9relcn4ReTcYOMictKiavcrELOnRllXo6ho1j0tfdnBF11rDjQiap3xR0Bv1Q1kBDdMPg7icTxdXJR3KtZku0XLIiaNzxib0/640?wx_fmt=png&from=appmsg)

为了便于理论分析，本文将高维状态观测s\_t^m解耦为语义核心变量u\_t和由环境决定的扰动函数phi\_m(.)：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2ODibBWNZib0k6cvF3bH8XsYmOjC4hbKiccY5sgGa1rcdrialdktfv6xmqmT9JsTMls3QFY7C3mjSiaTIojqHko2iaRZUCiccJjt8VbE/640?wx_fmt=png&from=appmsg)

其中u\_t隐式地包含了对智能体最大化期望回报至关重要的底层语义信息,如操控角色与周围障碍物的相对位置关系。phi\_m(.)表示混淆和掩盖了这些核心语义，表现为游戏的背景风格、渲染色彩等不相关特征。这表明即使是两种截然不同的状态也可能代表相同的语义，于是本文考虑一个完全由有用信息组成的隐马尔可夫决策过程（HMDP）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1xGeJSia2Z1EtcfflSbdEibMlVKJAVJQuv8whcHIF0yyaqnGulMjjL6DulNKofyvhibGagR8gcPiba8EL95vF8aljSZMtHgW6p6Pw/640?wx_fmt=png&from=appmsg)

**（2）理论分析与性能下界**

利用传统的CNN进行特征提取时，智能体极易利用phi\_m提供的冗余信息进行“作弊”,即仅靠死记硬背非语义特征获取高分，导致在未见过的测试环境中完全崩溃。为此，本文基于隐马尔可夫决策过程（HMDP）排除所有受环境扰动m影响的变量，推导出了智能体在目标泛化环境下的性能下界定理。为了量化由于环境扰动带来的策略偏差，本文引入了总变差距离，并推导出了训练集环境与测试集环境之间的策略鲁棒性差距。

首先，本文量化了由于环境扰动带来的策略偏差。假设存在两个不同的马尔可夫环境（或不同的关卡分布）m和tilde{m}，其对应的状态观测分别为s = phi\_m(u)和tilde{s} = phi\_{tilde{m}}(u)。通过引入总变差距离，可以证明两个智能体pi和tilde{pi}在面对相同核心语义、不同环境扰动时的期望最大总变差距离满足以下不等式约束：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0ibjKaOMMG5vrHeIPaCvqm6cDVKFnTJ30DNhhgD5Nr7bjicE8d6hicBYRklWcwwLyl1Pmv0DfwC5o3MLTSAjyfZLNw1SGHaC0PZQ/640?wx_fmt=png&from=appmsg)

该公式的左侧项代表两个智能体在相同观测下的策略差异。右侧前三项分别代表单个智能体跨环境的策略不稳定性（即对背景噪声的敏感度）以及在特定环境下的智能体间距，后三项为对应的交叉乘积项。

基于上述策略偏差边界，本文推导出了智能体在面对目标未见环境分布时的真实期望回报的性能下界。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0J6P2AlNJN1pc5nhQiadBYo0NmAN8hhsaXmDMwRTR3oPpRWt0jIZ8c3uKYv1AGvwfsKYncLoWuGVgereX6NzRfeJuicsbTiaTAyw/640?wx_fmt=png&from=appmsg)

进一步建立了未见测试集上的真实泛化目标性能与训练集目标性能之间的悲观下界关系：

**（3）网络结构**

由编码器和策略网络组成，编码器将原始状态 s（含无关特征，如背景、渲染风格）映射为语义表征 z：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1PeY9RQmXp0DrBPv5ia5uyIrEwicZGbuDMkzZfueibOZDmicFwTSeZIrAhQj37T2QzY9e99okl5sKTRlC0KPIhNdI3fcqhwibAKQU8/640?wx_fmt=png&from=appmsg)

策略网络 基于语义表征z输出动作a

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2Jy1efhjuZSk4gJYTBKicibRBdDibhiaibTicYm6zrMqlAQ7WJl5NtKXc7bfibxdtV4xNdHW04W52WKbg0YNibjcyDoHhicIdBWXIe1ALE/640?wx_fmt=png&from=appmsg)

**（4）双智能体对抗结构**

如图2所示，为了防止对手智能体产生良好的动作，智能体1试图改变两个编码器的参数来影响智能体2的决策，其中KL散度用于量化这种分布扰动：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp26ns8bnITHuGKwprVV1bu0dB63CrzujwlI8HsQ4NtK2bKgIe5mpRPXTSDtza6ziaIvW0tCTJqPvnsAkhqjMeVQXfnH7ljkwk0E/640?wx_fmt=png&from=appmsg)

同时智能体1自身试图对这种影响保持鲁棒性，可以表示为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp37NibX4TY4xIbeQw05UYvZPp7EbZZfOiboSgYCBF3FcAt7GraJXObte2icGBFnwfZ2sIZDFW5rfa7XPcER2jZOGzF2lxaCA5SwG8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0kVCoqS0LfMR82Mvr4gawZrIWgIcqaoB62YzAnELcIxtcNBkN1RDyH5bOZ2PXZp4ZUJG9GXZzRibmRR3YwLTPzC4wicwNuibq0Po/640?wx_fmt=png&from=appmsg)

图2 对抗策略学习

对抗过程与强化学习训练过程相结合总损失定义为：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp11rwnOtqHayG6eVfPaDHO2icB21zhf7DJYsVXN96EmRPDXjJObLBZWibiauQCvrlA9sDqaiceSV4g8icXfO6KiaDrzlCl0VIclcHQGQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0lAibVOS06iabiak6W44La2JTc4NydMD82F88cyibRPfCkz4mvjcVaCnFSBqOxFjsAjOm1DYMyeLicmk0FvooicMZm6JkicyMg0hxVdM/640?wx_fmt=png&from=appmsg)

**🌿**

**04**

**🌿**

实验结果分析

**(1) 实验设置**

实验在学术界公认的高难度强化学习泛化性基准Procgen Benchmark上展开。为了全面验证框架的鲁棒性，实验直接采用了Hard模式（包含多达200 个不同的随机生成关卡环境），并在8个最具代表性的任务（如BigFish, StarPilot, CaveFlyer 等）上进行了总计 2500万步的训练。

**(2) 基线方法**

PPO (Proximal Policy Optimization): 作为目前主流的工业级在线策略（On-policy）策略梯度算法。标准PPO在训练过程中直接针对当前环境的高维观测进行表征和策略更新。由于缺乏任何显式的泛化正规化约束，它在面对包含复杂背景、噪声干扰的环境时，极其容易将这些非语义核心特征一同死记硬背，是评估强化学习过拟合程度的标准基线。

DAAC (Decoupled Advantage Actor-Critic): 一种前沿的针对强化学习泛化性进行优化的先进基线算法。DAAC 核心思想是通过引入显式的解耦机制，将 Actor（策略网络）和Critic（价值网络）的表征学习进行分离。因为传统方法中 Critic 往往需要保留大量的环境背景细节来精准预测状态价值，DAAC通过这种解耦防止了Critic的过拟合噪声污染Actor的策略，是目前在Procgen泛化任务上表现强劲的算法之一。

**(3) 训练与测试表现对比**

如图3所示，在整个训练过程中，PPO、DAAC 以及加入我们对抗损失的PPO在8款 Hard级别Procgen游戏上的平均泛化性能表现从训练过程的性能曲线中可以观察到以下显著现象。

标准 PPO 算法虽然在训练初期能较快在训练集上取得高分，但在测试集上的归一化回报极低，泛化差距随着训练步数的增加而不断拉大，出现了典型的严重过拟合。

DAAC 算法得益于Actor和Critic的表征解耦，其测试集得分明显优于标准 PPO，表现出了一定的泛化鲁棒性。然而，由于DAAC本质上仍然是在单智能体架构下对静态特征进行解耦，面对环境动态扰动时的上界依然受限。

而本文提出的对抗框架由于引入了双智能体同质博弈，在训练初期因为要解决极小极大博弈的对抗平衡，收敛速度略有放缓。但随着博弈的深入，智能体开始自发剥离背景等噪声，其测试集得分在整个训练周期的中后期稳步攀升，最终的平均泛化回报以绝对优势超越了标准PPO和强基线 DAAC，显著收窄了泛化差距。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3cesOmiaKib4WCRvJrIx9P17TDrXecYY9GyibdF0S4Vq0FzjSicib9oQKy6maM5heH0GQf6Dg93cUJd6PjkHCBIWg5LTNEqxghdzx4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3l7XMYC8u2xF0htGrsdjrfBiblKa0UCHSaDmKvrBluicyCDYWxYG5f6k2oW5OmP1OGHbQb8yulTL5j2yia0Bxzs7sCDn4Cz2z77M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp0gxqeiaUDjJzbD7pOvLGx5tNfYibT9z0cjMfa7L0iamZa9J3AN0jutz86Ya3tKAkopX1GR9udicVv5wZDoGSvAaosPeAv3D7CeJoY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp31ssTqVuiauazSxYsxunfOy8yjQhsW84fDkaeCC9J0ZuichicXRglvxP5l5hwyK6ZtElcDaMHqWCJXqJ4rTquEJfLFLTvegic5tz8/640?wx_fmt=png&from=appmsg)

图3 不同传输速率的比较

**(4)不同任务环境下的定量分析**

了更具体地评估模型在不同类型噪声干扰下的表现，我们在8个Hard任务中对最终测试环境的得分进行了严谨的定量统计。表1详细列出了各个任务在25M时步训练结束时的最终测试得分对比。

表1平均泛化性能

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1UH12jBgeHibftI0MfskiaiapdSXlKSzzQIOib3ysAO6EF7PBWP5A3OSB9sbyrSSV9ADsfic5lkdYIqaNfsjAicwcphMJsm1euIuzKM/640?wx_fmt=png&from=appmsg)

在所有测试的Hard任务中，本文方法（Agent 1 & Agent 2）均取得了超越标准PPO和先进基线DAAC的成绩。在如BigFish和CaveFlyer这种视觉背景极其多变、干扰极其严重的任务中，本文方法较标准PPO实现了翻倍的得分提升。这强有力地证明了双智能体在对抗博弈过程中，确实能够迫使网络自发对环境中与控制无关的混淆特征产生免疫，从而真正捕捉到了核心底层语义。

**🌿**

**05**

**🌿**

总结

本文针对深度强化学习在面对未见过环境时严重的过拟合现象，提出了一种新颖的双智能体同质博弈对抗学习框架。通过两个智能体之间相互产生特征差异并追求稳定性的极大极小博弈，使模型能够自动且无监督地聚焦于真正有用的底层语义，避免对背景等无关噪声建模。在Procgen极高难度环境下的综合实验充分证明了本方法的有效性、通用性以及极低的超参数开销，为解决强化学习的高效泛化问题开辟了全新的途径。

—— END ——

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jBQAokCLibp1tLwicm6icynr13iaAyzTVFDeic1kyZicIVBoWm3I6hApG2TathgnkRxHWccuiaoI5Ta8cvpJtgCkPGs8fyc5Feria6puZKx9EZZ7zpE/640?wx_fmt=jpeg&from=appmsg)

==河海大学网络与安全实验室==

微信搜索：Hohai\_Network

联系QQ：1084561742

感谢关注！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ASlHg58pYMe1HLLDN2MwVD3d9iaphI4Evp3oib9RPtU2gOR3ubr5qzibTwSBgaJgJ52tuI5knfsB9ECKibfibAt40KA/0?wx_fmt=png)

网络与安全实验室

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序
...