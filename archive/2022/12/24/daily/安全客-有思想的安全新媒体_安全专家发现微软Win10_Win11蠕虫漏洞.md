---
title: 安全专家发现微软Win10/Win11蠕虫漏洞
url: https://www.anquanke.com/post/id/284593
source: 安全客-有思想的安全新媒体
date: 2022-12-24
fetch_date: 2025-10-04T02:24:15.733240
---

# 安全专家发现微软Win10/Win11蠕虫漏洞

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

# 安全专家发现微软Win10/Win11蠕虫漏洞

阅读量**189802**

发布时间 : 2022-12-23 10:00:37

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## [![]()](https://p5.ssl.qhimg.com/t01c2abc944836d51e2.jpg)

第426期

> 你好呀~欢迎来到“安全头条”！如果你是第一次光顾，可以先阅读站内公告了解我们哦。
>
> 欢迎各位新老顾客前来拜访，在文章底部时常交流、疯狂讨论，都是小安欢迎哒~如果对本小站的内容还有更多建议，也欢迎底部提出建议哦！

## 1、安全专家发现微软Win10/Win11蠕虫漏洞

[![]()](https://p2.ssl.qhimg.com/t010aba1cbcc3c652a7.png)

近日，网络安全专家近日在Windows平台上发现了一个代码执行漏洞，并将该漏洞追踪编号为CVE-2022-37958，允许攻击者在没有身份验证的情况下执行任意恶意代码。据了解，该漏洞与利用Windows操作系统WannaCry漏洞的蠕虫病毒相似，但这个新的漏洞可以利用更多的网络协议，而不是像WannaCry一样仅能使用SMB协议， 这意味着它将能够更为迅速的感染其他设备，存在更大的安全风险。

## 2、研究人员披露针对巴西用户的新型安卓恶意软件BrasDex

[![]()](https://p5.ssl.qhimg.com/t015be80fdc4b74ad4b.png)

近日，ThreatFabric分析师发现了一个针对巴西用户的多平台恶意软件活动，目前已有数千人感染，估计损失数美金。据了解，该活动涉及一个被ThreatFabric称为BrasDex的高新型安卓恶意软件，该软件冒充安卓应用程序，从而攻击巴西银行应用程序。在最新的活动中，它已经开始冒充一个特定的银行应用程序（Banco Santander BR）。

目前，网络安全分析师还在持续跟踪该恶意软件。

## 3、GitHub存储库被黑后Okta源代码被盗

[![]()](https://p1.ssl.qhimg.com/t01a4ebc0628fc7becb.png)

身份验证服务和身份与访问管理 (IAM) 解决方案的领先提供商 Okta 表示，其私人 GitHub 存储库本月遭到黑客攻击，攻击者窃取了 Okta 的源代码。

日前，外媒披露称， Okta遭遇了不明的黑客攻击，黑客还试图窃取Okta的源代码。目前，可确定的是源代码已被盗，但客户数据未受影响。

## 4、GodFather Android恶意软件盯上400家银行和交易所

[![]()](https://p5.ssl.qhimg.com/t013f032e58f63704db.png)

近日，一款名为“Godfather ”的 Android 银行恶意软件一直以16个国家/地区的用户为目标，试图窃取400多个在线银行网站和加密货币交易所的帐户凭据。

据悉，当受害者尝试登录网站时，该恶意软件会生成覆盖在银行和加密交换应用程序登录表单之上的登录屏幕，诱使用户在精心设计的 HTML 钓鱼页面上输入他们的凭据。

Godfather 木马是由 Group-IB 分析师发现的，他们认为它是Anubis 的继任者，Anubis 是一种曾经广泛使用的银行木马，由于无法绕过更新的 Android 防御而逐渐被淘汰。[[阅读原文]](https://www.bleepingcomputer.com/news/security/godfather-android-malware-targets-400-banks-crypto-exchanges/)

## 5、德国工业巨头ThyssenKrupp AG遭遇网络攻击

[![]()](https://p4.ssl.qhimg.com/t01d1f2030b3d5afab9.png)

德国跨国工业工程和钢铁生产巨头ThyssenKrupp AG宣布其材料服务部门和公司总部遭到网络攻击。目前，该公司尚未披露对其系统造成攻击的类型，也没有网络犯罪组织声称对此次攻击负责。

近日，有媒体披露称德国跨国工业工程和钢铁生产公司 ThyssenKrupp AG 成为网络攻击的目标，而这已不是该公司第一次遭受网络攻击，早在2012年，该公司曾遭受了一次被归类为“严重”的网络攻击。[[阅读原文]](https://securityaffairs.co/wordpress/139870/hacking/thyssenkrupp-targeted-cyberattack.html)

## 6、“盲区”攻击从Windows内核破坏EDR平台

![]()

一项新开创的技术可以通过从硬件断点上解除 Windows 内核 (NTDLL) 面向用户的模式，从而使端点检测和响应 (EDR) 平台“失明”。

据悉，该技术加载一个不受监控且未挂钩的 DLL，并利用允许运行任意代码的调试技术。研究人员警告说，这可能使恶意行为者能够在 EDR 不知情的情况下从 NTDLL 中执行任何功能并交付它。[[阅读原文]](https://www.darkreading.com/attacks-breaches/-blindside-attack-subverts-edr-platforms-windows-kernel)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/284593](/post/id/284593)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t01a1ab830955b940ce.png)

[![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)](/member.html?memberId=2)

[安全客](/member.html?memberId=2)

有思想的安全新媒体

* 文章
* **3687**

* 粉丝
* **225**

### TA的文章

* ##### [ISC.AI2024热点资讯](/post/id/297785)

  2024-07-10 17:00:28
* ##### [ISC2023热点资讯](/post/id/289102)

  2023-06-06 17:21:40
* ##### [数说安全《攻击面管理产品》报告发布 360以第一顺位入选国内代表性安全厂商](/post/id/288540)

  2023-05-05 12:03:24
* ##### [伪装成ChatGPT的 恶意软件被用来引诱受害者](/post/id/288531)

  2023-05-05 12:01:24
* ##### [研究人员发现Microsoft Azure API管理服务中的3个漏洞](/post/id/288526)

  2023-05-05 11:59:52

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

* [1、安全专家发现微软Win10/Win11蠕虫漏洞](#h2-1)
* [2、研究人员披露针对巴西用户的新型安卓恶意软件BrasDex](#h2-2)
* [3、GitHub存储库被黑后Okta源代码被盗](#h2-3)
* [4、GodFather Android恶意软件盯上400家银行和交易所](#h2-4)
* [5、德国工业巨头ThyssenKrupp AG遭遇网络攻击](#h2-5)
* [6、“盲区”攻击从Windows内核破坏EDR平台](#h2-6)

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