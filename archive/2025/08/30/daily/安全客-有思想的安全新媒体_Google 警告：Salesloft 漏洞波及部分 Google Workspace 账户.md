---
title: Google 警告：Salesloft 漏洞波及部分 Google Workspace 账户
url: https://www.anquanke.com/post/id/311697
source: 安全客-有思想的安全新媒体
date: 2025-08-30
fetch_date: 2025-10-07T00:17:50.569988
---

# Google 警告：Salesloft 漏洞波及部分 Google Workspace 账户

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

# Google 警告：Salesloft 漏洞波及部分 Google Workspace 账户

阅读量**85343**

发布时间 : 2025-08-29 16:13:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/google-warns-salesloft-breach-impacted-some-workspace-accounts/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Google 最新通报显示，Salesloft Drift 平台遭遇的入侵事件比最初披露的范围更大。攻击者除了窃取 Salesforce 实例中的数据外，还利用被盗的 OAuth 令牌访问了少量 Google Workspace 邮箱账户。

Google 表示：“根据 GTIG（Google 威胁情报组）掌握的新信息，此次入侵的范围不仅局限于 Salesloft Drift 与 Salesforce 的集成，还影响到其他集成场景。**我们建议所有 Salesloft Drift 用户，将存储在该平台或与之连接的所有认证令牌都视为可能已被攻破。”**

这起攻击活动由 Google 威胁情报（Mandiant）跟踪，编号为 UNC6395。事件最初于 8 月 26 日曝光，当时攻击者窃取了 Salesloft Drift AI 聊天集成的 OAuth 令牌，并借此访问了客户的 Salesforce 实例，在其中针对 Cases、Accounts、Users、Opportunities 等对象执行查询。

通过这些查询，攻击者得以扫描客户支持工单和消息，从中寻找敏感信息，例如 AWS 访问密钥、Snowflake 令牌以及密码等。**这些信息可能被用于进一步攻破云端账户，为未来的勒索或数据窃取铺路。**

在最新更新中，Google 确认此次入侵事件影响范围超出最初认知，不仅限于 Salesforce 集成。调查显示，“Drift Email” 集成所使用的 OAuth 令牌同样遭到泄露。攻击者在 8 月 9 日利用这些令牌，访问了极少量与 Drift 直接集成的 Google Workspace 邮箱账户。

Google 强调，除受影响的账户外，相关域名中的其他账户均未受到波及，Google Workspace 及 Alphabet 自身并未遭到入侵。

目前，**被盗令牌已全部吊销，相关客户也已收到通知**。Google 同时暂停了 Salesloft Drift Email 与 Google Workspace 的集成，以便进一步调查。

Google 现敦促所有使用 Drift 的组织采取以下措施：

1.将存储在 Drift 平台上的所有认证令牌视为已泄露；

2.立即吊销并轮换相关应用的凭证；

3.检查所有连接系统是否存在未授权访问痕迹；

4.审查所有与 Drift 相关的第三方集成；

5.搜索可能暴露的密钥，并及时重置。

Salesloft 在 8 月 28 日也更新了公告，称 Salesforce 已暂停与 Drift、Slack、Pardot 的相关集成，直至调查结束。

目前，Salesloft 已聘请 Mandiant 和 Coalition 协助调查此次事件。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/google-warns-salesloft-breach-impacted-some-workspace-accounts/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311697](/post/id/311697)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/google-warns-salesloft-breach-impacted-some-workspace-accounts/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/google-warns-salesloft-breach-impacted-some-workspace-accounts/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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