---
title: SteganoAmor：超过300家公司差点陷入复杂的“爱情陷阱”
url: https://www.anquanke.com/post/id/295699
source: 安全客-有思想的安全新媒体
date: 2024-04-18
fetch_date: 2025-10-04T12:14:35.613612
---

# SteganoAmor：超过300家公司差点陷入复杂的“爱情陷阱”

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

# SteganoAmor：超过300家公司差点陷入复杂的“爱情陷阱”

阅读量**114680**

发布时间 : 2024-04-17 11:12:23

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.securitylab.ru/news/547521.php>

译文仅供参考，具体内容表达以及含义原文为准。

TA558 网络犯罪组织最近显着增加了其恶意活动，使用各种类型的恶意软件攻击世界各地的组织。Positive Technologies 安全中心的专家发现 该组织实施了 320 多次攻击。

 TA558 组织使用复杂的感染链，包括 AgentTesla、FormBook、Remcos 等工具。这些黑客攻击的一个显着特征是使用隐写术——将恶意代码隐藏在图像和文本文件中。

 这些攻击从包含利用 CVE-2017-11882 漏洞的 Microsoft Office 文档的网络钓鱼电子邮件开始。 该安全漏洞已于 2017 年修复，但由于存在大量未更新的 Microsoft Office 副本，它仍然是黑客的热门目标。

 如果计算机上安装了过时版本的 Microsoft Office，该漏洞利用程序会下载 Visual Basic 脚本，该脚本又会下载嵌入恶意代码的图像。接下来，使用 PowerShell 从该图像中提取最终的恶意负载并执行。

 值得注意的是，攻击中使用的文件和脚本往往具有与爱情主题相关的名称，例如“greatloverstory.vbs”、“easytolove.vbs”甚至“iaminlovewithsomeoneshecuteandtrulyyoungunluckyshenotundersatnd\_howmuchiloveherbutitsallgreatwithtrueloveriamgivingyou.doc”。这就是研究人员将该活动命名为“SteganoAmor”的原因。

 攻击者经常使用 Google Drive 等合法云服务来存储恶意文件，这有助于他们避免被防病毒工具检测到。被盗信息的传输是通过受损的合法 FTP 和 SMTP 服务器进行的，这使得流量不那么可疑。

 分析显示，网络犯罪分子的主要目标是来自拉丁美洲的组织，尽管北美和西欧也有攻击记录。受影响者包括各个经济部门的代表，包括政府机构和私营公司。

 在所检查的一个案例中，攻击者发送了一封带有恶意附件的电子邮件，并将其伪装成 Excel 文档。通过打开该文件，用户会无意中运行一个宏来下载并执行 AgentTesla 恶意软件。该程序能够从浏览器、电子邮件客户端和远程访问系统窃取数据。

鉴于使用合法服务器来分发网络钓鱼和操作 C2 服务器，专家强烈建议组织仔细检查带有附件的电子邮件，即使它们来自知名组织或政府组织。

SteganoAmor 活动表明网络威胁正变得更加复杂且难以检测。定期更新防病毒程序并进行安全审核以及时识别和消除潜在威胁非常重要。

本文翻译自 [原文链接](https://www.securitylab.ru/news/547521.php)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295699](/post/id/295699)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.securitylab.ru/news/547521.php>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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