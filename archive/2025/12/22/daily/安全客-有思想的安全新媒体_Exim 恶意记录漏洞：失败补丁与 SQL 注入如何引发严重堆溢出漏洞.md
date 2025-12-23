---
title: Exim 恶意记录漏洞：失败补丁与 SQL 注入如何引发严重堆溢出漏洞
url: https://www.anquanke.com/post/id/313923
source: 安全客-有思想的安全新媒体
date: 2025-12-22
fetch_date: 2025-12-23T03:23:51.176263
---

# Exim 恶意记录漏洞：失败补丁与 SQL 注入如何引发严重堆溢出漏洞

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

# Exim 恶意记录漏洞：失败补丁与 SQL 注入如何引发严重堆溢出漏洞

阅读量**12308**

发布时间 : 2025-12-22 16:29:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/exims-poisoned-record-how-a-failed-patch-and-sql-injection-lead-to-critical-heap-overflows/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一份新的安全公告揭示了全球最受欢迎的邮件传输代理（MTA）之一 **Exim** 的重大安全隐患。美国国家标准与技术研究院（NIST）网络安全负责人安德鲁・法萨诺（Andrew Fasano）披露了 Exim 4.99 版本中的**两项严重漏洞**，警告称此前的补丁未能彻底修复问题，留下了部分隐患，如今已引发了更深入、更危险的系统缺陷。

该披露于 2025 年 11 月 22 日发送给 Exim 安全团队，详细说明了涉及 SQLite 集成的**一系列漏洞**，这些漏洞可能允许远程攻击者**破坏系统内存**，甚至可能**接管服务器控制权**。

法萨诺指出，此前针对 **CVE-2025-26794**（一个涉及 ETRN 命令的 SQL 注入漏洞）的修复并不彻底。

虽然最初的补丁修复了 ETRN 这个特定的攻击向量，但并未解决 `xtextencode()` 函数中存在的**根本问题**。这个负责清理数据库密钥的函数，仍无法正确转义单引号字符（ASCII 39）。

“提示数据库（hints db）仍存在注入风险”，法萨诺强调，该漏洞现在可以通过另一种途径被利用：**速率限制访问控制列表（Ratelimit ACLs）**。攻击者可以发送包含恶意 “发件人地址” 的特制电子邮件，向数据库中注入任意 SQL 命令。

虽然 SQL 注入本身已具备危险性，但法萨诺发现，它只是一个入口，会引发更严重的问题：**堆缓冲区溢出（Heap Buffer Overflow）**。

这个新漏洞存在于 Exim 处理数据库记录中 `bloom_size` 字段的方式中。系统会从数据库读取这个大小字段，但**不进行任何验证**，直接用它来确定内存中的数组边界。

“系统不会验证 `bloom_size` 是否与实际数组大小匹配”，法萨诺在技术报告中解释道。

通过将这两个漏洞**结合利用**，攻击者可以借助 SQL 注入植入一条包含超大恶意 `bloom_size` 的记录。当系统尝试使用这条 “恶意记录（poisoned record）” 时，写入的数据会远远超出分配的缓冲区，从而引发堆溢出。法萨诺已成功证明，该漏洞最多可覆盖 **1.5MB 的内存**。

尽管由于地址空间布局随机化（ASLR）等现代防护机制的存在，法萨诺尚未实现完全的远程代码执行（RCE），但他确认该漏洞可实现 “可靠的崩溃预言机（crash oracle）”，并认为通过进一步研究，**完全实现远程代码执行（RCE）是有可能的**。该漏洞目前被编号为 **CVE-2025-67896**。

该攻击需要满足一系列特定的 “极端条件” 配置：

1. **SQLite 支持**：Exim 编译时必须启用 `USE_SQLITE=yes`；
2. **速率限制配置**：配置中使用的速率限制，需要依赖攻击者可控的数据（如 `$sender_address`）作为密钥；
   * 使用默认的 `per_addr` 且未设置显式密钥的配置不会受到影响，因为这类配置依赖客户端 IP 地址，而该地址无法通过 SMTP 被篡改。

该报告建议分配两个新的 CVE 编号，分别跟踪这两个不同的问题。对于修复方案，法萨诺建议 Exim 团队：

1. 对数据库记录实施**严格验证**；
2. 修复 `xtextencode()` 中的字符串转义逻辑 —— 或者更彻底的方式，**全面迁移至参数化查询**，从根源上消除 SQL 注入风险。

运行集成了 SQLite 的 Exim 4.99 的管理员，应**尽快升级到最新版本**。

本文翻译自securityonline [原文链接](https://securityonline.info/exims-poisoned-record-how-a-failed-patch-and-sql-injection-lead-to-critical-heap-overflows/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313923](/post/id/313923)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/exims-poisoned-record-how-a-failed-patch-and-sql-injection-lead-to-critical-heap-overflows/)

如若转载,请注明出处： <https://securityonline.info/exims-poisoned-record-how-a-failed-patch-and-sql-injection-lead-to-critical-heap-overflows/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **840**

* 粉丝
* **6**

### TA的文章

* ##### [电视中的 “狼”：规模达 180 万的 Kimwolf 僵尸网络流量超谷歌，称霸物联网领域](/post/id/313933)

  2025-12-22 16:32:27
* ##### [“脚本麻雀” 组织利用自动化技术生成并发送攻击邮件](/post/id/313954)

  2025-12-22 16:32:15
* ##### [黑客窃取数百万 PornHub 用户数据用于敲诈勒索](/post/id/313929)

  2025-12-22 16:31:50
* ##### [黑客发起定向钓鱼攻击，HubSpot 用户成攻击目标](/post/id/313948)

  2025-12-22 16:31:30
* ##### [微软发布紧急带外更新修复影响 IIS 站点的 MSMQ 漏洞](/post/id/313944)

  2025-12-22 16:30:34

### 相关文章

* ##### [电视中的 “狼”：规模达 180 万的 Kimwolf 僵尸网络流量超谷歌，称霸物联网领域](/post/id/313933)

  2025-12-22 16:32:27
* ##### [“脚本麻雀” 组织利用自动化技术生成并发送攻击邮件](/post/id/313954)

  2025-12-22 16:32:15
* ##### [黑客窃取数百万 PornHub 用户数据用于敲诈勒索](/post/id/313929)

  2025-12-22 16:31:50
* ##### [黑客发起定向钓鱼攻击，HubSpot 用户成攻击目标](/post/id/313948)

  2025-12-22 16:31:30
* ##### [微软发布紧急带外更新修复影响 IIS 站点的 MSMQ 漏洞](/post/id/313944)

  2025-12-22 16:30:34
* ##### [微软为 Office、SharePoint、Exchange、Teams 及 Entra 推出基线安全模式](/post/id/313926)

  2025-12-22 16:30:11
* ##### [人工智能超级应用横空出世：OpenAI 推出 ChatGPT 应用目录，剑指数字生活核心入口](/post/id/313938)

  2025-12-22 16:29:53

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