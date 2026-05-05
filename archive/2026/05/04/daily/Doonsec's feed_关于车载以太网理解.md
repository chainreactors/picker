---
title: 关于车载以太网理解
url: https://mp.weixin.qq.com/s/vDtZdu1BPfjxNeBb_y49CA
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:58:09.052153
---

# 关于车载以太网理解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCzsHARI6we2R1Ml7BFGwjNicsQ37MOKiaKYhF2icniaG4665s16kpW5LKqaiaUfJwD48tMDtWvIQ7sIIt2gjIplCDoXju8SFUXRiae4/0?wx_fmt=jpeg)

# 关于车载以太网理解

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAgXyLqfnkPJhyibCoBSOMGSsdQ03SEf01kcUbPAEzhf5nb6vyvYWINevstJCARUgy8qNpTa2lKVo7g7RPFm8IicY9aYtviaowaTE/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

**01**

**车载以太网概述**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrNgjWy8546cvRq5BOX1DZbpJ1s0vwayWlH9DdYtZay4EJTgOeXdzVibQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

其中与车载以太网强相关的模块有：

* SOME/IP（Scalable Service-Oriented MiddlewarE over IP）：是一种用于传输服务（Service）信息的基于IP的可伸缩中间件，能够适应基于不同操作系统的不同大小的设备，小到摄像头，大到车机或自动驾驶模块；相比于传统的CAN总线的面向信号的通信方式，SOME/IP是一种面向服务的通信方式。
* DoIP：基于以太网的诊断传输协议，能够将UDS进行封装并基于IP网络进行传输；应用于车辆检查和维修、车辆或ECU软件的重编程、车辆或ECU的下线检查和维修等，其主要工作原理类似于Diagnostic over CAN（或称为DoCAN）。
* XCP：XCP on Ethernet能够基于以太网进行车载控制器的标定，主要用于标定、测量、少量的编程和刷新（大部分刷新会利用诊断协议）、ECU旁路功能等。
* UDPNM：是AUTOSAR组织制定的基于汽车以太网的网络管理协议，能够有效的实现车载以太网节点的协同睡眠和唤醒，其主要工作原理类似于AUTOSAR的CAN NM

其中与传统以太网最核心区别是物理层车载以太网要用 100BASE-T1,而非100BASE-TX，下面依次介绍与车载相关的各层。

**02**

**物理层 PHY**

**2.1 总体说明**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJreAm6ZcMScXYn6vho2bwXupdYFcfRdDQz5JUyuEQEl72zlKTSfJs2xQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

物理层PHY：数据传送与接收所需要的电与光信号、线路状态、时钟基准、数据编码和电路等，并向数据链路层设备提供标准接口；

数据链路层MAC：提供寻址机构、数据帧的构建、数据差错检查、传送控制、向网络层提供标准的数据接口等功能。

100BASE-T1在物理连接上使用了一对双绞线实现全双工的信息传输，而100BASE-TX则使用了两对双绞线实现全双工，一对用于收，另一对用于发。

100BASE-T1利用所谓的回音消除技术（echo cancellation）实现了在一对双绞线上的全双工通信。

回音消除技术的主要过程：作为发送方的节点将自己要发送的差分电压加载到双绞线上，而作为接收者的节点则将双绞线上的总电压减去自己发出去的电压，做减法得到的结果就是发送节点发送的电压。

车载以太网固定为全双工通信方式，出于对汽车启动时间的考虑而没有引入自动协商机制，此外车载以太网是通过单对非屏蔽或屏蔽电缆连接。

**2.2 物理层架构**

物理层主要作用：

1）定义硬件接口；

2）定义信号与编码；

3）定义数据与信号之间的转换收发；

物理层基本架构

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrlI5eFqJvPEPIzdygFGPyvqoH343Rqh74q82mQQJnkOHIKfbficoGCRg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

主要包括PMD，PMA和PCS。

PMD，介质依赖层，主要职责是转换PMA的数据与实际网络上的信号。发送时，它从PMA读取数据并执行实现该功能所需的必需的低级行编码功能设计的媒介。接收时，它会读取并解释这些内容编码信号，然后将它们转换回位以发送到PMA。

PMA，介质连接层，结余PMA和PCS之间，其中PMD是按照bit串行处理方式，而PCS则是按照数据块处理方式，因此PMA则是起到中间转换的作用，此外还起到数据冲突检测的功能。

PCS，编码子层，主要进行初始编码 ，实现特定于以太网速度和传输介质要求的子层中的一部分。

**2.3 物理层控制器的架构**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJr0GQHPp0oGibMODEyaPwvyZB6g05LXbJH5415NyWKmGZibGicpCMicbBicBw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

其中，MDI ， Medium Dependent Interface。MII Medium Independent Interface,MIIM主要用于寄存器的配置管理。

我们这里需要注意的是RXD 和TXD都是4个数据。

**2.4 物理层编码原理**

首先总线上的电平信号有，-1 0 和 1如图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJr005NvLu1rW4VBib2WZsUBXAzLibsGhciaNlibbF4bHt6PyOiaAfLl5TU1TA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

数据和电平的编码转换关系有如下表关系：

如数据 000 对应两根线上的电平为 -1 01 ，

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrnUJmxeHUc7lruX40sbtB6kxbk5WE15AHXbMzywKA97tbbNTEibY0zRw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

主要数据到电平转换过程为以下四步：

1.首先从MII接收到数据（4bit 4bit...）

2.接下来分割成(3bit 3bit...)进行处理；

3.根据上表，电平与数据编码的关系，转换为电平信号；

4.将电平信号发到总线。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrjW2Fib89ZCt5DhHxEBQqDLBEuR6NfPiaCpjgj9Z4E89kcbx9qedpuODg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

一个案例说明以上的转换过程：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrJicr7Lr4icsR6II5yEo9eiaG7sB4hpCdMC9akxMeCibm9qEV5t32DAo1xA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

100Mbps 速度的由来：

在微控制器的每个时钟周期中，MII接口到来的数据是4个bit，PHY从MII接口收到数据后，会首先进行一个4B3B的转换，为了匹配25MHz \* 4bit = 100Mbit/s的速率，PHY的MII接口时钟周期应该是33.3333M，每次接收3bit，也实现了33.3333M \* 3bit = 100Mbit/s的速率。之后PHY要再进行3B2T的操作，将每次接收到的3个bit转化为2个电平值（取值范围是-1，0，1），具体的对应关系如上图中的表所示。3个bit有8种组合（即2的三次方），两个电平值有9种组成（即3的平方），所以后者可以覆盖前者。此时时钟周期仍然是33.333M，但是每个时钟周期中的两个电平就能够表示3个 bit了，所以此时的数据速率仍然是100Mbit/s，每个电平实际上包含了1.5bit信息。最后一步是PAM3，将逻辑的-1，0，1转化为在双绞线上的电压，所以，最终在总线上信号的波特率是66.666MHz，但是它实现了100Mbit/s的通信速率。

**03**

**链路层 MAC**

MAC层主要内容，

1) 寻址

2) 传输方式

3) 帧格式

**3.1 MAC控制器架构**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrDXEO0EAPkfvyWt5cia8nngSFoUVSPmgzZ0iaulYnMYNrkm74ETT3eiaIQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

其中比较关键的是MII 和 MIIM 与PHY接口连接。

数据发送，MAC协议会判断当前是否适合发送数据，若能，它会在将要发送的数据上附加一些控制信息，最终使数据以规定的格式到达物理层；

数据接收，它会判断数据是否有错误，如果没有错误的话，它会去掉附加的控制信息发送至LCC（逻辑链路控制）子层。

SMI接口包括MDIO（控制和管理PHY以获取PHY的状态）和MDC（为MDIO提供时钟）。

MDC由MAC提供，MDIO是一根双向的数据线。用来传送MAC层的控制信息和物理层的状态信息。

MDIO数据与MDC时钟同步，在MDC上升沿有效。

**3.2 MAC地址**

在我们给别人联系时，我们往往需要知道对方的邮件地址或电话或住址，而以太网通信也是类似。因此需要通信的两个设备，必须具有唯一标识的MAC地址。

MAC地址长度为48bit、6byte，前三个字节是组织标识ID，后三个字节是本地管理ID。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJriaHj77f4XibOCaJJnsBeeicAEIibJSrKXicuhjnp2M6knJ3mY8EibHVPKmNw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

全局或本地地址U/L：第一个字节的第二位MAC地址的OUI字段（从右数第二低位开始计数）被称为U / L（通用/本地）标志。 设为0时，将MAC地址标记为被普遍管理； 当它是1时，MAC地址是本地管理的。

单播与组播MAC地址I/G：OUI的第一个字节的第一个（最低有效）位MAC地址的字段，称为I / G（个人/组）标志。当这个位设置为0，MAC地址是单个设备，并且消息是单播。设置为1时，表示组地址（多播）。

广播MAC地址：FF-FF-FF-FF-FF-FF

**3.3 数据传输**

主要介绍一下CSMA/CD 冲突检测方法。

在以太网中，网络不断监控（或感知）传输线，侦听确定线路是否繁忙。任何设备听到正在进行的传输则禁止尝试发送自己的消息，直到线路空闲为止。

它可以检测到网络上是否有数据在传送，如果有数据在传送中就等待，一旦检测到网络空闲，再等待一个随机时间后将送数据出去。如果两个碰巧同时送出了数据，那样必将造成冲突。这时候，冲突检测机构可以检测到冲突，然后各等待一个随机的时间重新发送数据。这个随机时间很有讲究的，并不是一个常数，在不同的时刻计算出来的随机时间都是不同的，而且有多重算法来应付出现概率很低的同两台主机之间的第二次冲突。

**3.4 MAC帧格式**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrL5noET45jymfr5kibcInhkVYWKvSjTtOAQyibG6ErKVyt2bibmMXPJYhw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

Preamble：7byte 帧前缀，主要用于帧设备之间的事件同步；

Start of frame delimiter：1byte,标识帧开始

MAC destination ：目标MAC地址

MAC source ： 源MAC地址

802.1Q Tag：是一个可选项，主要用于VLAN，如在这个字段中定义VLAN的ID或优先级等，未定义的则会自动把该帧丢弃。

length：数据长度/payload长度

Payload：有效负载、数据

frame check ：CRC

interframe gap ：帧之间的间隔

**04**

**网络层**

**4.1 IP地址**

主要作用为，寻址，数据封装，路由。仅以IPV4说明

长度为4byte 32bit，每个字节用dot隔开，用十进制表示。

192.168.0.1      ，其中加粗的前三个字节192.168.0 表示网络ID，最后一个字节 1表示主机ID

网络ID（网络ID）：一定位数，从头开始从最左边的位开始，用于标识主机或位于其他网络接口。 有时也称为网络前缀，甚至只是前缀。

主机ID（主机ID）：其余位用于标识 网络上的主机。

IP地址类别：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrbSbPiaCMh0afzVsicNp9pZ2OTF6M3SuRTtSa2dv56Qa40Ob99pgZbicwQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrOpQWEWlWr565m2Vm98ZzXD8iae1UmZfMrRYnFQAiaKhwKOTmknZxPT2w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

A类地址第一字节为网络ID，后三个字节为主机ID，范围是1.0.0.1—126.155.255.254；

B类地址第一二字节为网络ID，后两个字节为主机ID，范围是128.0.0.1—191.255.255.254；

C类地址前三个字节为网络ID，最后一个字节为主机ID，范围是192.0.0.1—223.255.255.254

D类地址：为组播地址

224.0.0.0～224.0.0.255为预留的组播地址（永久组地址），地址224.0.0.0保留不做分配，其它地址供路由协议使用；

224.0.1.0～224.0.1.255是公用组播地址，可以用于Internet；

224.0.2.0～238.255.255.255为用户可用的组播地址（临时组地址），全网范围内有效；

239.0.0.0～239.255.255.255为本地管理组播地址，仅在特定的本地范围内有效。

D类地址的MAC有特殊转换关系：

MAC地址前三位为：01 00 5E

MAC地址后三位为：0x7FFFFF & 组播IP地址

举例来说 组播IP地址 242.147.109.235 对应的MAC地址为：01.00.5E.13.6D.EB

**4.2 IP协议**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibEbvefcYnoWrZFHZskRlJrMhnbI4EsUH8g9bxMS0ML77Ure7GzT7NMhaq8HroXGibGNkcec5n1NicQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

Version：版本  如4表示IPV4      IPV4:4，IPV6:6

IHL：Internet Header length，Header 长度  没有选项，则一般为5（5x32bit＝20B）

DSCP：Differentiated Service   一般没有使用，详细参考RFC

ECN：Explicit Congestion Notification  用于扩展检测丢包

Total length ：总长度，header＋数据 总长度

Identification ：占16位,它是一个计数器,用来产生数据报的标识

Flags：标明是否分片 bit 0: Reserved; must be zerobit 1: Don't Fragment (DF) bit 2: More Fragments (MF)

Fragment Offset :占12位,指较长的分组在分片后某片在原分组中...