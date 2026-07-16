---
title: 通过UDP/IP上的MPLS实现确定性网络（DetNet）数据包复制、消除和排序功能（PREOF）
url: https://mp.weixin.qq.com/s/5Ue2Ukvv48z6c1DGY_svLA
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:56:55.942168
---

# 通过UDP/IP上的MPLS实现确定性网络（DetNet）数据包复制、消除和排序功能（PREOF）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YY73GMUZ1NkgsX3GHz3iaCrKDf4U5sSp0DaQZnst4r473u0dLI7AWNSGkcLjZUaJyQCs2YI0xOiaYFWm3icHd9icsnmvmfdo3YsemibrLIt1wpQY/0?wx_fmt=jpeg)

# 通过UDP/IP上的MPLS实现确定性网络（DetNet）数据包复制、消除和排序功能（PREOF）

衡水石头哥
衡水石头哥

铁军哥

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

```
RFC9566：Deterministic Networking (DetNet) Packet Replication, Elimination, and Ordering Functions (PREOF) via MPLS over UDP/IP，April 2024
```

梗概

本文档介绍了DetNet IP数据平面如何支持基于为DetNet MPLS数据平面定义的现有MPLS PREOF解决方案以及MPLS-over-UDP技术定义的机制构建的数据包复制、消除和排序功能（Packet Replication, Elimination, and Ordering Functions，PREOF）。

本备忘录的状态

本文档不是互联网标准跟踪规范；其发布仅供参考。

本文档是互联网工程任务组（IETF）的产品。它代表了IETF社区的共识。它已接受公众审查，并已被互联网工程指导小组（IESG）批准发布。并非IESG批准的所有文件都是任何级别互联网标准的候选文件；请参阅RFC 7841第2节。

有关本文档当前状态、任何勘误表以及如何提供反馈的信息，请访问https://www.rfc-editor.org/info/rfc9566。

版权声明

版权所有（c）2024 IETF Trust和文档作者。版权所有。

本文件受本文件发布之日生效的BCP 78和IETF信托与IETF文件相关的法律规定（https://trustee.ietf.org/license-info）的约束。请仔细阅读这些文件，因为它们描述了您与本文件相关的权利和限制。从本文档中提取的代码组件必须包括《信托法律条款》第4.e节中所述的修订版BSD许可证文本，并且不提供修订版BSD许可证中所述的保证。

1、简介

DetNet工作组定义了数据包复制（Packet Replication，PRF）、数据包消除（Packet Elimination，PEF）和数据包排序（Packet Ordering，POF）功能（表示为PREOF），以通过DetNet服务子层 [RFC8655] 提供服务保护。PREOF服务保护方法依赖于通过多个最大不相交路径发送的同一数据包的副本，并使用排序信息来消除重复。 [IEEE8021CB]中描述了PRF和PEF的可能实现，[IEEE8021CBcv]中定义了相关的YANG数据模型。 [RFC9550] 中描述了POF的可能实现。图1显示了在从源转发到目标的过程中应用PREOF的DetNet流程。

![](https://mmbiz.qpic.cn/mmbiz_png/YY73GMUZ1NnplrrxkJasldRkxeGZhvDPC8dBNdU4U4QmK3URXwrBB89Bwcib9m8rN9gNzribiaR66wITicbQK4IVerDYVGsxA0bSOLrYlnqcq2A/640?wx_fmt=png&from=appmsg)

图1：DetNet网络中的PREOF场景

一般来说，使用PREOF需要将排序信息包含在DetNet复合流的数据包中。这可以通过添加序列号或时间戳作为DetNet封装的一部分来完成。测序信息通常在源处或附近添加一次。

DetNet MPLS数据平面 [RFC8964] 指定如何在MPLS标头中对排序信息进行编码。然而，[RFC8939]中描述的DetNet IP数据平面没有指定如何在IP数据包中编码排序信息。本文档向DetNet IP节点提供排序信息，因此产生了DetNet IP数据平面的改进版本。正如 [RFC8938] 所建议的，该解决方案使用现有的标准化标头和封装。该改进是通过重用DetNet MPLS-over-UDP/IP数据平面 [RFC9025] 并限制使用零F标签来实现的。

2、术语

2.1、本文档中使用的术语

本文档使用DetNet架构 [RFC8655] 中建立的术语，并且假设读者熟悉该文档及其术语。

2.2、缩写

本文档中使用以下缩写：

DetNet：Deterministic Networking，确定性网络

PEF：Packet Elimination Function，数据包消除功能

POF：Packet Ordering Function，数据包排序功能

PREOF：Packet Replication, Elimination, and Ordering Functions，数据包复制、消除和排序功能

PRF：Packet Replication Function，数据包复制功能

3、DetNet IP添加PREOF的要求

将PREOF添加到DetNet IP的要求是：

\* 重用现有的DetNet数据平面解决方案（例如，[RFC8964]、[RFC9025]），以及

\* 允许以最少的实施工作实现IP数据包交换网络的DetNet服务子层。

所描述的解决方案利用MPLS标头字段，而不需要MPLS转发平面的支持。

4、将PREOF添加到DetNet IP

4.1、解决方案基础知识

支持DetNet服务子层的DetNet IP封装基于“UDP隧道”概念。该解决方案在DetNet中继节点的覆盖组之间创建一组底层UDP/IP隧道。

在支持PREOF的DetNet IP域的边缘，DetNet流封装在包含域内PREOF使用的序列号的UDP数据包中。该解决方案在DetNet传输节点中维护基于6元组的DetNet流标识，这些节点运行在DetNet服务子层节点之间的DetNet转发子层；因此，它与[RFC8939]兼容。图2显示了支持PREOF的DetNet IP数据平面如何融入DetNet子层。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YY73GMUZ1NmZLwQEWmqyUCdVyrrXqDIa2KoP7WAjDvskmic8KwNAyzJibaNWQxgQrVtTiakW5Vu86PHKxibE5HuUCgLdftnhUesyBTZicHE6OaUA/640?wx_fmt=png&from=appmsg)

图2：支持PREOF的DetNet IP数据平面

4.2、封装

支持PREOF的DetNet IP封装建立在直接通过UDP封装DetNet伪线（pseudowire，PW）的基础上。也就是说，它将DetNet MPLS [RFC8964] 与DetNet MPLS-in-UDP [RFC9025] 相结合，而不使用任何F标签，如图3所示。DetNet流在接收DetNet服务子层处理节点上通过S标签和/或UDP/IP标头信息进行识别。PREOF的排序信息由DetNet控制字（DetNet Control Word，d-CW）根据 [RFC8964] 提供。S标签用于识别DetNet流和DetNet应用程序流类型。UDP隧道用于将数据包穿过DetNet域引导至下一个DetNet服务子层处理节点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YY73GMUZ1NnGbFP8jE52cFsQEFDN8OwpFkfLTmXX0e0pSWIeX2jkTLskQuo3s85ab0aEyoDLKoNVhSRicszb1Nw7ICD7Y8uJC27njW7ORF6o/640?wx_fmt=png&from=appmsg)

图3：支持PREOF的DetNet IP封装

4.3、数据包处理

支持PREOF的DetNet IP域的IP入口和出口节点添加和删除DetNet服务特定的d-CW和服务ID（即S标签）。中继节点在处理DetNet流时可以更改Service-ID值，即DetNet流的传入和传出Service-ID可以不同。服务ID值是通过配置为每个DetNet服务提供的，例如通过 [RFC8938] 中描述的控制平面。在一些PREOF拓扑中，执行复制的节点将数据包发送到执行例如PEF或POF的多个节点，并且复制节点可以对同一DetNet服务的不同成员流使用不同的Service-ID值。

请注意，Service-ID是接收方的本地ID，用于标识下游DetNet服务子层接收方的DetNet流。

4.4、流量聚合

可以使用两种方法进行流聚合：

\* 使用相同的UDP隧道进行聚合，以及

\* DetNet流聚合为新的DetNet流。

在第一种方法中，不同的DetNet伪线使用相同的UDP隧道，因此它们在转发子层被视为单个（聚合）流。在服务子层，每个流使用不同的Service-ID（参见图3）。

对于第二种方法，通过向封装添加额外的Service-ID和d-CW元组来创建额外的层次结构。Aggregate-ID是Service-ID的特例，其属性仅在聚合和解聚合端点处已知。这是聚合ID的一个属性，它后面跟着一个d-CW，后面跟着一个服务ID/d-CW元组。图4展示了聚合情况下的封装。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YY73GMUZ1NnfaoXXR0sXT68XVgCgTgPuhZvibZm7JmBkhuibvf88QDn15rhxicffMmY1KVIlsRCmyjvOMicRhibGNIBy90FRib9PSN6NShoicDGoD8/640?wx_fmt=png&from=appmsg)

图4：将DetNet流聚合为新的DetNet流

聚合方法在聚合/解聚合节点中配置。

如果多个DetNet流聚合在单个UDP隧道中，则它们都需要遵循网络中的相同路径。

4.5、前处理

在DetNet服务子层对接收到的DetNet流进行操作的节点使用与接收到的服务ID关联的本地上下文来确定将哪些本地DetNet操作应用于接收到的数据包。可以分配唯一的服务ID，并且可以使用该唯一的服务ID来识别DetNet流，无论哪个输入接口或UDP隧道接收数据包。值得注意的是，Service-ID值是由接收方驱动的，而不是由发送方驱动的。

DetNet转发子层由UDP隧道支持，负责提供资源分配和显式路由。

可以通过提供UDP和IP头信息来实现传出的PREOF封装和处理。需要注意的是，在DetNet服务子层进行PRF时，存在多个成员流，每个成员流需要自己的Service-ID、UDP头信息和IP头信息。每个传出数据包的标头根据配置信息进行格式化，并且UDP源端口值设置为唯一标识DetNet流。然后，该数据包将作为具有PREOF功能的DetNet IP数据包进行处理。

传入的PREOF处理可以通过为接收到的DetNet流分配Service-ID并处理UDP和IP标头中的信息来实现。所提供的信息用于基于服务ID和/或传入封装标头信息的组合来识别传入应用程序流。

4.6、支持PREOF的DetNet IP域

图5显示了在支持PREOF的DetNet IP网络中使用PREOF，其中提供端到端的服务保护，而不仅仅是在子网内，如 [RFC8939] 的图4 <https://www.rfceditor.org/rfc/rfc8939#figure-4> 所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YY73GMUZ1NkCVbSIqRlQObxd0jpf5v4XzWCMbnZicgLiaxu5IqZdgibJxBnvXVwxCuXNW7Ke6ClFEm2cTPlbccklCNHpwTaVPOmVOsO8cSFPok/640?wx_fmt=png&from=appmsg)

图5：支持PREOF的DetNet IP域

5、控制管理平面参数

识别单个和聚合DetNet流所需的信息总结如下：

\* 映射到UDP/IP流的服务ID信息。请注意，例如，当使用PREOF时，单个Service-ID可以映射到多组UDP/IP信息。

\* IPv4或IPv6源地址字段。

\* IPv4或IPv6源地址前缀长度，其中零（0）值实际上意味着地址字段被忽略。

\* IPv4或IPv6目标地址字段。

\* IPv4或IPv6目标地址前缀长度，其中零（0）实际上意味着忽略地址字段。

\* IPv6流标签字段。

\* IPv4协议字段等于“UDP”。

\* IPv6（最后一个）下一个标头字段等于“UDP”。

\* 对于IPv4服务类型和IPv6流量类别字段：

- 区分服务代码点（Differentiated Services Code Point，DSCP）字段是否用于流标识，因为用于流标识的DSCP字段的使用是可选的。

- 如果DSCP字段用于标识流，则流标识信息（针对该流）包括给定DetNet流使用的DSCP列表。

\* UDP源端口。需要支持精确匹配和通配符匹配。可以选择使用端口范围。

\* UDP目的端口。需要支持精确匹配和通配符匹配。可以选择使用端口范围。

\* 对于终端系统，应用于传出DetNet IP流的可选最大IP数据包大小。

该信息是通过配置（例如通过控制平面）按DetNet流提供的。

例如，用于识别单个DetNet流的信息集的排序可用于为特定UDP流提供DetNet服务，具有唯一的源和目的端口字段值，同时为具有相同UDP目的端口值的所有其他流的聚合提供不同的服务。

DetNet服务子层配置的最小信息集总结如下：

\* 应用流识别信息

\* 序列号长度

\* 在DetNet流程上执行的PREOF类型

\* 成员流使用的服务ID

\* 关联转发子层信息

\* 服务聚合信息

DetNet转发子层配置的最小信息集总结如下：

\* UDP隧道特定信息

\* 流量参数

这些参数在DetNet流和服务信息模型 [RFC9016] 和DetNet YANG模型中定义。

注意：本文档重点介绍在整个DetNet IP网络中使用MPLS-over-UDP/IP封装，使基于MPLS的DetNet操作、管理和维护（Operations, Administration, and Maintenance，OAM）技术适用 [RFC9546]。仅对处理PREOF的DetNet IP网络的一部分使用所描述的封装将使OAM复杂化。

6、安全考虑

此解决方案没有引入新的DetNet相关安全注意事项。DetNet MPLS [RFC8964] 和DetNet MPLS over UDP/IP [RFC9025] 的安全考虑适用。

7、IANA考虑因素

本文档没有IANA行动。

8、参考文献

8.1、规范性参考文献

```
[RFC8655] Finn, N., Thubert, P., Varga, B., and J. Farkas, "Deterministic Networking Architecture", RFC 8655, DOI 10.17487/RFC8655, October 2019, <https://www.rfc-editor.org/info/rfc8655>.[RFC8938] Varga, B., Ed., Farkas, J., Berger, L., Malis, A., and S. Bryant, "Deterministic Networking (DetNet) Data Plane Framework", RFC 8938, DOI 10.17487/RFC8938, November 2020, <https://www.rfc-editor.org/info/rfc8938>.[RFC8939] Varga, B., Ed., Farkas, J., Berger, L., Fedyk, D., and S. Bryant, "Deterministic Networking (DetNet) Data Plane: IP", RFC 8939, DOI 10.17487/RFC8939, November 2020, <https://www.rfc-editor.org/info/rfc8939>.[RFC8964] Varga, B., Ed., Farkas, J., Berger, L., Malis, A., Bryant, S., and J. Korhonen, "Deterministic Networking (DetNet) Data Plane: MPLS", RFC 8964, DOI 10.17487/RFC8964, January 2021, <https://www.rfc-editor.org/info/rfc8964>.[RFC9016] Varga, B., Farkas, J., Cummings, R., Jiang, Y., and D. Fedyk, "Flow and Service Information Model for Deterministic Networking (DetNet)", RFC 9016, DOI 10.17487/RFC9016, March 2021, <https://www.rfc-editor.org/info/rfc9016>.[RFC9025] Varga, B., Ed., Farkas, J., Berger, L., Malis, A., and S. Bryant, "Deterministic Networking (DetNet) Data Plane: MPLS over UDP/IP", RFC 9025, DOI 10.17487/RFC9025, April 2021, <https://www.rfc-editor.org/info/rfc9025>.[RFC9546] Mirsky, G., Chen, M., and B. Varga, "Operations, Administration, and Maintenance (OAM) for Deterministic Networking (DetNet) with the MPLS Data Plane", RFC 9546, DOI 10.17487/RFC9546, February 2024, <https://www.rfc-editor.org/info/rfc9546>.
```

8.2、参...