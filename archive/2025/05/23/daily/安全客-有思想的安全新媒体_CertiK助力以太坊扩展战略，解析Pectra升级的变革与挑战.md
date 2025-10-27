---
title: CertiK助力以太坊扩展战略，解析Pectra升级的变革与挑战
url: https://www.anquanke.com/post/id/307428
source: 安全客-有思想的安全新媒体
date: 2025-05-23
fetch_date: 2025-10-06T22:26:59.388078
---

# CertiK助力以太坊扩展战略，解析Pectra升级的变革与挑战

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

# CertiK助力以太坊扩展战略，解析Pectra升级的变革与挑战

阅读量**76217**

发布时间 : 2025-05-22 18:00:15

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近期，美国知名金融科技媒体Benzinga发表文章，深入探讨以太坊Pectra升级的变革性影响，并特别引用了CertiK对潜在风险的权威分析，特别是EIP-7702引入的全新信任模型变化。此次升级不仅重新定义了EOA与智能合约的交互方式，还涉及质押模型优化和数据吞吐量的提升，为以太坊下一阶段的扩展性奠定了基础。

作为以太坊生态安全的重要贡献者，在以太坊扩展性战略的另一里程碑式事件中，CertiK也助其取得了重要进展。近日，[CertiK荣膺以太坊基金会2025年第一季度两项研究资助](https://mp.weixin.qq.com/s?__biz=MzU5OTg4MTIxMw==&mid=2247504168&idx=1&sn=a8c46dc247c8131e24040c5fb463f6a7&scene=21#wechat_redirect)，用于推进zkEVM形式化验证技术的研究与应用。

作为最大的Web3.0安全公司，CertiK的分析不仅限于问题识别，更致力于为开发者提供切实可行的解决方案。我们**建议开发者尽快更新代码库，避免继续将EOA视为被动账户的逻辑，采用业界标准的重入保护措施和更严谨的逻辑约束，以有效降低潜在攻击面**。

面对Pectra升级带来的信任模型变革，开发者需要重新审视其智能合约的信任模型，确保合约逻辑能够充分应对EOA执行能力的变化。CertiK将继续致力于为全球开发者提供最前沿的安全保护，与开发者、研究者和整个Web3.0社区携手，共同塑造Web3.0的未来。

以下为报道全文：

**以太坊Pectra升级正式上线：需要了解的关键变化**

以太坊于5月7日正式激活了备受期待的Pectra升级，这是自去年Dencun分叉以来网络发展的关键一步。

此次升级于美国东部时间6:05正式生效，并在10分钟后完成最终确认。

Pectra引入了对以太坊协议的多项重大改动，其中最引人注目的是EIP-7702。这一改动重新定义了外部账户（EOA）与智能合约的交互方式。

首次实现了常规用户钱包在保持相同地址的情况下执行合约逻辑，为构建更智能、更灵活的用户账户铺平了道路。

EIP-7702被视为实现全面账户抽象的基础，允许用户批量处理交易、跳过手动代币授权，并在不同应用间实现无缝交互。

此次升级还涉及验证者模型的调整。EIP-7251将每个验证者的质押上限从32 ETH提高到2,048 ETH，使得大额质押者能够更高效地整合资本，优化协议运行效率并改善奖励分配。

此外，EIP-7691将每个区块的Blob（一种专门用于存储大数据的临时数据结构）数据块数量从3个提升至6个，显著提高了Layer 2的吞吐量，并降低了Rollup交易的成本。

然而，Pectra升级也并非没有挑战。麻省理工学院教授、Optimum联合创始人Muriel Médard在发给Benzinga的一份声明中指出，随着Pectra的上线，以太坊面临的新瓶颈是网络带宽。

“在Pectra上线后，带宽成为了关键的限制因素，特别是由于Blob数据块需要在点对点网络中进行传播，”她表示。“以太坊能否高效且可预测地传播数据将决定其扩展能力。”

Médard补充道，随着Blob数据块的规模不断扩大，仅仅提高平均带宽已不足够，减少数据传播的可变性同样至关重要。

“不可预测性会削弱Rollup和应用的整体可靠性，这已经成为核心基础设施问题，”她强调道。

与此同时，安全专家也对EIP-7702可能带来的深远影响表达了担忧。

区块链安全公司CertiK在[一篇博客文章](https://www.certik.com/resources/blog/pectras-eip-7702-redefining-trust-assumptions-of-externally-owned-accounts)中警告称，这一升级打破了长期以来“EOA无法执行合约代码”的假设。

因此，那些依赖tx.origin == msg.sender等旧有逻辑进行重入保护或闪电贷防护的智能合约，可能因此暴露在新的风险之下。

“信任模型已经发生了变化，”CertiK在文章中指出。“EOA现在能够执行逻辑，这为未预料到这一特性的合约引入了全新的风险向量。”

CertiK还引用了今年3月BSC引入类似Pascal升级后出现的案例，称其观察到了一些利用此类假设漏洞的可疑交易。

为此，开发者被敦促尽快更新代码库，避免继续将EOA视为被动账户的逻辑。取而代之，应采用业界标准的重入保护措施和更加严谨的逻辑约束，以减少潜在攻击面。

尽管面临这些挑战，Pectra升级仍被广泛视为以太坊迈向下一阶段的重要里程碑。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**CertiK**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307428](/post/id/307428)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全，以太坊升级，以太坊，Web3](/tag/%E5%AE%89%E5%85%A8%EF%BC%8C%E4%BB%A5%E5%A4%AA%E5%9D%8A%E5%8D%87%E7%BA%A7%EF%BC%8C%E4%BB%A5%E5%A4%AA%E5%9D%8A%EF%BC%8CWeb3)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t01cb821c171a2ee685.png)CertiK

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t01c1c3406c6fc8955f.png)

[![](https://p2.ssl.qhimg.com/t01cb821c171a2ee685.png)](/member.html?memberId=149826)

[CertiK](/member.html?memberId=149826)

这个人太懒了，签名都懒得写一个

* 文章
* **18**

* 粉丝
* **0**

### TA的文章

* ##### [重塑Web3信任：CertiK首席商务官在Proof of Talk深入探讨行业长期安全机制](/post/id/308466)

  2025-06-16 11:26:31
* ##### [Proof of Talk专访CertiK联创顾荣辉：全周期安全方案护航Web3生态](/post/id/308375)

  2025-06-12 13:33:41
* ##### [CertiK联创顾荣辉做客纽交所，剖析Bybit与Coinbase事件暴露的Web3安全新挑战](/post/id/307779)

  2025-05-27 09:59:25
* ##### [CertiK荣获以太坊基金会两项资助，领跑zkEVM形式化验证](/post/id/307384)

  2025-05-26 11:46:21
* ##### [韩媒聚焦Lazarus攻击手段升级，CertiK联创顾荣辉详解应对之道](/post/id/307280)

  2025-05-23 15:02:30

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