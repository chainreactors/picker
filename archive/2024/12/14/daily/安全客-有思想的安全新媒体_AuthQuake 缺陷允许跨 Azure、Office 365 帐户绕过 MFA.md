---
title: AuthQuake 缺陷允许跨 Azure、Office 365 帐户绕过 MFA
url: https://www.anquanke.com/post/id/302703
source: 安全客-有思想的安全新媒体
date: 2024-12-14
fetch_date: 2025-10-06T19:37:36.710707
---

# AuthQuake 缺陷允许跨 Azure、Office 365 帐户绕过 MFA

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

# AuthQuake 缺陷允许跨 Azure、Office 365 帐户绕过 MFA

阅读量**87997**

发布时间 : 2024-12-13 10:15:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Waqas，文章来源：hackread

原文地址：<https://hackread.com/authquake-flaw-mfa-bypass-azure-office-365-accounts/>

译文仅供参考，具体内容表达以及含义原文为准。

**概要：**

* 微软MFA的漏洞被命名为AuthQuake，允许攻击者绕过安全措施并访问账户。
* 漏洞影响了Azure、Office 365和其他微软服务，超过4亿用户面临风险。
* 漏洞利用了登录会话中缺乏速率限制和TOTP代码延长有效性的问题。
* 攻击者可以在不到70分钟内以50%的成功率绕过MFA，无需用户交互。
* 微软于2024年10月9日永久修补了该漏洞，引入了更严格的速率限制机制。

Oasis Security的网络安全研究人员在微软的多因素认证（MFA）中识别了一个名为AuthQuake的漏洞，该漏洞允许攻击者绕过安全措施并获得对用户账户的未授权访问。

在超过4亿的付费Office 365订阅中，这个漏洞对于网络犯罪分子来说是一个极具吸引力的机会，他们可以窃取微软平台上的敏感信息，如电子邮件、文件和通信，包括Outlook、OneDrive、Teams、Azure等。

**利用速率限制和基于时间的一次性密码（TOTP）**

该漏洞利用了MFA设置中的两个关键弱点：缺乏速率限制和TOTP代码的延长时间框架。用户登录时，他们会被分配一个会话ID，并要求使用认证器应用中的基于时间的一次性密码（TOTP）来验证身份。问题是系统允许每个会话最多有10次失败的登录尝试，而不会通知用户或触发任何警报。

缺乏速率限制允许攻击者快速创建新的登录会话并尝试多个TOTP代码，这些代码本质上是六位数字。鉴于这些代码有百万种可能的组合，攻击者理论上可以在不遇到任何安全措施的情况下穷尽所有选项。
另一方面，TOTP代码通常只有效30秒，但Oasis的测试显示，系统允许代码保持有效长达3分钟。这个延长的时段显著提高了攻击者猜测正确代码的成功几率。

**结果如何？**

根据Oasis Security在12月11日周三发布前与Hackread.com分享的博客文章，研究人员得出结论，攻击者可以在不到70分钟内以50%的成功率绕过MFA，而无需任何用户交互或警报。

**微软的回应**

Oasis Security向微软报告了这一事件。这家科技巨头迅速做出回应，并在2024年7月4日部署了临时修复措施后，于2024年10月9日实施了永久修复。修复措施包括在多次失败尝试后引入更严格的速率限制，持续约半天时间。

Sectigo的高级研究员Jason Soroko强调了这一发现的更广泛影响，他说：“AuthQuake突显了微软MFA实现中的重大缺陷。这是对组织采用补丁并重新考虑对过时MFA解决方案依赖的警钟。走向无密码认证不仅是趋势，也是为了未来证明我们的安全措施的必要性。”

**对用户和公司的教训**

虽然特定的漏洞已经被修补，但组织应该通知员工网络安全的重要性，并鼓励他们报告任何可疑的登录尝试。此外，尽管最近出现了问题，MFA仍然是关键的安全措施，因此，使用认证器应用或探索更强的无密码方法以获得额外保护。

本文翻译自hackread [原文链接](https://hackread.com/authquake-flaw-mfa-bypass-azure-office-365-accounts/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302703](/post/id/302703)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/authquake-flaw-mfa-bypass-azure-office-365-accounts/)

如若转载,请注明出处： <https://hackread.com/authquake-flaw-mfa-bypass-azure-office-365-accounts/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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