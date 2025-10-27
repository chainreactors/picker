---
title: Splunk 修补关键漏洞，包括远程代码执行漏洞
url: https://www.anquanke.com/post/id/300899
source: 安全客-有思想的安全新媒体
date: 2024-10-16
fetch_date: 2025-10-06T18:45:39.890137
---

# Splunk 修补关键漏洞，包括远程代码执行漏洞

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

# Splunk 修补关键漏洞，包括远程代码执行漏洞

阅读量**61112**

发布时间 : 2024-10-15 17:26:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/splunk-patches-critical-vulnerabilities-including-remote-code-execution-flaws/>

译文仅供参考，具体内容表达以及含义原文为准。

**![Splunk Enterprise - CVE-2024-45731 and CVE-2024-45733]()**

领先的数据分析和安全监控平台 Splunk 发布了一系列安全更新，以解决 Splunk Enterprise 和 Splunk Cloud Platform 中的多个漏洞。这些漏洞的严重程度不一，有些可实现远程代码执行（RCE），有些则允许低权限用户访问敏感信息。

**需要立即关注的严重 RCE 漏洞**

其中最严重的漏洞是 CVE-2024-45731 和 CVE-2024-45733，这两个漏洞都可能允许攻击者在易受攻击的系统上远程执行代码。CVE-2024-45731 特别影响 Splunk Enterprise 安装在单独磁盘上的 Windows 安装。利用此漏洞，攻击者可将恶意 DLL 文件写入 Windows 系统根目录，从而可能导致系统完全崩溃。CVE-2024-45733 源自不安全的会话存储配置，影响 9.2.3 和 9.1.6 以下 Windows 版本的 Splunk Enterprise。

**低权限用户构成重大威胁**

多个漏洞会授予低权限用户未经授权的访问权限和功能。CVE-2024-45732 允许这些用户在 SplunkDeploymentServerConfig 应用程序中以 “nobody ”用户身份运行搜索，从而可能暴露受限数据。其他漏洞使低权限用户能够

* 查看主机上的图像 (CVE-2024-45734)
* 访问 Splunk 安全网关应用程序中的敏感配置数据 (CVE-2024-45735)
* 崩溃 Splunk 守护进程 (CVE-2024-45736)
* 操纵应用程序密钥值存储的维护模式状态 (CVE-2024-45737)

**还解决了信息披露和跨站脚本 (XSS) 漏洞**

除 RCE 和权限升级漏洞外，Splunk 还修补了可能导致敏感信息泄露 (CVE-2024-45738 和 CVE-2024-45739) 和持续跨站脚本 (CVE-2024-45740 和 CVE-2024-45741) 的漏洞。利用这些漏洞可泄露敏感数据或向其他用户浏览的网页注入恶意脚本。

**Splunk 敦促用户立即更新**

Splunk 已发布更新以解决这些漏洞，并强烈建议所有用户升级到最新的 Splunk Enterprise 和 Splunk Cloud Platform 版本。公司还为无法立即升级的用户提供了缓解和解决策略。

**有关受影响版本的完整列表和每个漏洞的详细信息，请参阅 Splunk 安全咨询页面。**

本文翻译自securityonline [原文链接](https://securityonline.info/splunk-patches-critical-vulnerabilities-including-remote-code-execution-flaws/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300899](/post/id/300899)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/splunk-patches-critical-vulnerabilities-including-remote-code-execution-flaws/)

如若转载,请注明出处： <https://securityonline.info/splunk-patches-critical-vulnerabilities-including-remote-code-execution-flaws/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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