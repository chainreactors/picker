---
title: 你没买过 rsETH，但你的 WETH 被冻了
url: https://mp.weixin.qq.com/s/0mQzuGlh8y8ncKP1WUXXQg
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:33:31.551458
---

# 你没买过 rsETH，但你的 WETH 被冻了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2ibKZs4HxyqvF95PyXKXsWbaickmwxnII9yYHxUALnpVwczf3CuVKiaH6b25xVqbCPmZfhXYmN6zZbYia6EgvI28aHQSNIyiayU4MPbtv9Rby0Gk/0?wx_fmt=jpeg)

# 你没买过 rsETH，但你的 WETH 被冻了

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ibKZs4HxyqsAhFuzRv41iaTAVGgEPenfYB3E8DPiaHeLWNx2M602OoMCZyXEgZlpCTHW1jEuGDibjsALY8klXOtv3LZKGib3piaWyChgzHrL12OQ/640?wx_fmt=gif&from=appmsg)

**简介**

核心要点：

* 2026年4月13日至4月19日期间检测到四起攻击事件，涉及 Ethereum、Unichain、Arbitrum 和 NEAR 等多条链，总估计损失约 $310M。
* 攻击向量包括针对 LayerZero DVN 的 RPC 基础设施毒化、MMR 证明伪造、保险基金中的有符号整数滥用，以及保证金交易协议中的循环交换路径利用。
* KelpDAO 事件（$290M）表明跨链桥安全已超越智能合约层面，延伸到链下验证基础设施。五条链上的 WETH 级联冻结和 Arbitrum 的强制状态转换进一步揭示了可组合性如何放大单点故障，以及 "去中心化" 系统的实际信任边界究竟在哪里。

在过去一周（2026/04/13 - 2026/04/19），BlockSec 检测并分析了四起攻击事件，总估计损失约 $310M。下表总结了这些事件，后续小节将对每起事件进行详细分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqvNMIhjY1XiaXYbf9X4htaRnKMpenpM635XFBfTupocIB5DPbaTKD4ypJz7OMHFtO2yMTTjnml9gHJLo4wruLeT3OFdDZYZWviag/640?wx_fmt=png&from=appmsg)

表 1：本周检测到的四起攻击事件概览

**本周看点：KelpDAO**

本事件被选为本周看点，因为其新型基础设施级攻击向量（针对唯一 DVN 的 RPC 毒化而非智能合约漏洞利用）、通过 DeFi 可组合性引发的多链级联影响，以及 Arbitrum 为追回被盗资金执行强制状态转换所引发的治理问题。

2026年4月18日，KelpDAO 的 rsETH LayerZero OFT 跨链桥被攻击，损失约 $290M。LayerZero Labs 将此次攻击归因于国家支持的攻击者，可能是朝鲜 Lazarus Group [1]。根本原因是 KelpDAO 的 1-of-1 DVN 配置，将跨链消息验证缩减为单点故障。攻击者毒化了 LayerZero Labs DVN 所信任的 RPC 基础设施，迫使其为一条伪造的跨链消息签名证明，导致 116,500 rsETH 在以太坊上被释放，而 Unichain 源链上并无对应的发送事件。

背景

LayerZero 是一个基于模块化安全架构的跨链消息协议。其核心的跨链消息完整性由去中心化验证者网络（DVN）保障，DVN 是链下实体，负责独立验证源链上发送的消息确实发生后，才允许在目标链上执行。每个在 LayerZero 上部署的应用自行配置 DVN 设置，包括信任哪些 DVN、需要多少个 DVN 参与、以及共识阈值。这种模块化赋予应用对安全模型的完全控制权，但也意味着完全的责任：弱配置无法被协议本身兜底。

KelpDAO 的 rsETH 作为 OFT（全链可替代代币）部署在 LayerZero 上，桥接路由连接 Unichain（源链）和以太坊主网（目标链）。OFT 标准允许代币在源链上被销毁，并在目标链上从锁定中释放，跨链消息是释放的唯一授权依据。以太坊侧适配器（0x85d456...e98ef3）负责在跨链消息经过验证和传递后，向接收者释放 rsETH。关键问题在于，KelpDAO 将此路径配置为 1-of-1 DVN 设置，指定 LayerZero Labs 作为唯一验证者。这意味着单个 DVN 证明即可授权任何代币释放，无需第二方确认。

为了执行验证职责，LayerZero Labs DVN 查询多个 RPC 节点，确认跨链发送事件确实在源链上发生。这些 RPC 节点包括自运营基础设施和外部提供商，DVN 依赖其集体响应来签署证明。此过程的完整性建立在大多数被查询节点返回真实数据的假设之上。

漏洞分析

该漏洞是基础设施和配置层面的系统性失败，由三个叠加的弱点构成。

第一，KelpDAO 的 1-of-1 DVN 配置消除了验证层的所有冗余。LayerZero 推荐的安全配置明确要求多 DVN 设置并使用独立验证者，确保没有单个 DVN 可以单方面授权一条消息。通过仅依赖 LayerZero Labs DVN，KelpDAO 确保了对该单一验证者的任何攻破都足以授权任意代币释放。

第二，DVN 的故障转移机制将验证查询路由到任何可达的 RPC 节点。这种设计假设节点不可用是偶发的而非蓄意的。然而，这创造了一种条件，攻击者不需要攻破所有数据源：通过 DDoS 使健康节点下线，并准备好被毒化的节点作为唯一可达的替代方案，攻击者可以完全控制 DVN 接收到的数据。

第三，替换 RPC 节点上的 op-geth 可执行文件需要对底层服务器的 OS 级访问权限。确切的初始访问向量未被披露，但攻破两个位于独立集群上的节点可能表明这些服务器的访问控制存在共同弱点。

这三个条件共同构成了完整的攻击链：第一个确保没有独立 DVN 可以交叉验证被证明的消息，第二个确保攻击者可以完全控制唯一 DVN 接收到的数据，第三个提供了使数据操纵成为可能的初始立足点。单独任何一个弱点都不足以成功。没有 1-of-1 配置，查询独立基础设施的第二个 DVN 会拒绝伪造消息。没有故障转移行为，健康节点会否决被毒化的节点。没有服务器攻破，攻击者将无法注入伪造数据。

攻击分析

以下分析基于交易 0x1ae232...4222 以及 LayerZero Labs 的官方事件声明。

Step 1：攻击者获取了 LayerZero Labs DVN 所信任的特定 RPC 节点列表。该列表构成了一个高价值情报目标，因为知道确切节点使攻击者能够策划精准的手术式行动，而非广泛的基础设施攻击。

Step 2：攻击者获得了两个 RPC 节点的 OS 级写入权限，并将运行中的 op-geth 二进制文件替换为恶意版本。这两个节点据描述运行在互不相连的独立集群上，暗示初始访问向量涉及共享的上游依赖（例如被泄露的部署凭证、CI/CD 流水线、或对同时拥有两处访问权限的运维人员的社会工程攻击）。LayerZero Labs 未披露确切的初始访问方式。此步骤是所有后续数据操纵的前提条件。

Step 3：恶意 op-geth 二进制文件实现了定向响应逻辑：仅向 DVN 的 IP 地址返回伪造的交易数据，同时向所有其他请求者提供真实的区块链状态，包括 LayerZero 自身的监控基础设施、区块浏览器和扫描服务。这种选择性毒化使攻击对所有现有可观测性系统不可见；从任何外部视角看，源链运行正常。

Step 4：DVN 的内部共识要求被毒化和未被攻破的 RPC 节点之间达成一致。为解决这一冲突，攻击者在攻击窗口期间（太平洋时间 10:20 至 11:40）对剩余健康节点发起 DDoS，触发 DVN 的故障转移逻辑，迫使其完全依赖被毒化的基础设施。此步骤必不可少，因为健康节点否则会返回与伪造响应矛盾的真实数据。

Step 5：由于 DVN 现在仅接收攻击者控制的数据，一条伪造的 LayerZero 跨链消息被呈现为有效。DVN 在以太坊目标端点上证明了 nonce 308，而该 nonce 在 Unichain 上没有对应的出站事件（源端点仍报告最大出站 nonce 为 307）。

Step 6：以太坊侧 rsETH 适配器收到经有效证明的消息后，向攻击者的接收地址（0x8b1b6c...0d3b）释放了 116,500 rsETH，该地址在数小时前已通过 Tornado Cash 预先注入资金。被盗代币随即被分散到七个分支钱包，并通过 Aave 抵押仓位、直接兑换 ETH、以及跨链至 Arbitrum 进行清算，最终收益汇聚至以太坊上的 0x5d3919...7ccc 及 Arbitrum 上的对应归集地址。

Step 7：恶意二进制文件在执行完成后触发自毁程序，删除自身及所有本地日志和配置文件。这极大地阻碍了事后取证恢复，体现了攻击者的高度操作成熟度。

Step 8：攻击者随后试图通过同一路径再次攻击以获取额外的 40,000 rsETH（约 $95M），但在 KelpDAO 检测到异常并暂停以太坊主网及各 L2 上所有相关合约后被阻止 [2]。

更广泛的影响

损害远不止于最初 $290M 的跨链桥漏洞。攻击者将约 89,567 rsETH（约 $221M）存入多个市场的 Aave，以 E-Mode 93% LTV 借出 WETH [4]。由于 Aave 无法在链上区分合法桥接的 rsETH 和通过伪造消息释放的代币，"有毒" 抵押品被视为完全有效。由此引发的 WETH 储备冻结从以太坊传导至 Arbitrum、Base、Mantle 和 Linea，波及到完全没有接触过 rsETH 的用户。这种级联传导，从单一跨链桥配置缺陷到多链借贷市场中断，说明了 DeFi 可组合性如何放大单点故障的影响范围和成本。

事件的后续发展同样引发了关于去中心化运营现实的重要问题。LayerZero Labs 宣布其 DVN 将不再为使用 1-of-1 配置的应用签名 [1]，这意味着仅靠协议层面的去中心化无法弥补应用层面的配置缺陷。

在链层面，Arbitrum Security Council 执行紧急操作，冻结了攻击者在 Arbitrum One 上持有的 30,766 ETH。据 BlockSec 分析 [5]，这是通过链级强制状态转换实现的：Security Council 临时升级以太坊 inbox 合约，注入一笔模拟攻击者地址的无签名 L1 到 L2 消息，然后恢复原始合约实现，全程不需要持有人签名 [3]。

这一操作是治理框架定义的紧急权力的合法行使，在与执法部门协调后公开透明地执行。但它同时表明，L2 链在设计上保留了中心化的紧急干预能力：原则上，Arbitrum One 上的任何资产都可以通过同样的机制被 Security Council 移动。正如本事件在每一层所揭示的，系统理论上的信任模型与其实际信任边界之间的差距，才是最关键的风险所在。

结论

本事件表明，跨链桥安全不能仅归结为协议正确性。LayerZero 协议本身按设计运行；漏洞完全存在于其上层的运营层面。核心教训是链下验证基础设施属于信任边界的一部分，其安全态势必须与其保护的价值相匹配。

以下三项缓解措施中的任何一项都能单独防止此次事件：

* 多 DVN 配置：要求多个独立 DVN 达成共识，将使单个 DVN 被攻破不足以授权一条消息，无论该 DVN 被欺骗得多彻底。
* 具备故障感知能力的 RPC 选择：在活跃验证窗口期间可达节点突然减少，应被视为潜在攻击信号而非常规可用性事件。DVN 实现应在节点集减少时暂停或告警，而非仅凭剩余节点继续运行。
* RPC 基础设施加固：能够替换生产 RPC 节点上正在运行的可执行文件，表明底层服务器的访问控制不足。DVN 依赖的用于获取源链真实状态的基础设施，应享有与 DVN 签名实例相同的安全边界。

更广泛地看，任何依赖链下证明的跨链桥或协议都应审计的不仅是智能合约层，还包括从源链事件到目标链执行的完整数据管道。当数亿美元依赖于 RPC 基础设施时，默认信任其可靠性的假设已不再成立。

参考资料

[1] LayerZero Labs，"KelpDAO Incident Statement"，2026年4月20日。https://x.com/LayerZero\_Core/status/2046081551574983137

[2] KelpDAO，"April 18 Incident: Additional Context"，2026年4月21日。https://x.com/KelpDAO/status/2046332070277091807

[3] Arbitrum，"Security Council Emergency Action"，2026年4月21日。https://x.com/arbitrum/status/2046435443680346189

[4] LlamaRisk，"rsETH Incident Report"，2026年4月20日。https://governance.aave.com/t/rseth-incident-report-april-20-2026/24580

[5] BlockSec，"Arbitrum Security Council Freeze Mechanism Analysis"，2026年4月21日。https://x.com/Phalcon\_xyz/status/2046467830498173088

**本周其它事件**

Hyperbridge

2026年4月13日，Hyperbridge，一个基于以太坊的跨链消息桥，因 MMR（Merkle Mountain Range）证明验证逻辑中的输入验证缺失被攻击，损失约 $242K。函数 MerkleMountainRange.VerifyProof() 未强制检查 leaf\_index < leafCount，使攻击者能够伪造跨链证明并执行特权操作，包括铸造 1,000,000,000 DOT 代币。

背景

Hyperbridge 在以太坊侧采用验证器和调度器模型处理跨链消息。在以太坊上，合约 HandlerV1 根据存储的 overlayRoot 验证提供的证明，如果证明被接受，则将消息分发到目标模块，如合约 TokenGateway。

合约 TokenGateway 是一个特权资产管理模块。除了常规的资产桥接外，它还支持治理类操作，如资产创建、注销和管理员管理。对于以 ERC6160Ext20 实现的桥接资产，管理员可以通过调用函数 changeAdmin() 直接转移铸造权限，新管理员随后可通过函数 mint() 铸造任意数量的代币。

这意味着整个资产桥的安全性取决于 HandlerV1 中证明验证路径的正确性。如果伪造的消息能通过验证，下游模块将把攻击者控制的载荷视为真实的跨链指令。

漏洞分析

核心问题在于合约 HandlerV1（0x6c84ed...6d64）中的 MMR 证明验证流程。入口函数 handlePostRequests() 首先根据攻击者提供的输入构建 MmrLeaf(leaf.kIndex, leaf.index, commitment)。然后调用 MerkleMountainRange.VerifyProof() 执行证明验证。

MerkleMountainRange.VerifyProof(root, request.proof.multiproof, leaves, request.proof.leafCount)

然而，VerifyProof() 仅检查 root == CalculateRoot(proof, leaves, mmrSize) 是否成立，并不验证每个 leaf.index 是否在有效范围内（即 leaf.index < leafCount）。通过选择 leafCount = 1 和 leaf\_index = 1，攻击者使 CalculateRoot() 跳过将伪造的请求承诺折叠进计算根的过程，直接返回峰值根。这破坏了消息到证明的绑定关系，使任意载荷能以历史 overlayRoot 的名义通过验证。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqusPFVgZQjeibwd5Gq4MOQeFDzIQelTYT63g7qfZPBrKVRFmOknX9Cq9LLh2qCBaz35O8IdXsuiccSPlia8AxrAoOdFTE5ibZBWnXw/640?wx_fmt=png&from=appmsg)

图：VerifyProof 函数缺失 leaf\_index 边界检查的代码片段

攻击分析

以下分析基于交易 0x240aeb...1109 [1]。

Step 1：攻击者 EOA 0xC513...F8E7 在同一笔交易中部署了辅助合约 0x518A...8f26 和 0x31a1...ca9AB。

Step 2：辅助合约 0x31a1...ca9AB 通过 HandlerV1 的漏洞验证路径提交了伪造请求。由于 VerifyProof() 未拒绝越界的 leaf\_index，伪造的请求承诺被排除在根计算之外，但证明仍与历史 overlayRoot 匹配。

Step 3：伪造消息被接受后，HandlerV1 将其分发到 TokenGateway，执行 ChangeAssetAdmin 操作。这将 DOT 代币的管理员更改为攻击者控制的辅助合约 0x31a1...ca9AB。

Step 4：辅助合约铸造了 1,000,000,000e18 DOT 代币。

Step 5：辅助合约通过 Odos Router V3 将新铸造的 DOT 代币兑换为 108.2 ETH。

Step 6：攻击者将 108.2 ETH 转移至其 EOA 账户。

结论

本事件由 Hyperbridge 的 MMR 验证逻辑中的证明验证不当导致。由于未强制检查 leaf\_index < leafCount，攻击者可以伪造一条承诺从未实际包含在计算根中的消息，却仍能通过历史状态根的验证。缓解措施应在证明验证之前强制执行严格的边界检查，如 leaf\_index < leafCount。

参考资料

[1] BlockSec，"Hyperbridge Attack Analysis"，2026年4月13日。https://x.com/Phalcon\_xyz/status/2043601549893738970

Dango

2026年4月13日，Dango，一个构建在 Cosmos AppChain 上的永续合约 DEX，因缺少符号检查被攻击，损失约 $1.5M。函数 replen...