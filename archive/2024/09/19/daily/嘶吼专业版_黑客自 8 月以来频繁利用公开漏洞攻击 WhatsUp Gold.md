---
title: 黑客自 8 月以来频繁利用公开漏洞攻击 WhatsUp Gold
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247578012&idx=1&sn=8f71511509699663e10b684f507e850d&chksm=e91461a6de63e8b0588b8f65c1d668014ee13a7b52f21c346c5d24a3829662398a9289002b91&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-09-19
fetch_date: 2025-10-06T18:26:24.115337
---

# 黑客自 8 月以来频繁利用公开漏洞攻击 WhatsUp Gold

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icqtSkbuA492yVNAhh7O2XkHSxjwuHdAlTFAtp0JYBVCy12FvotS4O8fS1lRW6EMu2NH621sGBgJA/0?wx_fmt=jpeg)

# 黑客自 8 月以来频繁利用公开漏洞攻击 WhatsUp Gold

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

黑客一直在利用 Progress Software 的 WhatsUp Gold 网络可用性和性能监控解决方案中两个严重漏洞的公开漏洞代码。

自 8 月 30 日以来，攻击中利用的两个漏洞是 SQL 注入漏洞，跟踪编号为 CVE-2024-6670 和 CVE-2024-6671，漏洞允许在未经身份验证的情况下检索加密密码。

尽管相关工作人员在两周前就解决了安全问题，但许多客户仍然需要更新软件，而威胁者正在利用这一漏洞发起攻击。

Progress Software 于 8 月 16 日发布了针对该问题的安全更新，并于 9 月 10 日在安全公告中添加了如何检测潜在危害的说明。

安全研究员 Sina Kheirkhah 发现了这些漏洞，并于 5 月 22 日将其报告给零日计划。8 月 30 日，该研究员发布了概念验证 (PoC) 漏洞。

该研究员在技术文章中解释了如何利用用户输入中不适当的清理问题将任意密码插入管理员帐户的密码字段，从而使其容易被接管。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icqtSkbuA492yVNAhh7O2Xkp02LiaEK6mSTG1mkjSqpXWUGswvia4T9ltfFZ34Mb3M4sQHwThbQ5ibjQ/640?wx_fmt=png&from=appmsg)

Kheirkhah 的漏洞概述

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icqtSkbuA492yVNAhh7O2Xkd1Fw1FhkGTk2pBXM0v5lZs3HxUkHs4sDmObE076hVDjsNmUybmoD2w/640?wx_fmt=png&from=appmsg)野外开发

网络安全公司最新的报告指出，黑客已经开始利用这些漏洞，根据观察，这些攻击似乎基于 Kheirkhah 的 PoC，用于绕过身份验证并进入远程代码执行和有效载荷部署阶段。在研究人员发布 PoC 漏洞代码五小时后，安全公司的遥测技术首次发现了主动攻击的迹象。

攻击者利用 WhatsUp Gold 的合法 Active Monitor PowerShell Script 功能，通过从远程 URL 检索的 NmPoller.exe 运行多个 PowerShell 脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icqtSkbuA492yVNAhh7O2XkQQ3zyFryiajbfcSorKR1YKpCPYfiaiaFgV34ZPEDFCHAS5aBoobEQWGSA/640?wx_fmt=png&from=appmsg)

攻击者部署的恶意 PowerShell 脚本

接下来，攻击者使用合法的 Windows 实用程序“msiexec.exe”通过 MSI 包安装各种远程访问工具 (RAT)，包括 Atera Agent、Radmin、SimpleHelp Remote Access 和 Splashtop Remote。

植入这些 RAT 可让攻击者在受感染的系统上建立持久性。

在某些情况下，研究人员观察到部署了多个有效载荷。分析师无法将这些攻击归因于特定的威胁组织，但使用多个 RAT 表明它可能是勒索软件参与者。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icqtSkbuA492yVNAhh7O2Xk7PzbosbVkiaF8v4pMg44fSndgdFDHeY4pTXKVYTiboMbOxkaDbpPbf3Q/640?wx_fmt=png&from=appmsg)

观察到的活动的攻击流程

据了解，这并不是 WhatsUp Gold 今年第一次受到公开漏洞的攻击。8 月初，威胁监测组织 Shadowserver Foundation 报告称，其蜜罐捕获了利用 CVE-2024-4885 的攻击，CVE-2024-4885 是一个于 2024 年 6 月 25 日披露的严重远程代码执行漏洞。这个缺陷也被 Kheirkhah 发现，两周后他在社交媒体上公布了完整的详细信息。

参考及来源：https://www.bleepingcomputer.com/news/security/hackers-targeting-whatsup-gold-with-public-exploit-since-august/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icqtSkbuA492yVNAhh7O2XkiamYZ3LzK6EjiadkzokRHJmVZc1wkNYoA6ia32fSKdQI9OJDJCibHHe9hQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icqtSkbuA492yVNAhh7O2XkiaibTqDuHrKtFQXlEVzYWvYdtv9kSFMPxcRK6B0KTBicLRNpiajia1BEkog/640?wx_fmt=png&from=appmsg)

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