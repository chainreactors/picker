---
title: 施乐打印机漏洞危及数据防线，Versalink C7025 用户凭证面临窃取风险
url: https://www.anquanke.com/post/id/304481
source: 安全客-有思想的安全新媒体
date: 2025-02-20
fetch_date: 2025-10-06T20:33:20.730410
---

# 施乐打印机漏洞危及数据防线，Versalink C7025 用户凭证面临窃取风险

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

# 施乐打印机漏洞危及数据防线，Versalink C7025 用户凭证面临窃取风险

阅读量**52597**

发布时间 : 2025-02-19 10:29:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/xerox-versalink-printers-vulnerable-to-pass-back-attacks-credentials-at-risk/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-12510 and CVE-2024-12511]()

Rapid7 公司的研究人员发现，施乐（Xerox）Versalink C7025 多功能打印机存在漏洞，攻击者可能利用这些漏洞窃取用户凭证。这些漏洞被认定为 CVE-2024-12510 和 CVE-2024-12511，可导致一种被称为 “回传攻击” 的情况，即打印机被诱骗将身份验证数据发送给攻击者。

施乐 Versalink C7025 是一款广受欢迎的企业级打印机，具备打印、复印、扫描、传真和电子邮件功能。受这些漏洞影响的是运行固件版本 57.69.91 及更早版本的设备。

Rapid7 的报告解释道：“这种回传式攻击利用了一个漏洞，使恶意行为者能够更改多功能打印机（MFP）的配置，并导致 MFP 设备将身份验证凭证发送给恶意行为者。”

攻击者可以利用这些漏洞获取诸如轻量级目录访问协议（LDAP）、服务器消息块协议（SMB）和文件传输协议（FTP）等服务的凭证。这可能使他们得以访问敏感信息，甚至在组织的网络内横向移动，进而攻陷其他系统。

攻击者需要获得打印机的管理员账户权限，或者能够对打印机控制台进行物理访问。然后，他们可以修改打印机的配置，将身份验证请求重定向到他们控制的服务器上。当用户尝试通过 LDAP 或 SMB 等服务进行身份验证时，打印机在不知情的情况下会将用户的凭证发送到攻击者的服务器上。

施乐公司已经发布了固件更新来修复这些漏洞。强烈建议使用受影响的 Versalink 打印机的机构尽快升级到最新的已打补丁的版本。

作为临时缓解措施，Rapid7 建议为管理员账户设置复杂密码，并避免在 LDAP 和 SMB 等服务中使用具有提升权限的 Windows 身份验证账户。同时，也建议为未经验证的用户禁用远程控制控制台。

本文翻译自securityonline [原文链接](https://securityonline.info/xerox-versalink-printers-vulnerable-to-pass-back-attacks-credentials-at-risk/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304481](/post/id/304481)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/xerox-versalink-printers-vulnerable-to-pass-back-attacks-credentials-at-risk/)

如若转载,请注明出处： <https://securityonline.info/xerox-versalink-printers-vulnerable-to-pass-back-attacks-credentials-at-risk/>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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