---
title: WordPress插件漏洞允许攻击者通过社交登录绕过身份验证
url: https://www.anquanke.com/post/id/312192
source: 安全客-有思想的安全新媒体
date: 2025-09-18
fetch_date: 2025-10-02T20:17:22.359192
---

# WordPress插件漏洞允许攻击者通过社交登录绕过身份验证

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

# WordPress插件漏洞允许攻击者通过社交登录绕过身份验证

阅读量**79823**

发布时间 : 2025-09-17 17:37:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/wordpress-plugin-vulnerability-3/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Case Theme User WordPress插件中存在一个严重的身份验证绕过漏洞，已成为重大安全威胁——未经身份验证的攻击者可利用**社交登录功能**获取网站管理员权限。

该漏洞编号为**CVE-2025-5821**，CVSS评分**9.8**，影响所有版本至1.0.3的插件，全球约**12,000个活跃安装实例**受影响。安全缺陷使攻击者能够完全绕过身份验证机制，在已知或可获取目标邮箱地址的情况下，未授权访问任何用户账户，包括**管理员级权限**。

此漏洞的危险性在于其**利用门槛极低**：攻击者无需复杂工具或专业知识，通过简单HTTP请求即可发起攻击。2025年8月22日漏洞公开披露后，次日便出现活跃利用，Wordfence分析师通过漏洞赏金计划发现该漏洞，并指出其防火墙已拦截**超20,900次**针对此漏洞的攻击尝试。漏洞的快速利用表明，它对寻求快速入侵WordPress站点的网络犯罪分子具有极强吸引力。

该插件捆绑于多个**付费主题**中，导致攻击面远超独立安装场景。攻击者被观察到通过常见模式（如admin@domain.com 、owner@domain.com ）猜测管理员邮箱，显示其针对多个目标的系统性攻击策略。

### **漏洞机制与代码分析**

漏洞源于Case\_Theme\_User\_Ajax类中**facebook\_ajax\_login\_callback()函数的逻辑缺陷**。该函数处理社交登录请求时，会根据提供的邮箱地址创建用户账户，但在授予访问权限前**未正确验证身份验证状态**。

![]()

**利用流程**（来源：Wordfence）分为两个阶段：

1. **注册临时账户**：攻击者向/wp-admin/admin-ajax.php 发送POST请求（action参数设为facebook\_ajax\_login），使用自身邮箱注册临时账户。恶意载荷包含伪造的Facebook用户数据（如data[name]=temp、data[email]=temp@attacker.com ），创建合法用户会话。
2. **会话权限转移**：攻击者利用已建立的会话，提交包含临时用户名但替换为受害者邮箱的请求。由于漏洞代码仅通过邮箱检索用户，未验证原始身份验证令牌，导致会话权限被转移至目标账户。

### **修复与防御建议**

1.0.4版本补丁通过在授予访问权限前实施**严格的身份验证验证**，修复了该逻辑缺陷。网站管理员应立即更新至最新版本，并审查访问日志中来自已知恶意IP（如2602:ffc8:2:105:216:3cff:fe96:129f、146.70.186.142）的可疑AJAX请求。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/wordpress-plugin-vulnerability-3/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312192](/post/id/312192)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/wordpress-plugin-vulnerability-3/)

如若转载,请注明出处： <https://cybersecuritynews.com/wordpress-plugin-vulnerability-3/>

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