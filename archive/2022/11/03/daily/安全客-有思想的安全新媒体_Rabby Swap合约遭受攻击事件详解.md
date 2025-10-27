---
title: Rabby Swap合约遭受攻击事件详解
url: https://www.anquanke.com/post/id/281760
source: 安全客-有思想的安全新媒体
date: 2022-11-03
fetch_date: 2025-10-03T21:36:11.018373
---

# Rabby Swap合约遭受攻击事件详解

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

# Rabby Swap合约遭受攻击事件详解

阅读量**180127**

发布时间 : 2022-11-02 12:00:52

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 0x1 背景

2022年10月12日，Rabby Swap合约中存在疑似任意用户资产转移漏洞。Rabby Swap官方表示，如果有使用，请撤销所有链上所有现有的 Rabby Swap 批准。对于没有使用过 Swap 的人来说，钱包安全且不受影响。零时科技安全团队及时对该事件进行分析。

## 0x2 攻击交易信息

*攻击者地址：*
0xb687550842a24D7FBC6Aad238fd7E0687eD59d55

*攻击者合约*：

0x9682f31b3f572988f93c2b8382586ca26a866475

Rabby Swap合约（漏洞合约未开源）：

0x6eb211caf6d304a76efe37d9abdfaddc2d4363d1

*攻击交易之一*：

0x366df0c20e00666749b16ae00475b3c41834dc659ebb29e059aa9bffa892c038

*受害者地址之一*：

0x0753cfbc797abfce05abaacbb1e6ae032feb5f1d

*授权被盗HOP Token 代币地址*：

0xc5102fE9359FD9a28f877a67E36B0F050d81a3CC

## 0x3 攻击步骤

分析攻击者交易，可以明确攻击者交易并不复杂，通过部署攻击合约，调用攻击合约0x8f965d0e签名方法进行攻击获利。

![]()

攻击者共部署两份合约，进行了27次交易步骤相同的攻击，这里选一笔交易进行详细分析。

0x366df0c20e00666749b16ae00475b3c41834dc659ebb29e059aa9bffa892c038

![]()

通过攻击交易来看，此次攻击似乎很简单，攻击合约给漏洞合约转移0枚USDT，之后将用户的资金转移至攻击者地址。由于官方漏洞合约未开源，并不能看到细节。但通过官方合约审计报告及调用合约签名可以明确，本次攻击主要调用的漏洞方法为\_swap。

**交易数据如下：**

![]()

\_swap代码片段如下：

![]()

![]()

通过交易数据分析，可以得出以下\_swap方法传参：
IERC20 srcToken: 0xdac17f958d2ee523a2206206994597c13d831ec7(USDT)
uint256 amount: 0
IERC20 dstToken: 0x9682f31b3f572988f93c2b8382586ca26a866475(攻击合约)
uint256 minReturn: 4660
address dexRouter: 0xc5102fe9359fd9a28f877a67e36b0f050d81a3cc(HOP)
address dexSpender: 0xc5102fe9359fd9a28f877a67e36b0f050d81a3cc(HOP)
bytes calldata data:
0000000000000000000000000000000000000000000000000000000000000100
00000000000000000000000000000000000000000000000000000183c1c270d7
0000000000000000000000000000000000000000000000000000000000000128
23b872dd(transferFrom(address,address,uint256))
0000000000000000000000000753cfbc797abfce05abaacbb1e6ae032feb5f1d(受害者地址)
000000000000000000000000b687550842a24d7fbc6aad238fd7e0687ed59d55(攻击者地址)
00000000000000000000000000000000000000000000001982589c49e57f7f8d(转账资金470.56)
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000002
000000000000000000000000dac17f958d2ee523a2206206994597c13d831ec7
000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
869584cd00000000000000000000000010000000000000000000000000000000
0000001100000000000000000000000000000000000000000000005f5265d161
uint256 deadline: 时间戳

根据以上交易的传参，继续分析\_swap内部逻辑（可以对照代码来看）。

首先require判断时间戳及传入的dexRouter、dexSpender满足条件；

之后将srcToken、dstToken计算得到srclsEth、dstlsEth均为false；

条件判断执行srcToken.safeTransferFrom(攻击者合约，漏洞合约，转移资金0)；

最后执行了最重要的一步操作，dexRouter.functionCallWithValue(data,value)。从上述\_swap方法传参可以知道，data数据进行了转账，攻击者完成获利；

在随后的逻辑计算和判断中，由于dstToken参数攻击者可控，所以攻击者传入攻击合约进行资金转移及判断，最终绕过条件顺利执行\_swap方法，成功获利。

## 0x4 攻击核心

通过上述攻击交易的详细分析，可以发现攻击者成功的原因主要是\_swap方法中多个参数可控，包括dstToken地址可传入任意合约地址进行资金转移；data数据未进行严格判断导致可传入攻击者构造的恶意转账；amount资金转移的数量没有进行区间限制。除此之外，Rabby Swap合约对于用户的资金授权未进行妥善处理，最终导致用户资金被盗。

## 0x5 事件后续

此次攻击事件中，攻击者获取了多种代币，并将所有代币兑换为114枚ETH和179枚BNB，价值19万美元，并将资金转入Tornado.Cash混币平台，攻击者初始资金（手续费）也来自Tornado.Cash。

发生攻击事件之后，Rabby Swap官方呼吁用户尽快撤销多条链上对于Rabby Swap合约的授权，以下为合约地址：

ETH: 0x6eb211caf6d304a76efe37d9abdfaddc2d4363d1

Polygon: 0xf23b0f5cc2e533283ea97f7b9245242b8d65b26b

BNB: 0xf756a77e74954c89351c12da24c84d3c206e5355

Avalanche: 0x509f49ad29d52bfaacac73245ee72c59171346a8

目前Rabby Swap官方正在追踪资金并表示会提供解决方案。

## 0x6 总结及安全建议

本次分析主要根据审计报告中代码进行分析，由于合约未开源，合约代码具体是否完全相同不得而知，从攻击交易分析来看，本次攻击事件中只要有两个方面的风险：第一对于Rabby Swap合约传参未进行严格判断导致部分参数可控；第二Rabby Swap合约未对用户在本合约的授权资金数量进行精确计算，导致使用Rabby Swap合约后，仍有授权资金。**对于以上安全事件，零时科技安全团队给出以下建议：**

合约上线前应对方法传参进行严格判断及测试，避免参数可控引起安全风险；
合约上线前进行多次安全审计，避免出现审计步骤缺失；
合约对于用户资金授权应尽量避免授权最大值，如需授权最大值，则应严格判断合约逻辑避免被其他人利用。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**零时科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/281760](/post/id/281760)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [风险分析](/tag/%E9%A3%8E%E9%99%A9%E5%88%86%E6%9E%90)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01482eaf8414a7973c.png)零时科技

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51
* ##### [当数字世界的“万能钥匙”被滥用，谁来守护核心资产？火山的 MCP 安全授权新范式](/post/id/311597)

  2025-08-28 09:50:41
* ##### [Python代码保护之重置操作码映射的攻与防探究（一）](/post/id/311484)

  2025-08-26 10:49:47
* ##### [广汽集团×火山引擎：出海合规助力企业新增长](/post/id/311498)

  2025-08-26 10:17:09
* ##### [从技术到安全：中科固源拆解车载以太网的演进路径与防护策略](/post/id/310094)

  2025-08-21 21:48:41
* ##### [智能体防御 | 一文了解3种系统提示词加固方法](/post/id/311279)

  2025-08-18 16:34:50

### 热门推荐

文章目录

* [0x1 背景](#h2-0)
* [0x2 攻击交易信息](#h2-1)
* [0x3 攻击步骤](#h2-2)
* [0x4 攻击核心](#h2-3)
* [0x5 事件后续](#h2-4)
* [0x6 总结及安全建议](#h2-5)

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