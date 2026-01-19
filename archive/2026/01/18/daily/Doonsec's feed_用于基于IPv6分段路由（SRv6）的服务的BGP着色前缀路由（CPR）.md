---
title: 用于基于IPv6分段路由（SRv6）的服务的BGP着色前缀路由（CPR）
url: https://mp.weixin.qq.com/s/tfvrk-uxXtAsPEeV28Re1A
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:43:04.037118
---

# 用于基于IPv6分段路由（SRv6）的服务的BGP着色前缀路由（CPR）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFtqXkV9RiaKmDRFE68KUs0VUJyVArXTLcbia9sEoXCGO7dia03AmZcJPbtgJ3ynTD1hJlbET5YSKzRr1bQmJnwww/0?wx_fmt=jpeg)

# 用于基于IPv6分段路由（SRv6）的服务的BGP着色前缀路由（CPR）

衡水石头哥
衡水石头哥

铁军哥

![]()

在小说阅读器中沉浸阅读

```
RFC 9723：BGP Colored Prefix Routing (CPR) for Services Based on Segment Routing over IPv6 (SRv6)，May 2025
```

梗概

本文档描述了一种在BGP中通告与颜色扩展团体字关联的IPv6前缀的机制，以便为IPv6分段路由（Segment Routing over IPv6，SRv6）服务建立端到端意图感知路径。这样的IPv6前缀被称为“着色前缀”，这种机制被称为“着色前缀路由”（Colored Prefix Routing，CPR）。在SRv6网络中，着色前缀是与不同意图关联的SRv6定位符。具有特定意图的SRv6服务（例如SRv6 VPN服务）可以在相应的SRv6定位符下分配SRv6分段标识符（Segment Identifiers，SID），这些标识符作为着色前缀进行通告。

这种操作方法允许根据SRv6服务SID与着色前缀的最长前缀匹配，将SRv6服务流量引导至端到端意图感知路径。现有的IPv6地址族和颜色扩展团体字被重新用于通告IPv6颜色前缀，而无需新的BGP扩展；因此，该机制易于互操作，并且可以在属于同一可信域的多自治系统（Autonomous System，AS）网络中增量部署。

本备忘录的状态

本文档不是互联网标准跟踪规范；其发布仅供参考。

本文档是互联网工程任务组（IETF）的产品。它代表了IETF社区的共识。它已接受公众审查，并已被互联网工程指导小组（IESG）批准发布。并非IESG批准的所有文件都是任何级别互联网标准的候选文件；请参阅RFC 7841第2节。

有关本文档当前状态、任何勘误表以及如何提供反馈的信息，请访问https://www.rfc-editor.org/info/rfc9723。

版权声明

版权所有（c）2025 IETF Trust和文档作者。版权所有。

本文件受本文件发布之日生效的BCP 78和IETF信托与IETF文件相关的法律规定（https://trustee.ietf.org/license-info）的约束。请仔细阅读这些文件，因为它们描述了您与本文件相关的权利和限制。从本文档中提取的代码组件必须包括《信托法律条款》第4.e节中所述的修订版BSD许可证文本，并且不提供修订版BSD许可证中所述的保证。

1、简介

随着同一个网络承载多种业务的趋势，每种业务对网络的要求也不同。此类要求通常被视为服务或客户的“意图”，其表示为称为“颜色”的抽象概念。

在跨多个自治系统（AS）交付服务的网络场景中，需要为服务提供不同的端到端路径来满足意图。[INTENTAWARE]描述了域间意图感知路由的问题陈述和要求。

域间路径可以使用多协议标签交换（Multi-Protocol Label Switching，MPLS）或IP数据平面来建立。在基于MPLS的网络中，通常的域间方法是基于[RFC8277]中定义的机制建立端到端的标签交换路径（Label Switched Path，LSP）（通常称为BGP-LU（BGP Labeled Unicast，BGP标签单播））。每个域的入口边界节点都需要对端到端的LSP进行标签交换，并将LSP所使用的标签栈强加到本域内。

在基于IP的网络中，可以通过BGP将IP可达信息发布到不同域的网络节点，以便所有域边界节点都能获取到其他域的目的节点的IP前缀的路由。随着SRv6[RFC8402][RFC8754][RFC8986]的引入，BGP服务被分配了SRv6服务SID[RFC9252]，这些SID可根据其SRv6定位符前缀在网络中进行路由。这样，只需根据到前缀的域间路由就可以建立域间路径。基于BGP-LU机制的域间LSP对于IPv6和SRv6网络来说不是必需的。

本文档描述了一种通告与颜色扩展团体字关联的IPv6前缀的机制，以便为SRv6服务建立端到端意图感知路径。颜色扩展团体字中的颜色值表示意图[RFC9256]。这种IPv6前缀称为“着色前缀”，这种机制称为着色前缀路由（CPR）。在SRv6网络中，着色前缀是与不同意图关联的SRv6定位符。具有特定意图的基于SRv6的BGP服务（例如SRv6 VPN服务）[RFC9252]可以在相应的SRv6定位符下分配SRv6 SID，这些定位符作为着色前缀进行通告。这允许根据SRv6服务SID与着色前缀的最长前缀匹配，将SRv6服务流量引导（如[RFC9252]中指定）进入端到端意图感知路径。在数据平面中，域间路径不需要专用传输标签或SID，因此与其他选项相比，封装开销更小。

现有的IPv6地址族和颜色扩展团体字可以重新用于通告IPv6颜色前缀，而无需新的BGP扩展；因此，该机制易于互操作，并且可以在属于同一可信域的多AS网络中增量部署（在[RFC8402]第8节所使用的意义上）。

2、BGP CPR

2.1、着色前缀分配

在SRv6网络中，需要为每个节点分配一个SRv6定位符。为了区分N个不同的意图，需要为提供商边缘（Provider Edge，PE）节点分配N个SRv6定位符，每个定位符都与由颜色值标识的不同意图相关联。实现此目的的一种方法是将节点的基本SRv6定位符拆分为N个子定位符，其中这些子定位符是与不同意图相关联的着色前缀。

例如，PE节点分配有基本SRv6定位符2001:db8:aaaa:1::/64。为了提供16个不同的意图，此基本SRv6定位符被分为16个子定位符，从2001:db8:aaaa:1:0000::/68到2001:db8:aaaa:1:F000::/68；每个子定位符都与不同的意图相关联，例如低延迟、高带宽等。

2.2、着色前缀宣告

PE节点上分配了Colored Prefix后，到这些Colored Prefix的路由需要在本域中发布，同时也需要通过BGP发布到其他域，以便使用相应的CPR路由来解析BGP SRv6业务路由。

在多AS IPv6网络中，[RFC2545]中定义的IPv6单播路由机制用于通告着色前缀路由，其中使用地址族/后续地址族（AFI/SAFI = 2/1）。颜色扩展团体字[RFC9012]由颜色前缀路由携带，颜色值指示意图[RFC9256]。以如下拓扑为例描述着色前缀通告的流程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFtqXkV9RiaKmDRFE68KUs0VUJyVArXTLgbiaEibqzYMY3seDaOQIMSGttOAxYA3AenrPkaea5vhWV3C60qaicia3lA/640?wx_fmt=png&from=appmsg)

图1：CPR路线图的拓扑示例

假设PE3配备有两个不同的着色前缀CLP-1和CLP-2，分别用于两个不同的目的，例如“低延迟”和“高带宽”。在此示例中，假设表示特定意图的颜色在所有域中都是一致的。

\* PE3为着色前缀PE3:CL1:: 和PE3:CL2:: 发起BGP IPv6单播（AFI/SAFI=2/1）路由。每条路线应携带相应的颜色扩展团体字C1或C2。PE3还发布了一条基本SRv6 Locator前缀PE3:BL的路由，该路由中没有携带Color Extended Community。

\* ASBR31和ASBR32接收PE3的CPR路由，并将CPR路由进一步发布给下一跳设置为自身的ASBR23和ASBR24。

\* ASBR23和ASBR24接收PE3的CPR路由。由于AS2中的颜色到意图的映射与AS3中的一致，因此接收到的CPR路由中的颜色扩展团体字保持不变。ASBR23和ASBR24在AS2中进一步通告CPR路由，下一跳设置为自身。

\* ASBR21和ASBR22的行为与ASBR31和ASBR32的行为类似。

\* ASBR11和ASBR12的行为与ASBR23和ASBR24的行为类似。

正常情况下，与CPR路由关联的颜色扩展团体字中的颜色值在所有域中都是一致的，从而使得CPR路由中的颜色扩展团体字保持不变。在某些特殊情况下，一个意图可能在不同域中表示为不同的颜色值。如果是这种情况，则需要根据颜色映射策略在域的边界节点处更新CPR路由中的颜色扩展团体字。例如，在AS1中，意图“低延迟”由颜色“红色”表示，而相同的意图在AS2中由颜色“蓝色”表示。当CPR路由从AS1发送到AS2时，CPR路由中的颜色扩展团体字需要在边界节点根据颜色映射策略从“红色”更新为“蓝色”。

在部分中间自治系统基于MPLS的网络场景下，在基于MPLS的中间域中，CPR路由仍可以使用IPv6单播地址族（AFI/SAFI=2/1）发布；在MPLS域边界节点，可以使用一些路由解析策略来使CPR路由解析为域内意图感知的MPLS LSP。另一种可能的机制是使用IPv6 LU地址族（AFI/SAFI=2/4）在MPLS域中通告CPR路由，详细过程在[SRv6-INTERWORK]的7.1.2.1节中描述。

2.3、CPR到域内路径解析

接收到CPR路由的域边界节点可以根据元组(N,C)将CPR路由解析为域内颜色感知路径，其中N为CPR路由的下一跳，C为CPR路由的颜色扩展团体。域内颜色感知路径可以使用以下任何机制来构建：

\* SRv6策略

\* SR-MPLS策略

\* SRv6 Flex算法

\* SR-MPLS Flex算法

\* RSVP-TE

例如，如果PE1收到一条到PE3:CL1:: 的CPR路由，颜色为C1，下一跳为ASBR11，则它可以根据元组（ASBR11, C1）将CPR路由解析为域内SRv6策略。

域内路径解析方案可以基于任何现有的隧道解析策略，并且如果需要的话可以引入新的隧道解析机制。

2.4、SRv6业务路由发布

对于与特定意图关联的SRv6服务，可以在相应的着色定位符前缀下分配SRv6服务SID。例如，在示例拓扑中的PE3上，可以为具有低延迟意图的SRv6 VPN服务分配SRv6 End.DT4 SID PE3:CL1:DT::，其中PE3:CL1:: 是低延迟服务的SRv6着色前缀。

SRv6服务路由使用[RFC9252]中定义的机制进行通告。采用域间VPN Option C，即SRv6业务路由的下一跳设置为始发PE，且不改变。由于服务的意图嵌入在SRv6服务SID中，因此SRv6服务路由不需要携带Color Extended Community。

2.5、SRv6服务引导

通过CPR路由机制，接收SRv6服务路由的入口PE节点遵循SRv6最短路径转发的行为（参见[RFC9252]的第5节和第6节）。业务路由中携带的SRv6业务SID作为封装业务报文的外层IPv6头中的目的地址。如果已接收并安装相应的CPR路由，则执行SRv6服务SID与着色前缀的最长前缀匹配。通过前缀匹配，找到的下一跳是域内颜色感知路径，该路径将用于转发SRv6业务流量。此过程在数据包所经过的每个域的边界节点处重复，直到到达目的地。

3、封装转发过程

本节介绍匹配相应CPR路由的数据包的封装和转发过程。

每个示例均使用图1的拓扑。

3.1、基于SRv6域内路径的CPR

以下是CPR over SRv6策略的报文封装和转发过程的说明。使用[RFC8754]第6节中描述的IPv6和分段路由报文头（Segment Routing Header，SRH）的抽象表示。

PE3配备有着色前缀PE3:CL1::，用于“低延迟”。

在AS1中，PE1上针对（ASBR11，C1）的SRv6策略用SID列表 <P1，ASBR11> 表示。

在AS2中，ASBR21上针对（ASBR23，C1）的SRv6策略用SID列表 <P2，ASBR23> 表示。

在AS3中，ASBR31上针对（PE3，C1）的SRv6策略用SID列表 <P3，PE3> 表示。

C-pkt是PE1从其连接的CE接收到的客户数据包。

对于属于与SRv6服务SID PE3:CL1.DT6关联的SRv6 VPN服务的数据包，使用H.Encaps.Red行为[RFC8986]的数据包封装和转发过程如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFtqXkV9RiaKmDRFE68KUs0VUJyVArXTLrVe2v210XJbKvME9qIbdAbAK3uQI1ou9qndnl5sJMdgDEgMIqJGcZQ/640?wx_fmt=png&from=appmsg)

图2

在某些自治系统中，SRv6 Flex-Algo可用于提供意图感知的域内路径。封装与SRv6策略的情况类似。

3.2、基于MPLS域内路径的CPR

在某些自治系统使用基于MPLS的数据平面的网络场景中，可以通过coloraware域内MPLS LSP解析CPR路由。这样的域内MPLS LSP可以使用SR-MPLS策略、SR-MPLS Flex-Algo或RSVP-TE来建立。

SRv6业务报文（实际上是IPv6报文）在域内MPLS LSP上的封装和转发基于[RFC3031]、[RFC3032]和[RFC8660]中定义的MPLS机制。该行为类似于IPv6提供商边缘路由器（IPv6 Provider Edge Routers，6PE）[RFC4798]。

在AS1中，PE1上针对（ASBR11，C1）的SR-MPLS策略用SID列表<P1，ASBR11>表示。

在AS2中，ASBR21上用于（ASBR23，C1）的SR-MPLS Flex-Algo用SID列表<ASBR23>表示。

在AS3中，ASBR31上针对（PE3，C1）的SR-MPLS策略用SID列表 <P3，PE3> 表示。

C-pkt是从其连接的CE接收到的客户数据包PE-1。

对于属于与SRv6 Service SID PE3:CL1.DT6关联的SRv6 VPN服务的报文，报文封装和转发过程如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFtqXkV9RiaKmDRFE68KUs0VUJyVArXTL8iagE3mruTsaRhfPZkBibt2EtljUB56SK7DIElicJJn6U4ticGPr5YJFeg/640?wx_fmt=png&from=appmsg)

图3

4、操作注意事项

CPR机制可用于多个互连AS属于同一运营商的网络场景，或者不同运营商的AS之间存在操作信任模型，这意味着它们属于同一可信域（在[RFC8402]第8节使用的意义上）。

如[INTENTAWARE]第5节中所述，域间意图感知路由可以通过适用于多个AS的SR策略创建的逻辑隧道来实现。此外，可以根据Color Extended Community发出的意图将具有特定意图的服务流量引导至域间SR策略。出于[INTENTAWARE]中描述的原因，运营商可能更喜欢基于BGP路由的解决方案。运营商还可以考虑用于端到端意图感知路径计算的域间控制器的可用性。本文档提出了一种替代解决方案，使用BGP通过IPv6着色前缀来表示意图。

当将着色前缀分配为节点的基本SRv6定位符的子定位符时，基本定位符前缀的IPv6单播路由是覆盖所有着色定位符前缀的前缀。为了保证着色定位前缀能够分发到边界节点的入口PE节点，需要对携带着色扩展团体的IPv6单播路由去使能路由聚合功能。

通过CPR机制，在前缀发起者处，每个着色前缀都与一种特定意图（即颜色）相关联。在每个域中，根据颜色映射策略，相同的CPR路由总是用相同的颜色更新。存在多个具有相同颜色前缀但不同颜色扩展团体字的CPR路由副本的情况被视为配置错误。

所有边界节点和入口PE节点都需要在RIB和FIB中安装Colored定位符前缀。对于支持CPR机制的中转域，边界节点可以使用元组（N, C）（其中N是下一跳，C是颜色）将CPR路由解析为意图感知的域内路径。对于不支持CPR机制的中转域，边界节点会忽略颜色扩展团体，并通过尽力而为的域内路径将CPR路由解析到下一跳N，而CPR路由将进一步发布到下游域，仅下一跳更改为自身。这允许CPR路由解析为支持CPR机制的任何自治系统中的意图感知域内路径，而CPR路由可以回退到解析传统自治系统中的尽力而为的域内路径。

相邻自治系统之间可能存在多个域间链路，并且边界节点BGP发言者可以通过外部BGP（External BGP，EBGP）接收来自另一个域中的多个对等BGP发言者的CPR路由。BGP发言者的本地策略在为特定的着色前缀选择最佳路径时，可以考虑域间链路的属性和接收到的CPR路由的属性，以更好地满足意图。详细的当地策略不在本文档的讨论范围之内。在多AS环境中，不同域的BGP发言者的策略需要保持一致。

在本文档中，IPv6单播地址族用于通告IPv6着色前缀。这种方法的主要优点是改进了与缺乏对意图感知路径的支持的传统网络的互操作性，并促进了意图感知路由机制的增量部署。一个潜在的问题是需要将着色前缀与公共IPv6单播路由分开。由于网络基础设施的IP前缀和SRv6定位符通常作为IP单播路由的一部分进行通告，并且在网络管理边界配置了适当的过滤器，因此这一问题不被认为是一个重要问题。[RFC9602]为SRv6 SID分配前缀5f00::/16。根据受信任域中参与者之间的共同协议，过滤器可以配置为默认丢弃来自5f00::/16的所有流量，但允许在这些域中使用着色前缀。[BGP-CAR]中的提案提供了一个补充解决方案，该解决方案也基于指示意图的颜色概念以及SRv6定位符前缀本身表示意图的位置；不同之处在于使用了单独的SAFI。

[BGP-CT]描述了另一种意图感知路由机制，其中SRv6服务SID不与意图直接关联（需要额外的SRv6传输SID来将流量引导至域间意图感知路径），并且在自治系统的边界节点上需要类似于MPLS标签交换的SRv6操作。

5、IANA考虑因素

本文档没有IANA行动。

6、安全考虑

本文档中描述的机制提供了一种基于现有BGP协议机制的域间意图感知路由的方法。现有的BGP IPv6单播地址族和现有的颜色扩展团体字将被重用，无需进一步的BGP扩展。通过这种方法，PE节点通告的IPv6着色前缀数量与其支持的意图数量成正比。这可能会向BGP IPv6路由表引入额外的路由。由于这些是基础设施路由，因此着色前缀的数量仅占IPv6前缀总数的一小部分。因此，对所需路由表大小的影响被认为是可以接受的。

由于CPR路由分布在属于受信任域的多...