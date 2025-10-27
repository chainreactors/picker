---
title: Earing Farm攻击事件分析
url: https://www.anquanke.com/post/id/281979
source: 安全客-有思想的安全新媒体
date: 2022-11-02
fetch_date: 2025-10-03T21:30:10.222305
---

# Earing Farm攻击事件分析

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

# Earing Farm攻击事件分析

阅读量**268816**

发布时间 : 2022-11-01 12:00:34

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 事件背景

零时科技区块链安全情报平台监控到消息，北京时间2022年10月15日，DeFi 投资工具 Earning.Farm 遭受闪电贷攻击，黑客获利超 34 万美元，攻击者地址为0xdf31f4c8dc9548eb4c416af26dc396a25fde4d5f，零时科技安全团队及时对此安全事件进行分析。

## 攻击步骤

1.调用闪电贷借出560 ETH

![]()

2.调用receiveFlashloan函数，根据userData传入参数调用\_withdraw函数计算获利资金为833 stETH

![]()

3.归还闪电贷资金560ETH，此时合约中仍有资金约273stETH

![]()

4.调用withdraw函数取出合约中资金

![]()

5.攻击者共获利268.7ETH

![]()

## 漏洞核心

合约正常逻辑为通过调用withdraw函数，判断用户持有的ef\_token数量后计算用户获得的收益，之后通过闪电贷还款后剩余的资金就是用户获得的收益。

![]()

但是在Vault合约中对于调用闪电贷的地址没有进行判断，因此攻击者可以自行调用闪电贷合约，将闪电贷的接受者设置为EFLevelValue的地址，并且传入的参数由用户控制，攻击者可以自行设置userData的数据。

![]()

在receiveFlashLoan函数中可以看到当传入参数哈希值与“0x2”哈希值相等时执行\_withdraw函数

![]()

攻击者传入参数userData为307832，通过进制转换可知为字符串0x2

![]()

在\_withdraw()函数中根据传入的 amount将stETH从AAVE中取出后兑换为WETH，之后归还闪电贷资金，剩余资金存在合约中。

![]()

在withdraw（）函数中转账数量计算时没有对于用户应收的资金进行判断，而是将合约中剩余资金全部转出。

![]()

因此攻击者通过正常调用withdraw函数，可以使用少量的ef\_token将合约中的资金全部转出。

![]()

## 资金来源及去向

攻击者初始资金来源于跨链合约

![]()

后续攻击者将部分资金转移至Tornado.cash混币平台，部分资金转移至 地址0xDa08116d1e36CaDe5dE91bc6892FB0fAF00eBf15后通过multichain款连合约转出

![]()

![]()

## 总结及建议

此次攻击主要是由于在闪电贷合约中没有对闪电贷合约发起者进行判断使得攻击者可以直接调用闪电贷将闪电贷接收者设置为被攻击合约进行计算奖励的操作，并且在提取奖励时没有对用户应获得的奖励进行判断，直接将合约剩余资金全部转出，因此攻击者可以使用少量的ef\_token将攻击获得资金全部转移。

**安全建议**

建议在闪电贷时对发起闪电贷地址进行判断，避免攻击者恶意调用合约

建议项目方上线前进行多次审计，避免出现审计步骤缺失

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**零时科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/281979](/post/id/281979)

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
* ##### [损失8800万美元，加密协议BonqDAO被攻击事件分析](/post/id/286163)

  2023-02-09 15:30:28
* ##### [分布式资本创始人4200万美金资产被盗分析及追踪工作](/post/id/283685)

  2022-11-29 16:00:36
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
* [攻击步骤](#h2-1)
* [漏洞核心](#h2-2)
* [资金来源及去向](#h2-3)
* [总结及建议](#h2-4)

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