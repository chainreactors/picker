---
title: Check Point 网关漏洞：澳大利亚发布高度警报
url: https://www.anquanke.com/post/id/297039
source: 安全客-有思想的安全新媒体
date: 2024-06-05
fetch_date: 2025-10-06T16:55:58.056211
---

# Check Point 网关漏洞：澳大利亚发布高度警报

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

# Check Point 网关漏洞：澳大利亚发布高度警报

阅读量**97223**

发布时间 : 2024-06-04 11:42:35

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/check-point-gateways-vulnerability-australia/>

译文仅供参考，具体内容表达以及含义原文为准。

澳大利亚网络安全中心 (ACSC) 已针对 Check Point 网关的漏洞发出高度警报通知。该零日漏洞被标识为 CVE-2024-24919，它使攻击者能够访问易受攻击系统上的私人数据，并且还可能危害大型网络。

**Check Point 网关漏洞 CVE-2024-24919 详解**
CVE-2024-24919 已被归类为任意文件读取漏洞。这意味着攻击者可以利用此漏洞读取任何受感染的文件，而无需事先进行身份验证或特殊权限。攻击者可以通过读取受影响设备上的任何文件来利用此漏洞。

攻击者可能会利用此漏洞通过破解散列密码来窃取用户凭据，或将其用于未来的网络钓鱼攻击。攻击者还可以通过使用窃取的凭据在网络内移动并访问更敏感的系统来发起横向攻击。他们还可以删除或修改关键数据并通过安装恶意软件来破坏操作，从而获得在未来在网络内发起攻击的权限。

ACSC在 5 月 31 日发布的高度警戒通知中确认，攻击者正在针对未打补丁的 Check Point 设备发起攻击。Check Point 已发布修补程序来解决 CVE-2024-24919 漏洞。利用此漏洞，攻击者可以访问敏感信息，并允许他们在网络内横向移动，从而可能获得完全控制权（包括域管理员权限）。

![]()
来源：X
**Check Point 网关：全球超过 15,000 台设备存在漏洞**
ODIN 是由Cyble为攻击面管理和威胁情报而构建的互联网搜索引擎，研究发现全球有超过 15,000 个 Check Point 设备实例面向互联网且可能存在漏洞。ODIN 用户可以使用查询服务模块 http.title:“Check Point SSL Network Extender” 来跟踪平台上暴露在互联网上的 Check Point 设备。受影响的 Check Point 产品包括：

* CloudGuard 网络
* 量子大师
* 量子可扩展机箱
* 量子安全网关
* 量子火花设备

受影响的软件版本包括：

R80.20.x、R80.20SP (EOL)、R80.40 (EOL)、R81、R81.10、R81.10.x 和 R81.20
**立即修补以防止检查点缺陷**
ACSC 强烈建议使用 Check Point 安全网关设备的澳大利亚组织检查其系统中是否存在受影响的软件版本，并按照 Check Point 的指示应用相应的补丁。作为一项额外的安全措施，许多组织已被指示在已修补的系统上重置本地帐户凭据以降低潜在风险，尤其是因为密码哈希可能被泄露。

**日益严重的威胁**
虽然 ACSC 的警告是专门针对澳大利亚组织发出的，但该漏洞对全球构成了重大威胁。全球组织应立即采取行动，识别并修补受影响的 Check Point 设备。CVE-2024-24919 的发现和随后的利用情况正在不断演变。

在接下来的几天里，我们可以期待：

进一步分析：安全研究人员将继续分析零日漏洞及其相应影响。预计将会发布详细的技术报告，概述漏洞利用机制和潜在攻击媒介。

漏洞代码可用性：恶意行为者还可能公开发布 CVE-2024-24919 的漏洞代码。这可能会大幅增加针对易受攻击设备的攻击数量。组织应做好准备，以检测和应对此类潜在的漏洞攻击。

补丁更新和指导： Check Point 可能会根据正在进行的分析改进和更新安全修补程序。组织应密切关注 Check Point 的任何更新或修订的修补说明。

攻击尝试次数增加：随着漏洞消息的传播，针对未打补丁的 Check Point 设备的攻击尝试次数可能会增加。组织应优先考虑修补漏洞，并警惕其网络中的任何可疑活动。

发现相关漏洞： CVE-2024-24919 的发现可能导致在其他 Check Point 产品或来自不同供应商的安全软件中发现类似漏洞。组织应随时了解任何相关漏洞并采取适当的缓解措施。

本文翻译自 [原文链接](https://thecyberexpress.com/check-point-gateways-vulnerability-australia/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297039](/post/id/297039)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/check-point-gateways-vulnerability-australia/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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