---
title: GlassWorm蠕虫重现：利用隐形Unicode字符重复感染VS Code扩展，并扩散至GitHub平台
url: https://www.anquanke.com/post/id/313100
source: 安全客-有思想的安全新媒体
date: 2025-11-10
fetch_date: 2025-11-11T03:12:24.991474
---

# GlassWorm蠕虫重现：利用隐形Unicode字符重复感染VS Code扩展，并扩散至GitHub平台

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

# GlassWorm蠕虫重现：利用隐形Unicode字符重复感染VS Code扩展，并扩散至GitHub平台

阅读量**24427**

发布时间 : 2025-11-10 17:24:27

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/glassworm-worm-resurfaces-invisible-unicode-malware-re-infects-vs-code-extensions-spreads-to-github/>

译文仅供参考，具体内容表达以及含义原文为准。

一场名为 **GlassWorm** 的复杂自传播恶意软件活动再度出现，已感染三个新的 VS Code 扩展，证实其对全球开发者生态系统构成重大威胁。最初披露该蠕虫的 **Koi Security** 报告称，在 OpenVSX 市场于 2025 年 10 月 21 日宣布事件“已完全控制并结束”仅 16 天后，新一轮感染浪潮已出现。

这不仅对代码市场构成威胁；对攻击者服务器的分析显示，受害者部分名单涵盖“美国、南美洲、欧洲和亚洲”，其中包括“中东某主要政府实体”。

2025 年 11 月 6 日，Koi Security 检测到 GlassWorm 针对 OpenVSX 注册表上另外三个扩展发起新一轮攻击：

1. **ai-driven-dev.ai-driven-dev** （3,300 次下载）
2. **adhamu.history-in-sublime-merge** （4,000 次下载）
3. **yasuyuky.transient-emacs** （2,400 次下载）

仅这一波攻击就造成约 10,000 台设备新增感染。

**GlassWorm** 的核心隐蔽手段仍是**不可见 Unicode 字符**的使用：恶意代码被编码为不可打印的 Unicode 字符，人类查看时“在代码编辑器中完全消失”，但被系统解释时会作为 JavaScript 执行。目前已确认该蠕虫还扩散至 GitHub 仓库，利用窃取的凭据向更多代码库推送恶意提交。威胁行为者使用“**AI 生成的提交记录**，将不可见有效载荷隐藏在看似合法的代码变更中”——这一危险演变使恶意代码与正常开发活动无缝融合。

![]()

攻击者的基础设施展现出强大韧性，依靠去中心化技术确保持久化：

1. **区块链 C2**：蠕虫继续利用 **Solana 区块链**作为其命令控制（C2）机制。攻击者在 Solana 区块链上发布低成本交易，提供更新的 C2 端点以下载下一阶段有效载荷。这种策略形成“无法清除的基础设施”，因为“即使有效载荷服务器被关闭，攻击者只需花费几分之一美分发布新交易，所有受感染设备就会自动获取新位置”。
2. **静态服务器**：尽管使用区块链 C2，主 C2 服务器（**199.247.10.166**）和数据泄露端点（**199.247.13.106:80/wall**）仍保持运行，与最初分析中的配置一致。

根据线索，Koi Security 访问了攻击者服务器上的一个暴露端点。提取的数据令人警醒，证实该蠕虫对全球组织造成了实际影响。

除受害者名单外，服务器中还包含攻击者自身的键盘记录数据，为溯源提供了重要线索：

1. 使用开源浏览器扩展 C2 框架 **RedExt**；
2. 恢复了多个加密货币交易所（如 **bybit.com/ru-RU** ）和消息平台的用户 ID。

本文翻译自securityonline [原文链接](https://securityonline.info/glassworm-worm-resurfaces-invisible-unicode-malware-re-infects-vs-code-extensions-spreads-to-github/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313100](/post/id/313100)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/glassworm-worm-resurfaces-invisible-unicode-malware-re-infects-vs-code-extensions-spreads-to-github/)

如若转载,请注明出处： <https://securityonline.info/glassworm-worm-resurfaces-invisible-unicode-malware-re-infects-vs-code-extensions-spreads-to-github/>

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
* ##### [软件供应链投毒警报：9个NuGet包内嵌定时触发破坏逻辑，将在硬编码日期导致应用彻底损毁](/post/id/313097)

  2025-11-10 17:25:49
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