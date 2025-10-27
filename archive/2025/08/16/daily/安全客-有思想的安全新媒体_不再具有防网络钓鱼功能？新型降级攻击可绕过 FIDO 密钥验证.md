---
title: 不再具有防网络钓鱼功能？新型降级攻击可绕过 FIDO 密钥验证
url: https://www.anquanke.com/post/id/311256
source: 安全客-有思想的安全新媒体
date: 2025-08-16
fetch_date: 2025-10-07T00:13:16.883153
---

# 不再具有防网络钓鱼功能？新型降级攻击可绕过 FIDO 密钥验证

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

# 不再具有防网络钓鱼功能？新型降级攻击可绕过 FIDO 密钥验证

阅读量**63697**

发布时间 : 2025-08-15 17:20:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

译文仅供参考，具体内容表达以及含义原文为准。

![]()

基于 FIDO 的密钥长期以来被视为防止钓鱼攻击和账户接管（ATO）的最强防线之一。但 Proofpoint 最新研究显示，即便是这些“抗钓鱼”机制也并非完全万无一失。公司在近期发布的分析中揭示，**攻击者可能利用降级攻击绕过 FIDO 保护**，从而为中间人（AiTM）攻击打开通道。

Proofpoint 表示：“基于 FIDO 的密钥仍然是防范常见凭证钓鱼和账户接管（ATO）威胁的强烈推荐认证方式。”然而，他们同时警告称：“FIDO 认证可能通过降级攻击被规避。”

该攻击依赖于经过修改的“**phishlet**”——一种被高级钓鱼工具（如 Evilginx）使用的配置文件，可模拟合法登录门户并捕获凭证或令牌。标准 phishlet 在 FIDO 保护的账户上通常会失败，触发错误并中止攻击。但 Proofpoint 的研究人员开发了专门的变体，使其能够强制回退至较弱的认证方式。

![]()

Proofpoint 描述的降级钓鱼攻击链如下：

1. **钓鱼诱饵**——攻击者通过电子邮件、短信或 OAuth 授权请求发送恶意链接。
2. **强制降级**——受害者看到错误提示，被迫选择其他登录方式。
3. **凭证与令牌窃取**——在使用替代 MFA 登录后，攻击者能够截取并查看登录凭证和会话 Cookie，就如同标准的 AiTM 钓鱼攻击一样。
4. **会话劫持**——被窃取的会话 Cookie 被导入攻击者的浏览器，从而无需额外身份验证即可完全访问账户。

Proofpoint 指出，一旦进入系统，攻击者可能进一步进行“数据外泄和受影响环境内的横向移动”。

目前，没有证据表明 FIDO 降级攻击已在实际环境中被利用。Proofpoint 认为，这是因为许多攻击者更倾向于低成本、高成功率的攻击方式，针对使用较弱 MFA 或未启用 MFA 的账户。此外，“创建或改造 phishlet 以实现 FIDO 降级攻击，需要更深的技术理解和专业知识”，这也阻碍了技术水平较低的攻击者。

尽管如此，Proofpoint 警告称，随着 FIDO 的普及，具备高级持续威胁（APT）能力和高技术水平的网络犯罪分子可能会采用这一技术。

随着 AiTM 钓鱼工具包和“钓鱼即服务”（PhaaS）平台的发展，Proofpoint 预计降级攻击功能可能会被整合进未来的攻击工具包中。

本文翻译自securityonline 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311256](/post/id/311256)

安全KER - 有思想的安全新媒体

本文转载自: securityonline

如若转载,请注明出处：

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