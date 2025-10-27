---
title: CERT/CC 警告 Workhorse 市政会计软件存在严重漏洞
url: https://www.anquanke.com/post/id/311347
source: 安全客-有思想的安全新媒体
date: 2025-08-21
fetch_date: 2025-10-07T00:47:43.888673
---

# CERT/CC 警告 Workhorse 市政会计软件存在严重漏洞

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

# CERT/CC 警告 Workhorse 市政会计软件存在严重漏洞

阅读量**50283**

发布时间 : 2025-08-20 17:50:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/cert-cc-warns-of-critical-flaws-in-workhorse-municipal-accounting-software/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

CERT 协调中心（CERT/CC）发布漏洞通告，称 Workhorse Software Services 的市政财务管理平台存在严重安全缺陷。**1.9.4.48019 之前的版本**由于设计层面的问题，可能导致市政单位的敏感财务数据和个人信息被未授权访问或被恶意导出。

通告称：“Workhorse Software Services 的市政财务软件在 1.9.4.48019 版本之前包含设计缺陷，可能允许未授权访问敏感数据，并导致数据外泄。”

此次确认了两个核心漏洞：

### 1. 明文存储数据库连接字符串（CVE-2025-9037）

该软件将 SQL Server 的连接凭据明文存放在配置文件中。通告说明：“软件把 SQL Server 连接字符串以明文形式存储在可执行文件旁的配置文件中……任何拥有该目录读取权限的人都可以获取这些凭据。”

### 2. 未认证的数据库备份功能（CVE-2025-9040）

应用程序设计缺陷允许**即使未登录的用户**也可以创建并下载未加密的数据库备份。CERT/CC 指出：“应用程序在登录界面即可访问的 ‘File’ 菜单提供数据库备份功能，它会执行 SQL Server Express 的备份操作，并允许用户将生成的 .bak 文件保存成未加密的 ZIP 压缩包。”

这些问题可能会被具备以下条件的攻击者利用：

**·** 拥有物理访问权限；

**·** 能读取网络共享文件的恶意软件；

**·** 社会工程手法骗取系统入口权限。

### 安全影响

CERT/CC 警告说：“攻击者可能获取完整数据库，其中可能包含**社会保险号（SSN）、完整市政财务记录和其他机密个人信息**。”
除了数据泄露，还可能导致：

**·** 财务记录被恶意篡改；

**·** 审计数据失真；

**·** 市政财政系统信任度受损。

### 官方建议

CERT/CC **强烈建议立即升级至 1.9.4.48019 版本**。
若短期无法升级，可采取以下缓解措施：

**·** 使用 NTFS 权限限制对软件目录的访问；

**·** 启用 SQL Server 加密和 Windows 身份验证；

**·** 在可行情况下禁用数据库备份功能；

**·** 配置网络分段与防火墙规则，减少暴露面。

本文翻译自securityonline [原文链接](https://securityonline.info/cert-cc-warns-of-critical-flaws-in-workhorse-municipal-accounting-software/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311347](/post/id/311347)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/cert-cc-warns-of-critical-flaws-in-workhorse-municipal-accounting-software/)

如若转载,请注明出处： <https://securityonline.info/cert-cc-warns-of-critical-flaws-in-workhorse-municipal-accounting-software/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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