---
title: 关于 HardBit 勒索软件的一些细节
url: https://www.anquanke.com/post/id/298049
source: 安全客-有思想的安全新媒体
date: 2024-07-19
fetch_date: 2025-10-06T17:40:50.689464
---

# 关于 HardBit 勒索软件的一些细节

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

# 关于 HardBit 勒索软件的一些细节

阅读量**147782**

发布时间 : 2024-07-18 15:19:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Graham Cluley，文章来源：tripwire

原文地址：<https://www.tripwire.com/state-of-security/hardbit-ransomware-what-you-need-know>

译文仅供参考，具体内容表达以及含义原文为准。

#### 发生了什么？

一种新的HardBit勒索软件变种已经在野外出现。它包含了一种保护机制，试图阻止安全研究人员的分析。

#### HardBit？我以前好像听说过。

很可能。HardBit首次出现在2022年末，并迅速因其针对企业数据加密后要求赎金的行为而声名狼藉。

#### 这听起来并不罕见。那是什么让HardBit与众不同？

你没错。在很多方面，HardBit与其他勒索软件类似。它是一种作为服务提供的勒索软件（RaaS），以价格提供给其他网络犯罪分子使用。恶意黑客侵入您的IT系统，加密您的数据，并要求支付加密货币作为赎金。然而，与其他许多勒索软件团伙不同的是，HardBit似乎没有在暗网上运营泄露网站。

#### 如果他们没有泄露网站，他们会泄露您的数据吗？

看起来他们不会。相反，他们似乎专注于通过交换解密密钥来勒索赎金，以便受影响的组织可以恢复他们的文件。此外，该团伙威胁如果其要求未得到满足，将对受害者发起更多攻击。那么，既然他们在暗网上没有泄露网站，您如何谈判赎金支付呢？

#### 勒索通知留下的信息要求受害者通过TOX联系，这是一个开源的点对点安全消息平台。

#### 如果你不联系他们……？

你可能找不到解密数据的方法，而且你的公司面临再次被攻击的风险。HardBit还警告说，如果48小时内不联系，赎金需求将会增加。

#### 所以压力很大……

是的，像许多其他勒索软件团伙一样，HardBit显然意在认真经营。在过去，该团伙通过鼓励其企业受害者匿名披露其网络安全保险的金额和条款来加强这一点，辩称分享这些信息会同时使攻击者和受害者受益——但保险公司本身除外。

#### 你提到了有新的HardBit变种。它有什么特别值得注意的地方吗？

是的，安全研究人员报告称，HardBit 4.0被设计得更难被恶意软件专家分析。新版的HardBit集成了密码短语保护。当勒索软件运行时，必须正确输入密码短语才能正常执行。意图似乎是让不知道密码短语的研究人员更难以分析勒索软件的工作原理。此外，HardBit 4.0有两种版本：一种是命令行版本的勒索软件，另一种则带有用户界面。看来，这种选择是为了让具有不同技术水平的操作者觉得勒索软件更具吸引力。

#### 勒索软件故意让自己对犯罪分子更有吸引力听起来并不是一个好现象……

我同意！请遵循我们的建议，了解如何保护您的组织免受攻击。

本文翻译自tripwire [原文链接](https://www.tripwire.com/state-of-security/hardbit-ransomware-what-you-need-know)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298049](/post/id/298049)

安全KER - 有思想的安全新媒体

本文转载自: [tripwire](https://www.tripwire.com/state-of-security/hardbit-ransomware-what-you-need-know)

如若转载,请注明出处： <https://www.tripwire.com/state-of-security/hardbit-ransomware-what-you-need-know>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [勒索攻击](/tag/%E5%8B%92%E7%B4%A2%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [Gunra Ransomware集团声称从美国医院泄露了40 TB数据](/post/id/308534)

  2025-06-17 16:00:49
* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45

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