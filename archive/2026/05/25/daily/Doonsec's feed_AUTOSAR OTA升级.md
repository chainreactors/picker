---
title: AUTOSAR OTA升级
url: https://mp.weixin.qq.com/s/x1RPq0hp8lgICYyn97kH0w
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T05:59:37.301889
---

# AUTOSAR OTA升级

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDQMyUFqGVzQmjUrpibQafEH6CibAR2WicLKdf8wW3HO7RoUw2M7ibKQuCL9XPws85icaMDo6Imicg6QLQ2GfCEDQTQ8eTkDmMQoYkTI/0?wx_fmt=jpeg)

# AUTOSAR OTA升级

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

**01**

**OTA技术概念**

随着高级辅助驾驶的发展和自动驾驶的引入，汽车变得越来越智能，这些智能汽车被软件控制，装有巨量的软件程序，当出现一个软件程序问题或者更新时，如果 按照传统的解决方式 ，那都将是一项很繁重的任务。以某车上市后出现的刹车逻辑问题为例，按照传统的解决方案，那么所有该车辆先将被召回，然后派人更新软件。这样，一方面影响用户体验和满意度，另一方面又要耗费大量的人力物力来修复问题。

为了解决传统方式的痛点，使得软件更新更迅速，一种远程升级软件的技术OTA被引入到汽车行业。汽车远程升级技术OTA (Over-the-Air)是指通过移动通信网络（2G/3G/4G或Wifi）对汽车的零部件终端上固件、数据及应用进行远程管理的技术。简单来说OTA技术实现分三步：首先将更新软件上传到OTA中心，然后OTA中心无线传输更新软件到车辆端，最后车辆端自动更新软件。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS8iadHaiaGH5zxXZqEiaTPbF7rCVF8HKhkfGnK8k3syjGae4ib9oL2eBslFA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

OTA体现的优势：

* 能有效提升用户体验与满意度
* 能大范围大批量升级系统并提供升级成功率
* 能快速修复车辆故障
* 能有效降低售后维护成本

而且随着汽车行业已进入软件定义汽车的时代，对售后汽车售卖各种各样功能的新商业模式兴起，也要求汽车必须具备OTA功能。这里准确地说，OTA分为两类，一类是 固件在线升级FOTA （Firmware-Over-the-Air），是指不改变车辆原有配件的前提下，通过写入新的固件程序，使拥有联网功能的设备进行升级，包括车辆的发动机，电机，变速箱，底盘等控制系统，比如特斯拉曾通过FOTA新增过自动驾驶功能、增加过电池容量和改善过刹车距离等。另一类是 软件在线升级SOTA （Software-Over-the-Air），是在操作系统的基础上对应用程序进行升级，是指那些离用户更近的应用程序，UI界面和车载地图、人机交互界面等功能，像娱乐系统更新操作界面或主题。

**02**

**OTA技术架构**

当前智能网联汽车的OTA架构由OTA云端，OTA终端和OTA升级三部分组成，如下所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS8EebINQQ4ENwPyPzAt39Lo6GnMV8bic0xXvrsf1ic0fm209h6iafGib11SQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

这里，OTA云端为OEM专属的云端服务器平台，OTA终端采用TBox，网络架构采用功能域划分方式。

**2.1 OTA云端**

OTA云端服务平台，也称为OTA云端，包含OEM支持OTA升级的ECU全部完整升级包。OTA云端的设计要求是独立的平台，可支持多车厂或客户的设备计入，支持多车型，多型号规格，多种类设备软件的升级。

**2.1.1 OTA云端能力**

OTA云端对OTA终端需要具备如下接口和能力，包括版本更新检查接口、升级下载接口、升级结果汇报接口、升级进度汇报接口、升级通知能力、OTA云端升级策略需要支持全量升级、不定增量包升级、差分升级，可以实现静默升级和非静默升级。支持升级版本的迭代，更新，版本的分支等。具备批量任务管理功能，分批升级避免升级拥堵。

**2.2 OTA终端**

OTA终端包含OTA引擎和OTA升级适配器。OTA引擎主要负责协调和调度终端OTA升级、接收OTA升级通知、主动升级检查、升级包下载、升级包解密、签名验证、差分包重构、升级包分发与调度等相关工作。OTA升级适配器则是为了兼容不同的软件或设备更新逻辑或流程，根据统一接口要求而封装不同实现，升级适配器由需要OTA升级的各个软件实现提供。

**2.3 升级对象**

汽车OTA升级对象主要包括操作系统和应用APP，以及车内嵌入式设备ECU的升级。操作系统升级采用双系统升级策略。

针对ECU升级的过程描述：FOTA系统主要通过车载移动互联网进行数据上报及下行传输，通过车内网对车内设备单元进行数据刷写。典型的FOTA系统网络安全主要由OTA远程管理平台端、TBox端（4G LTE）、中央网关、域控制器端及数个ECU等节点组成。

FOTA系统网络安全性需要确保升级包在远程服务器端的安全存储、后台服务器到车端的安全加密通讯、中央网关的升级包解密、防火墙和OTA 管理，以及车内网络基于堆成加密的安全通讯和安全Bootloader的要素。

**03**

**ECU的OTA技术实现方案**

**3.1 非易失性数据储存服务**

绝大多数的嵌入式系统都需要有一个存储空间来存储一些关键非易失性数据，可选的器件如：TF/SD卡，NAND/NORFLASH等，汽车弟子啊常用的则是EEPROM和FLASH。一般来说FLASH和EEPROM在写数据之前都需要先执行擦除操作，对于EEPROM而言，其最小可擦除单元为8到32个字节，而FLASH就会很大在512字节以上，所以这也决定了使用EEPROM更加简单，软件不会很复杂。

**3.1.1 分区刷写**

为了合理有效使用内存，同时也为了方便管理，通常会对内存进行一个分配，比如Bootloader、BSW、ASW分别分配在不同的连续内存区域里，这样就能在对ECU进行刷写时能够只更新其中一个，其他保持不变。

**3.1.2 地址映射**

为了保证CPU执行指令时可正确访问存储单元，需要用户程序中的逻辑地址转换为运行时由机器直接寻址的物理地址，这一过程称为地址映射。如何保证我们所写的代码能放到规定的内存空间？这里需要使用到#pragma:

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS8xyt6d7Sy6PWJG2EoaW3siabRUc9XjBryd7iaAL3mqWIyQ4yMUnYibRia7w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

在程序中定义如下，则run\_cnt1和run\_cnt2, 则run\_cnt1就会放在0x70001000, run\_cnt2放在0x70004000。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS83u7ZwrvTFsd6OHmpxPdy67pxjDJsUZJ1a7l1YeEQ3kibX6HSz3M7GsQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**3.2 Bootloader 及几种OTA实现方案**

**3.2.1 关于Bootloader**

在汽车电子，现在bootloader基本已成汽车ＥＣＵ必备，其负责应用程序的启动和通过ＣＡＮ总线来更新应用程序和数据等。

BootLoader就是ECU启动时候运行的一段小程序，这段程序负责ECU固件的更新，也就是ECU选择性的自己给自己下程序。如果BootLoader更新完程序后，跳转到新程序运行；不更新的话，BootLoader直接跳转到原来的程序去运行。BootLoader更新完程序后并不擦除自己，下次启动后依然先运行BootLoader程序，BootLoader就是用来管理单片机程序的更新。

一般而言，BootLoader通过CAN总线来更新应用程序，有些也会通过LIN或者UART来更新程序，不管通过何种方式，都可以基于ISO14229来实现，也就是说ISO14229 UDS协议算是一种上层应用协议，可以用在多种通讯总线之上，二ISO15765是基于CAN总线的UDS协议服务，其定义了如何通过CAN总线来传输大数据。

**3.2.2 HIS及Bootloader升级过程**

HIS是一个很成熟的BootLoader规范，其基于AUTOSAR，对一个BootLoader该有的元素都做了很详细的定义。

1、Session Control (会话控制 0x10)

三个会话层：

默认会话层（Default Session）
编程会话层（Programing Session）
拓展会话层（Extended Session）

编程会话层是BootLoader主要实现的一个会话层，在该会话层下要实现一系列的诊断服务，从而形成一个为升级应用程序提供服务的服务层，PC或者手持客户机即可通过合法访问该会话层下的服务来实现应用程序的更新。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS8ge2OkaqjM800DywOXmoA8xEjgrkpnVwAXdBPRmCicibg4KIXFiatWvibicQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

2、Security Access（安全访问 0x27）

对于BootLoader安全访问是必须的，从而保证应用程序不被非法客户机给破坏，安全访问一般分为两步：

客户机向服务器请求种子，并解析种子算出钥匙
客户机向服务器发送钥匙，服务器核对钥匙。

不同的服务需要不同的安全等级来访问，默认服务器的安全等级为0不需要解锁，可以随意访问。

3、Routine Control（过程控制 0x31）

在bootloader里过程控制31服务一般用于应用程序和非易失性数据NVM存储中的擦除操作，内存标识：0xff - Flash，0xFE-EEPROM。

4、Request Download（请求下载 0x34）

客户端请求从客户端到服务器的数据传输。服务器收到 requestDownload 请求消息后，服务器应在发送肯定响应消息之前采取所有必要的措施来接收数据。

5、Request Upload（请求上载 0x35）

客户端请求从服务器到客户端的数据传输。服务器收到 requestUpload 请求消息后，服务器应采取所有必要的措施在发送肯定响应消息之前发送数据。

6、Transfer Data（传输数据 0x36）

客户端将数据传输到服务器（下载）或从服务器请求数据（上传）。数据传输方向由前面的 RequestDownload 或 RequestUpload 服务定义。 如果客户端启动了 RequestDownload，则要下载的数据将包含在 TransferData 请求消息中的参数 transferRequestParameter 中。 如果客户端启动了 RequestUpload，则要上载的数据将包含在 TransferData 响应消息中的参数 transferResponseParameter中。

7、Request Transfer EXIT（请求传输结束 0x37）

客户端请求终止数据传输。

8、Ecu Reset（ECU复位 0x11）

ECU复位

BootLoader升级过程如下图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS8NDqfBph6JZqseFceib8Tia3ncjPgCoXzlHrUlcCS0uAfBh6VnUqp7lww/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

**3.2.3 Bootloader的升级设计方案**

**1.SB(start bootloader)更新CB(custom bootloader)**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS8wy5QEbalAibdIibt7DEicHErxXVUibWicxF5qnBkrVXt4Niau4QaJX9PruvQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

优点：

* 逻辑机构清晰，软件分工明确
* 操作简单

缺点：

* 需要flash空间大，资源浪费
* 三级启动，机构复杂，开发和维护成本高
* 无法更新SB

**2.RAM+Flash Reboot更新**

不存在SB情况下，程序启动顺序是CB→APP。需要刷新boot时，首先把Reboot程序下载到不用的RAM里，然后在RAM环境下运行Reboot 下载新的CB。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS8jsh2aQe0fRW25DHn2jykVdWQn68Atia02VYSia4pqBPvdRlAZA2HXfZA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

优点：

* 不需要额外的flash空间，只需要少量的RAM
* RAM擦写速度快，则下载Reboot速度也会很快

缺点：万一中途掉电，则机器变砖

**3.RAM+RAM Reboot更新**

首先把Reboot + New CB 一起下载到RAM里，然后运行Reboot 擦除CB Flash区域，将RAM中New CB复制到CB Flash区域。最后，重新上电复位，RAM中的Reboott和New CB自动丢失，程序重新开始运行。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS8CWZ7qMicWgncFF0sPYjvh9KkSYEnh04me80YoiaaaFMibQdiasl21AsDAw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

优点：

* 比方案二少了一步下载
* 相比方案二CB更新全部在CPU内部执行，不受外部干扰，耗时更短

**4. 借助APP程序Flash空间**

刷新分三步：首先运行CB，擦除App，把Reboot下载到App区域。再运行Reboot擦除旧CB，输入新CB。运行CB刷回App。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS85PT0tIRpcRUJ5p3EZDPTPHkdicCl2MWnK3yYvR2UJ3QOjwCkRSbdvBw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

优点：

* 不需要额外的Flash和RAM资源
* 稳定可靠，通过优化设计，可以保证任何一个步骤断电，上电后都能继续操作，不会刷死
* 对CB稍做修改就能称为Reboot程序，开发快

缺点：

* 步骤多，不熟悉的操作者不易操作
* 整体刷新时间长，两次boot+ 一次APP

**5.借助额外的flash空间**

相比方案四需要一块和CB一样大小的额外flash空间，刷新分三步：运行CB,刷入Reboot到额外flash，再运行Reboot，更新CB，最后，运行新的CB，擦除Reboot。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS8gshW7Ys6MqsqI5oudyEh2qTHoevmZyIsGEOKynShrxFySPq474krgg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

**优点：**相比方案四，不需要破坏和恢复APP程序，更节省时间

**缺点：**相比方案四，需要更多的flash空间，且必须是独立的block

**3.2.4 OTA设计方案**

全量升级

完整的下载新版本固件，下载完成后将固件搬运到APP程序运行的位置。（一般来说是将APP从片外flash搬运到片内flash上）。搬运完成后校验通过后重启APP。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ucJVB65qcEWXLwNwytyS8yEaRRrtSUTqib4gvWCu5EAZDwibPPtIFhYXz6T6icOuhwWCyhhIxzhbug/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

差分升级

利用算法，做出原版APP和新版APP程序的差分包，将差分包下载到flash，内部的BootLoader程序在利用算法将新版APP合...