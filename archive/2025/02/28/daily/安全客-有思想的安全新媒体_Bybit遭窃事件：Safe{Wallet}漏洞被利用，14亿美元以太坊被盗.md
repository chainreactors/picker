---
title: Bybit遭窃事件：Safe{Wallet}漏洞被利用，14亿美元以太坊被盗
url: https://www.anquanke.com/post/id/304806
source: 安全客-有思想的安全新媒体
date: 2025-02-28
fetch_date: 2025-10-06T20:35:22.139825
---

# Bybit遭窃事件：Safe{Wallet}漏洞被利用，14亿美元以太坊被盗

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

# Bybit遭窃事件：Safe{Wallet}漏洞被利用，14亿美元以太坊被盗

阅读量**99988**

发布时间 : 2025-02-27 11:00:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/bybit-heist-1-4b-ethereum-stolen-in-safewallet-exploit/>

译文仅供参考，具体内容表达以及含义原文为准。

![UNC5337 - CVE-2022-47945 Safe{Wallet} hack]()

加密货币交易所 Bybit 近期遭遇网络攻击，价值约 14 亿美元的以太坊被盗。被盗资产存于 Bybit 在 Safe {Wallet} 多签名平台上运行的保管钱包中。

攻击发生后，众多网络安全研究人员努力探究攻击者的作案手法。毕竟，黑客要同时攻破 Bybit 的钱包保管人以获取必要签名似乎不太可能。

然而，最新调查已明确排除 Bybit 的直接责任，显示安全漏洞存在于 Safe {Wallet} 自身。事实上，现已查明，臭名昭著的黑客组织Lazarus Group早在此次攻击前就已潜入 Safe {Wallet}，但一直在伺机对其高价值目标发动攻击。

研究人员称，此次攻击专门针对 Bybit。黑客将恶意 JavaScript 代码注入到 app.safe.global，该平台可供 Bybit 的签名者访问。不过，恶意脚本处于休眠状态，仅在特定条件下才会激活。这种选择性执行机制确保该后门不会被普通用户察觉。

对 Bybit 签名者机器的取证分析，结合通过Wayback Archive进行的历史回顾，研究人员发现了恶意 JavaScript 有效载荷的缓存版本。这一发现有力表明，Safe.Global 的Amazon  AWS S3 或 AWS CloudFront 账户或 API 密钥已遭泄露。

获取这些凭证后，攻击者得以操控 AWS S3 存储或 CloudFront CDN 服务，将恶意脚本注入平台。对 Safe {Wallet} 的 AWS S3 存储桶的进一步分析显示，存在专门针对 Bybit 的以太坊多签名冷钱包恶意软件。

Safe {Wallet} 在一份官方声明中证实，其调查追踪到攻击源自一台被入侵的 Safe {Wallet} 开发人员机器。本质上，黑客首先用恶意代码感染了一名开发人员的系统，然后利用被入侵开发人员的凭证将其 JavaScript 有效载荷注入平台。

作为回应，Safe {Wallet} 已全面重建和重新配置其基础设施，实施了全面的凭证轮换，包括 API 密钥，以确保所有攻击途径都已被消除，未来不会再被利用。

值得注意的是，研究人员在 Safe {Wallet} 的智能合约、前端或后端服务中未发现漏洞。相反，此次攻击的高明之处在于其精心策划、蓄谋已久的策略 —— 这是一场精心设计的供应链攻击，在对 Bybit 发动攻击之前成功渗透了 Safe {Wallet} 的开发环境。

本文翻译自securityonline [原文链接](https://securityonline.info/bybit-heist-1-4b-ethereum-stolen-in-safewallet-exploit/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304806](/post/id/304806)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/bybit-heist-1-4b-ethereum-stolen-in-safewallet-exploit/)

如若转载,请注明出处： <https://securityonline.info/bybit-heist-1-4b-ethereum-stolen-in-safewallet-exploit/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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