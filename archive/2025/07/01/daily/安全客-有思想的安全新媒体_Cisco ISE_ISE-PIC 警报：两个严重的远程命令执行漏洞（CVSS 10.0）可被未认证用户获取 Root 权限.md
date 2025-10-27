---
title: Cisco ISE/ISE-PIC 警报：两个严重的远程命令执行漏洞（CVSS 10.0）可被未认证用户获取 Root 权限
url: https://www.anquanke.com/post/id/309163
source: 安全客-有思想的安全新媒体
date: 2025-07-01
fetch_date: 2025-10-06T23:50:38.830842
---

# Cisco ISE/ISE-PIC 警报：两个严重的远程命令执行漏洞（CVSS 10.0）可被未认证用户获取 Root 权限

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

# Cisco ISE/ISE-PIC 警报：两个严重的远程命令执行漏洞（CVSS 10.0）可被未认证用户获取 Root 权限

阅读量**60815**

发布时间 : 2025-06-30 18:19:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/cisco-ise-ise-pic-alert-two-critical-rce-flaws-cvss-10-0-allow-unauthenticated-root-access/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

思科在其身份服务引擎 （ISE） 和被动身份连接器 （ISE-PIC） 中披露了两个关键漏洞，这些漏洞可能允许未经身份验证的远程攻击者以 root 权限执行任意命令。这些漏洞（CVE-2025-20281 和 CVE-2025-20282）的 CVSS 评分最高为 10.0，凸显了其严重性。

第一个漏洞 CVE-2025-20281 会影响思科 ISE 和 ISE-PIC 版本 3.3 及更高版本。它源于特定 API 终端中的输入验证不足。由于此漏洞，攻击者可以通过向受影响的系统提交构建的 API 请求来利用该漏洞。至关重要的是，攻击者不需要有效的凭证即可执行此作。

根据公告：

> “思科 ISE 和思科 ISE-PIC 的特定 API 中存在一个漏洞，可能允许未经身份验证的远程攻击者以 root 身份在底层作系统上执行任意代码。”

成功利用此漏洞的结果是系统完全受损，从而允许以 root 用户身份执行任意命令。Cisco 已在 ISE 3.3 补丁 6 中解决了此问题，除了修补之外，没有缓解漏洞的解决方法。

第二个漏洞 CVE-2025-20282 是思科 ISE 和 ISE-PIC 版本 3.4 独有的漏洞。它驻留在内部 API 中，该 API 缺乏对上传文件的充分验证。这种疏忽允许攻击者将任意文件上传到系统上的特权目录，然后可以使用 root 权限执行这些文件。

Cisco 的咨询报告解释说：

> “成功利用此漏洞可能允许攻击者在受影响的系统上存储恶意文件，然后执行任意代码或获得系统的 root 权限。”

与第一个漏洞一样，利用该漏洞不需要用户身份验证，除了应用 Cisco 的 Patch 2 for version 3.4 之外，没有其他解决方法。CVE-2025-20281 和 CVE-2025-20282 的补丁均可通过 Cisco 的支持渠道和软件存储库获得。

截至发布时，Cisco 的产品安全事件响应团队 （PSIRT） 尚未观察到任何公开的漏洞利用。

尽管如此，鉴于这些缺陷的未经身份验证的性质和根级影响，未来被利用的风险很高。强烈建议组织立即应用相关补丁。

本文翻译自securityonline [原文链接](https://securityonline.info/cisco-ise-ise-pic-alert-two-critical-rce-flaws-cvss-10-0-allow-unauthenticated-root-access/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309163](/post/id/309163)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/cisco-ise-ise-pic-alert-two-critical-rce-flaws-cvss-10-0-allow-unauthenticated-root-access/)

如若转载,请注明出处： <https://securityonline.info/cisco-ise-ise-pic-alert-two-critical-rce-flaws-cvss-10-0-allow-unauthenticated-root-access/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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