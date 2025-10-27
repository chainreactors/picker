---
title: Fortinet 发布未公开的 FortiManager 严重漏洞补丁
url: https://www.anquanke.com/post/id/301126
source: 安全客-有思想的安全新媒体
date: 2024-10-23
fetch_date: 2025-10-06T18:48:33.064676
---

# Fortinet 发布未公开的 FortiManager 严重漏洞补丁

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

# Fortinet 发布未公开的 FortiManager 严重漏洞补丁

阅读量**60757**

发布时间 : 2024-10-22 10:37:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2024/10/21/fortimanager-critical-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

最近几天，Fortinet 发布了 FortiManager 的重要安全更新，以修复一个据说被中国威胁者利用的重要漏洞。

**安全更新正在陆续推出**

众所周知，Fortinet 会在向公众披露关键漏洞之前发布修复程序，该公司已在一周前私下通知了部分客户，并分享了临时缓解建议。

建议显然包括配置 FortiManager，防止序列号未知的设备（即未经授权的设备）注册/连接到它们。

限制对 FortiManager 安装的访问通常也是个好主意，但一旦发布补丁，实施补丁是必不可少的。Fortinet 的支持门户网站已经提供了一些补丁。

**没有 CVE，没有详细信息（目前）**

尽管建议的缓解措施可能表明问题存在于 “Fortigate to FortiManager”（fgfm）连接/通信/管理功能中，但该公司尚未公开披露与此漏洞相关的详细信息或 CVE。

至于它是否与 CVE-2024-23113 有关（CVE-2024-23113 是一个影响 FortiOS fgfm 守护进程的格式字符串漏洞），还有待推测。

今年早些时候，FortiOS、FortiPAM、FortiProxy 和 FortiWeb 对 CVE-2024-23113 进行了修补。10 月初，CISA 证实攻击者正在利用该漏洞。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2024/10/21/fortimanager-critical-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301126](/post/id/301126)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2024/10/21/fortimanager-critical-vulnerability/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/10/21/fortimanager-critical-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

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