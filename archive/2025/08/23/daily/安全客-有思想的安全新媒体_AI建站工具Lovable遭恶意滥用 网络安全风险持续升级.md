---
title: AI建站工具Lovable遭恶意滥用 网络安全风险持续升级
url: https://www.anquanke.com/post/id/311398
source: 安全客-有思想的安全新媒体
date: 2025-08-23
fetch_date: 2025-10-07T00:17:52.890535
---

# AI建站工具Lovable遭恶意滥用 网络安全风险持续升级

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

# AI建站工具Lovable遭恶意滥用 网络安全风险持续升级

阅读量**78171**

发布时间 : 2025-08-22 17:17:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/ai-website-builder-lovable-increasingly-abused-for-malicious-activity/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络犯罪分子正日益滥用人工智能驱动的**Lovable**网站创建与托管平台，大量生成钓鱼页面、恶意软件投放门户及各类欺诈网站。

**通过该平台创建的恶意网站仿冒知名大型品牌**，并配备验证码等流量过滤系统以阻隔机器人检测。尽管**Lovable**已采取措施加强平台防护，但随着AI建站生成器数量的增长，网络犯罪的入行门槛持续降低。

![]()

### 由Lovable驱动的恶意活动

自二月以来，网络安全公司Proofpoint”观察到数万个通过电子邮件传播的**Lovable**链接被标记为威胁”。研究人员在今日报告中详细描述了四起滥用该AI建站工具的恶意活动。

典型案例是依托名为Tycoon的网络钓鱼即服务平台的大规模操作。欺诈邮件包含**Lovable**托管的链接，这些链接会先出现验证码界面，随后将用户重定向至带有Azure AD或Okta品牌标识的虚假微软登录页面。

这些网站通过中间人攻击技术窃取用户凭证、多因素认证（MFA）令牌和会话Cookie。在此活动期间，威胁行为者向5000家机构发送了数十万条欺诈信息。

![]()

第二起案例是冒充UPS快递的支付与数据窃取活动。犯罪分子发送近3500封钓鱼邮件，内含导向钓鱼网站的链接。这些网站要求访问者输入个人信息、信用卡号码及短信验证码，所有数据均被实时传输至攻击者控制的Telegram频道。

![]()

第三起活动针对加密货币领域，攻击者仿冒去中心化金融平台Aave，通过SendGrid邮件服务发送近万封欺诈邮件。目标用户被引导至由Lovable生成的跳转链接和钓鱼页面，诱骗其连接数字钱包，后续极可能实施资产盗取。

![]()

第四起案例涉及远程访问木马zgRAT的恶意软件传播活动。邮件中的链接指向伪装成发票门户的**Lovable**应用，最终投放托管于Dropbox的RAR压缩包。该文件包含一个经合法签名的可执行程序及被篡改的DLL文件，通过加载DOILoader最终部署zgRAT木马。

### 应对滥用行为

**Lovable**于七月推出了实时恶意网站创建检测系统，并每日自动扫描已发布项目，以识别和清除欺诈行为。该开发团队还宣布计划在今年秋季引入额外防护措施，主动识别并封禁平台上的滥用账户。

网络安全公司Guardio Labs向BleepingComputer证实，目前仍可利用Lovable创建恶意网站。在近期测试中，研究人员成功生成冒充大型零售商的欺诈网站，全程未遭遇平台拦截。

**Lovable**在致BleepingComputer的声明中表示，其当前策略是在恶意应用或网站广泛传播前，通过检测、预防和响应机制应对网络犯罪活动。该公司称已实施AI驱动的安全计划用于政策执行，会主动拦截违反政策的项目。

“我们的支持与安全团队持续保持监控，仅过去两周就下线了300多个违规网站，”公司发言人表示。一位**Lovable**代表还透露，当前系统每周拦截约1000个违反平台规则的特殊项目，并强调”Lovable绝不会容忍非法或恶意内容”。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/ai-website-builder-lovable-increasingly-abused-for-malicious-activity/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311398](/post/id/311398)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/ai-website-builder-lovable-increasingly-abused-for-malicious-activity/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/ai-website-builder-lovable-increasingly-abused-for-malicious-activity/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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