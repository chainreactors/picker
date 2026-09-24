---
title: 关于我对socket的理解，不知道正确与否？
url: https://mp.weixin.qq.com/s/eUDl5d00XtG16DaU6zKPyg
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:01:22.834293
---

# 关于我对socket的理解，不知道正确与否？

# 关于我对socket的理解，不知道正确与否？

原创

车小胖谈网络
车小胖谈网络

车小胖谈网络

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**看了很多关于**socket的文章，也整合了不同文章的描述，对于它有一个自己的认识，不知道对不对，想请教一下各位。socket是一个对tcp/ip这个网络通讯协议栈的全面封装与实现。就是说协议是一个概念，是一种规范和约定俗成的东西，我想要操作和应用这些协议，那它必须要有一个实现，socket就是这个实现，通过使用socket的一系列api,比如说connect,write,read 它能够依照tcp/ip的规范实现网络通讯。即socket是成对出现的，客户端一个socket,服务端一个socket,通过对它的一系列操作来实现tcp/ip的规范的功能。即socket连接也就是tcp连接的实现。我们在平时开发的过程中，关于网络通讯，其实本质封装的就是socket。因为tcp/ip是协议，协议是概念，具体实现的还是socket。

![](https://mmbiz.qpic.cn/mmbiz_png/JQNVqWAicEnlx2WXpgxUYLk7nRoiavvQOnfVsCzsqjkEvhoMPGtl11jQvJTibSKwoRdpud0icb3E0brP2JN97x1Lzn98JUn74YVLxvDJRdMHu6s/640?wx_fmt=png&from=appmsg)

现代socket的概念来自于**BSD** socket，即使没有TCP/IP，socket照样可以使用其它的协议通信。socket支持**40**多种**Address Family**，**IPv4**，**IPv6**仅仅是其中的2员。

Socket成对出现只是一种常见的组合。还有不太常见的组合，比如1个组播源socket在推送电视节目，N个组播接收socket在接收组播packet，这种就是1:N的关系。

在本机上Ping 1.1.1.1， 也使用socket。但只在本机创建了socket实例，被ping的主机1.1.1.1上并没有为这个ping创建任何socket实例，这种就是1：0的关系。

无论使用TCP还是UDP，(**destination ip == source ip**) && (**destination port == source port**) 为**TRUE**的情况，其实就是socket与自己的通信。广义上虽然也是1：1的映射，狭义上这里只有一个socket实例。Data在socket write queue与socket receive queue里搬迁。左口袋进，右口袋出。

究竟socket与TCP/IP是什么关系，进入剧场观看。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7IBfTjcqbuXUVID3tibfKK56ribvLtXSHLOE3soDPPM8cLgPnqc5jBNG3XrBcfPrdj5h6rs2qF7mHSD1dSo4ZHxA/0?wx_fmt=png)

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