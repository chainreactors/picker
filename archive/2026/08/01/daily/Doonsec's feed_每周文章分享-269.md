---
title: 每周文章分享-269
url: https://mp.weixin.qq.com/s/2fFNhQP26fT_qS-qS3JD-Q
source: Doonsec's feed
date: 2026-08-01
fetch_date: 2026-08-02T05:09:48.048666
---

# 每周文章分享-269

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jBQAokCLibp2OztEzhCx9DAMmv0Wtnw6JfRF3GcgVKpIJAAubhSFljNGFXIPAzyZIMdDZycgfHvaGq1ibiblicgauEFX2AhtDTu7PCHI3FUYoW8/0?wx_fmt=jpeg)

# 每周文章分享-269

网络与安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4DAaJy0Ok82ibMPxwHY4mibwrjmLoqmvIickMFksSta2uNYdIpd6BSh7GAKsqdYvoQq3Sg4RqvtofvuJLvGnIwDAIicnMN8A6wjias/640?wx_fmt=png&from=appmsg#imgIndex=56)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd79GRlwNhZak3b6NicAtrelJ5wXr5U8icCFGbOq9olPBSsVfSynibKpYAErrW6LMx4lyXdp5ibny1uCN8uPlrgJQNibuH3hYkIW2aBo/640?wx_fmt=png&from=appmsg#imgIndex=57)

**每周文章分享**

2026.07.27至2026.08.02

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4Ohaz7tlbUgBU08mJu9dD8frItmtjJ1C9xvR9d9Gic4CYK1bBjJA40NMpK6T89bFlj2aNTod2cSPT666sMXxIEia1FJy7QbLnrQ/640?wx_fmt=png&from=appmsg#imgIndex=60)

**标题:**FLgym: Toward Robust and Byzantine-Resilient Federated Learning

**期刊:**IEEE Transactions on Information Forensics and Security,vol. 21, 2026

**作者:**Ke Xiao , Qiyuan Wang , and Christos Anagnostopoulos

**分享人:**河海大学——骆凯文

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd7PdTwqxaMfpIS26krIsxls3gvlWl17nYzpFj5Zhtqcwy3z6MhbZh7hZmegdwno07C0icPN2GlR16gtHMFHOjswwUIO0ZHZRjKM/640?wx_fmt=png&from=appmsg#imgIndex=73)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***01.***

**研究背景**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

联邦学习（Federated Learning, FL）作为一种分布式机器学习范式，允许多个客户端在不共享原始数据的情况下协同训练全局模型，有效保护了数据隐私。然而，由于缺乏对客户端行为的集中管控，联邦学习系统天生易受投毒攻击。恶意客户端（又称拜占庭客户端）可以通过提交被操纵的模型更新来破坏全局模型的性能和完整性。

随着攻击手段日益复杂，如标签翻转、Fang攻击、Min-Max攻击和LIE攻击等，传统的异常检测技术往往难以奏效。现有的防御机制大多从单一维度进行拜占庭客户端检测，导致较高的假阳性率（False Positive Rate, FPR）和假阴性率（False Negative Rate, FNR）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***02.***

**关键技术**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

针对上述挑战，本文提出了FLgym——一个两阶段的拜占庭容错联邦学习框架。FLgym整合了三大核心组件：基于模型相似度的检测机制、基于客户端本地数据相似度估计的验证机制，以及针对已识别拜占庭客户端的权重恢复机制。

该方法的主要创新和贡献如下：

1）提出了两阶段拜占庭客户端检测框架：第一阶段采用基于基础网络（Base Network, BN）相似度的距离分析，利用模型浅层特征的稳定性进行初步筛查；第二阶段引入基于数据分布相似度的可信客户端验证机制，有效降低了非独立同分布场景下的假阳性率。

2）设计了基于窗口的权重恢复机制（Weight Recovery Mechanism, WRM）：对于被误判为拜占庭的良性客户端，通过渐进式恢复其聚合权重，减轻假阳性对模型性能的影响；同时引入概率性复检机制，防止真实的拜占庭客户端利用恢复过程进行攻击。

3）进行了全面的实验验证：在多个数据集和多种攻击场景（下，FLgym均取得了优于现有方法的性能，实现了最高90.95%的真阳性率（TPR）和最低6.3%的假阳性率（FPR）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***03.***

**算法介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

**（1）系统架构**

FLgym采用两阶段检测框架，结合了距离感知和模型评估两种视角，以提高检测效率和准确性。系统由一个服务器和多个客户端组成，整体工作流程如下：

第一阶段：服务器将全局模型分发给客户端，并指定模型浅层作为基础网络（BN）。客户端在本地训练后，将模型参数及训练准确率、损失值上传至服务器。服务器计算所有客户端之间的BN参数相似度，初步识别出明确的拜占庭客户端和可疑客户端。

第二阶段：对于可疑客户端，服务器根据客户端本地数据分布相似度估计，选择数据分布最相似的客户端作为验证器，将可疑客户端的模型发送给验证器进行验证。验证器在本地数据上评估该模型的性能，并将结果反馈给服务器。服务器综合验证结果，最终确定拜占庭客户端。

权重恢复机制（WRM）：服务器维护每个客户端被标记为拜占庭的最近轮次和权重恢复因子。被标记为拜占庭的客户端权重被置零，随着训练进行，其权重逐步恢复。恢复过程中的客户端会以一定概率被重新送入第二阶段验证，防止恶意客户端利用恢复机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp12iaOibyibxEyW8kDbgOkoGHBBVYTceZCqB3Vto5Q9LcdNz5xia0BQch27pgL2UEIHjUmeqdRvvQ7AW1bAgSibWnwMrjJxjiaXe1cfA/640?wx_fmt=png&from=appmsg)

图1  FLgym系统模型架构

**（2）系统设置**

**1. 第一阶段：基础网络距离分析**

FLgym创新性地选择模型的浅层（Base Network, BN）作为相似度计算的基础。实验表明，即使在数据分布差异较大的情况下，良性客户端的浅层特征仍然保持较高的相似性，因为浅层捕获的是更通用、与任务无关的特征。相比之下，整个模型的相似度受数据异质性影响更大，波动更明显。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1REvb6hR9AhdGiaOicHMY87fJ39K06MgJux1o0zsqcCAc60LWaIXvJCY7OuLth3OHqibqqPSrxTUEDDV1mgmPiaBMnibXHHlwsaP28/640?wx_fmt=png&from=appmsg)

图2 不同非独立同分布数据水平贝叶斯网络模型的平均相似度及整体模型相似度

具体而言，FLgym使用余弦相似度来度量BN相似度，因为它具有尺度不变性、有界性且计算成本低。对于客户端C1和C2，其BN相似度计算公式为：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp1ViaKt2XYAht4psFNxicOjgvlkTGy7IpUcIJbSXvPaGNTWW7y1Q720s0FKAkFiablSgnONKQhWhVW3EvtkRkjQJXzrhiaMQMdvK4Q/640?wx_fmt=png&from=appmsg)

服务器为每个客户端计算两个指标：与Top-K个最相似客户端的平均相似度（S\_i^top）和与所有客户端的平均相似度（S\_i^all）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp113pV3BL47ibV8RQtzY0OvmIS1l4uhhdC3OIJtM2orYGNIgiaruGNVNicCnCycIMradZxFFSfl12ibWU1sRZRwnC1QXXjsxZQ9viag/640?wx_fmt=png&from=appmsg)

基于这两个指标，服务器设置阈值，将客户端分为三类：明确的拜占庭客户端、可疑客户端和良性客户端。阈值会根据检测到的可疑和拜占庭客户端比例进行自适应调整，以保持合理的过滤强度。

**2. 第二阶段：可信客户端验证**

仅依靠模型参数分析的检测方法存在根本局限，尤其在非独立同分布场景下难以区分恶意更新和因数据异质性导致的良性更新。为此，FLgym引入了第二阶段——基于可信客户端的验证机制。

核心思想是：利用客户端之间的数据分布相似度，选择数据分布最接近的客户端作为验证器。因为数据分布相似的客户端在使用相同模型结构、参数和学习率训练相同轮次后，会产生相似的本地模型。将可疑客户端的模型放在数据分布相似的验证器上评估，可以更可靠地判断该模型是否被恶意篡改。

数据分布相似度通过模型分类层（通常是全连接层）的梯度相似度来估计：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp3CRCUiaOySAcU8ibYbq58KSKBytP8SsJfOPLSibr9Frl44qFJzHaibWmicvqEWgiaTcN0Ccz2HgtR86T4c3QNic5VM4qlSDpcVsf2MwE/640?wx_fmt=png&from=appmsg)

对于每个可疑客户端，服务器选择Top-K个数据分布最相似的客户端作为验证器，将可疑客户端的模型发送给它们进行验证。验证器在本地数据上评估该模型，返回准确率和损失值。服务器综合所有验证器的反馈（按相似度加权），计算损失变化分数S\_l和准确率变化分数S\_a，最终判断可疑客户端是否为拜占庭客户端。图3展示的是可疑客户端推理过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2TzsSa1vQibEHhZlNicicQ0yy0nibvFIDAGGS6uIVWtLUs73zrbGM8aD8wArmgfX3Hoy0J7Yl6kpVYqbqiacbqcd9Ushajg4jEavko/640?wx_fmt=png&from=appmsg)

 图3 可疑客户端推理

**（3）权重恢复机制**

为了减轻假阳性的影响，FLgym引入了基于窗口的权重恢复机制。当客户端被标记为拜占庭时，其权重恢复因子f\_t(c)被置为0，排除其更新参与聚合。随着训练进行，服务器逐步增加f\_t(c)，使客户端的权重逐渐恢复。参数λ设置为ln(100)/W，确保经过W轮后f\_t(c)趋近于1。

为了防止真实的拜占庭客户端利用恢复过程，FLgym实现了策略性复检机制：处于权重恢复过程中的客户端每轮以概率p\_t(c)被重新加入可疑集，接受第二阶段验证。复检概率随客户端的恢复因子f\_t(c)增加而增加，确保在客户端接近完全恢复时受到更严格的审查。如果在复检中检测到恶意更新，f\_t(c)将被重置。

这种设计使得攻击者想要获得足够的影响力来破坏全局模型，就必须在几乎整个窗口W内表现良好，而随着权重增加，被检测到的概率也随之增加，从而形成了有效的安全保障。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***04.***

**实验结果分析**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

**（1）实验设置**

实验环境包含1个服务器和128个客户端，每轮随机选择25%的客户端参与全局更新。默认设置25%的客户端为拜占庭客户端。采用FedAvg作为默认聚合方法。

数据集与模型

Fashion-MNIST：60,000张训练图像，10个类别，使用ResNet10模型

CIFAR-10：50,000张训练图像，10个类别，使用AlexNet模型

CIFAR-100：60,000张32×32彩色图像，100个类别，使用ResNet-18模型

HARBox：32,935条人类活动记录，5个类别，使用三层全连接DNN

使用Dirichlet采样器在客户端之间划分数据，浓度参数α控制数据异质性程度，默认α=0.5。

攻击方法与基线

评估的投毒攻击包括：Fang、LIE、Min-Max和MPHM，均为无目标攻击。对比的基线防御方法包括：FEDROLA、PCS、cosDefense、FLTrust、Multi-krum，以及防御聚合算法Trimmed-mean、GeoMed和krum。

**（2）实验分析**

如表1所示，FLgym在真阳性率和假阳性率方面表现出色。这种改进源于FLgym的两阶段框架：第一阶段通过BN相似度准确过滤掉大部分攻击者，第二阶段帮助验证部分可疑客户端，在检测能力和精确性之间取得了良好平衡。

表1 不同攻击下防御机制的FPR/TPR值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3Gg7dnoxDGWfFkPTRgg7ia2b0WZzWLm977X7Av8RFiapuaBuPkgc6lV0lTCPvYassnnK6Nwh2BibfYLUtozlEwdokkJux3xMWwQk/640?wx_fmt=png&from=appmsg)

通过调整Dirichlet分布的参数α，评估了不同数据异质性程度下各防御方法的性能。如图4结果显示，随着数据分布趋于均匀（α增大），所有方法的准确率都有所提升，但FLgym在整个α取值范围内始终保持最优性能。当客户端数据分布高度倾斜（α=0.1）时，传统的Trimmed-mean方法表现尤其差，因为它难以区分真正的恶意更新和因极端数据异质性而表现为统计异常的良性更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp1ObrRwGE2r3TEic5FRUS4h2oAUr7McvCTPQXV154T5IrIn5SiaDS26Siau5cszRtJOWGIIdgaxfK281yNh1AJ8icjLLKKuJgJibNWM/640?wx_fmt=png&from=appmsg...