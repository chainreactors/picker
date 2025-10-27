---
title: Microsoft修复无法访问的Windows Server域控制器
url: https://www.anquanke.com/post/id/308457
source: 安全客-有思想的安全新媒体
date: 2025-06-14
fetch_date: 2025-10-06T22:50:20.577378
---

# Microsoft修复无法访问的Windows Server域控制器

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

# Microsoft修复无法访问的Windows Server域控制器

阅读量**78154**

发布时间 : 2025-06-13 15:40:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-unreachable-windows-server-domain-controllers/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Microsoft 解决了一个已知问题，该问题导致某些 Windows Server 2025 域控制器在重启后无法访问并触发应用程序或服务故障。

正如 Redmond 在 4 月份承认该错误时所解释的那样，在重新启动后加载标准防火墙配置文件而不是域防火墙配置文件的服务器将无法正确管理网络流量。

由于此问题，在受影响的域控制器服务器或远程设备上运行的服务和应用程序可能会失败或无法访问同一网络上的端点和服务器。

“Windows Server 2025 域控制器（例如托管 Active Directory 域控制器角色的服务器）可能无法在重启后正确管理网络流量，”Microsoft 表示。

“因此，Windows Server 2025 域控制器可能无法在域网络上访问，或者无法通过端口和协议访问，否则域防火墙配置文件应阻止这些端口和协议。”

本周，该公司在 2025 年 6 月补丁星期二期间发布的 KB5060842 Windows 安全更新中解决了这一已知问题。

无法立即安装本月更新以缓解 bug 的管理员还可以应用临时解决方法，要求他们使用 PowerShell 命令在受影响的服务器上手动重启网络适配器。`Restart-NetAdapter *`

但是，请务必注意，他们必须在每次重新启动后重新启动它，直到安装 KB5060842 更新，因为每当重新启动受影响的域控制器时，此已知问题都会自动触发。

周二，Microsoft 还修复了另一个已知问题，该问题阻止某些 Windows 用户在安装 2025 年 4 月KB5055523安全更新后使用 Windows Hello 登录其帐户。

4 月，该公司解决了另一个 KB5055523 问题，该问题在使用 Kerberos PKINIT 预身份验证安全协议的系统上启用 Credential Guard 时导致身份验证问题。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-unreachable-windows-server-domain-controllers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308457](/post/id/308457)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-unreachable-windows-server-domain-controllers/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-unreachable-windows-server-domain-controllers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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