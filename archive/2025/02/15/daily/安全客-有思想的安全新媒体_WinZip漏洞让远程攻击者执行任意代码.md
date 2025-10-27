---
title: WinZip漏洞让远程攻击者执行任意代码
url: https://www.anquanke.com/post/id/304329
source: 安全客-有思想的安全新媒体
date: 2025-02-15
fetch_date: 2025-10-06T20:33:01.940193
---

# WinZip漏洞让远程攻击者执行任意代码

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

# WinZip漏洞让远程攻击者执行任意代码

阅读量**88242**

发布时间 : 2025-02-14 15:58:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/winzip-vulnerability-arbitrary-code/>

译文仅供参考，具体内容表达以及含义原文为准。

WinZip 中一个新披露的严重漏洞，被追踪为 CVE-2025-1240，远程攻击者可通过利用格式错误的 7Z 归档文件，在受影响的系统上执行任意代码。

这个漏洞在通用漏洞评分系统（CVSS）中的评分为 7.8，它影响 WinZip 28.0（内部版本 16022）及更早版本，用户需要更新到 WinZip 29.0 以降低风险。

**WinZip 漏洞 ——CVE-2025-1240**

该漏洞源于在解析 7Z 文件数据时验证不充分，这使得攻击者能够创建恶意归档文件，从而导致内存中的越界写入。

这种数据损坏可被利用，在 WinZip 进程的上下文中执行代码，如果与其他漏洞利用手段相结合，有可能导致整个系统被攻陷。

**关键的利用条件：**

1.用户交互（打开恶意的 7Z 文件或访问被攻陷的网页）。

2.漏洞利用针对的是 WinZip 的 7Z 文件处理组件，7Z 是一种常见的压缩数据格式。

安全公司零日计划（Zero Day Initiative，ZDI）将该漏洞详细记录为 ZDI-CAN-24986，并指出鉴于 WinZip 的全球用户基础，该漏洞存在被广泛滥用的可能性。

**影响与风险**

成功利用该漏洞会使攻击者获得与登录用户相同的权限。这可能导致：

1.恶意软件或勒索软件的安装。

2.敏感数据的窃取。

3.在网络内的横向移动。

虽然攻击需要用户交互，但 7Z 文件在软件分发和数据共享中十分普遍，这增加了成功实施网络钓鱼活动的可能性。

**缓解措施与补丁**

WinZip Computing 公司在 2024 年 12 月发布的 29.0 版本（内部版本 16250）中修复了这个漏洞。该更新还引入了增强的安全措施，包括：

1.更新了 7Z 和 RAR 库，以改进文件验证。

2.简化了补丁部署流程，以确保用户能及时收到关键修复程序。

**对用户的建议：**

1.立即通过官方网站或内置更新程序升级到 WinZip 29.0。

2.避免打开来自不可信来源的 7Z 文件。

3.启用自动更新，以防范未来出现的漏洞。

在这个漏洞披露之前，文件解析漏洞利用事件激增，包括最近 Windows 中的 OLE 零点击漏洞（CVE-2025-21298），该漏洞允许通过恶意电子邮件实现远程代码执行（RCE）。此类事件凸显了主动进行补丁管理的重要性，尤其是对于像 WinZip 这样广泛使用的实用工具，WinZip 每年处理超过 10 亿个压缩文件。

安全分析师敦促各组织优先更新受影响的软件，并对用户进行关于识别可疑文件附件的教育。

WinZip 对 CVE-2025-1240 漏洞的迅速响应，突显了供应商在网络安全方面承担责任的关键作用。建议用户和企业迅速应用更新，以消除这一高风险威胁。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/winzip-vulnerability-arbitrary-code/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304329](/post/id/304329)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/winzip-vulnerability-arbitrary-code/)

如若转载,请注明出处： <https://cybersecuritynews.com/winzip-vulnerability-arbitrary-code/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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