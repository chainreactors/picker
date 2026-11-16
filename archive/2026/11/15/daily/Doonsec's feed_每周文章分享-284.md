---
title: 每周文章分享-284
url: https://mp.weixin.qq.com/s/13hLgOSb7IjJ7LglKH4QeQ
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:46:16.954425
---

# 每周文章分享-284

# 每周文章分享-284

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4DAaJy0Ok82ibMPxwHY4mibwrjmLoqmvIickMFksSta2uNYdIpd6BSh7GAKsqdYvoQq3Sg4RqvtofvuJLvGnIwDAIicnMN8A6wjias/640?wx_fmt=png&from=appmsg#imgIndex=56)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd79GRlwNhZak3b6NicAtrelJ5wXr5U8icCFGbOq9olPBSsVfSynibKpYAErrW6LMx4lyXdp5ibny1uCN8uPlrgJQNibuH3hYkIW2aBo/640?wx_fmt=png&from=appmsg#imgIndex=57)

**每周文章分享**

2026.11.09至2026.11.15

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4Ohaz7tlbUgBU08mJu9dD8frItmtjJ1C9xvR9d9Gic4CYK1bBjJA40NMpK6T89bFlj2aNTod2cSPT666sMXxIEia1FJy7QbLnrQ/640?wx_fmt=png&from=appmsg#imgIndex=60)

**标题:**Federated Generalized Category Discovery via Personalized Contrastive Graph Learning

**期刊:**IEEE Transactions on Information Forensics and Security,VOL.21,2026

**作者:**Wenjing Li,Nan Pu,Jessica Fan,Nicu Sebe,and Zhun Zhong

**分享人:**河海大学——张宇

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd7PdTwqxaMfpIS26krIsxls3gvlWl17nYzpFj5Zhtqcwy3z6MhbZh7hZmegdwno07C0icPN2GlR16gtHMFHOjswwUIO0ZHZRjKM/640?wx_fmt=png&from=appmsg#imgIndex=73)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***01.***

**研究背景**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

广义类别发现（GCD）希望利用已知类的标注去聚类同时包含已知类与未知类的无标注样本，但传统广义类别发现方案必须把所有数据集中到中心服务器训练，这在医疗、金融、交通等隐私敏感场景（如各地医院的病例既需联合诊断已知疾病、又要及早发现未知疾病，但原始数据却受法规限制不能共享）下难以落地；此外现有方法几乎只盯着全局模型的提升、忽视了本地个性化的表现，导致本地模型甚至比单独用本地数据训练还差，且在客户端分布异构时，把这些有偏的本地更新一刀切地均匀聚合又会因类别关系估计不一致而带偏全局优化方向，被聚合后的全局模型再分发回去又进一步扭曲下一轮的本地关系估计，形成一个自我强化的负反馈循环。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***02.***

**关键技术**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

本文提出了一种全新的个性化本地图对比学习（PCGL）框架，该框架能够提升所学表征在未知类别上的泛化能力，让Fed-GCD模型可以灵活地处理通用知识与个性化知识。PCGL包含本地图对比学习（LGCL）模块与个性化知识聚合和提取（PKAE）模块。LGCL旨在充分利用未标注数据中的知识来增强表征学习。PKAE致力于缓解全局模型与本地模型之间的冲突，从而共同提升这些模型的性能。

1．在LGCL中，本文训练了一个KNN-former，其遵循渐进式范式，根据样本的邻域信息来预测样本之间的对比关系；随后，本文提出了一种混合对比学习损失，以充分利用预测得到的关联关系，从而进一步改进局部表征学习。

2．在PKAE中，首先引入了一种基于相似度匹配的个性化聚合机制，随后进一步提出自适应参数掩码技术，仅提取模型中与训练相关的参数，使模型在学习更全面的通用表征的同时，能够灵活地保留个性化性能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***03.***

**算法介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

整个系统包含N个本地客户端和一个服务器。每个客户端持有三部分：特征提取骨干网络φ、一个个性化的参数化GCD分类头θ，以及一个可聚合的KNN-Formerψ。由于各客户端标签空间互不兼容、无法对分类器做参数平均，因此分类头θ始终留在本地、不上传；跨端传输的只有骨干网络和KNN-Former。服务器侧把各端上传的骨干网络聚合为一个未掩码的通用骨干网络，作者把它定位成一个“通用知识银行（knowledge bank）”，沉淀跨客户端的完整类别知识；本地个性化模型则在这个通用骨干网络的基础上经私有掩码抽取得到。

图1给出了本文所提方案的完整结构：(a)是基线方法Fed-Sim，即在SimGCD上套用FedAvg，服务器只对骨干做平均聚合；(b)是PCGL主流程——本地骨干网络提取特征并构造KNN图，送入KNN-Former渐进学习样本对对比关系，经精炼得到个性化对比关系与伪标签，再做混合对比学习优化骨干网络，最后把骨干与KNN-Former上传，由FedAvg平均聚合与个性化聚合共同处理；(c)是带自适应参数掩码的KNN-Former内部结构；(d)是基于公共数据集的相似度匹配个性化聚合流程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1XKUhERwricRh9QFiaOdEic0d0fOvXlGrzovP6H3UF1EYZB4vkq1tnvCicI83q8CVlpiaITSggzIRABjOnUYhkiaFZmkia48iaKniaGdwg/640?wx_fmt=png&from=appmsg)

图1：PCGL框架图：(a)基线Fed-Sim；(b) PCGL主流程；(c)带自适应掩码的KNN-Former；(d)基于功能相似度的个性化聚合

**A. LGCL:本地图对比学习**

LGCL分两阶段：先训练KNN-Former学对比关系，再用关系做对比学习优化骨干网络，具体分五步。

(1).KNN图构建：用骨干网络提取每个样本x\_i的特征向量v=φ(x\_i)，按余弦相似度为每个节点与其N^k个最近邻相连。设N\_i表示节点v\_i的N^k个最近邻的索引集。边集E的计算公式如下:

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1iaJcGqQsakKEJK0fknFBX90tjmmJ3oDbZsZeKqqCqOsnLVJf7duQfU5IAuSzywe43uic6j0b0JwqjjS88r1KNWeYg5YmeDxdv8/640?wx_fmt=png&from=appmsg)

(2).KNN-Former设计：KNN-Former采用Transformer架构（3个相同层，每层含多头注意力与前馈网络，末尾接MLP）。对一对节点样本，先把各自特征与近邻特征拼成邻域矩阵，过Transformer编码器后取出代表双方的聚合特征，再把原始特征与聚合特征拼接后送入MLP与Sigmoid，输出两节点的连接概率。

(3).渐进式训练与动态置信因子：该训练目标是二元交叉熵形式的对比关系预测损失：文章设计了一种基于二元交叉熵损失的渐进式学习方法。首先，对于有标签数据，作者将具有相同类别标签的第i个样本和第j个样本视为正样本对，即s\_i,j的真值为1，否则其真值为0。其次，对于包含无标签数据的样本对，作者采用动态因子η来过滤低置信度的样本对。该因子随训练轮次ep的增加而减小，其定义为η=η\_begin\*ε^ep(初值η\_0=0.85，衰减系数ε=0.98)，其中为ε为衰减因子。整体训练目标为

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1Fo5tHVzGyxXEmFfIRKletfhXEIAt2TXkhqrKMdg2OFJ0fRibtsnI6JChyvSBwcaccDhFRL4njG5U8wAMgVBsPAf2bGvusvWrs/640?wx_fmt=png&from=appmsg)

(4).对比关系优化：用训练好的KNN-Former预测全量样本对关系，按阈值η\_0过滤不确定关系，进一步引入Infomap作为现成工具，为有标签数据和无标签数据生成最终的伪标签，形成带伪标签的代理数据集。

(5).混合对比学习(HCL)：先以GraphSampling按P=4个簇、每簇K=32个样本在小批量内提供有意义的对比样本，再结合KNN-Former给出的实例级与簇级双层对比关系构造混合对比学习损失，最后与SimGCD目标按权重λ加权融合为总损失（主实验λ=0.1，超参分析优选0.3）。

一个小批量中第i个实例的HCL损失：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0HEpydr6Licia2wsYRibGsYHrDRm6Gsc98neEEnD8KicSWsaMVebFaV2IBa4Qiad2uoK9Hsf8bfDVx47ZNw428zGPqHFgIhHXukqsk/640?wx_fmt=png&from=appmsg)

总损失：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1icRFfraJJUQY8vibGAGibzowu6NkL0u2iaLdVg4A2eyqNtrGCqpAEz1heQGJsJvOL0mcVVdSBAXgWgGJ6hicUWqUpuTbTOH4sbiaSc/640?wx_fmt=png&from=appmsg)

**B. PAKE：个性化知识聚合与提取**

(1).基于功能相似度的个性化聚合(针对KNN-Former)：不再对所有客户端的KNN-Former做一刀切平均，而是用一个公共数据集构建KNN图作为统一输入，输入给各端KNN-Former，比较它们输出之间的余弦相似度，再经softmax得到各端的聚合权重；只向功能相似、类别知识相关的KNN-Former借力，避免把无关社区的知识误吸取进来。

客户端i和j的KNN-Former之间的相似性为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1FPxz1v2jGSwr9uVDjJeSoOJf5GiankWKtyHVhicY1zAz5vebTicGI6lmOcwre4WsFH32eXp84kZAwnjNhibcPwptsH7j8kmtVH2Y/640?wx_fmt=png&from=appmsg)

(2).自适应参数掩码：本文为KNN-Former设计一个私有掩码、为骨干网络另设一个私有掩码（均不出本地），个性化模型由全局权重经掩码逐元素相乘调制得到，掩码取值经clamp函数限制在[0,1]范围内，初始化为全1。掩码在这里扮演“知识选择器”：低值（接近0）过滤掉知识银行里与本客户端无关的知识，高值抽取本客户端需要的知识。

(3).个性化目标、通用目标与联合优化：个性化目标为同时优化个性化KNN-Former的关系预测与掩码骨干网络的混合对比学习；通用目标则在未掩码的通用骨干网络上优化，不涉及私有掩码。两者相加构成联合目标，不引入额外权衡系数。作者还给出梯度层面的解释：个性化骨干网络由通用骨干网络经掩码逐元素缩放得到，回传到通用骨干网络的梯度也被同一掩码逐元素缩放，由于掩码元素∈[0,1]，缩放后的梯度范数不会超过原梯度范数，因此掩码不会放大作用于共享表示的个性化梯度，只会抑制无关维度；并且掩码对通用目标的梯度为零，私有掩码的优化不会直接改动通用目标，这就在数学上保证了个性化不会反噬泛化。

PCGL的整体目标可表述为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2kMVbtsVqzziaP8BWGuoU8sAygmsD5dPdeGeiaeRsQZb94W3aREkad5E4a5sO4icrtOiaGCn2SYrc0XCfxL5tW7KjxFLDxNaet6nk/640?wx_fmt=png&from=appmsg)

(4).交替优化与推理。先用基线Fed-Sim对骨干网络进行预热，随后每轮交替优化关系预测与表示学习目标，然后在服务器进行聚合，共100轮。推理时：个性化评估用掩码骨干网络加本地GCD分类器在本客户端无标注数据上进行预测；全局泛化评估用未掩码的聚合通用骨干网络，在服务器测试集上做k-means（真实类数已知），再用匈牙利算法匹配聚类与真实类别。

图2展示了学到的参数掩码可视化图:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1yqbdHMtw79miaet1TaJZXkPEwUrjB9zqFoGr5LrK4OyYB1qnnVu5GNQA2rX3yiaus6okDbUpo8hgjxyTibhcquDc3HbeWFz0H1k/640?wx_fmt=png&from=appmsg)

图2 客户端在CUB-200数据集上学习到的掩码的可视化(类别更少的Client 1以低掩码值为主，类别更多的Client 5出现大量高值掩码，说明掩码在按本端需求筛选知识)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***04.***

**实验结果分析**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

实验设置

论文的数据集设置为通用数据集CIFAR-10､CIFAR-100､ImageNet-100;细粒度数据集CUB200､Stanford Cars､Oxford-IIIT Pet;长尾数据集Herbarium19(683类植物)与NIH-CXRLT(20类胸片)｡每个数据集取一半类为旧类别,每个标注类随机抽50%样本作标注子集､其余作无标注子集；实验设置了三组对比方法：第一组使用SimGCD单独训练本地GCD模型，不进行参数掩码和客户端通信，即“Local-Sim”。第二组采用现有的联邦GCD方法(Fed-GCD和AGCL)，采用非参数推理。第三组将PCGL与基于SimGCD的基线方法(即“Fed-Sim”)进行比较，并将最先进的集中式GCD方法(DCCL、PromptCAL、CMS)适配到本文所提的pFed-GCD框架...