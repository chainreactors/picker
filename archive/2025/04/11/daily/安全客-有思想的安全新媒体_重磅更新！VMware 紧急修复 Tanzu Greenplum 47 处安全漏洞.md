---
title: 重磅更新！VMware 紧急修复 Tanzu Greenplum 47 处安全漏洞
url: https://www.anquanke.com/post/id/306336
source: 安全客-有思想的安全新媒体
date: 2025-04-11
fetch_date: 2025-10-06T22:03:07.045546
---

# 重磅更新！VMware 紧急修复 Tanzu Greenplum 47 处安全漏洞

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

# 重磅更新！VMware 紧急修复 Tanzu Greenplum 47 处安全漏洞

阅读量**47753**

发布时间 : 2025-04-10 10:03:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/vmware-patches-multiple-47-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

VMware 已发布关键安全更新，以修复多个 VMware Tanzu Greenplum 产品中存在的 47 个漏洞，其中包括 VMware Tanzu Greenplum 备份与恢复产品中的 29 个问题，以及 VMware Tanzu Greenplum 各组件中的 18 个漏洞。

2025 年 4 月 7 日发布的安全公告中包含了针对严重程度评分（CVSS）高达 9.8 的漏洞的补丁，这表明这些漏洞的严重程度极高，使用这些产品的机构需立即予以关注。

****已修复的重大安全漏洞****

在 VMware Tanzu Greenplum 备份与恢复产品的 29 个漏洞中，有几个被归类为严重漏洞，包括 CVE-2023-39320、CVE-2024-24790 和 GHSA-v778-237x-gjrc。

CVE-2023-39320 和 CVE-2024-24790 是严重漏洞（CVSS 评分为 9.8），可能在备份操作中存在权限提升或远程代码执行的风险。

GHSA-v778-237x-gjrc 修复了 Golang 的 golang.org/x/crypto 模块（版本低于 0.31.0）中的一个严重授权绕过漏洞，在该漏洞中，对 SSH 服务器公钥回调的不当处理可能会让攻击者通过测试多个密钥来获取未经授权的访问权限。

在此次更新中，像 CVE-2025-22866 和 CVE-2023-44487 这样的高严重性问题也得到了修复。

CVE-2025-22866 影响 VMware Tanzu Platform for Cloud Foundry 的网络组件，包括 cf-networking 和 silk，该漏洞可能会使隔离网段内出现未经授权的网络访问或数据拦截情况。

CVE-2023-44487 是一个 HTTP/2 协议缺陷（CVSS 评分为 7.5），它允许通过快速流重置进行拒绝服务攻击，可能会使服务器因资源消耗过大而不堪重负。

Tanzu Greenplum 6.29.0 的安全更新修复了多个组件中的 18 个漏洞，在 PL/Container Python3 镜像（GHSA-f73w-4m7g-ch9x 和 CVE-2024-3596）以及 DataSciencePython3.9（GHSA-x4wf-678h-2pmq）中发现了严重缺陷。

这些漏洞涉及众多组件，可能会使系统面临各种攻击途径。

Greenplum 平台扩展框架包含两个严重漏洞（CVE-2024-47561 和 CVE-2018-1282），如果不进行修复，可能会导致重大安全漏洞。

CVE-2024-47561 是 Apache Avro （1.11.3及以下版本）的 Java SDK中的一个严重漏洞，攻击者可在模式解析过程中通过反序列化不可信数据来执行任意代码。

CVE-2018-1282 是 Apache Hive JDBC 驱动程序（版本在 0.7.1 至 2.3.2 之间）中的一个严重 SQL 注入漏洞。

使用 gpbackup 实用程序执行备份操作的用户应注意，1.31.0 版本引入了关键修复，特别是针对 Greenplum 7 存储过程中的权限语句语法问题。

在受影响的系统上执行增量备份时，现在安全性得到了增强。

Broadcom 的安全公告确认了对 VMware  Tanzu Greenplum（6.29.0 之前的版本）、VMware  Tanzu Greenplum 备份与恢复（1.31.0 之前的版本）以及 VMware  Tanzu Greenplum 平台扩展框架（6.11.1 之前的版本）的安全更新。

****安全修复中的新功能****

尽管这些版本以安全为重点，但 VMware 在 Tanzu Greenplum Backup and Restore 1.31.0 版本中加入了功能改进，比如支持在通用数据保护条例（GPDR）恢复集群上进行备份。在这个版本中，相关的 gpbackup\_helper 实用程序没有变化。

对于 Tanzu Greenplum Disaster Recovery，最新的 1.3.0 版本引入了支持 Greenplum 6.29.0 及更高版本的只读副本模式，允许用户针对恢复集群运行只读查询。可使用 read-replica 命令启用此功能。

****需立即采取行动****

安全专家建议立即更新到最新版本。使用 VMware Tanzu Greenplum Backup and Restore 的机构应升级到 1.31.0 版本或更高版本，而 Tanzu Greenplum 的用户应安装 6.29.0 版本或更新的版本。

对于无法立即进行更新的管理员来说，查看并实施 VMware 安全公告中建议的缓解措施至关重要。

网络安全中心强调了这些更新的重要性，特别是因为有些漏洞可追溯到大约三年前。

这些补丁强化了Broadcom 在收购 VMware 后对安全问题的持续承诺，现在定期的安全更新通过 Broadcom 支持门户进行发布。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/vmware-patches-multiple-47-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306336](/post/id/306336)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/vmware-patches-multiple-47-vulnerabilities/)

如若转载,请注明出处： <https://cybersecuritynews.com/vmware-patches-multiple-47-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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