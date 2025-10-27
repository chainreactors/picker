---
title: 加州大学伯克利分校 | WebRTC的指纹识别
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491649&idx=1&sn=bc83920d74b744a309ceab87a1c26a3f&chksm=fe2d1fcac95a96dc040d41fc5846694d8ba4515a5a6b822a3c9deab2d23e7b880b89bc4b1763&scene=58&subscene=0#rd
source: 安全学术圈
date: 2025-02-08
fetch_date: 2025-10-06T20:38:03.842064
---

# 加州大学伯克利分校 | WebRTC的指纹识别

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WE68Zjyap9LSMcbmkkmtc3olnB8E2tCaT5HL3ibWIFlNmWVM0yoIU8U2iaVjfTF8Boy5gu4FwWrRWiaA/0?wx_fmt=jpeg)

# 加州大学伯克利分校 | WebRTC的指纹识别

原创

宋坤书@安全学术

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE68Zjyap9LSMcbmkkmtc3orszrR0ic5wKCWlgSywkjAiaE4egZAGYYlicntia6L3XgyFXib0TVDRwNgaA/640?wx_fmt=png&from=appmsg)

> *原文标题：Fingerprintability of WebRTC*
> *原文作者：David Fifield, Mia Gil Epner*
> *原文链接：https://arxiv.org/pdf/1605.08805*
> *笔记作者：宋坤书@安全学术圈*
> *主编：黄诚@安全学术圈*

### 1、背景介绍

互联网审查的核心任务是对网络流量进行分类，决定是否拦截或允许特定流量。审查者在分类过程中可能面临两种风险：过度拦截导致合法流量受阻，或不足拦截使得被禁流量漏网。规避审查的关键在于增加分类难度，使被禁流量的特征与合法流量尽可能相似，从而引发误判。为了绕过封锁，规避系统通常依赖代理访问受限内容，而IP地址伪装是规避审查的主要挑战。Snowflake是一种规避系统，通过在浏览器中运行代理，利用大量难以预测的IP地址解决了IP封锁的问题。

然而，即使解决了IP封锁，网络协议分类仍然是另一个难题。Snowflake基于WebRTC协议（浏览器内置的点对点通信框架）运行，其代理和客户端分别使用浏览器和独立的WebRTC实现。在通信中，代理充当WebRTC客户端，客户端则充当服务器。此设计可能暴露Snowflake的流量特征，尤其当WebRTC在现实中应用不足时，审查者可能会选择全面屏蔽该协议。因此，Snowflake的规避效果取决于其流量特征与其他合法WebRTC流量的相似性，以及WebRTC的普及程度是否足够高以避免被轻易识别和阻断。

### 2、WebRTC技术在规避网络审查中的潜力与挑战

#### 2.1 WebRTC技术概述

WebRTC是一个为实时通信应用设计的复杂协议和API集合，主要用于语音和视频聊天等。WebRTC不仅支持媒体流传输，还提供类似TCP的可靠数据通道和类似UDP的不可靠数据通道。WebRTC的一个重要特点是支持网络地址转换（NAT）穿越功能，这解决了早期基于TCP的Flash Proxy因缺乏NAT穿越而面临的采纳障碍。

WebRTC整合了多个相关协议，其中ICE协议用于NAT穿越，依赖于STUN和TURN技术。与此同时，WebRTC通过DTLS-SRTP协议来保护媒体流，DTLS用于安全的密钥交换，而SRTP则用于加密和保护实际的媒体流。本文旨在评估WebRTC在实际应用中的普及度、指纹多样性以及模仿重要应用指纹以规避封锁的可行性。WebRTC的协议栈如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE68Zjyap9LSMcbmkkmtc3ojqGNUZY3gyV2Laaq9V95XWF6WBl39NcCg9Yeh6OORel5w98bW0AzyA/640?wx_fmt=png&from=appmsg)

#### 2.2 威胁模型

在威胁模型中，审查者掌控被审查用户的通信外围，可以依据其策略阻断、修改或注入任何流量，但无法控制用户的个人设备。用户目标是访问受限的网络资源，而审查者则需在拦截流量和避免过度屏蔽之间权衡。假设审查者避免过度屏蔽的倾向越强，规避审查的成功概率也越高。

### 3、WebRTC协议特征

文中识别了多个WebRTC协议特征，这些特征可能有助于指纹识别。

* **STUN和TURN**：STUN和TURN协议用于NAT穿越，消息中包含属性（如SOFTWARE），有助于识别实现方式，类似于HTTP中的User-Agent头。除了客户端流量，服务器流量也可区分，且客户端选择的STUN服务器和发送的请求类型（如绑定请求、分配请求等）可作为指纹特征。某些应用强制使用TURN进行UDP转发，这也是一个可用于识别的特征。
* **DTLS**：DTLS层的多个特性，如DTLS版本（如v1.0和v1.2）、客户端提供的加密套件列表、服务器选择的加密套件、服务器的扩展信息等都有助于指纹识别。此外，服务器提供的证书（如“common name”字段和有效期）也包含可识别的信息。
* **媒体流与数据传输**：Snowflake使用可靠的WebRTC数据通道，基于DTLS协议进行传输，而其他WebRTC应用则通常使用媒体通道（如DTLS-SRTP或带SDES的SRTP）。虽然这些协议都是加密的，但它们之间可以通过传输协议的不同进行区分。

总的来说，这些WebRTC协议特征（如STUN/TURN服务器选择、DTLS版本、加密套件等）都可以用于区分不同应用和实现，从而形成可用于指纹识别的特征。

### 4、WebRTC应用的指纹分析

文中通过手动分析多款WebRTC应用的网络流量，探讨了它们在STUN/TURN连接、DTLS握手和加密特性方面的差异，以识别各应用的独特指纹。

* **Google Hangouts**：Google Hangouts使用WebRTC进行视频聊天，并通过 STUN 请求连接 Google STUN 服务器。然而在密钥交换过程中，它选择了SDES而非DTLS，因此DTLS在该实现中并未使用。
* **Facebook Messenger**：Facebook Messenger在浏览器通信中使用WebRTC和DTLS，在移动设备通信中使用SDES。其通过STUN和TURN请求连接，强制使用TURN进行数据转发。DTLS连接使用DTLSv1.0，包含指纹化特征，提供9个密码套件、无压缩方法、SRTP 扩展和两个椭圆曲线。
* **OpenTokRTC**：OpenTokRTC使用STUN请求连接到Tokbox TURN服务器，并通过多次Allocate 请求进行通信。DTLS连接使用DTLSv1.0，提供73个密码套件，其中很多过时且易受攻击。DTLS hello消息包含无压缩方法、SRTP扩展和心跳扩展。服务器选择TLS ECDHE RSA WITH AES 256 CBC SHA，证书有效期为30天。
* **Sharefest**：Sharefest作为数据传输服务，使用STUN请求连接Google STUN服务器。DTLS连接开始时发送两个相同的客户端hello消息，使用DTLSv1.0，提供9个密码套件、无压缩方法、SRTP扩展和两个椭圆曲线。服务器选择TLS ECDHE RSA WITH AES 256 CBC SHA，证书的公共名称为 "WebRTC"，有效期为30天。
* **Snowflake**：Snowflake使用STUN连接Google STUN服务器，并通过DTLSv1.0和v1.2建立连接。client hello提供17个密码套件，并包含无压缩方法、签名算法扩展、SRTP扩展和重新协商信息扩展。服务器选择DTLSv1.2，使用TLS ECDHE RSA WITH AES 128 GCM SHA256，证书有效期为 30 天。Snowflake是唯一使用DTLSv1.2的实现。

通过分析这些应用，可以发现虽然它们都采用了STUN/TURN和DTLS协议，但各自的实现细节和安全配置不同，从而形成了独特的指纹特征，这些特征可用于区分不同的WebRTC应用。

### 5、WebRTC流量的DTLS指纹分析与未来研究方向

本研究通过在Bro网络分析框架中编写脚本，探讨了如何通过DTLS握手特征进行指纹识别。该脚本记录了DTLS版本、密码套件、椭圆曲线、扩展和服务器证书有效期等信息，从而生成独特的指纹。通过在劳伦斯伯克利国家实验室（LBNL）的一天网络流量中运行该脚本，发现了仅有七次DTLS握手，涉及三个独特的客户端指纹和三个独特的服务器指纹。这个结果低于预期，表明WebRTC流量可能不广泛，或像Google Hangouts这样的应用程序未使用DTLS，从而在该流量中未被充分体现。

未来的工作将扩展脚本，分析更多流量并优化指纹识别方法，尤其是解决重复client hello消息等异常。此外，研究还计划扩大分析范围，涵盖STUN/TURN服务，并改进Bro框架对UDP连接的处理。关于WebRTC中数据通道与媒体通道的区分，研究讨论了审查者可能通过屏蔽数据通道而不影响整个WebRTC流量。Snowflake作为基于数据通道的应用，与使用媒体通道的应用相比，可能更容易受到单独的封锁。未来还可能通过在媒体通道上传输二进制数据，增加实现的复杂度，从而使Snowflake的流量更难与其他应用区分，有助于规避审查。本研究深入探讨了WebRTC协议在审查规避中的潜力，并揭示了指纹识别和规避方法的挑战。

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