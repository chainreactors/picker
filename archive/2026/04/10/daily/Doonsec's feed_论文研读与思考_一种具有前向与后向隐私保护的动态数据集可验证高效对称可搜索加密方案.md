---
title: 论文研读与思考|一种具有前向与后向隐私保护的动态数据集可验证高效对称可搜索加密方案
url: https://mp.weixin.qq.com/s/kCdci-TZBVHvnBtIdbJ-Dw
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:15:39.216783
---

# 论文研读与思考|一种具有前向与后向隐私保护的动态数据集可验证高效对称可搜索加密方案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIwxqM0J8IIqzgsQVoZamT0FnTfH7ZbThyNGYcVD4yibQvefbiaegf9Idrz2pPLrJIbpoBUL5HtsNwYCdQziaWudGaCUas6rxQUHgo/0?wx_fmt=jpeg)

# 论文研读与思考|一种具有前向与后向隐私保护的动态数据集可验证高效对称可搜索加密方案

Yue
Yue

玄枢战队-Arcane Hub

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

原文题目：A Veriﬁable and Efﬁcient Symmetric Searchable Encryption Scheme for Dynamic Dataset With Forward and Backward Privacy

原文作者：Xiaojie Zhu;Jiangcong Zhou;Yueyue Dai;Peisong Shen;Shabnam Kasra Kermanshahi;Jiankun Hu

期刊：IEEE Transactions on Dependable and Secure Computing

一、主要研究问题、目标及方法

1.1 论文的核心研究问题与研究动机

现有的对称可搜索加密（SSE）方案大部分假设云服务提供商（CSP）是诚实但好奇的，CSP会诚实且正确地执行协议，然而在实际应用中，CSP可能由于外部攻击、内部错误或自身利益，返回不完整、不正确甚至空的搜索结果。已经有很多研究来确保数据完整性以免受恶意CSP攻击，但仍存在以下两个大的方面的挑战：

①动态数据与隐私保护：大多数方案针对静态数据设计，当数据需要频繁插入或删除时，不完善的更新机制会泄露额外信息。例如，新插入或删除的文档可能与过往的搜索记录产生关联，从而破坏前向隐私或后向隐私，导致动态环境下的隐私保护变得非常脆弱。

②效率与系统实用性：许多方案的搜索时间与整个数据集的大小相关，导致搜索效率低下。客户端需要维护大量的状态信息，并非轻量级。搜索过程往往需要客户端与服务器进行多轮交互，无法实现非交互式搜索。此外，缺乏能够同时高效支持关键词检索和按文档标识符检索的灵活数据结构，限制了应用范围。

1.2 论文提出的关键方法、模型

针对上面的挑战，论文提出了两个层次化的关键方法，分别是Hexie与Jianding，并采用图字典分片技术进行优化。Hexie是基础动态可搜索加密方案，核心采用秘密共享技术隐藏索引条目，将每个关键词对应秘密拆分为与关联文档数量匹配的秘密分片，文档存储对应分片，客户端仅保留最后一个分片用于动态更新，通过伪随机函数、伪随机置换、对称加密与哈希函数构建加密索引，同时设计正向与反向索引的并行更新、陷门生成、搜索与解密流程，实现动态数据增删、非交互搜索与轻客户端负载。

Jianding是Hexie的可验证扩展方案，核心创新是将链式消息认证码（MAC）结构与秘密共享结合，每次数据更新时，不仅生成密文，还会为当前密文块计算一个MAC值，该值依赖于前一个密文块的MAC，从而形成一条不可篡改的认证链。客户端仅需存储每个关键词对应的最终MAC值。搜索完成后，客户端可逆序验证整个结果链的MAC，从而确保搜索路径与结果的完整性和正确性，并能有效检测恶意CSP返回的空结果、不完整或篡改的结果。

1.3 效率优化方法

为了提升方案在多服务器分布式环境下的搜索效率与可扩展性，论文提出了基于图结构的字典分片算法。每个关键词代表一个顶点，节点之间的边表示两个关键词是否出现在同一文档中，边的权重代表两个节点同时出现在不同文档中的频率。将问题转化为在n个节点中寻找|S|个聚类。

研究对服务器数量限制、服务器容量配置、工作负载均衡及响应时间这四个关键因素进行了综合考虑。如图1所示，（a）给出的是图划分实例，通过分析发现频繁同步出现的关键词更可能被存储在同一台服务器上。对于服务器容量限制，采用递归式地裁剪最远端节点，被裁剪节点将合并至邻近集群。如（b）所示，紫色集群中的一个节点被裁剪并合并至附近的红色集群。该流程可对每个集群重复应用，直至所有集群均满足服务器容量要求。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIwACjNDwXaCpjZIRjcdcfKW0rugb3l1o0PF7KnFyJ4cD6ZNuO8YGydialtUQ4ez9q1fGtVenqdaZsq86AuZoiap3AGfmXBCLIKzA/640?wx_fmt=png&from=appmsg)

图1

若某个集群负载过重，则需在集群间进行负载均衡。（c）中存在两种负载均衡方案：节点复制与节点置换。当剩余存储空间充足时，可将繁忙集群的节点复制至闲置集群，从而有效降低繁忙集群的工作负载；若存储空间不足，则可将当前集群的部分节点替换为闲置集群的节点。

二、主要发现、结论及创新点

2.1 论文的核心结果与主要发现

通过系统的实验评估，在搜索效率上，Hexie和Jianding方案显著优于现有方案。当匹配文档数达1024个时，检索单条目的耗时仅约0.03毫秒，比FPVSSE方案快1.6倍以上，比FVTSSE方案快82倍，比经典方案Sophos快520倍。在更新效率上，处理5千万条记录时，Hexie比Sophos快21.5倍。同时，基于图的字典分片使搜索效率进一步提升约一倍。安全性方面，形式化分析证明Hexie方案在随机预言机模型下满足自适应安全，并达到后向隐私Type-II等级。

2.2 作者得出的关键结论

作者得出结论，他们首次提出了一种支持动态数据集的SSE方案，该方案具备前向与后向隐私保护、非空/空搜索结果完整性验证、高效搜索、非交互式设计、轻量级客户端以及前向与后向索引功能。

为支持动态数据集，首先提出Hexie SSE方案，该方案不仅实现了前向隐私与后向隐私保护，还具备高效搜索、非交互式操作及轻量级客户端特性。

针对空搜索结果、不完整结果或错误结果的鲁棒性问题，提出Jianding SSE方案。此外，通过字典分片技术提出了一种提升搜索效率的方法，并评估了所提方案的有效性。

2.3 研究的贡献

（1）提出了首个DSSE方案（Hexie），该方案能够同时支持前后向隐私保护、对非空及空搜索结果的完整性验证、高效搜索、非交互式检索加密文档标识符、具备高效查询生成能力且客户端存储需求低的轻量级客户端，以及前向与后向索引功能。

（2）为增强对空结果、不完整结果或不准确搜索结果的抵御能力，研究提出对Hexie协议进行扩展，命名为Jianding。该扩展方案通过将链式MAC结构与秘密共享系统相结合，使客户端能够验证搜索结果的完整性。

（3）客户端只需存储一个秘密份额，这与基于计数器的最佳动态SSE方案具有可比性且所需计算量显著减少。

（4）为提升搜索效率，提出了一种基于图结构的字典分片机制，该机制综合考虑了服务器数量、服务器容量、工作负载均衡及响应时间等约束条件。

（5）对所提出的方案进行了形式化安全性分析，并证明该方案能够实现设计目标。此外，通过全面实验评估了所提出的方案及字典分片解决方案，结果表明两种方法均具有显著有效性。

2.4 与已有工作的对比

与现有的SSE方案相比，如表1所示，现有的发方案仅支持部分功能，比如Sophos支持动态性但无验证、FIDES支持动态与隐私但客户端负载高、FPVSSE支持验证但无完整索引、VSPS支持验证但无动态性，而Hexie与Jianding实现所有核心功能的融合。隐私保护层面，论文提出的方案同时实现前向隐私与II型后向隐私。验证能力层面，传统方案仅能验证非空结果，无法抵御恶意空结果攻击，Jianding通过链式MAC可同时验证空与非空结果。效率层面，现有方案多依赖高开销密码操作，搜索复杂度与数据集总规模相关，论文方案复杂度仅与匹配文档数相关，效率提升数十至数百倍。

表1

![](https://mmbiz.qpic.cn/mmbiz_jpg/q6TQOF8qUIxwwvz5UnZsQZicvsShL4J3cnNVAzayv6dYGedfxaW6MXD9iaqib78kR5ichhiceWmzBsDgjaKfpOibibBmDR87TBsmdecsgexiay0tKQo/640?wx_fmt=jpeg)

（dynamism：动态性；integrity of search result：搜索结果的完整性；robust against malicious empty search result：抵御恶意空搜索结果的能力；forward index：前向索引；SE：搜索效率；RT：往返效率；UE：更新效率；QGE：查询生成效率；FP：前向隐私；BP：后向隐私）

（N、D以及w分别表示关键词总数文档对、文档总数、数据集中不同关键词的总数。![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIyESPNAtRb421KJIogrzyWBlbMuldsCibSGN1ykr1bria4E24dvxDbNf4oh02FFSjeQje2qJZgCsa7UvjrmDPOgeWudMh7J0xhuI/640?wx_fmt=png)和 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIx1gv5p7agZGE2ic1G921RGiaSJcFA5euKevkAUoWNS7cD8Ma5pV7B0SQW1F2RNQu0f4R8ibak4MVyu0fGCt8usyZCDYsziaysia7qM/640?wx_fmt=png) 分别表示关键词w的更新总数及匹配文档总数。s表示并行线程数。\*表示在结果隐藏方案中检索匹配文档标识符所需的往返次数。）

[7] R. Curtmola, J. Garay, S. Kamara, and R. Ostrovsky, “Searchable symmetric encryption: Improved deﬁnitions and efﬁcient constructions,” J. Comput. Secur., vol. 19, no. 5, pp. 895–934, 2011.

[10] R. Bost, B. Minaud, and O. Ohrimenko, “Forward and backward private searchable encryption fromconstrained cryptographic primitives,” inProc. 2017 ACM SIGSACConf.Comput.Commun. Secur., 2017, pp. 1465–1482.

[28] S.-F. Sun et al., “Practical non-interactive searchable encryption with forward and backward privacy,” in Proc. Netw. Distrib. Syst. Secur. Symp., 2021, 1–18.

[30] J. GharehChamani, D. Papadopoulos,C. Papamanthou, andR.Jalili, “New constructions for forward and backward private symmetric searchable encryption,” in Proc. 2018 ACM SIGSAC Conf. Comput. Commun. Secur., 2018, pp. 1038–1055.

[31] C. Guo, W. Li, X. Tang, K.-K. R. Choo, and Y. Liu, “Forward private veriﬁable dynamic searchable symmetric encryption with efﬁcient conjunctive query,” IEEE Trans. Dependable Secure Comput., vol. 21, no. 2, pp. 746–763, Mar./Apr. 2024.

[32] D. Yuan, S. Cui, and G. Russello, “We can make mistakes: Fault-tolerant forward private veriﬁable dynamic searchable symmetric encryption,” in Proc. IEEE 7th Eur. Symp. Secur. Privacy, 2022, pp. 587–605.

[33] R. Bost, “ o ϕ oς: Forward secure searchable encryption,” in Proc. 2016 ACM SIGSAC Conf. Comput. Commun. Secur., E. R. Weippl, S. Katzenbeisser, C. Kruegel, A. C. Myers, and S. Halevi, Eds, Vienna, Austria, Oct. 24-28, 2016, pp. 1143–1154, doi: 10.1145/2976749.2978303.

[34] R. Bost, P.-A. Fouque, and D. Pointcheval, “Veriﬁable dynamic symmetric searchable encryption: Optimality and forward security,” IACR Cryptol. ePrint Arch., Rep. 2016/62, 2016.

[35] J. Zhu, Q. Li, C. Wang, X. Yuan, Q. Wang, and K. Ren, “Enabling generic, veriﬁable, and secure data search in cloud services,” IEEE Trans. Parallel Distrib. Syst., vol. 29, no. 8, pp. 1721–1735, Aug. 2018.

[36] Z. Zhang, J. Wang, Y. Wang, Y. Su, and X. Chen, “Towards efﬁcient veriﬁable forward secure searchable symmetric encryption,” in Proc. Eur. Symp. Res. Comput. Secur., Springer, 2019, pp. 304–321.

[37] X. Ge et al., “Towards achieving keyword search over dynamic encrypted cloud data with symmetric-key based veriﬁcation,” IEEE Trans. Dependable Secure Comput., vol. 18, no. 1, pp. 490–504, Jan./Feb. 2021.

三、实验结果与性能分析

3.1 研究设计与实验设置

论文严格形式化了系统安全模型，并基于标准密码学原语构建方案，给出了形式化安全证明。在实验层面，使用Python实现，并在本地机与云服务器上部署测试。

3.2 数据集特点

研究采用公开的Enron邮件数据集，这是可搜索加密领域的标准测试集。为测试方案的可扩展性，作者基于该数据集构建了5组不同规模的子数据集，数据条目数从五千条到五千万条不等，覆盖率从中小规模到超大规模的应用场景。

3.3 性能对比

（1）Hexie与Jianding方案评估

研究选用表2中的数据集，分别从搜索效率评估，更新效率评估，陷门生成效率评估，设置效率评估四个方面进行了评估。

表2

![](https://mmbiz.qpic.cn/sz_mmbiz_png/q6TQOF8qUIyhrExxia73ibo8NL7saHuCiadnO1MrcTAHibsMwS5UxMh3ic7ZibR8Z5J0xDcmJZvicJ5QejxZ2ibMKNpAfaibcUTPa22aF04henAaFjY4/640?wx_fmt=png)

如图2所示，（a）展示了检索单个展示了检索单个关键词的平均时间成本。Hexie和Jianding相较于FVTSSE、FPVSSE、FPVSSE-Ex及Sophos展现出更优的检索效率。随着匹配条目数量的增加，Hexie和Jianding的性能优势愈发显著。（b）中实验结果表明Hexie和Jianding的更新效率相较于其他方案具有显著性能优势。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIw5thdibo5fSBDZibSoBQWyQTVn4fgb7SAQW4TaYicl99CLzPiakAYewuIZHdqxTuMu1bvdp3MRhOqhNqNtm0xssa0NfzCfD7iaQDwo/640?wx_fmt=png)

图2

图（c）展示了生成单个陷阱门的平均时间成本。尽管Hexie和Jianding方案的陷阱门生成效率略优于其他方案，但所有方案的生成开销均呈现相近趋势。从（d）得出，Hexie、Jianding、FVTSSE、FPVSSE和FPVSSE -Ex的初始化效率表现相近，而Sophos的效率则明显偏低。这是因为Sophos需要生成RSA私钥和公钥，而其他五种方案仅需初始化空字典和变量即可完成初始化过程。

（2）词典分区方案评估

针对词典分片评估，论文从词典分片技术影响评估、工作负载均衡效果评估、关键词选择影响评估三个方面设计了三项实验。图3展示了关键词搜索平均耗时数据。对比分析表明，相较于未采用词典分片算法的基准方案，应用本算法的Jianding系统搜索速度提升了约两倍。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIxfTlfumooNlUz6oBYYYPFMGVhwJYEh7icazncMzib7ziaFDD8JTibWgvWHQlxaVPOVDaR4YibbUJTOPQ1UlEtPcvOycibdibhYj0P5gA/640?wx_fmt=png)

图3

图4显示，采用工作负载均衡方案的Jianding平台在完成关键词搜索操作时耗时显著缩短。

![](https://mmbiz.qpic.cn/mmbiz_png/q6TQOF8qUIzvYIG3J96vIkQZuzatnr7oRnPSLATkVVa7MHnGJf0xZuVn8GSTiaCyKicNvwBMic3joWwtH8...