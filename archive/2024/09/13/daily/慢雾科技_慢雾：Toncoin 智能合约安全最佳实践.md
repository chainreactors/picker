---
title: 慢雾：Toncoin 智能合约安全最佳实践
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500342&idx=1&sn=3c8681b941ccf3f03a308fa32558c327&chksm=fddebcb1caa935a7fa5fbefc2033f84e7a2e95be20db37fb1551459959def7fb0d9150130903&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-09-13
fetch_date: 2025-10-06T18:28:22.247088
---

# 慢雾：Toncoin 智能合约安全最佳实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrN4PLIGaKvqOtbcjCzw8aodHIEMMybOibUIHfvF52wxwQJicW7eutSfWlg/0?wx_fmt=jpeg)

# 慢雾：Toncoin 智能合约安全最佳实践

原创

慢雾安全团队

慢雾科技

TON(The Open Network) 是一个由 Telegram 团队最初设计和开发的去中心化区块链平台，一经上线就获得了关注。TON 的目标是提供一个高性能和可扩展的区块链平台，以支持大规模的去中心化应用(DApps) 和智能合约，关于 TON 的基础知识可查阅[初识 TON：账号、Token、交易与资产安全](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500158&idx=1&sn=7496a1dcfa1326533a145348078bb996&chksm=fddebff9caa936ef22ef30829b17a5e573b4961808b7ea5b1858a014f3058215b02d85485031&scene=21#wechat_redirect)。

值得注意的是，TON 与其他区块链有着截然不同的架构，TON 的智能合约除了主要使用 FunC 语言来编程，也有使用更高级的 Tact，或者更底层的 Fift。这些都是原创程度很高的语言，因此，确保智能合约的安全性很关键。

慢雾安全团队整合吸收了 TON 社区分享的安全开发实践，并结合自身多年积累的安全审计经验，发布「Toncoin 智能合约安全最佳实践」，旨在帮助开发者更好地理解 Toncoin 智能合约的安全风险，并提供实用的解决方案，以降低潜在的安全威胁。

由于篇幅限制，本文仅罗列「Toncoin 智能合约安全最佳实践」的部分内容，欢迎大家在 GitHub 上 Watch、Fork 及 Star：https://github.com/slowmist/Toncoin-Smart-Contract-Security-Best-Practices。

**Toncoin 智能合约常见陷阱**

**1. 缺少 impure 修饰符**

* 严重性：高
* 描述：攻击者可能会发现 "authorize" 函数未标记为 "impure"。缺少此修饰符将允许编译器在函数没有返回值或返回值未使用时跳过该函数的调用。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNSwPPq8umBw415zNzXibZ7XgfR3oxrsbJguk6MJnWlTib4fCcU6KiaJJCA/640?wx_fmt=png&from=appmsg)

* 建议：确保函数使用 "impure" 修饰符。

**2. 错误使用修改/非修改方法**

* 严重性：高
* 描述："udict\_delete\_get?" 被错误地用 "." 而不是 "~" 调用，因此实际的字典未被修改。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNFfPicpOicB0vRpC1QwHAoHB8eKpkpicdngfNZhXO3WPdqw8Dv3928GWmA/640?wx_fmt=png&from=appmsg)

* 建议：始终检查方法是否为修改/非修改方法。

**3. 错误使用有符号/无符号整数**

* 严重性：高
* 描述：投票权被以整数形式存储在消息中。因此攻击者可以在权力转移期间发送负值并获得无限投票权。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNPrSqxbTuHjIWBVAypb76RibnrQfwaQxcnjE939lv4JpxuBGhADrahCw/640?wx_fmt=png&from=appmsg)

* 建议：在一些场景下，无符号整数更安全，因为它们在发生溢出时会抛出错误。仅在确实需要时使用有符号整数。

**4. 不安全的随机数**

* 严重性：高
* 描述：种子来源于交易的逻辑时间，攻击者可以通过暴力破解当前区块中的逻辑时间来获胜（因为逻辑时间在一个区块的边界内是连续的）。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNOKLlTkTeKrhAbbWmIrmsfzgBlUXsvjiaOHevnWOib2eDcWZzLCKzIJ7w/640?wx_fmt=png&from=appmsg)

* 建议：在进行 "rand()" 之前始终随机化种子，最好是永远不要使用链上随机数，因为验证者可以控制或影响种子。

**5. 在链上发送私人数据**

* 严重性：高
* 描述：请记住，所有数据都会被存储在区块链上。
* 攻击场景：钱包受密码保护，其哈希值被存储在合约数据中。然而，区块链会记录一切 —— 密码会出现在交易历史中。
* 建议：不要在链上发送私人数据。

**6. 漏掉对退回消息的检查**

* 严重性：高
* 描述：用户发送 "check" 请求时，Vault 没有退回处理程序或代理消息至数据库。我们可以在数据库中将 "msg\_addr\_none" 设置为奖励地址，因为 "load\_msg\_address" 允许这样做。我们请求 Vault 检查，数据库尝试使用 "parse\_std\_addr" 解析 "msg\_addr\_none"，但解析失败。消息从数据库退回到 Vault，且操作不是 "op\_not\_winner"。
* 攻击场景：Vault 在数据库消息处理器中包含以下代码：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrN0ucAI315cHIkjkibxmtBFN90ttbVXzxwUE0o02ViaJunLiatprVFyib8CQ/640?wx_fmt=png&from=appmsg)

* 建议：始终检查退回的消息，不要忘记标准函数引起的错误，使您的条件尽可能严格。

**7. 在竞争条件下销毁账户的风险**

* 严重性：高
* 描述：不要轻易销毁账户。
* 攻击场景：你可以存钱，然后尝试在并发消息中两次提款。由于无法保证保留资金的消息会被处理，因此合约账号可以在第二次提款后关闭。攻击者之后可以重新部署合约，然后任何人都可以提取未拥有的资金。

  ![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNiaI2MdM1IqHb1gzBib810hOicellBwLXEicw0ZGluDraPxqEdBm6r7egLw/640?wx_fmt=png&from=appmsg)
* 建议：使用 "raw\_reserve" 而不是向自己发送资金。考虑可能的竞争条件。小心使用 hashmap 的气体消耗。

**8. 避免执行第三方代码**

* 严重性：高
* 描述：开发者没有办法在合约中安全地执行第三方代码，因为 CATCH 不能处理 gas 不足的问题，而攻击者只需提交合约的任何状态并引发气体不足即可实现攻击。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNeTcwQwvxx1xZKUpx1yL92w5f8HcA8OKiaynjfbVfRNTM3uiakZVR3LQg/640?wx_fmt=png&from=appmsg)

* 建议：避免在您的合约中执行第三方代码。

**9. 名称冲突**

* 严重性：中
* 描述：Func 变量和函数可能包含几乎任何合法字符。
* 攻击场景："var++"、"~bits"、"foo-bar+baz" 及逗号 "," 都是有效的变量和函数名称。
* 建议：编写和检查 Func 代码时，应该使用 Linter 工具。

**10. 检查 throw 的值**

* 严重性：中
* 描述：每次 TVM 执行正常停止时，它会以退出代码 "0" 或 "1" 停止。虽然它是自动完成的，但如果 "throw(0)" 或 "throw(1)" 命令直接抛出退出代码 "0" 和 "1"，TVM 执行可以在意外方式下直接中断。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNdFHVUD6V0q1fDxPuUOtkbthgJFWULIxU7YP6wFczibVLiaVqs3kjAgSw/640?wx_fmt=png&from=appmsg)

* 建议：不要使用 "0" 或 "1" 作为 throw 的值。

**11. 读/写正确类型数据**

* 严重性：中
* 描述：读取意外变量的值，并在不应有此类方法的数据类型上调用方法（或者其返回值未正确存储）是错误的，不会作为“警告”或“通知”被跳过，而是导致无法取到代码。
* 攻击场景：请记住，存储意外值可能是可以的，但是读取它可能会导致问题。例如，对于整数变量，错误代码 5（整数超出预期范围）可能被抛出。
* 建议：密切跟踪代码的操作和它可能的返回值。请记住，编译器仅关心代码及其初始状态。

**12. 合约代码可以更新**

* 严重性：中
* 描述：TON 完全实现了 Actor 模型，这意味着合约的代码可以更改。代码可以通过 "SETCODE" TVM 指令永久更改，或者在运行时设置 TVM 代码寄存器为新的单元值，直到执行结束。
* 攻击场景：不道德的开发者可能会恶意更新代码以窃取资金。
* 建议：注意合约代码是可以更新的，确保任何更新都遵循安全实践，并使用例如治理模型或多签名批准等机制进行更改。

**13. 交易和阶段**

* 严重性：中
* 描述：计算阶段执行智能合约代码，然后执行操作（如发送消息、修改代码、更改库等）。与基于以太坊的区块链不同，如果你预计发送的消息会失败，你将看不到计算阶段的退出代码，因为消息并不是在计算阶段执行的，而是在稍后的操作阶段执行。
* 攻击场景：在操作阶段消息失败时产生意外行为，导致对交易状态的错误假设。
* 建议：了解每个交易最多包含五个阶段：存储阶段、信用阶段、计算阶段、操作阶段和反弹阶段。

**14. 不能从其他合约中拉取数据**

* 严重性：中
* 描述：区块链上的合约可以驻留在不同的分片上，并由不同的验证者处理。因此，开发者无法按需从其他合约中拉取数据。通信是异步的，通过发送消息进行。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNpXaVtGc7dW0KLv2RDYNOsvEVZxnKWI43Z9gzqiaIFDImichuUtC5Uhnw/640?wx_fmt=png&from=appmsg)

* 建议：围绕异步消息设计合约逻辑，避免对同步数据可用性的假设。

**15. 两个预定义的 method\_id**

* 严重性：中
* 描述：有两个预定义的 method\_id：一个用于接收区块链内的消息 "(0)"，通常命名为 "recv\_internal"，另一个用于接收来自外部的消息 "(-1)"，命名为 "recv\_external"。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrN3liaZGxKLJkQUwfAflyLYc1RGv0z2yU9pCSaUgwcjpP55EJZe58C1vA/640?wx_fmt=png&from=appmsg)

* 建议：使用如 "force\_chain(to\_address)" 的方法来验证地址是否在正确的链上。

**16. 使用可反弹消息**

* 严重性：高
* 描述：TON 区块链是异步的，消息不必按顺序到达。失败的消息应得到正确处理。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNNWNpvXXib1SxGlcH0mCCO82lPeBB9XAkp1icKBibIY0ZiaFPWKEuTr8HDw/640?wx_fmt=png&from=appmsg)

* 建议：始终使用可反弹消息（"0x18"）来正确处理消息失败。

**17. 重放保护**

* 严重性：高
* 描述：为钱包（存储用户资金的合约）实现重放保护，可以使用序列号（"seqno"）来确保消息不被重复处理，或使用带有到期的唯一交易标识符。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNNZ7yfwSKia8GS1eNVicLL0qktDT2kYupQ0ic04OOIwex7xS0EP9ytuqRw/640?wx_fmt=png&from=appmsg)

* 建议：使用类似序列号或消息唯一标识符的重放保护方法，以防止重放攻击。

**18. 消息的竞态条件**

* 严重性：高
* 描述：消息级联可以跨多个区块处理，攻击者可能会启动一个并行流，从而导致竞态条件。
* 攻击场景：攻击者可能会利用时间差异操纵合约行为。
* 建议：通过在每个步骤验证状态并不假设消息流中的状态一致性来预防竞态条件。

**19. 使用携带值模式**

* 严重性：高
* 描述：在代币转账（例如 TON Jetton）中，余额应使用携带值模式进行转账。发送方扣减余额，接收方将其加回或反弹回去。
* 攻击场景：如果处理不当，Jetton 余额可能被操纵。
* 建议：使用携带值模式以确保正确的值转移。

**20. 小心退还多余的燃料费**

* 严重性：高
* 描述：如果未将多余的燃料费退还给发送者，资金可能会随着时间的推移在合约中积累。原则上，这并不可怕，但这是一种次优的做法。可以添加一个功能来清除多余的费用，但像 TON Jetton 这样的流行合约仍然会向发送者返回多余的费用消息 "op::excesses"。

**21. 检查函数返回值**

* 严重性：高
* 描述：函数总是会返回值或错误，如果忽略对返回值的检查，可能会导致逻辑上的致命错误。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNLFba1t6BDSSrQFMkrSSAvEHqpFtY5icepHBibMqk5cn7UvFtyy0nBgrg/640?wx_fmt=png&from=appmsg)

* 建议：始终检查函数的返回值。

**22. 检查假冒的 Jetton 代币**

* 严重性：高
* 描述：Jetton 代币由两部分组成："jetton-minter" 和 "jetton-wallet"。如果保险库合约没有正确验证，攻击者可能会通过存入假代币并提取有价值的代币来耗尽保险库中的资金。
* 攻击场景：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYlJHS3IIe8JmPFricXZymrNYA7xeBcQKw4wwNicIjDib0Me1aNT67kicIuibic3pULibNojysn0P9VvnBmQ/640?wx_fmt=png&from=appmsg)

* 建议：通过计算用户的 jetton 钱包地址，检查发送者是否发送了假冒的 Jetton 代币。

**写在最后**

对开发者而言，遵循这些最佳实践，可以有效提升智能合约的安全性，减少潜在的安全风险。在区块链技术日新月异的今天，安全永远是重中之重。希望这一最佳实践可以帮助更多的开发者打造安全可靠的智能合约，推动区块链技术的健康发展。

**参考链接：**

[1] https://dev.to/dvlkv/drawing-conclusions-from-ton-hack-challenge-1aep

[2] https://docs.ton.org/develop/smart-contracts/security/ton-hack-challenge-1

[3] https://docs.ton.org/learn/tvm-instructions/tvm-overview

[4] https://docs.ton.org/develop/smart-contracts/messages

[5] https://docs.ton.org/develop/smart-contracts/security/secure-programming

[6] https://docs.ton.org/develop/smart-contracts/security/things-to-focus

作者 | Johan

编辑 | Lisa

排版 | Liz

**往期回顾**

[慢雾出品 | Web3 项目安全手册](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500304&idx=1&sn=4907efb9509e7e555ad6c8bbc0094f65&chksm=fddebc97caa93581bad6bf8a23f9ae6ab95e80ffcaa5a687a1a416a38f5e2baa50f358910b3b&scene=21#wechat_redirect)

[Web3 安全入门避坑指南｜貔貅盘骗局](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500277&idx=1&sn=b1cfdb0c440c56b433b896725ff84c8d&chksm=fddebf72caa936645ea0bb960b45f65cc9c6462865b50523f65065f415348b22f3cc6fd83bf1&scene=21#wechat_redirect)

[观点｜国际合作执法将成打击加密货币犯罪的大趋势](http://mp.weixin.qq.com...