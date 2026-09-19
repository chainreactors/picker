---
title: 车联网TSP为什么要用MQTT协议传输数据？
url: https://mp.weixin.qq.com/s/XvAhzAs-UE7zHH6zsADzaA
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:53:26.164113
---

# 车联网TSP为什么要用MQTT协议传输数据？

# 车联网TSP为什么要用MQTT协议传输数据？

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

智能化汽车大都配置了车联网功能，车联网主要由三大部分组成，手机端的APP、云端的后台服务器TSP和车端的中控娱乐系统/T-BOX/网关设备。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I8Nzvia1vh9YxaCpTVItKK893RJOUXBhbLnVmUCiblU2AAsN8BalMjlicdw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

车联网系统图

车辆中的各类数据通过车端设备（如T-BOX）统一采集后，会通过4G/5G移动通信信号传输到云端的TSP平台，TSP平台进行数据处理后，再将信号传输到手机端的APP，手机端的APP就可以显示车辆的相关信息，比如位置、电量、温度等信息。

同样，手机端的控制命令，比如车辆启动、打开车门、开启空调等信号也是通过这个方式反向传递给车辆。

在这个过程中，TSP平台既要连接车载终端设备、又要连接手机终端APP，还可能需要连接第三方的监控平台和内容服务商，因此TSP在车联网中处于核心地位。

**01**

**TSP简介**

TSP是TelematicsService Provider的缩写，表示远程服务提供商。

TSP连接硬件、软件、整车厂商，主要功能是负责汽车与服务商之间的数据采集与供应，为车主提供多样化服务内容，包括位置服务、导航服务、通信服务、社交服务、娱乐服务、远程保养服务、安全服务等，从而实现车联网。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I8m3maVz7KoymbbxAkOUs3PRdzG6lqHl3CnpfRHOr70v7fjNqNl70woA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

TSP平台系统示意图

TSP平台所能提供的各种服务功能的基础是数据，车辆与TSP平台、手机APP与TSP平台、TSP与其它平台间都需要进行大量的数据交互，这些数据交互也需要使用一定的通信协议标准。

**02**

**HTTP与MQTT**

车内控制器间的通信协议有多种类型，比如CAN、LIN、FlexRay、MOST、Ethernet等等。这些都是基于硬线连接的有线通信，不同的控制器会根据数据量、实时性和成本要求来选择不同的通信方式。

车联网主要涉及到车端与TSP后台间的通信，TSP后台与手机APP间的通信，是基于无线网络的车辆外部的通信，可以采用私有协议，也可以采用公有协议。

早期的车联网业务简单，采用私有协议的效率更高，但是随着车联网业务场景需求的增加和车辆数量的不断增加,私有协议会出现很多问题。

首先是私有协议的所有功能(如保活、重连、下线消息等)都需要定制开发，功能定义和版本更新难以维护。另外，私有协议还需要定制开发终端硬件来适配，导致成本高、周期长、更新迭代速度慢。所以主机厂逐渐的采用公有协议，公有协议中常用的是HTTP和MQTT协议。

**2.1 HTTP协议简介**

HTTP是Hypertext Transfer Protocol的缩写，表示超文本传输协议，它的出现时间比较早，设计目的是为了在Web服务和浏览器之间实现通用、无状态的数据传输，适用于传统的Web应用和多媒体传输‌。

HTTP基于请求-响应模式，可以通过HTTPS提供加密，安全性较高‌，可提供丰富的内容和多媒体支持，适用于需要频繁交互和大量数据传输的场景‌，广泛用于网站和Web应用，也可以用于车联网TSP系统间的通信。

由于HTTP应用成熟，而早期车联网的业务也相对简单，使用HTTP完全可以满足功能需求。

但是随着业务的扩展,HTTP的一些缺点也体现出来，HTTP采用的请求响应模式‌是一种同步消息传递模式，请求者发送请求消息，响应者返回响应消息。请求者和响应者之间需要建立直接联系，请求者需要等待响应者的响应才能继续执行。请求者一旦收不到响应，就会影响它的工作。

此外，HTTP的头部信息相对较大，这会导致更多的数据传输，随着功能和终端数量的增加,整个平台的流量呈指数级增长,请求连接容易产生中断，这种传统的请求-响应模式的通信出现了性能瓶颈，难以高效率的满足新的业务数据传输需求。

**2.2 MQTT协议简介**

MQTT是Message Queuing Telemetry Transport的缩写，表示消息队列遥测传输，MQTT设计目的是为了在低带宽和不稳定网络环境中实现轻量级的发布-订阅通信。它适用于物联网（IoT）和移动应用，支持设备间的实时通信‌。

MQTT采用的发布订阅模式‌是一种异步消息传递模式，其中发布者将消息发布到主题，订阅者订阅感兴趣的主题并接收消息。发布者和订阅者之间没有直接联系，可以实现一对多的消息传递。

与HTTP的请求响应模式相比，发布者发布消息后不需要等待响应，可以继续执行其他任务。订阅者可以在方便的时候处理接收到的消息‌。

此外，订阅者可以在运行时动态地订阅或取消订阅某个主题，系统能够适应不断变化的需求‌。它支持长连接，设备可以与服务器建立持久的连接，实时接收或发送消息‌。

‌MQTT支持通过TLS加密，具体安全性取决于实现和配置‌，相对来说。虽然安全性上可能不如HTTP。但是由于MQTT是轻量级设计，它的数据包头部非常小，有效减少了数据传输的开销。

MQTT常用于物联网设备、智能家居和远程传感器等场景，这些场景中网络连接可能不稳定且带宽有限‌，而车联网是物联网在交通系统领域的典型应用，网络特点相似，所以MQTT很适合车联网中车辆与云端的数据通信。

**03**

**MQTT协议特性及规范**

MQTT可运行在TCP/IP协议或其他提供有序、无损、双向连接的网络协议，具有如下的特性：

1）使用发布/订阅消息模式，提供应用程序的一对多消息分发和解耦。

2）是一种与有效载荷内容无关的消息传输。也就是它不关心具体的消息功能和含义。

3）消息传递有三个服务质量QoS

第1个服务质量称为“最多一次”，是根据运行环境尽最大努力传递消息。可能会发生消息丢失。这个级别可用于例如环境传感器数据，在这种情况下，即使单个读到的数据丢失也无关紧要，因为下一个数据很快就会发布。

第2个是“至少一次”，确保消息到达，但可能会出现重复。

第3个是“精确一次”，确保信息准确到达一次。这一级别可用于例如计费系统，其中重复或丢失的消息可能会导致不正确的收费。

4）传输开销小，协议交换最小化，以减少网络流量。

5）当发生异常断开连接时有通知相关方的机制。

当应用程序消息通过MQTT传输时，它们就会具有相关的服务质量QoS和主题名称Topic Name。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I8v8L6oElsYfdiagricaRpYxRiapvN02cOMxmrZVPjdh2ibr3E4KZVQWMo5Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

MQTT系统示意图

MQTT中的客户端是指发布或订阅消息的程序或设备；

服务器是指在发布消息的客户端和订阅消息的客户端之间充当中介的程序或设备。服务器负责处理客户端的订阅和取消订阅的请求，转发与客户端订阅相匹配的消息。

**3.1数据表示**

MQTT中的整数数据是按照16位的大端排序，也就是高位字节位于低位字节之前，网络传输时会先传送高有效字节，再传送低有效字节。

MQTT控制包中的文本字段用UTF-8编码字符串来表示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I8CqbeGxwbZZGSTbYEQQbvn8hcLIF1RyXAkVChxHic1EFbiaD59HHoE77Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

UTF-8编码的字符串结构

每个字符串都以1个双字节长度字段Stringlength作为前缀，String length表示了字符串的字节数，最大值为65535。

如果服务器或客户端收到包含格式错误的UTF-8的控制包，则必须关闭网络连接。

**3.2控制包格式**

MQTT协议通过一系列的MQTT控制包Control Packets来工作，控制包是通过网络连接发送的信息包，MQTT定义了14种不同类型的控制包，其中有1个（发布包）是用于传递应用消息。

MQTT控制包最多由三个部分组成，固定报头、可变报头和有效载荷，它们始终按下面表格顺序排列：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I8E9RmLEJGPDFtz0NrdqxibA69OExQFcvF24v8XeIhsWvQ2U1LUU2VPKQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

MQTT控制包结构

3.2.1固定报头Fixedheader

每个MQTT都包含1个固定报头Fixed header，固定报头由控制包类型、标志位和剩余长度组成，格式如下表所示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I8asmicmp7yfBJlqkqQlkNicfUeAGtGv0tulRIjEg2gqdfkCzNB26aNROw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

固定报头格式

控制包类型ControlPacket type位于Byte1,bit4-7,4个位最多可以表示16种类型。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I8ZBctewHICwGpqa6I9PkKzpZvL0XRtwAqQic1abhgiaF4rbzarniakGo3g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

控制包类型

标志位Flags位于Byte1,bit0-3,也是4个位，包含每种控制包类型特定的标志。如果收到无效标志，接收器必须关闭网络连接。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I8dECJJBRqQtibf075yfUe62p7rpVtcAUO33p9dPJy3hSwc02ANazp0YA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

Flags位

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I8g7VOeaiacJrEBA5vahjB0h57vSowrkuVWQhBichpYGWZrtT1g7M7piblQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

剩余长度从第2个Byte开始，剩余长度表示当前数据包中剩余的字节数，包括可变报头和有效载荷中的数据。剩余长度不包括自己编码占用的字节。

剩余长度使用可变长度的编码方案，单个字节最多可以表示127个字节。更大的数值采用如下的处理方式：

每个字节的最低有效7位（bit0-6）对数据进行编码，最高有效位(bit7)用于表示还有后续字节。因此，每个字节可以编码128个值和1个“连续位”。剩余长度字段的最大字节数为4，也就是这个字段的可变长度是1-4。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I834OD78nmPhvZXRKT3RCkYmhPIOwMwTeqt2MByL5icvpdxgJGDN3qnaQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

Sizeof Remaining Length field

上表是剩余长度的范围，单字节比较简单，容易理解，多字节相对复杂一些，下面举两个例子说明下：

例1：数字64，其对应的十六进制数为0x40，只用1个字节，由于剩余长度单字节表示时，最高位（bit7）必须为0，而0x40的最高位本就是0，所以最后的剩余长度值仍然是0x40，这也验证了小于127的数可以用单字节来表示。

例2：数字321，数字321可以转换为65+2\*128。需要编码为两个字节，第1个字节是低有效位65，对应16进制数是0x41。由于最高位（bit7是1），所以实际上第1个字节是65+128=193，也就是0xC1。最高位是1，表示至少还有1个后续字节，则第2个字节是2，高字节的2就表示2个128，也就是256，256+65=321，所以最后剩余长度的数值是0xC1 0x02。

3.2.2可变报头Variableheader

某些类型的MQTT控制包包含可变报头组件。它位于固定报头和有效载荷之间。可变报头的内容因数据包类型而异。可变报头中的Packet Identifier字段在几种数据包类型中是共用的。

许多控制包类型的可变报头组件包含2个字节的Packet Identifier包标识符字段。这些控制数据包的类型是PUBLISH（其中QoS>0）、PUBACK、PUBREC、PUBREL、PUBCOMP、SUBCRIBE、SUBACK、UNSUBSCRIBE、UNSUBACK

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I8c41ShzrOEPcljTrSNPnuVwmBFsnEGM1qYnyyIs86jolabjJiaxjuxicg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

Packet Identifier bytes

SUBSCRIBE, UNSUBSCRIBE和 PUBLISH（QoS>0时）控制数据包必须包含数据包标识符。每次客户端发送这些类型的新数据包时，都必须为其分配一个未使用的数据包标识符。

如果客户端重新发送特定的控制包，则它必须在后续重新发送该包时使用相同的包标识符。

PUBACK、PUBREC或PUBREL数据包必须包含与最初发送的PUBLISH数据包相同的数据包标识符。同样，SUBACK和UNSUBACK必须分别包含相应的SUBSCRIBE和UNSUBSCRIBE数据包中使用的数据包标识符。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I8BvYgbU5zbwRaHQ3iazciaXP6bYMAN0HiawSuicunZpoIial38nsu20ykcOA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

控制包是否包含包标识符列表

3.2.3有效载荷Payload

有些MQTT控制数据包包含有效载荷并会将它作为数据包的最后一部分。比如有的PUBLISH数据包会包含有效载荷，此时有效载荷就是指应用消息。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I82dVwT9SephGxeD55Mdf1EW3koQmEQ53FnibUoAvpyfXXWic9PXLZZsCA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

控制包包含有效载荷列表

通过MQTT协议控制包格式可以看出，MQTT的报头由于涉及的信息比较少，比较简单，比如固定报头只包含控制包类型、标志位和剩余长度三个字段，最多5个字节。

而HTTP的报文由于包含的信息很多，如请求方法、资源路径、协议版本、状态码、原因等，占用的字节数多。此外，HTTP报头还包含安全性设置、性能优化、语言设置等。这些信息虽然可以提高网络稳定性、安全性和用户体验，但是影响了网络通信的效率和性能。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicubdpAic1L0hYuVOQP6p7I81C8xdktworDsribScua7ORTiaZLicwLqRgziacUmXcNVXa0icIXBGbBQbVw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

报头大占用带宽资源，传输效率低

随着汽车销售量的不断增加，TSP平台接入车辆终端的规模不断扩大，在高峰期间，平台需要能够维持接入几十万量级的并发连接。

为了实现丰富的业务场景，每个连接到云端的车载设备都会同时有多种上行及下行数据传输。所以当车辆数量达到几十万量级时，平台就需要支持百万级的消息吞吐，这对数据传输的效率、实时性都有很高的要求。

此外，车辆在行驶过程中经常会遇到遮蔽、隧道、基站切换等复杂网络环境，造成车辆终端与云端的链接断开，HTTP在不稳定网络环境下可能需要频繁重试，影响效率和用户体验‌。而MQTT协议...