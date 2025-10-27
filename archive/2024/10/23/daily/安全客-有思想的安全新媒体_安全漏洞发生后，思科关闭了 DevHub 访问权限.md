---
title: 安全漏洞发生后，思科关闭了 DevHub 访问权限
url: https://www.anquanke.com/post/id/301129
source: 安全客-有思想的安全新媒体
date: 2024-10-23
fetch_date: 2025-10-06T18:48:32.008965
---

# 安全漏洞发生后，思科关闭了 DevHub 访问权限

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

# 安全漏洞发生后，思科关闭了 DevHub 访问权限

阅读量**63204**

发布时间 : 2024-10-22 10:45:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：darkreading

原文地址：<https://www.darkreading.com/cloud-security/cisco-disables-access-devhub-site-security-breach>

译文仅供参考，具体内容表达以及含义原文为准。

![The Cisco logo]()

思科已禁止公众访问其 DevHub 环境之一，因为威胁行为者从该网站下载了一些客户数据，并在一个网络犯罪论坛上出售。

被泄露的数据包括源代码、API 标记、硬编码凭证、证书和其他属于一些大公司的机密，包括微软、Verizon、T-Mobile、AT&T、巴克莱银行和 SAP。

**面向公众环境的数据盗窃**

一周前，当研究人员发现三个使用 IntelBroker、EnergyWeaponUser 和 zjj 的威胁行为者在 BreachForums 上出售数据时，泄露的消息首次浮出水面。IntelBroker 是一个已知的塞尔维亚实体，于 2022 年开始运营，与几起重大数据盗窃案有关，其中包括欧洲刑警组织、通用电气和 DARPA（美国国防部高级研究计划局）的数据盗窃案。

思科公司于 10 月 15 日宣布正在调查这一事件。三天后，该公司在一次更新中确认了这起安全事件，但对攻击者设法访问和下载的数据种类没有提供多少细节。

思科公司自己的系统似乎没有受到此次事件的影响。“思科的公告指出：”我们已经确定，相关数据位于面向公众的 DevHub 环境中，这是思科的一个资源中心，通过提供软件代码、脚本等供客户根据需要使用，为我们的社区提供支持。“在现阶段的调查中，我们已经确定可能发布了少量未授权公开下载的文件”。

该公司表示，目前没有证据表明攻击者非法访问了任何个人身份数据或财务信息，但它补充说，它仍在调查这种可能性。“该公司表示：”出于谨慎起见，在继续调查的同时，我们已禁止公众访问该网站。

在他们的 BreachForums 帖子中，威胁者声称他们从思科 DevHub 站点下载的数据包括 GitHub 和 GitLab 项目、源代码、Jira 票据、容器镜像、AWS 存储桶中的数据，以及至少一些机密的思科信息。

**提醒： 确保面向公众资产安全的必要性**

Sectigo 高级研究员 Jason Soroko 说：”思科事件提醒我们，为什么企业需要采取输入验证等措施保护面向公众的环境，以防止注入攻击、强大的身份验证工具和流程，以及定期进行漏洞评估。

Soroko说：”在确保面向公众的资产安全方面，企业常犯的错误包括忽视OWASP指南、低估安全风险、没有定期更新系统以及没有优先考虑安全编码实践。恶意软件检测工具可以方便地进行定期扫描。

他补充说，企业有时会倾向于认为面向公众的资产不那么重要，而实际上，这些资产可能会暴露敏感信息，攻击者可能会利用这些信息进行未来的入侵。例如，攻击者在思科事件中获得的数据包括源代码、API 标记、证书和凭证，攻击者有可能在未来的活动中大量利用这些数据。

Salt Security 公司网络安全战略总监埃里克-施瓦克（Eric Schwake）说，导致敏感数据最终出现在企业面向公众的环境中的因素有很多。“他说：”这可能是由于访问控制的意外错误配置、代码或文件管理中的人为错误、部署前的安全测试不充分或第三方服务受到损害。这些疏忽可能会导致敏感数据的暴露，并为攻击者创造潜在的切入点。

Schwake 建议企业实施多层次的安全策略来降低这种风险。他说：“这包括实施严格的访问控制、推广安全编码实践、进行彻底的安全测试、建立态势治理标准以及定期进行安全评估。使用保密管理解决方案和持续监控工具可以进一步提高安全性，防止未经授权访问敏感信息。”

本文翻译自darkreading [原文链接](https://www.darkreading.com/cloud-security/cisco-disables-access-devhub-site-security-breach)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301129](/post/id/301129)

安全KER - 有思想的安全新媒体

本文转载自: [darkreading](https://www.darkreading.com/cloud-security/cisco-disables-access-devhub-site-security-breach)

如若转载,请注明出处： <https://www.darkreading.com/cloud-security/cisco-disables-access-devhub-site-security-breach>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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