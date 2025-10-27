---
title: Tycoon钓鱼工具包采用新技术隐藏恶意链接
url: https://www.anquanke.com/post/id/311909
source: 安全客-有思想的安全新媒体
date: 2025-09-06
fetch_date: 2025-10-02T19:43:01.691792
---

# Tycoon钓鱼工具包采用新技术隐藏恶意链接

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

# Tycoon钓鱼工具包采用新技术隐藏恶意链接

阅读量**422724**

发布时间 : 2025-09-05 18:25:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/tycoon-phishing-kit-employs-new-technique/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络犯罪分子正部署日益复杂的手段绕过安全系统，而最新威胁来自高级的 **Tycoon 钓鱼即服务工具包**。

这一恶意平台引入了旨在隐藏危险链接的新型技术，使其对传统检测系统几乎不可见，同时仍能对毫无防备的受害者发挥作用。

**Tycoon 钓鱼工具包**代表了基于电子邮件攻击的重大进化，它利用精心设计的语音邮件消息和伪造的会计服务通知来诱骗目标。

![]()

与依赖明显恶意指标的传统钓鱼活动不同，**Tycoon** 采用先进的 **URL 编码**和**结构操纵技术**，从根本上改变了链接在安全工具和人类接收者眼中的显示方式。

**Barracuda** 分析师在最近对凭证窃取活动的调查中发现了这些复杂规避策略的出现。

研究人员发现，攻击者现在正结合多种混淆方法，制造挑战现有安全范式的混合威胁。

**Tycoon** 攻击手段中最令人担忧的方面包括其使用的 **URL 编码技术**——通过在网址中插入使用 **%20** 代码的不可见空格。

这种方法将恶意组件推到自动安全系统的扫描范围之外，同时为点击链接的受害者保留功能性链接。

该技术还融入了 **Unicode 符号**，这些符号在视觉上类似于标准标点符号，但其底层代码结构却完全不同。

### 高级链接操纵技术

**Tycoon** 工具包的核心创新在于其 **冗余协议前缀技术**，该技术可创建包含故意结构不一致的部分超链接 URL。

攻击者构造的地址具有重复的协议声明或缺失的必要组件，例如包含两个“https”前缀或省略标准的“//”分隔符。

这种操纵确保安全扫描器会遇到解析错误，而浏览器仍能正确解释功能部分。

考虑以下示例实现：

```
hxxps:office365Scaffidips[.]azgcvhzauig[.]es\If04
```

在此结构中，“@”符号前的所有内容对接收者而言看似合法，包含“office365”等受信任品牌引用。

然而，实际目标位于“@”符号之后，将受害者定向至攻击者控制的基础设施。该技术利用浏览器解释协议，将“@”符号前的内容视为用户身份验证信息而非主要目标地址。

![]()

**子域滥用组件** 通过创建看似合法的微软关联地址进一步增强欺骗性。

尽管“office365Scaffidips”暗示官方微软基础设施，但真实目标“azgcvhzauig.es ”是一个完全独立的恶意域名，用于凭据窃取。

这些不断演变的技术表明，现代钓鱼活动正适应安全防护的改进，要求组织实施包含人工智能和机器学习能力的多层防御策略，以有效识别这些复杂威胁。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/tycoon-phishing-kit-employs-new-technique/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311909](/post/id/311909)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/tycoon-phishing-kit-employs-new-technique/)

如若转载,请注明出处： <https://cybersecuritynews.com/tycoon-phishing-kit-employs-new-technique/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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