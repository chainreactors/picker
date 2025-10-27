---
title: 美国网络安全和基础设施安全局 (CISA) 在其已知漏洞目录中增加了 Windows 内核、Mozilla Firefox 和 SolarWinds Web Help Desk 漏洞。
url: https://www.anquanke.com/post/id/300995
source: 安全客-有思想的安全新媒体
date: 2024-10-18
fetch_date: 2025-10-06T18:49:59.113431
---

# 美国网络安全和基础设施安全局 (CISA) 在其已知漏洞目录中增加了 Windows 内核、Mozilla Firefox 和 SolarWinds Web Help Desk 漏洞。

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

# 美国网络安全和基础设施安全局 (CISA) 在其已知漏洞目录中增加了 Windows 内核、Mozilla Firefox 和 SolarWinds Web Help Desk 漏洞。

阅读量**83410**

发布时间 : 2024-10-17 11:05:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/169882/hacking/u-s-cisa-microsoft-windows-kernel-mozilla-firefox-solarwinds-web-help-desk-bugs-known-exploited-vulnerabilities-catalog.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全和基础设施安全局 (CISA) 在其已知漏洞 (KEV) 目录中添加了以下漏洞：

* CVE-2024-30088 (CVSS 得分为 7.0) Microsoft Windows 内核 TOCTOU 竞赛条件漏洞
* CVE-2024-9680 Mozilla Firefox Use-After-Free 漏洞
* CVE-2024-28987 (CVSS 得分 9.1) SolarWinds Web Help Desk 硬编码凭证漏洞

攻击者可利用漏洞 CVE-2024-30088 获得 SYSTEM 权限。成功利用此漏洞需要攻击者赢得竞赛条件。

上周，Mozilla 为 Firefox 浏览器发布了一个紧急安全更新，以解决在攻击中被积极利用的关键免用漏洞 CVE-2024-9680。

CVE-2024-9680 漏洞存在于动画时间轴中。Firefox 动画时间轴是 Firefox 开发人员工具套件中的一项功能，允许开发人员直接在浏览器中检查、编辑和调试动画。它提供了一个可视化界面来管理动画，包括 CSS 动画和过渡效果，以及使用 Web Animations API 创建的动画。

攻击者可利用此漏洞在内容进程中执行代码。

SolarWinds 于 8 月份解决了 CVE-2024-28987 漏洞，该漏洞可允许未经身份验证的远程攻击者在未经授权的情况下访问易受攻击的实例。

SolarWinds 将 WHD 描述为一款经济实惠的帮助台票务和资产管理软件，被大型企业和政府组织广泛使用。

该公司发布的公告中写道：“SolarWinds Web Help Desk (WHD) 软件受到一个硬编码凭证漏洞的影响，允许未经身份验证的远程用户访问内部功能和修改数据。”

根据具有约束力的操作指令 (BOD) 22-01： 减少已知漏洞被利用的重大风险》，联邦经济与商业委员会各机构必须在规定日期前解决已发现的漏洞，以保护其网络免受利用目录中漏洞的攻击。

专家还建议私营机构审查目录并解决其基础设施中的漏洞。

CISA 命令联邦机构在 2024 年 11 月 5 日前修复该漏洞。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/169882/hacking/u-s-cisa-microsoft-windows-kernel-mozilla-firefox-solarwinds-web-help-desk-bugs-known-exploited-vulnerabilities-catalog.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300995](/post/id/300995)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/169882/hacking/u-s-cisa-microsoft-windows-kernel-mozilla-firefox-solarwinds-web-help-desk-bugs-known-exploited-vulnerabilities-catalog.html)

如若转载,请注明出处： <https://securityaffairs.com/169882/hacking/u-s-cisa-microsoft-windows-kernel-mozilla-firefox-solarwinds-web-help-desk-bugs-known-exploited-vulnerabilities-catalog.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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