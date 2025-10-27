---
title: G.O.S.S.I.P 阅读推荐 2024-09-30 MPFUZZ
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498937&idx=1&sn=36df820c4074b5bd0d4f219db1c40f8d&chksm=c063d260f7145b76a1959fea861e96163ae0a40dc7ebbb8f9ccb3f77a4201c3183c3f3cb4f93&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-10-01
fetch_date: 2025-10-06T18:53:33.439820
---

# G.O.S.S.I.P 阅读推荐 2024-09-30 MPFUZZ

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FXcPR7qlapNMwEeEFbu5KDHNh2eJYicHh53Meb1r2vYgIUdNhBjcuG1pm6GhjuE6PZWS3yROSDIzw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-09-30 MPFUZZ

Yibo@SYR

安全研究GoSSIP

9月的最后一天为大家推荐的论文是来自USENIX Security 2024的Understanding Ethereum Mempool Security under Asymmetric DoS by SymbolizedStateful Fuzzing，由雪城大学汤宇哲研究组完成并投稿。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FXcPR7qlapNMwEeEFbu5KDSiboKLztb5BIqzXicBiaLTwTCOGeBQPrytpuYU3jEkeEhc8Qiaib00p5OwQ/640?wx_fmt=png&from=appmsg)

在区块链网络中，交易池（mempool）在共识之前管理交易流，而对其服务的拒绝会显著影响网络的健康和安全。本文介绍了MPFUZZ，这是首个专门用于发现不对称拒绝服务（DoS）漏洞的交易池模糊测试工具。MPFUZZ通过探索符号化的交易池状态，并评估中间状态在触发漏洞预警方面的潜力，来揭示潜在的漏洞。与基线区块链模糊测试工具相比，MPFUZZ在发现已知的DETER漏洞方面实现了超过100倍的加速。将MPFUZZ应用于主要的以太坊客户端，发现了新型交易池漏洞，这些漏洞展现了多种复杂的攻击模式，包括隐蔽的交易池驱逐和交易池锁定。本文还提出了针对所有新发现漏洞的基于规则的缓解方案，为提升交易池安全性提供了全面的解决策略。

该论文的贡献主要包括：

* **新型模糊测试问题**：本文首次提出了交易池模糊测试问题，旨在自动发现不对称的拒绝服务（DoS）漏洞，并将其作为漏洞预警。交易池模糊测试面临着现有区块链模糊测试工具未曾涉及的新挑战，这包括更大的搜索空间，其中涵盖了无效交易和不同价格的交易。
* **新型模糊测试方法**：本文介绍了MPFUZZ的设计和实现，这是一个符号化状态的交易池模糊测试工具。MPFUZZ根据交易池的实现定义了符号化交易序列下的状态搜索空间，并利用符号化状态覆盖的反馈和中间状态在触发漏洞预警方面的潜力高效地搜索这一空间。MPFUZZ在实际以太坊客户端上运行，通过Python原型实现，发现已知的DETER漏洞的速度比基线工具提高了超过100倍。
* **新型交易池漏洞发现**：MPFUZZ在主网的六个主要以太坊客户端中发现了新的不对称DoS漏洞。经过真实交易工作负载的评估，所有发现的攻击都实现了84.6%至99.6%的成功率，并且攻击成本较低，例如对抗性交易费用比受害者交易费用低100倍。

**背景**

在以太坊中，Web3用户发送的交易首先会被缓存在交易池（mempool）中。随后，验证者从交易池中选择交易，并在将其包含到下一个区块之前进行验证。因此，交易池在整个交易流程中扮演着至关重要的角色。如果交易池服务被拒绝，验证者将无法读取未确认的交易，只能被迫生成空区块。这不仅使验证者无法从交易费用中获得以太币奖励，削弱其参与共识的动力，还会导致区块链网络的规模逐渐缩小，增加51%攻击的风险。此外，区块链用户的交易无法及时被包含到区块链中，严重影响去中心化金融（DeFi）应用的收益。

一个实际可行的攻击方式是以极低的成本拒绝交易池服务，称之为ADAMS攻击。具体来说，攻击者支付的伪造交易费用应远低于被驱逐出交易池的受害者交易的费用。在现有研究中，已知的ADAMS攻击仅包括发表在2021年CCS会议上的DETER攻击和2024年Security会议上的MemPurge攻击。这些攻击在以太坊测试网上的测试中表现出极大的实用性。

然而，当前研究对ADAMS攻击的理解仍不充分。这些攻击均通过手动方式发现，而以太坊软件发展迅速，手动检查在实际操作中过于繁琐。因此，本研究旨在探讨如何在给定交易池实现的情况下，自动化发现此类攻击。

常见的软件漏洞发现方法是模糊测试（fuzzing），但在区块链系统中对交易池进行模糊测试时，存在独特的挑战，使得现有的模糊测试工具无法有效应对。首先，作者的目标是发现设计缺陷，而非实现中的bug或崩溃，因此AFL和Loki等工具不适用。其次，交易池的输入空间远大于共识协议，因为交易池不仅接收无效交易，还接收不同价格的交易，而共识模糊测试通常仅考虑有效交易。此外，模糊测试交易池并非差分模糊测试问题，因为两个节点的交易池不同并不一定意味着系统失败。因此，差分模糊测试工具如Fluffy也无法有效应用于交易池的模糊测试中。

**研究方法**

为了解决发现新的交易池拒绝服务（DoS）漏洞的问题，作者设计了MPFUZZ，一个符号化状态交易池模糊测试工具。交易池模糊测试面临独特的挑战，主要是生成输入交易序列时输入空间的庞大。为应对这一挑战，作者采用了状态感知的模糊测试，通过探索交易池状态来进行测试。然而，这种方法仍然面临状态爆炸的问题。作者的核心思想是搜索符号化的交易和交易池状态，而不是具体的交易序列。作者发现，现实中的交易池实现通常基于抽象符号（例如未来交易）来接收交易，而不是具体的值。例如，发送两个未来交易会重复触发相同的交易池行为，无论发送方账户或交易的nonce如何。因此，作者为每组触发相同交易池行为的具体交易分配一个唯一的符号。这样，搜索一个交易就足够覆盖所有与该符号关联的交易，从而将搜索空间从具体交易缩小到符号空间。作者使用7个符号来覆盖交易空间，并在模糊测试过程中为每个符号实例化一个交易。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FXcPR7qlapNMwEeEFbu5KDTVWIIm56MzqApxNRDmPKaK3CvEhcp2iavUrFVwtbDSFORpib3QLUibuSQ/640?wx_fmt=png&from=appmsg)

图1: 符号化及交易空间缩减

在作者的模糊测试方法中，算法包括种子选择、交易变异、交易执行、触发漏洞预警和状态反馈五个步骤。作者对四个步骤进行了定制，分别是状态能量、交易变异、漏洞预警和状态反馈。特别地，作者定义了驱逐漏洞预警和锁定漏洞预警。在本研究中，作者重点介绍驱逐漏洞预警。具体而言，如果一个输入交易序列将交易池从初始状态转换到最终状态，并且在攻击后交易池中没有剩余的正常交易，作者称之为成功的驱逐攻击。此外，攻击成本也必须较低，即最终状态中的对抗性交易费用小于初始状态中正常交易费用。在交易变异过程中，交易是根据给定状态由符号实例化的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FXcPR7qlapNMwEeEFbu5KD9UIXZ6b5aeFjnJHlD9Cm6ES9Cw6dmlqsTFt36bf98ibjd3sdYK523ibA/640?wx_fmt=png&from=appmsg)

图2: MPFUZZ的工作流程

在模糊测试过程中，作者从种子数据库中根据种子能量选择种子状态。状态的能量由其符号化成本决定。作者旨在识别和选择那些更可能触发漏洞预警的状态。状态反馈也非常重要，主要涉及两个方面：一是符号化状态覆盖反馈，二是评估状态在达到漏洞预警方面的潜力，包括最终状态中的正常交易数量较少或对抗性交易成本较低。通过这些方法，作者期望能够有效地发现交易池中的潜在DoS漏洞。

**评估**

在评估阶段，MPFUZZ成功重新发现了DETER漏洞，并且识别出了四种新的驱逐模式。这些新模式比DETER漏洞更具隐蔽性，它们通过将有效交易转化为无效交易来实施攻击，例如将有效交易转变为透支交易或未来交易。这种新的驱逐模式对网络的影响更大，因为攻击负载能够传播到所有节点，使得整个网络都受到攻击。这些转化攻击已经在多个以太坊客户端中被识别，包括Go-Ethereum、Besu、Nethermind和Erigon，以及在类似以太坊的客户端如Binance、Flashbots、EigenPhi和bloXroute等中也得到了验证。

此外，作者还发现了新的锁定交易池的模式。在锁定攻击中，攻击者通过发送低成本的对抗性交易来占用交易池，并拒绝接收正常交易。这些锁定攻击已在包括OpenEthereum和Reth在内的以太坊客户端中被识别。这些发现展示了MPFUZZ在识别和分类交易池漏洞方面的能力和广泛适用性。

为了评估MPFUZZ提出的技术的性能，作者设计了四个基准模糊测试工具进行消融研究。第一个基准B1实现了一个无状态模糊测试工具。基准B2使用了具体状态覆盖作为反馈，基准B3则在B2的基础上利用无效交易数量作为能量，而基准B4则去除了MPFUZZ中的状态前景反馈。结果表明，MPFUZZ在发现已知DETER漏洞方面实现了超过100倍的加速，这证明了MPFUZZ在提高交易池模糊测试效率和效果方面的显著优势。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FXcPR7qlapNMwEeEFbu5KDcAMnM3hmicAr20x0d6PhH9ZOdsGTFPUm3euHgIh0pA0ic6XEdNBUNgDQ/640?wx_fmt=png&from=appmsg)

表1: 性能评估结果

本研究得到了以太坊基金会的支持，并部分由两个NSF奖项资助。作者在下表中记录了发现的漏洞，并且以太坊基金会确认了这些漏洞并给予了漏洞赏金。这些成果不仅验证了MPFUZZ的有效性，也为进一步的交易池漏洞检测和防御研究提供了宝贵的参考。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FXcPR7qlapNMwEeEFbu5KDd0oUXuChLKwrevpqBvblDVqpVyEj75ogqAKVmiaPMXIYwLaJicLQgXxw/640?wx_fmt=png&from=appmsg)

表2: 漏洞报告汇总：已识别问题、状态更新及修复情况

论文pdf：https://www.usenix.org/system/files/usenixsecurity24-wang-yibo.pdf

投稿作者简介：

王一博，2020级雪城大学博士生，导师为汤宇哲老师。他在华中科技大学获得工程学学士学位，并在雪城大学获得计算机工程硕士学位。他的研究重点是区块链的安全性和成本效益，在CCS, USNIX security, ESEC/FSE 等多个会议发表过相关研究成果。

汤宇哲，雪城大学电气工程与计算机科学系副教授。他广泛关注网络安全和计算机系统。他的安全研究涵盖了漏洞发现、威胁检测、威胁缓解以及对已部署系统的安全测量。他目前的研究主要集中在区块链领域。他还建立了BADD实验平台，以支持区块链和去中心化应用开发的主动学习。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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