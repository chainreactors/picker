---
title: PupkinStealer：小型恶意软件，通过 Telegram 机器人实施大规模盗窃
url: https://www.anquanke.com/post/id/307336
source: 安全客-有思想的安全新媒体
date: 2025-05-14
fetch_date: 2025-10-06T22:23:21.607022
---

# PupkinStealer：小型恶意软件，通过 Telegram 机器人实施大规模盗窃

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

# PupkinStealer：小型恶意软件，通过 Telegram 机器人实施大规模盗窃

阅读量**59395**

发布时间 : 2025-05-13 15:35:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/pupkinstealer-tiny-malware-big-theft-via-telegram-bot-exposed/>

译文仅供参考，具体内容表达以及含义原文为准。

![PupkinStealer，Telegram恶意软件]()

CYFIRMA 研究人员发现了一种基于 .NET 的新型信息窃取程序 PupkinStealer，这是一款轻量级但针对性极强的恶意软件，它会窃取浏览器凭证、消息会话数据和敏感桌面文件，然后通过 Telegram Bot API 悄悄传输这些数据。该恶意软件于 2025 年 4 月首次被发现，反映出利用合法云服务进行恶意数据泄露的趋势日益增长。

与那些收集所有能找到的数据的大型窃取程序不同，PupkinStealer 有一个明确的目标——窃取：

* 基于 Chromium 的浏览器（Chrome、Edge、Opera、Vivaldi）的浏览器密码
* Telegram 和 Discord 的会话文件
* 受害者桌面上的常见文件格式（.pdf、.txt、.jpg 等）
* 桌面截图

这些项目被存档，用系统元数据（如用户名和 IP）标记，并直接发送到攻击者控制的 Telegram 机器人。

CYFIRMA报告称：“*所有收集到的数据都会被压缩成一个 ZIP 档案，并通过 Telegram Bot API 传输到远程服务器，从而最大限度地降低可追溯性并增强隐蔽性。 ”*

PupkinStealer 绕过登录凭据的能力尤其令人担忧。它的目标是：

* Telegram 的 tdata 文件夹：允许攻击者无需用户凭据即可完全恢复会话。
* Discord 的 leveldb 存储：使用正则表达式模式提取 OAuth、MFA 和会话令牌。

CYFIRMA 警告说：“*通过窃取整个 tdata 目录，该恶意软件使攻击者能够在另一个系统上恢复受害者的 Telegram 会话，从而获得完全访问权限。 ”*

该恶意软件使用两个关键组件：

* FunctionsForStealer：从本地状态文件中提取特定于浏览器的加密密钥。
* FunctionsForDecrypt：使用 AES-GCM解密已保存的密码。

报告指出：“*这些解密密钥随后用于访问和解密浏览器登录数据 SQLite 数据库中存储的密码。 ”*

每个主要的 Chromium 浏览器都使用定制的方法（如 GetKeyChrome() 或 GetKeyVivaldi()）单独处理。

PupkinStealer 默默地：

* 以 1920×1080 的分辨率捕获受害者的主屏幕。
* 扫描桌面以查找 .sql、.jpg、.png 等高价值文件。
* 通过抑制文件收集期间的错误消息来避免警告用户。

收集所有数据后，PupkinStealer 将执行以下操作：

* 将其压缩为名为 [用户名]@ardent.zip 的 ZIP 档案。
* 在档案注释部分嵌入元数据（例如受害者的 IP、SID）。
* 使用自定义 Telegram Bot URL 发送。

由于 Telegram 的加密性、可靠性和匿名性，其数据泄露使用变得越来越流行——威胁行为者现在正在充分利用这些优势。

根据嵌入的字符串显示，恶意软件作者使用的别名是 Ardent。所使用的 Telegram 机器人 botkanalchik\_bot 似乎源自俄罗斯，其名称中含有“канал”（频道）的字样。

本文翻译自securityonline [原文链接](https://securityonline.info/pupkinstealer-tiny-malware-big-theft-via-telegram-bot-exposed/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307336](/post/id/307336)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/pupkinstealer-tiny-malware-big-theft-via-telegram-bot-exposed/)

如若转载,请注明出处： <https://securityonline.info/pupkinstealer-tiny-malware-big-theft-via-telegram-bot-exposed/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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