---
title: Django发布安全补丁 修复拒绝服务与权限类漏洞
url: https://www.anquanke.com/post/id/315047
source: 安全客-有思想的安全新媒体
date: 2026-03-06
fetch_date: 2026-03-07T03:54:35.217526
---

# Django发布安全补丁 修复拒绝服务与权限类漏洞

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

# Django发布安全补丁 修复拒绝服务与权限类漏洞

阅读量**23680**

发布时间 : 2026-03-06 10:56:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/django-releases-security-patches-to-address-dos-and-permission-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Django 安全团队已针对该框架所有受支持版本发布重要更新，修复两个新发现的安全漏洞。此次发布的更新涵盖 Django 6.0.3、5.2.12 和 4.2.29 版本，解决了一个**中等严重程度的拒绝服务（DoS）漏洞**，以及一个与文件权限配置错误相关的低严重程度问题。

官方强烈建议开发者尽快升级环境，以降低相关安全风险。

### CVE-2026-25673：Unicode 归一化引发的潜在拒绝服务攻击

这两个漏洞中影响更突出的是一个 “中等” 严重级漏洞，该漏洞影响 `URLField` 表单字段。在 Windows 系统中，该字段的 `to_python()` 方法所采用的处理流程可能被利用，导致服务器资源被大量消耗。

根据官方安全公告：“在 Windows 系统上，`urlsplit()` 函数会执行 NFKC 归一化（`unicodedata.normalize`），对于包含特定字符的大体积输入数据，该操作的执行速度会异常缓慢”。这种性能损耗形成了拒绝服务攻击的潜在载体，恶意攻击者可发送构造的恶意输入，导致服务器陷入卡顿。

为解决该问题，Django 团队实现了一套简化的协议检测逻辑，**完全绕过了 Unicode 归一化流程**。使用自定义验证器的开发者需注意：“字段值中的换行符、制表符及其他控制字符，将不再由 `URLField.to_python()` 处理”。

### CVE-2026-25674：文件系统权限风险

第二个低严重级漏洞，涉及 Django 在创建新文件或目录时的权限处理机制。此前，该框架的文件系统存储模块和基于文件的缓存后端，均依赖进程的 `umask`（权限掩码）来控制文件 / 目录权限。

安全团队发现，在多线程环境下存在这样的风险：“一个线程临时修改的 `umask` 会影响其他线程创建文件和目录的操作，导致文件系统对象被赋予非预期的权限”。这可能造成敏感文件被创建时，访问权限设置过于宽松的情况。

本次更新修改了这一行为：在目录创建完成后，立即通过 `os.chmod()` 应用指定的权限配置，**不再依赖全局的进程级 `umask`**，消除了这一安全隐患。

### 受影响版本与修复方案

相关补丁已应用于主开发分支，以及所有当前受支持的稳定分支。

| 受影响分支 | 已修复版本 |
| --- | --- |
| Django main | 已修复 |
| Django 6.0 | 6.0.3 |
| Django 5.2 | 5.2.12 |
| Django 4.2 | 4.2.29 |

### 总结

1. Django 紧急发布补丁修复两类漏洞：Windows 系统下 URLField 引发的 DoS 漏洞（CVE-2026-25673），以及多线程环境下的文件权限漏洞（CVE-2026-25674）。
2. DoS 漏洞的核心成因是 Unicode 归一化处理大体积恶意输入时性能异常，修复方式为绕过该归一化流程；权限漏洞则通过改用 `os.chmod()` 直接设置权限，摆脱对 `umask` 的依赖。
3. 所有受支持版本（6.0/5.2/4.2）均已推出对应修复版本，开发者需尽快升级以规避风险。

本文翻译自securityonline [原文链接](https://securityonline.info/django-releases-security-patches-to-address-dos-and-permission-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315047](/post/id/315047)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/django-releases-security-patches-to-address-dos-and-permission-vulnerabilities/)

如若转载,请注明出处： <https://securityonline.info/django-releases-security-patches-to-address-dos-and-permission-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1060**

* 粉丝
* **6**

### TA的文章

* ##### [Django发布安全补丁 修复拒绝服务与权限类漏洞](/post/id/315047)

  2026-03-06 10:56:33
* ##### [攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据](/post/id/315044)

  2026-03-06 10:54:37
* ##### [伊朗关联黑客瞄准监控摄像头漏洞](/post/id/315041)

  2026-03-06 10:54:12
* ##### [癌症中心研究数据遭黑客攻击120万人信息受影响](/post/id/315038)

  2026-03-06 10:53:46
* ##### [Outlook.com为何大量误拦正常商业邮件](/post/id/315035)

  2026-03-06 10:53:13

### 相关文章

* ##### [攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据](/post/id/315044)

  2026-03-06 10:54:37
* ##### [伊朗关联黑客瞄准监控摄像头漏洞](/post/id/315041)

  2026-03-06 10:54:12
* ##### [癌症中心研究数据遭黑客攻击120万人信息受影响](/post/id/315038)

  2026-03-06 10:53:46
* ##### [Outlook.com为何大量误拦正常商业邮件](/post/id/315035)

  2026-03-06 10:53:13
* ##### [Coruna席卷全球威胁格局的高性能iOS漏洞利用工具包](/post/id/315032)

  2026-03-06 10:52:45
* ##### [Grammarly 从文字纠错转向文学模仿](/post/id/315029)

  2026-03-06 10:52:13
* ##### [Cisco Secure FMC曝出10分高危漏洞 攻击者可获取企业防火墙Root权限](/post/id/315023)

  2026-03-06 10:51:30

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