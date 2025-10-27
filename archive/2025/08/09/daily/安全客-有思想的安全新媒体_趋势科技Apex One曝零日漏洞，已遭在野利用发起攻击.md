---
title: 趋势科技Apex One曝零日漏洞，已遭在野利用发起攻击
url: https://www.anquanke.com/post/id/310953
source: 安全客-有思想的安全新媒体
date: 2025-08-09
fetch_date: 2025-10-07T00:17:41.348552
---

# 趋势科技Apex One曝零日漏洞，已遭在野利用发起攻击

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

# 趋势科技Apex One曝零日漏洞，已遭在野利用发起攻击

阅读量**68014**

发布时间 : 2025-08-08 16:58:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-endpoint-protection-zero-day-exploited-in-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

趋势科技近日警告用户，需立即加强防护，防范其终端安全平台 Apex One 中一个正被积极利用的远程代码执行漏洞。

**Apex One 是一款面向企业的终端安全平台，可自动检测和响应各类威胁，包括恶意工具、恶意软件和系统漏洞。**

该严重漏洞（**根据 CPU 架构分别编号为 CVE-2025-54948 和 CVE-2025-54987**）源于 Apex One 本地部署版本管理控制台存在命令注入漏洞，允许未经身份验证的攻击者远程在运行未打补丁软件的系统上执行任意代码。

目前，趋势科技尚未发布用于修复此漏洞的正式安全更新，但已提供一款缓解工具，用于临时防止漏洞被利用。

日本计算机应急响应小组（JPCERT）也发布了相关安全警报，确认上述两个漏洞正在遭受攻击，并敦促用户尽快采取缓解措施。

“虽然该缓解工具可以完全防御已知的漏洞利用行为，但会导致管理员无法通过 Apex One 管理控制台使用远程安装代理（Remote Install Agent）功能部署终端代理程序。”趋势科技在周二发布的安全公告中表示。

趋势科技已观测到至少一次针对该漏洞的野外攻击尝试。

### **安全补丁预计于 8 月中旬发布**

该公司表示，将在 2025 年 8 月中旬左右发布安全补丁，届时也将恢复被缓解工具临时禁用的远程安装代理功能。

在安全补丁正式发布前，趋势科技敦促管理员尽快保护易受攻击的终端，即便这意味着需要暂时放弃远程管理功能。

“就此次漏洞而言，攻击者必须能够访问 Apex One 管理控制台。因此，控制台 IP 地址暴露于公网的客户，若尚未实施源地址限制等安全措施，应立即进行加固。”趋势科技补充道。

“尽管漏洞利用可能需要满足多个特定条件，趋势科技仍强烈建议客户尽快升级至最新版本。”

趋势科技此前曾修复另外两个 Apex One 零日漏洞，其中一个在 2022 年 9 月被利用于野外攻击（**CVE-2022-40139**），另一个则于 2023 年 9 月被修复（**CVE-2023-41179**）。

此外，该公司还在本月早些时候修复了多个影响 **Apex Central** 和 **Endpoint Encryption（TMEE）PolicyServer** 产品的严重远程代码执行和身份验证绕过漏洞。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-endpoint-protection-zero-day-exploited-in-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310953](/post/id/310953)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-endpoint-protection-zero-day-exploited-in-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-endpoint-protection-zero-day-exploited-in-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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