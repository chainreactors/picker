---
title: MCU如何通过UART进行OTA升级
url: https://mp.weixin.qq.com/s/48_VAt4PYmzM4DZU5hGPTA
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:16:57.347478
---

# MCU如何通过UART进行OTA升级

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaC1h6mQJfwX8RLYlPcnkvVBYnaqBiczCrz2vbQYXsQrSEds3WD1icvibiarwqtvksMiaoym9GXQfrJRDhGZelCOUBcib8CEsibEsj9PDA/0?wx_fmt=jpeg)

# MCU如何通过UART进行OTA升级

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247566311&idx=2&sn=27d2cf53ef824bfde9b824f90e864ec6&scene=21#wechat_redirect)

**01**

**概述**

空中下载技术OTA（Over-the-Air Technology）是用户自己的程序在运行过程中对User Flash的部分区域进行烧写，目的是为了在产品发布后可以方便地通过预留的通信口，对产品中的固件程序进行更新升级。通常实现OTA功能时，即用户程序运行中作自身的更新操作，需要在设计固件程序时编写两个项目代码，第一个项目程序为Bootloader区域，第二个项目程序App代码为真正的功能代码，执行应用和升级。这两部分项目代码同时烧录在User Flash中。

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvicC8TTgdBibJIrQIHlm35qR6MFzYUibUQTKvicXAa3SaEiaRSLCHAsfY9rkw/640?wx_fmt=jpeg&from=appmsg)

图1. OTA代码执行流程

在上图所示流程中，MCU复位后，从0x08000004地址取出复位中断向量的地址，并跳转到复位中断服务程序，在运行完复位中断服务程序之后跳转到Bootloader的main函数，如图标号①所示；在执行完Bootloader以后（App代码为图中FLASH灰底部分App程序的复位中断向量起始地址为0x08000004+N+M），跳转至App程序的复位向量表，取出App程序的复位中断向量的地址，并跳转执行App程序的复位中断服务程序，随后跳转至App程序的main函数，如图标号②和③所示，同样main函数为一个死循环，并且注意到此时AT32的FLASH，在不同位置上，共有两个中断向量表。

在main函数执行过程中，如果CPU得到一个中断请求，PC指针仍强制跳转到地址0x08000004中断向量表处，而不是App程序的中断向量表，如图标号④所示；程序再根据我们设置的中断向量表偏移量，跳转到对应中断源新的中断服务程序中，如图标号⑤所示；在执行完中断服务程序后，程序返回main函数继续运行，如图标号⑥所示。

通过以上两个过程的分析，我们知道OTA程序必须满足两个要求：

1) App程序必须在Bootloader程序之后的某个偏移量为x的地址开始。

2) 必须将App程序的中断向量表相应的移动，移动的偏移量为x。

**AT32 USART OTA 快速使用方法**

**硬件资源**

文档中是用AT-START-AT32F403A实验板的硬件条件为例，OTA demo源代码还包括AT32其他型号，用户只需编译对应型号工程烧录于AT-START实验板运行即可。

1) 指示灯LED2/LED3/LED4

2) USART1(PA9/PA10)

3) AT-START实验板

**软件资源**

1) tool\_release

● IAP\_Programmer.exe，PC机tool，用于演示OTA升级流程

2) source\_code

● Bootloader，Bootloader源程序，运行LED2闪烁

● App\_led3\_toggle，App1源程序，运行LED3闪烁

● App\_led4\_toggle，App2源程序，运行LED4闪烁

*注：工程基于keil v5建立，若用户需要在其他编译环境上使用，请参考对应BSP目录AT32F403A\_407\_Firmware\_Library\_V2.x.x\project\at\_start\_f403a\templates中各种编译环境（例如IAR6/7/8,keil 4/5,eclipse\_gcc）进行对应修改即可。*

**OTA Demo 使用**

本文档描述了两种常用的OTA应用demo，template app和dual app。

1) 打开Bootloader工程源程序，选择对应MCU型号的target编译后下载到实验板

2) 打开IAP\_Programmer.exe

3) 选择正确的串口、APP下载地址和bin文档，点击Download下载，如下图

4) 观察LED2/3/4闪烁，LED2闪烁-Bootloader工作，LED3闪烁-App1工作，LED4闪烁-App2工作

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvicylP2G2Sz2pFFq93tibrDgTRuWFIIn2xtWRncwEGfjO3zaIWd4uqUAZg/640?wx_fmt=jpeg&from=appmsg)

图2. IAP demo上位机

**02**

**Template app OTA程序设置**

**地址分布**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvica6tzGA6hUXb9zT3Mibod5DRjImhTVWSUGqFyfldv4kottKjVnLDTNrw/640?wx_fmt=jpeg&from=appmsg)

图3. Flash地址分配

*注：Bootloader区域最后一个扇区，用于存放防止升级过程出错（掉电等异常情况）的flag，用户编译修改Bootloader时，要保证不覆盖flag的地址。*

**执行流程**

OTA分为Bootloader、App和Template三部分，应用在App中执行，Template仅作为新App固件数据的临时存放空间。程序执行整体流程框图如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvicUrWKeEJibnkPpM0rhwZAXbMdPZgwNaia39CicUPEibUC9nqTpoK5yGm0yA/640?wx_fmt=jpeg&from=appmsg)

图4. 程序执行流程

**Bootloader project 设置**

1) Keil设置

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvicibc7W4JhasoSp3wGqiah4uZ19WKDgzicibfPt9xIZaMgLuBtEiaSMeiaR8gw/640?wx_fmt=jpeg&from=appmsg)

图5. Bootloader project中address 1在Keil设置

2) Bootloader源程序修改ota.h文件中

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvicLh5w8Kp8eKHyK1VZZlUN26SWgtND6rq69DET89y8ibOyANaxmOq0YXw/640?wx_fmt=jpeg&from=appmsg)

图6. Bootloader project中address 2在程序中设置

**App project 设置**

OTA demo提供了2个App程序供测试用，皆以address 2（0x800 4000）为起始地址。App1 LED3闪烁，App2 LED4闪烁。以App1为例，设计步骤如下：

1) Keil工程设置

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvicWINjEfmNmKVxYrLBFaweAsEMFjXgCibbDlnIUWonZTJsrTIx8qAe43A/640?wx_fmt=jpeg&from=appmsg)

图7. App project中address 2在Keil设置

2) App1源程序设置

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvicpUo3YdnQZmACT3xaKj7rWLNrUncFpcfTuUkRbEFA3X40cSUicRR4cnw/640?wx_fmt=jpeg&from=appmsg)

图8. App project向量表偏移在程序中设置

3) 编译生成bin文件

通过User选项卡，设置编译后调用fromelf.exe，根据.axf文件生成.bin文件，用于OTA更新。通过以上3个步骤，我们就可以得到一个.bin的APP程序，通过Bootloader程序即可实现更新。

4) 开启debug app code功能

如果在设计App code过程中需要对App project进行单独调试，请按照以下操作。

● 先下载Bootloader工程

● 再调试App工程

**03**

**Dual app OTA与程序设置**

**地址分布**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvicdGlApGLPIXzgJrUVsSOcfG4Y1G0lrkqWRQbLjFot1jC0lACEfrRblA/640?wx_fmt=jpeg&from=appmsg)

图9. Flash地址分配

*注：Bootloader区域最后2个扇区，用于存放App是否正常的flag，用户编译修改Bootloader时，要保证不覆盖flag的地址。*

**执行流程**

OTA分为Bootloader、App1和App2三部分，应用在App1或App2中执行。程序执行整体流程框图如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvicVljhF1g21aSlBHEFw8KvRz6AhA83E1GbrxuiaqzVAIf3RHX7ibrdBKtg/640?wx_fmt=jpeg&from=appmsg)

图10. 程序执行流程

**Bootloader project设置**

3) Keil设置

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWviccaFZicz3O5SeV9VVksxtHEtvRrqE3nASlO6Tm9SDwmOlJWJZm5I2pdg/640?wx_fmt=jpeg&from=appmsg)

图11. Bootloader project中address 1在Keil设置

4) Bootloader源程序修改ota.h文件中

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvicqEsC2DDCCUUic780UqA1OZc0ViakHunKsjmAcRpwAhvqA8Ddrql7iaR4Q/640?wx_fmt=jpeg&from=appmsg)

图12. Bootloader project中address 2在程序中设置

**App project设置**

OTA demo提供了2个App程序供测试用，app\_led3\_toggle以0x800 4000为起始地址，app\_led4\_toggle以0x8080000为起始地址。App1 LED3闪烁，App2 LED4闪烁。以App1为例，设计步骤如下：

5) Keil工程设置

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvicCvMG7RE6mWWLR5FEKfSRTrjAc3BgjCMyISsANaIwWYj9tr2geTFFVw/640?wx_fmt=jpeg&from=appmsg)

图13. App project中address 2在Keil设置

6) App1源程序设置

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvic1QXRRicZfVgWJ2cbup1rYGl6ibfxx4nRia388W04ckb8iah3n7Dpu1G1Uw/640?wx_fmt=jpeg&from=appmsg)

图14. App project向量表偏移在程序中设置

7) 编译生成bin文件

通过User选项卡，设置编译后调用fromelf.exe，根据.axf文件生成.bin文件，用于OTA更新。通过以上3个步骤，我们就可以得到一个.bin的APP程序，通过Bootloader程序即可实现更新。

8) 开启debug App code功能

如果在设计App code过程中需要对App project进行单独调试，请按照以下操作。

● 先下载Bootloader工程

● 再调试App工程

**04**

**Bootloader/App与上位机串口通信协议**

程序与上位机通信，接收固件升级数据，上位机端和嵌入式端通信协议如下：

1) 上位机通信协议

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWviceVuNGq7Xgg1dSajNXxrY35w1BoYbhmnJge6BS0Dt7MoYaoKqVialXLQ/640?wx_fmt=png&from=appmsg)

图15. 上位机通信协议

2) 嵌入式端下位机通信协议

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8ibr0ZmHdUpXg4lsT6xzWvic9cbYKC6PAgMb5FO5rsj1ROY4q4biaibtYOuSD7mwej84gqVGwAtZDPiaw/640?wx_fmt=png&from=appmsg)

图16. 下位机通信协议

注：ACK：0xCCDD

NACK：0xEEFF

Data：0x31+Addr+数据+chenksum（1byte）

Addr：4bytes，高位在前

Kbytes，下载数据，不足2K内容填充0xFF

Checksum：1byte，4bytes的Addr+2KBytes数据的校验和的低八位

来源：汽车ECU开发

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

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicHdaQsibvoH8dLYIIcT5YQibwbnuZn1MLCOMydw2SMKWbibsLpooeE2jgCt8FABvsVmlJZO5PO00Ryw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc...