---
title: 超过 1,400 个 CrushFTP 实例容易受到零日漏洞的攻击
url: https://www.anquanke.com/post/id/296087
source: 安全客-有思想的安全新媒体
date: 2024-04-29
fetch_date: 2025-10-04T12:14:33.477788
---

# 超过 1,400 个 CrushFTP 实例容易受到零日漏洞的攻击

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

# 超过 1,400 个 CrushFTP 实例容易受到零日漏洞的攻击

阅读量**74093**

发布时间 : 2024-04-28 11:31:12

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.securityweek.com/over-1400-crushftp-instances-vulnerable-to-exploited-zero-day/>

译文仅供参考，具体内容表达以及含义原文为准。

Shadowserver 基金会的数据显示，超过 1,400 个 CrushFTP 托管文件传输软件实例仍然容易受到最近披露的零日漏洞的影响。

该漏洞被追踪为CVE-2024-4040（CVSS 评分为 9.8），被描述为服务器端模板注入，允许远程攻击者逃离虚拟文件系统 (VFS) 沙箱、获得管理权限并执行任意命令代码。

CrushFTP 于 4 月 19 日披露了该漏洞，警告客户不要进行野外利用，并敦促他们升级到解决该问题的版本 10.71 或 11.1.0。 CrushFTP 版本 9、10 和 11 受到影响。

4 月 22 日，也就是空中客车 CERT 的 Simon Garrelou（因发现 CVE-2024-4040 而获得赞誉）发布针对该漏洞的概念验证 (PoC) 代码的前一天，CrushFTP 更新了其公告，警告在前面使用 DMZ应用程序的版本不再被视为保护选项，迁移到修补版本至关重要。

4 月 24 日，美国网络安全机构 CISA 将该安全缺陷添加到其已知可利用漏洞 (KEV) 目录中，为联邦机构确定了识别其环境中易受攻击的主机并在 5 月 1 日之前进行修补的最后期限。

虽然观察到的攻击的详细信息很少，但 CrowdStrike 一周前警告称，威胁行为者一直在以有针对性的方式利用它，主要针对美国的实体。

攻击集中在美国并不令人意外。Censys 表示，运行 CrushFTP 服务器的大约 5,000 台主机中有一半位于美国，而Tenable声称可能有超过 7,100 个可公开访问的 CrushFTP 服务器，其中 2,900 个位于美国。

周四，Shadowserver 基金会表示，超过 1,400 个可公开访问的 CrushFTP 安装可能受到该漏洞的影响。其中，700 多个在美国。

建议 CrushFTP 客户尽快更新到企业文件传输应用程序的修补版本。据 Rapid7 称，CVE-2024-4040 不仅受到积极利用，而且“它完全未经身份验证，而且很容易被利用。”

“成功利用该漏洞不仅可以以 root 身份读取任意文件，还可以绕过身份验证以进行管理员帐户访问和完全远程代码执行。成功利用该漏洞后，未经身份验证的远程攻击者可以访问并可能窃取 CrushFTP 实例上存储的所有文件。” Rapid7 解释道。

该网络安全公司还指出，检测利用尝试很困难，因为该错误的有效负载可以以多种形式传递，并且可以操纵日志和请求历史记录以删除攻击证据。此外，甚至标准反向代理后面的 CrushFTP 实例也可能成为攻击目标。

本文翻译自 [原文链接](https://www.securityweek.com/over-1400-crushftp-instances-vulnerable-to-exploited-zero-day/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296087](/post/id/296087)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.securityweek.com/over-1400-crushftp-instances-vulnerable-to-exploited-zero-day/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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