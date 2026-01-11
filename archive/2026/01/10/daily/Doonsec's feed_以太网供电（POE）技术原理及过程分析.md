---
title: 以太网供电（POE）技术原理及过程分析
url: https://mp.weixin.qq.com/s/WLDe0b8DZu44csjZnXnI0A
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:37:49.687125
---

# 以太网供电（POE）技术原理及过程分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibGv8CYfdNtefewG4T4Ir1sJP8DzaIWQKgFJuCD8wUfan1PznDoM0o6KSYRMM6NdfgmZlYQHnK6BA/0?wx_fmt=jpeg)

# 以太网供电（POE）技术原理及过程分析

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247564281&idx=2&sn=699099fdf353a20e4b133c9bb09efbe0&scene=21#wechat_redirect)

**01**

**以太网供电技术**

以太网供电技术（POE，Power Over Ethernet） 是指通过常用的语音、数据和视频的双纹线提供电源的技术。以太网供电技术是在现有以太网布线基础上就能保证为IP终端传输数据信号，同时为此类设备提供直流供电。借助通用以太网电缆同时传输以太网信号和直流电源，将电源和数据集成在同- -有线系统当中，在确保现有结构化布线安全的同时保证了网络的正常运作。以太网供电采用IEEE802.3af标准，802.3af突破了以太网的应用，它主要是- 一个电源传输协议，而不是数据协议。

**02**

**以太网供电系统构成及原理**

**2.1POE系统构成**

一个完整的POE系统包括供电端设备和受电端设备在POE系统中，提供电力的叫做“供电设备（PSE，Power两部分。Sourcing Equipment），负责将电源注入以太网线，并实施功率的规划和管理，而使用电源的称为“受电设备”（PD，Power Device）。

以太网供电开始于能提供电源的供电设备，该设备通过测量其共模终端来检测需要供电的设备。有效的受电设备必须具有一个25k9共模电阻的“检测特征”。PSE用- 一个称为分级的第： 二次测量来判断PD的峰值功率要求，掌握这一信息后PSE就能对那些需要供电的设备提供电源，而不会损坏不需要供电的设备，并能有效地分配可用功率。

**2.2 POE供电传输方式**

802 .3af标准定义了两种不同类型的PSEi一种是“Endpoint PSE”，即末端跨度PSE，把供电功能与网络交换机集成在-一起。EndpointPSE就是支持POE功能的以太网交换机、路由器或其他网络交换设备。末端跨度设备在双绞线中的1、2、3、6号线缆上同时接入电源和数据，如图1所示。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibGv8CYfdNtefewG4T4Ir1sO9eb3vzJUd4qrOCZEDoKnjukQicCiciaDhx018tsHKCTEdFjZmdCmiaMIQ/640?wx_fmt=png&from=appmsg)

末端跨度PSE支持10BASE-T.100BASE TX和1000BASE-T网络。末端跨度的POE系统中的PSE可以在信号线对之间或备用线对之间提供标称48V的DC电 源。

Midspan PSE是一个专即中闻跨度PSE，另一种是“MidspanPSE”是一个专门的电源管理设备，通常和交换机放在- 一起。它对应每个端口有两个RJ45接口，一个用短线连接至交换机，另一个连接远端设备。PD则有多种形式，如IP电话、AP.PDA或移动电话充电器等。

中间跨度PSE在交换机和PD之间，它通过双统线中没有使用4、5、7、8号线缆提供电源。数据通过中间跨度设备路由，不会有任何改动，中间跨度PSE通常与以太网交换机相邻安装在设备机架中，如图2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibGv8CYfdNtefewG4T4Ir1sTYaHtGdZgRWyHGRepAnKBvnn2mI3ktyMOcmJHrYp6KMTtm4bgUevqw/640?wx_fmt=png&from=appmsg)

空用段对中间跨度PSE只支持10BASE-T和100BASE -TX网络，而802.3af标准目前还未定义对1000BASE T网络的支持。中间跨度PSE在备用线对之间提供48V的DC电源。

**03**

**POE供电设备原理详解**

标准的五类网线有四对双绞线但是在10M BASE-T和100M BASE-T中只用到其中的两对。IEEE80 2.3af允许两种用法：

1.应用空闲脚供电时4、5脚连接为正极，7、8脚连接为负极。 下图为利用空闲线（4，5，7，8）传递48V的电源。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibGv8CYfdNtefewG4T4Ir1slLpHibQDuxia1uR9khiahTaicwKWsOAgMuHShkeHBSRIToB5J8AGsJKdqg/640?wx_fmt=png&from=appmsg)

2.利用信号线（1，2，3，6）同时传递数据信号和48V的电源。应用数据脚供电时，将DC电源加在传输变压器的中点，在这种方式下线对1、2和线对3、6可以为任意极性。传输数据所用的芯线上同时传输直流电，其输电采用与以太网数据信号不同的频率，不影响数据的传输。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibGv8CYfdNtefewG4T4Ir1sAEJWrWCjhvvDjFQwtKlMepvCHccvKaeiaxaJdurT7LCGyTvkicicsxs2g/640?wx_fmt=png&from=appmsg)

标准不允许同时应用以上两种情况。电源提供设备PSE只能提供一种用法，但是电源应用设备PD必须能够同时适应两种情况。该标准规定供电电源通常是48V、13W的。PD设备提供48V到低电压的转换是较容易的，但同时应有1500V的绝缘安全电压。

下面谈一下1000M BASE-T POE 供电系统

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibGv8CYfdNtefewG4T4Ir1srCC9ZXGo6gap6Uh3YOZNesxKNEaOHDic7VlnwxABpu5R1WIfhSBIiaHg/640?wx_fmt=png&from=appmsg)

1000M BASE-T POE 供电系统 4个线序对均传输数据，故无空闲对，均采用数据对供电，图4左图，1脚和2脚、3脚和6脚通过网络变压器进行电压、信号的分频、分离出来的电压连接到桥式整流进行整流供电，如图5

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibGv8CYfdNtefewG4T4Ir1sbAaX60xy6n7HDLWn8968Ef3HibqOUM6OlEcYf7OPjJnYBKZUKe6Pczw/640?wx_fmt=png&from=appmsg)

以上讨论的是POE adapter 供电模式，典型的POE adapter 如下图

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibGv8CYfdNtefewG4T4Ir1s7FKdRe5JSMOVwibIQZ4Cl4gswC0nKj7fy8Y2BzaZ5JyMyPOicBsmJQ5g/640?wx_fmt=png&from=appmsg)

另一种是通过POE供电交换机供电

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibGv8CYfdNtefewG4T4Ir1sZQWvVg1KtZ69OjInBPeGJQ0icu7FEHke7csGU291KLGiaNZercWEAfZQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibGv8CYfdNtefewG4T4Ir1s24OG4aTlpLZuIulK8rgQrlBs4PJuhzicuEtrpe2ODlAwAibnksp7TzKQ/640?wx_fmt=png&from=appmsg)

协商供电

当在一个网络中布置PSE供电端设备时，POE以太网供电工作过程如下所示。

1. 检测：一开始，PSE设备在端口输出很小的电压，直到其检测到线缆终端的连接为一个支持IEEE802.3af标准的受电端设备。
2. PD端设备分类：当检测到受电端设备PD之后，PSE设备可能会为PD设备进行分类，并且评估此PD设备所需的功率损耗。
3. 开始供电：在一个可配置时间（一般小于15μs）的启动期内，PSE设备开始从低电压向PD设备供电，直至提供48V的直流电源。
4. 供电：为PD设备提供稳定可靠48V的直流电，满足PD设备不越过15.4W的功率消耗。
5. 断电：若PD设备从网络上断开时，PSE就会快速地（一般在300～400ms之内）停止为PD设备供电，并重复检测过程以检测线缆的终端是否连接PD设备。

**04**

**以太网供电过程**

1. 侦测。在允许PSE向线路供电之前，它必须用- 一个有限功率的测试源来检查特征电阻，以避免将48V电源加给非兼容POE的网络设备，造成危害。在加电之前，PSE首先2.8V- 10V的探测电压去侦测是否有PD接入。具体实施时，是将2 8V 10V之间的两个电压送到网络链路，然后根据得到的两个不同的电流值再作运算（OV/OI）。
2. P0端设备分类。当检测到受电端设备PD之后，PSE设备可能会为PD设备进行分类，并且评估此PD设备所需的功率损耗。802.3af标准的PD要求开始于一个25kQ和小于120nF的特征识别，正是这-特征使PSE 将PD从不需要供电的其它以太网设备中区分出来。PD只需要具有这些检测特征，而同时链路处于检测模式即可实现检测。分级特征表明PD的峰值功耗，要求在端口电压为14.5到20.5V之间时PD吸收- 一个特定的DC电流。
3. 供电。在一个可配置时间的启动期内，PSE设备开始从低电压向PD设备供电，直至正常提供48V的直流电源。使电路的其当旁路电容充电完成后，端口电压就升高进入供电模式，余部分运行，并在它所在类的功耗极限内吸取电源。如果电流过高的时间超出50ms将会使电源关断。此外，PD必须吸收最低为10mA的电流，这样PSE就能知道它还保持连接。像恒温调节器这类功率敏感的应用可以通过脉电流为10mA，并且脉冲间隔时间保持冲调制使“保持功耗特征（MPS）75ms到250ms之间以减少功耗。PSE 为PD设备提供稳定可靠48V的直流电，满足PD设备不越过15.4W的功率消耗。
4. 断电。若PD设备从网络上断开时，PSE 就会快速地（300~ 400ms）停止为PD设备供电，并重复检测过程以检测线缆的终端是否连接PD设备。如果PD 直未接入或处于关断状态，PSE就停止输送电源，并不断检测有效PD的25kQ电阻特征电阻。以太网供电连接完全由PSE来进行控制。

来源：电子发烧友

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

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.w...