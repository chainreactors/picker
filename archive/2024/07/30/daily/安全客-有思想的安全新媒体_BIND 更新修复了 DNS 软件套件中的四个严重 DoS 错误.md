---
title: BIND 更新修复了 DNS 软件套件中的四个严重 DoS 错误
url: https://www.anquanke.com/post/id/298541
source: 安全客-有思想的安全新媒体
date: 2024-07-30
fetch_date: 2025-10-06T17:40:51.440962
---

# BIND 更新修复了 DNS 软件套件中的四个严重 DoS 错误

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

# BIND 更新修复了 DNS 软件套件中的四个严重 DoS 错误

阅读量**91410**

发布时间 : 2024-07-29 14:59:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/166190/security/bind-updates-high-severity-dos-bugs.html>

译文仅供参考，具体内容表达以及含义原文为准。

Internet Systems Consortium （ISC） 发布了 BIND 的安全更新，解决了可能被远程利用的 DoS 漏洞。攻击者可以利用这些漏洞来破坏 DNS 服务。

ISC 解决了四个高严重性漏洞（CVSS 评分为 7.5），分别跟踪为 CVE-2024-0760、CVE-2024-1737、CVE-2024-1975 和 CVE-2024-4076。

以下是美国网络安全机构CISA发布的**公告**中对上述问题的描述：

BIND 9 中的漏洞 CVE-2024-4076 在提供过时数据以及本地权威区域数据中的查找时，可导致断言失败。此问题会影响特定版本，包括 9.16.13 到 9.16.50、9.18.0 到 9.18.27、9.19.0 到 9.19.24、9.11.33-S1 到 9.11.37-S1、9.16.13-S1 到 9.16.50-S1 和 9.18.11-S1 到 9.18.27-S1。

BIND 9 中的漏洞 CVE-2024-1975 允许客户端通过发送 SIG（0） 签名的请求流来耗尽 CPU 资源，前提是服务器托管了“KEY”资源记录，或者解析器 DNSSEC 在缓存中验证了此类记录。该漏洞影响 BIND 9 版本 9.0.0 到 9.11.37、9.16.0 到 9.16.50、9.18.0 到 9.18.27、9.19.0 到 9.19.24、9.9.3-S1 到 9.11.37-S1、9.16.8-S1 到 9.16.49-S1 和 9.18.11-S1 到 9.18.27-S1

当解析器缓存或权威区域数据库包含同一主机名的许多资源记录 （RR） 时，可能会发生 BIND 9 中的性能问题（跟踪为 CVE-2024-1737）。该缺陷会影响内容的添加或更新以及客户端查询的处理。受影响的 BIND 9 版本包括 9.11.0 到 9.11.37、9.16.0 到 9.16.50、9.18.0 到 9.18.27、9.19.0 到 9.19.24 以及某些 9.11.4-S1、9.16.8-S1 和 9.18.11-S1 系列版本。

在 BIND 9 版本 9.18.1 到 9.18.27、9.19.0 到 9.19.24 和 9.18.11-S1 到 9.18.27-S1 中，存在一个被跟踪为 CVE-2024-0760 的漏洞，其中恶意客户端可以通过 TCP 发送大量 DNS 消息，从而可能在攻击期间破坏服务器的稳定性。一旦攻击停止，服务器就可以恢复。使用访问控制列表 （ACL） 无法缓解此问题

ISC 不知道这些漏洞的公开漏洞或在野外利用这些漏洞的攻击。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/166190/security/bind-updates-high-severity-dos-bugs.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298541](/post/id/298541)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/166190/security/bind-updates-high-severity-dos-bugs.html)

如若转载,请注明出处： <https://securityaffairs.com/166190/security/bind-updates-high-severity-dos-bugs.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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