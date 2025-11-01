---
title: Magecart团伙“剑齿虎”刷卡器通过恶意插件渗透WooCommerce，并将其有效载荷隐藏在伪造的PNG图片中
url: https://www.anquanke.com/post/id/312947
source: 安全客-有思想的安全新媒体
date: 2025-10-31
fetch_date: 2025-11-01T03:08:33.426055
---

# Magecart团伙“剑齿虎”刷卡器通过恶意插件渗透WooCommerce，并将其有效载荷隐藏在伪造的PNG图片中

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

# Magecart团伙“剑齿虎”刷卡器通过恶意插件渗透WooCommerce，并将其有效载荷隐藏在伪造的PNG图片中

阅读量**21390**

发布时间 : 2025-10-31 17:44:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/magecart-smilodon-skimmer-infiltrates-woocommerce-via-rogue-plugin-hiding-payload-in-fake-png-image/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Wordfence威胁情报团队发现了一场针对使用WooCommerce插件的WordPress电商网站的**高度复杂恶意软件攻击活动**。攻击者部署恶意插件，将恶意载荷隐藏在伪造图像中，通过自定义加密规避检测，并维持远程命令访问以实现持久化利用。

根据Wordfence研究人员的报告：“此恶意软件展现出高级特性，包括**自定义加密方法**、用于隐藏恶意载荷的**伪造图像**、允许攻击者按需部署额外代码的**强健持久化层**，所有功能均打包为一个恶意WordPress插件。”

该恶意插件伪装成类似合法工具的名称，例如“jwt-log-pro”“cron-environment-advanced”和“share-seo-assistant”。

每个样本包含两个PHP文件和两个PNG图像（其中一个为诱饵）。所有函数名、变量甚至文本字符串均经过**随机生成和混淆处理**。

插件**静默激活**，“从WordPress插件列表和表格视图中隐藏其条目，以最大程度降低被检测风险。”它还会记录所有拥有作者及以上权限的用户，设置持久化跟踪Cookie（pxcelPage\_c01002），使恶意软件能够识别返回的管理员并向其隐藏恶意代码——这一规避策略旨在让网站看起来正常运行。

Wordfence发现，恶意软件通过**两阶段流程拦截登录凭证**：首先将凭证存储在Cookie中，然后在成功登录事件后泄露数据。

“当用户输入用户名和密码时，它会将信息存储在Cookie中，然后等待实际登录操作以泄露数据。”报告解释道。

凭证被发送至攻击者的命令服务器hxxps://badping[.]info/SMILODON/index\_b.php?view= ，并经过**编码和混淆处理以伪装流量**。

一个隐藏的基于AJAX的后门使攻击者能够注入或更新恶意JavaScript载荷，甚至**远程执行任意PHP代码**。

Wordfence指出：“恶意软件使用两个 distinct 基于AJAX的访问端点建立后门，均采用基于Cookie的身份验证方法，**绕过WordPress原生身份验证**。”

其中一个端点允许动态更新窃取器载荷，另一个通过临时文件执行任意PHP代码——实际上授予了对受感染系统的**完全远程控制权**。

### **伪造图像隐藏载荷与多阶段窃取器**

该攻击活动最具欺骗性的手段之一是，恶意软件将其JavaScript窃取载荷存储在**伪造的PNG图像文件**中。这些文件模仿合法网站资源，但在伪造的PNG头部（‰PNG）后包含**反转和自定义Base64编码的代码**。

“共使用三种不同的伪造图像文件——自定义载荷、每日更新主表单劫持逻辑的动态载荷，以及包含相同逻辑静态备份副本的备用载荷。”

这种多层载荷结构确保即使一个文件被移除或损坏，窃取器仍能继续运行。JavaScript被注入WooCommerce结账页面，**休眠至客户输入信用卡数据时激活**。

JavaScript窃取器在页面加载三秒后激活，以避免干扰AJAX驱动的结账表单。它甚至包含**伪造验证系统**，让用户误以为其卡数据正在被安全处理。

捕获的数据（包括卡号、有效期和CVV）通过AJAX POST请求发送回受感染网站，随后泄露至外部服务器（如hxxps://geterror[.]info/SMILODON/index.php?view= ）。

Wordfence将此操作归因于**Magecart第12组**——最顽固的信用卡窃取团伙之一。

“证据强烈表明，两个C&C服务器URL中发现的‘SMILODON’字符串与Magecart第12组威胁行为者相关联。”报告称，并引用了自2021年以来观察到的共享基础设施和代码模式。

研究人员还注意到，“两个域名与该团伙过去的钓鱼和窃取操作相关的其他域名共同托管在IP地址121.127.33[.]229上。”

本文翻译自securityonline [原文链接](https://securityonline.info/magecart-smilodon-skimmer-infiltrates-woocommerce-via-rogue-plugin-hiding-payload-in-fake-png-image/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312947](/post/id/312947)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/magecart-smilodon-skimmer-infiltrates-woocommerce-via-rogue-plugin-hiding-payload-in-fake-png-image/)

如若转载,请注明出处： <https://securityonline.info/magecart-smilodon-skimmer-infiltrates-woocommerce-via-rogue-plugin-hiding-payload-in-fake-png-image/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

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
* **641**

* 粉丝
* **6**

### TA的文章

* ##### [Magecart团伙“剑齿虎”刷卡器通过恶意插件渗透WooCommerce，并将其有效载荷隐藏在伪造的PNG图片中](/post/id/312947)

  2025-10-31 17:44:46
* ##### [安全威胁“幻影乌鸦”被披露：126个恶意npm包通过隐藏依赖项窃取开发者令牌与敏感信息](/post/id/312950)

  2025-10-31 17:44:25
* ##### [攻击组织实施网络间谍活动：Airstalk恶意软件劫持VMware AirWatch MDM API以构建隐秘C2信道](/post/id/312953)

  2025-10-31 17:43:54
* ##### [Progress公司为其MOVEit Transfer的AS2模块发布补丁，修复高危漏洞 (CVE-2025-10932)](/post/id/312957)

  2025-10-31 17:42:55
* ##### [身份安全公司ConductorOne完成7900万美元融资，致力于革新现代化身份安全管理方案](/post/id/312961)

  2025-10-31 17:42:27

### 相关文章

* ##### [安全威胁“幻影乌鸦”被披露：126个恶意npm包通过隐藏依赖项窃取开发者令牌与敏感信息](/post/id/312950)

  2025-10-31 17:44:25
* ##### [攻击组织实施网络间谍活动：Airstalk恶意软件劫持VMware AirWatch MDM API以构建隐秘C2信道](/post/id/312953)

  2025-10-31 17:43:54
* ##### [Progress公司为其MOVEit Transfer的AS2模块发布补丁，修复高危漏洞 (CVE-2025-10932)](/post/id/312957)

  2025-10-31 17:42:55
* ##### [身份安全公司ConductorOne完成7900万美元融资，致力于革新现代化身份安全管理方案](/post/id/312961)

  2025-10-31 17:42:27
* ##### [OpenAI官方证实：GPT-5处理心理与情感困扰的能力已获显著优化](/post/id/312964)

  2025-10-31 17:42:05
* ##### [Chromium内核浏览器Blink渲染引擎中存在高危漏洞，可致攻击者在数秒内引发浏览器崩溃](/post/id/312968)

  2025-10-31 17:40:59
* ##### [360助力石家庄市教育行业网络安全运营中心启航，共筑教育安全新防线](/post/id/312971)

  2025-10-31 17:39:50

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