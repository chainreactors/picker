---
title: 趋势科技Apex One曝高危漏洞 可被利用执行恶意代码
url: https://www.anquanke.com/post/id/314940
source: 安全客-有思想的安全新媒体
date: 2026-03-03
fetch_date: 2026-03-04T04:02:01.861435
---

# 趋势科技Apex One曝高危漏洞 可被利用执行恶意代码

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

# 趋势科技Apex One曝高危漏洞 可被利用执行恶意代码

阅读量**26988**

发布时间 : 2026-03-03 10:01:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Abinaya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/trend-micro-apex-one-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

趋势科技已发布修复程序，解决 **Apex One** 中多个**高危至 critical 级**安全漏洞，其中包含管理控制台相关缺陷，可能被利用导致**远程代码执行（RCE）**。

本次涉及漏洞编号为 **CVE-2025-71210 至 CVE-2025-71217**，CVSS v3 评分从 **7.2 到 9.8** 不等。

2026 年 2 月的安全公告显示，受影响产品包括：

* Windows 版 **Apex One 2019（本地部署）**
* Windows 版 **Apex One as a Service（Trend Vision One Endpoint 标准终端防护）**

趋势科技在修复建议中明确建议用户升级至**最新可用版本**，即便此前补丁已修复部分问题，仍建议完整更新。

---

### 趋势科技 Apex One 漏洞详情

其中 **两个 critical 漏洞 CVE-2025-71210 和 CVE-2025-71211**，均属于 Apex One 管理控制台中的**目录遍历导致的远程代码执行漏洞（CWE-22）**。

攻击者可利用这些漏洞**上传恶意代码并在受影响系统上执行命令**。

趋势科技指出，利用该漏洞需要**能够访问 Apex One 管理控制台**。

官方同时警告，**控制台地址直接暴露在公网会显著提升风险**，建议未配置访问限制的用户立即添加源 IP 限制策略。

公告同时披露了影响 Windows 组件的本地提权（LPE）漏洞，包括符号链接跟随漏洞（CWE-59）与来源校验错误漏洞（CWE-346）。

表格

| CVE | 漏洞类型 | CVSS | 平台 | 关键说明 |
| --- | --- | --- | --- | --- |
| CVE-2025-71210 | 控制台目录遍历 RCE | 9.8 | Windows | 需要控制台访问权限；SaaS 环境已缓解 |
| CVE-2025-71211 | 控制台目录遍历 RCE | 9.8 | Windows | 与 71210 原理类似 |
| CVE-2025-71212 | 符号链接跟随 LPE | 7.8 | Windows | 需要先执行低权限代码 |
| CVE-2025-71213 | 来源校验 LPE | 7.8 | Windows | 需要先执行低权限代码 |
| CVE-2025-71214 | 来源校验 LPE | 7.2 | Mac | 仅作信息告知；此前已修复 |
| CVE-2025-71215 | TOCTOU 竞态 LPE | 7.8 | Mac | 仅作信息告知；此前已修复 |
| CVE-2025-71216 | TOCTOU 竞态 LPE | 7.8 | Mac | 仅作信息告知；此前已修复 |
| CVE-2025-71217 | 来源校验 LPE | 7.8 | Mac | 仅作信息告知；此前已修复 |

这类本地提权漏洞要求攻击者**已能在目标终端上执行低权限代码**，才能进一步利用。

对于 macOS 代理端，趋势科技将相关 CVE 列为**信息性参考**，表示这些问题已于 **2025 年中后期通过 ActiveUpdate / SaaS 更新提前修复**。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/trend-micro-apex-one-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314940](/post/id/314940)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/trend-micro-apex-one-vulnerabilities/)

如若转载,请注明出处： <https://cybersecuritynews.com/trend-micro-apex-one-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1050**

* 粉丝
* **6**

### TA的文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26

### 相关文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26
* ##### [Anthropic推出记忆导入功能，助力QuitGPT浪潮下用户迁移对话数据](/post/id/314990)

  2026-03-04 10:34:57
* ##### [Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风](/post/id/314994)

  2026-03-04 10:34:28

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