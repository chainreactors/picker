---
title: IGP灵活算法反向亲和力约束
url: https://mp.weixin.qq.com/s/5L40RYktozTqXEoD-8Xtsg
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T06:01:13.632167
---

# IGP灵活算法反向亲和力约束

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YY73GMUZ1NnG9fVUwjeOEaYp6lXibWt6YW6McjE3A1l263BNy8YHUZiab4kibPomia9OmiaOSPSEIp7GDh1t4bZ9WTQKDeXKL8VcuxuVTwlCFXMA/0?wx_fmt=jpeg)

# IGP灵活算法反向亲和力约束

衡水石头哥
衡水石头哥

铁军哥

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

```
RFC9917：IGP Flexible Algorithms Reverse Affinity Constraint，January 2026
```

梗概

IGP灵活算法（Flex-Algorithm）能够计算IGP域内基于约束的路径，允许运营商根据管理策略影响路径选择。本文档定义了Flex-Algorithm的扩展，允许根据与计算中的路径反向相关的管理组（也称为链路亲和属性）在路径计算中包含或排除链路。

本文档通过引入新的IANA注册表来更新RFC 9350和9843，该注册表指定了用于在Flex-Algorithm路径计算期间从拓扑中修剪链路的有序规则集。

本备忘录的状态

这是一份互联网标准跟踪文档。

本文档是互联网工程任务组（IETF）的产品。它代表了IETF社区的共识。它已接受公众审查，并已被互联网工程指导小组（IESG）批准发布。有关互联网标准的更多信息，请参阅RFC 7841第2节。

有关本文档当前状态、任何勘误表以及如何提供反馈的信息，请访问https://www.rfc-editor.org/info/rfc9917。

版权声明

版权所有（c）2026 IETF Trust和文档作者。版权所有。

本文件受本文件发布之日生效的BCP 78和IETF信托与IETF文件相关的法律规定（https://trustee.ietf.org/license-info）的约束。请仔细阅读这些文件，因为它们描述了您与本文件相关的权利和限制。从本文档中提取的代码组件必须包括《信托法律条款》第4.e节中所述的修订版BSD许可证文本，并且不提供修订版BSD许可证中所述的保证。

1、简介

历史上，IGP协议仅根据分配给链路的IGP度量来计算网络上的最佳路径。 [RFC9350] 中指定的IGP FlexAlgorithm允许IGP计算基于约束的路径。已经定义了在Flex-Algorithm路径计算期间包含或排除链路的几种机制：

\* 根据特定管理组的存在来包含或排除链路 [RFC9350]

\* 基于特定共享风险链路组（Shared Risk Link Group，SRLG）存在的链路排除 [RFC9350]

\* 基于最小带宽的链路排除 [RFC9843]

\* 基于最大延迟的链路排除 [RFC9843]

本文档扩展了IGP Flex算法，添加了基于与最短路径优先（Shortest Path First，SPF）计算反向相关的管理组的路径中包含或排除链路的附加约束。

本文档通过创建新的IANA注册表来更新 [RFC9350] 和 [RFC9843]，该注册表指定了用于在Flex-Algorithm路径计算期间从拓扑中修剪链路的有序规则集（请参阅第12.3.1节）。

本文档中的术语OSPF用于涵盖OSPFv2和OSPFv3协议。

2、需求语言

本文档中的关键字“必须”、“不得”、“必需”、“应”、“不应”、“应该”、“不应该”、“推荐”、“不推荐”、“可以”和“可选”当且仅当它们出现在所有内容中时，应按照BCP 14 [RFC2119] [RFC8174] 中的描述进行解释。

3、用例示例

灵活算法定义（Flexible Algorithm Definition，FAD）可以指定操作员使用的扩展管理组，以在灵活算法路径计算期间包含或排除链路 [RFC9350]。这些链路扩展管理组在SPF计算的路径方向上进行检查，例如，在从根顶点到距离增加的顶点的方向上。

在某些情况下，评估与链路反向相关的扩展管理组而不是仅评估路径计算方向上的扩展管理组是有益的。考虑表示为两个节点A和B之间的一对有向边的点对点链路。在计算从A到B的路径时，诸如链路上的输入错误之类的问题（只能在接收节点B处检测到）可能在操作上很重要。操作员可能会监视节点B上的循环冗余校验（Cyclic Redundancy Check，CRC）错误或其他与输入相关的故障等指标，并在定义的观察期内应用阈值。如果超过这样的阈值，节点B可以在本地向从B到A的方向上的链路分配特定的扩展管理组。

为了适应这种操作意图，在路径计算期间评估正向边（从A到B）时，可以扩展Flex算法以检查反向边（从B到A）的扩展管理组。这样可以根据在链路远端检测到的情况从计算的拓扑中排除链路，从而提高网络可靠性和策略控制。

4、部署注意事项

必须小心地对链路扩展管理组进行基于阈值的设置，以避免过度泛洪和持续的FlexAlgorithm路径重新计算。

一种可能的方法是在链路上设置和取消设置扩展管理组时使用两个不同的阈值。例如，当根据某些传入错误的百分比设置链路上的扩展管理组时，使用较高的阈值进行设置，而使用较低的阈值取消设置链路上的扩展管理组。

许多实现提供了一种抑制机制，该机制限制在IS-IS情况下的链路状态PDU（Link State PDU，LSP）或在OSPFv2和OSPFv3的情况下链路状态通告（Link State Advertisement，LSA）在发起者处更新的速率。这种机制通常不特定于任何特定链路属性，而是考虑LSP或LSA中的任何变化。应用这种限流机制还可以避免频繁改变链路上扩展管理组的设置而影响接收端的稳定性。

5、IS-IS灵活算法排除反向管理组子TLV

IS-IS灵活算法排除反向管理组（Flexible Algorithm Exclude Reverse Admin Group，FAERAG）子TLV用于通告在第11节中指定的灵活算法路径计算期间使用的排除规则。

IS-IS FAERAG Sub-TLV是IS-IS FAD Sub-TLV的子TLV。它具有以下格式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YY73GMUZ1NkqOfrUooncnC3ynB7rsS3PoHkto41icnibpXXnhCGlibcPube8GgkqrxcEKEwgv1SnwoleqqIRGicCvHU73dYpkaAiaEZEZYiaPwkak/640?wx_fmt=png&from=appmsg)

其中：

Type：类型，1个八位字节，10

Length ：长度，1个八位字节，可变，取决于扩展管理组的大小。长度必须是4个八位字节的倍数。如果长度不是4个八位位组的倍数，则接收方必须忽略整个子TLV。

Extended Administrative Group：扩展管理组，[RFC7308] 中定义的扩展管理组。

IS-IS FAERAG子TLV不得在单个IS-IS FAD子TLV中出现多次。如果它出现多次，则IS-IS FAD SubTLV必须被接收器忽略。

对于给定IS的给定Flex算法，IS-IS FAERAG子TLV不得在FAD子TLV集中出现多次。如果它在这样的集合中出现多次，则必须使用来自给定IS的最低编号LSP中第一次出现的IS-IS FAERAG Sub-TLV，并且接收器必须忽略任何其他出现。

6、IS-IS灵活算法包括-任何反向管理组子TLV

IS-IS灵活算法包含任何反向管理组子TLV用于通告在第11节中指定的灵活算法路径计算期间使用的包含任何规则。

IS-IS灵活算法包含任何反向管理组子TLV的格式与第5节中的FAERAG子TLV的格式相同。

IANA已为IS-IS灵活算法包含任何反向管理组子TLV分配类型值11。

IS-IS灵活算法包括任何反向管理组子TLV不得在单个IS-IS FAD子TLV中出现多次。如果它出现多次，则IS-IS FAD Sub-TLV必须被接收器忽略。

IS-IS灵活算法包括任何反向管理组子TLV不得在来自给定IS的给定Flex算法的FAD子TLV集中出现多次。如果它在这样的集合中出现多次，则必须使用来自给定IS的最低编号LSP中第一次出现的IS-IS灵活算法包括任何反向管理组子TLV，并且接收机必须忽略任何其他出现。

7、IS-IS灵活算法包含所有反向管理组子TLV

IS-IS灵活算法包含所有反向管理组子TLV用于通告在第11节中指定的灵活算法路径计算期间使用的包含所有规则。

IS-IS灵活算法包含所有反向管理组子TLV的格式与第5节中的FAERAG子TLV的格式相同。

IANA已为IS-IS灵活算法包含所有反向管理组子TLV分配类型值12。

IS-IS灵活算法包含所有反向管理组子TLV不得在单个IS-IS FAD子TLV中出现多次。如果它出现多次，则IS-IS FAD Sub-TLV必须被接收器忽略。

对于给定IS的给定Flex算法，IS-IS灵活算法包含所有反向管理组子TLV不得在FAD子TLV集中出现多次。如果它在这样的集合中出现多次，则必须使用来自给定IS的最低编号LSP中第一次出现的IS-IS灵活算法包含所有反向管理组子TLV，并且接收器必须忽略任何其他出现。

8、OSPF灵活算法排除反向管理组子TLV

OSPF灵活算法排除反向管理组（Flexible Algorithm Exclude Reverse Admin Group，FAERAG）SubTLV用于通告在第11节中指定的灵活算法路径计算期间使用的排除规则。

OSPF FAERAG Sub-TLV是OSPF FAD TLV的子TLV。它具有以下格式：

![](https://mmbiz.qpic.cn/mmbiz_png/YY73GMUZ1Nmm49W3xx40rgJJy827FicuO1cWC9tzcvYD4OEkic68vU2gSialw2rpd5EyfTZXSicpX9dHicUjMtBvrMwMI63bAV5nwzVBPqwvpLMg/640?wx_fmt=png&from=appmsg)

其中：

Type：类型，2个八位字节，10

Length：长度，2个八位字节，可变，取决于扩展管理组的大小。长度必须是4个八位字节的倍数。如果长度不是4个八位位组的倍数，则接收方必须忽略整个子TLV。

Extended Administrative Group：扩展管理组，[RFC7308] 中定义的扩展管理组。

OSPF FAERAG子TLV不得在OSPF FAD TLV中出现多次。如果它出现多次，则OSPF FAD TLV必须被接收方忽略。

9、OSPF灵活算法包括任何反向管理组子TLV

OSPF灵活算法包含任何反向管理组子TLV用于通告在第11节中指定的灵活算法路径计算期间使用的包含任何规则。

OSPF灵活算法包含任何反向管理组子TLV的格式与第8节中的OSPF FAERAG子TLV的格式相同。

IANA已为OSPF灵活算法包含任何反向管理组子TLV分配类型值11。

OSPF灵活算法包括任何反向管理组子TLV不得在OSPF FAD TLV中出现多次。如果它出现多次，则OSPF FAD TLV必须被接收方忽略。

10、OSPF灵活算法包括所有反向管理组子TLV

OSPF灵活算法包含所有反向管理组子TLV用于通告在第11节中指定的灵活算法路径计算期间使用的包含所有规则。

OSPF灵活算法包含所有反向管理组子TLV的格式与第8节中的OSPF FAERAG子TLV的格式相同。

IANA已为OSPF灵活算法包含所有反向管理组子TLV分配类型值12。

OSPF灵活算法包含所有反向管理组子TLV不得在OSPF FAD TLV中出现多次。如果它出现多次，则OSPF FAD TLV必须被接收方忽略。

11、灵活的算法路径计算

以下过程通过引入基于与链路反向相关的管理组（Administrative Groups，AG）的附加约束来增强 [RFC9350] 第13节中定义的规则。

\* 检查FlexAlgorithm定义中是否有任何排除反向管理组规则。如果存在此类排除规则，请检查是否也在反向链路上设置了作为排除规则一部分的任何管理组。如果在反向链路上设置了此类管理组，则必须从计算中删除该链路。

\* 检查是否有任何包含反向管理组规则是Flex-Algorithm定义的一部分。如果存在此类include-any规则，请检查是否也在反向链路上设置了属于include-any规则一部分的任何管理组。如果在反向链路上没有设置这样的管理组，则必须从计算中删除该链路。

\* 检查Flex-Algorithm定义中是否有包含所有反向管理组规则。如果存在此类包含所有规则，请检查属于包含所有规则的所有管理组是否也在反向链路上设置。如果所有此类管理组都没有在反向链路上设置，则必须从计算中删除该链路。

有关这些新增规则，请参阅第12.3节中的规则8、9和10。

12、IANA考虑因素

12.1、用于灵活算法定义的子子TLV

IANA已在“IS-IS TLV代码点”注册表组下的“用于灵活算法定义子TLV的IS-IS子子TLV”注册表中注册了以下内容：

类型：10

描述：灵活的算法排除反向管理组

MP：n

参考：RFC 9917，第5节

类型：11

描述：灵活的算法包括任何反向管理组

MP：n

参考：RFC 9917，第6节

类型：12

描述：灵活算法包含所有反向管理组

MP：n

参考：RFC 9917，第7节

12.2、OSPF灵活算法定义TLV子TLV注册表

本文档在“开放最短路径优先（Open Shortest Path First，OSPF）参数”注册表组下的“OSPF灵活算法定义TLV子TLV”注册表中进行以下注册：

类型：10

描述：灵活的算法排除反向管理组

参考：RFC 9917，第8节

类型：11

描述：灵活的算法包括任何反向管理组

参考：RFC 9917，第9节

类型：12

描述：灵活的算法包括所有反向管理组

参考：RFC 9917，第10节

12.3、IGP Flex算法路径计算规则注册表

IANA已在“内部网关协议（IGP）参数”注册表组内创建了一个名为“IGP Flex算法路径计算规则”的新注册表。新注册机构的注册程序是专家评审[RFC8126]。第12.3.1节为指定专家提供指导。

“IGP Flex-Algorithm Path Computation Rules”注册表指定了一组有序规则，这些规则用于在Flex-Algorithm路径计算期间从拓扑中修剪链路。

注册表支持的规则数量没有上限。

在表1中，“FAEMB”表示“Flex算法排除最小带宽”，“FAEMD”表示“Flex算法排除最大延迟”。

![](https://mmbiz.qpic.cn/mmbiz_png/YY73GMUZ1NlvDJ1oCcYxf0EG3qw0RGQxNt9ksn2E67vLPdTzZIEAibLgGMwviamyB9IVWsjt4vvpJyDeGRuefLROc51d6Bib6SXm24BWOibfkNc/640?wx_fmt=png&from=appmsg)

表1：IGP Flex算法路径计算规则

12.3.1、指定专家指南

自最初的Flex-Algorithm规范 [RFC9350] 以来，许多FlexAlgorithm扩展已被提出并标准化。其中许多为Flex-Algorithm路径计算添加了额外的规则。维护这些规则的IANA注册表允许跨多个文档独立进行规范。新的“IGP Flex-算法路径计算规则”注册表已创建并在第12.3节中指定。

本节为指定专家提供评估“IGP Flex-算法路径计算规则”注册表中新注册的指南：

1. 当定义一个新的约束时，与该约束相关的规则可以插入到任何位置。向后兼容性得到保证，因为不支持新约束的节点将不会参与FAD指定它们不支持的约束的算法。

2. 现有规则的相对顺序不得改变。这样做可能会产生向后兼容性问题。

3. 不得删除规则。鉴于规则仅根据获胜FAD中携带的信息有条件地使用，因此没有必要删除规则。

4. 不得合并或重复规则。

13、安全考虑

本文档继承了 [RFC9350] 的安全注意事项。

14、参考文献

14.1、规范性参考文献

```
[RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997, <https://www.rfc-editor.org/info/rfc2119>.[RFC7308] Osborne, E., "Extended Administrative Groups in MPLS Traffic Engineering (MPLS-TE)", RFC 7308, DOI 10.17487/RFC7308, July 2014, <https://www.rfc-editor.org/info/rfc7308>.[RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017, <https://www.rfc-editor.org/info/rfc8174>.[RFC9350] Psenak, P., Ed., Hegde, S., Filsfils, C., Talaulikar, K., and A. Gulko, "IGP Flexible Algorithm", RFC 9350, DOI 10.17487/RFC9350, February 2023, <https://www.rfc-editor.org/info/rfc9350>.[RFC9843] Hegde, S., Britto, W., Shetty, R., Decraene, B., Psenak, P., and T. Li, "IGP Flexible Algorithms: Bandwidth, Delay, Metrics, and Constraints", RFC 9843, DOI 10.17487/RFC9843, September 2025, <https://www.rfc-editor.org/info/rfc9843>.
```

14.2、参考资料丰富

```
[RFC8126] Cotton, M., Leiba, B., and T...