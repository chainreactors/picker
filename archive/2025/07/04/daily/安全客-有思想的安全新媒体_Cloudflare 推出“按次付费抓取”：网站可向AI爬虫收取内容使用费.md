---
title: Cloudflare 推出“按次付费抓取”：网站可向AI爬虫收取内容使用费
url: https://www.anquanke.com/post/id/309357
source: 安全客-有思想的安全新媒体
date: 2025-07-04
fetch_date: 2025-10-06T23:29:03.849548
---

# Cloudflare 推出“按次付费抓取”：网站可向AI爬虫收取内容使用费

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

# Cloudflare 推出“按次付费抓取”：网站可向AI爬虫收取内容使用费

阅读量**58417**

发布时间 : 2025-07-03 14:56:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/cloudflare-launches-pay-per-crawl-websites-can-now-charge-ai-crawlers-for-content/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

互联网服务提供商 Cloudflare 近日正式推出一项全新功能，旨在解决 AI 公司**未经授权抓取网站内容**的问题。该功能允许网站及内容发布者**向AI公司收取费用，以换取内容访问授权**。

目前，该功能正与部分指定网站进行试点测试。感兴趣的内容方需**手动提交申请**，经审核通过后，即可启用该功能并进行如下配置：是否完全屏蔽AI爬虫、是否设置访问费用、允许抓取的内容范围等。

具体而言：

* 网站或内容提供方可选择**全面屏蔽AI爬虫**、**只允许特定爬虫访问**、**设置付费访问机制**，或**开放内容供其免费抓取**。
* AI 公司则可根据查询量注册抓取请求、审查定价策略，并决定是否接受付费或拒绝访问，从而通过**正式机制获取优质内容**。

目前 Cloudflare 尚未披露统一的“内容抓取定价标准”。考虑到各网站内容价值差异较大，未来版本预计将允许发布方**自定义定价模型**，例如按篇收费等。

该功能仅适用于启用了 Cloudflare“橙云”防护的网站。一旦启用，所有流量都将通过 Cloudflare 网络转发，其可借助**专有爬虫识别数据库**对不同爬虫请求进行识别与管理。

启用“付费抓取”功能后，AI爬虫访问网站内容时，如获授权，将返回标准 HTTP 200 响应码；若返回 HTTP 402 Payment Required 状态码，则表示该内容需付费访问。

AI公司可通过解析这些HTTP响应码来判断目标网站的访问策略，若接受付费条款，需通过Cloudflare的“付费抓取”项目注册，注册成功后，即可**按约定条款访问内容**。

Cloudflare 已确认**多家AI公司已加入该付费接入计划**。不过，合作是否达成，仍取决于内容提供方设定的定价是否被AI公司接受。若发布方报价过高，AI方可选择**拒绝合作，终止抓取行为**。

本文翻译自securityonline [原文链接](https://securityonline.info/cloudflare-launches-pay-per-crawl-websites-can-now-charge-ai-crawlers-for-content/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309357](/post/id/309357)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/cloudflare-launches-pay-per-crawl-websites-can-now-charge-ai-crawlers-for-content/)

如若转载,请注明出处： <https://securityonline.info/cloudflare-launches-pay-per-crawl-websites-can-now-charge-ai-crawlers-for-content/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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