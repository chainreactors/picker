---
title: 被黑分析 | ShapeShift FOX Colony 授权信任链缺陷
url: https://mp.weixin.qq.com/s/7bimneyMUhZhzEysLINb7A
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:47:33.829276
---

# 被黑分析 | ShapeShift FOX Colony 授权信任链缺陷

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8z8bibAexaCJwJTI5usVmo4lCYPDkbUmgs9tmZkPEAjazyv66UeABq0TiaZWGeY9R8hiaaxPx9dxiczqr6AUwXecxDhrrMEUhk001N16q8Bicm6w/0?wx_fmt=jpeg)

# 被黑分析 | ShapeShift FOX Colony 授权信任链缺陷

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

********背景******

2026 年 5 月，ShapeShift FOX Colony 项目部署在 Arbitrum 上的 EtherRouterCreate3 合约遭到攻击。攻击者利用合约元交易机制中的「任意自调用」能力，配合 DSAuth 对 address(this) 的自动授权逻辑，绕过 auth 修饰符将合约的核心路由组件 resolver 替换为恶意版本，进而通过 delegatecall 清空合约持有的全部 ERC20 资产。本次攻击的本质是「元交易元语与内部自调用授权模式的语义冲突」所导致的一次完全权限绕过。

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCJ2l6HhGZfoDpk6dia1fRHtMD3mLnjQvj0BrjKmASOz8FZzNOhSbYa6QjZAQw7UTBeJk5ZNK2Dxicc1VIWIr7SRWGA1RNS3fkxRE/640?wx_fmt=png&from=appmsg)

## 攻击概览

|  |  |
| --- | --- |
| 字段 | 详情 |
| 攻击类型 | 访问控制绕过 / 元交易任意自调用致 Resolver 劫持 + 恶意 delegatecall 资产清空（Access Control Bypass via Meta-Transaction Self-Call → Resolver Hijacking） |
| 受害合约 | `0x5c59d0ec51729e40c413903be6a4612f4e2452da`（EtherRouterCreate3 / EtherRouter，ShapeShift FOX Colony） |
| 攻击者 EOA | `0xeed236afb6967f74099a0a6bf078bc6b865fbf28` |
| 攻击合约 | `0x835a701fd76b96a76ee84de037d41f059ee29f5c`（临时） |
| 获利金额 | 132,704.591501 USDC + 1.9495 WETH（约合 136,000 USD） |
| 所在链 | Arbitrum |
| 交易数量 | 单笔原子交易（攻击逻辑在 constructor 中全链路执行） |

## 漏洞根因

### executeMetaTransaction 的任意自调用：address(this).call(callData) 未过滤敏感 selector**

**### 合约 EtherRouter 本身是一个基于 resolver 的可升级代理架构：对于未知函数选择器，fallback() 调用 resolver.lookup(msg.sig) 找到实现地址后通过 delegatecall 执行。元交易功能（executeMetaTransaction）由旧 resolver 0x7490022b0e44aa65c030ac0d6728382a29458fc5 路由到实现合约 0x4e7f1e1e263678590007e89b7e129686ba7758d4 执行。该实现合约未开源，以下基于反编译结果：**

```
function executeMetaTransaction(    address userAddress,    bytes memory functionSignature,    bytes32 sigR,    bytes32 sigS,    uint8 sigV) public returns (bytes memory) {    // 使用 nonce、address(this)、chainid、functionSignature 构造消息    // 通过 ecrecover 校验签名恢复地址 == userAddress    require(recoveredAddress == userAddress);
    // nonce++    _executeMetaTransaction[userAddress]++;    // 构造 calldata    bytes memory callData = abi.encodePacked(        functionSignature,        0x2bcc191e283bfba76a1369ec8ba06566f33010645097c104c312753e04935e8,        userAddress    );
    // ⚠️ 漏洞点：验签后对 address(this) 执行任意 functionSignature 自调用，    // 未禁止 setResolver(address)、setOwner(address)、setAuthority(address) 等敏感 selector    (bool success, bytes memory returnData) = address(this).call(callData);    require(success);
    emit MetaTransactionExecuted(userAddress, msg.sender,     functionSignature);        return returnData;}
```

**问题本质：executeMetaTransaction 的设计意图是允许用户通过签名执行某些非敏感操作，但它对 functionSignature 不做任何过滤。攻击者可以使用自己的有效签名，让合约对自身调用 setResolver(恶意地址)。

### DSAuth.isAuthorized 的自动授权：src == address(this) 即放行

EtherRouter.setResolver(address) 受到 auth 修饰符保护，本应只允许 owner 或 authority 调用：**

```
Resolver public resolver;
function setResolver(address _resolver) public auth {    resolver = Resolver(_resolver);}
```

**但 DSAuth.isAuthorized(address src, bytes4 sig) 中存在自调用自动授权逻辑：**

```
function isAuthorized(address src, bytes4 sig) internal view returns (bool) {    if (src == address(this)) {        return true; // ⚠️ 漏洞点：自调用无条件授权    } else if (src == owner) {        return true;    } else if (authority == DSAuthority(0)) {        return false;    } else {        return authority.canCall(src, this, sig);    }}
```

**当 executeMetaTransaction 通过 address(this).call(setResolver(...)) 触发自调用时，setResolver 中看到的 msg.sender 即为合约自身 0x5c59...，因此被 DSAuth 自动放行。

单独来看，这两处设计都不算明显漏洞——自调用授权在许多代理模式中很常见，元交易机制本身也合理。但两套逻辑同时存在时，语义冲突就产生了：元交易提供的「任意自调用」能力恰好撞上了 DSAuth 的「自调用即信任」逻辑，合在一起就是完整的权限绕过链。

### EtherRouter.fallback() 的 delegatecall 动态路由：Resolver 被劫持后的完整控制权移交**

```
fallback() external payable {    address target = resolver.lookup(msg.sig);    require(target != address(0));
    // ⚠️ 漏洞点：对 resolver 返回的地址无条件执行 delegatecall，    // 一旦 resolver 被替换，任意未知 selector 都会被路由到攻击者实现    assembly {        calldatacopy(0, 0, calldatasize())        let result := delegatecall(gas(), target, 0, calldatasize(), 0, 0)        returndatacopy(0, 0, returndatasize())
        switch result        case 0 { revert(0, returndatasize()) }        default { return(0, returndatasize()) }    }}
```

**resolver 被替换后，攻击者只需调用 EtherRouter 上不存在的任意函数选择器，fallback() 就会无条件委托到攻击者控制的恶意实现。**

**### 恶意 Resolver 与 Drain 实现：无权限的函数映射注册表 + address(this) 资产清空

攻击者预先部署了两个合约：

恶意 Resolver

0x4e321af09012e15a67756522187c05b108b7ee0a（未开源，反编译）：**

```
contract FunctionPointerRegistry {    mapping(bytes4 => address) private _lookup;        function lookup(bytes4 sig) public returns (address) {        return _lookup[sig];    }        // ⚠️ 漏洞点：无任何权限控制，任何人可注册任意 selector → implementation 映射    function set(bytes4 functionSig, address implementation) public {        _lookup[functionSig] = implementation;    }}
```

**恶意 Drain 实现

0x0b971e0a8ecc7d5b2465c903cf75aeaedbfc39e2（未开源，反编译）：**

```
function drain(address token, address recipient) public {    // ⚠️ 由于该函数由受害合约 delegatecall 执行，    // address(this) 实际为受害合约地址 0x5c59...    uint256 balance = IERC20(token).balanceOf(address(this));    IERC20(token).transfer(recipient, balance);}
```

**攻击盈利公式**

```
攻击者 EOA 签名 → executeMetaTransaction 自调用 setResolver(恶意 resolver)→ DSAuth 自调用绕过 → resolver 被劫持→ 调用 EtherRouter.drain(token, attacker)→ fallback() → 恶意 resolver.lookup(0x837971e4) → 恶意 drain 实现→ delegatecall → drain 中 address(this) == 受害合约→ IERC20(token).balanceOf(受害合约) → IERC20(token).transfer(attacker, balance)= 攻击者获得受害合约持有的全部 ERC20
```

**## 攻击流程

攻击过程仅在一笔交易中完成，所有逻辑在临时攻击合约 0x835a701fd76b96a76ee84de037d41f059ee29f5c 的 constructor 中执行。**

**### 第一阶段：部署恶意基础设施

1. 攻击者 EOA 0xeed236afb6967f74099a0a6bf078bc6b865fbf28 发起交易，创建临时攻击合约 0x835a701fd76b96a76ee84de037d41f059ee29f5c。
2. 攻击合约调用恶意 resolver 0x4e321af09012e15a67756522187c05b108b7ee0a 的 set(bytes4,address)，将 drain(address,address) 的选择器 0x837971e4 映射到恶意 drain 实现 0x0b971e0a8ecc7d5b2465c903cf75aeaedbfc39e2。

### 第二阶段：通过元交易自调用劫持 Resolver

1. 攻击合约调用受害合约 0x5c59d0ec51729e40c413903be6a4612f4e2452da 的 executeMetaTransaction()。由于该函数不在 EtherRouter 自身 ABI 中，调用进入 fallback()，由旧 resolver 路由到元交易实现 0x4e7f1e...。
2. executeMetaTransaction 通过 ecrecover 校验签名，恢复出攻击者 EOA，签名验证通过（攻击者使用的是自己的有效签名，非签名伪造）。
3. executeMetaTransaction 构造自调用 calldata setResolver(0x4e321af...) 并执行 address(this).call(callData)。此时上下文是受害合约，所以 msg.sender == 0x5c59...。DSAuth.isAuthorized() 因 src == address(this) 返回 true，resolver 被成功替换。

### 第三阶段：通过被劫持的 Resolver 清空资产

1. 攻击合约调用受害合约的 drain(USDC, 0xeed236...)。该函数不在 EtherRouter 原生 ABI 中，进入 fallback()。被劫持的 resolver 返回恶意 drain 实现 0x0b971e0...，受害合约对其 delegatecall。恶意代码查询 USDC.balanceOf(0x5c59...) 得到 132704591501（即 132,704.591501 USDC），随后调用 USDC.transfer() 直接转入攻击者 EOA。
2. 攻击合约再次调用 drain(0xf929..., 0x835a701f...)，依相同路径将被盗中间代币 841086343608217839604694 单位转入攻击合约。
3. 攻击合约通过 Router 0x4752ba5dbc23f44d87826276bf6fd6b1c372ad24 将被盗中间代币在 Pair 0x5f6ce0ca... 中 swap 为 1.949506469643782660 WETH，WETH 直接转入攻击者 EOA。**

**### 获利闭合

|  |  |  |
| --- | --- | --- |
| 资产 | 金额 | 流向 |
| USDC | 132,704.591501 | 受害合约 → 攻击者 EOA |
| WETH | 1.9495 | 中间代币 swap → 攻击者 EOA |

## 资金追踪

**通过慢雾 MistTrack 对攻击者 EOA 0xeed236afb6967f74099a0a6bf078bc6b865fbf28 进行地址画像与交易对手分析：

* Gas 来源：攻击者的初始 Gas 由 TornadoCash 提供（地址 0x12d66f87a04a9e220743712ce6d9bb1b5616b8fc ）。
* 恶意标签：MistTrack 已标记该地址为 ShapeShift Exploiter
* 主要痕迹：

+ Relay.link — $4,368.08，DEX 聚合器，用于资产兑换。
+ Tornado.Cash — $218.09，从混币器提取初始 Gas。
+ LI.FI — $137,073.66，跨链/DEX 聚合器。

攻击者盗取的资金流入了Spark.fi Saving，且存在 Tornado.Cash 交互记录，增加了后续追踪的难度。慢雾 MistTrack 将持续监控相关地址的资金动向。**

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCKYLibzteicBXDUBQ5Z9YibTyAGvvxq1HX6tMnhJhGzTdTcW1aKfZaV385ibjZxlicyNZO115CRT9SL0xG8DOOp2qIVlGic5l9DyTZHM/640?wx_fmt=png&from=appmsg)**

## 总结

这次攻击的核心教训是：当合约同时具备「元交易任意自调用」和「自调用自动授权」两套语义时，二者会构成一个完整的权限绕过链——这不是单点代码漏洞，而是跨组件语义冲突的必然结果。 合约开发者在设计元交易或 relay 机制时必须明确划分敏感函数边界，至少在 executeMetaTransaction 中维护一份禁止调用的 selector 列表，并慎用 src == address(this) 的无条件自调用授权。慢雾安全团队建议项目方在部署前进行完整的外部安全审计。**

**往期回顾**

[Shai-Hulud 恶意软件深度剖析：开源即失控 ？](https://mp.weixin.qq.com/s?_...