---
title: 汽车网络安全之——ECU攻击
url: https://mp.weixin.qq.com/s/QZ5SUAiyoUWPH9XTDGBCTw
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:40:19.334640
---

# 汽车网络安全之——ECU攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCyU8xicEF2fTE1PN5yd4A2snUXoSUUO2XcPnBfpJqFdoGPY9FC148pTr6Q5hGHic8ZiaoMHfjNoSw1Y7iauAe1S1uYh0QvSbxo1R4/0?wx_fmt=jpeg)

# 汽车网络安全之——ECU攻击

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

**01**

**概述**

从 汽车 电子电器架构的角度来看，汽车就是由ECU（点）和总线（线）构成的一个结构体（对于无线传感，车内部很少用，把网关、T-BOX等也统称为ECU）。对汽车进行攻击，其实际就是针对不同的ECU进行攻击。ECU的攻击向量有哪些，如何攻击一个ECU，对于hacker来讲是最感兴趣的话题，对整车防御来讲也是首先要搞清楚的事情。

**02**

**ECU结构**

首先从几个不同角度来看看ECU是什么样子的

**1.物理**

拆开一个ECU，最直观来看，一个ECU可以分为两部分：

芯片/PCB + 接口；

芯片/PCB是被封装在金属外壳（电磁干扰）里的部分

接口又可以分为两种：不隐藏的通信接口+隐藏的调试接口

**2.操作系统**

从操作系统的角度看ECU，是要了解固件是如何运行的，是为了破解ECU的固件；

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA2pD1edtXXHWJdt54y8FCF4a1KHcibB4FMQ8eIgjiaJ40gduUhvxibic9ibkbnO9Sx7C4SaWYeAhra5F8wtHpGqlnXRm4ibkC8a3rYE/640?wx_fmt=png&from=appmsg)

**3.程序 架构**

这个是汽车的控制器独有的一部分，从这个分类角度可以进一步明确针对ECU不同模块的具体攻击手法。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBhMaiabZgYhHlRjJgfEepPFAQLAicY9kBa3lm3xibvwJ5pUqyWDarLwTnhlwWSmf0qumS69nNRaF79UOLibhObMO3sJew9DbPoxC0/640?wx_fmt=png&from=appmsg)

先从这三个角度来看ECU，这三个角度涉及到硬件、操作系统/程序运行方法、汽车电子软件，细说起来每一个部分都很多，希望日后可以详细说一下。

**03**

**ECU攻击**

上一节说了汽车ECU是什么，从什么角度对其进行分层分类，从而在这一节得到攻击向量，以上三个角度可以统一在以下三层：

* 网络（接口）：协议的攻击（从第一、第三角度看）
* 固件（FLASH）：固件的逆向（从第一、二、第三角度看）
* 芯片/PCB：物理攻击（从第一角度看）

**网络**

网络的攻击向量可以通过无线网络和有线网络；有线网络主要是CAN网络；CAN网络攻击可以分为对RAW帧的攻击和对协议报文的攻击；RAW帧的攻击主要是因为CAN本身的属性造成的：

1.无身份认证
2.优先级
3.广播
4.总线错误
对于协议报文则可以从第三角度来看：
对诊断报文
对应用报文
对网络管理报文

**固件**

固件获取：固件获取的方法有很多种，也有很多的介绍；从第一角度来看，固件获取可以从FLASH直接提取，从调试口读取甚至可以动态调试

固件分析：这个就要先从第二角度来看了，对于通用操作系统有自己的工具链，相对麻烦一些；对于操作系统和程序没有区分的可以直接用动静态分析工具去做。

漏洞利用：对于通用的操作系统，其利用方法很多；对于另一种可以窃取一些数据，更改一些参数，但是持久化利用是一个问题。

固件的具体分析方法可以参照：
https:// blog .csdn.net/Pan\_w\_w/article/details/105958014

**芯片**

到了芯片这一级，就是一些物理攻击手段了，最典型的就是侧 信道 分析和故障注入。参考NXP的一张图。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBp2qWtNj2GFBgTFyUHEnBQO2AuTANxicJOs0ALjyloBd52bMJ2kYhDRHCiaMtdw71p7LdibLobDqzNA56eQib7nOuWqdKrLPBR1jk/640?wx_fmt=png&from=appmsg)

**04**

**保护**

简单说一下保护。针对各种攻击都应有相应的保护手段。保护的根本还是基于密码学的，目前来看就是要保证硬件安全，建立可信体系，主要使用的就是硬件安全模块，如ＨＳＭ、ＴＰＭ。

HIS SHE

这个规范主要是讲基于对称加密( AES )的硬件安全模块,其密钥如何管理,如何使用,并介绍了安全启动等流程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDcZfcpc0hNk9l1g4POpwibHJh4NFXe3Wk478642IX9GoeS4FXOBXg9mvv3xtLAvzoKY0ibIr49kCibHVBWl2M96V6AIZc1IqDKick/640?wx_fmt=png&from=appmsg)

EVITA　SHE

这个项目介绍了对于不同场景采用不同的安全等级设计,分为FULL Medium Light三种,并对报文安全等级也进行了一个划分

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCwI7Fk4s9icK4fUcKZeLtaCCTslnLJE6Rh8zR6BPVkqVvia9gaOl8fdDeNicOGsS6yoicN9lutSQqYkiaa9cLqHnic44RjZa1AouJ58/640?wx_fmt=png&from=appmsg)

**05**

**小结**

笼统的介绍了一下ECU攻击的情况,其中有自己的 思考 和参考一些他人的思考,后面需要对每一种结合自己的实践进行一个更详细的介绍.汽车作为一种IoT设备,和普通IoT设备的漏洞挖掘有很多相似之处,但是也有很多不同,对以下四个问题需要进行进一步思考:

1.对于汽车ECU的攻击向量还有待发掘
2.如何进行漏洞的利用
3.保护方法有效性
4.攻防的均衡

来源：CSDN@闻者文也

https://blog.csdn.net/Pan\_w\_w/article/details/106058453?spm=1001.2014.3001.5502

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

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=appmsg)

**公司类型占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJABYuCSyTpLXjRNbVv7OUTUUCxmB1OuPhtcM4j1kw/640?wx_fmt=png&from=appmsg)

**文章**

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&chksm=e9270eacde5087bacb4d9c888f3a21ceae227156c89aba0be7d9ebc8b02a68b4f11e7595255a&scene=21#wechat_redirect)

[关于涉嫌仿冒AutoSec会议品牌的律师声明](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247531034&idx=2&sn=e466ca3e7c2927a91dd9a81be705afe1&chksm=e9273ec1de50b7d7f540ae2e4c255bfb42f842228a87f7dbc65297027a878544a9e796e09cf6&scene=21#wechat_redirect)

[一文带你了解智能汽车车载网络通信安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247517280&idx=2&sn=8bfafb17871598c9cc0041bc9ee5f65d&chksm=e927c0bbde5049ad8cdb3647f6cdfce00c2db7a7b484941027bb7edf3128e4eaa74d6727dd46&scene=21#wechat_redirect)

[网络安全：TARA方法、工具与案例](http://mp.weixin.qq.c...