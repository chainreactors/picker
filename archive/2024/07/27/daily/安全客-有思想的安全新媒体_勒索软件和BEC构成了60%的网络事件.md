---
title: 勒索软件和BEC构成了60%的网络事件
url: https://www.anquanke.com/post/id/298468
source: 安全客-有思想的安全新媒体
date: 2024-07-27
fetch_date: 2025-10-06T17:41:22.301955
---

# 勒索软件和BEC构成了60%的网络事件

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

# 勒索软件和BEC构成了60%的网络事件

阅读量**88732**

发布时间 : 2024-07-26 11:24:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 James Coker，文章来源：infosecurity magazine

原文地址：<https://www.infosecurity-magazine.com/news/ransomware-bec-cyber-incidents/>

译文仅供参考，具体内容表达以及含义原文为准。

根据思科 Talos 的一份报告，勒索软件和商业电子邮件泄露 （BEC） 攻击占 2024 年第二季度所有事件的 60%。

科技是这一时期最受攻击的行业，占事件的24%，比上一季度增加了30%。研究人员表示，攻击者可能会将技术公司视为进入其他行业和组织的门户，因为它们在为包括关键基础设施在内的一系列其他行业提供服务方面发挥着作用。

第二季度下一个最常针对的行业是零售、医疗保健、制药和教育。

最常见的初始访问方法是在有效帐户上使用泄露的凭据，占攻击的 60%。这比上一季度增长了 25%。

思科 Talos 在 2024 年第二季度观察到的最常的安全漏洞是易受攻击或配置错误的系统以及缺乏适当的 MFA 实施，均比上一季度增长了 46%。

## 勒索软件趋势

在此期间，勒索软件占思科 Talos 事件响应 （Talos IR） 团队参与度的 30%，与 2024 年第一季度相比增加了 22%。

该报告详细介绍了对一系列勒索软件组织进行的攻击的应对措施，其中许多组织部署了新颖的策略来攻击目标，包括使用有效工具来保持持久性并追求横向移动。其中包括：

* **地下团队：**在此事件中，威胁参与者利用安全外壳 （SSH） 在环境中横向移动，并战略性地重新激活了之前已禁用的某些 Active Directory 用户帐户。在交战过程中，攻击者向员工的个人电子邮件发送骚扰信息，以此胁迫受害者回应他们的要求。
* **BlackSuit****：**此威胁行为者通过不受 MFA 保护的 VPN 使用有效凭据获得访问权限。通过在环境中部署远程管理工具AnyDesk以及Cobalt Strike，建立了持久性。攻击者还利用 PsExec 和 Windows Management Instrumentation 命令行 （WMIC） 等离地二进制文件 （LoLBins） 在网络上横向移动。
* **Black Basta****：**在这种情况下，攻击者使用未受 MFA 保护的有效 RDP 帐户上的泄露凭据获得了初始访问权限。攻击者使用远程 PowerShell 执行在远程系统上启动 shell，并利用开源命令行工具 Rclone 来促进数据泄露。

立即阅读： 勒索软件组织优先考虑数据泄露的防御规避

思科 Talos 指出，在 2024 年第 2 季度 80% 的勒索软件事件中，缺乏在关键系统（如 VPN）上实施适当的 MFA，这使得初始访问更容易。

## BEC趋势

在 2024 年 4 月至 6 月期间，BEC 攻击也占思科 Talos 参与事件的 30%。这比 2024 年第一季度有所下降，当时它占攻击的 50%。

BEC 攻击涉及威胁行为者破坏合法的商业电子邮件帐户，并使用它们发送网络钓鱼电子邮件以获取敏感信息，例如帐户凭据，以及发送带有欺诈性财务请求的电子邮件。

研究人员观察了一系列用于破坏商业电子邮件帐户和发起BEC攻击的技术。其中包括：

* 短信钓鱼攻击，攻击者发送目标欺诈性短信，诱骗收件人共享个人信息或点击恶意链接以破坏他们的登录凭据
* 在一个案例中，一封网络钓鱼电子邮件被发送到员工的个人电子邮件地址，将他们重定向到一个虚假的登录页面。向用户发送了 MFA 推送通知并接受了该通知，从而授予攻击者访问权限
* 在另一组活动中，在访问用户的电子邮件帐户后，攻击者创建了 Microsoft Outlook 邮箱规则，将电子邮件发送到名为“已删除”的文件夹，然后使用受感染的帐户向内部和外部收件人发送一千多封网络钓鱼电子邮件。

本文翻译自infosecurity magazine [原文链接](https://www.infosecurity-magazine.com/news/ransomware-bec-cyber-incidents/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298468](/post/id/298468)

安全KER - 有思想的安全新媒体

本文转载自: [infosecurity magazine](https://www.infosecurity-magazine.com/news/ransomware-bec-cyber-incidents/)

如若转载,请注明出处： <https://www.infosecurity-magazine.com/news/ransomware-bec-cyber-incidents/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

### 热门推荐

文章目录

* [勒索软件趋势](#h2-0)
* [BEC趋势](#h2-1)

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