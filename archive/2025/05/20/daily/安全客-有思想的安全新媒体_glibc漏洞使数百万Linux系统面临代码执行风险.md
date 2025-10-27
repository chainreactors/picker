---
title: glibc漏洞使数百万Linux系统面临代码执行风险
url: https://www.anquanke.com/post/id/307535
source: 安全客-有思想的安全新媒体
date: 2025-05-20
fetch_date: 2025-10-06T22:23:47.473273
---

# glibc漏洞使数百万Linux系统面临代码执行风险

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

# glibc漏洞使数百万Linux系统面临代码执行风险

阅读量**57738**

发布时间 : 2025-05-19 16:26:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/glibc-vulnerability-cve-2025-4802-puts-millions-of-linux-systems-at-risk-of-code-execution/>

译文仅供参考，具体内容表达以及含义原文为准。

![glibc 漏洞 Linux 安全]()

GNU C 库(glibc)中新报告的漏洞,是无数 Linux 应用程序的基本组成部分,它详细介绍了静态 setuid 二进制文件的共享库加载机制中可能可利用的弱点。

跟踪为 CVE-2025-4802[,](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/)[environment](https://securityonline.info/lastpass-your-digital-life-secured-and-simplified-review-recommendation/)该漏洞源于静态 setuid 二进制文件在通过 dlopen() 进行动态库调用时不正确使用 LD\_LIBRARY\_PATH 环境变量。

GNU C 库或 glibc 是 GNU 工程和几乎所有主要 Linux 发行版所使用的标准 C 库。它充当操作系统内核和用户空间程序之间的桥梁,实现输入/输出处理、内存分配和网络通信等基本功能。

虽然glibc主要用于动态链接的二进制文件,但它也支持静态链接的可执行文件 – 自包含的程序,包括编译时所有必要的库。

缺陷在于静态 setuid 二进制文件与动态加载器之间的相互作用。[advisory](https://sourceware.org/cgit/glibc/tree/advisories/GLIBC-SA-2025-0002)根据咨询:

*调用 dlopen(包括 setlocale 后的内部 dlopen 调用或调用 NSS 函数(如 getaddrinfo)的静态链接 setuid 二进制文件可能会错误地搜索 LD\_LIBRARY\_PATH 以确定要加载的库,从而导致执行由攻击者控制的库代码。*

通常,像LD\_LIBRARY\_PATH这样的环境变量被特权二进制文件(即那些有setuid的二进制文件)忽略,以避免引入安全风险。然而,CVE-2025-4802打破了这一假设,允许恶意用户在存在易受攻击的setuid二进制文件并直接或通过常见的libc依赖函数调用dlopen()时注入任意代码。

风险被归类为局部和情境,因为它需要:

* 系统上的静态链接 setuid 二进制文件。
* 二进制文件必须调用 dlopen()()——手动或通过间接 libc/NSS 调用。
* [environment](https://securityonline.info/lastpass-your-digital-life-secured-and-simplified-review-recommendation/)环境必须允许用户设置 LD\_LIBRARY\_PATH。

*该咨询机构承认:“在发布此咨询时没有发现此类计划,但定制setuid程序的存在,尽管作为安全实践受到强烈劝阻,但不能打折扣。*

[这使得该漏洞成为低概率但高影响力的漏洞](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/),特别是在具有遗留或自定义静态二进制文件的环境中。

系统管理员和 Linux 发行商应:

* 将 glibc [更新到 2.39](https://www.gnu.org/software/libc/) 版本,或者如果维护自定义构建,请手动应用修复程序。
* 审核静态 setuid 二进制文件,并在可能的情况下删除或重新编译它们与动态链接。

本文翻译自securityonline [原文链接](https://securityonline.info/glibc-vulnerability-cve-2025-4802-puts-millions-of-linux-systems-at-risk-of-code-execution/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307535](/post/id/307535)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/glibc-vulnerability-cve-2025-4802-puts-millions-of-linux-systems-at-risk-of-code-execution/)

如若转载,请注明出处： <https://securityonline.info/glibc-vulnerability-cve-2025-4802-puts-millions-of-linux-systems-at-risk-of-code-execution/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)

**+1**3赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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