---
title: IETF重磅推进AI内容标注标准 全球首个AI生成内容识别规范即将落地
url: https://www.anquanke.com/post/id/311590
source: 安全客-有思想的安全新媒体
date: 2025-08-28
fetch_date: 2025-10-07T00:18:24.000457
---

# IETF重磅推进AI内容标注标准 全球首个AI生成内容识别规范即将落地

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

# IETF重磅推进AI内容标注标准 全球首个AI生成内容识别规范即将落地

阅读量**70868**

发布时间 : 2025-08-27 18:26:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/a-new-ai-header-the-ietf-is-building-a-standard-to-label-ai-generated-content/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

为应对AI生成内容的日益普及，互联网工程任务组（IETF）近日推出新草案提案，旨在通过Web响应头声明特定内容是否由人工智能创建。该提案采用兼容HTTP结构化字段语法的标头设计，可向**用户代理、AI爬虫和互联网档案馆**等系统提供元数据，这些系统可根据自身需求决定是否采用AI生成内容。

目前多数AI生成内容仍存在质量低下和事实性错误问题，模型经常产生”幻觉”甚至完全虚构信息。例如AI用户代理从网络获取内容生成响应时，若源材料本身来自AI模型且包含错误信息，将导致生成结果不可靠。互联网档案馆等存储系统也可能选择不保存此类内容——由于AI生成内容易大规模生产且可能不准确，排除此类内容可减轻存储和爬取压力。

根据提案，发布AI生成内容的网站可在响应头中添加声明。当AI代理或爬虫检测到该声明时，可识别内容的人工智能来源并选择忽略，从而避免错误传播。拟议的**AI-Disclosure标头**可包含生成模式、模型名称、提供商、审核团队、时间戳等标识细节，帮助自动化系统快速评估来源。

需要强调的是，该AI-Disclosure标头**完全基于自愿原则**：网站可自行选择是否设置。设置标头表明内容为AI生成，但未设置标头并不保证内容由人类创建。目前该提案仍处于草案阶段（有效期至2025年11月1日），若后续行业讨论无异议，预计将形成正式标准——届时所有网站均可选择采用此AI标注标头。

本文翻译自securityonline [原文链接](https://securityonline.info/a-new-ai-header-the-ietf-is-building-a-standard-to-label-ai-generated-content/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311590](/post/id/311590)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/a-new-ai-header-the-ietf-is-building-a-standard-to-label-ai-generated-content/)

如若转载,请注明出处： <https://securityonline.info/a-new-ai-header-the-ietf-is-building-a-standard-to-label-ai-generated-content/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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