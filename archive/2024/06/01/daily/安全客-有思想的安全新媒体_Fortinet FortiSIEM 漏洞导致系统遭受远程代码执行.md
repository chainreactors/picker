---
title: Fortinet FortiSIEM 漏洞导致系统遭受远程代码执行
url: https://www.anquanke.com/post/id/296970
source: 安全客-有思想的安全新媒体
date: 2024-06-01
fetch_date: 2025-10-06T16:55:23.945064
---

# Fortinet FortiSIEM 漏洞导致系统遭受远程代码执行

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

# Fortinet FortiSIEM 漏洞导致系统遭受远程代码执行

阅读量**105704**

发布时间 : 2024-05-31 10:56:14

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/fortinet-fortisiem-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

Fortinet FortiSIEM 最近发现多个漏洞，引发了人们对潜在远程代码执行漏洞的担忧。FortiSIEM 以其实时基础设施和用户感知功能而闻名，有助于精确检测、分析和报告威胁，但由于此 FortiSIEM 漏洞，它面临重大风险。

如果成功利用所发现的漏洞，远程攻击者就能够在受影响的服务帐户上下文中执行代码。

这可能导致一系列恶意活动，包括安装未经授权的程序、操纵数据，甚至创建具有广泛用户权限的新帐户。

**了解 Fortinet FortiSIEM 漏洞**
Fortinet FortiSIEM 漏洞的严重程度因受感染服务帐户的权限而异，其中管理帐户的风险最高。据SingCERT称， CVE-2024-23108和CVE-2023-34992 的概念验证漏洞已经可用，这表明对易受攻击的系统构成直接威胁。

Fortinet FortiSIEM 版本 7.1.0 至 7.1.1、7.0.0 至 7.0.2、6.7.0 至 6.7.8、6.6.0 至 6.6.3、6.5.0 至 6.5.2 以及 6.4.0 至 6.4.2 均受到这些漏洞的影响。

这些漏洞带来的风险因行业而异，大中型政府机构和企业面临的风险较高，而小型政府机构和企业面临的风险为中等。然而，家庭用户的风险暴露程度较低。

**FortiSIEM 漏洞技术分析**
对这些 FortiSIEM 漏洞进行技术分析后发现，该漏洞主要利用执行策略，具体针对命令和脚本解释器技术。在 FortiSIEM 管理器中已发现多起对 OS 命令中使用的特殊元素进行不当中和的情况。

这些漏洞可能被远程、未经身份验证的攻击者通过特制的 API 请求利用。为了减轻与这些 FortiSIEM 漏洞相关的风险，建议在经过全面测试后及时应用 FortiNet 提供的补丁。

其他措施包括为企业资产建立和维护记录在案的漏洞管理流程、定期执行自动应用程序更新、强制使用基于网络的 URL 过滤器来限制对潜在恶意网站的访问、为特权帐户管理实施最小特权原则、通过应用程序控制阻止未经授权的代码执行和脚本阻止、为企业资产和软件建立和维护安全配置流程，并根据企业的补救政策处理渗透测试结果。

通过遵循这些建议，组织可以有效地缓解 Fortinet FortiSIEM 中的漏洞，保护其系统免受潜在的远程代码执行攻击。利益相关者必须优先考虑这些行动，以确保其 IT 基础设施的安全性和完整性。

本文翻译自 [原文链接](https://thecyberexpress.com/fortinet-fortisiem-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296970](/post/id/296970)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/fortinet-fortisiem-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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