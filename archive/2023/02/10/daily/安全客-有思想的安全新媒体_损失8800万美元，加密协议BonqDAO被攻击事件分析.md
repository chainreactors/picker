---
title: 损失8800万美元，加密协议BonqDAO被攻击事件分析
url: https://www.anquanke.com/post/id/286163
source: 安全客-有思想的安全新媒体
date: 2023-02-10
fetch_date: 2025-10-04T06:12:09.100237
---

# 损失8800万美元，加密协议BonqDAO被攻击事件分析

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

# 损失8800万美元，加密协议BonqDAO被攻击事件分析

阅读量**241949**

发布时间 : 2023-02-09 15:30:28

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 事件背景

零时科技区块链安全情报平台监控到消息，北京时间2023年2月2日，polygon链上去中心化借贷协议BONQ受到黑客攻击，攻击者获得了1.13亿个WALTB和9865万个BEUR，攻击者地址为0xcAcf2D28B2A5309e099f0C6e8C60Ec3dDf656642，攻击者将部分BEUR售出获得USDC通过跨链转移至ETH链。零时科技安全团队及时对此安全事件进行分析。

## 漏洞及核心

TellorFlex中可通过调用submitValue函数进行更改代币价格，当用户质押的TRB代币大于stakeAmount时可获得修改代币价格权限。

![]()

stakeAmount初始值在构造函数中传入，后续可通过调用updateStakeAmount修改，从链上信息可知，updateStakeAmount函数未被调用，因此攻击者可通过质押初始值获得修改代币价格，从攻击交易中可得值为10TRB。

![]()

![]()

攻击者调用BONQ合约中的createTrove函数创建trove合约，trove合约中抵押价格计算方法是预言机中抵押品Token价格除以借款数量。

![]()

![]()

此合约中使用的预言机为TellorFlex合约，此前攻击者已经将ALBT代币价格修改到相当高，因此攻击者可以使用较小的WALBT借出大量BEUR。

![]()

从攻击交易中可以看出，攻击者使用0.1WALBT借出1亿个BEUR.

![]()

## 资金来源及流向

### 资金来源

此地址初始资金在ETH链上由Tornado.Cash混币平台转入

![]()

### 资金流向

攻击者将部分BEUR兑换为 534,535 USDC，通过跨链转移至ETH链，之后兑换为DAI，目前资金暂无进一步移动

![]()

攻击者目前共抛售1600万ALBT，获得约785ETH，目前资金仍存在ETH链上攻击者地址中。

## 总结及建议

本次攻击由于TellorFlex预言机报价修改时所需要的抵押物价值较小，且BONQ借贷合约中抵押物借贷数量只与TellorFlex预言机价格有关，因此攻击者可以使用较低的成本修改预言机报价后进行抵押借贷获得相当可观的利润。

### ♦安全建议

建议项目方增加多种喂价机制，避免预言机受到控制时由于单一喂价遭受损失。

建议项目方上线前进行多次审计，避免出现审计步骤缺失

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**零时科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286163](/post/id/286163)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [攻击事件](/tag/%E6%94%BB%E5%87%BB%E4%BA%8B%E4%BB%B6)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01482eaf8414a7973c.png)零时科技

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t01482eaf8414a7973c.png)](/member.html?memberId=155670)

[零时科技](/member.html?memberId=155670)

全球区块链安全技术提供商

* 文章
* **50**

* 粉丝
* **19**

### TA的文章

* ##### [零时科技 || Arbitrum链上Jimbos Protocol项目受到黑客攻击，攻击者获利约 776 万美元](/post/id/288931)

  2023-05-30 15:47:54
* ##### [攻击者获利约302万美元，Orion Protocol被攻击事件分析](/post/id/286259)

  2023-02-14 16:30:42
* ##### [损失8800万美元，加密协议BonqDAO被攻击事件分析](/post/id/286163)

  2023-02-09 15:30:28
* ##### [分布式资本创始人4200万美金资产被盗分析及追踪工作](/post/id/283685)

  2022-11-29 16:00:36
* ##### [TrustSwap 攻击事件分析](/post/id/282575)

  2022-11-08 10:30:07

### 相关文章

* ##### [零时科技 || Arbitrum链上Jimbos Protocol项目受到黑客攻击，攻击者获利约 776 万美元](/post/id/288931)

  2023-05-30 15:47:54
* ##### [分布式资本创始人4200万美金资产被盗分析及追踪工作](/post/id/283685)

  2022-11-29 16:00:36
* ##### [Earing Farm攻击事件分析](/post/id/281979)

  2022-11-01 12:00:34
* ##### [BEGO Token 攻击事件分析](/post/id/282010)

  2022-10-31 12:00:29
* ##### [EGD被黑客攻击损失超3.6万 BUSD，事件分析](/post/id/278035)

  2022-08-17 12:00:15
* ##### [Ronin Network侧链被盗6.25亿美金流向分析](/post/id/271413)

  2022-04-06 15:30:22
* ##### [Paraluni攻击事件分析](/post/id/270172)

  2022-03-17 15:30:29

### 热门推荐

文章目录

* [事件背景](#h2-0)
* [漏洞及核心](#h2-1)
* [资金来源及流向](#h2-2)
  + [资金来源](#h3-3)
  + [资金流向](#h3-4)
* [总结及建议](#h2-5)
  + [♦安全建议](#h3-6)

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