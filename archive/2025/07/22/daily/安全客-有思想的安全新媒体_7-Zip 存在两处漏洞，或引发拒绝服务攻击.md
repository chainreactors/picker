---
title: 7-Zip 存在两处漏洞，或引发拒绝服务攻击
url: https://www.anquanke.com/post/id/310360
source: 安全客-有思想的安全新媒体
date: 2025-07-22
fetch_date: 2025-10-06T23:16:53.858645
---

# 7-Zip 存在两处漏洞，或引发拒绝服务攻击

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

# 7-Zip 存在两处漏洞，或引发拒绝服务攻击

阅读量**70658**

发布时间 : 2025-07-21 17:24:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/two-vulnerabilities-in-7-zip-could-trigger-denial-of-service/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

研究人员披露，全球广泛使用的**开源文件压缩工具 7-Zip** 存在**两个新发现的漏洞**。这两个漏洞编号为 **CVE-2025-53816** 和 **CVE-2025-53817**，影响 7-Zip 25.0.0 版本之前的所有版本。尽管目前认为它们不会导致远程代码执行，但**可能引发内存损坏和拒绝服务（DoS）问题**。

这两个漏洞的 CVSS v4 基础评分为 **5.5**，属于中等严重级别，但仍需引起用户的立即关注，尤其是那些**处理不可信压缩文件**的用户。

**第一个漏洞（CVE-2025-53816）**存在于 7-Zip 对 **RAR5 压缩包的处理过程**中。具体而言，该软件在提取文件时，会根据攻击者可控的值来计算需要清零的内存字节数，从而出现处理不当的问题。

CVE 描述中提到：“在 25.0.0 版本之前的 7-Zip 中，**RAR5 处理器在堆缓冲区外写入零值，可能导致内存损坏和拒绝服务**。”

这一问题源于**涉及\_lzEnd 变量的错误计算**，该变量取决于压缩包中前一项的大小，且可能受到攻击者的影响。

安全公告解释道：“攻击者**可能控制要覆盖的字节数**…… 虽然不太可能导致任意代码执行，但可能因内存损坏引发拒绝服务。”

尽管目前尚无证据表明该漏洞可被用于执行代码，但堆空间内存损坏可能导致程序不稳定或崩溃。

**第二个漏洞（CVE-2025-53817）**影响 7-Zip 对**复合文档（Compound Document）格式文件的提取功能**。攻击者通过构造恶意复合文档文件，可能导致 7-Zip 应用程序意外崩溃，干扰正常工作流程，甚至可能在自动化文件处理环境中造成服务中断。

最新的 7-Zip 25.0.0 版本已修复这两个漏洞。建议用户立即更新，以确保安全处理压缩文件，尤其是来自不可信或未知来源的文件。

本文翻译自securityonline [原文链接](https://securityonline.info/two-vulnerabilities-in-7-zip-could-trigger-denial-of-service/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310360](/post/id/310360)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/two-vulnerabilities-in-7-zip-could-trigger-denial-of-service/)

如若转载,请注明出处： <https://securityonline.info/two-vulnerabilities-in-7-zip-could-trigger-denial-of-service/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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