---
title: 警惕 Cookie-Bite！多因素认证失效，云环境面临持续入侵风险
url: https://www.anquanke.com/post/id/306926
source: 安全客-有思想的安全新媒体
date: 2025-04-28
fetch_date: 2025-10-06T22:04:15.321602
---

# 警惕 Cookie-Bite！多因素认证失效，云环境面临持续入侵风险

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

# 警惕 Cookie-Bite！多因素认证失效，云环境面临持续入侵风险

阅读量**68160**

发布时间 : 2025-04-27 14:33:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/cookie-bite-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

一种被称为 “Cookie-Bite” 的复杂攻击技术，使网络犯罪分子能够在悄无声息中绕过多因素身份验证（MFA），并持续保持对云环境的访问权限。

Varonis Threat Labs 披露，攻击者利用窃取来的浏览器 Cookie 冒充合法用户，且无需使用用户的凭据，这实际上让传统的多因素身份验证保护措施形同虚设。

这种攻击的目标是关键的身份验证 Cookie，尤其是 Azure Entra ID（前身为 Azure Active Directory）所使用的 ESTSAUTH 和 ESTSAUTHPERSISTENT Cookie。这些 Cookie 可维持已通过身份验证的云会话，并允许用户访问 Microsoft 365、Azure 门户以及各种企业应用程序。
研究人员解释道：“通过劫持这些会话令牌，攻击者可以绕过多因素身份验证，冒充用户，并在云环境中进行横向移动。这使得这些 Cookie 成为信息窃取者和威胁行为者最有价值的攻击目标之一。”
网络犯罪分子采用多种方法来窃取这些身份验证 Cookie，其中包括：

1.使用反向代理工具进行中间人（AITM）攻击，以实时拦截 Cookie。

2.转储浏览器进程内存，以便从活动会话中提取已解密的 Cookie。

3.利用恶意浏览器扩展程序，在浏览器的安全环境中直接访问 Cookie。

4.解密本地存储的浏览器 Cookie 数据库。

研究人员的概念验证展示了攻击者如何创建自定义的 Chrome 扩展程序，该程序可在用户每次登录 Microsoft 的身份验证门户时，悄无声息地提取身份验证 Cookie。

这些 Cookie 随后会被泄露到攻击者控制的服务器上，并可被注入到威胁行为者的浏览器中，从而使攻击者能够立即访问受害者的云会话。

****无需凭据的持续访问****

“Cookie-Bite” 攻击特别危险之处在于其持续性。与传统的凭据窃取不同，这种技术不需要知道受害者的密码，也无需拦截多因素身份验证代码。一旦部署了恶意扩展程序，每次受害者登录时，该程序都会继续提取新的身份验证 Cookie。

研究人员指出：“这种技术确保了能持续提取有效的会话 Cookie，即使密码被更改或会话被撤销，攻击者仍能获得长期的未经授权访问权限。”

更令人担忧的是，这种攻击能够绕过企业作为额外安全层而部署的条件访问策略（CAPs）。

攻击者可以通过收集受害者环境的详细信息（包括域名、主机名、操作系统、IP 地址和浏览器指纹），精确模仿合法的访问模式。

通过成功的身份验证，攻击者能够访问像 Microsoft Graph Explorer 这样的关键企业应用程序，从而得以枚举用户、访问电子邮件，并有可能在企业内部提升权限。

安全专家建议采取以下几种应对措施来防范 “Cookie-Bite” 攻击：

1.持续监控异常的用户行为模式和可疑的登录情况。

2.在登录事件中利用Microsoft的风险检测功能。

3.配置条件访问策略，强制要求仅从合规设备进行登录。

4.实施 Chrome 策略，将浏览器扩展程序限制在已批准的白名单范围内。

5.部署令牌保护机制，以检测和防止令牌被盗。

随着云技术应用的加速发展，这些 Cookie 劫持技术凸显了基于身份验证的攻击手段的不断演变。企业必须调整其安全态势，以应对这些针对云身份验证系统基本信任机制的复杂威胁。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/cookie-bite-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306926](/post/id/306926)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/cookie-bite-attack/)

如若转载,请注明出处： <https://cybersecuritynews.com/cookie-bite-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**10赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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