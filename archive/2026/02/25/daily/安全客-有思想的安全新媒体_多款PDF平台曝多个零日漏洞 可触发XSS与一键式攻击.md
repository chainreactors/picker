---
title: 多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击
url: https://www.anquanke.com/post/id/314837
source: 安全客-有思想的安全新媒体
date: 2026-02-25
fetch_date: 2026-02-26T04:09:54.518315
---

# 多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击

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

# 多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击

阅读量**18726**

发布时间 : 2026-02-25 14:18:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/zero-day-flaws-pdf-platforms-xss-one-click-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

我们通常将 PDF（便携式文档格式）文件看作纸质文档的简单数字版。但一项向 [Hackread.com](https://Hackread.com) 披露的最新研究显示，这类日常工具已演变为复杂的**应用程序栈**，黑客可借此作为入侵专用网络的入口。

Novee Security 团队近期对两大主流 PDF 系统 ——Foxit 与 Apryse 展开安全检测。这项于 2026 年 2 月 18 日公布的研究，共梳理出**13 大类漏洞类型**，合计**16 种可被利用的系统入侵途径**。

值得注意的是，这些并非普通小缺陷；这批**零日漏洞**可让攻击者在**无需直接攻破浏览器或操作系统**的前提下，实现**账号接管**或在企业后端服务器**执行任意命令**。

### 借助 AI 挖掘安全漏洞

众所周知，在海量代码中定位安全漏洞是一项极大挑战。为提升效率，研究人员采用 “人 + 智能体” 协同模式 ：先人工识别出漏洞 “特征”（程序可能存在弱点的特定模式），再将这些模式交给 AI “集群” 进行学习。

研究团队发现，这类 AI 集群在扫描混淆代码时，速度远快于人工。该方法能有效挖掘出常规工具常遗漏的**高危害漏洞**。其中一项关键发现是：Foxit 签名服务器存在**高危漏洞**，该服务器负责处理法律文件的数字签名业务。

“我们的策略是**人与智能体共生**：研究人员先手动提炼基础漏洞模式，再将其教给 Novee 智能体。智能体掌握这类漏洞‘特征’后，便可自主遍历两大厂商的庞大攻击面，最终发现**13 个不同类型的漏洞**，覆盖高危**XSS**至**操作系统命令注入**等多种危害。” 研究人员介绍道。

### 一键式攻击原理详解

本次研究中最令人警惕的是**一键式攻击**：受害者仅需打开文档或点击链接，即可触发攻击陷阱。已确认的核心风险包括：

* CVE-2025-70402、CVE-2025-70400：Apryse WebViewer 存在漏洞，系统会不当信任远程配置文件，黑客可通过链接**执行恶意代码**。
* CVE-2025-70401：研究人员发现可将脚本隐藏在 PDF 评论的 “作者” 字段中。受害者在批注区输入任意字符时，脚本便会自动运行并**窃取登录凭证**。
* CVE-2025-66500：Foxit 网页插件存在同类缺陷，攻击者可构造伪造消息，诱使插件**执行恶意脚本**。

在实测中，AI 智能体仅通过向服务器发送简单请求，即可让目标**执行注入命令**，使研究人员获得对应系统模块的**完整控制权**。

### 安全防护需多方共担

Novee Security 在博客中指出，问题根源在于：现代 PDF 工具已采用类似高级网站的架构，使用 iframe 与服务端渲染技术，但多数企业仍将其视为**低风险文件**。这便引发了研究人员所说的“信任边界失效”—— 软件对本应二次校验的数据盲目信任。

好消息是，Novee Security 在公开前已与相关厂商协同处置。Foxit 与 Apryse 均已收到漏洞通报，对应的官方 CVE 编号已分配，相关漏洞正在**逐步修复**。完整漏洞清单可在官方链接中查看。

本文翻译自hackread [原文链接](https://hackread.com/zero-day-flaws-pdf-platforms-xss-one-click-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314837](/post/id/314837)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/zero-day-flaws-pdf-platforms-xss-one-click-attacks/)

如若转载,请注明出处： <https://hackread.com/zero-day-flaws-pdf-platforms-xss-one-click-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1020**

* 粉丝
* **6**

### TA的文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52

### 相关文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [黑客利用Facebook广告投放虚假Win11更新实施恶意攻击](/post/id/314844)

  2026-02-25 14:18:43
* ##### [银狐APT组织利用BYOVD攻击投放Winos 4.0恶意软件](/post/id/314847)

  2026-02-25 14:18:35
* ##### [CISA警告USR-W610物联网设备存在9.8分高危漏洞且已无补丁支持](/post/id/314851)

  2026-02-25 14:11:13

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