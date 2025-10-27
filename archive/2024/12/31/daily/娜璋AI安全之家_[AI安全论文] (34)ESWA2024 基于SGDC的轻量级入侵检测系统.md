---
title: [AI安全论文] (34)ESWA2024 基于SGDC的轻量级入侵检测系统
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501100&idx=1&sn=ea3de2aef633874c0c37a4410c27cdef&chksm=cfcf75e1f8b8fcf768444a93225a781f241afa81c80b228382f038c8ad4b404a55f034243d3f&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2024-12-31
fetch_date: 2025-10-06T19:41:52.454132
---

# [AI安全论文] (34)ESWA2024 基于SGDC的轻量级入侵检测系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRPDZRQvQspscjATT1MZg8rc9X20eM7Balia6FxPiaicH2ezka7eUAoKr5cRofuhgs8bdeDPREazmfUqw/0?wx_fmt=jpeg)

# [AI安全论文] (34)ESWA2024 基于SGDC的轻量级入侵检测系统

原创

吴炫璋

娜璋AI安全之家

> 24年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNWoWUKxrkcddY3241SdjDVicP35eEUlLNaQ3EAgHjrQibqebibK7qYa58o1vCmC0maFa4wsTZplRLibw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

《娜璋带你读论文》系列主要是督促自己阅读优秀论文及听取学术讲座，并分享给大家，希望您喜欢。由于作者的英文水平和学术能力不高，需要不断提升，所以还请大家批评指正，非常欢迎大家给我留言评论，学术路上期待与您前行，加油。

该文是贵大0624团队论文学习笔记，分享者吴炫璋同学，未来我们每周至少分享一篇论文笔记。前一篇博客总结了NDSS 2024系统安全和恶意代码分析方向相关论文。这篇文章将带来ESWA’24韩国忠北大学的轻量级入侵检测论文，本文的主要贡献为结合特征工程开发轻量级、准确高效的IDS，并且能够检测广泛的网络流量攻击，适合在资源受限且少样本标注的IoT设备上运行。此外，由于我们还在不断成长和学习中，写得不好的地方还请海涵，希望这篇文章对您有所帮助，这些大佬真值得我们学习。fighting！

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcxuaialibicNEKVooSmdJEaV7uC8aibMhedNU63DZPB2WEA7UkseIlnL4sA/640?wx_fmt=png&from=appmsg)

```
原文作者：Jahongir Azimjonov, Taehong Kim 原文标题：Stochastic gradient descent classifier-based lightweight intrusion detection systems using the efficient feature subsets of datasets 原文链接：https://www.sciencedirect.com/science/article/abs/pii/S0957417423019954 发表会议：Expert Systems with Applications 2024笔记作者：贵大0624团队 吴炫璋开源代码：SGDC-basedLightweightIDShttps://github.com/JahongirAzimjonov/Lightweight-IDS-based-on-SGD-Classifier-and-Ridge-Regressor
```

**一.摘要**

物联网（IoT）已成为现代生活中不可或缺的一部分。然而，随着IoT设备的广泛应用，针对资源受限IoT设备的僵尸网络攻击数量也在不断增加。为应对这些威胁，研究人员开发了入侵检测系统（IDS）。然而，基于深度/机器学习、模糊逻辑、粗糙集理论或数据挖掘技术的传统IDS通常在检测准确性和能效方面存在不足。因此，亟需轻量化、高精度且能效优异的IDS，以有效检测多种网络攻击类型。

本文提出了一种解决方案，通过使用随机梯度下降分类器（SGDC）和基于岭回归的四种特征选择算法构建轻量化、高精度的IDS。为提升IDS的检测精度并降低计算复杂度，本文对SGDC算法和岭回归模型的超参数进行了优化。此外，优化后的特征选择算法用于降低数据集的维度，以提升IDS的检测精度。

为验证所提IDS的有效性，本文选取了三种网络流量数据集（KDD-CUP-1999、BotIoT-2018和N-BaIoT-2021）进行实验评估。结果表明，该系统平均检测准确率达92.69%，特征数量平均减少了79.93%。实验结果证明，所提出的系统可作为适用于资源受限IoT设备的轻量化IDS。总体而言，本文为IoT设备的IDS研究领域做出了重要贡献，提供了一种高效、准确的解决方案。所提出的轻量化IDS有望显著提升IoT的安全性和隐私保护能力，从而保障敏感IoT数据的安全。

**二.引言及相关工作**

随着物联网在日常生活中的广泛应用，其安全问题日益突出。特别是针对资源受限的IoT设备的僵尸网络攻击呈现上升趋势，DoS、DDoS、侦察和信息窃取等多种形式。IoT网络由于安全协议薄弱和设备保护不足，特别容易受到这些攻击的威胁。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rciae7aQdqZQNEGwxSKB99Du7BzB7Yar0wib8PlYoMbe2bib1eP2ickeMp3w/640?wx_fmt=png&from=appmsg)

本文将目前的入侵检测系统分为传统IDS和轻量级IDS：

* 传统IDS：资源消耗大，算法复杂，检测能力强，适用于大型网络
* 轻量级IDS：资源消耗小，算法简单，但检测复杂攻击的能力较弱，适用于物联网设备

现有的IDS存在的局限性又有以下两点

* 传统的基于机器学习的IDS 忽视了特征工程的作用，理论研究不足
* 现有轻量级IDS无法捕获真实网络的攻击行为，准确性和鲁棒性存在不足

因此，开发一个轻量级并且能准确识别真实网络攻击行为的IDS迫在眉睫。研究需求:

* 结合特征工程开发更轻量级、准确和高效的IDS；能够检测广泛的网络流量攻击
* 适合在资源受限且少样本标注的IoT设备上运行；需要提高检测准确率和能源效率

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rc8AsribHQ5p7PZQC1McvxWq2XjToABBPe2rZvKnn9OPY9YPrbxfbzohQ/640?wx_fmt=png&from=appmsg)

本文的研究目标及创新点为开发轻量级和准确性高的入侵检测系统(IDS)，使其能在资源受限的IoT设备上运行。具体通过以下方式实现:

* 构建随机梯度下降分类器(SGDC)和基于岭回归模型的四种特征选择算法
* 使用网格搜索方法优化SGDC算法和岭回归模型的超参数,以提高检测准确性并降低计算复杂度
* 利用模型微调的特征选择器来降低数据集的维度以实现轻量化的IDS

**三.系统整体框架**

本文设计的框架如下图所示，具体步骤为：

* 数据预处理
* 构建四种基于岭回归的特征选择方法，使用网格搜索方法优化岭回归模型的超参数，能有效抽取最相关且多维度的特征子集
* 构建基于SGDC的入侵检测模块，使用网格搜索方法优化SGDC模型的超参数，能有效优化损失函数
* 利用多种性能评估指标和对比分析方法来评估和选择性能最佳的模型

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rc55WX16mM7hibat6icRIru7nqaia1icm0LJ1WZvTgicAdN8qBurtvqRoLzlw/640?wx_fmt=png&from=appmsg)

总体算法如下：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcblApOiaiaLDHwFDhf2YHfEyIibibTzbXoibW8snHA9zJKhVYDiceIS4mCyEQ/640?wx_fmt=png&from=appmsg)

**四.算法及系统实现细节**

1.网格搜索方法

网格搜索（Grid Search）是一种超参数优化方法，本文用于岭回归模型和SGDC的超参数优化，网格搜索通过遍历所有可能的超参数组合,并使用交叉验证评估每组超参数的性能，最终选择最优的超参数配置。这种优化帮助基于岭回归模型的四种特征选择方法更好的提取高效特征子集，并帮助SGDC分类器在各个数据集上取得了良好的性能,同时保持了模型的轻量级特性。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcq0BXIROLLTjLiaibhTZsUkTxTZdHkCarSFSicDPDnX2eia5voMgVsLIIDw/640?wx_fmt=png&from=appmsg)

2.特征选择

文中提到了四种基于岭回归的特征选择方法，其作用是计算特征与目标之间的关系系数，从数据集中选取出最相关和最有效的特征子集。

* 基于重要性系数的特征选择算法 (Importance-coefficient-based feature selection)
* 前向序列特征选择算法 (Forward-sequential feature selection)
* 后向序列特征选择算法 (Backward-sequential feature selection)
* 基于相关系数的特征选择算法 (Correlation-coefficient-based feature selection)

这些方法通过分析输入特征(自变量)和输出标签(因变量)之间的关系来评估每个特征的影响，基于计算出的重要系数来确定最相关和最有效的特征，通过消除不相关和低效的特征来优化特征集。不同类型的方法可以从不同角度评估特征的重要性，这些算法平均减少了79.93%的特征维度，同时保持了较高的入侵检测准确率(平均92.69%)，特别是在处理时间和准确性方面都表现良好。

具体算法如下，算法输出是数据集中最相关和最高效特征的子集集合。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcP7v53ItlYQxYu4ricTz1S56Nnoyicd9ricLa45eThCUdL6rW8uyxhrdOg/640?wx_fmt=png&from=appmsg)

（1）基于重要性系数的特征选择如下，通过计算特征重要性系数ci和排序，从数据集中选择最相关且高效的特征子集。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcek6srbCPqkJMvia7TZEXk8icj1rlshKdpicyua0l0Vj4JtZiaVyCYibfdeg/640?wx_fmt=png&from=appmsg)

（2）前向和后向序列特征选择算法如下，分别选择相关性最高的特征添加到集合、将相关性最低的特征从集合中消除。例如，KDD-CUP-1999和N-BaIoT-2021数据集分别有40个和115个特征。其中一些特征对SGDC和岭回归器的准确性有正面影响，而另一些则有负面影响。对岭回归模型和SGDC准确性有正面影响的特征应保留为有效特征，而对准确性有负面影响的特征应从数据集的子集中移除。该算法有助于选择对准确性有正面影响的特征，并剔除无效特征。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcCq7icp3kY1T4LXVECfGWXpSV8QzibEBzyjNlTDkxWmmY5sU9RFLrTj6g/640?wx_fmt=png&from=appmsg)

（3）构建通过后向消元的相关系数特征选择算法，该方法首先定义所有特征的集合𝑋和目标变量𝑦，同时设定一个显著性水平（𝑝值），通常为0.05。初始特征集𝑋1最初被设置为完整的特征集合𝑋。该算法逐步消除特征，直到没有特征的相关系数的𝑝值大于设定的显著性水平0.05为止。最终，该算法返回基于与目标变量的相关性和显著性水平选择的最终特征集。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcu1U2ObghbfaWQVrFnyG4hIicm0J9LuzxHVWCVicG7JCm6Z5ld1zP7eVQ/640?wx_fmt=png&from=appmsg)

3.SGDC

SGDC（stochastic gradient descent classifier ）是一个线性分类模型，它使用随机梯度下降来优化损失函数。与传统SVM和SVC不同，SGDC只使用部分训练集来优化损失函数，其适用于大规模样本的场景，作为轻量级分类器，适合部署在资源受限的IoT设备上。

> 随机梯度下降法：随机梯度下降法是一种迭代优化方法，通过计算损失函数相对于模型参数的梯度，来寻找损失函数的最小值或最大值

基于SGDC的入侵检测模块算法如下：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rc9fSpGsoDmnkfomfyfmyOyARHqdibciciap2932epibycu3xehbxTiaQkLaw/640?wx_fmt=png&from=appmsg)

**五.实验评估**

1.数据集及预处理

该论文的数据集为3个IOT入侵检测数据集。

* KDD-CUP-1999

  http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
* BotIoT-2018

  https://research.unsw.edu.au/projects/bot-iot-dataset
* N-BaIoT-2021

  http://archive.ics.uci.edu/ml/datasets/detection\_of\_IoT\_botnet\_attacks\_N\_BaIoT

在基于SGDC的机器学习模型中，导致过拟合或欠拟合的主要问题之一是数据的类别不平衡。作者选取的三个数据集中都存在数据类别不平衡的问题，作者做了以下处理：

* KDD-1999：97,277个正常包 vs 396,743个攻击包，处理方法：通过删除重复记录来平衡数据集
* BoTIoT-2018：477正常包 vs 5000攻击包，处理方法：从恶意数据包中选择5000个样本,保留全部正常数据包
* N-BaIoT-2021：62,154个正常包 vs 766,106个攻击包，处理方法：使用下采样(down-sampling)技术

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcaJ5C5bkcRBppJn9UWCSwNU7ok9pZ30wgoibWU4W8aPQC5TJAawFoVnA/640?wx_fmt=png&from=appmsg)

2.评估结果

在不同数据集上不同算法运行时间对比：基于重要系数的特征选择方法在前两个数据集运行最快，基于后向序列的特征选择方法时间表现性能最差。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcDgicgdYqJa1akiaKKVqczE1xib5MSOz4ARDgV98ebXrtlc47KLu3S45Lg/640?wx_fmt=png&from=appmsg)

数据集原始特征集子集（a, b, c）特征重要性系数（IPs）的直方图如下，子集通过选择特征重要性系数（IPs）大于或等于所有特征平均IP的特征构建而成。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcRWKEibhBUlmhIKZfMKSfeAWgGSz9uO2fibjz4H0icLdia1xZdGpMEz4tgQ/640?wx_fmt=png&from=appmsg)

训练特征子集的预测结果如下，四种特征选择方法均优于所有特征。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcyNqsUjSZ4sTeh72yBuxXbrZ1ESd9UgQUfFsBzZY1CmZsK7LGFWm4bw/640?wx_fmt=png&from=appmsg)

最后给出性能评估比较图。实验结果表明，基于SGDC的IDS在高效特征子集对比完整特征集上的训练和测试速度分别提升了3-15倍和2-28倍，使用高效特征子集训练的模型预测准确率也明显高于使用完整特征集，平均准确率达到了92.69%，特别是特别是前向序列法在N-BaIoT-2021数据集上达到了98.42%的最高准确率。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcmaseCWFYIxso6o0YAPpF72DXqicQbQyS7AxoBszMic5kCNT4fQHjrqSg/640?wx_fmt=png&from=appmsg)

三种数据集全特征训练的准确率分别为30.65%、77.84%和68.90%，特征选择方法均有一定程度提升。在KDD-CUP-1999完整数据集上训练的模型表现最差，可能原因是数据集中存在低效和无关特征，在使用前向序列法在N-BaIoT-2021提取的特征子集进行训练后达到了98.42%的最高准确率。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPDZRQvQspscjATT1MZg8rcdxia1bQ6SUsX2yzyWATZAiaHmjpe63DbvBPUWDEd8ZAVLPia74c3EyGxA/640?wx_fmt=png&from=appmsg)

**六.总结及个人感受**

目前尚且有着几个因素会显著影响当前研究的结果，包括...