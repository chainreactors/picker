---
title: Bootloader从入门到实战—OTA升级的基础
url: https://mp.weixin.qq.com/s/ZXgb2_NQO_9jB0YjUdo6GQ
source: Doonsec's feed
date: 2026-08-26
fetch_date: 2026-08-27T12:10:47.051687
---

# Bootloader从入门到实战—OTA升级的基础

# Bootloader从入门到实战—OTA升级的基础

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247576684&idx=2&sn=99b4244a2b1c95bd46442f3151ac6b4b&scene=21#wechat_redirect)

**01**

**上电第一件事：启动流程到底在干什么**

先说个反常识的结论：你的main函数不是程序的起点。MCU上电后跑的第一段代码，跟C语言半毛钱关系都没有，是硬件自动完成的。

以STM32为例，上电后CPU去0x08000000读数据。这个地址放的是中断向量表，它的第一个字是栈顶地址，第二个字是复位中断入口地址。硬件把第一个字装进MSP寄存器（主栈指针），把第二个字装进PC寄存器（程序计数器），然后就从复位入口开始取指执行。整个过程不需要你写一行代码，芯片出厂就这么设计的。

复位入口那段代码在启动文件里，干了三件事：先调SystemInit配置时钟和向量表，再进\_\_main把全局变量、栈初始化好，最后才调main。所以准确说，main是启动流程跑完的结果，不是开始。搞懂这点，你才能理解Bootloader跳转那几行神代码到底在干嘛——它就是用软件模拟了一遍上电启动。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBlIdYCTO1dcsHrtvF3he1cfwTEAw3DdOt7LZzmp6z6h9QGTRUZRtEUKxaUkRibLXkgyEYfaYQH8q6IypRibdltfAXAPNQMASbicg/640?wx_fmt=png&from=appmsg)

对照前面说的上电流程看：取栈顶装MSP、取复位入口跳转，跟硬件上电干的事一模一样。区别只是硬件从0x08000000读，Bootloader从APP区地址读。APP区第一个字必须存栈顶地址，所以跳转前可以顺手做个合法性检查，比如判断栈顶地址落在RAM区间（0x20000000开头）再跳，防止跳到空白Flash上死机。

这里有个跨行者必踩的坑：APP工程编译时，链接地址必须改成APP区起始地址，比如0x08004000，同时要设置中断向量表偏移。STM32上就是写一行SCB->VTOR = 0x08004000;，不写这行，APP一进中断就跑去执行Bootloader的向量表，程序直接跑飞。传统51单片机中断向量表不能偏移，所以传统51做不了Bootloader，STC是靠独立BOOTROM实现的——这是芯片架构决定的，不是软件能绕过去的。

那Bootloader怎么决定直接跳APP还是进升级模式？常见做法是上电后检查几个条件：某个GPIO引脚电平（比如产线刷写脚拉高就进升级）、通信接口有没有收到升级命令、或者APP区有没有有效的固件标记（一个magic number加版本号）。判定逻辑越简单越稳，别在Boot里堆太多功能，Boot越短小，出问题的面越小。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA2nmSaw8SSgnWboFlzTtxanV9j7a0OSlRsmOJPicWfjWUyoObwSqxOQteJGuPxqibaCuucDxgic3JPYgdLACcYL7ibpV8uF95WDyU/640?wx_fmt=png&from=appmsg)

上面这张Bootloader流程图就是整个系统的骨架，后面所有内容都是往这张图里填肉。

这里顺带把一级Boot、二级Boot说清楚。一级Boot是芯片出厂固化在内部BootROM里的程序，不可擦写，比如STM32串口ISP就是靠它实现的，开机时它检查BOOT引脚电平决定进用户Flash还是进系统存储器；二级Boot才是我们常说的那个能升级APP的Bootloader。多级Boot的好处是分工和保险：出厂固件永远有最后兜底，应用层怎么折腾都死不透。车规芯片上常见三级结构——ROM里固化一级，Flash里放二级，再往上才是APP。

还有个经常被问的细节：Bootloader从哪知道自己该升级？除了查GPIO和通信命令，很多设计会在Flash里存一个标志位区域（比如最后几个扇区），APP要升级时先写一个请求升级标志再软复位，Boot上电读到标志就进升级模式，升级完成后清掉标志。这个标志区要选擦写寿命长、不易被误擦的位置，而且读写都要带校验，防止标志位被干扰导致Boot误判。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC7YgsSlEVjgIIqRu0a0egOlHtg6CO75UURGssibjmMDQIZJmAzJ1eJvRK8kyyvQ3uAd7LOa9wNlSSECCPfmlZeZvLEejIicWkRY/640?wx_fmt=png&from=appmsg)

**02**

**上下位机怎么对话：刷写协议与帧格式**

Bootloader要接收固件，就得跟上位机（产线工具、诊断仪、手机App都算）说话。通信方式可以是UART、CAN、USB、以太网，但光有物理通道不够，两边得约定好协议：一帧数据多长、先发什么后发什么、怎么知道对方收到了、出错怎么办。

先看帧格式。一个典型的串口刷写帧，拆开来看长这样：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBLpza7msBXjPgJuTxibHUcWDSOGxonGLYlOdUWWKNOOm3mKdutGAEUTgawJZ4QQibZb6nLa5j5wvU8ibD9LF6mpuSqVicGOroYaAY/640?wx_fmt=png&from=appmsg)

帧头用来让接收方找对位置，防止数据流中间错位后一直错下去；命令字区分这条帧是干什么的，比如擦除、写数据、跳转APP；长度告诉对方数据区有多大；校验保证这帧没错。接收方收到一帧，先查帧头、长度、校验都对，才回一个ACK；不对就回NACK或者不回，发送方等超时没等到ACK就重传，重传几次还失败就报错终止。

这套请求-应答-超时重传机制是所有刷写协议的底子。Xmodem这类文件传输协议也是这个套路，只不过把一帧数据拉长到128或256字节，一帧帧传，每帧都带序号和校验，接收方收一帧回一帧。

汽车行业有自己的标准玩法，走的是UDS诊断协议（ISO 14229）。刷写一条固件走三个核心服务：0x34请求下载（告诉ECU我要写多大、写到哪个地址，ECU回一块最大块长度）、0x36传输数据（带块序号，一包一包发）、0x37请求退出传输（发完了，让ECU收尾校验）。前后还要配合0x10会话控制切到编程会话、0x27安全访问解锁。这套服务是行业通用标准，车厂、Tier1、工具链都认，面试和干活都躲不开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC7ZwAeg29D0SynibwPxs7XadypTvvdZ0P2HHn8GHRXS9LGZTpia6s7rJxicGZj331nmUUxaLFXed7HyfHU8LRvUiavsO4QL2I8TjE/640?wx_fmt=png&from=appmsg)

踩坑提醒：CAN刷写和串口刷写有个大区别——CAN一帧最多8字节数据，大固件得拆成成千上万帧，而且ECU擦Flash的耗时可能比发数据还长，所以上位机和Boot都要处理忙状态（UDS里ECU可以回NRC 0x78表示正在忙，请稍等）。新手最容易在这栽跟头：上位机噼里啪啦发完，Boot还在擦除，数据全丢了。

超时和重传参数也是调试重灾区。串口刷写里，波特率越高每帧传输时间越短，但误码率也上升；超时设太短，Boot处理一帧数据稍慢就误判丢包疯狂重传，把链路堵死；设太长，出错后等待时间感人。工程上一般是固定波特率 + 帧级ACK + 秒级超时 + 连续3次失败终止的配置起步，再按实测调。还有个细节：接收方处理完一帧要清空接收缓冲，否则残留字节会污染下一帧的帧头匹配，这种偶尔抽风的问题排查起来特别折磨人，多半就是缓冲没清干净。

协议层还有个现实问题：Bootloader要兼容不同固件格式。上位机发的是hex还是bin，Boot最好都认得。bin是纯数据，没地址信息，适合连续地址的刷写，但烧录时必须知道起始地址；hex带地址记录（Intel HEX格式），每一行都写了数据该放哪，Boot可以直接按行解析、按地址写Flash，还能跳过空区域。很多Boot为了简单只收bin，上位机负责把hex转成bin再发。格式转换放在上位机做，Boot保持精简，是工程上很常见的分工。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBZ1pVWIgaFib8fSzI0iaYSl83YC8qTSLrNBN4cRT5ZtblRkzIRKib7YmcibzYVDrVYJbwE0oxQqdGGoLZUmrSPhBvFQ04pjOwwicac/640?wx_fmt=png&from=appmsg)

**03**

**Flash擦写与校验：别把固件写坏了**

固件收到手，接下来是Flash擦写。这步有两个反直觉的规矩，必须先记住。

规矩一：Flash写之前必须先擦除。Flash的特性是只能把1写成0，想把0变回1只能擦除。而且擦除不是按字节来的，是按扇区/页来的——STM32F103一页1KB，F4系列一个扇区16KB起步，不同芯片粒度完全不同。你只改了一个字节，也得把整页擦了重写。擦除粒度这个参数在写Bootloader时必须查芯片手册确认，写错了轻则效率低，重则擦到别的区域。

规矩二：写Flash期间不能跑Flash里的代码。Bootloader自己就住在Flash里，擦写APP区时它自己在别的区域执行倒没事，但如果你把代码放到要擦的扇区（比如中断处理函数），一擦就全乱。这就是为什么很多Boot会把关键代码拷到RAM里跑，或者严格保证代码区和擦写区不重叠。

再就是写保护。芯片Flash有读保护和写保护机制，量产车机上一般会把Boot区设成写保护，防止固件被意外擦掉或被人篡改。保护是双刃剑：保护没配好，升级时发现自己擦不动自己的Boot区，板子直接变砖；保护配好了，又能挡住绝大多数手贱操作。

固件写完，校验这道关卡才是保命的。上位机传数据可能出错（线松、干扰、速度不匹配），所以Boot必须确认收到的和发的一样才敢跳转。最常用的是CRC32：上位机把整个固件算出一个32位校验值，追加在固件尾部一起发；Boot收完后对全部数据重新算一遍CRC，和收到的校验值比对，一致才跳APP。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAkLPzEibP2OiaHNn88wZZPTZpeUcy6mfzuESBR3AGDOAibYDIvYEtrNja130iaiboHciaE31AuAaBrPxly2g0L2YhYkLwN2puKqjicYQ/640?wx_fmt=png&from=appmsg)

这里有个工程上很重要的设计取舍：是边收边写APP区，还是先暂存到备份区、全部校验通过再搬进APP区？边收边写省Flash，但一旦传输中途出错，APP区已经被写了一半，板子就没法启动了；先暂存再校验，Flash成本翻倍，但安全性大幅提升——校验不过就丢弃，旧固件一点没动。量产工具大多边收边写靠协议兜底，车机OTA几乎都是暂存校验的路子，因为车不能刷一半就趴窝。

校验除了CRC，还有一道读回比对（Read Back Verify）：写完Flash之后，Boot把刚写的内容读出来，和接收缓冲区里的原始数据逐字节比对，防止Flash写入本身出错（比如写保护没关干净、电压波动导致写入不完整）。CRC是数据传没传对，读回比对是写没写进去，两道关卡各管一摊，车规刷写基本两个都要。预算紧张时读回比对可以抽样做，比如只比对每页首尾几个字节，但全量比对最稳妥。

再提醒一个擦写时的掉电问题：刷写过程中突然断电，APP区可能处于半擦半写的状态。轻则下次启动校验不过、停在Boot等重刷，重则连带损坏相邻扇区。所以升级流程里要设计刷写中掉电可恢复：要么靠A/B分区兜底（下面Part 04讲），要么Boot每次启动先检查APP完整性，发现坏了就自动进升级模式，而不是傻乎乎跳转死机。

**04**

**安全启动与A/B分区：OTA的保命设计**

讲到这儿，Bootloader已经能刷固件了，但离车规还差两件大事：安全和可回滚。

先说安全。你想想，如果攻击者伪造一个固件发给车机，Bootloader傻乎乎地收下、擦写、跳转，这车就成别人的了。所以车规Bootloader要安全启动：固件发布时用私钥对固件签名（对固件算SHA-256摘要，再用私钥加密摘要形成签名），Bootloader端用预置的公钥验签，验不过就拒绝执行。签名验证保证固件没被篡改且来源可信。

更讲究的是信任链：芯片出厂固化一段BootROM（一级Boot，不可改），它验证二级Bootloader的签名，二级Bootloader再验证APP的签名，一级验一级，层层传导。私钥放在哪也有讲究，高端芯片有HSM（硬件安全模块），验签和密钥操作在独立的安全岛里完成，就算应用层被攻破，也偷不到密钥。这部分水很深，转行的朋友先建立概念，细节等真正做安全启动项目时再抠。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCibQUVp08p67tFp6uOYAIMyqhqtnuIjOeOvPiaMzyjRtlJeo5BgxkTRQnT1gF3XpXtn7vowfBx6tnTWZiapJAVDSGibx6dKrDDG5U/640?wx_fmt=png&from=appmsg)

顺带说个安全启动的实践细节：验签算法有RSA和ECC两大流派，RSA实现简单、兼容性好，ECC密钥短、计算快，车规芯片大多两个都支持。签名的不是固件本身，而是固件的哈希摘要——先对固件算SHA-256，再对摘要签名，Boot端先自己算一遍摘要，再用公钥解签名比对。这样签名长度固定，验签也快。还有安全启动和Flash写保护的配合：Boot区的写保护+读保护一起开，既能防止固件被篡改，也能防止别人把Flash读出来逆向。安全这块，方案没有绝对的对错，只有攻击成本高不高，要按车型定位和法规要求来定。

再说可回滚。OTA最怕的不是升级失败，而是升级失败后设备变砖。A/B分区就是干这个的：Flash里放两份APP，Bootloader只从当前生效区启动。升级时往非生效区写，写完后置一个切换标志，重启后Bootloader发现标志，从新分区启动；新固件跑起来自检通过，标志确认生效；自检不过，自动回滚到旧分区继续跑。用户感知就是重启了一下，完全不知道升级过。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCTReQicuW4jGafww9e44uD182Q1JicLUZibucaeeL6vcNMicNTPibpJibF0ezmtAZe42a9EOXAGHOVIcFmdWl90Y8uQ5ibgyxF1ibjT8I/640?wx_fmt=png&from=appmsg)

汽车电子圈还有个专属玩法叫Bank交换，瑞萨RH850这类芯片支持双Bank硬件切换：两个Bank的代码在运行时可以整块交换映射，一条硬件指令完成分区切换，比纯软件改标志快得多、也安全得多。A/B分区和Bank交换本质都是双区备份+切换+回滚的思想，只是实现层级不同。开源项目里，mOTA是个不错的参考实现，基于STM32做了A/B分区加各种传输方式，想动手的可以拉下来读代码，比自己闭门造车快。

说句大实话，回滚设计比升级本身还重要。新固件上线，Bug率不会因为OTA就变成零，反而因为更新频繁更容易出问题。一套成熟的回滚机制要回答三个问题：什么算新固件跑坏了（启动超时、自检失败、应用崩溃重启），什么时候触发回滚（连续N次启动失败就回滚），回滚本身会不会失败（回滚也要校验）。这几个问题想清楚，OTA才算闭环。很多公司上线OTA第一天就翻车，不是升级链路的问题，是回滚策略没设计好。

最后补一个量产相关的实用技巧：Bootloader和APP合并成一个固件。产线上如果分两次烧录Boot和App，效率低还容易出错，所以通常用脚本把两个bin拼成一个文件，一次烧完。bin文件不带地址信息，需要按芯片起始地址转成hex（工具如srec\_cat可以干这活），也可以顺手把设备参数、标定数据一起拼进去，一次写入。这条经验对做量产支持的人很值钱，能省下大量产线时间。

把整条OTA链路拉通了看：云端下发固件包 → 网关或T-Box接收存储 → 通过CAN或以太网逐ECU分发 → 各ECU的Bootloader执行刷写 → 上报刷写结果。车上有几十个ECU，升级策略是整包分发还是差分升级（只传改动部分）、逐个升级还是分组升级（防止整车一起断电、一起变砖）、升级失败是回滚还是重试，都是架构级决策。新手进这个领域，先抓住一个ECU的Bootloader刷写闭环，再往外看整车调度，节奏就对了。

给想动手的朋友一个落地路径：拿一块STM32开发板，Boot占前16KB、APP从0x08004000开始，先把跳转函数跑通；再用串口做一版带帧头、命令字、CRC的刷写协议，用PC工具发固件；最后加上A/B双区切换和回滚标志，一套入门级OTA就成型了。开源参考可以看mOTA这类组件，重点是先读代码理解设计，再自己重写一遍，光看不写等于没学。

来源：从零学嵌入式

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt...