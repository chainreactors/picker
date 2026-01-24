---
title: 微软更新Microsoft 365企业版应用安全基线
url: https://www.anquanke.com/post/id/314495
source: 安全客-有思想的安全新媒体
date: 2026-01-23
fetch_date: 2026-01-24T03:30:06.862004
---

# 微软更新Microsoft 365企业版应用安全基线

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

# 微软更新Microsoft 365企业版应用安全基线

阅读量**15892**

发布时间 : 2026-01-23 10:17:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 Net Security，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2026/01/22/microsoft-365-security-baseline-2512/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

微软正式发布**Microsoft 365 企业版应用安全基线 2512 版本**。该基线文档明确了企业环境下 Office 应用的**推荐策略配置**，并将这些配置与当前的管理工具进行适配关联。

### 2512 版本基线的覆盖范围

2512 版本基线对 Word、Excel、PowerPoint、Outlook 和 Access 的各项配置进行归类整合，涵盖**宏、插件、ActiveX 控件、受保护视图**以及应用更新行为相关的管控项。其中的配置指引明确了默认值与推荐值，安全团队可通过策略直接应用。

微软提供的基线文件适配企业主流工作流格式，包括**组策略对象**和**Microsoft Intune 设置目录**。每项配置均附带说明文档与推荐取值，管理员可根据企业内部需求审核并调整相关配置。

### 与早期版本基线的差异

微软表示，2512 版本基线更新了配置推荐项，使其与**当前版本的 Microsoft 365 企业版应用**保持一致，同时文档内容也同步了近期 Office 版本迭代中，策略可用范围与命名规则的变更。

部分配置项所在的管理模板与早期基线相比发生了调整，文档中对这类变更做了**重点标注**，方便安全团队追踪各类策略在不同管理工具和操作系统版本中的呈现位置。

### 安全团队对该基线的使用方式

安全基线是企业环境**加固工作**的重要参考依据，安全团队通常会将现有 Office 配置与官方发布的推荐配置进行比对，以此发现配置漏洞与不一致的地方。

实际应用中，企业一般会先将基线导入测试环境，验证应用运行表现，再通过 Intune 或组策略部署选定的配置项。该基线将各项推荐配置独立呈现，而非打包强制推送，为这一落地流程提供了适配支持。

用户可从**微软安全合规工具包**中下载本次更新的基线，对推荐配置进行测试后，根据实际需求完成落地部署。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2026/01/22/microsoft-365-security-baseline-2512/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314495](/post/id/314495)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2026/01/22/microsoft-365-security-baseline-2512/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2026/01/22/microsoft-365-security-baseline-2512/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **950**

* 粉丝
* **6**

### TA的文章

* ##### [威胁行为者将Visual Studio Code武器化，部署多阶段恶意软件](/post/id/314458)

  2026-01-23 10:23:22
* ##### [遭野外利用：思科关键RCE漏洞（CVE-2026-20045）已被攻击](/post/id/314457)

  2026-01-23 10:22:51
* ##### [CVE-2025-13878：高严重性BIND漏洞可致服务器远程崩溃](/post/id/314469)

  2026-01-23 10:22:16
* ##### [攻击者滥用Discord传播剪贴板劫持程序，窃取粘贴操作中的钱包地址](/post/id/314467)

  2026-01-23 10:21:16
* ##### [带宽盗贼：伪造的Notepad++安装包暗藏 “代理劫持”恶意软件](/post/id/314481)

  2026-01-23 10:20:42

### 相关文章

* ##### [威胁行为者将Visual Studio Code武器化，部署多阶段恶意软件](/post/id/314458)

  2026-01-23 10:23:22
* ##### [遭野外利用：思科关键RCE漏洞（CVE-2026-20045）已被攻击](/post/id/314457)

  2026-01-23 10:22:51
* ##### [CVE-2025-13878：高严重性BIND漏洞可致服务器远程崩溃](/post/id/314469)

  2026-01-23 10:22:16
* ##### [攻击者滥用Discord传播剪贴板劫持程序，窃取粘贴操作中的钱包地址](/post/id/314467)

  2026-01-23 10:21:16
* ##### [带宽盗贼：伪造的Notepad++安装包暗藏 “代理劫持”恶意软件](/post/id/314481)

  2026-01-23 10:20:42
* ##### [蓝色起源推出太赫兹波卫星网络：6Tbps速率对标星链](/post/id/314480)

  2026-01-23 10:19:44
* ##### [勒索软件组织RansomHub攻击苹果供应商立讯精密，窃取1TB未发布产品数据](/post/id/314487)

  2026-01-23 10:19:09

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