---
title: G.O.S.S.I.P 阅读推荐 2022-11-22 Private, Efficient, and Accurate
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493343&idx=1&sn=4dab4d7840a2726256a41ffd74a2072e&chksm=c063c806f7144110ff721205e04a22bd7e6bf017f5e0696ce2a6ae4d9fecd7520713397f0aaf&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-11-23
fetch_date: 2025-10-03T23:30:15.423425
---

# G.O.S.S.I.P 阅读推荐 2022-11-22 Private, Efficient, and Accurate

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21ELDYNQXDicagGcgGKk05C9GGng6jysBUTYriabxRBiaZZChAjnqLxQd8FKyxZDTNDBPnicX1awXu10ow/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-11-22 Private, Efficient, and Accurate

Wenqiang@FDU

安全研究GoSSIP

今天为大家推荐的论文是来自复旦大学数据安全与治理研究组关于安全多方计算的最新研究工作Private, Efficient, and Accurate: Protecting Models Trained by Multi-party Learning with Differential Privacy，目前该工作已被IEEE S&P 2023收录。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21ELDYNQXDicagGcgGKk05C9GbzIaCEvK0BThY0TueTVTGxf5usjqCTf7xljnIng1zoLxWbs0Cvz8dA/640?wx_fmt=png)

**前言**

**安全多方学习（基于安全多方计算的机器学习）**是实现隐私计算的主流技术路径之一，旨在为数据要素流通提供一种**可证明安全的技术解决方案**。鉴于当前数据安全的相关法律法规对政府和企业的数据安全机制提出了更为严格的要求，安全多方学习将会有越来越广泛的应用场景和越来越高的实践价值。

尽管安全多方学习机制底层的安全多方计算协议为计算过程提供了严格的安全性保障，经由安全多方学习训练得到的模型依然无法抵抗那些仅依赖模型访问的攻击手段，例如成员推理攻击。此时，利用差分隐私技术可以**为安全多方学习的训练结果提供可度量的安全保障**。然而，尽管差分隐私技术能够为训练得到的结果模型提供可度量的安全保障，其所要求的大量随机噪声会给模型带来较大的精度损失。同时，底层的安全多方计算协议会为安全多方学习过程带来大量的通信开销。因此，如何在安全多方学习过程中针对模型平衡其隐私保障、效率以及精度是一个亟待解决的难题。

**为了实现模型训练过程的可证明安全与训练结果的可度量安全，**并实现隐私保障、效率以及精度的平衡，本文提出了一套解决方案PEA （Private， Efficient， and Accurate）。如Figure 1所示，PEA由一个安全差分隐私随机梯度下降协议以及两项效率与精度优化方法组成。首先，本文提出一个安全差分隐私随机梯度下降协议以在基于秘密共享协议的安全多方学习框架中实现差分隐私随机梯度下降算法。随后，为了降低差分隐私带来的精度损失并提升安全多方学习的效率，本文从安全多方学习训练过程的角度提出了两项优化方法：

1. 用于简化模型结构的数据无关特征提取方法；
2. 基于本地数据的全局模型初始化方法。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21ELDYNQXDicagGcgGKk05C9GIicPbQbbKTTEGMVWpnmBqHXwicdF9cOGqU1Uh54bHG18NM2ObY0ia864g/640?wx_fmt=png)

图 1 PEA概览

**安全差分隐私随机梯度下降协议**

Abadi等人于CCS 2016提出的差分隐私随机梯度下降算法中两个关键操作为通过计算平方根倒数对梯度向量的L2范数进行裁剪、向裁剪后的梯度添加随机高斯噪声。直接基于现有的安全多方计算协议实现平方根倒数安全计算会为训练结果带来少量计算误差，这些计算误差可能会影响梯度的安全裁剪过程，从而破坏差分隐私梯度下降算法的理论保障。为了在多方场景下安全地实现差分隐私随机梯度下降算法，作者设计了一个基于秘密共享协议的平方根倒数计算协议，并通过分析该计算协议的误差上界实现梯度的安全裁剪。同时，利用Dwork等人于2006年提出的多方随机高斯噪声生成协议安全地生成高斯噪声。结合上述方法，设计了一个安全差分隐私随机梯度下降协议。

**效率及精度优化方法**

为了降低差分隐私带来的精度损失并提升安全多方学习的效率，作者从安全多方学习训练过程的角度提出了两项优化方法：

1. 用于简化模型结构的数据无关特征提取方法。
2. 基于本地数据的全局模型初始化方法，用于加速模型训练过程的收敛。

**数据无关的特征提取方法：**现有的安全多方学习框架试图通过训练一个复杂的端到端深度神经网络模型同时实现特征提取与数据分类。然而，直接将已有的安全多方计算协议用于实现多方协作的模型安全训练会带来大量的通信开销，从而极大地影响了安全多方学习的效率。例如，在一个中等规模的数据集（如CIFAR-10）上训练一个主流的神经网络模型（如VGG-16）时，当前效率最高的安全多方学习框架之一CryptGPU在局域网环境下需要花费超过1个月的时间完成一次训练，并且传输的数据量超过200TB。此外，由于深度神经网络模型中存在许多冗余参数，在训练过程中加入差分隐私需要向这些冗余参数添加许多额外的噪声，导致模型精度大幅下降。为了解决上述两个问题，作者通过使用在大规模公开数据集上训练得到的特征提取器提取隐私训练数据中的特征信息，并基于提取得到的特征信息训练一个结构相对简单的浅层模型。通过上述方法，能够简化使用安全多方学习训练的分类模型的结构，从而极大地减少模型训练过程所需的计算量。

**基于本地数据的全局模型初始化方法：**在机器学习模型训练过程中，当基于一个相对精确的初始模型开始训练时，模型收敛所需的迭代数目能够大大减少。因此，作者先令各个参与方使用其本地数据训练得到一个具有一定精度的本地模型，随后通过聚合参与方的本地模型初始化一个相对精确的全局模型。在得到相对精确的全局模型后，利用上述的安全差分隐私随机梯度下降协议基于各个参与方的数据集继续训练提升该全局模型的精度直至模型收敛。通过上述方法，能够大大加快全局模型安全训练过程的收敛速度，从而达到减少安全多方计算原语调用数量，优化模型训练效率的目的。

**实验评估**

作者在两个开源安全多方学习框架（TF-Encrypted和Queqiao）上实现了上述协议与优化方法。作者称两个优化后的安全多方学习框架为TF-Encryptedε和Queqiaoε。在多个数据集上的实验结果验证了PEA的效率与有效性。例如，在局域网环境下，当Epsilon=2时，TF-Encryptedε可以在7分钟内基于CIFAR-10数据集训练一个精度达到88%的分类模型。上述结果远远优于当前最新的安全多方学习框架CryptGPU（其需要花费超过16个小时基于CIFAR-10数据集训练一个精度达到88%的无差分隐私保护的神经网络模型）。具体的实验结果如下图所示。端到端实验以及消融实验的结果表明PEA能够在提供结果安全性保证的前提下高效地训练一个精确的分类模型。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21ELDYNQXDicagGcgGKk05C9G1P6yR6FytkAJpD7rPp1RhDl6uBibAh4sJUUHIea7WLApMz0icsOSOFkA/640?wx_fmt=png)

图 2 与中心化深度学习模型的端到端比较

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21ELDYNQXDicagGcgGKk05C9GhaJNPLT3fibDINYTwaicQnA3TQ5UNLRrswmNTFcZk09qc16rdXgc5Vqg/640?wx_fmt=png)

 图 3 消融实验-特征提取方法

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21ELDYNQXDicagGcgGKk05C9GicQu4Gmv56FcB85EaLxbwGc1RC8PJgVFzPdXfh8N9ian1ZIiaI6vLicZaQ/640?wx_fmt=png)

 图 4 消融实验-模型初始化方法

**结论**

本文提出了一个提供**模型训练过程可证明安全以及训练结果可度量安全**的高效安全多方学习方案PEA。PEA由一个安全差分隐私随机梯度下降协议以及两项对效率与精度的优化方法组成。基于两个开源安全多方学习框架的实验结果表明PEA能够在增强已有安全多方学习框架隐私保护能力的同时极大地提升模型训练的效率。

**论文下载：**https://arxiv.org/abs/2208.08662

**作者简介：**阮雯强，本科就读于复旦大学软件学院，于2020年直博至复旦大学数据分析与安全实验室，师从韩伟力教授。他的主要研究方向为安全多方学习、差分隐私，在系统安全旗舰会议期刊IEEE S&P、ACM CCS，ACSAC、IEEE S&P Magazine等录用发表多篇高质量学术论文。

**投稿团队简介：**复旦大学数据安全与治理研究组长期围绕数据安全与隐私计算开展前沿研究工作，在安全多方学习框架与平台、加密资产生态监管与创新技术、用户口令安全等方面发表了系列高质量论文，构建了相应的软件平台。研究组长期招募对数据安全与隐私计算有着浓厚兴趣、拥有良好软件研发能力和扎实信息安全知识的博士后、博士研究生和硕士研究生。

研究组主页：https://dsg.fudan.edu.cn/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过