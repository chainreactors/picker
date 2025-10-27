---
title: 慢雾解析｜Safe 困局，Guard 能否重构契约巴别塔？
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501278&idx=1&sn=78004ffc4dc09460a509369556a45ff9&chksm=fddebb59caa9324fa417d562c455f14e50ee4f4557ec5db03b330ef4f050155884eb22d1e5dc&scene=58&subscene=0#rd
source: 慢雾科技
date: 2025-02-27
fetch_date: 2025-10-06T20:36:28.167875
---

# 慢雾解析｜Safe 困局，Guard 能否重构契约巴别塔？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLbFIv2cLgxKgjAibLMOBjkrxwG88XOB65GbTqERj4u6h5XcRoZGBK1mnToMJtxARXEjRiasrbJSGA4g/0?wx_fmt=jpeg)

# 慢雾解析｜Safe 困局，Guard 能否重构契约巴别塔？

原创

慢雾安全团队

慢雾科技

作者：flush & kong

编辑：Liz

**背景**

2025 年 2 月 21 日，加密货币行业遭遇史上最严重的资产管理危机。交易平台 Bybit 的链上多签钱包遭定向攻破，近 15 亿美元资产通过一笔“合法签名”的交易悄然流失。事后链上分析显示，攻击者通过精密的社会工程攻击获取了多签权限，利用 Safe 合约的 delegatecall 功能植入恶意逻辑，最终绕过多重签名验证机制，将资金转移至匿名地址。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbFIv2cLgxKgjAibLMOBjkrxzbZvc3o2fpmjuND2AYcGTaIKfiaHcHZaxnV3DR2RtCDEJNq5icJV3YaA/640?wx_fmt=png&from=appmsg)

此次事件暴露出一个残酷现实：“多重签名”不等于“绝对安全”，即便是 Safe 多签钱包这样的安全机制，如果缺乏额外的防护措施，仍然存在被攻破的风险。这也并非首个针对 Safe 多签钱包的攻击案例。去年 WazirX（损失 2.3 亿美元）和 Radiant Capital（损失 5,000 万美元）都遭遇了类似的攻击手法。正如[慢雾：Bybit 近 15 亿美元被盗背后的黑客手法与疑问](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501246&idx=1&sn=eafc7080cc28d1f8bf16c362f3ac2230&scene=21#wechat_redirect)一文中的分析， Safe 多签钱包攻击事件呈现出以下技术同源性：

* 过度依赖签名机制：将安全责任都交给私钥保管。
* 动态防御缺失：缺乏交易执行前的实时风险扫描。
* 权限控制粗粒度：未对 delegatecall 等高风险操作建立白名单机制。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbFIv2cLgxKgjAibLMOBjkrxcvbPmMGZ9gibNuIia2krOCr5QPRJ1Vgmt9CVwnNHRooTaLJh7Aiak3YpQ/640?wx_fmt=png&from=appmsg)

(Bybit 被盗流程：使用 Safe v1.1.1)

这一系列事件的核心问题不在于 Safe 合约本身，而是在于整个系统的集成过程中的安全隐患，特别是在前端验证环节。这促使我们需要思考：如何通过 Safe 的额外安全措施机制来强化多签钱包的防护能力？

# **Safe**

Safe 是一款多重签名(Multi-Sig) 钱包，主要用于管理高价值资产和数字货币的安全存储与转移。作为去中心化资产管理的基础设施，它通过多方协同验证机制确保资金操作的安全性，防止单一管理员或黑客利用单点故障进行恶意操作，广泛应用于 DAO 治理、企业资金托管、去中心化基金池等场景。该合约由 Safe（原 Gnosis Safe）团队开发，是当前行业标准的链上资产管理解决方案。合约采用 EIP-712 标准实现结构化数据签名，从而提高交易数据的安全性和可验证性。

## **核心用途**

* **资金安全管理：**合约要求多个预先设定的所有者(Owners) 共同确认交易才能执行，从而有效防止单点失误或恶意操作，确保资金安全。
* **交易执行与管理：**通过内置的多签验证机制，合约能够在满足签名阈值条件的情况下，执行对外转账、调用其他合约或处理复杂的业务逻辑，支持代币和原生币的支付和费用补偿。
* **模块化扩展：**合约采用模块化设计，通过继承和组合多个管理模块（如 OwnerManager、ModuleManager、GuardManager、FallbackManager 等），使其功能灵活且易于扩展，为不同应用场景提供定制化支持。

## **函数解析**

execTransaction 函数执行经过多重签名验证的交易：

* 计算交易的唯一哈希值（结合交易参数、nonce 等）；
* 验证所有签名的有效性，确保每个签名均来自合法的所有者或预先批准的地址；
* 调用目标地址的业务逻辑，并在交易执行后通过事件记录成功或失败状态；
* 支持灵活的 gas 费用处理，确保在支付补偿时准确计算交易成本。

checkContractSignatures & checkNSignatures 函数验证交易或消息的签名数据：

* 分别处理 EOA 账户签名、合约签名(EIP-1271)、以及预批准的哈希；
* 确保签名按照所有者顺序排列，并且每个签名都来自有效地址，防止重放攻击和签名篡改。

getTransactionHash 函数生成交易哈希，用于签名验证和防止重放攻击：

* 利用 EIP-712 标准对交易数据进行结构化哈希；
* 使用内联汇编优化内存操作，提高计算效率；
* 结合当前的 nonce 值，确保每笔交易的唯一性。

handlePayment 函数处理执行交易过程中的 gas 补偿支付：

* 根据实际消耗的 gas 费用和基础费用计算支付金额；
* 支持 ETH 以及其他代币的支付，确保费用补偿准确无误。

onBeforeExecTransaction 为内部虚拟钩子函数，在 execTransaction 函数执行之前被调用。该函数的设计目的是允许继承 Safe 合约的子合约在交易执行前进行自定义逻辑处理。接收的参数集包括：

* to：目标地址 - 交易要调用的合约或账户地址
* value：以太币值 - 随交易发送的以太币数量
* data：数据载荷 - 包含函数选择器和参数的调用数据
* operation：操作类型 - 确定是 CALL 还是 DELEGATECALL
* safeTxGas：交易 gas 限制 - 为交易执行预留的 gas 数量
* baseGas：基础 gas - 独立于交易执行的 gas 成本
* gasPrice：gas 价格 - 用于计算交易费用补偿的 gas 价格
* gasToken：gas 代币 - 用于支付交易费用的代币地址
* refundReceiver：退款接收者 - 接收交易费用补偿的地址
* signatures：签名集合 - 所有者对交易的签名数据

尽管多签钱包合约凭借其严谨的安全设计和灵活的模块化结构，为数字资产管理提供了高效且安全的解决方案，实现了从交易初始化到最终执行的全流程安全管控，并成为区块链安全管理的重要工具，但同样需要注意的是，受害者大多依赖硬件钱包进行签名，而部分硬件设备对结构化数据签名的显示效果欠佳，容易导致用户在短时间内无法准确识别交易数据，从而有“盲签”风险。针对这一现象，除了优化硬件及其数据展示效果之外，还可以探索增加多重确认、智能提示以及增强签名验证工具等措施，以进一步降低盲签带来的安全隐患。

# **Safe Guard**

Safe 合约在 1.3.0 版本中引入的重要安全功能 —— Safe Guard 机制。这一机制旨在为标准的 n-out-of-m 多签方案提供额外的限制条件，进一步增强交易安全性。Safe Guard 的核心价值在于能够在交易执行的不同阶段进行安全检查：

* **交易前检查(checkTransaction)：**Guard 机制可以在交易执行前，对交易的所有参数进行程序化检查，确保交易符合预设的安全规则。
* **交易后检查(checkAfterExecution)：**在交易执行完成后，Guard 还会进行额外的安全验证，检查交易执行后 Safe 钱包的最终状态是否符合预期。

##

## **架构分析**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbFIv2cLgxKgjAibLMOBjkrxmewxL1BN3PGmtVk4Hg7aibHAqXhApO5OFMVv1nqEOPBgctAVR5yyI4Q/640?wx_fmt=png&from=appmsg)

在 Safe 中，多签交易一般通过 execTransaction 函数进行执行。在 Safe Guard 启用的情况下，当用户执行多签交易时，Safe 合约将调用 Guard 合约的 checkTransaction 函数执行交易前检查，而当多签交易执行完成后，Safe 合约将调用 Guard 合约的 checkAfterExecution 函数对交易的执行结果进行检查。具体实现如下：

```
function execTransaction(        ...    ) external payable override returns (bool success) {        ...        address guard = getGuard();        {            if (guard != address(0)) {                ITransactionGuard(guard).checkTransaction(                    // Transaction info                    to,                    value,                    data,                    operation,                    safeTxGas,                    // Payment info                    baseGas,                    gasPrice,                    gasToken,                    refundReceiver,                    // Signature info                    signatures,                    msg.sender                );            }        }        ...        {            ...            success = execute(to, value, data, operation, gasPrice == 0 ? (gasleft() - 2500) : safeTxGas);            ...        }        {            if (guard != address(0)) {                ITransactionGuard(guard).checkAfterExecution(txHash, success);            }        }    }
```

当 Safe 合约通过 Guard 机制执行多签交易预检时，其 checkTransaction 函数将接收完整的交易上下文数据，包括目标合约地址、调用方式、执行数据（如 delegatecall）、owner 签名信息、Gas 配置及支付信息。该机制使开发者能够实现多维度的风控策略，例如合约白名单管控（限制可交互地址）、函数级权限管理（禁用高危函数选择器）、交易频率限制以及基于资金流向的动态规则等。通过合理配置 Guard 策略，可有效阻断攻击者利用非合约层面进行攻击。

在近期不断曝出安全事件的背景下，各方对多签钱包合约的安全性日益关注，硬件钱包提供商如 KeyStone 、OneKey、RigSec 等纷纷呼吁增强 Safe 合约的解析和防护能力，以预防类似风险的再次发生。在 Bybit 事件后，许多项目方开始聚焦 Safe 合约，并探索基于 Guard 机制的升级与扩展方案。其中，不乏有基于 Guard 机制的创新应用，构建一种建立在 Safe 多签钱包之上的中间层安全解决方案，为底层资产与用户资产之间提供了额外的安全保障。其核心作用在于，通过将 Safe 多签交易涉及的目标合约、调用方式、执行数据、owner 签名信息、付款信息以及 gas 信息传入 checkTransaction 函数，实现对交易的极细粒度检查，包括白名单合约调用、白名单函数操作、白名单转账目标、交易频次等权限控制。

值得注意的是，Safe 本身只提供 Guard 管理和回调功能，实际的多签交易检查逻辑由用户自行实现，其安全性取决于 Guard 实现的质量。如：Solv Guardian 拓展了这一思路，在每个 Vault 配置专门的 Guardian 来指定允许的目标地址和操作权限，实现了指定允许合约、定义允许函数操作和 ACL 验证需求三大权限控制要素。同时，采用分离的治理机制，由 Vault Guardian 负责执行，而 Governor 控制治理权限，确保即便 Guardian 出现问题，也能及时采取补救措施保护用户资产。类似的设计理念也在 Elytro 的 SecurityControlModule 中得到应用，该模块通过 preExecute 函数拦截关键操作，并借助白名单机制对模块安装、钩子设置和验证器管理等高风险操作进行精细管控，从而确保只有经过信任的合约才能被添加到系统中，为钱包提供了持久的安全保障。

在 Bybit 事件攻击链中，若 Safe 合约部署了合理配置的 Guard 机制，攻击者通过 execTransaction 发起的恶意 delegatecall 将在预检阶段被多重策略拦截：Guard 的 checkTransaction 函数首先识别到 delegatecall 操作类型并触发禁用规则（如强制限定 operation 仅为普通调用），随后解析 data 字段检测到非常规合约地址（0x4622...7242）及高危函数选择器，通过预设的合约白名单与函数黑名单策略直接回滚交易，最终形成「策略拦截 → 逻辑阻断」的防御体系，彻底阻断存储篡改与资金转移路径。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbFIv2cLgxKgjAibLMOBjkrxqMibG0oKiaAIz3NiaTPednlibgYTwLK11v8EwzCCvC2JPoNCFliagIOceHw/640?wx_fmt=png&from=appmsg)

(当使用 Safe 版本 ≥ v1.3.0  Safe Guard 模块的验证操作 https://excalidraw.com/#room=fd1df67dd09b3dab6bd8,Q1jeb1MZW7vwbY4NuxaV5A)

总的来说，Safe 仅在 1.3.0 版本之后才提供 Guard 功能，尽管 Guard 可以提供极为细粒度的多签交易检查，但用户在使用 Guard 功能时有较大的门槛。他们需要自行实现 Guard 检查逻辑，粗略的或者有缺陷的 Guard 实现可能无法帮助用户提升其 Safe 钱包的安全性，因此对 Guard 实现进行安全审计是必要的。毫无疑问的是，安全且适当的 Guard 实现可以极大提升 Safe 钱包的安全性。

# **结论与展望**

Bybit 被攻击事件凸显了及时更新安全基础设施的重要性，Bybit 使用的是 v1.1.1 (<1.3.0) 版本的 Safe 合约，这意味着他们无法使用 Guard 机制这一关键安全特性。如果 Bybit 升级到 1.3.0 或更高版本的 Safe 合约，并实现了合适的 Guard 机制，例如指定唯一接收资金的白名单地址，并进行严格的合约函数 ACL 验证，可能就能避免这次的损失。尽管这只是假设，但它为未来的资产安全管理提供了重要思路。

Safe Guard 机制就像给数字资产保险箱加装的智能安检系统，其效能取决于规则设计的严谨性和实施质量。面对日益精密的攻击手段，我们需要：

* 自动化验证：建立自动化的交易验证机制
* 动态策略调整：根据威胁情报实时调整安全策略
* 多层防御：结合多种安全机制构建深度防御体系
* 持续审计：对 Guard 实现进行定期安全审计

未来的数字资产管理，将是智能合约安全机制与持续攻防演进的共同进化过程。只有将安全理念融入每一个环节，才能在黑客的"矛"与守护者的"盾"的博弈中构筑真正的安全壁垒。

**参考资料**

[1] https://github.com/safe-global/safe-smart-account/blob/v1.3.0/CHANGELOG.md

[2] https://docs.safe.global/advanced/smart-account-guards

[3] https://docs.solv.finance/security/solv-guard

[4] https://github.com/safe-global/safe-smart-account/tree/main/contracts/examples/guards

[5] https://github.com/Elytro-eth/soul-wallet-contract/blob/v0.6/contracts/modules/securityControlModule/SecurityControlModule.sol

**往期回顾**

[加密货币 APT 情报：揭秘 Lazarus Group 入侵手法](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501259&idx=1&sn=0b2183929367aa5845f0a9e1d1a42e74&scene=21#wechat_redirect)

[慢雾：Bybit 近 15 亿美元被盗背后的黑客手法与疑问](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501246&idx=1&sn=eafc7080cc28d1f8bf16c362f3ac2230&scene=21#wechat_redirect)

[顺藤摸瓜｜披露假冒慢雾员工行骗事件](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501212&idx=1&sn=996e238a420...