---
title: Internet Archive 在一个月内遭到两次入侵
url: https://www.anquanke.com/post/id/301122
source: 安全客-有思想的安全新媒体
date: 2024-10-23
fetch_date: 2025-10-06T18:48:35.489873
---

# Internet Archive 在一个月内遭到两次入侵

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

# Internet Archive 在一个月内遭到两次入侵

阅读量**63630**

发布时间 : 2024-10-22 10:28:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/170068/data-breach/internet-archive-second-data-breach.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**互联网档案馆再次遭到入侵，攻击者通过窃取的 GitLab 身份验证令牌入侵了其 Zendesk 电子邮件支持平台。**

互联网档案馆 是通过 Zendesk 泄露的，用户在多次发出警报后收到了有关令牌轮换不当导致 GitLab 令牌被盗的警告。

BleepingComputer 首先报道了这一事件的消息，因为它收到了一些人的信息，这些人收到了对其旧的互联网档案馆移除请求的回复，警告说该组织再次被入侵，因为他们没有正确轮换被盗的身份验证令牌。

![Internet Archive Zendesk emails sent by the threat actor Source: BleepingComputer]()
威胁行为者发送的互联网档案 Zendesk 电子邮件
来源：BleepingComputer BleepingComputer

该邮件凸显了互联网档案馆糟糕的安全态势。尽管在几周前就得到了通知，但该组织未能轮换暴露的 API 密钥，尤其是可以访问 800,000 多张支持票据的 Zendesk 令牌，这反映出其事件响应不力。糟糕的网络卫生状况增加了进一步数据泄露的风险，并可能破坏用户的信任。

这些电子邮件是由授权的 Zendesk 服务器（192.161.151.10）发出的。

根据攻击者的 Zendesk API 访问权限，用户上传的用于 Wayback Machine 页面删除请求的个人身份证明文件可能会被泄露。

10 月 9 日，Internet Archive 的 “The Wayback Machine ”遭遇数据泄露，威胁者获取了包含 3100 万用户数据的用户数据库。

入侵该热门网站的威胁者与数据泄露通知服务机构 Have I Been Pwned data 共享了一份被盗数据的副本。

HIBP 证实，被盗档案中有 3100 万条记录，包括电子邮件地址、网名、bcrypt 密码哈希值和密码更改的时间戳。HIBP 补充说，54% 的被盗记录已经在其平台上。

特洛伊-亨特（Troy Hunt）告诉 BleepingComputer，互联网档案馆泄露的文件是一个名为 “ia\_users.sql ”的 6.4GB SQL 文件。

亨特注意到，数据库记录的最新时间戳是 2024 年 9 月 28 日，这很可能就是数据外泄的日期。Hunt 将很快把受影响用户的信息添加到 HIBP 中。

Hunt 还验证了被盗档案中信息的真实性。

互联网档案馆创始人布鲁斯特-卡勒（Brewster Kahle）也证实，该平台遭到了 DDoS 攻击，网站多次下线。

BleepingComputer 将这次攻击归咎于一个名为 SN\_BlackMeta 的亲巴勒斯坦组织。

Internet Archive 数据泄露事件的起因是一名威胁者在该组织的一台开发服务器上发现了一个暴露的 GitLab 配置文件。该文件包含一个身份验证令牌，允许攻击者下载互联网档案馆的源代码，其中包括其他凭据和令牌。然后，攻击者使用这些凭证访问档案馆的数据库管理系统、用户数据库和更多源代码，甚至修改网站。黑客声称窃取了 7TB 的敏感数据，包括用于电子邮件支持系统的 Zendesk API 标记。被暴露的令牌自 2022 年 12 月起就一直可用，据说此后还进行了多次轮换。

尽管有这样的说法，但攻击者并没有分享被盗数据的证据，不过 BleepingComputer 证实了被暴露的 GitLab 验证令牌和对包含个人信息的 Zendesk 支持票据的访问权限。

黑客称，这些源代码包含其他凭据和身份验证令牌，包括 Internet Archive 数据库管理系统的凭据。这使得威胁者可以下载该组织的用户数据库、更多源代码并修改网站。

威胁者声称从互联网档案馆窃取了 7TB 的数据，但不愿分享任何样本作为证据。

不过，现在我们知道，被盗数据还包括互联网档案馆 Zendesk 支持系统的 API 访问令牌。

目前，还没有人声称对此次安全漏洞事件负责。专家警告说，被盗信息正在地下网络犯罪组织中流传，其他威胁者可以利用这些信息实施其他攻击。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/170068/data-breach/internet-archive-second-data-breach.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301122](/post/id/301122)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/170068/data-breach/internet-archive-second-data-breach.html)

如若转载,请注明出处： <https://securityaffairs.com/170068/data-breach/internet-archive-second-data-breach.html>

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