---
title: ShrinkLocker：新勒索软件使用 windows系统安全工具BitLocker实施攻击
url: https://www.anquanke.com/post/id/296756
source: 安全客-有思想的安全新媒体
date: 2024-05-25
fetch_date: 2025-10-06T17:17:25.405638
---

# ShrinkLocker：新勒索软件使用 windows系统安全工具BitLocker实施攻击

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

# ShrinkLocker：新勒索软件使用 windows系统安全工具BitLocker实施攻击

阅读量**106407**

发布时间 : 2024-05-24 10:38:52

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.securitylab.ru/news/548533.php>

译文仅供参考，具体内容表达以及含义原文为准。

合法的 Windows 安全功能已成为黑客的工具。

卡巴斯基实验室专家 已发现 使用BitLocker的新型 ShrinkLocker 勒索软件对企业设备发起的攻击。 BitLocker 是 Windows 中的一项安全功能，允许您使用加密来保护您的数据。攻击的目标是工业和制药公司以及政府机构。

攻击者用 VBScript 创建了一个恶意脚本。此脚本检查设备上安装的 Windows 版本并相应地激活 BitLocker 功能。 ShrinkLocker 可以感染新版和旧版操作系统，最高可达 Windows Server 2008。

该脚本修改操作系统启动参数，然后尝试使用 BitLocker 加密硬盘分区。将创建一个新的启动分区，以便您稍后可以启动加密的计算机。攻击者还删除了用于保护 BitLocker 加密密钥的安全工具，以便用户以后无法恢复它们。

接下来，恶意脚本将有关系统的信息以及受感染计算机上生成的加密密钥发送到攻击者的服务器。然后它会“掩盖其踪迹”：它会删除有助于调查攻击的日志和各种文件。

在最后阶段，ShrinkLocker 强制阻止对系统的访问。受害者在屏幕上看到一条消息：“您的计算机上没有 BitLocker 恢复选项。”

![]()
卡巴斯基专家建议公司使用强密码、安全存储 BitLocker 密钥、备份数据并实施早期威胁检测和事件调查解决方案。

本文翻译自 [原文链接](https://www.securitylab.ru/news/548533.php)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296756](/post/id/296756)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.securitylab.ru/news/548533.php>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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