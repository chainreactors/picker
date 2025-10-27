---
title: 新的Crocodilus恶意软件完全控制Android设备
url: https://www.anquanke.com/post/id/308460
source: 安全客-有思想的安全新媒体
date: 2025-06-14
fetch_date: 2025-10-06T22:50:19.237684
---

# 新的Crocodilus恶意软件完全控制Android设备

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

# 新的Crocodilus恶意软件完全控制Android设备

阅读量**84365**

发布时间 : 2025-06-13 15:45:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-crocodilus-malware-that-gain-complete-control/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种名为 Crocodilus 的复杂新型 Android 银行木马已成为一个重大的全球威胁，它展示了先进的设备接管功能，使网络犯罪分子能够对受感染的智能手机进行前所未有的控制。

该恶意软件于 2025 年 3 月首次被发现，并迅速从本地化测试活动演变为针对多个大洲的金融机构和加密货币平台的全球行动。

该恶意软件最初出现在主要针对土耳其的活动中，但最近的情报显示，该策略积极扩张，现在包括波兰和西班牙在内的欧洲国家，同时将其覆盖范围扩展到南美市场。

Crocodilus 采用一种特别阴险的分发方法，通过伪装成合法银行和电子商务应用程序的恶意 Facebook 广告，向用户承诺奖金和促销优惠以吸引下载。

Threat Fabric 分析师指出，这些欺诈性广告以非凡的隐蔽性运行，仅保持活动状态一到两个小时，而每个广告的展示量超过 1000 次。

这些活动专门针对 35 岁以上的用户，战略性地关注可支配收入较高且更有可能参与金融服务的人群。

点击下载链接后，受害者会被重定向到提供 Crocodilus dropper 的恶意网站，该 dropper 经过精心设计可绕过 Android 13+ 安全限制。

![]()

该恶意软件的全球野心在其全面的目标列表中显而易见，其中包括来自阿根廷、巴西、西班牙、美国、印度尼西亚和印度的金融应用程序。

这种地域扩张与日益复杂的伪装技术相吻合，包括在欧洲市场冒充加密货币挖矿应用程序和数字银行服务。

![]()

Crocodilus 与传统银行恶意软件的区别在于其不断发展的功能集，其功能集远远超出了传统的凭证盗窃，代表了移动设备入侵的新范式。

## 高级联系人作和加密货币定位

最新的 Crocodilus 变体引入了一项特别令人担忧的功能，该功能允许攻击者通过特定的命令结构纵受害者联系人列表。

当恶意软件收到命令“TRU9MMRHBCRO”时，它会自动将指定的联系人添加到受感染设备的地址簿中。

此功能使网络犯罪分子能够插入欺诈性条目，例如带有攻击者控制的电话号码的“Bank Support”，为后续的社会工程攻击创造合法性的假象，同时可能绕过标记未知呼叫者的欺诈预防系统。

该恶意软件的加密货币定位功能也通过利用 Android 的 AccessibilityLogging 功能的改进的助记词收集器得到了显着增强。

该系统使用复杂的正则表达式来提取敏感数据：-

```
this.regex1 = "[a-fA-F0-9]{64}";
this.regex2 = "^(\\d+)\\.?\\s*(\\w+)$";
this.regex3 = "\\d+";
this.regex4 = "\\w+";
this.regex5 = "^\\d+\\.?\\s*\\w+$";
```

这些模式支持从加密货币钱包应用程序中自动提取私钥和助记词，恶意软件对捕获的数据进行实时预处理，以提供高质量的情报，以便立即用于欺诈。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-crocodilus-malware-that-gain-complete-control/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308460](/post/id/308460)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-crocodilus-malware-that-gain-complete-control/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-crocodilus-malware-that-gain-complete-control/>

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

* [高级联系人作和加密货币定位](#h2-0)

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