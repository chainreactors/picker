---
title: 慢雾：AAVE V2 安全审计手册
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501098&idx=1&sn=341bf68002be703b2f92d3c822dcf587&chksm=fddebbadcaa932bb7030f2cc169f728ac52c986cad2b24cb859ecd3ac23529a4bf7d3a450164&scene=58&subscene=0#rd
source: 慢雾科技
date: 2025-02-14
fetch_date: 2025-10-06T20:36:48.160119
---

# 慢雾：AAVE V2 安全审计手册

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLaia8TphRAUHuSZWKhLr0e2bLLliaicDMz1MibeUxSgyrzQibpicSNlH5SkNibRcrJTNmFqecbTWunFqcESQ/0?wx_fmt=jpeg)

# 慢雾：AAVE V2 安全审计手册

原创

慢雾安全团队

慢雾科技

**引言**

随着去中心化金融(DeFi) 生态系统的迅速发展，AAVE V2 作为领先的去中心化借贷协议之一，在提供创新借贷与流动性管理解决方案方面始终处于行业前沿。其独特的无信任机制和高效的资本利用率吸引了大量用户和机构的参与。然而，随着其应用的普及及所涉及的资金规模逐步扩大，安全审计和风控措施的重要性日益凸显。本手册将深入探讨 AAVE V2 协议的核心设计、关键功能及相关审计要点。

## **项目背景概述**

AAVE V2 是一个基于以太坊区块链构建的开放式借贷平台，允许用户存入各种 ERC-20 代币并从中赚取利息，同时也允许以支付利息的形式借用市场中的代币。通过引入“利率市场”的概念，AAVE V2 实现了去中心化的资金池管理和自动化的利率调整机制。此外，AAVE V2 还提供了闪电贷、抵押贷款和代币交换等高级功能，以满足用户的多样化需求，进一步巩固了其在 DeFi 领域的领先地位。

##

## **项目架构分析**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaia8TphRAUHuSZWKhLr0e2bmXfRTpVcQbzUYUhCAnQBGttl4MzvLWmMibOlOCDnX5xQMXnO1r3uAcQ/640?wx_fmt=png&from=appmsg)

AAVE V2 的整体架构设计围绕用户、资金流动管理、抵押机制、清算流程以及利率策略等关键功能展开，旨在提供高效且安全的去中心化借贷服务。以下是综合分析：

### **用户操作流程**

* **用户：**用户可以进行存款、借款、偿还、提取、借贷利率模式交换、闪电贷以及委托信用等多种操作。用户与协议交互时，会根据其操作自动铸造或销毁相应的 aTokens，代表其在协议中的存款权益，并根据利率策略获得收益。
* **委托信用：**用户可以将自己的信用额度委托给其他用户，扩展了协议的灵活性和使用场景。

###

### **核心组件**

* **LendingPool：**作为核心模块负责处理所有用户的操作请求，包括存款、借款、偿还、借贷利率模式交换、闪电贷和清算，并更新利率和状态。
* **Collateral Manager：**管理抵押资产，确保用户借款行为安全可控。当抵押资产不足时，会触发清算流程来保护系统的整体流动性。
* **Libraries：**封装储蓄金逻辑，验证逻辑，通用功能逻辑，如清算和借贷操作的计算，为 LendingPool 提供支持。

+ GenericLogic 计算并验证用户状态，包括资产评估、抵押品价值计算、健康系数等操作。
+ ReserveLogic 用于管理储备金池，追踪和更新每种资产的存款量、借款量以及当前利率情况。
+ ValidationLogic 负责验证用户的操作是否符合协议规则，在用户进行存款、借款、还款、清算、闪电贷、切换债务模式等操作时，对抵押品和负债进行严格检查。

###

### **债务与代币化**

* **Debt Tokens：**用来跟踪用户的借款负债，与贷出资金数额 1:1。债务代币分别有固定利率和可变利率选项（如 DebtDAI Stable、DebtDAI Variable 等），且债务代币不可转移。
* **aTokens：**用户存入资产时会生成 1:1 的 aTokens 锚定底层资产，这些 aTokens 会不断增值以反映存款所赚取的利息。其中由此引入与本金余额一起存储为一个比率，称为缩放余额 scaled balance (ScB)。

  公式如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaia8TphRAUHuSZWKhLr0e2bIsicR93o6u7xKv5InBIqahvH5Ray3jfsr011tWOa1B9E3jsiaRs5AAvw/640?wx_fmt=png&from=appmsg)

###

### **价格和利率**

* **Oracles Proxy：**依赖外部预言机 (Chainlink) 提供资产市场价格数据，用于评估用户抵押资产的价值，确保借贷行为的定价准确性和系统的稳定性。
* **Lending Rate Oracle：**根据系统的状态和市场情况，提供动态的借贷利率，优化资本利用率和流动性。

###

### **配置与管理**

* **Configurator：**用于配置系统参数，如不同资产的风险参数和借贷限额，管理储备金的各种操作，包括激活、借款、抵押、冻结、更新参数及在紧急情况下启用或禁用功能。确保协议可以根据市场变化进行动态调整。

###

### **其他关键功能**

* **Liquidation Manager：**当用户抵押品价值下降至清算门槛以下时，管理清算操作，保护系统的资金安全。清算人可以通过清算操作获得奖励。
* **Reserves Balances：**存储系统的储备资金数据，用于计算和调整利率策略。

###

### **利率策略**

* **Interest Rate Strategy：**根据市场和用户需求，动态调整利率以实现最佳资本配置，同时考虑流动性风险，确保系统在不同市场条件下的灵活性和稳定性。

  尽管存在两种利率模型（稳定型和浮动型），但是其模型计算都类似于一个拐点型模型。在拐点最优利用率下的 slope1 和超过最优利用率的 slope2 分段计算，且在这个条件下也分为固定利率模型和可变利率模型。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaia8TphRAUHuSZWKhLr0e2beibzm73uIpx88HBw0zn91WLEnsnicOKoWx2QaszZnrHS6ULOP92jNzrw/640?wx_fmt=png&from=appmsg)

公式如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaia8TphRAUHuSZWKhLr0e2bxdmcB2tuNibiaZrdfvtd8LgopxWmAU17qqibqQlg0C2GOhoDJoNggo8Ug/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaia8TphRAUHuSZWKhLr0e2bHNHToRv2QEfY5gQMgGP7SoNf4lWvOET5NIEguggNuLwxLWiaUNqhp9w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaia8TphRAUHuSZWKhLr0e2bvFpmkukrOicicASMkEiaZZdlvfMAQ9D0fgv42ic34unfrkiaibx9VCgKMOQA/640?wx_fmt=png&from=appmsg)

## **流程梳理**

###

### **存款**

用户通过调用 LendingPool 合约的 deposit 函数进行存款，该函数接受四个参数：资产地址、存款金额、接收方地址及推荐码。首先验证合约未处于启用状态，然后通过 ValidationLogic.validateDeposit 验证存款金额必须大于 0，同时确认储备处于激活状态且未被冻结。接着系统会更新储备状态，调用 reserve.updateState() 更新流动性累积指数和可变借款指数，并计算时间段内产生的利息，其中一部分利息会被铸造并转入协议国库。

公式如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaia8TphRAUHuSZWKhLr0e2bvf47HDic8k6Tic56eVV75fCYf7l61SQs7qUAo3HRVTMJVPDYGcr4Xzww/640?wx_fmt=png&from=appmsg)

随后通过 reserve.updateInterestRates 根据最新的供需关系动态调整流动性利率、稳定借款利率和可变借款利率（都由 DefaultReserveInterestRateStrategy.calculateInterestRates 函数计算更新)。资产转移环节，系统将用户的基础资产转入 aToken 合约，同时铸造等额 aToken 给用户所提交的 onBehalfOf 地址。其中，aToken 采用缩放机制 (scaled balance) 处理利息累积。如果是用户首次存款，系统会自动将该资产标记为用户的抵押品。

与 Compound 相比，AAVE V2 的存款过程有以下主要特点：

* 支持指定接收方地址(onBehalfOf)。
* 通过 ValidationLogic 合约进行存款验证。
* 更新流动性累积指数和可变借款指数计算并分配协议国库利息。
* 同时调整流动性、稳定借款和可变借款三种利率。
* 使用 aToken 的缩放机制(scaled balance) 处理利息。
* 首次存款自动标记为抵押品。

###

### **提现**

用户通过调用 withdraw 函数进行提现操作。首先取指定资产的储备数据，包括对应的 aToken 地址，检查此用户在 aToken 中的余额。接下来，调用 ValidationLogic.validateWithdraw 函数来验证提现请求，包括检查提现金额是否有效、用户余额是否足够、储备是否处于活动状态等。其中通过 GenericLogic.balanceDecreaseAllowed 对用户的健康系数以及提现是否影响抵押品进行检查，类似于 compound 中 getHypotheticalAccountLiquidityInternal 函数的作用。在 balanceDecreaseAllowed 函数中，calculateUserAccountData 和 calculateHealthFactorFromBalances 函数计算取出资金后的清算阀值并检查用户总抵押，总借贷数额以及用户当前的健康系数，以此来判断是否用户健康系数处于流动性阀值的安全状态。

HF 计算公式如下：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaia8TphRAUHuSZWKhLr0e2bFV3wEtJEiaWADbvUc1msUJo4e7mKv9XLnGmxh2oNB2bDaG4l72coFNQ/640?wx_fmt=png&from=appmsg)

随后更新储备的状态，并更新利率，将提现金额传递给函数。若用户请求的提现金额等于其当前余额，则更新用户配置，将该储备标记为不再作为抵押使用。最后销毁用户的 aToken，并将提现的资产转账到指定的地址。

与 Compound 相比，AAVE V2 的提现过程有以下主要特点：

* 使用 aToken 代表用户在协议中的存款，提现实际上是销毁 aToken。
* 允许用户提现到指定地址（通过 to 参数），增加了灵活性。
* 提供了部分提现和全额提现的选项。
* 在提现验证中，AAVE 使用了更复杂的 balanceDecreaseAllowed 函数来检查提现对用户整体抵押品状况的影响。
* AAVE 的提现过程直接更新了利率，而不是像 Compound 那样通过 accrueInterest 函数来更新。

###

### **借贷**

用户通过 borrow 函数进行借贷，执行借款会先从价格预言机获取资产的当前价格，将借款金额转换为 ETH 等价。随后通过 ValidationLogic.validateBorrow 检查以及 GenericLogic.calculateUserAccountData 用户借款是否合法，计算包括 onBehalfOf 地址的总抵押资产、总债务、当前贷款价值比率(LTV)、清算阈值和健康因子以及市场的稳定性等（类似于 Compound 的 getHypotheticalAccountLiquidityInternal），是否有足够的抵押资产借贷。reserve.updateState 更新储备状态，如利率和借款指数（这一步类似于 Compound 中的 accrueInterest），用于计算并更新利息。

随后根据用户选择进行的 interestRateMode（稳定利率或浮动利率）生成债务，选择不同的利率模型的代币合约来铸造代币。同时，铸造代币时也会进行检查，如果 onBehalfOf 地址不是调用者，则会在代币合约中减去其对调用用户的借贷授权。如果是用户的首次借款，会将其配置为活跃借款者。DebtToken 铸造给用户后，协议会通过 updateInterestRates 更新借款利率，反映借款后的新利率和储备池的变化。如果用户请求释放借款的底层资产，协议会将资产直接转移给用户。

与 Compound 相比，AAVE V2 的借贷过程有以下主要特点：

* 支持稳定和可变两种利率模式。
* 使用单独的验证逻辑合约进行借贷验证。
* 使用债务代币(DebtToken) 来表示用户的借款。
* 支持信用委托，允许用户代表其他地址进行借款。

### **还款**

用户通过 repay 函数进行还款，首先获取用户的当前债务（包括稳定债务 stableDebt 和浮动债务 variableDebt）。根据用户选择的利率模式（稳定或浮动），由 ValidationLogic.validateRepay 验证用户的还款操作合法性，包括用户的债务余额是否足够进行还款。根据用户选择的利率模式来确定还款的具体债务类型（稳定利率或浮动利率）。如果用户要还的金额小于当前债务余额，系统会使用用户提供的还款金额进行部分还款；否则，将偿还所有债务。更新储备的状态 updateState，用于计算并更新协议中的利息、借贷量以及借贷指数。随后燃烧相应的稳定债务代币，并通过 updateInterestRates 更新借款利率。此时，如果用户的所有债务（包括稳定和浮动债务）在还款后为零，则会将该用户的借款状态标记为 false，表示用户不再借款。最后用户将还款金额从其账户转移到协议的 aToken 合约地址。

与 Compound 相比，AAVE V2 的还款过程有以下主要特点：

* 支持稳定和浮动两种利率模式的还款。
* 使用 DebtToken 来表示和管理债务，还款时燃烧对应债务代币。
* 支持部分还款和全额还款，并分别处理稳定债务和浮动债务。
* 支持用户通过信用委托为其他地址还款。

###

### **清算**

用户通过 lendingpool 的 liquidationCall 函数进行清算，函数通过代理模式调用 LendingPoolCollateralManager 的 liquidationCall 函数，确保函数的成功执行。首先 GenericLogic.calculateUserAccountData 获取抵押品资产及债务资产的储备数据和用户的配置信息，计算用户的健康因子，并通过 getUserCurrentDebt 获取用户的当前稳定和可变负债。

ValidationLogic.validateLiquidationCall 函数验证清算调用的合法性，包括检查用户的健康因子、债务状态和抵押品配置。若健康因子小于阀值，已作为抵押品，且两种债务都不为 0 则验证通过。接着计算用户的最大可清算债务，并确定实际需要清算的债务数量。如果清算的债务超过用户的可用抵押物，将调整清算金额。

如果清算人选择接收被清算人抵押的底层资产，需要确保抵押物储备中有足够的流动性。更新债务储备的状态，并根据清算人是否接收 aToken 情况，燃烧相应数量的可变和稳定债务代币。更新债务的利率，反映清算后的市场情况。清算人奖励如果选择接收 aToken，清算人将获得相应数量的 aToken。如果不接受 aToken，则更新其抵押状态和抵押物的利率，从用户账户中燃烧掉对应数量的 aToken ，将底层资产转移给清算人。最后，将清算所需的债务资产从清算人转移到相应的储备 aToken 中，完成清算过程。

与 Compound 相比，AAVE V2 的清算过程有以下主要特点：

* 支持多种抵押品和债务资产的组合清算。
* 允许清算人选择接收 aToken 或 底层资产。
* 清算过程更加模块化，将验证逻辑、计算逻辑等分离到不同的函数中。
* 支持稳定利率和可变利率两种债务类型的清算。

###

### **闪电贷**

用户通过 lendingpool 的 flashLoan 函数进行闪电贷。作为借贷协议的闪电贷，可以允许当前闪电贷立刻还款或是作为债务来后续还款，其中以传入的 modes 参数不同而决定。0 为立刻还款，1 为作为稳定型债务，2 为浮动型债务。

函数首先通过 ValidationLogic.validateFlashloan 检查输入参数匹配，计算闪电贷所需的溢价成本，并直接将所需的 aToken 转给接收者地址。调用接受者的 executeOperation 操作实现预设的闪电贷。AAVE 实现的闪电贷操作已包括了兑换，兑换清算，以及兑换偿还操作。在 executeOperation 完成以上操作后，记录需偿还的闪电贷金额和相应的费用。如果用户选择以非债务模式归还资金：系统更新储备状态，累积储备流动性以及更新流动性指数。最后再从请求者转移资金和费用至储备池。若用户选择以债务模式处理，则调用 \_executeBorrow，开启相应的债务头寸。

### **转换债务模式**

在 AAVE V2 中，用户可以通过 swapBorrowRateMode 函数在稳定利率模式和浮动利率模式之间切换。首先通过 getUserCurrentDebt 函数获取用户在目标资产上的当前稳定利率债务和浮动利率债务，确定用户的债务状况。接着调用 ValidationLogic.validateSwapRateMode 函数验证切换操作是否合法。其中检查用户是否有足够的稳定或浮动债务以支持模式切换，确保切换目标模式符合资产的配置和用户的债务情况。调用 reserve.updateState 更新资产储备的状态，确保储备数据最新。随后就是对于两种债务代币的相互转换，燃烧稳定债务代币铸造浮动债务代币或是燃烧浮动债务代币铸造稳定债务代币。转换完成后，...