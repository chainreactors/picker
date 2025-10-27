---
title: 西门子SINEC安全监视器中存在多个关键漏洞
url: https://www.anquanke.com/post/id/300632
source: 安全客-有思想的安全新媒体
date: 2024-10-10
fetch_date: 2025-10-06T18:51:55.476035
---

# 西门子SINEC安全监视器中存在多个关键漏洞

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

# 西门子SINEC安全监视器中存在多个关键漏洞

阅读量**226397**

发布时间 : 2024-10-09 10:44:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/critical-vulnerabilities-discovered-in-siemens-sinec-security-monitor/>

译文仅供参考，具体内容表达以及含义原文为准。

西门子发布了其SINEC安全监视器的一个新的安全更新，这是一个模块化的网络安全软件，用于被动的，非侵入性的，持续的监测客户场所的生产环境。已在V4.9.0之前的版本中发现了几个关键漏洞，这些漏洞被追踪为CVE-2024-47553、CVE-2024-47662、CVE-20483和CVE-2024-4565。

![]()

SINEC 安全监视器中发现的4个漏洞，其严重程度和对受影响系统的潜在风险各不相同。如果被利用，它们可能允许攻击者执行任意代码，损害系统完整性，并有可能获得对底层操作系统的根层访问权限。

已解决的脆弱性包括:

CVE-2024-47553（CVSSv4 9.4）:由于ssmctl-client命令中用户输入的验证不当，允许经过身份验证的低权限攻击者以根权限执行任意代码。

CVE-2024-47562（CVSSv49.3）:由于用户输入ssmctl-client命令中的特殊元素被不当中和，使得经过身份验证的低特权本地攻击者能够执行特权命令。

CVE-2024-47563（CVSSv4 6.9）:由于对用于创建CSR文件的文件路径的验证不当，允许未经验证的远程攻击者在非预期位置创建文件。这可能会损害这些目录中文件的完整性。

CVE-2024-47565（CVSSv45.3）:允许经过身份验证的远程攻击者破坏应用程序的配置，原因是针对允许值对用户输入的验证不足。

西门子敦促用户将其SINEC Security Monitor安装更新到版本4.9.0或更高版本，以缓解这些漏洞。该更新可从西门子网站下载。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-vulnerabilities-discovered-in-siemens-sinec-security-monitor/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300632](/post/id/300632)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-vulnerabilities-discovered-in-siemens-sinec-security-monitor/)

如若转载,请注明出处： <https://securityonline.info/critical-vulnerabilities-discovered-in-siemens-sinec-security-monitor/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

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