---
title: 覆盖1400个服务器！OpenSSH 严重漏洞可导致整个系统遭入侵
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545671&idx=3&sn=86fc4f651ec46819ac9eb7c6c31d8e48&chksm=fa938586cde40c90916dad84cf4eef1b825910fcabc3861354084854d7c472fda2e8e905044b&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-04
fetch_date: 2025-10-06T17:44:26.442335
---

# 覆盖1400个服务器！OpenSSH 严重漏洞可导致整个系统遭入侵

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lpibcmuyltmmsItScgSorJVgSl1bSGicjic4etuwJUE5sFPGYQSBr6iaaMb3l0JAoZ4bicYYyY1tL7GVQ/0?wx_fmt=jpeg)

# 覆盖1400个服务器！OpenSSH 严重漏洞可导致整个系统遭入侵

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176lpibcmuyltmmsItScgSorJV1QIlmoTibZvv1M3JMdUX0fA4H0zxmrD33FWPf1ySB2c95JM5dzm2DWA/640?wx_fmt=png&from=appmsg)

根据最新分析表明，在 OpenSSH 服务器中发现一个严重漏洞后，超过 1400 万个暴露在互联网上的 OpenSSH 实例面临风险。
远程未经身份验证的代码执行 (RCE) 漏洞 (CVE-2024-6387) 可能导致整个系统被入侵，攻击者可以以最高权限执行任意代码。

这可能导致：

●全面接管系统

●安装恶意软件

●数据处理

●创建后门以实现持久访问

●网络传播，允许攻击者利用受感染的系统作为立足点，遍历和利用组织内其他易受攻击的系统

研究人员还警告说，通过此 CVE 获取根访问权限将允许威胁行为者绕过防火墙、入侵检测系统和日志记录机制等关键安全机制，进一步掩盖其活动。

这个被称为 regreSSHion 的漏洞被评为严重和危急，特别是对于那些严重依赖 OpenSSH 进行远程服务器管理的企业而言。

# **广泛存在的漏洞**

OpenSSH 是一种使用安全外壳 (SSH) 协议的远程登录连接工具，该协议用于在不安全的网络上实现安全通信。

该工具支持多种加密技术，是多种类 Unix 系统（包括 macOS 和 Linux）的标准配置。此特定漏洞会影响基于 glibc 的 Linux 系统。

由于 OpenBSD 在 2001 年开发了安全机制，因此 OpenBSD 系统不会受到此漏洞的影响。

Qualys 表示，通过使用 Censys 和 Shodan 的搜索，已发现超过 1400 万个潜在易受攻击的 OpenSSH 服务器实例暴露在互联网上。

Qualys 全球客户群中约有 700,000 个面向互联网的外部实例存在漏洞。

RCE 是之前已修补的漏洞 CVE-2006-5051 的回归，该漏洞于 2006 年报告。当之前已修复的漏洞在后续软件版本中再次出现时，就会发生回归，这通常是由于更改或更新无意中重新引入了该问题。

研究人员指出，该漏洞很难利用，因为它具有远程竞争条件特性，需要多次尝试才能成功攻击。这可能会导致内存损坏，并且需要克服地址空间布局随机化 (ASLR)。

然而，深度学习的进步可以为攻击者提供利用此类漏洞的“巨大优势”，从而显著提高利用率。

# **如何防止被利用**

由于此缺陷，OpenSSH 4.4p1 之前的版本容易受到攻击，除非它们针对 CVE-2006-5051 和 CVE-2008-4109 进行了修补。

由于意外删除了功能中的关键组件，该漏洞还在 v8.5p1 至 9.8p1（但不包括）中再次出现。

由于 CVE-2006-5051 的变换补丁，从 4.4p1 到 8.5p1（但不包括）的版本均不受到攻击。

已敦促使用受影响版本的组织采取以下措施，以减轻通过此漏洞进行攻击的风险：

●快速应用 OpenSSH 的可用补丁并确定正在进行的更新过程的优先级

●使用基于网络的控制来限制 SSH 访问，最大限度地降低攻击风险

●分段网络以限制关键环境中的未经授权的访问和横向移动

●部署系统来监控和警告可能表明存在攻击企图的常见活动

原文来源：E安全

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