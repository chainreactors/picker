---
title: 基于CAN总线的Autosar网络管理简述
url: https://mp.weixin.qq.com/s/2nO91ennEwWe0oNQt6wSjA
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:40:22.101783
---

# 基于CAN总线的Autosar网络管理简述

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAHVTs4MSZKRhaR2dDWAHdEnO3lOYCKJeqdv0TZdDHDusYR8IWMpHrOnmmdPYtgiaiaribWMFaQ35SaZsWISuK6l6qNhY9LSHiar2E/0?wx_fmt=jpeg)

# 基于CAN总线的Autosar网络管理简述

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

**01**

**AUTOSAR软件架构概述**

AUTOSAR定义的是一种自上而且的近乎分层结构的软件架构。可以最大化的在微控制器上抽象为三个软件层级：应用层（Application），运行环境层（Runtime Environment）和基础软件层（Basic Software）

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCVkUVdrdSZiaThZaxn9rq5xJXAhUaibibO06OslDibxEg83ibx4BKxtaDgpAYD25qualdicR3hFVAzTXzMdFWcbuLJeULmzxH8B2VUs/640?wx_fmt=jpeg&from=appmsg)

**1.1基础软件层**

AUTOSAR的基础软件层（BSW）又可分为服务层（Services Layer）、ECU抽象层、微控制器抽象层和复杂驱动层（Complex Drivers Layer）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaA2ibsH8uwtfBibnpxX0iccB02xRshHmrdswdexe5aXDBlGfInleaodZspvTHul0UedpWCDyCdAsvWTJWpBnAPvTkmXonZw7icqBnM/640?wx_fmt=jpeg&from=appmsg)

微控制器抽象层在BSW的最底层，它包含微控制的驱动程序；

ECU抽象层接口微控制器层的，它包含外部设备的驱动。该层提供API来访问外部设备。

（OSI分层结构中的CAN数据链路层对应AUTOSAR分层架构的微控制器抽象层和ECU抽象层）

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAN9cOhneOibCEkiaD40P0ddBXk75yEIXldeQmshJrpgEgULMXibeWSVmu4yK76kp0aNJCzlMOsz97ibCbicxh2yUZTjOib2QOrHH98Y/640?wx_fmt=png&from=appmsg)

引自：《AUTOSAR\_SWS\_\_COM》第2.1节

复杂驱动层可集成一些特定的功能、驱动或外设。AUTOSAR并未对改成进行详细规定。

服务层是BSW的最高层，包含以下功能：

（1）提供车辆网络通信和管理服务

（2）内存服务

（3）诊断服务

（4）ECU状态管理和模式管理

（5）操作系统的功能

（6）诊断服务（包括UDS通信、故障存储和错误处理等）

基础软件层按照提供的功能又可以分为几个不同的服务模块，这和上面的介绍只是分法不同。

大致可分为：

（1）输入\输出服务

（2）存储服务

（3）通信服务（本文介绍的内容均包含在这个模块）

**1.2 CAN通信协议栈的分层结构**

前面说到了BSW可以分为不同的服务模块，其中包含有通信服务，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCOVoPCsJDkFwbMzmBAg93Db1rrtIxtmq36F8qwGIrWNV3eDcyiaeqah2eNRHmJCrBLVP3X9qQjRNlXU24SuW5ZVfxg7O90Iibuc/640?wx_fmt=jpeg&from=appmsg)

本文要介绍的内容即为CAN NM模块，即基于CAN总线的AUTOSAR网络管理。

**02**

**CAN NM**

**2.1网络管理报文的格式**

做了AUTOSAR网络管理的ECU，原则上需要定义一条特定的报文作为网络管理报文，网络管理报文的类型应为Nosendtype。也许有人疑问，正常工作时网络管理报文都是按照特定的周期来发送的，为什么类型不是周期报文？这是因为在准备睡眠状态中是不发送网络管理报文的，在ECU被主动唤醒时还会以特定的周期快发，所以报文类型不能是周期报文。

刚才说到原则上是需要定义网络管理报文的，但是国内的有个别非常个性的主机厂，他们定义的整车中某个节点需要支持网络管理，但是不需要发送网络管理报文。原则上这是不符合AUTOSAR要求的，但如果该节点没有主动唤醒网络的需求，这种做法也是可以的。

**2.1.1网络管理报文的ID**

NM报文的ID一般定义为：基础ID+源地址。AUTOSAR并未指定网络管理报文的ID范围，这是OEM自行选择的，一般0x3xx、0x4xx、0x5xx和0x6xx的都有使用。

以0x53f为例，0x53f=0x500+0x3f，其中0x500即为基础ID，0x3f为源地址。

**2.1.2网络管理报文的数据场格式**

一般网络管理报文的DLC为8，AUTOSAR举例的8个字节的的网络管理报文格式如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAzBHlQySYXtGiahU2zewRle8ltjNHn9mluyJh5eOxhlFhXM9JiaJmONckXOCwMk8WliajyT2bKUE1lFpMpmyQ1KdoNOzyj22dVSw/640?wx_fmt=jpeg&from=appmsg)

注：图片来源《AUTOSAR\_SWS\_CANNetworkManagement》

（1）举例中的第一个字节为节点的源地址，源地址的用处可在刚被唤醒时根据源地址判定整个网段中有哪些节点在线。（不过现在很少有见到用的）

通过CanNmPduNidPosition设为off，可以不适用源地址字节。

（2）举例中的第二个字节为控制位向量，它的格式如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAbH9xeLPFwGd4zopIW4jhOIlkib1T1uWwYyibg9BXdhVKrq6MfAbc7544f0ibSR0J99xt33pzxRqRDhupiczbGsSM5wsSxn5ZHn4c/640?wx_fmt=jpeg&from=appmsg)

注：图片来源《AUTOSAR\_SWS\_CANNetworkManagement》

Bit0:重复报文请求位，当某个节点发的NM报文中的此位置1时，所有接收到该NM报文的节点均要返回Repeat Message State。

实际在使用中并未见过有这种需求的工况或场景，如有大神了解，请帮忙补充。

Bit3:协调睡眠准备位，当某个节点发出的NM报文中的此位置1时，意味着该控制器为多个网段的主协调器，且请求同步进入Shutdown。

Bit4:主动唤醒位，该位的作用是标示自身是被主动唤醒的还是被动唤醒的，当自身是被主动唤醒的则置1，被动唤醒则置0。这里的主动和被动既是外部条件，也是自身有无需求。主动唤醒，意味着ECU自身的本地唤醒事件被触发（本地唤醒事件只有当自身需要请求网络通信时才会被触发），自身有网络通信的需求。例如对于车身控制器BCM，车门状态的改变是它的本地唤醒条件，当外界环境（人）改变车门状态时，BCM即被主动唤醒，开发发送NM报文唤醒其它节点，此时该位要置1。被动唤醒是指自身的本地唤醒条件没有被触发，但是其它节点有和自己通信的需求，在收到其它节点的网络管理报文后被唤醒，此时该位置0。

需要注意，在一个唤醒-预睡眠周期内，该位不会重置。当ECU进入预睡眠状态时会重置该位。支持该位的前提是CanNmActiveWakeupBitEnabled=ture。

Bit6:局部网络信息位（PNI），该位置1标示ECU自身发送的NM报文中包含PNI。只有在整车网络中使用了局部网络管理时才会用到该位。

现在使用CAN总线协议为主干网的车型上，网段的数量约为4-6个，一般多为整车使用AUTOSAR网络管理，不做局部网络管理。但是实际在整车上根据不同的功能需求，可以将整多个网段定义为不同的局部网络管理，这样能够更进一步的节省能耗（貌似也节省不了多少），通信效率更高。

关于源地址和控制位向量，需要注意：

* 不是必须的，NM报文中可以不使用这两个位。

2.如果使用，推荐在byte(0)和byte(1)这两个字节。可以源地址在byte(1)，CVB在byte(0)。它们的位置可以通过CanNmPduNidPosition配置

（3）用户自定义数据User Data

在部分字节OEM可根据自身需求定义。一般可定义唤醒原因、维持唤醒原因、NM状态、PNC信息等内容。

网络管理报文很重要的一个作用是帮助排差整车异常唤醒或不休眠（延时休眠）的问题，如果User Data使用得当，非常有利于睡眠唤醒问题的排查。

**2.1.3 网络管理报文相关的测试**

首先要测试NM报文的格式是否符合OEM的定义，源地址和ID是否对应；

其次需要测试CVB每一位的置位情况是否正确，例如主要唤醒时（例如KL15 on）Active wakeup bit是否置1；

第三需要测试CVB每一位的初始化或重置是否正确。控制器在上电初始化时要将CVB各位置0.

**2.2 AUTOSAR网络管理的状态**

AUTOSAR规定有三种状态：睡眠模式（bus sleep mode）、预睡眠模式（Perpare Bus Sleep mode）和网络模式（Network mode）。

**2.2.1睡眠模式(Bus-Sleep mode)**

ECU上30电后要先进行初始化,初始化完成后默认进入睡眠模式。在初始化过程中ECU不能向总线发送报文甚至显性电平。在睡眠模式中控制器既不接收也不发送报文，但激活了唤醒源的监测，即如果此时总线上有网络管理报文在发送（发送成功了或NoAckError后自动重发），CAN NM模块需要通知应用层接收到了唤醒源，并由应用层决定是否被唤醒。

睡眠模式的作用主要是降低功耗，车辆在不使用的状态下（满足休眠条件下），控制器进入睡眠模式后的工作电流非常小。

在睡眠状态中如果总线上由应用报文持续发送，控制器是否给ACK取决于所选用的收发器。例如使用TJA 1041，控制器在睡眠状态中收到应用报文后给收发器上电，从而给出ACK应答。但应用报文并不是控制器的唤醒源，应答一段时间后就又关闭首发器。

如果使用TJA1043，则在睡眠状态中接收到应用报文会持续的给出ACK。

现在有些收发器在自身就带有屏蔽寄存器（TJA1042T\1043T\1145），可以自行判断收到的信号是否为唤醒源，进而自己觉得是否需要给出ACK应答。

需要注意，控制器在未上30电时的状态不属于睡眠状态。不同的控制器在上30电后的初始化时间也不相同。

**2.2.2预睡眠状态(Perpare Bus-Sleep mode)**

预睡眠状态的目的是确保网段上所有的节点有时间停止当前的网络活动（有些ECU在进入睡眠前可能还要往EEPROM中存储数据、等待一些执行机构完成动作等）在预睡眠模式控制器既不发送也不接收报文（CanNmTimeoutTime超时后如果发送缓存里面还有列队中的报文还是要发送的）。在预睡眠状态中控制器的收发器还未关闭，此时网总线持续发送应用报文，仍可关闭。

ECU进入预睡眠状态后会启动CanNmWaitBusSleepTime定时器，该定时器可配置，且不能重启，超时后ECU进入睡眠状态。

AUTOSAR规定在预睡眠状态中如果接收诊断请求，则需要进入Network mode，默认进入Repeat Message State。

**2.2.3网络状态（Network Mode）**

网络模式包含三种内在的状态：

* 重复报文状态（Repeat Message state）
* 正常工作状态（Normal Operation State ）
* 准备睡眠状态（Ready Sleep State）

ECU从睡眠状态或预睡眠状态跳转到网络状态时均要先进入重复报文状态。进入重复报文状态后，启动CanNmRepeatMessageTimer定时器。该定时器不会重启，超时后就会进入正常工作状态或准备睡眠状态。

重复报文状态的目的是定义了所有节点的NM模块stay active的最小时间。因为进入重复报文状态后都会发送自身NM报文，所有节点均网络在线，可用于当前的有哪些节点在线。在该状态ECU正常发送和接收NM报文和周期应用报文。

ECU进入重复报文状态后会发送自身NM报文，并启动NM-Timeout Timer(也可能是先接收到NM报文，同样会启动该定时器)，ECU成功发送或成功接收一帧NM报文后都会重启该定时器。

当CanNmRepeatMessageTimer超时后，如果控制器维持有本地唤醒条件（有请求网络通信的需求）则会进入正常工作状态。

我们在车辆的使用过程中，绝大部分时间均处在正常工作状态。同样的在正常工作作态，ECU成功发送或成功接收一帧NM报文就会重启NM-Timeout Timer定时器。因为该定时器可以重启，正常工作状态确保了节点可以长期维持网络唤醒，只要它对网络通信有需求。在该状态ECU正常发送和接收NM报文和应用报文。

当CanNmRepeatMessageTimer超时后，如果ECU没有本地唤醒条件被触发（没有请求网络通信的需求）则会进入准备睡眠状态。该状态是用来等待其他节点停止网络请求，同时进入预睡眠状态。在该状态中ECU正常发送应用报文，不在发送网络管理报文。正常接收网络管理报文和应用报文。当成功接收到一帧网络管理报文后会重启NM-Timeout Timer，使自身维持在准备睡眠状态。

**2.3 AUTOSAR网络管理的状态跳转**

在开始介绍这部分内容前，需要先明确几个概念。

两个状态：NetworkRequest和NetworkrRleased。这是NM模块内部（或额外的，不属于上述的三种模式）的网络管理状态，当处在NetworkRequest状态时，说明ECU有网络通信的请求，会持续发送NM报文，维持着整个网段的唤醒；当处在NetworkrRleased状态时，说明ECU没有网络通信的请求，不在发送NM报文，只发送应用报文，等待所有节点释放网络后同时进入预睡眠状态。

两类事件：本地唤醒事件和远程唤醒事件。本地唤醒事件也可称为主动唤醒事件，意味着ECU自身的本地唤醒条件被触发，需要自身请求网络，进而开发发送NM报文。例如最常见的KL15电，在车上，当KL15继电器闭合后，很多连接在KL15电的控制器被同时触发本地唤醒事件，同时请求网络，均要发出自身的NM报文。车辆在正常工作状态中，KL15继电器是闭合的，所有的有KL15电的节点均有请求网络通信的需求。远程唤醒事件，意味着ECU自身不需要主动请求网络通信，但是其它节点有通信需求，这个时候ECU只需要发送应用报文不发送NM报文，即维持在准备睡眠状态即可。即本地对应主动，远程对应被动。

综上，当触发本地唤醒条件时，会使NM模块进入NetworkRequst状态，会周期的发送NM报文；当收到远程唤醒事件时，会使NM模块进入NetworkRleased状态，重复报文状态后不在发送NM报文，进入准备睡眠状态等待所有节点都释放网络。

两个特征：低功耗和同睡（同醒，不是严格的同一时刻被唤醒）。使用网络管理的最终目的是为了降低能耗；整车所有做AUTOSAR的NM簇要同睡同醒。当总线上某个节点主动或被动唤醒，会同时唤醒其它节点（以无局部网络为例），当所有节点都释放网络后，等NM-Timeout Timer超时后同时进入预睡眠状态。

一般在多网段的车型上，网关节点都是最后一个释放网络的。网关最后释放网络，它的NM-Timeout Timer超时后所有网段的节点同时进入预睡眠状态（无局部网络管理）。网关要实现最后一个释放网络需要做一些特殊的策略，例如接收到其它节点的NM报文会作为网关的本地唤醒事件，使网关维持在正常工作状态。当其它所有节点都释放网络后，网关再延时一段事件释放网络，确保了所有节点同时NM-Timeout Timer超时。

来源：知乎@求正宇

https://zhuanlan.zhihu.com/p/71141532

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://m...