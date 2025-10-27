---
title: 零时科技 || Arbitrum链上Jimbos Protocol项目受到黑客攻击，攻击者获利约 776 万美元
url: https://www.anquanke.com/post/id/288931
source: 安全客-有思想的安全新媒体
date: 2023-05-31
fetch_date: 2025-10-04T11:37:53.861104
---

# 零时科技 || Arbitrum链上Jimbos Protocol项目受到黑客攻击，攻击者获利约 776 万美元

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

# 零时科技 || Arbitrum链上Jimbos Protocol项目受到黑客攻击，攻击者获利约 776 万美元

阅读量**331830**

发布时间 : 2023-05-30 15:47:54

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## 事件背景

零时科技区块链安全情报平台监控到消息，北京时间2023年5月28日，Arbitrum链上Jimbos Protocol项目受到黑客攻击，攻击者获利约 776 万美元。

攻击者地址为：

0x102be4bccc2696c35fd5f5bfe54c1dfba416a741

被盗资金通过跨链转移至ETH链后转移至地址：

0x5F3591e2921D5c9291F5b224E909aB978A22Ba7E

零时科技安全团队及时对此安全事件进行分析。

## 攻击步骤

1. 攻击者通过闪电贷借出 10,000 WETH
   ![image]()
2. 攻击者在交易池中使用 WETH 兑换获得大量 JIMBO 代币
   ![image]()
3. 攻击者向 JimboController 合约转移 100 JIMBO 代币
   ![image]()
4. 攻击者调用 shift 函数更新交易池，将合约中WETH与 JIMBO 代币转移至交易池中，此时JIMBO 代币价格被恶意拉高
   ![image]()
5. 攻击者使用更新后的价格进行兑换
   ![image]()
6. 攻击者重复上述步骤，几乎将池子掏空后获利离场。
   ![image]()
   此笔攻击中攻击者共获利约 4,048 ETH，约为 7,763,360 美元

## 核心漏洞

JimboController合约中shift()函数可以更新交易池流动性，但是此函数中没有限制调用者身份，任何人都可以调用此函数执行更新交易池操作，重新添加流动性时会将合约中的所有余额转移至交易池，并且重新添加流动性时没有对代币价格进行判断，因此攻击者能够将代币价格恶意拉高后通过调用函数使得JimboController合约接盘，从而获利。
![image]()

## 资金来源及流向

### 资金来源

攻击地址初始手续费通过跨链转入
![image]()

### 资金流向

攻击者将获利资金通过跨链合约转移至ETH链对应地址，之后将资金转移至地址 0x5F3591e2921D5c9291F5b224E909aB978A22Ba7E，目前资金仍在此地址未移动。
![image]()

## 总结及建议

此次攻击是由于代币价格存在滑点，并且合约中在更新交易池函数中没有用户权限并且没有对于价格滑点进行判断，导致攻击者能够恶意操纵代币价格，并且将合约中ETH也转入交易池后通过代币兑换获利。

### 安全建议

建议对合约中更新交易池函数设置用户权限

建议在更新交易池时增加对于代币价格判断的条件，避免出现滑点过大时币价被恶意操纵

建议项目方上线前进行多次审计，避免出现审计步骤缺失

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**零时科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/288931](/post/id/288931)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [攻击事件](/tag/%E6%94%BB%E5%87%BB%E4%BA%8B%E4%BB%B6)

**+1**8赞

收藏

![](https://p0.ssl.qhimg.com/t01482eaf8414a7973c.png)零时科技

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [事件背景](#h2-0)
* [攻击步骤](#h2-1)
* [核心漏洞](#h2-2)
* [资金来源及流向](#h2-3)
  + [资金来源](#h3-4)
  + [资金流向](#h3-5)
* [总结及建议](#h2-6)
  + [安全建议](#h3-7)

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