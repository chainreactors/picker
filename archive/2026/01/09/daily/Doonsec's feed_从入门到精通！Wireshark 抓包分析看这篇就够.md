---
title: 从入门到精通！Wireshark 抓包分析看这篇就够
url: https://mp.weixin.qq.com/s/FWt7Uobz3bZLn_hrI8JtpQ
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:26:00.050575
---

# 从入门到精通！Wireshark 抓包分析看这篇就够

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7iaECv1JGwFbicEZRkJY2WKOKaM2bxHU1OzsuUCFZiaF8ta1bqvKjvIuKA/0?wx_fmt=jpeg)

# 从入门到精通！Wireshark 抓包分析看这篇就够

易云安全应急响应中心

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtRPgfH7YtVL0yrce9mlgpJ7QrttS43eIGFhf3n3OEqzkoaNppbDcunJyNEmkE7qJ5gQ7GBweXNaHw/640?wx_fmt=png&from=appmsg)

**点击“蓝字”关注我们吧！**

一直以来，不少朋友问到抓包相关的，在我们弱电学习圈中，也有项目经理讨论到。

那么本期我们一起来详解抓包软件的使用与分析。

Wireshark的抓包与分析

WireShark是一个网络封包分析软件。网络封包分析软件的功能是撷取网络封包，并尽可能显示出最为详细的网络封包资料。Wireshark使用WinPCAP作为接口，直接与网卡进行数据报文交换。在网络封包和流量分析领域有着十分强大功能的工具，深受各类**网络工程师**和网络分析师的喜爱。

本文主要内容包括：

* 1、Wireshark主界面介绍。
* 2、WireShark简单抓包示例。通过该例子学会怎么抓包以及如何简单查看分析数据包内容。
* 3、Wireshark过滤器使用。通过过滤器可以筛选出想要分析的内容。包括按照协议过滤、端口和主机名过滤、数据包内容过滤。

我们首先来介绍一下Wireshark这款软件。![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCju81c3MObxq1189Ofy3XVJlrUAZJ0spsnMd7ByVByTWvia3jPX4xIBg/640?wx_fmt=jpeg&randomid=8mjdwsuk&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=0)

首先我们先认识一下这个软件的主界面是长这样的

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCMIiaHL6hpqvAQGgKOuNibDf1StO3RVOqmtl4d7MKqsPkNz0OzIlictpibQ/640?wx_fmt=jpeg&randomid=ag4fo500&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=1)

在这个界面中为Wireshark的主界面。

选择菜单栏上Capture -> Option，勾选WLAN网卡（这里需要根据各自电脑网卡使用情况选择，简单的办法可以看使用的IP对应的网卡）。点击Start。启动抓包。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCAUdOZOyI58XvicxnuN9ufliaGYtj0jgaJtQMHh2yoVGHGGDofrqicXcXQ/640?wx_fmt=jpeg&randomid=fwmjl3x7&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=2)

wireshark启动后，wireshark处于抓包状态中。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrC8m4qs5yWzQySeYJfFK878icG6U50OomdPKn6A60cIwevkfFpvJsHY6g/640?wx_fmt=jpeg&randomid=emman0ss&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=3)

1、执行需要抓包的操作，如ping www.baidu.com。

2、操作完成后相关数据包就抓取到了。为避免其他无用的数据包影响分析，可以通过在过滤栏设置过滤条件进行数据包列表过滤，获取结果如下。说明：ip.addr == 119.75.217.26 and icmp 表示只显示ICPM协议且源主机IP或者目的主机IP为119.75.217.26的数据包。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrC4hnS7BJaOwCgdBMibib8qK3YWVDmybpyU7wMia2XRzD1zaAPYWy0PhSmQ/640?wx_fmt=jpeg&randomid=ej9hkfxn&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=4)

3、wireshark抓包完成，就这么简单。关于wireshark过滤条件和如何查看数据包中的详细内容在后面介绍。

### Wireshakr抓包界面

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrChL0tDMiafFDDiaH2x0LXpTYFPuB4JASdv3SoZcshiauWFJ224aibdPWIrA/640?wx_fmt=jpeg&randomid=rmdh9i98&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=5)

说明：数据包列表区中不同的协议使用了不同的颜色区分。协议颜色标识定位在菜单栏View --> Coloring Rules。如下所示

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCD8BAQB9oMW26a6S9lA63IeBCqV9UJ9LuowgNmSV3ObTMBzynibhtibyg/640?wx_fmt=jpeg&randomid=j19tplwm&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=6)

WireShark 主要分为这几个界面

1. Display Filter(显示过滤器)， 用于设置过滤条件进行数据包列表过滤。菜单路径：Analyze --> Display Filters。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrChRb0fYibDLRmUE3mck4eCOMcg88zyYM9Z67qCfgYIKLtU3vBWqvXH4Q/640?wx_fmt=jpeg&randomid=lg0n1ux5&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=7)

1. Packet List Pane(数据包列表)， 显示捕获到的数据包，每个数据包包含编号，时间戳，源地址，目标地址，协议，长度，以及数据包信息。不同协议的数据包使用了不同的颜色区分显示。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCbOBUKFBqFjMPY7orOu9TNXmPC3TYD9fW3PFh2hzt4x77NibzmkMHlSw/640?wx_fmt=jpeg&randomid=qq912pkq&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=8)

1. Packet Details Pane(数据包详细信息), 在数据包列表中选择指定数据包，在数据包详细信息中会显示数据包的所有详细信息内容。数据包详细信息面板是最重要的，用来查看协议中的每一个字段。各行信息分别为

（1）Frame:   物理层的数据帧概况

（2）Ethernet II: 数据链路层以太网帧头部信息

（3）Internet Protocol Version 4: 互联网层IP包头部信息

（4）Transmission Control Protocol:  传输层T的数据段头部信息，此处是TCP

（5）Hypertext Transfer Protocol:  应用层的信息，此处是HTTP协议

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCsk7cDYtbwjqS3cfVBKWTd1mCBqFPtKbTneWyVaFAPU1JlGswq9HpWA/640?wx_fmt=jpeg&randomid=0dr7jaqg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=9)

TCP包的具体内容

从下图可以看到wireshark捕获到的TCP包中的每个字段。![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCp6a7ngzmMzjtPozgLcTG7WCJjj3qxwGE6F8Jc5PEiaS9ue3ib570Nd7Q/640?wx_fmt=jpeg&randomid=r00v4rpo&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=10)

1. Dissector Pane(数据包字节区)。

###

### Wireshark过滤器设置

初学者使用wireshark时，将会得到大量的冗余数据包列表，以至于很难找到自己自己抓取的数据包部分。wireshar工具中自带了两种类型的过滤器，学会使用这两种过滤器会帮助我们在大量的数据中迅速找到我们需要的信息。

（1）抓包过滤器

捕获过滤器的菜单栏路径为Capture --> Capture Filters。用于在抓取数据包前设置。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCpH34ibdEuJDRzlb1MrKp3aXdZG6wJMBntQhotSviaoUxhvziblxJEGibZQ/640?wx_fmt=jpeg&randomid=70omy237&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=11)

如何使用？可以在抓取数据包前设置如下。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCxYtSXoicEDEJFiagjcoTSo6hO2ibsPvrmG9huJhFQtxjmV1k0L3b6qMeA/640?wx_fmt=jpeg&randomid=as8ng6yu&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=12)

ip host 60.207.246.216 and icmp表示只捕获主机IP为60.207.246.216的ICMP数据包。获取结果如下：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrC22Smibw4DSIWJIic6HiaqeuMwLYmN2GHzyUEIgR6nCtOalSpfFnibYZNGQ/640?wx_fmt=jpeg&randomid=os0cfpd3&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=13)

（2）显示过滤器

显示过滤器是用于在抓取数据包后设置过滤条件进行过滤数据包。通常是在抓取数据包时设置条件相对宽泛，抓取的数据包内容较多时使用显示过滤器设置条件顾虑以方便分析。同样上述场景，在捕获时未设置捕获规则直接通过网卡进行抓取所有数据包，如下

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCpEAHkBm0FjJ80mUibBbk5icG9XxBAU4DsdRibRLFG2j942puVrSOUwAJw/640?wx_fmt=jpeg&randomid=apq7d893&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=14)

执行ping www.huawei.com获取的数据包列表如下

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCprAbBmyABF4Gfxal0uibicxXHJEnSbOJlSCMiaYqibRl1RiaJ3icxcnTwehg/640?wx_fmt=jpeg&randomid=n0lyh6qr&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=15)

观察上述获取的数据包列表，含有大量的无效数据。这时可以通过设置显示器过滤条件进行提取分析信息。ip.addr == 211.162.2.183 and icmp。并进行过滤。![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCPlrfTg4SzHNGaDtzsiaMWNLuoaEa6xhHbGcPRK4dA68JbYYibwn8OP0Q/640?wx_fmt=jpeg&randomid=8r54m754&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=16)

上述介绍了抓包过滤器和显示过滤器的基本使用方法。在组网不复杂或者流量不大情况下，使用显示器过滤器进行抓包后处理就可以满足我们使用。下面介绍一下两者间的语法以及它们的区别。

wireshark过滤器表达式的规则

1、抓包过滤器语法和实例

抓包过滤器类型Type（host、net、port）、方向Dir（src、dst）、协议Proto（ether、ip、tcp、udp、http、icmp、ftp等）、逻辑运算符（&& 与、|| 或、！非）

（1）协议过滤

比较简单，直接在抓包过滤框中直接输入协议名即可。

TCP，只显示TCP协议的数据包列表

HTTP，只查看HTTP协议的数据包列表

ICMP，只显示ICMP协议的数据包列表![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCibtKBRGGNicUc5oUia0HSUJ1iafdkLflTia1O7GRWaTG35bOiaqEk8n5uuJA/640?wx_fmt=jpeg&randomid=acucczo7&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=17)

（2）IP过滤

host 192.168.1.104

src host 192.168.1.104

dst host 192.168.1.104

（3）端口过滤

port 80

src port 80

dst port 80

（4）逻辑运算符&& 与、|| 或、！非

src host 192.168.1.104 && dst port 80 抓取主机地址为192.168.1.80、目的端口为80的数据包

host 192.168.1.104 || host 192.168.1.102 抓取主机为192.168.1.104或者192.168.1.102的数据包

！broadcast 不抓取广播数据包

2、显示过滤器语法和实例

（1）比较操作符

比较操作符有== 等于、！= 不等于、> 大于、< 小于、>= 大于等于、<=小于等于。

（2）协议过滤

比较简单，直接在Filter框中直接输入协议名即可。注意：协议名称需要输入小写。

tcp，只显示TCP协议的数据包列表

http，只查看HTTP协议的数据包列表

icmp，只显示ICMP协议的数据包列表

（3） ip过滤

ip.src ==192.168.1.104 显示源地址为192.168.1.104的数据包列表

ip.dst==192.168.1.104, 显示目标地址为192.168.1.104的数据包列表

ip.addr == 192.168.1.104 显示源IP地址或目标IP地址为192.168.1.104的数据包列表

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCYYALicKribm3oReoGMkgoDaYueG6paW8HpibribKNRt9zZxgQV0psvFlYA/640?wx_fmt=jpeg&randomid=7sve0nfl&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=18)

（4）端口过滤

tcp.port ==80,  显示源主机或者目的主机端口为80的数据包列表。

tcp.srcport == 80,  只显示TCP协议的源主机端口为80的数据包列表。

tcp.dstport == 80，只显示TCP协议的目的主机端口为80的数据包列表。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCbhgO44nj2vS4By0UicBUB6UUrasE55065NtgAMzPms8DCY9QkYdkTVA/640?wx_fmt=jpeg&randomid=738a9rom&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=19)

（5） Http模式过滤

http.request.method=="GET",   只显示HTTP GET方法的。

（6）逻辑运算符为 and/or/not

过滤多个条件组合时，使用and/or。比如获取IP地址为192.168.1.104的ICMP数据包表达式为ip.addr == 192.168.1.104 and icmp

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1cZiaCeD3MkS28Mct9BLypOLt95vZwNrCniaUibydX8icDEOuTTjdIkHwQ1FaOUYkrKNZwx4UZhp6cuUriaiaa3h84rg/640?wx_fmt=jpeg&randomid=ktgpmjxq&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=...