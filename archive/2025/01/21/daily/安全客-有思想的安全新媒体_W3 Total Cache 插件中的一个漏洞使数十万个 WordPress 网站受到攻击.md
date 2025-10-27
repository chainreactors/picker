---
title: W3 Total Cache 插件中的一个漏洞使数十万个 WordPress 网站受到攻击
url: https://www.anquanke.com/post/id/303621
source: 安全客-有思想的安全新媒体
date: 2025-01-21
fetch_date: 2025-10-06T20:08:11.500887
---

# W3 Total Cache 插件中的一个漏洞使数十万个 WordPress 网站受到攻击

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

# W3 Total Cache 插件中的一个漏洞使数十万个 WordPress 网站受到攻击

阅读量**55454**

发布时间 : 2025-01-20 09:42:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/173219/security/w3-total-cache-wordpress-plugin-cve-2024-12365.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**一个 WordPress W3 Total Cache 插件漏洞可能允许攻击者访问内部服务的信息，包括基于云的应用程序的元数据。**

WordPress W3 Total Cache 插件存在一个严重漏洞（CVE-2024-12365，CVSS 得分 8.5），可能会暴露内部服务和云应用程序的元数据。

WordPress W3 Total Cache 插件是一款流行的性能优化工具，旨在提高 WordPress 网站的速度和效率。该插件已安装在 100 多万个 WordPress 网站上，网站所有者使用该插件来增强用户体验、提高搜索引擎优化排名并减少服务器负载。

该漏洞允许拥有 Subscriber 访问权限的验证攻击者利用缺失的能力检查，导致信息泄露。该漏洞影响的插件版本最高可达 2.8.1。

该问题允许通过身份验证的用户（订户级或更高）利用缺失的能力检查，从而暴露敏感数据、消耗服务限制和访问内部服务，包括云应用程序元数据。

WordPress 发布的公告中写道：“WordPress 的 W3 Total Cache 插件存在未经授权访问数据的漏洞，原因是在 2.8.1 及以下的所有版本中，is\_w3tc\_admin\_page 函数的能力检查缺失。这使得拥有 Subscriber 级及以上访问权限的经过验证的攻击者有可能获取插件的 nonce 值并执行未经授权的操作，从而导致信息泄露、服务计划限制消耗以及向源自网络应用程序的任意位置发出网络请求，这些请求可用于查询内部服务的信息，包括基于云的应用程序上的实例元数据。”

尽管提供了安全补丁，但仍有数十万网站尚未升级到最新版本 2.8.2。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/173219/security/w3-total-cache-wordpress-plugin-cve-2024-12365.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303621](/post/id/303621)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/173219/security/w3-total-cache-wordpress-plugin-cve-2024-12365.html)

如若转载,请注明出处： <https://securityaffairs.com/173219/security/w3-total-cache-wordpress-plugin-cve-2024-12365.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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