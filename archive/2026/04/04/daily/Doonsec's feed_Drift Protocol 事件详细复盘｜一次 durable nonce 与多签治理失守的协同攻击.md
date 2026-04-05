---
title: Drift Protocol 事件详细复盘｜一次 durable nonce 与多签治理失守的协同攻击
url: https://mp.weixin.qq.com/s/2UxJ1zCfCF4Fh5WMCKyPuw
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:34:16.660255
---

# Drift Protocol 事件详细复盘｜一次 durable nonce 与多签治理失守的协同攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2ibKZs4HxyqtibSjUia9ndGib2mQSjzlVhNVzbGvQ37XGHIwELHTZVq2y4frH9nt9gsAOcKAW5s97FvhaJnZpetiaKicOpsr3wvHfEPOtoDr2pxias/0?wx_fmt=jpeg)

# Drift Protocol 事件详细复盘｜一次 durable nonce 与多签治理失守的协同攻击

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2ibKZs4Hxyqt0D2PVmxcGrqPt9ZNeFpG7C33jZYSN3xquibhWufnUoXlML6jbNuUv5Lke8VTmzq8iabyxH2E5j4MFiczwj0VQqSeDx6z64JlMts/640?wx_fmt=gif&from=appmsg)

**引言**

2026年4月1日(UTC),Solana 上的 Drift Protocol 遭遇了一次结合多签审批操纵和 durable nonce 利用的协同攻击。Durable nonce 是 Solana 的一种交易机制,允许预签的交易无限期保持有效。此次攻击预计总损失约 $285.3M [1, 2]。经过数周的链上准备,攻击者通过钓鱼或误导性签名请求,诱导五名安全委员会多签签名者中的两名预签了恶意治理交易。签名后的指令被保留至攻击者选定的时机,随后通过两笔快速交易完成了管理员接管并转移了管理控制权。获得完整管理员权限后,攻击者引入恶意抵押资产 CVT,虚增其预言机价格,放宽提款保护措施,并通过协议的借贷通道提取了高价值真实资产。

截至撰文时,Drift 已发布初步声明 [1] 但尚未公布完整的事后分析报告。以下分析基于公开可用的链上数据、Drift 官方时间线及独立研究 [2]。本文首先探讨 durable nonce 如何从根本上改变多签治理的安全假设,随后还原数周的攻击准备、治理接管执行和资金提取过程,最后总结针对此类风险的经验教训。

**背景**

**Drift Protocol 与 Squads 多签**

Drift Protocol 是 Solana 上的 DeFi 协议,支持保证金交易、借贷、现货市场和衍生品。其高权限操作,包括管理员变更、市场创建、预言机配置、风控参数更新和提款限额调整,由多签而非单一私钥管控。

Drift 使用 Squads 多签框架,这是 Solana 上常见的链上治理系统。在 Squads 中,特权操作被打包为提案下的交易。一旦足够多的成员批准提案,存储的指令即可通过 vaultTransactionExecute 原子化执行。攻击发生时,Drift 的安全委员会采用 2-of-5 阈值配置且时间锁为零,意味着五名签名者中任意两名即可授权管理操作并立即生效。该系统的安全性不仅取决于签名者密钥的保管,还取决于整个审批流程的完整性:创建了什么交易、签名者认为自己在批准什么、以及最终执行的指令是否与审核上下文一致。

**Durable Nonce 账户**

Durable nonce 账户为交易执行引入了关键的时间维度 [3]。正常情况下,Solana 交易依赖 recent blockhash,签名后如未及时广播将很快过期。Durable nonce 用存储在专用账户中的 nonce 替代短效的 blockhash,使已签名交易可在 nonce 被推进之前无限期保持有效。该特性适用于离线签名或延迟提交等合法场景,但也创造了一个重要的攻击原语:它将交易签名时间与链上执行时间分离。关键的是,一旦签名者批准了一笔 durable nonce 交易,除非 nonce 权限方手动推进 nonce 账户,否则签名者无法撤销其签名。

这种分离对多签安全有着微妙但根本性的影响。在正常的 blockhash 交易下,短暂的过期窗口充当了一个隐式安全层:签名者的授权要么被及时执行,要么无害地过期。这一时间约束意味着即使签名者被骗批准了恶意交易,攻击者也必须在狭窄的窗口内广播,限制了协同多步攻击的空间。Durable nonce 完全移除了这一约束。签名无限期有效后,一次签名失误的代价从根本上改变了:被骗的批准不再在几分钟内过期,而是在没有自动时限的情况下持续可利用,使攻击者完全掌控执行时机,并能从容协调后续攻击步骤。

**攻击分析**

攻击分三个阶段展开。在前期准备阶段,攻击者进行了持续数周的操作,制造虚假抵押资产并通过误导性签名请求获取治理访问权限。在治理接管阶段,两笔预签的 durable nonce 交易被快速提交以夺取管理控制权。在资金提取阶段,攻击者篡改协议参数并通过协议的借贷通道提取真实资产。下图展示了攻击执行流程的三个阶段,与后续各小节一一对应。并行的 CVT 代币制造过程详见前期准备部分,未在图中展示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqvD955R20KdxlfURE4CfmiaiaUcnNWOBvMX1UOicT8I5tF2htUvvmmuk0XY1AadXXhC0ibAibJfMt86LFMasTzEhOkRTcmuTxEkb7GI/640?wx_fmt=png&from=appmsg)

**前期准备**

此次攻击并非一次性的机会主义行为,而是一项持续数周、双轨并行的操作。第一条线聚焦于制造一个看似合理的抵押资产。3月11日,攻击者从 Tornado Cash 提取 10 ETH,用于部署 CarbonVote Token (CVT),铸造了 7.5 亿枚代币。在随后数周内,攻击者在 Raydium 上注入少量流动性,并通过洗交易建立了接近 $1 的人工价格历史,赋予 CVT 表面上的市场合法性 [4]。

第二条线瞄准治理访问权限。根据 Drift 官方时间线 [1],3月23日创建了四个 durable nonce 账户:两个关联 Drift 安全委员会多签成员,两个由攻击者控制。这表明至少两名(五分之二)签名者已签署了绑定 durable nonce 账户的交易,使攻击者获得了所需的 2-of-5 批准阈值。

3月27日,Drift 因委员会成员变更执行了计划中的安全委员会迁移。此次迁移使旧配置下收集的签名失效。然而到3月30日,一个新的 durable nonce 账户出现,关联至更新后多签的一名成员,表明攻击者已在新配置下重新获得了所需的 2-of-5 批准阈值。

这一序列揭示了攻击者在主动监控链上治理变更并实时调整策略。签名收集并非一次性的钓鱼行动,而是一个持续性操作,经受住了准备期间的多签重新配置。迁移本身可能无意中助长了攻击:在治理过渡期间,签名者更可能遇到并批准行政签名请求,形成了天然的社会工程窗口。

4月1日,攻击者选择了精确的执行窗口。Drift 首先执行了一笔来自保险基金的合法测试提款。约一分钟后,攻击者提交了预签的攻击交易。这一时机选择表明攻击者在实时监控链上活动,等待一次成功的合法操作确认系统处于正常运行状态后才发起攻击。

**治理接管**

4月1日约16:05 UTC,攻击者间隔四个 slot 提交了两笔预签的 durable nonce 交易。

第一笔交易 ([2HvMSg...2C4H][5] ）创建并批准了恶意管理员转移提案。

第二笔交易 ([4BKBmA...RsN1][6]）批准并执行了该提案,交易以 AdvanceNonceAccount 开始,激活存储的 nonce,随后通过 proposalApprove 和 vaultTransactionExecute 推进,最终调用 UpdateAdmin 将管理控制权转移到攻击者控制的地址。

此执行流程揭示了攻击的一个关键特性:决定性的授权并非发生在执行时,而是在更早的签名阶段。链上交易只是将已授予的权限具象化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqtNxXO2dxiaxOB3p9r5oQWIYckNpQ1iaMNYRNwdbu3Igz1X1XtyvRyfian4AFtXAqMv4OIFicxIlALXpkbl7our6L4mQeiakOice50Cg/640?wx_fmt=png&from=appmsg)

**olscan 上的预签治理交易,展示 AdvanceNonceAccount、proposalApprove、vaultTransactionExecute 和 UpdateAdmin 指令序列**

**资金提取**

获得管理控制权后,攻击者在提取资金前采取了三个准备步骤:为 CVT 创建恶意抵押品市场,切换到攻击者控制的预言机以虚增其价格,以及放宽提款保护以实现大规模提取。

第一步是为 CVT 创建恶意抵押品市场。该市场的问题不仅在于它是新创建的,更在于它缺乏真实流动性,却被赋予了过于宽松的风控参数。一个没有可赎回价值的资产,一旦被协议接受为高权重抵押品,就可以凭空创造借贷能力。

第二步是切换到攻击者控制的预言机并虚增价格。凭借管理员权限,这一步无需绕过任何限制。一旦预言机在攻击者手中,CVT 的账面价格就可以被任意抬高,使一个在真实市场几乎没有价值的资产在协议内被记录为高价值抵押品。

第三步是放宽提款保护和熔断机制。即使抵押品价格被虚增,如果主要资产市场的提款限额仍在,攻击者仍难以大规模提取真实资产。因此,这些护栏必须被提高或移除,之前虚构的抵押品价值才能转化为可提取的真实资产。

完成这些步骤后,攻击者将大量高估值的 CVT 存入协议,通过31次快速提款在约12分钟内提取了 USDC、JLP、SOL、cbBTC、USDT、wETH、dSOL、WBTC、JTO 和 FARTCOIN 等真实资产。这完成了资金提取闭环:获得治理控制权,修改参数,将无价值资产包装为高价值抵押品,最后沿协议现有的借贷和提款通道转移资金。

截至撰文时,总损失为 $285,279,417.69,基于攻击者提款账户 ([HkGz4K...pZES][7]) 计算。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqvZPcTV8f7UKkZ6WnHicsmbxXjzjmElBMq7Q4H1XgJL2iakIHqUTxhe8SL5l3vQYRxiaQgk1ibhEozkePaSZic75esc4dgAaggibbaVA/640?wx_fmt=png&from=appmsg)

**经验教训**

1. 多签安全不止于密钥保管。

保护私钥和执行签名阈值是不够的。整个授权流程,包括交易构造、展示和签名者理解,都必须是可信的。在此次事件中,签名者的密钥并未泄露,但审批流程被操纵,导致签名者在不知情的情况下授权了恶意操作。

2. 时间锁对高权限操作至关重要。

管理员变更等行政操作不应立即可执行。Drift 的零时间锁配置意味着预签交易一旦被触发,管理控制权在数分钟内即被转移并利用,没有留下任何检测或干预的机会。时间锁本可创建响应窗口,用于识别并阻止恶意转移。

3. 延迟执行机制在治理场景中需要额外保护。

Durable nonce 将签名与执行解耦,移除了签名者隐含依赖的时间保证。在治理系统中,此类机制应搭配更高的签名阈值、有时限或可撤销的批准机制,以及防止已签名交易无限期有效的限制措施。

**结论**

此次事件并非由智能合约漏洞或密钥泄露引起,而是多签授权流程在 durable nonce 延迟执行机制下的崩溃。攻击者通过误导性签名,预先收集了五名安全委员会签名者中两名的有效多签批准,利用 durable nonce 交易保存这些批准,随后执行以获取管理控制权。后续的资金提取是治理被攻破的直接后果,通过协议本身的合法操作完成。防范此类风险需要保护完整的授权流程、对高权限操作强制实施时间锁,以及为延迟执行机制增加额外的安全保障。结合能够实时检测异常治理活动的链上监控系统,这些措施共同构成了针对此类治理层攻击的完整安全体系。

BlockSec 持续监控链上安全动态，如果您的协议需要专业的安全审计或实时监控服务，欢迎通过官网或点击【阅读原文】联系我们。

**参考资料**

[1] DriftProtocol, "Official statement": https://x.com/DriftProtocol/status/2039564437795836039

[2] Phalcon (BlockSec), "Drift Protocol Exploit Analysis":https://x.com/Phalcon\_xyz/status/2039602380074016909

[3] Solana, "Introduction to Durable Nonces":https://solana.com/developers/guides/advanced/introduction-to-durable-nonces

[4] CoinDesk, "How Drift attackers drained more than $270 million using a Solana feature designed for convenience":

https://www.coindesk.com/tech/2026/04/02/how-a-solana-feature-designed-for-convenience-let-an-attacker-drain-usd270-million-from-drift

[5] https://solscan.io/tx/2HvMSgDEfKhNryYZKhjowrBY55rUx5MWtcWkG9hqxZCFBaTiahPwfynP1dxBSRk9s5UTVc8LFeS4Btvkm9pc2C4H

[6] https://solscan.io/tx/4BKBmAJn6TdsENij7CsVbyMVLJU1tX27nfrMM1zgKv1bs2KJy6Am2NqdA3nJm4g9C6eC64UAf5sNs974ygB9RsN1

[7] https://solscan.io/account/HkGz4KmoZ7Zmk7HN6ndJ31UJ1qZ2qgwQxgVqQwovpZES?exclude\_amount\_zero=true&from\_address=JCNCMFXo5M5qwUPg2Utu1u6YWp3MbygxqBsBeXXJfrw&remove\_spam=true&page\_size=100#transfers

---

关于BlockSec

BlockSec 是全球领先的区块链安全和合规公司，于 2021 年由多位业内知名专家联合创立。BlockSec 致力于提升 Web3 世界的安全性和易用性，提供一站式安全服务，包括智能合约/链/钱包安全审计服务、协议安全和数字货币合规(AML/CFT)平台 Phalcon Security / Phalcon Compliance / Phalcon Network、资金追踪调查平台 MetaSleuth和区块链交易分析工具 Phalcon Explorer 等。

目前，BlockSec 已服务全球逾 500 家客户，既涵盖 Web3 知名公司 Coinbase、Cobo、Uniswap、Compound、MetaMask、Bybit、Mantle、Puffer、FBTC、Manta、Merlin、PancakeSwap 等，也包括了权威监管机构及咨询机构，如联合国、SFC、PwC、FTI Consulting 等。

官网：https://blocksec.com/

Twitter：https://twitter.com/BlockSecTeam

推荐阅读👇

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTJKnQAjhicg47N8sLY3SKzqlEcnuEf3pYzPTIqpar2ibkeSeCvjqQsKrLwZwWyTcAXIazKXLQIXEchQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247490504&idx=1&sn=ed76941ba8ee144bdd12cb0ddb7df70c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTIje0g9kj9ic4b9GEzwpo1TCWq94NdL91n7Yt1FYkWUmPEXrkGzHKNvuQbOlu36LFXShpNOTklWvKw/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247491200&idx=1&sn=f0a133511ca63c3deb086c51654e4157&scene=21#wechat_redirect)

#BlockSec

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTKWV4NZYNjUicibdl9UQ4HibVfGa4a6ypSMKArRmWBI3Nibibicuo7YJbQibOC8XKvSMJXYGRFWIz3hsvvfA/0?wx_fmt=png)

BlockSec

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