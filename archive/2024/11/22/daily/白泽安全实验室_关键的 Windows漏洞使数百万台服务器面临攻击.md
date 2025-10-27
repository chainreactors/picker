---
title: 关键的 Windows漏洞使数百万台服务器面临攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492420&idx=1&sn=983ff5f33ddc1bf11baeca0a42b1516d&chksm=e90dc96ede7a4078dd37a6fa8042d5b533576a416e384248af4710dc495252353c671a1a9311&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-11-22
fetch_date: 2025-10-06T19:19:33.628474
---

# 关键的 Windows漏洞使数百万台服务器面临攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 关键的 Windows漏洞使数百万台服务器面临攻击

BaizeSec

白泽安全实验室

**一、事件概述**

Kerberos协议最初由麻省理工学院（MIT）在1980年代开发，目的是为了提供一个安全的身份验证机制，特别是在分布式计算环境中。它通过使用密钥分发中心（KDC）和基于凭证的认证机制，确保了用户身份的安全性和网络通信的保密性。从Windows 2000开始，微软在其操作系统中集成了对Kerberos协议的全面支持，使其成为Windows操作系统中实现安全认证和授权的核心机制被广泛使用。近日，微软在其“Patch Tuesday”更新中发布了针对Windows Kerberos认证协议的关键漏洞补丁。该漏洞（CVE-2024-43639）被评为9.8的CVSS严重性评分，表明其对全球数百万服务器构成了极高的安全风险。

**二、技术分析**

此次发现的是Windows Kerberos认证协议中的一个关键漏洞（CVE-2024-43639），允许未经身份验证的攻击者在受影响的系统上执行远程代码。通过利用这个缺陷，攻击者可以向一个易受攻击的系统发送特别制作的请求，利用Windows Kerberos中的密码协议漏洞获得未经授权的访问权限，并执行任意代码。根据Censys的调查，全球有超过两百万（2,274,340）台暴露的Windows服务器实例，其中1,211,834台可能易受攻击。然而，并非所有这些实例都易受攻击，只有配置为Kerberos KDC代理的服务器才会受到影响。

KDC代理协议服务器是一种允许客户端通过HTTPS安全地与KDC服务器进行通信的机制。这种服务器使用Kerberos协议来处理身份验证和授权，其中UDP/TCP 88端口用于Kerberos认证服务和票据授予服务的交换，而TCP 464端口则用于处理Kerberos密码更改。这些协议通常被设计为在可以直接和可靠访问KDC服务器的网络环境中工作，比如在同一局域网内或者通过VPN连接的远程位置。KDC代理协议服务器的应用场景包括远程桌面网关和DirectAccess等服务，它们使得用户即使在外部网络也能通过HTTPS安全地进行Kerberos认证，从而安全地访问内部网络资源。简而言之，KDC代理协议服务器通过HTTPS为Kerberos协议提供了一个安全的通信桥梁，使得用户可以在不同的网络环境下安全地进行身份验证和访问控制。

**三、漏洞详情**

|  |  |  |  |
| --- | --- | --- | --- |
| **C****VE ID** | CVE-2024-43639 | **公布时间** | 2024-11-13 |
| **类型** | 远程代码执行 | **CVSS** | 9.8 |
| **攻击向量** | 网络 | **所需权限** | 无 |
| **攻击复杂度** | 低 | **用户交互** | 不需要 |
| **PoC****/EXP** | 未公开 | **在野利用** | 未发现 |

参考链接：

https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2024-43639

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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