---
title: Fortinet FortiSIEM 中存在严重未经身份验证的 RCE 漏洞：已发布 PoC
url: https://www.anquanke.com/post/id/296781
source: 安全客-有思想的安全新媒体
date: 2024-05-25
fetch_date: 2025-10-06T17:17:09.185655
---

# Fortinet FortiSIEM 中存在严重未经身份验证的 RCE 漏洞：已发布 PoC

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

# Fortinet FortiSIEM 中存在严重未经身份验证的 RCE 漏洞：已发布 PoC

阅读量**125511**

发布时间 : 2024-05-24 11:47:59

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybersecuritynews.com/rce-vulnerability-fortinet-fortisiem/>

译文仅供参考，具体内容表达以及含义原文为准。

针对 Fortinet FortiSIEM 中一个严重的未经身份验证的远程代码执行漏洞（CVE-2023-34992）的概念验证 (PoC) 漏洞已发布。

该漏洞的 CVSS 评分为 10.0，是由 Horizo​​n3.ai 的研究人员在 2023 年初对 Fortinet 设备进行审计时发现的。

Fortinet FortiSIEM 是一种全面的安全信息和事件管理 (SIEM)解决方案，提供日志收集、关联、自动响应和补救功能。

**RCE 漏洞和 PoC**
在对 Fortinet 设备进行审计时发现了一个严重漏洞，该漏洞揭示了多个问题，最终导致了这一重大缺陷的发现。

通过分析反编译的 Java 代码，研究人员发现该 doPost 方法对 LicenseUploadServlet 用户输入的过滤不够充分，允许攻击者通过“Name”参数注入任意命令

FortiSIEM 的后端 Web 服务通过 Java 框架 Glassfish 部署。漏洞存在于 LicenseUploadServlet.classWeb 服务中。

发现该 servlet 的方法doPost容易受到命令注入攻击，从而允许未经身份验证的攻击者利用该系统。

PoC 演示了攻击者如何利用此漏洞来实现未经身份验证的远程代码执行。

通过利用LicenseUploadServlet，攻击者可以上传在 root 用户上下文中执行命令的恶意负载。

此访问权限可用于读取集成系统中的机密，从而实现网络内的进一步横向移动。完整的 PoC 可在GitHub上找到。

成功利用 CVE-2023-34992 可让攻击者：

* 以root用户身份执行任意命令。
* 从集成系统中读取敏感信息和秘密。
* 转向网络内的其他系统，可能会导致大范围的危害。

**减轻**
Fortinet 已在近期更新中修复了此漏洞。任何从 6.4.0 到 7.1.1 的 FortiSIEM 版本均存在风险。Fortinet 已针对 7.0.3、7.1.3 和 6.7.9 版本发布了补丁，建议升级到这些版本或更高版本。

此外，预计版本 7.2.0、6.6.5、6.5.3 和 6.4.4 的补丁将很快发布。

强烈建议用户应用最新补丁以降低风险。此外，建议遵循保护 SIEM 部署的最佳实践，例如限制对管理界面的访问和定期审核系统配置。

/opt/phoenix/logs/phoenix.logs使用 FortiSIEM 的组织应该检查其日志中是否存在任何异常活动，尤其是可能保存 phMonitor 服务收到的消息内容的文件中。

使用 Fortinet FortiSIEM 的组织应优先更新其系统，以防止可能利用此严重漏洞。

本文翻译自 [原文链接](https://cybersecuritynews.com/rce-vulnerability-fortinet-fortisiem/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296781](/post/id/296781)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybersecuritynews.com/rce-vulnerability-fortinet-fortisiem/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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