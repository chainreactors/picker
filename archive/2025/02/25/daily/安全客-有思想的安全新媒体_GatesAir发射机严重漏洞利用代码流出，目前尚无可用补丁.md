---
title: GatesAir发射机严重漏洞利用代码流出，目前尚无可用补丁
url: https://www.anquanke.com/post/id/304699
source: 安全客-有思想的安全新媒体
date: 2025-02-25
fetch_date: 2025-10-06T20:34:15.119246
---

# GatesAir发射机严重漏洞利用代码流出，目前尚无可用补丁

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

# GatesAir发射机严重漏洞利用代码流出，目前尚无可用补丁

阅读量**87797**

发布时间 : 2025-02-24 14:47:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/exploit-code-published-for-critical-gatesair-transmitter-vulnerabilities-no-patches-available-yet/>

译文仅供参考，具体内容表达以及含义原文为准。

![GatesAir Maxiva UAXT]()

安全研究员Mohamed Shahat披露了影响GatesAir Maxiva UAXT 和 VAXT 发射机的三个严重漏洞。这些广泛部署的发射机应用于包括广播、交通和公共安全等多个行业。一旦这些漏洞被利用，可能会产生严重后果，从会话劫持、数据泄露到系统完全被攻破。

**这些漏洞如下：**

****1.CVE – 2025 – 22960（会话劫持）****：此漏洞使未经身份验证的攻击者能够访问暴露的日志文件，有可能泄露与会话相关的敏感信息，如会话 ID 和身份验证令牌。攻击者可利用这一缺陷劫持活动会话，获取未经授权的访问权限，并在受影响设备上提升权限。

****2.CVE – 2025 – 22961（数据泄露）****：攻击者可通过公开暴露的 URL 直接访问敏感的数据库备份文件（db）。这一漏洞可能导致敏感用户数据被获取，包括登录凭据，进而可能导致系统完全被攻破。

****3.CVE – 2025 – 22962（远程代码执行）****：当调试模式启用时，拥有有效会话 ID 的攻击者可以发送特制的 POST 请求，在底层系统上执行任意命令。这个严重漏洞可能导致系统完全被攻破，包括未经授权的访问、权限提升，甚至可能完全控制设备。

**概念验证漏洞利用代码已发布：**

更严重的是，Shahat已经发布了概念验证漏洞利用代码，这使得恶意行为者更容易利用这些漏洞。这凸显了立即采取行动降低风险的紧迫性。

**缓解措施：**

GatesAir尚未发布针对这些漏洞的补丁。在此期间，建议使用受影响发射机的组织采取以下防御措施：

1.限制对敏感日志文件和目录的访问。

2.对日志和备份文件设置严格的文件权限。

3.避免记录与会话相关的敏感数据。

4.在存储前对敏感数据进行加密。

5.在生产环境中禁用调试模式。

6.实施更强大的身份验证和会话管理。

7.定期对系统及其文件处理流程进行安全审计。

强烈建议使用GatesAir Maxiva UAXT 和 VAXT 发射机的组织立即采取行动，保护其关键基础设施免受潜在攻击。

本文翻译自securityonline [原文链接](https://securityonline.info/exploit-code-published-for-critical-gatesair-transmitter-vulnerabilities-no-patches-available-yet/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304699](/post/id/304699)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/exploit-code-published-for-critical-gatesair-transmitter-vulnerabilities-no-patches-available-yet/)

如若转载,请注明出处： <https://securityonline.info/exploit-code-published-for-critical-gatesair-transmitter-vulnerabilities-no-patches-available-yet/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

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