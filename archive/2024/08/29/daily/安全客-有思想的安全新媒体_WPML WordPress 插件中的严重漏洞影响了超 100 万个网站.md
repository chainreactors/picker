---
title: WPML WordPress 插件中的严重漏洞影响了超 100 万个网站
url: https://www.anquanke.com/post/id/299564
source: 安全客-有思想的安全新媒体
date: 2024-08-29
fetch_date: 2025-10-06T17:59:19.798667
---

# WPML WordPress 插件中的严重漏洞影响了超 100 万个网站

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

# WPML WordPress 插件中的严重漏洞影响了超 100 万个网站

阅读量**57346**

发布时间 : 2024-08-28 12:52:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/167673/hacking/wpml-wordpress-plugin-rce-1m-websites.html>

译文仅供参考，具体内容表达以及含义原文为准。

## 安装在 100 万个网站上的 WPML WordPress 插件中的一个严重缺陷可能允许受影响的网站受到威胁。

适用于 WordPress 的 WPML 多语言 CMS 插件安装在超过 100 万个网站上。WPML 插件中经过身份验证的 （Contributor+） 远程代码执行 （RCE） 漏洞，跟踪 CVE-2024-6386（CVSS 评分为 9.9），可能允许入侵受影响的网站。

WPML 使构建和运行多语言网站变得容易。

“漏洞在于 WPML 插件中短代码的处理。具体来说，该插件使用 Twig 模板以短代码呈现内容，但未能正确清理输入，从而导致服务器端模板注入 （SSTI）。研究人员 Secretthcopter 发布的**一份报告**写道，该研究人员通过 Wordfence 漏洞赏金计划发现并负责任地报告了此问题。研究人员因这一发现获得了 1,639.00 美元的赏金。

WPML WordPress 插件依赖 Twig 模板来渲染短代码内容，但无法正确清理输入，从而导致服务器端模板注入 （SSTI） 漏洞。此漏洞可用于远程代码执行 （RCE），研究人员发布的概念验证 （PoC） 代码证明了这一点。

“这个漏洞是模板引擎中输入清理不当危险的一个典型例子。开发人员应始终清理和验证用户输入，尤其是在处理动态内容渲染时。这个案例提醒我们，安全是一个持续的过程，需要在开发和数据处理的每个阶段保持警惕。

该漏洞会影响 4.6.13 之前的插件版本

然而，该插件的维护者 OnTheGoSystems 淡化了这个问题，称该漏洞在现实世界中很难利用。

*“此 WPML 版本修复了一个安全漏洞，该漏洞可能允许具有特定权限的用户执行未经授权的操作。这个问题在现实世界中不太可能发生。OnTheGoSystems wrotes.“它要求用户在 WordPress 中具有编辑权限，并且该网站必须使用非常具体的设置，”*

*“考虑到此漏洞的严重性，我们鼓励 WordPress 用户尽快验证他们的网站是否已更新到 WPML 的最新补丁版本。”*

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/167673/hacking/wpml-wordpress-plugin-rce-1m-websites.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299564](/post/id/299564)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/167673/hacking/wpml-wordpress-plugin-rce-1m-websites.html)

如若转载,请注明出处： <https://securityaffairs.com/167673/hacking/wpml-wordpress-plugin-rce-1m-websites.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [安装在 100 万个网站上的 WPML WordPress 插件中的一个严重缺陷可能允许受影响的网站受到威胁。](#h2-0)

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