---
title: Linux 内核高危漏洞致系统面临权限提升攻击
url: https://www.anquanke.com/post/id/307049
source: 安全客-有思想的安全新媒体
date: 2025-05-01
fetch_date: 2025-10-06T22:23:27.472877
---

# Linux 内核高危漏洞致系统面临权限提升攻击

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

# Linux 内核高危漏洞致系统面临权限提升攻击

阅读量**425014**

发布时间 : 2025-04-30 14:08:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/linux-kernel-vulnerability-privilege-escalation/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Linux 内核的虚拟套接字 (vsock) 实现中存在一个严重漏洞，编号为 CVE-2025-21756，该漏洞可能允许本地攻击者将权限提升到 root 级别。

安全研究人员已确认，该漏洞的 CVSS v3.1 基本评分为 7.8（高），可在受影响的系统上被有效利用。

## 严重 Linux 内核漏洞 – CVE-2025-21756

根据 Hoefler报告，该漏洞源于 vsock 子系统在传输重新分配期间对套接字绑定处理不当。

具体来说，问题发生在套接字的引用计数器错误地减少的序列中，从而导致释放后使用的情况。

该漏洞的核心在于Linux内核中的以下代码路径：

![]()

当发生传输重新分配时，此函数会减少引用计数器，而不验证套接字是否已绑定并移动到绑定列表。

这可能会导致这样一种情况：后续对 vsock\_bind() 的调用假定套接字位于未绑定列表中，并调用 \_\_vsock\_remove\_bound()，从而导致释放后使用的情况。

Linux 内核开发人员实施的补丁通过添加一个简单的检查来解决这个问题，以保留套接字绑定直到套接字被破坏：

![]()

|  |  |
| --- | --- |
| **风险因素** | **细节** |
| 受影响的产品 | 具有 vsock（虚拟套接字）实现的 Linux 内核（特别是 6.6.79、6.12.16、6.13.4 和 6.14-rc1 之前的版本） |
| 影响 | 可能提升权限 |
| 漏洞利用前提条件 | 本地访问，能够创建和操作 vsock 套接字；攻击复杂度低；无需用户交互；攻击者必须拥有本地权限 |
| CVSS 3.1 评分 | 7.8（高） |

## 漏洞利用方法

安全社区中出现了一种详细的利用方法。该攻击涉及触发UAF漏洞，然后使用受控数据回收已释放的内存。

一种特别复杂的方法是利用管道支持页面来覆盖关键的内核结构。

该漏洞通过查找未受这些安全机制保护的功能来绕过 Linux 安全模块 (LSM) 保护，特别是 AppArmor。

通过使用 vsock\_diag\_dump() 作为侧信道，攻击者可以泄露 init\_net 的内存地址，从而有效地破坏内核地址空间布局随机化 (KASLR)。

利用这些功能，攻击者构建了一个面向返回编程 (ROP) 链，该链调用 commit\_creds(init\_cred) 来提升权限。

最后的漏洞利用通过调用套接字的 release() 函数触发 sk->sk\_error\_report 的函数指针覆盖来重定向执行。

## 受影响的系统和补丁发布

此漏洞影响所有运行易受攻击内核版本的 Linux 发行版。对于严重依赖 vsock 功能进行客户机与主机通信的云环境和虚拟化系统而言，此问题尤其令人担忧。

如果被利用，攻击者可以获得 root 权限，从而可能导致整个系统被入侵、数据被盗或服务中断。

主流Linux发行版均已发布修复该漏洞的补丁。用户应立即将系统更新至最新内核版本。

对于无法立即修补的系统，建议限制本地用户的访问并监控与 vsock 子系统相关的可疑活动。

CVE-2025-21756 对 Linux 系统构成重大安全风险。虽然要求本地访问可以限制其直接影响，但已知漏洞利用方法的可靠性使得此漏洞在多用户或容器环境中尤其危险。

系统管理员应优先修补受影响的系统以减轻这种威胁。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/linux-kernel-vulnerability-privilege-escalation/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307049](/post/id/307049)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/linux-kernel-vulnerability-privilege-escalation/)

如若转载,请注明出处： <https://cybersecuritynews.com/linux-kernel-vulnerability-privilege-escalation/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* [严重 Linux 内核漏洞 - CVE-2025-21756](#h2-0)
* [漏洞利用方法](#h2-1)
* [受影响的系统和补丁发布](#h2-2)

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