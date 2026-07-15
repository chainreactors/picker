---
title: OBD诊断协议
url: https://mp.weixin.qq.com/s/Z9p7wefVKXLP38Tqc8g5tg
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:43:34.071434
---

# OBD诊断协议

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBRWAupBERKGvrVplfiaA3mUXwrrcLgyder6gaRZsdCuibiaQ6Z3DZs4SbNzhZGenp1CEwLwRJibIB0OIxIWopxDPPxrohfAKo5IKM/0?wx_fmt=jpeg)

# OBD诊断协议

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

**硬件**

硬件比较简单，就2行8列16个口/引脚，实物长这样。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQuoSWcSgbA7FUZh6MiaM2aSKTW6nKeQyEBbHGCPO9eJLelflvPeVibUyg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

具体引脚的功能

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQwCCIk9udQZw0RVicJBQwr2zaCL0S20QXcicedr5SklicgtWOlrRZkMcrg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

1    Reserved

2    SAE J1850 总线的正线

3    Reserved

4    底盘地

5    信号地

6    CAN\_H

7    K线

8    Reserved

9    Reserved

10    SAE J1850 总线的负线

11    Reserved

12    Reserved

13    Reserved

14    CAN\_L Can

15    L线

16    电池电压

所以我们看到里面最重要的就是两条CAN线，一半我们也是重点关注这两条线。

**服务的总体介绍**

有以下几个服务，其中0x05已经删除了，因为0x06就能完全包含。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQqaNC9ib5lRnLW6vdd9WSk81Ovs3ckDWq7p31PrPBZMQtMStNlgCMdZw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**读取动力系统当前诊断相关数据(0x01)服务**

根据PID读取对应排放相关的当前数据，包括：模拟输入/输出数据数字输入/输出数据，系统状态信息。

要求必须是实际读取的值，非默认值或替代值。

里面定义了一种像DID一样的参数，叫PID，并不要求把这些参数都实现，可以支持部分PID就行。但是有一点，所有支持OBD标准的ECU都必须支持0x01，PID=0x00的服务，其它PID不做强制要求。

部分PID的作用是查询其他PID是否支持，譬如0x00,0x20,0x40,0x60...0xE0，我们称为查询PID，表示查询ECU对其它PID支持信息回复数据4字节32位，依次对应ECU对其后32个PID支持信息。举几个例子：

PID 0x00 用于查询（0x01~0x20）之间支持的PID参数

PID 0x20 用于查询（0x21~0x40）之间支持的PID参数

PID 0x40 用于查询 （0x41~0x60）之间支持的PID参数

……

后面一样一直到0xE0。

被支持的PID我们称为数据PID。

所以一般诊断的流程分两步：

1、先发送查询PID，看看是否支持我们想要的查询的数据PID。

2、根据接收到的支持PID结果，再发送想要的查询的数据PID。

**请求报文要求**

最多可以包含六个PID

在同一条请求报文中，可以重复出现同一个PID，但是不能同时出现查询PID不能和数据PID。

**响应报文要求**

ECU支持最多6个PID的请求

如果同一条请求当中，重复出现同一个PID，就当作多个处理。

响应报文中PID的顺序不要求同于在请求报文中的顺序，譬如请求时候是12345，响应的时候可以是54321。

**查询PID举例**

请求报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQmXWJANQoYkDHiaCJdG9Xy1b5TYLuv2ibjExFeBk23T4DsVj4PdicibA5Fw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

响应报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQT9X0ibbsJGDl0ibiccibH7p2emicOibGR74gCUjTMdlBVsiaf6iaklgr9jTiaog/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

**数据PID举例**

请求报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQSmKicsF648vCOqpZvLjic5IWf5sLUcOT7iaaR1ukueAaZUmHBVbGLUkiaw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

响应报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQqQpAFLldDDr7gOCS21W9DXbJthtFUkIgGXl6cYHayHKpt4Al6DHnVQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

在这里大家可以看出，相应的顺序不一定要跟请求的一样，而且每个PID具体数据长度是双方约定好的。

**读取动力系统冻结帧数据(0x02)服务**

跟UDS协议里面的冻结帧是一样的作用，这个服务也有查询PID，在0x02服务里面，PID就是冻结帧的ID。规定PID=0x02返回的是引起冻结帧数据的DTC，如果ECU中没有冻结帧数据，那么返回的DTC=0x00。OBD协议的DTC比较短，只有2个字节，例子如下。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQArzTQaulgkFAY7HgyoqNWr0XxVOkibxaYuamusWusLeqGAG3Khlkzfw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

**请求报文要求**

最多可以包含3个PID

在同一条请求报文中，可以重复出现同一个PID，但是不能同时出现查询PID不能和数据PID。

**响应报文要求**

ECU支持最多3个PID

如果同一条请求当中，重复出现同一个PID，就当作多个处理。

响应报文中PID的顺序不要求同于在请求报文中的顺序，譬如请求时候是12345，响应的时候可以是54321。

**查询PID举例**

请求报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQ5zibKXdInMib6gCDDOHQP2ia7Wcbic5RYKqshw7L5YicZp6Vq6wDkibhHASg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

响应报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQIbkIBwqTFbZy6juy6FmqWnDwVdT37Gw2Yr4AvN2qID5PjbYtQD6eHw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

**读取冻结帧举例**

请求报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQuPTc2HodzfXGBX2Abu7HEANriaLNj8GYyR0Z4lVAHHa3ibDDzW90UCbA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

响应报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQbBJeyAKDW3puQc7DgCahCPevkEicJMKicr0yVO0LcIqjsIGBzkUs2qTA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

**读取引起冻结帧数据的DTC举例**

请求报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQSUTW6p5jP6ZJlruts4eBXyVnBSZbp791C2B0qtRddppop0lTU7GZ4w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

响应报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQHKnutoiciamPibbIohMCsIZS8xGRYVOtquicOyrkCzFrQsnGNnbxMllzicw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

**读取确认的排放相关故障码(0x03)服务**

看看已经发生故障的DTC有哪些，跟UDS的19服务是一样的。

举例

请求报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQX0Gl4JgGDZicG4ic16ID1aYoDzD23C2TsuoNlmtLIh9GBMWRsiaI14dqw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

响应报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQxPblfwY482Bfw7d13U46TloSWnJlCgLxaCvsBFxC6icZBdmnrfQ4ARg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

如果都没有故障则会回复43 00

**清除排放相关诊断信息(0x04)服务**

相当于UDS的14服务，清除的数据包括DTC的故障状态码、冻结帧、扩展数据等。

举例

请求报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQMVgKoUVQBhpqZvoLiaR3W1LvdKyGaTqY3jmibiaUQMXI4YnuoT9ICtQyg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

响应报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQ2IcnYsvwaTlCT28838jGlY2thpeZKzb3v8wTtDJpV1GjHmIO6LgrbQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)

**请求氧传感器的检测结果(0x05)服务**

监控氧传感器的测试结果，一般06服务已经涵盖了05服务。它跟服务01一样，有查询PID，不过这里叫TID（Test Identifiers）测试表示符，分为三种查询TID，组件TID和数据TID。

整个流程有3步：

1、先发送查询TID，看看是否支持我们想要的查询的组件TID。

2、根据接收到支持的组件TID结果，再发送想要的查询的数据TID。

3、接收到的数据TID结果。

报文跟06服务差不多，如果没有组件TID，流程就缩减为2步，在第二步就请求数据TID结果。

**请求规定监测系统的OBD监测结果(0x06)服务**

跟UDS的31服务一样，这里的ID被称为MID。

举例

请求报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQL0lYuoet9zCkdRupjicTz3q9PeqwiaibUD1oic332icxCrtlJ4gumKQib6Gg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19)

响应报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQySCbydoqcNCj20h68kKE9V3zhpPCSZDSicffzQc18iaAcrIZR2koUyZA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20)

**读取排放相关当前或最后驾驶循环的故障码（0x07)服务**

该服务主要应用于汽车维修后的测试工作当清除所有故障码后，测试一个驾驶循环，如果失败，则会出现故障码，当然这并不代表部件/系统故障，还需要进一步的测试，于是就使用0x03服务进行详细的测试。

举例

请求报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQ2oh5SkpCQ5fASxQsaeFYu65cd5DXY6lEMB8CJxR4uSP8fVgPkRDCTQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=21)

响应报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQeCSBDiakXYKNWRmyxw8TDURd49AicCcGfUIUPIWFjhP1icP3wDaapIv7w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=22)

**请求控制车载系统、测试或元部件(0x08)服务**

这个服务使用的比较少，也就是UDS的0x31服务。请求报文只会请求开启、关断或者持续一定时间的循环测试。响应报文里面也只是上报个系统状态或者测试结果。这个服务也有查询TID。

举例

请求报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQ0jXv5br1Au92IzUSXDibKGPE2iagp4yMmdr9Vib6Pd6B55rjHeth8c0Xg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=23)

响应报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQIoo3ka0pzTRa1ibz6YbqZlT06WX4Z43ol7anweyC51LZS4pRibKsrpTw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=24)

**读取车辆信息(0x09)服务**

跟UDS的22服务读取DID一样，和前面提到的PID TID一样，这里叫InfoType，一样有查询InfoType。

举例

请求报文

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twib61xQVHSswcwOJKXj9ZJGQqRuR3iaI29Eia2WqBDNMBIfvWcRsoqveOMqXhaOWc6IDibrOxogQtQb6g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=25)

响应报文

![图片](https://mmb...