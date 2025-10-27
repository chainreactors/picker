---
title: 快速演进中的僵尸网络Masjesu
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247500091&idx=1&sn=4bb6568abf2b66bc50530a0a59c45fdf&chksm=f9c1f232ceb67b244e284b82f8879e64e735dcec8545de44d099dc0ace0d5348d5e86b66bc66&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-07-20
fetch_date: 2025-10-06T17:44:32.694543
---

# 快速演进中的僵尸网络Masjesu

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwRlKdqFVL1beW3moFmHrzQpY2ljR8tfibAYD99SiaPwVOw36RDicOOS38Q/0?wx_fmt=jpeg)

# 快速演进中的僵尸网络Masjesu

360威胁情报中心

近期，360安全大脑监测发现有一类ELF样本正在大规模活跃中，VT上各杀毒引擎厂商普遍将其检出为Mirai僵尸网络，然而它的指令特征却与Mirai大相径庭，这不禁引起了我们的兴趣。经过人工分析后，我们确认这批样本隶属于Masjesu僵尸网络。

与各种泛滥的Mirai/Gafgyt僵尸网络变种不同，Masjesu是由背后团伙重新构建的一个新型僵尸网络家族，在样本层面和C2交互上均使用了加密算法隐藏信息，此外还在样本中加入了持久化机制，在C2通信流量上加入随机生成的冗余数据以混淆视听。

下文将分享我们对Masjesu僵尸网络的一些发现。

**时间线**

****2023-11****

Masjesu样本的早期版本进入我们视野

****2023-12-07****

伏影实验室发布相关分析报告[1]，将其命名为xorbot

****2024-01-18****

安全研究员 @synawk 在博客上发布了对Masjesu的恶意软件分析报告[2]

****2024-06****

Masjesu的更新版本开始大规模活跃，样本同步开启版本迭代

#

**攻击活动分析**

#

Masjesu僵尸网络的整体攻击流程图可以描述为如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwibwxIgzB7RUaIHoRjHDo9CFddnQTeMhqwElHZD2ATShHjLpgnvplOtQ/640?wx_fmt=png&from=appmsg)

攻击者通过22端口（SSH）弱口令爆破攻击入侵系统，往其中植入名为bins.sh的恶意shell脚本。脚本负责从C&C服务器上拉取以随机文件名形式存储的ELF文件到本地并执行，之后将其删除以防留下痕迹。ELF文件区分了x86\_64、arm、powerpc、mips、sparc、m68k等多种不同的架构：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLw1G9SeWmqf364qvTZXByIkgulMABZLZAw934paXzU3rqaQAdJZ4zNyw/640?wx_fmt=png&from=appmsg)

## **1.样本行为分析**

### **1.1.初始化准备工作**

ELF文件运行后，借鉴了Mirai的table机制，调用table\_init函数，然后通过addthis函数将各个加密字符串添加进table中。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwOI2bfVIoJFrCTjYOXlWJbLNMev53hfL2WyZpxwe5xicHVwBdyTfbEPQ/640?wx_fmt=png&from=appmsg)

在使用table[id]对应的字符串前，调用Decrypt函数对table[id]进行解密。后文将要描述的server端下发的指令，也需要首先经过同样的算法解密后再使用。具体的解密算法类似Mirai的多轮异或，待解密数据逐字节依次异或0x16、0x9F、0x08、0x00:

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLw7TUtLdGcOcJMOA64hCy0EKEKiaWbmGxNIrichnZAoQPAZuo6vDIiaibbxA/640?wx_fmt=png&from=appmsg)

各id对应的加密字符串经过解密后分别为：

|  |  |
| --- | --- |
| id | 字符串 |
| 2 | conn.masjesu.zip |
| 3 | 91.224.92.38 |
| 4 | 443 |
| 5 | /usr/lib/systemd/systemd-journald |
| 20 | /usr/lib/ld-unix.so.2 |
| 21 | /etc/crontab |
| 22 | /usr/lib |
| 23 | crontab -l |
| 24 | crontab - |

在crontabinit函数中，Masjesu尝试将自身文件移动为/usr/lib/ld-unix.so.2以方便伪装成系统文件，同时将条目"\*/15 \* \* \* \* /usr/lib/ld-unix.so.2\n"写入到crontab中来维持持久化：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwEupoDQicLKeSb8WQZX1pe5H37cEQ8HalbviafSF1iasf3WQ6sSXdzBE0A/640?wx_fmt=png)

Masjesu通过调用fuckothernets函数，将/tmp目录权限修改为仅所有者可读，防止其他僵尸网络进入系统分一杯羹：

**![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwjGtLjBicyzeXxZSbFTXrIP4hfVxRWjHuIWLoG1ZQZSykt9xGINYd1fg/640?wx_fmt=png)**

### **1.2.C&C通信**

在initC2函数中，Masjesu首先尝试与解密后的域名conn.masjesu.zip:443建立连接，若域名解析失败，则转为使用预定义的IP地址91.224.92.38:443作为C&C服务器。

与传统的僵尸网络家族不同，Masjesu在连接C&C后并不会主动发送上线包，而是先等待C&C服务器下发数据：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwmoib0iaxwWqPWtFMUI40EMMtiaBs4dHZWBIw2UfFpqNfQwpsYsSp2xMlA/640?wx_fmt=png&from=appmsg)

server端每次给bot受控端下发的数据，都需要使用前文描述过的异或算法进行解密，当其长度为0xAC, 0x68, 0x62, 0x40时，表明这是由server端随机生成的无意义数据，仅起到维持连接的作用。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwBslcjKhHIibXTwia2hvtU0dwnHnLs7icuibufSghnJnRNKEU9dQkXz7ukw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwhYD7hxIHNKicusPoWvnVpTBRmVcSHKF8NruibibBMMCM3PadeW8Ypjt6w/640?wx_fmt=png&from=appmsg)

而受控端在接收到server端的数据后，也需要相应地进行回复。Masjesu的做法是在[a-zA-Z0-9]中随机生成长度为71, 41, 95, 147的数据回复给server端。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLw6BLA2hB2FFfBVria9u4wJW4nJo0E4g8SSnAEmicOgynicr5h9fnAHMXRg/640?wx_fmt=png)

另外，根据bot版本的不同，受控端还可能在这段随机数据后附加上空格和对应的版本号。在较早期的bot样本中由于不携带版本信息因此无需进行附加，后来Masjesu陆续释出的1.01, 1.02, 1.03等等不同版本则都会带上对应的版本号。

### **1.3.指令结构**

当server端下发数据的长度不等于0xAC, 0x68, 0x62, 0x40时，表明这是一条具有实际意义的cmd指令。不同版本的Masjesu在具体的指令结构上有一些差异，此处主要对当前活跃版本的指令进行解析。首先对server端下发的指令使用异或解密，解密后的数据为使用空格分隔的多个子串，各个子串的含义如下：

|  |  |
| --- | --- |
| **子串index** | **说明** |
| 0 | 随机字符串  当其长度为999时，bot退出  当其长度为200时，bot发起DDoS攻击 |
| 1 | 随机字符串  根据其长度不同，发起不同类型的DDoS攻击 |
| 2 | 攻击目标（IP或网段） |
| 3 | 攻击时长 |
| 4 | 攻击payload长度 |
| 5 | 攻击目标端口（或端口范围） |
| 6（可选项） | 是否开启IP头部伪造 |

其中，第二个子串长度与DDoS攻击类型的对应关系如下：

|  |  |
| --- | --- |
| **子串长度** | **DDoS类型** |
| 21 | udp |
| 22 | handshake |
| 23 | vse |
| 24 | gre |
| 25 | rdp |
| 26 | ospf |
| 27 | icmp |
| 28 | igmp |
| 29 | protorand |
| 30 | tcp\_syn |
| 31 | tcp\_ack |
| 32 | tcp\_ackpsh |

例如下面是我们实际捕获到的一条解密后的攻击指令（受害目标已掩去）：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwJUZCYUZYUbQMu8lmQSdZ13SPCdIjNe89R6dyA3g9247ibeghhrg995g/640?wx_fmt=png&from=appmsg)

## **2.攻击趋势分析**

我们截取了7月份以来Masjesu僵尸网络的DDoS攻击统计数据，可以看到Masjesu日均打出100+的攻击事件，高峰时一天之内打遍全球近300个目标，从活跃程度上来看已经规模乍现：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwNKW4oC9ibAp92P2BS7anZhic2DicwrPQ2QQmO1sP3PsarwYj9CNX07XGA/640?wx_fmt=png&from=appmsg)

在受害目标区域分布上，中美以及欧洲地区遭受攻击的程度较为严重。所谓树大招风，这也与这些区域的互联网网络业务发展水平较高不无关系。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwNOhXADgvMQjBz9sTa8PVF4diawwibd7Cgu3ibInYnxj5SZveHibRfibcakQ/640?wx_fmt=png&from=appmsg)

#

**归属研判**

#

Masjesu僵尸网络背后的运营者，目前正以telegram频道作为平台来向用户出租DDoSaaS(DDoS as a Service)服务。该频道创建于2023-12-28，目前拥有700+的订阅用户。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqokexC3R2V64HqcAcqYiaLwZPZTQrV1iabEN1yK2VppFlzaXZsj7hd754zHOvhiaX8b6Lm4jWtibvXuQ/640?wx_fmt=png&from=appmsg)

#

##

**总结**

自从半年前被安全研究人员曝光以来，Masjesu僵尸网络非但没有就此沉寂，反而逐步发展出了稳定运营的DDoS出租业务，目前来看攻击者还有持续进行更新升级的计划，这值得引起社区的关注。我们也将会持续监控Masjesu的最新动向。

#

**附录 IOC**

#

* MD5:

**Shell**

b3e02cf0deea259ae9b0a2c7729ff4f8

6358554b451baff2abf04ecc0e99745e

d122fb147bf1d67dbed80bea6be302b9

3d1adb7fffb82818e7f9286357b64450

25f6c56317ddbfc0f6c60b36cd9d855f

**ELF（不带版本号）**

53e8840a549587e8185a88b126a6d106

c68da5dd71ff181e70cc17591d8bdee0

6d6f8c6af49de05906722f48ec54f76d

6627006e1509c21bf9cb8f6c68aa987e

**ELF（1.01）**

61892dd978dd22299ffa208cbcff029e

a94b12addda03cb1b427d25bc57356d6

afa045b6547f6ece9e021dff7f4998a2

efe40aec8d33c1424f5d48415e01eb48

**ELF（1.02）**

4ebf794e5a2d918262ad472278c77339

4f7be3e728c7e343b39fcd68702ac81e

7beac6c8a64fffe0dae12a21eb234b31

31f631e3553d94a54c4389b0d79dd259

**ELF（1.03）**

d60b48095ab97a18e98c03640eae173e

8761659a0de2b09bbad8dae70fdec303

45313ebd33c2a368d677ea0def1a6796

* C2:

conn.masjesu[.]zip:443

91.224.92[.]38:443

* IP:

37.44.238[.]67

95.214.27[.]134

95.214.27[.]138

91.224.92[.]38

**参考**

[1] [https://mp.weixin.qq.com/s/7iPxctbQqSH-qh9lC72-zQ](https://mp.weixin.qq.com/s?__biz=Mzg2Nzg0NDkwMw==&mid=2247491911&idx=1&sn=9046e12407ad960ac3d0dd326b8ba87b&scene=21#wechat_redirect)

[2] https://synawk.com/blog/masjesu-una-botnet-para-gobernarlos-a-todos-analisis-de-malware-0x3

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

360威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

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