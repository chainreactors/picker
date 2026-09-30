---
title: 每周文章分享-278
url: https://mp.weixin.qq.com/s/mGP9yOUsf_aEy8ld475ydA
source: Doonsec's feed
date: 2026-09-29
fetch_date: 2026-09-30T07:40:34.618886
---

# 每周文章分享-278

# 每周文章分享-278

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4DAaJy0Ok82ibMPxwHY4mibwrjmLoqmvIickMFksSta2uNYdIpd6BSh7GAKsqdYvoQq3Sg4RqvtofvuJLvGnIwDAIicnMN8A6wjias/640?wx_fmt=png&from=appmsg#imgIndex=56)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd79GRlwNhZak3b6NicAtrelJ5wXr5U8icCFGbOq9olPBSsVfSynibKpYAErrW6LMx4lyXdp5ibny1uCN8uPlrgJQNibuH3hYkIW2aBo/640?wx_fmt=png&from=appmsg#imgIndex=57)

**每周文章分享**

2026.09.28至2026.10.04

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4Ohaz7tlbUgBU08mJu9dD8frItmtjJ1C9xvR9d9Gic4CYK1bBjJA40NMpK6T89bFlj2aNTod2cSPT666sMXxIEia1FJy7QbLnrQ/640?wx_fmt=png&from=appmsg#imgIndex=60)

**标题：**Scheduling Stochastic Traffic With End-to-End Deadlines in Multi-Hop Wireless Networks

**期刊：**IEEE TRANSACTIONS ON MOBILE COMPUTING, VOL. 25, NO. 7, JULY 2026

**作者：**Christos Tsanikidis and Javad Ghaderi.

**分享人：**河海大学——张月

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd7PdTwqxaMfpIS26krIsxls3gvlWl17nYzpFj5Zhtqcwy3z6MhbZh7hZmegdwno07C0icPN2GlR16gtHMFHOjswwUIO0ZHZRjKM/640?wx_fmt=png&from=appmsg#imgIndex=73)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***01.***

**研究背景**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

多跳无线网络已成为支撑实时视频、车联网和物联网等时延敏感应用的重要通信基础。然而，这些网络面临着随机业务到达与链路相互干扰下的数据包按时交付问题。数据包需要经过多跳转发才能到达目的节点，一旦超过端到端截止期，便会失去应用价值。现有调度方法主要关注吞吐量，或其性能保证随路由长度增加而下降，或依赖无限带宽等渐近假设，难以适用于实际有限资源场景。本文提出了两种调度算法，以最大化截止期内成功交付数据包的加权总和。首先，提出了一种多跳干扰感知近最优调度（MINOS）算法，利用线性规划引导概率转发与无干扰链路集合的随机选择，在满足一定信道数量等条件时实现近最优性能。其次，提出了一种结合概率转发的贪心极大调度（GMS-PF）算法，通过贪心选择可并发传输的链路集合降低计算复杂度，并支持分布式实现，在有限资源条件下提供具有理论保证的调度性能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***02.***

**关键技术**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

在本文中，提出了一种面向随机业务和严格端到端截止期的多跳无线网络联合路由与调度方法，以最大化按时交付数据包的加权总和。首先，提出了一种多跳干扰感知近最优调度（MINOS）算法，通过线性规划联合确定数据包转发概率与无干扰链路集合的选择概率，并依据数据包类型、已消耗时间和所在节点实施概率转发。其次，设计了一种结合概率转发的贪心极大调度（GMS-PF）算法，通过贪心选择可并发传输的链路集合，避免对全部独立集进行随机选择所带来的高计算开销，实现多项式时间计算并支持分布式执行。在满足相应随机到达假设及信道数量等条件时，两种算法分别提供近最优性能保证和与网络干扰度相关的近似性能保证。

该方法的创新和贡献如下：

1）本文在随机业务条件下，为存在链路干扰和严格端到端截止期约束的多跳无线网络提供了非渐近的近最优及常数近似结果。与依赖带宽、到达率和运行时间趋于无穷的既有方法不同，所提出的方法在这些参数均有限且满足相应条件时即可获得理论保证，其近似比不随数据包权重或最大路由长度增大而恶化。

2）提出了两种具有不同计算复杂度与性能保证的调度算法：a）多跳干扰感知近最优调度算法利用线性规划协调链路资源分配与概率转发，并预留容量裕量以降低随机流量超出可用资源造成的丢包，从而获得近最优的按时交付收益；b）结合概率转发的贪心极大调度算法利用规模更小的线性规划引导转发，在各时隙、各信道上贪心构建无干扰链路集合，在降低计算复杂度的同时保留可证明的性能保证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***03.***

**算法介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

**（1）多跳干扰感知近最优调度（MINOS）算法**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2ztB3bmarYcPiay1e9RmTMlo7Z6YYia9tOP0ff3F3FibXsY7SomdxCUuugEhshSDBSOib8xzWer7OtPknGNm8EB8CIiaVPxDSibgJrs/640?wx_fmt=png&from=appmsg)

图1  多跳干扰感知近最优调度算法的执行过程

多跳干扰感知近最优调度算法通过联合设计数据包转发策略和信道资源分配，提高随机业务在端到端截止期内的交付收益。算法利用干扰图描述链路之间的冲突关系：若两条链路之间存在干扰边，则不能在同一时隙、同一信道上同时传输；一个独立集则对应一组可以并发传输的无干扰链路。

如算法1所示，该方法包括线性规划求解、信道分配和在线概率转发三个阶段。首先，根据各类数据包的源节点、目的节点、截止期、权重及平均到达率，求解线性规划，获得转发变量和独立集选择概率。随后，为每个信道随机选择一个独立集，确定各条链路能够使用的信道数量，该分配在本次算法执行期间保持不变。

在线运行阶段，算法根据每个未过期数据包的类型、已消耗时间和当前所在节点，随机选择下一条转发链路。如果选择的是自环，则表示数据包在当前节点等待一个时隙；如果选择的是实际通信链路，则将其加入该链路的待发送集合。每条链路按照已分配的信道数量发送数据包，超过当时可用容量的剩余数据包被丢弃。

**（2）线性规划与概率转发机制**

线性规划是多跳干扰感知近最优调度算法的核心。设第j类数据包的权重为wj，平均到达率为λj，相对截止期为dj，目的节点为zj。变量f描述该类数据包在年龄为τ时经过链路l的规划流量比例，其中“年龄”表示数据包自到达以来已经经过的时隙数。优化目标为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3fym35ECqGKu4WsMsjibdV4yYkNjuadGeqvlEVicfG6uLMUtl4xWK3Ahhw9ae9IClCUZJFlz5b7jwbeicVbLs1h3r83MTUD1OWy4/640?wx_fmt=png&from=appmsg)

该目标最大化规划中按时到达目的节点的数据包加权收益。其中，Inc（zj） 表示进入目的节点的链路集合，包含目的节点自环。提前到达的数据包可以通过自环在目的节点保留，因此也计入按时交付收益。模型通过源节点约束、逐时隙流守恒和非负约束，使转发过程在时间和空间上连续。

为了协调转发需求与信道资源，算法设置以下容量约束：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2lhchXlrPK4jdfLLLgKNSaX7NeWnXSEAkO3ywibEaOkHic6upqdu1dibE8qFwrfN4gBye86oMsUBoicfPqL0vX5q87N56EFKPC7Jc/640?wx_fmt=png&from=appmsg)

左侧表示链路上的平均转发需求，右侧表示预留一定裕量后的平均服务能力。系数(1-ε)用于留出容量余量，降低随机到达造成瞬时需求超过可用资源的概率。

获得最优解后，每个信道按照以下混合概率选择独立集：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0fsbYCZhvqzVRgrSnz8TcjZdfQA9ficewqyJwbf1dMnibzsD3F8p9cMa6ZsyjStp8vRK3gJqa1V9iaibYu1Bm5eR8OrSnZkHfMOBQ/640?wx_fmt=png&from=appmsg)

对于位于节点v、类型为j、年龄为τ的数据包，下一条链路按照以下概率选择：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp0jfmtaLXJwbGibhIwk6w5IOicQEI2quA3pt33sxz1jotLib1cjxhtk2IQZFObMNv55KaRMy8PDbAI5R3zPf6QEGKzibveZfasCX3w/640?wx_fmt=png&from=appmsg)

该式将当前节点各条出链路上的最优转发变量归一化，得到实际执行时的条件选择概率，使数据包的逐跳转发遵循线性规划确定的资源安排。

**（3）结合概率转发的贪心极大调度（GMS‑PF）算法**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2C0Ficly44XibrsTvvURPheXCia9yE7Rm0SFoYiaicMRfk29tDKzBUp2JsyicWBswSWweBP7ERT2V0NOvznhSDW4ovbYrKmARPGTib9A/640?wx_fmt=png&from=appmsg)

图2  AIADC算法的工作流程

当网络规模增大时，干扰图中的独立集数量可能快速增长，增加多跳干扰感知近最优调度算法的线性规划求解开销。为此，本文提出结合概率转发的贪心极大调度算法，保留概率转发机制，并通过逐时隙贪心选择无干扰链路集合完成信道分配。

如算法2所示，首先求解简化后的线性规划，获得各类数据包的转发变量。在每个时隙，算法根据数据包类型、年龄和所在节点选择下一条链路，并将数据包加入相应的待发送集合。该概率选择方式与前述公式相同，但转发变量来自新的线性规划。

随后，算法依次处理各个信道，从具有待发送数据包的链路中选出一个极大独立集，并在其中每条链路上发送一个数据包。完成当前信道的分配后，更新待发送集合，再为下一信道选择链路。所有信道处理完毕后，丢弃尚未获得传输机会的剩余数据包。

这里的“极大独立集”表示不能再加入其他候选链路而不产生干扰，并不要求其包含的链路数量最多。因此，算法可以通过逐步选择链路并排除冲突邻居完成调度，无需求解最大独立集问题。

**（4）邻域容量约束与分布式信道选择**

结合概率转发的贪心极大调度算法采用干扰邻域容量约束，替代对各个独立集设置概率变量的方式。其优化目标仍为最大化按时交付的加权收益，核心容量约束为：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1LQWWnao0ldyZYNqXMTG8XibVRvN7cjfXjXMrbFJvA6dqtgzTzvL5hfFhez9vpfexE1c3xia0FibcfC7OibnLae07qqAdzxz1GMrw/640?wx_fmt=png&from=appmsg)

其中，Nl包含链路l本身及所有与其存在干扰的链路。该约束限制整个干扰邻域的平均转发需求，使相互竞争的链路保留足够的信道分配空间。模型同时保留原有的源节点、流守恒和非负约束。

由于不再为每个独立集引入变量，新的线性规划规模明显减小。在线调度时，算法可以采用贪心方式构建极大独立集，例如优先选择待发送数据包较多的链路，从而以较低的计算开销完成可并发链路选择。

此外，论文给出了基于随机定时器的分布式信道选择方法。各链路为不同信道设置随机定时器，定时器先到期且未被干扰邻居抢先占用的链路声明使用该信道；当一条链路获得的信道已足以发送其待发送数据包时，便取消剩余定时器。该机制用于分布式实现在线独立集选择。在控制开销足够小等假设下，可获得相应的理论性能保证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***04.***

**实验结果分析**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

**1. 不同干扰条件下的调度性能验证**

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0a7vuvnNo7ArwrysqW48OUTjXWuHIsDvGrFLtmVvZFmNmgQgavr3EALR5UUH0XxosmDH5P71L5ptkjg7vHoctZLGeTpbgHpqs/640?wx_fmt=png&from=appmsg)

图3  单跳干扰与一般干扰条件下的按时交付收益对比

本文分别在8节点的单跳干扰网络和20节点的一般干扰网络中进行实验，以每时隙内按时交付数据包的加权收益作为评价指标。如左图所示，随着信道数量增加，多跳干扰感知近最优调度（MINOS）算法始终获得最高收益，结合概率转发的贪心极大调度（GMS-PF）算法次之，两者均优于基线方法NEMS。

在一般干扰条件下，两种算法同样优于基线方法GIMS，其中MINOS表现最佳。结果表明，所提出的方法能够在不同链路干扰条件下有效利用信道资源，提高满足端到端截止期的数据包交付收益。

**2. 不同业务到达分布下的性能分析**

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0UhIcO3HIh3lhz9uenus3cZfZtFCO1oZQaduRyia4ojmr5HkiaZECJzscanoQIfOfeBasMB1MAXuFwicNV4H8GQItDyibicJ1U7L2s/640?wx_fmt=png&from=appmsg)

图8  100 节点网络中不同配置下的吞吐量和误码率结果

为分析随机业务特征对调度性能的影响，本文比较了二项分布、泊松分布和缩放伯努利分布三种到达模式，并保持各模式的平均到达率一致。评价指标为算法收益与线性规划最优值的比值，该指标给出了算法相对于离线最优调度的近似比下界。

如左图所示，MINOS...