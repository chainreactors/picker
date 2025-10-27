---
title: Kimsuky Hackers使用新的自定义RDP包装器进行远程访问
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581104&idx=1&sn=3008c37d11243c3623a0ad43c63ed814&chksm=e9146d8ade63e49c28298c2a9b3d0b77e46c198a870adb5ec4eab0136a34c0ec75b3b8a52d2a&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-13
fetch_date: 2025-10-06T20:36:28.166532
---

# Kimsuky Hackers使用新的自定义RDP包装器进行远程访问

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icLF3b1krPaMGaibA6sgM3y9nZWQGmrlTh1YLEYNic6m6dbKq0E0oO35zr2ZAqeZqplEduwAEfQkZwA/0?wx_fmt=jpeg)

# Kimsuky Hackers使用新的自定义RDP包装器进行远程访问

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

被称为Kimsuky的朝鲜黑客组织在最近的攻击中被发现使用定制的RDP包装器和代理工具直接访问受感染的机器。

发现该活动的AhnLab安全情报中心（ASEC）表示，朝鲜黑客现在正使用一套多样化的定制远程访问工具，而不再仅仅依赖于PebbleDash等嘈杂的后门，但PebbleDash目前仍在使用中，此举也是Kimsuky改变策略的手段之一。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icLF3b1krPaMGaibA6sgM3y9UcGiclyPxJyMn32jnRonoYKTYjYzfUjfDhFSyHZx3CqvfoNgyibO4HibQ/640?wx_fmt=png&from=appmsg)Kimsuky最新的攻击链

最新的感染链始于一封鱼叉式网络钓鱼电子邮件，其中包含伪装成PDF或Word文档的恶意快捷方式（. lnk）文件附件。这些电子邮件包含收件人的姓名和正确的公司名称，表明Kimsuky在攻击前进行了侦察。

打开.LNK文件会触发PowerShell或Mshta从外部服务器检索额外的负载，包括：

**·**PebbleDash，一个已知的Kimsuky后门，提供初始系统控制。

**·**一个修改版本的开源RDP包装工具，支持持久的RDP访问和安全措施绕过。

**·**代理工具绕过私有网络的限制，允许攻击者访问系统，即使直接RDP连接被阻止。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icLF3b1krPaMGaibA6sgM3y9UcGiclyPxJyMn32jnRonoYKTYjYzfUjfDhFSyHZx3CqvfoNgyibO4HibQ/640?wx_fmt=png&from=appmsg)自定义RDP包装器

RDP Wrapper是一个合法的开源工具，用于在Windows版本（如Windows Home）上启用本地不支持的远程桌面协议（RDP）功能。

它充当中间层，允许用户在不修改系统文件的情况下启用远程桌面连接。Kimsuky的版本改变了导出功能，以绕过反病毒检测，并可能区分其行为，足以逃避基于签名的检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icLF3b1krPaMGaibA6sgM3y9ms02ibxpRy3rYk5yV1kB9NYQickHicV8bRQsibicaGPo8lPg6161B73iaJmg/640?wx_fmt=png&from=appmsg)

自定义RDP包装器导出功能

使用自定义RDP包装器的主要优点是规避检测，因为RDP连接通常被视为合法的，允许Kimsuky在雷达下停留更长时间。

此外，与通过恶意软件进行shell访问相比，它提供了更舒适的基于gui的远程控制，并且可以通过中继绕过防火墙或NAT限制，允许从外部进行RDP访问。

ASEC报告说，一旦Kimsuky在网络上站稳脚跟，他们就会放弃二次有效载荷。其中包括一个键盘记录器，它捕获击键并将其存储在系统目录中的文本文件中，一个infostealer（强制复制）提取保存在web浏览器上的凭据，以及一个基于powershell的ReflectiveLoader，它允许在内存中执行有效负载。

整体来看，Kimsuky作为一个持续不断的威胁，也是朝鲜致力于收集情报最多产的网络间谍威胁组织之一。根据ASEC的最新发现表明，其威胁组织正转向更隐蔽的远程访问方法，以延长在受损网络中的停留时间。

参考及来源：https://www.bleepingcomputer.com/news/security/kimsuky-hackers-use-new-custom-rdp-wrapper-for-remote-access/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icLF3b1krPaMGaibA6sgM3y9fyJZpK5rs54WM9CrkluLRAv9qknYqIl6HhibnVaby0t7KsD2yAEiamRA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icLF3b1krPaMGaibA6sgM3y9TH6nvcrd1pyKYibMoW3eQ1LPsleXbCibbNRkVVfg8kveWrevPCS8MbwA/640?wx_fmt=png&from=appmsg)

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