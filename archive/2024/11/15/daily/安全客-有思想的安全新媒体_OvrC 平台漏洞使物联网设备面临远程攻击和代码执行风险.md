---
title: OvrC 平台漏洞使物联网设备面临远程攻击和代码执行风险
url: https://www.anquanke.com/post/id/301819
source: 安全客-有思想的安全新媒体
date: 2024-11-15
fetch_date: 2025-10-06T19:13:45.856341
---

# OvrC 平台漏洞使物联网设备面临远程攻击和代码执行风险

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

# OvrC 平台漏洞使物联网设备面临远程攻击和代码执行风险

阅读量**62294**

发布时间 : 2024-11-14 14:38:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/11/ovrc-platform-vulnerabilities-expose.html>

译文仅供参考，具体内容表达以及含义原文为准。

一项针对 OvrC 云平台的安全分析发现了 10 个漏洞，这些漏洞可以串联起来，允许潜在攻击者在联网设备上远程执行代码。

Claroty 研究人员 Uri Katz 在一份技术报告中说：“成功利用这些漏洞的攻击者可以访问、控制和破坏 OvrC 支持的设备；其中一些设备包括智能电源、摄像头、路由器、家庭自动化系统等。”

Snap One公司的OvrC（发音为 “oversee”）被宣传为一个 “革命性的支持平台”，能让业主和企业远程管理、配置网络上的物联网设备并排除故障。据其网站介绍，OvrC 解决方案已部署在 50 多万个终端用户地点。

根据美国网络安全和基础设施安全局（CISA）发布的协调公告，成功利用已发现的漏洞可使攻击者 “冒充并声称拥有设备，执行任意代码，并披露受影响设备的信息。”

已发现的这些漏洞会影响 OvrC Pro 和 OvrC Connect，该公司已于 2023 年 5 月发布了其中 8 个漏洞的修复程序，并于 2024 年 11 月 12 日发布了剩余 2 个漏洞的修复程序。

“我们发现的这些问题很多都是由于忽视了设备到云的接口而引起的，”卡茨说。“在许多这样的案例中，核心问题是由于弱标识符或类似的错误，物联网设备被交叉认领的能力。这些问题包括弱访问控制、身份验证绕过、输入验证失败、硬编码凭证和远程代码执行缺陷等。”

因此，远程攻击者可以利用这些漏洞绕过防火墙，在未经授权的情况下访问基于云的管理界面。更糟糕的是，这些访问权限随后可能被用于枚举和配置设备、劫持设备、提升权限，甚至运行任意代码。

最严重的漏洞列举如下

* **CVE-2023-28649** （CVSS v4 得分：9.2），允许攻击者假冒集线器并劫持设备
* **CVE-2023-31241**（CVSS v4 分值：9.2），允许攻击者绕过序列号要求，认领任意未认领设备
* **CVE-2023-28386** （CVSS v4 评分：9.2），允许攻击者上传任意固件更新，导致代码执行
* **CVE-2024-50381**（CVSS v4 分值：9.1），允许攻击者冒充集线器，任意取消认领设备，随后利用其他缺陷认领设备

“随着每天上线的设备越来越多，云管理成为配置和访问服务的主要手段，制造商和云服务提供商比以往任何时候都更需要确保这些设备和连接的安全，”Katz 说。“负面结果可能会影响连接到 OvrC 云的联网电源、商业路由器、家庭自动化系统等。

Nozomi Networks 在披露上述信息的同时，还详细介绍了影响 EmbedThis GoAhead 的三个安全漏洞，EmbedThis GoAhead 是嵌入式和物联网设备中使用的小型 Web 服务器，在特定条件下可能导致拒绝服务（DoS）。这些漏洞（CVE-2024-3184、CVE-2024-3186 和 CVE-2024-3187）已在 GoAhead 6.0.1 版本中得到修补。

最近几个月，江森自控的 exacqVision Web 服务也发现了多个安全漏洞，这些漏洞可被结合起来，控制连接到该应用程序的监控摄像头的视频流并窃取凭证。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/11/ovrc-platform-vulnerabilities-expose.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301819](/post/id/301819)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/11/ovrc-platform-vulnerabilities-expose.html)

如若转载,请注明出处： <https://thehackernews.com/2024/11/ovrc-platform-vulnerabilities-expose.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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