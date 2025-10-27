---
title: Quest修补了关键的VCE SM缺陷，包括CVSS10身份验证绕过
url: https://www.anquanke.com/post/id/309042
source: 安全客-有思想的安全新媒体
date: 2025-06-27
fetch_date: 2025-10-06T22:50:02.720600
---

# Quest修补了关键的VCE SM缺陷，包括CVSS10身份验证绕过

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

# Quest修补了关键的VCE SM缺陷，包括CVSS10身份验证绕过

阅读量**317312**

发布时间 : 2025-06-26 15:57:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/quest-patches-critical-kace-sma-flaws-including-cvss-10-authentication-bypass/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Quest Software发布了紧急安全修补程序，以解决其KACE系统管理应用方案（SMA）产品线中新发现的四个漏洞，其中一个漏洞的CVSS最高评分为10.0，表明对企业基础架构构成严重威胁。

这些漏洞是在 Seralys 的第三方安全审查期间发现的，影响了 KACE SMA 14.1 及以下版本，并包含可能允许攻击者完全绕过身份验证、上传恶意文件和破坏管理许可的问题。

**四个 CVE 及其影响**

1.CVE-2025-32975 – 通过 SSO 绕过身份验证 （CVSS 10.0）

最严重的缺陷存在于单点登录 （SSO） 身份验证机制中。该漏洞允许攻击者在不需要有效凭据的情况下模拟任何有效用户，从而授予对系统的完全管理控制权。

“完全绕过任何有效用户名的身份验证。对设备的完全管理访问权限。不需要身份验证凭证，“报告显示。

2.CVE-2025-32976 – 绕过双重身份验证 （CVSS 8.8）

此漏洞破坏了基于时间的一次性密码 （TOTP） 2FA 机制，使经过身份验证的用户能够由于验证过程中的缺陷而绕过双因素身份验证。

“该漏洞存在于 2FA 验证过程中，可以利用它来获得更高的访问权限，”Seralys 表示。

3.CVE-2025-32977 – 未经身份验证的备份文件上传 （CVSS 9.6）

此缺陷允许未经身份验证的攻击者将备份文件上传到系统。尽管存在签名验证机制，但它不够强大，无法防止上传恶意制作的内容。

“可以利用验证过程中的弱点上传可能损害系统完整性的恶意备份内容。”

4.CVE-2025-32978 – 许可证替换漏洞 （CVSS 7.5）

攻击者可以利用面向公众的许可证续订界面，将合法许可证替换为过期或试用版。这可能会导致阻碍管理作的拒绝服务 （DoS） 情况。

“未经身份验证的许可证替换功能。通过许可证损坏拒绝服务，”报告写道。

**受影响的版本和缓解措施**

Quest 已在一系列适用于以下 KACE SMA 版本的修补程序和修补程序中解决了所有四个漏洞：

* 13.0.385
* 13.1.81
* 13.2.183
* 14.0.341（补丁 5）
* 14.1.101（补丁 4）

敦促用户立即应用提供的更新，以防止潜在的漏洞利用。

本文翻译自securityonline [原文链接](https://securityonline.info/quest-patches-critical-kace-sma-flaws-including-cvss-10-authentication-bypass/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309042](/post/id/309042)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/quest-patches-critical-kace-sma-flaws-including-cvss-10-authentication-bypass/)

如若转载,请注明出处： <https://securityonline.info/quest-patches-critical-kace-sma-flaws-including-cvss-10-authentication-bypass/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**10赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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