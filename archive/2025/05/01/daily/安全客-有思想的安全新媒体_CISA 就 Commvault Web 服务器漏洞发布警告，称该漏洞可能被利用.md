---
title: CISA 就 Commvault Web 服务器漏洞发布警告，称该漏洞可能被利用
url: https://www.anquanke.com/post/id/307061
source: 安全客-有思想的安全新媒体
date: 2025-05-01
fetch_date: 2025-10-06T22:23:23.956205
---

# CISA 就 Commvault Web 服务器漏洞发布警告，称该漏洞可能被利用

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

# CISA 就 Commvault Web 服务器漏洞发布警告，称该漏洞可能被利用

阅读量**132729**

发布时间 : 2025-04-30 14:19:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/cisa-commvault-web-server-flaw/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全和基础设施安全局 (CISA) 已将Commvault Web 服务器漏洞 (CVE-2025-3928) 添加到其已知被利用漏洞 (KEV) 目录中，这表明威胁行为者正在积极利用此安全漏洞。

该机构于 2025 年 4 月 28 日宣布了这一补充，要求联邦机构在 2025 年 5 月 17 日之前根据具有约束力的操作指令 (BOD) 22-01 修复该漏洞。

## Commvault Web 服务器未指定漏洞 – CVE-2025-3928

CVE-2025-3928 被归类为影响 Commvault Web Server 的“未指定漏洞”，该漏洞使经过身份验证的远程攻击者能够在受感染的系统上创建和执行 Webshel​​l。

根据国家漏洞数据库，此高严重性漏洞的 CVSS 基本评分为 8.8，反映了其巨大潜在影响。

CISA 引用的 Commvault 建议指出：“不良行为者可以通过创建和执行 webshel​​l 来破坏 Web 服务器。”

这种类型的攻击允许恶意行为者以 Web 服务器的权限执行任意命令，同时保持对受感染系统的持续访问。

该漏洞的漏洞预测评分系统 (EPSS) 分数为 0.10%，表明未来 30 天内被主动利用的可能性。

尽管这一比例相对较低，但 CISA 将该漏洞添加到 KEV 目录中，证实了漏洞利用已经发生。

|  |  |
| --- | --- |
| **风险因素** | **细节** |
| 受影响的产品 | Commvault Web 服务器（Windows 和 Linux）最高版本：11.20.21611.28.14011.32.8811.36.45 |
| 影响 | – 完全服务器入侵 – 执行 webshel​​l – 机密数据泄露 – 服务中断 – 完整性修改 |
| 漏洞利用前提条件 | 远程、经过身份验证的低权限攻击者 |
| CVSS 3.1 评分 | 8.8（高） |

**受影响的系统和修补版本**

该安全漏洞影响 Windows 和 Linux 平台上的 Commvault Web Server 部署。Commvault 已在以下版本中修复此漏洞：

* 11.36.46
* 1989年11月32日
* 11.28.141
* 11.20.217

运行该软件早期版本的组织仍然容易受到潜在攻击。

CISA建议各组织在 5 月 17 日截止日期之前采取以下行动之一：

* 根据供应商的说明采取缓解措施
* 遵循适用的 BOD 22-01 云服务指南
* 如果没有缓解措施，请停止使用该产品

虽然 BOD 22-01 要求正式仅适用于联邦民事行政部门 (FCEB) 机构，但 CISA 强烈鼓励所有组织优先及时修复目录漏洞作为其安全实践的一部分。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/cisa-commvault-web-server-flaw/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307061](/post/id/307061)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/cisa-commvault-web-server-flaw/)

如若转载,请注明出处： <https://cybersecuritynews.com/cisa-commvault-web-server-flaw/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [Commvault Web 服务器未指定漏洞 - CVE-2025-3928](#h2-0)

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