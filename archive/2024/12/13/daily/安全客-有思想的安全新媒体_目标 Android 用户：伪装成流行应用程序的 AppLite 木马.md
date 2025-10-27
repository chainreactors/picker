---
title: 目标 Android 用户：伪装成流行应用程序的 AppLite 木马
url: https://www.anquanke.com/post/id/302672
source: 安全客-有思想的安全新媒体
date: 2024-12-13
fetch_date: 2025-10-06T19:36:21.813046
---

# 目标 Android 用户：伪装成流行应用程序的 AppLite 木马

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

# 目标 Android 用户：伪装成流行应用程序的 AppLite 木马

阅读量**68565**

发布时间 : 2024-12-12 14:30:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/android-users-targeted-applite-trojan-disguised-as-popular-apps/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

zLabs发现了AppLite，它是AntiDot银行木马的一个复杂的新变种，通过大范围的网络钓鱼活动以安卓设备为目标。该恶意软件伪装成 Chrome、TikTok 和企业工具等合法应用程序，能够窃取敏感凭证并完全控制受感染的设备。

该活动背后的攻击者采用了精心设计的社交工程策略来引诱受害者。他们伪装成人力资源代表或工作招聘人员，向潜在受害者发送精心制作的网络钓鱼电子邮件。这些电子邮件将用户重定向到模仿知名公司和教育机构的钓鱼网站，敦促他们下载恶意安卓应用程序。

一旦安装，这个看似合法的应用程序就会充当滴管，将 AppLite 银行木马暗中发送到受害者的设备上。正如 zLabs 所解释的那样： “受害者会被重定向到一个恶意登陆页面，以继续申请流程或安排面试。登陆页面会操纵受害者下载并安装一个恶意程序。

![AppLite banking trojan]()
攻击序列 Zimperium

AppLite 使用 ZIP 操作等混淆技术来逃避安全工具的检测： “恶意行为者经常使用各种方法改变 APK 文件的 ZIP 格式和 Android Manifest 文件的结构，使分析工具失效并逃避检测。解析器如果不更新，可能无法正确处理文件，从而使恶意软件绕过检测机制，继续安装在目标设备上。”

与其他银行木马类似，AppLite 利用叠加攻击来欺骗用户。当目标应用程序启动时，恶意软件会叠加一个模仿合法应用程序的恶意 HTML 页面，诱骗用户输入敏感凭据。

恶意软件通过 Webocket 与其命令和控制 (C&C) 服务器建立连接，实现实时双向通信。攻击者可以发布命令收集敏感数据，如联系人、短信和应用程序凭据，甚至可以利用虚拟网络计算（VNC）功能远程控制设备。

AppLite 最令人震惊的功能是自动解锁设备。通过使用辅助功能服务，它可以识别锁定模式视图、计算移动路径并模拟触摸手势，从而在无需用户交互的情况下解锁设备。

该活动针对精通英语、西班牙语、法语、德语、意大利语、葡萄牙语和俄语的用户。主要受害者是 95 个银行应用程序、62 个加密货币应用程序和其他金融服务的用户，分布在北美、欧洲和亚洲部分地区。

本文翻译自securityonline [原文链接](https://securityonline.info/android-users-targeted-applite-trojan-disguised-as-popular-apps/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302672](/post/id/302672)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/android-users-targeted-applite-trojan-disguised-as-popular-apps/)

如若转载,请注明出处： <https://securityonline.info/android-users-targeted-applite-trojan-disguised-as-popular-apps/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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