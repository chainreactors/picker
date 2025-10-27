---
title: Poseidon Stealer恶意软件通过虚假DeepSeek网站攻击Mac用户
url: https://www.anquanke.com/post/id/304721
source: 安全客-有思想的安全新媒体
date: 2025-02-26
fetch_date: 2025-10-06T20:32:41.337635
---

# Poseidon Stealer恶意软件通过虚假DeepSeek网站攻击Mac用户

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

# Poseidon Stealer恶意软件通过虚假DeepSeek网站攻击Mac用户

阅读量**86887**

发布时间 : 2025-02-25 09:57:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/poseidon-stealer-malware-targets-mac-users-via-fake-deepseek-site/>

译文仅供参考，具体内容表达以及含义原文为准。

![Poseidon Stealer malware]()

eSentire 威胁响应部门（TRU）发现了一场新的攻击活动，该活动使用  Poseidon Stealer 恶意软件来针对 Mac 用户。此次攻击活动利用了一个模仿合法的 DeepSeek 平台的虚假网站，诱骗用户下载并执行恶意负载。

感染过程始于用户被重定向到一个虚假的 DeepSeek 网站（deepseek.exploreio [.] net），通常是通过恶意广告被引导过去的。这个虚假网站与真正的 DeepSeek 网站极为相似，欺骗用户点击一个 “立即开始” 按钮，点击后会跳转到一个下载页面。当用户点击 “下载适用于 Mac OS 的版本” 时，就会下载一个恶意的 DMG 文件。

![]()

假冒 DeepSeek 网站 |来源：TRU

下载的 DMG 文件中包含一个伪装成 DeepSeek 应用程序的 shell 脚本。当用户将这个 “应用程序” 拖放到终端（Terminal）中时，该脚本就会执行，从而绕过macOS GateKeeper安全措施。随后，该脚本会下载并执行Poseidon Stealer恶意负载。

Poseidon Stealer 是一种恶意软件即服务（MaaS），它的目标是从基于 Chromium 或Firefox的浏览器中窃取敏感数据，包括信用卡信息、密码、书签以及加密货币钱包数据。它还会收集系统信息，窃取钥匙串数据库，并从Desktop、Downloads 和 Documents目录中盗取文件。

此次攻击利用通过终端执行的方法绕过了 GateKeeper 的保护机制。Poseidon Stealer恶意负载采用了反调试和字符串加密技术，以阻碍对其进行分析。该恶意软件还会进行检测，判断自己是否在沙盒环境或研究环境中运行，如果检测到是这样的环境，它就会自行终止运行。

用户应保持警惕，防范虚假的软件下载网站，并采取积极主动的安全措施来降低风险。

本文翻译自securityonline [原文链接](https://securityonline.info/poseidon-stealer-malware-targets-mac-users-via-fake-deepseek-site/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304721](/post/id/304721)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/poseidon-stealer-malware-targets-mac-users-via-fake-deepseek-site/)

如若转载,请注明出处： <https://securityonline.info/poseidon-stealer-malware-targets-mac-users-via-fake-deepseek-site/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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