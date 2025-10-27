---
title: 探索 Sui：高性能背后的技术与合约安全
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500228&idx=1&sn=195ae5a2f3856f0f9d4423361c32901c&chksm=fddebf43caa93655f65f77eb70477de461132ad38bf01408a54504c042e941d447ba87fc7a4d&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-09-04
fetch_date: 2025-10-06T18:28:20.986419
---

# 探索 Sui：高性能背后的技术与合约安全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZFbh40PMMgMRBGUleMrx6gkMdaYuVYybkEUv00dau3FfDG0ccvuaXPfzUVmAaPL82Q8EMAiaH40PA/0?wx_fmt=jpeg)

# 探索 Sui：高性能背后的技术与合约安全

原创

慢雾安全团队

慢雾科技

By: Johan & Victory!

##

## **背景**

前段时间，我们在[初识 TON：账号、Token、交易与资产安全](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500158&idx=1&sn=7496a1dcfa1326533a145348078bb996&chksm=fddebff9caa936ef22ef30829b17a5e573b4961808b7ea5b1858a014f3058215b02d85485031&scene=21#wechat_redirect)中讨论了 TON 的特点及用户资产安全问题。今天，我们一起来学习另一个新兴的高性能区块链平台 —— Sui，它具备多项创新技术和独特特性，吸引了开发者和研究人员的关注。Sui 专注于提供快速、安全的交易体验，适合各种应用场景。本篇文章将通过讲解 Sui 的账号模型、代币管理、交易机制和资产安全等内容，帮助读者认识 Sui。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZFbh40PMMgMRBGUleMrx6g1LN2lGgGjKPLSGHc7mxnHGF7AQiczbRgPibvnHc6bpZctEkGG2UflkwA/640?wx_fmt=png&from=appmsg)

## **账号模型**

###

### **地址**

Sui 遵循加密货币行业中广泛接受的钱包规范，包括 BIP-32（及其变种 SLIP-0010）、BIP-44 和 BIP-39，以便为用户提供密钥管理。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZFbh40PMMgMRBGUleMrx6g3xOtLXWHdX5MXXbUSgHfu3xVPkys5Og0icq1x5KWxjkoYOmmaLAeDibA/640?wx_fmt=png&from=appmsg)

为了派生一个 32 字节的 Sui 地址，Sui 使用 BLAKE2b（256 位输出）哈希函数将签名方案标志（1 字节）与公钥字节连接起来。Sui 地址当前支持纯 Ed25519、Secp256k1、Secp256r1 和 MultiSig，对应的标志字节分别为 0x00、0x01、0x02 和 0x03。

### **余额**

在 Sui 上，一切都是对象，用户的余额也是对象。在转账过程中，如果对象中包含的余额不等于需要的数值，则需要将对象拆分或合并。例如，你有一个包含 100 SUI 的对象，但你只想转账 30 SUI，那么系统会将这个对象拆分为两个对象：一个包含 30 SUI，另一个包含 70 SUI。你可以转移包含 30 SUI 的对象，而保留剩下的对象。反之，如果需要更大的数额，你也可以将多个余额对象合并，形成一个更大的数额对象。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZFbh40PMMgMRBGUleMrx6gmyxTFkLY31ibcNiadE9GwibpMBF9hFBNCC1OG0rH040nKRalaUibNneyLQ/640?wx_fmt=png&from=appmsg)

## **代币管理**

Sui 官方实现了 Coin 的标准代码，开发者在发行 Coin 时只需要在合约里调用 `use sui::coin;` 就可以使用这个标准库的所有功能。

由于使用了 Move 语言，与其他区块链常用的编程语言（如 Solidity）有所不同，开发者在使用时需要了解并注意一些独特的功能或特性，我们来看一段代码：

```
module regulated_coin_example::regulated_coin {    use std::option;
    use sui::coin;    use sui::coin::{TreasuryCap};    use sui::transfer;    use sui::tx_context::{Self, TxContext};
    struct REGULATED_COIN has drop {}        fun init(otw: REGULATED_COIN, ctx: &mut TxContext) {        let (treasury_cap, deny_cap, meta_data) = coin::create_regulated_currency(            otw,            5,            b"tUSD",            b"Test USD",            b"Example Regulated Coin",            option::none(),            ctx        );
        let sender = tx_context::sender(ctx);        transfer::public_transfer(treasury_cap, sender);        transfer::public_transfer(deny_cap, sender);        transfer::public_transfer(meta_data, sender);    }
    public fun mint(        treasury_cap: &mut TreasuryCap<REGULATED_COIN>,         amount: u64,         recipient: address,         ctx: &mut TxContext,    ) {        let coin = coin::mint(treasury_cap, amount, ctx);        transfer::public_transfer(coin, recipient)    }}
```

这是一个完整的 Coin 发行合约，Sui 上的智能合约设计与以太坊或 Solana 等区块链平台有所不同，我们在源代码中看不到权限的管理。使用该函数创建 Coin 时(coin::create\_regulated\_currency)，合约的创建者会收到一个 TreasuryCap 对象，该对象是铸造新 Coin 或销毁现有 Coin 所必需的。只有有权访问此对象的地址才能维护 Coin 发行。

对于收到 Coin 的用户来说，他的账号控制了这些代币的所有权，在调用智能合约使用这些代币时，也需要传入这些对象，并对交易进行签名。

##

## **交易机制**

交易是基本的区块链世界中的概念，它是与区块链交互的一种方式。交易用于更改区块链的状态，并且是唯一的方法。在 Sui 使用的 Move 编程语言中，交易用于调用包中的函数、部署新包以及升级现有包。

在构建交易时需要注意，每笔交易要明确地指定其操作的对象！这点和 Solana 的交易需要传入账号有一些相似。

交易包含的内容：

* 发送方 -- 签署交易的账户
* 指令列表（或指令链）-- 要执行的操作
* 命令输入 -- 命令的参数：纯文本 -- 简单的值，如数字或字符串，或对象 -- 交易将访问的对象
* Gas 对象 -- 用于支付交易的 Coin 对象
* Gas 价格和预算 -- 交易成本

##

## **合约安全**

Sui 使用 Move 做为智能合约的编程语言，在一定程度上能解决 Solidity 高发的漏洞问题，如重入攻击、整数溢出、双花、DoS 攻击和编译器问题，但避免不了开发者在代码中引入错误，因此安全审计依旧是必要的。以下是开发者在开发过程中需要注意的一些事项：

**1. 权限检查：**分析对外函数所接收的对象类型，对于涉及敏感操作的特权函数，需要确保传入的对象是具有特权的对象。如果函数接收并使用了特权对象，那么函数调用者必须是该对象的合法拥有者。

**2. 对外函数检查：**有些函数本身不应该被外部直接调用，如果有不应该外放的函数接口，开发者要提出该函数不宜公开。

**3. 对象分析检查：**由于 Sui 里面的对象可以被转成公共对象(Shared Object)，因此，开发者要整理出所有用到的对象的类型，确认它们是静态的还是公共的，以及是否存在错误。如果把应该私有化的对象转换成了公共对象，那么任何人都可以使用这个对象，这就存在安全风险。

**4. Coin 消耗检查：**Sui 的代币模型与其他链的有所不同，其设计允许代币对象可以被其他对象包含和持有，还可以进行拆分，由此衍生出了几种代币消耗模式：

* 直接将代币对象转移给另一个对象；
* 将代币对象进行结构调整后生成一个新的对象，再转移给目标对象；
* 将代币对象拆分，并将拆分出来的部分转移给新对象。

因此，在代币消耗的情况下，开发者需要检查以下几点：

* 消耗的金额是否正确；
* 对象是否已经转移；
* 如果有拆分，拆分的数额对不对。

**5. 预言机价格操纵攻击：**如果 Sui 上的合约使用预言机来获取价格，那么也需要注意价格被操纵的可能性。开发者可以通过引入多个数据源和共识机制，以防范单一数据源被操纵的风险。此外，还可以使用时间加权平均价格来防范预言机操纵风险。

**6. 治理攻击：**在 Sui 上的合约中，如果治理代币的投票权设计不合理，也存在遭遇治理攻击的风险，这方面可以参考一些成熟的去中心化组织的社区治理逻辑。

**7. 套利攻击：**如果逻辑设计不合理，Sui 上的 DeFi 合约也存在套利攻击的风险。开发者在开发的时候应仔细审查合约中的逻辑，避免被攻击者利用。

**8. 假充值攻击：**交易所或开发者在处理 Sui 代币充值时，还需要注意检查交易的状态是否成功，代币的 Package ID 是否正确，防范假充值攻击。

##

## **总结**

在本文中，我们简单探讨了 Sui 的设计特点，包括其账号模型、代币管理、交易机制以及合约安全性。利用 Move 编程语言，Sui 在确保高性能与低延迟的同时，还引入了创新的数据模型和对象存储方法，显著提升了安全性和灵活性。相比其他区块链平台，Move 语言在防止常见的智能合约漏洞（如溢出、重入攻击等）方面表现出色，这使得 Sui 在技术层面上更加稳健和可靠。然而，开发者仍需关注业务逻辑层面的安全性，特别是在权限管理、对象类型的使用以及代币消耗方面，谨防由于代码中的错误或不当设计而导致资产损失。

**参考链接：**

https://docs.sui.io/

https://docs.sui.io/standards/coin

https://move-book.com/

**往期回顾**

[每月动态 | Web3 安全事件总损失约 3.16 亿美元](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500217&idx=1&sn=3d0739b9da5b1aa080541b5a9bdca7d7&chksm=fddebf3ecaa93628158db7785c0fd8fda98a198ced9dc704c38810535b002d26441fbae9b7e0&scene=21#wechat_redirect)

[Web3 安全入门避坑指南｜假矿池骗局](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500196&idx=1&sn=897d51b7228f0f97045472e157d051b1&chksm=fddebf23caa93635e642d8828d054a361da7ae3d90918ea9b9e1b58eb500fd0395b36178607e&scene=21#wechat_redirect)

[慢雾(SlowMist) 创始人受邀出席 2024 外滩大会，共探 Web3 新发展](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500185&idx=1&sn=c1de17fad9e6c1c8d4e1fc710ffb5a8a&chksm=fddebf1ecaa9360898a6f90504211d1273e08db2285414dc45711b1e8ff102f1a95738204b32&scene=21#wechat_redirect)

[Web3 安全入门避坑指南｜空投骗局](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500174&idx=1&sn=e3cb8f76396b64e8dd23bbcdc1a24bcd&chksm=fddebf09caa9361fef844c27d8b8b4360cac62f2fb5f3b8b9fe83f1cfa44de95311a62915f8d&scene=21#wechat_redirect)

[初识 TON：账号、Token、交易与资产安全](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500158&idx=1&sn=7496a1dcfa1326533a145348078bb996&chksm=fddebff9caa936ef22ef30829b17a5e573b4961808b7ea5b1858a014f3058215b02d85485031&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8Togv4VUdq4r7iak19Hta2pfbzPrGohPNR71WxPKrBoK9nyibPVL7ssCuW3yA/640?wx_fmt=png)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过