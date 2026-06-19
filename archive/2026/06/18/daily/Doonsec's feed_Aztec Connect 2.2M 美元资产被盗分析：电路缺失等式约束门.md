---
title: Aztec Connect 2.2M 美元资产被盗分析：电路缺失等式约束门
url: https://mp.weixin.qq.com/s/MMvqyqWBL3XRy-8XkgC7ew
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T06:59:51.495122
---

# Aztec Connect 2.2M 美元资产被盗分析：电路缺失等式约束门

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8z8bibAexaCLXwS39bP7liam7mXEPQ9qy57mqJb0a6ZcQagtJEyWHPIq9RxVFR4hBtARUoibuZ54251Yic0LkI6bo6dvyehiaFVK1qCmdIRia6qNA/0?wx_fmt=jpeg)

# Aztec Connect 2.2M 美元资产被盗分析：电路缺失等式约束门

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

********## 背景******

******##

2026 年 6 月 18 日，以太坊 Layer2 隐私协议 Aztec Connect 的 RollupProcessor 合约遭遇攻击。攻击者利用其 Escape Hatch（逃生舱）机制在 Solidity 层缺少独立的资金归属与提款额度校验这一信任边界缺陷，以及相关电路约束缺失，提交了 TurboVerifier 接受的 escape hatch proof，直接从合约余额中提走 1,158 ETH（约 206 万美元），另通过同一机制盗取 150,000 DAI 与 0.47 renBTC，合计损失约 222 万美元。

## 攻击概览

|  |  |
| --- | --- |
| 字段 | 详情 |
| 攻击类型 | 逻辑缺陷 / Escape Hatch 提款路径信任边界缺陷（Permission Bypass via Escape Hatch） |
| 受害合约 | `0x737901bea3eeb88459df9ef1be8ff3ae1b42a2ba`（Aztec Connect RollupProcessor） |
| 攻击者 EOA | `0x6952d9246e9aFE8B887B2877225163436F78E97F` |
| 攻击合约 | 无（攻击者直接以 EOA 发起调用） |
| 获利金额 | 约 222 万美元（1,158 ETH + 150,000 DAI + 0.47 renBTC） |
| 所在链 | Ethereum |
| 交易数量 | 3 笔 |

攻击交易：

|  |  |  |
| --- | --- | --- |
|  | 资产 | 交易哈希 |
| 1 | 1,158 ETH | [`0xab306cd2184d23b6ba3e151b10b3b9a0b81f211cc16f4f3b0c79f0b17a59c2b5`] |
| 2 | 150,000 DAI | [`0x5c196c37a109d74c9797254287a0331f30e0daa637af241bd28fdc43774705c3`] |
| 3 | 0.46963295 renBTC | [`0x9e1d6ab7c20ae235409d7dd3a9cd47c04f07293585b3498b8beed82d6f6b03ca`] |

## 漏洞根因******

******##

### escapeHatch() 的信任边界缺失******

******###

RollupProcessor 的公开入口函数 escapeHatch() 仅检查 escape hatch 状态是否开启，随后直接进入 processRollupProof()，不执行任何调用者权限校验：

```
function escapeHatch(   bytes calldata proofData,   bytes calldata signatures,   bytes calldata viewingKeys) external override whenNotPaused {   (bool isOpen, ) = getEscapeHatchStatus();   require(isOpen, '...');

   // ⚠️ 漏洞点 1：没有 onlyOwner 修饰符   // ⚠️ 漏洞点 2：没有 rollupProviders[msg.sender] 授权检查   // ⚠️ 漏洞点 3：没有 provider signature 校验   // ⚠️ 漏洞点 4：任何外部地址在 escape hatch 开启时均可提交 proofData   processRollupProof(proofData, signatures, viewingKeys);}
```

相比之下，普通 rollup 处理路径 processRollup() 会校验 rollupProviders[provider] 授权并验证 provider signature。而本攻击中调用的是 escapeHatch()，传入的 signatures = 0x、viewingKeys = 0x，完全绕过了 provider 授权流程。

### verifyProofAndUpdateState() 对 Verifier 的盲目信任******

******###

进入 processRollupProof() 后，合约调用 TurboVerifier.verify(proofData, 0)：

```
function verifyProofAndUpdateState(bytes memory proofData)    internal    returns(uint256 numTxs){    // rollupSize == 0 时，TurboVerifier 使用 EscapeHatchVk（keyId=0）    // 对应 vk.num_inputs = 26，用于 escape hatch proof 的 Plonk 数学验证    bool success = verifier.staticcall(        abi.encodeWithSelector(            0xac318c5d, // verify(bytes,uint256)            proofData,            rollupSize  // = 0        )    );    require(success, "...");    // ⚠️ 漏洞点 5：verifier 只做 Plonk 数学验证，不检查：    //   - 调用者身份    //   - ETH 余额归属    //   - 提款额度    //   - pending deposit    // 只要数学上 proof 与 public inputs 一致就返回成功}
```

TurboVerifier 本身行为正确——它完成了 Plonk proof 的数学验证。真正的问题在于 RollupProcessor 将数学验证成功等同于业务合法性，未在 Solidity 层再做一层独立校验。

### processDepositsAndWithdrawals() 无条件执行提款******

******###

Verifier 返回成功后的核心执行逻辑：

```
function processDepositsAndWithdrawals(    bytes memory proofData,    uint256 numTxs,    bytes memory signatures) internal {    for (uint256 i = 0; i < numTxs; i++) {        // 从 proofData 解析 inner tx 字段        if (proofId == 0 && publicOutput > 0) {            // ⚠️ 漏洞点 6：直接信任 proofData 中的 publicOutput 和 outputOwner            // 没有在 Solidity 层确认：            //   - 该提款是否对应真实存款            //   - outputOwner 是否有合法的可提款余额            //   - 调用者与 outputOwner 是否存在关联            withdraw(publicOutput, outputOwner, assetId);        }    }}
```

最终资金转出函数：

**```
function withdraw(   uint256 withdrawValue,   address receiverAddress,   uint256 assetId) internal {   require(receiverAddress != address(0), '...');   if (assetId == 0) {       // 注意：ETH 分支故意不对 call 失败执行 revert，       // 防止攻击者构造必然失败的提款来使整个 rollup block 无效化（griefing 攻击）。       // 因此返回值被显式丢弃，call 失败不回滚。       // receiverAddress = 攻击者 EOA       // withdrawValue   = 1158 ETH       payable(receiverAddress).call{gas: 30000, value: withdrawValue}('');   } else {       // ERC20 提款路径（DAI / renBTC 攻击使用此分支）   }   // totalWithdrawn 累加在转账之后，索引为 assetId 而非硬编码 0   totalWithdrawn[assetId] = totalWithdrawn[assetId].add(withdrawValue);}
```

**zkSNARK 电路缺失等式约束门（根本原因）**********

********###

**在 Aztec join-split 证明电路中，old\_data\_root 被分为两条独立路径使用：

* 内部见证 A：传入 join-split 子电路，用于验证私有笔记的 Merkle 成员资格
* 公共输入 B：作为公共输入暴露给 Solidity 层，供 validateMerkleRoots() 与链上 dataRoot 比对

电路中缺失约束 A == B，导致两者可以独立赋值：

* A 可以是攻击者构造的伪造 Merkle 树根（树中含任意金额笔记）
* B 可以是真实链上 dataRoot（使 Solidity 检查通过）

由于约束系统允许 A ≠ B，整个 zkSNARK proof 仍然有效。****

## 攻击流程********

****准备阶段：伪造 Merkle 树和 proof**

******###

**攻击者在本地构建一棵伪造的 data Merkle 树，树中插入一条私有笔记：

* 价值：1158 ETH（合约当时持有约 1158.7598 ETH）
* 所有者：攻击者持有对应私钥

攻击者构造 zkSNARK proof：

* 内部见证 A（old\_data\_root） = 伪造树根
* 公共输入 B（old\_data\_root） = 链上实际 dataRoot = 0x184bea7d9493cd9a5efb6b679d04066a8c92a34ac8ec150e9635133c6010977b

**### 第一阶段：构造攻击交易

攻击者 EOA 0x6952d9246e9aFE8B887B2877225163436F78E97F 直接向 RollupProcessor（0x737901bea3eeb88459df9ef1be8ff3ae1b42a2ba）发起顶层调用：

* 函数签名：escapeHatch(bytes,bytes,bytes)
* msg.value = 0
* signatures = 0x
* viewingKeys = 0x

攻击者构造的 proofData 中包含关键 public inputs：****

```
rollupId      = 0x1187publicOutput = 0x3ec67a70a72e580000（= 1,158 ETH）outputOwner  = 0x6952d9246e9aFE8B887B2877225163436F78E97F（攻击者地址）assetId      = 0（代表 ETH）
```

### 第二阶段：绕过权限检查******

******###

escapeHatch() 仅检查 getEscapeHatchStatus() 返回 true 后，直接调用 processRollupProof()。该路径不执行普通 processRollup() 中的 rollupProviders[provider] 授权检查，也不验证 provider signature。调用者身份与提款接收者之间无任何绑定关系。

### 第三阶段：Verifier 数学验证******

******###

RollupProcessor 对 TurboVerifier（0x48cb7ba00d087541dc8e2b3738f80fdd1fee8ce8）发起 STATICCALL：

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCJ091YSwGj3zkic2BKa60hq6xHejT3xXZJxelZwvOhN3DRNicKoDaKibFQON5madiansXb5eOABW7F9Zd120Qvl5CQ2IgyGyJ7mg28/640?wx_fmt=png&from=appmsg)

因为 rollup\_size = 0，TurboVerifier 通过 VerificationKeys.getKeyById(0) 选择 EscapeHatchVk（vk.num\_inputs = 26）进行 Plonk proof 数学验证。Verifier 只验证 proof 与 public inputs 的数学一致性，不读取 RollupProcessor 状态，不检查余额归属。

本交易中 verifier 调用成功返回，说明攻击者提交的 escape hatch proof 在数学上正确。

### 第四阶段：执行提款******

******###

Verifier 返回成功后，RollupProcessor 更新 rollup 状态：

```
nextRollupId:   0x1187 → 0x1188dataSize:       0xe5080 → 0xe5082data root / null root / root root 均已更新event RollupProcessed(uint256,bytes32,bytes32,bytes32,uint256) 被触发
```

随后进入 processDepositsAndWithdrawals()，在 escape hatch 模式下 rollupSize == 0 仍按 1 笔 inner tx 处理。解析 proofData 后发现：

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCK8gysoiaWdggQmKiaQZQRdDlrldd0ZP6CP2Rhogp4cMCH9Z3ibvRDSNWPJiavAicNV4IP3L3gY27NYyicial1ibuAePmOQZibFYbkK6XsI/640?wx_fmt=png&from=appmsg)

直接调用 withdraw(1158 ETH, 攻击者地址, 0)，通过 receiverAddress.call{value: 1158 ETH}("") 将资金转出。

### 第五阶段：同模式攻击 DAI 与 renBTC******

******###

攻击者在同一时期使用完全相同的漏洞路径，分别构造了针对 ERC20 资产（assetId ≠ 0）的 escape hatch proof，将 150,000 DAI 和 0.47 renBTC 从 RollupProcessor 中盗取。withdraw() 函数中 assetId ≠ 0 分支执行 ERC20 的 transfer() 完成转账。

三笔攻击的净收益：

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCJEt6UWK9G6Pj6TeLKAhKtsdlKhfJ9LxCuibMy7eMSwp3ia3ljWGK1KJqInH2YtI5TEZD4CNTBTYxf5Pp9t7O6uwzTuXsXqiaOlpY/640?wx_fmt=png&from=appmsg)

资金追踪

通过慢雾 MistTrack 反洗钱追踪系统对攻击者 EOA 0x6952d9246e9aFE8B887B2877225163436F78E97F 进行分析：

资金来源：攻击者创建地址使用的初始 Gas 来自 0x963737c550e70ffe4d59464542a28604edb2ef9a（unionchain.ai 实体地址）。该地址首次活跃于 2026 年 6 月 18 日 02:21:11 UTC，恰在攻击行动启动时刻，属于专为本次攻击创建的一次性地址。

资金去向：被盗资金当前分布如下：

* 802 ETH 代币仍留存于攻击者主地址 0x6952d9246e9aFE8B887B2877225163436F78E97F， 150,000 DAI 和 0.47 renBTC 也仍未转移
* 300 ETH 已转移至 0x15930a0fef3421f48c6553b5691682cc1b22edb3（MistTrack 标记为 Aztec Exploiter 关联恶意地址）
* 约 56 ETH 已转移至另一恶意地址（同样标记为 Aztec Exploiter 关联）
* 0x33d6a0d9bc210e823e043d604179cd844eb467df AML 风险评分 100/100（Severe），同样涉及 Aztec Exploiter 事件

##******

******## 总结******

******##

**本次攻击的核心教训是：zkSNARK 电路的"数学正确"≠"业务安全"。验证器只能证明"你知道某个满足约束的见证"，如果约束本身是错的（或缺失的），证明系统就成了合法的伪造机器。**慢雾安全团队建议项目方对所有零知识证明约束路径进行专项审计，确保电路的安...