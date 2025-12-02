---
title: “哈希劫持”攻击手法通过操纵URL片段标识符（#）来操控AI浏览器的行为
url: https://www.anquanke.com/post/id/313521
source: 安全客-有思想的安全新媒体
date: 2025-12-01
fetch_date: 2025-12-02T03:17:33.699446
---

# “哈希劫持”攻击手法通过操纵URL片段标识符（#）来操控AI浏览器的行为

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

# “哈希劫持”攻击手法通过操纵URL片段标识符（#）来操控AI浏览器的行为

阅读量**14798**

发布时间 : 2025-12-01 17:45:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/hashjack-attack-url-control-ai-browser-behavior/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

2025年11月25日，网络安全公司Cato Networks披露了一种名为**HashJack**的新威胁。在这种威胁中，**网址（URL）中的简单井号（#）**可以隐藏针对AI浏览器助手的恶意指令，例如谷歌的Gemini、微软的Copilot以及Perplexity的Comet。

### 漏洞详情

HashJack是首个此类间接提示注入技术案例。攻击者将命令隐藏在AI稍后会读取的内容中，在这种情况下，就是URL本身。这使得HashJack能够利用AI助手读取完整URL的方式，包括#之后的部分（URL片段），而这部分通常是Web服务器会忽略的。

**这使得恶意行为者可以将任何合法网站武器化**，而无需对该网站本身进行黑客攻击。正如Cato Networks的高级安全研究员Vitaly Simonovich所解释的，弱点在于AI助手对URL的处理方式。由于用户信任合法网站，他们也就信任了AI被操纵后的建议。

隐藏的命令可能导致各种恶意行为，包括诱骗用户泄露其登录详细信息（凭证窃取），甚至提供错误的健康相关建议（医疗伤害）。更令人担忧的是，在高级代理模式下（AI自动执行任务），助手可能会被指示通过在后台获取攻击者的URL来窃取敏感用户数据（数据泄露）。

此外，AI还可能被引导给出执行危险技术任务的分步说明，例如打开系统端口或下载实际上是恶意软件的软件包。研究人员还指出，在一些高级AI浏览器中，如Perplexity的Comet，攻击甚至可能升级到AI助手自动获取用户数据并将其发送到外部地址。

![]()

### 科技巨头的不同反应

Cato Networks威胁研究团队从2025年7月和8月开始向受影响的公司披露了他们的发现。微软反应迅速，于10月27日为Edge浏览器的Copilot应用了修复程序。Perplexity也在2025年11月18日之前为其Comet浏览器应用了修复程序。

然而，谷歌尚未解决Chrome浏览器中Gemini的这一问题。该报告于2025年10月被谷歌Abuse VRP/Trust & Safety标记为“不会修复（预期行为）”，并被评为低严重性。值得注意的是，在该研究发表时，此问题仍未得到解决。

Cato CTRL™威胁研究的发现（独家分享给Hackread.com ）引入了一类新的AI安全风险，因为恶意命令隐藏在URL片段中，可以绕过传统防火墙。这一发现提醒业界，随着AI助手处理敏感数据，供应商必须紧急修复AI设计中的缺陷，以防止未来的上下文操纵攻击。

本文翻译自hackread [原文链接](https://hackread.com/hashjack-attack-url-control-ai-browser-behavior/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313521](/post/id/313521)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/hashjack-attack-url-control-ai-browser-behavior/)

如若转载,请注明出处： <https://hackread.com/hashjack-attack-url-control-ai-browser-behavior/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **760**

* 粉丝
* **6**

### TA的文章

* ##### [Devolutions Server 中存在严重漏洞（CVE-2025-13757），已认证的攻击者可利用SQL注入窃取所有存储的密码](/post/id/313498)

  2025-12-01 17:48:48
* ##### [新型TangleCrypt加壳器可隐藏EDR对抗工具，但因编码缺陷反致勒索软件意外崩溃](/post/id/313501)

  2025-12-01 17:48:27
* ##### [GeoServer 中存在高危漏洞（CVE-2025-58360），可利用未授权的XXE攻击实现文件窃取与服务端请求伪造](/post/id/313505)

  2025-12-01 17:48:01
* ##### [新型恶意软件即服务运营商 TAG-150 利用 ClickFix 诱饵及自定义 CastleLoader，已入侵美国境内 469 台设备](/post/id/313509)

  2025-12-01 17:47:16
* ##### [OpenAI在ChatGPT安卓测试版中启动广告功能测试，引发用户对数据隐私的担忧](/post/id/313514)

  2025-12-01 17:46:49

### 相关文章

* ##### [Devolutions Server 中存在严重漏洞（CVE-2025-13757），已认证的攻击者可利用SQL注入窃取所有存储的密码](/post/id/313498)

  2025-12-01 17:48:48
* ##### [新型TangleCrypt加壳器可隐藏EDR对抗工具，但因编码缺陷反致勒索软件意外崩溃](/post/id/313501)

  2025-12-01 17:48:27
* ##### [GeoServer 中存在高危漏洞（CVE-2025-58360），可利用未授权的XXE攻击实现文件窃取与服务端请求伪造](/post/id/313505)

  2025-12-01 17:48:01
* ##### [新型恶意软件即服务运营商 TAG-150 利用 ClickFix 诱饵及自定义 CastleLoader，已入侵美国境内 469 台设备](/post/id/313509)

  2025-12-01 17:47:16
* ##### [OpenAI在ChatGPT安卓测试版中启动广告功能测试，引发用户对数据隐私的担忧](/post/id/313514)

  2025-12-01 17:46:49
* ##### [美国CISA已将OpenPLC ScadaBR系统中正遭积极利用的XSS漏洞（CVE-2021-26829）列入其关键漏洞目录](/post/id/313517)

  2025-12-01 17:46:23
* ##### [“河内窃贼”攻击行动：黑客利用伪多语言LNK/图像混合文件，通过DLL侧加载投送LOTUSHARVEST窃密木马](/post/id/313495)

  2025-12-01 17:45:09

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