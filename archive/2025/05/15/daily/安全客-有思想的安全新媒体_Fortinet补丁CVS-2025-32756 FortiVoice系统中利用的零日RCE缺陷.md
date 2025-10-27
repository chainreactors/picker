---
title: Fortinet补丁CVS-2025-32756 FortiVoice系统中利用的零日RCE缺陷
url: https://www.anquanke.com/post/id/307359
source: 安全客-有思想的安全新媒体
date: 2025-05-15
fetch_date: 2025-10-06T22:23:26.295024
---

# Fortinet补丁CVS-2025-32756 FortiVoice系统中利用的零日RCE缺陷

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

# Fortinet补丁CVS-2025-32756 FortiVoice系统中利用的零日RCE缺陷

阅读量**62124**

发布时间 : 2025-05-14 15:21:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/05/fortinet-patches-cve-2025-32756-zero.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Fortinet 修补了一个严重的安全漏洞，据称该漏洞已被利用为针对 FortiVoice 企业电话系统的零日攻击。

该漏洞被跟踪为 CVE-2025-32756，CVSS 评分为 9.6 分（满分 10.0 分）。

该公司在一份公告中[表示](https://fortiguard.fortinet.com/psirt/FG-IR-25-254)：“FortiVoice、FortiMail、FortiNDR、FortiRecorder 和 FortiCamera 中基于堆栈的溢出漏洞 [CWE-121] 可能允许未经身份验证的远程攻击者通过精心设计的 HTTP 请求执行任意代码或命令。

该公司表示，它观察到该漏洞在 FortiVoice 系统上被广泛利用，但没有透露攻击的规模及其背后的威胁行为者的身份。

它进一步指出，威胁行为者执行了设备网络扫描，擦除了系统崩溃日志，并启用了 fcgi 调试以记录来自系统或 SSH 登录尝试的凭据。

此问题影响以下产品和版本 –

* FortiCamera 1.1、2.0（迁移到固定版本）
* FortiCamera 2.1.x （升级至 2.1.4 或以上版本）
* FortiMail 7.0.x （升级到 7.0.9 或更高版本）
* FortiMail 7.2.x （升级至 7.2.8 或以上版本）
* FortiMail 7.4.x （升级到 7.4.5 或更高版本）
* FortiMail 7.6.x （升级至 7.6.3 或以上）
* FortiNDR 1.1、1.2、1.3、1.4、1.5、7.1（迁移到固定版本）
* FortiNDR 7.0.x（升级到 7.0.7 或更高版本）
* FortiNDR 7.2.x（升级到 7.2.5 或更高版本）
* FortiNDR 7.4.x（升级到 7.4.8 或更高版本）
* FortiNDR 7.6.x（升级到 7.6.1 或更高版本）
* FortiRecorder 6.4.x（升级到 6.4.6 或更高版本）
* FortiRecorder 7.0.x（升级到 7.0.6 或更高版本）
* FortiRecorder 7.2.x（升级到 7.2.4 或更高版本）
* FortiVoice 6.4.x （升级至 6.4.11 或以上版本）
* FortiVoice 7.0.x （升级到 7.0.7 或更高版本）
* FortiVoice 7.2.x （升级到 7.2.1 或更高版本）

Fortinet 表示，该漏洞是由其产品安全团队根据源自以下 IP 地址的威胁行为者活动发现的 –

* 198.105.127.124
* 43.228.217.173
* 43.228.217.82
* 156.236.76.90
* 218.187.69.244
* 218.187.69.59

建议 FortiVoice、FortiMail、FortiNDR、FortiRecorder 和 FortiCamera 的用户应用必要的修复程序，以保护其设备免受主动利用尝试。如果无法立即修补，建议禁用 HTTP/HTTPS 管理界面作为临时解决方法。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/05/fortinet-patches-cve-2025-32756-zero.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307359](/post/id/307359)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/05/fortinet-patches-cve-2025-32756-zero.html)

如若转载,请注明出处： <https://thehackernews.com/2025/05/fortinet-patches-cve-2025-32756-zero.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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