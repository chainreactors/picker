---
title: Proton 推出独立身份验证器：将多因素认证与密码分离，追求极致安全
url: https://www.anquanke.com/post/id/310768
source: 安全客-有思想的安全新媒体
date: 2025-08-02
fetch_date: 2025-10-07T00:17:56.710220
---

# Proton 推出独立身份验证器：将多因素认证与密码分离，追求极致安全

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

# Proton 推出独立身份验证器：将多因素认证与密码分离，追求极致安全

阅读量**100624**

发布时间 : 2025-08-01 17:24:40

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/proton-launches-standalone-authenticator-separating-mfa-from-passwords-for-ultimate-security/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

端到端（End-to-end）加密邮件服务提供商 **ProtonMail** 近日发布了全新的**跨平台多因素认证（MFA）应用** —— **Proton Authenticator**。该应用支持云同步，是 Proton 密码管理器之外的又一新成员。延续 Proton 一贯的理念，新应用依然坚持开源和端到端加密。

那么，Proton 为什么不将 MFA 功能直接整合进自家的密码管理器，并作为付费功能推出？背后的原因是为了解决当前行业中一个关键的安全隐患：**将密码管理和 MFA 捆绑在一个工具中，反而可能削弱整体安全性。**

自 Google Authenticator 推出以来，MFA 应用大多运行在移动设备上。这种**设备间的分离设计**，能有效防止密码泄露后 MFA 验证码也被一并获取。例如，用户通常在桌面端使用密码管理器自动填充登录信息，而 MFA 验证码则保存在手机等独立设备中，更加安全。

相比之下，一些**集成了账号密码和 MFA** 的工具（如 1Password），则存在较大风险：一旦密码管理器的数据库遭到攻击，或攻击者接触到未锁定的电脑，就可能同时获取登录凭据和验证码，从而完全接管账户。

![]()

如果追求便利性，用户可以选择使用**集成 MFA 的密码管理器**（如 Proton Pass），实现无缝登录体验；但若追求最高安全性，更推荐单独使用 Proton Authenticator，手动获取并输入验证码，从而保持账号信息与认证机制的有效隔离。

Proton Authenticator 使用**端到端加密**，只有在用户成功认证后，数据才会在本地解密，并可在离线状态下访问。即便是 Proton 官方，也无法读取存储在其服务器上的用户验证数据，安全性大大提升。

此外，该应用还支持**生物识别与PIN 解锁**，即使在用户设备本身上，也能保障验证码的安全。Proton Authenticator 支持 Windows、macOS、Linux、Android 和 iOS 多平台，并可实现**数据的无缝同步**。

用户还可轻松从其他身份验证器导入数据，无需繁琐地手动解绑、重新绑定账号。同时也支持导出功能，方便未来的数据迁移。

本文翻译自securityonline [原文链接](https://securityonline.info/proton-launches-standalone-authenticator-separating-mfa-from-passwords-for-ultimate-security/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310768](/post/id/310768)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/proton-launches-standalone-authenticator-separating-mfa-from-passwords-for-ultimate-security/)

如若转载,请注明出处： <https://securityonline.info/proton-launches-standalone-authenticator-separating-mfa-from-passwords-for-ultimate-security/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**7赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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