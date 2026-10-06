---
title: 车规级MCU的DMA功能原理及设计架构
url: https://mp.weixin.qq.com/s/caQHrqk62ugKI43G-KcNzA
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:43.911645
---

# 车规级MCU的DMA功能原理及设计架构

# 车规级MCU的DMA功能原理及设计架构

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

不同于普通芯片，汽车半导体由于其恶劣的工作环境，它不仅对数据传输的速度有着高要求，对芯片及数据传输的安全性的需求也与日俱增。在汽车电子领域，普通的MCU不能适应汽车的工作环境，考虑到复杂的应用环境和安全性，相关厂商们研发了车规级MCU来满足市场需求。车规级MCU是一类具有广泛应用场景的车载芯片，也是现阶段众多汽车芯片中最重要且需求量最大的种类之一。在大批量的数据传输中，DMA的功能与工作效率对车规级MCU的系统性能至关重要。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9ibyILg8j4S1BU5s3bRicx2EUpv5HsYWVuNA3zpAsXLgXPSvjmqyc6TwCuvNHDRv4eFoVoetqFlEYQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**01**

**车规级MCU的功能安全需求**

功能安全即通过安全功能措施来避免不可忽视的功能风险的技术总称。功能安全（Function Safety）中的功能指的是监控受控对象和控制器的安全装置起的作用。通常我们将计算机作为安全装置，如果控制器发生故障，则该计算机将会关闭受控对象，并向用户发出危险警告。

谈及汽车电子的功能安全，必然绕不开ISO26262标准[10]。2018年，ISO26262在IEC61508功能安全标准的基础上应运而生，它是针对公路车辆内的电子/电气系统的汽车开发行业标准[11]。ISO26262标准引入了ASIL等级（汽车安全完整性等级）的概念，除了无需处理的QM等级，ASIL有四个等级，从低到高分别为A，B，C，D，其中A是最低的等级，D是最高的等级。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9ibyILg8j4S1BU5s3bRicx2EZS7NicN64s6Ekw8WTlZJnicHsrmaYBh1fsVlzcAKxcic4r2IuvXbqgA8g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

ASIL不同等级对应的相关功能安全风险如表2.1所示。ASIL等级越高，对系统的安全性要求以及实现功能安全付出的代价越高[12]，对功能安全模块的开发流程和技术要求也越严格。

ASIL四个等级的划分主要依据严重程度、暴露率和可控性这三个指标，下面分别简要介绍这三个指标。

• 严重程度：由于危险事件所造成的潜在伤害或损失的严重性，用S表示。

• 暴露率：人员暴露于危险当中的出现频率，用E表示。

• 可控性：车中人员采用紧急操作避免产生事故的可能性，用C表示。

典型的一些保障功能安全的方法有奇偶校验，时钟安全系统，双核锁步技术，看门狗技术等等。下面简单介绍一下这些保障功能安全方法的原理。

**奇偶校验**

奇偶校验可以用来检测SRAM的瞬时和永久性故障，如由于电磁干扰导致SRAM中存在的数据错误，是一种用于检测二进制数据中错误的方法。奇偶校验码编码的基本原理即在信息位之前或之后额外增添1个冗余位，使得整个码字中1的个数保持为奇数或偶数。通过检测这个冗余位（即奇偶校验位）的数据，检查是否出现1位错误。如果数据传输过程中发生了错误，如由于噪声引起了一个二进制位的变化，那么这个错误就会影响到奇偶校验位，从而导致奇偶校验位产生变化。

在接收端，我们通过检测奇偶性是否正确来判断数据是否正确。奇偶校验可以分为奇校验和偶校验：奇校验通过添加一个校验位，使得数据位和校验位中1的个数为奇数；而偶校验则通过添加一个校验位，使得数据位和校验位中1的个数为偶数[15]。由于奇偶校验的检测原理，使得它只能检测出奇数个的比特位错误，并且不能对错误数据进行纠正。

在STM32系列带奇偶校验的MCU产品中，为 SRAM每个字节增加了一位奇偶校验位，所以SRAM的数据总线是36位。在对SRAM进行写操作时，硬件自动计算并存储奇偶校验，当进行读操作时，硬件自动对数据进行校验操作。如果检测到错误，会立刻产生不可屏蔽的中断信号（NMI），并且可以配置可触发定时器的“刹车”功能。

**时钟安全系统**

MCU内部的时钟安全系统（CSS）可以用来检测外部高速时钟（HSE）和外部低速时钟（LSE）是否丢失。当检测到HSE时钟丢失后，CSS触发定时器的刹车功能和系统中断，并自动切换到内部高速时钟，软件可以根据这些触发的事件，制定相应的保护措施。LSE是RTC的时钟源，当检测到LSE丢失后，RTC不能再使用LSE时钟源，并产生CSS中断，在中断中需要将RTC切换到其他时钟源。

CSS只能检测时钟是否丢失。对于时钟存在但发生偏移的情况，可以通过时钟交叉测试来进行检测。该测试利用了MCU的TIMER模块的输入捕获功能，LSI时钟内部连接到TIMER的一个输入捕获通道，当分别使用HSE或者HSI作为计数时钟时，通过检测LSI的频率是否在正常范围内，间接地检测了HSE/HSI的频率。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9ibyILg8j4S1BU5s3bRicx2EpicBPfkZfyHQibOzFz2Wol4UrzMHf0NbSSPTOhQfOF6ogLSNjPDIOE7g/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**双核锁步技术**

双核锁步技术（DCLS：Dual Core Lock Step）是指对安全关键型的核心处理模块进行复制，在每一个时钟周期对双核的输出进行比较，在发生故障时输出错误标识信号，以供系统及时采取应对措施。在航空器、汽车等很多需要高可靠性计算的系统中，通常需要采取双核锁步技术。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9ibyILg8j4S1BU5s3bRicx2Ea6qY86FicIucIdDTmnwVaMTDX8rMUxUc6iaSWiaBVdYTAYwCqAo6PmF7g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**02**

**DMA**

**DMA 功能**

DMA（Direct Memory Access）即直接存储器访问，是一种应用在系统中高效搬运数据的专用接口电路。DMA可以不借助CPU，将数据从一个地址空间拷贝到另一个地址空间，从而在传输过程中释放CPU。DMA在外设和存储器之间提供高速数据传输，由于其不需要通过CPU全程控制数据，解放了CPU资源，大大提高了CPU的工作效率。

\* DMA模块能够处理复杂的数据传输，其可以执行以下功能：

• 能向CPU发出DMA请求信号；

• 在CPU响应DMA请求后能接管系统总线进入DMA周期；

• 向地址总线发出地址信号，向控制总线发出读/写控制信号；

• 能控制所传输数据的字节数；

• 能从源地址中读取数据写入到目的地址；

• 能在数据读写后进行源地址和目的地址的计算；

• 能够进行寄存器信息更新，包含16个通道的传输控制描述符（TCD）；

• 能够执行DMA突发传输；

• 能判断DMA操作是否结束，在传输完成后产生中断信号并释放总线。

一次DMA传输工作需要在传输前需要配置信息，在传输后需要处理信号。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9ibyILg8j4S1BU5s3bRicx2Ec5yBAyFqVtiaA1BrFRA8MhFmfKKlDSXtAWmjV45VBdGJNy5puT1Ds9g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

**DMA 传输过程**

对整个传输过程来说，一次DMA传输工作，按照顺序可分为传输前的配置、传输过程中的工作和传输完成后的处理这三个部分。

**\* 传输前的配置：**

数据传输前，CPU需要提前配置好DMA中承载传输信息的寄存器，以明确DMA的传输状态。这些信息需要包括数据传输的控制与状态信息，数据传输的源地址与目的地址，每次读写的数据大小，每次传输后的地址偏移量，每次小循环传输的字节数，数据的传输特性，起始主循环计数值与当前主循环计数值，错误状态标志位以及DMA控制器使能判断的命令等信息。没有预先配置好寄存器，DMA就无法开始工作。

**\* 传输过程中的工作：**

当初始化配置结束后，根据配置信息，外部源端向DMA控制器发起总线访问的请求信号，该请求信号通过DMA反馈给CPU。一旦CPU准许总线访问请求，DMA获得总线控制权，开始进行数据传输。当数据开始传输后，控制状态寄存器中的工作状态位置1，通道进入工作状态，当数据传输完成后，通道工作状态位置0，通道完成标志位置1，数据传输结束。

**\* 传输完成后的处理：**

传输工作结束后，DMA发起一个中断信号给CPU，CPU在接收此中断信号后，数据传输工作完成。DMA将总线控制权重新交给CPU，DMA则从总线中的主机设备再次变为从机设备。

**DMA 工作方式**

在DMA方式中，有可能出现CPU与DMA因竞争使用主存产生冲突的情况。为解决这一问题，DMA传输一般有以下三种方式。

**\* CPU暂停访问方式：**

当需要DMA传输时，DMA向CPU发出总线请求。之后 DMA一直占用总线，直到数据传输结束后才把总线的控制权还给CPU，这种传输方式在传输过程中完全不需要CPU进行传输工作，被称为CPU暂停访问方式。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9ibyILg8j4S1BU5s3bRicx2ESh6tVor4MODmgfsRxEkr5GlBmGic8WLjaUrrk99QY2ujLWeGgWcHh3A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

图为CPU暂停访问方式的工作时间示意图

实现CPU暂停访问方式的电路较为简单、适用于数据传输率高的设备成组传输，但同时也存在内存未充分发挥、部分工作周期空闲等缺点。

**\* 交替访问主存方式：**

交替访问主存方式是另一种解决DMA和CPU访问主存冲突的方法。交替访问主存方式以固定时间单位交替让DMA和CPU传输数据，从而能够交替访问主存而不产生冲突。在这种方式下，DMA不需要向CPU发出申请和归还总线权限的信号。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9ibyILg8j4S1BU5s3bRicx2EUIicAia7xjicaGE548QVpK5XzZzs6ptu0tmcZD25Erhib8xC0uRGRowhgQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

在这种方式中，DMA传输效率很高，但会影响CPU的工作效率。同时，这种方式所需要的硬件逻辑相当复杂，实现起来相当困难，因此这种方式在实际应用中并不常见。

**\* 周期挪用方式：**

周期挪用方式是指在CPU没有访问主存的周期中，采用DMA 实现数据传输，由于CPU没有访问主存，因此DMA不会影响CPU的工作。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9ibyILg8j4S1BU5s3bRicx2EvMWibbR66GYktGA2ibcSal68lVibRvvc5xKeMFncY4VqEdZEz59yzeCaA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

周期挪用方式实现了CPU和DMA的并发工作。但这种传输方式存在申请、建立、归还总线控制权三个过程，需要复杂的时序电路，且数据传输过程是不连续的和不规则的，因此这种传输方式适用于I/O设备读写周期大于内存存储周期的设备。在实际应用中，需要面临的情况比较复杂，需要DMA控制不止一个I/O设备。由于DMA通常只控制一台或少数几台同类设备，为了同时控制许多台同类或不同类的设备，因此引入了通道设备。

参考文献:

李希源.基于AMBA总线的车规级MCU的DMA设计[D].中国电子科技集团公司电子科学研究院,2024.DOI:10.27728/d.cnki.gdzkx.2024.000120.

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=app...