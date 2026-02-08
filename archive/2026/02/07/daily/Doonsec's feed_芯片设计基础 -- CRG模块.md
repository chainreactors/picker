---
title: 芯片设计基础 -- CRG模块
url: https://mp.weixin.qq.com/s/DR78PN2MYozsCzQjpFNsdQ
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:30:34.284483
---

# 芯片设计基础 -- CRG模块

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCU1cNx788jaFrh0KbogDZfoWp3Rx9qRc8V0ic2QH52T0XNRViaV75fyoZZegqYb9fdxlatMwK8bjZ3yFZ0VTke9FPeVaraY4ia8M/0?wx_fmt=jpeg)

# 芯片设计基础 -- CRG模块

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

CRG是芯片里的时钟和复位生成模块，全称是Clock Reset Generator。CRG模块提供整个系统所需要的时钟和复位信号。本文主要介绍一下CRG时钟系统和复位系统的基本模块和概念

**01**

**CRG时钟系统**

CRG的时钟部分一般都包括时钟源、锁相环（PLL）、时钟分频、片上时钟控制器（OCC）、时钟门控（ICG）、时钟切换、时钟buffer等电路结构。

**1.时钟源** 一般来自外部的晶振。常见的外部晶振有32.768KHz时钟和24MHz时钟（这个频率可变）。32.768KHz时钟一般提供给RTC模块等，用于产生系统时钟、时间戳等。24MHz时钟一般用做PLL的参考时钟。

**2.锁相环（PLL）** 基于晶振提供的基准时钟，生成稳定的高频时钟。

**3.时钟分频（divider）** 将锁相环输出的高频时钟进行分频，从而满足不同模块的时钟需求。

**4.片上时钟控制器（OCC，On–chip Clock Controller）** OCC是插在SoC上的逻辑电路，用来做DFT测试。在自动测试机台上对芯片进行全速测试时，根据scan信号控制选通ATE时钟或芯片内部时钟。

**5.时钟门控（ICG，Integrated Clock Gating）** ICG通常是用于控制打开和关闭时钟，从而降低功耗。一般模块级的ICG是手动加，寄存器级别的ICG是综合工具自动加。

**6.时钟切换**一般分为clk mux和clk switch。

clk mux是组合逻辑，用于静态切换，动态切换的话会出现glitch，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC0DF5zbJ5XA5KoBodibYIK46rhOibX7rj6hlhTbZjf9adE1ovRkEuHcgQtk26JhdO6Y0Wx4xxXCibU8zNE6dO0VfPcS2L6EynVN8/640?wx_fmt=png&from=appmsg)

clk mux

clk switch，时序逻辑，可用于动态切换。在两个电平相反的时候切换时钟，肯定有毛刺；电平相同的时候，即使不产生毛刺，时钟切换后的第一个时钟的周期或占空比也不是理想的。所以为避免毛刺的产生，需要在两个时钟都为低电平时进行切换。一种典型的无毛刺时钟切换电路如下所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCgG0NQ8xS5sTjVEafDviana99zX8vMvDnRib7BTQJZicKEZmTsJza2ae6jZaSYIu5Hx1Xs1CwlOyAjLWOm3OhicUY7ZJwPBJwR0icc/640?wx_fmt=png&from=appmsg)

glitch free clock switch

该电路利用时钟下降沿对时钟选择信号 sel\_clk 进行缓存。同时一个时钟选择信号对另一个时钟进行反馈控制，保证同一时刻只能有一路时钟有效。最后采用或操作将两路时钟合并，完成时钟切换的过程。

**7. 时钟buffer** 增强时钟信号的驱动能力。

**02**

**CRG复位系统**

在芯片设计中，复位逻辑是一个很重要的部分。复位是让芯片进入一个能稳定操作且确定的初始状态，从而避免芯片在上电后进行某个随机的状态而死机，或者是运行过程中出现了问题，能通过看门狗等方式产生复位而恢复初始状态。

芯片中的复位源一般分为片外reset源和片内reset源。

片外的reset源一般有来自PMIC的power reset，来自系统板上的pad reset，jtag reset等。片内的reset源有watchdog timeout reset，software reset及其他硬件机制产生的reset等。一个模块的reset可能由几种或者全部reset源控制。

复位的类型包括同步复位、异步复位、异步复位同步释放。

复位的类型包括同步复位、异步复位、异步复位同步释放。

**2.1 同步复位**

同步复位是指复位信号只有在时钟有效沿到来时，才能有效。同步复位的verilog代码如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBP5Aiad1jB32FhrVJQtiadGmj44enlhynbulDFQib5WTB5m5CEeOKE1GFqFUOdic0tsGEia7vhLSh7Lg01GMCqaGDrwFgZianHWnwYE/640?wx_fmt=png&from=appmsg)

其综合得到的电路如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC9EQWd1ycHjuJZ6hbhT08AicOaDVFQJtIYsJIG2hQseIsRrAsWovibuHibRMa8HtqjNlSfoD4qWaMM1M5OFhdfskicWfbKDWODaicw/640?wx_fmt=png&from=appmsg)

带同步复位的可加载触发器

**同步复位的优点：**

* 同步复位一般能确保电路是100%同步的，有利于时序分析，综合出来的最高频率一般较高；
* 同步复位会综合成更小的触发器，特别在该复位信号被触发器的输入逻辑门控时；
* 同步复位确保复位只发生在有效时钟沿。时钟可以作为过滤掉复位毛刺的手段；
* 在一些设计中，复位必须由一组内部条件产生。推荐在这样的设计中使用同步复位信号，这样可以将时钟之间的复位毛刺过滤掉。

**同步复位的缺点：**

* 大多数逻辑器件库中的DFF只有异步复位端口，所以使用同步复位，综合器会在寄存器的数据输入端插入组合逻辑，一是会耗费组合逻辑资源，二是综合器无法分辨复位信号和其他数据信号，需要判断综合出的复位信号是否满足设计需求。
* 复位信号的有效时间必须大于时钟周期，才能保证被可靠地识别，完成复位。所以有时需要脉冲展宽器，以保证复位信号能出现再时钟有效沿处。
* 门控时钟电路情况：同步复位需要时钟来复位电路。在使用门控时钟时可能出现问题。在复位信号发出时，时钟可能关闭，在这种情况下只能使用异步复位，并在时钟恢复前移除复位信号。

**2.2 异步复位**

异步复位是指无论时钟沿是否到来，只要复位信号有效，就对系统进行复位。使用异步复位的触发器在设计时就加入了一个独立的复位引脚，通过有效的复位信号即可将触发器进入复位初始状态。

下面是带有异步复位信号的触发器的verilog代码：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaC9YGdW75GhEZI8H7HicKtJEzic6ZJqzSAibt7nVkcYWrFBeBre62h2OiaS8eZzDCb4CsZs5icNcicsP7gTSOGBh04XHdJbpW9iaAHEGk/640?wx_fmt=png&from=appmsg)

上述代码所综合出的电路结构如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCCRW1BXfdj5aibibAEWBo7GqbIOvdqyVpb4ibfM2H7POEb7IQhHWBnflQCTRjBQL5ztpnPXzWN8UjmqMOKW0hNDPyzN3mOHOyE8I/640?wx_fmt=png&from=appmsg)

异步复位可加载触发器

**异步复位的优点：**

* 异步复位最大的优点是不增加数据路径的延迟，保证数据路径上是干净的，这对于时序很紧张的数据路径来说非常友好。
* 大多数器件库的DFF都有异步复位端口，采用异步复位可以节省逻辑资源。
* 最明显的优势是有没有时钟都可以复位，在芯片上电或者门控时钟也能正常复位触发器。

**异步复位的缺点：**

* 在复位信号释放的时候可能会出现亚稳态问题：复位释放在时钟有效沿附近；
* 容易受到毛刺的影响

**2.3 异步复位同步释放**

与数据信号需要满足的建立时间和保持时间类似，复位信号也需要满足恢复时间（recovery time）和撤销时间（removal time）：

* 恢复时间：指的是异步复位被设置为无效后，在下一个时钟有效沿到来之前需要保持稳定的最短时间。类似于同步电路中的setup time。
* 撤销时间：指在时钟有效沿来临之后，异步复位信号需要继续保持有效的最短时间。类似于同步电路中的hold time。

如果不满足异步复位信号的恢复时间和撤销时间，那么可能产生亚稳态。因此需要在异步复位信号释放时对其进行同步（异步复位同步释放），即使用复位同步器，结构如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBQGK86wHSWsadMPprV9aKucLEGYjMdSibDYXOlibldBKQicbpkHVWZbKabjVOpqmvIrcljgP6UuzUbIjDm4DiamDNr0Qh5zzLX1mY/640?wx_fmt=png&from=appmsg)

复位同步器

verilog代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAPaIhrPNia0VvJZ2VPezvfuXktsz7QkN7QHp3oSnd3twiaIK4ibqICIKSE01EOrxC43MFGCNs5iaUvXLY3hngu7SsCCpx7JqoicwzE/640?wx_fmt=png&from=appmsg)

首先，当异步复位信号有效时，两个触发器都会被复位为0值，进而驱动主复位信号masterrst\_n通过复位缓冲树，再到达设计中的其他触发器，然后整个设计都异步复位（即所谓"异步复位”）。

当复位信号被置为无效时，第一个复位寄存器将在时钟的控制下被置为1，随后下一个周期，第二个复位寄存器也会被置为1，最终花费了两个时钟有效沿移除了主复位信号，进而整个设计开始正常工作（即所谓"同步释放”）。

上述两个过程合起来称为异步复位同步释放。

来源：知乎@someone

https://zhuanlan.zhihu.com/p/701208905

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicHdaQsibvoH8dLYIIcT5YQibwbnuZn1MLCOMydw2SMKWbibsLpooeE2jgCt8FABvsVmlJZO5PO00Ryw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561756&idx=2&sn=f9b8c214978537f47cccba736cdb5bfd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg=...