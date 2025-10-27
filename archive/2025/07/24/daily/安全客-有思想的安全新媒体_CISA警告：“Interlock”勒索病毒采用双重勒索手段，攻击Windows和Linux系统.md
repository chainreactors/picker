---
title: CISA警告：“Interlock”勒索病毒采用双重勒索手段，攻击Windows和Linux系统
url: https://www.anquanke.com/post/id/310457
source: 安全客-有思想的安全新媒体
date: 2025-07-24
fetch_date: 2025-10-06T23:16:38.381181
---

# CISA警告：“Interlock”勒索病毒采用双重勒索手段，攻击Windows和Linux系统

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

# CISA警告：“Interlock”勒索病毒采用双重勒索手段，攻击Windows和Linux系统

阅读量**77190**

发布时间 : 2025-07-23 17:24:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/interlock-ransomware-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全和基础设施安全局（CISA）、联邦调查局（FBI）、美国卫生与公共服务部（HHS）以及多州信息共享与分析中心（MS-ISAC）发布了紧急联合公告，警告**“Interlock”勒索病毒团伙自2024年9月底以来，针对企业和关键基础设施部门发起的攻击愈加严重**。

新出现的Interlock变种代表着一种特别复杂的威胁，采用了与传统勒索病毒不同的攻击方法，使其与常见的勒索病毒操作有所区别。

与许多网络犯罪团伙不同，Interlock攻击者**通过从受感染的合法网站进行下载攻击（drive-by download）获得初始访问权限**，这是一种在勒索病毒领域较为少见的技术，增加了检测难度。

CISA在今天发布的公告中指出：“Interlock攻击者是机会主义者，具有财务动机，他们根据机会而非特定行业目标来选择攻击对象。”该团伙已成功渗透了北美和欧洲的多个组织，显示出其**广泛的操作范围和适应性**。

### **双重勒索放大威胁**

Interlock的核心策略是使用**双重勒索手段**，攻击者不仅**加密受害者的数据**，还**窃取敏感信息**。这种双重攻击大大增加了组织支付赎金的压力，因为受害者不仅面临操作中断，还面临通过该团伙的暗网泄露网站公开数据的威胁。

该勒索病毒已被观察到同时攻击Windows和Linux操作系统，特别是**针对加密跨平台的虚拟机**。这种跨平台能力使得Interlock对运行混合IT环境的组织尤其危险。

更令人担忧的是，Interlock采用了**ClickFix社交工程技术**，受害者被诱导点击看似解决系统问题的假验证码提示，从而执行恶意负载。这一手段之前与其他恶意软件攻击活动有关，但在勒索病毒传播方式上是一次新进展。

公告中指出：“受害者会收到一个唯一的代码，并被指示通过Tor浏览器上的.onion网址与勒索团伙联系。”

与许多勒索病毒团伙不同，Interlock在其勒索信中没有列出初始赎金要求，而是通过**直接沟通**渠道与受害者进行谈判。

### **Interlock勒索病毒使用的工具**

![]()

### **关键基础设施面临风险**

此次攻击针对**关键基础设施部门**，特别引发了关于潜在服务中断的担忧。联邦调查人员指出，尽管当前的攻击主要集中在加密虚拟机上，但未来可能会扩展到物理服务器和工作站。

为了应对这些威胁，CISA建议组织实施强有力的**端点检测与响应（EDR）功能**，特别是在虚拟机环境中。其他防护措施包括DNS过滤、Web访问防火墙、网络分段以及针对社交工程识别的全面用户培训。

FBI的调查持续进行，最近在2025年6月发现，Interlock与已知的**Rhysida勒索病毒变种**之间存在相似性，暗示这两个团伙可能存在联系或共享技术资源。

此次联合公告是#StopRansomware行动的一部分，旨在为网络防御者提供详细的技术指标和应对策略，以保护自己免受这一新兴威胁的攻击。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/interlock-ransomware-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310457](/post/id/310457)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/interlock-ransomware-attack/)

如若转载,请注明出处： <https://cybersecuritynews.com/interlock-ransomware-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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