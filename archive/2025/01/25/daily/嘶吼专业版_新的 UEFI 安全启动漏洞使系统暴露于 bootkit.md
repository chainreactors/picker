---
title: 新的 UEFI 安全启动漏洞使系统暴露于 bootkit
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580965&idx=2&sn=35ac8cf9ec1bfacb175b8622720863e2&chksm=e9146d1fde63e40910e314cac61af17533c328067d6bd015df8402266ba7692efae9a049c79f&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-01-25
fetch_date: 2025-10-06T20:11:07.375565
---

# 新的 UEFI 安全启动漏洞使系统暴露于 bootkit

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVL5x4atCsfmKibb6s9xa1nmhgadTk1eCNg2kRkKzlB8TekchtibAMOHlA/0?wx_fmt=jpeg)

# 新的 UEFI 安全启动漏洞使系统暴露于 bootkit

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

即使安全启动保护处于活动状态，也可能会利用一个新的 UEFI 安全启动绕过漏洞（编号为 CVE-2024-7344）影响 Microsoft 签名的应用程序来部署 bootkit，多个第三方软件开发商的多个实时系统恢复工具中存在易受攻击的 UEFI 应用程序。

Bootkit 是一种难以检测的严重安全威胁，因为它们在操作系统加载之前采取行动，并且在操作系统重新安装后仍然存在。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVTCoHkULXatTf8wYazBefNeicWc5vKnx3Qr0RGbXBkvg7Gsu5uKtP8gQ/640?wx_fmt=png&from=appmsg)根本问题

该问题源于使用自定义 PE 加载程序的应用程序，该加载程序允许加载任何 UEFI 二进制文件，即使它们未签名。具体来说，易受攻击的 UEFI 应用程序不依赖于“LoadImage”和“StartImage”等可信服务来根据信任数据库 (db) 和吊销数据库 (dbx) 验证二进制文件。

在这种情况下，“reloader.efi”手动解密“cloak.dat”中的二进制文件并将其加载到内存中，其中包含基本的加密 XOR PE 映像。攻击者可以通过使用易受攻击的“reloader.efi”替换应用程序在 EFI 分区上的默认操作系统引导加载程序，并在其名义路径上植入恶意“cloak.dat”文件来利用此不安全的过程。

系统启动时，自定义加载程序将解密并执行恶意二进制文件，而无需安全启动验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVHerch5kzDYJzVI4Vlw9h6tck5qpkMYavGUvpOvqX4UD9DHvoK1Lplw/640?wx_fmt=png&from=appmsg)

UEFI安全启动流程

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVTCoHkULXatTf8wYazBefNeicWc5vKnx3Qr0RGbXBkvg7Gsu5uKtP8gQ/640?wx_fmt=png&from=appmsg)影响范围

该漏洞影响旨在协助系统恢复、磁盘维护或备份的 UEFI 应用程序，而不是通用 UEFI 应用程序。ESET 的报告将以下产品和版本列为易受攻击的产品和版本：

**·**Howyar SysReturn 10.2.023\_20240919 之前版本

**·**Greenware GreenGuard 10.2.023-20240927 之前版本

**·**Radix SmartRecovery 11.2.023-20240927 之前版本

**·**三丰EZ-back系统10.3.024-20241127之前版本

**·**WASAY eRecoveryRX 8.4.022-20241127 之前版本

**·**CES NeoImpact 10.1.024-20241127 之前版本

**·**SignalComputer HDD King 10.3.021-20241127之前版本

应该注意的是，即使目标计算机上不存在上述应用程序，攻击者也可以利用 CVE-2024-7344。黑客可以通过仅部署易受攻击的“重新加载器”来执行攻击。

来自这些应用程序的 efi' 二进制文件。但是，使用上述应用程序和受影响版本的用户应尽快迁移到较新的版本，以消除攻击面。ESET 发布了一个视频，演示如何在启用了安全启动的系统上利用该漏洞。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVTCoHkULXatTf8wYazBefNeicWc5vKnx3Qr0RGbXBkvg7Gsu5uKtP8gQ/640?wx_fmt=png&from=appmsg)修复和缓解措施

Microsoft 已发布 CVE-2024-7344 补丁 ESET 于 2024 年 7 月 8 日发现该漏洞，并将其报告给 CERT 协调中心 (CERT/CC)，以便协调向受影响方披露。

受影响的供应商修复了其产品中的问题，微软于 1 月 14 日补丁星期二更新撤销了证书。在接下来的几个月中，ESET 与受影响的供应商合作评估建议的补丁并消除安全问题。

最终，微软于 2025 年 1 月 14 日撤销了易受攻击的 UEFI 应用程序的证书，这应该会阻止任何执行其二进制文件的尝试。此缓解措施会自动应用于安装了最新 Windows 更新的用户。

ESET 还共享 PowerShell 命令，关键系统的管理员可以使用这些命令手动检查撤销是否已成功应用。

参考及来源：https://www.bleepingcomputer.com/news/security/new-uefi-secure-boot-flaw-exposes-systems-to-bootkits-patch-now/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVJwwIXJQd0MIb7N5eVJc0NiaDS9p1PmFD0dmJpCAxfibVuqq8nAlKfkicQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2iczWfib6GrgzGeGiaSWecJUtVEEw1EicbLmcvb6zgPPiaGA7uPQia3Q2MeJEibqebtzSraxJgiald5yMTGAw/640?wx_fmt=png&from=appmsg)

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