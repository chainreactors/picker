---
title: 黑客利用 React2Shell 漏洞入侵了 700 多台 Next.js 服务器
url: https://mp.weixin.qq.com/s/FLJ69EfeBYuFCV5UxwbGVQ
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:12:03.451738
---

# 黑客利用 React2Shell 漏洞入侵了 700 多台 Next.js 服务器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7MvxQE1S9joEXefcd4an8Smw69OqicyNgG4ibaygUtrIaH07yFU6dvTiba87fxFUp4790jClhX1Os55Riav2jK4yBlHyCV6icPYQNo0/0?wx_fmt=jpeg)

# 黑客利用 React2Shell 漏洞入侵了 700 多台 Next.js 服务器

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

一场大规模的自动化凭证窃取活动正在全球范围内积极攻击网络应用程序。思科Talos网络安全研究人员发现，一个名为UAT-10608的黑客组织正在实施一项行动，该组织已入侵超过700台服务器。

攻击者正在利用名为 React2Shell 的严重安全漏洞来获取访问权限并窃取高度敏感的数据。黑客专门针对易受CVE-2025-55182（即 React2Shell）漏洞影响的 Next.js 应用程序。

这是 React 服务器组件中一个严重的远程代码执行漏洞。它允许攻击者向存在漏洞的服务器发送特制的 Web 请求。

由于服务器未能正确检查传入数据，因此会执行攻击者隐藏的命令。更糟糕的是，这种攻击无需密码或用户交互。

## **700 多个 Next.js 主机被利用**

UAT-10608 组织使用自动化工具扫描互联网，寻找存在漏洞的 Next.js 服务器。一旦找到目标，他们就会启动React2Shell 漏洞利用程序来获取初始访问权限。该漏洞利用程序随后会将恶意脚本下载到服务器上。

该脚本在后台静默运行，就像一台数字吸尘器。它会搜索服务器的文件、云设置和系统内存，以收集有价值的凭证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7OFVCN5MWdMibdDZZbiaEFAlGwgqWkIvSg78xoNOw2eggPmLVMMXAU8hdj4CTGvQTtlcnWKFTrQMh1HwMDJbZOFD5ttMGyFP7Z0A/640?wx_fmt=png&from=appmsg)

该脚本分多个阶段运行，提取从云令牌到数据库密码的所有信息，然后将窃取的数据发送回黑客的命令和控制服务器。

为了管理海量被盗信息，攻击者使用了一个名为“NEXUS Listener”的自定义网络控制面板。思科Talos的研究人员发现，仅在24小时内，该控制面板就记录了766台被入侵的主机。

仪表盘揭示了盗窃案令人震惊的规模：

* 超过 90% 的主机数据库凭证被盗。
* 近 80% 的用户丢失了用于安全访问服务器的私钥。
* 黑客还窃取了 AWS 云凭证、Stripe 实时支付密钥和 GitHub 访问令牌。

这次攻击的后果不堪设想。黑客利用被盗的数据库密码，可以访问用户的私人信息和财务记录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7O6FQlgv4wAibxD5kME3w3uG0WRia17ib0rA8UCj6GDvUp8ia40fY01wLkagXMY2NvKt6GSPM4p81eOnXp8K04zGb6R8npo7kZzjh4/640?wx_fmt=png&from=appmsg)

暴露的 SSH 密钥使他们能够在公司网络内的不同服务器之间自由移动。

此外，被盗的云凭证使攻击者能够接管整个云环境，而 泄露的GitHub 令牌可用于将恶意代码插入合法的软件更新中。

使用 Next.js 的公司必须立即采取行动保护自身安全。各组织应尽快更新其Web 应用程序，以修复 React2Shell 漏洞。

此外，任何可能成为攻击目标的公司都应立即更改其所有密码、API 密钥和安全令牌。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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