---
title: 攻击者获利约302万美元，Orion Protocol被攻击事件分析
url: https://www.anquanke.com/post/id/286259
source: 安全客-有思想的安全新媒体
date: 2023-02-15
fetch_date: 2025-10-04T06:35:44.065767
---

# 攻击者获利约302万美元，Orion Protocol被攻击事件分析

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

# 攻击者获利约302万美元，Orion Protocol被攻击事件分析

阅读量**288113**

发布时间 : 2023-02-14 16:30:42

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 事件背景

零时科技区块链安全情报平台监控到消息，北京时间2023年2月3日，BSC链与ETH链上Orion Protocol受到黑客攻击，攻击者获利约300万美元，攻击者地址为0x837962b686fd5a407fb4e5f92e8be86a230484bd，被盗资金已转移至Tornado.Cash混币平台。零时科技安全团队及时对此安全事件进行分析。

## 漏洞及核心

Orion Protocol是一个交易聚合协议，用户可以进行代币交易，兑换以及跨链操作等。此处以BSC链攻击交易为例。

攻击者执行兑换操作，其中路径1代币由攻击者控制。

![]()

![]()

在执行第一次兑换后，转入攻击者构造的恶意合约中进行代币转账，转账函数由攻击者恶意构造，在恶意构造的转账函数中攻击者将通过闪电贷获得的191,606 USDT 调用ExchangeWithAtomic合约中depositAsset函数存入合约中，此时修改了assetBalances变量的值，但是在最终转账时并没有执行assetBalances变量的修改。

![]()

![]()

计算最终兑换代币数值是由当前代币余额减去执行兑换之前合约对应代币余额

![]()

由于在执行兑换过程中攻击者已经向合约转移大笔资金，因此攻击者兑换出的USDT资金变多

![]()

兑换前余额

![]()

执行兑换操作后余额

攻击者在此次兑换中使用1USDC共兑换出191,606 USDT

![]()

由于攻击者此前执行了depositAsset函数操作，但是兑换完成时并没有涉及到此函数中变量，攻击者仍可以通过调用withdraw函数取出之前通过depositAsset函数存入的资金。

![]()

## 资金来源及去向

### 资金来源

ETH链攻击地址资金来源为Bianace15交易所

![]()

BSC链攻击地址资金来源为Tornado.Cash混币平台

![]()

### 资金流向

BSC链被盗资金通过跨链全部转移至ETH链攻击者地址

![]()

ETH链将被盗资金兑换为ETH共1100 ETH转移至 Tornado.Cash混币平台

![]()

## 总结及建议

此次攻击是由于ExchangeWithAtomic合约中对于合约内不同函数间的重入未做限定，使得攻击者能够通过调用构造的恶意合约实现重入操作，且合约中代币兑换后转出资金计算方式只受合约代币余额影响，因此攻击者在执行兑换时通过调用其他函数转入资金影响合约余额后将转入的资金取出实现获利。

🔹**安全建议**

建议对合约中涉及资金转移函数添加防重入机制保护，避免攻击者通过控制恶意合约进行攻击

建议项目方上线前进行多次审计，避免出现审计步骤缺失

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**零时科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286259](/post/id/286259)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [区块链](/tag/%E5%8C%BA%E5%9D%97%E9%93%BE)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01482eaf8414a7973c.png)零时科技

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [披露！币圈空投黑吃黑“脏”手段，“偷家”这招儿真有你的](/post/id/284309)

  2023-01-04 17:30:27
* ##### [iDASH 2022隐私计算大赛——字节跳动Jeddak Team获得佳绩](/post/id/284269)

  2022-12-19 17:30:53
* ##### [Glupteba恶意软件在被谷歌中断后重新活跃](/post/id/284418)

  2022-12-19 11:15:03
* ##### [TrustSwap 攻击事件分析](/post/id/282575)

  2022-11-08 10:30:07
* ##### [Victor the Fortune攻击事件分析](/post/id/282574)

  2022-11-07 10:30:11
* ##### [DPC攻击复现](/post/id/281186)

  2022-10-09 11:00:17
* ##### [BXH攻击事件分析](/post/id/281172)

  2022-10-08 11:00:51

### 热门推荐

文章目录

* [事件背景](#h2-0)
* [漏洞及核心](#h2-1)
* [资金来源及去向](#h2-2)
  + [资金来源](#h3-3)
  + [资金流向](#h3-4)
* [总结及建议](#h2-5)

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