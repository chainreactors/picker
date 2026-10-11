---
title: 私钥没泄露，近 3.9 亿美元怎么被转走的？
url: https://mp.weixin.qq.com/s/YrLmCshE4-ZXne0xwcRYyQ
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:00:07.444743
---

# 私钥没泄露，近 3.9 亿美元怎么被转走的？

# 私钥没泄露，近 3.9 亿美元怎么被转走的？

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ibKZs4HxyqtTUJibmiaaDgadp610m0ahHpndAtK8Y4B9dAlMY539eDia191DN7avhWFrMQOav9ny1Miaic7wEibdzWibq3Jjev4oz6kds90U3A4sicM/640?wx_fmt=gif&from=appmsg)

核心要点

本期收录 2026 年 9 月 21 日至 10 月 4 日发生的 8 起区块链安全事件，估计损失合计约 $418.4M，涉及 Ethereum、BNB Chain、Solana、Bitcoin、TRON、XRP Ledger、Zcash、Avalanche、NEAR 及相关网络。

事件类型包括第三方安全产品漏洞、疑似证明系统 soundness flaw、区块与输入校验失败、网络配置核验不足、访问控制缺陷等。

重点分析的两起事件中，下游签名和执行都建立在错误的上游信息之上。资产系统需要在签名前和资金释放前进行独立校验。

预计阅读时长 9 分钟

过去两周（2026/09/21 - 2026/10/04）共发生 8 起区块链安全事件，估计损失合计约 $418.4M。

![本期安全事件概览](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqtlESibVtIM1KQCrTj9mu78mwkAZ6qbjYHK1qdu8iaGdboKDyYoPGnZh0DjpNIzDiaTGTlDjOfe6uHp5BQVjR6GWWHhzPiaiaRec4s0/640?wx_fmt=png&from=appmsg)

图 1：本期安全事件概览

**入选理由**

* Bitget：该事件占本期损失的绝大部分。攻击者从链下系统入手，伪造提现指令，最终形成有效链上转账，过程中没有发生私钥泄露或智能合约漏洞利用；
* NEAR Intents：退款校验错误和状态回滚缺失把跨链充值解析失败转化为没有资产支持的内部余额，并让该余额通过正常提现路径转出。

**Bitget**

9 月 24 日，约 $387.5M 从 Bitget 的部分热钱包和温钱包基础设施转出，涉及 Ethereum 及其他 EVM 网络、XRP Ledger、Zcash 和 TRON。链上交易带有有效的钱包签名。

Bitget 表示，攻击者利用第三方安全产品中的漏洞取得内网访问凭据，并伪造提现指令；私钥和冷钱包仍然安全[1][2]。

**事件概述**

两份独立调查报告进一步解释了攻击路径，但没有披露两款受影响安全产品的名称。

Mandiant 发现，攻击者取得两款安全设备的特权访问权限，在 Product B 上部署 web shell 并建立 C2 连接，随后横向移动至生产 wallet job server。

调查人员恢复了一款定制提现工具，该工具会伪造 risk-control 参数、构造提现请求并调用提现流程。攻击者如何在所有相关系统之间移动，仍在调查中。

公链记录的是最终签名转账，而不是这些上游操作。

链上记录显示，18:31 UTC，攻击者先收到 93 枚 TRX，11 秒后又收到 0.84 枚 ETH。Bitget 最新时间线显示，对账系统于 19:05 UTC 发现显著差异，并在 19:14 UTC 启动最高级别应急响应[1]。

19:16 UTC，攻击者控制的 TRON 地址另收到 20.59M 枚 TRX；Chen 称，攻击者随后在另外 8 条网络上发起 17 笔大额转账，合计约 $361M[3]。

Bitget 于 19:40 UTC 开始执行遏制措施，并在 21:44 UTC 关闭钱包提现和签名服务[1]。

**资金状态与生态响应**

截至 9 月 29 日 16:35:28 UTC，Bitget 官方持仓页面记录的攻击者当前持仓为 $322.67M，已冻结资金约 $632,700，仍可由发行方冻结的稳定币约 $312,500，另有 $55.87M 处于跨链途中或仍在分析。

地址浏览器采用另一套分类口径，其中余额主要集中在 BTC（$288.51M）、ZEC（$28.91M）和 ETH（$7.17M）。

Binance 共享情报并协助资金追踪，Bybit 则更新 LazarusBounty 并提供帮助[4][5]。基础设施服务方选择了不同做法。

Bitget 要求 THORChain 拒绝向已公布的攻击者地址提供服务，并表示去中心化不应成为协助已知被盗资金流通的挡箭牌[6]。

THORChain 拒绝选择性拉黑，称其控制机制只能暂停更广范围的活动或某条链的路线，不能只针对一个地址或一笔交易[7]。

NEAR Intents 表示，SHIELD 在去除重复尝试后识别并阻断了超过 $50M 与攻击者相关的尝试流量。约 $503,000 在执行过程中被冻结，约 $166,000 成功通过；

其中 $50M 指尝试流量，并非冻结或追回金额[8]。追踪页面后来将 NEAR Intents 处的 $293,507 归类为已冻结资金，公开来源尚未解释两者差异。

**经验与启示**

* 攻击者通过第三方安全产品进入内部系统，触达 wallet job server，并将伪造提现请求转化为带有有效签名的链上交易。

  具备这类访问能力的第三方产品属于实际资产安全边界：机构应隔离部署此类产品，限制身份与权限，持续监控其行为，并在签名前独立验证提现意图；
* 追回权限分散在交易所、稳定币发行方、路由服务和基础协议之间，任何单一参与方都无法独立完成处置。受影响机构需要尽快共享经核实的地址和交易数据，基础设施服务方与安全团队则应在各自技术和治理约束下，协同完成资金追踪、冻结、交易筛查和追回；
* 关于从本次事件中提炼出的防御措施，可参阅Bitget 链下安全事件深度分析。该文围绕特权访问、提现意图、资金流监控和应急响应提出了一套纵深防御框架。

**NEAR Intents**

9 月 30 日至 10 月 1 日，intents.near 中的退款校验错误和状态回滚缺失产生了没有对应资产支持的内部余额，导致 NEAR Intents 损失约 $3.87M。

攻击者利用该余额取得有效的 HOT MPC 提现签名，并从协议位于 BNB Chain 的 vault 中提取真实 USDT[9][10]。

**背景**

NEAR Intents 是部署在 NEAR 上的意图执行系统。其核心合约 intents.near 持有 omni-assets、记录用户内部余额，并根据用户签署的 intent 处理资产交换和提现。

在跨链充值过程中，源链上的 vault 锁定真实资产。Omni 在 NEAR 上创建对应的 omni-asset 并转入 intents.near，随后 intents.near 增加用户的内部余额。

![NEAR Intents 跨链充值流程](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4Hxyqsx17sPSPFF2bWGXibJuQg1GoU1vMpL7USLSVcPxuibYeibkEsQTDsS0aibzcd5PUMuBPBctBKFdsuROKhUiaaLKYMAggia4qu7QLsjY/640?wx_fmt=png&from=appmsg)

图 2：NEAR Intents 跨链充值流程

提现时，intents.near 请求 Omni 销毁对应的 omni-asset 并创建提现记录。HOT MPC 验证该记录并生成签名，目标链上的 vault 验证签名后释放真实资产。

因此，intents.near 记录的内部余额必须始终由合约实际持有的 omni-assets 提供支持。

![NEAR Intents 跨链提现流程](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqtXRW0HO1NkjThfQWIWUXGp6TlAWur7AUxoKP7PPJiabhJO7cQAZKehWTFNsNRQHrrbvYLqX9BDtek55icWTNhictLtzzZJygicvDQ/640?wx_fmt=png&from=appmsg)

图 3：NEAR Intents 跨链提现流程

**漏洞分析**

充值路径会在跨合约转账完全完成解析之前，先增加接收方的内部余额。

在解析过程中，resolve\_deposit\_internal()使用接收方持有该代币的总余额限制 receiver 可控的 requested\_refund，却没有使用 deposited 限制退款；

deposited 表示本次正在解析的充值实际转入了多少，也是本次操作允许退款的最大范围。总余额只能说明账户付得起多少，不能说明其中有多少属于本次充值。

缺少 deposited 这一上限后，拥有大量历史余额的接收方就能请求远高于本次充值金额的退款[10]。

![退款逻辑使用接收方总余额限制 requested_refund](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4Hxyqu76eLO3EjFfKMGfbwvhGRTWic8sFYVLhOznKEicYamLHucu7HicYQv4wSVgtzLoU28F7mWU4L1YbicaZ1WRLvLibl5sM2LHQfGAjFc/640?wx_fmt=png&from=appmsg)

图 4：退款逻辑使用接收方总余额限制 requested\_refund

对于包含多个长 token\_id 的批量充值，错误的退款数值会扩大序列化后的 MtBurnEvent。

当该事件超过 NEAR 的日志总长度限制时，check\_refund().unwrap\_or\_panic\_display().emit()路径会 panic，导致 mt\_resolve\_deposit receipt 失败。

![超长日志导致退款事件生成失败](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4Hxyqtq8jVNGV8qzDhX41e8RUEtFc4JaK1ySvRvpdWehz8b0JAeTWjaRbQSjUElpgcZrbDffBJrAe92CMkCtbw4bicl2H3lsv02v3TI/640?wx_fmt=png&from=appmsg)

图 5：超长日志导致退款事件生成失败

内部余额已在更早的 receipt 中记入。此次 panic 会回滚 callback receipt 尝试执行的余额与总供应量扣减，却不会撤销此前已经提交的内部余额。

Omni 随后把已转移资产返还给发送方，攻击者因此保留了可提现的内部余额，而 intents.near 不再持有匹配的 omni-assets。该漏洞由退款校验错误和异步 receipt 序列中的状态回滚缺失共同造成。

**攻击分析**

以下攻击过程还原基于公开信息分析[11]。

**阶段一：在 NEAR 上制造没有资产支持的内部余额**

* Step 1：攻击者通过 BNB Chain 上的 Omni/HOT vault 充值 10 枚 USDT，使恶意接收方账户在 NEAR 上拥有非零 omni-asset 余额。 ；
* Step 2：攻击者调用 v2\_1.omni.hot.tg 的 mt\_batch\_transfer\_call()。

  在 mt\_on\_transfer()中，intents.near 先通过 deposit()增加接收方余额，再通知恶意接收方，并把返回结果交给 mt\_resolve\_deposit()处理。 ；
* Step 3：恶意接收方返回远高于本次充值金额的 requested\_refund。由于校验以接收方的代币总余额为上限，该异常数值进入退款处理阶段。 ；
* Step 4：在这批条目中，过大的退款数值使序列化后的 MtBurnEvent 超过 NEAR 的日志总长度限制。

  mt\_resolve\_deposit callback 发生 panic，回滚了本次 callback 尝试执行的退款扣减，但没有撤销更早 receipt 已经提交的内部余额。

  Omni 退回已转移资产，而 intents.near 中的余额仍然可用。攻击者重复这一过程，获得了可提现但没有资产支持的余额。 。

**阶段二：从 BNB Chain vault 提取真实资产**

* Step 5：9 月 30 日 18:57 和 20:05 UTC，攻击者使用有效的 HOT MPC 授权，先后从 BNB Chain vault 测试提现 10 枚和 11 枚 USDT。第一笔测试交易确认该 vault 会接受上游授权。

![Phalcon 展示的首笔小额测试提现交易](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4Hxyqvc8R8wWIhux1wmMQ6Qhensv11hI0xsXLUafFNt1IjkY1rDYxkOOuxW3VAmMsY2FfDVCU7A1pECT4OH6D7NwPVuRfpBMyfzhQk/640?wx_fmt=png&from=appmsg)

图 6：Phalcon 展示的首笔小额测试提现交易

* Step 6：从 9 月 30 日 23:54 UTC 至 10 月 1 日 06:08 UTC，攻击者发起 5 笔大额提现，金额分别为 800,000 枚、1.2M 枚、1.5M 枚、330,000 枚和 35,000 枚 USDT，合计从 vault 转出 3.865M 枚 USDT。

**结论**

NEAR Intents 事件的根本原因是退款校验错误和充值解析失败后的状态回滚缺失。攻击者通过超额退款请求，让底层资产退回后内部余额仍然保留，并利用这笔没有资产支持的余额发起提现。

Omni 据此创建提现记录，HOT MPC 对记录签名，BNB Chain 上的 vault 验证签名后释放真实 USDT。

退款处理应针对每种代币，将退款金额限制在当前正在解析的充值金额以内。协议还应尽可能让余额增加与解析原子化；无法原子化时，必须在失败后执行可靠的补偿回滚。

发出提现签名前，系统应核对内部余额总量与实际 omni-asset 持仓，发现不一致时立即暂停提现。事件生成也必须设置边界，避免过大的日志使关键状态解析路径中止。

**参考资料**

[1] https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response

[2] https://x.com/GracyBitget/status/2104515761691939026

[3] https://www.theblock.co/news/regulation/2026-09-28-bitget-attacker-tested-risk-controls-small-transfers-388-million-theft-ceo-says-417045

[4] https://www.binance.com/en/square/post/09-25-2026-binance-news-richard-teng-puts-binance-s-security-muscle-behind-an-industry-wide-response-370442242243629

[5] https://x.com/benbybit/status/2103328213141508335

[6] https://x.com/GracyBitget/status/2103812967066439817

[7] https://www.coindesk.com/tech/2026/09/28/thorchain-rejects-bitget-request-to-block-hacker-as-usd6-million-moves-to-bitcoin

[8] https://x.com/GracyBitget/status/2104602301503816040

[9] https://x.com/near\_intents/status/2105642219357241796

[10] https://github.com/near/intents/pull/362

[11] https://x.com/Phalcon\_xyz/status/2105680009687957909

---

关于BlockSec

BlockSec 是全球领先的区块链安全和合规公司，于 2021 年由多位业内知名专家联合创立。BlockSec 致力于提升 Web3 世界的安全性和易用性，提供一站式安全服务，包括智能合约/链/钱包安全审计服务、协议安全和数字货币合规(AML/CFT)平台 Phalcon Security / Phalcon Compliance / Phalcon Network、资金追踪调查平台 MetaSleuth和区块链交易分析工具 Phalcon Explorer 等。

目前，BlockSec 已服务全球逾 1000 家客户，既涵盖 Web3 知名公司 Coinbase、Cobo、Uniswap、 Compound、MetaMask、Bybit、Mantle、Puffer、FBTC、Manta、Merlin、PancakeSwap 等，也包括了权威监管机构及咨询机构，如联合国、SFC、PwC、FTI Consulting 等。

官网：https://blocksec.com/

Twitter：https://twitter.com/BlockSecTeam

推荐阅读 👇

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTJKnQAjhicg47N8sLY3SKzqlEcnuEf3pYzPTIqpar2ibkeSeCvjqQsKrLwZwWyTcAXIazKXLQIXEchQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247490504&idx=1&sn=ed76941ba8ee144bdd12cb0ddb7df70c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg...