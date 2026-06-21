---
title: 确定性网络（DetNet）数据平面：IP over IEEE 802.1时间敏感网络（TSN）
url: https://mp.weixin.qq.com/s/BPBk3ATGfNkMwBTsQHWWPQ
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:49:08.737088
---

# 确定性网络（DetNet）数据平面：IP over IEEE 802.1时间敏感网络（TSN）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YY73GMUZ1NmvWWSylt15MzQODIWsQRuOoDPsJGDCic4WLXmUNzrAskXWBexOpt2XJla26tBATjicXW1F4yibZoRZAiawV0G7FHN5Zl6RVMfvguI/0?wx_fmt=jpeg)

# 确定性网络（DetNet）数据平面：IP over IEEE 802.1时间敏感网络（TSN）

衡水石头哥
衡水石头哥

铁军哥

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

```
RFC9023：Deterministic Networking (DetNet) Data Plane: IP over IEEE 802.1 Time-Sensitive Networking (TSN)，June 2021
```

梗概

本文档指定了在时间敏感网络（Time-Sensitive Networking，TSN）子网上运行时的确定性网络IP数据平面。本文件没有定义新的程序或流程。每当本文档提出声明或建议时，这些声明或建议均取自引用的RFC中的规范文本。

本备忘录的状态

本文档不是互联网标准跟踪规范；其发布仅供参考。

本文档是互联网工程任务组（IETF）的产品。它代表了IETF社区的共识。它已接受公众审查，并已被互联网工程指导小组（IESG）批准发布。并非IESG批准的所有文件都是任何级别互联网标准的候选文件；请参阅RFC 7841第2节。

有关本文档当前状态、任何勘误表以及如何提供反馈的信息，请访问https://www.rfc-editor.org/info/rfc9023。

版权声明

版权所有（c）2021 IETF Trust和文档作者。版权所有。

本文件受本文件发布之日生效的BCP 78和IETF信托与IETF文件相关的法律规定（https://trustee.ietf.org/license-info）的约束。请仔细阅读这些文件，因为它们描述了您与本文件相关的权利和限制。从本文档中提取的代码组件必须包括信托法律条款第4.e节中所述的简化BSD许可证文本，并且在提供时不提供简化BSD许可证中所述的保证。

1、简介

确定性网络（Deterministic Networking，DetNet）是网络可以向DetNet流提供的服务。DetNet为这些流提供极低的丢包率，并保证最大的端到端传输延迟。DetNet的一般背景和概念可以在DetNet架构[RFC8655]中找到。

[RFC8939]指定为IP封装数据提供DetNet服务的IP主机和路由器的DetNet数据平面操作。本文档重点介绍DetNet IP节点通过时间敏感网络（Time-Sensitive Networking，TSN）子网互连的场景。

DetNet架构将DetNet相关的数据面功能分解为两个子层：服务子层和转发子层。服务子层用于提供DetNet服务保护和重新排序。转发子层用于提供拥塞保护（低丢失、有保证的延迟和有限的重新排序）。如[RFC8939]中所述，没有添加DetNet特定标头来支持DetNet IP流。因此，DetNet IP域内只能支持转发子层功能。可以按子网提供服务保护，如此处针对IEEE 802.1 TSN子网场景所示。

2、术语

2.1、本文档中使用的术语

本文档使用DetNet架构[RFC8655]中建立的术语和概念。TSN特定术语由IEEE 802.1工作组的TSN任务组定义。假定读者熟悉这些文档及其术语。

2.2、缩写

本文档中使用以下缩写：

DetNet：Deterministic Networking，确定性网络

FRER：Frame Replication and Elimination for Redundancy，帧复制和冗余消除（TSN功能）

L2：Layer 2，二层

L3：Layer 3，三层

TSN：Time-Sensitive Networking，时间敏感网络；TSN是IEEE 802.1工作组的一个任务组。

3、DetNet IP数据平面概述

[RFC8939]描述了DetNet节点（即主机和路由器）如何使用IP来识别DetNet流并提供DetNet服务。从数据平面的角度来看，遵循端到端的IP模型。DetNet 使用基于“6 元组”的流标识，其中“6 元组”指的是在 [RFC8939] 中定义的 IP 和更高层协议头中携带的信息。

DetNet流聚合可以通过使用通配符、掩码、前缀和范围来启用。IP隧道也可用于支持流聚合。在这些情况下，预计 DetNet 感知的中间节点将通过资源分配和拥塞控制机制，在聚合层面上提供 DetNet 服务保障。

拥塞保护、延迟控制和资源分配（排队、监管和整形）均通过底层链路/子网特定的机制实现。由于缺乏可供中间节点使用的统一端到端排序信息，IP DetNet 层无法提供端到端的业务保护（数据包复制和数据包消除功能）。但是，可以针对每个底层 L2 链路和每个子网提供此类业务保护。

DetNet 路由器通过分配本地资源（包括接收和发送）以及将每个流的服务需求映射到相应的子网机制，确保每个跃点都满足 DetNet 服务需求。此类映射与子网技术密切相关。本文档主要关注由 TSN 子网互连的 DetNet 节点。DetNet IP 流到 TSN 流的映射以及 TSN 保护机制将在第 4 节中介绍。

4、DetNet IP在IEEE 802.1 TSN子网上的流动

本节介绍 DetNet IP 流如何在 IEEE 802.1 TSN 子网中运行。图 1 展示了这样一种场景：两个 IP（DetNet）节点通过 TSN 子网互连。IP（DetNet）节点的服务组件周围的虚线表示它们感知 DetNet 服务，但不执行任何 DetNet 服务子层功能。节点 1 为单宿主，节点 2 为双宿主连接到 TSN 子网，它们在 TSN 子网内部分别被视为发送方或监听方。需要注意的是，从 TSN 的角度来看，发送方或监听方节点的双宿主特性对 IP 层是透明的。

![](https://mmbiz.qpic.cn/mmbiz_png/YY73GMUZ1Nn1ZxjtFb1ZEBQWYSOEgoicLFr1Boux6QQ31UC8RSxlDibibUVT6E1pwFxvwXVOuLjFoGaZQyS1YhshK1PciaPESeVK0TWQSUw4j8w/640?wx_fmt=png&from=appmsg)

图1：TSN子网上支持DetNet的IP网络

截至本文撰写之时，IEEE 802.1 工作组的时间敏感网络 (TSN) 任务组已经（或正在）对 [IEEE802.1Q] 进行了一系列修订，旨在桥接网络中实现零拥塞损失和有界延迟。此外，[IEEE802.1CB] 定义了帧复制和消除功能，以提高可靠性，这些功能应能与 DetNet 网络兼容并发挥作用。所有这些功能都必须能够识别需要 TSN 处理的流。

TSN 子网的 TSN 功能可通过 [IEEE8021CB] 附录 C.5 中描述的协议互通功能提供给 IP (DetNet) 流。例如，在 TSN 边缘端口应用该功能，可以将入口单播 IP (DetNet) 流转换为使用特定的 L2 组播目标媒体访问控制 (MAC) 地址和 VLAN，以便通过桥接网络内的特定路径转发数据包。在 TSN 子网的另一端应用类似的互通功能，可以将数据包恢复到其原始的 L2 目标 MAC 地址和 VLAN。

TSN功能的放置取决于节点的TSN能力。IP（DetNet）节点可能支持也可能不支持TSN功能。对于给定的TSN 信元流（即映射的DetNet流），IP（DetNet）节点被视为TSN子网络内的Talker或Listener。

4.1、DetNet流到TSN 信元流映射的函数

DetNet IP 流到 TSN 流的映射是通过帧级（二层）被动信元流识别功能和主动信元流识别功能的组合来实现的。被动信元流识别功能用于捕获 DetNet IP 流的 6 元组，而主动信元流识别功能则根据映射的 TSN 流的 ID 修改以太网帧头。

[IEEE8021CB]第6.7条定义了IP信元流识别功能，该功能可用作使用UDP或TCP的IP DetNet流的被动功能。[IEEEP8021CBdb]的第6.8条定义了Mask-andMatch信元流识别功能，可用作任何IP DetNet流的被动功能。

[IEEE8021CB]第6.6条定义了活动目标MAC和VLAN信元流识别功能，可以替换一些以太网报头字段：（1）目标MAC地址，（2）VLAN-ID，以及（3）具有备用值的优先级参数。为从上层向下传递到堆栈或从下层向上传递到堆栈的帧提供替换。

活动目标MAC和VLAN流标识可在信源中使用以设置流身份，或在接收端中使用以恢复原始寻址信息。它还可以用在为终端系统提供翻译作为代理服务的TSN桥中。

4.2、IP DetNet节点的TSN要求

本节介绍使用TSN子网络的TSN感知DetNet节点所需的行为。TSN数据包处理功能的实现必须符合相关的IEEE 802.1标准。

从TSN子网络的角度来看，DetNet IP节点被视为可能（1）TSN不感知或（2）TSN感知的信源或接收端。

在TSN不感知IP DetNet节点的情况下，TSN子网内的TSN中继节点必须修改DetNet IP流的以太网封装（例如，MAC转换、VLAN-ID设置、序列号添加等），以允许在子网内进行正确的TSN特定处理。本文档中没有为不支持TSN的IP DetNet节点定义任何要求。

具有TSN感知能力的IP（DetNet）节点可以被视为TSN不感知的发话器/监听器和TSN中继的组合，如图2所示。在这种情况下，IP（DetNet）节点必须通过通向子网的链路提供TSN子网特定的以太网封装。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YY73GMUZ1NndaOJ1HQxaLibI0icLMY4zLTtVbLtX5dGjHD8L6tvf9KjqnS4wHxHxAYJOVAnjHs8Imaomkibx96R1icUwIRLCWOclKDdORvBOMaw/640?wx_fmt=png&from=appmsg)

图2：具有TSN功能的IP（DetNet）节点

TSN感知IP（DetNet）节点实现必须支持信元流识别TSN组件以识别流。

信元流识别组件必须能够实例化以下内容：（1）活动目标MAC和VLAN信元流识别，（2）IP信元流识别，（3）掩码和匹配信元流识别，以及（4）[IEEE8021CB]和[IEEEP8021CBdb]第9条中的相关管理对象。

如果在TSN子网内部使用FRER，则TSN感知IP（DetNet）节点实现必须支持[IEEE8021CB]第7.4和7.6条中定义的排序功能和序列编码/解码功能。

序列编码/解码功能必须支持[IEEE8021CB]第7.8条中的冗余标签（R-TAG）格式。

当节点是FRER的复制或消除点时，TSN感知IP（DetNet）节点实现必须支持[IEEE8021CB]第7.7和7.5条中定义的流分割功能和单独恢复功能。

4.3、TSN子网内的服务保护

支持DetNet流的TSN 信元流可以根据TSN 信元流的丢失服务要求（源自DetNet映射流的DetNet服务要求）使用[IEEE8021CB]第8条中定义的FRER。FRER的具体操作没有因DetNet的使用而修改，并且遵循[IEEE8021CB]。

FRER功能和提供的服务恢复仅在TSN子网内可用，因为TSN 信元流ID和TSN序列号在子网外无效。IP（DetNet）节点代表L3边界，因此它终止L2帧中编码的所有相关信息元素。

4.4、DetNet流到TSN 信元流映射期间的聚合

本文档的实现应使用管理和控制信息将DetNet流映射到TSN 信元流。应支持N:1映射（将DetNet流聚合到单个TSN 信元流中）。提供流映射的管理或控制功能应确保分配和配置足够的资源，以提供映射流的适当服务要求。

5、管控意义

只有支持 TSN 的 IP（DetNet）节点才需要 DetNet 流和 TSN 流映射相关信息。从数据平面的角度来看，流映射相关信息的来源（管理平面或控制平面）并无实际区别。

下面总结了配置DetNet IP over TSN所需的一组信息：

\* 根据DetNet IP节点的DetNet角色的DetNet-IP相关配置信息，按照[RFC8939]。

\* 根据DetNet IP节点的TSN角色的TSN相关配置信息，按照[IEEE8021Q]、[IEEE8021CB]和[IEEEP8021CBdb]。

\* DetNet IP流和TSN 信元流之间的映射。DetNet IP信元流识别在[RFC8939]的第5.1节中进行了总结，包括所有通配符、端口范围以及忽略特定IP字段的能力。关于TSN 信元流标识信息的信息在[IEEE8021CB]和[IEEEP8021CBdb]中定义。请注意，用于TSN 信元信元流识别的托管对象可以在[IEEEP8021CBcv]中找到。

必须根据DetNet流程配置此信息。

DetNet与TSN管理和控制平面之间的映射超出了本文档的范围。下面重点介绍了一些挑战。

TSN感知IP DetNet节点是DetNet域和TSN子网的成员。在TSN子网络中，TSN感知IP（DetNet）节点具有TSN感知发送者/监听者角色，因此必须实现TSN特定的管理和控制平面功能。DetNet和TSN中使用的管理平面技术有许多相似之处，但控制平面协议却并非如此。例如，RSVP-TE和IEEE 802.1的多流注册协议（Multiple Stream Registration Protocol，MSRP）的行为不同。因此，管理和控制平面的设计是DetNet和TSN之间需要映射的场景的一个重要方面。

为了在DetNet节点之间使用TSN子网络，必须将DetNet特定信息转换为TSN子网络特定信息。DetNet流ID和流相关参数/要求必须转换为TSN 信元流ID和流相关参数/要求。请注意，由于TSN子网络只是端到端DetNet路径的一部分（即从IP角度来看的单跳），因此某些参数（例如延迟）可能会有很大差异。由于TSN子网内使用的L2封装，其他参数（如带宽）也可能必须进行调整。

在某些情况下，确定一些与 TSN 流相关的信息可能具有挑战性。例如，在作为发送方的 TSN 感知 IP（DetNet）节点上，很容易确定哪个 DetNet 节点是映射的 TSN 流的监听方（即 IP 下一跳）。然而，要找到该监听方连接到 TSN 子网的点/接口可能并非易事。此类属性可能需要控制平面和管理平面功能之间以及 DetNet 域和 TSN 域之间的交互。

如果未明确提供，则 TSN 感知的 IP (DetNet) 节点可以根据为配置 TSN 信元流识别功能（IP 信元流识别、掩码匹配信元流识别和活动信元流识别功能）提供的信息，在本地完成 DetNet 流标识符和 TSN 流标识符之间的映射。

在 TSN 子网中触发 TSN 流的建立/修改，就是一个需要在 DetNet 和 TSN 子网之间进行管理和/或控制平面交互的例子。由于不了解 TSN 的 IP（DetNet）节点完全独立运行，且它们对子网一无所知，因此这种触发操作会变得更加复杂。

TSN 子网内 TSN 特定功能（例如 FRER）的配置是 TSN 域特定的决策，在 DetNet 域中可能不可见。

6、安全考虑

[DETNET-SECURITY]中详细描述了DetNet的安全注意事项。[RFC8655]中描述了一般安全注意事项。[RFC8939]中总结了DetNet IP数据平面的具体注意事项。本节讨论特定于DetNet IP-over-TSN子网场景的安全注意事项。

DetNet节点之间的子网络需要受到适当的保密。此外，了解子网提供的DetNet/TSN服务可以提供可用于各种安全攻击的信息。修改连接的DetNet节点之间的信息交换的能力可能会导致虚假操作。因此，DetNet节点和TSN子网之间的接口受到授权、身份验证和加密非常重要。

TSN子网络在二层运行，因此可以使用IEEE定义的各种安全机制来保护DetNet节点之间的连接（例如，可以使用MACsec[IEEE802.1AE-2018]提供加密）。

7、IANA考虑因素

本文档没有IANA行动。

8、参考文献

8.1.  规范性参考文献

```
[IEEE8021CB]IEEE, "IEEE Standard for Local and metropolitan area networks--Frame Replication and Elimination for Reliability", IEEE 802.1CB-2017, DOI 10.1109/IEEESTD.2017.8091139, October 2017, <https://standards.ieee.org/standard/802_1CB-2017.html>.[IEEEP8021CBdb]IEEE, "Draft Standard for Local and metropolitan area networks -- Frame Replication and Elimination for Reliability -- Amendment: Extended Stream Identification Functions", IEEE P802.1CBdb / D1.3, April 2021, <https://1.ieee802.org/tsn/802-1cbdb/>.[RFC8655]Finn, N., Thubert, P., Varga, B., and J. Farkas, "Deterministic Networking Architecture", RFC 8655, DOI 10.17487/RFC8655, October 2019, <https://www.rfc-editor.org/info/rfc8655>.[RFC8939]Varga, B., Ed., Farkas, J., Berger, L., Fedyk, D., and S. Bryant, "Deterministic Networking (DetNet) Data Plane: IP", RFC 8939, DOI 10.17487/RFC8939, November 2020, <https://www.rfc-editor.org/info/rfc8939>.
```

8.2.  参考资料

```
[DETNET-SECURITY]Grossman, E., Ed., ...