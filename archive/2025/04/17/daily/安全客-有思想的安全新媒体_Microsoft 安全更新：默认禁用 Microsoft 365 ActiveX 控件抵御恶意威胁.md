---
title: Microsoft 安全更新：默认禁用 Microsoft 365 ActiveX 控件抵御恶意威胁
url: https://www.anquanke.com/post/id/306592
source: 安全客-有思想的安全新媒体
date: 2025-04-17
fetch_date: 2025-10-06T22:02:47.457390
---

# Microsoft 安全更新：默认禁用 Microsoft 365 ActiveX 控件抵御恶意威胁

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

# Microsoft 安全更新：默认禁用 Microsoft 365 ActiveX 控件抵御恶意威胁

阅读量**59241**

发布时间 : 2025-04-16 11:14:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/microsoft-disables-activex-by-default/>

译文仅供参考，具体内容表达以及含义原文为准。

Microsoft 采取了关键举措，通过在 Microsoft 365 应用程序中默认禁用 ActiveX 控件来增强其生产力套件的安全性。

这项重要的安全更新本月初开始逐步推出，旨在降低长期以来困扰这一旧有技术的恶意软件风险以及未经授权的代码执行风险。

从 2025 年 4 月起，Windows 版本的 Microsoft Word、Excel、PowerPoint 和 Visio 将在无通知的情况下自动阻止 ActiveX 控件。

这一变化是继 2024 年 10 月发布的独立版 Office 2024 软件包中实施的类似安全措施之后的又一举措。

****安全变更影响主要的 Office 应用程序****

Office 安全团队的产品经理 Zaeem Patel 表示：“之前的默认设置‘在启用所有限制最少的控件之前提示我’，使得用户能够启用潜在危险的 ActiveX 控件，而攻击者可以通过社会工程手段或恶意文件来利用这些控件。”

“新的默认设置更加安全，因为它完全阻止了这些控件，降低了恶意软件或未经授权的代码执行的风险。”

从技术层面来看，这相当于默认启用现有的 “DisableAllActiveX” 组策略设置。

当用户打开一个包含 ActiveX 控件的文档时，他们现在会看到一个通知横幅，上面写着 “已阻止的内容：此文件中的 ActiveX 内容已被阻止”，并提供了一个了解更多信息的选项。

对于需要 ActiveX 功能的组织，系统管理员可以通过组策略来修改这一行为，或者，也可以使用 Microsoft 365 的云策略服务来部署云策略。

****存在安全漏洞的旧有技术****

ActiveX 于 1996 年推出，近三十年来一直是 Microsoft Office 框架的一部分。它允许开发人员在文档中创建交互式元素。然而，由于它能够深度访问系统资源，这使其成为了网络犯罪分子的主要攻击目标。

安全专家们长期以来一直主张进行这一变革。ThreatDown 的一项安全分析指出：“让其订阅客户稍作等待以获得更好的安全性，这体现了 Microsoft 在逐步去除其旗舰软件中不安全功能时所采取的谨慎、分阶段的策略。”

当 ActiveX 被禁用时，用户将无法再在 Microsoft 365 文件中创建或与 ActiveX 对象进行交互。

一些现有的 ActiveX 对象仍会显示为静态图像，但不具备交互功能。

Microsoft 建议，当遇到提示更改 ActiveX 设置的文件时要保持谨慎：

1.避免打开意外的文件附件，即使附件看似来自可信来源。

2.如果你不认识的人鼓励你更改 ActiveX 设置，要保持警惕。

3.对敦促调整 ActiveX 设置的弹出消息持怀疑态度。

仍然需要 ActiveX 功能的个人用户可以通过以下步骤重新启用它：

1.选择 “文件”>“选项”>“信任中心”。

2.点击 “信任中心设置”。

3.进入 “ActiveX 设置”。

4.选择 “在启用所有限制最少的控件之前提示我”。

5.点击 “确定”。

也可以将注册表项 HKEY\_CURRENT\_USER\Software\Microsoft\Office\Common\Security\DisableAllActiveX 设置为 0（REG\_DWORD），以恢复之前的行为。

此更新目前已面向 Beta 通道的用户提供，并正在逐步推送给运行版本 2504（内部版本 18730.20030）或更高版本的当前通道（预览版）用户。

这一变化体现了 Microsoft 在其生产力套件中持续致力于平衡向后兼容性与现代安全要求的承诺。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/microsoft-disables-activex-by-default/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306592](/post/id/306592)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/microsoft-disables-activex-by-default/)

如若转载,请注明出处： <https://cybersecuritynews.com/microsoft-disables-activex-by-default/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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