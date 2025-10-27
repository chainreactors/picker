---
title: Netflix招聘骗局：借虚假职位窃取用户Facebook登录数据
url: https://www.anquanke.com/post/id/311234
source: 安全客-有思想的安全新媒体
date: 2025-08-16
fetch_date: 2025-10-07T00:13:11.334064
---

# Netflix招聘骗局：借虚假职位窃取用户Facebook登录数据

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

# Netflix招聘骗局：借虚假职位窃取用户Facebook登录数据

阅读量**73500**

发布时间 : 2025-08-15 17:22:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/netflix-job-phishing-scam-steals-facebook-login-data/>

译文仅供参考，具体内容表达以及含义原文为准。

安全研究人员近日警告称，一种利用虚假Netflix招聘信息的新型网络钓鱼骗局正针对求职者实施攻击，诱骗他们泄露Facebook账户登录信息。

据Malwarebytes安全研究人员披露，这一攻击活动主要锁定从事市场营销及社交媒体相关工作的求职者。攻击者通过伪造的Netflix职位邀请与面试流程获取受害者信任，并在过程中引导他们输入Facebook账号与密码，从而窃取登录凭证。

研究人员提醒，求职者在接收到来源可疑或流程异常的招聘信息时，应仔细核实职位真实性，避免在不可信的平台或链接中输入任何敏感账户信息，以防遭受账号被盗等安全风险。

Malwarebytes在接受Hackread.com采访时透露了该网络钓鱼活动的细节，指出其技术手段更为高级，且主要针对企业的社交媒体账户。

### **攻击流程如下**

根据Malwarebytes的报告，**诈骗邮件通常由AI生成，外观高度仿真**，几乎与Netflix人力资源团队发出的正式面试邀请邮件一致，并会根据收件人的职业背景进行个性化定制。

求职者一旦点击邮件中的**“安排面试”（Schedule Interview）链接**，就会被引导至一个伪造的招聘网站，该页面在外观上与Netflix官网极为相似，但仔细查看网址即可发现其为钓鱼站点。

该虚假页面会提示用户创建“职业档案”（Career Profile），并提供使用Facebook账号或电子邮件地址登录的选项。但无论选择哪种方式，下一步都会要求通过Facebook账号登录——这正是攻击的关键环节。Malwarebytes提供的登录页面截图显示，攻击者的真正目标是窃取Facebook的登录凭证。

更为隐蔽的是，黑客利用特殊的WebSocket方法在受害者输入信息的瞬间即时捕获登录数据。**一旦点击“登录”（Log In）按钮，攻击者便可立即尝试访问受害者的真实Facebook账户**。即便密码输入错误，由于攻击响应极快，账户仍可能已被部分或完全控制。

此外，所谓的面试安排页面本身也具有明显的欺骗性，进一步迷惑受害者，使其难以及时察觉风险。

![]()

这一登录页面也是使此次攻击更为复杂和高明的关键所在。**攻击者利用WebSocket方法，在用户输入凭证的同时实时拦截提交数据**，从而能够立即尝试这些登录信息。若密码有效，他们可在数秒内登录受害者的真实Facebook账户；如需多因素认证（MFA），攻击者也可能立刻发起验证请求，以进一步获取账户访问权限。

真正的危险在于，此类诈骗的目的不仅是窃取个人的Facebook账户。攻击者瞄准的是那些拥有企业Facebook商务账户管理权限的专业人士。**一旦控制这些账户，黑客便可发起恶意广告活动、勒索企业支付赎金以恢复访问，或利用企业信誉实施更大范围的诈骗。**

因此，普通用户，尤其是求职者，应对未经申请的职位邀请保持高度警惕，仔细核对网站地址，并在所有设备上部署可靠的安全防护方案，以最大限度降低风险。

本文翻译自hackread [原文链接](https://hackread.com/netflix-job-phishing-scam-steals-facebook-login-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311234](/post/id/311234)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/netflix-job-phishing-scam-steals-facebook-login-data/)

如若转载,请注明出处： <https://hackread.com/netflix-job-phishing-scam-steals-facebook-login-data/>

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