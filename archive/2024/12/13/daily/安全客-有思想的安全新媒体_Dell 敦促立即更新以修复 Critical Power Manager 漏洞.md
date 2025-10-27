---
title: Dell 敦促立即更新以修复 Critical Power Manager 漏洞
url: https://www.anquanke.com/post/id/302710
source: 安全客-有思想的安全新媒体
date: 2024-12-13
fetch_date: 2025-10-06T19:36:16.261607
---

# Dell 敦促立即更新以修复 Critical Power Manager 漏洞

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

# Dell 敦促立即更新以修复 Critical Power Manager 漏洞

阅读量**77484**

发布时间 : 2024-12-12 16:59:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/dell-urges-update-critical-power-manager-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

**概要：**

* **严重漏洞警报：**Dell Power Manager 3.17版本之前的版本存在一个高严重性的访问控制漏洞（CVE-2024-49600），允许攻击者获得提升的权限。
* **利用风险：**拥有本地访问权限的攻击者可以执行任意代码，绕过安全措施，并危及系统的机密性、完整性和可用性。
* **软件更新：**Dell已发布Power Manager 3.17版本以解决此漏洞；用户应立即更新，因为没有可用的解决方法。
* **漏洞发现：**此漏洞由CHT Security的TsungShu Chiu发现并负责任地披露。
* **Dell近期数据泄露事件：**Dell在2024年9月面临多次数据泄露，暴露了员工和项目的敏感信息，进一步强调了需要强有力的安全措施。

Dell就其Power Manager软件中发现的不当访问控制漏洞发布了严重安全警报（DSA-2024-439）。这个被标识为CVE-2024-49600的漏洞可能允许攻击者在受影响的系统上执行恶意代码并获得提升的权限。该漏洞影响3.17版本之前发布的Dell Power Manager版本。

需知悉的是，Dell Power Manager是一款广泛用于管理Dell系统电源设置的软件。这个应用程序延长了系统电池寿命，并提供可自定义的电池维护设置。它还提醒用户关于电源适配器、电池、底座和USB Type-C设备的不兼容性问题。

该漏洞源于软件内的不当访问控制，使得拥有低权限的本地用户可以加以利用。攻击者可以绕过安全措施，执行任意代码，未经授权访问敏感的系统功能。这个漏洞的严重性被评为高，CVSS基础评分为7.8。

如果被利用，它可能导致受损害系统的重大安全风险，危及它们的机密性、完整性和可用性。执行任意代码可能导致恶意软件安装、数据盗窃或系统受损，获得更高级别的系统权限将使未经授权的行为者能够执行原本受限制的操作。

Dell已发布Power Manager的更新版本（3.17版）以解决该漏洞。强烈建议用户立即更新其软件以保护系统，因为目前没有可用的解决方法。

“Dell Technologies强烈建议尽快应用这个重要更新。该更新包含关键的错误修复以及改进您的Dell系统功能、可靠性和稳定性的更改，”通告中写道。

CHT Security的TsungShu Chiu发现了这个漏洞，并负责任地向Dell Technologies披露，Dell随后确认并感谢了Chiu的努力。

Dell最近因一系列负面新闻而登上头条。Hackread.com最近报道了一系列Dell数据泄露事件，涉及敏感信息的暴露。在2024年9月19日至24日之间，一个名为“grep”的黑客三次入侵Dell（一次与黑客“Chucky”合作），窃取了与Jira文件、数据库表和模式迁移相关的机密数据，总计3.5 GB未压缩数据，10863名员工的数据，以及大约500 MB的敏感数据，包括项目文件和多重因素认证（MFA）数据。

本文翻译自hackread [原文链接](https://hackread.com/dell-urges-update-critical-power-manager-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302710](/post/id/302710)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/dell-urges-update-critical-power-manager-vulnerability/)

如若转载,请注明出处： <https://hackread.com/dell-urges-update-critical-power-manager-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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