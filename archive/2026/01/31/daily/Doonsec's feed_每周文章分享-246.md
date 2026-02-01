---
title: 每周文章分享-246
url: https://mp.weixin.qq.com/s/KCvGZaFemXKRcmD2JNFHJw
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:24:35.171277
---

# 每周文章分享-246

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oawJlbewO4fyxFXb125ZMMWxm0ib9jOdf7N6ArS0Uj5MdPalkqcoM38kg/0?wx_fmt=jpeg)

# 每周文章分享-246

网络与安全实验室

![]()

在小说阅读器中沉浸阅读

每周文章分享

2026.01.26至2026.02.01

**标题:**Sequential Asynchronous Action Coordination in Multi-Agent Systems: A Stackelberg Decision Transformer Approach

**会议:**International Conference on Machine Learning (ICML), 2024.

**作者:** Bin Zhang, Hangyu Mao, Lijuan Li, Zhiwei Xu, Dapeng Li, Rui Zhao, Guoliang Fan.

**分享人:**河海大学——刘渊

01  研究背景

在多智能体系统（MAS）中，智能体不仅需要通过与环境交互最大化个体收益，还需与其他智能体动态协调以实现最优集体策略。多智能体强化学习（MARL）虽为解决该问题提供了有效途径，但仍面临严峻挑战：现有主流方法多聚焦于完全协作任务，且假设所有智能体同步行动，难以应对更具通用性的混合任务（包含协作与竞争动态）及现实场景中普遍存在的异步行动协调问题。博弈论为解决智能体间交互提供了有力框架，其中斯塔克尔伯格博弈（SG）明确建模了智能体间的连续异步行动协调，通过“领导者——追随者”的层级决策结构实现优化。然而，现有基于SG的MARL方法在网络架构和环境设置上存在严格限制：仅适用于共享状态环境，且需按序更新各智能体策略，导致学习成本高昂、扩展性差。近年来，自然语言处理领域的自回归序列模型为强化学习带来新的突破。本文核心洞察在于SG的层级决策结构与自回归序列模型的建模方式高度契合，据此提出一种全新方法，有效解决异步行动协调中的上述难题。

02  关键技术

本文提出斯塔克尔伯格决策Transformer（STEER），融合SG的层级决策结构、自回归序列模型的建模能力及MARL的探索性学习方法，高效处理多智能体决策过程。其创新与贡献如下：。

1）首次将自回归序列模型与SG框架结合，提出启发式斯塔克尔伯格决策机制（SDM），自然实现斯塔克尔伯格均衡（SE）策略的收敛，突破传统同步决策假设的局限。

2）设计双Transformer架构（Inner Transformer Block + Outer Transformer Block）的Stackelberg Decision Transformer（STEER），灵活适配多种环境配置（部分观测/全局共享状态、连续/离散控制、完全/不完全协作任务）。

3）支持并行更新所有智能体策略，大幅降低传统SG-based MARL方法的计算成本；同时通过知识蒸馏模块，实现去中心化执行扩展，兼顾训练效率与部署灵活性。

03  算法介绍

**（1）斯塔克尔伯格博弈（SG）**

斯塔克尔伯格博弈是一种经典博弈论框架，核心特征是层级化决策结构，明确区分“领导者”和“追随者”两类角色。领导者拥有决策优先级，先承诺自身行动策略，追随者观察领导者的行动后，选择对自身最优的响应策略。领导者会预判追随者的最优响应，进而选择自身最优策略，最终收敛到斯塔克尔伯格均衡（SE）。对于两智能体场景，该均衡可形式化为双层优化问题：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oayxBmOzRCbrsuHelDBEvWq6ZWhSVlicicOvwy9gALvUiaHZCqXibgg0cjjg/640?wx_fmt=png&from=appmsg)

其中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oa0d9albE0djl8yARtah8hOtGBmD5EJicpYv97wXNfQrxtxFBWrI7fsHw/640?wx_fmt=png&from=appmsg)

**（2）启发式斯塔克尔伯格决策机制（SDM）**

为扩展SG至n智能体场景，为每个智能体分配优先级h^I，形成n层级优化问题。SDM中，每个智能体同时扮演“上级领导者”和“下级追随者”双重角色。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oaZu5qMKUvh2z5TgC1x8dS3rDNsicTIxuCxSDuVicXCs8BxDJ2VPjibamZw/640?wx_fmt=png&from=appmsg)

图1 提出的SDM架构

追随者在执行和训练过程中接收上级智能体的决策信息，按对领导者的最优响应方向更新策略梯度。领导者将下级智能体视为环境一部分，通过与环境交互感知追随者反应，最大化自身私有收益。这种机制天然缩小追随者的行动空间，避免策略冲突，同时能自然收敛到SE点，提升协作效率。多层优化的公式如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oa3rYHibk0akXdWbRBqWFGRShNd5tW2bTRcxOUVGItyadjmnlIEhltkAg/640?wx_fmt=png&from=appmsg)

**（3）STEER架构设计**

STEER（Stackelberg Decision Transformer）的核心是双Transformer架构，专门适配斯塔克尔伯格博弈的层级决策逻辑，同时兼容多种环境配置和训练需求，其结果如图2所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oa9RnB9YFWfKchgu4L9srEtGJjTmicUWhvHtrK2xJIeme9ibvRiaaLUcKSA/640?wx_fmt=png&from=appmsg)

图2 提出的STEER架构

STEER 的核心设计理念是将智能体间的层次化异步决策过程，建模为一个序列生成任务。其Inner Transformer Block（ITB）负责处理不同环境配置的状态信息，通过多头自注意力机制捕捉智能体间的状态关联，将全局状态和智能体局部观测映射为全局状态嵌入和智能体特定状态嵌入，可灵活支持共享状态、局部观测等多种场景。

Outer Transformer Block（OTB）则以全局状态嵌入和优先级靠前的智能体动作序列为输入，借助掩码多头自注意力机制自回归生成各智能体的决策信息，完美适配斯塔克尔伯格博弈（SG）的连续决策结构。

Actor-Critic Heads会结合ITB和OTB的输出构建子游戏状态嵌入，其中Actor头用于生成动作策略，Critic头负责估计状态价值。

整个训练范式基于近端策略优化（PPO）实现端到端训练，策略网络通过最大化裁剪目标函数优化策略。价值网络则通过最小化贝尔曼TD误差提升价值估计精度，且训练阶段支持联合动作序列并行计算，大幅提升了训练速度。

**（4）去中心化执行扩展**

STEER模型本质上是集中式的，在训练和执行时，它的Outer Transformer Block需要按智能体优先级顺序地、自回归地生成每个智能体的动作。这意味着，在运行时，智能体i的动作生成依赖于智能体1到i-1的真实动作。这要求所有智能体的观测信息必须集中到一个中心节点进行处理，或者智能体之间进行顺序通信，这在许多现实分布式系统中（如自动驾驶车队、无人机集群）是不切实际或低效的。为解决 STEER 架构集中式训练与去中心化部署的适配问题，文章引入知识蒸馏模块构建去中心化执行方案，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oaDUjby2bRv6T0jMqUr7vxd02x30cHaBJvkq7C0ygsJIdxuCeernNIaA/640?wx_fmt=png&from=appmsg)

图3 知识蒸馏模块

学生网络架构是为每个智能体i构建一个简单的多层感知机。该MLP的输入仅是智能体i的局部观测o\_i，输出是其动作策略分布。蒸馏目标不是让学生网络直接学习环境奖励，而是让它模仿教师网络（STEER）的决策行为。具体来说，是让学生网络学会在给定自身观测下，以与教师网络（在给定全局状态下）相同的概率选择教师网络认为最优的动作。

论文中使用的蒸馏损失函数是一个结合了对数均方根误差和香农熵正则项的复合损失：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oaFC2a7NaoDIPU19JAdDTyD6FfCDZqNV72Aiaia2uHMGwtvqsaicAPBemAA/640?wx_fmt=png&from=appmsg)

知识蒸馏降低学习难度。学生网络无需从零开始解决复杂的多智能体协调问题，只需学习一个相对简单的“模仿”任务：复制教师的行为模式。同时还保留Stackelberg均衡特性。教师网络STEER已经学会了Stackelberg均衡策略。通过精确的行为模仿，学生网络继承了这一均衡策略的精髓，从而在分布式执行时仍能维持高效的协调能力。训练完成后，每个智能体的MLP可以独立运行，无需通信全局状态或其他智能体的实时动作，满足了实际系统对低延迟、高可靠性的要求。

04  实验结果分析

**（1）SE策略收敛验证**

作者首先用简单的矩阵游戏场景对STEER进行性能验证，场景如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oaRX7lnTyDhU4yibzVhfNPa2gqknunBNs6OoE2ibheWyw928ELRB1yJicXA/640?wx_fmt=png&from=appmsg)

图4 矩阵游戏场景

单步矩阵游戏包含Penalty和Mixing两个子场景，均为离散控制的混合任务（含协作与竞争动态），环境配置为共享状态和固定状态；其中 Penalty 场景的收益矩阵中包含惩罚项k，任何智能体偏离最优策略都会对做出正确决策的另一方造成严重惩罚，k的绝对值越大，智能体学习SE解的难度越高，而Mixing场景则通过非对称的收益分布，测试算法在智能体存在私有奖励时的协作协调能力。多步矩阵游戏则包括Coordination和Cooperation两个子场景，同样为离散控制任务，但环境配置为独立全局状态，需要智能体通过多步交互、持续协作才能获得最终奖励。算法的收敛曲线如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oaMiboPyN5jicCicXZQDdeRic7QcNibhQeQ7aDyns9avXLPuMkZEAOkcnGgpw/640?wx_fmt=png&from=appmsg)

图5 矩阵游戏收敛曲线

从图中可以看到，STEER 在所有矩阵游戏场景中均能稳定收敛到SE，获得最优平均收益。而其他基线算法多陷入次优纳什均衡，收益显著降低。

**（2）复杂场景**

为验证STEER在真实多智能体交互场景中的适应性和优越性，文章选取3类主流复杂仿真环境，覆盖连续/离散控制、全合作/混合任务、共享/局部状态等多样化配置，核心对比STEER与基线算法的性能差异。3个场景分别为Multi-Agent MuJoCo、Google Research Football、Highway On-Ramp Merging。下图是STEER与4类基线算法在3类复杂场景中的性能对比图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oaYFic7kiadsOcyCKFhkf9vegoBFmOuBqmWTzD3FXbblSYyJdxmA1Q9uQQ/640?wx_fmt=png&from=appmsg)

图6 复杂场景收敛曲线

STEER在三个场景中均展现出全面且显著的优势，其收敛速度比基线算法快30%以上，最终平均收益比最优基线高10%-25%，且95%置信区间最窄、性能最稳定；相比之下，MAPPO、HAPPO等经典MARL方法难以适配混合任务和动态协作需求，MAT因缺乏Stackelberg层级决策机制导致协作效率不足，STEP则受限于共享状态假设且收敛缓慢，这些基线方法在偏离适场景后性能均出现明显下降，而STEER凭借双Transformer架构和 Stackelberg 决策机制，灵活适配了离散/连续控制、全合作/混合任务、共享/局部状态等多样化配置，充分验证了其在复杂多智能体交互场景中的优越性和通用性。

05  总结

本文提出了一种新颖的多智能体异步协调框架STEER，其核心创新在于将Stackelberg博弈的层次化决策结构与Transformer的自回归序列建模能力深度融合，通过内部Transformer模块灵活处理环境状态、外部Transformer模块以掩码自注意力实现顺序决策生成，从而引导智能体自然学习Stackelberg均衡策略。实验表明，STEER在矩阵游戏中能稳定收敛至理论均衡，在Google Research Football、Multi-Agent MuJoCo及高速匝道汇合等复杂场景中均显著优于主流基线，且通过知识蒸馏实现了高效的去中心化部署，在计算效率、环境适应性和实际可扩展性方面展现出显著优势，为多智能体系统的异步协调问题提供了兼顾理论严谨性与实践效能的通用解决方案。

END

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ASlHg58pYMeX4K7YXm3NJia3ONhDsf9oamzN2KYONLNDHA2kWRnUUFEcS7teogTq7I4KHku95FCMKxLW0eVUIRg/640?wx_fmt=jpeg&from=appmsg)

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

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ASlHg58pYMe1HLLDN2MwVD3d9iaphI4Evp3oib9RPtU2gOR3ubr5qzibTwSBgaJgJ52tuI5knfsB9ECKibfibAt40KA/0?wx_fmt=png)

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