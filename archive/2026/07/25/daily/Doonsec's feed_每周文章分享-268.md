---
title: 每周文章分享-268
url: https://mp.weixin.qq.com/s/MWDl5TkGRkR0gHiiKIP7BQ
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:23:48.951624
---

# 每周文章分享-268

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jBQAokCLibp0VHLLq7PBfTSUicgiaib17Hia5NgZ00E0rrW0bTDLZNIWcTMOIESONSKEH5hbdY6YefPVeWZTF36ETqgtNcJ20tkTjo7mibpV0Kn0s/0?wx_fmt=jpeg)

# 每周文章分享-268

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4DAaJy0Ok82ibMPxwHY4mibwrjmLoqmvIickMFksSta2uNYdIpd6BSh7GAKsqdYvoQq3Sg4RqvtofvuJLvGnIwDAIicnMN8A6wjias/640?wx_fmt=png&from=appmsg#imgIndex=56)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd79GRlwNhZak3b6NicAtrelJ5wXr5U8icCFGbOq9olPBSsVfSynibKpYAErrW6LMx4lyXdp5ibny1uCN8uPlrgJQNibuH3hYkIW2aBo/640?wx_fmt=png&from=appmsg#imgIndex=57)

**每周文章分享**

2026.07.20至2026.07.26

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4Ohaz7tlbUgBU08mJu9dD8frItmtjJ1C9xvR9d9Gic4CYK1bBjJA40NMpK6T89bFlj2aNTod2cSPT666sMXxIEia1FJy7QbLnrQ/640?wx_fmt=png&from=appmsg#imgIndex=60)

**标题:**Rainbow Delay Compensation: A Multi-Agent Reinforcement Learning Framework for Mitigating Delayed Observation

**期刊 / 会议:**39th Conference on Neural Information Processing Systems (NeurIPS 2025), arXiv:2505.03586v4, 12 Nov 2025.

**作者:**Songchen Fu, Siang Chen, Shaojing Zhao, Letian Bai, Hong Liang, Ta Li, Yonghong Yan.

**分享人:**河海大学——田檬

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd7PdTwqxaMfpIS26krIsxls3gvlWl17nYzpFj5Zhtqcwy3z6MhbZh7hZmegdwno07C0icPN2GlR16gtHMFHOjswwUIO0ZHZRjKM/640?wx_fmt=png&from=appmsg#imgIndex=73)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***01.***

**研究背景**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

多智能体强化学习（MARL）已经被广泛用于多人博弈、机器人协作、智能通信、量化交易等场景。相比单智能体任务，多智能体系统中的每个智能体通常只能获得局部观测，并且需要在其他智能体策略不断变化的条件下做出决策，因此天然面临非平稳性、部分可观测性、信用分配困难和维度灾难等问题。

在真实系统中，一个更加容易被忽视的问题是观测延迟。智能体看到的状态往往不是环境的真实当前状态，而是经过通信、感知或传输之后到达的旧信息。已有延迟强化学习研究多集中在单智能体或固定延迟情形。对于多智能体系统而言，延迟不仅会让观测滞后，还会加剧策略非平稳性和信用分配困难：智能体根据旧观测采取动作，而奖励却由之后的真实交互结果产生，二者在时间上不再严格对齐。固定延迟下，智能体可能通过训练逐渐形成某种“认知惯性”；但在随机延迟下，这种隐式预测会变得不可靠。

因此，本文试图解决的问题可以概括为：在多智能体系统中，当不同观测成分存在个体化、随机化、不同步的延迟时，如何让智能体尽可能恢复接近无延迟环境下的决策能力。为此，作者提出了DSID-POMDP建模方式和Rainbow Delay Compensation（RDC）训练框架。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***02.***

**关键技术**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

本文的关键技术可以概括为“先把延迟观测问题说清楚，再通过补偿框架把旧观测尽量恢复成当前观测”。它不是简单地给现有MARL算法换一个网络，而是从问题建模、延迟观测生成、观测补偿、价值估计和策略训练五个层面共同处理随机延迟。

该方法的创新和贡献如下：

1）提出DSID-POMDP建模方式，用统一框架描述多智能体系统中的随机个体延迟观测问题，尤其强调“同一个智能体的不同观测成分可能来自不同历史时刻”。

2）提出RDC训练框架，将观测重构、延迟一致化价值估计、Actor课程学习和教师-学生知识蒸馏组合起来，形成可嵌入现有MARL算法的通用补偿方案。

3）设计Flash和Echo两种补偿模式，并使用Transformer与GRU实现补偿器，使方法可以在推理速度和延迟泛化能力之间进行权衡。

4）将RDC与VDN、QMIX等经典值分解MARL算法结合，在MPE和SMAC两类基准上验证固定延迟与非固定延迟条件下的效果。

5）开源了RDC-pymarl代码，便于复现DSID-POMDP观测生成、补偿器训练以及MPE/SMAC延迟实验设置。

代码链接：                                                 https://github.com/linkjoker1006/RDC-pymarl

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***03.***

**算法介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

为了更直观地理解RDC，可以先把它看成一个“延迟观测修复器+MARL决策器”的组合。环境交互时，智能体并不能直接拿到当前真实状态，而是先经过Delay Filter得到带延迟的delayed obs。随后，补偿器利用历史观测、历史动作和延迟向量，估计当前时刻更接近真实情况的补偿观测。最后，Actor根据补偿后的观测输出动作。

整个算法的核心问题不是“如何让智能体忽略延迟”，而是“如何显式利用历史信息把不同时间来源的观测成分对齐”。因此，RDC的算法流程可以分成六个部分：延迟建模、延迟观测生成、补偿器输入构造、Flash/Echo 补偿、强化学习训练，以及最终去中心化执行。

**（1）DSID-POMDP：把“不同来源的信息不是同一时刻”建模出来**

传统Dec-POMDP默认每个智能体在每个时刻接收一个局部观测，但本文认为局部观测本身由多个成分组成：自身状态、其他智能体状态和环境实体状态。在DSID-POMDP 中，系统状态被扩展为“当前状态+过去T步历史状态”。当智能体i需要观察实体j时，系统会根据D\_ij采样一个延迟值，并从对应历史状态中取出该实体的信息。这样，一个智能体当前看到的局部观测可能同时混合了t时刻、t-1时刻、t-3时刻等不同来源的信息。图1展示了这种扩展状态和个体延迟分布的含义。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2lRcTJIjryO3WDrCYXFPS024nv925r3NOJd2ib1nn9Mt11IkVJVZsicrx01RAbHic1RALz7ywPfJItbpaXiabaibxicmLMZKG2Ztthg/640?wx_fmt=png&from=appmsg)

图1  DSID-POMDP 对多智能体延迟观测进行建模的示意图

**（2）延迟发生与补偿：先制造真实延迟，再学习如何恢复**

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3OSrXVEgiaHAgByrSzfwN6IalzFV8QNiaeed5esvgibB19Q10STgtEtwlC5AT8VfvxAPtRWYiawkx6Zb4dmj3j6iaRfzjtlEsibBAQs/640?wx_fmt=png&from=appmsg)

图 2  RDC 训练框架的内部结构

为了在常用MARL基准中研究延迟问题，作者通过Delay Filter人为生成延迟观测。图3中左侧表示延迟发生过程：每个小格中的数字表示该观测成分来自哪个环境时间步，数字越小，说明信息越旧。可以看到，同一个智能体在当前时刻接收到的不同观测成分并不一定来自同一个时间。

图3右侧表示延迟补偿过程：补偿器需要把旧观测逐步向当前时刻推进。直观地说，如果某个观测成分落后了3步，就需要进行 3 步补偿；如果只落后了1步，就只需要补偿1步。RDC 的补偿器正是围绕这一过程设计的。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp18PUNfX4kKr6c2j1ibv2M8FtgoqcaLNahGJoVpVX2l3HZUKO56mg4yk7q2F7SIBPGwicfIuJpIR7EyvhykNiaxk9IJNWPUHQ2gak/640?wx_fmt=png&from=appmsg)

图 3  多智能体观测延迟的发生与补偿过程

**（3）补偿器输入构造：把历史观测、动作和延迟向量一起送入模型**

补偿器并不是只看当前的delayed obs，而是会利用一段历史窗口。输入通常包括过去T步观测序列Z、过去T步动作序列A，以及表示不同观测成分延迟大小的 delay vector。引入动作历史是因为多智能体环境的状态变化与各智能体过去动作密切相关，只看观测历史可能无法判断状态为什么变化。

图4展示了不同网络结构下的补偿器输入形式。Transformer更适合并行处理固定长度历史序列，能够利用注意力机制捕捉较长时间依赖；GRU则以递归方式处理序列，结构更轻量，适合资源受限或更强调推理效率的场景。对于Echo模式，模型还会在自回归过程中把上一步补偿结果继续作为下一步输入。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1ibxRCmSeibtrCiaARBuwop6mpA0Qkia8nWL5j5nJ8qZNdmWP8v6picxLuEtSpMK6y1LytIPLjYpBvvdu1FtbToO5znhnic6gRaOayY/640?wx_fmt=png&from=appmsg)

图 4  补偿器在不同模式和网络结构下的输入构造

**（4）Flash 与 Echo：两种不同的补偿路径**

Flash 可以理解为“一步到位”的补偿器。它把历史信息整体输入模型，直接输出当前时刻的估计观测。由于只需要一次前向传播，Flash的推理速度更快，计算开销更低。不过，当测试阶段的延迟分布与训练阶段差异较大时，Flash可能更容易出现泛化不足。

Echo 更像“逐步滚动预测”。它每次只把观测向前补偿一步，再把输出结果作为下一步补偿的输入。经过 T 步自回归补偿后，mask layer 根据每个观测成分实际需要补偿的步数选择最终结果。Echo 的计算成本高于 Flash，但补偿过程更贴近图3中“几步延迟对应几步补偿”的理想过程，因此在复杂延迟和分布外测试中通常更加稳定。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3RPTH9qLiaYvbcQu9qHGAscIs9bXLGz73nhCicaVrKCeavkbOb6OnsHKeTPtOprkviaYbwdHencoPpWWZoBzXtvNckebRMcW0kRg/640?wx_fmt=png&from=appmsg)

图 5  Flash 与 Echo 两种补偿器工作流程

**（5）延迟一致化Critic：训练时给价值函数更准确的信息**

RDC借鉴CTDE思想：训练阶段可以使用更丰富的信息，但执行阶段每个智能体仍然只依赖本地可获得信息。具体来说，Critic在训练时可以接收无延迟全局状态，用更接近真实当前状态的信息估计价值，从而减少延迟观测给价值函数带来的偏差。

这种设计不会破坏去中心化执行，因为Critic只在训练阶段更新网络参数，推理阶段并不参与动作选择。也就是说，执行时真正运行的是“补偿器+Actor”，不需要访问全局真实状态。

**（6）课程学习Actor：从容易输入过渡到真实延迟输入**

训练早期补偿器还不准确，如果Actor一开始就完全依赖补偿观测，策略可能会被错误补偿结果带偏。为了解决这个问题，作者引入课程学习：训练初期以较高概率向Actor提供无延迟观测，让策略先学习较容易的决策模式；随着训练推进，逐渐降低无延迟观测的使用概率，最终让Actor完全依赖补偿观测。

这个过程类似于先让学生在“标准答案较多”的条件下学习基本规律，再逐步切换到真实高延迟场景。对于MPE这类相对简单的任务，课程学习并不总是必要；对于SMAC这类更复杂的任务，它可以明显改善训练稳定性。

**（7）知识蒸馏：用低延迟教师模型指导高延迟学生模型**

RDC还引入教师-学生式知识蒸馏。作者先在低延迟环境中训练教师模型，使其获得接近无延迟条件下的较高性能；随后在高延迟环境中训练学生模型时，让教师模型根据补偿观测给出动作分布、Q值和隐藏表示方面的指导。

需要注意的是，作者没有把教师补偿器直接迁移给学生补偿器，而是让学生补偿器在线学习。这一点很重要，因为高延迟环境中的数据分布可能与低延迟环境不同，直接复制教师补偿器不一定有效。作者希望验证的是“策略层面的教师指导”能否帮助高延迟学生模型更快收敛。

**（8）完整训练与执行流程**

第一步，在MPE或SMAC中通过Delay Filter生成delayed obs，并记录对应的delay vector。

第二步，将历史观测、历史动作和延迟向量输入Flash或Echo补偿器，输出补偿观测。

第三步，Actor根据补偿观测选择动作，环境根据联合动作转移到下一状态。

第四步，用补偿目标训练补偿器，用强化学习目标训练VDN/QMIX主体，用 delay-free state辅助Critic进行更稳定的价值估计。

第五步，在需要时加入课程学习和知识蒸馏，让学生模型从低难度输入逐渐过渡到真实高延迟输入。

第六步，测试或部署时只保留补偿器和Actor，每个智能体根据本地延迟观测独立补偿和决策。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***04.***

**实验结果分析**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyy...