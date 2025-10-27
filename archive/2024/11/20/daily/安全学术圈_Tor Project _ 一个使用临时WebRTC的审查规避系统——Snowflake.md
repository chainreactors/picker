---
title: Tor Project | 一个使用临时WebRTC的审查规避系统——Snowflake
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491398&idx=1&sn=2f6dfdc343502405d1889ebc6c6270e7&chksm=fe2ee0cdc95969db9f6b4c0e37a3f87ef1d1c3c4d74df6cac63e11646f17fe86cef7299b2c76&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-11-20
fetch_date: 2025-10-06T19:18:51.265910
---

# Tor Project | 一个使用临时WebRTC的审查规避系统——Snowflake

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WHiaHyLjNNLYNYo0x785fgImIEzNF15JtRC11KibIhWrm149tOf7VbiaSQo5EZ5dLMtDQtYhEoKLibzaw/0?wx_fmt=jpeg)

# Tor Project | 一个使用临时WebRTC的审查规避系统——Snowflake

原创

宋坤书

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHiaHyLjNNLYNYo0x785fgImucq7HRsbVoBcYkYABoibBsCNwrrUXW3YAWABC332qugxLhD0ghkBYmQ/640?wx_fmt=png&from=appmsg)

> *原文标题：Snowflake, a censorship circumvention system using temporary WebRTC proxies*
> *原文作者：Cecylia Bocovich, Arlo Breault, David Fifield, Serene, Xiaokang Wang*
> *原文链接：https://www.usenix.org/conference/usenixsecurity24/presentation/bocovich*
> *发表会议：USENIX Security*
> *笔记作者：宋坤书@安全学术圈*

### 1、研究背景

Snowflake作为一个抗审查的网络通信系统的设计和效果。其主要特点是通过大量低成本、临时的代理服务器（例如WebRTC代理）来绕过审查，使得审查者无法轻易封锁整个系统。系统的核心目标是增加审查者的封锁成本，使其在封锁时面临过度封锁或无法有效封锁的困境。Snowflake通过分散的、可替换的代理来实现这一点，每个代理的可靠性较低，但可以通过多个代理池来保障用户的连通性。

本文还介绍了Snowflake如何解决技术挑战（例如如何提供良好的用户体验，尽管每个代理可能不稳定），并讨论了Snowflake在X罗斯、X朗、X国和X曼斯坦等国家的实地测试案例。总的来说，本文主要评估了Snowflake的设计思路、实施效果及其在抗审查中的作用。

### 2、Snowflake工作原理

Snowflake代理连接的包括三个阶段：对接阶段（Rendezvous），客户端向中心服务器（称为 "broker"）发送请求以匹配一个临时代理；连接建立（Connection Establishment），客户端和代理通过 WebRTC 建立连接，使用对接阶段交换的信息完成连接；数据传输（Data Transfer），代理将客户端的数据传输到桥接节点（bridge），而桥接节点则将数据定向到最终目标（如 Tor 网络）。下图是Snowflake代理连接过程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHiaHyLjNNLYNYo0x785fgIm2BW1AW9BySribyKqjIt3fnoiciapEsBqoGNJoxHCP7blmXpGeicoZx8PMw/640?wx_fmt=png&from=appmsg)

Snowflake代理连接的包括三个阶段，以此实现稳定的网络规避能力：

1. 对接阶段：客户端通过间接方式向中心服务器（broker）请求代理匹配，代理通过WebRTC与客户端建立直接连接。模块化设计结合多种抗审查策略（如域前置、AMP缓存）等抗审查方法隐藏broker,提升对接可靠性。Snowflake对接阶段的信息交互如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WHiaHyLjNNLYNYo0x785fgIm9zCqQQUSL1OzDfJ4gnia15YTxhHSCC8zyhwgyDibvPaEyEC3S3IRqrxA/640?wx_fmt=png&from=appmsg)

2. 连接建立：使用WebRTC的ICE流程完成NAT遍历，客户端与代理找到可用路径实现对等连接，同时避免使用易被封锁的TURN中继。代理动态匹配策略优化资源利用。
3. 数据传输：代理充当中转站，通过WebRTC和WebSocket实现数据传输，配合端到端加密（如Tor协议）保障隐私与安全。采用Turbo Tunnel机制应对代理失效，支持会话恢复，实现流量连续性。

### 3、Snowflake协议指纹识别

Snowflake 旨在通过模仿合法WebRTC流量的特征绕过审查。然而，由于WebRTC协议的复杂性，它容易暴露特定指纹，本文总结了主要风险与应对策略。

#### 3.1 指纹识别的主要问题及应对

1. STUN服务器
   风险：若使用专用STUN服务器，审查者可轻松封锁这些节点。应对：随机选择公共STUN服务器池，避免固定化。
2. STUN 消息格式
   风险：通过明文UDP传输的STUN消息，可能暴露特定顺序或内容特征。应对：考虑引入加密协议（如DTLS）以增加伪装性。
3. TLS指纹暴露
   风险：HTTPS对接机制可能通过TLS指纹（如加密算法选择、握手细节）被识别。应对：使用uTLS模拟主流浏览器的TLS指纹，避免显著差异。
4. DTLS握手特征
   风险：WebRTC的DTLS握手层在UDP上运行，特征明显。应对：通过修改Pion WebRTC库减少独有特征，但效果有限。
5. 流量类型差异
   风险：Snowflake使用WebRTC数据通道，而主流应用多使用音视频流，易被区分。应对：必要时可伪装数据为音视频流，模拟真实应用场景。

#### 3.2 相关研究发现

1. 未伪装的TLS指纹曾导致Snowflake的域名前置机制在伊朗被屏蔽，可以使用uTLS伪装TLS指纹[1]。
2. Pion DTLS握手特征曾被用于在俄罗斯阻断Snowflake流量[2]，可以通过修改Pion库减少DTLS指纹特征。
3. DNS查询（如常见的STUN服务器和Snowflake客户端的DNS查询）和数据通道特性仍可能被利用[3]，可以探索替代对接方法或采用更智能的STUN服务器。

### 4、值得注意的拦截尝试

Snowflake在遭遇审查时，用户数量通常是增加而不是减少，因为随着审查的加强，用户从弹性较弱的系统转移到弹性较强的系统。下面是Snowflake在X国、X罗斯、X朗和X曼斯坦的封锁经历：

1. X国：没有长期的系统性封锁，但多次尝试封锁Snowflake的特定功能，早期通过封锁代理IP地址和STUN服务器来限制连接，最近的封锁尝试（如域名前置封锁和流量节流）通常是暂时的或非针对性行为，对用户数量的影响相对较小。
2. X罗斯：2021年通过分析DTLS指纹封锁Snowflake，这次行动只是部分成功，反而促进了更多用户使用。团队通过修复漏洞和发布更新解决了问题。
3. X朗：2022年抗议期间用户数量激增，但因TLS纹封锁用户数量减少。团队通过启用伪装功能（uTLS）恢复了用户量。
4. X曼斯坦：封锁手段严厉且无差别，包括DNS和TCP RST注入、UDP端口阻断等，导致用户数量大幅下降，尽管采取备用端口等措施，仍难以应对。

网络审查和封锁形式因国家不同而异，成功的抗封锁需要与用户沟通，并根据审查者的技术和资源制定策略。封锁抵抗是一个相对过程，不是绝对的。虽然Snowflake可以被封锁，但其目标是提升抗封锁能力，使更多审查者无法轻易封锁。

### Reference

[1]Sergey Frolov and Eric Wustrow. The use of TLS in censorship circumvention. In Network and Distributed System Security. The Internet Society, 2019.
https://dx.doi.org/10.14722/ndss.2019.23511.

[2]Kyle MacMillan, Jordan Holland, and Prateek Mittal. Evaluating Snowflake as an indistinguishable censorship circumvention tool. CoRR, abs/2008.03254, 2020.
https://arxiv.org/abs/2008.03254.

[3]Junqiang Chen, Guang Cheng, and Hantao Mei. F-ACCUMUL: A protocol fingerprint and accumulative payload length sample-based Tor-Snowflake traffic-identifying framework. Applied Sciences, 13(1), 2023.
https://www.mdpi.com/2076-3417/13/1/622.

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