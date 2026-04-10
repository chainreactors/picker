---
title: BlockSec 安全周报｜九起攻击，从合约漏洞到治理失守（3.30–4.05）
url: https://mp.weixin.qq.com/s/jg7FxhBvWtr0XEDg2obQCg
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:43:56.438742
---

# BlockSec 安全周报｜九起攻击，从合约漏洞到治理失守（3.30–4.05）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ibKZs4HxyqvOzndcFzMMZdoLNM3BK3GiasASW8M0EaC51umh6VKEssoQVibVle2TgW1YFoiaPNiaOpBNw6T1O5CbOX7qDz018ssx3bLfrGmUq70/0?wx_fmt=jpeg)

# BlockSec 安全周报｜九起攻击，从合约漏洞到治理失守（3.30–4.05）

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2ibKZs4HxyqsWDFIicic8P3BDA4tqxYBCvr95xoDscl7HG86SQeFeSGPDTdsAZ10o9X7vqbF6sV2jYpeRKS7Nx7QtNPJ5D5icHEH5oJhb554xrw/640?wx_fmt=gif&from=appmsg)

**引言**

在过去一周 (2026/03/30 - 2026/04/05),BlockSec 检测并分析了 9 起攻击事件,估计总损失约为 $287M。下表汇总了这些事件,各事件的详细分析见后续小节。9 起攻击事件中，有两起仅定位到受损合约，无法定位到具体项目方，因此下文中以unknown Incident标示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4Hxyqu5HvAZibXYqggpt0vCudbiakwHoU3rI4sULwgCvh4ZngQ03mTRyOWU05ALIpfrsEmdcKia4T1TljZf2fAoKHMtQoLT2n8DN4YnEQ/640?wx_fmt=png&from=appmsg)

**Unknown Protocol Incident**

**简要概述**

2026 年 3 月 30 日,BNB Chain 上的一个未知协议因业务逻辑缺陷损失约 $10K。该协议会将用户存入资金的一部分用于购买平台代币 PSTART 并添加流动性,这意味着用户实际上持有的是会随市场价格波动的 LP 头寸。然而在用户提取时,协议并未基于 LP 当前的实际可赎回价值进行结算,而是依然按照历史存入金额和预定义规则,承诺向用户支付固定金额的稳定币。结果,攻击者通过强制投资进入头寸后,便能够以预先约定的固定价值取回资金,实质上将本应由 LP 头寸承担的损失转嫁给协议本身,最终实现零成本获利。

**背景**

协议运作方式如下:用户存入 BUSD 后,协议会自动用其中一部分资金购买 PSTART,然后将其与剩余的 BUSD 配对添加到资金池作为流动性。所得 LP 份额由 Vault 托管,同时协议会在内部账本中为该用户记录一笔订单,承诺固定的日收益。

之后,用户可以按固定利率领取奖励,在退出时,Vault 会按预定义规则结算本金和收益,而不是严格按照底层 LP 头寸当前的真实净资产值进行赎回。

**漏洞分析**

漏洞源于该协议合约 ([0x587984...73a43c](https://bscscan.com/address/0x587984549f7e61c0ed8131b1f6614f592573a43c#code)) 的一个不合理设计:结算逻辑与底层资产的实际价值脱钩。

用户存入 BUSD 后,协议用其中一部分购买 PSTART 并添加流动性,这意味着用户的真实底层头寸是一个价值随市场波动的 LP 敞口。然而当用户退出时,协议并不按 LP 当时的实际可赎回价值结算,而是仍按历史存入金额和预定义结算规则,承诺支付固定金额的稳定币。

攻击者利用此缺陷,通过闪电贷获取大量资金,然后反复执行 deposit()。在此过程中,攻击者迫使协议持续买入 PSTART 并改变资金池的资产构成,从而人为推高 PSTART 价格,制造出套利机会。

随后攻击者执行 withdraw(),以预先承诺的固定价值赎回资金,实际上把本应由底层 LP 头寸承担的损失转嫁给了协议本身,最终实现 零成本获利。

**攻击分析**

以下分析基于交易 [0xf3b8...55e7](https://app.blocksec.com/phalcon/explorer/tx/bsc/0xf3b8ceae88818d7121c84b7f00f7c99d1c6c45409ceb9de2eae10a92391755e7)。

**Step 1:**攻击者通过闪电贷获取约 2,000,000e18 BUSD,并在资金池中将其换成 19,013,120e18 PSTART。

**Step 2:**攻击者反复调用合约的 deposit() 函数进行质押。每次存款时,协议会计算应使用多少 BUSD 购买代币,以使最终用于添加流动性的代币与 BUSD 比例更接近资金池当前的比例。通过反复存款,攻击者不断向池中注入 BUSD,而 PSTART 数量几乎保持不变。结果 PSTART 的价值持续上升。在此阶段,攻击者通过存款获得的 LP 实际上是以亏损价格取得的。

**Step 3:**接着攻击者将 Step 1 中购入的 PSTART 卖回资金池。由于 Step 2 增加了池中的 BUSD 储备,这次交换返还了约 2,010,655e18 BUSD,在单个攻击周期内带来约 10,655 BUSD 的利润。

**Step 4:**最后,攻击者对 Step 2 开立的所有质押头寸执行 withdraw()。此时这些头寸对应资产的市场价值已远低于其初始存入价值。在正常的经济逻辑下,本不应允许全额赎回。然而协议是基于历史存入金额计算可赎回的 BUSD 数量,使攻击者得以在不承担任何损失的情况下,完整收回此前的强制投资成本。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqtXko3ibwxGQXDCagIp4OC0FHeGoaYesTibMd3VtgDIRCibOw7toeZZgINibWPTVgzWicXibfGHKCCZVicibSY1WQ2YMiboQMQWSYsbokJE/640?wx_fmt=png&from=appmsg)

**结论**

本次事件的根本原因在于,协议将用户资金投入受市场价格波动影响的 LP 头寸,却仍按历史存入金额和预定义规则承诺以固定数量的 BUSD 进行结算。这造成了协议负债与底层资产真实价值之间的脱节。

攻击者利用此缺陷,反复使用 deposit() 改变池的资产结构,推高 PSTART 价格,然后通过外部头寸完成套利,最后用 withdraw() 以账面价值赎回此前的亏损头寸。本应由这些头寸自身承担的损失因此被转嫁给了协议,最终实现无风险获利。

**WDGG Token Incident**

**简要概述**

2026 年 3 月 30 日,BNB Chain 上的 WDGG 代币遭到攻击,造成约 $40K 损失。根本原因是 burnFrom() 函数缺少访问控制。具体而言,burnFrom() 允许任意用户从任何地址销毁 WDGG 代币。攻击者利用此漏洞从 PancakeSwap 池中销毁 WDGG 代币,然后调用 sync() 减少池中的 WDGG 储备,随后执行反向交换提取利润。

**背景**

本事件涉及单一代币 WDGG,这是一个分红型代币,在每次转账时收取手续费。

**漏洞分析**

WDGG 代币合约 ([0x512de7...6b90c5](https://bscscan.com/address/0x512de7b4da71e1ab1c4c186e80905b3ea46b90c5#code)) 的 burnFrom() 函数缺少调用者权限校验。因此,任何地址都可以从任意持有者(包括 PancakeSwap 池本身)销毁 WDGG 代币。结合 PancakeSwap 公开可调用的 sync()(用于将记录的储备与实际余额对齐),该漏洞使得池中的 WDGG 储备可以被任意减少,恒定乘积不变量在没有任何合法交易的情况下被打破,从而暴露出价格失衡套利窗口。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqvRwVkS1SbCfO9reQqgaSdVrQaQ9JyAQwf04OicsloMhoqEyU6dFmibpiceaARibn5NSL0oxYBb3o5u82WDcBYsSlC8eic5aHibromHk/640?wx_fmt=png&from=appmsg)

另一处次要漏洞是 setWdgAddress() 允许任意调用者将任意地址标记为手续费豁免,进一步放大了可通过此攻击面提取的利润。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyquEMic5XzN1oRm1ANIoxSiauna25EhibLOTeguddIUaWa4sicibnpntPlkZhIrXbCE58voGib5SEDJAxubpl6B2aLCyFwCfzETbniaC2E/640?wx_fmt=png&from=appmsg)

**攻击分析**

以下分析基于交易 [0x2da5...0bd1](https://app.blocksec.com/phalcon/explorer/tx/bsc/0x2da59a05359c07bb640075ce99416846f6f26f9fb594dedaab9e1662de750bd1)。

Step 1: 攻击者首先调用setWdgAddress(),将自己的地址设为手续费豁免地址,使后续转账可绕过代币的转账费。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqvuQvFKwGxxFkiaU9BZutib5yjOo6tSjAwQhRt3vmRmTqQYBxj1dtRSt764xYeMU5HQichrqhIdlBGPBAxIiczJo3x8xJN8oSibvndg/640?wx_fmt=png&from=appmsg)

Step 2: 攻击者随后通过 PancakeSwap 池用少量 BNB 换取 WDGG 代币。

Step 3: 获得 WDGG 后,攻击者调用 burnFrom() 直接从 PancakeSwap 配对地址中销毁 WDGG 代币。

Step 4: 攻击者随后调用 sync(),迫使配对合约根据被操纵的代币余额更新储备。结果池中的 WDGG 储备被减至 1 wei。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqsvxztOuib7DXicflDDcyLuE7Gyf13wZcOYibbg52woPOAYHdm0anuEp9LfbpibfHd2VRk3SMQDyoiaACFm8gDEgy159ic3wBAZ6wSp0/640?wx_fmt=png&from=appmsg)

Step 5: 在池储备严重失衡后,攻击者执行反向交换,从价格失衡中提取利润。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4Hxyqv6tnfc6YRuUCt3rJTg4Zt8nypSZYv79VhPOEExczpQECb3yx0u4WM6CiaRzHAxdVPfyksxakS1IC7xkhOMrLsHBcJXWM5a4TMY/640?wx_fmt=png&from=appmsg)

**结论**

本次事件的根本原因是 WDGG 代币合约的 burnFrom() 函数缺少访问控制。攻击者得以直接从 PancakeSwap 池中销毁代币,通过 sync() 操纵池储备,并利用由此产生的价格失衡获利。

**i6Token Incident**

**简要概述**

2026 年 3 月 31 日,BNB Chain 上的 i6 Token 损失约 $273.8K,原因是 invest() 会推动池的现货价格,而 withdraw() 依赖滞后更新的 TWAP 结算余额,两者可在同一交易内组合调用。攻击者通过 invest() 抬高现货价格,再由 withdraw() 以过期 TWAP 赎回超额的 i6,随后把这些 i6 卖回被推高的池中获利。

**背景**

协议运作方式如下。用户调用 invest() 时,USDT 被存入,其中一部分用于在 PancakeSwap 上购买 i6。所获得的 i6 与剩余的 USDT 一起作为流动性添加到 USDT/i6 池中,所产生的 LP 代币会被销毁。协议以 USDT 计价记录用户和推荐余额。

调用 withdraw() 时,协议以 USDT 计算用户累计价值,然后通过协议维护的 TWAP 价格 (twapPrice) 将其换算为 i6。

**漏洞分析**

根本原因在于协议合约 ([0x1cb36b...2a18a](https://bscscan.com/address/0x1cb36b0f1efd9b738997da3d5525364c7e82a18a#code)) 中,invest() 在购买 i6 并添加流动性的过程中会作为副作用推动 USDT/i6 池的现货价格,而 withdraw() 则使用协议维护的 TWAP (twapPrice) 将累积的 USDT 计价余额结算为 i6,该 TWAP 只有在时间窗口流逝后才会更新。合约本身没有任何机制阻止这两个函数在同一交易中被连续调用。

由于 invest() 可以在同一交易内推高现货价格,而紧随其后的 withdraw() 读到的是尚未更新的 TWAP,两者事实上对同一池状态看到了两套不同的价格。通过 withdraw() 赎回的 USDT 计价余额因此会按过期且显著偏低的价格支付 i6,而此时池中每一枚 i6 已经可以兑换远多于结算价的 USDT。这一差距把协议内累积的任何 USDT 余额,都变成了内部结算价与池现货价之间可被利用的价差。

**攻击分析**

以下分析基于交易 [0xc1b9...2f16](https://app.blocksec.com/phalcon/explorer/tx/bsc/0xc1b9a237a00b53a595e1e2d0d93841154ddcdf9aa217be8f395449b8e4ab2f16)。

**Step 1:**攻击者首先通过闪电贷获取 270,000 WBNB,然后将其作为抵押品供给 Venus 借出大量 USDT。攻击者还在 0xda49 部署攻击合约 A,在 0x096a 部署辅助合约 B。

**Step 2:**攻击合约执行第一次 invest()。这一过程中,协议先用 531,489e18 USDT 购入 234,188e18 i6,然后将 354,326e18 USDT 与 72,607e18 i6 一起加入池中。结果池的现货价格从约 1.05159 USDT/i6 迅速涨到约 4.89287 USDT/i6,而协议记录的 TWAP 仍只是 1.05159。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4Hxyqt6sIksK8GJr4YMROB0M1NtpmXgXe8gXSCN1P5dUOzCcZrcvYQ3MNjH1gCLZ8KFrRo9XapY1ONeIFqtMbaa6BbkKsB2hzhLvgM/640?wx_fmt=png&from=appmsg)

**Step 3:** 攻击者随后向辅助合约 B 转入 124,014,184e18 USDT,后者再以 referrer = A 调用 invest()。这一步再次迫使协议进行大规模 USDT -> i6 购买和 addLiquidity(),把池储备推到对应约 15,528 USDT/i6 现货价格的新状态。然而由于没有新的时间窗口流逝,协议没有相应更新 TWAP。

**Step 4:**第二次 invest() 完成后,作为推荐人的攻击合约 A 立即获得以 USDT 计价的推荐奖励权益。攻击者随后调用 withdraw()。协议使用过期的 TWAP 计算应支付的 i6 数量,并从自身余额中转出代币,最终一次性发放了 5,896,508e18 i6。

**Step 5:**收到 i6 后,攻击者立即调用 swapExactTokensForTokensSupportingFeeOnTransferTokens(),把全部 5,896,508e18 i6 卖回池中,换得 125,177,224e18 USDT。由于这些 i6 是按约 1.05159 USDT/i6 的过期 TWAP 结算获得的,而被卖出时所对的池现货价格已被攻击者推高至约 15,528 USDT/i6,攻击者得以直接落袋两者之间的巨大价差。

Step 6: 偿还闪电贷后,攻击者保留了 273,802e18 USDT,这就是本次攻击的实际利润。

**结论**

本次事件的根本原因在于,一个改变池现货价格的函数 (invest()) 和一个按 TWAP 结算的函数 (withdraw()) 可以在同一交易中被组合调用,使二者对同一池状态看到不同的价格。

为防范此类缺陷,结合 AMM 交互与延迟定价机制的协议应当避免在同一交易内同时执行 "移动池现货价格" 和 "按 TWAP 结算余额" 这两类操作,并将支付锚定在池的实时可实现价值上,而不是过期或衍生出的价格。

**Drift Protocol Incident**

**简要概述**

2026 年 4 月 1 日 (UTC),Drift Protocol 在 Solana 上遭到攻击,损失约 $285.3M。根本原因不是智能合约 bug,而是多签授权流程的失效,叠加 5 选 2 的安全委员会零时间锁配置以及 Solana 的 durable nonce 机制,这让预先收集到的多签批准可以无限期保持有效,直到攻击者选定时机再执行。经过数周的前置准备,攻击者诱导五位签名者中的两位预签了绑定到 durable nonce 账户的恶意治理交易,随后将其提交以夺取管理员控制权,继而引入伪造的抵押资产 (CVT),抬高其预言机价格,放宽取款限额,并通过 Drift Vault ([JCNCMF...XJfrw](https://solscan.io/account/JCNCMFXo5M5qwUPg2Utu1u6YWp3MbygxqBsBeXXJfrw)) 提走真实资产。

**背景**

Drift Protocol 是 Solana 上的一个 DeFi 协议,支持保证金交易、借贷、现货市场和衍生品。其高权限操作,包括管理员变更、市场创建、预言机配置、风险参数更新和取款限额调整,均由 Squads 多签框架治理,而不是由单个私钥直接控制。攻击发生时,Drift 的安全委员会采用 5 选 2 的阈值配置且零时间锁,意味着五位签名者中任意...