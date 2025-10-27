---
title: 打印机安全警报：Rapid 7发现Multi Brother型号中的关键缺陷（CVSS9.8）
url: https://www.anquanke.com/post/id/309087
source: 安全客-有思想的安全新媒体
date: 2025-06-28
fetch_date: 2025-10-06T22:52:07.094300
---

# 打印机安全警报：Rapid 7发现Multi Brother型号中的关键缺陷（CVSS9.8）

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

# 打印机安全警报：Rapid 7发现Multi Brother型号中的关键缺陷（CVSS9.8）

阅读量**71879**

发布时间 : 2025-06-27 14:23:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/printer-security-alert-rapid7-uncovers-critical-flaws-cvss-9-8-in-multi-brother-models/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在一次重要的协调披露中，Rapid7 公布了一系列令人不安的漏洞，这些漏洞影响了四大供应商–博锐、富士商业创新、理光和东芝技术公司–的多种多功能打印机 (MFP)。这些发现涉及 8 个不同的 CVE，影响到 742 种打印机、扫描仪和标签打印机型号，给企业和消费者环境都带来了巨大的安全风险。

最严重的问题被追踪为 CVE-2024-51978 (CVSS 9.8)，这是一个身份验证绕过漏洞，远程未认证攻击者只需知道设备的序列号，就能获取设备的默认管理员密码。Rapid7 解释说“这是由于发现了 Brother 设备使用的默认密码生成程序。该程序将序列号转化为默认密码。”

更令人担忧的是，这一漏洞无法通过固件更新得到完全修复。相反，Brother 不得不改变受影响设备的生产流程，这意味着只有新生产的设备才能幸免于难。对于旧机型，该公司已经发布了一种解决方法。

更令人担忧的是，此缺陷无法通过固件更新完全修复。相反，Brother 不得不更改受影响设备的制造流程，这意味着只有新生产的设备才能免疫。对于旧型号，该公司已经发布了解决方法。

另一个影响较大的漏洞 CVE-2024-51979 （CVSS 7.2） 涉及基于堆栈的缓冲区溢出，经过身份验证的攻击者可以利用该漏洞。结合 CVE-2024-51978，攻击者可以实现完全远程代码执行：

“漏洞 CVE-2024-51979 允许经过身份验证的攻击者触发基于堆栈的缓冲区溢出…实现远程代码执行 （RCE） 的足够漏洞利用原语。”

此攻击链将看似的配置疏忽转变为整个系统入侵的潜在网关。

Rapid7 的报告概述了另外六个漏洞，包括：

* **CVE-2024-51977**：通过 HTTP/IPP 服务泄露信息
* **CVE-2024-51980 / CVE-2024-51981**：服务器端请求伪造 （SSRF） 支持网络透视
* **CVE-2024-51982 / CVE-2024-51983**：导致设备崩溃的拒绝服务缺陷
* **CVE-2024-51984**：来自已配置的外部服务（如 LDAP 和 FTP）的密码泄露

根据 Rapid7 的说法，“*691 个模型受到身份验证绕过漏洞 CVE-2024-51978 的影响*”，其他漏洞每个漏洞影响多达 208 个模型。

使这些缺陷特别令人担忧的是它们可通过网络访问进行利用。例如，CVE-2024-51977 可以暴露打印机的序列号，从而启用 CVE-2024-51978 链。即使 CVE-2024-51977 没有被利用：

“未经身份验证的远程攻击者仍然可以通过 PJL 或 SNMP 查询发现目标设备的序列号。”

凭借默认凭据和对网络工具的访问，坚定的攻击者可以利用这些漏洞进行横向移动、数据泄露，甚至更深入地进入企业环境。此外，Rapid7 还发布了这些缺陷的概念验证源代码。

Rapid7 充当 CVE 编号机构 （CNA），并在 13 个月的时间内与 JPCERT/CC 和 Brother 协调披露。已发布固件更新以缓解 8 个漏洞中的 7 个。对于 CVE-2024-51978，Brother 为未来型号提供了解决方法和更新的制造。

建议用户：

* 立即更新固件
* 更改默认管理员凭据
* 查看特定于供应商的公告，了解其他缓解措施

本文翻译自securityonline [原文链接](https://securityonline.info/printer-security-alert-rapid7-uncovers-critical-flaws-cvss-9-8-in-multi-brother-models/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309087](/post/id/309087)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/printer-security-alert-rapid7-uncovers-critical-flaws-cvss-9-8-in-multi-brother-models/)

如若转载,请注明出处： <https://securityonline.info/printer-security-alert-rapid7-uncovers-critical-flaws-cvss-9-8-in-multi-brother-models/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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