---
title: GPIO的8种模式你知道几种？
url: https://mp.weixin.qq.com/s/2jIhl3SurefbFZFqtcY7oA
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:40:00.836466
---

# GPIO的8种模式你知道几种？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ajPz2rZHFU67EEMeTX5yQqFaIxKDmTjPiaUvQ67IJibcQHwANNyPCZtjzrIXod1eovYaLa3kO0ibq57bPpRDJenVg/0?wx_fmt=jpeg)

# GPIO的8种模式你知道几种？

谈思实验室

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

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571424&idx=3&sn=06a2de166c8d828d40fe379a99129609&scene=21#wechat_redirect)

嵌入式系统中最常用的就是GPIO通用输入输出口，比如检测1个按键按下，控制1个LED点亮等都是通过GPIO实现的。

GPIO从名字上可以看出它可以作为输入也可以作为输出，输入和输出只是它最基本的分类，其实根据输入、输出的不同特性，它还可以细分为8种模式，今天我们就一起来看看具体有哪些模式。

**01**

**输入内部结构**

GPIO的输入和输出相对独立，我们先学习下输入部分，在了解输入的相关模式前，我们先要了解下输入的内部结构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC6qHYCEHHV1C6gmJsqnu6GAjEibMgzPIjwVeSd7F9WNy11BHXRHibW4Gq2D0kuXWrRRJaxQdqJRPhFsTQiayaSRdwOEthZKA6nV0/640?wx_fmt=png&from=appmsg)

输入内部结构图

如上图所示，GPIO引脚的内部首先会有两个保护二极管分别接到电源VDD和地VSS，这两个二极管的作用是对输入的电压信号进行过压保护和负压保护。

假如主芯片的工作电压VDD是3.3V，如果外部输入了1个超过3.3V的高电平过压信号5V，这个5V就会使上面的二极管D1导通，D1导通后，由于D1（硅管）的压降是0.7V，所以I/O引脚的电压就会被钳位在3.3+0.7=4V。

输入低电平时，正常的低电平信号是0V，如果外部输入了1个低于0V的负压信号-1.5V，这个-1.5V就会使下面的二极管D2导通，D2导通后，同样由于D2的压降也是0.7V，所以I/O引脚的电压就会被钳位在0-0.7=-0.7V。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAYncbzjLEBMTEmnBPk8nP2ebUdsqcXJ1tXGV6321oThwz8xptLJukGYuwYibx3JqNiayfqicZLtq8fNQUNl5Kziba5b7m0vloF3yc/640?wx_fmt=png&from=appmsg)

过压（D1）和负压(D2)保护二极管

也就是说，这两个保护二极管把外部输入的电压从原始范围-1.5V~5V钳制在了-0.7V~4V的更窄更安全的范围，这样可以防止过压或负压损坏内部电路。

引脚通过保护二极管之后会接入上拉和下拉电阻，然后接入1个TTL施密特触发器，施密特触发器输出给输入数据寄存器，CPU就可以读取这个寄存器得到输入信号值。

施密特触发器的输入端又引出一条线，连接到模拟输入；

施密特触发器的输出端也引出一条线，连接到复用功能输入；

这里我们主要介绍下施密特触发器，施密特触发器的基本原理源于电压比较器，普通的电压比较器是单限比较器：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBa50wL3JLCLoUYJOhF4qAKQGPN6ABgyr2nVCm31icJD3D7pOjC3TBU8EricpsZGOcqKlp028Ur60I5bSR19zibNW7BSyaexoMjmc/640?wx_fmt=png&from=appmsg)

电压比较器-单限比较器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBv27cK0J4oE7Vyujsqliahe2dkNVDgCRQtu0TwvTG5Qjg2ibcxLXmT7cbEovFSib9Pmr76sf9T5Okcpjnv8WAibeQMpXOaWd14iadQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAFf8CPIDHoYch4AC8jIW84ibUdawfSZHUGs71I6ZGgXW4AWCJUFUE91IArS570qlYibKzo1xA5UMBuAdtjJ0kMtY5bLOfuYTibPE/640?wx_fmt=png&from=appmsg)

线性信号的波形转换

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBoYgwmGdpqbiceuL1fofVKWSOr4ZibniabNnQnLPuuFOWKs5lCvbibnAWNhibSWO75KibS8cFXLrxMfYwoteReibhtYXW0GS172fTgyw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDfsEWxeRq3S5LNFicSI6D48JHf4HBxAzTVNFrfegJGBLXgicHA6P2DDemdmO8HyOTKiaPqmRwpdSHOTwaDMN5WNy84iceDxibaMCfo/640?wx_fmt=png&from=appmsg)

施密特触发器波形图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDzxXkstElicmwZS9vbl1dyXiabtXBrdjHCdVOlJS6dO6mhSN0qMZq5Hy3Kch1XBu5ZQkcPp1mMPUQlic04ibAhibkZlkwkPibzpo82U/640?wx_fmt=png&from=appmsg)

施密特触发器本质上是一种滞回电压比较器，有了施密特触发器，使得芯片的GPIO口在采样数字信号时，能有效抑制噪声干扰，避免因信号微小波动引起的误触发，显著提升了采样时的抗干扰能力。

**1.1输入浮空**

浮空模式是输入模式的一种，浮空的特点就是内部输入端没有上拉和下拉电阻，外部信号直接进入施密特触发器，经过施密特触发器转换后再进入输入数据寄存器。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBNoVXTYOTSjrEHFv33NPQIMEnFCj5icbYVS28Wic6nwStiaZJps79QYCI9zJRSibZeiav807icHjh3DfeiaiaZnK1f3A9EGaVVImrhG4s/640?wx_fmt=png&from=appmsg)

浮空模式示例

浮空模式适合那些本身具有强驱动能力或已设置上/下拉的外部信号源，这些信号由外部设备主动驱动，电平变化明确，浮空输入能避免内部电阻对信号的干扰，确保接收的纯净性。

浮空输入在实际中应用的很少，因为大多数的‌按键、开关等无源器件都是一端悬空，一端上拉或下拉；如果使用浮空模式，当按键未按下时，引脚会处于“浮空”状态，电平不确定，极易受电磁干扰导致误触发。

**1.2 输入上拉**

输入上拉模式很容易理解，就是输入端内部接上拉电阻，不接下拉电阻。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBic1z8L6oSQ4OfQPrAZ42recsKFiaO4d8Aw5NcFSzibMov1GA1YQIiaicaeic1s7t7Ovpxkr7eibTCavxqaY5P7F8zzVFu2tlO5qZoP4/640?wx_fmt=png&from=appmsg)

输入上拉示例

这种模式平时会将引脚内部上“拉”至高电平（VDD），当外部信号将引脚拉低时，MCU即可检测到明确的下降沿或低电平状态。这种模式适合用于检测‌需要默认保持高电平、并以低电平作为有效触发信号‌的输入场景。比如接地型的按键或低有效的开关信号。

**1.3输入下拉**

输入下拉模式与上拉相对应，就是内部输入端接下拉电阻，不接上拉电阻。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBpA3g2pzsYHf2zufn2VcT0F6CsiammSjnuIrDo6mH9KB8iaic5zbick4sh0KAuVOVcS7TtwAMIT8ibtyAnsjFT7jONWyqrD0HicjeMo/640?wx_fmt=png&from=appmsg)

下拉模式示例

下拉模式适合接电源型的按键或高电平有效的开关信号。

**1.4模拟输入模式**

模拟输入模式是用于外部信号为模拟量时的采样，此时输入端内部不能接上下拉电阻，施密特触发器关闭，信号在施密特触发器之前就被输送到芯片内部的ADC模块进行转换。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAhmZrPYVWTmNwHL6QMNf3WkkvmlCo6uHI7hMNs4v90Oh8U9VGaUAvhVspl9dLkynut8xSFJyFUgxgKBtbkKFY7ib5sPDQ64cCA/640?wx_fmt=png&from=appmsg)

模拟输入示例

模拟输入模式适合需要采集‌连续变化的模拟信号‌的场景，比如电池电压的检测、温度、湿度、压力传感器信号的检测。

**02**

**输出内部结构**

上面介绍了输入相关的模式，输入输出虽然相对独立，但是由于它们最终是连接在同一个IO引脚上，所以它们之间也是有一定联系的。

比如CPU输出数据时，可以通过输入寄存器再读取这个电平；而输入采样时是要禁止输出的，否则内部输出会影响外部信号的采样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCupoOiafZ01MfFAJXib0Xaibvpw3JIvibviaoiazMcEyx5ujeYKhKqAdXAk9uXs9uW1WWHtEqZqgw0YRf1usxqCib1j6cXwgmGkRqK9I/640?wx_fmt=png&from=appmsg)

GPIO模块框图-黄框内为输出部分

上图是GPIO的整体框图，上面是输入部分，跟之前的介绍是一样的，下面是输出部分。

输出的过程是CPU将数据写入输出数据寄存器，输出数据寄存器将数据传送到输出控制电路，输出控制电路通过控制P-MOS和N-MOS的通断，决定输出的电平高低。

**2.1开漏输出**

开漏输出就是保持P-MOS一直断开，只通过控制N-MOS开关进行输出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCSiboKz1LGqt9Lp1U1Jct16Tzo9AzdjibsugVOu7iaNKHlTatNFicC0j6Q5H3DvgaJ0cfp7uGdftOTQibwLr0c88ORDFVSahP1GsjI/640?wx_fmt=png&from=appmsg)

开漏输出示例

开漏输出适合低电平驱动的电路，比如驱动LED点亮。

**2.2推挽式输出**

推挽式输出就是通过分别控制P-MOS和N-MOS的导通来达到输出高低电平的能力。

推挽输出能提供足够的‌拉电流‌（从IO口流出电流）和‌灌电流‌（电流流入IO口），非常适合直接驱动需要明确高低电平控制的数字器件。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaD0SicVLjNx1qGZ7fIw812LTqCdCpNAZ0bnFwF50caGFFEjiba9iawicrb4n1Qv3nkOctNAKicTY8e8eyibwBnsjic9ic7DGOq7Uib4WyXo/640?wx_fmt=png&from=appmsg)

推挽输出示例

当需要MCU引脚作为‌强输出‌，且‌无需电平转换‌或‌线与逻辑‌时，推挽输出是首选，比如控制数码管段选/位选、驱动晶体管或MOS管的栅极等。

**2.3推挽式复用功能输出**

推挽式复用功能的输出原理跟普通推挽式输出是一样，只不过它的信号来自片上外设，不是输出数据寄存器控制。

芯片为了提高引脚的利用率，通常会设计为多种功能共用1个引脚，所以引脚除了通用的IO功能，还可以配置为其他的功能，比如IO可以和UART、AD、TIM共用引脚。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDdZ0XWiaGacw9j64PaAlMzYeXLk59O84Fa9OPXJajsTNZOuWDp8yD7txmSa5AeZOssdoz27m9rXWrpOmhlX87tQr3KAK5WsroA/640?wx_fmt=png&from=appmsg)

推挽式复用功能

推挽式复用功能主要用于将GPIO引脚配置为由内部外设模块自动控制输出信号，而非由用户程序直接控制电平。这种模式适用于需要高速、稳定且由硬件自动处理的数字信号输出场景。比如UART、SPI、定时器PWM、USB、CAN通信等等。

**2.4开漏复用功能输出**

开漏复用功能输出原理跟普通开漏输出也是一样的，只不过它的信号来自片上外设，不是输出数据寄存器控制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBACF2H92miaXOBqtSeibbPOJE2WSGNQJibnkARaJp4uy4gbibHDASjk2o2MIHV2FAqZlk8fFG1Vj8ZQbgcLSUP1aydWHyPEHoWojk/640?wx_fmt=png&from=appmsg)

开漏复用功能模式可以用于需要支持线与逻辑的通信，比如I2C等。

**03**

**小结**

主芯片GPIO的常用8种模式包括输入浮空、输入上拉、输入下拉、模拟输入、开漏输出、推挽式输出、推挽式复用功能输出和开漏复用功能输出，可以通过寄存器根据不同场景的需要灵活设置。

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=j...