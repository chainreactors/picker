---
title: GitLab 紧急推出多版本补丁，强势修复高危安全漏洞
url: https://www.anquanke.com/post/id/306934
source: 安全客-有思想的安全新媒体
date: 2025-04-29
fetch_date: 2025-10-06T22:04:25.843422
---

# GitLab 紧急推出多版本补丁，强势修复高危安全漏洞

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

# GitLab 紧急推出多版本补丁，强势修复高危安全漏洞

阅读量**57295**

发布时间 : 2025-04-28 09:47:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/gitlab-security-update/>

译文仅供参考，具体内容表达以及含义原文为准。

GitLab 已发布关键安全补丁，以应对其平台中存在的多个高严重性漏洞，这凸显了在网络威胁日益加剧的情况下该公司采取的强有力的安全措施。

该公司已针对社区版（CE）和企业版（EE）发布了 17.11.1、17.10.5 和 17.9.7 版本的补丁。

这些更新修复了重大缺陷，包括跨站脚本攻击（XSS）、拒绝服务攻击（DoS）以及账户被接管的风险，同时还进行了一系列重要的漏洞修复。

****解决********的********重大漏洞****

此次安全更新处理了几个对 GitLab 安装构成重大风险的严重漏洞。

Maven 依赖代理中存在的两个关键跨站脚本攻击（XSS）问题已得到修复。

第一个漏洞（CVE-2025-1763）使得攻击者能够绕过内容安全策略指令，其通用漏洞评分系统（CVSS）评分为 8.7，属于高危漏洞。

一个利用配置错误的缓存头进行攻击的几乎相同的 XSS 漏洞也已修复，并被赋予标识符 CVE-2025-2443。

此外，GitLab 修复了网络错误日志记录（NEL）头注入漏洞（CVE-2025-1908，CVSS 评分为 7.7），该漏洞可能会让恶意行为者监控用户的浏览器活动，甚至可能导致账户被完全接管。

一个影响问题预览功能的中等严重性拒绝服务（DoS）漏洞已通过 CVE-2025-0639 进行修复，其 CVSS 评分为 6.5。

此外，一个即使在存储库资产被禁用时仍允许未经授权查看分支名称的访问控制漏洞也已修复，并被赋予 CVE-2024-12244 的编号，评分为 4.3。

****本次发布的重要漏洞修复****

GitLab 的补丁版本还修复了一系列影响较大的漏洞，进一步提升了系统的稳定性和性能：

****17.11.1 版本****

1.管道安全：“allow\_composite\_identities\_to\_run\_pipelines” 功能现在由一个功能标志保护。

2.Amazon  Q 集成：修复了与亚马逊 Q 相关的连接中断问题和文档错误。

3.持续集成 / 持续交付（CI/CD）改进：纠正了 CI 输入的字符串转换问题；通过静态可达性改进了对最新 DS 模板的处理。

4.云连接器：令牌现在每小时同步一次，以提高可靠性。

5.Workhorse 和 Gitaly：更新了依赖项以提升性能和稳定性。

6.用户界面修复：解决了新界面外观中的文件附件问题。

****17.10.5 版本****

1.邮件处理位置：修复了通用基础镜像（UBI）的邮件处理路径问题。

2.Go gRPC 更新：升级到 1.71.1 版本以增强安全性。

3.Zoekt 索引：对项目过滤、节点管理和索引的即时清除进行了多项修复。

4.会话安全：现在浏览器关闭时会清除会话 cookie，降低了会话被劫持的风险。

5.人工智能事件回填：改进了从 PostgreSQL 到 ClickHouse 的数据回填。

6.云连接器：反向移植了每小时令牌同步补丁。

****17.9.7 版本****

1.联邦信息处理标准（FIPS）和通用基础镜像（UBI）：反向移植了管道命名修复以符合合规要求。

2.加密密钥：引入了 “gitlab:doctor:encryption\_keys” 任务，以便更轻松地管理密钥。

3.Workhorse 和 Gitaly：更新了依赖项以提升稳定性。

4.邮件处理位置：反向移植了 UBI 邮件处理路径修复。

5.Go gRPC 更新：安全更新到 1.71.1 版本。

随着网络威胁的复杂性不断演变，GitLab 通过透明的沟通和及时的安全补丁，继续保持其积极主动的应对策略。

根据相关安全公告，安全专家强烈建议各组织立即升级其安装版本，以降低与这些已知漏洞相关的风险。

此次更新体现了开源社区的协作精神，通过 HackerOne 漏洞赏金计划提交的漏洞报告得到了认可。

随着数字威胁环境变得日益复杂，各组织应遵循网络安全最佳实践，包括定期进行系统审计和及时应用更新，以确保服务的持续运行和数据保护。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/gitlab-security-update/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306934](/post/id/306934)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/gitlab-security-update/)

如若转载,请注明出处： <https://cybersecuritynews.com/gitlab-security-update/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**9赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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