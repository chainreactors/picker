---
title: BlockSec 登上国际刑警组织技术论坛讲台，分享 Telegram 诈骗生态研究
url: https://mp.weixin.qq.com/s/JR5JqDOEAqQbWiWuMej1cw
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:45:11.863146
---

# BlockSec 登上国际刑警组织技术论坛讲台，分享 Telegram 诈骗生态研究

# BlockSec 登上国际刑警组织技术论坛讲台，分享 Telegram 诈骗生态研究

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ibKZs4HxyqtTUJibmiaaDgadp610m0ahHpndAtK8Y4B9dAlMY539eDia191DN7avhWFrMQOav9ny1Miaic7wEibdzWibq3Jjev4oz6kds90U3A4sicM/640?wx_fmt=gif&from=appmsg)

2026 年 9 月 29 日至 30 日，国际刑警组织（INTERPOL）创新中心主办的新技术论坛（New Technologies Forum 2026）在奥地利维也纳举行。

BlockSec 联合创始人、香港中文大学副教授周亚金受邀出席，并作题为「Uncovering Telegram-Based Guarantee Platforms and the Fraud-as-a-Service Ecosystem」的专题分享。

周亚金教授向来自全球的执法人员、检察官与研究者介绍团队在 Telegram 担保平台与「诈骗即服务」（Fraud-as-a-Service）生态方面的最新研究成果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqtXyNIznbl0vS7iauoxOZWjvK6jhYV0NXOGsnjKBG0rZbavibcF4tC73RPGIpFYRy2kQGN140EYaTszveE10g6iavLYfWGor2BFTg/640?wx_fmt=png&from=appmsg)

图 1：INTERPOL 新技术论坛 2026

**登上INTERPOL 讲台的唯一亚太区域安全公司**

INTERPOL 国际刑警组织拥有 196 个成员国，是全球规模最大的国际警务合作组织。设于新加坡的 INTERPOL 创新中心，专门研判新兴技术对全球执法的影响，新技术论坛是它面向各成员国执法机构的重要活动。

本届论坛以「NextGen Investigation: Decoding Emerging Technologies」为主题，由巴伐利亚州司法部与维也纳 Complexity Science Hub 共同支持，INTERPOL 创新中心主任 Toshinobu Yasuhira、巴伐利亚州司法部长 Georg Eisenreich 致开幕辞。

两天议程围绕「去中心化平台」与「去中心化账本的未来」展开，台上台下是各国监管、警方、检察机关、法证机构的一线调查人员，以及受邀的研究者和产业代表。

在本届论坛的讲者名单中，BlockSec 是唯一的亚太区域公司。我们很荣幸把 BlockSec 团队在反诈反洗钱一线的研究带到 INTERPOL 的讲台，与各国执法同行交流。

**Jessica 可能根本不存在**

当地时间 9 月 30 日下午，周亚金教授的分享从一个真实案例切入。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ibKZs4Hxyqv6ganzRqP2cXob7IYiaOvRstGibvwUtlEiaGFY3mlpWYCrbMnWtmSwk7RPlwIYEqgbDzZZpu6d2208xr6h3noS05ufStVxy3CkibQ/640?wx_fmt=jpeg)

图 2：周亚金教授现场分享

这个案例曾在美国引发广泛关注。2022 年 7 月，ABC7 电视台报道旧金山湾区一名投资者在加密货币骗局中损失 120 万美元，当时加州的同类案件数量正在成倍增长。

同年 9 月，《福布斯》以「一个人如何在加密货币『超级骗局』中损失一百万美元」为题发表长篇调查，基于受害者 CY 提供的长达 27.1 万字、480 页的 WhatsApp 聊天记录，逐日还原了骗局的每一步；2023 年 12 月，CNN 在关于东南亚诈骗园区的深度调查中再次以 CY 为核心案例。

此后几年，西方媒体和公众谈起「杀猪盘」，CY 的故事一直是被引用最多的案例之一。

一个自称「Jessica」的账号在 WhatsApp 上主动联系 CY，说在通讯录里看到他的号码，以为是旧同事。彼时 CY 的父亲正在临终关怀阶段，他处于最脆弱的时期。

对方每天和他聊天，逐步建立信任，然后以帮他承担父亲后事费用为由，引导他在一个虚假交易 App 上投资。

两个月内，CY 卖掉了股票，动用了三十年的积蓄和女儿的教育基金，向发小借钱，还以房子抵押贷款，最终损失 120 万美元，其中四分之一是借来的。「Jessica」随后消失，CY 把自己送进了医院。

周教授在现场提问：Jessica 真的是一个人吗？一个人能同时做到精准筛选受害者、社交工程、搭建虚假投资平台、准备支付通道、完成资金清洗这一整套事情吗？

显然不能。「Jessica」背后是一个成熟的 Fraud-as-a-Service 市场。账号与支付通道、被窃取的个人数据、话术与照片、洗钱服务，都能作为独立模块在市场上买到。诈骗者按需采购、组装，就能运转一个完整的诈骗操作。实际上，甚至可能根本不存在一个真实的 Jessica。

**犯罪分子也需要信任：Telegram 上的担保平台**

犯罪分子之间同样面临信任问题：买卖双方互不相识，谁先付款谁就可能被骗。解决这个问题的，是运行在 Telegram 上、以 TRON USDT 结算的担保平台。

担保平台的机制是「押金加仲裁」：服务提供方向平台缴纳押金（通常为 USDT）成为商户，交易发生纠纷时由平台裁定责任方，并用押金补偿受损一方，平台从中收取费用。

它的架构可以类比电商平台：Telegram 频道相当于平台首页与商品搜索系统，负责发布规则、公示官方押金地址、撮合买卖双方；每个商户的 Telegram 群相当于一家独立店铺，商户在群内发布服务与交易规则，潜在买家进群询价。

2025 年 5 月，Telegram 下架了与「新币」（Xinbi）担保平台相关的多个频道和群组；2026 年 3 月，英国对 Xinbi 相关实体及 TRON 地址实施制裁。周教授在现场抛出第二个问题：封几个频道、制裁几个地址，真的有效吗？

**16 个平台、71.64 亿 USDT：把地下市场画出来**

要回答这个问题，首先要系统性地找到这些平台。零散的举报和人工搜索做不到这一点，研究团队基于两个洞察设计了自动化发现方法。

其一是「半公开性」，担保平台需要持续吸引新的买家和卖家，因此无法完全隐匿；其二是「连通性」，Telegram 社区之间高度互联，可以从高置信度的公开种子频道出发，递归发现更多相关频道与群组。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyquYM1ziapicouicoDKnFnDiarMq4bwXHe4Yx0YDb0U3ibDJEibe3YCicRqkeQ2uRSpXmYhOoEia4icH4ZNfIM7grJre548JicXQG55kCAJxI/640?wx_fmt=png&from=appmsg)

图 3：担保平台的自动化发现方法

基于这套方法，团队得到了如下结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyquG0UengGjCJ1d7NL46XX66HnxjGL0OWCANibwNTHwP4icYwGJBxMy7dl0A9IkS77T681BibGuTcXD726S4UgxLpXWq4DJ8vcjoibE/640?wx_fmt=png&from=appmsg)

图 4：研究核心数据

在 9 类服务中，有 4 类正好串起了从受害者定位、社交工程、虚假投资平台与支付通道，到资金转移与清洗的完整诈骗流水线。

资金流向分析进一步显示，来自洗钱服务的 USDT 中，约 5,440 万最终流入 57 家加密服务提供商完成变现。周教授特别指出，犯罪分子对于交易所的反洗钱策略进行了研究，简单增加一跳就可以规避一些交易所的反洗钱筛查。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ibKZs4HxyquG8TboLCJrgHtAcfwj7SLUdmxk0Wrn4ZK8rIcUppEfbNDt3PZm2Fq5U6p2sveIZE9Ba2anbhibVV3ntWEg8AsPXEn24xxovQl4/640?wx_fmt=jpeg)

图 5：洗钱资金到达交易所所需的跳数分布，大部分在2跳内就到达交易所

**封了频道、上了制裁名单，然后呢？**

分享中最有冲击力的部分，是对执法行动效果的量化评估。

以 Xinbi 为例，团队追踪了其押金地址在两次干预前后的活动。Telegram 下架相关频道后，Xinbi 押金活动的 7 日均值上升 17.56%，14 日均值上升 45.87%；英国制裁后，7 日与 14 日均值分别上升 1.61% 和 1.55%。两次干预都没有带来持续的下降，可见影响甚至不如公共假期。

原因之一是平台的地址轮换策略。研究观察到 Xinbi 先后使用了 24 个官方押金地址，而英国制裁名单中的地址在被列入时已经闲置了 155 天。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ibKZs4HxyqsPuPtfK4Ytc8zib91jQH49zZDt2iaLMQxkq5CCEsCtIDRZ1M75bp9Ckpfibf1jib0AQzZvBdhCUNW6ta0n4zuViczJTRB5TiaVazrDk/640?wx_fmt=jpeg)

图 6：Xinbi 先后使用的 24 个押金地址，红色为被英国列入制裁的地址

担保平台远不止托管服务，它们是完整的非法服务市场。被动地封频道、列名单，挡不住这个市场运转；真正需要的，是主动的、自动化的持续监测。

**台下的追问**

对现场多数执法人员来说，Telegram 担保平台仍是一个陌生领域，这也是这场分享受到关注的原因。问答环节的提问集中在研究方法和平台运作细节上，讨论一直延续到会后，多位执法人员主动与团队交流各自辖区内的相关案件线索。

区块链调查专家 Richard Sanders 在问答环节公开表示，这项研究很有意义，团队是这一领域的专家。

对团队而言，这些反馈说明研究找对了问题：担保平台已经是诈骗产业链的基础设施，执法界需要系统性地认识它。

**6 亿地址标签背后：把研究变成能力**

这项研究由BlockSec 和香港中文大学、香港城市大学、浙江大学联合完成，也是 BlockSec 一贯坚持的「学术研究与产业实践相互驱动」路径的一个缩影。研究中「主动发现、持续监测、多跳追踪」的方法论，与 BlockSec 反诈反洗钱产品的底层逻辑是同一条主线。

主动监测的前提是知道每个地址是谁。Phalcon Compliance 的核心能力正是地址标签：BlockSec 目前积累了超过 6 亿个地址标签，覆盖交易所、OTC、支付机构、混币器、受制裁实体，以及诈骗、担保平台、洗钱服务等涉案实体。

标签覆盖要全，更新也要快。像本次研究中发现的担保平台押金地址和轮换规律，这类一线情报会持续沉淀进标签库。

面对 Xinbi 这样不断更换押金地址的平台，静态黑名单列进去时地址已经闲置，而持续更新的标签体系能跟上地址轮换的节奏，让交易所、支付机构在资金到达之前就识别出风险，不必等到事后再补救。

这也是 BlockSec 能够服务超过 50 个辖区的监管机构、金融情报单位和执法部门，以及 1,000 多家机构客户的基础。

MetaSleuth 则面向调查人员，支持对可疑资金进行跨链、多跳的可视化追踪。研究告诉我们问题在哪里，产品负责把答案交到一线手上。

**写在最后**

诈骗已经演变成一个分工明确的服务经济，与之对抗也必须成为一项协作的事业。感谢 INTERPOL 创新中心的邀请，更感谢现场每一位认真提问、坦诚交流的执法同仁。让学界、产业界与执法机构坐在同一间屋子里直接对话，这样的论坛本身就是一种推动。

BlockSec 将继续与全球执法机构、监管部门和研究机构合作，把研究成果转化为可落地的能力，共同应对加密资产领域不断演进的犯罪形态。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ibKZs4HxyqscHkaNO2Tst7HlicrgBAI25CMStOmX8mriaW8dqebX2w4peN2zdKYBA2HbMyRFC25SIs5XHyePla81SO6QgufYtBTFbOVOGyH0w/640?wx_fmt=jpeg)

图 7：周亚金教授与胡宇峰博士在论坛现场

---

关于BlockSec

BlockSec 是全球领先的区块链安全和合规公司，于 2021 年由多位业内知名专家联合创立。BlockSec 致力于提升 Web3 世界的安全性和易用性，提供一站式安全服务，包括智能合约/链/钱包安全审计服务、协议安全和数字货币合规(AML/CFT)平台 Phalcon Security / Phalcon Compliance / Phalcon Network、资金追踪调查平台 MetaSleuth和区块链交易分析工具 Phalcon Explorer 等。

目前，BlockSec 已服务全球逾 1000 家客户，既涵盖 Web3 知名公司 Coinbase、Cobo、Uniswap、 Compound、MetaMask、Bybit、Mantle、Puffer、FBTC、Manta、Merlin、PancakeSwap 等，也包括了权威监管机构及咨询机构，如联合国、SFC、PwC、FTI Consulting 等。

官网：https://blocksec.com/

Twitter：https://twitter.com/BlockSecTeam

推荐阅读 👇

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTJKnQAjhicg47N8sLY3SKzqlEcnuEf3pYzPTIqpar2ibkeSeCvjqQsKrLwZwWyTcAXIazKXLQIXEchQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247490504&idx=1&sn=ed76941ba8ee144bdd12cb0ddb7df70c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTIje0g9kj9ic4b9GEzwpo1TCWq94NdL91n7Yt1FYkWUmPEXrkGzHKNvuQbOlu36LFXShpNOTklWvKw/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247491200&idx=1&sn=f0a133511ca63c3deb086c51654e4157&scene=21#wechat_redirect)

#BlockSec

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTKWV4NZYNjUicibdl9UQ4HibVfGa4a6ypSMKArRmWBI3Nibibicuo7YJbQibOC8XKvSMJXYGRFWIz3hsvvfA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过