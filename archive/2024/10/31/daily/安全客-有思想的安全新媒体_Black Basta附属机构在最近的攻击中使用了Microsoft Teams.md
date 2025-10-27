---
title: Black Basta附属机构在最近的攻击中使用了Microsoft Teams
url: https://www.anquanke.com/post/id/301418
source: 安全客-有思想的安全新媒体
date: 2024-10-31
fetch_date: 2025-10-06T18:51:17.795292
---

# Black Basta附属机构在最近的攻击中使用了Microsoft Teams

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

# Black Basta附属机构在最近的攻击中使用了Microsoft Teams

阅读量**50741**

发布时间 : 2024-10-30 16:17:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/170311/cyber-crime/black-basta-ransomware-microsoft-teams.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**ReliaQuest研究人员观察到Black Basta的分支机构依赖微软团队获得目标网络的初始访问权限。**

ReliaQuest研究人员警告，Black Basta勒索软件的分支机构已转向使用微软团队，假装IT支持人员，诱使员工授权访问。

BlackBasta勒索软件的操作者被发现在员工面前伪装成企业帮助台，联系员工帮助他们缓解正在进行的垃圾邮件攻击。

威胁行为者用电子邮件充斥员工的收件箱，然后在微软团队上伪装成IT支持人员，提供关于垃圾邮件问题的“帮助”。

ReliaQuest发布的报告指出：“他们之前的做法包括用电子邮件垃圾邮件淹没用户，促使他们创建一个合法的帮助台工单来解决问题。然后攻击者会联系终端用户，假装是帮助台，回应工单。在最近的事件中，攻击者通过使用微软团队聊天消息与目标用户沟通，并引入恶意二维码来促进初始访问。”

威胁行为者试图诱使用户下载远程监控和管理（RMM）工具，如AnyDesk，一旦获得目标环境的初始访问权限，就部署勒索软件。

研究人员指出，发送给潜在受害者的信息量非常大；在一个实例中，他们观察到在短短50分钟内向一个用户发送了大约1000封电子邮件。

攻击者将目标用户添加到与外部用户的微软团队聊天中。这些外部用户使用他们创建的Entra ID租户进行操作，采用命名规则伪装成支持、管理员或帮助台人员。

以下是攻击者使用的一些租户：

* **cybersecurityadmin.onmicrosoft[.]com**
* **securityadminhelper.onmicrosoft[.]com**
* **supportserviceadmin.onmicrosoft[.]com**
* **supportadministrator.onmicrosoft[.]com**

“这些外部用户将他们的个人资料设置为‘DisplayName’，旨在让目标用户认为他们是在与帮助台账户沟通。”报告继续说道。“在我们观察到的几乎所有实例中，显示名称都包含了字符串‘Help Desk’，通常周围有空格字符，这可能是为了让名称在聊天中居中。我们还观察到，通常情况下，目标用户被添加到了‘一对一’聊天中。”

威胁行为者还在聊天中发送二维码，作为Quishing尝试的一部分。

专家根据域名创建和Cobalt Strike配置的共同点，高度自信地将攻击归因于Black Basta。

专家观察到，外部用户的操作通常起源于俄罗斯，位于莫斯科时区。

获得访问权限后，攻击者部署恶意文件，包括代理恶意软件和Cobalt Strike，以加深网络渗透。专家建议限制外部微软团队通信，并记录可疑聊天活动以提高安全性。

报告总结说：“这场活动仍在发展，Black Basta展现了他们快速适应TTP（战术、技术和程序）的能力，这可能是为了挫败防御者，为自己在网络上争取更多时间以进一步发动攻击。虽然他们的初始访问方法已经改变，但他们的后利用活动可能与之前观察到的模式保持一致，这些模式已被现有的安全工具和检测规则所覆盖。”

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/170311/cyber-crime/black-basta-ransomware-microsoft-teams.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301418](/post/id/301418)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/170311/cyber-crime/black-basta-ransomware-microsoft-teams.html)

如若转载,请注明出处： <https://securityaffairs.com/170311/cyber-crime/black-basta-ransomware-microsoft-teams.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

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