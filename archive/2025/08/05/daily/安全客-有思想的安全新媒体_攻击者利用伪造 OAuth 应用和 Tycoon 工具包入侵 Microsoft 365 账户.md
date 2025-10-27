---
title: 攻击者利用伪造 OAuth 应用和 Tycoon 工具包入侵 Microsoft 365 账户
url: https://www.anquanke.com/post/id/310868
source: 安全客-有思想的安全新媒体
date: 2025-08-05
fetch_date: 2025-10-07T00:17:43.566421
---

# 攻击者利用伪造 OAuth 应用和 Tycoon 工具包入侵 Microsoft 365 账户

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

# 攻击者利用伪造 OAuth 应用和 Tycoon 工具包入侵 Microsoft 365 账户

阅读量**88558**

发布时间 : 2025-08-04 17:16:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：thehackernews

原文地址：<https://thehackernews.com/2025/08/attackers-use-fake-oauth-apps-with.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员近日披露了一起新型攻击活动：攻击者通过**伪造企业身份**创建**假冒的 Microsoft OAuth 应用程序**，诱导用户授权，从而窃取凭证并接管 Microsoft 365 账户。

Proofpoint 在周四的报告中指出：“这些假冒的 Microsoft 365 应用程序伪装成多个知名公司的服务，包括 RingCentral、SharePoint、Adobe 和 Docusign。”

这波攻击活动最早于 **2025 年初**被发现，攻击者通过**钓鱼工具包（如 Tycoon 和 ODx）**发起攻击，利用 OAuth 应用作为突破口，绕过多因素身份验证（MFA），非法获取用户的 Microsoft 365 账户访问权限。

据该安全公司观察，此类攻击已被用于多个邮件钓鱼活动中，涉及 **超过 50 个伪造的应用程序**。

攻击通常以来自已被攻陷账户的钓鱼邮件开场，邮件内容伪装成“报价请求”（RFQ）或商业合同的共享请求，诱使收件人点击链接。

点击后，受害者会被引导至一个伪造的 Microsoft OAuth 授权页面，该页面请求用户授权一个名为 “iLSMART” 的应用访问其基础资料，并持续访问已有授权的数据。

值得注意的是，攻击者伪造的“iLSMART”正是一个真实存在的航空、航海和国防行业配件与维修服务在线交易平台。攻击者利用该平台的合法身份来提高钓鱼页面的**可信度**。

Proofpoint 表示：“虽然这些应用请求的权限对攻击者的直接利用价值有限，但它们为下一阶段的攻击埋下了伏笔。”

无论用户是否同意授权，都会被重定向到一个验证码页面，验证通过后再跳转到一个伪造的 Microsoft 登录页面。这一页面通过 Tycoon 提供的**“中间人钓鱼”（AiTM）**技术，窃取用户的**账户凭证和 MFA 验证码**。

就在上月，Proofpoint 还发现另一波冒充 Adobe 的攻击活动，攻击邮件通过 Twilio SendGrid 发送，目的是诱导用户点击授权链接或触发取消操作，从而将用户重定向到钓鱼网站。

尽管这只是 Tycoon 工具包相关攻击活动中的冰山一角，但其影响范围依然广泛。2025 年以来，已有 **近 3000 个用户账户、覆盖 900 多个 Microsoft 365 环境**遭遇类似尝试入侵。

Proofpoint 警告道：“攻击者正在不断创造更复杂的攻击链，试图绕过安全检测，入侵全球各地的组织。我们预计，未来他们会愈发集中攻击‘身份’本身，AiTM 凭证钓鱼将逐步成为网络犯罪的主流手段。”

对此，微软已于上月宣布将更新默认安全设置：**禁用旧版认证协议，并要求第三方应用获取管理员授权**。此更新预计将于 2025 年 8 月前完成。

Proofpoint 表示：“这项更新将在整体上提升安全水平，限制攻击者利用该类技术的能力。”

此次披露还与微软另一项安全变更同步：自 2025 年 10 月至 2026 年 7 月，**微软将逐步默认禁用 Excel 外部工作簿对高风险文件类型的链接**，以提升数据安全。

与此同时，Seqrite 也警告称，近期有针对企业的定向钓鱼邮件伪装成付款收据，利用 AutoIt 注入器传播一种名为 **VIP Keylogger** 的 .NET 恶意软件，该软件可从受害主机中窃取敏感信息。

还有报告指出，自 2024 年 11 月以来，有攻击活动**通过 PDF 文件**隐藏远程桌面工具的安装链接，以绕过邮箱和安全系统防护，目标主要集中在法国、卢森堡、比利时和德国。

芬兰安全公司 WithSecure 表示：“这些 PDF 通常伪装成发票、合同或房产信息，看起来像是被隐藏的合法内容，从而诱导用户点击链接并安装程序。”所引导安装的程序名为 **FleetDeck RMM**，为远程监控与管理工具。

此外，攻击者还部署了多个 RMM 工具，包括 Action1、OptiTune、Bluetrait、Syncro、SuperOps、Atera 和 ScreenConnect 等。

WithSecure 总结称：“虽然目前尚未发现后续载荷，但使用 RMM 工具高度暗示其作为初始访问载体的角色，**尤其受到勒索软件团伙的青睐**。”

本文翻译自thehackernews [原文链接](https://thehackernews.com/2025/08/attackers-use-fake-oauth-apps-with.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310868](/post/id/310868)

安全KER - 有思想的安全新媒体

本文转载自: [thehackernews](https://thehackernews.com/2025/08/attackers-use-fake-oauth-apps-with.html)

如若转载,请注明出处： <https://thehackernews.com/2025/08/attackers-use-fake-oauth-apps-with.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

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