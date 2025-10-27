---
title: Apache CloudStack 在最新版本中修补了重大安全漏洞
url: https://www.anquanke.com/post/id/300978
source: 安全客-有思想的安全新媒体
date: 2024-10-18
fetch_date: 2025-10-06T18:50:04.918105
---

# Apache CloudStack 在最新版本中修补了重大安全漏洞

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

# Apache CloudStack 在最新版本中修补了重大安全漏洞

阅读量**61742**

发布时间 : 2024-10-17 10:26:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/apache-cloudstack-patches-critical-security-flaws-in-latest-release/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-45219 - CVE-2024-45693]()

Apache CloudStack 项目宣布发布 LTS 安全版本 4.18.2.4 和 4.19.1.2，以解决四个安全漏洞，其中两个被评为 “重要”。CloudStack 是一个流行的开源平台，用于构建和管理基础设施即服务（IaaS）云。

最严重的漏洞 CVE-2024-45219 可让攻击者控制基于 KVM 的基础架构。该公告警告说：“上传和注册的模板和卷可用于滥用基于 KVM 的基础架构。该漏洞源于验证检查的缺失，使攻击者能够部署恶意实例或附加受攻击的卷，从而访问主机文件系统。”

该项目解释说：“这可能导致由 CloudStack 管理的基于 KVM 的基础架构的资源完整性和保密性受损、数据丢失、拒绝服务和可用性。”

另一个 “重要 ”缺陷（CVE-2024-45693）涉及请求来源验证绕过，可能导致账户接管。攻击者可以诱骗登录用户提交恶意请求，从而可能允许访问敏感数据和控制用户的资源。

此外，还修补了两个 “中等 ”严重性漏洞：

* CVE-2024-45461： 配额功能中未执行访问检查，可能允许未经授权修改配额配置。
* CVE-2024-45462：网络界面注销时会话失效不彻底，如果用户的浏览器会话仍处于活动状态，则可能导致未经授权的访问。

**缓解措施**

Apache CloudStack 项目强烈建议用户升级到 4.18.2.4 或 4.19.1.2 版本，以缓解这些漏洞。该公告还详细说明了如何扫描和验证模板和卷，以确保它们不会受到攻击。

“此外，还可以扫描所有用户上传或注册的 KVM 兼容模板和卷，并检查它们是否为平面文件，是否使用了任何额外或不必要的功能”，该公告称，“此外，还可以扫描所有用户上传或注册的 KVM 兼容模板和卷，并检查它们是否为平面文件，是否使用了任何额外或不必要的功能。”

本文翻译自securityonline [原文链接](https://securityonline.info/apache-cloudstack-patches-critical-security-flaws-in-latest-release/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300978](/post/id/300978)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/apache-cloudstack-patches-critical-security-flaws-in-latest-release/)

如若转载,请注明出处： <https://securityonline.info/apache-cloudstack-patches-critical-security-flaws-in-latest-release/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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