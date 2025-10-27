---
title: Bing 广告冒充 NordVPN 旨在传播 SecTopRAT 恶意软件
url: https://www.anquanke.com/post/id/295379
source: 安全客-有思想的安全新媒体
date: 2024-04-09
fetch_date: 2025-10-04T12:15:03.339254
---

# Bing 广告冒充 NordVPN 旨在传播 SecTopRAT 恶意软件

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

# Bing 广告冒充 NordVPN 旨在传播 SecTopRAT 恶意软件

阅读量**128232**

|评论**1**

发布时间 : 2024-04-08 11:16:04

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.scmagazine.com/news/bing-ad-posing-as-nordvpn-aims-to-spread-sectoprat-malware>

译文仅供参考，具体内容表达以及含义原文为准。

人们发现，一则看似安装 NordVPN 链接的 Bing 广告会指向远程访问木马 SecTopRAT 的安装程序。

Malwarebytes Labs于周四发现了这一恶意广告活动，用于恶意广告的域名是在一天前创建的。 URL (nordivpn[.]xyz) 的设计看起来像合法的 NordVPN 域。广告链接重定向到另一个带有误植 URL 的网站 (besthord-vpn[.]com) 和真实 NordVPN 网站的副本。

欺诈网站上的下载按钮会导致包含安装程序 NordVPNSetup.exe 的 Dropbox。该可执行文件包括真正的 NordVPN 安装程序和恶意软件负载，该负载被注入 MSBuild.exe 并连接到攻击者的命令和控制 (C2) 服务器。

威胁行为者尝试对恶意可执行文件进行数字签名，但发现签名无效。然而，Malwarebytes ThreatDown 实验室的首席威胁研究员 Jérôme Segura 周五告诉 SC Media，他后来发现该可执行文件具有有效的代码签名证书。

Segura 表示，一些安全产品可能会因其无效签名而阻止可执行文件，但是，“也许更好的规避技术是动态进程注入，将恶意代码注入到合法的 Windows 应用程序中。”

“最后，我们应该注意到，该文件包含 NordVPN 的安装程序，这很可能会阻止整个可执行文件的检测，”Segura 补充道。

恶意负载 SecTopRAT，也称为 ArechClient，是一种远程访问木马 (RAT)，[最初](https://x.com/malwrhunterteam/status/1195288774957244416)由 MalwareHunterTeam 于 2019 年 11 月发现，不久后由 G DATA 的研究人员进行分析。研究人员发现，RAT 创建了一个“隐形”的第二个桌面，使攻击者能够控制受害者系统上的浏览器会话。

SecTopRAT还能够向攻击者的C2服务器发送系统信息，例如系统名称、用户名和硬件信息。

Malwarebytes 向拥有 Bing 的微软和 Dropbox 报告了该恶意软件活动。 Dropbox 此后删除了存储恶意软件的帐户，Segura 表示，截至周五，他的团队尚未收到微软的回复。

“我们确实注意到威胁行为者昨晚更新了他们的基础设施，也许是对我们的报告的反应。他们现在将受害者重定向到一个新的域名 theordvpn[.]info ，这可能表明恶意广告活动仍然活跃，可能是在另一个广告商身份下，”Segura 说。

过去曾发现过其他传播 SecTopRAT 的恶意广告活动。 2021 年，Ars Technica 报道了一场利用 Google 广告宣传 Brave 浏览器的活动。

去年 10 月，威胁行为者结合使用恶意广告、搜索引擎优化 (SEO) 中毒和被破坏的网站来诱骗用户安装包含GHOSTPULSE 恶意软件加载程序的虚假 MSIX Windows 应用程序包。安装后，GHOSTPULSE 使用进程分身来促进多种恶意软件的执行，包括 SecTopRAT。

本文翻译自 [原文链接](https://www.scmagazine.com/news/bing-ad-posing-as-nordvpn-aims-to-spread-sectoprat-malware)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295379](/post/id/295379)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.scmagazine.com/news/bing-ad-posing-as-nordvpn-aims-to-spread-sectoprat-malware>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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