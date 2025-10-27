---
title: 预言机——黑暗森林中的神谕or神罚？
url: https://mp.weixin.qq.com/s?__biz=MzkzODE2NjgyNQ==&mid=2247502694&idx=1&sn=5416b1e12b0fd701782e75a409b97bf0&chksm=c286d420f5f15d3614b6f0fc569b618819d2d08d2ed9b6e05f981ddbd3ba0862cf318540f47a&scene=58&subscene=0#rd
source: 零鉴科技
date: 2023-03-18
fetch_date: 2025-10-04T09:58:39.122796
---

# 预言机——黑暗森林中的神谕or神罚？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/e9yMd8aXlde3sXl0vzPPv38dSyhMGmmu4aAkalk1G3HofxKBicujQIDHQZEWVoNU1xanSNvk7AJyEOZ6WcC2lqw/0?wx_fmt=jpeg)

# 预言机——黑暗森林中的神谕or神罚？

原创

零鉴科技

零鉴科技

![](https://mmbiz.qpic.cn/mmbiz_png/wQM6iajf8b9oe3ic0wT2bOJK3Rp60A7u4s9Wib7y0OY39HQRJmwa3SyvQ7J8TRgk8FfbxuziadYy1G9tZyOCj48hgA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qPZVWl5XibY8f0EpEYU1EtbFXZkUwYTTAjgSdOQ5767gCeGialK8NVtoM2XJyKiccBczKAY8NPMnyNTP4roadySEg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/e9yMd8aXlde3sXl0vzPPv38dSyhMGmmuV2YHyFKHZt7KAkACAP2qicdQ6gmeDn6bPX7lJoicI8icuqUMmhRYgrJUQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/HdAtLMKtFXcvCO6I9V9gFsdWlGpqV7Q6LcGibc4P68hskqGiaLVniaL3NfB5TUfEIicX1Mq2VS1Xc1iblPRfrvgJAbg/640?wx_fmt=png)

在电影《黑客帝国》中有一位先知，名叫 Oracle，虽然看似不起眼，但其实她才是最关键策划者，把三大势力都放到她的局中。

而在区块链这一黑暗森林中，也有 Oracle，同样扮演了非常重要的角色，能够将区块链连接至真实世界中的数据和系统，但在这里，中文翻译不叫先知，而是叫预言机。

那什么是区块链预言机呢？

01

概述

**预言机**

预言机（Oracle），单从字面意思上来看，很容易地被大家联想成预测某些未来事件的机器，但其实不然。

这个名字翻译得并不形象，很容易地误导大家对它的理解。

先举个例子，比如说张三和李四想对这个星期六的比特币价格进行下注。

张三认为比特币的价格将在 8500 美元或更高，相反，小黑认为在 8000 美元或更低。

于是，他们设计了一个智能合约（双方都会向其发送资金），谁预测的价格更靠近实际价格，谁就赢得了资金。

到了星期六，智能合约取得比特币的价格后，比如返回的值是周六比特币价格为 8600 美元，那么智能合约将根据其条件执行并将所有资金发送给张三。

以上看似完成了一个去中心化且安全的赌约，但是「智能合约取得比特币的价格」这一过程并不简单。

如果直接让矿工在互联网上获取比特币的价格，我们无法保证每个节点获取的结果相同，这时验证者就会认为这是错误的数据，从而影响整个区块链达成共识。

![](https://mmbiz.qpic.cn/mmbiz_png/e9yMd8aXlde3sXl0vzPPv38dSyhMGmmu5LaDaXaglWgBRXMiayoKovqR2z1Aun9sibYnW6nYvgzPkAlOZwibibuzMg/640?wx_fmt=png)

像上面这样需要用到但又得不到链下数据的例子还有很多。我们迫切的需要一种工具使得区块链能够获取链下数据，从而预言机就应运而生了。

也就是说预言机是一个可以将外界信息传入到区块链工具。

**预言机的分类**

预言机可以分为链上和链下预言机。链上预言机因为闪电贷的出现，遭到了大量的攻击，并且它的能力有限，所以本文我们主要分析链下预言机。

从另一个角度，按照预言机系统运行的方式，又可以将预言机分为中心化预言机和去中心化预言机。

**预言机的工作原理**

预言机（Oracle）其实可以看作用户的智能合约和 Web Server 的中间件。

它会在链下向 Web Server 请求链下数据并传给链上的预言机合约，而用户的智能合约通过调用预言机的链上智能合约就可以获取链下数据。

我们以 Chainlink 为例，分析预言机的工作原理。

![](https://mmbiz.qpic.cn/mmbiz_png/e9yMd8aXlde3sXl0vzPPv38dSyhMGmmuUPlOemvywTcmcGRBxDHNAa4oibe88bF7NtP6Qvlrc4fefoufKibpkr5w/640?wx_fmt=png)

上图是 Chainlink 提供的 Oracle 的使用流程。白色的部分指链上，蓝色的部分指链下。

链上部分工作原理：以Chainlink为例，用户合约继承 Chainlink 提供的 ChainlinkClient 合约，然后向 Oracle Contract 发起请求数据的外部调用并支付一定的 LINK Token，此后 Oracle Contract 就会发起回调函数返回 ChainlinkClient 所请求的链下数据。这一过程就是 Chainlink 的链上工作流程。虽然在细节上可能有所不同，但大多的 Oracle 在这一过程其实与 Chainlink 大同小异。

链下部分工作原理：链下部分的工作其实就是之前提到的「Oracle 也会在链下不断地向 Web Server 请求链下数据并传给链上的 Oracle 合约」。不同的 Oracle 在这一过程中使用不同的方式。根据此方式的不同大致可以将 Oracle 分成中心化的 Oracle 和去中心化的 Oracle：

中心化的 Oracle：往往由唯一确定的一个或几个节点在互联网获取向 Oracle 合约传送链下数据。这样的结构使得 Oracle 的设计更简洁且简单，但同时却使得数据的可靠性，系统的稳定性难以得到保障。如易发生单点故障、易受攻击等，且需要 Oracle 的用户完全信任一个或者几个节点。往往大多数项目初期短期内选择使用自己搭建的中心化 Oracle 服务。如 Compound 使用的就是中心化的 Oracle 提供的数据。

![](https://mmbiz.qpic.cn/mmbiz_png/e9yMd8aXlde3sXl0vzPPv38dSyhMGmmucf24g8JS60HZm0w5xF2LhqD2FDE7R9OKJ1CfUibRSTg8QUnsVywXPmw/640?wx_fmt=png)

去中心化的 Oracle：被更广泛的使用，因为它提供了更高的数据可靠性以及更高的系统稳定性。一个去中心化的 Oracle 往往有许多独立的节点，它们需要对链下数据达成共识，不同的 Oracle 节点获取到的数据不一定是相同的。因此他们需要一套共识机制，从而得出最终 Oracle 提供的数据结果。图中两个常见的 Oracle 共识机制。下面这个图里是两个最常见的去中心化预言机的链下结构。

![](https://mmbiz.qpic.cn/mmbiz_png/e9yMd8aXlde3sXl0vzPPv38dSyhMGmmuGPMOPYZSOgEUpNa05DzCorTSI6zZGSRB16xsGfV4syrKZnE5KYLxsw/640?wx_fmt=png)

图A中，Oracle 节点各自独立地向 Oracle Contract 提交链下数据，最终根据 Oracle Contract 中的逻辑达成对链下数据的共识。

图B中，Oracle 节点组成了一个去中心化的网络，也可以把它理解成一条去中心化的基于节点信誉二层网络，这些 Oracle 节点在链下直接达成共识，并由一个提案者向 Oracle Contract 提供链下数据以及 Oracle 节点们对这条数据的聚合签名。

如果该聚合签名签名者的数量超过设定的阈值，那么就能通过 Oracle Contract 的验证，这时链下数据就会被存入 Oracle Contract 中以达成对链下数据的共识。

![](https://mmbiz.qpic.cn/mmbiz_png/e9yMd8aXlde3sXl0vzPPv38dSyhMGmmuIvH9b1d7yjFEqx3nDhu6jl1dvUb9sbPVPiaT2ejcBTMDScuIw4ichyYA/640?wx_fmt=png)

作为去中心化的 Oracle 的代表，Chainlink 使用了图B中的设计模式，因为它能更好地节约gas费。

**预言机的应用**

前面说到，预言机其实是一个可以将外界信息写入到区块链的工具。所以说一切需要与链下进行数据交互的 DApp 都需要使用到预言机。

如借贷平台、稳定币、NFT、金融衍生品交易平台、快递追踪/IoT、博彩游戏、保险、预测市场等。

DeFi：包括借贷平台、稳定币和金融衍生品交易平台在内的 DeFi 领域是现在预言机服务最主要的使用者。AAVE，Compound 等借贷平台需要知道某种加密货币的价格，如 ETH / USDT 的价格，来计算抵押物价值、用户健康度以及确定是否某个用户的抵押物价值过低需要被清算等。而现有区块链内部系统中的 DEX 的所提供加密货币价格十分容易被闪电贷攻击而篡改。所以这些借贷平台往往都会依靠链下预言机提供的加密货币的价格。类似 DAI 这样的稳定币系统，也同样需要获取 ETH 的实时价格，来判断所抵押的加密货币是否达到了平仓价格进而触发平仓。另外，像 Synthetix 这样的去中心化金融衍生品交易平台也需要链下的金融数据才能正常运作。

![](https://mmbiz.qpic.cn/mmbiz_png/e9yMd8aXlde3sXl0vzPPv38dSyhMGmmuxiaUh6ZzI27EYdMXCj6xkAY64GaPm69gGVelB2foPfMYQvZ0LTmqJNg/640?wx_fmt=png)

NFT：NFT 越来越被大众所认可，但是 NFT 和链下数据的绑定和交换一直是一个难以解决的难题。比如与体育运动相关的 NFT，为进球数量达到一定数量的球星生成 NFT，这个时候我们需要每次手动地操作吗？这时我们可以使用预言机去自动且快速地基于链下数据生成 NFT。

博彩游戏：现在的大多数博彩游戏都是在链上生成随机数，所以很容易被预测和破解，导致资产被盗。大家有兴趣的可以去看一下博彩 DApp 被盗的相关研究报告，很多因为随机数问题被盗的。比如 BetDice、Dice2Win。而使用预言机提供的 VRF 服务（后面会提到），可以保证向链上提供链下生成不可预测且可验证的随机数，博彩合约就可以使用该随机数设计游戏规则了。

保险：保险行业的用户们其实迫切地需要一个公开透明的保险产品，以保障自己的利益。而区块链技 术就为此提供了基石。但保险中最为重要的一环——理赔，由于这一过程涉及到了链下的信息，难以在链上直接完成。这时需要预言机提供链下生成的是否理赔的报告结果传到链上，保证保险流程的正确运行。在区块链上已经有一些保险相关的 DApp 。如Nexus Mutual 保险协议，利用预言机在将理赔报告并发布到区块链之前验证理赔。

除此之外预言机的应用其实还有很多，如物联网、预测市场等。

**主流的预言机服务提供商**

**1、Chainlink**

https://chain.link/

Chainlink 是行业内最大的预言机服务提供商，市值一度曾超过十亿美元大关。它主要为基于 EVM 的一层网络、二层网络以及 Solana 提供去中心化的预言机服务。

主要包括提供链下数据、VRF 以及 Chainlink Automation（智能合约的自动化调用）服务。被大量的其他顶尖 Web3 应用所使用，如 AAVE, Compound, Synthetis, ENS 等。

**2、Universal Market Access (UMA)**

https://umaproject.org/

UMA 是一个基于以太坊的预言机。但 UMA 除了提供预言机服务外，还为用户提供智能合约模板「以创建金融资产以及组合资产合约」。

通过使用 UMA 提供的平台，用户可以轻易地将现实世界的金融资产数字化、代币化。

通过这种方式，Defi 可以更加轻松广泛地渗入现实世界。

此外，UMA 同样也是开源且去中心化的——所有智能合约都由 UMA 社区运行和管理，他们使用 UMA 代币投票和提交提案。

**3、API3**

https://api3.org/

API3 是一个社区管理的预言机。API3 Oracle直接从数据来源方请求一手数据，这与其他使用预言机节点作为中介来搜索、查询和传递数据的预言机有所不同。

**4、WinkLink**

https://winklink.org/#/home

首个波场生态全系统预言机，可以认为是波场链上的Chainlink。它除了提供普通资产的价格数据之外，还为区块链提供合成资产的价格数据。

此外WINkLink作为去中心化预言机还建立了保证金惩罚制度，激励节点诚实守信。采用博弈论的原理激励节点提供准确的数据，提高预言机的安全性。

除此之外，区块链中还有 Band Protocol, Nest Protocol, plugchain, XYO Network, WINkLink, DIA 等预言机服务提供商。

02

深入了解预言机

**使用Chainlink预言机**

使用 Chainlink 预言机为我们的智能合约提供链下数据：

官方文档：https://docs.chain.link/data-feeds/price-feeds

![](https://mmbiz.qpic.cn/mmbiz_png/WO9VV25obe6EhYScXDsYM5JuQxsEy23Pff3wrHnAoiavctIBg38X8h2KHUOp2wxgUmryib4cicXz9Izw0yibgD3omw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/UmhticF6CACyKsVxxyCnaMdszMEHWomU2Uvlzic6EOWf8F4t7tbmgEILVzN5nEibELicOV6rg88nWhw8xQAh6WnmUA/640?wx_fmt=png)

1、首先我们需要获取预言机的地址，以BTC/USD的价格为例，它在Goerli测试网的地址为：

0xA39434A63A52E749F02807ae27335515BA4b07F7。

2、从 @chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol 文件中引入接口AggregatorV3Interface。并将预言机地址作为实现。

3、现在我们只需要在合约中调用latestRoundData()就可以获取到BTC/USD的最新价格。

![](https://mmbiz.qpic.cn/mmbiz_png/e9yMd8aXlde3sXl0vzPPv38dSyhMGmmupfYicv72mg6W3YWP9smq6xDh8wUwiaIfpfbQ7R1ib08dZlqID3aUZjqrg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HibnYZIeibmicUolebQVsdiboTCP6xs1awxvKEhrSnHRtCsObWicGicnGJjFzJziaYR5xLS5PxLibj9ydzk25LMbrl5jBw/640?wx_fmt=png)

Chainlink 免费提供了主流的代币和货币的价格，可以直接用上面的方法取得。

同时Chainlink还支持自定义 API 的预言机，这时 Chainlink 的 DON（去中心化预言机网络）会从智能合约获取我们自定义的 API 代码，然后获取并上传数据到链上，不过这样的自定义 API 需要付费使用，Chainlink 仅接受 Link 作为支付代币。

**常见预言机攻击面**

预言机的VRF为链上博彩提供数据支撑

博彩一直是一个多金且游走在法律边缘的行业。它的本质其实就是对某一随机事件的预测，所以它需要一个不可预测且可验证的随机数。

区块链提供了一个透明且去中心化的平台，这两个特点迎合了博彩行业用户的需求。

但是区块链却很难独立的产生随机数，因为智能合约需要不管在何时何地运行都得到一致的结果，没有随机性可言，而 BlockHash 这样的随机数很容易被出块者篡改。导致博彩合约难以在区块链系统中得到需要的随机源。

而 Oracle 就能提供链下生成的随机数满足这一需求。

VRF (Verifiable Random Function)是一个可证明和验证的随机数生成器 (RNG)。

它常被 Oracle 用于向链上提供不可篡改且可验证的随机数。同时它也在 PoS 的区块链中，常常被用于作为随机选举出块者和验证者的随机源。

![](https://mmbiz.qpic.cn/mmbiz_png/e9yMd8aXlde3sXl0vzPPv38dSyhMGmmu3jPj4VhmmOia8LIqDsSjmOoIJgM95DFEcOrdWHYUNq89nrLxWgvlayA/640?wx_fmt=png)

VRF 的数据输入通常包含一对公钥和私钥（也称为“verification key”和“secret key”）以及一个 seed 。

Oracle 利用这三个数据为博彩合约提供不可篡改且可验证的随机数的过程如下：

1、博彩合约向 VRF 合约发起随机数请求，然后 VRF 合约会先通过一个固定算法生成一个 preSeed，同时记录下当前这笔交易的 blockNumber，然后将 preSeed 作为 Event Log 内容发送至以太坊上。

2、Oracle 会监听到此 Event 后，就得到了 preSeed 和 blockNumber，并且根据 blockNumber 得到对应的blockHash。

3、在等待指定数量的区块确认之后，Oracle 用自己的私钥将上述包括 preSeed、blockHash 在内的参数作为前面提到的 seed 去生成随机数以及Proof，并将它们提交回 VRF 合约中。

4、这时VRF合约会根据自己生成的 preSeed，blockHash 和公钥去验证这个随机数和 Proof。

5、如果验证通过，这个随机数就可以被博彩合约使用了。如果验证不通过，那么这次 Oracle 提交的 Proof 交易就会被回滚，这样 Oracle 节点就无法获取奖励。

VRF 之所以能产生不可预测的随机数，主要是因为采用了两个未知因素：

*1.  BlockHash（在区块被矿工打包确认前是未知的，被打包之后才能...