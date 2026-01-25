---
title: 中国科学院智能信息处理重点实验室关于文生图扩散模型后门检测的工作被T-PAMI接收
url: https://mp.weixin.qq.com/s/sW3zemb5PFHJuw8xHJM0oA
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:53:28.334083
---

# 中国科学院智能信息处理重点实验室关于文生图扩散模型后门检测的工作被T-PAMI接收

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsNickAI6APc3lV2z7c1skjfUvBDdBlE12LSWWlb8jq075gKF65DFypQkQp95SVkCic6LW51vMWncn2jw/0?wx_fmt=jpeg)

# 中国科学院智能信息处理重点实验室关于文生图扩散模型后门检测的工作被T-PAMI接收

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

近日，中国科学院智能信息处理重点实验室关于文生图扩散模型后门检测的工作**“Dynamic Attention Analysis for BackdoorDetection in Text-to-Image Diffusion Models”（作者：王中琦，张杰，山世光，陈熙霖）**被T-PAMI接收。T-PAMI全称为IEEE Transactions on Pattern Analysis and Machine Intelligence, 是模式识别、计算机视觉及机器学习领域的主流国际期刊, 2025年公布的影响因子为18.6。

最近的研究表明，文生图扩散模型易受到后门攻击，攻击者可以植入隐蔽的文本触发器来操控模型输出。以往的后门检测方法主要侧重于利用后门样本的静态特征，然而扩散模型启发于动力学模型，其动态性是其内在的关键属性。为此，本研究引入了一种全新的后门检测视角，称为**动态注意力分析（****Dynamic Attention Analysis, DAA****）**，并表明这种动态特征能更好的作为后门样本的指示特征。具体的，通过观察跨注意力图的动态演化过程，我们发现后门样本在<EOS> token（即句子结束符）展现出与良性样本显著不同的特征演化模式。为了量化这些动态异常，我们首先提出了DAA-I方法，该方法将各 token 的注意力图视为空间上独立的，并使用Frobenius范数衡量其动态特征。进一步，为了更好地捕捉注意力图之间的交互关系并优化提取的特征，我们提出了一种基于动力学系统（Dynamical System）的检测方法，称为DAA-S。该模型通过图结构的状态方程来刻画注意力图之间的空间相关性。我们从理论上证明了该模型的全局渐近稳定性，确保了特征建模的鲁棒性。在六种具有代表性的后门攻击场景中实验证明，我们的方法在检测性能上显著优于现有方法，平均F1值达到 79.27%，AUC达到86.27%。

![](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNickAI6APc3lV2z7c1skjfUvZnuepsORvL2mX4V1KepJwKnUbunibkNndTzzysAwjH6cZ85ogdTfnqw/640?wx_fmt=png&from=appmsg)

来源：中国科学院智能信息处理重点实验室

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=qnylxjok&tp=webp#imgIndex=2)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=fbknkhlb&tp=webp#imgIndex=3)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=23elspay&tp=webp#imgIndex=4)

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