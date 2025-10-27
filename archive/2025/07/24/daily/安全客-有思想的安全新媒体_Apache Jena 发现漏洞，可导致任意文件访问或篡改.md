---
title: Apache Jena 发现漏洞，可导致任意文件访问或篡改
url: https://www.anquanke.com/post/id/310442
source: 安全客-有思想的安全新媒体
date: 2025-07-24
fetch_date: 2025-10-06T23:16:44.057619
---

# Apache Jena 发现漏洞，可导致任意文件访问或篡改

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

# Apache Jena 发现漏洞，可导致任意文件访问或篡改

阅读量**75682**

发布时间 : 2025-07-23 17:21:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/apache-jena-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Apache Jena 已披露两个影响至版本 5.4.0 的重大安全漏洞，建议用户立即升级至版本 5.5.0。

CVE-2025-49656 和 CVE-2025-50151 于 2025 年 7 月 21 日公布，属于高严重性的漏洞，利用管理员权限攻击，可能破坏服务器文件系统的完整性。

##### 关键要点：

1. ##### Apache Jena v5.4.0 存在两个漏洞（CVE-2025-49656、CVE-2025-50151）；
2. ##### 漏洞利用 Fuseki 管理接口的路径验证不足，导致文件系统绕过攻击；
3. ##### 请立即升级至 v5.5.0 修复这两个问题。

这些漏洞暴露了 Fuseki 服务器管理接口中的关键弱点，输入验证不足使得未经授权的文件系统操作超出了预定的目录范围。

### CVE-2025-49656: 目录遍历漏洞

第一个漏洞，CVE-2025-49656，允许管理员用户通过 Fuseki 管理界面在指定的服务器目录空间之外创建数据库文件。

这个目录遍历攻击漏洞利用了管理界面中路径验证机制不足的漏洞，允许具有合法管理员凭证的攻击者绕过文件系统限制。

漏洞的根源在于数据库创建操作过程中文件路径参数未经过适当的清理。

技术分析显示，该漏洞很可能与对用户提供的目录路径在向管理端点发送 POST 请求时的验证不足有关。

攻击者可以利用如 `../` 的路径序列来遍历父目录，从而将文件写入服务器文件系统上的任意位置。

这代表了经典的路径遍历漏洞，可能导致配置文件篡改、日志污染，或根据目标系统配置的不同，可能引发远程代码执行等安全风险。

### CVE-2025-50151: 配置文件上传漏洞

第二个漏洞，CVE-2025-50151，影响了管理界面中的配置文件上传功能。

上传的配置文件中的文件访问路径缺乏适当的验证，这为任意文件访问攻击提供了机会。

该漏洞允许管理员上传包含恶意路径引用的配置文件，从而绕过预定的安全边界。

技术实现的薄弱点出现在配置解析器处理文件路径指令时。系统在处理上传的配置文件时，未能验证或清理文件访问路径，可能通过相对路径操作引用到敏感的系统文件。

这可能使攻击者能够引用应用程序目录结构之外的配置文件、系统二进制文件或敏感数据。

此漏洞的发现归功于 Cyber Defense Institute, Inc. 的 Noriaki Iwasaki，强调了安全研究合作的重要性。

![]()

### **缓解措施**

运行 Apache Jena 部署的组织应立即升级到 5.5.0 版本，该版本已针对两个漏洞进行了全面修复。

更新版本引入了增强的路径验证机制，并限制了任意配置文件上传，以防止漏洞被利用。

由于这两个漏洞都需要管理员访问权限，因此即时风险仅限于管理员凭证可能被泄露或存在内部威胁的环境。

系统管理员应检查访问日志，留意异常的文件创建模式，并验证只有信任的人员具有 Fuseki 服务器的管理员访问权限。

此外，实施深度防御策略，如文件系统级别的访问控制，可以为类似漏洞提供额外的保护层。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/apache-jena-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310442](/post/id/310442)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/apache-jena-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/apache-jena-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**7赞

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