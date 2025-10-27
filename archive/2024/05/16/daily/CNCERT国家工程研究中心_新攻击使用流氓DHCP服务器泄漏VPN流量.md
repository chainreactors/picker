---
title: 新攻击使用流氓DHCP服务器泄漏VPN流量
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247544602&idx=2&sn=527f2ba1a3cd70ef0987f463ea4f5bb1&chksm=fa9399dbcde410cd3b218bfedbb3fcd7336979d194d7fbf97398901aa0483668b574e707399a&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-05-16
fetch_date: 2025-10-06T17:16:37.555337
---

# 新攻击使用流氓DHCP服务器泄漏VPN流量

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176klnZrvTNYGoJ4dFiaPCCiciaT73lARpfXnfPPXpJ9ufqcicwcH5klu2cAQ3Oiay4Cxmv2UsmB1CBvtfSw/0?wx_fmt=jpeg)

# 新攻击使用流氓DHCP服务器泄漏VPN流量

网络安全应急技术国家工程中心

一种名为“TunnelVision”的新攻击可以将流量路由到 VPN 加密隧道之外，从而使攻击者能够窥探未加密的流量。

Leviathan Security 的报告中详细描述了该方法，它依赖于动态主机配置协议 (DHCP) 选项 121 的滥用，该选项允许在客户端系统上配置无类静态路由。

攻击者设置恶意 DHCP 服务器来更改路由表，以便所有 VPN 流量直接发送到本地网络或恶意网关，而不会进入加密的 VPN 隧道。

该报告中写道：“我们的技术是在与目标 VPN 用户相同的网络上运行 DHCP 服务器，并将 DHCP 配置设置为将自身用作网关。当流量到达网关时，会使用 DHCP 服务器上的流量转发规则将流量传递到合法网关，同时监听它。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28UxlpXkveudegRBvY9dkW5T28hVZsUYpUtmyN5fJFmcIHlN2HoqDPG7pIz75p7pODS5ncSoicjHRg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

开采过程

该问题在于 DHCP 缺乏可操纵路由的传入消息的身份验证机制，并被分配了漏洞标识符 CVE-2024-3661。

安全研究人员指出，该漏洞至少自 2002 年起就已被恶意分子利用，但尚无已知的主动利用案例。

Leviathan 已通知受影响的供应商以及 CISA 和 EFF。研究人员现已公开披露该问题以及概念验证漏洞，以提高人们的认识并迫使 VPN 供应商实施保护措施。

# **减轻 TunnelVision 攻击**

如果用户将设备连接到由攻击者控制或存在攻击者的网络，则他们更容易受到“TunnelVision”攻击的影响。

可能的场景包括咖啡店、酒店或机场等公共 Wi-Fi 网络。目标设备上的 VPN 容易受到路由操纵，大多数使用系统级路由规则而没有防泄漏保护措施的 VPN 客户端通常都会出现这种情况。

最后，需要在目标设备上启用自动 DHCP 配置，以便在网络连接期间应用恶意 DHCP 配置。

这又是一种常见的配置。但应注意，要使这种攻击发挥作用，用户必须先连接到合法 DHCP 服务器，然后再连接到恶意 DHCP 服务器。

研究人员表示，攻击者可以通过多种方式增加其恶意服务器首先被访问的机会，包括针对合法服务器的 DHCP 饥饿攻击。

·在 Linux 上使用网络命名空间将网络接口和路由表与系统的其余部分隔离，防止恶意 DHCP 配置影响 VPN 流量。

·配置 VPN 客户端以拒绝所有不使用 VPN 接口的入站和出站流量。例外情况应仅限于必要的 DHCP 和 VPN 服务器通信。

·将系统配置为在连接到 VPN 时忽略 DHCP 选项 121，这可以防止应用恶意路由指令，但在某些配置下可能会破坏网络连接。

·通过个人热点或虚拟机 (VM) 内进行连接。这将 DHCP 交互与主机系统的主网络接口隔离，从而降低了恶意 DHCP 配置的风险。

·避免连接到不受信任的网络，尤其是在处理敏感数据时，因为这些是此类攻击的主要环境。

VPN 提供商应增强客户端软件以实施自己的 DHCP 处理程序或集成额外的安全检查，以阻止应用有风险的 DHCP 配置。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/new-tunnelvision-attack-leaks-vpn-traffic-using-rogue-dhcp-servers/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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