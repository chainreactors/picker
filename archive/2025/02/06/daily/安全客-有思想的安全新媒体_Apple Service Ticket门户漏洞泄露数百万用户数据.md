---
title: Apple Service Ticket门户漏洞泄露数百万用户数据
url: https://www.anquanke.com/post/id/303819
source: 安全客-有思想的安全新媒体
date: 2025-02-06
fetch_date: 2025-10-06T20:34:34.024828
---

# Apple Service Ticket门户漏洞泄露数百万用户数据

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

# Apple Service Ticket门户漏洞泄露数百万用户数据

阅读量**362759**

发布时间 : 2025-02-05 14:55:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/apple-service-ticket-portal-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

苹果服务工单门户网站曝出严重安全漏洞，数百万用户的敏感数据或遭泄露。

该漏洞源于不安全的直接对象引用（IDOR）与权限提升问题的叠加，使得未经授权的人员能够访问用户信息，其中包括 Mac 序列号、国际移动设备识别码（IMEI）以及服务工单详情。

研究人员维图维尔（Virtuvil）在使用二维码提交维修工单后，通过对门户网站后端功能展开调查，发现了这一问题。

### SIEM 即服务

利用 IDOR 漏洞，他得以访问其他用户的服务工单及敏感数据。进一步深入探究后发现，还可利用权限提升漏洞完全接管管理面板。

该问题的核心在于门户网站在设计时缺失访问控制检查。

* **IDOR 漏洞**：门户网站为服务工单分配了唯一标识符，但却未对用户是否有权限访问这些记录进行验证。例如：包含类似<https://service.apple.com/ticket?id=12345>这样参数的网址，只需更改 id 值就能被修改。这使得未经授权的人员无需经过身份验证，即可访问其他用户的工单。
* **权限提升**：一旦实现未经授权的访问，进一步的利用手段便可实现权限提升至管理员级别。这种纵向权限提升能够让攻击者掌控敏感的系统功能，如修改维修预约或访问客户数据库。
* **缺乏速率限制**：由于缺少速率限制机制，风险被进一步放大。攻击者可以使用诸如入侵脚本之类的自动化工具，遍历工单 ID 或用户参数，从而有系统地大规模窃取数据。

### 遭泄露的数据

此次数据泄露涉及广泛的敏感信息：

* **客户数据**：姓名、联系方式和地址。
* **设备详情**：Mac 序列号、IMEI 码以及保修状态。
* **服务信息**：维修记录和预约时间表。

研究人员表示：“我查看自己工单的请求时，注意到网址中包含一个极易修改的参数 —— 我的手机号码。通过更改请求中的手机号码，我无需任何身份验证措施，就能访问另一位用户的工单。”

### 遭泄露的客户数据

这样的漏洞影响极为严重，个人信息的泄露可能导致身份盗窃或网络钓鱼攻击。恶意行为者还可能取消或更改大量的维修预约。

苹果公司在通过漏洞悬赏计划得知该漏洞后，随即进行了修复。受影响的系统均已推出安全更新，加强了授权检查并实施了速率限制措施。

此次数据泄露事件深刻地提醒我们，积极主动的网络安全措施对于保护用户数据至关重要。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/apple-service-ticket-portal-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303819](/post/id/303819)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/apple-service-ticket-portal-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/apple-service-ticket-portal-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [数据泄露](/tag/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)

**+1**5赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [德克萨斯州交通部 (TxDOT) 数据泄露事件暴露了 30 万份车祸报告](/post/id/308355)

  2025-06-11 16:33:57
* ##### [税务解决方案公司 Optima Tax Relief 遭勒索软件攻击，数据泄露](/post/id/308262)

  2025-06-09 17:29:27
* ##### [美国电话电报公司（AT&T）再次遭遇大规模身份数据泄露事件](/post/id/308193)

  2025-06-06 15:22:45
* ##### [美实名爆料：马斯克领导的DOGE被指入侵劳工机构系统，敏感数据疑遭泄露](/post/id/306743)

  2025-04-21 16:48:48
* ##### [DeepSeek数据泄露——12000个硬编码的有效API密钥和密码遭曝光](/post/id/304864)

  2025-02-28 15:37:26

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