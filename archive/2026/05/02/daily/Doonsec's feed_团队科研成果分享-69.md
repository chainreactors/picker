---
title: 团队科研成果分享-69
url: https://mp.weixin.qq.com/s/5MBIcgzl0fA0DtUKcUd31A
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:28:05.057601
---

# 团队科研成果分享-69

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jBQAokCLibp1tNA8N38geibzibuP4pVsfiaiaZn8RIwvBAPH7NDU6sbw9PhtH61WkCT7XxPGNl4OicVwibrtXW3MhiboG5NBU0XuDWicT8XwY5s6R7M8/0?wx_fmt=jpeg)

# 团队科研成果分享-69

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jBQAokCLibp3hXnicZ06ZEmgwibPKib9JCtJvmq8qfl7UYicsMGzIRfZmrKfl4xo05OEDI86dSkicvNicAXzYuWJkBK5EM519Kqc1htfOEZicc5RZIE/640?wx_fmt=jpeg&from=appmsg)

**团队科研成果分享**

2026.04.27-2026.05.03

**标题:**Multi-AUV Path Planning based on Stackelberg TD3 Framework with Adaptive S-surface Control for IoUT Data Collection

**期刊:**IEEE TRANSACTIONS ON MOBILE COMPUTING

**作者:**Yuanbo Zhu, Guangjie Han\*, Chuan Lin, Fan Zhang, and Yun Hou

**分享人:** 河海大学——祝远波

**01**

**研究背景**

**BACKGROUND**

**研究背景**

水下物联网在环境监测和数据收集等任务中至关重要，AUV是执行这些任务的核心载体。然而，在实际海洋中实现多AUV协同路径规划面临严峻挑战。复杂的环境因素导致航行器运动漂移、路径不准及控制力减弱。传统的模型驱动控制器过度依赖精确建模与繁琐调参。在面对存在未建模扰动的动态海洋场景时，其适应性极差，易导致碰撞风险增加和效率低下。因此，基于强化学习的路径规划方法凭借处理高维、非线性系统的优势成为主流。RL通过环境交互学习鲁棒策略，降低了对物理模型的依赖。尽管如此，现有RL框架仍面临两大应用瓶颈：第一，训练极不稳定。常规方法将actor与critic网络分离优化，忽略了两者间的博弈互动，在复杂水下易引发严重震荡与收敛困难。第二，存在控制鸿沟。RL生成的高层离散策略难以在极端洋流干扰下，直接且稳定地驱动六自由度AUV物理动力学系统。综上所述，当前亟需一种具有分层架构的新型控制策略，以同时兼顾全局多智能体协同训练的稳定性，并有效弥合高层战略规划与底层物理执行之间的鸿沟。

**02**

**关键技术**

**TECHNOLOGY**

**关键技术**

针对水下物联网数据收集中的AUVs路径规划问题，本文提出了一种基于Stackelberg双延迟深度确定性策略梯度与自适应S面控制器的协同路径规划框架。其关键技术有1） Stackelberg博弈优化的Actor-Critic机制：将Actor和Critic的交互建模为两人一般和Stackelberg博弈，其中Actor作为领导者，Critic作为跟随者。Actor通过显式预测Critic的反应，利用隐式梯度机制更新优化自身策略。这有效克服了复杂水下环境中多智能体非平稳交互带来的训练震荡，大幅加速了算法收敛并提升了训练稳定性。2）跨越控制鸿沟的分层规划架构：采用高层战略协调与底层鲁棒控制相结合的分层架构。该架构将STTD3模型生成的高层连续动作策略无缝转化为精确的底层控制信号。这从根本上解决了传统强化学习高层离散策略难以在极端洋流下稳定控制六自由度AUV动力学系统的控制鸿沟难题。3）自适应S面控制器：在底层控制中引入自适应S面控制器，将高层动作向量映射为物理参考指令。该控制器通过非线性映射提供平滑饱和特性，将控制输入限制在合理范围内，既能结合速度反馈实现快速阻尼响应，又能避免过度震荡，确保了面对未建模扰动时的鲁棒局部控制。

该方法的创新和贡献如下：

1）构建了解决IoUT数据收集多AUV路径规划问题的STTD3-ASC框架，在实现水下场景自适应可靠控制的同时，显著增强了训练鲁棒性并加速了收敛。

2）提出基于Stackelberg的TD3模型，允许领导者通过全导数更新参数，跟随者使用标准梯度更新，加速了全局最优策略的搜索。

3）设计了自适应S面控制器以转化高层协同策略，在海洋场景的实验测试中，该模型在避免碰撞、提高数据收集率以及降低系统能源消耗等核心指标上，均实现了大幅度的实质性改善。

**03**

**算法介绍**

**ALGORITHMS**

**算法介绍**

**（1）问题描述**

本文研究的核心问题是水下物联网数据收集中的AUVs路径规划问题。求解该问题并将其应用于复杂动态的真实海洋场景面临以下的核心挑战：首先是强化学习的训练不稳定难题。大多数现有的RL框架通常将actor和critic网络分开进行独立优化，忽略了两者之间固有的博弈互动关系。在复杂多变的水下环境中，这种非平稳交互往往会导致严重的训练震荡，使得模型收敛性极差。其次是高层规划与底层执行之间的控制鸿沟。真实的海洋环境充斥着强烈的洋流干扰、复杂的地形限制以及高度非线性的动态特征，经常导致航行器的运动发生严重漂移。综上所述，如何设计一种既能稳定多智能体协同训练过程、克服网络交互非平稳性，又能有效弥合高层战略规划与底层物理执行之间鸿沟的鲁棒自适应路径规划框架，是本研究亟待解决的关键问题。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2cwa72ib99UibYYg3Sv3jZPXKkZibuAKqW97cGkFRuLIPfdzh5Gia6DuiaT8OatsJP5A1aqY62WtiawdaribOfg6Q8kjlztrFoox9e8w/640?wx_fmt=png&from=appmsg)

图1 多智能体强化学习路径规划在IoUT数据采集中的应用

**（2） 基于FIM的USV定位方法**

![image.png](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2ouAAcjmia10B0Fj2I408v162mUia7iczy2Fy2nTdBSzGQIkyrBnJURlOGiawicia8jdnKMc1RgiacpQWom3OGibaEAb8hvIQYvG0m318/640?wx_fmt=png&from=appmsg)

图2 USV路径规划示意图

图2展示了USV路径规划的示意图。该图详细阐释了USV与水下多AUV系统之间的协同定位与导航框架。在运行过程中，位于水面的USV配备了超短基线声学系统，用于测量底层各个AUV（如图中所示的AUV 1、AUV 2和AUV 3）的相位差向量。USV的移动路径是通过最大化Fisher信息矩阵（FIM）的行列式来决定的，该矩阵的行列式与多AUV系统的定位不确定性呈反比关系，以此来不断降低水下编队的定位误差。通过这种复杂的数学优化，系统可以计算出当前时间步下USV的最优水平位置。随后，USV会主动向该最优位置移动并测量更新后的AUV位置，在每一个时间步不断重复这一优化过程，从而生成一条动态优化的移动轨迹。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3SyeR7mgYkILM9icDrJD2obW5VgJaga51c0PxHcbBa4fickQROFJH8gpSzwOAibLpXgSicdhZZroCeJLhMDfPKvq11P9EzyOvcmKQ/640?wx_fmt=png&from=appmsg)

图3 STTD3-ASC框架

图3展示了本文提出的STTD3-ASC框架。该框架专为在中心化训练与去中心化执行范式下，解决水下物联网数据收集的多AUV协同路径规划问题而设计。其核心运行机制包含三个主要环节：首先，STTD3模型中的Actor网络根据从模拟环境中提取的局部观测数据生成高层动作策略，而Critic网络则通过评估中心化的状态价值来指导和细化策略学习。其次，在网络参数优化方面，框架引入了独特的Stackelberg更新过程，通过计算包含共轭梯度的隐式梯度项：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2PUJQIK81mdK1kv3qbYdqicauneCJ0Eib71dvicpgpaGE1FdAyq8KskA79RicF0L7pwibywblMH4IIziaxSZ1o8xjzvxLqK0YF5Uia5U/640?wx_fmt=png&from=appmsg)

允许Actor（作为博弈中的领导者）在更新参数时能够显式地预测并适应Critic（作为跟随者）的响应，从而大幅增强了训练的稳定性与收敛效率。最后，自适应S面控制器接收生成的高层动作指令，将其精准转化为底层的物理控制信号并作用于真实的物理仿真环境，由此成功构建了一个将高阶多智能体战略协调与底层物理模型鲁棒执行紧密结合的完整分层控制闭环。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp09ynp8ficontjczAwafg93A69plKb9GtQsdaxh9icxg3lDs6bcIq6rnoibrGicAIUOHHfBeHwb9qWTzTUPwh45ONj1EMSGsppk5A4/640?wx_fmt=png&from=appmsg)

图4 S-曲面控制器

图4展示了自适应S面控制器的控制输出与位置误差e\_x及速度误差e\_v之间的三维曲面及切片映射关系。该控制器的核心控制律公式定义为{2/[1+exp(k\_1\*e\_x+k\_2\*e\_v)]}-1，它巧妙地将位置与速度误差的线性组合平滑地映射到有界区间(-1,1)内。从图中特征可以看出，当控制增益k\_1>0时，该函数关于组合误差单调递增，且其过零点精确出现在e\_x=-(k\_1/k\_2)\*e\_v处。特别是在过零点附近的小误差区域内，控制器关于e\_x的局部增益为k\_1/2，这意味着在此区域该非线性映射可近似等效为线性表达式1/2(k\_1\*e\_x+k\_2\*e\_v)。这种精心设计的非线性映射机制不仅为底层物理控制信号提供了极佳的平滑性，还通过其内置的饱和特性将控制输入严格限制在安全范围内，从而有效减少了系统运动的超调量，防止了控制发散。

**04**

**实验结果**

**EXPERIMENTS**

**实验结果**

**（1）仿真参数设置**

表1、表2和图5共同确立了文章的实验环境。表3展示了STTD3-ASC框架的超参数。

表1 MAPP水下数据采集场景的实例

![image.png](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp35THeXupAk4SpXZKlaicfI6CHTE7QiaYMCPHpN8lRPr6qQtOnDHELISQJKSNSTUmliaOUyVCGcniaNHOFffUAOoQKQgw8dKyEYnAI/640?wx_fmt=png&from=appmsg)

表2 实验环境参数

![image.png](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2icuoDRmRNsSTP60SOjwACicUWEDVWDlI9HgHFrBExliaThEKTbFp3lnxVf372zb7ibL2Dluvtg0BWV7b8pRS6gtlGUp2pyU67ynM/640?wx_fmt=png&from=appmsg)

表3 STTD3-ASC超参数

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3UsayhEib4OyVRaian4ngAZOosWHW5jW1tNgxhqxhVv9YE4w2iaias5BVKmXicJr1QkgxnsbJOPLSCOhCxb3q7LJCsLXwStxMBPKPY/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3icJPRkIatnNrNWaN1vicdVV6bq19tLmp5icrcSlfbzCPeiat04EUjjV6NoWMGy0Bry8Vcf1TsejODcVRdR8l1gycX4nl3fDxdegk/640?wx_fmt=png&from=appmsg)

图5 场景2可视化

消融实验：1）MADDPG, 2）SAC, 3）PPO, 4）hierarchical RL, 5）A\*, 6）APF and 7）RRT\*

性能评价指标：

1）总速率（SR）代表所有AUV的数据传输速率之和。

2）信息数据利用率(IDU)表示在仿真过程中，每艘AUV成功从目标点收集或上传数据的效率或频率。

3）能耗(EC)表示仿真中AUV的总能耗。

4）数据溢出次数(ND)表示在当前模拟步中，其数据缓冲区已达到或超过最大容量的传感器节点的数量。

5）碰撞分数(CS)是一项累积惩罚指标，涵盖模拟过程中AUV与AUV之间的碰撞、地形碰撞以及边界越界情况。

**（2）仿真结果与分析**

图6展示了不同学习率对所提出的STTD3-ASC框架收敛性能的显著影响。从图中可以直观地观察到，当采用相对较小的学习率（例如0.0012和0.0016时，模型训练表现出收敛速度缓慢的特性，并且最终未能达到令人满意的全局奖励水平。相反，当使用过大的学习率（例如0.0004和0.0001）时，虽然能够在初期有效加速收敛，但最终会导致模型获取的平均奖励降低，并伴随着明显的训练震荡现象。为了平衡收敛速度与最终奖励的稳定性，研究通过对比选定了0.0008这一居中的学习率作为最佳参数设置。该设置在避免剧烈震荡的同时实现了最优的收敛效果，并被统一应用于后续的所有实验评估中。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2bIBkQurwiaaLLlic77z8nqDbN7qSM8GibNn3UjqliaKV6YjwWlRZngD9d9lMb7H5k4GxGmTXKmPmL3qNGnmB7wJnFFpclO3clEJY/640?wx_fmt=png&from=appmsg)

图6 学习率消融实验

图7展示了验证所提框架各核心组件有效性的消融实验结果。从实验数据可以看出，完整的STTD3-ASC框架在第1311个回合即可收敛至-49185.17的奖励值，显著优于标准TD3基线算法（在第2053个回合仅达到-57247.42）。实验结果充分验证了各模块的独立贡献：Stackelberg机制的作用：该机制使得Actor能够预测Critic的反应，与未包含该机制的模型相比，有效提升了全局策略的最优性，并实现了更快的收敛和更高的奖励稳定性。自适应S面控制器的作用：ASC模块在高度非线性的水下动力学环境中提供了鲁棒的底层执行保障，进一步加速了模型的整体收敛过程并确保了物理控制的稳定性。综合来看，通过将基于博弈论的战略更新与自适应物理控制相融合，该分层架构较标准TD3算法的收敛时间大幅缩短了36.1%，最终奖励提升了14.1%。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0k4uCXPMS7PpSYdoRhDiaLXic5GA91MCENnAQ4coTczgw6lKK3s93Efsib2cyicO1ZkxV9d8Yrxz55ldqcEkr8yPk5ic3pYWiaiblpicM/640?wx_fmt=png&from=appmsg)

图7 不同模块消融实验

图8展示了MARL框架在训练阶段的性能对比结果。数据显示，STTD3-ASC框架在最优收敛时间和最大奖励值上均展现出显著的优越性。具体而言，STTD3-ASC在第1311个回合即快速收敛至-49185.17的高奖励值，收敛速度大幅领先于其他RL框架。作为对比，其他基线算法（如TD3、HRL、SAC、PPO、DDPG等）分别在第1887、1434、1446、1878和1458回合才达到收敛，且最终奖励值仅介于-56679.33至-52997.33之间，表现均逊色于所提框架。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3ogZNQZWCoib9KIhrD911YWNhPnZP3t4V8Ie53ibbrDbIq6oTibZa3yP1U5Bco9rTsiciaOhTDcRDcdibvjJN8k6jCXO1ickn5frzlas/640?wx_fmt=png&from=appmsg)

图8不同MARL的对比试验

表4对比了不同MARL框架与启发式算法在SR这一核心指标上的性能表现。结果表明，本文提出的STTD3-ASC框架在所有测试场景中均展现出一致且卓越的性能，显著优于其他对比基线。具体而言，场景1：STTD3-ASC的SR达到218.79，较TD3基线提升了22.2%，较表现最佳的启发式算法（APF）提升了高达92.9%。场景2：SR达到296.57，较TD3和APF分别提升了12.1%和36.5%。场景3：SR达到298.87，较TD3和APF分别提升了9.4%和36.8%。场景4：SR达到285.72，比TD3高出1.1%，比APF高出44.2%。

表4不同强化学习框架在SR上的比较

![image.png](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3CNbY2jp8ScYy5IQ3OsPTzmHRQd6VovQvkFoggIZCdJyTicf1wL6ESQZgbCzhWemrwksAMNNvnPnCK10e3tuEiadxrMTxbegeek/640?wx_fmt=png&from=appmsg)

表5对比了不同MARL框架与启发式算法在IDU这一指标上的性能表现。结果表明，本文提出的STTD3-ASC框架在所有四个测试场景中均一致取得了最优性能。具体的性能提升如下，场景1：STTD3-ASC的IDU值达到174，较TD3基线算法提升了4.2%，较最佳的启发式算法（APF）大幅提升了54.0%。场景2：IDU达到258，较TD3和APF分别提升了9.3%和38.0%。场景3：IDU达到275，较TD3和APF分别提升了3.0%和50.3%。场景4：STTD3-ASC记录了最高的I...