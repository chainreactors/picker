---
title: Booking.com网络钓鱼活动使用隐蔽的"ん"字符进行欺诈
url: https://www.anquanke.com/post/id/311257
source: 安全客-有思想的安全新媒体
date: 2025-08-16
fetch_date: 2025-10-07T00:13:18.526167
---

# Booking.com网络钓鱼活动使用隐蔽的"ん"字符进行欺诈

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

# Booking.com网络钓鱼活动使用隐蔽的"ん"字符进行欺诈

阅读量**64892**

发布时间 : 2025-08-15 17:20:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ax Sharma，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/bookingcom-phishing-campaign-uses-sneaky-character-to-trick-you/>

译文仅供参考，具体内容表达以及含义原文为准。

### ![]()

攻击者近期在一轮新的恶意邮件活动中，滥用 Unicode 字符让钓鱼链接看起来像是合法的 Booking.com 域名，从而诱导用户下载恶意软件。

此次攻击利用了一个日文假名字符“ん”。在某些系统或字体渲染中，这个字符看上去很像斜杠 “/”，使钓鱼网址在匆忙浏览的情况下显得真假难辨。

BleepingComputer 还发现了另一起针对财务软件 Intuit 的类似钓鱼活动，攻击者将域名中的小写字母“i”换成大写字母 “L”，以达到混淆视听的效果。

## 使用日本同形字符伪装 Booking.com 链接

此次攻击最早由安全研究员 JAMESWT 发现。攻击者滥用了日文平假名“ん”（Unicode U+3093），它在某些字体中看起来与 “/n” 或 “/~” 近似，从而能够构造出看似属于 Booking.com 的网址，实际上却指向恶意站点。

研究员公布了一封钓鱼邮件的样本：

![]()

*安全研究员詹姆斯・WT（JamesWT）分享的钓鱼邮件副本*

邮件正文中显示的链接为：

```
https://admin.booking.com/hotel/hoteladmin/...
```

看起来像正常的 Booking.com 链接，但真实的超链接却是：

```
https://account.booking.comんdetailんrestric-access.www-account-booking.com/en/
```

![]()

*在网页浏览器中显示的钓鱼页面*

在浏览器地址栏中，多个“ん”字符让人误以为那是 Booking.com 域下的子目录，但其实真正的注册域名是：

```
www-account-booking[.]com
```

也就是说，booking.com 前面的“admin”、“account”这些部分其实只是伪装的子域名。

受害者点击后会被重定向到：

```
www-account-booking[.]com/c.php?a=0
```

然后从 CDN 链接中下载一个恶意 MSI 安装程序：

```
https://updatessoftware.b-cdn[.]net/john/pr/04.08/IYTDTGTF.msi
```

样本可在 abuse.ch 的 MalwareBazaar 上获取，any.run 的分析显示该 MSI 文件会继续投递更多恶意载荷，比如信息窃取器或远程控制木马等。

## 利用同形字符（Homoglyphs）进行钓鱼

这种攻击方式属于同形字符攻击（Homograph Attack）的一种。攻击者使用形似但不同字符集的字符（如日文、俄文等）来伪装域名。例如俄文字母 “О” (U+041E) 肉眼看上去就是英文字母“O”，但实际上是完全不同的字符。

近年来，这类技术被反复用于钓鱼邮件和伪造网站。虽然各大平台也陆续推出了检测与告警机制，但仍存在识别盲区。

## 类似案例：Intuit -> “Lntuit”

另一波钓鱼活动针对财务软件 Intuit 用户。攻击邮件表面看起来来自 intuit.com，但实际上使用了以 “Lntuit” 开头的域名。因为小写字母 “lntuit” 在某些字体下与 “intuit” 十分相似。这种替换同样简单却有效。

![]()

*在 macOS 系统的 Mailspring 邮件客户端上查看的、来自 “Lntuit.com” 的 Intuit 钓鱼邮件（由塞尔吉乌・加特兰 / Sergiu Gatlan 提供）*

钓鱼邮件布局很窄，明显更适合移动端查看，攻击者显然是希望用户在手机上“点都不看”就点击“Verify my email”（验证我的邮箱）按钮。

按钮真实指向：

```
https://intfdsl[.]us/sa5h17/
```

![]()

*Intuit 钓鱼邮件在移动设备上的显示效果（塞尔吉乌・加特兰 / Sergiu Gatlan 提供）*

有意思的是，如果不是从目标用户的邮箱环境中点击，而是直接访问该链接，它会把你重定向回真·Intuit 登录页面（https://accounts.intuit.com/…），这也是一种混淆视线的技巧。

## 风险提醒与防范建议

这些案例再次提醒我们：攻击者会持续通过字体、字符视觉误差来诱导用户点击钓鱼链接。简单的肉眼识别已不够安全。

#### 建议包括：

**·** 鼠标悬停在链接上，查看真实跳转地址；

**·** 始终识别最右侧、首个“/”之前的完整域名，那才是真正的注册域；

**·** 警惕域名中混入的类似字符，如“ん”“О”“І”“ɑ”“ο”等；

**·** 保持终端安全软件更新，因为现代钓鱼往往直接投递恶意程序。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/bookingcom-phishing-campaign-uses-sneaky-character-to-trick-you/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311257](/post/id/311257)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/bookingcom-phishing-campaign-uses-sneaky-character-to-trick-you/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/bookingcom-phishing-campaign-uses-sneaky-character-to-trick-you/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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

* [使用日本同形字符伪装 Booking.com 链接](#h2-1)
* [利用同形字符（Homoglyphs）进行钓鱼](#h2-2)
* [类似案例：Intuit -> “Lntuit”](#h2-3)
* [风险提醒与防范建议](#h2-4)

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