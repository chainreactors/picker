---
title: BlockSec 深度剖析 Hyperliquid Improvement Proposal 3
url: https://mp.weixin.qq.com/s/NHi30DDhvdhZSyu0Ib36tw
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:29:00.413279
---

# BlockSec 深度剖析 Hyperliquid Improvement Proposal 3

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTIibuBzviaFibkOEUPs1jPAX5rhoHLdxETmS2fqsq4icdCVOWODlf2IL7ZMqTnkSQPrr7FPzLjH08Rb2A/0?wx_fmt=jpeg)

# BlockSec 深度剖析 Hyperliquid Improvement Proposal 3

原创

BlockSec

BlockSec

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/icl4OTbk4icTIibuBzviaFibkOEUPs1jPAX5rNXKhhzIuae7ibZhm3Q8A0ia1Y5doWK25K6xiaJgz8OwzfP3baq3RVxPXg/640?wx_fmt=gif&from=appmsg)

**HIP-3（Hyperliquid Improvement Proposal 3）** 上线主网已经约3个月，自推出以来第三方自定义市场累计成交量已突破130亿美元，这意味着“上新”这件事正在从交易所内部流程，变成一种可被外部开发者直接调用的基础设施能力。

在中心化交易所里，“上新”天然是一项平台权力：哪些标的能交易、何时上线、参数怎么定，基本都由运营与风控流程决定。即便在链上，永续合约这种重基础设施的品类也常被少数团队的部署与治理节奏所约束。

HIP-3的革新在于把这件事从“平台审批”改成“接口开放”：只要满足条件，第三方就能在同一套交易与清算底座上部署新的永续合约市场，让中心化的上新权力被系统化地外包给生态。这一改进不仅降低了创新门槛，还加强了市场的可扩展性。然而，开放接口带来的潜在安全风险不容忽视，如何确保这些市场的运营合规且无恶意行为，仍是HIP-3设计中需要严格审视的关键问题。

**0x1 Hyperliquid：HIP-3 的基座**

Hyperliquid 是运行在自有链上的永续交易基础设施。对 HIP-3 而言，最关键的一点是：撮合、清算与结算由协议底座统一提供，市场能力可以复用，而不是从零搭一套交易系统。

Hyperliquid 采用了双层架构:

* HyperCore：为合约交易优化的定制化 L1 区块链，每秒可处理 20 万笔订单，并具备确定性最终性。
* HyperEVM：应用层，可运行智能合约，兼容 EVM 。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTIibuBzviaFibkOEUPs1jPAX5r4Y4Yv2uxz4AQGwN72UZV1uN31PVmZVWgx7NrmBngpbkz3hJhbBInyA/640?wx_fmt=webp&from=appmsg)

Hyperliquid 的原生 perp 市场（validator-operated perps）在上架上仍更像传统 CEX 的流程：官方根据社区的意愿自行上架永续合约；而下架则由验证者节点投票决定。

The Hyperliquid protocol will support builder-deployed perps (HIP-3), a key milestone toward fully decentralizing the perp listing process.

Hyperliquid 协议将支持构建者部署的永续合约（HIP-3），这是实现永续合约上架流程完全去中心化的关键里程碑。

**0x2 HIP-3：开发者部署的市场**

HIP-3 的理念很简单：在不改动 Hyperliquid 交易与清算底座的前提下，把“新增永续市场”的能力开放给满足条件的 builder。Builder 负责定义市场的关键参数与喂价/运维责任，协议则用统一的保证金与清算引擎承接执行与风控边界；由此，“上新”从平台流程变成可调用的标准接口。

简单来说：builder 可以上架一个基于 HyperCore 引擎的永续合约市场，自行喂价与调整市场参数。

**Builder 的职责边界**

在 HIP-3 中，builder 对一个 perp 市场（market）承担两类工作：定义市场与运营市场。

1. 市场定义（Market definition）：

官方把这部分概括为 oracle definition + contract specifications。在可操作层面，它至少包含：

* oracle 定义：

  包括初始 oraclePx和价格源的定义。builder在定义市场时应该明确定义一个有明确、难以操纵且具备经济实质的标的资产或数据源；在注册资产时就需要提供一个初始的oraclePx 。
* 合约规格：

  在 API 接口中明确定义“资产符号/最小下单单位/最大杠杆”等市场参数（coin、szDecimals、maxLeverage 等）。

* DEX选择：

  Builder 首先部署的是一个 perp DEX（每个 DEX 独立保证金、订单簿、deployer 设置），同时可选择任意报价资产作为该 DEX 的抵押品（例如 USDC），每个 perp 市场都会对应一个 DEX。

2. 市场运营（Market operation）：

官方列举的是 setting oracle prices / leverage limits / settling the market if needed，详细来说：

* 更新喂价：

  通过 setOracle 接口进行对市场的 Oracle Price 进行持续喂价。
* 杠杆上限：

  通过为资产配置对应的保证金表（margin table）来约束最大杠杆——杠杆上限随仓位规模分档设定，从而把可用杠杆限制在预设范围内。
* 必要时结算：

  Builder 可以用 haltTrading 接口中止市场，触发结算——取消所有订单、把仓位按当前 mark price（标记价格） 结算；同一个动作也可用于恢复交易。

目前 HIP-3 市场只支持逐仓（isolated-only），未来可能会支持全仓（cross）。

**Market 上线全流程**

![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTIibuBzviaFibkOEUPs1jPAX5rMKicLysUxBSQcUaGt51rQC1popuUVe60UTAEb5XZuelwrC1QZNRzyuw/640?wx_fmt=png&from=appmsg)

1. Stake

   主网要求 builder 维持 500k HYPE 质押；并且即使把自己 DEX 上的市场都中止了，质押要求仍需维持 30 天。
2. Build

   满足质押门槛后，builder 可以部署 一个 perp DEX。每个 perp DEX 是一套独立的交易域：独立保证金、订单簿、以及 deployer 设置。
3. Set collateral

   该 DEX 的 collateral 可以选择 \*\*任意 quote asset（报价资产），\*\*但若该 quote asset 失去 permissionless quote asset 资格（验证者投票决定），使用它作 collateral（抵押品）的 perp DEX 会被禁用。
4. Add markets

* 前3个市场可直接部署；
* 继续新增市场时，需要通过荷兰拍卖（Dutch auction）获取“新增名额”。

5. Operate markets

市场上线后，builder 的工作变成“把市场跑稳”，即市场运营。

6. Unstake

当 DEX 上所有 market 都已结算后，质押的 500k HYPE 才能解锁，发起 unstake 后会进入7 天 unstaking queue，这段时间质押仍可能被罚没。

荷兰拍卖：当前周期为 31H 一轮，每次起拍价为上次 2 x 最终价格（成交价/最低价）。

**SetOracle：三类价格输入**

在 HyperCore 中，oracle price 主要用于锚定并计算资金费（funding），而 mark price 则作为保证金与清算等风控场景的标记价格（也用于触发 TP/SL 等）。

在原生市场里，mark price并不是某一个喂价的直接结果，而是取三个价格计算结果的中位数：

1. oraclePx + EMA(midPx - oraclePx)
2. median(best bid, best ask, last trade)（本地订单簿盘口价格）
3. 多家 CEX 永续合约中间价 (perp mid prices) 的加权中位数

而到 HIP-3，oracle price 和 mark price 的作用没有发生改变 ，但计算机制发生了改变：

1. setOracle 输入

   a. oraclePx（必须)

   核心定义与 HyperCore 一致。

   b. markPx (可选)

   可以提交 0～2 组 外部 mark price 作为真正的 mark price 计算候选值。

   c.externalPerpPx（必须）

   作为一个 mark price 的参考值输入，用于防止 mark price 发生突然偏离。

Builder 往往会部署 relayer 节点进行喂价，oraclePx

由 relayer 结合外部价格源综合计算；markPx由 relayer 自定义算法计算；externalPerpPx 来自多家 CEX perp mid prices 的加权中位数。

2. 实际 mark price

HIP-3 的 mark price 并不是直接使用 setOracle 的喂价：

* 计算 local mark：median(best bid, best ask, last trade) 。
* 把 local mark 和  markPx（0–2 组） 放在一起，取中位数，得到新的 mark price。

3.setOracle 限制

* 更新频率：两次调用之间至少间隔 2.5 秒，10s 未更新 markPx 将会回退为 local mark price。
* 幅度限制：markPx 每次波动幅度不超过 ±1% ；所有价格都会被 clamp 到当日开盘（start-of-day）值的 10× 范围内。

**7×24H & 非 7×24H：定价机制的差异**

在 HIP-3 中，永续合约市场支持任何资产的上线，而这些资产可以分为 7×24H 资产（全天候交易）和 非 7×24H 资产（只有特定交易时段，非交易时间段现货市场无法交易）。这两类资产的交易时间特性决定了其价格获取方式的差异。

对于 7X24H 资产（例如BTC），可以从CEX/DEX或可信预言机综合获取稳定价格:

![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTIibuBzviaFibkOEUPs1jPAX5rTJ1bJvhjZS8zK33tvicicY6pmLXWjrwKFO9eklR3RxA0PWrTTGH0z6EA/640?wx_fmt=png&from=appmsg)

对于非 7X24H 资产（例如股票）, 只有在开盘时间段才能获得流动性充足、相对稳定的外部市场报价，要维持此类资产在HIP-3中全天候正常运行，需要在休市期间使用另一套定价机制。

以trade.xyz上的股票永续合约市场为例:

1. 在股市开盘期间，使用Pyth等外部预言机服务提供的稳定喂价。
2. 在股市休市期间，基于股票的上一次收盘价，结合内部买卖盘压力进行价格调整。mark prices限制为上一次收盘价上下浮动的1/max\_leverage（e.g.， Tesla 10x -> 10%）。

**清算**

HIP-3 市场主要复用了 HyperCore 的清算逻辑，因此清算触发逻辑沿用平台：当仓位净值（isolated position value）不足以覆盖维持保证金要求时进入可清算状态。

清算相关判断以 mark price 为准，而不是某一笔成交价。

**清算价公式：**

![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTIibuBzviaFibkOEUPs1jPAX5r3LxLDCmbYSoE5fu74EXuTwT3aTdH4stpEA4BDgLWH4WPLuS7ql46mw/640?wx_fmt=png&from=appmsg)

* side = 1（long），-1（short）
* l ：即维持保证金率

![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTIibuBzviaFibkOEUPs1jPAX5rib4vLibb8P9fehPG4KRic1vVSYhmGQ6TiaGMbiaEIX7ckC40TCFmwjpfNxw/640?wx_fmt=png&from=appmsg)

而 MAINTENANCE\_LEVERAGE 的取值来自该仓位对应的保证金档位（margin tier）：先在该档位读出维持保证金率 mmr：

![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTIibuBzviaFibkOEUPs1jPAX5rrgWkMp5Bt3ssicN4NIuEbPPs0acD7AlkKG8eRJeiaRbbd4ex6cSsG6Og/640?wx_fmt=png&from=appmsg)

如果有分档（tiers），清算价对应的仓位名义价值落在哪一档，就用那一档的mmr。

* margin\_available

  isolated：isolated\_margin - maintenance\_margin\_required

进入可清算状态后，系统会优先通过订单簿用市价单平仓；如果能把风险拉回安全区间，剩余保证金仍归交易者。

但在深度不足或跳空时，实际平仓成交均价可能显著差于 mark price，从而形成“清算缺口”。

Isolated position value：指某个 isolated 仓位在当前 mark price 下的净价值（仓位盈亏计入后减去该仓位所绑定的保证金）。

**ADL：**

此时 ADL (Auto-Deleveraging) 机制可以用来在极端情况下进行兜底：

当 isolated position value 变为负值，则触发 ADL，从对手盘仓位中按未实现盈亏和使用杠杆排序，依次在 previous mark price 上强制减仓/平仓，用对手盘的盈利填平缺口，保证系统不出现坏账。

排序标准按照以下标准计算：

![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTIibuBzviaFibkOEUPs1jPAX5rd3yDBXsN2fq3WzvrThZdhE38ribHiaKevJ5pbPiahnRnXcKVaDkKXWWXg/640?wx_fmt=png&from=appmsg)

previous mark price：指触发 ADL 前系统记录的上一笔 mark price。

**例子：**

* 触发 ADL 前，系统的 mark price = 3,000。
* 由于 setOracle 的约束，新的mark price最多只能更新到 2,970（-1%）。
* 但此时订单簿买盘很薄，清算市价单打进盘口后，实际平均成交价 = 2,910（相对 3,000 是 -3%）。
* 多头仓位的亏损按 2,910 结算，可能把该仓位的 isolated position value 打到0以下（出现缺口），于是触发 ADL。
* ADL 随后从对手盘（盈利空头）里挑选仓位，按 previous mark price = 3,000 结算强制减仓/平仓，把缺口转移为“盈利方被动少赚”。

**0x3 风险面概览：**

**可追责约束与关键风险**

**罚没机制（Slashing）：可追责的权限**

HIP-3 把“上新与运营权”交给 builder 的同时，也把责任用一套可执行的罚没规则写进协议：builder 必须质押 HYPE，一旦被认定为不当运营，验证者可以投票罚没并销毁（burn）其质押。

1. 质押要求

   主网要求 builder 维持 500k HYPE 质押，即使 builder 将其全部市场中止，仍需继续维持 30 天（责任不会因为停盘立刻解除）。
2. 触发与表决

   当出现恶意市场操作时，验证者可以发起并执行 stake-weighted vote（按质押权重投票）来决定是否对 builder 的质押进行罚没。
3. 判定原则

   官方明确：罚没不区分“恶意 / 能力不足 / 私钥被盗”等原因，核心看 builder 的行为是否造成了无效状态、长时间宕机或性能退化等后果。
4. 罚没幅度

   罚没比例由验证者投票决定，参考上限：

* 导致无效状态或长时间宕机：最高 100%
* 短暂宕机：最高 50%
* 性能退化：最高 20%

被罚没的质押代币会被销毁，而不是补偿给受影响用户。

**参数配置风险**

1. setOracle

   Oracle prices 一般来源于 builder 的 relayer 服务器，存在中心化的风险，一旦私钥泄漏或者遭受DDoS 攻击，Market中的 oracle price 可能会被恶意操控或长期脱锚。
2. haltTrading

   Builder 可通过 haltTrading 取消 market 中的所有订单，并按当前 mark price 平仓。

   该操作应当谨慎使用，例如存在如下场景:

   当检测到市场被攻击者恶意操控，调用 haltTrading 直接以 mark price 平仓，则会直接兑现攻击者仓位的浮盈(原本攻击者可能难以找到足够对手方订单)，并且可能导致坏账。
3. setMarginTableIds / InsertMarginTable

* InsertMarginTable：定义一个新的 margin table，其中定义了某一类资产的保证金要求和最大杠杆。
* setMarginTableIds：把某个 market绑定到指定的 marginTableId。

  对于一个低流动性/做市能力不足的市场，把 max leverage 设得过高，会增加 ADL 触发概率。

  突然切换 marginTableId 等同于修改用户仓位的维持保证金比例，可能让大量账户在同一时刻从安全变成可清算，引发连环清算。

4. setMarginModes

 ...