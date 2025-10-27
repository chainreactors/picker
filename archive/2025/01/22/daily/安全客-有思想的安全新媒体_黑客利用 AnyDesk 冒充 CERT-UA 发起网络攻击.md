---
title: 黑客利用 AnyDesk 冒充 CERT-UA 发起网络攻击
url: https://www.anquanke.com/post/id/303670
source: 安全客-有思想的安全新媒体
date: 2025-01-22
fetch_date: 2025-10-06T20:04:46.071528
---

# 黑客利用 AnyDesk 冒充 CERT-UA 发起网络攻击

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

# 黑客利用 AnyDesk 冒充 CERT-UA 发起网络攻击

阅读量**111187**

发布时间 : 2025-01-21 10:24:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Veronika Telychko，文章来源：socprime

原文地址：<https://socprime.com/blog/anydesk-exploitation-attack-detection/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

黑客经常利用合法工具进行恶意攻击。广受欢迎的 AnyDesk 远程工具也在很大程度上被黑客用于攻击目的。网络防御者揭露了最近滥用 AnyDesk 软件连接目标计算机的情况，并将这些恶意行为伪装成 CERT-UA 的活动。

**根据 CERT-UA 的研究检测利用 AnyDesk 的网络攻击**

攻击者经常利用远程管理工具进行恶意攻击。例如，在针对乌克兰的攻击活动中，远程实用工具软件被广泛使用。最新的 CERT-UA 警报揭示了另一种合法远程访问工具 AnyDesk 被滥用的情况，它以进行安全审计为名，诱使受害者利用被入侵的工具。用于集体网络防御的 SOC Prime Platform 收集了一套相关的检测算法，可帮助安全工程师确定 AnyDesk 使用了哪些主机，从而最大限度地降低入侵风险。由于对手知道 AnyDesk ID 并试图冒充 CERT-UA 连接到主机，因此 SOC Prime 提供了相关的 SOC 内容，以检测这些具有 ID 的实例，它们可能是目标。

单击 “探索检测 ”按钮，访问与 MITRE ATT&CK® 框架一致的专用检测内容项，并通过相关威胁情报和可操作元数据（如攻击时间表、误报率和审计配置建议）进行增强。所有检测还与业界领先的 SIEM、EDR 和数据湖技术兼容，以实现无缝跨平台威胁检测。

**AnyDesk 滥用： 网络攻击分析**

CERT-UA 的研究人员收到了有关多个攻击者试图使用 AnyDesk 应用程序远程连接目标实例的信息，据称这些攻击者是代表 CERT-UA 进行攻击的。

根据研究，攻击者通过 AnyDesk 发送连接请求，伪装成安全审计以验证保护级别，谎称代表 CERT-UA，利用 CERT-UA 徽标和 AnyDesk ID “1518341498”（在不同事件中可能会有所不同）。

值得注意的是，在某些情况下，CERT-UA 团队可能会使用包括 AnyDesk 在内的远程访问工具来帮助组织保护其网络安全资产。这包括提供预防、检测和减轻网络事件后果的活动。但是，只有在通过预先建立的通信渠道达成事先协议后，才能执行这些操作。

在最新的恶意活动中，攻击者采用了利用信任和权威的社交工程技术。如果对手可以访问受害者的 AnyDesk ID，并且受影响的计算机上安装了功能正常的 AnyDesk 软件，那么这些利用 AnyDesk 的网络攻击就会成功。此外，这可能表明目标 AnyDesk ID 很可能是在其他情况下泄露的，包括利用对手先前授权远程访问的其他系统。

为降低 AnyDesk 被利用的风险，CERT-UA 提示用户保持警惕，确保仅在活动会话期间启用远程访问工具，并确保任何涉及远程访问的操作都是通过既定通信渠道亲自商定的。此外，还强烈建议企业采用主动防御策略，及时发现任何可疑行为的蛛丝马迹。如果组织依赖 AnyDesk，则应主动检测该远程实用程序使用的主机，以最大限度地降低未经授权的远程访问风险。用于集体网络防御的 SOC Prime Platform 为安全团队提供了面向未来的网络防御的完整产品套件，提供高级威胁检测、自动威胁捕猎和智能驱动的检测工程，帮助企业始终领先对手一步。

**MITRE ATT&CK 背景**

要深入了解据称以 CERT-UA 名义实施的最新攻击，请查看一组 Sigma 规则，这些规则可帮助识别利用 AnyDesk 的主机。依靠 MITRE ATT&CK 还可以提高与涉及 AnyDesk 冒充 CERT-UA 的恶意活动相关的行为模式的可见性。

![]()

本文翻译自socprime [原文链接](https://socprime.com/blog/anydesk-exploitation-attack-detection/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303670](/post/id/303670)

安全KER - 有思想的安全新媒体

本文转载自: [socprime](https://socprime.com/blog/anydesk-exploitation-attack-detection/)

如若转载,请注明出处： <https://socprime.com/blog/anydesk-exploitation-attack-detection/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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