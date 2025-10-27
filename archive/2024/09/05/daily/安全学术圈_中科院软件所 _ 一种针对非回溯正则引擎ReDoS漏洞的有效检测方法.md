---
title: 中科院软件所 | 一种针对非回溯正则引擎ReDoS漏洞的有效检测方法
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491193&idx=1&sn=0b4f11ecd294dd99667d2b21ba9ec44b&chksm=fe2ee1f2c95968e4852df2a4c4f8252a9e40265645fc3c8b9dc391d8637dcca7d1d5d5ddabdb&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-09-05
fetch_date: 2025-10-06T18:26:56.633657
---

# 中科院软件所 | 一种针对非回溯正则引擎ReDoS漏洞的有效检测方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WG4b9LxSOhicB1fRz8ITbARUfnV47DBBa7QW75v5IRfMSZt9libgf7kDTV9CUL7BBED08hvf2DeV4kA/0?wx_fmt=jpeg)

# 中科院软件所 | 一种针对非回溯正则引擎ReDoS漏洞的有效检测方法

原创

苏韦豪

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WG4b9LxSOhicB1fRz8ITbARURkfprpc6kDHaiaBiaeVGrJ0gNSFqicEUUibP4tlW193HJXzNY8BhJGENvA/640?wx_fmt=png&from=appmsg)
> 原文标题：Towards an Effective Method of ReDoS Detection for Non-backtracking Engines
> 原文作者：Weihao Su and Hong Huang and Rongchen Li, Haiming Chen, Tingjian Ge
> 发表会议：USENIX Security '24
> 笔记作者：苏韦豪@软件所
> 原文链接：*https://www.usenix.org/conference/usenixsecurity24/presentation/su-weihao*

本次分享由`中国科学院软件研究所陈海明研究员`团队与`马萨诸塞大学洛厄尔分校葛廷健教授`合作完成的论文“Towards an Effective Method of ReDoS Detection for Non-backtracking Engines”。本文研究非回溯正则引擎的正则表达式拒绝服务（ReDoS）漏洞成因与检测方法。

# 1. 研究背景

正则表达式在计算机科学的诸多领域都得到了广泛应用。如今多数主流编程语言都原生或通过程序库支持正则表达式。近期研究指出30%到40%的Java、JavaScript以及Python项目都使用了正则表达式。然而正则表达式拒绝服务（ReDoS）攻击的风险在网络服务间广泛且严重：有实证研究指出现实项目中超过10%的正则表达式存在ReDoS风险；在2016年ReDoS曾导致Stack Overflow其服务在世界范围内中断34分钟；Cloudflare在2019年7月因使用回溯引擎导致其服务在世界范围内中断27分钟。ReDoS漏洞是由攻击者使用恶意输入触发正则引擎的超线性匹配时间导致。该恶意输入称作攻击串。

已有大量工作研究ReDoS漏洞正则的检测。然而目前工作多着眼于回溯引擎，甚至有研究工作认为非回溯引擎可以消除ReDoS漏洞的风险。Cloudflare在遭受服务中断后也采用RE2、Rust等非回溯引擎以取代回溯引擎试图消除ReDoS漏洞。非回溯引擎的ReDoS检测问题在很大程度上是一个未决问题。本文主要贡献有：基于复杂度理论给出非回溯引擎的ReDoS漏洞的`第一个系统性的成因分析`与提出具备在非回溯正则引擎上检测出`与回溯引擎同一量级的ReDoS漏洞`能力的检测算法。

正则表达式匹配算法大体可以分为两类：其一为`回溯算法`，该算法易于实现且易于扩展，在许多编程语言中广泛采用，例如.NET, Python, Perl, PHP, Java, JavaScript, and Ruby。但这类匹配算法可能导致关于输入串长度指数的算法时间复杂度。其二则基于经典的自动机理论，称为`非回溯匹配算法`。这类匹配器通常被认为较为迅速，但开发难度较高。对性能要求较高的工业应用如NIDS和微软的Credential Scanning均采用非回溯匹配器。非回溯匹配器近期还受到编程语言研究社区的较多关注，并在Go、Rust、.Net 7、JavaScript等编程语言中得到应用，以减轻ReDoS漏洞的风险。此外grep、awk、sed等Unix/Linux命令以及高性能正则引擎如Hyperscan也采用非回溯匹配器。

当代非回溯引擎多为复杂的软件系统，往往首先包括确定性有穷自动机（DFA）匹配器，一些还采用非确定性有穷自动机（NFA）匹配器，非回溯引擎如grep甚至使用回溯匹配器支持反向引用。根据DFA匹配器是否在匹配之前生成整个DFA，此类匹配器可以分为离线与在线DFA匹配器。此外不同引擎采用的自动机模型不尽相同，可以将非回溯引擎归类为: 1. 基于εNFA的引擎，如RE2、Go和Rust的正则引擎使用Ken Thompson的NFA构造法，Haskell的TDFA与RE2C扩展标签确定性有穷自动机（tagged DFA）；2. 基于位置的引擎，如GNU grep、sed、awk采用Alfred Aho提出的grep自动机，Hyperscan采用位置自动机的确定化，即McNaughton-Yamada自动机；3. 基于正则表达式推导的引擎：例如OCaml的正则库、.Net 7的Nonbacktracking引擎使用正则表达式的Brzozowski推导。主流非回溯引擎的分类见下表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WG4b9LxSOhicB1fRz8ITbARUkj83xQf63u9XiaiaPVYoia5via9CYPnP3w8WB7Yq2M93lnibrEHt7zFXcAQ/640?wx_fmt=png&from=appmsg)

在本文之前唯一关注非回溯引擎的安全性的工作是GadgetCA。该工作认为正则表达式的有界重复，或称为有界计数操作符，形如，会导致非回溯引擎上的ReDoS漏洞。然而GadgetCA采用的自动机模型只能处理一类受限的正则表达式，而对其不支持的正则表达式甚至可能输出错误结果。这导致GadgetCA的可用性非常受限。且由于其对非回溯引擎上的ReDoS漏洞成因的认知不全面，采用的实验评估指标不实际，非回溯引擎上的ReDoS漏洞检测问题仍未得到真正的解决。

# 2. ReDoS漏洞的复杂度理论分析

有界计数操作符既不是非回溯引擎上的ReDoS漏洞的唯一成因，也不是非回溯引擎上的ReDoS漏洞的直接成因。本文实验中在不同引擎上检出了数千个不含有界计数操作符但仍有ReDoS漏洞风险的正则表达式。本文首先给出正则表达式在给定正则引擎上有ReDoS漏洞的形式定义，然后从计算与描述复杂度理论出发，系统性地分析非回溯引擎上的ReDoS漏洞的成因。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WG4b9LxSOhicB1fRz8ITbARUlvhryYOH4vcmdujeFlWYiaYb5u4kEAZVp8r0TDWUO7HUiaZaUukBLN9g/640?wx_fmt=png&from=appmsg)

上图为正则表达式在给定正则引擎上有ReDoS漏洞的形式定义，即正则表达式在给定引擎上含ReDoS漏洞当且仅当存在一个字，其使得无法在关于长度的线性时间内判定是否属于描述的语言。ReDoS攻击是一类算法复杂度攻击，其成因首先依赖于引擎。

## 2.1. 匹配器与匹配函数的时间复杂度

以下用表示输入串长度，用表示NFA状态数。

**在线DFA匹配器有ReDoS风险.** 在线DFA匹配器最坏情况下对每个字节构造一个迁移，并记录在缓存中。Jean-Marc Champarnaud证明构造一个迁移需要()时间。使用Union-Find算法将其降低到(())，其中为Ackermann反函数。然而如果不构造迁移，在线DFA匹配器匹配一个字节只需要()时间，这也是非回溯引擎在非恶意输入上通常较回溯引擎表现更好的原因。综合而言，在线DFA匹配器最坏情况下至少需要()时间，此外还需加上关于NFA规模指数的检查状态缓存的开销。

**退化到NFA匹配器可以导致ReDoS.** 由于计数正则表达式的DFA最坏情况下有双指数规模，非回溯引擎通常为在线DFA匹配器设置状态缓存上限。如果缓存超过该上限（RE2设置为超过两次），非回溯引擎退化为使用NFA匹配器。Introduction to Automata Theory, Languages, and Computation一书认为NFA匹配算法需要()时间，Compilers: Principles, Techniques, & Tools一书则认为至少需要()时间。RE2、Rust正则引擎的开发文档中明确指出NFA匹配器是引擎中最慢的匹配算法，GadgetCA中也认为非回溯引擎退化到NFA匹配器造成ReDoS。

**匹配函数影响ReDoS.** 非回溯正则引擎中通常默认使用部分匹配函数，即检查正则是否匹配输入串的某一个子串。替换、匹配提取等函数功能均依赖于部分匹配函数实现。目前实现部分匹配有两种方式：其一在正则表达式左边添加。该方法易于实现，已被RE2、Nonbacktracking等引擎采用。但易证明存在一类正则表达式在这种实现下所对应的NFA的非确定性指数级增长。且这种方法无法确定部分匹配的起始点，替换、匹配提取等功能需要额外倒序匹配一遍。另一种方法可以确定起始点，但需要在输入的所有子串上重复()次部分匹配，时间复杂度最坏情况下至少达到。这种实现方式在ReDoSHunter中发现会导致回溯引擎的ReDoS漏洞。

## 2.2. 描述复杂度爆炸

ReDoS漏洞的描述复杂度分析研究正则表达式所对应的自动机的规模。这方面的分析可以根据经典的状态复杂度研究分为研究正则表达式、NFA、DFA之间转换的`转换状态复杂度`和研究不同操作符对正则表达式的DFA状态数影响的`操作状态复杂度`。

**确定化爆炸.** 转换状态复杂度研究最为经典的结果是对个状态的NFA使用子集构造法，最坏情况下得到的DFA有个状态。深包检测系统的实践中也有研究发现具有指数规模DFA的正则表达式导致程序的高时空间成本，这进而导致ReDoS。本文从描述复杂度理论研究中收集了一些具有关于其长度指数规模的最小DFA的正则表达式，并提出了若干新变体，如下表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WG4b9LxSOhicB1fRz8ITbARUnRcbZDloRicGeehxMRgXfrgXr07E0ljsx2IU23u8QI8L846Dolh87eQ/640?wx_fmt=png&from=appmsg)

**计数操作符.** 计数正则表达式在完备正则引擎实现中展开为最坏情况下规模的不含计数操作符的正则表达式。Wouter Gelade证明嵌套的计数操作符与确定化爆炸共同导致规模的DFA。此外本文证明了存在一类含计数操作符的正则表达式，其NFA状态的非确定度关于其长度成指数。

**字符类的离散表示.** 非回溯引擎遵循UTF-8标准编码字符类。由于UTF-8采用变长编码，许多字符类的自动机表示规模庞大，如UTF-8字符类\W在RE2中需要1441个状态的自动机以表示其语言。文中举例正则表达式(\W\D)在部分匹配函数中使用ASCII编码仅需80个状态，而使用UTF-8编码则需要678980个状态。因此一些引擎如grep放弃使用自动机编码UTF-8字符类，退化为更易触发ReDoS漏洞的回溯匹配器进行匹配，产生指数级ReDoS漏洞风险。

> 简而言之，本文的主要观点有：
>
> 1. ReDoS漏洞不仅与正则表达式相关，还与正则引擎、调用函数以及程序上下文相关。
> 2. 基于NFA、DFA的非回溯匹配算法的时间复杂度均非线性，无法消除ReDoS的风险。
> 3. 在线DFA匹配器不需构造新状态即可识别的字符不降低引擎效率。
> 4. 不同匹配函数与其实现方式都可能导致ReDoS。
> 5. 正则表达式的非确定性直接影响非回溯引擎识别字符的开销。
> 6. 正则表达式的描述复杂度直接影响非回溯引擎的空间复杂度。
> 7. 正则表达式的描述复杂度取决于正则表达式的非确定性与正则操作符的简洁性。
> 8. 正则操作符的简洁性可能增加正则表达式的非确定性。
> 9. 非回溯引擎的ReDoS漏洞的成因复杂，各类成因之间相互影响。ReDoS漏洞既无法被有穷地枚举为“漏洞模式”，也并非某些特定操作符的结果。

## 3. ReDoS检测

基于以上分析，本文将非回溯引擎上的ReDoS问题建模为-简单串问题，并提出一种带启发式策略的增量式确定化算法求解该问题，并产生攻击串。

### 3.1. 简单串

本文首次提出简单串的概念，其定义为：给定正则表达式与其DFA ，一个简单串是一个有穷字，其在上的路径仅含一个终结态且所有状态两两不同。

已有一些理论研究讨论有穷自动机的简单语言的描述复杂度并刻画其性质。正则表达式的简单串有如下性质：任意非空正则表达式的简单串集合非空；正则表达式的简单语言是无前缀语言；简单串在上的路径无环；表示正则表达式的简单语言的最小DFA的状态数可达到状态数的指数。注意不同DFA构造法可以产生互不包含的简单串集合，且不必要为最小DFA。

为刻画求最长简单串的难度，本文进而提出-简单串问题，即给定正则表达式与其DFA 是否存在一长度大于等于的简单串。本文证明了该问题为EXPSPACE-hard。

### 3.2. -简单串的增量式求解

朴素的离线-简单串求解算法由于DFA的双指数规模极不实际。本文以grep DFA（见下图）为例，展示了一种不需显式构造有穷自动机的在线算法，并加入以下策略提升其实际表现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WG4b9LxSOhicB1fRz8ITbARUs8ma9IAItmWCIFWNzPXEyI830bvZa3Sx9gwmO4mbRn2iakD7gYicB1bw/640?wx_fmt=png&from=appmsg)

(a) `非确定性引导策略`：状态的非确定度指从某一状态出发，对某符号可转移到的状态数目。非确定性是标准正则表达式DFA状态爆炸的根源。非确定性引导贪婪地选择具有最高非确定性的符号引导搜索过程，有效增加了攻击字符串的搜索效率。该策略选择的符号在下图中标绿。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WG4b9LxSOhicB1fRz8ITbARU6ysj4Tj6GMm2zD8YBCfia8wt48Du5pCuvwEic8FiaSuvqexgJVIt949BQ/640?wx_fmt=png&from=appmsg)

(b) `推广词典序策略`：本文推广线性化函数对正则表达式的字符类标号，使得每个grep DFA状态均包含一个有序多重集，本文利用多重集的支撑集定义一种状态之间的推广词典序。算法选择优先级高的状态作为后继，有效避免了优先探索可导致搜索提前终结的状态。该策略选择的状态在下图中标紫。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WG4b9LxSOhicB1fRz8ITbARUKRG5qoy97Me2NTuQ9w0nrf0iaAmQeRhaknRcwibITc5fATgcic7fViarJg/640?wx_fmt=png&from=appmsg)

(c) `非完备非时序回溯`：在前两个策略都失效后，算法保留失效状态位置。如果此后经过一定步数的探索，新的DFA状态未能大量增长，搜索直接回溯到失效位置并选择其他分支继续搜索，从而探索其他更有效的分支。这个策略牺牲了算法的完备性，但提升了求解效率。该机制回退的行为在下图中标绿。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WG4b9LxSOhicB1fRz8ITbARUSrHYnibiaQqg5bPDK508ibzcG4iazSG5Luic9Nhsiaqb9xib3wW1JaDPWj2EQ/640?wx_fmt=png&from=appmsg)

# 4. 实验结果

本文主要采用的数据集由736535个语法不等价的现实世界正则表达式组成，命名为`SET736535`。其数据来源包括ReDoS研究中常用的数据集、Davis等从现实项目中抓取的大规模正则表达式数据集、Maven等代码仓库中抓取的现实正则表达式数据集和网络入侵检测系统的规则集。

本文提出了两种指标以评估ReDoS影响。先前研究未对评估标准形成共识，Davis等人的实证研究以100K-1M`字符`消耗引擎1s-10s作为存在ReDoS漏洞的标准，此外还有以多次重复中缀组成攻击串消耗回溯引擎1s作为评估标准的工作。由于UTF-8标准下，一个`字符`可以对应4个字节，这些标准都不够精确。本文提出以与机器相关的`正则引擎的吞吐率`和与机器无关的`DFA状态数`作为有潜在ReDoS漏洞的评价标准，并将回溯与非回溯引擎在同一指标下评价，以在非回溯正则引擎上检出与回溯引擎同一量级的的ReDoS漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WG4b9LxSOhicB1fRz8ITbARUgjyw8E4uDXxOSCMVkN8ntc0e03Og9gJdt5B65235UUvUVTJKz8UPKA/640?wx_fmt=png&from=appmsg)

表5展示本文提出的检测工具EvilStrGen与目前最为先进的检测工具在大规模现实正则表达式的数据集上的实验数据。实验表明，EvilStrGen在非回溯引擎和回溯引擎上均表现出先进的漏洞检测能力。实验结果还表明-简单串在回溯引擎上也具备一定揭露ReDoS漏洞的能力。此外Hyperscan在GadgetCA文中认为无懈可击，然而EvilStrGen找到了2327个可能触发Hyperscan的ReDoS漏洞的正则。

表6与表7均展示SET736535中若干正则表达式子类上的性能。表6中列出的子类都是GadgetCA不支持的，但从表6的结果可以看出不同子类的正则表达式均有可能触发ReDoS，且含有离散字符类的正则表达式更易对Hyperscan造成威胁。表7使用的数据集`ABOVE20`（共8099个正则表达式）是GadgetCA原文实验采用的，其工具支持的，且有界计数操作符的上界总和大于20的正则表达式，是大规模数据集中含有计数操作符的一个真子集。结果说明在该数据集上EvilStrGen也具有显著更强的漏洞发掘能力。

# 5. 结论

本文提出了一种检测非回溯正则表达式引擎中的ReDoS漏洞的新方法，并展示了其在大规模真实世界基准测试中的优异性能。实验结果表明，本文提出的工具EvilStrGen不仅在非回溯引擎上表现突出，在回溯引擎上同样具备强大的漏洞检测能力。利用EvilStrGen，作者从GitHub上Rust和Go语言开发的高星和广泛下载的项目中识别了85个可能存在ReDoS漏...