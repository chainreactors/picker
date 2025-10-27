---
title: Ragic 企业云数据库存在多个漏洞
url: https://www.anquanke.com/post/id/301041
source: 安全客-有思想的安全新媒体
date: 2024-10-19
fetch_date: 2025-10-06T18:51:13.662220
---

# Ragic 企业云数据库存在多个漏洞

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

# Ragic 企业云数据库存在多个漏洞

阅读量**85745**

发布时间 : 2024-10-18 10:26:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/ragic-enterprise-cloud-database-patches-multi-flaws-including-cve-2024-9984-cvss-9-8/>

译文仅供参考，具体内容表达以及含义原文为准。

![Ragic Enterprise Cloud Database - CVE-2024-9983 - CVE-2024-9984 - CVE-2024-9985]()

Ragic 企业云数据库中发现的多个漏洞，Ragic 企业云数据库是一个用于构建自定义商业应用程序的流行无代码平台。

这些漏洞由 DEVCORE 红队报告，被识别为 CVE-2024-9983、CVE-2024-9984 和 CVE-2024-9985，每个漏洞的风险程度不同，但如果不打补丁，都会构成重大威胁。 它们会影响 2024 年 8 月 8 日发布更新之前的 Ragic 企业云数据库版本。

**漏洞细目：**

* **CVE-2024-9983 （CVSS 7.5）： 通过路径遍历任意读取文件：** 此漏洞允许未经认证的攻击者利用特定页面参数中的漏洞读取任意系统文件，从而可能暴露敏感信息。
* **CVE-2024-9984 （CVSS 9.8）： 关键功能验证缺失：** 一个关键漏洞允许未经身份验证的远程攻击者利用缺失的身份验证检查，获取任何用户的会话 cookie。 这可能导致帐户被完全接管和敏感数据泄露。
* **CVE-2024-9985 （CVSS 8.8）： 任意文件上传：** 此漏洞可让拥有一般用户权限的攻击者上载恶意档案（如 webshell）至服务器。 攻击者可利用此漏洞执行任意代码并完全控制系统。

**影响和补救措施：**

这些漏洞对使用Ragic企业云端数据库的企业构成重大风险。 成功利用漏洞可能导致：

* **数据泄露：** 敏感业务数据可能被窃取或篡改。
* **系统受损：**攻击者可完全控制数据库服务器和连接系统。
* **业务中断：** 依赖数据库的关键业务流程可能会中断。

Ragic 已在 2024 年 8 月 8 日发布的安全更新中解决了这些漏洞。 强烈呼吁 Ragic 企业云数据库的所有用户立即将其系统更新至 2024/08/08 09：45：25 或更高版本。

本文翻译自securityonline [原文链接](https://securityonline.info/ragic-enterprise-cloud-database-patches-multi-flaws-including-cve-2024-9984-cvss-9-8/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301041](/post/id/301041)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/ragic-enterprise-cloud-database-patches-multi-flaws-including-cve-2024-9984-cvss-9-8/)

如若转载,请注明出处： <https://securityonline.info/ragic-enterprise-cloud-database-patches-multi-flaws-including-cve-2024-9984-cvss-9-8/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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