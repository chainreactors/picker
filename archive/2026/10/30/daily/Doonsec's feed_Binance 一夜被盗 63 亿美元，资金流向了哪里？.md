---
title: Binance 一夜被盗 63 亿美元，资金流向了哪里？
url: https://mp.weixin.qq.com/s/6Kp2-VM36AjFR67DZ8Bj6A
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:42:22.419154
---

# Binance 一夜被盗 63 亿美元，资金流向了哪里？

# Binance 一夜被盗 63 亿美元，资金流向了哪里？

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

2026 年 10 月 29 日 20 点左右（UTC），Binance 发生多链资产被盗事件。根据 Binance 最新公示，被盗资产总额约为 63 亿美元。

目前已识别的资金流出涉及至少 10 条链，包括 Ethereum、Bitcoin、Tron、Solana、Arbitrum、Avalanche、Polygon、Optimism、Base 和 XRP Ledger。

根据已完成的链上核验，约 27.98 亿美元资产已确认被冻结，主要为 USDT、USDC 等稳定币，也包括 wBETH、RLUSD、USD1、FDUSD、USDT0，以及 XAUt、PAXG 等黄金代币。

此外，约 3,847 万美元资产由项目方或链方实施救援处置，包括 984.25M 枚 BEAM 被直接销毁，8.41M 枚 SNX 和 58.40M 枚 SAND 通过特权操作移出攻击者地址，三者交易时估值合计约 747 万美元。Arbitrum 上的 8.43K 枚 ETH 和 74.56M 枚 ARB 被转入临时冻结地址，参考估值约 3,101 万美元。

然而，大额资产仍停留在攻击者地址中。

按美元价值从高到低，主要包括：18.27K 枚 BTC（约 14.26 亿美元）；500.18K 枚 ETH（约 11.16 亿美元）；233.46M 枚 XRP（约 2.88 亿美元）；970.55K 枚 SOL（约 9,441.57 万美元） 等等。

**分链资产与现状**

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqtXuZleD37xjhyCYE6IStLAFHvDblzNquOibyQuxpcaHuJYaiavg7LIM1cbvhe99kI3XZcg5OT1dkyL7icekIbtE7qSx0GDbdpYew/640?wx_fmt=png&from=appmsg)

图 1：分链资产与现状

注：总价值采用已收集记录的历史估值；现状来自分析时快照；Avalanche 路径在 Ethereum 被冻结的 USDC 计入 Ethereum 冻结额，不在 Avalanche 重复计算。

**已转出资金的分链去向**

**Bitcoin：拆分转移后停留在多个地址**

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqtPGZicVP8rZdEdicbUvbic5MiavbVqD6uicGDGPOFNKuf1yxdmu75DwBRicJOMjy5VjuRmkV27jah74hTAIfyTdslCy9ILndvBR9sw0/640?wx_fmt=png&from=appmsg)

图 2：BTC 从最初接收地址分散至下游

MetaSleuth 完整图谱：https://metasleuth.io/result/btc/bc1q0mtc2f5agpkvlq6hhahmfr3hlr55kyfjhl2mnm?source=ece5788b-cd36-4dfc-a3b8-2264c7883d25

在已核验的下游持仓中，约 18,270.20 枚 BTC 分布于 19 个地址：17 个各持有约 1,000 枚 BTC，另外两个分别持有约 832.50 枚和 437.70 枚 BTC。

资金已离开最初接收地址，但仍停留在这些已识别的下游地址中。

**Ethereum：分发、兑换与部分资产冻结**

Ethereum 上的首批转出发生于 2026 年 10 月 29 日 20:24:23（UTC）。多个 Binance 钱包中的资产汇入 0x5227f6...2f8c，累计高达 37.4 亿美元。该地址随后向 19 个地址转出资产，转出时估值合计约 15.54 亿美元。

在已核快照中，该地址仍有约 20.85 亿美元资产处于冻结状态，包括 1.18B USDT、823.00M USDC、12.57K XAUt、27.82M USD1、1.91K PAXG 和 3.45M FDUSD。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyquibYozux6mDURSdsMQYq8ic8zxGtMIhXNmDqYFk0ric6jxdmjRX8WmX4xI72JoFa2uMNibaCmGCTCgwmeJOtDf35uGfVughtk2mtQ/640?wx_fmt=png&from=appmsg)

图 3：Ethereum 上的资产汇入与下游分发

MetaSleuth 完整图谱：https://metasleuth.io/result/eth/0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c?source=b1d343c7-c9c6-490d-a410-96d7af35d497

后续路径中，部分代币被兑换为 ETH，并在多个地址间转移、归集；部分资产在下游地址被冻结，包括约 205M 枚 USDT、40.54M 枚 RLUSD、1.60M 枚 USDC，以及 29.93K 枚 wBETH。另有 60M 枚 USDT 被存入 Aave，形成存款权益，同时借出了 WETH。

**Tron：部分 USDT 冻结，其余资金继续分散**

Tron 上被盗 612.73M 枚 USDT 和 46.39M 枚 TRX，被盗时估值合计约 6.28 亿美元。其中，312.73M 枚 USDT 被及时冻结；另有 300M 枚 USDT 分两笔进入下游。

后续路径中，65.99M 枚 USDT 在转移的过程中被冻结。两处已核实冻结的 USDT 合计 378.72M 枚，参考估值约 3.78 亿美元。剩余有部分 TRX 分散后通过 Bitget wallet，Symbiosis 和 Changehero 跨链至以太坊。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqsoA0HwUy6dsP2tyRQ3oZ4NaAH9VP1KNAkzvhN0aI7rrfknRIT9rU609NvAmu4bQSHiaBjr1B67zl1ibhwMvqC15HzrbCibv8icmo4/640?wx_fmt=png&from=appmsg)

图 4：Tron 上的 USDT 冻结与 TRX 分发路径

MetaSleuth 完整多链图谱：

https://metasleuth.io/result/arbitrum/0x1b5b4e441f5a22bfd91b7772c780463f66a74b35?source=465db100-9be0-4db4-8b35-7ff182992517

**Arbitrum：资金归集后被链方冻结**

Arbitrum 上，被盗的 8.43K 枚 ETH 和 74.56M 枚 ARB 先进入直接接收地址，随后归集至 0x3e2bf1...32d5。

10 月 30 日 00:18:20，Arbitrum 安全委员会通过两笔交易，将相关资产转入临时冻结地址 0x0000000000000000000000000000000000000da0，参考估值约 3,101 万美元。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4Hxyqu39orXHmoZYFTVCHWMAypO2LkbmDGqaACib0SNdzVWr2TwOULOWNLUiawZSePyzgosa9KAHxlKeL9r4sQzwo1tzhy4TJ4b9fIFM/640?wx_fmt=png&from=appmsg)

图 5：Arbitrum 上的 ETH 和 ARB 经归集后，通过两笔交易转入临时冻结地址

MetaSleuth 完整多链图谱：https://metasleuth.io/result/arbitrum/0x1b5b4e441f5a22bfd91b7772c780463f66a74b35?source=465db100-9be0-4db4-8b35-7ff182992517

**Avalanche：部分资产停留，部分跨链后在 Ethereum 被冻结**

Avalanche 上被盗 2.26M 枚 AVAX 和 8.41M 枚 USDt，被盗时估值合计约 2,794 万美元，其中 USDt 被成功冻结。

向下游转出的 AVAX 中，有 200.01K 枚 AVAX 进入了后续兑换和跨链路径。这部分 AVAX 兑换为 USDC 后，经 Circle CCTP 转入 Ethereum。

Ethereum 上的同址接收端 0xc39e69...9824 收到 1.56M 枚 USDC，并于到账后 4 分 24 秒被冻结。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4Hxyqtp1p42ia7KmF197bc1s3VA1SUYZB9H59oTpge87t0oPZLLYQ2J7eIDXq8TxBz3Lvn15aEZky9ZsJSaQkXk4ibk9z88dFnI1RSDs/640?wx_fmt=png&from=appmsg)

图 6：AVAX 向下游转移后出现部分回流，另有约 200K 枚 AVAX 进入跨链路径

MetaSleuth 完整多链图谱：https://metasleuth.io/result/arbitrum/0x1b5b4e441f5a22bfd91b7772c780463f66a74b35?source=465db100-9be0-4db4-8b35-7ff182992517

**事件进展总结**

**总体来看，此次事件约 63 亿美元被盗资产中，已确认约 27.98 亿美元被冻结，以 USDT、USDC 等稳定币为主；另有约 3,847 万美元已由项目方或链方完成救援处置。与此同时，仍有大额资金滞留于攻击者地址，仅已核验的 BTC、ETH、XRP、SOL 四类资产即合计约 29.24 亿美元，其中以 BTC 和 ETH 为主。**

**BlockSec 正协同相关团队开展资金追踪与调查，密切监测攻击者地址及跨链资金流向，为后续冻结与追偿提供支持，并将随链上核验与调查的推进持续更新相关信息。**

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