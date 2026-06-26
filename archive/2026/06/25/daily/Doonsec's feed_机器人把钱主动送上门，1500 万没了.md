---
title: 机器人把钱主动送上门，1500 万没了
url: https://mp.weixin.qq.com/s/RZPXLCaRGXB42cZhA42gUg
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:07:05.195154
---

# 机器人把钱主动送上门，1500 万没了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ibKZs4HxyqscSHRsZianVy3YibckXM3Ajywnkw3trVzTfibhmLoH3LibiaWCDE3tB55a5GNZ2sjibUSDNmMJdu1L0oaCgHR9Vm71hdT1e1PFeRmnE/0?wx_fmt=jpeg)

# 机器人把钱主动送上门，1500 万没了

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ibKZs4HxyqulmpJena0QpvmibL1tj9eWTCzeiacKwPpGxib5BIxN6Qxd8O1gR44Tiaiam7EmCgRG8wIQjeDev4U7ibdTZic6gicQK4KUqrFQKOvraKY/640?wx_fmt=gif&from=appmsg)

**简介**

核心要点：

* 横跨 Ethereum 和 BNB Chain 的 3 起安全事件，总损失约 $18.3M。
* 攻击类型包括 MEV 机器人合约授权管理不当、ZK 公共输入绑定缺陷，以及代币参数错误配置导致的储备金操纵。
* 本期重点 jaredFromSubway 事件揭示了一种与传统 DeFi approval 漏洞方向相反的攻击模式。传统场景中，攻击者利用可信 DeFi 合约的漏洞转走用户 approve 给合约的资产；本次攻击中，MEV 机器人为了套利主动将自身资产 approve 给不可信的第三方合约，攻击者积累这些对外授权后一次性提取 ~$15M。

过去一周（2026/06/15 – 2026/06/21），我们观察到 3 起值得关注的安全事件，总损失约 $18.3M。下表汇总了本周事件，后续小节将对重点事件进行详细分析。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqtUQUdyYViazIsVagQqgBYcT7OumdDVgoQpCF5yFSc44KXQAbgdRGu9x2jpicOGJ2RQ5x3Z4iaThKCFUSAUpW7VzMyZKJZe7hbbiaU/640?wx_fmt=png&from=appmsg)

表 1：本周检测到的安全事件概览

* Aztec：该协议在三天内第二次被攻击，这次通过 escape hatch 电路实施，凸显了 ZK proof binding 问题的反复出现。
* jaredFromSubway：MEV 机器人合约对不可信代币合约授权后未验证消耗、未撤销残余额度，攻击者得以积累并提取 ~$15M。

**本期看点：jaredFromSubway**

与传统 approval 漏洞不同——传统场景中攻击者利用可信 DeFi 合约的缺陷转走用户 approve 给合约的资产——本次攻击方向相反：MEV 机器人为了套利主动将自身资产 approve 给不可信的第三方代币合约。攻击者构建了伪造交易环境（本质上是蜜罐），伪造交易池发出真实的 Swap 和 Sync 事件而伪造代币从未消耗已授予的额度，不断积累这些对外授权后一次性收割，报告总损失约 $15M。

2026 年 6 月 20 日，Ethereum 上 MEV 机器人运营者 jaredFromSubway 损失约 $15M [1]。根据链上分析，根本原因是机器人合约的授权管理不当：机器人向不可信的 wrapper 合约授权后，这些合约从未消耗授权额度，攻击者不断积累这些未消耗的授权，最终在单笔交易中提取了机器人的真实余额。

背景

jaredFromSubway 是 Ethereum 上知名的 MEV 机器人运营者，专注于三明治攻击和链上套利。受害合约（0x1f2f...f387）是其运营钱包之一，持有大量 WETH、USDC 和 USDT 营运资金。

此类 MEV 机器人需要动态与链上出现的任意新代币和交易池交互。它们监控 mempool、模拟交易，并自动授权代币交互以捕获套利机会。这一运营模式依赖于一个假设：执行 swap 时，代币合约会通过调用 transferFrom 消耗已授予的额度。

漏洞分析

根本原因是 MEV 机器人合约对不可信合约的授权管理不当。

机器人通过 Uniswap 池和 router 执行多种套利路径。大多数交互中，机器人通过 transfer 直接向池推送代币，此时机器人本身是 msg.sender，不需要授权。但与 wrapper 类型代币合约的交互采用拉取模式：机器人调用 wrapper.wrapTo()，在该调用内部，wrapper 合约调用 realToken.transferFrom(bot, wrapper, amount) 拉取机器人的真实代币。由于 transferFrom 时的 msg.sender 是 wrapper 合约而非机器人本身，因此需要事先 approve：

1. <真实代币>.approve(tokenContract, amount) — 向 wrapper 合约授予真实代币的额度
2. tokenContract.wrapTo() → 多跳 swap() → tokenContract.unwrap() — wrap 真实代币，经池路由，再 unwrap 回真实代币

机器人假设 wrapTo() 会通过 transferFrom 消耗授权，这是合规 wrapper 合约的标准行为。然而机器人从未验证操作后授权是否实际被消耗，也未撤销残余额度。若 wrapTo() 不调用 transferFrom，全部授权额度在操作后仍然存续，成为持续的攻击面——持有该授权的任何合约日后可调用 transferFrom 转移机器人的真实资产。

攻击分析

根据链上还原，攻击者构建了三层伪造交易环境来利用上述漏洞：

1. 伪造 wrapper 代币：每个伪造代币使用真实代币的 name 但在 symbol 前加 f 前缀（如 name 为 USD Coin、symbol 为 fUSDC 对应 USDC）。实现了 wrapTo() 和 unwrap() 模拟合法 wrapper，以及仅限攻击者调用的 withdraw() 函数通过 transferFrom 提取未消耗的授权额度。
2. 伪造交易池：攻击者通过自部署的工厂合约创建了约 44 个 Uniswap V2 风格的交易池，将伪造代币相互配对形成 swap 路由。调用 swap() 时，池发出真实的 Sync 和 Swap 事件，与合法交易无法区分。
3. 攻击者构造的利润：unwrap() 执行时，伪造代币通过 transfer 向机器人发送少量真实代币。机器人获得了真实利润，但这是攻击者刻意构造的而非来自市场套利。

攻击者通过外部合约的按区块 getStatus() 开关控制这些组件。getStatus() 在与激活交易处于同一区块时返回 1（激活交易设置 \_getStatus = block.number），否则返回 0。当 getStatus() == 0 时，wrapTo() 正常调用 transferFrom 消耗授权。当 getStatus() == 1 时，wrapTo() 跳过 transferFrom——授权不被消耗——而 unwrap() 仍向机器人返还攻击者构造的代币。攻击者很可能通过 builder 贿赂将激活交易与机器人交易放入同一区块，以此控制何时积累授权。

攻击分三阶段进行：

第一阶段：部署攻击基础设施

Step 1：攻击者在区块 25354424 至 25354519 期间部署了基础设施，包括：伪造代币工厂合约（0x81f2...0091）、通过自部署工厂创建的 ~44 个伪造 Uniswap V2 池、为池注入初始代币余额使 swap() 调用可执行，以及向收割合约（0xb84d...df52）发送 0.01 ETH 用于 gas 和 builder 贿赂。

Step 2：攻击者通过 CREATE2 批量生产伪造 wrapper 代币，每个代币模仿真实代币（使用真实 name 但在 symbol 前加 f 前缀）并携带仅限攻击者调用的 withdraw() 函数。CREATE2 提供确定性地址，使收割合约可以遍历调用。

第二阶段：建立信任并积累授权

Step 3（初始信任）：在最早的交易中（如区块 25354425 的 0x542d...362b），伪造代币尚未部署 getStatus() 开关——wrapTo() 直接调用 transferFrom 消耗授权。机器人正常执行 approve、wrap、swap、unwrap 并获利。这使伪造代币建立了可盈利的交易机会形象。

Step 4（持续信任）：在后续交易中（如 0x085e...37e51），getStatus() 开关已部署但返回 0（与激活交易不在同一区块）。wrapTo() 仍调用 transferFrom 消耗授权。机器人继续获利并持续交互。

Step 5（授权积累）：从区块 25360519 的 0x8560...1915 开始，攻击者通过 builder 贿赂将激活交易与机器人交易放入同一区块，使 getStatus() 返回 1。此模式下 wrapTo() 跳过 transferFrom——授权不被消耗——但 unwrap() 仍通过 transfer 向机器人发送少量真实代币。机器人看到盈利操作，保持授权不撤销。在约 600 个区块（~13 笔交易）中，机器人对 WETH、USDC 和 USDT 重复此模式，三种真实资产的未消耗授权不断积累。

第三阶段：收割

Step 6：攻击者在收割交易 0x2be870...cf3e65 中对所有伪造代币调用 withdraw()，利用未消耗的授权调用 transferFrom 将机器人的真实余额转移给攻击者。交易包含 0.01 ETH 的 builder 贿赂以确保被打包。仅从受害合约就收割了 1,474.58 WETH + 2,870,573 USDC + 2,035,760 USDT（~$7.5M）。

已确认的攻击交易造成约 $7.5M 损失，总损失约 $15M 来自 jaredFromSubway 的声明 [1]。

结论

本次事件的根本原因是 MEV 机器人合约对不可信合约的授权管理不当。与传统 approval 漏洞——攻击者利用可信 DeFi 合约的缺陷转走用户 approve 给合约的资产——不同，本次攻击方向相反：机器人为了套利主动将自身资产 approve 给不可信的第三方合约，攻击者积累这些对外的、未消耗的授权后一次性收割。

为降低类似风险，与不可信代币合约交互的机器人合约应在每次操作后验证授权是否被消耗，并撤销任何残余额度。成功交易后授权未被消耗是恶意代币行为的强信号。

**本期其它事件**

Aztec

2026 年 6 月 18 日，Aztec escape hatch ZK 电路中缺失的相等约束使攻击者从 Ethereum 上的旧版 RollupProcessor 合约提取了约 $2.2M（1,158 ETH、150K DAI 和 ~0.47 renBTC）[2]，[3]。这是三天内 Aztec 第二次被攻击（第一次收录于上期报告，针对升级后的 RollupProcessorV3），同样源于 ZK 电路 public input binding 缺陷。

背景

Aztec 的旧版 RollupProcessor 包含 escapeHatch 函数，这是一个安全机制，当 rollup 运营方停止处理时，允许任何人提交单笔交易 proof。与需要授权 provider 的常规 processRollup 不同，该 escape hatch 按区块号周期性开放，任何人均可调用：

```
function escapeHatch(    bytes calldata proofData,    bytes calldata signatures,    bytes calldata viewingKeys) external override whenNotPaused {    (bool isOpen, ) = getEscapeHatchStatus();    require(isOpen, 'Rollup Processor: ESCAPE_BLOCK_RANGE_INCORRECT');    processRollupProof(proofData, signatures, viewingKeys);}
```

该 escape hatch 使用专用的 ZK 电路（escape\_hatch\_circuit）处理 join-split 交易：从 Merkle tree 中消费输入 note 并创建输出 note。电路必须验证输入 note 存在于当前 data tree 中（使用 old\_data\_root 进行 Merkle 成员证明），然后将相同的根暴露为 public input 供 L1 合约与链上状态比对。

漏洞分析

漏洞位于 escape hatch 电路（escape\_hatch\_circuit.cpp）。old\_data\_root 值被创建为两个独立的 witness，二者之间没有 equality constraint。

第一个 witness（line 33）传入 join-split 电路组件，用于 Merkle 成员证明以验证输入 note 存在于 data tree 中：

```
join_split_inputs inputs = {    // ...    witness_ct(&composer, tx.js_tx.old_data_root),        // line 33: first witness    // ...};auto outputs = join_split_circuit_component(composer, inputs);
```

第二个 witness（line 50）独立创建并暴露为 public input（line 88），即 Solidity 合约提取并与链上 data root 比对的值：

```
auto old_data_root = field_ct(witness_ct(&composer, tx.js_tx.old_data_root));  // line 50: second witness// ...composer.set_public_input(old_data_root.witness_index);    // line 88: exposed as public input
```

在 ZK 电路中，每次 witness\_ct 调用创建一个独立变量。line 33 和 line 50 之间没有显式 assert\_equal，prover 可以为这两个 witness 赋予不同的值。在 Solidity 侧，validateMerkleRoots 仅使用 line 50 的 public input 检查 require(oldDataRoot == dataRoot)，对 line 33 使用的值不可见。

同样的 unbinding 模式也存在于 input\_owner 和 output\_owner：这些值在 line 38-39 被 witness（传入 join\_split\_circuit\_component 用于所有权验证），又在 line 111-112 作为独立的 public witness 暴露。不过我们未发现该问题的实际利用路径。

攻击分析

该 escape hatch 电路已在 aztec-connect 代码库中被删除 [4]，但已部署的 verifier 合约仍保留 EscapeHatchVk 验证密钥，使用该漏洞电路生成的 proof 仍可通过链上验证。攻击发生时，该合约已沉寂 142 天，escape hatch 窗口处于开放状态。攻击者地址在攻击前 14 小时才通过 Union Chain 创建 [2]，攻击由以下三个核心步骤构成：

Step 1：攻击者构造了一棵包含自有 note（任意面额）的假 Merkle tree。这些 note 不存在于真实的链上 data tree（存储所有有效 note 的 Merkle tree）中。

Step 2：攻击者利用上述未绑定的 witness 生成 escape hatch proof。Line 33 的 witness（用于 join-split 组件内的 Merkle 成员验证）设为假 Merkle root（成员证明通过，因为伪造的 note 确实存在于假树中；所有权验证通过，因为攻击者持有签名密钥）。Line 50 的 witness（暴露为 Solidity 检查的 public input）设为真实链上 data root（Solidity 侧 require(oldDataRoot == dataRoot) 检查通过，因为该值与合约存储的根一致）。

Step 3：电路和 Solidity 两侧检查均被满足，proof 验证成功。合约将该 escape hatch 交易视为合法并释放资金。

攻击者针对不同资产通过三笔交易（0x9e1d6a...6b03ca、0xab306c...59c2b5、0x5c196c...4705c3）重复上述流程，分别提取了 1,158 ETH、150K DAI 和 ~0.47 renBTC，合计约 $2.2M。

结论

根本原因是 escape hatch 电路中 old\_data\_root 的两个 witness 缺少 equality constraint。一个 witness 用于 join-split 组件内的私有 note 成员验证，另一个暴露为 Solidity 检查的 public input。缺少约束绑定，攻击者在假 Merkle tree 上证明了伪造 note 的所有权，而 L1 合约看到的是有效的链上根。值得注意的是，从源码中删除漏洞电路并未使已部署的 verifier 合约失效——旧版 RollupProcessor 上的 escapeHatch 函数在其区块号窗口开放时仍可被调用。

为降低类似风险，当同一逻辑值在 ZK 电路中多处出现时，所有实例必须被显式约束为相等——对同一值的独立 witness\_ct 调用即为 binding 缺口。电路审计应系统性验证每个 public input 是否绑定到其所代表的电路内部值。

参考资料

[1] jaredFromSubway 官方声明（~$15M 损失）— https://x.com/jaredsmev/...