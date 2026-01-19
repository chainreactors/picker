---
title: 车载以太网 | 传输层：TCP&UDP详解
url: https://mp.weixin.qq.com/s/lJgJn0VzBeR_UNhFRcGAFg
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:37:07.049435
---

# 车载以太网 | 传输层：TCP&UDP详解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UgnH8yibPexHvrGteUe5IFhoSfQjPYvH4ggF5C3PwG055Ye8EmKh23Ig/0?wx_fmt=jpeg)

# 车载以太网 | 传输层：TCP&UDP详解

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247564281&idx=2&sn=699099fdf353a20e4b133c9bb09efbe0&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UHbPPhwKHtIkGH8yROIpENCZ8kyK1Jxr2sMMrsCUV70mQbibAJNhI9cg/640?wx_fmt=jpeg&from=appmsg)

**01**

**为什么需要传输层？**

IP协议就能够实现源节点和目的节点之间的数据传输，为什么还要传输层呢？

两个设备之间的通信不是简单的数据传输，更准确的是两个设备上的应用进程之间的数据交换。换句话说，IP层虽然将数据报从源节点发送到目的节点，但该数据报还只是停留在网络层，而没有往上层（应用进程）交付。传输层即是在网络层基础之上，为应用进程提供通信服务。如下图所示：

计算机A上的微信（应用进程）发送消息给计算机B，怎么能保证是计算机B上的微信接收到消息，而不是QQ或小红书（其他应用进程）接收到信息呢？这就是传输层为相互通信的应用进程提供逻辑通信的简单举例。

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UjMIQX5PV6zqk9vmKtcZHsPLYaqyhVTgY1IJ48ClZLKNGvXyAicrBdEA/640?wx_fmt=jpeg&from=appmsg)

并且，在网络层介绍IP数据报格式时，首部校验和字段只验证首部是否有错误，而没有对数据部分做校验。在传输层，就会对收到的数据报进行差错检测。

**02**

**协议端口的作用**

仍以上面的例子来看，

* 计算机A上的微信、QQ、小红书（不同应用进程）发送消息给计算机B，都需要进行传输层的数据传输给到网络层，即传输层的复用；
* 计算机B收到传输层的消息后，需要指明数据交付给微信、QQ还是小红书，即传输层的分用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UCTpyW5sTicT7gLyo1GURtvZxkO7GrdlBic7W2dPldlC44QCgN3PmnP6A/640?wx_fmt=jpeg&from=appmsg)

要实现A微信与B微信（应用进程）之间的通信，就需要在传输层和应用层之间指明传输终点。这就是协议端口的作用，即A微信数据经过传输层后通过端口1发送给B微信应用层。通过端口号就能实现应用层的不同协议进程与传输层的交互。需要指明的是：

* 这里的端口是软件层面的，与ECU上的硬件端口是不同的概念。
* 不同ECU上的相同端口号是不存在关联性的。（如：A微信端口号1和B微信端口号1不搭噶）
* 端口号区分源端口和目的端口。
* TCP/IP的传输层用16位端口号来标识一个端口，16位端口号有65535个不同端口号。
* 常见端口号：DoIP：13400\3496、HTTP：80、HTTPS：443等。

**03**

**UDP用户数据报协议**

车载以太网复用传统以太网的传输层两大主要协议UDP和TCP。其中，用户数据报协议UDP（User Datagram Procotol）只是在IP数据报基础上增加了复用分用和数据差错校验功能。

**3.1 UDP的特点**

**1、UDP是无连接的。**

* 数据发送前，不需要建立连接，降低时延，实时性强。

**2、UDP不保证可靠交付。**

* UDP尽可能的交付，不需要维持状态表。

**3、UDP是面向报文的。**

从下图可直观看到，

* 对应用层发来的报文，UDP不合并，也不拆分，直接照搬，添加UDP首部后发给网络层。
* 对发往应用层的报文也一样，直接去除UDP首部后交付给应用层。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UI1NoaM6MT2rB08TbNlnaL2ZBmedrEoAf4kGooJ7Ciahaia1NIMpdy5icA/640?wx_fmt=png&from=appmsg)

**4、UDP没有拥塞控制。**

* 即出现网络拥塞时，UDP不会降低源节点的发送速率。
* 拥塞出现时，可能会出现数据丢失。（类似视频聊天的卡顿丢帧）

**5、UDP支持一对一、一对多、多对一和多对多的通信。**

**6、UDP的首部开销小，只有8字节。**

**3.2 UDP的报文格式**

UDP首部4个字段，每个字段都是2字节。

**源端口：**源端口号，需要对方回复时选用，否则可用全0。

**目的端口：**目的端口号，在目的节点交付报文时必须要用。

* 目的节点UDP发现接收报文中的目的端口不正确，会丢弃该帧，并通过ICMP报文（Type=3、Code=3）发送端口不可达给源节点。

**长度：**UDP数据报的长度，在仅有首部时，最小长度为8。

**校验和：**检测UDP数据报是否有错误，有错就丢弃。

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UP1Jo7hLPcbtRAZTibDrXYuMqhNe1VqlSYsH2rbHoL3nvFOT7PTde4Bw/640?wx_fmt=jpeg&from=appmsg)

**关于UDP的校验和字段的计算，一个很有意思的点：**

UDP计算校验和时，会在原UDP数据报之前增加12字节的伪首部。

* 伪首部仅在计算UDP校验和时使用，不向上下层交付。
* UDP校验和校验范围：伪首部+UDP首部+UDP数据。
* 既校验了收发双方的端口，也校验了IP地址。
* 源节点发送报文时，先以校验和字段为全0来计算出校验和填入。

**04**

**TCP传输控制协议**

介绍了较为简单的UDP协议，我们再来看看较为复杂的TCP（Transmission Control Protocol）传输控制协议是什么。

**4.1 TCP的特点**

**1、TCP是面向连接的协议。**

* 先建立连接，再进行数据通信。

**2、TCP保证可靠交付。**

* TCP传输数据是无差错、不丢失、不重复、按序到达的可靠传输。

**3、TCP是面向字节流的。**

* 所谓面向字节流，是指数据传输的字节序列。TCP传输数据仅看作是无结构的字节流，不知道具体字节的含义。
* 一个TCP报文所包含的数据长度是不固定的。(如下，字节流中一个颜色表示一个TCP报文)
* 收发双方的字节流是完全一致的。
* TCP不保证收发双方的数据块具有对应大小的关系。（可能发4个，收到后只用2个交付给上层）

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UpccVLTkQjAPVicjVjNwYbvpu6hZ4yug21xpaG9ZXCSdFXCicv6FNtfyw/640?wx_fmt=png&from=appmsg)

**4、TCP连接是点对点的。**

**5、TCP是全双工通信。**

**4.2 TCP的报文格式**

TCP报文首部前20字节是固定的，即首部最小长度为20字节。

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UUwa8V8e8mZO4uicZkj6as0yfKZ9y5aTBzQzkFpIWiatNt30nFheRtNDQ/640?wx_fmt=jpeg&from=appmsg)

源端口Source Port：2字节，源节点端口号。

目的端口Destination Port：2字节，目的节点端口号。

序号Sequence Number（seq）：4字节，标识本报文段所发送的数据的第一个字节的序号。

* 序号范围0-2^32-1，当序号增加到2^32-1后，下一个序号转回到0。
* TCP面向字节流，传输的字节流都按顺序编号。
* 同一个颜色为一个TCP报文，依次编号：

一报文段的序号字段值=1；

二报文段的序号字段值=4；

三报文段的序号字段值=13；

四报文段的序号字段值=19。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UialWSj5rUibMY4UG0lW5jLU5JWvicmogOzhV3FRNey3Lxx0cbZmrQTOUw/640?wx_fmt=png&from=appmsg)

确认号Acknowledgment Number（ack）：4字节，标识期望收到对方下一个报文段的第一个数据字节的序号。

* ECU2正确收到ECU1发来的TCP数据段，序号为1，长度为3；
* ECU2期望收到ECU1的下一个数据段的序号为4；
* 此时ECU2在发给ECU1的确认报文段中把确认号设为4。

指明两点：

* 收到确认号为x，表明到x-1的全部数据都已经被正确收到。
* 序号轮询重复使用时，表示旧序号数据已正确收到。

数据偏移Data Offset：4位，实际是TCP首部长度，单位是4字节。

* 4位的最大长度为15\*4=60字节。

保留Reserved：6位，目前为全0。

紧急URG：1位，URG=1时，表示紧急指针字段有效，用来告诉系统该报文段中存在紧急数据。

* 紧急数据相当于高优先级数据，要尽快传送，而不按原顺序传送。
* 这就像路口排队的车辆（普通Data）一样，突然后面开来一辆响着急救铃（URG=1）的救护车(紧急Data)，就不能排队等在后面了，需要其他车辆让路先行通过。

确认ACK：1位，仅当ACK=1时确认号字段才有效。ACK=0时，确认号无效。

* TCP建立连接后，所有传送的报文段都必须让ACK=1。

推送PSH：1位，不等接收方缓存填满后才交付，而是直接交付应用层。

* 发送端PSH=1时，接收端收到该报文后直接交付到应用层。

复位RST：1位，RST=1时，表示TCP连接出现严重错误，必须释放连接，进行重新建立连接。

同步SYN：1位，用来做同步序号。

* 当SYN=1 & ACK=0，表示是一个连接请求报文段；
* 若同意连接，则响应报文中SYN=1 & ACK=1。

终止FIN：1位，用来做释放连接。

* 当FIN=1时，表示此数据传输完成，要求释放连接。

窗口Window：2字节，指发送本报文段的一方的接收窗口。

* 即告诉对方，从该报文段首部中的确认号算起，接收方目前允许对方发送的数据量。
* 窗口的整数范围为0-2^16-1。
* 窗口的数值指明了当前允许对方发送的数据量。

* ECU2正确收到ECU1发来的TCP数据段，序号为1，长度为3；
* ECU2期望收到ECU1的下一个数据段的序号为4；
* ECU2在发给ECU1的确认报文段中把确认号设为4，窗口设为5。
* ECU1收到报文后，就知道ECU2目前能接受5字节数据，ECU1最大就能发5字节。

校验和Checksum：2字节，校验范围：TCP首部+数据部分。

* 与UDP校验时一样，TCP计算校验时也要在报文前加12字节的“伪首部”，伪首部格式也一致（协议字段=6）。

紧急指针Urgent Pointer：2字节，表示本报文段中的紧急数据的字节数，仅在URG=1时才有效。

* 紧急指针标出了紧急数据的末尾在报文段中的位置。
* 当所有紧急数据处理完，恢复正常操作。
* 即使窗口为0，也可以发送紧急数据。

可选Options：长度是8位的倍数，如存在，需加入到校验和的计算中。最大不超过40字节（TCP首部最大长度60-固定20=40）。

填充Padding：0填充，确保TCP报头结束。

**4.3 TCP建立连接-三次握手**

**4.3.1 什么是socket套接字**

TCP连接的两个端点叫做socket套接字，注意这不是前面提到的协议端口。

在RFC 793中将socket描述为一种地址，是IP地址和端口号的连接。即：

Socket = （ IP Address ：Port ）

如IP地址=192.168.0.1，端口号=443，则socket = 192.168.0.1 : 443。

所谓TCP面向连接，即由通信双方的socket所唯一确定。这是TCP建立连接确认对方存在的关键。

**4.3.2 建立连接的过程**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5U2tog3dtNk1LqrbzITuzetwO5SribXTDiaZ34bTF9pLHafNDMBESXJNGg/640?wx_fmt=png&from=appmsg)

在TCP报文格式中清楚了同步SYN、确认ACK、确认号ack、序号seq的作用，就不难理解三次握手。需要指出的是：

* ECU2请求建立连接时，请求报文中SYN=1，不能携带数据，但是仍然会消耗掉一个序号。
* ECU1同意ECU2建立连接时，回复的报文也不能携带数据，同样也会消耗掉一个序号。

**这里有一个面试经常遇到的问题：2次握手行不行？**

**不可行。**

1、假设ECU2发送第一条请求连接报文，因网络原因延时到达；

2、ECU2发送的第二条请求连接报文正常被响应确认，2次握手成功进行数据传输；

3、此时ECU2发送的第一条请求连接报文到达ECU1，ECU1响应确认，建立新的连接；

4、ECU2由于没有发送连接请求，是不理会ECU1的确认报文的，也不发送数据；

5、即会导致“沟通偏差”，ECU1一直等ECU2的数据，造成资源浪费。

**4.4 TCP释放连接-四次挥手**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UibZNwD7e7bEKAVAugct8wvDEiaXficgQjjdLR3DRHW4dEzCicsTcngLx4w/640?wx_fmt=png&from=appmsg)

过程看图不赘述，指明三点：

ECU2主动请求释放报文FIN=1，seq=u，该报文即使不携带数据，也会消耗掉一个序号。

ECU1被动关闭，此时ECU2已经没有报文要发了，但ECU1可能还有没发完的报文在继续发送给ECU2。

* 正因为ECU1有报文在发送，所以seq是从v到w（不确定报文数量）
* ECU2没有报文要发，所以ECU1发的报文中ack一直为u+1。

MSL（Maximum Segment Lifetime）最长报文寿命是为了保证ECU2发出的最后一条报文能被ECU1成功接收。万一在2MSL时间内报文丢失了，ECU2可以超时重传并重启2MSL计时器。否则ECU1收不到最后一条报文无法关闭。2MSL也能避免2次握手中提到的类似问题。

**4.5 TCP的状态机**

所谓TCP的状态机，即是下图红圈中收发双方从CLOSED到CLOSED的各个阶段状态的跳转，同时涵盖了各种异常情况下的状态切换，类似AUTOSAR网络管理的状态图。暂不展开，后续在TC8测试中涉及到再介绍。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwictNbyF6vOpb0iaDQmN6zv5UY9wNgDhZMwzHyR7TLoxUPzb2kOZlQ5Qw4H4iaOb9jQ63BlY3NVqjXuQ/640?wx_fmt=png&from=appmsg)

来源：乙乙的车COOL

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=ap...