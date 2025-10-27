---
title: Stack Overflow 警报！libexpat 中的 XML 漏洞威胁广泛软件
url: https://www.anquanke.com/post/id/307305
source: 安全客-有思想的安全新媒体
date: 2025-05-13
fetch_date: 2025-10-06T22:23:21.852816
---

# Stack Overflow 警报！libexpat 中的 XML 漏洞威胁广泛软件

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

# Stack Overflow 警报！libexpat 中的 XML 漏洞威胁广泛软件

阅读量**57219**

发布时间 : 2025-05-12 14:28:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/stack-overflow-alert-xml-flaw-in-libexpat-threatens-widespread-software/>

译文仅供参考，具体内容表达以及含义原文为准。

![libexpat，XML 漏洞]()

计算机紧急响应小组 (CERT) 协调中心 (CERT/CC) 发布了一份漏洞通告，警告 libexpat XML 解析库中存在一个堆栈溢出漏洞，编号为 CVE-2024-8176。该漏洞的 CVSS 评分为 7.5，攻击者可以利用该漏洞导致应用程序崩溃或潜在地触发内存损坏——具体取决于该库在受影响环境中的部署方式。

libexpat 是一个用 C 语言编写的开源、面向流的 XML 解析器。它广泛应用于各种软件生态系统，尤其是在需要高效处理大型 XML 文件的系统中。

libexpat 被各种不同的软件和公司广泛使用。由于 libexpat 广泛应用于各种平台（从嵌入式系统到大型企业软件），因此其漏洞可能造成深远影响。

该漏洞的根源在于 libexpat 处理递归实体扩展的方式。当解析特制的 XML 文件时，攻击者可以深度嵌套实体引用，从而引发无限制递归，最终导致堆栈溢出。

CERT/CC解释说：“存在*堆栈溢出漏洞……在解析具有深度嵌套实体引用的 XML 文档时，libexpat 可能会被迫无限递归。 ”*

这种无限制递归会导致拒绝服务 (DoS) 情况，并且在特定条件下可能导致可利用的内存损坏，从而为更严重的攻击打开大门。

任何使用未修补版本的 libexpat 解析 XML 的软件都存在漏洞。攻击者无需提升权限，只需使用 libexpat 向系统输入恶意 XML 文件即可。

CERT/CC 警告说：“*攻击者……可以向程序提供 XML 文档并引发 DoS 攻击或内存损坏攻击。 ”*

libexpat 广泛集成到众多开源和商业项目中，使得供应链风险成为一个主要问题。

libexpat 2.7.0版本中已提供该漏洞的修复程序。强烈建议开发人员和维护人员立即更新，并使用官方GitHub问题中提供的概念验证 (PoC) 有效载荷来验证保护措施。

该漏洞由 Google Project Zero 的 Jann Horn 负责任地披露。

本文翻译自securityonline [原文链接](https://securityonline.info/stack-overflow-alert-xml-flaw-in-libexpat-threatens-widespread-software/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307305](/post/id/307305)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/stack-overflow-alert-xml-flaw-in-libexpat-threatens-widespread-software/)

如若转载,请注明出处： <https://securityonline.info/stack-overflow-alert-xml-flaw-in-libexpat-threatens-widespread-software/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**5赞

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