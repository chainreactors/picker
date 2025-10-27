---
title: Angular SSR漏洞允许攻击者访问敏感数据
url: https://www.anquanke.com/post/id/312100
source: 安全客-有思想的安全新媒体
date: 2025-09-13
fetch_date: 2025-10-02T20:04:23.804711
---

# Angular SSR漏洞允许攻击者访问敏感数据

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

# Angular SSR漏洞允许攻击者访问敏感数据

阅读量**57126**

发布时间 : 2025-09-12 17:34:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/angular-ssr-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Angular的服务器端渲染（SSR）实现中发现一个严重漏洞，可能导致攻击者访问敏感用户数据。该漏洞源于Angular处理并发请求的方式，可能造成一个用户会话的数据泄露给另一个用户。

Angular团队已为所有活跃支持版本发布补丁，修复了这一问题。漏洞影响使用`@angular/platform-server`、`@angular/ssr`和`@nguniversal/common`的应用。

### **漏洞原理：依赖注入容器的竞争条件**

问题核心在于Angular SSR过程中，依赖注入（DI）容器（称为“平台注入器”）存在**竞争条件**。该注入器负责存储请求特定信息，但被错误地作为JavaScript模块作用域的全局变量存储。

这种设计意味着当服务器同时处理多个请求时，可能意外共享或覆盖全局注入器的状态，导致不同会话间的数据污染。

在实际场景中，此漏洞可能导致应用向一个用户返回包含另一用户数据的页面，泄露渲染页面中或响应头中的敏感信息（如身份验证令牌）。攻击者只需通过网络发送大量请求并检查响应，即可从其他用户的活跃会话中提取泄露数据。由于无需特权位置，任何触发渲染响应的流量都可能被利用，因此风险尤为突出。

多个API（包括`bootstrapApplication`、`getPlatform`和`destroyPlatform`）因依赖共享状态而被确认存在漏洞。

### **修复与缓解措施**

Angular团队已为所有活跃版本（18、19、20及v21预发布版）发布补丁。修复引入了必要的**破坏性变更**，尤其是`bootstrapApplication`函数——在服务器环境中需显式传入上下文，避免隐式状态共享。

为简化更新流程，Angular提供了自动 schematic 工具处理代码修改。开发者需通过运行对应版本的`ng update`命令升级应用。

对于无法立即应用补丁的情况，可采用临时缓解方案：**禁用SSR**、移除自定义引导函数中的异步行为，或确保服务器构建显式禁用Angular的“JIT”模式。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/angular-ssr-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312100](/post/id/312100)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/angular-ssr-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/angular-ssr-vulnerability/>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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