---
title: 慢雾：Sui - Move 合约审计入门
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500411&idx=1&sn=a9bd3a971824eb5bdb342a54e6da1782&chksm=fddebcfccaa935ea03d21c459875d19309c50a4822337c62f7285e0c9136698c750ee2584eb2&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-09-28
fetch_date: 2025-10-06T18:28:04.763947
---

# 慢雾：Sui - Move 合约审计入门

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZo8U1ibh7pFfe8vvDU5wBZKYKgoiavPZofljwxiasqqaBCHcdclw67pACia9t620VJsLFSibibRl0Vguzg/0?wx_fmt=jpeg)

# 慢雾：Sui - Move 合约审计入门

原创

慢雾安全团队

慢雾科技

Sui 作为一个新兴的高性能区块链平台，具备多项创新技术和独特性，同时专注于为各种应用场景提供快速、安全的交易体验。关于 Sui 的基础知识可查阅[探索 Sui：高性能背后的技术与合约安全](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500228&idx=1&sn=195ae5a2f3856f0f9d4423361c32901c&chksm=fddebf43caa93655f65f77eb70477de461132ad38bf01408a54504c042e941d447ba87fc7a4d&scene=21#wechat_redirect)。与其他区块链常用的编程语言（如 Solidity）有所不同，Sui 使用 Move 语言，在一定程度上能解决 Solidity 高发的漏洞问题，如重入攻击、整数溢出、双花、DoS 攻击和编译器问题，但避免不了开发者在代码中引入错误。因此，开发者在使用时需要了解并注意一些独特的功能或特性，确保智能合约的安全性。

慢雾安全团队整合吸收了 Sui 社区分享的安全开发实践，并结合自身多年积累的安全审计经验，发布 Sui - Move 合约审计入门，旨在帮助开发者更好地理解 Sui 智能合约的安全风险，并提供实用的解决方案，以降低潜在的安全威胁。

由于篇幅限制，本文仅罗列 Sui - Move 合约审计入门的部分内容，欢迎大家在 GitHub 上 Watch、Fork 及 Star：https://github.com/slowmist/Sui-MOVE-Smart-Contract-Auditing-Primer/blob/main/README\_CN.md。

## **关键知识点**

**1. 模块声明和可见性**

1.1 "public(friend)" 函数（在最新的 Sui 版本中 "public(friend)" 被替换成 "public(package)"）

定义：用于声明函数，使其只能被指定的友元模块访问。这提供了更细粒度的访问控制，介于 "public" 和 "private" 之间。

示例：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZo8U1ibh7pFfe8vvDU5wBZK7mTtLJ72L52cxeSh7PeqL2picuiaiaeVw8iabFwzHu9LBRrdaiaJ8theqFg/640?wx_fmt=png&from=appmsg)

1.2 "entry" 函数

定义："entry" 函数是模块的入口点，允许从事务块中直接调用。参数必须来自事务块的输入，不能是块中先前事务的结果或被修改的数据。此外，"entry" 函数只能返回具有 "drop" 能力的类型。

示例：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZo8U1ibh7pFfe8vvDU5wBZKxMBM8YjH6yZl6rXmdMPRava0DuxvqibXL5UlrO56zibib6RUV4UMmLJKA/640?wx_fmt=png&from=appmsg)

1.3 "public" 函数

定义："public" 函数可以从事务块和其他模块调用，适合外部交互。在参数和返回值上没有和 "entry" 函数一样的限制，通常用于将功能暴露给外部。

示例：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZo8U1ibh7pFfe8vvDU5wBZKBFocsBzhIicqibmiaGMfR4juKW73AY9EUWSrxYuRiaccCPSMIOX0CNoIDw/640?wx_fmt=png&from=appmsg)

**2. 对象管理**

2.1 对象的唯一性

定义：每个 Sui 对象都有唯一的 "objID"，确保了对象在链上的唯一性。

2.2 包装和解包

定义：

* 直接包装：将一个 Sui 对象作为另一个对象的字段，解包时必须销毁包装对象。
* 对象包装：包装后的对象成为另一对象的一部分，不再独立存在。解包后对象的 ID 不变。

2.3 自定义转移策略

定义：使用 "sui::transfer::transfer" 定义自定义转移策略，针对具有 "store" 能力的对象，可以通过 "sui::transfer::public\_transfer" 创建。

2.4 对象的属性

定义：Sui 对象的属性包括 "copy", "drop", "store", 和 "key"，这些属性决定了对象的行为方式。

2.5 对象的权限检查

* Address-Owned Objects

定义：由特定地址（账户地址或对象 ID）拥有的对象，只有对象的所有者可以访问和操作这些对象。

* Immutable Objects

定义：不可变对象无法被修改或转移，任何人都可以访问。适用于需要全局访问但不需要修改的数据。

* Shared Objects

定义：共享对象可以被多个用户访问和操作，适用于去中心化应用等场景，但由于需要共识，操作成本较高。

* Wrapped Objects

定义：包装对象是将一个对象嵌入另一个对象，包装后的对象不再独立存在，必须通过包装对象访问。

**3. 安全性检查**

3.1 数值溢出检查

Sui 的智能合约默认进行数值溢出检查。

3.2 重入检查

所谓的重入攻击是在一笔正常的合约调用交易中，被插入一笔非预期的（外部）调用，从而改变整体的业务调用流程，实现非法获利的行为。涉及到外部合约调用的位置，都可能存在潜在的重入风险。目前的重入问题我们可以分为三类：单函数重入、跨函数重入以及跨合约重入。Move 语言的一些特性为防范重入攻击提供了天然的保护：

* Move 中无动态调用，其外部调用都需先通过 use 进行导入，即外部调用都是预期、确定的。
* 无 Native 代币转账触发 Fallback 功能。
* 在 Move 中，资源模型确保资源一次只能由单个执行上下文访问。这意味着如果函数执行未完成，则在执行完成之前其他函数无法访问同一资源。

##

## **审计入门**

**1. 溢出审计**

说明：Move 进行数学运算时会进行溢出检查，运算溢出的话交易将失败。但需要注意的是，对于位运算，Move 并不会进行溢出检查。

定位：寻找代码中进行位运算的位置，检查是否有溢出风险。

**2. 算术精度误差审计**

说明：Move 中没有浮点类型。因此，在进行算术运算时，如果运算结果需要以浮点数表示，可能会产生精度误差。虽然精度误差在某些情况下难以完全避免，但可以通过优化和合理设计来减轻其影响。

定位：审查代码中所有涉及算术运算的部分，特别是可能产生精度误差的计算，确保这些运算不会对合约逻辑或数值准确性产生负面影响，并提出优化建议以减轻精度误差。

**3. 条件竞争审计**

说明：Sui 中的验证者也可以对用户提交的交易进行排序，因此在审计中我们仍需要注意在同一个区块中对交易进行排序而获利的问题。

定位：

* 是否有对函数调用前合约的数据状态进行预期管理。
* 是否有对函数执行中的合约数据状态进行预期管理。
* 是否有对函数调用后的合约数据状态进行预期的管理。

**4. 访问控制审计**

说明：合约中的某些关键函数应仅限于内部调用，例如能够直接更新用户存款数额的函数。如果这些函数不慎对外部开放，可能绕过权限控制，导致安全漏洞，甚至引发资产损失。因此，必须严格设置访问权限，确保只有授权角色或模块可以调用这些函数，或者确保函数只能在内部使用。

定位：需要检查所有函数的访问控制设置，特别是那些不应该对外公开的函数，确保它们只能在内部调用。如果发现不应暴露的函数接口已经公开，必须标记为高风险并提出修正建议。

**5. 对象管理审计**

说明：在 Sui 中，对象可以被转换为共享对象 (Shared Object)，这意味着对象的访问权限可能从私有变为公共。因此，需要对所有使用的对象进行详细审查，明确每个对象是静态的还是共享的。特别要注意是否有对象被错误地从私有对象转换为共享对象，这样可能导致未经授权的用户访问这些对象，带来潜在的安全风险。

定位：整理并分析模块中所有涉及的对象，检查对象的类型和权限设置，确保该对象的权限与业务需求匹配。如果发现私有对象被错误地转换为共享对象，必须标记为潜在风险并提出修正建议。

**6. Token 消耗审计**

说明：Sui 的代币模型与其他链的代币模型有所不同。Sui 允许对象持有代币，并且代币对象可以嵌套在其他对象中，还可以进行拆分。因此，在涉及代币消耗的场景中，需要特别关注代币的管理和流转，以避免安全问题或意外损失。

定位：

* 检查消耗的金额是否准确。
* 检查代币对象是否已经正确转移。
* 检查代币的拆分和合并是否合理。
* 检查代币与对象的绑定。

**7. 闪电贷攻击审计**

说明：Sui 的 Move 也有闪电贷的用法(Hot Potato)。用户可以在一笔交易中借取大量的资金任意使用，只需在这笔交易内归还资金即可。恶意用户通常使用闪电贷放大自身的资金规模进行价格操控等大资金攻击。

定位：分析协议本身的算法（奖励、利率等）及预言机依赖是否合理。

**8. 权限漏洞审计**

说明：在 Sui 的 Move 合约中，权限漏洞这部分和业务的需求以及功能设计关系较大，所以遇见较为复杂的 Module 时，需要和项目方确认各个方法的调用权限（这里的权限一般是指函数的可见性和函数的调用权限）。

定位：

* 检查和确认所有函数方法的可见性及调用权限，在项目评估阶段就需要项目方提供设计文档，审计时根据设计文档中的描述从而确认权限。
* 梳理项目方角色的权限范围，如果项目方角色的权限会影响用户的资产，则存在权限过大的风险。
* 分析对外函数里面传递进去的对象是什么类型，如果是一些特权函数，则必须要有一些特权对象参与。

**9. 合约升级的安全审计**

说明：在 Move 中，外部模块通过 use 关键字导入。需要注意的是，Sui 的合约是可升级的，但发布的合约包(package) 是不可变的对象，一旦发布就无法撤回或修改。合约升级的本质是通过在新的地址上重新发布更新的合约，并将旧版本合约的数据迁移至新的合约中。因此，合约升级过程中需要特别注意：

* "init" 函数："init" 函数仅在合约第一次发布时执行，后续合约升级时不会再次触发。
* 升级合约不会自动更新依赖：如果合约包依赖于外部包，当外部包升级时，合约包不会自动指向升级后的合约地址。因此，需要手动升级自己的合约包以指定新的依赖项。

定位：需要对合约升级过程中数据迁移的逻辑进行详细检查，确保迁移操作安全、准确，并避免遗漏重要数据或依赖更新的问题。

**10. 外部调用安全审计**

说明：与外部模块使用审计项相同，由于 Move 中进行外部调用需要先将外部模块导入，因此理论上外部调用的结果都是开发人员所预期，所需主要的是外部模块的稳定性。

定位：需要对外部引入的库进行检查。

**11. 返回值的检查**

说明：和其他智能合约语言类似，在 Move 合约中，需要对某些函数的返回值进行检查。如果忽略了对这些返回值的处理，可能会导致关键逻辑没有正确执行，进而引发安全问题。

定位：需要检查代码中每个函数调用的返回值，特别是那些涉及外部调用或重要状态更新的函数。如果返回值未被处理或验证，可能会导致不可预期的行为，应该标注为潜在风险点。

**12. 拒绝服务审计**

说明：拒绝服务(DoS) 攻击可能由代码逻辑错误、兼容性问题或其他安全漏洞引发，导致智能合约无法正常运行。此类问题可能影响合约的可用性，甚至使其完全瘫痪。

定位：

* 重点检查业务逻辑的健壮性，确保在各种情况下都能正常执行，不会因错误或漏洞导致合约中断。
* 关注与外部模块交互的部分，确保其兼容性，以防止由于外部依赖问题导致的服务中断。

**13. Gas 优化审计**

说明：与以太坊一样，Sui 也有 Gas 机制，任何模块脚本调用都会消耗 Gas。因此对一些冗长且高复杂度的代码进行优化是有必要的。

定位：

* 涉及到复杂的调用看是否可以解耦。
* 涉及到高频率的调用看是否可以优化函数内部执行的效率。

**14. 设计逻辑审计**

说明：设计逻辑审计的重点是检查代码中的业务流程和实现，确认是否存在设计缺陷或与预期不符的情况。代码实现如果与预期逻辑不一致，可能会导致意外的行为或安全风险。

定位：

* 根据不同角色的权限和作用范围，梳理业务流程中的可能调用路径。
* 确定每个业务流程所涉及的数据范围，确保数据的操作与业务设计一致。
* 将实际的调用路径与预期的业务流程进行比较，识别并分析任何可能导致非预期结果的调用情况。

**15. 其他**

未在上述表述中体现的内容。

##

## **写在最后**

对开发者而言，遵循这些最佳实践，可以有效提升智能合约的安全性，减少潜在的安全风险。希望这一最佳实践可以帮助更多的开发者打造安全可靠的智能合约，推动区块链技术的健康发展。

**参考：**

[1] https://intro.sui-book.com/

[2] https://docs.sui.io/

[3] https://move-dao.github.io/move-book-zh/introduction.html

作者 | Victory!

编辑 | Lisa, Liz

**往期回顾**

[报告解读｜FBI 发布 2023 年加密货币欺诈报告](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500371&idx=1&sn=0ca64fc5fb738f708f356eb36d0a2552&chksm=fddebcd4caa935c2e13981ab968ee71d08200546d133a886313dbbacf788f5cf016b72078291&scene=21#wechat_redirect)

[慢雾：Toncoin 智能合约安全最佳实践](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500342&idx=1&sn=3c8681b941ccf3f03a308fa32558c327&chksm=fddebcb1caa935a7fa5fbefc2033f84e7a2e95be20db37fb1551459959def7fb0d9150130903&scene=21#wechat_redirect)

[慢雾出品 | Web3 项目安全手册](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500304&idx=1&sn=4907efb9509e7e555ad6c8bbc0094f65&chksm=fddebc97caa93581bad6bf8a23f9ae6ab95e80ffcaa5a687a1a416a38f5e2baa50f358910b3b&scene=21#wechat_redirect)

[Web3 安全入门避坑指南｜貔貅盘骗局](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500277&idx=1&sn=b1cfdb0c440c56b433b896725ff84c8d&chksm=fddebf72caa936645ea0bb960b45f65cc9c6462865b50523f65065f415348b22f3cc6fd83bf1&scene=21#wechat_redirect)

[观点｜国际合作执法将成打击加密货币犯罪的大趋势](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500259&idx=1&sn=21387da04ed0f8530bb29c034818e125&chksm=fddebf64caa9367207ace3aebd169af612da04daf1c2fd69163f3d838aac13eba8c7a5268db9&scene=21#wechat_redirect)

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

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4...