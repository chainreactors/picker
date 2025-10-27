---
title: 微软修复了打开电子邮件时导致崩溃的Outlook错误
url: https://www.anquanke.com/post/id/309134
source: 安全客-有思想的安全新媒体
date: 2025-07-01
fetch_date: 2025-10-06T23:50:49.583859
---

# 微软修复了打开电子邮件时导致崩溃的Outlook错误

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

# 微软修复了打开电子邮件时导致崩溃的Outlook错误

阅读量**39574**

发布时间 : 2025-06-30 18:18:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源： bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-outlook-bug-causing-crashes-when-opening-emails/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

微软已经修复了一个已知问题，该问题会导致经典的 Outlook 电子邮件客户端在打开电子邮件或开始新邮件时崩溃。

本月早些时候更新了Outlook for Microsoft 365的所有Microsoft 365 Office渠道的用户都会受到该漏洞的影响。

“当您打开或开始新邮件时，经典 Outlook 会崩溃。出现这个问题是因为 Outlook 无法打开表单库。Outlook 团队在上周承认这一问题时表示：”这一问题的新出现情况是在虚拟桌面基础架构（VDI）上。

该公司表示，该错误已在多个渠道得到解决，为当前频道预览、每月企业频道、半年企业频道、Outlook 2021 和 Outlook 2024 用户发布了修复版本。

Redmond 还将分别在 7 月 1 日和 7 月 8 日发布非安全更新以修复 Outlook 2016 和 Outlook 2019 的问题。

无法立即更新或仍在等待修复版本的用户可以在 C：\Users\<username>\AppData\Local\Microsoft\FORMS2 中手动创建缺少的 FORMS2 文件夹作为临时解决方法。

为此，您必须按照以下步骤作：

1. 关闭 Outlook 和其他 Office 应用程序。
2. 选择 **Start**> **Run**并输入路径 %localappdata%\Microsoft然后选择 **OK。**
3. 在 **File Explorer** 菜单中，选择 **New****> Folder**并将其命名为 FORMS2。

Microsoft 还解决了影响当前频道和 Beta 频道中用户的 Outlook 问题，该问题导致在更新到 Outlook 版本 2505（内部版本 18827.20128）后将项目移动到文件夹时，邮箱文件夹闪烁并四处移动。

建议无法应用修复的受影响用户恢复到版本 2504，或者通过禁用下载共享文件夹作为解决方法来关闭共享邮箱的缓存。

最近几周，Redmond 还推送了一项服务更新，以解决在打开 Viva Engage、Yammer、Power Automate 和其他电子邮件时触发 Outlook LTSC 2019 崩溃的错误。

今年早期，Microsoft 发布了针对另一个已知问题的修复程序，该问题导致经典 Outlook 和 Microsoft 365 应用程序在 Windows Server 系统上崩溃。此外，该公司还分享了在编写、回复或转发电子邮件时影响经典 Outlook 的崩溃的临时修复程序。

本文翻译自 bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-outlook-bug-causing-crashes-when-opening-emails/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309134](/post/id/309134)

安全KER - 有思想的安全新媒体

本文转载自:  [bleepingcomputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-outlook-bug-causing-crashes-when-opening-emails/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-outlook-bug-causing-crashes-when-opening-emails/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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