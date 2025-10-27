---
title: Litespeed Cache 漏洞导致数百万 WordPress 网站遭受接管攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247577691&idx=2&sn=8d5b89fd888317e60e720a84a091937d&chksm=e9146061de63e97744313abc7ee0b3d3c84ad30fc1f925a8ab1d2742cb0a38b49c693c0f24be&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-08-28
fetch_date: 2025-10-06T18:04:53.401411
---

# Litespeed Cache 漏洞导致数百万 WordPress 网站遭受接管攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29nMlzGib3DpdrAEZmYA0vZrkSYbZNtPx4QgD6JF7hl1tLSV1ian7G2IiaBzkwoALERy8PyFicZEwgaQA/0?wx_fmt=jpeg)

# Litespeed Cache 漏洞导致数百万 WordPress 网站遭受接管攻击

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

LiteSpeed Cache 是开源的，也是极受欢迎的 WordPress 网站加速插件，拥有超过 500 万个活跃安装，并支持 WooCommerce、bbPress、ClassicPress 和 Yoast SEO。

该插件的用户模拟功能中发现了未经身份验证的权限提升漏洞 (CVE-2024-28000)，该漏洞是由 LiteSpeed Cache 6.3.0.1 版及之前的版本中的弱哈希校验引起的。

安全研究员于 8 月 1 日向 Patchstack 的漏洞赏金计划提交了这个漏洞。LiteSpeed 团队开发了一个补丁，并将其与 8 月 13 日发布的 LiteSpeed Cache 6.4 版一起发布。

成功利用该漏洞可使任何未经身份验证的访问者获得管理员级别的访问权限，通过安装恶意插件、更改关键设置、将流量重定向到恶意网站、向访问者分发恶意软件或窃取用户数据，可以完全接管运行易受攻击的 LiteSpeed Cache 版本的网站。

Patchstack 安全研究员解释说：“暴力攻击会迭代安全哈希的所有 100 万个已知可能值并将它们传递到 litespeed\_hash cookie 中，即使以每秒 3 个请求的相对较低速度运行，也能够在几小时到一个星期内以任何给定的用户 ID 访问该网站。”

唯一的先决条件是知道管理员级别用户的 ID 并将其传递到 litespeed\_role cookie 中。

确定此类用户的难度完全取决于目标站点，并且在许多情况下，使用用户 ID 1 即可成功。

虽然开发团队已于上上周发布了修复此严重安全漏洞的版本，但 WordPress 官方插件库的下载统计数据显示，该插件的下载次数仅为 250 多万次，这意味着超过一半使用该插件的网站可能面临攻击。

今年早些时候，攻击者利用 LiteSpeed Cache 未经身份验证的跨站点脚本漏洞 (CVE-2023-40000) 创建恶意管理员用户并控制易受攻击的网站。

5 月，Automattic 的安全团队 WPScan 警告称，威胁分子在 4 月份开始扫描目标，因为他们发现仅一个恶意 IP 地址就发起了超过 120 万次探测。

Wordfence 威胁情报负责人也强烈建议用户尽快使用 Litespeed Cache 的最新修补版本（撰写本文时为 6.4.1 版）更新其网站。由此可推断，这个漏洞很快就会被积极利用。

6 月，Wordfence 威胁情报团队还报告称，一个威胁分子在 WordPress.org 上至少植入了五个插件后门，并添加了恶意 PHP 脚本，以在运行这些插件的网站上创建具有管理员权限的帐户。

参考及来源：https://www.bleepingcomputer.com/news/security/litespeed-cache-bug-exposes-millions-of-wordpress-sites-to-takeover-attacks/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29nMlzGib3DpdrAEZmYA0vZrQ2STsnnlgfl0yVBCjEicaP4libXMQseicB64d82c1uS3GSy5Y4x8MNiaPA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29nMlzGib3DpdrAEZmYA0vZrURmEY1tWibVrASZVNepR8D5Iau8687NgicCbojdOiaz6KfoSZjpHYsYEQ/640?wx_fmt=png&from=appmsg)

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