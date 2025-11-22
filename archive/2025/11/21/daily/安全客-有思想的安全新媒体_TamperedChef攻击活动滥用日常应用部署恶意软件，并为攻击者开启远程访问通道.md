---
title: TamperedChef攻击活动滥用日常应用部署恶意软件，并为攻击者开启远程访问通道
url: https://www.anquanke.com/post/id/313323
source: 安全客-有思想的安全新媒体
date: 2025-11-21
fetch_date: 2025-11-22T03:06:33.161733
---

# TamperedChef攻击活动滥用日常应用部署恶意软件，并为攻击者开启远程访问通道

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

# TamperedChef攻击活动滥用日常应用部署恶意软件，并为攻击者开启远程访问通道

阅读量**23304**

发布时间 : 2025-11-21 17:55:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mayura Kathir，文章来源：gbhackers

原文地址：<https://gbhackers.com/tamperedchef-campaign/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Acronis 威胁研究部门发现了一场名为 **TamperedChef** 的复杂全球性恶意广告活动，该活动通过伪装成日常合法应用来攻陷全球系统。

此行动利用社会工程学、搜索引擎优化策略和 **欺诈获取的数字证书**，诱骗用户安装后门程序，使攻击者获得对受感染机器的远程访问和控制权。

TamperedChef 代表了恶意软件分发的新演进，它交付 **功能完整的伪造应用**，模仿浏览器、PDF 编辑器、电子书阅读器和游戏等热门软件。

![]()

这些恶意安装程序携带来自 **美国注册空壳公司的有效代码签名证书**，使其看似可信并帮助逃避安全检测。

该活动主要影响美洲地区的组织，约 80% 的受害者位于美国，但其基础设施遍布全球多个大陆和行业。

### 工业化规模基础设施

TamperedChef 的幕后威胁行为者以企业级 sophistication 运作，维持着由在特拉华州和怀俄明州等注册的 **一次性空壳公司** 组成的网络。

![]()

这些实体（如 Performance Peak Media LLC、Fusion Core Reach LLC 和 Unified Market Group LLC）充当幌子，从合法机构获取 **扩展验证（EV）证书**。

一旦某个证书被标记或吊销，操作者会迅速以类似通用名称注册新公司并获取新凭证，以维持其运作的合法性。

就受影响行业而言，遥测数据显示受害者遍布多个行业，但 **医疗保健、建筑和制造业** 明显集中。

![]()

所有下载域名均遵循一致模式，使用“download”作为子域名，例如 download.allmanualsreader.com 或 download.anyproductmanual.com ，通过 NameCheap 注册并使用冰岛的隐私保护服务。

域名注册期限仅为一年，使攻击者能在基础设施被取缔后快速重建。

命令与控制（C2）服务器最初使用随机域名生成字符串，但最近已转向更易识别的名称（如 get.latest-manuals.com ），以混入常规网络流量。

### 攻击链与技术细节

Acronis 遥测数据显示，医疗保健、建筑和制造业面临该活动的风险尤其高。

这些行业的工作人员经常需要在线搜索 **高度专业化设备的产品手册**——而这正是 TamperedChef 通过恶意广告和优化搜索结果所利用的行为。

难以找到母语手册可能解释了为何美洲英语地区的受害者浓度更高。

攻击链始于用户遇到恶意广告或被操纵的搜索结果，引导至伪造下载站点。

安装后，应用看似完全合法，显示许可协议和感谢消息，强化真实性假象。

在幕后，安装程序会投放 XML 配置文件以创建计划任务，建立每 24 小时执行一次的持久化机制，并带有随机延迟以逃避检测。

JavaScript payload 本身使用开源混淆工具进行 **深度混淆**，使分析极为困难。

激活后，后门支持远程代码执行、通过机器 ID 生成进行系统指纹识别，并使用 XOR 加密和 base64 编码通过 HTTPS 连接与 C2 服务器进行加密通信。

### 多威胁场景

![]()

安全研究人员认为 TamperedChef 可能同时服务于多种目的：

1. 作为 **初始访问中介**，向其他犯罪集团出售已攻陷系统的访问权限以牟利。
2. 鉴于医疗保健受害者集中，攻击者可能针对敏感患者数据和凭证，在暗网市场 monetization。
3. 持久化后门访问为未来勒索软件部署提供理想条件，而对政府或研究机构的 opportunistic 访问可能促成间谍活动。

时间线分析显示，操作者在不断调整策略：
早期活动使用三年期证书和域名生成算法模式的 C2 服务器，但在多次吊销后，到 2025 年年中已转向 **短期证书和人类可读域名**，显示其致力于逃避安全措施并维持运营连续性。

本文翻译自gbhackers [原文链接](https://gbhackers.com/tamperedchef-campaign/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313323](/post/id/313323)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/tamperedchef-campaign/)

如若转载,请注明出处： <https://gbhackers.com/tamperedchef-campaign/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **716**

* 粉丝
* **6**

### TA的文章

* ##### [N-able N-central 中存在严重漏洞，允许攻击者未授权交互遗留API并读取敏感文件](/post/id/313330)

  2025-11-21 17:56:21
* ##### [TamperedChef攻击活动滥用日常应用部署恶意软件，并为攻击者开启远程访问通道](/post/id/313323)

  2025-11-21 17:55:57
* ##### [新型macOS窃密木马DigitStealer伪装成DynamicLake，专门针对苹果M2/M3芯片设备](/post/id/313320)

  2025-11-21 17:55:18
* ##### [欧盟提出GDPR全面修订案，拟重新界定个人数据范畴与用户同意规则](/post/id/313317)

  2025-11-21 17:54:53
* ##### [Windows图形组件存在关键漏洞，可致攻击者通过单张图片夺取系统控制权](/post/id/313312)

  2025-11-21 17:54:23

### 相关文章

* ##### [N-able N-central 中存在严重漏洞，允许攻击者未授权交互遗留API并读取敏感文件](/post/id/313330)

  2025-11-21 17:56:21
* ##### [新型macOS窃密木马DigitStealer伪装成DynamicLake，专门针对苹果M2/M3芯片设备](/post/id/313320)

  2025-11-21 17:55:18
* ##### [欧盟提出GDPR全面修订案，拟重新界定个人数据范畴与用户同意规则](/post/id/313317)

  2025-11-21 17:54:53
* ##### [Windows图形组件存在关键漏洞，可致攻击者通过单张图片夺取系统控制权](/post/id/313312)

  2025-11-21 17:54:23
* ##### [“Tsundere”僵尸网络利用游戏诱饵及基于以太坊的命令与控制服务器在Windows平台进行扩张](/post/id/313308)

  2025-11-21 17:53:47
* ##### [WSUS中存在关键远程代码执行漏洞（CVE-2025-59287），正被积极利用以部署ShadowPad后门](/post/id/313305)

  2025-11-21 17:52:53
* ##### [新型Sturnus木马可突破WhatsApp/Signal加密防护并完全控制Android设备](/post/id/313302)

  2025-11-21 17:51:00

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