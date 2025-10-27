---
title: 新型 Web3 攻击利用交易模拟窃取加密货币
url: https://www.anquanke.com/post/id/303476
source: 安全客-有思想的安全新媒体
date: 2025-01-15
fetch_date: 2025-10-06T20:07:21.054879
---

# 新型 Web3 攻击利用交易模拟窃取加密货币

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

# 新型 Web3 攻击利用交易模拟窃取加密货币

阅读量**63989**

发布时间 : 2025-01-14 10:37:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/new-web3-attack-exploits-transaction-simulations-to-steal-crypto/>

译文仅供参考，具体内容表达以及含义原文为准。

![Crypto hacker]()

威胁者正在使用一种名为 “交易模拟欺骗 ”的新策略来窃取加密货币，其中一次攻击成功窃取了 143.45 个以太坊，价值约 46 万美元。

ScamSniffer 发现的这次攻击突出了现代 Web3 钱包中使用的交易模拟机制的一个缺陷，该机制旨在保护用户免受欺诈和恶意交易的侵害。

**攻击的原理**

交易模拟是一项允许用户在签署和执行区块链交易之前预览其预期结果的功能。

该功能旨在帮助用户验证交易的结果，如转移的加密货币数量、气体费用和其他交易成本，以及其他链上数据变化，从而提高安全性和透明度。

攻击者会诱使受害者访问一个模仿合法平台的恶意网站，该网站会启动看似 “索赔 ”的功能。交易模拟显示，用户将收到一小笔 ETH。

但是，由于模拟和执行之间存在时间延迟，攻击者可以改变链上合约状态，从而改变交易被批准后的实际情况。

受害者相信了钱包的交易模拟结果，签署了交易，从而允许网站将其钱包中的所有加密货币清空，并将其发送到攻击者的钱包中。

![Attack flow]()
**攻击流程**
来源：ScamSniffer

ScamSniffer 强调了一个实际案例，受害者在状态变化 30 秒后签署了欺骗性交易，结果损失了所有资产（143.35 ETH）。

ScamSniffer 警告说：“这种新的攻击载体代表了网络钓鱼技术的重大演变。”

ScamSniffer警告说：“攻击者现在不再依靠简单的欺骗，而是利用用户所依赖的可信钱包安全功能。这种复杂的方法使侦测变得特别具有挑战性。”

![Initial simulation (top) and manipulated transaction (bottom)]()
**初始模拟（上）和操纵交易（下）**
来源：ScamSniffer

区块链监测平台建议Web3钱包降低模拟刷新率，使其与区块链区块时间相匹配，在关键操作前强制刷新模拟结果，并添加过期警告，提醒用户注意风险。

从用户的角度来看，这种新的攻击说明了为什么不应该相信钱包模拟。

加密货币持有者应谨慎对待模糊网站上的 “免费认领 ”提议，只信任经过验证的 dApp。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/new-web3-attack-exploits-transaction-simulations-to-steal-crypto/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303476](/post/id/303476)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/new-web3-attack-exploits-transaction-simulations-to-steal-crypto/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/new-web3-attack-exploits-transaction-simulations-to-steal-crypto/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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