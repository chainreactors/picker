---
title: Z0Scan设计与实现：通用插件与分布式扫描新思路
url: https://www.anquanke.com/post/id/312991
source: 安全客-有思想的安全新媒体
date: 2025-12-16
fetch_date: 2025-12-17T03:17:51.406229
---

# Z0Scan设计与实现：通用插件与分布式扫描新思路

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

# Z0Scan设计与实现：通用插件与分布式扫描新思路

阅读量**21269**

发布时间 : 2025-12-16 10:26:40

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

各位前辈老师好，我是九泠，目前是某三线城市的一名普通高中生，也是 **Z0Scan** 项目的发起人与核心开发者。我希望借这次机会，向各位前辈们系统地介绍下 **Z0Scan**。

![image.png]()

```
项目地址
GitHub - https://github.com/JiuZero/z0scan
Gitee - https://gitee.com/JiuZero/z0scan
```

Z0Scan 的萌芽始于我初三时期，当时深受 w13scan 与 xray 的启发，逐渐萌生了一个想法：

打造一款不依赖臃肿 POC、专注于大通用型漏洞探测的扫描器。她不仅具备高度通用的漏洞插件架构，更致力于探查那些被忽视的、冷门却广泛存在的安全风险，探索Web黑盒的更多可能。

![image.png]()

在设计理念上，Z0Scan 将 WAF 嗅探融入指纹识别环节，并基于 WAF 存在与否智能调度插件与 Payload，从而以更少的请求、更低的拦截率完成检测。

但 Z0Scan 的调度逻辑不止于此——服务类型、中间件等指纹信息同样可作为调度依据，正如 EZScanner 中的“HTTP Request Reduce”技术所倡导的那样：

![image.png]()

随着不断迭代，Z0Scan 逐步发展出多项核心特性：

1. **本地与分布式一体化架构**

   支持本地与基于 Redis 的分布式部署，融合了主被动扫描能力，并彻底摆脱对 BurpSuite 的依赖，延续了 myscan 在分布式方面的设计思路。

![image.png]()

1. **AI 辅助的 JS 敏感信息校验**

   为避免传统正则匹配的误报，Z0Scan 引入 AI 对初步匹配结果进行二次校验，提升准确性与可信度。
2. **原生 IPv6 支持**

   从 myscan 中汲取灵感，Z0Scan 实现了对 IPv6 环境的完整兼容，拓展了适用场景以达到绕过部分防火墙的目的。

![image.png]()

1. **伪静态参数智能提取**

   针对 EZScanner、Xray 等工具尚未完善的伪静态路径解析能力，Z0Scan 进行了初步实现，覆盖多种伪静态结构。

   得益于 **WAF 指纹信息对插件的干涉**，sqli-bool 采用了**更保守、更少的Payload**完成了检测：

![image.png]()

1. **Web 控制台：流量队列与插件热管理**

   提供流量队列机制，避免被动扫描时抢占关键请求；同时支持在扫描过程中动态启停插件，灵活适配不同测试场景，提升控制精度。

![image.png]()

1. **插件外部动态导入**

   借助 Python 的灵活性与 Nuitka 编译优化，Z0Scan 支持插件热加载，兼顾开发效率与运行性能。

```
├─config
│  ├─lists
│  └─others
├─data
├─fingerprints
│  ├─os
│  ├─programing
│  └─webserver
└─scanners
    ├─PerDir
    ├─PerDomain
    ├─PerHost
    └─PerPage
```

1. **被动指纹支持**

   CMS百家争鸣，0day、1day层出不穷，当 afrog、nuclei 项目并不能够满足红队工作者的历史漏洞全面性要求时，其它更具针对性而全面的漏洞扫描体将成为红队工作者的更佳选择。

   而 afrog与 nuicle 的社区活跃度本已不是 z0scan 所能追及的，那么则应在两者间寻求平衡点——通过融合被动指纹识别与被动扫描能力，将指纹匹配与历史漏洞检索的完整性问题交由用户判断，同时赋予用户自主选择漏洞检测策略的权利。

   Z0Scan 目前支持近6000种CMS指纹识别，并向插件开放指纹检索，为针对特定CMS的0day漏洞检测插件（POC）开发提供了灵活、可扩展的实现方案。

![image.png]()

1. **主机端口漏洞探查**

   赓续 myscan 的开发思想，Z0Scan 支持了针对每一主机（基于HOST IP去重）的端口探测与漏洞探查，并借助动态导入优势减少不必要的端口开放检测。

此外，Z0Scan 还具备些小的创新优化：

如对SQL注入存在概率的判断算法，它来自于 DetSQL

![image.png]()

这里使用的是EZ – 1.9.0，但在后续 EZ 的更新中有提及对SQL盲注的优化（不清楚还会不会误报，属实没积分了/泪水）

Z0Scan 最终的被动工作流程如下：

![image.png]()

当然，命令行操作并非对所有人都友好。因此，我同步开发了 Ling 。

![image.png]()

```
项目地址
GitHub - https://github.com/JiuZero/Ling
Gitee - https://gitee.com/JiuZero/Ling
```

一个为 Z0Scan 量身打造的可视化操作界面。她将 Z0Scan 的各项能力以更直观、更美观的方式呈现，助力安全研究者轻松上手，高效“食用”Z0。

![image.png]()

![image.png]()

![image.png]()

在 Z0Scan 的成长路上汲取了一些开源项目的养分，它们包括但不限于：W13Scan、GourdScanV2、myscan、Sitadel..

插件开发离不开它们：tplmap、webcrack、SQLmap..

```
相关信息
文档：https://jiuzero.github.io/tags/z0scan
发行页：https://github.com/JiuZero/z0scan/releases
更新日志：https://github.com/JiuZero/z0scan/blob/master/doc/CHANGELOG.MD
```

同时 Z0Scan 的开发也离不开各位大师傅们的支持与肯定，**最后诚以此向各位网安工作者们表达最深的敬意。**

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**泠、**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312991](/post/id/312991)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [0day](/tag/0day)
* [Web安全](/tag/Web%E5%AE%89%E5%85%A8)
* [工具分享](/tag/%E5%B7%A5%E5%85%B7%E5%88%86%E4%BA%AB)
* [红队](/tag/%E7%BA%A2%E9%98%9F)
* [黑盒](/tag/%E9%BB%91%E7%9B%92)

**+1**0赞

收藏

![](https://thirdwx.qlogo.cn/mmopen/vi_32/PiajxSqBRaEJP6cPvpGTD1Avc2gNqfp2GncGA44H4PlvibicxCguVaNZxqgOcibJfYvJoOBR4Wwgjk2aSibwzcRy2qC6HEDNOBviaBIUtLvAUNVGXicYvsz1kxHPA/132)泠、

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://thirdwx.qlogo.cn/mmopen/vi_32/PiajxSqBRaEJP6cPvpGTD1Avc2gNqfp2GncGA44H4PlvibicxCguVaNZxqgOcibJfYvJoOBR4Wwgjk2aSibwzcRy2qC6HEDNOBviaBIUtLvAUNVGXicYvsz1kxHPA/132)](/member.html?memberId=179085)

[泠、](/member.html?memberId=179085)

这个人太懒了，签名都懒得写一个

* 文章
* **1**

* 粉丝
* **0**

### TA的文章

* ##### [Z0Scan设计与实现：通用插件与分布式扫描新思路](/post/id/312991)

  2025-12-16 10:26:40

### 相关文章

* ##### [CVE-2025-9868 Nexus Repository 2 – 远程浏览器插件导致的未授权 SSRF 漏洞复现](/post/id/312467)

  2025-12-12 18:10:16
* ##### [美实名爆料：马斯克领导的DOGE被指入侵劳工机构系统，敏感数据疑遭泄露](/post/id/306743)

  2025-04-21 16:48:48
* ##### [ISCC-2025-第22届信息安全与对抗技术竞赛通知](/post/id/306659)

  2025-04-18 15:49:50
* ##### [梨子带你刷burpsuite靶场系列之服务器端漏洞篇 - sql注入专题更新部分](/post/id/288407)

  2025-03-26 16:05:51
* ##### [梨子带你刷burpsuite靶场系列之客户端漏洞篇 - 跨站脚本(XSS)及跨站请求伪造(CSRF)专题更新部分](/post/id/288408)

  2025-03-26 16:05:51
* ##### [「奇御」AI.安全技术沙龙 · 3月29日北京开启！](/post/id/305187)

  2025-03-20 11:24:51
* ##### [Yakit从入门到实战](/post/id/300674)

  2024-11-12 17:44:56

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