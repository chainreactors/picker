---
title: Microsoft 在 Windows Server 中弃用 PPTP 和 L2TP VPN 协议
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247578417&idx=2&sn=b5e742b3ebb5a7f43bbe8f1182b48246&chksm=e914630bde63ea1ddbc255507394a85e8ff0385ce03f5e5f5f59392553730a06e1a6ba57a690&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-10-17
fetch_date: 2025-10-06T18:52:54.404912
---

# Microsoft 在 Windows Server 中弃用 PPTP 和 L2TP VPN 协议

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28jFB6tysKv6jWFRhXKz4djpaqibqBGDYTekY0WeBnPF3HLXxukHheOmqvic0PfhMe2gljw5GALF9Eg/0?wx_fmt=jpeg)

# Microsoft 在 Windows Server 中弃用 PPTP 和 L2TP VPN 协议

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Microsoft 已在未来版本的 Windows Server 中正式弃用点对点隧道协议 (PPTP) 和第 2 层隧道协议 (L2TP)，并建议管理员切换到提供更高安全性的不同协议。

20 多年来，该企业一直使用 PPTP 和 L2TP VPN 协议来提供对企业网络和 Windows 服务器的远程访问。

然而，随着网络安全攻击和资源变得更加复杂和强大，协议变得越来越不安全。例如，PPTP 很容易受到捕获的身份验证哈希值的离线强力攻击，而 L2TP 不提供加密，除非与其他协议（如 IPsec）结合使用。

但是，如果 L2TP/IPsec 配置不正确，可能会引入使其容易受到攻击的弱点。

因此，Microsoft 建议用户转向更新的安全套接字隧道协议 (SSTP) 和 Internet 密钥交换版本 2 (IKEv2) 协议，这些协议可提供更好的性能和安全性。

微软表示：“此举是微软战略的一部分，旨在通过将用户过渡到安全套接字隧道协议（SSTP）和互联网密钥交换版本 2（IKEv2）等更强大的协议来增强安全性和性能。”

这些更新协议能提供相对来说的更加安全的加密、更快的连接速度和更好的可靠性，使它们更适合当今日益复杂的网络环境。Microsoft 还分享了每个协议的优点。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jFB6tysKv6jWFRhXKz4djzBJDUGXwCKwQuqfZIVSlSBxyYs6hqWYyJZtqXMHDF25xR8kWCQ1e6Q/640?wx_fmt=png&from=appmsg)SSTP 的优点

**·强加密**：SSTP使用SSL/TLS加密，提供安全的通信通道。

**·防火墙穿越**：SSTP可以轻松穿过大多数防火墙和代理服务器，确保无缝连接。

**·易于使用**：凭借 Windows 的本机支持，SSTP 的配置和部署非常简单。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jFB6tysKv6jWFRhXKz4djzBJDUGXwCKwQuqfZIVSlSBxyYs6hqWYyJZtqXMHDF25xR8kWCQ1e6Q/640?wx_fmt=png&from=appmsg)IKEv2的优点

**·安全性高**：IKEv2支持强大的加密算法和稳健的认证方法。

**·移动性和多宿主**：IKEv2 对于移动用户特别有效，可在网络变化期间保持 VPN 连接。

**·性能卓越**：与传统协议相比，IKEv2 能够更快地建立隧道并降低延迟，提供卓越的性能。

微软强调，当一项功能被弃用时，并不意味着它被删除。相反，它只是不再处于积极开发状态，并且可能会从未来版本的 Windows 中删除。此弃用期可能会持续数月至数年，让管理员有时间迁移到建议的 VPN 协议。

作为此弃用的一部分，Windows RRAS Server（VPN 服务器）的未来版本将不再接受使用 PPTP 和 L2TP 协议的传入连接。但是，用户仍然可以进行传出 PPTP 和 L2TP 连接。

为了帮助管理员迁移到 SSTP 和 IKEv2，Microsoft 在 6 月份发布了支持公告，其中包含了有关如何配置这些协议的步骤。

参考及来源：https://www.bleepingcomputer.com/news/microsoft/microsoft-deprecates-pptp-and-l2tp-vpn-protocols-in-windows-server/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jFB6tysKv6jWFRhXKz4djXyfXvVohf1Obv89GejzfSUuKWfRwAhynQekoglpU2nJ24ibyuOjSeyw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jFB6tysKv6jWFRhXKz4djARicWdKuQZKf8xunP2fFcHu4FIfF4Qv5zGhQtvr4UwuhickfAwDiac5icg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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