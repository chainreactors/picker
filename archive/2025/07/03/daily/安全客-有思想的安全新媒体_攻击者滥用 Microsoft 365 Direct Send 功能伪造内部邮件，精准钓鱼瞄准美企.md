---
title: 攻击者滥用 Microsoft 365 Direct Send 功能伪造内部邮件，精准钓鱼瞄准美企
url: https://www.anquanke.com/post/id/309296
source: 安全客-有思想的安全新媒体
date: 2025-07-03
fetch_date: 2025-10-06T23:49:29.123786
---

# 攻击者滥用 Microsoft 365 Direct Send 功能伪造内部邮件，精准钓鱼瞄准美企

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

# 攻击者滥用 Microsoft 365 Direct Send 功能伪造内部邮件，精准钓鱼瞄准美企

阅读量**40580**

发布时间 : 2025-07-02 14:51:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源： hackread

原文地址：<https://hackread.com/scammers-microsoft-365-direct-spoof-emails-us-firms/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

攻击者正在滥用 Microsoft 365 的 Direct Send（直接发送）功能，伪造“内部邮件”对美国企业发起钓鱼攻击，利用虚假语音邮件通知与二维码，绕过安全过滤系统，精准窃取用户凭据。

Varonis 威胁实验室的安全研究人员披露了这一**利用 Microsoft 365 较少被关注功能的新型钓鱼攻击活动**。该攻击始于 2025 年 5 月，至今仍在活跃，已锁定超过 70 家机构，其中 **95% 为美国企业**。

研究人员在分享给 Hackread.com 的分析文章中指出，这一攻击的特别之处在于：**攻击者无需入侵任何账户，即可伪造来自“内部用户”的邮件**，大幅增加了绕过传统邮件安全系统的成功率。

###

### 滥用 Direct Send 功能

该攻击活动依赖于 Microsoft 365 的 Direct Send 功能。该功能原本是为打印机等设备设计，用于无需身份验证发送邮件。然而，攻击者正利用这一设计缺陷。

Varonis 威胁实验室的 Tom Barnea 指出：“该方式的关键在于——不需要登录或凭据。”攻击者只需掌握一些公开可得的信息，如企业域名、内部邮箱格式（通常容易猜测），就能构造邮件。

借助 Direct Send，攻击者可伪装成组织内部邮箱发送邮件，实则来源于外部。这类邮件往往被 Microsoft 自身或第三方安全产品**误判为合法内部通信**，从而顺利绕过检测。

Varonis 还发现，**这类伪造邮件通常伪装成“语音留言提醒”**，并附带一份 PDF，其中嵌有二维码。受害者扫码后将被引导至一个伪造的 Microsoft 365 登录页面，进而窃取其凭据。

###

### 检测与防御建议

针对这一新型钓鱼方式，企业需保持警觉。Varonis 建议，从以下几个方向加强检测与防御：

* 检查邮件头部是否出现异常，如 **来自外部 IP 地址但发送给 Microsoft 365 Smart Host**（如 tenantname.mail.protection.outlook.com）。
* 对内部域名执行 SPF、DKIM、DMARC 时是否验证失败。
* 行为线索识别：如用户给自己发送邮件、来源地异常但无登录行为等。

为提升防御能力，Varonis 建议采取如下措施：

* **在 Exchange 管理中心启用“拒绝 Direct Send”设置**。
* 配置严格的 **DMARC 策略**。
* 加强员工培训，**重点警示关于二维码附件的 Quishing（二维码钓鱼）攻击**风险。
* 为所有用户启用 **多因素认证（MFA）**。
* 部署 **条件访问策略**，即使凭据被盗也能降低风险。

该事件再次警示我们：攻击者正在深挖云办公系统中的灰色功能边界，以更隐蔽方式达成钓鱼目的。企业安全防护需及时跟进最新攻击技巧与邮件攻击面变化，全面提升邮件安全策略和用户意识防线。

本文翻译自 hackread [原文链接](https://hackread.com/scammers-microsoft-365-direct-spoof-emails-us-firms/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309296](/post/id/309296)

安全KER - 有思想的安全新媒体

本文转载自:  [hackread](https://hackread.com/scammers-microsoft-365-direct-spoof-emails-us-firms/)

如若转载,请注明出处： <https://hackread.com/scammers-microsoft-365-direct-spoof-emails-us-firms/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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