---
title: ChatGPT遭诱导泄露Windows家庭版、专业版及企业版密钥
url: https://www.anquanke.com/post/id/309931
source: 安全客-有思想的安全新媒体
date: 2025-07-12
fetch_date: 2025-10-06T23:16:48.023576
---

# ChatGPT遭诱导泄露Windows家庭版、专业版及企业版密钥

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

# ChatGPT遭诱导泄露Windows家庭版、专业版及企业版密钥

阅读量**69759**

发布时间 : 2025-07-11 16:12:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/researchers-trick-chatgpt/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种复杂的“越狱”技术绕过了ChatGPT的防护机制，通过巧妙伪装的猜谜游戏诱导该人工智能**泄露有效的Windows产品密钥**。这一突破暴露了当前人工智能内容**审核系统**存在的严重漏洞，也引发了人们对防护机制抵御社会工程学攻击能力的担忧。

#### ****核心要点****

1. 研究人员通过将获取Windows产品密钥的请求伪装成无害的猜谜游戏，绕过了ChatGPT的防护机制。
2. 攻击中可能使用HTML标签（<ahref=x></a>）隐藏敏感词汇，避开关键词过滤，同时不影响人工智能的理解。
3. 利用游戏规则、提示信息及“我放弃”这一触发短语，成功提取到真实的Windows家庭版/专业版/企业版密钥。
4. 该漏洞同样适用于其他受限制内容，暴露出基于关键词的过滤方式相较于上下文理解存在的缺陷。

##### ****防护机制绕过技术****

0din机构报告称，这种攻击利用了人工智能模型在**处理上下文信息和执行内容限制方面**的根本性弱点。

防护机制是旨在**防止人工智能系统共享序列号、产品密钥和机密数据等敏感信息**的保护机制。0din的研究人员发现，通过**战略性的框架构建和模糊处理技术**，这些防护措施可以被规避。其核心方法是将交互过程伪装成**无害的猜谜游戏**，而非直接请求敏感信息。通过制定迫使人工智能参与并如实回应的游戏规则，研究人员成功掩盖了真实意图。关键突破在于采用HTML标签模糊处理技术，将“Windows10序列号”等敏感词汇**嵌入HTML锚点标签**中，以**避开内容过滤器的检测**。

攻击过程分为三个不同阶段：**制定游戏规则、请求提示信息、通过“我放弃”短语触发信息泄露**。这种系统性方法利用了人工智能的逻辑流程，使其误认为信息披露是**正当游戏环节的一部分**，而非安全漏洞。

![]()

![]()

*聊天互动导致密钥泄露*

研究人员采用精心设计的提示词和代码生成技术，制定了一套系统方法。主要提示词构建了**游戏框架**：

![]()

这段代码展示了HTML模糊处理技术，**敏感词汇中的空格被替换为空HTML锚点标签（<ahref=x></a>）**。

这种方法成功避开了基于关键词的过滤系统，同时保留了人工智能模型能够理解的语义。

攻击中使用的是公共论坛上常见的**临时密钥**，包括Windows家庭版、专业版和企业版密钥。

![]()

人工智能对这些公开已知密钥的熟悉度可能助长了此次绕过行为，因为系统未能在游戏场景中识别出这些密钥的敏感性。

##### ****缓解策略****

该漏洞的影响不仅限于Windows产品密钥，还可能涉及其他受限制内容，包括**个人身份信息、恶意网址和成人内容**等。这一技术暴露了当前防护机制架构存在的根本性缺陷——**过度依赖关键词过滤，而缺乏上下文理解能力**。

有效的缓解措施需要**多层次方案**，包括增强上下文感知系统、能检测欺骗性框架模式的逻辑级防护，以及强大的社会工程学攻击检测机制。人工智能开发者必须实施全面的验证系统，能够识别各种表现形式的操纵企图，确保对复杂的提示词注入技术具备更强的抵御能力。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/researchers-trick-chatgpt/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309931](/post/id/309931)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/researchers-trick-chatgpt/)

如若转载,请注明出处： <https://cybersecuritynews.com/researchers-trick-chatgpt/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

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