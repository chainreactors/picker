---
title: 钓鱼攻击新变种：“同形异字”绕过防御，AI助推风险升级
url: https://www.anquanke.com/post/id/310659
source: 安全客-有思想的安全新媒体
date: 2025-07-29
fetch_date: 2025-10-06T23:50:23.994668
---

# 钓鱼攻击新变种：“同形异字”绕过防御，AI助推风险升级

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

# 钓鱼攻击新变种：“同形异字”绕过防御，AI助推风险升级

阅读量**62721**

发布时间 : 2025-07-28 16:37:47

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/the-homograph-illusion-phishing-attacks-exploit-lookalike-characters-to-bypass-defenses-ai-amplifies-the-threat/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在最新的报告中，Palo Alto Networks 的 Unit 42 揭示了一种隐蔽的钓鱼技术，这种技术继续绕过人类感知和自动化防御：同形异字攻击。这些攻击利用拉丁字母与非拉丁字母（如西里尔字母和希腊字母）之间的视觉相似性，制作看似完全合法的邮件，但隐藏着微妙的操控，欺骗眼睛并逃避检测。

对人眼而言，“Homograph”和“Ηоmоgraph”之间没有区别。但实际上，后者包含了希腊字母和西里尔字母，而不是拉丁字母。例如，拉丁字母“H”被替换成希腊字母“Η”，而“o”则被西里尔字母“о”替换。

报告指出：“自动化防御系统在分析这个词时无法识别它为实际的词，因此可能会认为它是有效的，或者在分析过程中跳过了被操控的词。”

这些相似字符欺骗了人类和机器，创造出一种新的钓鱼邮件类型，能够绕过内容过滤，冒充可信实体，诱使用户与恶意内容互动。

Unit 42 的研究强调了三个成功使用同形异字技术的钓鱼攻击案例，涉及不同类型的邮件信息。

### 案例 1：Google Drive 文件共享钓鱼攻击

攻击者冒充一家跨国金融机构，通过 Google Drive 与目标共享文档。邮件的显示名称通过同形异字字符模仿该公司，尽管实际的发件人域名与之无关。内置的过滤器未能标记该邮件为钓鱼邮件。

![]()

该文档包含一个“VERIFY”按钮，指向 messageconnection.blob.core[.]windows[.]net —— 这是一个被认为用于凭证窃取或恶意软件传播的域名。

### **案例研究 2：虚假电子签名平台**

在另一个场景中，攻击者假装发送电子文档供签署。邮件主题和显示名称中的词汇——如“Сonfidеntiаl”、“Տtаtеmеnt”和“Ꭲiꮯkеt”——都包含了具有欺骗性的字符。

这些邮件伪装成 DocuSign，点击“SIGN DOCUMENTS”按钮会触发一系列重定向，最终指向恶意域名，如 kig.skyvaulyt[.]ru。

这个复杂的骗局还包括一个虚假的验证页面和定制的邮件内容，其中包含目标的姓名、公司品牌和真实的 CAPTCHA 挑战，使得即使是警觉的用户也难以察觉。

### **案例研究 3：Spotify 账单伪装**

第三个案例模仿了 Spotify，邮件敦促用户更新他们的支付方式。显示名称“Sρօtifу”中包含多个非拉丁字符，误导用户认为发件人是合法的。

攻击者使用了一个受信任的 URL 缩短服务，掩盖了链接的真实意图，该链接很可能引导用户到一个用于凭证窃取的钓鱼网站。

Unit 42 的报告警告称，人工智能正在加剧这一威胁，攻击者能够快速生成看似真实的邮件。当与同形异字技术结合时，这些邮件几乎无法与合法邮件区分开来。

“新人工智能模型的广泛应用使得攻击者能够创建更具说服力和个性化的邮件，”报告总结道。

本文翻译自securityonline [原文链接](https://securityonline.info/the-homograph-illusion-phishing-attacks-exploit-lookalike-characters-to-bypass-defenses-ai-amplifies-the-threat/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310659](/post/id/310659)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/the-homograph-illusion-phishing-attacks-exploit-lookalike-characters-to-bypass-defenses-ai-amplifies-the-threat/)

如若转载,请注明出处： <https://securityonline.info/the-homograph-illusion-phishing-attacks-exploit-lookalike-characters-to-bypass-defenses-ai-amplifies-the-threat/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**7赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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