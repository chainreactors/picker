---
title: 每周文章分享-244
url: https://mp.weixin.qq.com/s/--1YYakix-8Z2FSBV5gKFg
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:38:00.738286
---

# 每周文章分享-244

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ASlHg58pYMcBEHuGb68n4rufkia7l7po47sE9VsmkLSQo6PVSBUpymLK9Su9YA9icibmf42mrLicQ46sVELK8zWGJg/0?wx_fmt=jpeg)

# 每周文章分享-244

网络与安全实验室

![]()

在小说阅读器中沉浸阅读

每周文章分享

2026.01.12至2026.01.18

**标题:**Neural Network Model-Based Reinforcement Learning Control for AUV 3-D Path Following

**期刊:**IEEE TRANSACTIONS ON INTELLIGENT VEHICLES, VOL. 9, NO. 1, JANUARY 2024

**作者:**Dongfang Ma , Xi Chen, Weihao Ma, Huarong Zheng , and Fengzhong Qu

**分享人:**河海大学——齐倩文

01  研究背景

随着海洋资源开发与海洋探索的不断推进，自主水下航行器（AUV）作为能够替代人类在水下完成特定作业的重要工具，受到了广泛关注。AUV相关技术的持续发展，为海洋研究领域带来了革命性变革，在管道检修等诸多任务中，AUV需要沿着特定路径航行，因此其路径跟踪控制问题成为关键研究课题。在经典控制领域，学者们提出了多种控制方法来解决路径跟踪问题，如比例 - 积分 - 微分（PID）控制、自适应控制、滑模控制（SMC）以及模型预测控制（MPC）等。然而，这些传统控制算法面临着两大挑战。一方面，它们大多高度依赖受控系统的动力学模型，而水下环境具有强非线性和时变性，建立通用且准确的AUV动力学模型极为困难。尽管数据驱动的MPC方法通过数据学习系统相关特性受到关注，但针对非线性系统设计兼具稳定性和约束满足性的数据驱动MPC方法仍极具挑战性。另一方面，传统控制算法忽略了AUV与周围环境之间的交互信息，难以感知和适应环境的动态变化。强化学习（RL）通过在智能体与环境的持续交互中最大化累积奖励，在众多复杂任务领域取得了超越人类的性能，深度强化学习（DRL）方法更是结合了深度学习的感知能力与强化学习的决策能力，为实现最优自主控制提供了可能。但现有DRL-based控制方法在AUV控制中仍存在不足，如部分算法训练出的模型实时性不佳、训练效率有待提升等。基于此，本文旨在提出一种新的基于强化学习的AUV路径跟踪控制框架，以解决传统控制方法的局限性，提升AUV在复杂海洋环境中的路径跟踪性能。

02  关键技术

**（一）Actor-Model-Critic(AMC)架构**

本文提出了一种新颖的 Actor-Model-Critic(AMC)架构，该架构在传统 Actor-Critic(AC)架构的基础上，嵌入了一个神经网络模型。神经网络模型用于学习 AUV 及外部环境的时空变化模式所对应的状态转移函数，为Critic网络提供更多有效信息，进而提升算法的收敛速度和控制鲁棒性。这种架构并非简单地将模型与强化学习算法分离，而是将其有机融合，使模型能够更好地辅助强化学习过程，克服了传统模型基方法中模型与算法脱节的问题。

**（二）ModelPPO控制器**

基于AMC架构，本文构建了名为ModelPPO的强化学习控制器智能体。该智能体结合了先进的近邻策略优化（PPO）算法与神经网络模型，其中PPO算法通过限制策略更新的幅度，解决了传统AC算法对策略更新大小敏感的问题，保证了训练过程的稳定性和有效性。ModelPPO负责控制AUV的方向舵和升降舵，使AUV能够跟踪期望路径，而AUV所需的航行速度则通过传统的比例 - 积分（PI）控制器来实现。

**（三）课程学习训练方法**

为提升训练效果和效率，本文采用课程学习（curriculum learning）方法对ModelPPO进行训练。训练场景从理想环境下无任何干扰的纯路径跟踪开始，逐步引入海洋水流等干扰因素，使智能体从简单场景入手，逐步积累经验，提升在复杂环境下的控制能力，有效加快了训练收敛速度，增强了模型的鲁棒性。

03  算法介绍

**（一）强化学习框架下的问题建模**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po4NKZib7eMn9zbluhm0cWMzhiaZicdshvKYJNdia8g9wn7jJhFksBEKRXrvw/640?wx_fmt=png&from=appmsg)

图1自主水下航行器（AUV）路径跟踪控制问题中的强化学习（RL）框架

图 1 描述了自主水下航行器（AUV）路径跟踪控制问题中强化学习（RL）框架的问题定义。在 AUV 路径跟踪控制问题的强化学习框架中，智能体根据环境状态s\_t执行动作a\_t，并从环境中获得奖励r\_t以评估动作选择的优劣。其目标是最大化期望累积奖励G\_t。

状态设计：状态是对AUV自身状态和水下环境条件的特征表示，包括相对速度（纵荡、横荡、垂荡）、姿态角（横滚、俯仰、偏航）、角速度（横滚率、俯仰率、偏航率）、航向误差、elevation误差以及海流速度（纵荡、横荡、垂荡）等。这些变量经归一化处理后，转换为神经网络可处理的数值形式，确保状态能够充分描述AUV和环境的关键信息。

动作空间：在运动控制中，AUV的巡航速度由传统PI控制器维持恒定，智能体通过控制方向舵和升降舵的角度来调整AUV的姿态，因此动作空间为方向舵和升降舵角度的控制信号，即一个2×1的向量。

奖励函数设计：奖励函数的设计对强化学习的方向至关重要。本文的奖励函数不仅对实际姿态与期望姿态之间的误差（航向误差和elevation误差）进行惩罚，还对横滚角、横滚角速度以及控制输入的使用进行惩罚，以激励智能体控制AUV跟踪参考路径的同时，尽可能节省能量，避免出现不安全的姿态。奖励函数表达式如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po44utH55UaTFVHK5CMs9AIZqhh5cDziaQmMx3RJkDVjK5PiajXFaHzJEJA/640?wx_fmt=png&from=appmsg)

**（二）AMC 架构详解**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po4NRfHyuQiaDSbzALRnlWzcBXCZvsWRs7HrLz0v9ssqTiafoTFbBNXHbNQ/640?wx_fmt=png&from=appmsg)

图2 AC 和 AMC 架构对比图（Δ 为时间延迟模块）

传统AC架构：传统AC架构包含Actor网络和Critic网络。Actor网络接收当前状态作为输入，输出当前动作；Critic网络输入当前状态和Actor选择的动作，计算状态 - 动作值Q或状态值V。Actor根据Critic输出的价值信息进行更新，Critic则利用时序差分（TD）误差进行更新。

AMC架构改进：如图2所示，AMC架构在AC架构的基础上，于Actor和Critic之间添加了一个模型网络（Model Net）。该模型网络以当前状S\_t和 Actor Net1 输出的潜在策略p\_t为输入，学习状态转移函数，输出状态在时间步长Δt内的变化量，进而预测出下一状态。

Critic网络则接收当前状态s\_t、Actor Net1输出的策略p\_t以及模型网络预测的状态变化作为输入，输出状态值V。此外，Actor部分由Actor Net1和Actor Net2组成，Actor Net1输出动作选择的策略p\_t，Actor Net2根据动作分布形式（本文采用高斯分布）输出动作的均值a\_t，结合预先设定的方差，在动作选择模块中生成动作分布曲线并采样得到最终动作。

**（三）ModelPPO 算法训练流程**

训练场景设置：采用课程学习方法，首先在无海流的理想环境中训练智能体，使其掌握基本的路径跟踪控制能力；随后在存在海流的干扰环境中训练，以提升模型的鲁棒性，并保存整个训练过程中的最优模型。

损失函数构建：

优势函数估计：利用广义优势估计（GAE）方法估计优势函数，即

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po4MoPIttRQoQoHj3AQv0Uuz0UCYYAzYI9gAvkrQiap6byCC3v8T5y7rEQ/640?wx_fmt=png&from=appmsg)

策略替代损失：采用 PPO 的裁剪替代目标函数，限制策略更新幅度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po4aWYntdocicdt4sXJ13QJ9seQB8xm05iaspiaIKQvOTxTY1zicvy1EtJJbQ/640?wx_fmt=png&from=appmsg)

模型网络损失：通过最小化预测状态变化与实际状态变化的均方误差来训练模型网络。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po4ZVYFpKHyJvtHNMszP4KoapX9WI6q7DaCsEic9CAdibwBYSPqibYicAqZmg/640?wx_fmt=png&from=appmsg)

价值函数损失：价值函数的损失为预测状态值与目标状态值的均方误差。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po4EMwL0o4kbwO0u5y1N0Hf19Z4VeubmFzcubOx8g3bYD5QAbLicAV49tA/640?wx_fmt=png&from=appmsg)

总损失函数：综合策略替代损失、价值函数损失、模型网络损失和熵奖励，以平衡训练稳定性、准确性和探索能力，表达式为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po4vBXQHj5kEHeJjV4ZqkZnq8X1tiaM5xGjlWlEAUm14mmzlJfmYUv8WkQ/640?wx_fmt=png&from=appmsg)

算法训练步骤：

1.初始化数据集D和网络参数。

2.迭代训练：在每个迭代中，智能体执行当前策略pi\_theta\_old，收集轨迹数据并存储到D中。

3.计算优势估计以及各部分损失。

4.随机选取批量样本，通过梯度下降法更新网络参数，重复K个epoch。

5.更新theta\_old为当前参数theta，进入下一轮迭代。

04  实验结果分析

**（一）实验设置**

仿真平台构建：基于AUV的6自由度刚体动力学模型构建仿真平台，该模型包括运动学和动力学两部分，分别描述AUV的位置姿态变化和运动的受力情况。采用东北天（NED）坐标系和体坐标系来描述AUV的运动状态。

环境扰动设置：引入3维无旋海流模型作为环境扰动，海流强度通过一阶高斯马尔可夫过程生成，强度限制在0.5~1 m/s之间，每个episode的海流方向随机初始化且保持不变。

路径生成：采用二次多项式插值（QPMI）方法的3维扩展形式，由5个随机航点生成参考路径，相邻航点间距为50米，起点为NED坐标系原点。

对比算法：选取模型预测控制（MPC）以及其他基于强化学习的算法（A2C、PPO、SAC）作为对比算法，所有算法中AUV的巡航速度均由传统PI控制器维持在1.5 m/s。

评价指标：以航向误差、elevation误差和总跟踪误差作为评价指标，成功跟踪定义为AUV 到达最后一个航点周围1米的接受半径内。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po4P7lO6CK0iaxFeiadMHqMOOl6HymBJZaJOa6bPLYhSVd63Jg47whnY5PQ/640?wx_fmt=png&from=appmsg)

图3.五种控制方法下自主水下航行器（AUV）的三维路径图

如图3所示，在两种环境下，五种方法均能使AUV跟踪给定路径，但A2C方法的控制效果较差，AUV在两种场景下均明显偏离参考路径；SAC方法的跟踪误差较大，尤其是在有海流的干扰环境中；MPC在理想环境下跟踪效果较好，但在海流干扰下偏差显著；PPO和 ModelPPO的跟踪效果较好，其中ModelPPO的路径与参考路径最为接近。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po47B8xEeHDGia7t9XShcRpQ1rjOgMsW8BAn2oxkgJtytNibAciciaS3FCpDQ/640?wx_fmt=png&from=appmsg)

图4.五种控制方法的位置跟踪误差图

如图4所示，MPC 的跟踪误差在整个时间段内分布相对均匀，而基于强化学习的方法在路径曲率较大的时刻（约 45s、65s、90s）跟踪误差会突然增大。总体而言，ModelPPO 在两种环境下均取得了令人满意的跟踪结果，其次是 PPO。在有海流干扰时，ModelPPO 的误差增长幅度远小于其他算法，进一步验证了其鲁棒性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po4PliaXwkjlmD4LZTOKAUt2n6ZtwBwVPFFrSKj6FpbnqiazYPtZPkAI11A/640?wx_fmt=png&from=appmsg)

图5.五种控制方法的控制输入

如图5所示，MPC 的控制输入最大，且在干扰环境下波动剧烈，这是因为 MPC 需要通过增大控制输入来克服模型偏差导致的跟踪误差。相比之下，基于强化学习的方法控制输入更小且波动平缓，在节能方面具有明显优势。在有海流存在时，所有控制方法的控制输入均有所增加，这是由于海流干扰导致 AUV 偏离参考路径，需要调整控制输入以尽快回到期望路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po4bdkJkZI4OqK1dIQU826MiaNtLM84wXeKZOqzLHAGl0r3z6GLaNkYC6w/640?wx_fmt=png&from=appmsg)

图 6.基于强化学习（RL）方法的训练曲线

如图6所示，在无干扰的理想场景中，SAC的训练效率最高，ModelPPO在约80,000 个episode时收敛，比PPO算法快约30%，且最终奖励值最高。在有海流的场景中，ModelPPO 的训练初期进展较慢，但随后快速提升，与PPO大致在相同时间收敛。SAC作为离线策略方法，训练效率高但训练效果不佳，在干扰环境下甚至无法收敛；A2C在两种场景下的最终奖励均显著低于PPO和ModelPPO。综合来看，ModelPPO在训练效率和训练效果方面均表现最优。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po46LrUOqL2d13GWpC1G8GwJ8jVpDULIEBBQTswAFRJJibheKBtnTGaIXA/640?wx_fmt=png&from=appmsg)

图7.存在初始定位误差时自主水下航行器（AUV）的三维路径图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMcBEHuGb68n4rufkia7l7po4JYFECA14ThJGo6Q1mmyP1qODMuLDUyD24LFxZzCibqphTicMJf5OJRvA/640?wx_fmt=png&from=appmsg)

图8.存在初始定位误差时的位置跟踪误差图

为验证 ModelPPO 在初始定位存在误差情况下的性能，随机选取初始位置坐标进行测试。如图7和图8所示，在理想环境和干扰环境中，尽管存在初始误差，但 AUV 仍能成功紧密跟踪参考路径。初始时刻由于 AUV 初始位置与参考路径起点存在差异，跟踪误差较大，但随后误差逐渐减小，表明 ModelPPO 能够在 AUV 出现显著偏离时使其回到期望路径。

05  总结

本文针对AUV的3D路径跟踪问题，提出了一种新的基于强化学习的控制策略，设计了名为ModelPPO的算法。该算法融合了神经网络模型和先进的强化学习算法PPO，其中神经网络模型用于拟合AUV系统的状态转移函数，学习策略对状态的影响，并为PPO提供额外信息。在复杂海洋环境中，AUV会遭遇各种未知扰动（如随机扰动、海流等），由于代表AUV动力学特性的模型网络能够定期更新，即使在这些扰动下，路径跟踪任务仍能圆满完成。

仿真实验验证了基于ModelPPO的控制器的可行性和鲁棒性。在无海流环境中，其跟踪误差相较于SAC、PPO和A2C分别降低了49.7%、15.8% 和 84.8%；在有海流环境中，跟踪误差相较于MPC、SAC、PPO和A2C分别降低了49.1%、61.3%、30.9%和88.4%。

未来工作中，将把所提出的方法应用于多AUV编队控制，并开展真实AUV 的实验研究。在仿真平台中训练的算法可作为真实环境中的预训练模型，以减少实际训练数据的采样需求；若能获取真实世界的训练数据，需对强化学习控制算法进行重新训练，确保其在真实环境中能够有效工作，进一步探索强化学习技术在AUV控制中的应用潜力。

END

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ASlHg58pYMcBEHuGb68n4rufkia7l7po4R9H9iaGRotNvIVvsNT1tkibgrbB9QicL2YVVzKvNwnIjj9rZicVibMHjubg/640?wx_fmt=jpeg&from=appmsg)

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

![](http://mmbiz.qpic.cn/mmbiz_png/ASlHg58pYMe1HLLDN2MwVD3d9iaphI4E...