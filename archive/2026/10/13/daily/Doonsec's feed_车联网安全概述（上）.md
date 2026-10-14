---
title: 车联网安全概述（上）
url: https://mp.weixin.qq.com/s/rcQit1ejGb4garSMYawzug
source: Doonsec's feed
date: 2026-10-13
fetch_date: 2026-10-14T06:50:48.232822
---

# 车联网安全概述（上）

# 车联网安全概述（上）

原创

朝阳
朝阳

Sec朝阳

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 车联网安全概述（上）

# 车辆网络与协议

本章节介绍车辆中使用的各种通信网络类型。现代车辆通常配备多个ECU，这些ECU通过不同类型的网络连接。

首先从汽车制造商提供的文档入手。寻找在线门户网站，上面有电路图和其他的信息和软件。

接下来介绍车辆中最常用的网络，LIN、CAN、FlexRay以及各种类型的车载以太网。CAN总线章节还涵盖了总线上发送的消息类型，以及常见的完整性保护措施，例如计数器和校验和。

# 一、车辆文件

## 1、制造商文档

许多汽车电路图（EWD）或诊断软件都可以在网上以低价购买。这些通常提供给消费者，以符合美国的维修权或欧5排放标准。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBMnYoBxwF1EAaPECOz5mkBXe1Lzr2yuKTWF9jSQcaK7UQkbJBZslsCRA62Fqg1JAySuUh31m87gCT2RgK1icj6UXGialBwRgZs8/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaC7L9SOGHHlCicliaalepsicbWeYialv5zaqlmudxMZsG0Pbia0ibNFe1GGibtUbr6icD2greiakn6wia9hBhu1ibsm17GQHibvtAZVArsmy4g/640?wx_fmt=png)

## 2、J2534直通装置

J2534是一种用于USB转CAN适配器通信以重新编程ECU的标准。汽车制造商要求允许消费者或独立维修技师使用J2534刷新ECU以满足排放要求。CAN适配器制造商通常会.dll为其适配器提供J2534兼容版本。

订阅服务通常包含一个诊断程序，该程序可通过J2534兼容适配器与车辆连接。但是与原厂诊断工具或平板电脑相比，该软件的功能有时会受到限制。

简单来说，J2534直通装置就是给汽车电脑刷机的工具。就像手机刷机要用电脑+数据线一样，汽车也有个电脑（ECU），刷固件要用这个标准接口和适配器来操作。

## 3、接线图

常见的电路图是电气线路图（EWD）。它显示了ECU与各种组件之间的线路连接，以及连接器和引脚编号。需要注意的是，ECU通常会在电路图中被分成不同的部分，并且可能分布在多页上，每页显示不同的引脚。特定的ECU或连接器通常也有字母/数字组合的标识，甚至同一制造商的不同车型之间也可能重复使用这些标识。

## 4、CAN总线图

另一种比较关键的就是显示连接到特定CAN总线的所有设备的图表。下图显示了起亚EV6上的ADAS CAN总线，连接着四个角雷达。这种图表可以帮助我们找到CAN总线的最佳接入点。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaBOZcyUe8rH3CdpGvY7Mznlx8tgPo4O2pqzJZicHSfurHOicoLv1CdW2gOV3PaY40Z8QzibBslgtd895s2uEdQPfbOPy1fsJoSNGU/640?wx_fmt=png)

## 5、连接器位置和引脚排列

从接线图中通常可以点击查看特定部件的连接器引脚图。有时这些信息可以在专门的连接器列表中找到。如果ECU有多个连接器，有时会有一张图显示每个连接器的位置。否则我们需要根据引脚数量、线色或连接器形状来匹配正确的连接器。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaB4DpbC78y21ibs3fAdyuxM36m5icjfyiaZO2xJwgsFficMkWlIP0KAAcDWlSDWIVuyRwiaAN34YHibnwiadvU5IpZH3ia8bKnW08cEicVo/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaB4DpbC78y21ibs3fAdyuxM36m5icjfyiaZO2xJwgsFficMkWlIP0KAAcDWlSDWIVuyRwiaAN34YHibnwiadvU5IpZH3ia8bKnW08cEicVo/640?wx_fmt=png)

## 6、组件位置

在汽车中查找特定部件时，一张显示其位置的示意图会很有帮助，在寻找特定连接器或ECU时尤其有用。有时这些示意图会以实际部件照片的形式提供。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaCTEia0biabfJFJltbO1bg3meJibPuKCgtpxBryEfQMTLol1hsBkz2EenEJ1gtDibDjjLp4NTQywy4jrhtS8icOZ7jRlITKIvADZ1yo/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaAbpo9GgoZTMncyplBkuNdSm9KruoamyL9va4OjT1ulqTHkjZTREeNj8RRiacZIWZbDcSBql85Y2Csxvyv3ReP76GAlkkxVJyWw/640?wx_fmt=png)

# 二、本地互联网络（LIN）

LIN总线是一种单线总线，用于ECU之间的低速通信。为CAN总线的低成本替代方案，用于非关键系统，例如车门锁、后视镜、雨刮器和空调控制系统。

LIN被标准化ISO 17987。

## 1、物理层

LIN总线由一个指挥节点和最多16个响应节点组成。指挥节点负责调度总线上的通信。响应节点只能在指挥节点请求时发送数据。总线最长可达40米，最大运行速度为19.2kbit/s(LIN2.0为20kbit/s)，它支持每帧最多8字节的数据。

该物理规范基于ISO 9141（K线），仅需一根导线。总线通过上拉电阻拉高至12V。将总线拉低发送显性位，释放总线电压发送隐性位。总线处于高电平时处于空闲状态。

简而言之就是如果这根线通过电阻被拉到12V高电平，此时处于空闲或隐性状态，发送数据时把线拉低到0V这叫显性位。发送完松开，线回到12V。

## 2、LIN框架

LIN事务来自指挥节点的帧头开始，帧头包含以下内容。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaC3ODtNuAb1EW1uc5o0AyLksPZQ8tWQLDkDlvJPOKjmmDmuJopj86nibgbMPfeRWFkhibILybfqYBGywA1Ix0Uvcxep4vfPU2ZSo/640?wx_fmt=png)

SBF（起始位域）：用于指示帧的开始。它包含13个或更多显性位，后跟一个隐性位，即同步分隔符。

同步：同步字段用于同步指挥节点和其他节点之间的时钟。他由一个值为字节组成0x55，其中包含交替的显性位和隐性位。

PID（受保护标识符）：包含6位帧标识符和两个奇偶校验位（基于该ID计算得出）。帧标识符由响应方用于确定是否响应该帧。

响应方随后发送响应。指挥官也可以恢复自己的报文头，从而向一个或多个响应方发送数据。

数据：数据字段包含帧和实际有效载荷。2、4、8字节长。

校验和：包含一个8位校验和。LIN 1.X仅基于数据字节计算；LIN 2.X，校验和中还包含了标识符。

注：由于这是机翻，所以看起来有点晦涩，这里用我自己的话解释。

SBF，首先指挥节点拉很长一段时间低电平，通知各个响应节点我要开始发送数据

同步信号，发送一个固定0x55，也就是01010101的交替信号，让所有响应节点对齐一下自己的时钟，确保大家节奏一致

身份号（PID），指挥节点说出这次要问谁、问什么并带有校验位防止出错

数据，被点名的响应节点回答，最多说出8字节内容

校验和，最后再发送一个校验字节，检查刚才说的信息有无错误。

## 3、框架类型

LIN定义了以下几种帧类型：

无条件框架：最常见的框架类型，其中指挥官向响应者请求数据。指挥官发起事务，单个响应者回复数据。

事件触发帧：用于接收不经常变化的数据。使用事件触发帧可以节省带宽，无需逐个轮询每个响应节点。指挥方会询问所有响应节点是否有新数据要发送。然后所有响应节点可能会同时响应数据，但大多数情况下只有一个节点会响应。当多个节点同时响应时，指挥方会检测到冲突，并使用无条件帧逐个询问每个节点。

零星帧：有时指挥官需要向响应者发送数据。这种情况下，指挥官发起事务，但随后数据回复到自己的头部。

诊断帧：LIN2.2A规范保留ID 60和61用于诊断和配置目的，例如动态分配节点地址或发出睡眠命令。

注：

普通问答（无条件框架）：指挥节点点名一个响应节点，响应节点必须回答。

有事才问（事件触发帧）：指挥节点询问是否有新消息，有新消息的响应节点才回答

自问自答（零星帧）：指挥节点既提问又自己回答，用于给响应节点发指令

诊断专用（诊断帧）：专门用作配置、休眠、分配地址等特殊操作

# 三、控制器局域网CAN

CAN总线，ISO 11898，是一种广泛应用于现代车辆的通信协议。用于连接各种ECU。

## 1、物理层

CAN由双绞线CAN-H、CAN-L组成。特性阻抗为120Ω，它支持最大1Mbit/s的数据速率，最大传输距离为40米，两个或多个节点可以连接到同一物理总线上，并且任何一个节点都可以随时发起传输。

显性状态（逻辑0），空闲状态（逻辑1）。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaCgasibVibuUBMs7GsBnCs5jt682UJgY7OqamAJicDAsMnhBQQf3ndTxsnibDkKPGfyWxhnNpDPw8hGEk6HibtS4OLEY9x3FuXPicBCA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBMRFS5xib5ibcDW0mySCE01BXWqr2P0MKE4icic6sfnjLKEjrr52UVvEfiadVSPuKo7VyxmibmZXN38QGviaib4dCTrDOCNGib1I8I2icvk/640?wx_fmt=png)

## 2、CAN框架

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaCvBz14KzqNWyLDX0HfBttGRibxiaIeAZFfwPZdvjaI77dyriaSuaplo24dROjt9qtAJh3qPlJRxbUyL06yM5VXxqfgicic2VFuW17o/640?wx_fmt=png)

就是这样的一个架构。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaC11jAzFBSZXiaCVl32XUhC5AUMwhFkrmIO2VGGKRDQjzTtcBwSfYATUoia2sMBBHjvDrZtkDX1xRDEC1rTf65bkcoUrxsW5ljvI/640?wx_fmt=png)

简单过一遍，图中第二部分绿色的是仲裁ID，11位标识符，ID越小，这个报文优先级越高。然后1字节的DATA。

这里为了节省时间，可参考我其他文章，有专门聊过结构，这里介绍一下比较重要的内容。

这里介绍一下比较关键的信息。

CAN是什么？和LIN的区别？

首先CAN是控制器局域网，LIN是本地互联网络。

CAN是多主，每个节点都可发送信息，LIN是主从结构，只有指挥节点才能发送通信。

其次CAN是双绞线且传输速度更快，LIN单根线。

CAN的速度更快、实时性更好，适合动力、地盘刹车等关键系统，LIN成本低、速度慢适合车身小模块。

CAN有完善的错误处理和仲裁机制，LIN更为简单。

CAN是多主，如何解决总线冲突？

通过仲裁机制解决。仲裁ID越小，优先级越高。

其实这个我们在前面了解CAN的时候会反应到的，LIN是没有解决冲突的机制。

标准帧和拓展帧区别？

区别在于仲裁ID长度。

标准帧使用11位ID

拓展帧使用29位ID

且拓展帧支持更多的报文ID，适合网络节点较多的车型。

关于安全机制

传统CAN协议几乎没有安全机制，无加密、无身份认证、无完整性校验，CRC也只是防传输错误无法防止恶意篡改。

所以我们能接触到物理总线，就能监听、注入、重放报文。

总结起来，常见的攻击方式就是嗅探、注入、重放、总线关闭攻击（故意发送错误帧，让ECU报错使总线进入关闭状态）、DOS。

关于CAN FD和传统CAN区别？

CAN FD（Flexible Data-rate）是CAN升级版

速度更快、数据量更大，一帧可传输64字节数据，传统CAN只有8字节。

## 3、关于错误状态机制（CAN DOS攻击核心）

每个ECU都有一个错误计数器

<128正常可通信

>127只能被动报错，不影响其他ECU

>255直接断开总线，不接收

对应的是下图状态

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaD4iaGs9Md5LZfG3DNicichrcJmshoVkgYymuuC8puLMXGicauapy9vJxCFMWZU9It72cfdM5C3O4tk2bboFa8tZbTofuP5XibHf38E/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDIM06l1yKtxBPEsXFPJjMOonoyD3bEJEicSSYXef8XW2aQm3n3UuBFrgHQlrzubibqhGibn7vw3dDpfFPx2zPRoRGuziaukADLP8M/640?wx_fmt=png)

## 4、关于实际攻击

中间人（MITM）

由于CAN总线通信没有实时性要求，因此实施中间人攻击非常容易。攻击者只需接收总结上的浏览，然后将消息转发给目标接收者即可。

DOS攻击

过载攻击

发送过载帧，将导致总线上的所有节点停止发送消息，而不会增加错误计数器。

CAN优先级反转

ECU有个待发队列。如果程序员把它写成先进先出（FIFO）就会出现，一条低优先级报文进入队列，后面来了一条高优先级报文如刹车，因FIFO低优先级先发，高优先级等待，总线忙的状态，导致刹车报文被卡住。本身为ECU的设计缺陷。

雅努斯攻击

一条报文，发给两个节点，他们看到的内容不同。

核心用途就是如果车辆网关或安全模块部署了IDS，他会检查CAN报文的载荷内容。攻击本意是让IDS看到的载荷是干净的，但目标ECU收到的载荷是恶意的。

DLC>8字节

标准CAN数据包为8字节，然后DLC数据大小为4位，因此他最高可容纳高达15的值，如果接收端没有正确检查DLC数据，将其作用memcpy等函数，可能造成缓冲区溢出。可以理解为DLC溢出吧。

计数器

如果CAN消息的有效载荷中有空间，通常会包含一个计数器。这在ECU固件中很有用，可以检测消息是否仍在更新以及是否丢失了任何消息。

校验和

CAN报文里有校验和，很多ECU不检查，如果伪造或篡改报文他们依旧执行。

# 四、安全机载通信（SecOC）

是AUTOSAR标准中用来解决CAN总线安全问题的方案。传统CAN报文没有身份标识符，谁都可以发送，ECU收到就执行。SecOC就是在报文中添加认证机制。

就是加了MAC认证、计数器，防伪造、防篡改、防重放。

# 五、FlexRay

FlexRay是比CAN更高级的车载总线，专门给底盘、线控、动力系统这种对实时性和可靠性要求极高的地方使用。

和CAN比，他速度更快，10Mbit/s，是CAN（500k）的20倍。确定性：通信按固定时间周期走，不像CAN靠仲裁，延迟可以精确预测。容错：支持双通道冗余，一条线断了另一条顶上。

# 六、ISO 15765-2（ISO-TP）

CAN总线有效载荷仅限于8字节。与ECU的诊断数据交换通常需要发送超过8字节的数据。ISO-TP一种通过CAN总线发送更大数据量的标准。

## 1、消息结构

每个ISO-TP消息都由一个头部和一个有效载荷组成。如果有效载荷小于等于7字节，则数据可以放入单个CAN帧中。如果有效载荷较大，则需要将其拆分为多个帧。帧的第一个半字节指定消息类型，单帧、首帧、连续帧、流帧。

如果CAN帧长度小于8字节，可以进行填充或使用更短的DLC发送。ISO规范使用进行填充0xCC，但实际更常见的使用0xAA或0x55。

## 2、单帧

如果有效载荷小于或等于7字节，则可以放入单个CAN帧中。第一个半字节设置为0，表示单帧。下半个字节是有效载荷长度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaA2Chc98cN9eR4RpVvAiaOEPUPbLypWK7IKkJ3ZKiaScXXvdsiaVwgNWFtpZibOJSReDouqOVVqMvoibNVGJdMicD5v3cicRSF8iahibiacM/640?wx_fmt=png)

这里就像我们使用zlg或者Pcan发送的报文一样，前面的就是帧类型。

## 3、第一帧和连续帧

如果有效载荷太大，无法放入单个帧中，需要进行拆分。第一个消息的第一个半字节设置为1，表示第一帧，后面跟着12位表示有效载荷的长度，以及6字节的有效载荷。接收方随后会回复一个流控制消息。该流控制消息会告诉发送方是否可以继续发送、帧之间需要等待多久。

经过流量控制后，发送方可以使用连续帧发送剩余有效载荷。连续帧以2开头，后门跟一个4位索引，以确保消息按正确的顺序到达。当索引达到15时，他会回到0。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaBroaJGbnQnbnmNAYCFDSNt0k4tic924Tcx0RMGECz4ek0AG7uPmu5oickq3UNCd18uuauIZmxSPUFokVjPfFJflsNOibthWL55uw/640?wx_fmt=png)

## 4、流量控制

流量控制消息用于控制后续数据的发送速率。流量控制消息的第一个半字节设置为3。下一个半字节表示流量控制的状态。状态可以是（继续0）、（等待1）、（溢出2）。

继续消息的一部分是块大小和分离时间。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaATRBFkmJQjbvOkvEurmhCuUnornnia13O7ibmltFiap9sldZfSczVyCPTSgdGPCEGJcANxeaQyMdYFxI7AQK0jJboiaeAick4KfKOI/640?wx_fmt=png)

等待，当发送方...