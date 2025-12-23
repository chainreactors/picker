---
title: n8n 深陷危机：CVSS 10.0 严重远程代码执行漏洞致服务器完全受控
url: https://www.anquanke.com/post/id/313920
source: 安全客-有思想的安全新媒体
date: 2025-12-22
fetch_date: 2025-12-23T03:23:54.735239
---

# n8n 深陷危机：CVSS 10.0 严重远程代码执行漏洞致服务器完全受控

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

# n8n 深陷危机：CVSS 10.0 严重远程代码执行漏洞致服务器完全受控

阅读量**14864**

发布时间 : 2025-12-22 16:28:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源： securityonline

原文地址：<https://securityonline.info/n8n-under-fire-critical-cvss-10-0-rce-vulnerability-grants-total-server-access/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

广受欢迎的工作流自动化工具 n8n 在发现一处可能允许攻击者**完全控制平台**的漏洞后，发布了**严重安全警报**。该漏洞编号为 **CVE-2025-68613**，被评定为 CVSS 最高分值 **10.0 分**，这意味着未打补丁的实例将面临**直接且灾难性的风险**。

该漏洞被描述为 “通过表达式注入实现的远程代码执行（Remote Code Execution, RCE）”，它将 n8n 平台的最大优势 ——**灵活性**，转化成了一项**关键弱点**。

n8n 深受技术团队青睐，因其能 “为技术团队提供代码级的灵活性，同时兼具无代码工具的高效性”。而这种灵活性的实现，依赖于在工作流配置过程中**动态表达式评估能力**。

根据安全公告，漏洞存在于这一 “工作流表达式评估系统” 中。在特定条件下，已认证用户提供的表达式会 “在与底层运行时**未充分隔离**的执行环境中被评估”。

简单来说，本应用于限制这些用户自定义脚本的**安全沙箱存在漏洞**。攻击者只要能够登录并配置工作流，就能注入恶意代码，突破 n8n 应用环境的限制，**直接在服务器上执行**。

由于注入的代码会以 **n8n 进程自身的权限** 运行，一旦利用成功，攻击者将获得服务器的 “完全控制权”。

安全公告警告称，漏洞利用可能导致 “受影响实例**完全被攻陷**”，具体包括：

* 数据窃取（Data Theft）：“非法访问敏感数据”；
* 恶意破坏（Sabotage）：“篡改工作流”；
* 服务器接管（Server Takeover）：“执行系统级操作”。

鉴于 n8n 通常处于企业技术栈的**核心位置**—— 连接数据库、客户关系管理系统（CRM）和应用程序接口（API），此处被攻陷可能会为攻击者提供便利，实现**全网横向渗透**。

n8n 维护团队已在 **n8n v1.122.0 版本** 中发布修复补丁，并强烈敦促所有用户**立即升级**，以获得 “限制表达式评估的额外安全防护措施”。

对于无法立即下线平台进行升级的企业，官方提供了两项临时缓解方案，但需注意这些方案 “**无法完全消除风险**”：

* 限制访问权限（Restrict Access）：“仅向完全信任的用户开放工作流创建和编辑权限”。由于攻击需要攻击者具备认证权限，此举可缩小攻击面；
* 强化运行环境（Harden the Environment）：在严格管控的环境中部署 n8n，限制其操作系统权限，并缩减网络访问范围，以在漏洞被利用时最大程度降低影响范围。

编辑分享

润色一下这段翻译，让它更符合中文表达习惯

请再提供一些关于n8n的信息。

除了n8n，还有哪些类似的工作流自动化工具？

本文翻译自 securityonline [原文链接](https://securityonline.info/n8n-under-fire-critical-cvss-10-0-rce-vulnerability-grants-total-server-access/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313920](/post/id/313920)

安全KER - 有思想的安全新媒体

本文转载自:  [securityonline](https://securityonline.info/n8n-under-fire-critical-cvss-10-0-rce-vulnerability-grants-total-server-access/)

如若转载,请注明出处： <https://securityonline.info/n8n-under-fire-critical-cvss-10-0-rce-vulnerability-grants-total-server-access/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **840**

* 粉丝
* **6**

### TA的文章

* ##### [电视中的 “狼”：规模达 180 万的 Kimwolf 僵尸网络流量超谷歌，称霸物联网领域](/post/id/313933)

  2025-12-22 16:32:27
* ##### [“脚本麻雀” 组织利用自动化技术生成并发送攻击邮件](/post/id/313954)

  2025-12-22 16:32:15
* ##### [黑客窃取数百万 PornHub 用户数据用于敲诈勒索](/post/id/313929)

  2025-12-22 16:31:50
* ##### [黑客发起定向钓鱼攻击，HubSpot 用户成攻击目标](/post/id/313948)

  2025-12-22 16:31:30
* ##### [微软发布紧急带外更新修复影响 IIS 站点的 MSMQ 漏洞](/post/id/313944)

  2025-12-22 16:30:34

### 相关文章

* ##### [电视中的 “狼”：规模达 180 万的 Kimwolf 僵尸网络流量超谷歌，称霸物联网领域](/post/id/313933)

  2025-12-22 16:32:27
* ##### [“脚本麻雀” 组织利用自动化技术生成并发送攻击邮件](/post/id/313954)

  2025-12-22 16:32:15
* ##### [黑客窃取数百万 PornHub 用户数据用于敲诈勒索](/post/id/313929)

  2025-12-22 16:31:50
* ##### [黑客发起定向钓鱼攻击，HubSpot 用户成攻击目标](/post/id/313948)

  2025-12-22 16:31:30
* ##### [微软发布紧急带外更新修复影响 IIS 站点的 MSMQ 漏洞](/post/id/313944)

  2025-12-22 16:30:34
* ##### [微软为 Office、SharePoint、Exchange、Teams 及 Entra 推出基线安全模式](/post/id/313926)

  2025-12-22 16:30:11
* ##### [人工智能超级应用横空出世：OpenAI 推出 ChatGPT 应用目录，剑指数字生活核心入口](/post/id/313938)

  2025-12-22 16:29:53

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