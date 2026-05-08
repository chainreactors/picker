---
title: 独立看门狗与窗口看门狗有什么区别？
url: https://mp.weixin.qq.com/s/HC9wScz8kAnF7E8EoeeiOw
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:55:08.325511
---

# 独立看门狗与窗口看门狗有什么区别？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6MmZYM3RhXdaKtPK2EgLgXibM7WVrRxOBBp0dvpicUoZiaEIibhye1DEuibllwatxMVibEOZYZClONsStIEeCVE5eoKHnkAsia5YibjtqGBRnjyazeM/0?wx_fmt=jpeg)

# 独立看门狗与窗口看门狗有什么区别？

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于汽车电控知识
，作者安己乐人

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6j5af2Q2k1xdAVsogZDicBJA7ibwvcRA8UDSp3GKThzmZw/0)

**汽车电控知识**
.

快乐学习汽车ECU知识、轻松进入汽车电子行业！

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572731&idx=2&sn=c138b1b1bce7ef6c8f8d8b93df959bcd&scene=21#wechat_redirect)

看门狗按照功能特性可以分为独立看门狗和窗口看门狗，今天我们学习下两种看门狗的工作原理，看看这两种看门狗有什么区别？

**01**

**独立看门狗IWDG**

独立看门狗的基本原理并不复杂，以STM32为例，就是在看门狗模块的内部有1个12位的计数器，计数器有个初值，启动看门狗后，这个计数器就会开始递减运行，也就是按照一定的时钟频率自动减1，当数值减为0时就会产生复位。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDB5GQ3y4ed8v4xlaVz0kKLqMDnqT85d2jPgNjClb0SkfatHX8HrgjFImX85EVUu2iceibuZic8IPxy0fvRMW0ibD96hmWSzl8ezOw/640?wx_fmt=png&from=appmsg)

独立看门狗框图

如上面框图所示，自左向右，先通过预分频寄存器设置好看门狗要使用的时钟频率，比如分频系数为4，则计数器时钟频率=40kHz/4 =10kHz。

再通过重装载寄存器设置好12位重装载数值，比如数值=0x3E7=999；则复位周期=（999+1）\*（1/10kHz）=1000\*0.1ms=100ms。

然后启动看门狗，12位的递减计数器就开始运行减1了，运行期间需要通过键寄存器定期喂狗（写入固定值0xAAAA）,这个键寄存器就是控制寄存器，如果超过100ms还没有喂狗，12位的递减计数器减为0就会复位。

看门狗工作期间还可以通过状态寄存器查看预分频和重装载值是否更新完成。

这里有个问题，就是这个看门狗为什么称为“独立”看门狗呢？这个“独立”是从何而来呢？

它的独立性主要来自以下两个方面：

**1.1时钟独立性**

独立看门狗(IWDG)由内部的低速时钟(LSI)驱动，而系统运行的主时钟是外部高速时钟HSI或内部高速时钟HSE。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBn87aLftbCbhVpHPibyxN7Je0SqMDtLdsO99u8nyYxI7hHqq3coMLk3dibI0W4TXqRqBgeJsrvQMIY8krSgkofDZ6S7K7wicxVE0/640?wx_fmt=png&from=appmsg)

时钟源框图

由上面框图可知，LSI与其它时钟是完全独立的，所以即使主时钟HSI或HSE发生故障，系统运行异常，独立看门狗模块也会正常运行，计数器的自减功能仍然有效，需要复位的时候还是可以复位的。

但是这里的时钟也有1个缺点，就是内部时钟LSI使用的是RC振荡器，它的精度偏低，适用于对时序要求不高的场景。

**1.2电源独立性**

从电源框图中还可以看出，独立看门狗的寄存器位于1.8V供电区，而分频器、计数器和重装载数值等功能都位于VDD供电区。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaARh3BOEfg6K4Mq7D3fiaaCIhxyGbcXWmu8SMs37Ioib0tfIS1boYibLfvyVYjK9iaUeTlB9zibqakSmz0HlF3ogILXJfbCM4bGLEibE/640?wx_fmt=png&from=appmsg)

VDD供电区

这样设计的原因是MCU在低功耗的standby模式中会关闭1.8V供电区，而VDD供电区是一直保留的。

另外，虽然图中显示寄存器位于1.8V供电区，但是实际上看门狗的核心寄存器属于备份域，备份域是由 ‌VBAT引脚‌或内部 LSE/LSI 时钟电路直接供电，‌独立于主VDD和1.8V内核域。

Standby待机模式下‌，虽然1.8V内核供电域被‌完全切断‌，SRAM和通用寄存器内容丢失，但‌备份域（包括 RTC、备份寄存器和 IWDG 寄存器）仍由VBAT保持供电‌。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDibewKvl8yiaR9vFzN4sYSNLjcDAzKrSTAicC4nKDhOJCDtvhmYZ5CG6kbfxVibmnfT2qyPGicJsYXX7KFXaql9Tp2hnfSRgSelkqY/640?wx_fmt=png&from=appmsg)

三种低功耗模式

所以这样设计的结果是看门狗不仅在MCU正常运行时可以工作，在低功耗模式中，包括最严苛的standby模式下也可以工作。

**02**

**窗口看门狗**

独立看门狗的主要特点是有1个喂狗的最晚时间限值，超过了这个时间限值就会复位，也就是喂狗不能太慢。

而窗口看门狗的特点是有两个时间限值，除了这个最晚的时间限值，还有1个最早的时间限值，也就是喂狗既不能太慢也不能太快。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDaKm3tmxuct9SBM2g5JcobYH9SQxR7UphiaGH2F3xqPl102Tmtbh2ry3RGWw0ovHDS0tyG4uyztPra3AQuiaqibf2XWuZcicbE9Ac/640?wx_fmt=png&from=appmsg)

窗口看门狗框图

如上图所示，窗口看门狗的工作原理与独立看门狗有些不同，首先是时钟来源不同，独立看门狗的时钟来自内部低速时钟LSI（固定频率40kHz）。而窗口看门狗的时钟来自PCLK1。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA5vdnyttic0tXYfvFglsxPjUiaukIHicmTu5xFwic3ia4RVhwRAFvlzWTo3DCprfKfRmRudwNZJGQB5RlMRkznAhadAZI2v72ZqGgs/640?wx_fmt=png&from=appmsg)

系统时钟分配

由上图可知，PCLK1是来自于高速总线时钟HCLK，而HCLK又是来自于系统时钟SYS CLK，PCLK1的最大频率是36MHz，比内部低速时钟LSI(40kHz)要高很多。

PCLK1的特点是频率很高，精度也很高，但是它的缺点是并不独立，依赖于系统时钟。

所以在有些低功耗模式（如 Stop/Standby）中，当主时钟关闭时，窗口看门狗WWDG无法正常运行；

窗口看门狗的递减计数器是6位（T0-T5），位数比独立看门狗少了一半。当计数器值从0x40翻转到0x3F，也就是T6从1变为0时，产生一个复位。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCpPa8aOhBbUFz7LPUdfOicw1ZxS2LUeScxHNyP9NiaP2yE1YxmebHK0qZWAFpFjfxOiaUtjm1mCtA0ib6o40ktxA6WBqYSSXlQwt4/640?wx_fmt=png&from=appmsg)

T6清零时复位

如面框图所示，递减计数器减到T6为0时会产生复位，这里要注意的是，递减计数器不是在看门狗启动时递减的，而是一直处于自由运行状态，如果计数器运行到快复位时刚好看门狗被启用，启用后就会立即产生一个复位。

为了防止这种现象，看门狗被启用时，必须先将T6置1。

程序在正常运行过程中必须定期地写入WWDG\_CR寄存器以防止MCU发生复位。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCt8kd6pb09nic0ACRZibIcl9zTqu6Cic9tXs9BEKtmXkxmVBx3ADH4RpzdF5uWTmmgCUPicYicyBPSqdrqciblIzR3jajWiarUM2RAibk/640?wx_fmt=png&from=appmsg)

窗口看门狗时序图

如上图所示，递减计数器T[6:0]从大到小递减运算，假设是从0x7F开始递减，如果窗口寄存器W[6:0]=0x70,那么在0x7F减到0x70之间是不能喂狗的，也就是不允许刷新，刷新会产生复位，配置寄存器(WWDG\_CFR)中包含窗口的上限值。

在0x70~0x3F区间是可以喂狗的，这个区间就是刷新窗口，如果刷新窗口没有喂狗，等到计数器等于0x3F时，看门狗就会产生复位。

要避免产生复位，递减计数器T必须在其值小于窗口寄存器的数值W并且大于0x3F时被重新装载。

**03**

**超时时间**

独立看门狗只有1个“超时时间”，窗口看门狗也有“超时时间”，只是多了1个“窗口时间”。两者在“超时时间”的原理上虽然一样，但是具体的参数差异却很大。

独立看门狗的时钟来自内部低速时钟LSI，频率固定是40kHz，所以计数器间隔时间长，超时时间TIWGD以ms为单位的计算公式如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaB7ebBicpmG5rW11ZwWG9GRKOWsiaP9Ria7So2PqUMCZ3wdWA5Ra5Rk3HuLe3icdDVqbQFeo2iaSR3va0N8icOEiaKc5MDLEf4ibXy8mFk/640?wx_fmt=png&from=appmsg)

根据计算公式可以得到如下的超时时间范围。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCXKERlHFAExIvHEyoaB2xwk2vo613vCnsX0OAaiaNh3MWWx2OQl9K1Rwgj1ChpsYFsvj9Q8vrfjJFyWwXFSXW5XM2ic5K24VWlQ/640?wx_fmt=png&from=appmsg)

独立看门狗超时时间

由上表可知，独立看门狗的超时时间范围很广，从0.1ms~26214.4ms。

而窗口看门狗的时钟来自PCLK1，频率随指着系统时钟可变，但是频率通常很高，所以计数器的间隔短，它的计算公式如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBRUOzTL5kBicQwYCAyCLR5wpQgXXbnyn26mZvIBkvZDMQKbJNnev5iaI4QdMFY8nicVTXGuW0Eiagxxa8K6NzwhUeB9A7aShuh70c/640?wx_fmt=png&from=appmsg)

注意，PCLK1常用的频率是36MHz，由于这个频率太高，所以进入窗口看门狗模块前会先按固定的4096分频，然后再通过WDGTB进一步分频。根据上面公式，以常用的36MHz为例计算如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBeNB8pzmkb6EXtjVJkxx6KAEaxic0Vfb4ibusEibTf9XrDiclDKa3YAMsfiadN2HdG4n571MA1UgSbGH1yg7NjA9cXgnvmcFiao2s48/640?wx_fmt=png&from=appmsg)

窗口看门狗超时时间

由上表可知，窗口看门狗的超时时间范围很窄，从113us~58.25ms。尤其是最大值58.25ms,这个时间很短，远远的短于独立看门狗的26214.4ms，也就是26s。

所以有些任务很长时不适合用窗口看门狗，比如Flash 擦写可能耗时数十甚至数百毫秒容易触发 WWDG 超时复位‌。

**04**

**软件示例**

下面通过两个示例来看下软件的执行过程。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBgGzyIUWyt3icV2dxaPUMqYKW8htgUuNo8Jibmgd2XOzacJjWd79fWhLVTTqk86iarERT7FoY03sic8L4dCk80GzTtRTycje8lvH4/640?wx_fmt=png&from=appmsg)

独立看门狗示例

上面是独立看门狗的软件示例，STM32独立看门狗的各种控制指令都是通过对键寄存器IWDG\_KR的操作完成的。

首先独立看门狗为了更安全，预分频寄存器IWDG\_PR 和重装载寄存器IWDG\_RLR 具有写保护功能。

要修改这两个寄存器的值，必须先向键寄存器 IWDG\_KR中写入0x5555。所以第一行代码是先解除寄存器的写保护。

然后设置预分频值IWDG\_PR 为16，由于重装载寄存器IWDG\_RLR为2499，根据独立看门狗的超时时间计算公式：

计算结果为:

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCHjFuTYy1leJpILEQbe4EJDibES8gkNt2MJfPf1BrSf7MIC6vMjlfB5Lm4teygK67CvMJ9zFuZynaa9wNv8WJS4npudlsKFYOI/640?wx_fmt=png&from=appmsg)

设置后先重新加载一次计数值，在键寄存器IWDG\_KR中写入0xAAAA，将IWDG\_RLR中的值2499加载到计数器。

然后在键寄存器IWDG\_KR中写入0xCCCC，开始启用独立看门狗；此时计数器开始递减计数，当计数器计数到末尾0x000时，就会产生一个复位信号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDHNWJ4Ticib0xWbPgfkeWpS8FDDk9mZribMJoTWEyTEDKGFIQG8Zul1yamYuFIEtUxg3cNoIoKJ4C4ZtVaTNb389xI7hqGwiawIM8/640?wx_fmt=png&from=appmsg)

窗口看门狗示例

上面是窗口看门狗的软件示例，窗口看门狗的时钟不是独立的，是来自于APB1总线的时钟PCLK1，所以首先要使能APB1的时钟。

然后设置预分频值为8，注意这里的超时计数器值是在最后一行代码的启动看门狗函数中设置的，数值为54，所以根据超时时间的计算公式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDaiaqgSlMxSP7fkSIBuQXiabgj6TZAxqmxCZYVUK4Acfg54g9O2T4pHOde0rT3eibJt59tLhO3V45XZiaBKxsERgpJ8p6SZjOcxK4/640?wx_fmt=png&from=appmsg)

计算结果为：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBa58hxQtBvErNib9fhnfoacuUdv8icdw3QwV8Gvab3kxCCUkS2sEWYxJVKsdMibs57v50wwwRFYDRxxhVJTpsAZHZEK6Bmt8qgibs/640?wx_fmt=png&from=appmsg)

再根据窗口时间的计算公式：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCqibBxMjVk7l3sHsjibefALb6nd4YevxLoz4YWtRpNX84A7n0uNmqXKPjoUCENvZvtwzEaF2VLSKVgPf9Mty5A8Ek8IZWgKmQibw/640?wx_fmt=png&from=appmsg)

计算结果为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAUfIlaZicBIkzypSMSibcgjFeETZpEIfKnwZYibbic5zjgkBmdOjFCwZhl3xr61CIjlEu7R1AjWEQCNpYLNueVHcK5aibiaRoW0IXvY/640?wx_fmt=png&from=appmsg)

所以窗口看门狗的喂狗时间是在20-50ms之间，在这个范围之外喂狗都会发出复位信号。

**05**

**小结**

独立看门狗的时钟和电源独立性强，能够完全独立工作，在各种模式中都可以运行，通用性强，适合对时间精度要求不高的大部分场景。

窗口看门狗的时间精度高，但是超时时间较短，某些低功耗模式下不能使用，通用性弱一些，更适合‌实时性要求高、需严格监控程序执行节奏‌的特定场景，如电机控制、通信协议栈等。

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mi...