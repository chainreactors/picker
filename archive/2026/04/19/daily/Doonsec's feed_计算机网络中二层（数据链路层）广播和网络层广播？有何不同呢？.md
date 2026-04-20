---
title: 计算机网络中二层（数据链路层）广播和网络层广播？有何不同呢？
url: https://mp.weixin.qq.com/s/J3pBOFgx0IZw53NuUFnfQw
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:54:23.328514
---

# 计算机网络中二层（数据链路层）广播和网络层广播？有何不同呢？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JQNVqWAicEnmcPqgCyXySqYG8T7FMuohLV7sZVWhRgJkmoS3n8kI0M2Cr2eTVYWPTfnOdGpV8wyvex4GiabVod6ynOhAib6wJdEmpmFicpAvxGA/0?wx_fmt=jpeg)

# 计算机网络中二层（数据链路层）广播和网络层广播？有何不同呢？

原创

车小胖谈网络
车小胖谈网络

车小胖谈网络

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**关于数据链路层和网络层广播的一些疑问：**

**![Multiple IP subnets over single L2 broadcast domain.](https://mmbiz.qpic.cn/sz_mmbiz_png/JQNVqWAicEnlyANpElfK8DAmXnWbXN5rSGxX4QVG0qX20KJdd4lGS4HnBNcKwh7zibpkdG00P17BFLkCZkzhYo0VFlcOKIkeSOuiatFEt085uw/640?wx_fmt=png&from=appmsg)**

**Q1: 两层的广播不都是同一网段都可以接受吗，为什么两层都要有广播呢，有什么不一样呢？**

**二层（Level 2）广播**

典型代表是**ARP**，集成在**Kernel** coding里。

L2 Destination Address = **ff-ff-ff-ff-ff-ff**

无论是ARP的请求方（**Requester**），还是ARP的响应方（**Responder**），都不需要额外的**application**。

ARP广播必须扩散到广播域内每一台host。如果被广播域被某些技术诸如**VxLAN**、**L2 MPLS**、**VLAN Tunnel**分割，则需要使用对应的**VxLAN Tunnel、L2 MPLS Tunnel、VLAN Tunnel**进行扩散。但是无论如何扩散，ARP原始区域、扩散区域依然是同一个网段、同一个广播域。如同孙大圣蹦得再欢，也无法跳出如来佛掌。

比如一个广播域10.1.1.x/24，分别位于北京、上海、广州被VxLAN云分割，理论上任何一个地方主机发出的ARP广播，都需要蔓延到北京、上海、广州。但是它们的网段都是10.1.1.x/24。

**三层（Level 3）广播**

典型代表是**DHCP**，处于 **User** coding里。

L2 Destination Address = **ff-ff-ff-ff-ff-ff**

L3 Destination Address = **255.255.255.255**

无论是DHCP的请求方（**Requester**），还是DHCP的响应方（**Responder**），都需要额外的**application**。

三层广播，具有二层广播的一切特征(**VxLAN****、L2 MPLS、VLAN Tunnel云**)。但是三层广播可以使用DHCP Relay这个角色，将DHCP Discovery广播报文传输到一个完全不同网段的DHCP Server上。

去向通过将L3 Destination Address = **255.255.255.255 ----> DHCP Server IP**

反向通过将L3 Source Address =**DHCP Server IP****----> 255.255.255.255**

**Q2：当主机向DHCP服务器发送discovery类型的报文的时候，此时目的地址是广播(255.255.255.255)，那么这个时候，将这个广播包发送出去，封装的帧中目的地址也是广播（ff-ff-ff-ff-ff-ff）吗？**

是的。

但是，一旦DHCP Client成功获取IP地址之后，会记忆DHCP Server的IP。

当续租的时候，无需再discovery、offer、request、ack 4次消息交换。

而只需要request、ack 2次消息交换，即可续租IP。

既然已经知晓DHCP Server的IP，为何还要discovery广播？

很显然，如果将DHCP报文直接封装在Ethernet二层头，request、ack 2次消息交换是不可能完成的任务。但是封装在三层IP + UDP头上，**request、ack 2次消息交换却是可能完成的任务！**

如关机重启，记忆的DHCP Server的IP内存会释放，依然需要4次消息交换。

二层（Level 2）广播，还有一个常见的应用，**PPPoE**，处于 **User** coding里。

L2 Destination Address = **ff-ff-ff-ff-ff-ff**

无论是**PPPoE****Client**，还是**PPPoE****Server**，都需要额外的**application**。

如果想将PPPoE传输得更远，可以使用**L2TP**、**PPTP**Tunnel技术。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7IBfTjcqbuXUVID3tibfKK56ribvLtXSHLOE3soDPPM8cLgPnqc5jBNG3XrBcfPrdj5h6rs2qF7mHSD1dSo4ZHxA/0?wx_fmt=png)

车小胖谈网络

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