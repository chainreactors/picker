---
title: CAN总线错误帧分析方法
url: https://mp.weixin.qq.com/s/hn8tvNT-i6KWeFUK4mMO_Q
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:26:06.788071
---

# CAN总线错误帧分析方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDfaBv4ib6aJ1czq1sTSicu5AYyiaibNBNrfjaDFYSSEhCZmzEkPkjnDfZKCYgia1rQt7se2icYW1fJaNEpGBQgE2icsGDwVVichOibZSJk/0?wx_fmt=jpeg)

# CAN总线错误帧分析方法

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

本文从两种不同平台（片上系统Linux平台以及STM32）解读分析了当出现CAN节点检测到CAN总线出现错误与故障时，我们如何从CAN控制器的角度去分析并解决问题，并在不上分析仪等设备的情况下，通过在线仿真解决问题。

我们先简单总结一下CAN 的错误处理与故障界定：

CAN控制器记录发生在发送/接收过程中，总线数据出现错误的总数（位错误，CRC错误等）。

CAN控制器根据总线出错数量由低到高，依次处于主动错误状态，被动错误状态，以及总线关闭状态。

位于主动错误的节点，在检测到错误时，可以发送主动错误标志（6位显性位），告知总线上所有节点发生了总线的错误，之后进行正常的收发操作。保证如果总线CAN\_H与CAN\_L出现短路等会影响整个总线通讯的问题时，各个控制器会迅速反应。

当随着发送/接收错误总数的增加，节点将位于被动错误状态，当检测到总线发生错误的时候，将等待总线出现被动错误帧（连续6位隐性位），之后才可正常进行收发操作。保证如果总线因为线长或者节点数增大，远处的节点干扰严重，则干扰严重的节点将不会影响其余节点的正常通信。

如果发送错误总数达到了255，则进入bus-off状态，处于这种状态的节点将会与总线隔离，直到检测到128 次出现11 个连续“隐性”位后，才可以恢复错误主动状态，错误计数器 也清零。

**01**

**Linux SocketCAN**

Linux 4.17.0-RC6 内核网络部分增加了SocketCAN，用于Linux的CAN协议 的一种实现。以前的嵌入式开发板的CAN驱动是以基于字符串设备的驱动注册到内核中，新的内核使用Berkeley套接字API，Linux网络堆栈并将CAN设备驱动程序作为网络接口来实现。CAN套接字API的设计与TCP / IP协议尽可能相似，以便熟悉网络编程的程序员轻松使用CAN套接字进行CAN通信。具体详细的特性介绍详见https://www.kernel.org/doc/html/latest/networking/can.html。其中章节“Network Problem Notifications”中介绍了一种CAN总线错误的记录机制，SocketCAN将所有总线上的错误包装成一个“错误帧”，注意这块的“错误帧”不是CAN总线上实际跑的错误帧，而是驱动部分将控制器或者总线上的检测的错误，包装成一个CAN帧，上报给基于网络层之上的用户程序。

我们在linux4.9内核E:\linux-4.9\linux-4.9\drivers\net\can目录下的Makefile中看到内核支持了包括SJA1000，以及赛灵思的开发板的CAN驱动支持，我们比较关心的CAN错误的定义呢，在E:\linux-4.9\linux-4.9\include\uapi\linux\can中定义了所有CAN总线可能上报给用户层的错误信息具体的关系图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAG7GroiaXxPZeSdVoicB3A6YgsCJic8zBhXnmguHhMMg90llTdXftfTAbNO5FhFERhWRKC0iaS7qzMDzcMOQmRxtQTUfj4xA0tibe4/640?wx_fmt=png&from=appmsg)

三个能展开的三级目录分别如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAYtKhKZLMHObxAPwn70stTK4ejzYfdGScfPWCvricH9icMQ9zrbYDtrILDAxfqEHxZG0y6ByndImwp26zt38X6gfnJIvz2Hib6Uk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDe7YicNxARpDOw3hfpibLhBrxUMvdAjhwNGz4MuOFbBaIGOecqNB4zgjPCs1X5zqfL9D4ufwp6954e85zUBjAMSU3Qfg3CzwLno/640?wx_fmt=png&from=appmsg)

这其中我们举个例子来说明这个伪造的错误帧是如何产生的，以AT91的驱动为例，下面的描述均来自内核源码。首先在设备的Open函数处注册了中断处理函数at91\_irq，函数在发生终端时候，判断中断类型为错误中断，调用at91\_irq\_err处理设备错误信息，细分中断源来定义当前新状态为bus-off、报警、主动错误状态还是被动错误状态，如果状态发生了变化，则调用at91\_irq\_err\_state形成错误帧进行上报。假如这个时候如果原状态为主动错误，而新的状态为RX/TX错误计数达到报警状态，则会更新设备当前状态，并向上层监听端口的用户程序发送一个表示控制器错误-->RX/TX错误计数达到报警状态的错误帧。用户程序就可以知道CAN总线发生了这样的错误，并检查干扰源。

**02**

**STM32F10x bxCAN**

工业现场的总线上一般有两种设备，一种为普通的can节点设备，他们在整条总线上按需分布，反馈一些即时的信息（传感器信息或者摁键等），另一种设备一般一根CAN总线上就一台这样的设备，它负责将CAN总线上的数据转发到以太网接口，WIFI，或者zigbee等通信接口，或者它本身带有屏幕，显示各个节点上报的信息并进行统一的控制。这种类似‘网关’的设备一般会上嵌入式实时操作系统，或者linux内核裁剪一下拿QT做做界面，或者直接就安卓了。

反观线上多数的设备，一般为了压低成本等原因，会采用STM32来进行开发，而总线上的状态，往往是这些处于总线远端的设备能更好的体现，并且出问题的设备也大概率会是这些设备，但是这些设备往往没有实时操作系统，业务开发起来比较缓慢且不易多人维护，导致往往对于异常的处理不足，关注实现往往大于功能实现的效率以及质量。而其更没有Linux比较完善的官方驱动支持，如上文一样可以给用户程序主动报一些总线上的错误。所以，基于STM32开发CAN的时候，更应该借鉴Linux的驱动实现方式，对总线上的错误进行记录，方便查询。

我们首先来分析一下STM32 bxCAN的错误中断源：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAeicWcGAzkkmGunicAYE7DfjrsYFAWeibY5nus9nWgGRfwA78aDXlQbiaabwbDwNUgRO24T5K1DMhXrkaykoKg5VSpicgcPL9CZ6hI/640?wx_fmt=png&from=appmsg)

由上图可知，ERRIE为错误中断的总使能位，EWGIE为错误警告中断使能，当接收/发送的错误数到达报警标准之后触发此中断，EPVIE为错误被动中断使能，当接收/发送的错误数到达被动错误标准时触发此中断，BOFIE为离线中断使能，当接收/发送的错误数到达离线标准时触发此错误，LECIE为上次错误号中断使能，当接收/发送出现错误的时候，且与上次错误不同，触发此中断，错误号根据手册能表示一下错误：000: No Error，001: Stuff Error，010: Form Error，011: Acknowledgment Error，100: Bit recessive Error，101: Bit dominant Error，110: CRC Error，111: Set by software。

在发送过程，bxCan有三个发送mailbox，STM32的库函数CAN\_Transmit负责将数据放到mailbox中并触发发送（若没有空闲的mailbox则返回错误），由手册可知，可根据TME来判断mailbox是否可能，库函数CAN\_TransmitStatus封装好能够直接获得当前mailbox的状态，这里建议对CAN控制器的CAN\_NART配置为DISABLE，使能报文重传功能，这样报文如果发送失败，将在SCHEDULED和TRANSMIT两个状态切换，直到发送完毕，才会释放邮箱。除非你的应用需要报文发送的准确时间点进行记录，并且你的应用实时性要求也不高，能够腾出时间去处理报文重传（如果你把CAN控制器的报文重传功能去掉了，那你必然要自己实现）。从这个流程中可以看出，我们可以将发送溢出（邮箱占满），以及发送仲裁丢失作为控制器的错误记录下来。

在接收过程中，就有接收溢出的中断可供记录接收溢出错误。

综上所述，STM32F10x  bxCAN提供的寄存器能够满足类似Linux的除了收发器其余的所有错误记录，通过库函数能够很方便的将CAN控制器的状态变化以及总线上的错误记录下来，从而可以分析现场CAN总线的状态。

来源：CSDN@「十六宿舍」

https://blog.csdn.net/geek\_liyang/article/details/80404636

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=appmsg)

**公司类型占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJAB...