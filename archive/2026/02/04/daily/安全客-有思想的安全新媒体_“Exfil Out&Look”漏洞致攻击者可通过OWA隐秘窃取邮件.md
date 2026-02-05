---
title: “Exfil Out&Look”漏洞致攻击者可通过OWA隐秘窃取邮件
url: https://www.anquanke.com/post/id/314701
source: 安全客-有思想的安全新媒体
date: 2026-02-04
fetch_date: 2026-02-05T04:07:38.911458
---

# “Exfil Out&Look”漏洞致攻击者可通过OWA隐秘窃取邮件

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

# “Exfil Out&Look”漏洞致攻击者可通过OWA隐秘窃取邮件

阅读量**28542**

发布时间 : 2026-02-04 11:28:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/exfil-outlook-flaw-lets-spies-steal-emails-via-owa-undetected/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

瓦罗尼斯威胁实验室（Varonis Threat Labs）发布的最新报告指出，**Microsoft 365 的日志记录功能存在重大盲区**，攻击者可借此窃取敏感邮件且不留下任何痕迹。这种被命名为 “Exfil Out&Look” 的攻击手段，利用 Outlook 合法插件实现数据的隐秘外泄，直接绕过安全团队用于发现入侵者的审计日志。

该漏洞的核心问题，在于 Outlook 桌面端与网页端的日志记录机制不一致。桌面端安装插件时会生成本地日志，而**Outlook 网页版（OWA）在插件安装和执行过程中，不会生成任何审计日志条目**。这一问题造成了**严重的溯源与监控空白**，让 OWA 沦为攻击者实施数据窃取的 “幽灵通道”。

插件的设计初衷是提升办公效率，但一旦落入不法分子手中，就会成为绝佳的间谍工具。瓦罗尼斯的研究人员验证发现，攻击者或恶意内部人员可通过 OWA 安装自定义插件，该插件能将用户收发的**每一封邮件副本自动转发至外部服务器**。

正是由于日志记录功能的失效，**通过 OWA 安装的插件可被恶意利用，在不生成审计日志、不留下任何取证痕迹的前提下，隐秘提取邮件数据**。

这与 Outlook 桌面端的正常机制形成鲜明对比 —— 桌面端的插件安装行为会被完整记录在日志中。但在以云为核心的 OWA 环境中，上述操作全程处于**日志不可见状态**。对于那些高度依赖统一审计日志开展威胁检测和事件调查的企业而言，这一盲区会让**恶意插件或权限过度开放的插件长期隐秘运行**，不被发现。

报告明确了该漏洞可能引发严重后果的多种场景：

* **恶意内部人员作案**：员工在离职前安装自定义插件，窃取自身的通信邮件记录。**由于插件的安装和执行不会生成任何审计日志，安全团队无法发现相关操作**。
* **账户遭入侵利用**：外部攻击者通过钓鱼攻击获取账户权限后，可安装该插件，以此**长期持续获取受害者的邮件流数据**。
* **高权限账户滥用**：恶意管理员可在整个企业内部部署该恶意插件，实现对**所有外发邮件的全面拦截**。
* **供应链投毒**：看似合法的第三方插件，可能隐藏着以 “AI 处理” 为名义的数传功能，企业对此类数据外泄行为**完全无迹可查**。

最令人担忧的，当属厂商对此问题的回应。瓦罗尼斯已于 2025 年 9 月向微软披露该漏洞，但经微软评估后，**将 “Exfil Out&Look” 归为低严重性产品缺陷或功能建议，且暂无立即修复或发布补丁的计划**。

本文翻译自securityonline [原文链接](https://securityonline.info/exfil-outlook-flaw-lets-spies-steal-emails-via-owa-undetected/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314701](/post/id/314701)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/exfil-outlook-flaw-lets-spies-steal-emails-via-owa-undetected/)

如若转载,请注明出处： <https://securityonline.info/exfil-outlook-flaw-lets-spies-steal-emails-via-owa-undetected/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

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
* **1000**

* 粉丝
* **6**

### TA的文章

* ##### [“Exfil Out&Look”漏洞致攻击者可通过OWA隐秘窃取邮件](/post/id/314701)

  2026-02-04 11:28:08
* ##### [新型高级Web后门潜入通信基础设施，利用高危漏洞将电话系统变为持久化后门](/post/id/314704)

  2026-02-04 11:26:44
* ##### [暗网现新型工业控制系统攻击框架，直指能源基础设施](/post/id/314710)

  2026-02-04 11:26:03
* ##### [微软新版Windows 11更新悄然收紧存储设置权限](/post/id/314713)

  2026-02-04 11:25:28
* ##### [Apache Syncope修复高危登录跨站脚本及外部实体注入漏洞](/post/id/314719)

  2026-02-04 11:24:58

### 相关文章

* ##### [新型高级Web后门潜入通信基础设施，利用高危漏洞将电话系统变为持久化后门](/post/id/314704)

  2026-02-04 11:26:44
* ##### [暗网现新型工业控制系统攻击框架，直指能源基础设施](/post/id/314710)

  2026-02-04 11:26:03
* ##### [微软新版Windows 11更新悄然收紧存储设置权限](/post/id/314713)

  2026-02-04 11:25:28
* ##### [Apache Syncope修复高危登录跨站脚本及外部实体注入漏洞](/post/id/314719)

  2026-02-04 11:24:58
* ##### [Notepad++被劫持国家级攻击者投毒更新包，持续数月作恶](/post/id/314722)

  2026-02-04 11:24:22
* ##### [Open VSX供应链攻击事件，黑客利用遭攻陷开发者账户传播GlassWorm恶意程序](/post/id/314725)

  2026-02-04 11:23:54
* ##### [WiFi劫持风险，海康威视修复DS-3WAP系列无线接入点命令注入漏洞](/post/id/314716)

  2026-02-04 11:23:22

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