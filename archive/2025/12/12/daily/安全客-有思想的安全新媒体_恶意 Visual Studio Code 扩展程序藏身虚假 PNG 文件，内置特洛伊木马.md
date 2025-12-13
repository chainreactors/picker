---
title: 恶意 Visual Studio Code 扩展程序藏身虚假 PNG 文件，内置特洛伊木马
url: https://www.anquanke.com/post/id/313712
source: 安全客-有思想的安全新媒体
date: 2025-12-12
fetch_date: 2025-12-13T03:14:01.020020
---

# 恶意 Visual Studio Code 扩展程序藏身虚假 PNG 文件，内置特洛伊木马

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

# 恶意 Visual Studio Code 扩展程序藏身虚假 PNG 文件，内置特洛伊木马

阅读量**13000**

发布时间 : 2025-12-12 18:04:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/malicious-vs-code-extensions-trojan-fake-png-files/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()
网络安全公司**ReversingLabs（RL）** 检测到一场针对 Visual Studio Code（VS Code）应用市场开发者的**精密且长期持续的攻击行动**。总计发现**19 款恶意扩展程序**暗藏特洛伊木马，该攻击行动自 2025 年 2 月起便处于活跃状态，直至 12 月 2 日才被发现。

需要说明的是，VS Code 是众多开发者的核心工具，因此其用于分发扩展程序（附加功能组件）的应用市场，自然成为网络犯罪分子的**首要攻击目标**。而就在此次发现的数周前，该应用市场中一款伪造的 “Prettier” 扩展程序，还被曝出会投放**Anivia 信息窃取器**。

### 依赖项篡改陷阱

据 RL 威胁研究员**佩塔尔・基尔马耶尔（Petar Kirhmajer）** 介绍，攻击者采用了一种经典的木马植入技术 —— 将恶意软件伪装成无害程序。在本次攻击中，恶意代码被藏匿于扩展程序的**依赖项文件夹**内，该文件夹存储的是扩展程序正常运行所需的预打包核心代码。

攻击者实施了一处巧妙的操作：他们并未直接添加新的恶意代码，而是篡改了一款**高知名度且受信任的依赖包 `path-is-absolute`**—— 这款依赖包自 2021 年以来下载量已超**90 亿次**。
![]()

攻击者在将这个受信任的包捆绑至恶意扩展程序之前，对其植入了新的代码。这段新增代码的唯一功能，就是在 VS Code 启动时**立即执行**，并解码一个隐藏在名为 `lock` 的内部文件中的 **JavaScript 投放器**。这意味着，那些盲目信任依赖项列表中知名包名称的用户，完全不会察觉到任何异常。

### 伪造 PNG 文件伪装术

攻击流程的最后一环，也是最具迷惑性的一步，涉及一个名为 `banner.png` 的文件。尽管后缀名 `.png` 看似是标准图片文件，但 RL 研究员指出，这仅仅是一种**伪装手段**。若尝试用常规图片查看器打开该文件，只会弹出错误提示。

进一步调查发现，`banner.png` 根本不是图片，而是一个**包含两个恶意二进制文件**（恶意软件的核心执行组件）的压缩归档包。解码后的投放器会调用 Windows 系统原生工具 `cmstp.exe` 来启动这两个二进制文件。其中体积较大的那个文件是一款**功能复杂的特洛伊木马**，不过其具体攻击能力目前仍在分析中。

值得注意的是，该攻击行动中的其他多款恶意扩展程序，采用了不同的攻击路径 —— 它们篡改的是另一款依赖项 `@actions/io`，且不依赖伪造 PNG 文件的伪装方式，而是将恶意二进制文件拆分至独立的 `.ts` 文件与 `.map` 文件中。

本文翻译自hackread [原文链接](https://hackread.com/malicious-vs-code-extensions-trojan-fake-png-files/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313712](/post/id/313712)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/malicious-vs-code-extensions-trojan-fake-png-files/)

如若转载,请注明出处： <https://hackread.com/malicious-vs-code-extensions-trojan-fake-png-files/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **800**

* 粉丝
* **6**

### TA的文章

* ##### [利用薪资评审诱饵实施精密钓鱼攻击：绕过防御窃取 Okta 单点登录会话令牌](/post/id/313745)

  2025-12-12 18:24:46
* ##### [高危漏洞预警 | CVE-2025-64188（CVSS 9.8）：WordPress “Soledad” 主题存在严重缺陷，订阅用户可直接接管网站](/post/id/313703)

  2025-12-12 18:05:27
* ##### [OpenAI 严阵以待：下一代 AI 模型或具备突破防御体系的能力](/post/id/313710)

  2025-12-12 18:04:59
* ##### [恶意 Visual Studio Code 扩展程序藏身虚假 PNG 文件，内置特洛伊木马](/post/id/313712)

  2025-12-12 18:04:19
* ##### [2022 年数据泄露致 160 万用户受影响，英国对 LastPass 处以 120 万英镑罚款](/post/id/313715)

  2025-12-12 18:03:30

### 相关文章

* ##### [利用薪资评审诱饵实施精密钓鱼攻击：绕过防御窃取 Okta 单点登录会话令牌](/post/id/313745)

  2025-12-12 18:24:46
* ##### [高危漏洞预警 | CVE-2025-64188（CVSS 9.8）：WordPress “Soledad” 主题存在严重缺陷，订阅用户可直接接管网站](/post/id/313703)

  2025-12-12 18:05:27
* ##### [OpenAI 严阵以待：下一代 AI 模型或具备突破防御体系的能力](/post/id/313710)

  2025-12-12 18:04:59
* ##### [2022 年数据泄露致 160 万用户受影响，英国对 LastPass 处以 120 万英镑罚款](/post/id/313715)

  2025-12-12 18:03:30
* ##### [Notepad++ 漏洞存在重大风险：攻击者可劫持网络流量，通过更新通道植入恶意软件](/post/id/313725)

  2025-12-12 18:02:46
* ##### [新型恶意软件 DroidLock 现身：锁定安卓设备并索要赎金](/post/id/313730)

  2025-12-12 18:01:37
* ##### [技能缺口持续扩大，INE 聚焦企业培训模式向实践操作转型](/post/id/313735)

  2025-12-12 18:00:56

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