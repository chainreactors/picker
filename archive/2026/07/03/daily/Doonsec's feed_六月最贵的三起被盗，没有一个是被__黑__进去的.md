---
title: 六月最贵的三起被盗，没有一个是被\"黑\"进去的
url: https://mp.weixin.qq.com/s/nUZokRYvY2b95zwLQKgakA
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:40:33.485003
---

# 六月最贵的三起被盗，没有一个是被\"黑\"进去的

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2ibKZs4HxyquSeQLZUwXvD6XTbeX1SH1Uz2khicH7pXiaeGxzwtDwE5icMYGNFXhkNoMUOwVqTz0iasp2tczohiaOehAAHG84UHtBzJBeudd6rtl8/0?wx_fmt=jpeg)

# 六月最贵的三起被盗，没有一个是被"黑"进去的

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ibKZs4HxyqtrINeL1FoibOOxykzibTibs4WCaM5Ibic6hNIZ1uBiaHH4rX1VQyPibX0Fibz498oldQ7Xow2mFxlDvZwOM2BvxKJtegmXLDWiabDFtmw/640?wx_fmt=gif&from=appmsg)

# 六月三大安全事件

六月最大的三起事件并非源于某个单一漏洞，而是暴露了一种共通的失误：表面上完好的安全保障，实际上从未被真正落实。MEV bot 信任了"看起来有利可图"的交易，却没有确认授权额度是否真的被消耗。两个仍留有资金的旧版 Rollup 接受了形式上有效的证明，却从未把证明与它本应代表的结算状态真正绑定。一个钱包的签名代码悄悄漏掉了安全性所依赖的那个秘密输入，使本应无法预测的值，变成任何人都能从公开数据反推出来的东西。这些协议都不是被硬破解的密码学攻破的，而是被一个从没有人真正核实过的假设攻破的。

# JaredFromSubway：约 1500 万美元

2026 年 6 月 20 日，以太坊上知名的 MEV bot 运营者 JaredFromSubway 在一次蜜罐攻击中损失约1500 万美元。

攻击者搭建了一个仿真的交易环境，包括伪造的 wrapper 合约、伪造的 Uniswap V2 风格交易池。这些交易池在调用 swap() 时会发出真实的 Sync 和 Swap 事件，与合法交易无法区分。在合法交易中，wrapper 合约的 wrapTo() 函数内部本应调用真实代币的 transferFrom()，以消耗 bot 此前授予的额度。然而，伪造的 wrapper 代币合约却完全跳过了这一步，同时仍通过 unwrap()返回一笔精心构造的小额利润。由于机器人从未核实授权额度是否真正被消耗，也没有撤销剩余授权，未被使用的授权额度逐渐累积，最终被攻击者通过 withdraw() 一次性收割。其中一个受影响的钱包损失约  750 万美元。JaredFromSubway [1] 后来公布的受影响钱包总损失约为 1500 万美元。

这次事件的教训是，即使模拟交易显示有利可图，MEV bot 也必须把未知的代币和资金池代码视为潜在的敌意代码。自动化策略需要严格的授权对象白名单、代码哈希校验、交易后授权额度核查，以及对剩余授权的及时清理。

Aztec Rollup 事件：约 435 万美元

2026 年 6 月，两个独立的 Aztec 遗留部署先后遭到攻击，合计造成约 435 万美元损失。两起事件的根本原因不同，但都发生在零知识证明的有效性与 L1 结算语义之间的边界。

第一起攻击 [2] 发生在 6 月 14 日，针对 Aztec Connect 的 RollupProcessorV3，造成约 215 万美元损失。在漏洞合约中， numTxs 参数决定了 L1 结算循环需要处理的存款交易数量，攻击者将其设置为 1，同时在后续才会被解码的交易槽位中植入了一笔真实存款。ZK 证明电路仍会在内部处理该槽位并将其计入余额，但 L1 结算循环仅按 numTxs = 1 迭代一次，因此未对该笔存款调用 decreasePendingDepositBalance()，其待处理存款余额也就未被相应扣减。由于这笔存款在 L1 侧从未被正式核销，攻击者随后通过正常提款流程，将这笔未被抵押的余额提走。

第二起攻击 [3] 发生在 6 月 18 日，针对另一个独立的遗留 PrivateRollupBridge / RollupProcessor 部署，造成约 220 万美元损失。该部署仍然保留着本应废弃的 escapeHatch() 接口，而相应的电路缺少关键约束。这让攻击者得以在一棵伪造的私有树中证明自己拥有高价值票据，同时对外公布真实的 L1 dataRoot 作为公开根。链上的 Verifier 接受了该证明，L1 合约随即执行了提款。

这两起事件共同说明，仅有证明验证是不够的。所有决定结算边界的数值，都必须与证明所验证的公开输入严格绑定。而所有代表 L1 状态的私有见证，也都必须被明确约束为与结算实际使用的公开状态一致。

SecondFi：约 240 万美元

2026 年 6 月 23 日，EMURGO 旗下的浏览器插件钱包 SecondFi（原名 Yoroi）披露了其 Ed25519 签名实现中的一个严重漏洞，影响 v10.0.3 到 v10.0.6 版本。

存在漏洞的代码只用公开的交易消息计算签名随机数，遗漏了本该加入的私密前缀。这让签名方程变成只有一个未知数，任何人都能直接从链上公开数据反推出钱包私钥。两名攻击者各自独立利用了这个漏洞，从 374 个钱包中卷走约 240 万美元（1600 万 ADA），EMURGO 随后抢救回另外 1.29 亿 ADA。

这次事件的教训是，钱包签名代码需要和协议层加密算法一样严格的审查。哪怕只是遗漏一个看似不起眼的隐私输入，也足以让私钥完全暴露，因此自定义的 Ed25519 实现应该经过独立审计，而不能被默认当作标准库那样可靠。

彩蛋：Zcash Orchard 健全性漏洞

Zcash Orchard 健全性漏洞因为目前尚未确认到实际利用，未能进入前三名，但它仍是六月最重要的漏洞披露之一。 该漏洞源于 Orchard 屏蔽资金池电路中缺失的一个等式约束，理论上可能导致同一张屏蔽票据生成不同的 nullifier，从而被多次花费。这个缺陷自 2022 年 5 月 Orchard 激活以来就一直存在，而在 2026 年 6 月才被发现，最终通过 NU6.2 紧急升级得到修复。

这起事件再次印证了 Aztec 事件所揭示的更深层教训：在 ZK 系统中，安全性取决于电路实际约束了什么，而非周边协议假设它约束了什么。

阅读关于漏洞的深度分析：[七天蒸发四成，全因一个藏了四年的错误](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247492229&idx=1&sn=9ca872e60f4ca7330148dd958c0a743d&scene=21#wechat_redirect)

以上内容基于截至 2026年7月1日 00:00（UTC） 的公开信息整理。

参考链接

[1] JaredFromSubway 的事件声明：

https://x.com/jaredsmev/status/2069482824055521356

[2] Aztec 关于第一次攻击的官方声明：https://x.com/AztecLabs\_/status/2066175340926345555

[3] Aztec 关于第二次攻击的官方声明：https://x.com/AztecLabs\_/status/2067511785637163354

[4] SecondFi 事件的官方声明：https://x.com/secondfiapp/status/2069306133337227382

[5] ZCash Orchard 漏洞技术分析：

[七天蒸发四成，全因一个藏了四年的错误](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247492229&idx=1&sn=9ca872e60f4ca7330148dd958c0a743d&scene=21#wechat_redirect)

---

使用 Phalcon Security APP防范DeFi攻击

面对频发的DeFi安全威胁，BlockSec Phalcon 为协议提供实时监控和自动阻断能力。

![图片](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTKawosatk2Qj3FEREfIFVg7PbLIV56BvalRnPUlPkyJCGa9rP3MicUO6r5X6rd3BT3ZHdBb9kuPH3w/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

已有500亿美元资产在Phalcon保护下安全运行。

我们成功阻止了20+真实世界的黑客攻击，挽救了超过2000万美元的资产。想知道如何用 Phalcon Security 防范这类 DeFi 攻击？点击下方视频号，get 详细教学内容，快速掌握安全防护核心技巧👇

点击文章左下角「阅读原文」或访问下方链接，10秒完成预约，前30位预约用户可申请免费试用！

🔗 访问官网：

https://blocksec.com/phalcon/security

🔗 预约演示：

https://blocksec.com/expert-contact

---

关于BlockSec

BlockSec 是全球领先的区块链安全和合规公司，于 2021 年由多位业内知名专家联合创立。BlockSec 致力于提升 Web3 世界的安全性和易用性，提供一站式安全服务，包括智能合约/链/钱包安全审计服务、协议安全和数字货币合规(AML/CFT)平台 Phalcon Security / Phalcon Compliance / Phalcon Network、资金追踪调查平台 MetaSleuth 和区块链交易分析工具 Phalcon Explorer 等。

目前，BlockSec 已服务全球逾 500 家客户，既涵盖 Web3 知名公司 Coinbase、Cobo、Uniswap、Compound、MetaMask、Bybit、Mantle、Puffer、FBTC、Manta、Merlin、PancakeSwap 等，也包括了权威监管机构及咨询机构，如联合国、SFC、PwC、FTI Consulting 等。

官网：https://blocksec.com/

Twitter：https://twitter.com/BlockSecTeam

推荐阅读👇

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTJKnQAjhicg47N8sLY3SKzqlEcnuEf3pYzPTIqpar2ibkeSeCvjqQsKrLwZwWyTcAXIazKXLQIXEchQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247490504&idx=1&sn=ed76941ba8ee144bdd12cb0ddb7df70c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTIje0g9kj9ic4b9GEzwpo1TCWq94NdL91n7Yt1FYkWUmPEXrkGzHKNvuQbOlu36LFXShpNOTklWvKw/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247491200&idx=1&sn=f0a133511ca63c3deb086c51654e4157&scene=21#wechat_redirect)

#BlockSec #每月安全速递

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTKWV4NZYNjUicibdl9UQ4HibVfGa4a6ypSMKArRmWBI3Nibibicuo7YJbQibOC8XKvSMJXYGRFWIz3hsvvfA/0?wx_fmt=png)

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