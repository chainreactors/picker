---
title: 慢雾：Compound Finance V2 安全审计手册
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500572&idx=1&sn=9eac34a1334593433eb57a9814175dbe&chksm=fddebd9bcaa9348d60952988c07e8d73ffdaf3be9aeb80d68777ac58e7a66be5ff3f669c51d8&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-10-17
fetch_date: 2025-10-06T18:52:33.023357
---

# 慢雾：Compound Finance V2 安全审计手册

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLaNgaoicfHPnnQDjIP1j0Urp9fiagJMII1sTozyvVvMdsHpmC5xTV6ZedRaO1RxicEGPUdVicrew3s2Xg/0?wx_fmt=jpeg)

# 慢雾：Compound Finance V2 安全审计手册

原创

慢雾安全团队

慢雾科技

**引言**

随着 DeFi 生态系统的迅速发展，Compound Finance V2 作为该领域的先驱者之一，凭借其创新的借贷模式吸引了大量用户。然而，任何复杂的分布式应用都面临着潜在的安全威胁，尤其是涉及到价值数百万甚至上亿美金的资金流动时。因此，对 Compound Finance V2 及其分叉项目进行全面且细致的安全审计显得尤为重要。本手册旨在为开发者、安全研究员以及 DeFi 爱好者提供一份详尽的安全审计指南，帮助大家更有效地识别和防范潜在的风险。

## **1. 项目背景概述**

Compound Finance V2 是一个基于以太坊区块链构建的开放式借贷平台，允许用户存入各种 ERC-20 底层代币并从中赚取利息，同时也允许以支付利息的形式借用市场中的代币。通过引入“利率市场”的概念，它实现了去中心化的资金池管理和自动化的利率调整机制。

##

## **2. 项目架构分析**

Compound Finance V2 的核心架构组件包括：

* Comptroller：控制整个系统逻辑，如利率计算、账户状态维护等。
* cToken：实现 ERC-20 标准的自定义代币，代表用户在系统中的权益。
* InterestRateModel：计算存款和借款利率的模型。
* PriceOracle: 提供资产价格的预言机。
* Governance：负责社区治理相关的功能。

###

### **2.1 Comptroller**

Comptroller 合约是 Compound Finance V2 的中枢神经系统，它负责协调各个 cToken 实例的行为。主要职责有：

* 管理市场列表，确定哪些市场是活跃的。

```
   function enterMarkets(address[] memory cTokens) override public returns (uint[] memory) {}
   function exitMarket(address cTokenAddress) override external returns (uint) {}
   ...
```

* 执行跨市场操作的各类检查，如用户的头寸健康度检查等。

```
   function mintAllowed(address cToken, address minter, uint mintAmount) override external returns (uint) {}
   function redeemAllowed(address cToken, address redeemer, uint redeemTokens) override external returns (uint) {}
   function borrowAllowed(address cToken, address borrower, uint borrowAmount) override external returns (uint) {}
   function repayBorrowAllowed(address cToken, address payer, address borrower, uint repayAmount) override external returns (uint) {}
   function liquidateBorrowAllowed(address cTokenBorrowed, address cTokenCollateral, address liquidator, address borrower, uint repayAmount) override external returns (uint) {}
   ...
```

* 设置和更新全局参数，如借款限额、抵押因子、清算阈值等。

```
   function _setCloseFactor(uint newCloseFactorMantissa) external returns (uint) {}
   function _setCollateralFactor(CToken cToken, uint newCollateralFactorMantissa) external returns (uint) {}
   function _setLiquidationIncentive(uint newLiquidationIncentiveMantissa) external returns (uint) {}
   function _setMarketBorrowCaps(CToken[] calldata cTokens, uint[] calldata newBorrowCaps) external {}
...
```

**2.2 cToken**

每个支持的 ERC-20 代币都有一个对应的 cToken 实例（即 CErc20 / CEther 合约），用于处理该代币所有与项目的交互操作。每个 cToken 除了实现了基本的代币转账功能外，还添加了一些特定于 Compound 的功能，如借贷、累积利息和分配奖励。所以我们可以将 cToken 看作是用户在 Compound 上存入资产的凭证和用户进行借贷操作的入口。

当用户将底层的资产代币存入合约后，即可铸造对应的 cToken 代币，cToken 与标的资产的兑换比例按照如下公式计算：

```
exchangeRate = (totalCash + totalBorrows - totalReserves) / totalSupply
```

###

### 注意：borrows 表示借款额，cash 表示资金池余额，reserves 表示储备金。借款利率由使用率决定，存款利率由借款利率决定。

用户一般通过与不同的 cToken 合约交互来在不同的市场中进行代币的借贷操作：

```
    function mint(uint mintAmount) override external returns (uint) {}
    function redeem(uint redeemTokens) override external returns (uint) {}
    function redeemUnderlying(uint redeemAmount) override external returns (uint) {}
    function borrow(uint borrowAmount) override external returns (uint) {}
    function repayBorrow(uint repayAmount) override external returns (uint) {}
    function repayBorrowBehalf(address borrower, uint repayAmount) override external returns (uint) {}
    function liquidateBorrow(address borrower, uint repayAmount, CTokenInterface cTokenCollateral) override external returns (uint) {}
    ...
```

**2.3 InterestRateModel**

InterestRateModel 合约定义了计算利率的方法。不同的市场可能会使用不同类型的利率模型，以适应各自的风险偏好和流动性需求。

Compound V2 的市场中使用的利率模型主要有两种，一种是直线型，一种是拐点型。

直线型模型的借款利率计算公式如下：

```
borrowRate = utilizationRate * (multiplierPerBlock/1e18) + baseRatePerBlock// 借款利率 = 资金使用率 * 斜率 + 基准年利率
```

资金使用率的计算公式如下：

```
utilizationRate = borrows / (cash + borrows - reserves)// 资金使用率 = 总借款 / (资金池余额 + 总借款 - 储备金)
```

存款利率则随着借款利率线性变化：

```
// 存款利率 = 资金使用率 * 借款利率 *（1 - 储备金率）supplyRate = utilizationRate * borrowRate * (1 - reserveFactor)
```

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaNgaoicfHPnnQDjIP1j0UrpJPz7xQuDMB1uXXGRNjufic8e5iaKBTVOJtG8LibUEZP8Bibq6Cv4rcC3ibQ/640?wx_fmt=png&from=appmsg)

使用率逐渐升高则意味着资金池里的钱在逐渐减少，当达到一定峰值时可能会导致用户无法正常存款和借款。为尽量避免这种情况，Compound 推出了第二种利率模型 —— 拐点型。

拐点型的借款利率计算公式如下：

```
// 未达到峰值拐点时则与直线型相同：borrowRate = utilizationRate * (multiplierPerBlock/1e18) + baseRatePerBlock
// 达到峰值拐点过后的公式如下，其中 jumpMultiplierPerYear 表示剧增的斜率，kink 表示利用率的峰值拐点borrowRate = jumpMultiplierPerYear * (utilizationRate - kink) + (kink * (multiplierPerBlock/1e18) + baseRatePerBlock)
```

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaNgaoicfHPnnQDjIP1j0Urp3vyk9eVX9Sju6qYaVPxEq1ebqbYvZJsvrLDphxB5NKeibmhtA2r4vSg/640?wx_fmt=png&from=appmsg)

当使用率达到一定的峰值时，会瞬间大幅提高借款利率和存款利率，激励用户多存款少借款，以此将使用率控制在合适的范围，这个峰值也被称为拐点（一般是利用率达到 80% 时）。

### **2.4 PriceOracle**

PriceOracle 合约负责获取外部市场价格信息，并将其转换为系统内部使用的数值，这对于准确计算用户的头寸价值至关重要。

```
   function getUnderlyingPrice(CToken cToken) public override view returns (uint) {        ...    }
```

###

### **2.5 治理机制与激励模型**

Compound 引入了一种独特的治理机制，允许持有治理代币(COMP) 的用户参与重要决策的投票，如更改某些参数或添加新的资产类型。通过发行治理代币(COMP)，Compound 激励用户积极参与平台活动，并为贡献者提供奖励。详细内容可参考 Compound 官方文档和代码仓库。(https://docs.compound.finance/v2/; https://github.com/compound-finance/compound-protocol)

## **3. 交互流程**

接下来，我们通过简单示例来说明用户在 Compound Finance V2 上进行交互的大致过程：

### **3.1 存款和赎回流程**

如果用户 Alice 需要将 1 个 WBTC 存入 Compound，那么他将调用 cWBTC 合约的 mint 函数来进行存款。该合约继承了 cToken 合约，会先通过 mintInternal 函数内部调用 accrueInterest 函数来更新借款和存款利率，之后调用 mintFresh 进行具体的铸造操作。

mintFresh 函数会外部调用 Comptroller 合约的 mintAllowed 函数来检查当前市场是否允许存款，然后将用户的 1 个 WBTC 通过 doTransferIn 函数转入合约，再根据当时最新的兑换率为用户铸造相应数量的 cToken 代币（假设当前最新的兑换率是 0.1，那么 Alice 将收到 10 个 cWBTC 代币）。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaNgaoicfHPnnQDjIP1j0UrpzqWaqHS0sGZXVf8Rl9AnNhV2syWEUskl5Qw9cf9ly8hspkGL4051xg/640?wx_fmt=png&from=appmsg)

如果 Alice 未来决定赎回存款，她可以通过调用 redeem 函数将 cWBTC 兑换回 WBTC，兑换率可能已经改变（假设为 0.15），这意味着 Alice 能够赎回 1.5 个 WBTC，其中 0.5 个 WBTC 为利息收入。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaNgaoicfHPnnQDjIP1j0Urp0VVAfxEwbrlc78jymr38ibArWAncRrjV4VmG7TFGFBRNwj4OfCm7TbA/640?wx_fmt=png&from=appmsg)

###

### **3.2 借款和还款流程**

Alice 首先需要调用 Comptroller 合约的 enterMarkets 函数将她的 cWBTC 设置为可作为抵押品的状态，之后才可以进行借款。

```
   function enterMarkets(address[] memory cTokens) override public returns (uint[] memory) {        uint len = cTokens.length;
        uint[] memory results = new uint[](len);        for (uint i = 0; i < len; i++) {            CToken cToken = CToken(cTokens[i]);
            results[i] = uint(addToMarketInternal(cToken, msg.sender));        }
        return results;    }        function addToMarketInternal(CToken cToken, address borrower) internal returns (Error) {        Market storage marketToJoin = markets[address(cToken)];
        ...                marketToJoin.accountMembership[borrower] = true;        accountAssets[borrower].push(cToken);
        ...    }
```

假设 Alice 选择借出 70 个 USDC，由于 WBTC 的抵押因子为 0.75，Alice 最多可以借出相当于 75% 的 WBTC 价值资产，所以这不会超过她的最大借款额度。

注意：为了避免被清算的风险，Alice 应该保留一定的缓冲空间而不是完全用尽她的借款额度。

Alice 调用 cUSDC 合约的 borrow 函数，其会先通过 borrowInternal 函数内部调用 accrueInterest 函数来更新借款和存款利率，之后调用 borrowFresh 进行具体的借款操作。

在通过 Comptroller 合约的 borrowAllowed 函数进行用户的头寸价值检查后，先进行借款数据的记账，之后通过 doTransferOut 函数将代币转出给用户。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaNgaoicfHPnnQDjIP1j0Urp27HuzicR64kxXzZBfcJNKmIIP6aoDZ7wCLlM1s0GL9Qp925cVicohLOQ/640?wx_fmt=png&from=appmsg)

若 Alice 需要还款，可以通过调用 cUSDC 合约的 repayBorrow 函数自行还款，或者让其他人调用 repayBorrowBehalf 函数来代还款。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaNgaoicfHPnnQDjIP1j0UrpjZeTIAlhWzlSmMRbm2g6axQnWpkw9zR9eeJgTyQTZv8Q3xiat2BIS5Q/640?wx_fmt=png&from=appmsg)

###

### **3.3 清算流程**

如果 WBTC 的价格大幅下跌，使得 Alice 的抵押品价值低于其借款额度的 75%，则 Alice 的贷款头寸将处于被清算状态。

外部清算人（例如 Bob）可以调用 cUSDC 合约中的清算函数 liquidateBorrow 来帮助 Alice 清偿部分债务。其会先通过 liquidateBorrowInternal 函数同时更新 cUSDC 与还款用的抵押品 cToken 的利率，之后调用 liquidateBorrowFresh 进行具体的清算操作。

在通过 Comptroller 合约的 liquidateBorrowAllowed 函数进行是否允许清算的检查后，会先调用 repayBorrowFresh 函数将 USDC 转入合约进行还款，并更新被清算人的借款数据。接着调用 Comptroller 合约的 liquidateCalculateSeizeTokens 函数根据清算的价值来计算 Bob 可以拿到 Alice 相应价值的抵押品数量，最后通过指定抵押...