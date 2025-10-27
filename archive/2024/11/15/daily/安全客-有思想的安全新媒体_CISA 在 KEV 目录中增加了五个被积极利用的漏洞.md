---
title: CISA 在 KEV 目录中增加了五个被积极利用的漏洞
url: https://www.anquanke.com/post/id/301822
source: 安全客-有思想的安全新媒体
date: 2024-11-15
fetch_date: 2025-10-06T19:13:44.794177
---

# CISA 在 KEV 目录中增加了五个被积极利用的漏洞

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

# CISA 在 KEV 目录中增加了五个被积极利用的漏洞

阅读量**69453**

发布时间 : 2024-11-14 14:46:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/cisa-adds-five-actively-exploited-vulnerabilities-to-kev-catalog/>

译文仅供参考，具体内容表达以及含义原文为准。

![KEV Catalog]()

美国网络安全和基础设施安全局（CISA）扩充了其已知漏洞（KEV）目录，突出强调了目前在野外被利用的五个安全漏洞。这些漏洞横跨微软、思科、Atlassian 和 Metabase 产品，对处理敏感数据或暴露于公共网络的系统构成重大风险。

**1. CVE-2024-43451 (CVSS 6.5)： NTLM 哈希值泄露漏洞**

该漏洞因其触发简单而特别令人担忧。据微软称，与恶意文件的最小交互（如单击或右键单击操作）可能会将用户的 NTLMv2 哈希值暴露给远程攻击者。NTLM 哈希值是用户的加密凭据，攻击者可以通过它验证被攻击用户的身份，从而访问敏感资源。

**2. CVE-2024-49039 (CVSS 8.8)： Windows 任务调度程序权限提升漏洞**

由 Google 的威胁分析小组发现，此漏洞允许攻击者执行特制的应用程序，将权限从低完整性 AppContainer 环境提升到中完整性级别。这种权限升级可使攻击者运行通常仅限于高权限账户的 RPC 功能，从而在未经授权的情况下访问原本受保护的资源。

**3. CVE-2021-41277 (CVSS 10)： Metabase GeoJSON API 本地文件包含漏洞**

Metabase 是一个广泛使用的开源商业智能平台，它隐藏着一个关键漏洞，允许攻击者利用 GeoJSON API 进行本地文件包含。该漏洞可导致未经授权的数据访问和系统泄露，突出表明了及时进行软件更新和安全配置实践的重要性。

**4. CVE-2014-2120： Cisco ASA WebVPN 跨站脚本漏洞**

该漏洞存在于 Cisco Adaptive Security Appliance (ASA) 软件的 WebVPN 登录页面中，攻击者可利用该漏洞注入恶意脚本，从而可能泄露用户凭据并为会话劫持提供便利。这一遗留漏洞的持续存在强调了全面漏洞管理计划的重要性，以及解决所有系统漏洞（无论其使用年限长短）的必要性。

**5. CVE-2021-26086 (CVSS 5.3)： Atlassian Jira 服务器和数据中心路径遍历漏洞**

Atlassian Jira Server and Data Center 存在此漏洞，攻击者可利用路径遍历漏洞，在未经授权的情况下访问敏感文件。该漏洞凸显了安全编码实践的重要性，以及进行持续安全测试以识别和修复软件应用程序漏洞的必要性。

**减轻威胁**

CISA 要求联邦经济与商业委员会各机构在 2024 年 12 月 3 日前修补这些漏洞，这是对各行业组织优先进行漏洞管理的重要提醒。

本文翻译自securityonline [原文链接](https://securityonline.info/cisa-adds-five-actively-exploited-vulnerabilities-to-kev-catalog/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301822](/post/id/301822)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/cisa-adds-five-actively-exploited-vulnerabilities-to-kev-catalog/)

如若转载,请注明出处： <https://securityonline.info/cisa-adds-five-actively-exploited-vulnerabilities-to-kev-catalog/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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