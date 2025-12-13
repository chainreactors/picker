---
title: 利用薪资评审诱饵实施精密钓鱼攻击：绕过防御窃取 Okta 单点登录会话令牌
url: https://www.anquanke.com/post/id/313745
source: 安全客-有思想的安全新媒体
date: 2025-12-12
fetch_date: 2025-12-13T03:13:50.293154
---

# 利用薪资评审诱饵实施精密钓鱼攻击：绕过防御窃取 Okta 单点登录会话令牌

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

# 利用薪资评审诱饵实施精密钓鱼攻击：绕过防御窃取 Okta 单点登录会话令牌

阅读量**16692**

发布时间 : 2025-12-12 18:24:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/sophisticated-okta-sso-phishing-bypasses-defenses-to-steal-session-tokens-with-salary-review-lures/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

就在员工们开始期待年终绩效评估之际，一场**精密的新型钓鱼攻击行动**悄然浮出水面，将加薪的期待转化为了一场网络安全噩梦。**Datadog 安全实验室**发布的一份新报告显示，目前正有一场活跃的攻击行动，专门针对采用**Microsoft 365**与 \*\*Okta 单点登录（SSO）\*\* 方案的机构，攻击者运用先进技术绕过安全防护机制，进而窃取用户会话令牌。

这场攻击行动自 2025 年 12 月初便处于活跃状态，其阴险之处在于**恶意利用企业福利发放周期**实施诈骗。受害者会收到伪装成人力资源部门，或是**ADP、Salesforce**等薪资服务机构发送的钓鱼邮件。邮件主题经过精心设计，目的是引发收件人的紧迫感与好奇心，常见标题包括 “**紧急行动：请查阅你的 2026 年薪资与奖金信息**” 或 “**机密：薪酬调整通知**”。

部分攻击还会采用带密码保护的加密 PDF 附件，而密码则直接在邮件正文中提供 —— 这是一种用于**绕过邮件安全扫描器检测的经典手段**。

该钓鱼攻击行动的与众不同之处，在于其在身份联合认证环节展现出的**极高技术复杂度**。攻击者搭建了一套 “代理” 系统，这个系统绝非简单模仿登录页面的外观，而是能够**与真实的登录页面进行交互**。

本文翻译自securityonline [原文链接](https://securityonline.info/sophisticated-okta-sso-phishing-bypasses-defenses-to-steal-session-tokens-with-salary-review-lures/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313745](/post/id/313745)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/sophisticated-okta-sso-phishing-bypasses-defenses-to-steal-session-tokens-with-salary-review-lures/)

如若转载,请注明出处： <https://securityonline.info/sophisticated-okta-sso-phishing-bypasses-defenses-to-steal-session-tokens-with-salary-review-lures/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **800**

* 粉丝
* **6**

### TA的文章

* ##### [利用薪资评审诱饵实施精密钓鱼攻击：绕过防御窃取 Okta 单点登录会话令牌](/post/id/313745)

  2025-12-12 18:24:46
* ##### [高危漏洞预警 | CVE-2025-64188（CVSS 9.8）：WordPress “Soledad” 主题存在严重缺陷，订阅用户可直接接管网站](/post/id/313703)

  2025-12-12 18:05:27
* ##### [OpenAI 严阵以待：下一代 AI 模型或具备突破防御体系的能力](/post/id/313710)

  2025-12-12 18:04:59
* ##### [恶意 Visual Studio Code 扩展程序藏身虚假 PNG 文件，内置特洛伊木马](/post/id/313712)

  2025-12-12 18:04:19
* ##### [2022 年数据泄露致 160 万用户受影响，英国对 LastPass 处以 120 万英镑罚款](/post/id/313715)

  2025-12-12 18:03:30

### 相关文章

* ##### [高危漏洞预警 | CVE-2025-64188（CVSS 9.8）：WordPress “Soledad” 主题存在严重缺陷，订阅用户可直接接管网站](/post/id/313703)

  2025-12-12 18:05:27
* ##### [OpenAI 严阵以待：下一代 AI 模型或具备突破防御体系的能力](/post/id/313710)

  2025-12-12 18:04:59
* ##### [恶意 Visual Studio Code 扩展程序藏身虚假 PNG 文件，内置特洛伊木马](/post/id/313712)

  2025-12-12 18:04:19
* ##### [2022 年数据泄露致 160 万用户受影响，英国对 LastPass 处以 120 万英镑罚款](/post/id/313715)

  2025-12-12 18:03:30
* ##### [Notepad++ 漏洞存在重大风险：攻击者可劫持网络流量，通过更新通道植入恶意软件](/post/id/313725)

  2025-12-12 18:02:46
* ##### [新型恶意软件 DroidLock 现身：锁定安卓设备并索要赎金](/post/id/313730)

  2025-12-12 18:01:37
* ##### [技能缺口持续扩大，INE 聚焦企业培训模式向实践操作转型](/post/id/313735)

  2025-12-12 18:00:56

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