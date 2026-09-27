---
title: 每周文章分享-277
url: https://mp.weixin.qq.com/s/8GDe9i0Lzrk4JCHOHMZ1wA
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:23:56.679549
---

# 每周文章分享-277

# 每周文章分享-277

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4DAaJy0Ok82ibMPxwHY4mibwrjmLoqmvIickMFksSta2uNYdIpd6BSh7GAKsqdYvoQq3Sg4RqvtofvuJLvGnIwDAIicnMN8A6wjias/640?wx_fmt=png&from=appmsg#imgIndex=56)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd79GRlwNhZak3b6NicAtrelJ5wXr5U8icCFGbOq9olPBSsVfSynibKpYAErrW6LMx4lyXdp5ibny1uCN8uPlrgJQNibuH3hYkIW2aBo/640?wx_fmt=png&from=appmsg#imgIndex=57)

**每周文章分享**

2026.09.21至2026.09.27

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4Ohaz7tlbUgBU08mJu9dD8frItmtjJ1C9xvR9d9Gic4CYK1bBjJA40NMpK6T89bFlj2aNTod2cSPT666sMXxIEia1FJy7QbLnrQ/640?wx_fmt=png&from=appmsg#imgIndex=60)

**标题:**HMARL-CBF – Hierarchical Multi-Agent Reinforcement Learning with Control Barrier Functions for Safety-Critical Autonomous Systems

**期刊:**39th Conference on Neural Information Processing Systems (NeurIPS 2025)

**作者:**H. M. Sabbir Ahmad, Ehsan Sabouni, Alexander Wasilkoff, Param Budhraja, Zijian Guo, Songyuan Zhang, Chuchu Fan, Christos Cassandras, and Wenchao Li

**分享人:**河海大学——朱志行

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd7PdTwqxaMfpIS26krIsxls3gvlWl17nYzpFj5Zhtqcwy3z6MhbZh7hZmegdwno07C0icPN2GlR16gtHMFHOjswwUIO0ZHZRjKM/640?wx_fmt=png&from=appmsg#imgIndex=73)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***01.***

**研究背景**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

随着自动驾驶汽车、无人机、群体机器人以及自主水下航行器等多智能体自主系统逐步进入高动态、强交互的真实环境，智能体不仅需要通过协同决策完成整体任务，还必须在整个执行过程中持续满足碰撞避免、道路边界或障碍物规避等安全约束。传统多智能体强化学习通常将安全约束转化为奖励惩罚项，并利用一个扁平策略同时学习任务性能与安全行为，但随着智能体数量和交互复杂度增加，这种方式容易面临样本复杂度高、训练不稳定和可扩展性不足等问题，更重要的是，奖励惩罚只能在统计意义上鼓励安全行为，难以保证每一个时刻都不违反安全约束。已有基于约束马尔可夫决策过程（CMDP）的安全强化学习方法主要控制轨迹上的累计期望成本，本质上仍属于平均意义的安全，而安全关键系统往往要求“逐时刻安全”，即每一个时间步都必须满足约束。针对这一问题，本文提出HMARL-CBF，将层次化多智能体强化学习与控制障碍函数（Control Barrier Function, CBF）结合：高层策略负责学习多智能体之间的协同行为与技能选择，低层策略负责在执行具体技能时通过CBF强制满足安全约束，从而在集中训练、分散执行的框架下同时兼顾协同效率、可扩展性与形式化安全保证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***02.***

**关键技术**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

本文的核心思路不是直接让一个MARL策略输出连续控制量，而是将“协同决策”和“安全控制”拆分到两个时间尺度中。高层将每个智能体的动作抽象为具有明确语义和持续时间的技能，例如巡航、加速、让行以及左右换道，并通过MARL学习不同智能体在不同局部观测下应该选择什么技能；低层则把高层给出的技能转化为连续控制动作，并将CBF和控制Lyapunov函数（Control Lyapunov Function, CLF）写入一个参数化二次规划（Quadratic Program, QP），使安全约束直接成为控制器必须满足的硬约束。与此同时，QP中的目标权重、CBF参数和CLF收敛参数并非固定，而是由神经网络根据当前观测和技能进行学习，因此整个低层安全控制器仍可通过策略梯度进行优化。

控制障碍函数的关键思想是先利用函数b(s)定义安全集合C={s | b(s)≥0}。如果控制动作a始终满足下式，则从安全集合内部出发的状态轨迹能够保持在安全集合中，即具有前向不变性：

L\_f b(s) + L\_g b(s)a + α(b(s)) ≥ 0

与单纯在Reward中增加碰撞惩罚不同，这一约束直接作用于每个时间步的控制动作，因此安全性不再完全依赖强化学习是否“学会避障”。本文进一步利用CLF驱动智能体收敛到当前技能的目标状态，使“安全”和“完成技能”分别由CBF与CLF承担。

该方法的创新和贡献如下：

1）本文提出HMARL-CBF，一个基于集中训练、分散执行（CTDE）的安全层次化多智能体强化学习框架，将全局协同行为学习与个体安全技能执行解耦，并通过CBF在训练与执行阶段提供逐时刻安全约束。

2）本文构建了基于技能的双层决策结构：高层MARL在较慢时间尺度上选择联合技能，低层通过可学习的CBF-QP策略执行连续动作；这种结构既利用时间抽象降低了扁平MARL的学习难度，又使安全控制能够在每个智能体本地完成。

3）本文在多种高冲突道路环境以及额外的LiDAR多智能体环境中进行验证，在五类METADRIVE道路场景中取得接近100%的任务成功/安全率，并在时间、能耗和收敛速度等指标上整体优于多种MARL与安全MARL基线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***03.***

**算法介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

**（1）HMARL-CBF整体层次化框架**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2DalYoTDnoibWIXwmMARibZcse5TYibvRJk8ksmDa8mQH1hfcgSjMv0lic9PDibF4ibYe5GGOB8GK7XZdpBAGZvaOz0xsKEag5hYGz4/640?wx_fmt=png&from=appmsg)

图1  HMARL-CBF整体层次化框架

如图1所示，HMARL-CBF将多智能体决策分为高层策略和低层技能策略。对于智能体i，高层策略π\_H^i仅根据自身局部观测（以及需要时的历史信息）选择离散技能z\_i；随后低层策略接收当前观测与技能z\_i，并通过参数网络生成QP控制器所需参数，最终由CBF-QP输出连续控制动作a\_i。高层的学习目标来自任务相关的外部轨迹回报R\_H(τ)，用于优化所有智能体的整体协同行为；低层则使用每个智能体自身的内部轨迹回报R\_L^i(τ\_i)学习如何稳定、平滑地完成具体技能。高层和低层网络均在智能体之间共享参数，从而避免随着智能体数量增加而为每个智能体单独维护一套网络。

从决策逻辑上看，这一框架把原本“每一步都同时思考协作、避碰和连续控制”的困难问题改写为：高层回答“下一阶段应该做什么”，低层回答“怎样安全地把这件事做完”。因此，高层可以更加关注全局交通效率和智能体之间的配合，而低层把碰撞、道路边界等强安全条件交给控制理论约束处理。

**（2）基于技能的MSMDP与异步决策**

由于一个技能通常会持续多个环境步，HMARL-CBF不是使用普通MDP描述高层，而是采用多智能体半马尔可夫决策过程（Multi-Agent Semi-Markov Decision Process, MSMDP）。每个技能包含启动条件、终止集合、最大持续时间T\_max、安全约束集合、内部奖励以及对应的技能策略。技能有两种终止方式：一是智能体已经进入该技能规定的终止集合，说明技能执行完成；二是超过T\_max后强制结束，以避免技能无限持续。

更重要的是，本文采用异步的τ\_continue更新方式。当某个智能体的技能先结束时，只允许该智能体重新选择技能，其他尚未结束的智能体继续执行原技能，而不要求所有智能体同时切换。这使层次化策略更符合真实多智能体系统：不同车辆可以以不同速度完成“让行”“换道”或“加速”，无需为了同步决策而人为中断正在执行的行为。

在METADRIVE实验中，作者为每个智能体定义了5种具有明确语义的低层技能：巡航（Cruising）、加速（Speeding up）、让行/减速（Yielding/Slowing down）、左换道（Left Lane Changing）以及右换道（Right Lane Changing）。这些技能并非额外的规则控制器，而是由低层可学习的QP策略实现；高层只负责判断何时调用哪一种技能。

**（3）高层多智能体协同策略学习**

高层的目标是学习所有智能体在技能空间上的协同策略。由于技能持续时间不同，高层奖励R(s,z,k)累积当前联合技能z在k个环境步内产生的任务Reward，并在技能结束时用于更新高层策略。在CTDE框架下，训练阶段可以使用集中式Critic或价值分解利用全局信息，而执行阶段每个Actor只依赖本地观测独立选择技能。论文强调该高层并不依赖某一种固定MARL算法：基于策略梯度时可以使用MAPPO，基于价值分解时可以使用QMIX。实验中，on-policy版本采用MAPPO学习高层策略，off-policy版本则采用QMIX。

这种设计的意义在于，高层动作从连续转向、加速度等原子控制转换为“巡航/减速/换道”等较低维技能后，决策频率和有效动作空间都明显降低，多智能体协作因而更容易学习。例如在拥堵入口处，高层真正需要学习的是“哪些车辆先让行、哪些车辆保持速度、哪些车辆换道”，而不是直接在联合连续动作空间中搜索所有车辆每一个时间步的控制量。

**（4）CBF-QP低层安全技能执行**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1kUvHpwt6CZUd3oxmbLXbcMuzo0mzK5ibxXm3liaz29ia0tgLnDTwNPoNxERdQRAOp4JTMXxu2OgXF2M6MPmuDm0M5mkufPZhfSw/640?wx_fmt=png&from=appmsg)

图2  智能体间与环境安全约束示意图

低层是本文提供形式化安全保证的核心。对于每个智能体，作者根据与其他车辆和环境边界的相对状态构造安全函数b\_j^i。例如图2中，车辆之间可以根据相对位置、速度及安全半径构造碰撞约束，道路边界或收费站等静态环境也可以形成对应的安全约束。只要CBF约束始终成立，安全集合就保持前向不变，因此控制器不会为了追求更高Reward而主动选择违反安全集合的动作。

具体实现上，低层动作不是神经网络直接输出，而是在每一个时间步求解一个带CBF和CLF约束的二次规划：

min\_{a,e}  a^T H(φ\_H)a + F(φ\_F)^T a + φ\_e^T e

其中，QP目标主要衡量控制代价、跟踪误差以及CLF松弛项；CBF对应“不能进入危险区域”的硬安全约束，而CLF负责把速度、航向等状态逐步拉向当前技能的目标值。由于目标函数为凸二次形式、约束对控制输入为仿射形式，该问题可以在每个控制周期快速求解，适合实时安全控制。

HMARL-CBF与传统“CBF安全过滤器”还有一个重要区别：QP中的H、F、CBF类K函数参数、安全区域大小以及CLF收敛率等参数由网络Γ\_ν(o\_i|z\_i)根据当前观测与技能动态生成，而不是人工固定。论文利用QP最优解对参数的梯度以及策略梯度对这些参数进行学习，使低层既保持CBF结构带来的安全性，又能够针对不同交通状态自动调整控制器的保守程度和技能执行方式。

**（5）高低层联合优化与任务对齐**

如果低层只追求“把技能做得平滑”，可能出现技能本身执行正确但并不利于整个多智能体任务的问题。为此，作者除了设置低层内部Reward外，还将高层策略的优势函数A^{π\_H}引入低层奖励，用系数λ在“全局任务收益”和“技能内部收益”之间进行权衡：

r̃\_L^i = λ·A^{π\_H}/N + (1−λ)·r\_L^i

这样，高层如果发现某种技能组合真正提高了整体交通效率，对应的优势信息会反向影响低层技能参数，使低层不是孤立地优化局部行为，而是逐渐与高层协同目标保持一致。理论上双层问题可以顺序求解，实际实现中作者采用交替更新高层与低层参数的方式进行联合训练，并让两层共享同一批交互数据，因此层次化分解没有额外引入独立的数据采集开销。论文进一步证明，只要低层QP中的CBF约束得到满足，各个安全技能对应的轨迹就保持在安全集合内，从而给出整个HMARL框架的安全保证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***04.***

**实验结果分析**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

本文主要在METADRIVE复杂道路网络中验证HMARL-CBF，同时在额外的LiDAR多智能体环境中测试方法的泛化性。METADRIVE包含Merging、Intersection、Roundabout、Bottleneck和Tollgate五类高冲突场景，各车辆从随机起点生成并被分配随机目的地；成功到达目的地记为成功，与其他车辆碰撞或驶出道路则记为失败。训练时Merging使用15辆车，Intersection和Roundabout各30辆，Bottleneck使用25辆，Tollgate使用40辆，环境运行过程中还会持续生成新车辆，因此实际同时参与交互的智能体数量可能进一步增加。实验同时给出on-policy和off-policy版本，并与CoPo、IPPO、MFPO、Curriculum Learning等方法比较，在总体性能评估中还加入MAPPO-Lagrangian和MACPO等安全MARL基线。本文主要通...