---
title: 汽车ECU BootLoader升级
url: https://mp.weixin.qq.com/s/C4dF6GrEsL9e1Y1pU63XMQ
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:09:25.815164
---

# 汽车ECU BootLoader升级

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDqkmVicrIRDwzEIp56OkxrKhsSnl48SLJiabLariafB6ktdY1RFuhticibuzfzuGXMLrRiaicVGhkDGDib5GwhUDgxU01pEUPSicNmriaxc/0?wx_fmt=jpeg)

# 汽车ECU BootLoader升级

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247566311&idx=2&sn=27d2cf53ef824bfde9b824f90e864ec6&scene=21#wechat_redirect)

**01**

**什么是 BootLoader**

MCU正常运行时总是从固定地方取指令，顺序运行，程序更新时需要使用烧录器等工具烧录，于是有人将程序设计成，由一个程序跳转到另一个程序，这个程序通常称作Bootloader，另一个叫做APP。

Bootloader是一段独立的程序。它包含启动代码、中断、主程序（Boot\_main函数）、操作系统（非必须）。Bootloader存在的意义就是指更新App程序。

**02**

**Bootloader刷写使用的协议**

UDS（Unified Diagnostic Services，统一诊断服务）诊断协议是用于汽车行业诊断通信的需求规范，由ISO 14229系列标准定义。

**03**

**Bootloader 的划分**

一个ECU包含了三部分 Boot Manager、Application Software以及Boot Software，其中Boot Software由Boot Manager和Reprogramming Software组成，在汽车嵌入式中，我们常说的bootloader就是Boot Software。

* Boot manager：引导程序启动
* Reprogramming Software: 更新软件程序，主要更新App程序

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCqFwPOExp5B5J4ibt4oDE6Q2DajOBPIMvU1kTZibbou07pyzTFPDbCz9tL1PWjPRvve5matZjqzjeEdWNqpzV6yyDE7ZBUVVoHI/640?wx_fmt=png&from=appmsg)

程序运行到Boot Manager以后，通过一些条件判断，决定进入Application Software还是Reprogramming Software。

如果进入Application Software，则意味着功能运行；如果进入Reprogramming Software，则意味着需要更新Application Software。

**04**

**FBL、PBL、SBL**

Boot Loader在嵌入式系统里，一般分为两部分：PBL（Primary Bootloader，第一引导加载程序）和SBL（Second Bootloader，第二引导加载程序）。

FBL 和 PBL 实际是一个。

ECU的内存至少需要划分三个部分：FBL、SBL、App。

**1、SBL**

SBL的本质就是Reprogramming Software，和我们经常提到的"Bootloader"作用一样，为更新Application而生。

**2、PBL**

因为整车销售到终端用户以后，只能通过OBD接口或者OTA方式升级Application，而这两种方式，均需要依赖Bootloader程序，如果Bootloader程序不可用，对应的ECU就不能正常使用。

所以，针对Bootloader更新失败这种工况，需要一个程序专门刷写Reprogramming Software，这个程序仅出厂烧录一次，以后永远不更新。这个程序就是 PBL。

这样，即使刷写Reprogramming Software失败，还可以重新刷写Reprogramming Software，之后，Reprogramming Software再更新Application程序。这样，就不会出现ECU不可用的情况。

PBL依然保留刷写程序的功能，但是，限定PBL仅刷写或者激活SBL，激活SBL以后，由SBL负责更新Application Software。

**05**

**ECU 升级/刷写**

ECU 升级的内容一般分为 boot 和 APP 。

同时，ECU的升级方式又有2种：

* 通过 OBD 接口升级
* 通过 OTA 云升级

**1、OBD接口升级**

OBD接口升级，即使用诊断仪，通过OBD 接口与 ECU 连接进行升级。

Boot 刷新所用到的两个文件是FlashDriver驱动程序 和boot软件，在这里我们可以将SBL理解为FlashDriver驱动程序，PBL理解为Boot软件。

Boot 刷写一般都是刷写 SBL，SBL存在的意义就是更新APP程序。

当MCU收到1002请求，ECU复位后会进入PBL模式中判断是否跳转到 SBL；如果需要进行APP 更新，程序就会跳转到SBL进行APP更新。

APP 刷新是通过 SBL，SBL先擦除 APP flash数据，再将新的 APP 刷写到 flash。

**2、OTA 云升级**

OTA是Over-the-Air的简称，既空中下载的意思，具体指远程无线方式。

对于汽车的OTA升级，主要分FOTA和SOTA两种。

* SOTA只针对软件升级，例如显示屏上某个APP软件的升级；是对车系系统的VI展现、操作方式方面的优化,对于车辆驾驶体验来说不会有任何提升。
* FOTA是对ECU、悬架控制单元等等车辆核心驾控部件的升级，带来的更多是驾驶体验的整体提升。例如更新 BMS的 APP 数据。

OTA 升级只能用来升级 APP 数据，通常使用 A/B 双bank 分区策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDaCjicEYWJwg1nJDTicheOjumDV6iciaZwguWpW2pGlGibgYlRrfHzNJ7CaMH85soZkbe0VnkiarbAia826YD4M3aibVxlssRwib2Fzicqc/640?wx_fmt=png&from=appmsg)

所谓A/B 双bank 分区升级，是指在设备上开辟两个存储空间（A/B存储空间），每个存储空间上均安装有一个系统，其中一个系统处于激活使用状态，另外一个系统处于备用待命状态。在进行系统升级时候，可在激活的系统中对备用系统进行升级，升级完成重启后切换成新升级的系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAThBv76Fwmhwia5zAysTYOmDA9iaJesjLGOyaTd42mMDSLr6tTQYFtNtDxkmWnHVuVCs17qc3sMERx7mwCemZicz2xFtEoKVCOX8/640?wx_fmt=png&from=appmsg)

**06**

**Bootloader中诊断升级流程**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCfUic2kyZmVfOlwNF7WZicBmCclepEttvBSvic9XiaBWENbPL5amfQBIsHBtaWc6WvLXUPKP6icK5Csm29Yq2I8QTYicOzHm0TBWDRU/640?wx_fmt=png&from=appmsg)

UDS服务设计复杂，Bootloader升级一般分为以下三步：

* 1）预编程
* 2）编程
* 3）后编程

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAqz3AZxg8icc98AZF48wH3NV39uKsiaZCSyOLMlSXw5Qts1nicf1nBpyeIwx0PmrBptaa1VsxcicfHZC8dQsDPPeicelkKYiaW74ibKE/640?wx_fmt=png&from=appmsg)

**1、预编程**

在进入刷新之前，UDS的85服务和28服务，关闭DTC诊断同时停发非诊断报文。使整个CAN 网络处于静默（Silent）状态。这是对整车网络进行操作的，一般都是以功能寻址（Functional addressing）的方式来发送。

注意：先用85服务关闭DTC，再使用28服务关报文。

* 关闭DTC诊断是防止升级过程误报DTC（例如通信丢失DTC等）
* 关闭CAN通信是为了降低总线负载，加快刷写速度。

此阶段的主要做一些Application Software升级前的检查，确保正式升级Application软件之前，车辆工况的安全性。

这里举几个常见的检查条件：车速、诊断电压、KL15信号有效性等。

* 车速：约束车速＜2Km/h，也就是说不允许车辆行驶过程中进行软件升级。
* 诊断电压：诊断电压会约束在一定的范围，比如：10V~16V，避免升级过程中，因电压过低或者过高导致刷写失败。
* KL15信号有效性：为了确保收到的信号质量，一般会检查这个信号的有效性（Valid or Invalid），有效的信号才能确保升级过程中的稳定性。

以上这些都是安全检查，目的就是一个保证安全。

2、编程

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBNJlV7TQ63LFvCkDndfZ7w3ojeSeD4Q57TUn44JicHvIJKLyWKqgh0x8C5icibrbvPqt4GIQ1NjgPAvq5s0OsY5qQiaicWCOeNcmXs/640?wx_fmt=png&from=appmsg)

**3、后编程**

刷写完成之后，ECU进行重启，重新进入扩展会话，打开之前关闭的配置。

注意：先使用28服务开启报文，再用85服务打开DTC记录。

ECU重启 常用的做法就是执行ECU Reset，也可以让诊断刷写的S3时间超时，程序重新复位。

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

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid...