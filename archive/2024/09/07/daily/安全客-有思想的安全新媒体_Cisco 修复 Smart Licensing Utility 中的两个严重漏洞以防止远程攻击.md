---
title: Cisco 修复 Smart Licensing Utility 中的两个严重漏洞以防止远程攻击
url: https://www.anquanke.com/post/id/299859
source: 安全客-有思想的安全新媒体
date: 2024-09-07
fetch_date: 2025-10-06T18:22:24.570834
---

# Cisco 修复 Smart Licensing Utility 中的两个严重漏洞以防止远程攻击

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

# Cisco 修复 Smart Licensing Utility 中的两个严重漏洞以防止远程攻击

阅读量**132011**

发布时间 : 2024-09-06 11:16:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/cisco-fixes-two-critical-flaws-in-smart.html>

译文仅供参考，具体内容表达以及含义原文为准。

Cisco 已针对影响其 Smart Licensing Utility 的两个关键安全漏洞发布了安全更新，这些漏洞可能允许未经身份验证的远程攻击者提升其权限或访问敏感信息。

这两个漏洞的简要描述如下 –

* CVE-2024-20439（CVSS 评分：9.8）- 存在管理帐户的未记录静态用户凭据，攻击者可利用该凭据登录受影响的系统

* CVE-2024-20440（CVSS 评分：9.8）- 由于调试日志文件过于冗长而引起的漏洞，攻击者可利用该漏洞通过构建的 HTTP 请求访问此类文件，并获取可用于访问 API 的凭据

虽然这些缺点的成功并不相互依赖，但 Cisco 在其咨询中指出，它们“除非 Cisco Smart Licensing Utility 由用户启动并积极运行，否则它们不可被利用。

在内部安全测试期间发现的缺陷也不会影响 Smart Software Manager On-Prem 和 Smart Software Manager Satellite 产品。

建议 Cisco Smart License Utility 版本 2.0.0、2.1.0 和 2.2.0 的用户更新到固定版本。该软件的 2.3.0 版不易受到该错误的影响。

Cisco 还发布了更新，以解决其身份服务引擎 （ISE） 中的命令注入漏洞，该漏洞可能允许经过身份验证的本地攻击者在底层操作系统上运行任意命令并将权限提升到 root。

该漏洞被跟踪为 CVE-2024-20469（CVSS 评分：6.0），要求攻击者在受影响的设备上拥有有效的管理员权限。

“这个漏洞是由于对用户提供的输入验证不足，”该公司表示。“攻击者可以通过提交精心设计的 CLI 命令来利用此漏洞。成功利用此漏洞可让攻击者将权限提升到 root。

它影响以下版本 –

* 思科 ISE 3.2（3.2P7 – 2024 年 9 月）
* 思科 ISE 3.3（3.3P4 – 2024 年 10 月）

该公司还警告说，概念验证 （PoC） 漏洞利用代码可用，尽管它不知道该漏洞有任何恶意利用。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/cisco-fixes-two-critical-flaws-in-smart.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299859](/post/id/299859)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/cisco-fixes-two-critical-flaws-in-smart.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/cisco-fixes-two-critical-flaws-in-smart.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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