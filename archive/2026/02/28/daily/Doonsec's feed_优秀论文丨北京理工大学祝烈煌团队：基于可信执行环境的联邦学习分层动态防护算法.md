---
title: 优秀论文丨北京理工大学祝烈煌团队：基于可信执行环境的联邦学习分层动态防护算法
url: https://mp.weixin.qq.com/s/vfTDBg2eLxUUrchnuW6FSA
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:19:03.530408
---

# 优秀论文丨北京理工大学祝烈煌团队：基于可信执行环境的联邦学习分层动态防护算法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsNibibpibXLhQK1DnfucDXRZNa7JFpjC6PebxsVyqZFDGY8SkIIILxSDNU6u46qicdSJuyFG9WlqlANC2A/0?wx_fmt=jpeg)

# 优秀论文丨北京理工大学祝烈煌团队：基于可信执行环境的联邦学习分层动态防护算法

原创

信息网络安全杂志
信息网络安全杂志

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibibpibXLhQK1DnfucDXRZNa7cwMkw9buWqPbArtl9hicwYJNPoNVN33oclGLibh70r542VMgQkibNO3NQ/640?wx_fmt=png&from=appmsg)

**引用本文**

王亚杰, 陆锦标, 李宇航, 等. 基于可信执行环境的联邦学习分层动态防护算法[J]. 信息网络安全, 2025, 25(11): 1762-1773.

WANG Yajie, LU Jinbiao, LI Yuhang,  et al. Hierarchical Dynamic Protection Algorithm for Federated Learning Based on Trusted Execution Environment[J]. Netinfo Security, 2025, 25(11): 1762-1773.

**研究背景**

联邦学习（Federated Learning，FL）通过“本地训练、参数共享”实现跨域协同建模，但参数更新仍可能泄露与训练数据相关的信息，并被用于对抗样本、梯度投毒、模型窃取等攻击。可信执行环境（Trusted Execution Environment，TEE）可在硬件隔离条件下保护关键计算过程，为提升联邦学习安全性提供了可行路径。然而，将更多训练环节纳入TEE往往会带来额外时延与资源开销；保护范围过小又难以有效抑制攻击。现有方法多采用固定的保护范围配置，难以随模型结构、攻击压力与资源条件变化而自适应调整，因而难以同时兼顾安全性与效率。围绕这一矛盾，本文提出一种面向资源约束的分层动态防护方法，在控制训练开销的同时提升对典型攻击的抵抗能力。

**研究方法**

本文将模型更新按敏感程度区分对待，并以可量化的安全收益与开销代价驱动保护范围的动态确定。训练过程中，服务端对不同的受保护层集合进行对比测量：一方面在多种攻击条件下观察安全性变化（如对抗样本成功率、投毒影响等），另一方面统计相应的训练与通信开销，并据此选取单位开销带来更高安全收益的保护范围。客户端训练阶段，对被选中的敏感部分在TEE内完成关键计算与上传前的加密封装，其余部分采用常规训练与聚合，以减少敏感信息暴露面。为适应TEE资源约束，训练过程采用分阶段的组织方式以降低单次训练的资源峰值，使多层保护能够在既定资源条件下稳定执行。通过这些机制，保护范围能够随训练状态与攻防压力变化而调整，从而获得更稳健的安全与效率权衡。

**实验设计与结果**

实验在图像分类任务上开展，选取 CIFAR-10 与 ImageNet 作为数据集，以 VGG16 为代表模型，在联邦训练设置下对比固定保护与动态选择策略在安全性、开销与主任务性能上的差异。结果表明，在主任务精度保持在可控波动范围内的前提下，动态分层防护相较于“对大多数客户端或层进行重保护”的基线，可将保护相关开销最高降低约 82%。在攻击评估中，该方法削弱了攻击者通过观测更新构造有效扰动与操纵训练过程的能力；在梯度投毒等场景下，攻击效果最高可被削弱约 35%。总体来看，动态选择相较固定配置更能实现以较小开销获取更高安全收益的权衡。

**研究结论**

本文提出的分层动态防护方法面向TEE资源受限条件，将保护范围从经验设定转化为基于安全收益与开销代价的自适应决策，并通过差异化训练与聚合路径降低敏感更新暴露，从而在可控性能影响下提升联邦学习对典型攻击的抵抗能力。实验结果验证了其在降低保护开销与抑制攻击效果方面的综合优势。后续可进一步研究与差分隐私（Differential Privacy，DP）等机制的互补协同，并在更强自适应攻击与更复杂联邦形态下开展系统化评估。

**通信作者:**

张子剑 wangyajie19@bit.edu.cn

**作者简介:**

**王亚杰（1993—），男，河北，助理研究员，博士，CCF会员，主要研究方向为人工智能安全、数据安全与隐私保护。**

**陆锦标（2002—），男，广东，硕士研究生，主要研究方向为人工智能安全、隐私保护。**

**李宇航（2002—），男，江苏，硕士研究生，主要研究方向为人工智能安全、隐私保护。**

**范青（1996—），女，山东，副教授，博士，CCF会员，主要研究方向为应用密码学、信息安全与安全协议设计。**

**张子剑（1984—），男，北京，教授，博士，CCF会员，主要研究方向为区块链安全、通信安全、数据隐私。**

**祝烈煌（1976—），男，浙江，教授，博士，CCF会员，主要研究方向为密码算法及安全协议、区块链技术、云计算安全、大数据隐私保护。**

![](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibibpibXLhQK1DnfucDXRZNa7pEP0RuNWujcp9fcIeia2icX3ExibawofgiacR0C3Dd8SkkwicDic3GBbLIQA/640?wx_fmt=png&from=appmsg)

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