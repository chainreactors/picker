---
title: Microsoft SharePoint RCE 漏洞可被利用来破坏公司网络
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247579462&idx=1&sn=541bd360da0c5a0e969b17d37f31681c&chksm=e914677cde63ee6addc2f0510740f14706afe244ad9f07bb05ef43e5a56bceea731f0f8f06e5&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-11-09
fetch_date: 2025-10-06T19:19:05.653050
---

# Microsoft SharePoint RCE 漏洞可被利用来破坏公司网络

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o296hS5tD8MwVlk7lDqOHyYoI69XOg2ib0z2jzia21dSqXDhHTakqFbyqHjx0yXariazrDb2QMDn6KjVQ/0?wx_fmt=jpeg)

# Microsoft SharePoint RCE 漏洞可被利用来破坏公司网络

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

最近披露的 Microsoft SharePoint 远程代码执行 (RCE) 漏洞（编号为 CVE-2024-38094）正被用来获取对企业网络的初始访问权限。

CVE-2024-38094 是一个高严重性（CVSS v3.1 评分：7.2）RCE 漏洞，影响 Microsoft SharePoint，这是一个广泛使用的基于 Web 的平台，用作内联网、文档管理和协作工具，可以与 Microsoft 365 无缝集成应用程序。

微软于 2024 年 7 月修复了该漏洞，作为 7 月补丁星期二包的一部分，将该问题标记为“重要”。

上周，CISA 将 CVE-2024-38094 添加到已知被利用的漏洞目录中，但没有透露该漏洞是如何在攻击中被利用的。

Rapid7 发布的一份新报告揭示了攻击者如何利用 SharePoint 漏洞，称该漏洞被用于调查他们调查的网络漏洞。

相关报告中写道：“我们的调查发现，一名攻击者未经授权访问了服务器，并在网络中横向移动，从而损害了整个域。”

攻击者在两周内仍未被发现。Rapid7 确定初始访问向量是利用本地 SharePoint 服务器内的漏洞 CVE 2024-38094。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o296hS5tD8MwVlk7lDqOHyYozKW9P1EUvh7r7akTunWQ9q69w2N2reMFgLq7Ya3hFricMLQxU9gAbbw/640?wx_fmt=png&from=appmsg)使用 AV 损害安全

Rapid7 现在报告称，攻击者利用 CVE-2024-38094 未经授权访问易受攻击的 SharePoint 服务器并植入 Webshell。

调查显示，该服务器是通过公开披露的 SharePoint 概念验证漏洞被利用的。攻击者利用其初始访问权限，破坏了具有域管理员权限的 Microsoft Exchange 服务帐户，从而获得了更高的访问权限。接下来，攻击者安装了 Horoung Antivirus，这会造成冲突，导致安全防御失效并削弱检测能力，从而允许他们安装 Impacket 进行横向移动。

具体来说，攻击者使用批处理脚本（“hrword install.bat”）在系统上安装Huorong Antivirus，设置自定义服务（“sysdiag”），执行驱动程序（“sysdiag\_win10.sys”），并运行“HRSword” .exe' 使用 VBS 脚本。

这种设置导致了资源分配、加载驱动程序和活动服务等方面的多重冲突，导致该公司的合法防病毒服务崩溃而无能为力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o296hS5tD8MwVlk7lDqOHyYoKnrRXliaPJLS3iaGOJdXSIGJJlLkIZK16IY3Cp3UQEPtiaZltiaUEn2Mpg/640?wx_fmt=png&from=appmsg)

攻击的时间轴

在接下来的阶段，攻击者使用 Mimikatz 进行凭证收集，使用 FRP 进行远程访问，并设置计划任务进行持久化。

为了避免被发现，他们禁用了 Windows Defender、更改了事件日志并操纵了受感染系统上的系统日志记录。

everything.exe、Certify.exe 和 kerbrute 等其他工具用于网络扫描、ADFS 证书生成和暴力破解 Active Directory 票证。

第三方备份也成为破坏的目标，但攻击者试图破坏这些备份却失败了。

尽管尝试擦除备份是勒索软件攻击中的典型做法，为了防止轻松恢复，Rapid7 没有观察到数据加密，因此攻击类型未知。

随着主动利用的进行，自 2024 年 6 月以来未应用 SharePoint 更新的系统管理员必须尽快执行此操作。

参考及来源：https://www.bleepingcomputer.com/news/security/microsoft-sharepoint-rce-bug-exploited-to-breach-corporate-network/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o296hS5tD8MwVlk7lDqOHyYoaDia27XD7hMw91B9uxicqvM3ZdEiaAzk4JXzM62YGcMgDtticIdLdNfpkw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o296hS5tD8MwVlk7lDqOHyYoAhKKBMlscnFu3IZu35CgaZVibuGibdgFTbyd8mBd9dA0iclWJaRLlmZzA/640?wx_fmt=png&from=appmsg)

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