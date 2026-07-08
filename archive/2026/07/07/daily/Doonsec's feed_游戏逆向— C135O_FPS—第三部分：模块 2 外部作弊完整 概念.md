---
title: 游戏逆向— C135O_FPS—第三部分：模块 2 外部作弊完整 概念
url: https://mp.weixin.qq.com/s/y313f39gAiRoPPLeFGHpcw
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T04:59:45.997564
---

# 游戏逆向— C135O_FPS—第三部分：模块 2 外部作弊完整 概念

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icfnkibn16VehRtqEdRBx388EwFRwkppb65ruBNw7vCRLkHUNOYQCg3PmtW3gVrtwleokIuM1s6pBBxF0Kg1nthrcMTyIaB67jDqcaV6agcI4/0?wx_fmt=jpeg)

# 游戏逆向— C135O\_FPS—第三部分：模块 2 外部作弊完整 概念

原创

bl0ckdev
bl0ckdev

Esn技术社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

置顶目的文章：

**[2026年“新”-Bl0ckdev 的 Ai MCP 逆向实验训练室「不择手段。只要能拆。」](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247493236&idx=1&sn=d8e73f26ddceafe6e97dec378191d220&scene=21#wechat_redirect)**

本文要求:

要求：[ ESN能够创建出自己的程序 ]

* 软件构成原理（构建出自己的图形化软件）
* 软件逆向原理（懂创建才能知道如何拆解）
* 逆向软件使用（基础的逆向工作Ida流程）

本文摘要：

摘要：[ 更换Mac 后的日常与安全编码和逆向的发展 ]

* 合理的使用Ai如 #Deepseek  #Codex  #Claude 对自己的项目进行维护和更新！
* MCP的重要性和适配那些逆向工具与安全编码中汇编的重要性！
* 当你读懂汇编的时候#LLms 你会发现原来并不是魔法而是趋势！

本文目的：

目的：仅ID:成员 逆向教育用途,请勿用于违法！！

* 帮助ID:成员理解内存、系统编程和游戏内部结构的工作原理。
* 目标不是干扰游戏或伤害他人，而是在负责任的离线环境中与机器人对抗，积累技术知识。

------------------

安全汇编/编码与高级红队技能—本地合法化研究严禁违法

档案标签：#C135O#N2800#Y7899#Z20K

![](https://mmbiz.qpic.cn/mmbiz_gif/PwaXL3w2IRbEpH2mA2MoUTn5BlpMich3KpXAMm8icTq6Uoz3cLsZaRHnAQL7lhuBWuyxJQE9DmDkU7vUB3Ctr8fg/640?wx_fmt=gif&from=appmsg)

**「ESN技术社区」**

![](https://mmbiz.qpic.cn/mmbiz_gif/PwaXL3w2IRbEpH2mA2MoUTn5BlpMich3KHia9IsDCGaRQT1YChSVbNEEpvwUKBtqkicHDyKpNSnVlWykodEcOiawVQ/640?wx_fmt=gif&from=appmsg)

H6|F200 - 今日互动|Disoc[r]d |2026/7/7

|  |
| --- |
| F200:ios 18系列漏洞研究互动F200:  F200:Android如何防御恶意App与分析恶意App。  F200:Ai Agent和 Claude+codex 的高级玩法研究讨论 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Vej3ConbNJo8Kjev1AnQ09pGOXX9WicmF48lab5zCP2micK6qxb9P2tAEWPicicmTeHEeEDhvmiaKibniblBCBr6D3chrYWKeFbwJt3GYQ/640?wx_fmt=png&from=appmsg)

知识星球|C135O| 2026/7/7

|  |
| --- |
| x64dbg\_mcp\_本地LLM\_智能Agent\_自动化逆向实践过程  要求显卡最低：8Gb因为我使用的是本地LLMS。其他的没有实际测试！ |

**Y7899和Z20K 要求显卡：16Gb或M4-5系列 64+1T最低标准**

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VegfYtJYwicG6uL5zUnpYiaiavtbAyd8sWSmNMiaEdiaa7eUU1Wyo77GeqL2iaVNNjs2Wjaq1KwGQEssJBJxxiceAia6WvicwtbTVMnHVaMU/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_gif/PwaXL3w2IRbEpH2mA2MoUTn5BlpMich3KC7ialXLOXUgL1jfYn7fibL6mgw4utPnI4zFALcuBGZhHz5Pnw4micYPSA/640?wx_fmt=gif&from=appmsg)SOS 组授权问题或群问题超过8小时没有处理请在这里进行提交你当前的问题并且,后期关闭注册彻底修改为邀请注册。**

```
https://discord【.】com/channels/1387624412735471737/1496441227363750068
```

**标题：下一步的简介与要点**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Vegc9Miceo0V9O9nJOQic3E4QbYiao1dPSLn1YzoAGlIAr4bcicXL8p0qwrEkHkprBJOzxU7gVaTaVct7nRXhx5gXaIPN20Nfj0zqw8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWyPAA3nEav0W1sUAlCNdvPvW9NyaciaLictUkoncKegfuXAic6tYu7qSFA/640?wx_fmt=other&from=appmsg)

一：工具集

1. Ida pro
2. VS C++

![](https://mmbiz.qpic.cn/mmbiz_jpg/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWyPAA3nEav0W1sUAlCNdvPvW9NyaciaLictUkoncKegfuXAic6tYu7qSFA/640?wx_fmt=other&from=appmsg)

二：内部与外部作弊的理解 —  结构化[ 描述/非教程和细节 ]

[1.游戏逆向— Bl0ckdev \_FPS—第二部分：模块1 内部作弊和外部作弊的解释](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247493778&idx=1&sn=7eb1446b29b16ba953102d3cb2d8d974&scene=21#wechat_redirect)

[2.游戏逆向— Bl0ckdev \_FPS—第二部分：模块 2 游戏作弊内部与外部的代码示例](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247493793&idx=3&sn=6abe67c89fdd0852cd97b62ff62b9c13&scene=21#wechat_redirect)

[3.游戏逆向— C135O\_FPS—第三部分：模块 1 :Cheat Engine去验证(1)的三个值[概述]](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247493712&idx=1&sn=2bb9b5abc129ae4e4a571ebcfa00acf0&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWyPAA3nEav0W1sUAlCNdvPvW9NyaciaLictUkoncKegfuXAic6tYu7qSFA/640?wx_fmt=other&from=appmsg)

三：操作系统/通讯

1. Windows
2. Mac book
3. 通讯：Disoc[.]d/ - [ zsxq ]

   ![](https://mmbiz.qpic.cn/mmbiz_jpg/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWyPAA3nEav0W1sUAlCNdvPvW9NyaciaLictUkoncKegfuXAic6tYu7qSFA/640?wx_fmt=other&from=appmsg)

四：验证后的步骤

  验证后我们需要把我们需要的内容拼凑起来,如人物/名字/视角相关的拼凑起来,从而形成有效的使用。具体的我会逐步的在ID:成员专属服务器中仅更新完毕！一步一步地添加细节。目前细节还没构思！单纯的发出来让给位Ai大神去做最新的教程。。。

* 作弊引擎
* ViewMatix
* 血量相关的指针
* 视角相关的指针
* 瞄准的相关动态
* 然后是图形化 ImGui

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VehOibaPbCnrGcmMhESo4H5l24yDLfIEJZg6wcGaA6kibvUCp2YJllS9Hn1y1xxkG8kaNWRfsnTZFTOZpktXHUps9E9IILZdypcnc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VejVWqBLC2EQ8tUrV9BPWnbRXSRt71tFIMFjibbG2XRmiaPQXS6W9UxzfTmTcAnWicFePicjicoUtBav4szmUcaEWcQYjxqVjmbcdKJ8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16Vejqs14IBibGyS5mVZx0dOyWxAP6UOSx69N4RY7YQoc0jHy63npMEhCBuH1h0N434iaI8qlicyRUXsFOCCficOyyyTx53Wiba66UpBeo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VeguqoxlslQTiaqrfmvz26icR9br8AhRHzFomJIQNRKwGX59kib5kSZw1svKDuoyHq1p1G74dTmXR4fkzE6pkTDXNpvxO9ymDiacib8k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VehSS5N8icteLJMdqfy92O0sPEEmibs3zxMH844O5icSTtEHicjLQFJrKqoOXPDKlRls5KHRXDk0BonyCumw5SWHWDkUh4sy92KkKIU/640?wx_fmt=png&from=appmsg)

给各位Ai大神,你可以跟着我的提示通过Ai仅限完整的复现出,可使用的部分：目前有效时间是20260707,今天过后就又失效一个方法！因我又给游戏厂商发了个邮件！！！！！！！

![图片](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VehDz4bWCrCwneekZIpEc21utlO5F1yjRxNR46c87xXcvV7lGiaSN3XI8wz6ziclicqfibPVJtYZSqKhUeCsicthzwR9qgT3HDjcLY6E/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VegEibpTZHU36PPV91dr3fMRdFx6icN4JMXxcficmdLgR1nB12kBMlUG5bSm0xoH1WRFsb3lSsTRRU7wCo6Az1AjXwBYI2EDyfhs5k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/PwaXL3w2IRbEpH2mA2MoUTn5BlpMich3KHia9IsDCGaRQT1YChSVbNEEpvwUKBtqkicHDyKpNSnVlWykodEcOiawVQ/640?wx_fmt=gif&from=appmsg)

**「ESN」**

**![](https://mmbiz.qpic.cn/mmbiz_gif/PwaXL3w2IRbEpH2mA2MoUTn5BlpMich3KfxQF5VMtca1ou6iaWQmxfpBpejXVBbm0DPktgBBfLrAicRxicxN9AY0FQ/640?wx_fmt=gif&from=appmsg)**

![](https://mmbiz.qpic.cn/mmbiz_jpg/PwaXL3w2IRaDgaRQG5ujsPrXostCchunyCR5Y0VpBpPTkXATnVMxBwPRnYBKdqgPx7AB433icw5FXez1xp6Nibqg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

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
在看
，轻点两下取消在看
分享
留言
收藏
听过