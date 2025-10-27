---
title: Interlock勒索软件采用“FileFix”手法投递恶意程序
url: https://www.anquanke.com/post/id/310056
source: 安全客-有思想的安全新媒体
date: 2025-07-16
fetch_date: 2025-10-06T23:39:09.567793
---

# Interlock勒索软件采用“FileFix”手法投递恶意程序

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

# Interlock勒索软件采用“FileFix”手法投递恶意程序

阅读量**51802**

发布时间 : 2025-07-15 18:16:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/interlock-ransomware-adopts-filefix-method-to-deliver-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

黑客组织近期在 Interlock 勒索软件攻击中采用一种名为**“FileFix”**的新技术，在目标系统中植入**远程访问木马（RAT）**。

过去几个月中，Interlock 勒索软件的活动显著增加。攻击者开始使用 **KongTuke 网络注入器（又称“LandUpdate808”）**，通过被攻陷的网站**投放恶意载荷**。

据 The DFIR Report 与 Proofpoint 安全研究人员观察，自**5月起该攻击手法发生了变化**。当时，受害者访问被攻击网站后，会被引导通过一个**伪造的 CAPTCHA 验证页面**，然后被要求将自动复制到剪贴板的内容粘贴进“运行”对话框。这种方式与 **ClickFix** 攻击手法一致。该方法诱使用户**执行一个 PowerShell 脚本**，从而下载并运行一个基于 Node.js 的 Interlock RAT **远程访问木马变种**。

6月，研究人员又发现了一个**基于 PHP 的 Interlock RAT 变种**，该变种同样通过 KongTuke 注入器投递，显示攻击方式具有**多样性**。

![]()

*Interlock的 FileFix 攻击（**来源：DFIR 报告）*

本月初，Interlock 的恶意程序投递方式再次发生**重大变化**，攻击者开始采用 **ClickFix 技术的变种“FileFix”**作为新的主要手段。

“FileFix”是一种**社会工程攻击技术**，由安全研究员 mr.d0x 开发。它是 ClickFix 的升级版本，后者在过去一年中已成为**最广泛使用**的恶意载荷传播方式之一。

在 FileFix 技术中，攻击者利用 **Windows 操作系统中受信任的用户界面元素**（如文件资源管理器和 HTML 应用程序 .HTA 文件），诱导用户执行恶意的 PowerShell 或 JavaScript 脚本，而不会触发任何安全警告。

用户会被提示“打开文件”，并被引导将复制好的字符串粘贴进文件资源管理器的地址栏。该字符串实际上是**伪装成文件路径的 PowerShell 命令**，利用注释语法掩盖其真实意图。

在近期的 Interlock 攻击中，攻击者要求受害者**将一个伪装成文件路径的命令粘贴进资源管理器地址栏**，从而下载并执行托管在 [trycloudflare.com](http://trycloudflare.com) 上的 PHP 远控木马。

感染成功后，该木马会执行一系列 PowerShell 命令，用以**收集系统与网络信息**，并将这些数据以结构化 JSON 格式回传给攻击者。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/interlock-ransomware-adopts-filefix-method-to-deliver-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310056](/post/id/310056)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/interlock-ransomware-adopts-filefix-method-to-deliver-malware/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/interlock-ransomware-adopts-filefix-method-to-deliver-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**7赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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