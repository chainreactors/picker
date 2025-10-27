---
title: Palo Alto Networks 警告公众利用防火墙劫持漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247578576&idx=1&sn=af22a7aa77dc9421a9f89d19b22a0e46&chksm=e91463eade63eafc5d2d910ffeb0b54892bb97f09d19f2dbd1be6ccbf95470ea7a7d6ed16af4&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-10-23
fetch_date: 2025-10-06T18:52:56.167647
---

# Palo Alto Networks 警告公众利用防火墙劫持漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibt63gegQV5CLnQPGtqIa1AdRdMIkUcVlibuoU6hLmq2G4ibicib2M6XhbBEtxu9ibWJ1gNZLhXoiaLB61g/0?wx_fmt=jpeg)

# Palo Alto Networks 警告公众利用防火墙劫持漏洞

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Palo Alto Networks 近期提醒客户尽快修补安全漏洞（使用公开的漏洞利用代码），因为这些漏洞可以被链接起来让攻击者劫持 PAN-OS 防火墙。

这些漏洞是在 Palo Alto Networks 的 Expedition 解决方案中发现的，该解决方案有助于从其他 Checkpoint、Cisco 或支持的供应商迁移配置。它们可以被用来访问敏感数据，例如用户凭据，这可以帮助接管防火墙管理员帐户。

该公司在发布的一份公告中表示，“Palo Alto Networks Expedition 中的多个漏洞允许攻击者读取 Expedition 数据库内容和任意文件，以及将任意文件写入 Expedition 系统上的临时存储位置。综合起来，这些信息包括用户名、明文密码、设备配置和 PAN-OS 防火墙的设备 API 密钥等信息。”

这些错误是命令注入、反射跨站脚本 (XSS)、敏感信息的明文存储、缺少身份验证和 SQL 注入漏洞的组合：

**·**CVE-2024-9463（未经身份验证的命令注入漏洞）

**·**CVE-2024-9464（经过身份验证的命令注入漏洞）

**·**CVE-2024-9465（未经身份验证的 SQL 注入漏洞）

**·**CVE-2024-9466（存储在日志中的明文凭据）

**·**CVE-2024-9467 （未经身份验证的反映XSS漏洞）

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibt63gegQV5CLnQPGtqIa1AuHkg7OjqmgA2v9LU04NyofqdpNb4ectfok1jiawPVrI8SDcjbfYc1Ew/640?wx_fmt=png&from=appmsg)可用的概念验证漏洞

Horizon3.ai 漏洞研究员 Zach Hanley 发现并报告了其中四个漏洞，他还发布了一份根本原因分析文章，详细介绍了他在研究 CVE-2024-5910 漏洞，这允许攻击者重置 Expedition 应用程序管理员凭据。

Hanley 还发布了一个概念验证漏洞，该漏洞将 CVE-2024-5910 管理员重置漏洞与 CVE-2024-9464 命令注入漏洞链接起来，以在易受攻击的 Expedition 服务器上获得“未经身份验证”的任意命令执行。

Palo Alto Networks 表示，目前没有证据表明这些安全漏洞已被利用在攻击中。

Expedition 1.2.96 以及所有更高版本的 Expedition 中都提供了对所有列出问题的修复。受 CVE-2024-9466 影响的明文文件将在升级过程中自动删除。升级到 Expedition 的固定版本后，所有 Expedition 用户名、密码和 API 密钥都应轮换。

Expedition 处理的所有防火墙用户名、密码和 API 密钥应在更新后轮换。

无法立即部署当前安全更新的用户必须将 Expedition 网络访问限制为授权用户、主机或网络。4 月份，该公司开始发布针对最严重的零日漏洞的修补程序，自 3 月份以来，该漏洞一直被追踪为 UTA0218 的国家支持的威胁者积极利用，以在 PAN-OS 防火墙中设置后门。

参考及来源：https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-firewall-hijack-bugs-with-public-exploit/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibt63gegQV5CLnQPGtqIa1AeB3icwmQMGsRTgxcPdyCxmZPMfHWZCgUsCcdHKfb7JLAMu2K8ZQ1nvQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibt63gegQV5CLnQPGtqIa1AfoUKiaiblwCcEQLmCvianNYemvlJ2nFTbxEBgR5TopKqjTyFdMMPOEibYQ/640?wx_fmt=png&from=appmsg)

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