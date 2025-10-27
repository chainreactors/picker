---
title: Fortra 修复了关键的 FileCatalyst Workflow 硬编码密码问题
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247577743&idx=1&sn=fd085f9d9b3b676c4b6928efb98ba20a&chksm=e91460b5de63e9a398e839ef98dd6c997d6f2ce056d7d4e9ec2101c2a32995435a0ac485deb9&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-08-31
fetch_date: 2025-10-06T18:05:25.702612
---

# Fortra 修复了关键的 FileCatalyst Workflow 硬编码密码问题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29K0fW3qrFhPG8KI9zEzx5peACCBH8wNvCh1J1wia34H4n4ic0bIWrz58zB8picPkkkaY5OIia59zGeAQ/0?wx_fmt=jpeg)

# Fortra 修复了关键的 FileCatalyst Workflow 硬编码密码问题

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Fortra 称，FileCatalyst Workflow 中存在一个严重的硬编码密码漏洞，攻击者可以利用该漏洞未经授权访问内部数据库，从而窃取数据并获得管理员权限。

任何人都可以使用该硬编码密码远程访问暴露的 FileCatalyst Workflow HyperSQL (HSQLDB) 数据库，从而未经授权访问潜在的敏感信息。

此外，数据库凭据可能会被滥用来创建新的管理员用户，因此攻击者可以获得对 FileCatalyst Workflow 应用程序的管理级访问权限并完全控制系统。

在最近发布的安全公告中，Fortra 表示该问题被跟踪为 CVE-2024-6633（CVSS v3.1：9.8，“严重”），影响 FileCatalyst Workflow 5.1.6 Build 139 及更早版本。建议用户升级到 5.1.7 或更高版本。

Fortra 在公告中指出，HSQLDB 仅用于简化安装过程，并建议用户在安装后设置替代解决方案。因为没有按照建议配置 FileCatalyst Workflow 使用备用数据库的用户很容易受到任何可以到达 HSQLDB 的来源的攻击。暂时还没有缓解措施或解决方法，因此建议系统管理员尽快应用可用的安全更新。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29K0fW3qrFhPG8KI9zEzx5pFpulPk1pvbIT4KzdovibgHM515QFLubVmX8gNoAYIVH4P9PbicwicCgTw/640?wx_fmt=png&from=appmsg)缺陷发现和细节

Tenable 于 2024 年 7 月 1 日发现了 CVE-2024-6633，当时他们在所有 FileCatalyst Workflow 部署中都发现了相同的静态密码“GOSENSGO613”。Tenable 解释说，在产品的默认设置下，可以通过 TCP 端口 4406 远程访问内部 Workflow HSQLDB，因此暴露程度很高。

一旦登录到 HSQLDB，攻击者就可以在数据库中执行恶意操作。例如，攻击者可以在 DOCTERA\_USERS 表中添加管理员级别的用户，从而允许以管理员用户身份访问 Workflow Web 应用程序。

高访问级别、易利用性以及利用 CVE-2024-6633 的网络犯罪分子的潜在收益使得此漏洞对 FileCatalyst Workflow 用户来说极其危险。Tenable 指出，最终用户无法通过常规方式更改此密码，因此升级到 5.1.7 或更高版本是唯一的解决方案。

Fortra 产品因为其中的严重漏洞可能导致多个高价值企业网络同时遭受大规模攻击，因此始终是攻击者的主要目标之一。

参考及来源：https://www.bleepingcomputer.com/news/security/fortra-fixes-critical-filecatalyst-workflow-hardcoded-password-issue/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29K0fW3qrFhPG8KI9zEzx5pIib4dfsBSh8OFfLSNqiaPpWfUkticsFw1Y9h9rGH6vssA5E3Bb2j6mFEw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icEjy5ZrpCcgr4BicXicPv08DSsrgibDcJQpvwkZoO4OqdIpJNhj6TO5xV0ic0AnVf7f2kcPnNevQlTtQ/640?wx_fmt=png)

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