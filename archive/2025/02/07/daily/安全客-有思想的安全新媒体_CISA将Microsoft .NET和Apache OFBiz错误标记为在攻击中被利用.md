---
title: CISA将Microsoft .NET和Apache OFBiz错误标记为在攻击中被利用
url: https://www.anquanke.com/post/id/303897
source: 安全客-有思想的安全新媒体
date: 2025-02-07
fetch_date: 2025-10-06T20:33:40.321395
---

# CISA将Microsoft .NET和Apache OFBiz错误标记为在攻击中被利用

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

# CISA将Microsoft .NET和Apache OFBiz错误标记为在攻击中被利用

阅读量**332332**

发布时间 : 2025-02-06 15:03:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/cisa-tags-microsoft-net-and-apache-ofbiz-bugs-as-exploited-in-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全与基础设施安全局（CISA）在其 “已知被利用漏洞” 目录中新增了四个漏洞，并敦促联邦机构和大型组织尽快应用现有的安全更新。

其中包含影响微软.NET Framework 和 Apache OFBiz（开放式企业应用平台）这两款广泛使用软件的漏洞。

尽管该机构已将这些漏洞标记为在攻击中被积极利用，但并未提供有关恶意活动的具体细节，包括攻击者是谁、攻击对象是谁等信息。

首个漏洞编号为 CVE – 2024 – 29059，是.NET Framework 中的一个严重（CVSS v3 评分：7.5）信息泄露漏洞，由 CODE WHITE 发现，并于 2023 年 11 月提交给微软。

2023 年 12 月，微软关闭了该漏洞披露报告，称 “经过仔细调查，我们认定此案例不符合我们立即进行修复的标准”。

然而，微软最终在 2024 年 1 月的安全更新中修复了该漏洞，但却错误地未发布 CVE 编号，也未对研究人员予以认可。

2 月，CODE WHITE 发布了用于泄露内部对象统一资源标识符（URI）的技术细节及概念验证性攻击手段，这些 URI 可用于实施.NET 远程处理攻击。

2024 年 3 月，微软最终针对 CVE – 2024 – 29059 这个漏洞发布了安全公告，并将漏洞发现归功于研究人员。

Apache OFBiz 的漏洞编号为 CVE – 2024 – 45195，是一个严重程度为 “危急”（CVSS v3 评分：9.8）的远程代码执行漏洞，影响 18.12.16 版本之前的 OFBiz。

该漏洞由强制浏览漏洞导致，它使得未经身份验证的直接请求攻击能够访问受限路径。

该漏洞最初由 Rapid7 发现，该公司还展示了概念验证性（PoC）攻击手段，而供应商于 2024 年 9 月修复了该漏洞。

建议用户升级到 Apache OFBiz 18.12.16 或更高版本，以消除这一特定风险。

目前，CISA 敦促可能受影响的机构和组织在 2025 年 2 月 25 日前应用可用的补丁和缓解措施，否则停止使用相关产品。

此次添加到 “已知被利用漏洞” 目录中的另外两个漏洞是 CVE – 2018 – 9276 和 CVE – 2018 – 19410，二者均影响 Paessler PRTG 网络监控软件。这些问题在 2018 年 6 月发布的 18.2.41.1652 版本中已得到修复。

第一个漏洞是操作系统命令注入问题，第二个是本地文件包含漏洞。这两个漏洞的修复截止日期同样设定为 2025 年 2 月 25 日。

遗憾的是，目前尚无这些漏洞在攻击中具体被利用方式的相关信息。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/cisa-tags-microsoft-net-and-apache-ofbiz-bugs-as-exploited-in-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303897](/post/id/303897)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/cisa-tags-microsoft-net-and-apache-ofbiz-bugs-as-exploited-in-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/cisa-tags-microsoft-net-and-apache-ofbiz-bugs-as-exploited-in-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全漏洞](/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24
* ##### [CoreDNS DoS 漏洞：未经验证的攻击者可通过 DNS-over-QUIC 使服务器崩溃](/post/id/308349)

  2025-06-11 16:08:49
* ##### [“欧洲版CVE”上线，EUVD释放漏洞治理新信号](/post/id/307472)

  2025-05-16 18:04:21
* ##### [CVE-2025-24977:OpenCTI平台中的关键RCE缺陷将基础设施暴露为根级攻击](/post/id/307143)

  2025-05-07 16:32:13
* ##### [僵尸网络通过CVE-2024-6047和CVE-2024-11120开发旧GeoVision物联网设备](/post/id/307139)

  2025-05-07 16:27:26
* ##### [CVE-2025-47241:浏览器使用中的关键白名单绕过暴露了内部服务](/post/id/307134)

  2025-05-07 16:17:59
* ##### [微软7月补丁日多个产品安全漏洞风险通告，包含5个紧急漏洞和2个在野利用漏洞](/post/id/297800)

  2024-07-10 19:33:07

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