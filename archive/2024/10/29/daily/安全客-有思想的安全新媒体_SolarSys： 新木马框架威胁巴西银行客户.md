---
title: SolarSys： 新木马框架威胁巴西银行客户
url: https://www.anquanke.com/post/id/301308
source: 安全客-有思想的安全新媒体
date: 2024-10-29
fetch_date: 2025-10-06T18:49:06.707824
---

# SolarSys： 新木马框架威胁巴西银行客户

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

# SolarSys： 新木马框架威胁巴西银行客户

阅读量**48449**

发布时间 : 2024-10-28 10:55:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/solarsys-new-trojan-framework-threatens-brazilian-banking-customers/>

译文仅供参考，具体内容表达以及含义原文为准。

![SolarSys Trojan]()

360 安全中心在最近的一份报告中揭示了巴西银行客户面临的一个新威胁，即 SolarSys 的出现，这是一个木马框架，旨在窃取敏感数据，同时逃避检测。该框架主要活跃在巴西这个众所周知的银行木马热点地区，它使用复杂的规避技术和多种攻击模块，从多个方面破坏用户安全。

SolarSys通过多组件结构运行，包括JavaScript后门、邮件蠕虫和各种间谍模块。正如360安全公司解释的那样，“SolarSys框架主要由JavaScript后门、邮件蠕虫和多种间谍模块组成”，每个组件都执行专门的任务，使木马能够绕过安全屏障，捕获宝贵的用户数据。

为了保持弹性存在，SolarSys 使用域名生成算法（DGA）生成大量动态域名，作为其命令与控制（C&C）地址。这种机制使攻击者能够在安全厂商试图阻止访问时迅速切换域名。“报告指出：”当安全厂商封锁部分域名时，黑客会迅速激活新的域名，以确保整个僵尸网络不受影响。

SolarSys 通过伪造的 MSI 安装程序发起感染，这些安装程序伪装成 Java 和 Microsoft HTML 帮助等合法应用程序。这些文件一旦被执行，就会利用 InstallUtil 启动恶意 .NET 动态库 uninstall.dll，将自己注册为受感染系统上的持久后门。从那里，恶意软件可以每隔 11 小时下载并执行额外的病毒模块，从而实现对 SolarSys 功能的持续访问和更新。

![]()
图片 360 安全中心

该后门的持久机制涉及一个 JavaScript 文件 Install.js，它 “每 11 个小时下载并执行最新的病毒模块”，确保 SolarSys 在受感染设备上保持活跃，而不会引起用户的怀疑。

SolarSys 的一个独特功能是其邮件蠕虫模块，该模块利用用户的联系人列表进行传播。通过在受感染的机器上建立 Node.js 环境，SolarSys 可模拟用户点击，直接向受害者的联系人发送钓鱼邮件。钓鱼邮件包含一个附件，旨在利用模板注入技术逃避检测，从而进一步传播恶意软件。虽然研究人员无法检索到特定模板，但他们怀疑 SolarSys 将继续通过这一渠道更新其有效载荷。

SolarSys 部署了多个间谍组件来捕获敏感信息，包括一个旨在从 Google Chrome 浏览器中提取数据的模块。该模块可捕获账户凭证、浏览历史和其他用户详细信息。此外，SolarSys 还包括一个银行木马，它会在用户访问网上银行网站时进行检测，并覆盖一个伪造的登录界面。正如报告所解释的，“伪造的网上银行登录界面……诱骗用户输入各种凭证”，然后将这些凭证传输到攻击者的服务器。

该恶意软件专门针对多家巴西银行，包括巴西银行、Bradesco、Itaú、桑坦德银行和 Sicoob 等，对巴西金融业构成直接威胁。

截至报告发布时，SolarSys 的检测已被证明具有挑战性，360 Security Center 是 VirusTotal 上唯一能够识别该病毒的供应商。

![]()
图片： 360 安全中心

本文翻译自securityonline [原文链接](https://securityonline.info/solarsys-new-trojan-framework-threatens-brazilian-banking-customers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301308](/post/id/301308)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/solarsys-new-trojan-framework-threatens-brazilian-banking-customers/)

如若转载,请注明出处： <https://securityonline.info/solarsys-new-trojan-framework-threatens-brazilian-banking-customers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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