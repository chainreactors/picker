---
title: Oasis Security 研究团队公布微软 Azure 多因素身份验证（MFA）系统存在关键漏洞
url: https://www.anquanke.com/post/id/302727
source: 安全客-有思想的安全新媒体
date: 2024-12-17
fetch_date: 2025-10-06T19:34:49.577796
---

# Oasis Security 研究团队公布微软 Azure 多因素身份验证（MFA）系统存在关键漏洞

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

# Oasis Security 研究团队公布微软 Azure 多因素身份验证（MFA）系统存在关键漏洞

阅读量**51534**

发布时间 : 2024-12-16 10:37:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/critical-microsoft-azure-mfa-bypass-exposed-what-you-need-to-know/>

译文仅供参考，具体内容表达以及含义原文为准。

Oasis Security 的研究团队公布了微软 Azure 的多因素身份验证（MFA）系统中的一个关键漏洞，它使数百万用户面临潜在的漏洞攻击。这种绕过技术允许攻击者未经授权访问敏感账户，包括 Outlook 电子邮件、OneDrive 文件、Teams 聊天和 Azure 云服务，而无需用户交互或通知。

该漏洞利用了基于时间的一次性密码（TOTP）实施中的弱点，这是大多数验证器应用程序使用的标准。据 Oasis 称，攻击者可以利用以下关键问题绕过 MFA：

* **缺乏速率限制**： 报告指出：“通过快速创建新会话和枚举代码，Oasis 研究团队展示了非常高的尝试率，这将很快耗尽 6 位代码的选项总数。”由于缺乏适当的节流措施，攻击者可以同时执行多次尝试。
* **延长代码有效期**： 虽然 TOTP 代码的有效期通常为 30 秒，但微软的系统允许约三分钟的容许窗口，为暴力尝试提供了六倍于通常的时间框架。这个延长的窗口大大增加了猜测有效代码的机会。

攻击方法简单而隐蔽，令人震惊。Oasis Security 公司报告说：“旁路非常简单，执行时间约为一小时，不需要用户交互，也不会产生任何通知或向账户持有人提供任何麻烦迹象。”

在大约 70 分钟内，攻击者有 50% 的机会成功猜出代码。这一时间框架加上攻击的无声性，使许多组织容易遭受未被发现的漏洞攻击。

发现漏洞后，Oasis Security 与微软合作解决了这一问题。虽然具体的技术细节仍然保密，但该公司引入了更严格的速率限制措施。据该报告称，“微软引入了更为严格的速率限制，在尝试失败若干次后就会生效；严格的限制持续时间约为半天”。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-microsoft-azure-mfa-bypass-exposed-what-you-need-to-know/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302727](/post/id/302727)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-microsoft-azure-mfa-bypass-exposed-what-you-need-to-know/)

如若转载,请注明出处： <https://securityonline.info/critical-microsoft-azure-mfa-bypass-exposed-what-you-need-to-know/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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