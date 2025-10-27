---
title: iCloud日历遭滥用：攻击者利用苹果服务器发送钓鱼邮件
url: https://www.anquanke.com/post/id/311972
source: 安全客-有思想的安全新媒体
date: 2025-09-09
fetch_date: 2025-10-02T19:49:34.675928
---

# iCloud日历遭滥用：攻击者利用苹果服务器发送钓鱼邮件

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

# iCloud日历遭滥用：攻击者利用苹果服务器发送钓鱼邮件

阅读量**1273158**

发布时间 : 2025-09-08 17:47:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/icloud-calendar-abused-to-send-phishing-emails-from-apples-servers/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

攻击者正滥用iCloud日历邀请功能，通过苹果官方邮件服务器发送伪装成支付通知的**回拨钓鱼邮件**，大幅提升绕过垃圾邮件过滤器并进入目标收件箱的概率。

本月初，一名读者向BleepingComputer分享了一封钓鱼邮件，谎称其**PayPal账户**被扣除599美元，并提供“客服电话”诱导联系。邮件内容显示：“您好，您的**PayPal账户**已被扣费599.00美元。我们确认收到您最近的付款……如需讨论或修改，请联系支持团队：+1 (786) 902-8579。”

![]()

此类邮件的核心目的是诱骗收件人相信账户被盗刷，进而拨打骗子的“客服”电话。一旦接通，诈骗者会谎称账户已被入侵，或要求远程连接电脑以“处理退款”，实则诱导下载恶意软件，最终窃取银行账户资金、部署 malware 或盗取数据。

### **漏洞根源：日历邀请功能被劫持**

这起钓鱼事件的异常之处在于，邮件发自**noreply@email.apple.com** ，且通过了SPF、DMARC和DKIM安全验证，证明其确实来自苹果服务器。

邮件头验证结果显示：

```
Authentication-Results: spf=pass (sender IP is 17.23.6.69)
 smtp.mailfrom=email.apple.com; dkim=pass (signature was verified)
 header.d=email.apple.com;dmarc=pass action=none header.from=email.apple.com;
```

**攻击流程**如下：

1. 攻击者在iCloud日历事件的“备注”字段中植入钓鱼文本。
2. 邀请一个受其控制的Microsoft 365邮箱（如Billing3@WilliamerDickinsonerLTD.onmicrosoft.com ）。
3. 苹果服务器自动发送日历邀请邮件，发件人为“noreply@email.apple.com ”。
4. 该Microsoft 365邮箱实为**邮件列表**，自动将邀请转发给所有群组成员（即钓鱼目标）。

为避免转发时SPF验证失败，Microsoft 365通过**发件人重写方案（SRS）** 将原始Return-Path（noreply@email.apple.com ）改写为微软关联地址（如bounces+SRS=8a6ka=3I@williamerdickinsonerltd.onmicrosoft.com ），确保邮件通过SPF检查。

### **风险与防范建议**

尽管钓鱼诱饵本身并无新意，但**滥用iCloud日历邀请、苹果服务器及官方域名**赋予了邮件极高的可信度，使其能绕过基于发件人信誉的过滤机制。

**用户需警惕**：

1. 意外收到的日历邀请，尤其是包含陌生链接或联系方式的内容。
2. 声称“账户异常”“紧急扣费”并要求立即回电的邮件，务必通过官方渠道核实。

BleepingComputer已就此事联系苹果，但尚未收到回应。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/icloud-calendar-abused-to-send-phishing-emails-from-apples-servers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311972](/post/id/311972)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/icloud-calendar-abused-to-send-phishing-emails-from-apples-servers/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/icloud-calendar-abused-to-send-phishing-emails-from-apples-servers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

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