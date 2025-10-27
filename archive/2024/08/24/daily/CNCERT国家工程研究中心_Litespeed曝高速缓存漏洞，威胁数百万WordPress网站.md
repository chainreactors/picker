---
title: Litespeed曝高速缓存漏洞，威胁数百万WordPress网站
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546571&idx=1&sn=995ff830fdcb2120e3e322525d780f14&chksm=fa93800acde4091c521d46f7f1793ddc7234c48d18396f323ed7d30a93f0c094bf2dd84fefc7&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-24
fetch_date: 2025-10-06T18:05:37.638513
---

# Litespeed曝高速缓存漏洞，威胁数百万WordPress网站

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mxzrSiaf7o2PBUQUCuN4LWos3Gblwm0GhlIprswHGovv0CQXptQzhLrNAUBGibkmbXVBiaS5iaicDfojQ/0?wx_fmt=jpeg)

# Litespeed曝高速缓存漏洞，威胁数百万WordPress网站

网络安全应急技术国家工程中心

近日，有研究人员在插件的用户模拟功能中发现了未经身份验证的权限升级漏洞 (CVE-2024-28000)，该漏洞是由 LiteSpeed Cache 6.3.0.1 及以下版本中的弱散列检查引起的。这个漏洞可能会让攻击者在创建恶意管理员账户后接管数百万个网站。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39JWkgKTqMmZIuwHGu9Kv8h8AxzzrfBIJmEJFRkgh8zflKYOot9W1zFgic3jZK88ibwI9mUKVkVSloQ/640?wx_fmt=jpeg&from=appmsg&wxfrom=13&tp=wxpic)

LiteSpeed Cache 是开源的，也是最流行的 WordPress 网站加速插件，拥有超过 500 万的活跃安装量，支持 WooCommerce、bbPress、ClassicPress 和 Yoast SEO。

本月初，安全研究员John Blackbourn向Patchstack的漏洞悬赏计划提交了该漏洞。LiteSpeed团队开发了补丁，并在 8月13日发布的LiteSpeed Cache 6.4版本中一并提供。

一旦有攻击者成功利用该漏洞，任何未经身份验证的访问者都可以获得管理员级别的访问权限，从而通过安装恶意插件、更改关键设置、将流量重定向到恶意网站、向访问者分发恶意软件或窃取用户数据等方式，从而完全控制运行易受攻击的 LiteSpeed Cache 版本的网站。

Patchstack 安全研究员Rafie Muhammad本周三（9月21日）解释称：目前我们能够确定，暴力攻击会遍历安全散列的所有 100 万个已知可能值，并将它们传递到 litespeed\_hash cookie 中，即使以相对较低的每秒 3 个请求的速度运行，也能在几小时到一周内以任何给定用户 ID 的身份访问网站。

唯一的先决条件是需要知道管理员级用户的 ID，并将其输入 litespeed\_role cookie。确定这样一个用户的难度完全取决于目标网站，在许多情况下，用户 ID 为 1 就能成功。

虽然开发团队在上周发布了解决这一关键安全漏洞的版本，但根据 WordPress 官方插件库的下载统计显示，该插件的下载次数仅略高于 250 万次，这可能导致一半以上使用该插件的网站受到攻击。

今年早些时候，攻击者利用 LiteSpeed Cache 的一个未经验证的跨站脚本漏洞（CVE-2023-40000）创建了恶意管理员用户，并获得了对脆弱网站的控制权。

今年 5 月，Automattic 的安全团队 WPScan 曾发布警告称，威胁者在看到来自一个恶意 IP 地址的 120 多万次探测后曾在4月对目标进行了大量扫描。

他们强烈建议用户尽快用最新的 Litespeed Cache 补丁版本更新自己的网站。Wordfence威胁情报主管Chloe Chamberland今天也警告称：这个漏洞被利用的风险性极高。

今年 6 月，Wordfence 威胁情报团队还报告称，一名威胁行为者在 WordPress.org 上至少后门了五个插件，并添加了恶意 PHP 脚本，以便在运行这些插件的网站上创建具有管理员权限的账户。

**参考资料：**

https://www.bleepingcomputer.com/news/security/litespeed-cache-bug-exposes-millions-of-wordpress-sites-to-takeover-attacks/

原文来源：FreeBuf

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