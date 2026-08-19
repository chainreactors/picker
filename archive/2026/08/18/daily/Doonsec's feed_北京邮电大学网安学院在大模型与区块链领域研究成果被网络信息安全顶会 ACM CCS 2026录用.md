---
title: 北京邮电大学网安学院在大模型与区块链领域研究成果被网络信息安全顶会 ACM CCS 2026录用
url: https://mp.weixin.qq.com/s/81MCF4E58UpnYqVdFAECVA
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:53:59.123922
---

# 北京邮电大学网安学院在大模型与区块链领域研究成果被网络信息安全顶会 ACM CCS 2026录用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTONLRfeyRwOQicHERojEHxHvb0MWnEaibViaarS56iadCLib5sg4MAyOgNWrRyic6fynfJguOgFWQkPbagSC4xXibJ3UiaTL5gxygSxllc/0?wx_fmt=jpeg)

# 北京邮电大学网安学院在大模型与区块链领域研究成果被网络信息安全顶会 ACM CCS 2026录用

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日，北京邮电大学网络空间安全学院张熙教授团队、石瑞生副教授团队各1项研究成果被第33届ACM计算机与通信安全会议（ACM Conference on Computer and Communications Security，ACM CCS 2026）录用。

ACM CCS为CCF A类会议，与IEEE S&P、USENIX Security、NDSS并称为网络与信息安全领域四大国际顶级学术会议，代表着网络与信息安全研究的最前沿水平。

**成果1**

张熙教授团队的研究成果，论文题目“Logit Laundering: Evading Data-Use Auditing in Large Language Models”。该研究工作由北京邮电大学网络空间安全学院2023级博士生胡睿涵、2024级硕士生罗伟在导师张熙教授、尚煜茗副教授联合指导下完成。北京邮电大学是该论文的第一作者和通信作者单位，合作单位包括中关村实验室和奥古斯塔大学。北京邮电大学网络空间安全学院2025级博士生李梅、2023级本科生张楚轩参与了该成果的研究工作。

论文简介：大语言模型的数据使用审计旨在判断特定数据是否被用于模型训练，是保护数据所有权、追踪未经授权使用的重要手段。当前主流方案通过在训练数据中嵌入可追踪的水印信号，并在模型输出中检测该信号来验证数据使用情况。然而，现有研究主要关注审计方法本身，对模型提供方可能主动规避审计的行为缺乏系统研究。论文从对抗视角出发，系统分析了大语言模型数据使用审计面临的规避风险，指出简单的数据层扰动不仅可能破坏训练语料质量，也难以彻底消除可检测信号。

论文提出了模型层审计规避框架Logit Laundering。该框架在推理阶段对模型输出词元概率进行重塑，通过轻量级统计偏差估计器识别并抑制水印引入的统计信号，无需修改模型参数，可作为即插即用组件部署。为兼顾审计规避效果与模型效用，论文进一步设计了置信度感知的缩放机制，根据模型对下一词预测的置信度自适应调整抑制强度，从而尽量保留模型学习到的知识和通用生成能力。论文在多个基础大语言模型和代表性数据使用审计方法上开展了广泛评估。实验结果表明，Logit Laundering能够有效削弱水印的可检测信号，同时较好保留模型从训练数据中学习的知识和通用任务性能。

研究意义：论文揭示了现有大语言模型数据使用审计在推理阶段输出操纵下的潜在脆弱性，为构建更稳健的数据水印、审计流程和知识产权保护机制提供了重要参考。

**成果2**

石瑞生副教授团队研究成果，论文题目“Are Unreachable Nodes Truly Safe? Fully Eclipsing Monero’s P2P Network!”。该研究工作是北京邮电大学网络空间安全学院2024级硕士生曾佳淇在导师石瑞生副教授、兰丽娜副教授等联合指导下完成的。北京邮电大学是该论文的第一作者和通信作者单位，合作单位有浙江大学、香港理工大学、CRISO。北京邮电大学网络空间安全学院2024级硕士生张诗含、2024级硕士生韩冰参与了该成果的研究工作。

论文简介：日蚀攻击通过垄断区块链节点的网络连接来使其孤立。针对门罗币（NDSS'25）、比特币（USENIX'15/21，S&P'20）和以太坊（WWW26）的现有攻击隐含地假设攻击者能够建立入站连接，从而排除了一类规模庞大且实际上占据主导地位的节点：即位于NAT后方、无法被访问的节点。人们普遍认为这类节点能够免受日蚀攻击的威胁。我们挑战这一假设：节点的“不可达性”并不意味着抗日蚀攻击能力。

论文提出了针对门罗币网络中不可达节点的首例日蚀攻击。我们的攻击无需对受害者进行入站访问，而是首先污染可达节点的对等节点列表，这些节点随后作为传播中继，进一步污染不可达节点的白名单。攻击者接着利用门罗币内置的出站连接刷新机制，驱逐良性邻居，最终垄断所有出站连接。我们将该策略具体化为两种攻击：Nyx攻击针对长期存在的不可达节点，通过全网范围的污染实现完全且持久的日蚀；而Moros则是一种更隐蔽的攻击，利用启动阶段快速对新加入的不可达节点实施日蚀。

研究意义：论文揭示了区块链网络潜在的重大安全威胁，对于区块链网络安全机制的设计与分析具有重要参考价值。

来源：北京邮电大学网络空间安全学院

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

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