---
title: 威胁行为者积极利用 ServiceNow RCE 漏洞来窃取凭证
url: https://www.anquanke.com/post/id/298537
source: 安全客-有思想的安全新媒体
date: 2024-07-30
fetch_date: 2025-10-06T17:40:49.675972
---

# 威胁行为者积极利用 ServiceNow RCE 漏洞来窃取凭证

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

# 威胁行为者积极利用 ServiceNow RCE 漏洞来窃取凭证

阅读量**79901**

发布时间 : 2024-07-29 15:00:01

**x**

##### 译文声明

本文是翻译文章，文章来源：heimdalsecurity

原文地址：<https://heimdalsecurity.com/blog/servicenow-rce-flaws/>

译文仅供参考，具体内容表达以及含义原文为准。

威胁行为者正在利用公开的漏洞将 ServiceNow 漏洞链接在一起，以便在数据盗窃活动中渗透到政府组织和商业公司。

安全研究人员监控了恶意活动并确定了多个受害者，包括政府机构、数据中心、能源供应商，甚至软件开发公司。

尽管该公司于 2024 年 7 月 10 日通过安全升级修复了这些漏洞，但数以万计的系统仍可能受到入侵。

ServiceNow 是一个被广泛采用的基于云的平台，可帮助组织管理企业运营的数字工作流程。它被各行各业的公司使用，包括公共部门组织、医疗保健、金融机构和大型企业。

## 有关利用的详细信息

ServiceNow 于 2024 年 7 月 10 日提供了针对 CVE-2024-4879 的修补程序，CVE-2024-4879 是一个主要（CVSS 评分：9.3）输入验证漏洞，允许未经授权的用户在各种 Now Platform 版本上远程执行代码。

第二天，即 7 月 11 日，发现该问题的研究人员发布了一份关于另外两个 ServiceNow 漏洞（CVE-2024-5178 和 CVE-2024-5217）的综合报告，除了 CVE-2024-4879 之外，还可以链接这些漏洞以完全访问数据库。

根据 CVE-2024-4879 的文章和大规模网络扫描程序，威胁行为者几乎立即使用了迅速淹没 GitHub 的大量有效漏洞来识别易受攻击的实例。

该操作使用有效负载注入来检查服务器响应中的特定结果，然后使用第二阶段有效负载来检查数据库内容。

如果成功，攻击者会转储用户列表和帐户凭据。尽管其中大多数都经过了哈希处理，但仍有一些违规实例暴露了明文凭据。

由于大量客户和地下论坛上关于ServiceNow漏洞的普遍讨论，网络犯罪社区对利用这些漏洞产生了浓厚的兴趣。

ServiceNow 本月早些时候修复了这三个漏洞，并发布了 CVE-2024-4879、CVE-2024-5178 和 CVE-2024-5217 的不同公告。

建议用户验证他们是否已在所有实例上应用了补丁，如果尚未应用，则尽快通过查找公告中列出的补丁版本来验证。

本文翻译自heimdalsecurity [原文链接](https://heimdalsecurity.com/blog/servicenow-rce-flaws/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298537](/post/id/298537)

安全KER - 有思想的安全新媒体

本文转载自: [heimdalsecurity](https://heimdalsecurity.com/blog/servicenow-rce-flaws/)

如若转载,请注明出处： <https://heimdalsecurity.com/blog/servicenow-rce-flaws/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [有关利用的详细信息](#h2-0)

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