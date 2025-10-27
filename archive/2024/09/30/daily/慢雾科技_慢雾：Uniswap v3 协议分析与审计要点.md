---
title: 慢雾：Uniswap v3 协议分析与审计要点
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500440&idx=1&sn=e447aeff528fb5a5c96a3d88f2d31531&chksm=fddebc1fcaa9350964866990b32e3a928e3a6b76a9c39eabe7e8755c4bb47a03a15e48da678a&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-09-30
fetch_date: 2025-10-06T18:25:33.041269
---

# 慢雾：Uniswap v3 协议分析与审计要点

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZkYPv8Dd1FMZ407ZnLdHf6W3wWBwa4EI8s0aAJibHG6y29RNAliaXKKP0CFJHqaWnqrVewulWaDKhw/0?wx_fmt=jpeg)

# 慢雾：Uniswap v3 协议分析与审计要点

原创

慢雾安全团队

慢雾科技

**前言**

随着去中心化金融(DeFi) 的快速发展，Uniswap 作为领先的去中心化交易所一直走在创新的前沿。本文将深入分析 Uniswap v3 协议的核心机制，并详细解读其功能设计，包括集中流动性、多重费率、代币兑换及闪电贷等关键功能，同时为审计人员提供相关的审计要点。（注：本文中的图片可在 https://www.figma.com/board/QyIpAUR93MxZ4XZZf2QjDk/uniswap-v3 查看高清版，点击阅读原文可直接跳转。）

#### **架构简析**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZkYPv8Dd1FMZ407ZnLdHf6PWuSfNGibwebLc5yqFpHiaKNIKicgVcibM0icIy9kKgyM3NfhePFRFXVNibg/640?wx_fmt=png&from=appmsg)

Uniswap v3 协议主要由四个模块组成：

* **PositionManager：**用户进行流动性操作的主要接口，用户可以通过它创建代币池、提供/移除流动性，并使用 ERC721 作为流动性提供者(LP) 的凭证。
* **SwapRouter：**用户进行代币交换的入口，用户可以通过该模块完成代币的交换操作。
* **Pool：**负责实现代币交易、流动性管理、收取交易手续费，以及 Oracle 数据的管理功能。其中，Tick 机制将价格范围划分为多个精细的刻度。
* **Factory：**用于创建和管理 Pool 合约。

####

#### **流程梳理**

**创建代币对**

用户可以通过 createAndInitializePoolIfNecessary 函数来完成。用户需传入代币对的 token0、token1、手续费(fee) 以及初始价格（）。首先，系统会通过 getPool 函数检查该代币对是否已存在，如果尚未创建，则调用 createPool，并使用 CREATE2 指令进行交易对的部署。最后，通过 initialize 函数完成价格、手续费、tick、预言机等相关参数的初始化。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZkYPv8Dd1FMZ407ZnLdHf6U7kGicib2y7gT149ribiaG0ye9gUVF4HQwzBRicRziaM9KXbgAwrTccEmp2Q/640?wx_fmt=png&from=appmsg)

**提供流动性**

用户可以通过 mint 函数创建新的流动性头寸并生成对应的 NFT，或通过 increaseLiquidity 函数为现有的 NFT 流动性头寸增加流动性。首先，系统会检查交易是否在规定的时间范围内执行，然后调用 addLiquidity 函数完成具体操作。在该函数中，首先计算出池子的地址和流动性的大小，接着调用 \_updatePosition 更新用户的 Position，修改 lower、upper tick 以及累计的手续费总额。随后，系统通过 \_modifyPosition 添加流动性，确保 tick 满足上下限条件，返回计算出的 token0 和 token1 数量(int256)，并将其发送到池中。最后，系统根据用户的 tokenId 更新对应的 Position 信息。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZkYPv8Dd1FMZ407ZnLdHf6gxoKIxWq7vE70VOTGugk0SqCLxrksuWvQx805jPA3zwzZfhDoX60hA/640?wx_fmt=png&from=appmsg)

**移除流动性**

用户可以通过 decreaseLiquidity 函数来移除流动性。首先，系统会检查 LP 凭证的权限以及交易的时间有效性。在确保池子拥有足够流动性的前提下，调用 burn 函数来移除流动性。随后，系统会核实实际移除的代币数量是否满足用户设定的最小限度要求，并相应地更新用户的 Position 信息。

**swap**

用户可以通过 exactInput 函数指定支付的 token 数量以及期望获得的最小 token 数量，或通过 exactOutput 函数指定支付的最大 token 数量并设定期望获得的 token 数量。系统首先解析路径(path)，然后依次调用 exactInputInternal 或 exactOutputInternal 函数完成每一步的 swap 操作。

在 swap 函数中，系统首先锁定 unlocked 状态，防止其他交易干扰状态变量的更新。进入循环后，系统通过 tick 找到下一个交易价格，并调用 computeSwapStep 函数计算每一步的交换，直到 tokenIn 或 tokenOut 达到用户预期。同时，系统会更新手续费、流动性、tick 以及价格的相关值。如果 tick 发生变化，还需要更新 Oracle 数据。完成这些操作后，系统将 tokenOut 支付给用户，用户再通过回调函数 uniswapV3SwapCallback 支付 tokenIn，这种机制可以被视为一种闪电交换(flash swap)。随后，系统会检查合约余额是否匹配，并在确认无误后解锁 unlocked 状态。

当路径中的所有 swap 操作都完成，且交易符合用户的预期时，交易即成功结束。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZkYPv8Dd1FMZ407ZnLdHf6g4M3h20v6ffiakUibicavnibibTf7CcXblU51C2hLnP88yn5LY8E8XwT4uA/640?wx_fmt=png&from=appmsg)

**flash**

用户可以通过 flash 函数来进行闪电贷操作。首先，系统会计算借贷的手续费，然后将用户所需的 token 发送到指定的借贷地址。接下来，系统回调用户实现的 uniswapV3FlashCallback 函数，用户在此函数中完成还款操作。系统会在回调后检查合约余额的变化，确保其与用户借贷的数量相符，同时更新相应的手续费。除了 flash 函数，用户也可以通过 swap 操作实现类似的闪电贷功能，即在交易过程中先借入再偿还 token。

####

#### **审计要点**

**1. 检查 swap 操作后是否有调用 refundETH**

在 exactInput 函数中，用户需要指定支付的 token 数量和预期获得的最小 token 数量。在调用 uniswapV3SwapCallback 之前，系统会重新计算 amount0 和 amount1，以确保用户可以精确地发送 token。然而，当使用 ETH 进行交换时，用户需要随交易一起发送 ETH。即便在交易过程中未使用完所有的 ETH，函数不会自动退回多余部分。exactInput 函数仅返回 amountOut，因此交易者无法直接得知此次交换实际消耗了多少 ETH。

此外，任何人都可以调用 refundETH 函数，从合约中提取未使用的 ETH。因此，建议检查 swap 操作后是否调用 refundETH 以防止用户未使用的 ETH 遗留在协议中，或使用 MultiCall 函数在一次操作中完成多个函数的调用。

```
function refundETH() external payable override {        if (address(this).balance > 0) TransferHelper.safeTransferETH(msg.sender, address(this).balance);    }
```

**2. 检查是否实现 TWAP 来获取预言机价格**

当将 Uniswap 作为价格来源时，外部协议直接访问 Slot0 获取 sqrtPriceX96 可能存在价格操纵的风险。攻击者能通过 swap 等方式操纵流动性池的状态，从而在执行交易时获得有利的价格。

为了降低这种风险，建议开发者进一步实现时间加权平均价格(TWAP) 来获取价格，因为 TWAP 能有效减少短期内价格的剧烈波动影响，使操纵价格的难度增加。

```
function observe(        Observation[65535] storage self,        uint32 time,        uint32[] memory secondsAgos,        int24 tick,        uint16 index,        uint128 liquidity,        uint16 cardinality    ) internal view returns (int56[] memory tickCumulatives, uint160[] memory secondsPerLiquidityCumulativeX128s) {        require(cardinality > 0, 'I');
        tickCumulatives = new int56[](secondsAgos.length);        secondsPerLiquidityCumulativeX128s = new uint160[](secondsAgos.length);        for (uint256 i = 0; i < secondsAgos.length; i++) {            (tickCumulatives[i], secondsPerLiquidityCumulativeX128s[i]) = observeSingle(                self,                time,                secondsAgos[i],                tick,                index,                liquidity,                cardinality            );        }    }
```

**3. 建议允许用户自行设置滑点参数**

当其他协议使用 Uniswap v3 进行 swap 操作时，建议开发者根据业务场景设置滑点保护，并允许用户自行调整参数，以防止遭受三明治攻击。在此 swap 函数中，第四个参数 sqrtPriceLimitX96 用于指定用户愿意执行交换的最低或最高价格。这一参数可有效防止在交易过程中价格出现极端波动，从而降低用户因滑点过大而产生的损失。

```
function swap(        address recipient,        bool zeroForOne,        int256 amountSpecified,        uint160 sqrtPriceLimitX96,        bytes calldata data    ) external override noDelegateCall returns (int256 amount0, int256 amount1) {    ...}
```

**4. 建议引入流动性池白名单机制**

在 Uniswap v3 中，基于不同的手续费(fee)，同一对 ERC20 代币可能同时存在多个流动性池(Pool)。通常，少数流动性池拥有绝大部分的流动性，而其他池的总锁仓量(TVL) 可能非常少，甚至尚未创建。这些 TVL 较低的池更容易成为价格操纵的目标。

因此，项目方在选择使用流动性池数据时，应该避免简单地以 LP 为数据源。为确保数据的可靠性，建议引入白名单机制，筛选出流动性充足且较难操纵的池。这种机制可以显著降低风险，确保价格引用数据的安全性和准确性，同时防止因 TVL 过低的池被操纵而引发的潜在损失。

```
function createPool(        address tokenA,        address tokenB,        uint24 fee) external override noDelegateCall returns (address pool) {        require(tokenA != tokenB);        (address token0, address token1) = tokenA < tokenB ? (tokenA, tokenB) : (tokenB, tokenA);        require(token0 != address(0));        int24 tickSpacing = feeAmountTickSpacing[fee];        require(tickSpacing != 0);        require(getPool[token0][token1][fee] == address(0));        pool = deploy(address(this), token0, token1, fee, tickSpacing);        getPool[token0][token1][fee] = pool;        // populate mapping in the reverse direction, deliberate choice to avoid the cost of comparing addresses        getPool[token1][token0][fee] = pool;        emit PoolCreated(token0, token1, fee, tickSpacing, pool);    }
```

**5. 检查是否在 TickMath.sol、FullMath.sol 和 Position.sol 中使用 unchecked**

TickMath、FullMath 和 Position 等模块在 Uniswap v3 中用于执行复杂的数学计算，这些计算依赖于 Solidity 中的溢出处理机制。在早期的 Solidity 版本（<0.8.0）中，整数溢出和下溢行为默认不抛出异常，因此代码可以基于这种假设进行正常运行。然而，自 Solidity 0.8.0 版本开始，溢出和下溢会自动抛出异常，这会影响现有代码的执行。为确保这些模块在 Solidity 0.8.0 及更高版本中正常运行，开发者需要在特定函数中使用 unchecked 代码块，手动禁用溢出检查。这可以恢复之前版本中的行为，并确保高效执行溢出敏感的运算。

官方已经针对 Solidity 0.8.0 及更高版本做了相应的支持和调整，详情可参见此更新(https://github.com/Uniswap/v3-core/commit/6562c52e8f75f0c10f9deaf44861847585fc8129)。这一改动确保在新版编译器下，TickMath、FullMath 和其他相关模块能够继续正确运行。

**6. 检查 path 编码解码方式是否相同**

在 Uniswap v3 的 exactInput 和 exactOutput 函数中，用户需要输入 path 参数，该路径必须按照固定格式进行编码和解码，即 tokenA-fee-tokenB，用于逐步进行代币交换操作。这个路径结构明确指定了每一跳交易中涉及的两个代币以及它们之间的手续费级别。如果外部协议在使用 Uniswap v3 的代币交换功能时选择了不同的路径解码方式，可能会导致与 Uniswap 预期的路径格式不符。这种情况下，协议可能无法正确解析路径，从而无法成功执行预期的代币交换操作。

因此，建议开发者在集成 Uniswap v3 的代币交换功能时，确保外部协议严格遵循 Uniswap 的路径编码规则。为防止出现路径解码错误，外部协议应在调用 exactInput 和 exactOutput 时，仔细检查 path 参数的格式，以避免交易失败或获得意外的结果。

```
function decodeFirstPool(bytes memory path)        internal        pure        returns (            address tokenA,            address tokenB,            uint24 fee        )    {        tokenA = path.toAddress(0);        fee = path.toUint24(ADDR_SIZE);        tokenB = path.toAddress(NEXT_OFFSET);    }
```

**7. 检查代币顺序是否影响项目逻辑**

在 Uniswap 中，token0 是排序顺序较低的代币，用作基础代币(base token)，而 token1 是排序顺序较高的代币，用作报价代币(quote token)。Uniswap 会根据两个代币的地址按字典序进行排序，确保代币对的顺序在池子中始终保持一致。

然而，由于同一代币在不同区块链网络上的合约地址可能不同，尤其是跨链部署的合约，代币的排序顺序可能会发生变化。这种变化会导致 token0 和 token1 的角色互换，从而影响价格表现。例如，在某些链上，特定代币可能是 token0，但在其他链上，它可能被排序为 token1，导致基础代币和报价代币的关系不同，最终影响显示的价格。因此，建议开发者检查代币顺序是否会影响项目逻辑，特别是在跨链环境中，务必考虑代币顺序可能导致的价格问题，以避免对价格表现和交易逻辑产生不利影响。

```
(address token0, address token1) = tokenA < tokenB ? (tokenA, tokenB) : (tokenB, tokenA);
```

####

#### **总结**

上述基础检查项基于 Uniswap v3 当前版本，供审计人员对与 Uniswap v3 有交互的项目进行检查。不同项目的实现各具特点，...