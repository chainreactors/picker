---
title: 每周文章分享-283
url: https://mp.weixin.qq.com/s/3dSgBOE6FeQHNDpYd2qkxw
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:12:22.954537
---

# 每周文章分享-283

# 每周文章分享-283

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4DAaJy0Ok82ibMPxwHY4mibwrjmLoqmvIickMFksSta2uNYdIpd6BSh7GAKsqdYvoQq3Sg4RqvtofvuJLvGnIwDAIicnMN8A6wjias/640?wx_fmt=png&from=appmsg#imgIndex=56)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd79GRlwNhZak3b6NicAtrelJ5wXr5U8icCFGbOq9olPBSsVfSynibKpYAErrW6LMx4lyXdp5ibny1uCN8uPlrgJQNibuH3hYkIW2aBo/640?wx_fmt=png&from=appmsg#imgIndex=57)

**每周文章分享**

2026.11.02至2026.11.08

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4Ohaz7tlbUgBU08mJu9dD8frItmtjJ1C9xvR9d9Gic4CYK1bBjJA40NMpK6T89bFlj2aNTod2cSPT666sMXxIEia1FJy7QbLnrQ/640?wx_fmt=png&from=appmsg#imgIndex=60)

**标题:**Meta-SimGNN: Adaptive and Robust WiFi Localization Across Dynamic Configurations and Diverse Scenarios

**期刊:**IEEE Transactions on Communications, vol. 74, pp. 1732–1746, 2026. DOI: 10.1109/TCOMM.2025.3637041.

**作者:**Qiqi Xiao, Ziqi Ye, Yinghui He, Jianwei Liu, and Guanding Yu.

**分享人:**河海大学——杨禹卿

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd7PdTwqxaMfpIS26krIsxls3gvlWl17nYzpFj5Zhtqcwy3z6MhbZh7hZmegdwno07C0icPN2GlR16gtHMFHOjswwUIO0ZHZRjKM/640?wx_fmt=png&from=appmsg#imgIndex=73)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***01.***

**研究背景**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

工业移动机器人、增强现实和室内导航需要可靠的位置服务。WiFi基础设施部署广泛，利用信道状态信息（channel state information，CSI）进行指纹定位，可从多径传播中学习位置特征。然而，深度学习模型通常依赖特定环境和设备配置：房间布局、遮挡或人员活动改变会引起CSI分布偏移；接入点（access point，AP）数量、带宽和天线数量改变，还会使输入维度发生变化。既有元学习方法主要处理环境变化，难以直接解决输入尺寸不一致的问题。作者提出Meta-SimGNN，将细粒度CSI构图与相似度引导的元学习结合，在利用少量新场景标注数据的同时，适配动态设备配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***02.***

**关键技术**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

图神经网络（graph neural network，GNN）通过节点间的信息传递和聚合学习关系。本研究将每个AP作为一个节点，利用AP之间的空间关系融合多源CSI。图级池化能够将不同数量的节点汇聚为固定长度表示，为增减AP提供统一的预测接口。

空间金字塔池化（spatial pyramid pooling，SPP）按多个尺度划分特征图，对各区域池化后拼接。无论输入CSI图像的尺寸如何变化，输出长度均由池化层级决定，从而统一不同带宽及天线配置产生的节点特征。元学习则学习便于快速微调的模型初始参数，减少新场景重新训练的需求。

该方法的创新和贡献如下：

1）以AP为节点构图，同时使用幅相融合与SPP，分别处理CSI可靠性和输入维度变化。

2）为历史场景保存专属元参数，根据新旧场景的分布相似度选择微调初始化。

3）使用商用WiFi设备，在多场景及动态配置条件下验证定位精度和适应能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***03.***

**算法介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1GDIbQC4icbpSazRgglT4nJQ5iavjtoruGZDG1rv7a9u6ibglvDXmznhZpxG7E43sYqqzPsy7IWr6ly3dRuVbYOFQyWkvHyqzkM8/640?wx_fmt=png&from=appmsg)

图1  Meta-SimGNN整体框架

图1中，上方流程处理历史场景数据并训练元参数，下方流程处理新场景数据并完成微调与定位。两个阶段采用相同的CSI清洗、幅相融合和细粒度构图过程。系统最终输出用户设备的二维位置，模型以预测位置与真实位置之间的平方误差作为训练目标。

**（1）CSI清洗与幅相融合**

CSI同时包含幅度和相位。幅度反映信号强弱及频率选择性衰落，相位包含传播几何和多径信息，但更易受到频偏、同步误差等因素影响。作者先对幅度采用基于离散小波变换的滤波，再对相位采用已有校正方法去除偏移，避免把硬件误差直接当作位置特征。

对于第n个AP，将发射天线、接收天线与子载波维度展开并重排成二维方阵；图像边长N\_img由N\_tx、N\_rx和子载波数K\_n的乘积开平方后向上取整得到。每个AP单独生成一幅图像，不将固定数量的AP拼进同一幅图，因此AP数量改变不会破坏图像构建接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2gKCTz7wSmTBE3L5ISMN5ufIb7Zxyw9iaQ0fv4ibqMDLRyN8vypDxV7HJHuEKNCO9GZx2lRHZatoDUTVLVcaRAW9O2epjD1lzWg/640?wx_fmt=png&from=appmsg)

图2  幅度、相位及翻转幅度的三通道融合

图2的R通道使用幅度，B通道使用相位，G通道使用上下翻转后的幅度，随后组合成RGB图像。这里的“2∶1”表示两个幅度通道与一个相位通道的配置，并非对复数CSI进行2∶1加权求和。幅度占主导、相位辅助的表示旨在兼顾稳定性与空间信息，翻转则增加表示形式的多样性。

数据流可概括为：各AP的复数CSI→幅度与相位清洗→方阵重排→三通道CSI图像。其输出仍可能因带宽或天线配置而具有不同尺寸，需要继续提取固定维度特征。

**（2）固定维度特征提取与细粒度构图**

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1kUNXctiafCRxe0hicsSm0jvsFq32cOypRbIvuErwxfzAX26ib1Go23EoVUjXoYsRJJoDDZannjC8CAEmI5KtatIG1wcVdKltuuE/640?wx_fmt=png&from=appmsg)

图3  基于空间金字塔池化的特征提取

图3中，CSI图像先经过卷积模块提取局部模式，模块使用线性整流函数（rectified linear unit，ReLU）和批归一化（batch normalization，BN）。不同尺寸图像产生不同大小的特征图，但SPP在每一层级输出预定数量的池化区域，再由全连接层形成固定长度的AP特征。

例如，若池化层级采用1×1、2×2和4×4网格，每个特征通道会产生1+4+16=21个值，输入边长变化时这一数量仍保持不变。该例用于解释SPP机制；论文以L\_pool和c\_l描述一般层级及其网格大小。SPP解决的是特征维度一致性，并不意味着不同带宽提供的信息量完全相同。

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0wfv5v0BWSwB5hXKtIzgHPKXUdStczP5dpbqydxhv2nhr25wlglib6ibErGG4zEsVJJDP902NLH2kOXJVwyKTbuV7T7LpVXuLm0/640?wx_fmt=png&from=appmsg)

图4  以AP为节点的细粒度CSI图

图4中，每个AP对应一个节点，其初始特征x\_n^(0)来自前述特征提取网络。作者考虑室内AP部署规模较小，构造任意两AP之间均有连接的完全图。对不同AP之间的边，权重A\_n,m=1/d\_n,m，d\_n,m为两个AP的欧氏距离；距离越远，信息聚合时赋予的权重越小（原文式(6)）。

构图后，模型通过3层图卷积传播和更新节点特征，每层后接ReLU与BN。全局平均池化将全部AP节点汇聚成图级表示，再由全连接层回归位置。AP数量变化对应节点数量变化，无需将预测网络改成不同输入宽度。训练时最小化位置平方误差（原文式(7)），使节点特征与AP空间关系共同服务于定位。

**（3）相似度引导的元学习与新场景微调**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1UVNDHUnl8uztI36GU3Frr3V4bIEibjkG4biciaZgFJhWo0QXnC8pFiaL1uXOw54AIRBxbEcZOxnze3ial9aicmStZDuSiaS1SfhftvE/640?wx_fmt=png&from=appmsg)

图5  场景专属元参数训练与相似度引导微调

图5上半部分为历史场景元训练，下半部分为新场景适配。作者采用模型无关元学习（model-agnostic meta-learning，MAML）的内外循环框架，但保留各历史场景对应的参数，而非仅依赖一组面向所有场景的共享初始化。新场景首先选择合适的历史参数，再使用少量已知位置的CSI样本微调。

**A. 历史场景元训练**

对第p个历史场景的数据随机分组，每组划分支持集S\_p,i和查询集Q\_p,i。内循环在支持集上进行梯度更新，得到组专属参数theta\_p,i'；外循环评价更新后模型在查询集上的位置误差，并据此优化初始参数theta。内、外循环学习率分别为alpha和beta，对应原文式(8)与式(9)。支持集负责快速适应，查询集负责评价适应后的表现。

完成迭代后，保存该场景的元参数theta\_p\*。对历史场景重复这一过程，获得可供选择的参数集合。其作用是保留不同典型环境的适应起点，减少新场景从不匹配初始化出发所需的调整。

**B. 场景相似度计算与参数选择**

作者使用图自编码器压缩CSI图：编码器由3层图卷积及池化组成，输出低维场景表示；解码器通过重建输入图训练编码器。随后使用最大均值差异（maximum mean discrepancy，MMD）比较新旧场景嵌入的分布，采用高斯核计算距离。MMD越小，表征分布越接近；选取MMD最小的历史场景p\*及其参数theta\_p\*。

**C. 微调与位置预测**

从选定参数出发，在新场景支持集S\_ne上执行L\_f轮梯度更新，再在查询集Q\_ne上评价模型（原文式(12)）。部署时，新采集CSI按相同流程构图并输入微调后的GNN得到位置。相似度由数据表征计算，不是人工判断房间名称；该方法仍依赖少量带位置标签的新场景样本。用于场景相似度学习的数据按原文假设采用统一设备配置，这与定位网络支持动态配置的范围应区分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***04.***

**实验结果分析**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

**（1）实验设置**

实验部署4台TP-LINK AX5400路由器，接收端使用双天线Intel AX210网卡，天线间距6 cm。设备采用IEEE 802.11ax标准，中心频率5.25 GHz，带宽取20、40或80 MHz；AP与接收端天线高度分别为1.8 m和1.55 m。通过PicoScenes在监听模式下以100 Hz采集CSI，模型由Python 3.9.0与PyTorch 1.11.0实现。

场景1为8×9 m教室，另设人员走动干扰条件；场景2为8×7 m会议室；场景3为8×9.5 m实验室。参考点（reference point，RP）间距为0.5 m。各场景初次在每个RP采集1000个数据包，15天后再采集1500个；教室另采集存在障碍干扰的数据。默认每个RP用80个CSI样本进行历史场景训练，用20个样本进行新场景微调，其余用于测试。

比较方法包括不采用元学习的GNN、结合传统MAML的Meta-GNN，以及MetaLoc中的MAML-TS和MAML-DG。评价主要使用平均定位误差，同时报告部分误差分布与标准差。MAML-TS、MAML-DG的实现固定使用3个AP，其AP利用能力与图网络方法存在差异，结果应结合这一条件理解。

**（2）带宽与AP数量变化**

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2yAOBrfGMuaumI5JKGNkWAN1Cemu1wGFj1G6r0T2tLyvgdVgTXJoora7oWFWAiccKic1lMByggrSwicm8Vt4apg1mABvDkBc5Cyc/640?wx_fmt=png&from=appmsg)

图6  带宽与AP数量对定位误差的影响

图6左图横轴为带宽，纵轴为平均定位误差。Meta-SimGNN在20、40、80 MHz下的误差分别为1.63、1.53、1.45 m。较大带宽提供更多子载波，四种方法的误差总体降低。需要注意：原文Fig.14对各带宽分别训练，并在含干扰的对应带宽数据上测试，因此该图本身不能证明“只用一种带宽训练即可迁移至其他带宽”。

图6右图横轴为AP数量。Meta-SimGNN误差从2个AP时约1.93 m降至4个AP时约1.70 m，Meta-GNN也随AP增多改善。固定使用3个AP的两种MetaLoc基线不能利用第4个AP；少于3个AP时无法按其原接口工作。结果说明可变节点构图能够利用额外AP信息，且性能受实际可用AP数量影响。

**（3）跨场景误差与少样本适配**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp0I8v1vsOrYo...