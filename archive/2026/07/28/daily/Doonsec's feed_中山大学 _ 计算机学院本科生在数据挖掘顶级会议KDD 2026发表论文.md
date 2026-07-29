---
title: 中山大学 | 计算机学院本科生在数据挖掘顶级会议KDD 2026发表论文
url: https://mp.weixin.qq.com/s/J3XL3vfAHYnPxqjI8CvHSw
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T05:01:08.187898
---

# 中山大学 | 计算机学院本科生在数据挖掘顶级会议KDD 2026发表论文

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTNQRcsibCMic28KicemGJGibicO5lfocAcpvLcKTXUb9ZY6AhzQj6uy8Ic0NNX06X3Af66Qf4DZWd5ngtSLwDibkAia2SGbueqPj9O4Fc/0?wx_fmt=jpeg)

# 中山大学 | 计算机学院本科生在数据挖掘顶级会议KDD 2026发表论文

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日，国际数据挖掘顶级会议KDD 2026（ACM SIGKDD Conference on Knowledge Discovery and Data Mining）公布论文录用结果，中山大学计算机学院2022级本科生黄玥文作为第一作者的论文"UniHam: A Large-Scale SOC-Complete Dataset and Benchmark for Hamiltonian Learning in Materials"被录用并受邀做口头报告，指导老师为卢宇彤教授、陈品老师。KDD是中国计算机学会（CCF）推荐的A类国际会议，与SIGMOD、VLDB并称数据挖掘领域三大旗舰会议。

**立足 AI for Science 破解材料领域数据瓶颈**

在"AI for Science"前沿领域，利用深度学习直接预测材料的电子结构（哈密顿量）是加速新材料发现的关键技术——一个准确的哈密顿量可同时推导出能带、态密度、带隙等数十种物理性质，从而绕过高成本的量子力学迭代计算。然而，该领域长期面临高质量公开数据的严重不足：现有数据集规模小、元素种类少，且普遍缺失描述重元素的关键物理效应（自旋轨道耦合，SOC），缺乏对模型的跨越广泛材料空间的可重复基准测试、扩展性分析和稳健的分布外评估的支持ra。

本次研究针对上述痛点，依托国家超算集群完成大规模运算（累计消耗约 300 万 CPU 核时），构建了目前规模最大、物理最完备的开放哈密顿量数据集与系统评测基准（超10万晶体结构，覆盖72种元素），系统揭示了现有AI模型在重元素/强相对论效应条件下的性能退化规律，并验证了基于该数据集训练的模型在跨数据集材料筛选中可达到92%的预测一致率，核心成果分为三方面。

![ab3acae5eece4a0fccba4bb00563c4f4.png](https://mmbiz.qpic.cn/sz_mmbiz_png/MMMialvZdKjgsCTNA9lx8IAyNPDAFJLtXFcGINiakpMweKdbThw18pe2VTeV9ia0vDWyvf3cLlFdjoqmXPibfRwFEghRHQPDjHsDibfwTX9wfSsA/640?wx_fmt=png&from=appmsg)

图1：UniHam基准框架整体示意

**构建了目前规模最大、物理最完备的开放哈密顿量数据集（UniHam）**

UniHam包含103,121个晶体结构，覆盖72种元素（包括此前所有公开数据集均未涉及的9种镧系稀土元素）和225个空间群（共230个），规模约为此前最大同类公开数据集的6倍。所有数据均在完整的相对论效应（全自旋轨道耦合，SOC）框架下完成高精度第一性原理计算，约三分之二的结构含重元素（Z≥37），填补了现有开源数据在规模、化学多样性和物理完备性上的空白，为该领域的模型研发提供了坚实的数据基础。

****建立了一套系统化的模型评测基准****

该基准从哈密顿量矩阵重建精度、系统尺寸外推、化学组成外推、下游物性预测四个维度，配合矩阵元素误差、能带能量误差、态密度误差和带隙误差四项互补指标，从算符级和可观测级两个层面评估模型能力。未来该领域的新模型可以直接在这一标准框架下进行训练和测试，实现公平、可复现的性能对比。

****揭示了当前技术的关键瓶颈与改进方向****

在两种代表性等变图神经网络模型（DeepH-pack和HamGNN）上的系统实验发现：(1) 现有模型在轻元素体系上表现良好，但在重元素与强SOC条件下出现一致且单调的性能退化，揭示了学习相对论自旋-轨道相互作用的固有困难；(2) 在化学组成外推场景中，不同模型的泛化鲁棒性差异明显，表明架构设计对零样本泛化能力具有决定性影响；(3) 更为关键的是，哈密顿量矩阵元素的逐点重构精度并不等价于下游物理性质的预测可靠性——在能谱层面引入监督信号可大幅提升模型对实际物性的预测能力（带隙误差降低约2.7倍），说明谱级评估对于判断模型真实效用不可或缺。

此外，论文还展示了端到端的应用潜力：将训练的模型零样本迁移至外源数据库中的3,000个晶体结构进行高通量筛选，模型预测其中720个为直接带隙半导体候选材料，与国际权威数据库Materials Project的独立验证结果一致率达92%，全程无需额外的第一性原理迭代计算，表明模型确实学到了可迁移的物理化学规律，有望直接服务于大规模材料发现。论文数据集与代码已在GitHub开源（https://github.com/WendyYW/UniHam），为该领域提供了一个可复现、物理完备的公共评测平台，对推动下一代材料基础模型的发展具有重要参考价值。

![](https://mmbiz.qpic.cn/mmbiz_gif/MMMialvZdKjjleQPVPaYnmaxiaqKbPBsiaRH4iat0yIvhehBnziahQWqd5WgSuBZccukGPDZiaV13gCR3TGlQNYGSFHfQAdaTqSWSyC9iahy84jYEY/640?wx_fmt=gif&from=appmsg)

计算机学院长期重视本科生科研能力培养，通过举办科技文化节、组织走进国家超算广州中心、班主任带队走访实验室、配备科研导师、引导学生参与前沿课题研究等多项举措，厚植学生科研素养与创新实践能力。学院将持续完善本科生科研培养体系，为计算机与交叉学科领域培养输送更多拔尖后备人才。

![](https://mmbiz.qpic.cn/mmbiz/DoiaG6QibmcNCVF2sdSEgAvEAYT226VEtHm3NsjJDmHBN1aGHXjsFjiawSVJVNVPdSicsd9TRC6TwibVFuQyH5l5zcQ/640?wx_fmt=png)

来源：中山大学计算机学院

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=png)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=jpeg)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=png)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

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