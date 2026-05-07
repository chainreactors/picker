---
title: 优秀论文 | 南京理工大学逄淑超：面向无目标后门攻击的投毒样本检测方法
url: https://mp.weixin.qq.com/s/L2CDDSxjqusF3KTTrqL_Tw
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:26:00.484677
---

# 优秀论文 | 南京理工大学逄淑超：面向无目标后门攻击的投毒样本检测方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FNlvhjUaDTNOviaMFLznb5c6xpuNsJAGA6MMxOTtibZe9DmAckiaTBwsrzCEsg6KTopmh9h5BupskzQTWiasNwKOy56fakZHjh8uou0zpn51CI0/0?wx_fmt=jpeg)

# 优秀论文 | 南京理工大学逄淑超：面向无目标后门攻击的投毒样本检测方法

原创

信息网络安全杂志
信息网络安全杂志

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTPr3Mhy8UEialj68GtFjfLZdJGakMzoB6GN8aqbf2rLd3XjkNpFew741ZX1BiaFoWwibibBl5NxyCrQjPTl5R4h6jSZjeTERTvomCQ/640?wx_fmt=jpeg&from=appmsg)

**引用本文**

逄淑超, 李政骁, 曲俊怡, 马儒昊, 陈贺昌, 杜安安. 面向无目标后门攻击的投毒样本检测方法[J]. 信息网络安全, 2025, 25(12): 1878-1888.

PANG Shuchao, LI Zhengxiao, QU Junyi, MA Ruhao, CHEN Hechang, DU Anan. Detecting Poisoned Samples for Untargeted Backdoor Attacks[J]. Netinfo Security, 2025, 25(12): 1878-1888.

**研究背景**

随着深度神经网络在各领域的广泛应用，数据集的安全性与可靠性问题日益严峻，尤其是后门攻击作为数据投毒的一种主要方式，严重威胁模型的训练安全。现有的主流防御方法大多是针对“特定目标后门攻击”设计的，其防御机制依赖于攻击样本在特征空间中形成的集中统计异常。然而，在“无目标后门攻击”场景下，中毒样本的预测结果被分散至多个不同的错误类别，这种分散性导致传统的集中式统计信号消失，使得依赖该假设的检测方法难以发挥作用。此外，在黑盒设置下，用户往往缺乏对训练过程的控制权，进一步增加了利用第三方数据集进行训练的安全风险。因此，开展黑盒设置下特别是面向无目标后门攻击的防御研究，对于完善数据集版权保护技术具有重要的现实意义。

**研究方法**

本文提出了一种面向无目标后门攻击的投毒样本检测方法，该方法在黑盒设置下通过比较预测行为的异常差异来识别潜在的后门样本。整体框架由基于预测行为异常的投毒样本检测模块和面向投毒样本攻击的扩散模型数据生成模块组成。

其核心逻辑是利用生成模型对训练集数据进行重构：首先利用原始可能含毒的数据集训练分类器，模型会学习到后门特征；随后利用潜在扩散模型对数据进行重构，鉴于扩散模型在正向加噪和反向去噪过程中倾向于保留图像主体语义特征而破坏隐蔽的触发器模式，重构后的数据可视作不含触发器的“干净”样本。最后，将新生成的训练集输入已完成训练的分类器进行预测，通过对比前后两次预测行为的不一致性（即原始样本被误分而重构样本被正确分类）来精准锁定可疑的投毒样本。

**实验设计与结果**

为了验证方法的有效性，实验在ImageNet数据集的子集上进行，设置了10%的投毒比例，并涵盖了BadNets、高斯噪声、Sig变换和图像融合四种不同类型的无目标后门攻击。

实验首先对比了DCGAN、VAEs和Stable Diffusion（SD）三种生成模型，结果显示SD模型在生成图像质量和破坏触发器效果上均表现最优，有效降低了误报率。在攻击检测方面，本文方法在面对BadNets和Sig变换攻击时表现出色，检测成功率分别达到100%和95.16%，攻击成功率显著降低。与Neural Cleanse和Activation Clustering等主流防御方法的对比实验也表明，传统方法在应对无目标攻击时因无法识别分散的异常而失效，而本文方法在准确率、误报率及检测成功率等各项指标上均具有显著优势。

**研究结论**

本文提出的基于扩散模型重构的投毒样本检测方法，成功解决了黑盒场景下无目标后门攻击检测难的问题。研究证明，利用扩散模型强大的特征重构能力，可以在保留图像语义的同时有效破坏潜在的后门触发器，从而通过预测差异分析实现对投毒样本的精准检测。未来的研究可以通过探索非高斯噪声驱动的扩散模型以及引入更客观的图像质量评估指标来进一步优化方法的泛化能力和鲁棒性。

**通信作者:**

杜安安anan.du@niit.edu.cn

**作者简介:**

逄淑超（1988—），男，山东，教授，博士，CCF会员，主要研究方向为人工智能应用安全、数据安全与隐私保护 。

李政骁（2002—），男，江苏，硕士研究生，主要研究方向为网络空间安全、无数据蒸馏、模型鲁棒性 。

曲俊怡（2002—），男，山东，本科，主要研究方向为人工智能应用及其安全 。

马儒昊（2000—），男，山东，硕士研究生，主要研究方向为数据安全与隐私保护、人工智能应用 。

陈贺昌（1988—），男，吉林，研究员，博士，主要研究方向为机器学习、数据挖掘、智能博弈、知识工程、复杂系统 。

杜安安（1989—），女，山东，副教授，博士，主要研究方向为弱监督学习、智能感知、人工智能模型安全。

![](https://mmbiz.qpic.cn/mmbiz_png/FNlvhjUaDTNHgWwXNU6WjtxNaHNnmkYYg50l85NZyULSriaO2GXfr8LmI38POBzaxbBIwRly9Ykr4DXGFfpHBp0QZ88ibZ1icZZ6IJ2iaEPBX7s/640?wx_fmt=png&from=appmsg)

**阅读原文**

长按识别二维码

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

信息网络安全杂志

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