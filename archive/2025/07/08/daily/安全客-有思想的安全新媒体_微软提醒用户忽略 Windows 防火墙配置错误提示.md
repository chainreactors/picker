---
title: 微软提醒用户忽略 Windows 防火墙配置错误提示
url: https://www.anquanke.com/post/id/309447
source: 安全客-有思想的安全新媒体
date: 2025-07-08
fetch_date: 2025-10-06T23:17:55.038619
---

# 微软提醒用户忽略 Windows 防火墙配置错误提示

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

# 微软提醒用户忽略 Windows 防火墙配置错误提示

阅读量**56752**

发布时间 : 2025-07-07 15:54:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源： bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/microsoft/microsoft-asks-users-to-ignore-windows-firewall-config-errors/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近期，微软发布公告称，用户在安装 2025 年 6 月 Windows 预览更新（KB5060829）并重启系统后，如果在事件查看器中看到与 **Windows 高级安全防火墙相关的错误提示，可放心忽略**。

这些错误事件被记录为“事件 2042”，内容为**“配置读取失败（Config Read Failed）**”，并伴有“**有更多数据可用（More data is available）**”的信息。

微软指出，该问题源于一个**仍在开发中的新功能**，目前尚未完全集成到操作系统中。“在安装 2025 年 6 月非安全性预览更新（KB5060829）后，安全事件日志中可能包含一条与 Windows 高级安全防火墙相关的错误事件，但该事件可以**安全忽略**，”微软在 Windows 更新健康状态仪表盘上表示。

“请注意，**Windows 防火墙的功能不会受到影响**，用户**无需采取任何操作**来预防或修复此类错误事件。该日志仅与一个尚未正式启用的开发中功能有关。”

目前，这些错误日志仅出现在运行 Windows 11 24H2 的系统上，但**不会影响与此事件相关的任何 Windows 系统进程**。

微软表示，已着手修复该已知问题，并将在后续提供进一步更新。

事实上，近几个月来，微软也遇到过多个类似的错误报告问题，这些问题虽引发系统提示，但对实际功能**无任何影响**。

例如，今年 4 月，微软修复了一个导致 Windows 10 和 Windows 11 设备误报 BitLocker 加密错误的 Bug。该问题出现在企业管控环境中，仅影响强制启用操作系统和固定磁盘加密的设备。

同月，微软还确认并修复了另一个已知问题，该问题会在安装 2025 年 4 月的 Windows 恢复环境（WinRE）更新后，错误地触发 0x80070643 安装失败提示。

本文翻译自 bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/microsoft/microsoft-asks-users-to-ignore-windows-firewall-config-errors/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309447](/post/id/309447)

安全KER - 有思想的安全新媒体

本文转载自:  [bleepingcomputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-asks-users-to-ignore-windows-firewall-config-errors/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/microsoft/microsoft-asks-users-to-ignore-windows-firewall-config-errors/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**4赞

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
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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