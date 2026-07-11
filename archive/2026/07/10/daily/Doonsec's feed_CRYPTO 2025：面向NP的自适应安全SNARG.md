---
title: CRYPTO 2025：面向NP的自适应安全SNARG
url: https://mp.weixin.qq.com/s/4v1_u36s2ZrT-mnu6S48GA
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:03:00.355313
---

# CRYPTO 2025：面向NP的自适应安全SNARG

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FNlvhjUaDTNwqcUnpNc9VJ2MibQlPHqPaBibdTnFzhLHia2hxY6XMIFMvexumX5TeZRSDbAjppvbTnRYthrS5cNBRY9micyAnHpvicJt0CdfibPaE/0?wx_fmt=jpeg)

# CRYPTO 2025：面向NP的自适应安全SNARG

原创

潘理文；王煜宇
潘理文；王煜宇

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、引子

SNARG，即简洁非交互论证，是现代密码学中的核心工具之一，它允许证明者用很短的证明，说服验证者某个NP语句为真。SNARG在可验证计算、零知识证明和区块链等方向都是一种基础工具。

所谓自适应安全SNARG，在公共参考串（CRS）模型下，是指攻击者可以在看到CRS后，再选择要伪造证明的假语句。它是多数密码学原语的基本安全性要求，相比非自适应安全更难实现。

iO即不可区分混淆，它可以使原电路对应的混淆电路的原功能被完全保留，并且两个功能相同的电路被混淆后不可以显著优势区分。

文章“A Pure Indistinguishability Obfuscation Approach to Adaptively-Sound SNARGs for NP”关注的问题是：能否在CRS模型下，仅基于不可区分混淆（iO）和普通单向函数，构造对NP适用的自适应安全SNARG？

二、论文速览

构造自适应安全的SNARG并非易事，2011年，Gentry和Wichs证明了自适应安全的SNARG与可证伪假设的黑盒分离，即二者无法通过多项式规约。此前，Waters和Wu以及Waters和Zhandry已经基于iO“两挑战”范式给出了自适应安全SNARG构造，但这些方案还需要额外的代数结构，例如离散对数、分解假设，或LWE所支持的损失函数。本文的主要进展在于：作者证明，在亚指数安全的iO和亚指数安全的普通单向函数存在的前提下，就可以构造NP的自适应安全SNARG，而不再额外依赖这些代数假设。

文章的核心技术，是对已有“两挑战”范式进行重新实现，使单向函数不再必须出现在真实协议的挑战生成过程中，而主要出现在安全性证明中。

该构造的特点为：CRS大小为关系电路规模和安全参数的多项式，证明大小仅为安全参数的多项式，并且满足完美零知识，是一个具有实际意义的SNARG。

三、深度解剖

原有方案采用“两挑战”范式：每个语句对应两个伪随机挑战，诚实证明者只会给出其中一个挑战的原像；若攻击者为假语句给出另一侧挑战的原像，就可以被归约为打破单向性。问题在于，过去为了让这一归约成立，需要可重随机化单向函数或损失函数，而这些对象通常依赖额外代数结构。

文章将挑战生成和证明验证合并到同一个混淆程序中。也就是说，CRS中不再发布一个单独生成单向函数挑战的程序，而是发布一个直接执行验证逻辑的混淆程序。这样一来，真实方案本身并不需要计算单向函数；单向函数只在安全性证明的混合实验中被引入。这个看似偏“语法”的改变，实际上打开了摆脱额外代数假设的空间。

为了完成归约，作者进一步引入“带低效采样器的单射单向函数”这一中间对象。通常，从普通单向函数直接得到单射单向函数并不容易；但本文只要求采样算法可以是低效的，因为该对象不需要在真实协议中执行，只服务于安全性证明。作者利用通用哈希来减少原像数量，从普通单向函数构造出所需对象。由此，方案避免了对可重随机化结构、损失结构等额外代数工具的依赖。

四、局限与展望

文章“A Pure Indistinguishability Obfuscation Approach to Adaptively-Sound SNARGs for NP”是一项偏理论的构造，不能被理解为面向直接部署的高效SNARG。其假设仍然较强：需要亚指数安全的iO和亚指数安全的单向函数；安全性分析的规约并不“紧”，规约损耗较高。

不过，这些局限并不削弱论文的理论意义。文章真正推进的是假设结构的简化：在已有iO的前提下，不再额外要求离散对数、分解或LWE等代数假设。未来值得继续研究的问题包括：能否进一步降低iO相关假设的强度，能否减少CRS开销，能否继续降低证明长度。

五、启示

总体来看，这篇论文的贡献不在于提出一个立即实用的证明系统，而在于给出了一个更干净的理论路径。它表明，自适应安全SNARG并不必然依赖额外代数结构；在iO与普通单向函数的组合下，通过重新组织验证逻辑和安全性证明，也可以达到目标。

对于关注适应性SNARG、iO的研究者而言，这篇文章值得阅读。它不仅提出了一个新的密码学构造，同时也展示了一个重要经验：密码学研究的关键突破，不仅仅在于增加新的工具，它也可以通过重新安排已有工具的位置实现。

点评人：潘理文（电子科技大学硕士研究生）、王煜宇（电子科技大学 教授）

主要研究方向：可证明安全密码学

原文标题：

A Pure Indistinguishability Obfuscation Approach to Adaptively-Sound SNARGs for NP

原文作者：

Brent Waters, The University of Texas at Austin, NTT Research

David J. Wu, The University of Texas at Austin

期刊/会议：CRYPTO 2025

DOI: 10.1007/978-3-032-01907-3\_10

版权与来源声明：本文依据《中华人民共和国著作权法》第二十四条之规定，为介绍、评选之目的，在此适当引用。原文版权归原作者所有。

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