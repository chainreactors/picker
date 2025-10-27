---
title: TrustSwap 攻击事件分析
url: https://www.anquanke.com/post/id/282575
source: 安全客-有思想的安全新媒体
date: 2022-11-09
fetch_date: 2025-10-03T22:01:46.472388
---

# TrustSwap 攻击事件分析

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

# TrustSwap 攻击事件分析

阅读量**355761**

发布时间 : 2022-11-08 10:30:07

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 事件背景

零时科技区块链安全情报平台监控到消息，北京时间2022年10月27日，TrustSwap项目遭受黑客攻击，影响金额至少约779万美元(880.2554ETH和6429327.65DAI)。此外，本次攻击还盗取了CAW和TSUKA代币，价值约550万美元。攻击者地址为 0x161cebb807ac181d5303a4ccec2fc580cc5899fd，漏洞合约为0x48D118C9185e4dBAFE7f3813F8F29EC8a6248359。零时科技安全团队及时对此安全事件进行分析。

## 漏洞核心

攻击者调用LockToken函数锁定令牌获得id用于后续攻击

![]()

攻击者通过调用LockToken合约中migrate函数迁移流动性，此时传入的id值为之前锁定令牌时获得的id，因此攻击者可以通过对于lockerc20地址的验证

![]()

![]()

![]()

进行资金迁移之后将剩余资金返回LockToken合约

![]()

![]()

由于新建池子的价格由用户自己控制，攻击者通过设置sqrtPricex96造成价格差

![]()

在V2中交易对的余额

![]()

在V3中计算获得的应添加的数量

![]()

将剩余的资金退还给攻击者

![]()

在这一步攻击中攻击者获利约601ETH

![]()

## 资金来源及流向

攻击者初始资金由FixedFloat转入

![]()

**资金流向**

攻击者将资金转移至地址 0xBa399a2580785A2dEd740F5e30EC89Fb3E617e6E 目前资金无进一步移动

![]()

![]()

## 总结及建议

本次攻击是由于攻击者能够通过执行锁定代币获得ID来绕过检测，将流动性转移至攻击者控制的V3交易对中，并且新的交易对创建的池子价格由攻击者控制，资金迁移后剩余资金转移给用户，因此攻击者能够设置池子价格在资金迁移后获得巨额剩余。

**安全建议**

建议对于转移流动性时添加对于新池子的初始价格的判断，避免在进行资金迁移时有巨额资金剩余。

建议项目方上线前进行多次审计，避免出现审计步骤缺失

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**零时科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/282575](/post/id/282575)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [区块链](/tag/%E5%8C%BA%E5%9D%97%E9%93%BE)

**+1**1赞

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

* ##### [攻击者获利约302万美元，Orion Protocol被攻击事件分析](/post/id/286259)

  2023-02-14 16:30:42
* ##### [披露！币圈空投黑吃黑“脏”手段，“偷家”这招儿真有你的](/post/id/284309)

  2023-01-04 17:30:27
* ##### [iDASH 2022隐私计算大赛——字节跳动Jeddak Team获得佳绩](/post/id/284269)

  2022-12-19 17:30:53
* ##### [Glupteba恶意软件在被谷歌中断后重新活跃](/post/id/284418)

  2022-12-19 11:15:03
* ##### [Victor the Fortune攻击事件分析](/post/id/282574)

  2022-11-07 10:30:11
* ##### [DPC攻击复现](/post/id/281186)

  2022-10-09 11:00:17
* ##### [BXH攻击事件分析](/post/id/281172)

  2022-10-08 11:00:51

### 热门推荐

文章目录

* [事件背景](#h2-0)
* [漏洞核心](#h2-1)
* [资金来源及流向](#h2-2)
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