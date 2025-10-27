---
title: Victor the Fortune攻击事件分析
url: https://www.anquanke.com/post/id/282574
source: 安全客-有思想的安全新媒体
date: 2022-11-08
fetch_date: 2025-10-03T21:54:08.672864
---

# Victor the Fortune攻击事件分析

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

# Victor the Fortune攻击事件分析

阅读量**346571**

发布时间 : 2022-11-07 10:30:11

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 事件背景

零时科技区块链安全情报平台监控到消息，北京时间2022年10月27日，BSC链上Victor the Fortune 合约受到黑客闪电贷攻击，攻击者已获利约5.8万美元，耗尽了流动资金池，攻击者地址为0x57c112cf4f1e4e381158735b12aaf8384b60e1ce，零时科技安全团队及时对此安全事件进行分析。

## 攻击步骤

1.攻击者通过闪电贷借出约100,000 USDT

![]()

2.将借出的USDT兑换为77,853 VTF

![]()

3.调用updateUserBalance()函数计算获得奖励

![]()

4.调用transfer函数将资金全部转移至 地址 0x1dd557415a0ddea7d3e56f49c78d54ebbf31f569

![]()

5.调用updateUserBalance()函数获得奖励

![]()

6.重复执行第四步和第五步，最后共获得 499,803,157 VTF

![]()

![]()

7.将获得的VTF兑换获得 158,450 USDT

![]()

归还闪电贷后共获利 58,450 USDT

![]()

## 漏洞核心

攻击者通过调用transfer函数进行转账，在转账函数中调用了updateUserBalance()函数，由于此时userBalanceTime[user]为0会将当前时间赋值给userBalanceTime[user]。

![]()

之后调用updateUserBalance()，当userBalanceTime大于0时会调用 getUserCanMint函数计算奖励值

![]()

在getUserCanMint函数中计算返回值是用户的余额除以常数乘当前时间与用户开始时间的时间差，由于没有设置最小时间差，因此在很短时间调用函数也可以获得奖励。

![]()

由于调用一次updateUserBalance()函数后会更新时间，攻击者通过调用transfer函数将资金转移至一个新的地址，再次调用updateUserBalance()函数可以继续获利，并且当攻击者地址资金增加时获得的奖励也随着增加，攻击者通过重复以上步骤获得奖励逐渐增加直到将池子掏空。

## 总结及建议

此次攻击是由于合约中的计算奖励函数的算法只与用户地址余额和时间差有关，攻击者通过先调用转账获得用户初始时间，之后调用获得奖励的函数，通过这两个函数调用过程中的时间差计算获得奖励。通过多次转账计算获得奖励使得资金累加，最后将池子中代币几乎掏空。

****安全建议****

建议对于计算获得奖励时设置最小时间差，避免攻击者通过短时间多次调用函数获利。

建议项目方上线前进行多次审计，避免出现审计步骤缺失

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**零时科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/282574](/post/id/282574)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [区块链](/tag/%E5%8C%BA%E5%9D%97%E9%93%BE)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t01482eaf8414a7973c.png)零时科技

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [攻击者获利约302万美元，Orion Protocol被攻击事件分析](/post/id/286259)

  2023-02-14 16:30:42
* ##### [披露！币圈空投黑吃黑“脏”手段，“偷家”这招儿真有你的](/post/id/284309)

  2023-01-04 17:30:27
* ##### [iDASH 2022隐私计算大赛——字节跳动Jeddak Team获得佳绩](/post/id/284269)

  2022-12-19 17:30:53
* ##### [Glupteba恶意软件在被谷歌中断后重新活跃](/post/id/284418)

  2022-12-19 11:15:03
* ##### [TrustSwap 攻击事件分析](/post/id/282575)

  2022-11-08 10:30:07
* ##### [DPC攻击复现](/post/id/281186)

  2022-10-09 11:00:17
* ##### [BXH攻击事件分析](/post/id/281172)

  2022-10-08 11:00:51

### 热门推荐

文章目录

* [事件背景](#h2-0)
* [攻击步骤](#h2-1)
* [漏洞核心](#h2-2)
* [总结及建议](#h2-3)

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