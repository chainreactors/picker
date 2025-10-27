---
title: 支持零知识证明的交易数据隐私保护方案
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535501&idx=1&sn=552861c7d0009628272ac9b3f74ee7f8&chksm=fa93fd4ccde4745a320cb86473974b36ce0de6cc3a4b12481f3a0121de344b7613df2476c4db&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-16
fetch_date: 2025-10-04T09:45:42.071763
---

# 支持零知识证明的交易数据隐私保护方案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176ms8vzq4GecSbDuUdrY06rHtiaKap7X2FzABkkmmIEoInw5yjUtbIBExiaDRUN05BCdQGNpW3SiaTDZg/0?wx_fmt=jpeg)

# 支持零知识证明的交易数据隐私保护方案

网络安全应急技术国家工程中心

以下文章来源于信息安全与通信保密杂志社
，作者Cismag

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM57SpaEcnib8NMGibzYLk6p0uOuGZThgJsy6XBtuoV6SmKQ/0)

**信息安全与通信保密杂志社**
.

网络强国建设的思想库、安全产业发展的情报站、创新企业腾飞的动力源

**摘要：**面对传统区块链系统交易过程信息在链上公开透明化时，极易遭到攻击者透露秘密的问题，根据传统区块链系统完成交易过程时所存在的漏洞，对通过零知识证明解决隐私泄露问题的方法，展开了深入细致的探究。方案不但可以实现对区块链中的交易数据加密，还可以让链码端在所有交易数据都是密文的情形下证明交易过程的合规性，并详细地分析了该方法在区块链信息安全保障流程中的应用效果。此外，针对加密情形下的链上链下数据可能存在的不一致问题提出了基于 IPFS 系统的协同改进方案。

由于传统区块链系统在链上数据完整性和安全性方面存在局限性 ，且链上与链下的数据无法进行高效协同。因此，本文提出在提供隐私保护的同时保证链上与链下数据的强关联性。采用零知识证明、链下计算等技术来解决数据协同的关键性问题，最终实现区块链性能拓展与安全性能的提升。将链下的交易数据生成零知识证明并置于区块链中存储，达到隐私保护的效果。

区块链是运用密码学技术将区块以链表形式联系起来，由众多参与者一起完成并维护的分布式账本 ，由于具有去中心化、不可篡改等特点，使其在近几年受到更深入的研究与使用。其中，以联盟链为框架的区块链平台（例如 Fabric）在国内得到了越来越多的研究与实际上的应用开发，然而联盟链中的账本交易数据对于每个参与维护区块链的组织来说是公开透明的，这意味着每个组织都能够看见链上每个用户的交易信息。用户的交易等隐私信息很容易被泄露，这对于一些特别注重隐私性的行业是不能够接受的 。

因此，在既可以实现区块链去中心化的功能同时也可以对链的信息进行安全性的保障是本文研究的重要课题。问题的处理关键在于，交易底层的区块链信息和实际应用层间的传输接口隐私保密度，以及处理交易的智能合约的可验证度。针对与基于零知识证明的隐私保护有机结合的问题，本文在研究同态的 Paillier 算法的基础上，给出了与零知识验证结合的区块链隐私保护方法。

零知识证明是属于当前区块链链下 Layer2扩容的一种技术路线，其利用零知识验证进行链下的安全运算形成数据，随后再将计算结果交给链上的智能协议验证，以建立链下计算链上验证的隐私防护系统 。零知识证明技术尽管在一些数字货币如 Zcash、Monero 中有了广泛应用，但其对数据所产生的智能合约证明的效率仍然比较慢。基于此，将数据利用零知识证明和链下的加密算法形成证据，然后将计算结果交给链上的智能合约验证，以建立链下计算链上验证的隐私与安全体系。

随着数据时代的到来，本机处理数据的负载也越来越大。而云计算的发展很好地解决了对数据计算处理的效率问题，但将数据外包给第三方服务器进行加密很有可能造成数据泄露，因此本方案结合安全多方协议，在云服务器上对数据高效计算的同时保证数据的隐私性。

在基于零知识证明的链下计算链上验证的拓展架构方案中，会面临分布式存储可能带来的风险，使得这种链上存证链下计算面临越来越复杂的安全考验，同时也增大了数据丢失与链上链下数据不协同带来的不确定风险。因此，如何在功能拓展的同时确保链上链下数据协同统一，规避数据在管理过程中的风险问题是架构需要着重讨论的内容。

针对这一难题，一般给出的解决方案是对数据在链下进行计算、生成证据、加密等处理后再上传，这其中就包括上面所提到的零知识证明的隐私保护相关理念与保护手段。但区块链与传统的隐私保护机制不同 ，如果直接对数据进行加密处理后再上传可能会导致整个链上交易无法完成共识，即便使用零知识证明技术在加密算法环境下满足了隐私安全的需求，但是链上数据的协同一致性也会大打折扣。

基于此背景，对于区块链链上数据与链下数据存储相结合的可拓展性研究逐渐受到关注。Niu 等人 将可搜索加密方案应用到了区块链架构上，通过区块链实现了不信任的多方间建立可靠数据共享的方案，然而该方案基于复杂的索引与排序算法进行设计，所以计算开销过大。文献 [10] 提出了一种区块链多授权可搜索的属性基加密方案，并结合布隆过滤器与可搜索加密减少链上搜索时间，但只能在簇内可信的机制下适用。以上方案在安全性和开销效率之间的平衡难以得到解决，所以需要一种解决方案来满足两者之间的需求平衡。让链上服务回归链上，链下服务回归链下，实现链上链下数据协同，提出链上链下协同一致的方案，以达到区块链的高可用性、高安全性和高拓展性 。

本文主要的研究工作如下：（1）研究基于零知识证明的数据上链机制和链下计算技术，实现隐私保护功能，提高交易数据的隐私保护能力。（2）提出基于区块链的数据协同模型，构建一种基于区块链的安全可控数据协同技术架构，以此保障交易数据流通中的隐私安全。

# **1、预备知识**

**1.1　区块链**

区块链科技的源头是以比特币为代表的加密货币，由化名为中本聪的学者在 Bitcoin: A Peer-to-Peer Electronic Cash System 中提出关于区块链的概念，是指一个可以根据时间序列将所有储存数据的区块以链表的形式组织的数据结构体 。它可以通过使用密码学维持一个去中心化的账本，而这种账本的各节点间的信息共享关系是无法修改并且也不能进行伪造的。这样的结构形成了一个去中心化的分布式系统，存储每个节点的历史交易记录信息，所有节点通过共识机制来保证数据库上数据的一致性，并使交易具有可追溯和不可逆转的特性。区块链技术最初是用于记录比特币等加密货币交易的数据结构，加密货币的技术原理是利用区块链的分布式网络基于密码学算法来生成的，代表着区块链技术的 1.0 时代——数字货币时代 。随着数字加密货币技术平台的发展，后来在数字货币的基础上加入了智能合约的概念，代表着区块链技术的 2.0 时代。与加密货币相关的底层技术逐步改进形成了区块链技术，如今在其他领域也展现出迅猛的发展势头，在各个行业与领域中进行智能化应用的开发，代表着区块链发展进入到 3.0 时代。

**1.2　零知识证明**

零知识证明技术，最早是由 Goldwasser 等人于 20 世纪 80 年代提出的一种最小泄露证明。其设计理念与证明思想被广泛应用于身份证明、电子现金、数字签名等场景。

通常来说，零知识证明的初始化过程包括以下几个步骤：

(1）声明：证明方根据论断内容产生一些派生的数据，然后把它们发送给验证方。

(2）挑战：验证方利用断言产生一些等价问题，然后把这些问题发送给证明方。

(3）响应：证明方求解这些等价问题，然后把对应的解答返回给验证方（但验证方无法利用这些等价问题的解答获得原问题的解答）。

(4）验证：验证方判断那些等价问题的解答是否正确。

初始化算法：![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjkjUcRqRzNoYAMrzusEHQTP5icZ5ibVfM9GJq8A37iaVDIlYY4RRP4EkMw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

证明算法：![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjB0bLvZiaib6via5a4OD82bOia5nwCUCIu5DgQVGE8UnJKQYtReCqnKRuAw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)，输入公共字符串 str ，语句![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjbtmJGwo9R1hvssM2WvH6y8ibQJ9ElV1icHibvKBtvYrnMmrx9JFXLGEGg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)（其中 L 是 NP Language），证据ω ，输出证明π 。

验 证 算 法：![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDj9ibNjxdImxMyZofXdwyQ6ibJBClXictEcLExpbSozlJzRSPWeqWBFhmibw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)，输入公共字符串 str ，语句 ι ，证据 ω ，输出布尔变量b∈{0,1} ，判断输入证明语句ι 是否成立。

检 查 算 法：![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjrdSYALqFhAoXaRstv9UB8NJLvep1IbbllfgZzKk3XdVgEx27YvrsCQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)，输入公共字符串 str ，语句ι ，证据ω ，输出布尔变量d ∈{0,1}，判断ω 是否使得ι 成立。

**1.3　Paillier 算法**

Paillier 加密算法是 Pascal Paillier 在 1999 年发明的概率公钥加密算法。优点是原理简单、易实现，缺点是仅支持加法运算。

(1）密钥生成：先随意选定两个大素数p 和 q ，运算出它们的积![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjM9OHhncYdqpnaWdeNuDeID5D8EBh7X1txIjdfics09x4AORuITux4WA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)和最小公倍数![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjg3iaibVadn21klkFyWH6icF9gPCq9UQrMaiawn2NOdQz3NkOdESibibib798w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)选择随机数![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjMTvyDgTlpyM2I7ImT76yNkehVSicc6QLCOE2Lv9cicbJ7r5d11mD9oYw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjIHF7YEgXAEkXgJwwSoKdzb3e6AIl0h0vicOMdCsHxWXMoSoPFEKtE0g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)且满足最大公约数![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjrZrpeic73gvB1vpN6K06PibRJiau9zetHcDOOfiaYPxpvNXiboHDh6TDlibg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)定义![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjIsrpVrBqFicfG6xISialzwNt7USW7S2tlAnvF9LLGeTzBfick9PQIjL6w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)存在![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjHOq8iabcnFVCKn75pfCnIfT8fibj5Fiay37iceWVE4hy0y9wpPxqgbpkfw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)此时得到公钥为![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjKH89WmfuFRzmlNiaeOvgHhuTibfVUkmiaByvE7uTPrW74dqKqgV5gHY1w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)私钥为![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjdicxDzTDUahibicM5uo1Lc0Im0OQFcAjVQATzlial3Xdn5MKTOicGtHJH9g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

(2）加密：对于明文 m ，明文信息需要满足 m 小于 n ，选择一个随机数![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjOdbBB1TwES6g6ydDicf1Fk205DB7vP4pdN5RDDekniaicHlHsKxeYLibHw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)密文![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjwwial53RGLeDruUNzWm2uKmicEL87vjPJ4ccfgwZiaGMZe6LlFS8Ayriag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

(3）解密：对于密文 c ，明文![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjY8tXJxKk832yJhxGwicY0y6KkhRq8M6x9SNPrwpibzemF6Hj5619B74w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjhickKqnP852js12zXySEdlcSNcwITh3iaMLAOXSPEib3306GByaYGG2KQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

同时，Paillier 也存在快速生成密钥的算法：

在密钥长度相同的情况下，可以快速生成密钥![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjOVLAQxph2woSU2YvGMDOWAfWImKfctMGvKruZWjzp8ey3EPq9oQIOQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)所以n 更像是加密环境值，![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBywnfBOFyqAYm8ZWRwqEicDjfnHVxYYmnypfPEpBNlRErICylAhqKibNMzHlgv80YIfO5ibXRWMoRIEw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)对应密钥。

**1.4　IPFS 系统**

星际文件系统（Inter Planetary File System，IPFS）是一种点对点的分布式文件系统，同样具有去中心化存储的特性，因此与区块链具有较好的结合性，同时也可以较好地解决当前区块链中区块存储容量存在限制的问题。

目前有一些与区块链和 IPFS 相关的研究，王路阳等人 提出了一种基于区块链和 IPFS 网络的监控信息隐私保护机制。该方案结合 IPFS和区块链技术，解决了监控管理中的隐私保护问题。其中区块链用于安全存储带有哈希的信息，并为哈希值提供验证信息，IPFS 用于存储和分发监控信息。Hao 等人 针对农产品可溯性管理中数据可能被篡改从而影响食品安全的问题，提出了一种基于 IPFS 的区块链存储模型。该方案主要用于存储不同环节中农产品的信息，该方案存储数据完全公开透明，虽然通过区块链保证了数据不被篡改，然而并未考虑存储数据的安全问题。

有关区块链和 IPFS 技术的应用结合问题还处在理论研究的起步阶段，许多方案还未得到实际的应用和落地 。因此区块链和 IPFS 技术的应用结合仍然任重而道远，相关应用的探索还要一直持续，但是可以为两者的进一步实质性结合提供借鉴价值。

在数据存储和共享上，IPFS 能够处理重复冗余的数据文件，把相同的文件合并，减少了数据复杂程度，节省了服务器的存储资源。对上传到 IPFS 的数据文件进行加密和哈希函数处理后，都会生成唯一文件哈希密文值。哈希密文值唯一指定了数据文件，对数据信息进行修改后就会重新获得更新的不重复的哈希值。在获取文件时，IPFS 进行用户访问权限控制，完成验证后根据密文哈希值从分布式存储节点中返回解密之后的内容。

# **2、系统方案**

基于目前的零知识证明技术现状，针对基于零知识证明的交易数据隐私保护的工作可以从零知识证明的区块链隐私保护、加密后数据的链上链下一致协同两方面展开。

**2.1　方案模型**

本文基于零知识证明的交易数据隐私保护模型如图 1 所示。方案设计包括区块链、交易存证服务、零知识证明算法和同态加密算法创建隐私保护模型，以实现区块链系统中的交易安全与隐私保护。

![](https://mmbiz.qpic.cn/...