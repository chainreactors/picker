---
title: 每周文章分享-266
url: https://mp.weixin.qq.com/s/5m1WvwjYoVC73w7JAebRiQ
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:11:03.830288
---

# 每周文章分享-266

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jBQAokCLibp39l9xkyFejO0IWBvmmxpjUvIFaibknUCqO9hBNhwh9icXRt0S5686UthA5Gj6MwN9oeMTZZ008EYKR05lb0icr6EICErf5GbpOFM/0?wx_fmt=jpeg)

# 每周文章分享-266

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4DAaJy0Ok82ibMPxwHY4mibwrjmLoqmvIickMFksSta2uNYdIpd6BSh7GAKsqdYvoQq3Sg4RqvtofvuJLvGnIwDAIicnMN8A6wjias/640?wx_fmt=png&from=appmsg#imgIndex=56)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd79GRlwNhZak3b6NicAtrelJ5wXr5U8icCFGbOq9olPBSsVfSynibKpYAErrW6LMx4lyXdp5ibny1uCN8uPlrgJQNibuH3hYkIW2aBo/640?wx_fmt=png&from=appmsg#imgIndex=57)

**每周文章分享**

2026.07.06至2026.07.12

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4Ohaz7tlbUgBU08mJu9dD8frItmtjJ1C9xvR9d9Gic4CYK1bBjJA40NMpK6T89bFlj2aNTod2cSPT666sMXxIEia1FJy7QbLnrQ/640?wx_fmt=png&from=appmsg#imgIndex=60)

**标题:**Semi-Asynchronous Federated Split Learning for Computing-Limited Devices in Wireless Networks

**期刊:**IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, VOL. 24, NO. 6, JUNE 2025.

**作者:**Huiqing Ao, Hui Tian, Wanli Ni, Gaofeng Nie, and Dusit Niyato.

**分享人:**河海大学——王柯欣

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd7PdTwqxaMfpIS26krIsxls3gvlWl17nYzpFj5Zhtqcwy3z6MhbZh7hZmegdwno07C0icPN2GlR16gtHMFHOjswwUIO0ZHZRjKM/640?wx_fmt=png&from=appmsg#imgIndex=73)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***01.***

**研究背景**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

随着6G、边缘计算和人工智能的发展，工业物联网等场景中的大量数据逐渐分布在边缘设备侧，传统集中式训练难以满足低时延、低通信开销和隐私保护需求。联邦学习虽然可以避免上传原始数据，但许多边缘设备计算能力有限，难以独立训练大规模深度模型；分割学习可以减轻设备计算压力，却容易带来较长的顺序训练时延。

联邦分割学习结合了二者优势，但现有方法通常依赖同步聚合。在无线信道波动和设备能力差异较大的情况下，服务器需要等待慢设备完成训练，导致训练时延增加和收敛效率下降。针对这一问题，本文提出半异步联邦分割学习框架，通过个性化模型划分和非周期聚合机制，降低等待时延，并进一步结合在线资源优化提升系统训练效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***02.***

**关键技术**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

在本文中，提出了半异步联邦分割学习（SAFSL）框架，主要面向计算能力受限、无线信道动态变化的边缘网络。该框架将联邦学习的并行训练能力与分割学习的模型拆分能力结合起来，使终端设备不需要独立训练完整深度模型，同时避免传统同步聚合中straggler问题。

该方法的创新和贡献如下：

1）本文采用个性化模型划分机制，根据不同设备的资源能力灵活分配计算负载。

2）本文设计了半异步模型聚合机制。服务器不再强制等待所有设备完成训练，而是在设定的聚合时间内，对已经完成设备-边缘协同训练的设备进行模型聚合；未完成训练的设备则继续执行训练，不会被中断。

3）Lyapunov在线优化。面对时变无线环境和长期时延/能效目标，使用虚拟队列和交替优化来做在线决策。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***03.***

**算法介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

**（1）框架设计**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3qx2RmibbalPwqpv8gsgiayjJo6dyoVtHwGlLhFcaZiazicYg7QCibhQr27OIiaJQy4sVbLmvnXeysfmjhdOmPtIf6mxHXdZVnvWyibo/640?wx_fmt=png&from=appmsg)

本文考虑的是一个典型的无线边缘智能网络：系统中包含一个带有边缘服务器的基站，以及多个计算能力不同的终端设备。所有设备共同训练一个全局模型，但与传统联邦学习不同，本文采用的是联邦分割学习，即完整的深度神经网络不会全部放在设备端训练，而是被切分为两部分：浅层模型部署在设备端，深层模型部署在边缘服务器端。

整体训练目标可以表示为：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3S9Vgjgcy6DXnrmyt1cMIbBMhBkniaiaSCPA9InkqAKbwlfOSqSysJsLqzgHLibLDpnNdCic7GgQiamvIPPqOibePlN5q7vVk7J62O4/640?wx_fmt=png&from=appmsg)

其中，Fn(w)表示第n个设备上的本地损失函数，∣Dn∣/∣D∣表示该设备数据量在全体数据中的占比。系统希望综合所有设备的数据贡献，训练出一个全局效果最好的模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp12SjZRaV8Vlffmsr07r2b4XaYxoI7XW69ZEnnanlvvgsnmgWKI9bAdLSPwrQm0uhv6k2Q7xO8ynPp5BdjtUfuNL6MnNbtGzgU/640?wx_fmt=png&from=appmsg)

本文的核心训练流程可以概括为三步：

1)模型划分与下发：训练开始时，服务器根据设备的计算能力和网络状态，为每个设备选择不同的模型切分层。计算能力较强的设备可以承担更多设备端模型层，计算能力较弱的设备则只承担较少模型层。这样可以避免所有设备采用相同切分方式导致的资源浪费或训练阻塞。

2)设备-边缘协同训练：在每一轮训练中，设备先使用本地数据完成设备端模型的前向传播，并生成中间特征，也就是 smashed data。随后，设备将中间特征和标签上传给服务器，服务器继续完成服务器端模型的前向传播和反向传播，再将梯度传回设备。设备收到梯度后，继续完成本地反向传播并更新设备端模型。

3)半异步模型聚合：服务器在一个聚合时间窗口内，只聚合已经完成设备-边缘协同训练并成功上传模型的设备；没有完成训练的设备继续训练，不会被强制中断。

服务器端的模型聚合为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp36Rn0STgH526LwXeTssSibOM5xic7EticMAfOlV4tw62BhNL7pWMmHGmbW1yb29Knf1bFJCZIYvuXwqDZ9vuMAc8UPb3AfMV85rQ/640?wx_fmt=png&from=appmsg)

其中，m\_{n,t}表示设备n在第t轮是否完成训练并参与聚合，ρ\_{n,t}表示聚合权重，w\_{n,t}^H表示设备经过H次协同训练后的模型。这个公式体现了半异步机制的核心：不是所有设备都必须参与当前轮聚合，只有已经完成训练的设备才会被纳入全局更新。

在时延建模方面，本文一轮训练的总时延由多个环节共同决定，包括模型下发时延、设备端前向传播时延、中间特征上传时延、服务器端计算时延、梯度下发时延、设备端反向传播时延，以及设备端模型上传时延。对于第 nnn 个设备，其一次设备-边缘协同训练的时延可以概括为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3sxZXa06mfTbdz9mQibDJtwHmTiapPfhwpyYNibRabPbOWt91y6lLeX2Ur4LC9xJ552zdECic1ibMvl0uEgpaFNGd6crT540bZuTAA/640?wx_fmt=png&from=appmsg)

其中，五项分别对应设备端前向传播、中间特征上传、服务器端计算、梯度下发和设备端反向传播。经过多次协同训练后，第n个设备在第t轮的总时延还要进一步加上模型下发和模型上传时延。

由于每一轮训练需要等待当前聚合窗口内的设备完成，因此系统第t轮的训练时延由最慢的相关设备决定：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3Q1QxnPKwHJlok6ub7kGk3WmficX5GMn1qNuTBHEt8yRDXl0qUaWAzuG1ksnU8ZeVib28k2Xuf5lY1zeau5UhjKgnibaLEnWvV9A/640?wx_fmt=png&from=appmsg)

这也是本文为什么要优化模型切分层、带宽、服务器计算资源和设备参与状态的原因。不同切分层会影响设备端计算量、中间特征大小和服务器计算量；不同带宽会影响上传和下载时延；不同服务器资源分配会影响服务器端计算时延。因此，这些因素共同决定了一轮训练到底有多慢。

在能耗建模方面，本文同样把能耗分成通信能耗和计算能耗。设备上传中间特征、上传设备端模型，以及服务器下发模型和梯度都会产生通信能耗；设备端和服务器端执行前向、反向传播则会产生计算能耗。

**（2）基于Lyapunov的在线优化**

在完成系统建模后，本文进一步考虑一个更实际的问题：无线网络中的信道状态、设备计算能力、带宽资源和能耗都会动态变化。因此，系统不能只做一次静态优化，而需要在每一轮训练中，根据当前网络状态在线调整资源分配和训练策略。

本文的优化目标可以概括为：在满足长期能耗约束的前提下，尽可能降低长期平均训练时延。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2o0yibnKRsibhY5lNYCSKnmaWHnMpDdSOcGLTle0hp7n66aVhlI4owPxUU7hrsTwn0fE7ibpQVbCPJWzHvPSyELkIbBzDhrrLRFU/640?wx_fmt=png&from=appmsg)

这里涉及的决策变量包括带宽分配、服务器计算资源分配、每轮训练迭代次数、设备是否参与聚合，以及模型切分层选择等。由于这些变量既包含连续变量，也包含整数变量，同时还受到随机无线信道影响，所以原问题是一个复杂的长期随机优化问题，难以直接求解。

为了解决这个问题，本文引入Lyapunov在线优化思想。它的核心作用可以理解为：把一个长期约束问题，转化为每一轮都可以即时求解的小问题。

文章为能耗约束构造了一个虚拟能耗队列Q\_{t+1}=max{Q\_t-ϕ+E\_t}，该队列可以理解为当前系统的能耗压力。如果某一轮能耗E\_t超过长期能耗预算ϕ，队列就会变长，说明后续系统应该更重视节能；如果能耗较低，队列压力就会减小。

本文将每一轮的优化目标转化为最小化drift-plus-penalty的上界

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp08uMmgiaRwCOydyLZ6AUN2YIYbB1YTOssibk8rtarzy1sC7ibWWoTtXg2O6LwxvicBlDW2c23VG2nibaEM8sToRiaybnoEqum6iczDQ0/640?wx_fmt=png&from=appmsg)

该优化目标表示当前轮既要控制能耗超标，又要减少训练时延。其中，V是一个权衡参数，用来调节系统更偏向低时延，还是更偏向节能。

在得到每轮优化目标后，本文采用交替优化思想进行求解，拆成几个子问题依次处理：

1)固定其他变量，优化带宽和服务器计算资源

2)固定资源分配，优化设备是否参与聚合以及训练迭代次数

3)根据设备能力和网络状态，选择合适的模型切分层

这种处理方式的好处是降低了求解复杂度，使算法能够适应动态无线网络环境。整体来看，Lyapunov方法负责把长期随机问题转化为每轮在线问题，交替优化方法负责把复杂问题拆开求解，二者共同支撑了本文的资源调度算法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***04.***

**实验结果分析**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

本文通过仿真实验验证SAFSL框架和Lyapunov在线优化算法的有效性。实验中，系统设置为1个基站和10个无线设备，设备与基站之间的距离随机分布在100 m到1000 m之间。设备计算能力在[0.1,2]×10^9[0.1,2]cycles/s范围内随机变化，体现不同终端之间的计算异构性；基站侧最大计算资源设置为3×10^10 cycles/s，系统总带宽为50MHz。实验还考虑了无线信道随机衰落、设备发射功率、噪声功率谱密度等因素，使仿真环境更接近实际无线网络。

在学习任务方面，本文采用CIFAR-10和HAM10000两个数据集，并分别在AlexNet、VGG-19和ResNet-34三种典型深度神经网络上进行测试。其中，AlexNet参数量相对较小，VGG-19计算开销最大，ResNet-34处于二者之间，因此可以比较不同模型复杂度下SAFSL的表现。对比方法包括传统FL、Vanilla SL、FSL、FedAsync和ASFL。

**(1)训练收敛性能对比**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp18hZNZTPb72j6bxasjCrVlfR2iawKlWmwW6tPDfyPQN17VIDdGm7My0AbS66dJ2JI1BwFia88IQnDqkXkpdR...