---
title: DeFi 协议 DittoETH 补丁中发现大规模折扣费漏洞
url: https://www.anquanke.com/post/id/300071
source: 安全客-有思想的安全新媒体
date: 2024-09-14
fetch_date: 2025-10-06T18:24:09.946570
---

# DeFi 协议 DittoETH 补丁中发现大规模折扣费漏洞

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

# DeFi 协议 DittoETH 补丁中发现大规模折扣费漏洞

阅读量**131821**

发布时间 : 2024-09-13 15:10:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 克里斯托弗·罗克，文章来源： Cointelegraph

原文地址：<https://cointelegraph.com/news/code4rena-discount-fee-exploit-defi?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound>

译文仅供参考，具体内容表达以及含义原文为准。

去中心化审计平台 Code4rena 在即将推出的 DittoETH 算法稳定币平台补丁中发现了一个漏洞。该漏洞将允许存入大量代币的用户赚取超额利润，增加协议中的坏账，并最终损害其生存能力。

这一发现意味着该漏洞不会添加到 DittoETH 的生产版本中，因为它已在较新的测试版本中通过缓解措施被删除。

Web3 教育公司 Rare Skills 的星探 Block 在 X 上报告了这一发现。

根据其文件，Code4rena 是一个众包审计平台。参与者分为三组：赞助商、看守和评委。

赞助商是 Web3 协议，提供奖品以换取漏洞的发现。典狱长相互竞争以发现漏洞以换取奖金。法官裁决发起人和看守者之间关于漏洞是否真实以及其严重程度的争议。

Code4rena 声称它不举办“漏洞县”比赛，它声称这涉及“尽快找到最大的 [漏洞] 的竞赛”。相反，“每个付出努力并发现有效的东西的人都会得到回报。

根据 Block 的说法，该漏洞是由 Code4rena 典狱长あああああ（日语中的“aaaaa”）发现的。DittoETH 团队最初不相信该漏洞是真实的，但后来在 Aaaaa 提供进一步证据后放弃了反对意见。

该漏洞包括向 DittoETH 的 yDUSD 金库中的储户分配稳定币奖励的机制存在错误。

用户可以将协议的原生稳定币 dUSD 添加到此保险库中以获得收益。此收益来自在实际代币价格与 oracle 提供的价格相差时在平台上产生的“折扣费用”。该系统的目的是激励流动性提供者在市场承压时期增加流动性。

尽管名称中包含“fee”一词，但任何人都不需要支付折扣费用。相反，它们作为新铸造的代币支付并发送到 yDUSD 金库。每当发生这种情况时，平台的相应债务也会与该金额成正比地增加。

典狱长发现，“matchIsDiscounted”函数中的数学缺陷可能会从少量交易量中产生大量债务，这与协议仅在市场压力时期支付这些费用的预期设计相矛盾。

Block 在他们的报告中指出，“关键是，只有当贴现金额超过总债务的某个阈值时，才会发生第 6-9 步。当它们确实发生时，它们会根据系统的整个债务产生新的债务，而不仅仅是贴现金额。这就是漏洞的根本原因所在，因为小额贴现交易可能导致不成比例的巨额新债务产生和代币铸造。

7 月 15 日，Aaaaa 在该项目的 github 上发布了对漏洞利用的解释。作为回应，DittoETH 团队成员和至少一名 Code4rena 法官最初声称，攻击者将无法制造坏账，因为其他成员会加入资金池并“稀释”攻击者的收益。

然而，Aaaaa 回答说，攻击者不能被稀释，因为 [d] eposits 不会影响股票可以索取多少资产。

Aaaaa 还在 Foundry 中编写了一个测试，模拟了攻击和“其他用户在保险库中存入了大量资金”。他们邀请团队成员在自己的设备上运行测试。

据报道，测试显示攻击者获利 20,454.54 美元，为协议创造了等于该金额的新债务。据推测，这种攻击可能会重复以获得更大的收益。

7 月 12 日，评委 Hans Friesse 将提交的内容标记为“令人满意”，表明 Aaaaa 将获得该奖项团队。DittoETH 代表也放弃了他们的反对意见，表示“nvm 这是有效的，很好的发现！

审计涉及协议代码的非生产副本。但是，如果错过了这个漏洞，它可能会被部署到区块链上并在野外被利用。

如果在部署漏洞之前没有发现漏洞，DeFi 漏洞可能是毁灭性的。4 月，Ronin 游戏网络桥在升级引入新漏洞后被耗尽了 980 万美元。今年 3 月，DeFi 平台 Unizen 的用户因攻击者发现平台生产副本中的“批准”漏洞而损失超过 200 万美元。

本文翻译自 Cointelegraph [原文链接](https://cointelegraph.com/news/code4rena-discount-fee-exploit-defi?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300071](/post/id/300071)

安全KER - 有思想的安全新媒体

本文转载自:  [Cointelegraph](https://cointelegraph.com/news/code4rena-discount-fee-exploit-defi?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound)

如若转载,请注明出处： <https://cointelegraph.com/news/code4rena-discount-fee-exploit-defi?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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