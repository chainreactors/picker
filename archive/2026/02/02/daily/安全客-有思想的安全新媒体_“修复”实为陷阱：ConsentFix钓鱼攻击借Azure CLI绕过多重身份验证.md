---
title: “修复”实为陷阱：ConsentFix钓鱼攻击借Azure CLI绕过多重身份验证
url: https://www.anquanke.com/post/id/314685
source: 安全客-有思想的安全新媒体
date: 2026-02-02
fetch_date: 2026-02-03T04:08:26.876701
---

# “修复”实为陷阱：ConsentFix钓鱼攻击借Azure CLI绕过多重身份验证

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

# “修复”实为陷阱：ConsentFix钓鱼攻击借Azure CLI绕过多重身份验证

阅读量**14457**

发布时间 : 2026-02-02 16:11:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/the-fix-is-a-trap-consentfix-phishing-bypasses-mfa-via-azure-cli/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种狡猾的新型钓鱼技术正利用用户对微软官方工具的信任实施攻击。这种被命名为 “ConsentFix”（又称 AuthCodeFix）的攻击手段，通过滥用 Azure CLI 等正规应用所采用的**OAuth 2.0 授权流程**，诱骗受害者交出微软账号的控制权。

该技术由 NVISO 威胁检测工程团队的斯塔马蒂斯・查齐芒古分析发现，标志着 “修复类” 钓鱼攻击迎来**危险的进化**。攻击者不再窃取密码，而是盗取预先批准的**授权码**，借此绕过多重身份验证（MFA）和条件访问策略。

攻击以经典场景启动：受害者被诱导访问钓鱼页面并尝试登录。但关键陷阱出现在身份验证之后 —— 受害者会被重定向至微软官方登录页面，要求授权一款应用，而该应用通常是 Azure CLI 这类受信任的微软第一方工具。

由于 Azure CLI 是微软官方应用，它 “被 Entra ID 默认信任”，这意味着用户往往**不会看到任何授权确认弹窗**，直接完成授权流程。

当受害者被重定向至**[localhost](https://localhost)本地地址**时，陷阱正式触发。由于受害者设备上并未运行任何能接收该请求的应用，浏览器会显示 “无法访问此网站” 的错误页面。这一错误并非意外，而是攻击者刻意设计的核心环节。

“攻击者会利用这一情况，指示受害者：若出现该错误，需将包含授权码的 URL 复制粘贴回钓鱼网站。”

受害者误以为自己在 “修复” 登录故障，便手动将包含**核心授权码**的 URL 粘贴到攻击者的虚假网站中。

攻击者获取该授权码后，可通过微软 API 将其兑换为**访问令牌**。该令牌将赋予攻击者与所伪造应用相同的权限，直接访问受害者的账号。

关键在于，这一兑换过程在攻击者的设备上完成，从而**彻底规避了安全控制**。“尽管用户最初的登录行为受条件访问策略约束，但一旦攻击者获取授权码，便可将其兑换为访问令牌，且不会触发新的条件访问评估。”

这使得攻击者能够 “从未经合规验证的设备或不受信任的位置获取令牌”—— 而这些场景在正常情况下都会被拦截。

报告指出，Azure CLI 只是众多存在漏洞的微软第一方应用之一，其他还包括：

* Microsoft Azure PowerShell（微软 Azure PowerShell）
* Visual Studio Code（Visual Studio 代码编辑器）
* Microsoft Teams（微软 Teams）
* Microsoft SharePoint Online Management Shell（微软 SharePoint Online 管理外壳）

攻击者可选择不同的 “回调 URI” 让骗局更具迷惑性。例如，使用`https://aadrm.com/adminpowershell`作为回调地址，会将受害者重定向至看似正规的页面，但授权码仍会暴露在地址栏中。

由于该攻击滥用的是**正规授权流程**，若不影响必要的开发者工具正常使用，很难对其进行拦截。但查齐芒古指出，攻击行为会在日志中留下痕迹。

安全团队可通过关联受害者的初始登录记录与攻击者后续的令牌兑换行为，发现此类攻击。关键在于排查`AADNonInteractiveUserSignInLogs`日志表中的**IP 地址和位置字段差异**：同一会话 ID（Session ID）会显示来自两个地理位置遥远的活动记录 —— 分别是受害者和攻击者的位置。

随着用户对传统凭证钓鱼的防范意识不断提升，ConsentFix 攻击提醒我们：攻击者正将目标转向**身份认证底层协议本身**，安全防护需进一步向协议层面延伸。

本文翻译自securityonline [原文链接](https://securityonline.info/the-fix-is-a-trap-consentfix-phishing-bypasses-mfa-via-azure-cli/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314685](/post/id/314685)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/the-fix-is-a-trap-consentfix-phishing-bypasses-mfa-via-azure-cli/)

如若转载,请注明出处： <https://securityonline.info/the-fix-is-a-trap-consentfix-phishing-bypasses-mfa-via-azure-cli/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

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
* **990**

* 粉丝
* **6**

### TA的文章

* ##### [明修栈道，暗度陈仓：TA584组织投放“傲娇僵尸程序”并利用隐形注册表项实施攻击](/post/id/314678)

  2026-02-02 16:32:30
* ##### [苹果为十年前iPhone推出史无前例的安全更新，标志着老旧设备支持策略生变](/post/id/314675)

  2026-02-02 16:15:59
* ##### [太空探索技术公司的大胆布局：星链数据中心卫星如何重塑云计算经济格局](/post/id/314671)

  2026-02-02 16:12:53
* ##### [飞塔单点登录配置漏洞暴露企业认证系统核心安全隐患](/post/id/314667)

  2026-02-02 16:12:24
* ##### [签名盗用：“幻影窃取者”借虚假敦豪物流发票攻陷Java应用](/post/id/314681)

  2026-02-02 16:11:51

### 相关文章

* ##### [明修栈道，暗度陈仓：TA584组织投放“傲娇僵尸程序”并利用隐形注册表项实施攻击](/post/id/314678)

  2026-02-02 16:32:30
* ##### [苹果为十年前iPhone推出史无前例的安全更新，标志着老旧设备支持策略生变](/post/id/314675)

  2026-02-02 16:15:59
* ##### [太空探索技术公司的大胆布局：星链数据中心卫星如何重塑云计算经济格局](/post/id/314671)

  2026-02-02 16:12:53
* ##### [飞塔单点登录配置漏洞暴露企业认证系统核心安全隐患](/post/id/314667)

  2026-02-02 16:12:24
* ##### [签名盗用：“幻影窃取者”借虚假敦豪物流发票攻陷Java应用](/post/id/314681)

  2026-02-02 16:11:51
* ##### [Moltbook AI平台曝出高危漏洞，致邮箱地址、登录令牌及API密钥泄露](/post/id/314663)

  2026-02-02 16:11:48
* ##### [工业控制系统监控与数据采集漏洞引发拒绝服务攻击，或对工业生产运营造成中断影响](/post/id/314653)

  2026-02-02 16:11:14

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