---
title: 软件供应链投毒警报：9个NuGet包内嵌定时触发破坏逻辑，将在硬编码日期导致应用彻底损毁
url: https://www.anquanke.com/post/id/313097
source: 安全客-有思想的安全新媒体
date: 2025-11-10
fetch_date: 2025-11-11T03:12:23.800638
---

# 软件供应链投毒警报：9个NuGet包内嵌定时触发破坏逻辑，将在硬编码日期导致应用彻底损毁

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

# 软件供应链投毒警报：9个NuGet包内嵌定时触发破坏逻辑，将在硬编码日期导致应用彻底损毁

阅读量**23805**

发布时间 : 2025-11-10 17:25:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/nuget-sabotage-time-delayed-logic-in-9-packages-risks-total-app-destruction-on-hardcoded-dates/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

NuGet 包注册表中发现了一起复杂的供应链攻击，攻击者以 **shanhai666** 为别名发布了九个恶意包，旨在针对数据库应用程序和工业控制系统执行**破坏性、延时触发的有效载荷**。Socket 威胁研究团队识别了这些包，它们于 2023 年至 2024 年间发布，累计下载量达 9,488 次。

该攻击活动中的每个恶意包几乎都提供了其宣传的全部功能，将**正常代码与隐藏的破坏代码混合**。Socket 的分析显示，99% 的代码库是合法的，实现了存储库（Repository）、工作单元（Unit of Work）和 ORM 反射映射等知名企业级设计模式。

“这些合法功能有多重目的：通过包的实际效果建立信任；在代码审查中让审核者看到熟悉的模式和真实实现；提供实际价值以鼓励采用；将约 20 行的恶意有效载荷隐藏在数千行合法代码中；并延迟被发现的时间。”

其结果是，这些包看似专业、功能正常且可靠——直到它们突然自我销毁或悄悄破坏数据完整性。

该攻击活动的技术核心是**扩展方法注入模式**，攻击者利用 C# 扩展方法将恶意逻辑注入现有 API。

“恶意软件利用 C# 扩展方法，将恶意逻辑透明地注入到每一次数据库和 PLC 操作中，”Socket 解释道。“扩展方法允许开发者在不修改原始代码的情况下为现有类型添加新方法——这一强大的 C# 特性被威胁行为者武器化以实现拦截。”

所有恶意包中都添加了两个方法：用于数据库操作的 **.Exec()** 和用于 PLC 通信的 **.BeginTran()**。这些方法看似无害，但包含条件触发器，可根据特定日期和概率终止应用程序或损坏数据。

Socket 研究人员发现，大多数恶意包包含硬编码的触发日期——例如 **2027 年 8 月 8 日**和 **2028 年 11 月 29 日**——之后它们开始随机终止宿主进程。

“每次应用程序执行数据库查询或 PLC 操作时，这些扩展方法会自动执行……触发日期过后，恶意软件生成一个 1 到 100 之间的随机数。如果数字超过 80（即 20% 的概率），恶意软件会调用 **Process.GetCurrentProcess().Kill()**，立即终止整个应用程序。”

尽管 20% 的触发率看似较低，但 Socket 指出，每分钟执行数百次数据库调用的应用程序一旦满足日期条件，几乎会立即崩溃。对于高吞吐量系统，这意味着几秒钟内服务完全中断。

“每小时执行数百次查询的生产应用程序将在几秒钟内崩溃，”报告警告称。

“电子商务（100 次查询/分钟）：约 3 秒 → 结账中断
医疗保健（50 次查询/分钟）：约 6 秒 → 关键系统 outage
金融（500 次查询/分钟）：<1 秒 → 平台完全故障
制造业（10 次操作/分钟，Sharp7Extend）：约 30 秒 → 生产崩溃 + 80% 静默写入失败，危及安全系统”

最复杂的包 **Sharp7Extend** 专门针对工业自动化系统，模仿西门子 S7 可编程逻辑控制器（PLC）的合法 .NET 库。

“**Sharp7Extend** 包专门针对合法 Sharp7 库的用户……通过在受信任的 Sharp7 名称后附加‘Extend’，威胁行为者利用了搜索 Sharp7 扩展或增强功能的开发者。”

为隐藏恶意意图，**Sharp7Extend** 将真实的 Sharp7 库（版本 1.1.79）与其恶意代码捆绑在一起。这确保所有标准 PLC 通信在测试期间完全正常工作，而隐藏的扩展则悄悄准备发起攻击。

Socket 在 **Sharp7Extend** 中识别出两种破坏机制：

1. **随机进程终止**：在 2028 年 6 月 6 日之前，每次 PLC 连接时有 20% 的概率终止进程。
2. **静默数据损坏**：经过 30–90 分钟的宽限期后，该包开始导致 80% 的写入操作静默失败。

这种两阶段破坏使调试极其困难。初期崩溃看似随机，后续数据损坏则表现为“硬件故障”，使恶意软件能在生产环境中长期潜伏而不被发现。

为提高采用率，**shanhai666** 攻击者还在九个恶意包之外发布了三个合法包，以在 NuGet 上建立可信贡献者的历史记录。

“开发者研究作者时，会发现真实可用的包与恶意包并存，从而降低怀疑，”Socket 指出。“恶意包战略性地针对 .NET 应用中使用的三大数据库提供商——SQL Server、PostgreSQL、SQLite——以及工业控制系统。”

攻击者甚至伪造了 .nuspec 文件的作者字段，在不同包中显示不同名称，以此规避基于声誉的安全扫描。

Socket 已向 NuGet 报告了所有恶意包，NuGet 确认正在调查并着手移除。然而，截至 Socket 发布报告时，这些包仍在注册表中处于活跃状态。

本文翻译自securityonline [原文链接](https://securityonline.info/nuget-sabotage-time-delayed-logic-in-9-packages-risks-total-app-destruction-on-hardcoded-dates/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313097](/post/id/313097)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/nuget-sabotage-time-delayed-logic-in-9-packages-risks-total-app-destruction-on-hardcoded-dates/)

如若转载,请注明出处： <https://securityonline.info/nuget-sabotage-time-delayed-logic-in-9-packages-risks-total-app-destruction-on-hardcoded-dates/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **673**

* 粉丝
* **6**

### TA的文章

* ##### [iPhone未来图景：卫星通信将支持地图导航、照片传输及“自然交互”功能](/post/id/313091)

  2025-11-10 17:27:30
* ##### [三星设备零点击漏洞（CVE-2025-21042）可通过恶意DNG图像传播LANDFALL间谍软件](/post/id/313094)

  2025-11-10 17:27:09
* ##### [软件供应链投毒警报：9个NuGet包内嵌定时触发破坏逻辑，将在硬编码日期导致应用彻底损毁](/post/id/313097)

  2025-11-10 17:25:49
* ##### [GlassWorm蠕虫重现：利用隐形Unicode字符重复感染VS Code扩展，并扩散至GitHub平台](/post/id/313100)

  2025-11-10 17:24:27
* ##### [智能体编排框架LangGraph中存在远程代码执行漏洞（CVE-2025-64439），系统面临安全风险](/post/id/313104)

  2025-11-10 17:22:22

### 相关文章

* ##### [iPhone未来图景：卫星通信将支持地图导航、照片传输及“自然交互”功能](/post/id/313091)

  2025-11-10 17:27:30
* ##### [三星设备零点击漏洞（CVE-2025-21042）可通过恶意DNG图像传播LANDFALL间谍软件](/post/id/313094)

  2025-11-10 17:27:09
* ##### [GlassWorm蠕虫重现：利用隐形Unicode字符重复感染VS Code扩展，并扩散至GitHub平台](/post/id/313100)

  2025-11-10 17:24:27
* ##### [智能体编排框架LangGraph中存在远程代码执行漏洞（CVE-2025-64439），系统面临安全风险](/post/id/313104)

  2025-11-10 17:22:22
* ##### [信息窃取木马Vidar首次攻击npm生态系统：通过17个仿冒软件包及安装后脚本传播](/post/id/313107)

  2025-11-10 17:21:20
* ##### [Snapchat斥资4亿美元达成协议，为其My AI功能引入Perplexity先进搜索技术](/post/id/313113)

  2025-11-10 17:19:53
* ##### [新型工具“Whisper Leak”可窃取加密流量中用户向主流AI智能体发送的提示词](/post/id/313116)

  2025-11-10 17:19:17

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