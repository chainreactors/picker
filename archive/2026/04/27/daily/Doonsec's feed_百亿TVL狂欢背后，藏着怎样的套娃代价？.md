---
title: 百亿TVL狂欢背后，藏着怎样的套娃代价？
url: https://mp.weixin.qq.com/s/jBihuh9HjCtlw09Ss9eUag
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:23:04.576550
---

# 百亿TVL狂欢背后，藏着怎样的套娃代价？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibicDQQkq5lsKHHNYxgD0vYVAuib2ICK87QHFoFJ3Hia59vV9Abk3g8zBLMIWKhpOrd7X2iaos9k3zuLMsAaT7L6RgTLuzxk3vWRQNg3R3UaC1GM/0?wx_fmt=jpeg)

# 百亿TVL狂欢背后，藏着怎样的套娃代价？

原创

ChainSecLabs
ChainSecLabs

ChainSecLabs

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

区块链安全相关的内容

我们将在这里分享一些

*Hi，这里是ChainSecLabs!*

**百亿美元TVL的涌入，正将再质押变成一场危****险的“套娃”游戏。本文将深挖流动性盛宴之下，从级联清算到共识过载的系统性安全风险，揭示这场狂欢背后不为人知的代价。**

![](https://mmbiz.qpic.cn/mmbiz_png/ibicDQQkq5lsKczA6tibHTlGmjZKluDegDP7MAYtjv0Up8IxEbpoln2obbL48kFd2zXeKmVYXUaN84icQJbNom9kkWaV6p04zhtIbFQ1xib3Vqk4/640?wx_fmt=png&from=appmsg)

引言

自EigenLayer主网上线以来，百亿美元级别的TVL如海啸般涌入。在曾经“一鱼多吃”的狂热下，无数的以太坊被包装成各种LRT（即流动性再质押代币），嵌套在一层又一层的智能合约之中。然而，当所有人都沉浸在这场流动性盛宴时，悬在以太坊共识机制之上的达摩克利斯之剑已经悄然出鞘。今天，我们就要拨开收益的迷雾，去审视这个庞大金融套娃底层的系统性安全风险。

![](https://mmbiz.qpic.cn/mmbiz_png/ibicDQQkq5lsIuNXDfPhE66EOR6cxUvp8fiaiacVIzyu1RnovTyjIOjBhHibJdYZd9ZibPh4KJKYCmcJR93HNfQ2Ix6aO0aOw3TYAZaaLzjCOIkeU/640?wx_fmt=png&from=appmsg)

> EigenCloud是基于EigenLayer再质押协议构建的统一可验证云平台，它将EigenLayer提供的去中心化信任封装为开发者可直接调用的云服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsIpOTkLwRFTqDUialVVKFIHCLqQsaM0JjvSmTkU33FPv3YROC3wELtIE9ocXz5UrJFSbsju12icuOiaMw4wetXPpISAdPmw7FD1zU/640?wx_fmt=png&from=appmsg)

套娃的本质

要理解这场安全危机的潜在爆发点，我们先来回顾再质押的本质是什么：

以太坊的PoS质押，就像是把资金存入央行，换取绝对安全的无风险利率；而EigenLayer相当于允许你拿着央行的存款凭证，再次抵押给各种地方性的商业机构（即AVS，主动验证服务，如预言机、跨链桥、数据可用性层等），从而赚取额外的利息。

为了解决资金被锁死的流动性问题，市场上又诞生了诸如KelpDAO、Renzo等LRT协议，它们帮你把这些复杂的抵押关系打包，发给你一张名为rsETH或ezETH的二级凭证，你甚至可以拿着这张凭证继续去DeFi借贷平台加杠杆。这种极其精妙的乐高积木式设计，成倍放大了资金效率，但也极其隐蔽地将脆弱的连环风险植入了以太坊的骨髓。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsJx5wrG7bwTdGSDmMtlzsa5jiaEIMoqxdKqU5sicRWcfwhGJr0H9wxo0ic7GEfFhw7WibpfYPZvUP2FpNmiaNK43LOm0clzXDlibYSro/640?wx_fmt=png&from=appmsg)

级联清算

这其中，最令人担忧的系统性黑天鹅，莫过于DeFi乐高的级联效应与连环踩踏。近期，一起关于KelpDAO rsETH跨链桥的重大安全事件中，这种套娃的代价则展现得淋漓尽致。

此次事件中，KelpDAO为了实现rsETH的跨链流通，其跨链消息验证仅依赖于单一的DVN（去中心化验证网络）节点。攻击者并未去破解复杂的智能合约，而是直接对该节点依赖的RPC基础设施进行投毒，在源链毫无资产销毁的情况下，凭空在目标链伪造释放了高达11.6万枚rsETH。

如果你以为损失仅仅停留在KelpDAO内部，那就大错特错了—真正的灾难才刚刚开始。

![](https://mmbiz.qpic.cn/mmbiz_png/ibicDQQkq5lsKl8amgH6Rd5gyjOIXee3JyhON9H7biasnftBm1kxLX8mA9wibqqa2tjBDiaRgOghgDVaX63pibha6zjOxqEbaUrMr7q0AAvbvOdtU/640?wx_fmt=png&from=appmsg)

攻击者拿着这些凭空捏造的rsETH，并没有直接抛售，而是利用DeFi的可组合性，将其存入了借贷巨头Aave的池子中。由于Aave的预言机依然将这些假代币视为合法资产，并给予了高达93%的抵押率（LTV），攻击者轻松地以极高的杠杆借出了超过8.2万枚真实的wETH。

这瞬间抽干了借贷池的流动性。为了防止这场由衍生品的套娃带来的坏账危机继续蔓延，Aave官方被迫动用紧急权力，接连冻结了Ethereum、Arbitrum 等五条链上的wETH储备。这是一个极其恐怖的信号：全城最大银行的提款通道被切断，仅仅是因为一款大多数存款人从未听过的再质押产品遭到了攻击。

这种联动效应标志着全城最大的提款通道被迫切断，而起因仅仅是一款多数存款人从未参与过的再质押产品遭到了攻击。当应用层的金融坏账规模足以动摇以太坊的核心流动性（如wETH）时，它就不再仅仅是某个协议的局部纠纷。

正如以太坊创始人Vitalik早在2023年《不要使以太坊的共识过载》一文中所警告的：如果应用层的安全隐患倒逼底层的协议层进行干预或治理，将引入难以修复的社区分裂风险。在极端情况下，如果流动性枯竭引发系统性崩盘，社区将不得不面对一个抉择：是坐视生态毁灭，还是违背去中心化精神，动用底层共识力量进行硬分叉来挽救应用层的损失？这种将应用层风险裹挟至共识层仲裁的行为，正是对以太坊安全根基最深重的威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsK2ibLZUhJ3emBtic8BDia51gKiaFHUgBxQjdp3InreJKIKfCSlb4bYchicTcEBSxibzmY6RKPJAYJkEmialJOQt9yqFoMvRRe0MfHPuk/640?wx_fmt=png&from=appmsg)

复杂性诅咒

而当我们把视线转向代码时，会发现再质押带来的挑战同样严峻。即除了经济学上的清算踩踏，从代码安全层面来看，Restaking生态也面临着史无前例的复杂性诅咒。

传统的DeFi乐高往往只是代币层面的互相调用，而EigenLayer生态则涉及到了极其复杂的委托、提款队列以及链下节点验证逻辑。许多安全审计团队在审查时往往只关注链上合约，却忽略了链下客户端代码的健壮性。如果攻击者通过伪造恶意的P2P消息或是利用客户端漏洞让大批量AVS节点宕机，还会触发EigenLayer底层的Slashing机制，导致用户质押的真金白银被直接销毁，这构成了一种跨越链上链下边界的全新攻击面。

面对这些令人如履薄冰的前沿风险，开发者们也并非完全无动于衷，为了防止代码漏洞导致的大规模误杀与连环爆雷，EigenLayer官方也曾在主网部署中采取了极为谨慎的态度。根据其技术文档和社区提案，EigenLayer在早期阶段并未直接激活全自动的Slashing机制，而是引入了一个名为否决委员会（Veto Committee）的多签治理实体。当AVS触发罚没条件时，必须经过该委员会的审核才能真正执行资产扣除，以此作为防止代码bug导致系统性崩溃的最后一道防火墙。

![](https://mmbiz.qpic.cn/mmbiz_png/ibicDQQkq5lsLB3qlLUr6cNIfVCwYd3ScgSLMjFHhaibWicEKhsE4vnSGbZ467dfK27ydne93MusBicgxDZicCOQkbKd9FKqwJtyZRhG2iabXKuOU4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsKNpMJMXmGkYachuibEibDT0F8337TRuhSpiaeH2PJqOezA6JTIq6DF90x1E63kZGeD9yU99xZOFYwwZsACp9UvoP6YIG5NEWMmiaM/640?wx_fmt=png&from=appmsg)

结语

技术总是在狂热与修正的交替中螺旋上升。Restaking无疑是一场伟大的去中心化信任共享实验。但无论是代币脱锚，还是rsETH漏洞引发的多链流动性冻结，都在反复敲打着行业的神经。

当数以百亿计的真实财富被堆砌在这座尚未经过长周期实战检验的沙丘之上时，任何一行代码的疏漏、任何一个单点节点的崩溃，都可能成为引发雪崩的最后一片雪花。作为Web3的参与者，我们在享受流动性红利的同时，必须对这层层嵌套的技术黑盒保持敬畏。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsIUbdy0iaApYmGcNAWSmPIeyiaexiapRISrAn0WodUChicqOBUXDicicE2YdvbZMMtiaJQLeibEMHfZBx2eXxH0ngPtfPaMeuIiaFUZMxfI/640?wx_fmt=png&from=appmsg)

参考文章

* LlamaRisk: rsETH Incident Report

* Vitalik Buterin: Don't overload Ethereum's consensus (vitalik.eth.limo)

* EigenCloud Official Whitepaper & Documentation (docs.eigenlcloud.xyz)

* 《不要使以太坊的共识过载》https://vitalik.eth.limo/general/2023/05/21/dont\_overload.html

———————————END———————————

作者：Dino

编辑：Legend

审核：Chloe

---

ChainSecLabs

**往期推荐**

Previous Recommendations

[Drift Protocol遭史诗级攻击](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247485113&idx=1&sn=436d5db89ec979ce7a934ee87ade5907&scene=21#wechat_redirect)

本文介绍了Drift被以500美元假币盗走2.7亿美元；说明DeFi最薄弱的环节是治理与权限。

[DEX安全简述](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247485094&idx=1&sn=a5d9d0670c47bddff639fa3b5ee0469c&scene=21#wechat_redirect)

本文梳理了DEX的主要类型及常见攻击手法，通过多个真实安全事件分析其风险成因。

[Layer2的身份幻觉](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247485039&idx=1&sn=bcb57bfb4e4f593912e2757d8db28e4a&scene=21#wechat_redirect)

本文讨论了以太坊 Layer2 中地址别名的相关内容，包括其概念、安全背景、易踩的坑以及总结建议等。

[授权方式的更迭: 从 ERC20 到 Permit2](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4OTAxNg==&mid=2247484939&idx=1&sn=8bbf8350d1217502f66261fe3e1add5d&scene=21#wechat_redirect)

本文讨论了 DeFi 领域代币授权方式从 ERC20 到 Permit2 的更迭过程及相关特点。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/hlJuicHobAgAkYmYg8k9LKNWSibARYtAfX4VX0d6Q0HvQyKjdGKnkBRHYD9WGpQbtfD4W2ldGxKRBeBP2iaNFTFFg/640?wx_fmt=jpeg&from=appmsg)

***ChainSecLabs***

搜索公众号

关注我们

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibicDQQkq5lsL3ibguqVGyEkgztlBzxbFauA0xP5YOib5RY0pSMrW4dBv2DFBQjxm1bl8aiaXhdPsyia41l251qskqa1WEhD9sF7ZvXte3hLTXPtY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/ibicDQQkq5lsJvt9DBibrojiakmiaQh3RjicYFx3Wpkn3yictXW4TcTcUN5COQYodnOkgaD1Z7GicEU2oDrbfIbat6g5NbnmFYIUS8PJ1JZywajunXQ/640?wx_fmt=gif&from=appmsg)

---

**免责声明**

本文章旨在分享安全技术相关知识与经验，内容仅供学习与研究参考。文中所提及的技术手段、工具或操作流程，均基于公开资料与作者个人理解，不代表任何官方立场，也不构成对读者的具体操作建议。

请勿将本文所述技术用于任何非法用途，否则后果自负。作者严禁并坚决反对一切网络攻击、非法入侵、数据窃取等违法行为，且不承担因读者不当使用文章内容而引发的任何直接或间接责任。

若文章中引用了第三方工具或资料，版权归原作者所有，若有侵权或不妥之处，请及时联系，我们将第一时间予以处理。

网络安全关乎法律与伦理，请读者在合法合规的前提下，自主学习、合理应用。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hlJuicHobAgDplSpg2SBicqBEmlAlkxzR1vgnpCD7JMrKzoohqQrwYTgPu4oFYhVLwibVPOPjSjOpeX1E0BNibN3hg/0?wx_fmt=png)

ChainSecLabs

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hlJuicHobAgDplSpg2SBicqBEmlAlkxzR1vgnpCD7JMrKzoohqQrwYTgPu4oFYhVLwibVPOPjSjOpeX1E0BNibN3hg/0?wx_fmt=png)

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