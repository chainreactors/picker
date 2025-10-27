---
title: WhatsApp漏洞与苹果零日漏洞遭组合利用，间谍软件攻击复杂度升级
url: https://www.anquanke.com/post/id/311781
source: 安全客-有思想的安全新媒体
date: 2025-09-03
fetch_date: 2025-10-02T19:32:36.069238
---

# WhatsApp漏洞与苹果零日漏洞遭组合利用，间谍软件攻击复杂度升级

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

# WhatsApp漏洞与苹果零日漏洞遭组合利用，间谍软件攻击复杂度升级

阅读量**56692**

发布时间 : 2025-09-02 15:46:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Alex Lekander，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/whatsapp-flaw-exploited-alongside-apple-zero-day-in-spyware-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

WhatsApp 已修复一个关键的零点击漏洞，该漏洞曾在针对苹果用户的高级攻击行动中被利用。

这一漏洞编号为 CVE-2025-55177，据称与苹果近期披露的零日漏洞（CVE-2025-43300）被联合使用，**用于在完全无需用户交互的情况下投递间谍软件。**

WhatsApp 在上周五晚间发布的安全公告中披露了该漏洞，称其由内部安全团队发现。受影响的版本包括：iOS 平台 2.25.21.73 之前的 WhatsApp、iOS 平台 2.25.21.78 之前的 WhatsApp Business，以及 Mac 平台 2.25.21.78 之前的 WhatsApp。问题源于其多设备同步机制中授权校验不完整，**攻击者可强迫目标设备从任意 URL 拉取并渲染内容**，从而在用户毫无操作的情况下远程控制设备处理恶意数据。

WhatsApp 隶属于 Meta，是全球最广泛使用的即时通讯应用之一，拥有超过 20 亿用户。其支持的“设备多开”功能正是这次安全漏洞的核心所在。

加拿大多伦多大学公民实验室（Citizen Lab）的安全研究员 Bill Marczak 在 X 平台上指出，该漏洞在攻击链中扮演了零点击投递通道的角色。完整攻击过程结合了 CVE-2025-43300——这是苹果 Image I/O 框架中的一个零日漏洞，苹果已于本月修复。**该漏洞可通过在图像文件中嵌入恶意代码来攻陷设备，而 WhatsApp 的漏洞正好为攻击者提供了一个可静默加载并显示恶意图像的完美入口。**

CVE-2025-43300 已在 2025 年 8 月 20 日发布的 iOS 18.6.2、iPadOS 18.6.2、macOS Sequoia 15.6.1 等版本中得到修复。漏洞成因是 Image I/O 在解析图像时存在越界写问题，几乎影响所有当前的苹果设备，包括 iPhone、iPad 和 Mac。通过在图像处理过程中破坏内存，攻击者可实现任意代码执行，而一旦与投递通道（如 CVE-2025-55177）结合，就能完全控制目标设备。

**国际特赦组织安全实验室也证实，安卓用户同样受到波及**。该组织安全部门负责人 Donncha Ó Cearbhaill 表示，其团队正在协助多名攻击受害者，其中不少来自公民社会群体，包括记者与人权维护者。

![]()

WhatsApp 已向部分遭到攻击的用户发出定向威胁通知，并建议他们寻求专业安全支持。

安全专家提醒，用户应立即将 WhatsApp 更新至 iOS 2.25.21.73 或更高版本、macOS 2.25.21.78 或更高版本，同时确保苹果设备已修复 CVE-2025-43300。此外，iOS 用户可启用“锁定模式”（Lockdown Mode），安卓用户可启用“高级防护模式”，以进一步增强设备在零点击与间谍软件攻击下的安全防御能力。

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/whatsapp-flaw-exploited-alongside-apple-zero-day-in-spyware-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311781](/post/id/311781)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/whatsapp-flaw-exploited-alongside-apple-zero-day-in-spyware-attacks/)

如若转载,请注明出处： <https://cyberinsider.com/whatsapp-flaw-exploited-alongside-apple-zero-day-in-spyware-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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