---
title: 慢雾：Uniswap v3 协议分析与审计要点
url: https://www.freebuf.com/articles/blockchain-articles/412689.html
source: FreeBuf网络安全行业门户
date: 2024-10-13
fetch_date: 2025-10-06T18:50:26.938460
---

# 慢雾：Uniswap v3 协议分析与审计要点

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

慢雾：Uniswap v3 协议分析与审计要点

* ![]()
* 关注

* [其他](https://www.freebuf.com/articles/others-articles)

慢雾：Uniswap v3 协议分析与审计要点

2024-10-12 11:40:28

所属地 海外

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# **前言**

随着去中心化金融(DeFi) 的快速发展，Uniswap 作为领先的去中心化交易所一直走在创新的前沿。本文将深入分析 Uniswap v3 协议的核心机制，并详细解读其功能设计，包括集中流动性、多重费率、代币兑换及闪电贷等关键功能，同时为审计人员提供相关的审计要点。（注：本文中的图片可在 https://www.figma.com/board/QyIpAUR93MxZ4XZZf2QjDk/uniswap-v3 查看高清版。）

# **架构简析**

![1728703951751741.jpg](https://image.3001.net/images/20241012/1728704430_6709efae4b0da312aa938.jpg!small)

Uniswap v3 协议主要由四个模块组成：

* **PositionManager：**用户进行流动性操作的主要接口，用户可以通过它创建代币池、提供/移除流动性，并使用 ERC721 作为流动性提供者(LP) 的凭证。
* **SwapRouter：**用户进行代币交换的入口，用户可以通过该模块完成代币的交换操作。
* **Pool：**负责实现代币交易、流动性管理、收取交易手续费，以及 Oracle 数据的管理功能。其中，Tick 机制将价格范围划分为多个精细的刻度。
* **Factory：**用于创建和管理 Pool 合约。

# **流程梳理**

**创建代币对**

用户可以通过 createAndInitializePoolIfNecessary 函数来完成。用户需传入代币对的 token0、token1、手续费(fee) 以及初始价格（）。首先，系统会通过 getPool 函数检查该代币对是否已存在，如果尚未创建，则调用 createPool，并使用 CREATE2 指令进行交易对的部署。最后，通过 initialize 函数完成价格、手续费、tick、预言机等相关参数的初始化。

![1728703951892843.jpg](https://image.3001.net/images/20241012/1728704432_6709efb08e6a2066900e5.jpg!small)

**提供流动性**

用户可以通过 mint 函数创建新的流动性头寸并生成对应的 NFT，或通过 increaseLiquidity 函数为现有的 NFT 流动性头寸增加流动性。首先，系统会检查交易是否在规定的时间范围内执行，然后调用 addLiquidity 函数完成具体操作。在该函数中，首先计算出池子的地址和流动性的大小，接着调用 \_updatePosition 更新用户的 Position，修改 lower、upper tick 以及累计的手续费总额。随后，系统通过 \_modifyPosition 添加流动性，确保 tick 满足上下限条件，返回计算出的 token0 和 token1 数量(int256)，并将其发送到池中。最后，系统根据用户的 tokenId 更新对应的 Position 信息。

![1728703951999474.jpg](https://image.3001.net/images/20241012/1728704435_6709efb3679fc67fda65a.jpg!small)

**移除流动性**

用户可以通过 decreaseLiquidity 函数来移除流动性。首先，系统会检查 LP 凭证的权限以及交易的时间有效性。在确保池子拥有足够流动性的前提下，调用 burn 函数来移除流动性。随后，系统会核实实际移除的代币数量是否满足用户设定的最小限度要求，并相应地更新用户的 Position 信息。

**swap**

用户可以通过 exactInput 函数指定支付的 token 数量以及期望获得的最小 token 数量，或通过 exactOutput 函数指定支付的最大 token 数量并设定期望获得的 token 数量。系统首先解析路径(path)，然后依次调用 exactInputInternal 或 exactOutputInternal 函数完成每一步的 swap 操作。

在 swap 函数中，系统首先锁定 unlocked 状态，防止其他交易干扰状态变量的更新。进入循环后，系统通过 tick 找到下一个交易价格，并调用 computeSwapStep 函数计算每一步的交换，直到 tokenIn 或 tokenOut 达到用户预期。同时，系统会更新手续费、流动性、tick 以及价格的相关值。如果 tick 发生变化，还需要更新 Oracle 数据。完成这些操作后，系统将 tokenOut 支付给用户，用户再通过回调函数 uniswapV3SwapCallback 支付 tokenIn，这种机制可以被视为一种闪电交换(flash swap)。随后，系统会检查合约余额是否匹配，并在确认无误后解锁 unlocked 状态。

当路径中的所有 swap 操作都完成，且交易符合用户的预期时，交易即成功结束。

![1728703952140123.jpg](https://image.3001.net/images/20241012/1728704439_6709efb7239a62402e7be.jpg!small)

**flash**

用户可以通过 flash 函数来进行闪电贷操作。首先，系统会计算借贷的手续费，然后将用户所需的 token 发送到指定的借贷地址。接下来，系统回调用户实现的 uniswapV3FlashCallback 函数，用户在此函数中完成还款操作。系统会在回调后检查合约余额的变化，确保其与用户借贷的数量相符，同时更新相应的手续费。除了 flash 函数，用户也可以通过 swap 操作实现类似的闪电贷功能，即在交易过程中先借入再偿还 token。

# **审计要点**

**1. 检查 swap 操作后是否有调用 refundETH**

在 exactInput 函数中，用户需要指定支付的 token 数量和预期获得的最小 token 数量。在调用 uniswapV3SwapCallback 之前，系统会重新计算 amount0 和 amount1，以确保用户可以精确地发送 token。然而，当使用 ETH 进行交换时，用户需要随交易一起发送 ETH。即便在交易过程中未使用完所有的 ETH，函数不会自动退回多余部分。exactInput 函数仅返回 amountOut，因此交易者无法直接得知此次交换实际消耗了多少 ETH。

此外，任何人都可以调用 refundETH 函数，从合约中提取未使用的 ETH。因此，建议检查 swap 操作后是否调用 refundETH 以防止用户未使用的 ETH 遗留在协议中，或使用 MultiCall 函数在一次操作中完成多个函数的调用。

![1728704080976023.jpg](https://image.3001.net/images/20241012/1728704440_6709efb8ce6ca30400bc6.jpg!small)

**2. 检查是否实现 TWAP 来获取预言机价格**

当将 Uniswap 作为价格来源时，外部协议直接访问 Slot0 获取 sqrtPriceX96 可能存在价格操纵的风险。攻击者能通过 swap 等方式操纵流动性池的状态，从而在执行交易时获得有利的价格。

为了降低这种风险，建议开发者进一步实现时间加权平均价格(TWAP) 来获取价格，因为 TWAP 能有效减少短期内价格的剧烈波动影响，使操纵价格的难度增加。

![1728704114092056.jpg](https://image.3001.net/images/20241012/1728704442_6709efba831bc926129d6.jpg!small)

**3. 建议允许用户自行设置滑点参数**

当其他协议使用 Uniswap v3 进行 swap 操作时，建议开发者根据业务场景设置滑点保护，并允许用户自行调整参数，以防止遭受三明治攻击。在此 swap 函数中，第四个参数 sqrtPriceLimitX96 用于指定用户愿意执行交换的最低或最高价格。这一参数可有效防止在交易过程中价格出现极端波动，从而降低用户因滑点过大而产生的损失。

![1728704140827348.jpg](https://image.3001.net/images/20241012/1728704443_6709efbbe581952e00c23.jpg!small)

**4. 建议引入流动性池白名单机制**

在 Uniswap v3 中，基于不同的手续费(fee)，同一对 ERC20 代币可能同时存在多个流动性池(Pool)。通常，少数流动性池拥有绝大部分的流动性，而其他池的总锁仓量(TVL) 可能非常少，甚至尚未创建。这些 TVL 较低的池更容易成为价格操纵的目标。

因此，项目方在选择使用流动性池数据时，应该避免简单地以 LP 为数据源。为确保数据的可靠性，建议引入白名单机制，筛选出流动性充足且较难操纵的池。这种机制可以显著降低风险，确保价格引用数据的安全性和准确性，同时防止因 TVL 过低的池被操纵而引发的潜在损失。

![1728704179675382.jpg](https://image.3001.net/images/20241012/1728704445_6709efbda7d4f0419259c.jpg!small)

**5. 检查是否在 TickMath.sol、FullMath.sol 和 Position.sol 中使用 unchecked**

TickMath、FullMath 和 Position 等模块在 Uniswap v3 中用于执行复杂的数学计算，这些计算依赖于 Solidity 中的溢出处理机制。在早期的 Solidity 版本（<0.8.0）中，整数溢出和下溢行为默认不抛出异常，因此代码可以基于这种假设进行正常运行。然而，自 Solidity 0.8.0 版本开始，溢出和下溢会自动抛出异常，这会影响现有代码的执行。为确保这些模块在 Solidity 0.8.0 及更高版本中正常运行，开发者需要在特定函数中使用 unchecked 代码块，手动禁用溢出检查。这可以恢复之前版本中的行为，并确保高效执行溢出敏感的运算。

官方已经针对 Solidity 0.8.0 及更高版本做了相应的支持和调整，详情可参见此更新(https://github.com/Uniswap/v3-core/commit/6562c52e8f75f0c10f9deaf44861847585fc8129)。这一改动确保在新版编译器下，TickMath、FullMath 和其他相关模块能够继续正确运行。

**6. 检查 path 编码解码方式是否相同**

在 Uniswap v3 的 exactInput 和 exactOutput 函数中，用户需要输入 path 参数，该路径必须按照固定格式进行编码和解码，即 tokenA-fee-tokenB，用于逐步进行代币交换操作。这个路径结构明确指定了每一跳交易中涉及的两个代币以及它们之间的手续费级别。如果外部协议在使用 Uniswap v3 的代币交换功能时选择了不同的路径解码方式，可能会导致与 Uniswap 预期的路径格式不符。这种情况下，协议可能无法正确解析路径，从而无法成功执行预期的代币交换操作。

因此，建议开发者在集成 Uniswap v3 的代币交换功能时，确保外部协议严格遵循 Uniswap 的路径编码规则。为防止出现路径解码错误，外部协议应在调用 exactInput 和 exactOutput 时，仔细检查 path 参数的格式，以避免交易失败或获得意外的结果。

![1728704219175495.jpg](https://image.3001.net/images/20241012/1728704447_6709efbf08ade2f334e0c.jpg!small)

**7. 检查代币顺序是否影响项目逻辑**

在 Uniswap 中，token0 是排序顺序较低的代币，用作基础代币(base token)，而 token1 是排序顺序较高的代币，用作报价代币(quote token)。Uniswap 会根据两个代币的地址按字典序进行排序，确保代币对的顺序在池子中始终保持一致。

然而，由于同一代币在不同区块链网络上的合约地址可能不同，尤其是跨链部署的合约，代币的排序顺序可能会发生变化。这种变化会导致 token0 和 token1 的角色互换，从而影响价格表现。例如，在某些链上，特定代币可能是 token0，但在其他链上，它可能被排序为 token1，导致基础代币和报价代币的关系不同，最终影响显示的价格。因此，建议开发者检查代币顺序是否会影响项目逻辑，特别是在跨链环境中，务必考虑代币顺序可能导致的价格问题，以避免对价格表现和交易逻辑产生不利影响。

![1728704249311360.jpg](https://image.3001.net/images/20241012/1728704448_6709efc0589336b6170b5.jpg!small)

**总结**

上述基础检查项基于 Uniswap v3 当前版本，供审计人员对与 Uniswap v3 有交互的项目进行检查。不同项目的实现各具特点，因此审计人员需深入理解协议，并根据实际情况进行严格检查。对于正在开发的项目，慢雾安全团队建议开发者在开发过程中认真考虑这些检查项，以确保协议的安全性和可靠性。

作者 | Sissice

编辑 | Liz

# 安全审计

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/202507...