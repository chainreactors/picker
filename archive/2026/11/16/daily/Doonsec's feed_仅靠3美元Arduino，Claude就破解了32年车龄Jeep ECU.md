---
title: 仅靠3美元Arduino，Claude就破解了32年车龄Jeep ECU
url: https://mp.weixin.qq.com/s/-nu4LWCTayEhXr80-UumsA
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:51:38.336797
---

# 仅靠3美元Arduino，Claude就破解了32年车龄Jeep ECU

# 仅靠3美元Arduino，Claude就破解了32年车龄Jeep ECU

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX2H17ODeBq0uzFJ7jWj1ickg4wuebhaCKP1K1lM2aicejBfiae8YM74IAYDXz00hLicSR6qDAaQKqoibKjP4QiaXciafgzcypv6QF3vPQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3jU9IG88u0j7XPH25mv8Caa97HS6WBIRkkFVaibSRlkibVFMG16QNrJPrAlf9JINjelsr5FcKwreTezia4juXMiajMhBiboibSOjf6A/640?wx_fmt=png&from=appmsg)

车主Muhammad Zulali表示，一款AI coding Agent帮助他读取、复制并在1994款Jeep切诺基的发动机电脑内运行代码。整个过程耗时约一周。他仅使用了价值3美元的Arduino Nano，最终这辆Jeep顺利通过加州尾气检测。2026年11月10日，Zulali在YouTube视频中分享了完整项目过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3ibN5gJgM6H8CsaBIEvnavwtiaK5HiaPoI5lgBE8jZpw7Zz3hE2JuR8PmibTAWuQz6Sg6S2JicopHzbmzwyBtqgibdS6mWTqoaCbgVo/640?wx_fmt=png&from=appmsg)

Part01

老旧Jeep无通用诊断接口

3美元Arduino搭建通信链路

这辆Jeep出厂时间较早，没有配备现代车辆通用的OBD2接口，市面上的常规扫描工具无法与其建立通信。车辆此前在25英里/小时工况下检测时，因NOx排放过高未通过尾气检测——发动机空燃比过稀时，NOx排放量会明显上升。

Zulali最初尝试更换氧传感器解决问题，不料15英里/小时工况下的检测结果反而更差。每次尾气检测的费用约为100美元，反复试错的成本过高，他因此求助Claude Code寻找更高效的解决方案。

Claude分析发现，这款发动机电脑采用克莱斯勒早年的低速SCI协议通信。与普通串口相比，该协议的信号线极性反转，需要搭配小型转换装置才能正常通信。只需一块价值3美元的Arduino Nano插在面包板上就可以实现转换，整套配件总成本约15美元。

Part02

从只读数据到控制车辆

定位尾气超标根因

据Tom's Hardware报道，这套通信链路的传输速率约为7800波特，仅用到车辆六针诊断插头中的三根接线。其中一个针脚在车辆钥匙通电时携带12伏电压，误触会直接烧坏电路板。

团队在凌晨1点30分首次成功读取到车辆数据，当时仅能获取冷却液温度和电池电压两项信息。后续读取到的数据出现异常，显示燃油修正值似乎会额外增加22%的喷油量。Zulali实测燃油压力后发现，实际油压仅为10 PSI，远低于正常水平。

随后Claude独立控制燃油泵运行了约10秒，Zulali认为这是工具从只读数据转向直接控制车辆的关键节点。过程中AI也曾出现错误，问题源自一款公开工具：Claude后续发现，ChryslerScanner的参数表与他的Jeep车型不匹配，实际发动机是在减少喷油量，而非增加。项目团队也在致谢名单中特别标注了该扫描工具的作者László Dániel，感谢他提供的参数表。

接下来Claude将发动机电脑的整套程序拷贝到笔记本电脑中，分析代码后发现一套加州专属的燃油映射表，会在尾气检测对应的负载工况下减少喷油量，这很可能就是NOx排放超标的根本原因。重刷芯片是最直接的修复方案，但这台发动机电脑生产于1993年12月，比支持重刷功能的批次早了约四个月，无法直接重刷。

Part03

Codex辅助实现代码运行

这时OpenAI的Codex介入解决了这一问题，它找到了一种方法，可以通过同样的三根接线向发动机电脑下发小型程序，并引导电脑直接运行。系统几秒内就清除了首个版本的程序，Codex随后将代码迁移到EEPROM中——这种存储介质在车辆断电后也不会丢失数据。Zulali表示，整个项目中Claude负责大部分诊断工作，Codex负责内存相关的代码实现，他本人只负责接线和实车测试。

目前该项目已基于GPLv3协议开源，截至发稿时，GitHub上的xj-scanner仓库已获得252个星标、30个复刻（fork）。开发者仅在一台1994款搭载4.0L发动机的切诺基XJ上完成了测试，作者明确提示，使用者需自行承担所有风险。

对安全从业者而言，这一案例的启示在于AI Agent掌握老旧冷门系统的速度极快。此前研究人员曾证实，攻击者通过物理接入可以操控车载电脑关闭刹车系统，如今Agent可大幅降低这类工作所需的skills与时间成本。

此前本站报道过Claude Code发现模型隐藏后门的案例，也呈现出相同的规律。Agent本身也存在安全风险，此前就有攻击者通过下载文件夹中的文件劫持Codex与Claude Code。Anthropic发布的Claude Code安全指南明确建议，用户在批准执行命令前，必须先审核命令内容。

Zulali坦言自己并非专业汽修人员，部分关于发动机的结论可能存在错误。本次项目的结果由车主自行上报，目前尚无第三方对其进行独立验证。

参考来源：

Claude Cracks 32-Year-Old Jeep ECU Using a $3 Arduino and Reverse Engineers Its Engine Computer

https://cybersecuritynews.com/claude-cracks-32-year-old-jeep-ecu/

###

### **推荐阅读** [![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX38ibvFWu8tnORNBELsice6a0HbKoyGH0LDKjzxAxpAr4ib5Qn3oKb4huesy0pnDicAXIdDmoumzuj6nAPZsCTU1QBX0hQYzdJj5uo/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651351016&idx=3&sn=d224081e5f21f76580f08cd93c037d34&scene=21#wechat_redirect) **电报讨论** ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2cCEVtIlLczLq1S4rms9uYa8x5Xedy0Il667ib20FMyHawNapLuHBl3peZxWoStYkAJdBcMicfmy9icChQA8uKfBib5EPaMicU5ykw/640?wx_fmt=png&from=appmsg) ![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png) ![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
推荐
，轻点两下取消推荐
分享
留言
收藏
听过