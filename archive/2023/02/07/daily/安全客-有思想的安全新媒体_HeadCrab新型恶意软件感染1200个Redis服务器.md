---
title: HeadCrab新型恶意软件感染1200个Redis服务器
url: https://www.anquanke.com/post/id/285988
source: 安全客-有思想的安全新媒体
date: 2023-02-07
fetch_date: 2025-10-04T05:50:34.589561
---

# HeadCrab新型恶意软件感染1200个Redis服务器

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

# HeadCrab新型恶意软件感染1200个Redis服务器

阅读量**115252**

发布时间 : 2023-02-06 10:00:29

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## [![]()](https://p5.ssl.qhimg.com/t01c2abc944836d51e2.jpg)

第451期

> 你好呀~欢迎来到“安全头条”！如果你是第一次光顾，可以先阅读站内公告了解我们哦。
>
> 欢迎各位新老顾客前来拜访，在文章底部时常交流、疯狂讨论，都是小安欢迎哒~如果对本小站的内容还有更多建议，也欢迎底部提出建议哦！

## 1、Twitter API将不再提供免费访问

[![]()](https://p5.ssl.qhimg.com/t01ee65a4b51cab74f8.png)

Twitter宣布从2月9日开始它的API（包括 v2 和 v1.1）将不再支持免费访问，使用其API将必须付费。这事实上杀死了第三方客户端和利用免费API对Twitter推文进行研究的项目，以及各种在多平台上交叉发帖的工具。在马斯克(Elon Musk)收购Twitter之后，API访问已经多次出现问题，上个月 Twitter 修改了 API 规则，明确禁止开发者开发第三方客户端。

或许，API付费只是最后一根稻草。[[阅读原文]](https://www.solidot.org/story?sid=74021)

## 2、小米汽车“设计文件”泄密，供应商被罚100万元！

[![]()](https://p2.ssl.qhimg.com/t016f939d17bdfc2509.png)

自2021年雷军正式宣布造车以来，小米汽车一直吸引着业界的密切关注。2023年年初，小米汽车首款量产车的设计效果图被曝光，内部代号为MS11，预计将在2024年开始量产，可谓赚足了用户的眼球。随后，昵称为“不是郑小康”的汽车博主，在微博发布一则关于小米MS11车型的图片，主要展示了小米汽车保险杠、小米MS11的装饰件以及小米与北汽模塑相关合作细节等。一时间，“小米汽车设计文件泄密”事件被传的沸沸扬扬。

针对该事件，小米公关部总经理王化1月24日发文回应称，的确是二级供应商保密的设计文件泄密；该供应商仅仅是为模具打样的供应商，泄密的文件是非常早期的招标过程的设计稿，并非最终文件；小米公司一定会根据与该供应商签订的保密协议进行严肃处理。

## 3、LockBit 纳新，开始使用基于 Conti 的加密器

[![]()](https://p5.ssl.qhimg.com/t0199455c631155608d.png)

日前，外媒披露称知名勒索软件组织LockBit 开始使用一种新型加密器，其源代码来自已经被解散的Conti 勒索软件。 据推特上多位知名安全博主表示，LockBit使用的这种新型加密器被称为“LockBit Green”，通过对样本进行逆向工程，发现它100%基于Conti泄露的源代码，但令人困惑的是，LockBit已经拥有属于自己的加密器，却还要选择基于 Conti 构建有效负载。

## 4、HeadCrab新型恶意软件感染1200个Redis服务器

[![]()](https://p5.ssl.qhimg.com/t01bbce95cd4bf181db.png)

自2021年9月以来，用于在线搜索易受攻击的Redis服务器的新型隐身恶意软件已经感染了1000多台服务器，以构建一个针对Monero加密货币的僵尸网络。

由Aqua Security研究人员Nitzan Yaakov和Asaf Eitani发现，并将其命名为 HeadCrab，该恶意软件迄今已诱捕至少1200台此类服务器，这些服务器还用于在线扫描更多目标。

研究人员称：“这个高级威胁行为者利用无代理和传统防病毒解决方案无法检测到的最先进的定制恶意软件来破坏大量Redis服务器。”[[阅读原文]](https://www.bleepingcomputer.com/news/security/new-headcrab-malware-infects-1-200-redis-servers-to-mine-monero/)

## 5、安全研究员披露Facebook、Instagram双因素身份验证漏洞

[![]()](https://p1.ssl.qhimg.com/t017df8cc971d7353b9.png)

一名来自尼泊尔的安全研究员Gtm Mänôz，披露了一个影响Instagram和Facebook的双因素身份验证漏洞。在向Meta报告此漏洞后，其将一笔27200美元的赏金收入了囊中。

双因素身份验证(2FA)是目前常见的一种保护用户账户安全的手段。它是一种需要提供两个身份验证因素以确认身份的身份验证过程，用户需要用两种方式（用户所知道的和用户所拥有的，例如密码和手机收到的验证码）证明自己的身份才能获得账户访问授权。

据悉，该漏洞存在于Facebook母公司Meta用于确认手机号码和电子邮件地址的组件中。Gtm Mänôz注意到，该组件未对验证码做时间和失败次数校验，这使得攻击者在获知受害者的手机号码后，能够暴力破解验证码。[[阅读原文]](http://www.hackdig.com/02/hack-897826.htm)

## 6、1800+种Android网络钓鱼形式，极低价格暗网兜售

[![]()](https://p4.ssl.qhimg.com/t018c655d213114f36f.png)

一个名为InTheBox的攻击组织正在俄罗斯网络犯罪论坛上发布1894个网络注入（网络钓鱼窗口的覆盖）的清单，用于从银行、加密货币交易所和电子商务应用程序中窃取凭据和敏感数据。

Cyble Research 和 Intelligence Labs (CRIL) 的调查显示，威胁行为者 InTheBox 一直在增加其驻留在暗网上的在线商店中与各种 Android 银行恶意软件兼容的网络注入库存。

Android web inject 是一个定制模块，旨在从特定应用程序中收集敏感信息。注入 InTheBox 商店的目标是零售银行、移动支付系统、加密货币交易所和移动电子商务应用程序。澳大利亚、巴西、印度、印度尼西亚、日本、科威特、马来西亚、菲律宾、卡塔尔、沙特阿拉伯、新加坡、泰国和美国以及欧洲和亚洲各地的组织都受到了影响。

InTheBox 商店为各种银行恶意软件提供范围广泛的 Web 注入，包括 Alien、Ermac、Octopus、MetaDroid、Cerberus 和 Hydra。数百次注射的包装价格从近4000美元到6500美元不等。单个 Web 注入的价格已从每个50美元降至30美元。自2020年2月以来，InTheBox 一直是经过验证的 Android 移动应用程序网络注入供应商。[[阅读原文]](https://cybernews.com/news/inthebox-targets-android-banking-applications/)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/285988](/post/id/285988)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**15赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t01a1ab830955b940ce.png)

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

* [1、Twitter API将不再提供免费访问](#h2-1)
* [2、小米汽车“设计文件”泄密，供应商被罚100万元！](#h2-2)
* [3、LockBit 纳新，开始使用基于 Conti 的加密器](#h2-3)
* [4、HeadCrab新型恶意软件感染1200个Redis服务器](#h2-4)
* [5、安全研究员披露Facebook、Instagram双因素身份验证漏洞](#h2-5)
* [6、1800+种Android网络钓鱼形式，极低价格暗网兜售](#h2-6)

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