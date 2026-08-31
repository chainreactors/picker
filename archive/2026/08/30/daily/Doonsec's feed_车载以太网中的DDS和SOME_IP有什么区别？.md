---
title: 车载以太网中的DDS和SOME/IP有什么区别？
url: https://mp.weixin.qq.com/s/JdbMbAIFG6Ku-C_abTOOJg
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:50:30.821996
---

# 车载以太网中的DDS和SOME/IP有什么区别？

# 车载以太网中的DDS和SOME/IP有什么区别？

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于汽车电控知识
，作者安己乐人

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM6j5af2Q2k1xdAVsogZDicBJA7ibwvcRA8UDSp3GKThzmZw/0)

**汽车电控知识**
.

快乐学习汽车ECU知识、轻松进入汽车电子行业！

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247576519&idx=2&sn=9b21ae1557b5189e3ac3d934941609ab&scene=21#wechat_redirect)

软件中的中间件是指位于应用程序和基础软件之间的软件层，基础软件主要是指操作系统、网络或数据库等。中间件使应用程序和网络通信之间解耦，使得应用程序的编写更加灵活。

之前我们介绍过的SOME/IP就是车载网络中使用的一种中间件，SOME/IP是Scalableservice-Oriented MiddlewarE over IP的缩写，表示“运行于IP之上的可扩展的面向服务的中间件”。

SOME/IP是最早应用在汽车上的通信中间件，但是汽车上可用的中间件不只有SOME/IP,还有DDS，那么DDS协议有什么特点，它与SOME/IP有什么区别呢？

**01**

**DDS简介**

随着SOA在汽车领域的发展和运用，面向服务的通信中间件SOME/IP标准协议被引入到软件架构标准中。

但是随着软硬解耦、软软解耦的进一步发展，应用和服务之间除了服务能力的提供，还出现数据共享的需求。DDS正是以数据为中心的通信中间件，用Topic为单元实现数据的共享，按照用户定义的方式存储、发布和订阅数据，支持运行在不同系统上，不同开发语言的应用可以分布式的互相收发数据。

DDS是DataDistribution Service的缩写，表示数据分发服务。它是由OMG联盟在2004年发布的中间件协议标准。

它将应用程序从操作系统，网络传输和低级数据格式的详细信息中抽象出来，以接口定义语言模式提供了支持多种编程语言的API，用于协调和管理不同软件组件之间的通信和交互。使不同应用程序可以在不同的环境中进行交换信息。目的是支持高性能、实时和可靠的数据传输。

DDS 被广泛应用在航空航天、船舶、军事、工业、医疗、交通、能源等领域中。

**02**

**DDS的特点**

DDS管理了数据格式、发现、连接、可靠性、协议、传输选择、QoS、安全性等底层细节。提供丰富的QoS（Quality of Service）服务质量策略，可满足各种分布式系统实时通信的低延迟、高可靠性、可扩展性的需求。

DDS主要具备以下几个特点：

**1）以数据为中心的发布订阅模型**

分布式通信系统中常用的主要有两种模型，一种叫客户端-服务器模型。

客户端（Client）-服务器（Server）模型中，客户端直接向服务器发送请求，服务器处理请求后返回结果给客户端。客户端和服务器之间需要建立直接的连接，客户端需要知道服务器的地址和端口，服务器也需要知道客户端的请求‌。

客户端-服务器模型的特点是数据都集中在了服务器server上，服务器把算法和数据封装成标准接口，客户端client通过请求-响应机制来调用接口，也就是远程过程调用RPC的方式，SOME/IP就是基于客户端-服务器模型。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrZDAI8hox8cT9uKCkES1ic6IricGTuuDoTPdBuBibIU2gSLRxQaWtG8omA/640?wx_fmt=png&from=appmsg)

客户端-服务器模型

客户端-服务器模型适合数据集中且数据流向明确的系统，适用于需要直接交互的场景，即需要直接控制和管理的系统‌，比如文件服务器系统、邮件系统、数据库访问等。

另外一种模型，叫发布（Publisher）-订阅（Subscriber）模型。在这种模型中，发布者将数据以主题Topic为单位发送消息到代理，代理负责将消息路由到所有订阅该主题的订阅者。发布者和订阅者之间不需要建立直接的联系，发布者发送消息时不需要知道订阅者是否存在，订阅者订阅主题时也不需要知道发布者的具体信息‌。DDS就是基于发布-订阅模型。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrj4Hvwt1yribM15ethYPUibkHdb1goq3FPqYOjuNVnwyiafkvfWZ6J3t6w/640?wx_fmt=png&from=appmsg)

发布-订阅模型

由于发布（Publisher）-订阅（Subscriber）模型中系统的组件可以独立运行，不需要直接连接，所以适用于需要松耦合通信的场景，如消息队列、事件驱动架构、通知服务等，更适合分布式系统。

DDS以数据为中心，可以实现高效的数据传输和共享。数据发布者将数据发布到DDS网络中，订阅者可以选择订阅感兴趣的数据，并接收到相应的数据更新。与SOME/IP的面向服务相比，DDS面向数据，颗粒度小，灵活性强。

**2）支持多种QoS（Quality of Service）策略**

DDS支持多达22种QoS策略，用于定义数据传输的质量要求。可以根据具体应用需求进行配置和调整，以满足不同的性能和可靠性要求。而SOMEIP是不支持QoS的。

**3）大规模的可扩展性**

DDS具备大规模的可扩展性，能够适应复杂的分布式系统和大量的数据交换。它支持灵活的拓扑结构和节点间的动态发现，可以方便地扩展和集成新的节点和功能。

**4）较好的安全性**

DDS提供了一系列的安全机制，用于保护数据的传输和存储。它支持数据加密、身份验证、访问控制等安全特性，可以有效地防止数据泄露和未经授权的访问。

随着汽车电子系统对车内通信传输性能、安全性和灵活性提出更高要求，越来越多的OEM开始采用DDS作为通信解决方案。

**03**

**DDS协议**

DDS标准可以分为4个部分：核心标准、扩展标准、网关标准和API标准。其中，核心标准包括了4个协议：

1）DDS：主要描述了DCPS模型和QoS策略

2）DDSI-RTPS：定义了DDS基于有线传输的通信行为、报文格式等内容

3）DDS-XTYPES：描述了数据的序列化表示及Type System

4）DDS-SECURITY：描述了四类security策略，如认证、数据加密等

**3.1 DCPS**

DCPS（Data-CentricPublish-Subscribe）模型定义了应用程序在DDS中发布和订阅数据对象的功能。

DCPS由域（Domian）、参与者（Participant）、发布者（Publisher）、订阅者（Subscriber）、数据写入者（DataWriter）、数据读取者（DataReader）、主题（Topic）、监听器（Listener）等实体（Entity）组成。

域（Domian）是DDS的基本结构，是一个逻辑上的概念，由唯一的DomianID标识。域是基于不同的应用需求、安全性要求或其他特定的业务需求将不同的数据通信划分为不同的区域。只有在同一个域内的通信实体才能通信（交互数据）。不同域的应用实体，不能通信。

参与者（Participant）表示在特定域中的一个实体，也是服务的入口点，应用程序如果要发布、订阅数据，只有获取Domian Participant以后，方能创建、删除或者管理实体。即它是数据的发布者、订阅者和主题的创造者及管理者，负责管理DDS中的实体对象和通信配置。

发布者（Publisher）用来获取发布数据，并将其发布到对应的域中。发布者负责将数据发布到特定的主题（Topic）中，发布者Publisher作为发送方，可以包含一个或者多个DataWriter。

订阅者（Subscriber）接收发布者Publisher发布的数据，并将其传递给对应的上层应用实体。订阅者通过订阅相关主题(Topic)来接收所需的数据。订阅者作为接收方至少包含一个DataReader。

主题Topic是DCPS中定义数据传输的逻辑分类和组织单元。它可以看作是一种数据的标签，用于区分不同类型的数据。

主题主要由Name（名称）和Type（类型）构成，本质是网络中待传输的数据。Topic Name是一个字符串，且在Domian内唯一标识；Topic Type是数据类型定义，每个主题类型可以指定对应的Key，用于区分相同Topic的不同实例。

DCPS通信的模型中，DataWriter和DataReader的Topic必须一致，才能建立连接。

数据写入者（DataWriter）负责将数据写入到特定的主题中,上层的应用程序如果要发送数据，需要通过DataWriter，将特定的Topic写入指定类型的接口。DataWriter对数据编码，通过Publisher传输。一个DataWriter必须和一个Topic绑定。

数据读取者（DataReader）负责从主题中读取相应的数据。Subscriber通过DataReader从绑定的Topic中获取数据，然后传递给应用程序。一个DataReader可以绑定多个Topic。

它们之间的关联关系如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJr0O4oc5wfXW3ynKKO8ZlDFe3wcAGxtuMlNqlKVFLOsxU9DwnqjPObsw/640?wx_fmt=png&from=appmsg)

DCPS关系原理图

图中的结构看起来比较复杂，我们先化繁为简，首先要知道DCPS的最基本的原理就是"Publisher"发布者将"Topic"主题发布出来，而"Subscriber"订阅者则对感兴趣的主题进行订阅。

其中的"Topic"主题代表了一类数据的集合，用于标识一组相关的数据。这些数据是哪来的？或者说Publisher发布者首先是怎么获得数据的呢？

发布信息时，数据是通过"DataWriter"传递给"Publisher"的。而对于"Subscriber"，当订阅数据后，需要通过"DataReader"来访问和接收具体的数据。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJroK6HnFVunmibWgj7zyucXTpriaOR8jO9NlzTKTj1nPb1BPVNAlicyzn9g/640?wx_fmt=png&from=appmsg)

发布-订阅原理框图

这里需要注意的是，1个"DataWriter"或"DataReader"只能对应1个"Publisher"或"Subscriber",也可以理解成前者是由后者创造的，而1个"Publisher"/"Subscriber"可以创造多个"DataWriter"/"DataReader"。当我们想发布不同的"Topic"时，可以使用不同的"DataWriter"来向发布者传递数据。

当系统中有很多的"Publisher", "Subscriber"， "Topic"时，DCPS模型还会使用全局数据空间GDS（GlobalData Space）。全局数据空间是一个集中存储和管理所有数据对象的共享空间。一个全局数据空间即一个DDS域（DDS Domain），DDS域是一个逻辑上的容器。具体会由域中的参与者Participant来负责创建和管理"Publisher","Subscriber"，"Topic"。

对于订阅方来说，DDS还提供了以下两种基础策略：

1）Listen（监听）：订阅者可以使用监听方式来接收数据。它会一直等待，直到接收到数据为止。这种方式是阻塞型的，即订阅者在接收到数据之前会一直等待。

2）StatusCondition（状态条件）：使用Condition和Waitset（条件和等待集），订阅者可以实现异步数据访问。可以为一个或多个条件对象设置条件，然后等待条件满足或特定事件发生。这种方式是非阻塞的，订阅者可以继续执行其他操作，而不必一直等待。

通过选择适当的策略，订阅者可以根据不同的需求进行数据访问和处理。监听方式适用于需要及时响应并处理数据的场景，而条件和等待集方式适用于需要异步处理数据或等待特定条件发生的场景。

**3.2 QoS服务质量**

QoS（Quality of Service）是一种用于确定通信系统中信息传输质量的策略。QoS策略用于满足不同应用场景下对信息交互的特殊需求。

通过定义和配置一系列QoS参数和策略，能够在数据传输过程中实现对带宽、延迟、可靠性和安全性等的控制和优化。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrgiab3v0JuEicwqfBGGvqlrzezvef45xYticB4RxzPZzrhD8ZzMEbDva4A/640?wx_fmt=png&from=appmsg)

QoS服务质量

用户可以通过设置QoS策略来控制数据在应用程序之间共享的方式，如可靠性，周期等，以满足不同场景下应用程序对功能和性能的需求。

目前，DDS提供了22种不同的QoS策略，它们可以独立或组合使用。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrp0sYlynDpPsViba1hWwPmtWKxc5QnNribkOyiboSvfVRZtbibAOCqP4TibQ/640?wx_fmt=png&from=appmsg)

QoS部分策略表

表格中最左侧的一列是QoS的策略名称。

第二列Concerns表示QoS可为哪些实体配置，包括：Topic, DataWriter,DataReader, Publisher, Subscriber, 和DomainParticipant。

第三列的RxO表示是否兼容设置。YES表示通信两端要求兼容，也就是两端必须设置一致才能通信。NO表示可独立配置，N/A表示该QoS只在一端配置,不存在兼容的问题。

最后一列的Changeable表示实体Entity创建后是否可改变QoS配置，也就是运行时是否可改变此策略。

我们以QoS中的几个策略为例来介绍下它的功能。

**1）DURABILITY（持久性）**

DURABILITY策略用于确定数据的存储方式。可设置为VOLATILE、TRANSIENT\_LOCAL、TRANSIENT和PERSISTENT。

"VOLATILE"为默认值，表示数据不进行永久储存，仅提供给现有的订阅者。也就是说如果某个节点因为启动慢或者通信故障，错过了之前的数据，则不会再收到此数据。

"TRANSIENT\_LOCAL"，表示数据会保存在DataWriter的本地内存中，这样后加入的订阅者也能收到数据。

"TRANSIENT"表示由GDS保存数据，即使本地出现故障，订阅者也可以收到数据。

"PERSISTENT"表示由GDS永久保存，即使节点重启也不会丢失。

在车载通信系统中，Durability可以确保重要数据在异常情况下不会丢失。同时，持久性存储还可以支持数据的历史记录和回放，为数据分析、故障排查等提供有力支持。

SOME/IP也有重新获取数据的机制，但是只能从服务器去获取，如果服务端有故障，就无法获取。所以DDS的Durability策略更安全可靠，当然永久保存会占用大量存储空间，要根据需求设置。

**2）LIFESPAN（有效期）**

这个策略表示数据采集的有效时间，默认为永久。在车载通信中，有些数据变化慢，有效期长，比如电源模式、门开状态等；有些数据变化很快，有效期很短，比如转速、车速、雷达等数据。变化快的数据就需要将LIFESPAN的值设置的小一些，比如200ms,超过这个有效时间的数据就无效了。

**3）RELIABILIT（可靠性）**

这个策略用于确保数据传输的可靠性。它可以设置为"BEST\_EFFORT"或"RELIABLE"。

BEST\_EFFORT表示尽力送达，不保证可靠传输，数据可能会丢失或重复，适用于某些实时性要求较高的应用场景。

RELIABLE表示可靠送达，可以保证数据的传输和接收的可靠性。数据不会丢失，确保所有订阅者都可以接收到相同的数据。

由于以太网的传输层并不可靠，有可能发生数据丢失后重传，如果重传的数据太多，占用带宽太大，也会导致新的数据也无法发送。所以可靠送达是有代价的，要根据系统资源和数据对延时和可靠性的实际需求来设置。

**4）PARTITION（分区）**

这个策略通过一组字符串来定义发布者和订阅者的分区。分区是一种逻辑上的划分，用于将数据发布者和数据订阅者按照一定的规则进行分组。当发布者和订阅者使用相同的分区标识符时，它们将进行匹配并允许进行数据交互。这样可以实现对数据的精确过滤，实现灵活的数据管理。

PARTITION的原理类似于VLAN,但是它比VLAN灵活，VLAN是静态配置，而它是可以动态配置的。

**5）DEADLINE时效性**

这个策略用于约束数据的发送周期，发送端设置DEADLINE表示必须在给定的时间周期内写入数据；比如设置1s,则发送端必须在每个1s内写入数据,这个1s的周期实际上也说明了数据的有效期为1s。

**6）TIME\_BASED\_FILTER 时基滤波器**

这个策略表示在指定时间内只希望收到1个数据，多余的数据将被订阅者丢弃。这个策略主要是为了优化网络负载和节点的计算资源。

比如接收方要求1s接收1个数据，但是发送方是1s发送10个数据，则发送方检测到TIME\_BASED\_FILTER后，会降低发送频率，这样就可以节省带宽资源。

**7）PRESENTATION 表示**

这个策略可设置为Coherent Access和Ordered Access

Coherent Access表示如果一组数据之间有关联，就需要等这组更新的数据都到达后，应用程序才能访问这组数据...