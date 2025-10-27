---
title: Bleem: 面向数据包序列的协议模糊测试 | 技术进展
url: https://mp.weixin.qq.com/s?__biz=MzU1NTEzODc3MQ==&mid=2247486874&idx=1&sn=311b59a1953758bc2f69485cbf107d4b&chksm=fbd9a626ccae2f30d7167e5d9ee742af35355e569368a8dbc1d983fbcb3d90104f174138b5fa&scene=58&subscene=0#rd
source: FuzzWiki
date: 2025-01-13
fetch_date: 2025-10-06T20:17:22.788363
---

# Bleem: 面向数据包序列的协议模糊测试 | 技术进展

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JchE46RGRlqhicVN0NtrttGjpBl7ytA2Pia0jdmg261Dboom7PsUVSXunQIOCHeq7dCK8gicP1CVRndQL1a1EHt5A/0?wx_fmt=jpeg)

# Bleem: 面向数据包序列的协议模糊测试 | 技术进展

FuzzWiki

![](https://mmbiz.qpic.cn/mmbiz_gif/JchE46RGRlr92CPaC2cSiaTUCEWwOd0OucLNLlY09jGCso4gTL4BmXsBNsvOlSMv9qPopLaecg7r21KD4gBERqA/640?wx_fmt=gif)

**基本信息**

**原文名称：**Bleem: Packet Sequence Oriented Fuzzing for Protocol

Implementations

**原文作者：**Zhengxiong Luo; Junze Yu; Feilong Zuo; Jianzhong Liu; Yu Jiang; Ting Chen; Abhik Roychoudhury; Jiaguang Sun；

**原文链接：**https://www.usenix.org/conference/usenixsecurity23/

presentation/luozhengxiong

**发表期刊：**USENIX Security Symposium 2023

**一、引言**

协议安全是网络通信安全的基石。由于网络协议常直接暴露于网络环境之中，其必须妥善处理各种潜在的恶意威胁。尽管传统协议模糊测试工具已广泛应用于协议漏洞的检测中，并揭示了众多安全隐患，但它们仍具有一些局限性。

首先，当前的数据包生成策略效率较低且资源浪费较多。传统模糊测试工具，诸如Peach，依赖于预定义模型生成数据包，缺乏实时的程序状态反馈机制。这意味着测试工具无法即时获知生成的输入是否触发了新的程序行为或引起了状态变化，从而限制了检测效能的提升。随后兴起的基于覆盖率反馈的模糊测试方法，虽然弥补了这一不足，却也带来了新的挑战：（一）这些反馈机制往往要求修改源代码或二进制文件，当协议实现是黑盒时可能是不可行的；（二）一些协议的特定验证规则可能会使现有的进化过程无效。例如，一些常见的协议，如TLS、DTLS和SSH，在握手过程中使用随机的中断，以防止“重放攻击”。在这种场景中，在之前探索中保留的有价值的输入可能不再重现有趣的行为。

此外，由于协议是有状态的，有效地遍历巨大的状态空间并覆盖各种状态转换需要精心设计的数据包序列。然而，构造这样的数据包序列并不简单，因为它涉及到复杂的协议逻辑。

因此，针对于上述问题，作者提出了一种面向数据包序列的黑盒模糊测试工具BLEEM以解决上述问题，在如下两方面做出了创新：

(1)首先，作者提出了一种新的动态反馈机制。该反馈机制在运行时会收集目标系统的数据包输出序列，分析其中蕴含的语义信息，从而抽象出系统内部的状态转换；

(2)其次，作者设计了系统状态跟踪图SSTG来指导数据包序列的生成。系统状态跟踪图能记录已经探索的状态空间，并能为达到未知状态提供指导；

**二、概述**

Bleem的基本框架如下图所示，主要由三部分组成：

(1) 被测系统（SUT）：网络协议通常遵循客户端-服务器模式。传统模糊测试在测试协议时，主要针对协议的一端。例如，为了测试协议的服务器端，传统fuzzer会充当客户端不断向服务器端发送数据包进行测试。而Bleem则将发送数据的双方视为一个整体。被测系统中一端发送的数据会先进入Bleem进行分析和处理，然后再发送给另一端。

(2) 反馈收集模块：反馈收集模块会先捕获SUT执行期间的数据包。然后，对包进行分析，提取其中的关键语义信息，之后，将数据包序列抽象成为一种包含客户端和服务器状态信息的序列，作为SUT的反馈传递给模糊测试引导模块。

(3) 模糊测试引导模块：模糊测试引导模块会将反馈的状态信息序列合并到系统状态跟踪图（SSTG）中，并通过设计的引导性的序列生成策略选择数据包中的变异位置和要应用的突变操作，生成新的数据包传递给接收端，以有效地探索状态空间。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PpFCwCIibjT80AnPjIO1mtRjlrEJFgS4NVPC0D5UEFoDLVZtyhRYxgMQ/640?wx_fmt=png&from=appmsg)

**图 1  Bleem流程概述图**

**三、反馈收集模块**

为了提高Bleem的反馈能力并使其能适应黑盒的场景，作者提出了一种基于被测系统输出获得系统反馈的方法，具体工作流程如图2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PxnrghRpSGBjNFAg3qSMsJcNZgLKGR7LUniacFnRc91DGXIuPn6hDs8A/640?wx_fmt=png&from=appmsg)**图 2 反馈收集工作流程**

过滤数据包序列：在模糊测试过程中，Bleem为了在系统捕获的流量中挑选出能表示SUT状态的数据包，会只考虑由被测系统发送出的数据包，过滤掉经过Bleem分析和处理后发送给被测系统的包。

数据包抽象： 为了表示SUT的状态，直接使用具体的数据包可能会造成混淆，因为有些字段，例如数据字段，与系统状态的关联很低。 因此需要提取出数据包中所携带的和被测系统状态相关的关键语义信息。作者通过对50多个协议的调查，发现枚举字段中的不同值通常代表不同类型的包或帧。因此，作者保留数据包中的枚举字段中值来表示该数据包，具体过程如图3所示。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2Pw9ibJBu5ibkqshQzqEsr6YtwW2hW4dBQmpF23ib08szMvBm21mumxFfNQ/640?wx_fmt=png&from=appmsg)

**图 3 数据包抽象**

数据包处理：为了方便构建状态跟踪序列以及准确的表示被测系统当前状态，作者将来自同一发送端在未接收到另一端发送的下一数据包前的相邻抽象数据包合并在一起，得到该发送端的当前状态ω。

构造状态跟踪序列：对于一个抽象数据包序列 π: {ω1,ω2,...,ωn}，单个抽象数据包还不足以描述整个系统的当前状态，为此，作者构造了 < T1(ω1) | T2(ω2)>来代表T1发送ω1响应T2发送的ω2请求，通过将被响应的数据包和当前发送的数据包作为一个整体来描述系统的当前状态，具体过程如图4所示。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PoNmhQ5iaicgdjic8WGnqgiaUjiasm639qRXl9xBRNfCVRmAGWVfVOK4t6hw/640?wx_fmt=png&from=appmsg)

**图 4 构造状态跟踪序列**

**四****、模糊测试引导模块**

系统状态跟踪图(SSTG)：系统状态跟踪图将会记录被测系统的状态转换过程，以及在这个过程中所使用的突变操作序列。P⊕σ就可以表示为使用突变操作σ对数据包P进行变异所产生的包，其将视为系统状态转换的条件。系统状态跟踪图是不确定性有限自动机（NFA）的一个变体，可以用5元组(Q,q0,Ω,Σ,∆)表示。其中Q是SUT状态的有限集合，q0是初始状态，Ω是一个抽象数据包的字母表，Σ是一组突变算子，∆定义了一个转换函数Q× {Ω⊕Σ} →P(Q)，具体如图5所示。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PP2IBVicXTicIEKtiamwLExpVFONAj4x5OibbYK1USKqIfd9vKKPv9x8qfg/640?wx_fmt=png&from=appmsg)

**图 5 系统状态跟踪图**

序列生成引导：为了根据反馈信息全面的探索被测系统，作者设计了相应算法来对序列生成进行引导，具体算法如图6所示。作者利用所提出的突变算符（第1-4行）来压力测试每个具有不同输入的SSTG状态。具体来说，对于每个SUT状态转变中发送的基础包α,Bleem将选择一个之前未选择的突变操作符σ构造一个不同的包模式α⊕σ作为测试输入。在遍历完SSTG后，将转向低密度区域来促进对SSTG的全面遍历。从初始状态（第7行）开始，然后循环运行，直到达到结束状态（第8行）：在每个步骤中，在相应状态的可用转换中选择基于执行次数确定的优先级中最高的一个变异操作（第9行），记录相应包模式（第10行），然后进行此转换（第11行）。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PtXFRdeaZ1WufM8bbZdzzA4FuD9T0PCRhhtfYJ4Nfw65OViaaIUzB6ibA/640?wx_fmt=png&from=appmsg)

**图 6 引导算法**

变异操作：作者设计了包级别的变异操作和序列级别的变异操作来完成对数据的变异。包级别的变异将在给定的数据包中随机选择几个字段，并根据字段类型进行相应的突变操作。序列级别的变异包括数据包的重复和数据包顺序的修改。

**五、实验设计及结果**

**(一). 实验设置**

作者选取了部分常见的开源协议（如图7）和一些主流物联网制造商的固件使用中所包含的协议作为测试目标。作者选择了学术界和工业界广泛使用的三个著名的黑盒协议模糊器作为黑盒方案的基准，包括Peach、BooFuzz[2]和Snipuzz[3]。此外，为了证明BLEEM的有效性，也选择了AFLNet[4]和SGFuzz[5]这两种最先进的集成了覆盖和状态反馈的灰盒协议模糊测试工具进行比较。由于固有的随机性，模糊测试性能会有一定程度的波动，因此作者在每个选定的项目上使用了24小时的时间预算来运行每个模糊测试工具，并重复了每个24小时的实验10次。为了公平起见，每个模糊测试活动都在一个配置有1个CPU核心和1G RAM的Docker容器上运行。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PkHIV3T5SF1cianiapPV9oRxVkFHx0c8jLMiaeSYdriaC5oibc9dCS7S8Bsw/640?wx_fmt=png&from=appmsg)**图 7 选择的开源协议**

**(二). 具体实验**

**实验一：覆盖率分析**

图8显示了服务器端被不同的模糊测试工具所覆盖的分支数量。在24小时内，BLEEM的分支覆盖率分别比Snipuzz、AFLNet、SGFuzz、BooFuzz和Peach分别高40.3%、35.7%、23.4%、48.9%和28.5%。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PFicA9tgb2vfIX4zeot1L94uBibuJFETAuHM55k2kyMhFObMYZGCVicaLA/640?wx_fmt=png&from=appmsg)**图 8 覆盖率统计**

**实验二：bug发现能力**

开源方面，作者使用AddressSanitizer和UndefinedBehaviorSanitizer（也称为ASan和UBSan）报告的唯一漏洞数量作为统一指标。BLEEM已经在几个广泛使用的知名协议中检测到了15个新的漏洞，并在分配了10个CVE标识符。图9总结了BLEEM以及其他模糊测试工具发现的漏洞。具体来说，Peach、BooFuzz、AFLNet、SGFuzz和Snipuzz分别发现了8个、5个、6个、7个和5个漏洞，而且都是BLEEM发现漏洞的子集。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PGHkmHCMBG2Fbib0M9NdFamUZeq2cnhZ7mfRWbZbfcCiajRoSMTMBlsVw/640?wx_fmt=png&from=appmsg)**图 9 发现开源协议未知bug的数量**

闭源方面，作者将Bleem与选定的黑盒模糊测试工具进行了比较，并使用网络相关的监视器通过端口探测检测服务的活跃性来发现崩溃。作者使用首次崩溃时间作为评估这些模糊测试工具漏洞检测能力的度量标准。如图10所示，与其他模糊测试工具相比，Bleem实现了最佳的CVE发现性能。Bleem和Peach都能找到所有这些CVE漏洞，而BooFuzz和Snipuzz分别只能找到3个和1个。平均而言，BLEEM至少比Peach、BooFuzz和Snipuzz分别快7.5倍、13.3倍和87.1倍发现崩溃，这证明了BLEEM相对于最新技术的效率提升。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PLW5D46gRo4ubc5xqgtujrficv6EkQrrj1XLv4cyBiaR6RgoXxRM1ClmQ/640?wx_fmt=png&from=appmsg)**图 10 发现闭源协议未知bug的数量**

**实验三：序列生成有效性的评估**

为了评估引导序列生成的有效性，作者实现了BleemRand，即Bleem的一个变体，用随机序列选择取代它，并保持SSTG结构不变进行比较。“Paths”列显示在SSTG构建过程中发现的唯一状态跟踪的数量；“Len”列显示这些路径的平均长度；“Types”列显示抽象数据包（连接后）的不同类型数量，它们是SUT状态的元素；“Nodes”和“Trans”列分别表示SSTG的状态和状态转换数量；“Branch Coverage”显示了整个SUT的已达到的唯一分支覆盖率，包括两侧的覆盖率。图11显示了每个指标的平均值。从图11的每一行来看，作者提出的SSTG的复杂性与数据包类型和所覆盖的唯一分支大致呈正相关，说明SSTG可以在一定程度上反映SUT的系统内部的执行状态。在引导序列生成策略的帮助下，Bleem平均比BleemRand多实现5.7%的独特分支，而且服务器上的改进通常与客户端上的提升程度基本一致。

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PfmOib2fs0Crza36CuU2kmOISG4BsRCeGzda2jQYSkqDjzEtyjQZfmqw/640?wx_fmt=png&from=appmsg)

**图 11 序列生成有效性的评估**

**六、总结**

作者提出了一个面向数据包序列的协议模糊测试工具，采用一种进化的方法来探索大量的协议状态空间。该工具通过分析输出序列来生成系统反馈，并通过所提出的引导模糊策略来动态调整探索方向。同时，BLEEM通过利用观察到的交互流量生成具有高度协议逻辑感知的数据包序列。与最先进的模糊测试工具相比，BLEEM可以在真实协议测试场景中实现更高的覆盖范围并检测更多的错误。并且BLEEM可以黑盒测试大多数通用的协议。

**—END—**

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrFxo5eqwR0gsfAItibNmfykKRSz1SvNIKndIPoSB9dQk8u1iaH2IcWlV4vR3Ov4uXgMibO6uPGRA2dQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqicsiaxDHZjSsKx6Eoahhic8tm1AUvF5TI33T7kuQmpqnP5HoOUicFhuIhrcXcyaZJzHJrYaLibPCZSRQ/640?wx_fmt=png)

[![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PmibrfZ4CAIiaRx4LOjASCwrRM18N7ibE0SzDVSl2NM2WgqR6A0ThwkFeg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU1NTEzODc3MQ==&mid=2247486850&idx=1&sn=dced461f84a7bc0c0fce0bc7d690ea72&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PwHcZyWaEwibFCdcFX3tXGOibx3Ge3NFKMV08Pica8ZwI6O1JmCaU3JKtA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU1NTEzODc3MQ==&mid=2247486836&idx=1&sn=e87ccea6ced6bd899720e4677398f497&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlqhicVN0NtrttGjpBl7ytA2PHpFVZGhkSDkxDCQzt0HBS1xS4IibywTic0jGHO1jBUurel6O6CFKw3ag/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU1NTEzODc3MQ==&mid=2247486803&idx=1&sn=325727c087e1cdfc1ec211b9dd3eec1d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/JchE46RGRlrFxo5eqwR0gsfAItibNmfyk5wLcpKFBfhV2gLHUvrA15ticyqNAUM2Nvak36LBpQmxVQdliabzKmaSg/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文
...