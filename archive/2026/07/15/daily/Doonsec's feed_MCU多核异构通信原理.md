---
title: MCU多核异构通信原理
url: https://mp.weixin.qq.com/s/C9bXuebA50Dvjy68e2YB1g
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:53:56.686317
---

# MCU多核异构通信原理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDu26ibUBErrGvA2pE9AJvkSGkSwicXG8XGXtnIO1WJBicweOLqgwG4l3ZyLWCtofJFjNPrIlhGiaz0HzyuQyajlGSHCh3brCVgSeI/0?wx_fmt=jpeg)

# MCU多核异构通信原理

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

随着电子技术的不断发展，以及市场需求的日益增长，嵌入式系统不仅要求执行复杂的控制任务，还需要实时地采集和处理数据。

为了满足这些需求，多核异构处理器成为了一种流行的解决方案。这类处理器通常结合了ARM架构的A系列核心（用于处理高级计算任务）以及M系列或R系列核心（专注于实时操作）。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twibia9vX5iclguiaNQny26fOhhgcuicCXdR3SjNQ2icdfdDHiccZk8qFsuaRFAiaSicD1TppYZTZ0ibwncDEdsA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

在这种架构下，复杂的控制任务可以由搭载Linux的A核心处理，而实时数据的采集和处理则可以交由运行RTOS的M核或R核来完成。

本文结合瑞萨RZ/G2L 多核处理器，给大家讲述一下多核异构设计及通信的原理。

**01**

**多核处理器概述**

在传统设计中，两颗芯片之间需要通过外部接口交换大量数据，这不仅占用了宝贵的引脚资源，而且数据传输效率低下。

相反，集成了A核和M核或R核的多核异构处理器利用内部总线结构实现了快速通信，并共享内部资源，从而避免了对外部引脚的占用。

这种多核异构的系统设计不仅降低了通信过程中的信息安全风险，还减少了芯片采购和管理成本，缩减了PCB板的成本和尺寸，并简化了开发流程。

**瑞萨RZ/G2L处理器概述**

配备双核Arm® Cortex®-A55 (1.2 GHz) CPU和单核Arm® Cortex®-M33 (200 MHz) CPU、3D图形加速引擎和视频编码解码引擎器的通用微处理器。

G2L框图

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibia9vX5iclguiaNQny26fOhhgAibFEBRpazykfykv3ocwmmJ8BOEZGdKlPo1LlkSY7xTOBsaVINIQFHw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**02**

**异构通信机制**

异构通信机制（OPENAMP Open Asymmetric Multi-Processing）的方案越来越成熟了。

在RZ/G2L系列的MPU中，我们可以看到多核异构架构的一个实际应用。这款MPU拥有一个大核Cortex-A55，频率高达1.2GHz，能够运行Linux操作系统，以及一个小核Cortex-M33，频率为200MHz，专门用于运行RTOS或裸机(bare-metal)程序。这两个核心之间的异构通信是通过OpenAMP软件框架实现的。

OpenAMP是一个轻量级的通信协议，它使得不同的处理器能够通过共享内存或消息传递机制来进行交流。在一个多核处理系统中，各个处理器可能会运行不同的软件模块，而OpenAMP框架则为这些模块之间的数据交换和协作提供了一种有效的手段。通过这种方式，OpenAMP不仅简化了多处理器间的通信，还增强了整个系统的协同效率和功能性。见图1。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twibia9vX5iclguiaNQny26fOhhgicbFtWGTupuO8OwALJxU2Lib3CZZA6ujGWBduc5uiagPiaeK1oVVOP8YHw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

图1

**03**

**Virtio 虚拟化模块**

Virtio是一个共享内存管理的虚拟设备框架，Virtio中的vring是指向数据缓冲区指针的FIFO队列，有两个单向的vring，一个vring专用于发送到远程处理器的消息，另一个vring用于从远程处理器接收的消息， 数据就存放于共享的内存中，即Vring buffers， 一半用于发送，一半用于接收。

**04**

**RPMsg远程处理器消息传递**

RPMsg框架位于Virtio的上层，RPMsg（Remote Processor Messaging）框架是一种基于Virtio的消息总线。见图2。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twibia9vX5iclguiaNQny26fOhhgHsiceywDnWwJq38ehe5oj9Q42ibSCwem8zN0ARCvCL4KU3icUp0RMasAA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

图2

**05**

**Remoteproc**

主处理器上的Linux操作系统可以对远程处理器及其相关软件环境进行生命周期管理，即启动或关闭远程处理器。见图3。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibia9vX5iclguiaNQny26fOhhgiasO9BictAmgmYbToMcQppeQL5RSYQcicKlEG09olpXOWImnxfz2kBNaQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

图3

**06**

**IPCC处理器间通信控制器**

MHU（Message Handling Unit）是MPU芯片内的一个IP模块，担任IPCC角色，用于Cortex-A55（CA55）之间或与Cortex-M33（CM33）之间的消息通信。数据传输通过共享内存方式实现。

一个通道由一对数据传输处理寄存器和响应传输处理寄存器组成，共挂载12个通道（CA55 Core0/Core1 CM33，安全和非安全区域）。见图4。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibia9vX5iclguiaNQny26fOhhg0SGrSBCCTtyqK8Vq0JoibN5xoDEGabicb6bhTuMA69icibcmY5VfG3XHFA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

图4

**以上介绍了RZ/G2L双核异构的通信方式，同时RZ/G2L产品也提供相应的软件支持。**

**07**

**Multi-os (CA55 Linux + CM33 RTOS)**

客户可以使用灵活的软件包（FSP）快速开发应用程序，使用OpenAMP创建与Linux配合使用的应用程序。见图5。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibia9vX5iclguiaNQny26fOhhgCnANYgFc234XYMjfvpFysuLEv4r5H4RPTAcraibcy2Nuu0q3PLOaNSg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

图5

**08**

**Cortex-M33开发环境**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibia9vX5iclguiaNQny26fOhhgGR3Dib4DasfP6Q3qFicr9yT47oFgzvgiaXlBOBkgJmeye6q42SMMCKIFg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

图6

相应硬件板及软件工具可以通过瑞萨官网获得。

**09**

**JTAG在线调试**

当连接JTAG时，必须如下设置DIP SW1。见图7。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibia9vX5iclguiaNQny26fOhhgcngS7hUgZ7dOSS8PfOGaicYPOwwvW8gtnaQ9bB9xDCiah0HYL1u6y1xg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

图7

**CORTEX-M33启动方式**

* CM33由CA55加载启动

* 引导过程中有多个时间点可以执行此操作：

● Arm Trusted Firmware

 启动CM33的最快方法

 允许将代码加载到安全RAM中

● u-boot -> Multi OS SW package默认方式

 CM33 固件容易更新

 二进制文件存储在u-boot可以访问的文件系统中

● Linux (remoteproc)

 最方便维护，软件升级改动少

**共享资源**

资源共享时，请注意如下分配

* 引脚复用

* 内存分配

* 外设分配

来源：车端软件开发

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

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

博世、大陆集团、联合汽车电子、安波福...