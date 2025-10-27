---
title: 美国海军学院 | 使用FEP(完全加密协议)隐藏协议元数据
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491632&idx=1&sn=7c316f672f7ccc9f615c337740a94a9a&chksm=fe2d1fbbc95a96ad7d8e3f625e6b6b7ae923ce9136b0addef351a29df91e5a4bc88180bd0565&scene=58&subscene=0#rd
source: 安全学术圈
date: 2025-02-06
fetch_date: 2025-10-06T20:36:11.786407
---

# 美国海军学院 | 使用FEP(完全加密协议)隐藏协议元数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WFyAnWzm1OIkoib0JhdSqJQ19Z33HDXIFUS7zwErhBYvNibPtoYWNlKr1T6iakptLMgxoFLkPWp7g00Q/0?wx_fmt=jpeg)

# 美国海军学院 | 使用FEP(完全加密协议)隐藏协议元数据

原创

孙汉林@安全学术

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFyAnWzm1OIkoib0JhdSqJQ1JiaibewYrLOjSAibfj3RFEAa0giaB8L3Ms9NP4PELicsCEibibmG6TWT6KfEw/640?wx_fmt=png&from=appmsg)
> *原文标题：Bytes to Schlep? Use a FEP: Hiding Protocol Metadata with Fully Encrypted Protocols*
> *原文作者：Ellis Fenske and Aaron Johnson*
> *发表会议：ACM CCS '24*
> *原文链接：https://dl.acm.org/doi/10.1145/3658644.3690198*
> *笔记作者：孙汉林@安全学术圈*
> *主编：黄诚@安全学术圈*

### 1、引言

完全加密协议（FEP）通过隐藏通信元数据（如版本号和长度字段）使数据呈现为随机字节，从而规避网络审查。尽管存在检测和阻断方法，但其仍具有很高的实用性。完全加密趋势也反映在 TLS 和 QUIC 等协议中。此外，FEP还通过填充技术隐藏协议字段和消息的长度，进一步增强了规避审查的能力。常见的FEP有Tor中的obfs4、V2ray中的Vmess、Shadowsocks等等。

这篇论文的主要贡献如下：

* 提出了针对数据流类型（TCP）的完全加密协议（FEP）的安全性定义，与现有的安全性定义[1]进行了比较，并构建了一个可证明安全的数据流FEP。
* 同样提出并分析了数据报类型（UDP）FEP的安全性定义，并构建了一个可证明安全的数据报FEP。
* 对现有的多种FEP进行了评估，发现了新的识别特征，包括由错误引发的通道关闭行为和最小消息长度。这些发现为现有协议的改进和未来设计提供了参考。

作者为FEP的安全性提供了理论基础，提出了具体的安全目标，并分析了现有协议的优缺点，揭示了它们可能被识别的方式。

### 2、数据流安全概念

本节将作者提出的新的数据流安全概念与Fischlin等人提出的数据流安全概念[1]进行了对比。因前者是后者的基础，所以介绍前者所用篇幅较大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFyAnWzm1OIkoib0JhdSqJQ1CulcdIZm4gtibWoE2TTJ2EfBhoqPbwpTUQGYeo6sJHPfg3mlh4LwvBQ/640?wx_fmt=png&from=appmsg)

图中方框与实线部分是Fischlin等人[1]提出的安全性概念：

* **IND-CPFA (Indistinguishability under Chosen Plaintext Fragment Attack)**: 在选择明文片段攻击下的不可区分性，攻击者可以选择一系列明文片段，并观察其对应的密文。确保加密方案对于任何选择的明文片段，攻击者无法通过观察密文来区分两组不同的明文片段。
* **IND-CCFA (Indistinguishability under Chosen Ciphertext Fragment Attack)**: 在选择密文片段攻击下的不可区分性，攻击者不仅可以选择明文片段并观察其对应的密文，还可以对已加密的密文片段进行修改，并观察报错协议信息。保障加密方案在面对主动攻击（包括密文的修改和插入）时，攻击者无法区分两组明文片段的加密结果。
* **INT-PST (Integrity of Plaintext)**: 明文的完整性，保证明文流的完整性，确保接收端输出的明文流与发送端输入的明文流一致。若攻击者修改了信道中的数据或插入了新数据，接收端应能检测到，并将其视为攻击。攻击者无法通过操控密文来实现明文的插入、修改或伪造。
* **INT-CST (Integrity of Ciphertext)**: 密文的完整性，只要密文片段经过篡改、伪造或以其他方式被攻击者操控，接收端必须能检测到这些问题，并拒绝篡改后的密文流，而不是尝试解密并输出潜在的明文内容。
* **ERR-PRED (Predictability of Error Symbols)**: 错误符号的可预测性，目标是限制攻击者通过发送恶意密文片段来“探测”协议的行为。它要求接收算法（Recv）在处理错误密文时，输出的错误符号必须是攻击者可以预测的，而不是暴露额外信息或让攻击者利用协议的错误处理机制进行推测。

其中，INT-CST能推出INT-PST，这显而易见（Trivial）。ERR-PRED、INT-CST和IND-CPFA能推出IND-CCFA。因为ERR-PRED（错误可预测性）确保接收端对异常密文的错误处理是可预测的。这防止攻击者利用错误消息行为获得密文或协议的元数据信息。INT-CST（密文流完整性）防止攻击者通过篡改或伪造密文片段来欺骗接收端输出伪造的明文。这确保接收端只会处理合法密文，防止攻击者对解密结果进行干扰。IND-CPFA（明文片段选择性攻击下的不可区分性）确保被动攻击者无法通过观察密文区分明文内容。这为 IND-CCFA 的被动部分提供了基础。

图中椭圆与虚线部分是本文提出的新的安全性概念：

* **FEP-CPFA (FEP security against a chosen plaintext fragment attack)**:确保在被动攻击下，完全加密协议的密文对明文片段不可区分，同时隐藏明文内容和元数据（如长度）。
* **FEP-CCFA (FEP security against a chosen ciphertext fragment attack)**:确保在主动攻击下，完全加密协议的密文对明文片段不可区分，并防止通过篡改密文获取任何信息。
* **IND-CPFA-CL**:确保带关闭操作的信道在明文片段选择性攻击下，密文对明文不可区分，即关闭行为不会泄露信息。
* **CH-REG (Datastream Channel Length Regularity)**:保证信道生成的密文长度与明文内容无关，以防止通过密文长度泄露明文信息。
* **ERR-FREE**:确保接收端在处理异常密文时不生成带内错误消息，避免通过错误行为泄露信息。

相应的推导关系已经在图中详细展示，所以不再赘述。`重要的是`，作者推出，FEP-CPFA 和传统机密性定义（ IND-CPFA 和 IND-CCFA）之间并非互相包含，特别是元数据泄露可能破坏 FEP-CPFA 的要求。Fischlin等人提出的AEAD (Authenticated Encryption with Associated Data)虽然满足标准机密性定义，但如果使用未加密的长度字段标记密文块边界，仍违反 FEP-CPFA 的要求（因为元数据泄露）。

### 3、数据流完全加密协议

作者在Shadowsocks的基础上，设计了一个满足所有安全性需求的完全加密协议。相较于Shadowsocks来说，具体改进点如下：

* **增强元数据保护**：引入固定长度的“长度块”和包含填充字段的“负载块”分块机制，支持流量整形（Traffic Shaping），消除明文长度泄露风险，有效防御流量分析攻击。
* **更严格的安全机制**：采用失败状态（Fail State）取代带内错误消息，发生错误时不再发送错误信息，防止错误反馈泄露信息。
* **通用性和灵活性提升**：设计通用的缓冲和填充机制，适配其他完全加密协议（如 obfs4 和 InterMAC），并支持基于超时的连接关闭策略，增强抗分析能力和协议适应性。

该协议满足正确性（Correctness）、流量整形（Traffic Shaping）、信道长度规则性（CH-REG）、被动和主动机密性（FEP-CPFA/FEP-CCFA）及密文流完整性（INT-CST）等所有安全要求。

### 4、数据报完全加密协议

数据报安全概念与数据流安全概念的证明类似，所以对于数据报，我们主要关注与数据流不同的地方。

数据流（Datastream）与数据报（Datagram）的主要区别在于传输方式和特性：数据流以连续的字节流传输，消息可能被分片或合并，接收端需解析边界，通常提供顺序性和可靠性保障（如 TCP）；数据报则以独立完整的消息原子传输，无需分片或合并，消息边界明确，但可能乱序或丢失，不保证可靠性（如 UDP）。

在 **Correctness** 中，**数据流**模型假设消息按顺序传输，关注确保顺序正确并恢复消息，而**数据报**模型要求每个消息在发送和接收后能够正确恢复，并处理可能的错误（如消息过大、输出长度不适等），而不依赖于消息顺序。

在 **Traffic Shaping** 中，**数据流**模型比较灵活，不强制要求每次输出的密文长度与请求的长度完全匹配，而**数据报**模型要求输出的密文长度严格与请求的长度一致，并允许通过设置参数关闭流量整形。

针对数据报，作者同样设计了一个满足所有安全性需求的完全加密协议，主要改进点如下：

* **增强随机性和安全性**：该构造基于 AEAD 加密方案，通过随机数（nonce）前缀和明确的消息编码方案，实现消息长度控制以支持流量整形（Traffic Shaping），避免泄露消息大小或协议元数据。
* **无状态设计**：协议设计为无状态，每次调用返回新的对称密钥，简化了状态管理并提升了适配性。

该协议同样满足正确性（Correctness）、流量整形（Traffic Shaping）、FEP-CCA、INT-CTXT和IND-CCA.等所有安全要求。

### 5、现有完全加密协议分析

作者分析了一些试图在传输层之上实现完全加密的开源协议，以评估其是否符合本文的安全定义，以及它们在多大程度上具有本文的安全定义所要解决的识别特性（即泄露的某些元数据）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFyAnWzm1OIkoib0JhdSqJQ1Bk0JNo10MfxppoHFNK8lxqiaQrIG3OUosEbBDSlsdSeGyTHMq6ibuXCg/640?wx_fmt=png&from=appmsg)

安全性分析结果如下：

* 几乎所有现有的FEP协议都满足被动FEP安全性，即确保协议在被动攻击下能够防止元数据通过密文泄露；但没有数据流协议完全满足主动FEP安全性，即确保协议在面对篡改或恶意插入等主动攻击时依然能够防止元数据通过密文泄露，通常涉及如何处理连接关闭和错误处理。
* 现有的协议，无论是数据流还是数据报，都不满足流量整形（Traffic Shaping），所有协议都可以通过其最小消息长度来识别。

### 6、总结

本文给出了FEP的安全定义和证明，提出了新的安全定义，涵盖了FEP的元数据保护目标，适用于数据流和数据报模型（TCP和UDP），并且证明了这些新概念与现有安全定义之间的关系，并展示了新的FEP构造及其安全性。此外，作者还调查了现有的FEP候选协议，分析了它们在满足FEP安全性方面的程度，并识别了这些协议在响应数据错误和最小消息大小方面的可识别性。

一个安全的FEP，要能够防止主动攻击下的元数据泄露。

### References

[1] Fischlin, Marc, et al. "Data is a stream: Security of stream-based channels." Advances in Cryptology--CRYPTO 2015: 35th Annual Cryptology Conference, Santa Barbara, CA, USA, August 16-20, 2015, Proceedings, Part II 35. Springer Berlin Heidelberg, 2015.

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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