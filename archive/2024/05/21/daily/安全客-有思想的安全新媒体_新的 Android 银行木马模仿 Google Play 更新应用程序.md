---
title: 新的 Android 银行木马模仿 Google Play 更新应用程序
url: https://www.anquanke.com/post/id/296617
source: 安全客-有思想的安全新媒体
date: 2024-05-21
fetch_date: 2025-10-06T16:49:06.602981
---

# 新的 Android 银行木马模仿 Google Play 更新应用程序

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

# 新的 Android 银行木马模仿 Google Play 更新应用程序

阅读量**112758**

发布时间 : 2024-05-20 11:19:52

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.infosecurity-magazine.com/news/android-banking-trojan-google-play/>

译文仅供参考，具体内容表达以及含义原文为准。

威胁情报提供商 Cycble 的研究部门 Cyble 研究与情报实验室 (CRIL) 检测到了一种针对 Android 设备的新银行木马。

在 5 月 16 日发布的一份报告中，CRIL 描述了复杂的恶意软件，其中包含一系列恶意功能，包括覆盖攻击、键盘记录和混淆功能。

研究人员根据其源代码中的一个字符串将该木马称为“Antidot”。

Antidot 木马是什么样子
Antidot 伪装成 Google Play 更新应用程序，在安装时显示伪造的 Google Play 更新页面。

Cyble 观察到，这个虚假的更新页面是用多种语言制作的，包括德语、法语、西班牙语、俄语、葡萄牙语、罗马尼亚语和英语。这表明该恶意软件针对的是不同地区的 Android 用户。

![Antidot 的虚假更新页面以不同语言制作。来源：Cyble]()
Antidot 的虚假更新页面以不同语言制作。来源：Cyble
在虚假更新页面上，“继续”按钮会将用户重定向到 Android 设备的辅助功能设置。

一旦用户授予服务的可访问性，恶意软​​件就会向服务器发送第一条“ping 消息”以及 Base64 编码数据，其中包含以下内容：

* 恶意软件应用程序名称
* 软件开发套件（SDK）版本
* 手机型号
* 手机制造商
* 语言和国家代码
* 已安装的应用程序包列表
* 解码 Antidot 的功能

在后台，恶意软件启动与其命令和控制 (C2) 服务器“hxxp://46[.]228.205.159:5055/”的通信。

除了HTTP连接之外，木马还使用socket.io库建立WebSocket通信，从而实现服务器和客户端之间的实时、双向通信。

恶意软件通过“ping”和“pong”消息维持服务器与其客户端之间的通信。

一旦服务器生成了僵尸程序 ID，Antidot 银行木马就会向服务器发送僵尸程序统计信息并接收命令。该恶意软件总共执行了 35 个命令，包括收集 SMS 消息、发起 USSD 请求，甚至远程控制相机和屏幕锁定等设备功能。

该恶意软件包含多种功能，使其能够部署一系列恶意活动，包括：

* 虚拟网络计算 (VNC)
* 键盘记录
* 叠加攻击
* 屏幕录制
* 呼叫转移
* 收集联系人和短信
* 执行 USSD 请求
* 锁定和解锁设备

Cyble 研究人员写道：“Antidot 对字符串混淆、加密和虚假更新页面的战略部署的利用表明了一种有针对性的方法，旨在逃避检测并最大限度地扩大其在不同语言区域的影响力。”

针对 Android 银行木马的 Cyble 缓解建议
减轻这种威胁的一些建议包括：

* 仅安装来自官方应用商店的软件，例如 Google Play Store（Android 手机）或 Apple App Store（iOS 手机）
* 使用知名的防病毒和互联网安全软件包
* 尽可能使用强密码并强制执行多重身份验证 (MFA)
* 打开通过短信或发送到您的移动设备的电子邮件收到的链接时要小心
* 始终在 Android 设备上启用 Google Play Protect
* 警惕授予应用程序的任何权限
* 使设备、操作系统和应用程序保持最新

本文翻译自 [原文链接](https://www.infosecurity-magazine.com/news/android-banking-trojan-google-play/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296617](/post/id/296617)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.infosecurity-magazine.com/news/android-banking-trojan-google-play/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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