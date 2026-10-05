---
title: 车载网络系统基础：架构、传输方式与总线协议综述
url: https://mp.weixin.qq.com/s/1pbOyOfSrXr7K1nTnAME_w
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:53:54.493475
---

# 车载网络系统基础：架构、传输方式与总线协议综述

# 车载网络系统基础：架构、传输方式与总线协议综述

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**01**

**车载网络系统概述**

**1、线束连接方式对比**

传统线束连接方式 —— 点对点连接

特点：

* 布线复杂，占用空间大，从而限制功能的拓展
* 故障率增加，降低汽车的可靠性，故障率增高且排查难度加大
* 大量的数据传输线，会增加重量和成本
* 控制器上的针脚数需要不断增加，且会带来更多的干扰。
* 线路更复杂

如下图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBvWFD4k1tVK8icDUhayiamhwS4Rd8vcFDhibzrZicLgRk9vzcFjwicNNQtqw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**总线连接方式 —— 指在一条数据线上传递的信号可以被多个系统共享**

特点：

* 简化线束。减少重量，减少成本，减小尺寸，减少连接器的数量

如下图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBPzlK4OD1yc2yT9yG9qSBrz6vhcwoOaVLmcf5bknNVfhK5CXZ1e12DA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**2、信息传递方式对比**

**传统线束 —— 并行数据传输方式**

特点：

* 几个信号需要几条信号传输线
* 信号都属于平行关系，互相之间并没有关联，每个信号都有专属的信号线，多个信号多条线进行

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBUgaIB1CbeyGMpJ5jexVq1AAibsB5VdPp3XDC8YSHf83ic35Q0MzeCDBA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**总线方式 —— 串行数据传输方式**

特点：

* 仅需要1或2条传输线即可
* 按照内部程序转换为各种数据后，通过1或2条线，在通信线上传输的"0"和"1"的数字信号

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBOPHL8KialSUyIre3DIluZU9LFicvPyCLj5aCbVqKicE4xtEqMVVVfH4pw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

传统信号方式和总线方式对比图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBavCuypC6Js76jicLLDpjeqdzcyjibSKFoUY1EJ3Eoe1PPxeUlnqZsDibg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

**02**

**车载网络系统的功能**

**多路传输功能**

同一通道或线路上同时传输多条信息

**唤醒和休眠功能**

用于减少在关闭点火开关时蓄电池的额外能量消耗

**失效保护功能**

当系统的CPU发生故障时，硬件失效保护功能使其以固定的信号进行输出，以确保车辆能继续行驶，当系统某控制装置发生故障时，软件失效保护功能将不受来自有故障的控制装置的信号影响，以保证系统能继续工作。

**故障自诊断功能**

故障自诊断功能包括多路传输通信系统的自诊断模式和各系统输入线路的故障自诊断模式，既能对自身的故障进行自诊断，又能对其他系统进行故障诊断。

**03**

**车载网络系统的常用术语**

**数据总线**

可以实现在一条数据线上传递的信号可以被多个系统（控制单元）共享

**局域网**

汽车上的总线传输系统（车载网络）是一种局域网

**节点**

在计算机多路传输系统中的控制单元模块被称为节点

**链路**

有线：双绞线，同轴电缆，光纤

无线：蓝牙

**比特率**

每秒传送的比特（bit）数。单位为bit/s，也可表示为bps

**传输协议**

通信协议，是控制通信实体间有效完成信息交换的一组约定和规则。换句话说，要想交流成功，通信双方必须“说同样的语言”（例如相同的语法规则和语速等）。

**传输仲裁**

避免数据传输冲突，保证信息按其重要程度来发送。

**04**

**数据传输方式**

**并行传输**

发送装置向接收装置同时（并行）传输7～8位数据，两个设备之间必须包括7或8根平行排列的导线

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBx4QpnicM8xKhzPbT0UUuKEIZ8pZib6CV41wYLib1fCkzJw100Ooe2rrug/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

**串行传输**

数据处理设备之间进行数据通信。在1根导线上以位为单位依次（连续形式）传输所需数据

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBuxeKkxT6bGouQ482mTjCVppb2VBdgHUTEQ4JMerr5ia8RAIqWibiaaDrQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

**同步数据传输**

使用1个共同的时钟脉冲发生器可保持发送装置和接收装置时间管理的同步性

**异步数据传输（后面CAN总线会详细介绍）**

系统通过起始位和停止位识别数据组的开始和结束。只有当接收装置确认已接收到之前的数据后，发送装置才会传输后续的数据

**单工通信**

在数据总线上，信息流（数据流）只能由一个控制单元传向另一个控制单元，而不能反向传输

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBibicAYgB6FVkR7KnwuLe6iaIc87xzunp7of0w1bibBQF9nmWvIq0TibJlmw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

**双工通信**

在数据总线上，信息流（数据流）可以由一个控制单元传向另一个控制单元，而且可以进行反向传输，则称为双工通信

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBZWsDGBC9LPfXoJic0wRdpthusWY1MWFiahpNzmlqfmI7IkEqJrJOQ18g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

**05**

**车载网络分类和协议标准**

汽车网络分类：

依据通信速率分类，如下图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBCCbwHJpwMOweUwZBT4RzdGtHY2AXqkguW4JKjicPGeOuU8yzoibR1g5Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

图示拆解：

* A类：控制模块与智能传感器或智能执行器之间的通信网络，总线主流为LIN
* B类：主要应用于车身系统控制，诊断，总线主流为低速CAN
* C类：汽车安全相关，动力控制系统、电子制动系统等，总线主流为高速CAN
* D类：信息娱乐和远程信息设备，汽车导航系统
* 低速 —— 远程通信，诊断及通用信息传送，基于IDB-C协议
* 高速 —— 实时的音频和视频通信，如MP3、DVD和CD等的播放，采用光纤，总线协议：D2B,MOST,IDB-1394
* 无线 —— 无线通信，采用蓝牙规范
* E类：安全总线，如安全气囊系统，总线协议：Byteflight

依据传输类型分类：

* CAN（CANFD）
* LIN
* MOST
* FlexRay
* 车载以太网
* PS： 总线类型的成本和通信速率消耗图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBibxcwuHvMVs8nDotKjapTibvgePWtLmaOjAO6WfVooPyLNMFXlr0oSyQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

汽车网络总线拓扑图：

PS：在汽车中，会有不同的网络并存，因此就要求网络之间可以互相连接，也可以断开。为了实现即插即用，都将各个局域网与总线相连，根据汽车的平台选择并建立所需要的网络。典型的车用网络如图所示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOB372MEs3dWiaibn1tyUtk8bBgKOeYKehulzBCWVYa8YuHn5uzE4YNXwBA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

**06**

**数据在总线上的传输**

**比特**

总线导线上的电压电平以相同的时钟节拍切换，则可以在相同时段内表示二进制代码数据

**总线上的比特编码方法**

ps：下面三种方法的区别在于表示一个比特所需要的时段（时间窗）数量不同。

非归零法（NRZ）

一个时段即可表示一个比特，在整个比特时间内所示比特的电平保持不变（CAN和LIN中使用这种方法）

曼彻斯特法

脉冲宽度调制法

上面2种，每个比特都包含一次用于总线设备同步的脉冲沿切换

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBVFibslZ29pLkbiatKib15rVxFvkJVd1icIPN4R2mVwTH8sg9mHAoYrqiaWg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

**信号传输速度**

数据导线上的电压电平按传输二进制数值的规律切换。在此数据接收器必须知道数据发送器让每个比特在数据总线上停留多长时间（直至下一个数值传到数据导线上为止的时间）。这个循环时间是系统的时钟频率。

时间越短，信息传输越快，但是数据发送器和接收器的工作速度也必须越快

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9P8as3VLzQ5HhpPqhibnibOBJMhKqB2yh5thCWSDpic1AGibv1iadT8SBFaiaLUKxERX0LGsDVGeUh89Tg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

**显性比特和隐性比特\*\*\***

ps：总线上布置了多个发送器，则同时发送时会造成信息重叠，所以低位（0）覆盖高位（1）所以CAN总线采用仲裁方法来处理。

低位状态称为显性（0）

高位状态称为隐性（1）

**优先权的仲裁（CAN总线详细介绍）**

CAN总线以报文为单位进行数据传送，报文的优先级结合在11位标识符中，具有最低二进制数的标识符有最高的优先级。这种优先级一旦在系统设计时被确立后就不能再被更改。

举例：

当3个站同时发送报文时，站1的报文标识符为011111，站2的报文标识符为0100110，站3的报文标识符为0100111。通过比较3个站的报文标识符，发现所有标识符前面2位相同都为01，直到第3位进行比较时，站1的报文被丢掉，因为它的第3位为高，而其他两个站的报文第3位为低；站2和站3报文的4、5、6位相同，直到第7位时，站3的报文才被丢失。

来源：https://blog.csdn.net/Coisini\_gu/article/details/129131121

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

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=...