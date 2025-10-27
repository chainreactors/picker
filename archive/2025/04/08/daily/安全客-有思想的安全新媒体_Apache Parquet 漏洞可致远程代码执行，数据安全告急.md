---
title: Apache Parquet 漏洞可致远程代码执行，数据安全告急
url: https://www.anquanke.com/post/id/306235
source: 安全客-有思想的安全新媒体
date: 2025-04-08
fetch_date: 2025-10-06T22:02:45.690021
---

# Apache Parquet 漏洞可致远程代码执行，数据安全告急

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

# Apache Parquet 漏洞可致远程代码执行，数据安全告急

阅读量**58828**

发布时间 : 2025-04-07 10:30:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/critical-apache-parquet-rce-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

在 Apache Parquet 的 Java 库中发现了一个严重的远程代码执行（RCE）漏洞，这可能会影响全球数千个数据分析系统。

该漏洞编号为 CVE-2025-30065，通用漏洞评分系统（CVSS）评分为最高的 10.0 分。攻击者可利用 parquet-avro 模块中的不安全反序列化来执行任意代码。

这个安全问题被归类为 “对不可信数据的反序列化”（CWE – 502），影响所有 1.15.0 及以下版本的 Apache Parquet Java 库。

### ****Apache Parquet 远程代码执行漏洞****

该漏洞自 1.8.0 版本引入，不过所有历史版本都应进行审查。此漏洞的核心在于 parquet-avro 模块的模式解析存在严重缺陷。

根据 Apache 的官方公告，“Apache Parquet 1.15.0 及之前版本的 parquet-avro 模块在模式解析时，会使恶意行为者能够执行任意代码”。

该漏洞的技术根源在于，在解析 Avro 模式时存在不安全的类加载问题，这使得攻击者在处理特制的 Parquet 文件时，能够注入并执行恶意代码。

利用此漏洞无需用户交互或身份验证。攻击者只需诱使目标通过其数据管道处理恶意的 Parquet 文件即可。

该漏洞由 Amazon 研究员 Keyi Li 发现并以负责任的方式披露。以下是该漏洞的概要信息：

|  |  |
| --- | --- |
| ****风险因素**** | ****详情**** |
| 受影响产品 | Apache Parquet Java 库版本 ≤ 1.15.0（包括 parquet-avro 模块） |
| 影响 | 远程代码执行（RCE） |
| 利用前提 | 特制的 Parquet 文件；无需用户交互或身份验证 |
| CVSS 3.1 评分 | 10.0（严重） |

### ****对大数据生态系统的广泛影响****

该漏洞影响众多大数据环境，包括 Hadoop、Spark 和 Flink 的实现，以及 AWS、Google 和 Azure 云平台上的分析系统。

已知在其数据基础设施中使用 Parquet 的大型公司包括 Netflix、Uber、Airbnb 和 LinkedIn。

如果该漏洞被成功利用，攻击者可能会：

1.完全控制受影响的系统。

2.窃取或篡改敏感数据。

3.部署勒索软件或其他恶意负载。

4.破坏关键的数据服务和业务运营。

Endor Labs 在其安全公告中警告称：“该漏洞可能会影响导入 Parquet 文件的数据管道和分析系统，尤其是当这些文件来自外部或不可信来源时。”

系统安全的各个方面 —— 保密性、完整性和可用性 —— 都面临着很高的风险。

### ****立即采取的补救措施****

Apache Software Foundation 已发布 1.15.1 版本，修复了该漏洞。强烈建议各组织立即采取以下措施：

1.将所有 Apache Parquet Java 依赖项升级到 1.15.1 版本。

2.对于无法立即更新的系统，要对 Parquet 文件（尤其是来自外部来源的文件）实施严格的验证。

3.加强对处理 Parquet 文件的系统的监控和日志记录，以检测潜在的利用尝试。

4.审查数据处理工作流程，以识别潜在的暴露点。

截至 2025 年 4 月 4 日，尚无该漏洞在现实中被利用的确认报告。然而，安全专家警告称，鉴于该漏洞的严重性且现已公开，可能很快就会出现利用尝试。

研究人员表示：“尽管潜在危害令人担忧，但需要注意的是，只有在导入恶意的 Parquet 文件时，该漏洞才可能被利用。”

尽管如此，此漏洞的严重性要求所有在其数据基础设施中使用 Apache Parquet 的组织立即予以关注。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/critical-apache-parquet-rce-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306235](/post/id/306235)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/critical-apache-parquet-rce-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/critical-apache-parquet-rce-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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