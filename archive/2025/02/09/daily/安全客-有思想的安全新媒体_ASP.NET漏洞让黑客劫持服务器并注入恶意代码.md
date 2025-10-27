---
title: ASP.NET漏洞让黑客劫持服务器并注入恶意代码
url: https://www.anquanke.com/post/id/303978
source: 安全客-有思想的安全新媒体
date: 2025-02-09
fetch_date: 2025-10-06T20:33:26.564666
---

# ASP.NET漏洞让黑客劫持服务器并注入恶意代码

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

# ASP.NET漏洞让黑客劫持服务器并注入恶意代码

阅读量**679300**

发布时间 : 2025-02-08 14:42:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/asp-net-vulnerability-hackers-servers-inject-malicious-code/>

译文仅供参考，具体内容表达以及含义原文为准。

微软的网络安全专家发现了一个影响[ASP.NET](https://asp.net/)应用程序的漏洞，致使数千台 Web 服务器面临风险。该问题源于开发人员在配置中使用了公开可用的[ASP.NET](https://asp.net/)机器密钥，而黑客如今正利用这些密钥实施 ViewState 代码注入攻击。

2024 年 12 月的一次近期攻击就利用了这一漏洞来部署 “哥斯拉”（Godzilla），这是一个危险的后渗透框架，能够执行命令、注入壳代码，并持续保持对受攻击服务器的访问权限。微软警告称，超过 3000 个公开披露的机器密钥可能会被用于类似攻击。

为何此事至关重要

[ASP.NET](https://asp.net/)机器密钥旨在通过对 ViewState 数据进行加密和验证来保护 Web 应用程序，确保攻击者无法篡改数据。然而，一些开发人员错误地从在线资源复制了这些密钥，在不知不觉中让黑客能够生成恶意的 ViewState 数据并注入到他们的服务器中。

一旦黑客获取了正确的机器密钥，他们就可以精心构造恶意负载，并将其发送到存在漏洞的网站。服务器信任该密钥，会解密并执行攻击者的代码，从而导致完全的远程代码执行。

2024 年 12 月发生了什么？

一名身份不明的黑客利用一个公开已知的[ASP.NET](https://asp.net/)机器密钥部署了 “哥斯拉”，这是一种后渗透工具，可提供对受攻击服务器的远程访问。攻击始于注入，攻击者使用泄露的机器密钥发送恶意的 ViewState 负载。

一旦服务器接收到该负载，便会对代码进行解密并执行，在不知情的情况下运行攻击者的指令。这导致了 “哥斯拉” 的部署，负载触发了 assembly.dll 的执行，加载该框架并允许进一步的攻击。

![ASP.NET Vulnerability Lets Hackers Hijack Servers, Inject Malicious Code]()

注入链条显示 ViewState 代码会导致 “哥斯拉”（攻击程序运行）。（源自微软）

微软的应对措施

根据微软的博客文章，该公司已从公开文档中删除了机器密钥示例，以阻止不良的安全实践。微软还通过微软端点防护（Microsoft Defender for Endpoint）发布了新的检测警报，以标记任何公开披露的机器密钥的使用情况。

如果您的系统受到攻击，仅仅轮换机器密钥可能还不够。微软建议进行全面的取证调查，因为攻击者可能已经安装了后门程序或其他恶意软件。

黑鸭（Black Duck）软件供应链风险策略主管蒂姆・麦基（Tim Mackey）对这一新情况评论道：“这种配置错误使得攻击者能够使用通过公开可用密钥加密的 ViewState 负载进行攻击，这些密钥通常来自演示代码。开发人员应该更换示例密钥，但有些人在不了解风险的情况下复制了它们。生产环境中硬编码的密钥表明配置不佳。对照微软的公钥列表进行检查会有所帮助，但 DevOps 团队也应该使用工具来检测并删除硬编码的机密信息。”

自我保护措施

为保护您的 Web 服务器免受攻击，如果您从在线资源复制了公开可用的机器密钥，首先应更换这些密钥。接下来，通过生成新密钥并在 Web 场中的所有服务器上一致应用，来轮换并保护您的密钥。

此外，在 web.config 文件中对机器密钥进行加密将有助于防止密钥暴露。监控可疑活动也至关重要。微软端点防护现在能够检测公开披露的[ASP.NET](https://asp.net/)机器密钥，启用攻击面减少规则有助于阻止网页木马攻击。

升级到[ASP.NET](https://asp.net/) 4.8 可通过整合反恶意软件扫描接口（AMSI）支持来增强安全性。最后，进行安全审计很重要。如果机器密钥已暴露，应假定发生了数据泄露，进行彻底调查，并检查是否存在未经授权的访问。

本文翻译自hackread [原文链接](https://hackread.com/asp-net-vulnerability-hackers-servers-inject-malicious-code/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303978](/post/id/303978)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/asp-net-vulnerability-hackers-servers-inject-malicious-code/)

如若转载,请注明出处： <https://hackread.com/asp-net-vulnerability-hackers-servers-inject-malicious-code/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**13赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [新 Eleven11bot 黑客攻击 86,000 台 IP 摄像机，发动大规模 DDoS 攻击](/post/id/308201)

  2025-06-06 15:33:29
* ##### [黑客发起全球间谍行动，政府邮箱被利用XSS漏洞入侵](/post/id/307477)

  2025-05-16 18:05:26
* ##### [虚假CAPTCHA投递Lumma Stealer窃密木马](/post/id/306195)

  2025-04-03 15:14:44
* ##### [Hugging Face 上的恶意ML模型利用Pickle Format 格式来逃避检测](/post/id/304018)

  2025-02-10 10:47:45
* ##### [新的恶意广告活动正在分发假冒的 Cisco AnyConnect 安装程序](/post/id/304015)

  2025-02-10 10:31:39
* ##### [“SparkCat” 恶意软件攻击：安卓与 iOS 用户受威胁，超 24.2 万次下载](/post/id/303878)

  2025-02-06 11:12:51
* ##### [400,000+ 系统受感染：DigitalPulse 代理软件带着新技巧回归](/post/id/303738)

  2025-01-23 09:38:26

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