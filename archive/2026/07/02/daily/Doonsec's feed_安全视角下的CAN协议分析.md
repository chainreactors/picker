---
title: 安全视角下的CAN协议分析
url: https://mp.weixin.qq.com/s/tfGLJVkyv0t-YnkydlECIA
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:46:37.085050
---

# 安全视角下的CAN协议分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDLxJsMHdbbeNEIboggicDaAXuDmoxNrOFcGQaF4gHBZEibichFrYHG7NpWcDcpWpYxyhdq8pYQ6ibdClAfdhMU96kPGZhMFzvkevE/0?wx_fmt=jpeg)

# 安全视角下的CAN协议分析

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

控制器局域网（CAN  bus）由罗伯特·博世公司于1983年开发。该协议于1986年美国密歇根州底特律市举行的国际汽车工程师学会（SAE）会议上正式发表。第一个CAN控制芯片，由英特尔和飞利浦生产，并且于1987年发布。 世界上第一台装载了基于CAN的多重线系统的汽车是1991年推出的梅赛德斯-奔驰 W140。

**01**

**CAN节点介绍**

连接到CAN总线上的单元被称为CAN节点，所有连接到同一个CAN总线上的节点同CAN总线一起组成了CAN网络。CAN节点一般由以下几个模块组成：

1）中央处理器、微处理器或主处理器

处理器对收发到的消息进行解析和处理，类 似于CAN节点的大脑，经由该大脑的分析之后将指令下发给传感器、驱动器和控制设备。

2）CAN控制器，用于收发消息的控制模块

接收：CAN控制器将从总线上串行接收的字节流，直到整个消息接收完毕，然后将消息发送给处理器进行分析处理。

发送：主处理器发送信息到CAN控制器，之后当总线空闲时将信息以比特流的方式串行发送至总线。

3）收发器，由ISO11898-2/3标准定义

接收：把数据流从CAN总线层转换成CAN控制器可以使用的标准。

传输：把来自CAN控制器的数据流转换至CAN总线层。

CAN总线上的每个节点都能够发送和接收信息，但不能够同时进行。 一个消息或帧主要包括标识符(ID)、CRC、ACK等字段。ID表示信息的优先级，最多八个数据字节。消息采用不归零(NRZ)格式串行传送到CAN总线，并且可被所有节点接收。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCRqmpleyzJLNxoCXA3W9AiaxZwurJEE3V8O3rCrX0NZJS45TUEibffx2ZyT09zJHDHOberchogEcxEwO0fibgfxCNGiaQWJKwSdhk/640?wx_fmt=png&from=appmsg)

被CAN网络连接的设备通常是传感器，驱动器和其他控制设备。 这些设备通过一个中央处理器、一个CAN控制器，和一个CAN接收器连接至总线。

**02**

**CAN帧结构介绍**

CAN节点在CAN总线上以帧结构发送CAN消息。CAN帧结构，包括帧起始标志SOF、帧结束标志EOF、仲裁字段、控制字段、数据字段、CRC校验字段ACK字段七个组成部分。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaANzNZiaS6KQ9Q2MWj6E2cuMxXreyYTLAhxVGdUTq8XC5uOf52FMUibyDfeLaib4pPA3SemC0pibPHEdJoZYS11CPRicPlPqSzQqzhY/640?wx_fmt=png&from=appmsg)

CAN帧格式（图片来自维基百科）

CAN总线有四种不同的帧类型，分别是数据帧、远程帧、错误帧和过载帧。数据帧用来传送数据，远程帧通过特殊的Identifier请求指定消息，当节点检测到错误时会发送一个错误帧，过载帧用来在数据帧和远程帧之间设置延迟。CAN帧格式各个字段解释如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDZ07FSmYMvOuQabgotaMPVgeuPsFtegzKicIUiaIJicrK0e6YQmZPR5ibhv4d9QdpPdmeicRg0p270QGnnBCS0icyX7kutPN3NxBmVE/640?wx_fmt=png&from=appmsg)

CAN帧各字段解释（表格来自维基百科）

**03**

**CAN总线攻击面分析**

CAN总线攻击面包括远程攻击面和物理接触攻击面两个大的方面，其中远程攻击面有远程信息处理单元（TBOX ，或5G模块）、车载信息娱乐系统（HU）、蓝牙模块、WIFI、遥控钥匙和远程诊断接口等，物理接触攻击面主要为OBD-II诊断端口和各类传感器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCiaIlWEFkYicFgxjcdfXC3g2SZB8e0QDP8AiaQxLibvNGHy8pWu1G1RbPywPHibqUWib83bpUc6lyG89tlavAZJxFtItibicK6g5EXzTA/640?wx_fmt=png&from=appmsg)

CAN总线攻击面

**04**

**CAN总线安全缺陷**

**基于ID的仲裁机制**

CAN帧没有标识发送者和接收者，CAN协议使用一种叫“带有冲突检测的载波侦听多路访问”机制进行仲裁。当多个节点同时发送消息时，ID最小的节点拥有最高的优先级。当任意一个节点发送控制位时，其他节点均会读取控制位，无论控制位的值是多少。当一个节点检测到更高优先级的数据帧时，它将停止发送。

我们以两个不同ID的节点简单介绍以下仲裁机制生效的方式。假设在同一个CAN总线上存在节点15和节点16，两个节点在CAN总线空闲时同时抢占总线，它们即将发送的帧数据如下表所示：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDFRrSyia4raQgoSPicLVmEL1RC57ybQGb5KhicXGtgXJU6D6I4Ax4ibQcqibR5G6a9BJZGjKQEDzZqR4eQs4OhqqAEyv3lWutz9aq8/640?wx_fmt=png&from=appmsg)

（表格数据来自维基百科）

Node 15和Node 16在同一时间想要发送数据，两个节点分别发送最高的位，一次发送一位，使用“线与”机制判断，0为显性，1为隐性，前面6个比特两个节点都发送0，接收到0；第七比特位，Node 15发送0接收0，Node 16发送1接收0，Node 15胜出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDib01BbqJxByBy8pQOlibjAwkqscehpoVglNd7CVicjdqcNX90pGPeRVwErgVLkrbZmojW1XibDWgIAACcFnsKT6tRKPoQ1RxJs5s/640?wx_fmt=png&from=appmsg)

**安全缺陷**

针对这种仲裁机制，大家很容易就能想到攻击者可以伪造高优先级的报文，频繁地向CAN总线上发送，导致CAN总线上合法节点无法正常发送报文，即拒绝服务攻击。究其原因，CAN协议没有标识发送者和接收者的机制，也没有额外的认证手段；此外，在CAN总线上传输的数据的机密性也无法得到保证。

**05**

**针对CAN总线的攻击方式**

由于CAN总线没有提供认证机制和保密性机制，攻击者可以对CAN总线发起DOS攻击、Fuzzy攻击、嗅探与重放攻击以及节点伪造等等。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBMwqXQQfxhYhQsmVeRsicAhdQ5R2BdphWLk0m1TewFWnRhAJJ4n19TwiagtpR5tt7F37wmpuFrLEX8A3O1d4iblJR4rJWrW1Wznw/640?wx_fmt=png&from=appmsg)

针对CAN总线的攻击方式

针对没有认证机制的缺陷，攻击者可以以高频率的方式频繁发送最高优先级的消息：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDgicNFZruW7mw0UVUwRaBvKETib4nm5QzYDjWLYTE7SzlkqokUptva6bmRibsRCicUwckBlPCSWFjTc8htK8j7ibCQTL9ajFgXpupw/640?wx_fmt=png&from=appmsg)

DOS攻击示意图

同样地，攻击者可以使用Fuzzy的方式随机注入消息，测试CAN总线和节点是否存在逻辑漏洞和内存相关的安全缺陷：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAv23yXicBhnhuwib7k5kNokHneLfttYghsTydx0vzMqTfNSIibvpWhFOqv24sBhyhhdHXQLnNY9HURiclgqg3mSIwlfvtD1jBr2jQ/640?wx_fmt=png&from=appmsg)

Fuzz攻击示意图

针对缺少保密性和认证的缺陷，攻击者可以先嗅探CAN总线，然后对消息进行重放，通过这种方式可以实现多种针对车辆控制系统的操作：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDFyoW31j54uSY9g6gYAiaTyMiaRqD59tyiadomQxsQN0DsJ4LVpEViabANfgbC2VIyMG9WxoibjBan6ZjAbD0UXHtybibVlPqlwkLZc/640?wx_fmt=png&from=appmsg)

嗅探与重放攻击示意图

节点伪造攻击也同样适用于CAN总线，因为总线没有认证节点身份的机制，攻击者可以通过物理接触的方式添加任意节点：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD6KtX6iaIBhNjTaLGLE14jqvA5DzFdRH0Y8WsSXnySf5l6dBFSPa6rZDrlC0qMmIgRIbNYE4o9RhPvJjmJVvaJ7O7JjxGwFeXs/640?wx_fmt=png&from=appmsg)

节点伪造攻击示意图

来源：CSDN@车联网安全杂货铺

https://blog.csdn.net/didaliping/article/details/121464134

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD9qjQXZdMwY876TkFlhIUib1kn4wc72e4cib9eharylSOXtAgAq234jTmZYKrXsGd0OALDotYN7MYS8h0mElMEuPddlDZic56KCg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572912&idx=3&sn=58184d21d6dabc713e8d93a0c1d80e40&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb...