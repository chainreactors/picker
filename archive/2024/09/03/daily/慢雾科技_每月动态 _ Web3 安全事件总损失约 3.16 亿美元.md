---
title: 每月动态 | Web3 安全事件总损失约 3.16 亿美元
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500217&idx=1&sn=3d0739b9da5b1aa080541b5a9bdca7d7&chksm=fddebf3ecaa93628158db7785c0fd8fda98a198ced9dc704c38810535b002d26441fbae9b7e0&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-09-03
fetch_date: 2025-10-06T18:26:16.300622
---

# 每月动态 | Web3 安全事件总损失约 3.16 亿美元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYyulhDhoF6fpnVGJpet2I2elC9miafZryug81XYs7jcopzibVGc7Sib6obMIkpzsg5I9hiaM4uzqDVRA/0?wx_fmt=jpeg)

# 每月动态 | Web3 安全事件总损失约 3.16 亿美元

慢雾安全团队

慢雾科技

**概览**

2024 年 8 月，Web3 安全事件总损失约 3.16 亿美元。其中，据慢雾区块链被黑档案库(https://hacked.slowmist.io) 统计，被黑事件共发生 28 起，导致损失约 2.53 亿美元，有 1358 万美元得到返还，事件原因涉及合约漏洞、账号被黑和前端攻击等。此外，据 Web3 反诈骗平台 Scam Sniffer 统计，本月有 9145 名钓鱼事件受害者，总损失达 6293 万美元。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYyulhDhoF6fpnVGJpet2I2GwqyiaE2SicK1icFViaq9C0y25moyU9iajpRey8hxTJrv7ee4mquLdLe9Mw/640?wx_fmt=png&from=appmsg)

(https://dune.com/scam-sniffer/august-scam-sniffer-2024-phishing-report)

#

# **主要事件**

**Convergence Finance**

2024 年 8 月 1 日，Convergence Finance 被攻击，攻击者铸造并出售了 5800 万个 CVG 代币，约 21 万美元（相当于专门用于质押发放的全部代币份额）。此外，来自 Convex 的约 2 千美元未领取的奖励也被盗。根据 Convergence Finance 发布的事故分析报告，此次事件的根本原因是奖励分配合约的 `claimMultipleStaking` 函数缺乏对用户输入的验证。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYyulhDhoF6fpnVGJpet2I2IicqiaF4ibWY8qjyWdqXhbxEoiaarBD5eMVWXWibzVQ8ia98lCiaNibhYPy0Lw/640?wx_fmt=png&from=appmsg)

(https://medium.com/@cvg\_wireshark/post-mortem-08-01-2024-e80a49d108a0)

**Ronin**

2024 年 8 月 6 日，游戏区块链 Ronin 遭攻击，Ronin Bridge 项目出现异常提取跨链资产的行为。据慢雾安全团队分析，此次攻击是由于权重被修改为意外值，资金无需经过任何多重签名阈值检查即可提取。攻击者从桥中提取了约 4000 枚 ETH 和 200 万枚 USDC，价值约 1200 万美元。截至 8 月 7 日，白帽归还了价值 1200 万美元的资产，并获得 50 万美元的漏洞赏金。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZaaNBZNuX9ACZj2gxwoI9giamDXwibGTWvCO0GicdbiaabWD99xCUibuINNfwDxV7dk28J2UgpGTQbibng/640?wx_fmt=png&from=appmsg)

(https://x.com/slowmist\_team/status/1820783952145355247?s=46&t=DLwbX9Nw4QECiyZQ0av-fg)

**Nexera**

2024 年 8 月 7 日，一名外部攻击者获得了管理 Nexera Fundrs 平台智能合约的凭证。利用这些凭证，攻击者从以太坊上的 Fundrs 质押合约中转移了 NXRA 代币，导致约 183 万美元的损失。在被盗的 4724 万 NXRA 代币中，攻击者只售出了 1475 万代币（约合 44.9 万美元）。Nexera 成功从攻击者的钱包中移除了剩余的 3250 万 NXRA 余额，防止了进一步的损失。

**Vow**

2024 年 8 月 13 日，Vow 因合约漏洞遭攻击，损失约 120 万美元。据 VOW 消息，当时团队正在测试 v$ 合约的 USD 汇率设置功能，以便为新的借贷池和预言机功能铸造 v$。攻击者利用了短暂的时间窗口和汇率变动，购买并发送了大量 VOW 代币到合约中，导致生成了近 20 亿 v$，并将其卖回 Uniswap 池中，从而获利。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZaaNBZNuX9ACZj2gxwoI9gDdBtPxiaAscUasASQJTEDrSefH5hvU5gLyND5cIdy9ReVNG3HSiaKDxg/640?wx_fmt=png&from=appmsg)

(https://x.com/Vowcurrency/status/1823407231658025300)

**User**

2024 年 8 月 19 日，据链上侦探 ZachXBT 消息，一笔涉及 4064 BTC（约合 2.38 亿美元）的可疑转账可能来自一名潜在的受害者。随后资金很快被转移到 ThorChain、eXch、Kucoin、ChangeNow、Railgun 和 Avalanche Bridge。截至 8 月 27 日，已有 20.5 万美元被收回。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZaaNBZNuX9ACZj2gxwoI9gd7DibZy9JELcUE9baJdJJTSrHhUMsHpH3730gQfibB8aUBawomU0p8XQ/640?wx_fmt=png&from=appmsg)

(https://x.com/zachxbt/status/1825499490956231021)

**User**

2024 年 8 月 21 日，据 Scam Sniffer 监测，一名受害者在签署了针对其 DeFi Saver Proxy 的网络钓鱼交易后，损失了价值 5543 万美元的 DAI。据 MistTrack 分析，这笔资金被发送到多个地址，随后大部分被兑换成 ETH。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZaaNBZNuX9ACZj2gxwoI9gNdpObNe3kVDb3icO44QaxowibhtnzwXrNWiahGGSibQyC58NqabbGcXOibw/640?wx_fmt=png&from=appmsg)

(https://x.com/MistTrack\_io/status/1826273448626356697)

**Aave**

2024 年 8 月 28 日，DeFi 借贷平台 Aave 的一个外围合约遭攻击，攻击者利用了一个任意调用错误，导致约 5.6 万美元的损失。受影响的外围合约 ParaSwapRepayAdapter 并不属于 Aave 核心协议，该合约用于允许用户利用现有的抵押品偿还贷款，通过去中心化交易所 ParaSwap 进行资产交换。虽然该合约本身并没设计为持有用户资金，但由于交易中的正滑点，合约中会逐渐累积一些剩余的代币。Aave 的相关人员强调，此次攻击没有对用户资金造成威胁，也没有影响核心 Aave 协议的安全。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZaaNBZNuX9ACZj2gxwoI9gx0Zzibjic02Ev37jLtdUBAudOGr43tN5y0fyJZIUI6WgMdOb5y5NvPwA/640?wx_fmt=png&from=appmsg)

 (https://x.com/bgdlabs/status/1828736554262470792)

# **总结**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYyulhDhoF6fpnVGJpet2I2ccLxWia1IOXicT0wBe5iaW3kwibCFhHLhibm36A6IB3d2OXudFlN8Ds0sUw/640?wx_fmt=png&from=appmsg)

本月账号安全问题成为风险重灾区，账号被黑事件数占总被黑事件数的 64.3%。值得注意的是，黑客的攻击对象不单是区块链知名项目和成员，还包括明星及传统行业的知名品牌，如足球明星 Kylian Mbappe，麦当劳等。黑客盗取知名账号后，常发布含有钓鱼链接的动态或推广某代币，慢雾安全团队提醒广大用户谨防钓鱼攻击，多方确认消息的真实性，谨慎投资。本月的账号被黑事件多发生在 Discord 上，此前我们在[慢雾：揭露浏览器恶意书签如何盗取你的 Discord Token](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247495383&idx=1&sn=3695e16c9f33aff690bb033de6f77b20&chksm=fdde9050caa919464a53d117159ff1b1ad52490b04edf372e5a9b65fde400031dad24f1348dd&scene=21#wechat_redirect) 中讲解过 Discord Token 机制，点击链接可跳转阅读。

最后，本文收录的事件为本月主要安全事件，更多区块链安全事件可在慢雾区块链被黑档案库(https://hacked.slowmist.io/) 查看，点击阅读原文可直接跳转。

**往期回顾**

[Web3 安全入门避坑指南｜假矿池骗局](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500196&idx=1&sn=897d51b7228f0f97045472e157d051b1&chksm=fddebf23caa93635e642d8828d054a361da7ae3d90918ea9b9e1b58eb500fd0395b36178607e&scene=21#wechat_redirect)

[慢雾(SlowMist) 创始人受邀出席 2024 外滩大会，共探 Web3 新发展](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500185&idx=1&sn=c1de17fad9e6c1c8d4e1fc710ffb5a8a&chksm=fddebf1ecaa9360898a6f90504211d1273e08db2285414dc45711b1e8ff102f1a95738204b32&scene=21#wechat_redirect)

[Web3 安全入门避坑指南｜空投骗局](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500174&idx=1&sn=e3cb8f76396b64e8dd23bbcdc1a24bcd&chksm=fddebf09caa9361fef844c27d8b8b4360cac62f2fb5f3b8b9fe83f1cfa44de95311a62915f8d&scene=21#wechat_redirect)

[初识 TON：账号、Token、交易与资产安全](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500158&idx=1&sn=7496a1dcfa1326533a145348078bb996&chksm=fddebff9caa936ef22ef30829b17a5e573b4961808b7ea5b1858a014f3058215b02d85485031&scene=21#wechat_redirect)

[「区块链黑暗森林自救手册」印尼文版正式发布](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500140&idx=1&sn=88f5db074ebd46d5ef0debb09aeb90a7&chksm=fddebfebcaa936fdecb584664a7c668adde29124f69886d189ca16aa1e42470e5ad89ea74511&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8Togv4VUdq4r7iak19Hta2pfbzPrGohPNR71WxPKrBoK9nyibPVL7ssCuW3yA/640?wx_fmt=png)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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