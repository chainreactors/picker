---
title: 黑客瞄准 15 万个网站使用的 WordPress 日历插件
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545885&idx=3&sn=7e310cc888afb3a72f90affc44e6ecbd&chksm=fa9382dccde40bca60535f8526f4504121463fad6c6d7d9d214126c4a23e37ffd72752cccbee&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-18
fetch_date: 2025-10-06T17:45:33.620463
---

# 黑客瞄准 15 万个网站使用的 WordPress 日历插件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kHZv8Syx1fHtL2DPGWCEticuK88zJib7ddyBVMsicstf7raVzqAZWbwmdmYtlbLw8dwceXK9jA1Tm4Q/0?wx_fmt=jpeg)

# 黑客瞄准 15 万个网站使用的 WordPress 日历插件

网络安全应急技术国家工程中心

研究发现，黑客正试图利用现代事件日历 WordPress 插件中的漏洞（该漏洞存在于超过 150,000 个网站上），将任意文件上传到易受攻击的站点并远程执行代码。

该插件由 Webnus 开发，用于组织和管理现场、虚拟或混合活动。

攻击中利用的漏洞被标识为 CVE-2024-5441，并获得了高严重性评分（CVSS v3.1：8.8）。该漏洞由 Friderika Baranyai 于 5 月 20 日在 Wordfence 的 Bug Bounty Extravaganza 期间发现并报告。

在一份描述安全问题的报告中，Wordfence 表示，安全问题源于插件的“set\_featured\_image”函数缺乏文件类型验证，该函数用于上传和设置事件的特色图片。

该函数获取图像 URL 和帖子 ID，尝试获取附件 ID，如果未找到，则使用 get\_web\_page 函数下载图像。

它使用 wp\_remote\_get 或 file\_get\_contents 检索图像，并使用 file\_put\_contents 函数将其保存到 WordPress 上传目录。

现代事件日历版本（直至 7.11.0）不检查上传的图像文件中扩展名的文件类型，允许上传任何文件类型，包括有风险的 .PHP 文件。

一旦上传，这些文件就可以被访问和执行，从而可以在服务器上执行远程代码，并可能导致完全的网站接管。

任何经过身份验证的用户（包括订阅者和任何注册会员）均可利用 CVE-2024-5441。如果插件设置为允许非会员（没有帐户的访问者）提交事件，则无需身份验证即可利用 CVE-2024-5441。

Webnus 近日发布了现代事件日历 7.12.0 版本修复了该漏洞，可有效避免网络攻击风险的推荐升级。

然而，Wordfence 报告称，黑客已试图利用该问题进行攻击，并在 24 小时内阻止了 100 多次攻击尝试。

鉴于正在进行的攻击活动，现代事件日历和现代事件日历精简版（免费版）的用户应尽快升级到最新版本或禁用该插件，直到他们可以执行更新。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/hackers-target-wordpress-calendar-plugin-used-by-150-000-sites/

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