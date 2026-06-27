---
title: AUTOSAR CanNm 详解：整车 CAN 网络同步唤醒与休眠实现原理
url: https://mp.weixin.qq.com/s/hhtWRln7hquBNo3WKiUjUg
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:48:07.299160
---

# AUTOSAR CanNm 详解：整车 CAN 网络同步唤醒与休眠实现原理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBjBdzjSXXcAXeXlhtwr6RBehkWUKhiaOjzazmkBjakrVpY6NpY8TkpItuY76BnYk7nV19HrUUkBCPAqUkp5WVEX12b9OLmdNbA/0?wx_fmt=jpeg)

# AUTOSAR CanNm 详解：整车 CAN 网络同步唤醒与休眠实现原理

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

**01**

**网络管理目的**

网络管理的目的是使车辆网络中的 ECU 节点有序的睡眠和唤醒。 在没有通信需求的时候睡眠，在需要通信的时候唤醒， 可以节约汽车电池的电量。

CAN Network Management(CanNm)是一种独立于硬件的协议实现的软件模块， 只能在 CAN 网络上使用， 主要功能是协调网络正常运行和总线睡眠模式之间的转换。 CanNm 提供了网络管理接口（NmIf） 和CAN 接口（CanIf） 模块间的适配。

**02**

**CanNM与其他模块之间关系**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAqLC3ibnbVwu7drWLUkqJbQFXw38FWx80GLv8gvjDARP7mmLSwPwmyciazb2UYIAibmEfXhZdfhIYQhLsPR8X7YCVCUic5oiaPZAFw/640?wx_fmt=png&from=appmsg)

**03**

**主动唤醒和被动唤醒**

网络管理唤醒分为主动唤醒和被动唤醒。（BMS的休眠唤醒包括CAN唤醒，CAN唤醒又叫网络管理唤醒）

主动唤醒和被动唤醒的区分： 简单来说，除了收到其他节点发送的网络唤醒报文是被动唤醒外，其他都是主动唤醒（如：KL15、菊花链、RTC定时唤醒等）。

主动唤醒请求： 来自模块内部对网络的请求，并通过发送NM PDU尝试唤醒其他ECU。主动唤醒又叫做本地唤醒，和硬线相关的唤醒方式一般称为本地唤醒源。如：KL15硬线，硬线传感器信号（如：脚踢门、后备箱打开）主动唤醒节点（BMS即是一个节点）的网络管理报文必须先于应用报文发送。

被动唤醒请求： 来自总线上其他节点对该节点（例：BMS）的网络请求。被动唤醒的节点，发送的网络管理 PDU 和应用报文没有顺序要求（实际以项目 要求为准）。被动唤醒又叫做远程唤醒，简单来说就是和总线信号相关的唤醒方式。比如收到网络管理报文或者指定诊断报文（以项目要求为准，部分项目不会使用诊断报文作为唤醒源），或者包含KL15信号的应用报文（有些节点没有KL15硬线，而是网关转发包含KL15信号的应用报文唤醒）。

**04**

**状态管理**

AUTOSAR CanNm 包含三种模式，其中 Network Mode包括三种子状态：

网络模式（Network Mode）

* 重复报文状态（Repeat Message State）
* 常规运行状态（Normal Operation State）
* 准备睡眠状态（Ready Sleep State）

准备总线睡眠模式（Prepare Bus-Sleep Mode）

总线睡眠模式（Bus-Sleep Mode）

**1. 总线睡眠模式（Bus-Sleep Mode）**

总线睡眠模式(BusSleepMode)的作用，是当网络上没有通信需求的时候，减少节点对蓄电池电量的消耗。 节点进入总线睡眠模式(BusSleepMode)后，对蓄电池电量的消耗下降到适当的程度。节点保留唤醒机制，等待被唤醒。

原则上，处于总线睡眠模式(BusSleepMode)的节点不接收应用报文并且不应给出ACK应答。如果此时节点数据链路层被唤醒且给出了ACK应答，需要在最短时间内重新进入低功耗模式。

**2. 准备总线睡眠模式（Prepare Bus-Sleep Mode）**

准备总线睡眠模式(PrepareBusSleepMode)的作用，是保证在进入总线睡眠前，节点有足够的时间停止其网络活动。在准备总线睡眠模式（PrepareBusSleepMode）下，总线活动减少（如：存在于发送缓存中的报文被发送，以清空发送缓存），最终总线将不再有活动（即没有任何报文被发送）。

节点进入准备总线睡眠模式(PrepareBusSleepMode)后，将立即开启T\_WAIT\_BUS\_SLEEP定时器。在该定时器溢出后，该节点将离开准备总线睡眠模式(PrepareBusSleepMode)，进入总线睡眠模式(BusSleepMode)。

当处于准备总线睡眠模式(BusSleepMode) 的节点接收到网络管理报文时 ， 将向网络模式(NetworkMode)转换；默认情况下，节点进入网络模式(NetworkMode)中的重复报文状态（RepeatMessageState）。

当处于准备总线睡眠模式(PrepareBusSleepMode)的节点对网络通信有需求时，将向网络模式(NetworkMode)转换；默认情况下，节点进入网络模式(NetworkMode)的重复报文状态(RepeatMessageState)。

**3. 网络模式（Network Mode）**

当节点从总线睡眠模式(BusSleepMode)或准备总线睡眠模式(PrepareBusSleepMode)进入网络模式(NetworkMode)时，在默认情况下，需进入重复报文状态(RepeatMessageState)。

节点进入网络模式(NetworkMode)后，需开启T\_NM\_TIMEOUT定时器；

节点处于网络模式 (NetworkMode)，成功接收或成功发送一帧网络管理报文（NM PDU）后，需重启T\_NM\_TIMEOUT定时器；

**3.1 重复报文状态(RepeatMessageState)**

无论其睡眠条件是否满足，重复报文状态(RepeatMessageState)都可以使节点保持一段时间的活跃状态。该状态可以被用来监测在线节点，并且告诉其它节点我上线了，可以正常通信了。

当节点进入重复报文状态(RepeatMessageState)后，需要开始（或重新开始）发送网络管理报文。

节点处于重复报文状态(RepeatMessageState)，T\_NM\_TIMEOUT定时器超时溢出时，需要重启T\_NM\_TIMEOUT定时器。

节点接收到本地唤醒源后，进入快发重复报文状态（InnmediateTransmitState）；

节点接收到被动唤醒源后，进入正常重复报文状态（NormalTransmitState）。

节点在进入重复报文状态 (RepeatMessageState)后，需要保持一段时间 ，这段时间由参数T\_REPEAT\_MESSAGE 决定；T\_REPEAT\_MESSAGE 超时后，节点状态需进入常规运行状态(NormalOperationState)或准备睡眠状态(ReadySleepState)。 T\_REPEAT\_MESSAGE需保证网络上其它的节点都可以被网络管理报文唤醒。

节点离开重复报文状态(RepeatMessageState)后，若对网络通信有需求，应进入常规运行状态(NormalOperationState)。

节点离开重复报文状态(RepeatMessageState)后，若对网络通信无需求，应进入准备睡眠状态(ReadySleepState)。

节点离开重复报文状态(RepeatMessageState)后，需将重复报文请求标志位（RepeatMessageRequestBit）清零。

**3.2 常规运行状态(NormalOperationState)**

常规运行状态(NormalOperationState)用于保证只要对网络通信有需求，任何一个网络管理节点都可以保持网络处于唤醒状态。

当节点由重复报文状态(RepeatMessageState)或准备睡眠状态(ReadySleepState)进入常规运行状态(NormalOperationState)时，需按照T\_NM\_MessageCycle的周期发送网络管理报文。

当节点处于常规运行状态(NormalOperationState)，而定时器T\_NM\_TIMEOUT溢出时，需要重启定时器。

当节点处于常规运行状态(NormalOperationState)，而本地睡眠条件满足时，需进入准备睡眠状态(ReadySleepState)。

当节点处于常规运行状态(NormalOperationState)，而接收到重复报文请求标志位（RepeatMessageRequestBit）置位的网络管理报文时，需进入重复报文状态(RepeatMessageState)。

当节点处于常规运行状态(NormalOperationState)，而RepeatMessageRequest()函数被调用时，需进入重复报文状态(RepeatMessageState)，并将报文中重复报文请求标志位（RepeatMessageRequestBit）置位，同时启用快速发送机制（autosar中未明确此时是否需要启用快发机制）。

**3.3 准备睡眠状态(ReadySleepState)**

当节点从重复报文状态(RepeatMessageState)或常规运行状态(NormalOperationState)进入准备睡眠状态(ReadySleepState)后，需停止发送网络管理报文。

当节点处于准备睡眠状态(ReadySleepState)，定时器T\_NM\_TIMEOUT溢出后，需进入准备总线睡眠模式(PrepareBusSleepMode)。

当节点处于准备睡眠状态(ReadySleepState)，但因发生本地唤醒事件，睡眠条件不再满足时，需进入常规运行状态(NormalOperationState)。

当节点处于准备睡眠状态(ReadySleepState)，接收到重复报文请求标志位（RepeatMessageRequestBit）置位的网络管理报文后，需进入重复报文状态(RepeatMessageState)。

当节点处于准备睡眠状态(ReadySleepState)，RepeatMessageRequest()函数被调用时，需进入重复报文状态(RepeatMessageState)，并将网络管理报文中的重复报文请求标志位（RepeatMessageRequest）置位，同时启用快速发送机制。（autosar中未明确此时是否需要启用快发机制）

**05**

**网络管理定时参数**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCHia4iaNLm9RECF5PhLYL0ZlFlJRnzazibYxODLD89LWR2icoqjWdWgnfkMYHRQ6IOAQBeBFnuyFpsIBwdNl90bVB7EGgiaEwXALMU/640?wx_fmt=png&from=appmsg)

**06**

**状态切换整体框图**

下图显示了与API规范相关的UML状态图。模式更改相关转换用绿色表示，错误处理相关转换用红色表示，可选节点检测相关转换用蓝色表示。此外，还假定启用了总线负载减少功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDNKgyp00KKorMtPH9XwvtCD9LAc8qS85JwCBkibvqa7et49GHavu0lxRKZaibXqxQXLGRmmw1la9UZANGnibkOFrFdQ8Zd4ic6QDY/640?wx_fmt=png&from=appmsg)

状态切换详述：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaC54wQjGtUeXulZ9LKkdcbXZXgVkKuiaksdgPWCqWHxbL3giclaP2Nd8FV1CjMSx627EdUvjSTnB7AmV0qOHLoyUONoWnf1s15h8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCKx7p5dhp5tvGA19ErmLwkxE4icVXicySzv8xRwI8vIpuokibV9APNSrobFsoMDnPE3gmT1caSBl9UicSlauua0QNukfeqPsuvrwI/640?wx_fmt=png&from=appmsg)

当ECU处于不同的运行模式时，可以发送和接收的CAN报文的类型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaB4SLicRLG1eaaRzeGFUvE8acDZDibqRnAzBeiaqgHNrm7ofenMPmspcPqxfCyJaaWbLRmKzKzRH6INia8aTTsKbwzvQwuuH1QmZ4k/640?wx_fmt=png&from=appmsg)

**07**

**网络管理报文（NM PDU）**

每一个AUTOASAR网络管理节点都会被分配一个唯一的网络管理报文ID。

NM PDU数据结构如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCOGHq2D9Sw1dyY11nINcv0FKmrlUMaaXBQTsUaDgM0Jw32icYJPGibpyib4fj449icOgpG8NU7uCDebHSpicE4y7WibsSXAntK117Mo/640?wx_fmt=png&from=appmsg)

**源节点地址（SourceNodeIdentifier**）

每一个参与网络管理的节点都会被分配一个唯一的标识符（NODE\_ID），存放于网络管理报文的Byte0（SourceNodeIdentifier）中。

Byte 0表示当前节点的Source ID，比如如何当前节点发送的NM报文ID为0x514，那么该Source ID就为0x14；

**控制比特向量（ControlBitVector）**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDL8sxhlOsGpunMibNBNiaVicuw9WOqMHmibsU7SnVcfNVaiaY5FqVWJ3rI5bKtvKItLD8ST6J0Bt1rmMuwWQLZTmuPclQ4iccJ6tOvA/640?wx_fmt=png&from=appmsg)

Bit0：重复报文请求标志位(RepeatMessageRequestBit)，信号值描述为：

* 0x0：该报文发送节点未请求其他节点进入重复报文状态
* 0x1：该报文发送节点请求其他节点进入重复报文状态

Bit3：NM协调器休眠位

* 主协调器未请求启动同步关机
* 主协调器请求启动同步关机

Bit4：主动唤醒网络标志位(ActiveWakeupBit)，信号值描述为：

* 0x0：该报文发送节点未主动唤醒网络（被其它节点唤醒）
* 0x1：该报文发送节点主动唤醒网络重复报文请求标志位(RepeatMessageRequestBit)的默认值为 0。

当节点由于 RepeatMessageRequest() 函数被调用，从常规运行状态(NormalOperationState)或准备睡眠状态(ReadySleepState)进入重复报文状态(RepeatMessageState)时，需将其发送的网络管理报文中的重复报文请求标志位置 1，直到其离开重复报文状态。

当节点由于本地睡眠条件不再满足（NetworkRequest），从总线睡眠模式(BusSleepMode)或准备总线睡眠模式(PrepareBusSleepMode)进入重复报文状态(RepeatMessageState)时，需将主动唤醒网络标志位(ActiveWakeupBit)置 1，直到其进入准备睡眠状态(ReadySleepState)。

当节点由于接收到网络管理报文而进入重复报文状态(RepeatMessageState)，需将其发送的网络管理报文中的主动唤醒网络标志位(ActiveWakeupBit)置 0。控制比特向量中未使用的位须 0。

Bit6：PN功能位

* 0x0：网络管理不使用PN功能。
* 0x1：网络管理报文中包含PNC信息。如果项目中，网络管理要求使用PN功能，发送的网络管理报文中，有PNC请求时，需要先置位PNI。接收节点会根据PNI情况决定网络管理的处理流程。

CanNm\_RepeatMessageRequest函数可以设置RMR位(RepeatMessageRequestBit)。

调用CanNm\_RepeatMessageRequest函数，需要在Normal Operation State或Ready Sleep State状态下，其他节点在收到RMR位后，不需要设置RMR位。

发送节点： 主动调用CanNm\_RepeatMessageRequest，发送时Repeat Message Request 置位

接收节点: 接收Repeat Message Request 位，进入Repeat Message State状态， 不需要置Repeat Message Request 位。

**用户数据（Userdata）**

在网络管理报文中有6个字节的用户数据（Userdata0~5），可以被应用层读取和写入，用于传输用户定义信息。

**08**

**被动唤醒和主动唤醒时的状态切换**

被动唤醒：

处于休眠状态的主板，在收到NM报文唤醒时，会从 Bus-Sleep 模式切换到Network 模式的Repeat state，进行慢发NM报文，以 CanNmMsgCycleTime（例：200ms） 为周期，在Repeat Message Timer（例：1000ms）定时器到时时...