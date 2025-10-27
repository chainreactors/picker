---
title: 警惕！恶意 “Adobe Drive X” 借微软页面行网络钓鱼，骗取用户凭证
url: https://www.anquanke.com/post/id/304378
source: 安全客-有思想的安全新媒体
date: 2025-02-18
fetch_date: 2025-10-06T20:36:09.320338
---

# 警惕！恶意 “Adobe Drive X” 借微软页面行网络钓鱼，骗取用户凭证

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

# 警惕！恶意 “Adobe Drive X” 借微软页面行网络钓鱼，骗取用户凭证

阅读量**54206**

发布时间 : 2025-02-17 10:44:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/fake-adobe-drive-x-app-sneaks-through-microsoft-login-to-steal-credentials/>

译文仅供参考，具体内容表达以及含义原文为准。

![Adobe Drive X]()

来自 “Adobe Drive X” 的权限请求，“Adobe Drive X” 是一个由威胁行为者控制的自定义微软 365 应用程序 | 来源：考凡思（Cofense）

考凡思（Cofense）公司的网络钓鱼防御中心（Phishing Defense Center，简称 PDC）发现了一场网络钓鱼活动，该活动利用合法的微软登录页面诱骗用户授权访问一个恶意的 “Adobe Drive X” 应用程序。然后，这个应用程序会将受害者重定向到一个伪造的微软登录页面，以窃取他们的凭证信息。

攻击始于一封伪装成 Office 365 密码重置请求的网络钓鱼邮件。邮件中包含一个链接，点击后会跳转到一个真正的微软身份验证页面，这使得这次攻击看起来更具说服力。然而，一旦用户在这个合法页面上输入了他们的凭证信息，随后就会被提示授权一个名为 “Adobe Drive X” 的自定义微软 365 应用程序。

这正是攻击者狡猾策略的体现之处。通过看似无害的与 Adobe 相关的应用程序来请求访问权限，他们利用了用户对微软和 Adobe 的信任。该应用程序请求获取用户的电子邮件地址和基本个人资料信息，这进一步增加了其合法性的表象。

如果用户接受了这些权限，他们就会被重定向到一个旨在模仿微软登录页面的凭证钓鱼页面。这个页面并非托管在微软的域名下，但毫无防备的用户可能会忽略这个关键细节，尤其是在之前已经成功通过合法的微软页面登录之后。

考凡思在其报告中解释道：“威胁行为者很可能在合法的微软 365 登录页面之后设置了这个凭证钓鱼企图，以便打用户一个措手不及。”“警惕性较低的用户可能不会去验证第二个登录页面的网址，从而成为凭证钓鱼攻击的受害者。”

用户应该始终仔细检查网址，对向未知应用程序授予权限保持警惕，并报告任何可疑活动。

本文翻译自securityonline [原文链接](https://securityonline.info/fake-adobe-drive-x-app-sneaks-through-microsoft-login-to-steal-credentials/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304378](/post/id/304378)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/fake-adobe-drive-x-app-sneaks-through-microsoft-login-to-steal-credentials/)

如若转载,请注明出处： <https://securityonline.info/fake-adobe-drive-x-app-sneaks-through-microsoft-login-to-steal-credentials/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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