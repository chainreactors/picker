---
title: 后门病毒伪装Word文档，利用钓鱼邮件传播
url: https://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247513250&idx=1&sn=f678f3ee30b0b8888b1b09694e3a9f14&chksm=eb706a9ddc07e38b0b9e8b69852ffbd3816a38ab87ea2c990f496886b32b9426d990bfd02d26&scene=58&subscene=0#rd
source: 火绒安全实验室
date: 2023-03-10
fetch_date: 2025-10-04T09:09:24.943912
---

# 后门病毒伪装Word文档，利用钓鱼邮件传播

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dGER6eFoiat3AvE7jSSweiaMruzc7UqGiaakogpCtCTfuR6Cu0Dribv9HhA/0?wx_fmt=jpeg)

# 后门病毒伪装Word文档，利用钓鱼邮件传播

原创

火绒安全

火绒安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dBn42CPQh8tQ3N9dLmhfEfelp36M0zfSh4YxSXY2S7NU84W0sZQ8OMw/640?wx_fmt=gif)

近期，火绒工程师发现针对国内企业投放病毒的威胁事件，经排查分析后，确认为后门病毒，主要通过钓鱼邮件进行传播，其会伪装成Word文档来诱导用户打开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dOb5OoaIY0cdfYRlYDPvUA5ibQDdpFjcbQPlDRXkBFhLon7v83Z7pjcQ/640?wx_fmt=png)

伪装成Word文档的病毒样本

当用户被诱导点击运行病毒后，黑客可通过C&C服务器下发各类指令来执行各种恶意功能，如：恶意代码注入、利用开机自启来进行持久化操作、获取系统进程信息等恶意功能。不仅如此，该病毒还会使用多种手段（控制流混淆、字符串混淆、API混淆）来躲避杀毒软件的查杀。

病毒的执行流程，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dpkib9uLv6BkyrMIaOpPHQ0aqddYc57KeKib2J9uXVrCVDJS5XyV5P6xg/640?wx_fmt=png)

病毒执行流程

对此，火绒安全提醒用户不要轻易点击来历不明的邮件附件，火绒安全产品可对该病毒进行拦截查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6d7ibt4Qu2ics6ppKYLxuib1XWnQTosyEeuKd5JWkhhicTb8dQj74qELOFtg/640?wx_fmt=png)

查杀图

**一**

**样本分析**

**0****1**

**混淆手段**

该病毒启动后会率先执行一段shellcode，相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6djibPMvmzn05anPFXk7VozIhRdVf4c6EFGoJCQWiclv12mHN2weWOztaQ/640?wx_fmt=png)

执行shellcode

在shellcode中使用多种手段来对抗杀毒软件的查杀，如：控制流混淆、字符串混淆、API混淆等。控制流混淆，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6d60RfwsJicE4ibCoExDSY51bOCic2WLM7D9jiaURCnLekYoFR93ad6YhABA/640?wx_fmt=png)

控制流混淆

字符串混淆，每个字符串使用时，动态进行解密，并且每个字符串都有单独的解密函数，不同字符串解密函数对比，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dagEUvVS2iaVEm4NtS7aeONx6axmDrMK3Io3vgyuL4IRODiapLpqeWLtw/640?wx_fmt=png)

不同字符串解密函数对比

API混淆，在shellcode中会将用到的API地址加密并保存，使用时动态解密出来，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6ddKK21T4HH05dJWfnc5RbKgFicTF5bZRlxhkBOJqk0Z1qkRpN1mcziaibg/640?wx_fmt=png)

加密API地址

使用API之前会动态进行解密，利用位运算特性，每次解密的方法不同，但是结果一致，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dOfEoChicbFGgv18zRXyHhOeqdNIrjL8ia1xE7vCARHm41bupaWlObQtg/640?wx_fmt=png)

不同解密方式

**0****2**

**恶意行为**

获取本机的信息（用户名、计算机名、系统版本等）并发送给C&C服务器，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dBODz5xH4ULsZUczHIU46lficotmnTDGVVdxnpQ8VxRdo10Hb6kWd5xw/640?wx_fmt=png)

发送上线包

黑客可通过C&C服务器下发命令来执行各种恶意功能如：执行任意CMD命令、下发任意恶意模块、进程注入、获取系统进程信息、持久化等恶意功能，以下进行分析。

启动进程，该功能常被用于执行CMD命令，可执行C&C服务器下发的任意的恶意命令，相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dtiau1Uq4XJSibicpGed4QLKuPBTyibj6eaaHs8vjKtORWwd6ia4yKibyGiaRA/640?wx_fmt=png)

启动进程

该样本具备多种注入手段，一利用傀儡进程将恶意模块注入到其他进程中执行；二利用远程线程来在其他进程中执行恶意代码，傀儡进程注入，相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dGX138KqxMibmXmNBDnichH8uuRRKbIic5FhjeDxdnRPRBJnibgHHgNJWlA/640?wx_fmt=png)

傀儡进程注入

远程线程注入，相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6d5Ihk9H7SGy83ALp0f7pE4doH2IoyR7vIqxPzL7z8JZE1XNNuywIbKA/640?wx_fmt=png)

远程线程注入

获取系统进程信息，相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dNoKZIN4BJsEPj04qZ0h1H3tlNCVOPnTeb69ymvo4dDTrxFxwk5qLeA/640?wx_fmt=png)

获取系统进程信息

获取指定目录文件信息，相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6degulvBOcO45ICicJibnLk2I8icFGJpFyxGWoTVAhibKmlor8Oy4qnQFFFA/640?wx_fmt=png)

遍历目录文件

可通过添加服务来进行持久化，相关代码，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dMvQm5JkEZybtxrqA3doj21yfHQBwvMBd3EZ9XcwJayLUF6hP0axdQg/640?wx_fmt=png)

持久化

**二**

**附录**

C&C

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dSAskcwmj0krjPQrgA7ibVcRX3W4WKam3p6KqaQNGj1G4kYY6Sia5vicNg/640?wx_fmt=png)

HASH

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6dyIWibvWPjxWrPia8XvFZSL9xtRPjxoOamyZbnL7YB3DjNcK0MMicCibWpw/640?wx_fmt=png)

|  |  |  |
| --- | --- | --- |
|  |  |  |

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz48UWHKMxicuSHC5lOFq4d6daUcz6rBqZibpW9Y6r3jCQ7kfX30FYWtmLgkIjoAfficgmaWIoXB7CYicQ/640?wx_fmt=jpeg)

扫码关注

了解更多安全干货、资讯、以及火绒安全大事记

分享收藏点赞在看

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

火绒安全

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

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