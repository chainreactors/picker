---
title: Advantech紧急警报：严重缺陷（CVSS 9.6）使工业自动化面临远程接管
url: https://www.anquanke.com/post/id/308997
source: 安全客-有思想的安全新媒体
date: 2025-06-27
fetch_date: 2025-10-06T22:50:06.658478
---

# Advantech紧急警报：严重缺陷（CVSS 9.6）使工业自动化面临远程接管

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

# Advantech紧急警报：严重缺陷（CVSS 9.6）使工业自动化面临远程接管

阅读量**65944**

发布时间 : 2025-06-26 14:03:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/urgent-advantech-alert-critical-flaws-cvss-9-6-expose-industrial-automation-to-remote-takeover-poc-releases/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

幻影新加坡网络安全局 （CSA） 发布了一份紧急安全公告，强调了影响研华工业自动化产品的多个高影响漏洞，特别是 WISE-4010LAN、WISE-4050LAN 和 WISE-4060LAN 系列。这些设备广泛部署在工业控制系统 （ICS） 中，利用这些漏洞可能会导致远程接管、系统重启、modbus纵，甚至物理设备受损。

据 CSA 称，研华已通过安全补丁和缓解策略解决了这些漏洞（跟踪为 CVE-2025-48461 到 CVE-2025-48470），但系统管理员仍需要采取紧急行动。

在披露的 8 个 CVE 中，有几个因其潜在的未经身份验证的远程利用、关键基础设施控制和持久访问而脱颖而出：

* CVE-2025-48469 （CVSS 9.6）：允许未经身份验证的攻击者通过公共更新页面上传固件，从而为后门安装或权限提升打开大门。
* CVE-2025-48466 （CVSS 8.1）：允许远程攻击者发送恶意 Modbus TCP 数据包以纵数字输出，从而有效地获得对继电器开关的物理控制，这对工业运营构成令人担忧的风险。
* CVE-2025-48461 （CVSS 5.0）：涉及可预测的会话 Cookie，允许暴力帐户接管和对 root/admin 帐户的未授权访问。

“成功利用该漏洞可能允许未经身份验证的攻击者进行暴力猜测和帐户接管……可能允许攻击者获得 root、admin 或 user 访问权限并重置密码”*，*CSA 警告说。

此外，CVE-2025-48468 还暴露了一个物理向量，允许具有 JTAG 访问权限的攻击者注入或修改固件，尽管这在较新的固件版本中已得到缓解。

更紧迫的是，已经发布了针对两个关键 CVE 的公共 PoC 漏洞利用代码：

* CVE-2025-48466 – Modbus 中继纵
* CVE-2025-48469 – 未经身份验证的固件上传

这些证明证明了现实世界的可利用性，并增加了广泛攻击的风险，尤其是在尚未实施修复程序的环境中。

CSA 根据漏洞的严重性概述了双管齐下的缓解策略：

1. 启用“安全模式”

适用于：CVE-2025-48461、CVE-2025-48462、CVE-2025-48463、CVE-2025-48469、CVE-2025-48470。

“安全模式限制对不安全的 Web 界面的访问，并禁用不必要的服务以减少攻击面。”

2. 固件更新至 A2.02 B00

涵盖 CVE-2025-48466、CVE-2025-48467 和 CVE-2025-48468。主要更改包括：

* 手动禁用 Modbus TCP（如果不使用）。
* JTAG 接口在正常作期间默认禁用。

“鼓励受影响产品的用户和管理员更新并实施建议的缓解措施，”CSA 公告指出。

本文翻译自securityonline [原文链接](https://securityonline.info/urgent-advantech-alert-critical-flaws-cvss-9-6-expose-industrial-automation-to-remote-takeover-poc-releases/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308997](/post/id/308997)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/urgent-advantech-alert-critical-flaws-cvss-9-6-expose-industrial-automation-to-remote-takeover-poc-releases/)

如若转载,请注明出处： <https://securityonline.info/urgent-advantech-alert-critical-flaws-cvss-9-6-expose-industrial-automation-to-remote-takeover-poc-releases/>

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

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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