---
title: 黑客发起全球间谍行动，政府邮箱被利用XSS漏洞入侵
url: https://www.anquanke.com/post/id/307477
source: 安全客-有思想的安全新媒体
date: 2025-05-17
fetch_date: 2025-10-06T22:26:19.828060
---

# 黑客发起全球间谍行动，政府邮箱被利用XSS漏洞入侵

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

# 黑客发起全球间谍行动，政府邮箱被利用XSS漏洞入侵

阅读量**174638**

发布时间 : 2025-05-16 18:05:26

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

近日，安全研究人员披露，一个名为**“RoundPress”**的全球网络间谍活动正在持续展开，攻击者通过 Webmail 服务中的数个XSS漏洞，对全球多国政府和关键机构发起邮件窃密攻击。该行动被认为与黑客组织 APT28（又称“Fancy Bear”或“Sednit”）有关。

**一、行动时间跨度长，涉及目标广泛**

这项网络间谍活动始于 2023 年，并在 2024 年持续扩展攻击范围。被攻击的 Webmail 系统包括 Roundcube、Horde、MDaemon 及 Zimbra。

根据披露，遭到攻击的目标涵盖：

1. 希腊、乌克兰、塞尔维亚、喀麦隆等**国家政府部门**；
2. 乌克兰和厄瓜多尔的**军方单位**；
3. 乌克兰、保加利亚、罗马尼亚的**国防企业**；
4. 乌克兰和保加利亚的**关键基础设施单位**。

![]()

攻击目标分布（来源：ESET）

**二、打开邮件即中招，攻击过程零交互**

攻击从一封带有当前新闻或政治内容的钓鱼邮件开始，攻击者常引用**真实新闻片段**提升可信度。

邮件正文中嵌入恶意 JavaScript 脚本，借助 Webmail 前端页面的 XSS 漏洞实现执行。受害者**仅需打开邮件即可触发攻击，无需点击链接、输入信息或其他操作**。

![]()

攻击链概述（来源：ESET）

攻击脚本不具备持久化能力，但足以在一次执行中完成以下行为：

1. 创建隐藏输入字段，引导浏览器或密码管理器**自动填充邮箱凭据**；![]()凭据窃取函数（来源：ESET）
2. 读取页面 DOM 或发送 HTTP 请求，获取邮件内容、联系人、Webmail 配置、登录记录、2FA 设置及密码等信息；
3. 将采集数据通过 HTTP POST 请求发送至攻击者控制的远程服务器。

根据目标 Webmail 产品的不同，攻击脚本具备略有差异的功能模块，表现出**高度定制化**。

**三**、**涉及多个严重 XSS 漏洞**

“RoundPress” 行动利用了多个 Webmail 产品中的 XSS 漏洞，进行恶意 JavaScript 注入。具体漏洞包括：

**1.Roundcube – CVE-2020-35730**

2023 年被用于攻击的存储型 XSS 漏洞，攻击者将脚本嵌入邮件正文，用户在浏览器中**打开即被执行**，导致凭据和数据泄露。

**2.Roundcube – CVE-2023-43770**

2024 年初被利用的漏洞，Roundcube 在处理超链接文字时存在过滤不当问题，攻击者可插入 **<script>**标签实施攻击。

**3.MDaemon – CVE-2024-11182**

2024 年底被用作零日攻击的 HTML 解析器漏洞，攻击者构造畸形 title 属性及 noembed 标签，通过隐藏的**<img onerror>**实现 JavaScript 执行，获取凭据并**绕过双因素认证**。

**4.Horde –** **未确认 XSS 漏洞**

黑客曾尝试在 **<img onerror>** 中注入脚本攻击 Horde，但疑因新版系统具备过滤机制未能成功，具体漏洞未被证实，疑似已被修复。

**5.Zimbra – CVE-2024-27443**

该漏洞出现在 Zimbra 的日历邀请处理功能，攻击者利用 X-Zimbra-Calendar-Intended-For 头部未过滤输入，实现 JavaScript 注入，在用户查看日历邀请时执行。

虽然尚未发现 2025 年有明确的 RoundPress 攻击活动迹象，但研究人员指出，鉴于主流 Webmail 产品中仍持续曝出 XSS 漏洞，黑客组织所使用的攻击技术具备**高度可复用性**，仍对全球政府机构及关键行业构成潜在威胁。

消息来源：

https://www.bleepingcomputer.com/news/security/government-webmail-hacked-via-xss-bugs-in-global-spy-campaign/

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307477](/post/id/307477)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

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