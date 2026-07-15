---
title: 箭影博弈：端侧TEE保护LLM分区推理中的权重混淆安全性研究
url: https://mp.weixin.qq.com/s/7DMTNozcE5TJIVsctna9WQ
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:46:34.534709
---

# 箭影博弈：端侧TEE保护LLM分区推理中的权重混淆安全性研究

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTN8IdkX1kNmUibNG0fXT8gOf2HDSvMtuAxE7gCwYicd3ABYdVLFDMdE8sx0w27pldoskhxoJB01muqOk7qUUKdOXUbp0xWmtrqdM/0?wx_fmt=jpeg)

# 箭影博弈：端侧TEE保护LLM分区推理中的权重混淆安全性研究

原创

李萌
李萌

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

引子：随着大语言模型（LLM）向端侧设备迁移，如何在用户控制的端侧设备及其不可信宿主环境中保护高价值模型权重，成为了学术界和工业界共同的痛点。一种具有代表性的研究路线是TEE-Shielded LLM Partition（TSLP）：将重负载的矩阵运算卸载到GPU，并将权重进行轻量级混淆。然而，该研究指出了这一防御体系中的关键薄弱环节。作者发现，现有轻量级混淆算法存在一个被低估的几何缺陷，即难以有效破坏权重向量的方向相似性。这一看似微小的几何特征，使端侧AI权重保护在特定攻击前提下面临明显风险。

速览：现有的商业TEE（如Intel SGX）计算能力和可信内存受限，TSLP方案为了效率，在TEE内仅使用复杂度为O(n·l)的逐向量操作（如按向量缩放、排列）来混淆权重。但这种妥协带来了一个核心缺陷，即微调后的私有模型与公开的预训练模型在向量方向上高度一致，且逐向量混淆很大程度上保留了这一方向特征。作者提出利用余弦距离比对混淆权重和公开权重的方向，能够高精度恢复出排列和缩放逻辑，从而重构私有模型权重。为缓解这一问题，作者引入了矩阵-向量乘法作为新的混淆操作。该方法在不增加渐进复杂度的情况下，通过引入由私有权重线性组合得到的混淆向量，显著扰乱外发权重的方向信息。在论文实验覆盖的代表性轻量级混淆方案中，ARROWMATCH能以超过98%的精度恢复私有权重。而ARROWCLOAK在论文实验设置下可将泄漏风险降至原来的约1/6.5，并使总体开销降至全TEE屏蔽方案的约35.3%。

深度解剖：这项研究的价值在于，它重新审视了端侧模型保护中轻量级混淆的安全边界，揭示了仅依赖排列和缩放的轻量级混淆在方向特征保护上的系统性不足。既有方案虽然能够改变权重的显式位置或数值尺度，却难以充分破坏权重列向量的方向结构。由于私有模型通常由公开预训练模型微调而来，其权重方向与基座模型仍保持较强相似性，攻击者便可以利用这一几何锚点恢复混淆关系。ARROWCLOAK的关键改进，是在不显著增加渐进复杂度的前提下，引入轻量级矩阵-向量乘法来保护方向信息。作者进一步借助带误差学习问题（LWE）的形式，对该混淆结构进行安全性分析，使方案不再只是经验性的工程混淆，而具有更清晰的理论解释和安全性分析依据。

局限：尽管攻防逻辑较为清晰，但该研究中 ARROWMATCH 攻击成功的重要前提，是攻击者能够获取与受害者模型同源的公开预训练基座权重。一旦企业采用完全从头训练（Train-from-scratch）策略，方向相似性的锚点便会明显削弱。下一步研究可以进一步探讨在弱先验或无公开基座模型场景下，如何评估端侧模型分区推理中的权重泄漏风险；同时也可以考察这类方向性保护机制能否扩展至模型运行时的中间激活值、LoRA模块或KV-Cache等状态，并进一步分析其与侧信道缓解机制协同的可能性。

启示：对工业界而言，本文敲响了警钟，真正的安全机制不能建立在“攻击者看不到细节”的侥幸假设之上，未来的端侧安全防御必须走向拥有理论托底的路线。本文展示了如何将密码学中的LWE思想与系统架构优化结合起来，由此突破现有启发式防御主要依赖经验混淆的局限。对于学界而言，它打破了系统安全工程与基础密码学之间的壁垒，在异构计算普及的时代，探索介于纯TEE隔离与重型密码计算之间、兼顾工程效率与安全论证的中间路线，依然是未来大模型安全研究的重要方向。

本人仅代表作者个人观点

本期点评论文

作者：陈毅飞、胡耀、吴梦、乔焰 副教授、童秋云 讲师、李萌（合肥工业大学计算机与信息学院 教授 数据安全与隐私保护领域）

原文标题：

Game of Arrows: On the (In-)Security of Weight Obfuscation for On-Device TEE-Shielded LLM Partition Algorithms

原文作者：

Pengli Wang，Bingyou Dong，Yifeng Cai，Zheng Zhang，Junlin Liu，Huanran Xue，Ye Wu，Yao Zhang，Ziqi Zhang

期刊/会议：

34th USENIX Security Symposium

版权与来源声明：本文依据《中华人民共和国著作权法》第二十四条之规定，为介绍、评选之目的，在此适当引用。原文版权归原作者所有。

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=other)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=other)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=other)

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