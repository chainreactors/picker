---
title: Palo Alto Networks 证实积极利用最近披露的零日漏洞
url: https://www.anquanke.com/post/id/301988
source: 安全客-有思想的安全新媒体
date: 2024-11-20
fetch_date: 2025-10-06T19:15:08.832316
---

# Palo Alto Networks 证实积极利用最近披露的零日漏洞

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

# Palo Alto Networks 证实积极利用最近披露的零日漏洞

阅读量**49465**

发布时间 : 2024-11-19 14:13:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/171057/hacking/palo-alto-networks-zero-day-exploitation.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**Palo Alto Networks 证实其 PAN-OS 防火墙中的零日漏洞正在被利用，并发布了新的入侵指标（IoCs）。**

上周，由于 PAN-OS 中存在一个潜在的远程代码执行漏洞（CVSSv4.0 基础分：9.3），Palo Alto Networks 警告客户限制对其下一代防火墙管理界面的访问。该网络安全公司没有关于该漏洞的更多细节，也未发现有人在利用该漏洞。

“Palo Alto Networks 发现 PAN-OS 管理界面存在远程代码执行漏洞。目前，我们尚不清楚该漏洞的具体情况。我们正在积极监控任何利用迹象。我们强烈建议客户确保按照我们推荐的最佳实践部署指南正确配置对管理界面的访问。特别是，我们建议您确保只能从受信任的内部 IP 而不是从互联网访问管理界面。绝大多数防火墙已经遵循了 Palo Alto Networks 和行业最佳实践。”

Palo Alto Networks 建议审查确保设备管理访问安全的最佳实践。

确保 Palo Alto 管理界面安全的准则包括：将其隔离在专用管理 VLAN 上，使用跳转服务器进行访问，将入站 IP 地址限制在经批准的管理设备上，以及只允许安全通信（SSH、HTTPS）和 PING 进行连接测试。

该网络安全公司表示，它没有足够的信息表明存在任何入侵迹象。

现在，该公司证实，其 PAN-OS 防火墙管理界面中的零日漏洞已在野外被积极利用，并发布了入侵指标（IoCs）。

“Palo Alto Networks 发现有威胁活动利用一个未经验证的远程命令执行漏洞，对暴露在互联网上的有限数量的防火墙管理界面进行攻击。我们正在积极调查这一活动。”

“我们强烈建议客户确保按照我们推荐的最佳实践部署指南正确配置对管理界面的访问。特别是，我们建议您立即确保只能从受信任的内部 IP 访问管理界面，而不能从互联网访问。绝大多数防火墙已经遵循了 Palo Alto Networks 和行业最佳实践。”

网络安全公司观察到来自以下 IP 地址的恶意活动

* 136.144.17[.]\*
* 173.239.218[.]251
* 216.73.162[.]\*

公告指出，这些 IP 地址可能与 VPN 服务有关，因此也与合法用户活动有关。

Palo Alto 指出，该零日漏洞已被利用，在受攻击设备上部署了 Web Shell，允许持续远程访问。CVE 正在等待分配。

“我们发现了一个校验和为 3C5F9034C86CB1952AA5BB07B4F77CE7D8BB5CC9FE5C029A32C72ADC7E814668 的 web shell。”

限制对特定 IP 的管理界面访问可大大降低利用风险，但首先需要特权访问。在这种情况下，CVSS 得分为 7.5（高）。

本周，美国网络安全和基础设施安全局（CISA）在其已知漏洞（KEV）目录中增加了以下 Palo Alto Expedition 漏洞：

* CVE-2024-9463 Palo Alto Networks Expedition 操作系统命令注入漏洞
* CVE-2024-9465 Palo Alto Networks Expedition SQL 注入漏洞

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/171057/hacking/palo-alto-networks-zero-day-exploitation.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301988](/post/id/301988)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/171057/hacking/palo-alto-networks-zero-day-exploitation.html)

如若转载,请注明出处： <https://securityaffairs.com/171057/hacking/palo-alto-networks-zero-day-exploitation.html>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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