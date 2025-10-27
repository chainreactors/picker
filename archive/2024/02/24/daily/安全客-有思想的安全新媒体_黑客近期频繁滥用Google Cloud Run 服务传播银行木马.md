---
title: 黑客近期频繁滥用Google Cloud Run 服务传播银行木马
url: https://www.anquanke.com/post/id/293389
source: 安全客-有思想的安全新媒体
date: 2024-02-24
fetch_date: 2025-10-04T12:05:51.559950
---

# 黑客近期频繁滥用Google Cloud Run 服务传播银行木马

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

# 黑客近期频繁滥用Google Cloud Run 服务传播银行木马

阅读量**130740**

发布时间 : 2024-02-23 10:30:42

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

分析师警告称，黑客最近开始频繁滥用Google Cloud Run 服务，大规模传播 Astaroth、Mekotio 和 Ousaban 等银行木马。

Google Cloud Run允许用户部署前端和后端服务、网站或应用程序以及处理负载。无需管理基础设施和扩展。

思科 Talos 的研究人员 注意到，从 2023 年 9 月开始，攻击者使用 Google 服务传播恶意软件的情况急剧增加。随后，巴西黑客发起了 MSI 安装程序活动来传播恶意负载。

专家表示，Google Cloud Run 因其成本效益和绕过标准安全措施的能力，已成为对网络犯罪分子有吸引力的平台。

**攻击机制**

攻击首先向潜在受害者发送网络钓鱼电子邮件。这些信件经过精心制作，与官方银行支票、财务报表或政府通知没有什么不同。

研究人员表示，大多数电子邮件都是西班牙语，因为它们是针对拉丁美洲的。但它们也有意大利语版本。这些电子邮件包含将受害者重定向到 Google Cloud Run 上托管的恶意网络服务的链接。

在某些情况下，恶意软件是通过 MSI 文件传播的。在其他情况下，该服务会发出 302 重定向到 Google Cloud Storage，其中包含带有恶意 MSI 的 ZIP 存档。

当 MSI 文件启动时，会下载并安装新的特洛伊木马组件。第二阶段交付是使用合法的 Windows 工具 BITSAdmin 进行的。

最后，该程序通过将 LNK 文件添加到启动文件夹来在受害者的系统上建立永久存在。它们被配置为运行执行恶意脚本的 PowerShell 命令。

**恶意软件详细信息**

该活动以三种银行木马为特色：Astaroth/Guildma、Mekotio 和 Ousaban。每一个都旨在秘密侵入系统、建立持久存在并窃取敏感信息以渗透受害者的银行账户。

Astaroth 使用先进技术来逃避检测。它最初针对巴西，现在攻击 15 个拉丁美洲国家的 300 多家金融机构。最近，该木马开始收集数据以访问加密货币交换服务。

通过按键拦截、屏幕捕获和剪贴板捕获，Astaroth 不仅窃取机密数据，还监控互联网流量以窃取银行帐户的登录名和密码。

Mekotio 也已活跃多年，目标瞄准拉丁美洲。它侵入银行账户并进行非法交易。该恶意软件经常使用网络钓鱼链接来欺骗用户。

Ousaban 特洛伊木马还使用网络钓鱼和利用虚假银行门户侵入帐户。Cisco Talos 指出，Ousaban 是在 Astaroth 攻击的后期阶段交付的。这意味着这些程序的运营者可能是相关的，也可能是同一个人。

谷歌代表感谢研究人员的工作，并承诺加强安全措施：“我们已经删除了可疑链接，并正在探索加强安全性的选项，以防止未来出现类似的恶意活动。”

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293389](/post/id/293389)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**5赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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