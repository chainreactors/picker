---
title: 攻击者在“PoisonSeed”钓鱼攻击中通过降级手段绕过FIDO2多因素认证（MFA）
url: https://www.anquanke.com/post/id/310339
source: 安全客-有思想的安全新媒体
date: 2025-07-22
fetch_date: 2025-10-06T23:16:38.223599
---

# 攻击者在“PoisonSeed”钓鱼攻击中通过降级手段绕过FIDO2多因素认证（MFA）

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

# 攻击者在“PoisonSeed”钓鱼攻击中通过降级手段绕过FIDO2多因素认证（MFA）

阅读量**79340**

发布时间 : 2025-07-21 17:41:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/threat-actors-downgrade-fido2-mfa-auth-in-poisonseed-phishing-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

PoisonSeed钓鱼活动通过**滥用WebAuthn的跨设备登录功能**，绕过**FIDO2安全密钥保护**，诱使用户在虚假企业门户上批准登录认证请求。

PoisonSeed威胁行为者以**大规模钓鱼攻击进行金融诈骗**而闻名。过去，他们通过发送包含加密货币助记词的邮件来窃取数字钱包资产。

Expel近期观察到的此次钓鱼攻击中，PoisonSeed攻击者并未利用FIDO2安全机制的漏洞，而是滥用其合法的跨设备认证功能。

**跨设备认证**是WebAuthn的一项特性，允许用户通过在另一设备上的安全密钥或认证应用完成登录，而无需物理连接，如插入安全密钥，认证请求通过蓝牙或二维码扫描在设备间传输。

攻击过程始于将用户引导至**冒充Okta或Microsoft 365等企业登录门户的钓鱼网站**。当用户在门户输入凭据时，攻击者利用中间人（AiTM）后端，实时悄无声息地使用提交的凭据登录真实门户。

受害用户通常会使用FIDO2安全密钥验证多因素认证请求，但钓鱼后端告知真实门户使用跨设备认证，导致门户生成二维码并返回给钓鱼页面展示给用户。

当用户使用智能手机或认证应用扫描该二维码时，即**自动批准**了攻击者发起的登录尝试。

![]()

这种攻击方法通过让攻击者发起依赖跨设备认证的登录流程，而非用户的实体FIDO2安全密钥，从而有效**绕过了FIDO2安全密钥的保护**。

Expel警告称，该攻击并未利用FIDO2实现中的漏洞，而是滥用了一个合法功能，导致FIDO密钥认证过程被降级。

为降低风险，Expel建议采取以下防御措施：

1. 限制用户允许登录的地理位置，并为出差人员建立注册流程；

2. 定期检查来自未知地点和不常见安全密钥品牌的未知FIDO密钥注册情况；

3. 组织可考虑强制要求跨设备认证必须使用基于蓝牙的认证方式，这将显著降低远程钓鱼攻击的有效性。

Expel还观察到另一事件，攻击者在通过疑似钓鱼手段攻破账户并重置密码后，**注册了自己的FIDO密钥**，该攻击**无需通过二维码**等方式欺骗用户。

此次攻击凸显了威胁行为者通过诱导用户完成**绕过实体安全密钥物理交互的登录流程，来规避抗钓鱼认证的手段**。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/threat-actors-downgrade-fido2-mfa-auth-in-poisonseed-phishing-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310339](/post/id/310339)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/threat-actors-downgrade-fido2-mfa-auth-in-poisonseed-phishing-attack/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/threat-actors-downgrade-fido2-mfa-auth-in-poisonseed-phishing-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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