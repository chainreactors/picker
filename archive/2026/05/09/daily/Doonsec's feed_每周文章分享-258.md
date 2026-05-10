---
title: 每周文章分享-258
url: https://mp.weixin.qq.com/s/97bzSfq--1NloanUdG_Pag
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:36:18.849681
---

# 每周文章分享-258

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jBQAokCLibp1QbzO8dT6d1zm3VwQuoyzZRQZhBeYSnpKg0VrjKuVgD38ibs72vB4ib465Eh5ic2qZNbZ6kLDSbsv5OoJCPUr841Lce0zG7AO7cE/0?wx_fmt=jpeg)

# 每周文章分享-258

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4DAaJy0Ok82ibMPxwHY4mibwrjmLoqmvIickMFksSta2uNYdIpd6BSh7GAKsqdYvoQq3Sg4RqvtofvuJLvGnIwDAIicnMN8A6wjias/640?wx_fmt=png&from=appmsg#imgIndex=56)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd79GRlwNhZak3b6NicAtrelJ5wXr5U8icCFGbOq9olPBSsVfSynibKpYAErrW6LMx4lyXdp5ibny1uCN8uPlrgJQNibuH3hYkIW2aBo/640?wx_fmt=png&from=appmsg#imgIndex=57)

**每周文章分享**

2026.05.04至2026.05.10

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4Ohaz7tlbUgBU08mJu9dD8frItmtjJ1C9xvR9d9Gic4CYK1bBjJA40NMpK6T89bFlj2aNTod2cSPT666sMXxIEia1FJy7QbLnrQ/640?wx_fmt=png&from=appmsg#imgIndex=60)

**标题：** ETPNav：Evolving Topological Planning for Vision-Language Navigation in Continuous Environments

**期刊：**IEEE Transactions on Pattern Analysis and Machine IntelligenceVolume： 47,Issue：7,July 2025)

**作者：** Dong An,Hanqing Wang,Wenguan Wang,Zun Wang,Yan Huang, Keji He,Liang Wang

**分享人：** 河海大学——潘银河

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd7PdTwqxaMfpIS26krIsxls3gvlWl17nYzpFj5Zhtqcwy3z6MhbZh7hZmegdwno07C0icPN2GlR16gtHMFHOjswwUIO0ZHZRjKM/640?wx_fmt=png&from=appmsg#imgIndex=73)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***01.***

**研究背景**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

视觉语言导航要求智能体根据自然语言指令在真实环境中行动，该任务在embodied AI领域日益重要，同时在自主导航、搜索与救援及人机交互中具有应用潜力。

早期研究多基于离散图结构简化导航过程，但难以反映现实部署的复杂性，因此后续引入了连续环境下的视觉语言导航任务，让智能体在三维网格中自由移动。然而，连续环境导航的难度远高于离散版本，现有模块化航点方法虽通过分解航点生成、子目标选择与底层控制提升了性能，但仍存在航点预测局限于局部区域、关键设计缺乏系统性验证、以及避障控制能力不足等问题，限制了其在复杂场景下的表现。

本文提出新型导航框架ETPNav解决以上问题

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***02.***

**关键技术**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

本文提出了一种分层导航框架，其核心创新体现在三个方面：在线自组织拓扑地图支持的全局规划、对拓扑地图关键设计的系统性研究，以及一种新型鲁棒避障控制器。

该框架通过将全局路径规划与局部执行控制相分离，有效克服了以往视觉语言导航方法中只关注局部区域、易受障碍物卡住等局限。

该方法的创新和贡献如下：

1）在全局规划层面，智能体在导航过程中将预测的航点在线自组织成拓扑地图，其中节点表示地点，边表示可达性。该地图能够高效捕捉环境全局布局与远程导航依赖关系，使智能体可在地图上进行最短路径等远程规划，区别于传统方法需要预定义图或预先探索环境的方式。

针对航点预测任务，作者通过系统性设计选择研究指出，仅使用深度信息的预测器优于使用RGB信息的方案，因其能更准确地推断空间可达性，并在新环境中具备更强的泛化能力。

2）在局部执行层面，为应对视觉语言导航连续环境中智能体易被障碍物卡住、尤其在禁止沿障碍物滑动的严苛场景下的问题，作者设计了一种基于试错启发式方法的底层避障控制器。该控制器能够主动帮助智能体从死锁状态中摆脱出来，几乎完全消除了因严格物理约束而导致的性能下降问题。

3）通过将拓扑地图赋予的全局规划能力与鲁棒避障控制器赋予的可靠局部执行能力相结合，该系统在多个视觉语言导航连续环境基准测试中取得了最先进的性能，并在相关挑战赛中夺冠，验证了所提分层框架的有效性与优越性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***03.***

**模型介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

本文模型利用基于高级拓扑地图的规划与低级控制器完成VLN‐CE任务。如图1所示， ETPNav模型包含三个模块：拓扑建图、跨模态规划与控制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp11JtOG86TRGh5Diapo7jwZHuTCsHzCSLbTEBECZ0ZesWpE9pibNJ7ocINR0pzLPXqj065IGBwk35OMzGIXY4R12g8ibZfickibBoVM/640?wx_fmt=png&from=appmsg)

图1  提出的ETPNav模型

在每个训练周期中，拓扑建图模块通过整合遍历路径上的观测数据逐步更新维护拓扑地图。随后，规划模块对地图和指令进行跨模态推理以预测长期目标， 并制定高级拓扑路径规划。该规划由控制模块执行，通过低级动作驱动 智能体向目标移动。下面具体讲解各个模块及其关键功能

**（1）拓扑建图模块**

本文智能体会动态构建拓扑地图，将遍历路径上的位置抽象为图结构。图中节点存储视觉与位置信息，边表示节点间的直接可达性并记录相对距离。这些节点分为已访问节点、当前节点和幽灵节点，其中幽灵节点表示已被观察到但尚未探索。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1qYoPVt2uRc9JxJcDibBRiagsFsvM0ViaQawMHvjx6Ft0YDrUcypTt6blich7AticOPDUtbibYhELwcsMej4DPPiaRvc9lvlANuhUP7I/640?wx_fmt=png&from=appmsg)

图2  拓扑建图模块

如图2，在每一步 t，智能体首先预测几个附近的航点，代表智能体附近可能可到达的位置。同时， 在智能体当前位置初始化一个当前节点，并连接到上一个已访问节点(如果存在)。再经图更新操作后，这些航点将被组织以更新先前的拓扑地图 G\_t−1 并获得当前地图 G\_t。

下面补充图更新中三种情况下，航点定位函数F\_L的逻辑:

匹配到幽灵节点：将输入航点的信息（位置、视觉特征）合并到该幽灵节点中，节点的新状态取所有累积信息的平均值，逐步优化节点表示。

无匹配节点：将输入航点创建为一个新的幽灵节点，作为待确认的潜在地标加入系统。

匹配到已访问节点：直接删除输入航点，并在当前节点与已匹配节点之间建立一条边，用于记录路径连接关系。

**（2）跨模态规划模块**

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2xCzeVibSB4MiadwbrlLhCUVp9DehzQoul2te1RQlyyLRduIPhsTGgyrB9pvhvuJLFKKJia8zVkngIlcd09gEia7TbMX8C8ia9gsWg/640?wx_fmt=png&from=appmsg)

图3  跨模态规划模块

跨模态规划模块由一个文本编码器和一个跨模态图编码器组成。当前回合的指令由文本编码器进行编码。 然后，跨模态图编码器在拓扑地图和编码指令上进行推理， 以预测一个长期目标节点。输出是通往目标的规划拓扑路径。

智能体根据预测的目标分数s\_i(分数最高的节点)选择一个长期目标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1QhyRg3qWp0edZ9Kae9VxUShCy77iawGtXDCEx1R1nuvwVb7yRVx9mNOGothZLgu8r1wjWoIlU4hGYBS057KUgMS14k5zics2Xo/640?wx_fmt=png&from=appmsg)

**（3）控制模块**

控制模块负责将拓扑规划转换为一系列低级动作，以引导智能体到达目标。其输入为规划路径上的子目标节点及智能体的实时位姿；输出采用VLN‐CE任务中定义的参数化动作空间。

此外，由于VLN‐CE任务模拟了一个实际导航场景，故而导航控制过程中障碍物规避至关重要， 尤其是在沿障碍物滑动被禁止的情况下。在此类情况下，若智能体底盘接触障碍物则无法前进。这会导致死锁和控制无进展，极端情况下将提前终止任务并导致导航失败。

为解决此问题，本文设计了一种名为'Tryout'的启发式方法，利用试错法防止导航陷入停滞。

如图4，实际的禁止滑动步骤可能导致智能体卡在障碍物中并导致导航失败。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3PUeafENdhbsT1jkukOh7KfjicHsyYKArov52mzQ2dfedw68nqPv5aX7phaYS46QDQV1u8cXGQdOGlBmBAfU7duqb1IepAFMyE/640?wx_fmt=png&from=appmsg)

图 4  Tryout使用与否的影响

例如，在没有尝试的情况下，一旦底盘与墙壁碰撞(第6步和第7步)，智能体便无法继续前进。这种情况一直持续到导航结束(第14步)，智能体未能成功逃离死锁，最终导致导航失败。

相反，本文的模型中集成的 Tryout控制有效地解决了这个问题。在第4步，尝试在与墙壁碰撞时被触发，导致智能体扭转并摇晃着远离障碍物，并在第6步成功完成导航。

**（4）模型的训练与推理**

在这一部分，本文主要做了预训练、微调与推理的工作。

预训练阶段是为了提高智能体的泛化能力，本文使用自监督代理任务对规划模块进行预训练，遵循基于Transformer的 VLN模型中的常见做法。

微调是为避免过拟合专家经验，在每一步预测的长期目标根据预测分数的概率分布进行采样。在每个决策循环中，智能体依次更新地图、预测目标、规划路径。确定每一步的教师动作节点，引入与DAgger算法类似的交互式演示器，选择与最终目标测地距离最短的幽灵节点作为教师节点。总体策略学习的目标函数如下：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2GTKUs1WuZTHsCchx1ZzS7HUlrgJXXcrwBWOhovfN2qkQ5UIEm3aHukDr9BiacwpBgoWTrbBdp3ibn4ZPxI9ANONRNH4UgW40I0/640?wx_fmt=png&from=appmsg)

推理阶段的工作大致与微调阶段一致，主要区别在于规划步骤所采用的长期目标采样策略不同。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***04.***

**实验结果分析**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

本文在R2R-CE和RxR-CE数据集上进行了实验。

这两个数据集是通过Habitat模拟器将R2R和数据集中离散路径转换为连续环境而创建的。它们在路径长度、指导粒度和智能体形态等多个方面存在差异，如表1所示：

表1  R2R‐CE 和 RxR‐CE的数据统计

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2UkEtib6Scd6tSgtgtVHibd28cnCpSic5haZSd8Oy8xV6R2DJl346Xicx4rXkUyIgTr44H97KXnRDwTiazKUDSrm75XJMbGgLMcqm8/640?wx_fmt=png&from=appmsg)

与R2R‐CE相比，RxR‐CE提供了更多的指令，涵盖英语、印地语和泰卢固语的多语言描述，每条指令平均需要120个单词。此外，RxR‐CE中的标注路径比 R2R‐CE中的长得多(15.23米对比9.89米)。值得注意的是，RxR‐CE中的智能体被禁止沿着障碍物滑动，并且较大的底盘半径(0.18米)使其容易与障碍物发生碰撞。这也使得 RxR‐CE更具挑战性，因为在遇到障碍物时导航很容易陷入困境，从而突显了障碍物规避在这一挑战性任务中的重要作用。

本文采用以下导航指标：

轨迹长度 ( TL)、 导航误差 (NE) 、成功率 (SR) 、预言机成功率 (OSR)

路径长度惩罚成功率 (SPL)、归一化动态时间规整 (NDTW) 、经成功率惩罚的归一化动态时间规整 (SDTW)。

R2R‐CE使用SR和SPL作为其主要指标，而RxR‐CE更关注路径保真度， 并使用NDTW和SDTW作为其主要指标。

**（1）与最先进水平方法对比**

表 2 与最先进水平的方法在R2R‐CE数据集上的比较

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1rOzKUuYgwKibiambGmMCGkvL8hQlpB87hevHHSdk4VOpz3rxcsiaUSWNiaHU14gUo7eTAuAWZyfOKgoLLBerRoGtblHEgQfKtpKI/640?wx_fmt=png&from=appmsg)

表2将ETPNav与当前最先进的方法在R2R‐CE数据集上进行了比较。结果表明，本文模型在NE、OSR、SR和 SPL所有分割上都优于现有模型。特别是在验证不可见集上， ETPNav超过了第二好的模型CWP‐RecBERT模型，在成功率上提高了13%，在路径长度加权成功率上提高了10%。此外，本文的模型在测试未见集...