---
title: Windows Defender 绕过工具在 GitHub 上分享
url: https://www.anquanke.com/post/id/296923
source: 安全客-有思想的安全新媒体
date: 2024-05-31
fetch_date: 2025-10-06T16:49:30.868256
---

# Windows Defender 绕过工具在 GitHub 上分享

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Windows Defender 绕过工具在 GitHub 上分享

阅读量**150608**

发布时间 : 2024-05-30 10:47:06

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/windows-defender-bypass-tool-github/>

译文仅供参考，具体内容表达以及含义原文为准。

一个禁用 Windows Defender 和防火墙的 GitHub 项目在网络安全研究人员中引起了轰动。

CERT 高级漏洞分析师 Will Dormann在 Mastodon 网络安全实例上发布了有关 GitHub 项目的文章。

Dormann 写道：“有人发现了第三方 AV 用来禁用 Microsoft Defender 的秘密技术，这样它们就可以不受干扰地运行。这个工具使用这种技术来安装一个空 AV 产品，从而达到简单地禁用 Microsoft Defender 的效果。”

Dormann 提供了该工具运行的屏幕录像，看来它运行有效（下面的截图）。

![“无防御者”Windows Defender 绕过 GitHub]()
“无防御者”Windows Defender 绕过
这个 GitHub 项目简称为“ No Defender ”，号称是“一种禁用 Windows Defender + 防火墙的有趣方式”。

在项目说明中，存储库所有者“es3n1n”表示，他们基本上对防病毒供应商用来禁用 Windows Defender 的 API 进行了逆向工程。

该说明指出：“Windows 中有一个 WSC（Windows安全中心）服务，防病毒软件会使用该服务让 Windows 知道系统中还有其他防病毒软件，并且应该禁用 Windows Defender。”

“这个 WSC API 没有文档记录，而且需要人们与 Microsoft 签署保密协议才能获得其文档，因此我决定采取一种有趣的方法，并使用了一款名为 Avast 的现有防病毒软件。这款 AV 引擎包含一个所谓的 wsc\_proxy.exe 服务，它本质上为 Avast 设置了 WSC API。通过一点逆向工程，我将这项服务变成了一项可以添加我自己的内容的服务。”

es3n1n 指出的一个限制是“为了在重启后保留 WSC 内容，no-defender 会将自身（不是真正的自身，而是 Avast 的模块）添加到自动运行中。因此，您需要将 no-defender 二进制文件保留在磁盘上。”

### 绕过 Windows Defender 需要管理员权限

EDR（端点检测和响应）和防病毒软件绕过并不罕见，因为黑客和研究人员都找到了禁用安全防御的方法。

安全研究人员和测试人员经常在研究和测试过程中关闭安全防御，因此此类工具也有合法用途。正如一位评论者在 ycombinator Hacker News feed上指出的那样，“Defender 在进行安全研究时真的很烦人，而且几乎不可能完全永久关闭。即使使用组策略编辑器或 regedits 也不可靠。即使您确实让它停止，几周后它也会随机重新启用……对于绝大多数人来说，这是一件好事！”

Dormann 指出，只需提升管理员权限即可运行 No Defender 工具，因此 Windows 用户还有另一个理由不以管理员身份运行 Windows。“如果您不像我们这些注重安全的人那样以管理员身份登录 Windows，那么您就不必担心那么多，”Dormann 写道。

一位 Mastodon 评论员认为 GitHub 工具是 Avast 而非微软的漏洞，并指出“它需要用 AuthentiCode SigningLevel 7 签名的可执行文件（“由产品使用 AMPPL 的反恶意软件供应商签名”）。

“我认为这更像是 Avast wsc\_proxy.exe 组件的一个漏洞，它被滥用，允许不受信任/未签名的代码与其进行交互，”这位网名是“faebudo”的评论者说道。

Dormann 评论这个问题“更像是一种新奇事物，而不是漏洞本身。具有管理员权限的用户可以执行管理员操作。其中包括重新配置他们所在的系统。包括内核级访问。”

本文翻译自 [原文链接](https://thecyberexpress.com/windows-defender-bypass-tool-github/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296923](/post/id/296923)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/windows-defender-bypass-tool-github/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)