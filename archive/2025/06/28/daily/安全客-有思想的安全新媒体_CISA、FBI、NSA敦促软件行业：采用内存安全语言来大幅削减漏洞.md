---
title: CISA、FBI、NSA敦促软件行业：采用内存安全语言来大幅削减漏洞
url: https://www.anquanke.com/post/id/309080
source: 安全客-有思想的安全新媒体
date: 2025-06-28
fetch_date: 2025-10-06T22:52:05.569712
---

# CISA、FBI、NSA敦促软件行业：采用内存安全语言来大幅削减漏洞

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

# CISA、FBI、NSA敦促软件行业：采用内存安全语言来大幅削减漏洞

阅读量**67239**

发布时间 : 2025-06-27 14:24:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/cisa-fbi-nsa-urge-software-industry-adopt-memory-safe-languages-to-drastically-cut-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全和基础设施安全局 （CISA） 与 FBI、NSA 和主要国际网络安全合作伙伴一起发布了一份新指南，呼吁软件行业过渡到内存安全编程语言 （MSL），作为减少软件漏洞的关键步骤。

该指南的标题为“内存安全语言：减少现代软件开发中的软件漏洞”，强调当今可利用的安全漏洞的很大一部分源于使用非内存安全语言（如 C 和 C++）编写的软件中的内存安全问题。

几十年来，内存安全漏洞（如缓冲区溢出、释放后使用错误和数据争用）一直困扰着软件系统。这些错误主要来自 C 和 C++ 等语言，这些语言授予低级内存控制，但提供有限的安全保证。风险是关键的。正如指南所强调的：

**“Heartbleed 影响了超过 800,000 个访问量最大的网站……BadAlloc 影响了嵌入式设备、工业控制系统和超过 1.95 亿辆汽车，展示了内存漏洞如何威胁国家安全和关键基础设施。”**

Google 的 Project Zero 发现，2021 年，67% 的在野零日漏洞是内存安全漏洞，这一统计数据生动地说明了系统性变革的迫切需求。

Rust、Go、Java 和 Swift 等内存安全语言旨在默认强制实施严格的内存安全，从而大大降低此类漏洞的可能性。与依赖开发人员规则的传统语言不同，MSL 将安全机制直接嵌入到语言中：

**“MSL 提供内置的保护措施，将安全负担从开发人员转移到语言和开发环境。”**

这些保护措施包括边界检查、严格的所有权和借用规则（如 Rust）、垃圾回收（在 Go 和 Java 等语言中）和运行时安全检查等功能。这些措施可以防止缓冲区溢出和释放后使用访问等常见错误，这些错误通常是漏洞利用的入口点。

该指南最引人注目的示例之一来自 Android。2019 年，其 76% 的漏洞源于内存安全问题。认识到这一点后，Google 做出了战略转变：

**“Android 团队做出了一项战略决策，在所有新开发中优先考虑 MSL，特别是 Rust 和 Java……到 2024 年，内存安全漏洞已骤降至总数的 24%。”**

该指南中的一个关键信息是实用性。虽然对现有代码库进行全面改造可能不可行，但将 MSL 集成到新项目和高风险组件中既可以实现又有影响力。该指南鼓励：

* 使用 MSL 进行新开发。
* 优先考虑高风险组件，例如面向网络的服务和文件解析器。
* 采用模块化设计，通过定义明确的 API 将 MSL 与遗留代码集成。

正如指南所解释的：

**“目前，在所有情况或解决方案领域，开始采用 MSL 并非都可行;可能需要额外的投资来减少内存安全错误。”**

MSL 不仅可以提高安全性，还可以提高系统可靠性和开发人员的工作效率。通过消除整类错误并通过运行时检查支持更好的调试，它们可以减少停机时间并加快创新周期。

**“在编译或运行时测试期间及早检测到错误可以加快调试速度，缩短故障排除时间，并最大限度地降低代价高昂的事件风险。”**

CISA 和 NSA 建议组织发布*内存安全采用路线图*，并与 NIST 安全软件开发框架 （SSDF） 等框架保持一致。他们还强调了行业、政府和学术界在培养 MSL 意识和技能方面的重要性。

归根结底，本指南是一个号召性用语：

**“战略性采用 MSL 是对安全软件未来的投资。通过定义内存安全路线图并引领采用最佳实践，组织可以显著提高软件弹性，并帮助确保更安全的数字环境。**

本文翻译自securityonline [原文链接](https://securityonline.info/cisa-fbi-nsa-urge-software-industry-adopt-memory-safe-languages-to-drastically-cut-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309080](/post/id/309080)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/cisa-fbi-nsa-urge-software-industry-adopt-memory-safe-languages-to-drastically-cut-vulnerabilities/)

如若转载,请注明出处： <https://securityonline.info/cisa-fbi-nsa-urge-software-industry-adopt-memory-safe-languages-to-drastically-cut-vulnerabilities/>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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