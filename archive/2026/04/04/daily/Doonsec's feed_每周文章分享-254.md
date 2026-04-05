---
title: 每周文章分享-254
url: https://mp.weixin.qq.com/s/d1yS2kap6xnQ3XH11kd1-g
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:37:17.800355
---

# 每周文章分享-254

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jBQAokCLibp3Qqt3Md90S7dOucanM2uuyODEH0HOHiciaRSdxicC6r4820otAzkPawMic3dfWDlwzy2BPE9WKEqhw5X5gymiczUGNRM7loabuibvog/0?wx_fmt=jpeg)

# 每周文章分享-254

网络与安全实验室

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4DAaJy0Ok82ibMPxwHY4mibwrjmLoqmvIickMFksSta2uNYdIpd6BSh7GAKsqdYvoQq3Sg4RqvtofvuJLvGnIwDAIicnMN8A6wjias/640?wx_fmt=png&from=appmsg#imgIndex=56)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd79GRlwNhZak3b6NicAtrelJ5wXr5U8icCFGbOq9olPBSsVfSynibKpYAErrW6LMx4lyXdp5ibny1uCN8uPlrgJQNibuH3hYkIW2aBo/640?wx_fmt=png&from=appmsg#imgIndex=57)

**每周文章分享**

2026.03.30至2026.04.05

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4Ohaz7tlbUgBU08mJu9dD8frItmtjJ1C9xvR9d9Gic4CYK1bBjJA40NMpK6T89bFlj2aNTod2cSPT666sMXxIEia1FJy7QbLnrQ/640?wx_fmt=png&from=appmsg#imgIndex=60)

**标 题:**FLGuardian: Defending Against Model Poisoning Attacks via Fine-Grained Detection in Federated Learning

**期刊:**IEEE TRANSACTIONS ON INFORMATION FORENSICS AND SECURITY, VOL. 20, 2025

**作者:**Xingjie Zhou , Xianzhang Chen , Shukan Liu , Xuehong Fan , Qiao Sun , Lin Chen , Meikang Qiu ,and Tao Xiang

**分享人:**河海大学——田檬

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd7PdTwqxaMfpIS26krIsxls3gvlWl17nYzpFj5Zhtqcwy3z6MhbZh7hZmegdwno07C0icPN2GlR16gtHMFHOjswwUIO0ZHZRjKM/640?wx_fmt=png&from=appmsg#imgIndex=73)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***01.***

**研究背景**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

联邦学习（FL）作为一种分布式机器学习范式，允许多个参与者在不共享本地训练数据的前提下协同训练全局模型，契合隐私法规要求并已在词预测、风险评估、医学成像等多个领域成功应用，其核心流程为服务器分发全局模型、客户端本地训练后上传模型更新、服务器聚合更新迭代全局模型，但由于数据存在非独立同分布（non-IID）特性，联邦学习易遭受模型投毒攻击（MPAs），这类攻击分为无目标攻击和有目标攻击，且可进一步分为篡改整个模型参数的模型空间攻击和仅篡改部分特定层参数的层空间攻击，其中新兴的层空间攻击（如LPattack）隐蔽性更强；尽管现有拜占庭鲁棒聚合规则等防御方法能应对传统模型空间攻击，但模型空间防御因仅关注全局模型参数差异，难以识别层空间攻击的微小全局差异，层空间防御要么仅关注固定层、要么将所有层视为同等重要，无法应对层空间攻击灵活选择攻击层且仅植入少量攻击层的特点，实验表明现有主流防御方法在面对LPattack时后门成功率（BSR）均超过93%，完全无法有效防御，因此亟需设计一种自适应的分层防御方法，精准识别层空间攻击中的恶意客户端，保障联邦学习系统的安全性与鲁棒性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***02.***

**关键技术**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

本文提出的FLGuardian框架针对联邦学习（FL）中新兴的层空间模型投毒攻击（MPAs）展开防御，其核心创新与贡献如下：

1）提出了首个能有效抵御层空间后门投毒攻击的防御方法FLGuardian，突破了现有防御要么聚焦模型全局、要么忽视层间差异的局限，填补了层空间隐蔽攻击防御的技术空白，尤其对LPattack等新型攻击表现出显著防御效果。

2）创新设计了分层加权的检测与评分机制，首次在防御中考虑模型层的重要性差异——基于神经网络深层含高维特征、攻击影响更大的特性，为深层赋予更高权重，通过累加客户端在各层良性集的加权得分计算信任值，精准识别仅篡改少量关键层的隐蔽恶意客户端。

3）融合双距离聚类的细粒度分层检测策略，针对无目标攻击和后门攻击的不同特性，分别采用成对余弦距离（捕捉角度偏差）和成对欧氏距离（捕捉参数篡改幅度），结合k-means聚类取交集得到各层良性集，实现对两类攻击的全面覆盖与精准检测，避免单一距离指标的防御盲区。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***03.***

**算法介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![image.gif](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1Aia5kbcZ8FC6SwDiaAsNZsXvejEnpSG7xvFfpDFdor07I7Qu9SKH438zlHMR30fqF0hnGviatFAFMNeibg7uDmnKLMZyApLEBXvc/640?wx_fmt=png&from=appmsg)

图1 FLGuardian的框架图

FLGuardian的防御流程围绕 “客户端上传模型更新→服务器分层处理与检测→加权评分→筛选聚合”展开，全程在服务器端完成，不增加客户端额外通信与计算开销，具体步骤如下。

**步骤1：模型更新分层与本地训练**

客户端基于本地数据集D\_i和服务器分发的全局模型w^t−1，通过本地训练生成模型更新g\_i^t，训练过程遵循经典联邦学习本地更新逻辑（如SGD优化）。

服务器接收所有选中客户端的g\_i^t后，按模型结构将其拆解为各层独立的参数更新g\_it^(l)（l=1,2,...,L），实现按层单独检测。

**步骤2：双距离计算（余弦距离+欧氏距离）**

针对每一层l，服务器计算所有客户端对之间的两类距离，分别适配无目标攻击和后门攻击的检测需求：

**（1）成对余弦距离（适配无目标攻击）**

无目标攻击通过制造模型参数的角度偏差降低全局模型精度，余弦距离可精准刻画该偏差，公式定义为：

![image.gif](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3rpOxQiav8aQicV3ejsZVZ54hXdPRanJoAnCgAcWibn0jXLkQAAMI73NxDdRXiajoaxSs2UOXsMvYEIibvAdr0FrwiaRoM4sHwYvWtA/640?wx_fmt=png&from=appmsg)

其中，c\_ij^t(l)∈[0,2]，值越大表示两客户端第l层参数更新的角度差异越大，客户端越可能是恶意的。

**（2）成对欧氏距离（适配后门攻击）**

后门攻击（无论高毒化率还是参数缩放策略）会导致参数更新的幅值偏差，欧氏距离可捕捉该差异，公式定义为：

![image.gif](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1MngIQ5wYtRJe5FjF72IOCTgWia3OX9NCoktDrQxv8jZEuJjOIVB2m6ic17YA4bXkKG8xX7dJtzqfuxjLtWlMoDibPnFu6Kiaz7mU/640?wx_fmt=png&from=appmsg)

其中，e\_ij^t(l)≥0，值越大表示两客户端第l层参数更新的幅值差异越大，后门攻击的可能性越高。

**步骤3：k-means聚类与良性集确定**

对每一层l的两类距离（c\_ij^t(l)和e\_ij^t(l)），分别执行k-means聚类（聚类数K=2），核心逻辑如下：

由于恶意客户端占比不超过50%，聚类后规模更大的集群为该距离指标下的候选良性集（记为Scost(l)和Seuct(l)）；

取两个候选良性集的交集，作为第l层的最终良性集，确保仅保留在两类距离下均无异常的客户端：St(l)=Scost(l)∩Seuct(l)若客户端i属于St(l)，则标记其第l层为良性（x\_i^(l)=1），否则为恶意（x\_i^(l)=0）。

**步骤4：分层加权评分与客户端筛选**

基于神经网络“深层含高维特征、攻击影响更大”的特性，为各层分配与深度正相关的权重，计算客户端的信任得分：

**（1）信任得分计算**

客户端i的信任得分为其所在所有良性层的权重之和，公式如下

![image.gif](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp0C82vk4UwrMbGicDLvRATOYtvoHMj9dQoKM7fx0gJm5tNRlcY6lBMUNEUuUQXHF4FH2bD33RDsxt59cOL0b9vevpQsCyWYvaHk/640?wx_fmt=png&from=appmsg)

其中，β为权重调节参数（论文默认β=2），β^l表示第l层的权重——层越深（l越大），权重越高，可精准惩罚篡改深层关键层的隐蔽攻击（如LPattack）。

**（2）筛选与全局模型聚合**

服务器按score\_i降序排序，选择前k个高得分客户端的模型更新进行平均聚合，更新全局模型：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp0mCgaq7lMzdzcxXFLMtMyMjMN412tadKkVZjJEq6hkeZwMnweRqibe3cJ01CTXIrQWGibLYlegf8ibrqcrkT0V2AbFnqfia3VrHRg/640?wx_fmt=png&from=appmsg)

其中，S为得分前k的客户端集合，该聚合方式可有效剔除恶意客户端的干扰，保障全局模型的安全性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***04.***

**实验结果分析**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

**（一）实验设置**

**（1）硬件与软件环境**

实验基于NVIDIAA100TensorCoreGPU，采用PyTorch框架实现，所有模型训练、攻击模拟及防御验证均在该环境下完成，确保计算效率与结果稳定性。

**（2）数据集与模型配置**

数据集：选用MNIST、Fashion-MNIST（FMNIST）、CIFAR-10三大主流图像分类数据集，均含10个类别。其中MNIST和FMNIST各含60,000训练样本、10,000测试样本；CIFAR-10含50,000训练样本、10,000测试样本，覆盖不同图像复杂度场景。

数据分布：采用非独立同分布（non-IID）设置，通过参数q=0.5控制数据分布差异（q越大非-IID程度越高），模拟真实联邦学习中客户端数据异质性。

全局模型：MNIST和FMNIST采用4层卷积神经网络（CNN），CIFAR-10采用ResNet18模型，模型架构贴合数据集特征提取需求，确保实验的代表性。

**（3）攻击与防御配置**

攻击类型：涵盖4种无目标攻击（Trimattack、Min-Max、Min-Sum、LIE）和3种后门攻击（ModelReplacementAttack、DBA、LPattack），其中LPattack为新兴层空间隐蔽攻击，是核心验证对象。

恶意客户端配置：默认20%客户端为恶意，每轮训练随机选取10个客户端（含2个恶意客户端），后续通过变量实验验证比例提升至40%时的防御鲁棒性。

对比防御方法：选取9种主流防御方法，包括FedAvg、FLTrust、Multi-Krum、FLARE、DeFL、FLANDERS、FLAME、DeepSight等，全面对比验证FLGuardian的性能优势。

评估指标：无目标攻击采用模型准确率（MA）评估；后门攻击采用“主任务准确率（MA）/后门成功率（BSR）”双指标，BSR低于10%视为防御有效。

**（二）实验结果**

**（1）层空间攻击（LPattack）的专属防御效果**

针对新兴的LPattack（层空间后门攻击），原文Fig.1展示了不同防御方法的BSR变化趋势。实验结果显示，所有对比防御方法（包括FLTrust、Multi-Krum、DeFL、DeepSight等）的BSR随训练迭代次数增长均快速上升，训练至200轮时均突破93%，完全丧失防御能力；而FLGuardian全程将BSR稳定控制在3%以下，成为唯一能有效抵御层空间攻击的方法。

![image.gif](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2jicJpZPrpibnU5UPbnyK2ofdBw7wosbswicLwRn5VymCa3ETc9ZMxHTs2e98b6ZDHWf2MYXyBp5EIU6f1kyNdxkKoLOib7BL7GmM/640?wx_fmt=png&from=appmsg)

这一差异源于LPattack的隐蔽性特点：其仅篡改模型少数深层关键层参数，传统模型空间防御因聚焦全局参数差异，难以识别局部层的微小篡改；现有层空间防御要么平等对待所有层（如DeFL），要么仅检测固定层（如FLARE关注倒数第二层），无法应对LPattack灵活选择深层攻击的策略。FLGuardian通过分层加权评分机制，为深层赋予更高权重，精准识别并排除篡改关键层的恶意客户端，实现了对层空间攻击的针对性防御。

**（2）不同攻击类型下的综合防御性能**

基于原文TableIV的实验数据，FLGuardian在所有7种攻击类型下均表现出卓越性能：无目标攻击场景中，其MA始终保持在74%以上（CIFAR-10数据集），显著高于FLTrust（最低45.91%）、FLARE（最低20.11%）等对比方法；后门攻击场景中，其MA未低于67.8%，且BSR均控...