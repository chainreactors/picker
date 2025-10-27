---
title: Grafana 高危漏洞可致关键业务数据泄露，官方补丁及时发布化解危机
url: https://www.anquanke.com/post/id/306841
source: 安全客-有思想的安全新媒体
date: 2025-04-25
fetch_date: 2025-10-06T22:04:29.961085
---

# Grafana 高危漏洞可致关键业务数据泄露，官方补丁及时发布化解危机

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

# Grafana 高危漏洞可致关键业务数据泄露，官方补丁及时发布化解危机

阅读量**87923**

发布时间 : 2025-04-24 10:41:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/grafana-patches-cve-2025-3260-and-more-in-critical-security-update/>

译文仅供参考，具体内容表达以及含义原文为准。

![Grafana Vulnerability Dashboard Permission Bypass]()

Grafana Labs 已针对多个产品版本发布了安全更新，修复了一个高危和两个中危级别的漏洞，这些漏洞影响了Grafana OSS 和 Grafana Enterprise。其中最严重的漏洞是 CVE-2025-3260，通用漏洞评分系统（CVSS）评分为 8.3（高危），该漏洞可能导致未经授权的用户访问和修改仪表盘，即使是权限极低的用户也能做到。

****CVE-2025-3260：仪表盘权限绕过****

此漏洞自Grafana 11.6.x 版本引入，影响 /apis/dashboard.grafana.app/\* 端点，允许具有Viewer 或 Editor 角色的用户在其所在组织内绕过仪表盘级别的权限限制：

1.查看者可以访问所有仪表盘，无论其被分配的访问权限如何。

2.Editor 可以查看、编辑和删除同一组织内的任何仪表盘。

3.当匿名用户被配置为 Viewer 或 Editor 角色时，该漏洞也会对其产生影响。

匿名用户将能够根据其配置的角色查看或修改所有仪表盘。虽然组织边界仍然存在，但公告警告称，使用匿名身份验证的实例特别容易受到攻击。

****CVE-2025-2703：XY 图表插件中的 DOM********XSS****

一名外部研究人员发现，在 Grafana 内置的 XY 图表插件中存在一个中危级别的基于文档对象模型（DOM）的跨站脚本（XSS）漏洞。该漏洞的 CVSS 评分为 6.8，它使得：当具有general.writer基于角色的访问控制（RBAC）权限的Editor或用户向 XY 图表中注入恶意代码时，可执行任意 JavaScript 代码。

Grafana Labs 指出，现有的内容安全策略（CSPs）无法防范此漏洞，但建议启用可信类型（Trusted Types）来减轻基于 DOM 的跨站脚本攻击向量的影响。

第三个漏洞 CVE-2025-3454 是在 Grafana 的数据源代理 API 中发现的另一个中危级别的漏洞（CVSS 评分为 5.0）。它允许：

1.通过在 API 路径中附加一个额外的正斜杠（/），未经授权地读取访问普罗米修斯（Prometheus）和警报管理器（Alertmanager）数据源。

2.该问题影响 Grafana 8.0 及更高版本，具体影响使用基本身份验证和特定路由权限的数据源中的只读路径。

该团队警告称：“ Grafana 用户可能会获得对 GET 端点的未经授权的读取访问权限，尽管他们被分配了相应的角色和权限。”

****受影响的版本和补丁****

这些漏洞影响以下版本：

1.CVE-2025-3260：≥ Grafana 11.6.0 版本

2.CVE-2025-2703：≥ Grafana 11.1.0 版本

3.CVE-2025-3454：≥ Grafana 8.0 版本

以下版本中提供了补丁：

1.Grafana 11.6.0+security-01

2.Grafana 11.5.3+security-01

3.Grafana 11.4.3+security-01

4.Grafana 11.3.5+security-01

5.Grafana 11.2.8+security-01

6.Grafana 10.4.17+security-01

****缓解措施****

如果无法立即打补丁，Grafana 建议采取以下临时缓解措施：

1.对于 CVE-2025-3260：阻止发往以下地址的入站流量：

（1）/apis/dashboard.grafana.app/v0alpha1

（2）/apis/dashboard.grafana.app/v1alpha1

（3）/apis/dashboard.grafana.app/v2alpha1

2.对于 CVE-2025-2703：启用可信类型以实施更严格的 DOM 操作策略。

3.对于 CVE-2025-3454：使用反向代理对传入的 URL 进行规范化和清理。

Grafana Labs 敦促所有用户和机构尽快进行更新：“如果您当前正在运行Grafana OSS 或 Grafana Enterprise，请更新到上述安全版本之一，以修复所有漏洞。”

本文翻译自securityonline [原文链接](https://securityonline.info/grafana-patches-cve-2025-3260-and-more-in-critical-security-update/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306841](/post/id/306841)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/grafana-patches-cve-2025-3260-and-more-in-critical-security-update/)

如若转载,请注明出处： <https://securityonline.info/grafana-patches-cve-2025-3260-and-more-in-critical-security-update/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**8赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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