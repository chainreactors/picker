---
title: 黑客利用Cityworks RCE漏洞入侵Microsoft IIS服务器
url: https://www.anquanke.com/post/id/303987
source: 安全客-有思想的安全新媒体
date: 2025-02-09
fetch_date: 2025-10-06T20:33:22.103435
---

# 黑客利用Cityworks RCE漏洞入侵Microsoft IIS服务器

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

# 黑客利用Cityworks RCE漏洞入侵Microsoft IIS服务器

阅读量**277443**

发布时间 : 2025-02-08 15:28:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toula，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/hackers-exploit-cityworks-rce-bug-to-breach-microsoft-iis-servers/>

译文仅供参考，具体内容表达以及含义原文为准。

![City]()

软件供应商天宝（Trimble）发出警告，黑客正在利用 Cityworks 反序列化漏洞，在 IIS 服务器上远程执行命令，并部署 Cobalt Strike 信标以实现初始网络访问。

天宝 Cityworks 是一款以地理信息系统（GIS）为核心的资产管理和工单管理软件，主要面向地方政府、公用事业公司和公共工程机构。

该产品可帮助市政当局和基础设施机构管理公共资产、处理工单、办理许可和执照、进行资本规划与预算编制等事务。

此漏洞编号为 CVE – 2025 – 0994，属于严重级别（通用漏洞评分系统 v4.0 评分为 8.6）的反序列化问题，已认证用户可利用该漏洞对客户的微软互联网信息服务（IIS）服务器发起远程代码执行（RCE）攻击。

天宝表示，已对客户有关黑客利用该漏洞未经授权访问客户网络的报告展开调查，这表明该漏洞正在被利用。

利用漏洞入侵网络

美国网络安全与基础设施安全局（CISA）发布了一份协同公告，警告客户立即保护其网络免受攻击。

CVE – 2025 – 0994 漏洞影响 15.8.9 版本之前的 Cityworks 软件，以及办公配套版本在 23.10 之前的 Cityworks。

最新版本 15.8.9 和 23.10 分别于 2025 年 1 月 28 日和 1 月 29 日发布。

管理本地部署的管理员必须尽快应用安全更新，而云托管实例（CWOL）将自动接收更新。

天宝称，已发现部分本地部署的 IIS 身份权限可能过高，并警告不应以本地或域级管理员权限运行。

此外，部分部署的附件目录配置有误。该供应商建议将附件根文件夹限制为仅包含附件。

完成上述三项操作后，客户即可恢复 Cityworks 的正常运行。

虽然 CISA 尚未透露该漏洞的利用方式，但天宝已发布了针对利用此漏洞攻击的入侵指标（IoC）。

这些入侵指标表明，威胁行为者部署了多种远程访问工具，包括 WinPutty 和 Cobalt Strike 信标。

微软昨日也发出警告，威胁行为者正在入侵 IIS 服务器，利用在网上暴露的[ASP.NET](https://asp.net/)机器密钥，通过 ViewState 代码注入攻击来部署恶意软件。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/hackers-exploit-cityworks-rce-bug-to-breach-microsoft-iis-servers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303987](/post/id/303987)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/hackers-exploit-cityworks-rce-bug-to-breach-microsoft-iis-servers/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/hackers-exploit-cityworks-rce-bug-to-breach-microsoft-iis-servers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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