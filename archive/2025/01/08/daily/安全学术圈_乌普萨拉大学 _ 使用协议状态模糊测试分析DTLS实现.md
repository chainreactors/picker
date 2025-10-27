---
title: 乌普萨拉大学 | 使用协议状态模糊测试分析DTLS实现
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491545&idx=1&sn=168ec87f8235a16dee4fb964a0d813ac&chksm=fe2ee052c95969447f320f7827e8496e3cb8fd4a0a845caa93a13f082197233e28e8ec60bb5f&scene=58&subscene=0#rd
source: 安全学术圈
date: 2025-01-08
fetch_date: 2025-10-06T20:10:49.378915
---

# 乌普萨拉大学 | 使用协议状态模糊测试分析DTLS实现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WE7QmrTEsehxOXAiaxkCDL90X1PZMEhEdF1648EDniajcnickKHKdaXuItWkaYNK0Lqs1WwbIlWNvfpw/0?wx_fmt=jpeg)

# 乌普萨拉大学 | 使用协议状态模糊测试分析DTLS实现

原创

宋坤书

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE7QmrTEsehxOXAiaxkCDL90Rmu16Uoy23NzVxmaLbed5bJV76oYz1dW5glrvITDrevoYcF8RiamFWw/640?wx_fmt=png&from=appmsg)
> *原文标题：Analysis of DTLS Implementations Using Protocol State Fuzzing*
> *原文作者：Paul Fiterau-Brostean, Bengt Jonsson, Robert Merget, Joeri de Ruiter, Konstantinos Sagonas, Juraj Somorovsky*
> *原文链接：https://www.usenix.org/conference/usenixsecurity20/presentation/fiterau-brostean*
> *发表会议：USENIX Security*
> *笔记作者：宋坤书@安全学术圈*
> *主编：黄诚@安全学术圈*

### 1、研究背景

UDP（用户数据报协议）作为一种不可靠传输协议，广泛应用于VoIP（网络电话）、隧道技术、物联网（IoT）和Web协议。由于UDP本身不提供任何安全机制，DTLS（数据报传输层安全协议）被引入以确保在不可靠传输环境下的通信安全。DTLS是TLS（传输层安全协议）的变体，专为处理UDP的无连接特性设计，如消息丢失、乱序、分片以及DoS攻击防护。这些特性使得DTLS的协议分析比基于TCP的TLS更为复杂，而现有的DTLS安全研究尚显不足。

本文通过扩展TLS-Attacker框架开发了支持DTLS的测试平台，并利用协议状态模糊测试技术分析了13种DTLS实现。本文发现多个安全漏洞，包括JSSE的认证绕过漏洞以及物联网和WebRTC常用实现中的加密处理缺陷。这些发现推动了漏洞修复，并为DTLS安全性研究提供了重要支持。

### 2、DTLS测试框架与协议状态模糊测试

#### 2.1 DTLS测试框架的实现

本文基于TLS-Attacker框架扩展了对DTLS 1.0和1.2的支持，开发了一个DTLS测试框架。TLS-Attacker是一个开源Java工具，专门用于TLS协议分析和测试。扩展后的框架支持生成和处理DTLS数据包，包括握手消息分片、服务器Cookie处理、记录纪元、消息序列号管理、重传和分片操作等，使DTLS协议的测试更加灵活高效。这些特性特别针对DTLS在处理UDP的无状态和不可靠传输时的复杂性。

#### 2.2 DTLS协议的关键特性

DTLS协议包含几个关键特性，这些特性直接影响测试框架的设计：

1. **DTLS版本**：包括DTLS 1.0（基于TLS 1.1）、DTLS 1.2（基于TLS 1.2）以及正在开发中的DTLS 1.3。
2. **DTLS握手协议**：负责协商加密算法、会话密钥等。客户端和服务器通过一系列消息交换信息并建立安全通道，DTLS握手协议的过程如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE7QmrTEsehxOXAiaxkCDL90bulK7n7iaNYRrCAo7rFZUOYlYFHtlL1OxH2icHjJgb2TwBXWU2zUfgTg/640?wx_fmt=png&from=appmsg)

3. **记录层**：所有数据都被封装成记录。每个记录包含头部信息和数据部分，负责加密、完整性校验等。
4. **分片与重组**：由于UDP的大小限制，DTLS允许将较大的消息分成多个片段传输，并支持重组。
5. **消息序列号与重放保护**：DTLS使用显式的消息序列号和重传机制，确保消息传输的可靠性。

这些特性决定了测试框架必须能够处理UDP的无连接特性，如消息丢失、乱序和分片。

#### 2.3 协议状态模糊测试框架

本文提出的状态模糊测试框架通过模型学习技术推断协议实现的行为模型，以Mealy机（一种有限状态自动机）描述协议如何响应一系列消息。框架由LEARNER（学习器）、MAPPER（映射器）和SUT（被测系统）组成：LEARNER生成输入符号，MAPPER将其转换为完整的协议消息并发送至SUT，同时将SUT的响应翻译为输出符号，最终通过记录输入输出关系构建最小化的确定性Mealy机模型。整个学习过程通过假设构建和假设验证的交替迭代，逐步提高模型的准确性。协议状态模糊测试框架组成如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE7QmrTEsehxOXAiaxkCDL90eUB5T5aaRPNBL8OyRichsjzbQdgOyE9icufBI6wCibAM8hkhyhwaYXU9A/640?wx_fmt=png&from=appmsg)

### 3、实验设置与实验结果

#### 3.1 实验设置

实验设置包含协议实现、密钥交换算法、客户端认证设置（决定输入字母表的组成）以及是否丢弃重传消息等其他相关配置。分析的协议实现包括13种DTLS实现，其中既有通用TLS实现（如OpenSSL、GnuTLS、MbedTLS等），也有专为物联网设计的轻量级实现（如Scandium和TinyDTLS）。在实验中，输入字母表包括使用支持的每种密钥交换算法执行握手所需的输入、两个警报和一个应用程序消息，并根据客户端认证设置三种模式（必需、可选和禁用）。部分实现由于功能限制或模型规模过大，针对不同密钥交换算法分别生成模型以保持学习时间合理。13种DTLS实现如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE7QmrTEsehxOXAiaxkCDL908bo9I6YiajxdggQHKFflsKiabx0CvDVSiaiadS38opcAyVxK6lf1iawgibfw/640?wx_fmt=png&from=appmsg)

#### 3.2 实验结果（模型学习效果）

1. **状态数量**：实验结果显示，所有DTLS实现的状态数量平均为25个，明显高于TLS实现的9个，说明DTLS协议具有更高的复杂性。状态数量受输入字母表的影响，例如，PSK配置生成的模型状态较少，而ECDH配置因握手流程更长，状态数量更多。此外，状态数量越大的模型中通常发现更多漏洞，例如JSSE、PionDTLS和的模型。
2. **测试数量**：测试数量在2.1万到11万之间，模型状态越多的实现（如PionDTLS）测试次数多，而GnuTLS尽管状态较少，却因特殊实现导致测试次数接近PionDTLS。这是因为其设计对偏离正常流程的输入响应有限，增加了状态唯一识别序列的难度。
3. **学习时间**：大多数实验在一天内完成，但较大的模型（如PionDTLS）或响应延迟较长的实现（如Scandium和GnuTLS）显著增加了学习时间。这表明响应时间优化和输入管理对提升学习效率至关重要，同时模型中发现的漏洞强调了减少状态数量的重要性。

实验结果如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE7QmrTEsehxOXAiaxkCDL90ricmicuFheericYFezZH25cFXEFic0s3ibJUVqqzonHbUGW0Fe8EpLiaptCw/640?wx_fmt=png&from=appmsg)

### 4、非规则行为识别及总结

#### 4.1 非规则行为识别策略

为了识别潜在的漏洞，研究采用了三种主要策略。

1. **识别不规则的握手流程**：通过分析学习到的模型，识别与规范不符但能完成握手的异常流程，例如缺失、重复或改变消息顺序的情况。研究使用脚本简化模型，去除无法完成握手的状态，从而更容易定位异常握手。这一方法揭示了“提前完成握手（early Finished）”这样的问题，其中握手在缺少ChangeCipherSpec消息时即完成。此类问题已在JSSE、Scandium和PionDTLS等实现中被发现并记录
2. **检查不符合规范的服务器输出**：研究重点分析不符合规范的服务器响应，尤其是ServerHello消息。通过对手动构造的消息进行探测，研究发现了一些意外的行为，例如TinyDTLS在使用无效的epoch值时依然能完成握手。此外，研究还关注了系统如何响应异常的Alert消息，这有助于揭示系统在处理加密错误时的潜在问题。
3. **分析代码实现**：研究通过检查引发不规则行为的代码路径，进一步发现了可能更严重的安全漏洞。这种方法不仅揭示了与已知问题直接相关的缺陷，还发现了与这些行为无直接关系但存在相同代码路径的漏洞，如PionDTLS中的提前处理应用数据问题。这些策略结合在一起，为DTLS协议的安全分析提供了更全面的视角。

#### 4.2 非规范行为总结

在对学习到的模型进行分析后，发现多种符合和不符合规范的行为模式，检测到的DTLS实现的非规范行为如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE7QmrTEsehxOXAiaxkCDL90cwhsWUfvAicQ09rY29Gboq2PP8R6mA5k246G8ibN4Q9PTibga26lrH3mw/640?wx_fmt=png&from=appmsg)

1. **无效message\_seq序号的握手**：5个DTLS实现允许用较高的message\_seq值启动握手，违背了DTLS规范要求。
2. **不符合规范的Cookie计算**：4个DTLS实现在计算Cookie值时出现错误，导致无法正确验证后续的ClientHello消息。NSS甚至完全跳过了Cookie交换步骤，与规范的推荐不符。
3. **无效消息顺序的握手**：JSSE、PionDTLS和未能正确验证消息顺序，允许无效消息序列完成握手，此类行为可能导致严重的安全问题。

### 5、DTLS实现中发现的安全漏洞

在对DTLS协议的分析中，研究发现了多个安全漏洞，这些漏洞主要源于协议实现中不符合规范的行为，特别是缺乏对握手流程和消息顺序的严格验证。本文通过扩展TLS-Attacker框架，采用协议状态模糊测试方法，分析了多种DTLS实现，发现了诸如认证绕过、无效消息序列号、无效的握手顺序等问题。

这些漏洞的根本原因是大多数DTLS实现没有使用适当的状态机设计。许多实现通过简单的逻辑（如switch语句）来验证握手流程，但没有进行完整的消息流验证。例如，Scandium未能严格检查握手消息顺序，导致了安全漏洞。此外，TLS和DTLS协议中的代码复用现象较为普遍，意味着一个协议中的漏洞可能影响到另一个协议的安全性。研究发现的具体漏洞如下：

1. **JSSE中的客户端认证绕过**：JSSE允许客户端绕过认证，导致可以在没有证书或CertificateVerify消息的情况下完成握手。
2. **Scandium中的状态机问题**：Scandium允许提前发送Finished消息或多次发送ChangeCipherSpec，暴露了状态机设计问题。
3. **PionDTLS中的严重漏洞**：PionDTLS存在提前发送Finished消息、处理未加密应用数据和错误重传HelloVerifyRequest的漏洞。
4. **GnuTLS中的无效握手开始**：GnuTLS 3.5.19错误地将大多数消息当作ClientHello处理，导致无效握手开始。
5. **TinyDTLS中的安全漏洞**：TinyDTLS允许不安全的重协商、ChangeCipherSpec崩溃和无效epoch号握手。
6. **OpenSSL中的漏洞**：OpenSSL错误处理重传的Finished消息，并未正确发送适当的警报。

此外，研究还发现，DTLS协议在设计时未能明确解决一些问题，如ChangeCipherSpec消息的顺序问题，这为漏洞提供了潜在的源头。虽然在DTLS 1.3草案中已经移除了ChangeCipherSpec消息以解决这一问题，但早期版本仍然存在此歧义，导致一些实现出现问题。总体而言，缺乏状态机设计和不规范的消息验证是导致DTLS协议中安全漏洞的主要原因。因此，在协议标准中应该明确规定状态机设计，并要求实现遵守这些设计，以提高协议的安全性。

### 6、本文贡献

本文的主要贡献包括：

* **扩展TLS-Attacker框架**：本文将TLS-Attacker框架扩展以支持DTLS协议，利用该框架实现了一个DTLS服务器的协议状态模糊测试平台。
* **提供Mealy机模型**：为十三种DTLS服务器实现提供了Mealy机模型，涵盖了常见的密钥交换算法和客户端证书认证设置。
* **漏洞分析**：通过分析学习到的模型，报告了多个不符合规范的行为和安全漏洞。这些漏洞不仅影响DTLS实现，也影响了相关库中的TLS部分。

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