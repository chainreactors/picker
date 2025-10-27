---
title: RotaJakiro后门与Buni后门关联性分析
url: https://buaq.net/go-138495.html
source: unSafe.sh - 不安全
date: 2022-12-05
fetch_date: 2025-10-04T00:30:33.301196
---

# RotaJakiro后门与Buni后门关联性分析

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/9608000da0a71fea4fa1f1c01521163b.jpg)

RotaJakiro后门与Buni后门关联性分析

本文为看雪论坛优秀文章看雪论坛作者ID：guyioo本文将根据360Netlab报告中提到的RotaJakiro后门特点以及微步报告中描述的Buni后门特点对二者关联分析。经分析，两种后门的相似之处如
*2022-12-4 18:11:38
Author: [mp.weixin.qq.com(查看原文)](/jump-138495.htm)
阅读量:24
收藏*

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HDGvMlPib6bpzxpPaNb91zHsFjUabjEDusDnHktUthC97ao1ZIzcPcc6DS6AnratDJze7vja5qib5w/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：guyioo

本文将根据360Netlab报告中提到的RotaJakiro后门特点以及微步报告中描述的Buni后门特点对二者关联分析。经分析，两种后门的相似之处如下：

1、单一实例

RotaJakiro通过文件锁来实现单一实例，具体实现如下图左所示。图右为Buni单一实例实现方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RjeU9JkzNGpBEmLeov6j1ibZTOjsWtOdICS0c5Y2CRlAJ9lNGKOhRPTQ/640?wx_fmt=png)

2、发包与收包

RotaJakiro后门将构造上线信息加密发送至C2，其中send函数如下：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RicCJH43UnMMomE0oibzAjZI9IWhchRM6AlFvrm510cia71bth0ic1tliaxA/640?wx_fmt=png)
同样的，recv函数也十分相似。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5R0f5biaj1hvpgDHLrB4SKjpEDKLBzF5u3bIIgsmskGw8px7SRCRbrLGA/640?wx_fmt=png)

然而，RotaJakiro与Buni的不同之处似乎更多。

1、C2解密算法

OceanLotus RotaJakiro样本中调用AES+Rotate Left解密C2，对抗技巧之一：使用stack strings obfuscation技术存储加密的敏感资源信息。其与解密相关的各种参数如下图所示，密文长度为32字节，明文长度为26字节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RAJh8LzYTMV6FIsZcj2CgM5oFK7iaibSZVSf4Z3xJrD3EH0mxEfBlgxiag/640?wx_fmt=png)
AES解密，其中aes\_dec的采用的是AES-256, CBC模式，key&iv都是硬编码。

Rotate为循环移位，此处使用的循环左移，其中移位的次数由plain\_len(明文长度)&7的值决定。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RsBerLh2ib8gdOwI7iaXacZBs1Gz8sHP8WWXxjcPgAZicFOw4hlUYc23pw/640?wx_fmt=png)
AES解密后得到以下“次级密文”：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RlV3Zw6ibYicAl4JuOHvWRNBFjFY9M1g49sH08QoicOdw4eBqUHiahjox1w/640?wx_fmt=png)
从次级密文中取出有效密文，其中有效密文从第8字节开始，长度为明文长度减8，此处即为26-8=18字节。

最后通过明文长度26可以计算26&7=2，得到移位的次数，将上述有效密文逐字节左移2位之后得到C2明文。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RrhfjbjveIia29rvmuicvSicicEff4pwMQSWPF3o2ibe2ehfkIZSCibFYiaMMA/640?wx_fmt=png)
而Buni后门中使用的C2加密算法为XOR。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RBAuQmRPTeoaFibCOJFv09UW22ZbibwnFP4auCpb9MN0qpb9ZYkyXgphA/640?wx_fmt=png)
与0xB1异或结果为 zabbixasaservice.com:443。

2、结构化流量/网络通信包

RotaJakiro的网络通信包由Head，Key，Payload三部分组成。其中header是必须的，长度为82字节，而body&payload部分是可选的。head&key采用的XOR&Rotate加密，payload采用AES&ZLIB加密压缩。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5Rxksut64ynCCsPCuRxjsGh0wV7icfRlWeDvvyIBVTibUAAzAQ4aDFqCLw/640?wx_fmt=png)

head通过逐字节左移3位，然后和0x1b异或进行解密。

解密后可得
offset 0x09, 4 bytes -> payload length
offset 0x0d, 2 bytes -> key length
offset ox0f, 4 bytes -> cmdi

key的长度为0x8字节，payload 的长度为0x20字节，要执行的指令码为0x18320e0，即上报设备信息。

key使用和head一样的解密方法，解密后作为AES的密钥来解密payload。

payload 使用解密后的key做为AES-256的密钥，以CBC模式解密，第8字节起即为ZLIB压缩数据，进行解压。

解压后做为新的AES密钥，配合参数解密样本中硬编码的加密指令。

最后发送至C2的数据包仍以上述结构组成，其中payload 经解密为上述指令执行的结果。

Buni则是通过逐字节recv接收的方式解析流量结构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RBaStZhibjxxbPibr2QaVWfYEdu3nHrVAE4XqMicHzM7ojEV9hFQsgfY1A/640?wx_fmt=png)
解析结果如下，要执行的指令码为0xdafe。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5R8LroicsoJ9lrBmf6qmrrjJOlTm7AniaVZPCYNHuIsyFeE0DX4vrZRXZw/640?wx_fmt=png)
Buni的通信流量特征与RotaJakiro相似度较低。

**进程伪装**

RotaJakiro进程伪装对root/non-root做了区分。

针对root用于伪装的文件名：/bin/systemd/systemd-daemon 或 /usr/lib/systemd/systemd-daemon

针对non-root：$HOME/.dbus/sessions/session-dbus 和$HOME/.gvfsd/.profile/gvfsd-helper

Buni 通过随机函数产生6-12的随机长度字符串，调用 prctl 函数设置随机进程名称，伪装成系统进程。

再来看RotaJakiro与2017年Palo Alto披露的海莲花macOS后门的相同之处。

1、C2会话建立函数

RotaJakiro与海莲花macOS后门均使用了相对小众的getaddrinfo()函数，Buni后门中则使用Linux常见的域名解析函数gethostbyname()。

2、上线包构造手法

RotaJakiro和海莲花的网络数据包都是由Head,Key,Payload三部分组成，其中Head是必须的，长度为82字节，而Key和Payload则是可选的。Head中的关键字段包括：

偏移1，DWORD类型，存放一个magic；

偏移9，DWORD类型，存放Payload长度；

偏移13，WORD类型，存放Key长度；

偏移15，DWORD类型，存放消息码。

RotaJakiro通过一个单独的函数初始化上线包的Head，海莲花样本中也存在一个专门初始化上线包Head的函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RYBzMSr90d8WEt7O7ByicChYF0IMongLoeia26EA1vJODSfWCFSUEAO4g/640?wx_fmt=png)
最终上线包如下，RotaJakiro与海莲花上线包明文结构一样，关键字段值基本相同。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RjHnmUJGYNjR6bzQ2ibicArGMz7IxpQfAibrBhEFzOjQNzo26p7ImLscCg/640?wx_fmt=png)
Buni上线包如下：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RMSeekT7pGKfnu1jy46rra7mA1JiaiaaAxj0SpVql09Wkvc9qh7Vdic9Xw/640?wx_fmt=png)

3、均存在rotate函数

RotaJakiro和海莲花都存在一个“rotate()”的函数，用于加/解密，Buni后门不包含该特征。

4、相同的指令码

RotaJakiro和海莲花都用DWORD类型的指令码来指定消息的功能，并且共享了多个语义相同的指令码。
Buni指令码为WORD类型，未发现指令码共享。

研究人员将Buni后门归因为海莲花的主要原因是其与RotaJakiro后门存在相似之处。

经分析，Buni后门与RotaJakiro后门的关联性较低，只有创建文件锁、发包与收包函数相似，在其他方面例如加解密算法：RotaJakiro样本中几乎没有明文存在，C2地址以及执行指令均经过加密，涉及到的算法包括动态AES、Rotate Letf、ZLIB，而Buni中的指令以明文硬编码存在，C2地址仅以异或加密，上线包特征，指令特征，持久化实现、进程伪装等方向均无重合之处，因此笔者认为Buni后门或不足以归因为海莲花。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWV01oTjDbjs2QibNSlnR5RP28KltRBD02YoCPIVSgDSH6MQzuEDWeEANfCvtf1YZwibbAU7J73kUw/640?wx_fmt=png)

**看雪ID：guyioo**

https://bbs.pediy.com/user-home-855355.htm

\*本文由看雪论坛 guyioo 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0XCHXZ3icZXcMlqrP9xKN6J9cwRouvpXMfRrRxdE0xCpPmeqybJGOPibw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458479751&idx=1&sn=ca684920ebd23cc09080ba6eefb94165&chksm=b18e5c0d86f9d51b3b31b8a99231416b78566b3365abfbe25625aeba78a44b769576548b316f&scene=21#wechat_redirect)

看雪2022KCTF秋季赛官网：https://ctf.pediy.com/game-team\_list-18-29.htm

**#****往期推荐**

1.[CVE-2022-21882提权漏洞学习笔记](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471430&idx=1&sn=6a47d0c5c8f3f6204548e80977ecd059&chksm=b18e7c8c86f9f59a88d9b8e83c8297e0ef65034a73436998ab835531baadaa51f3d630793b95&scene=21#wechat_redirect)

2.[wibu证书 - 初探](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471429&idx=1&sn=a85188de9b9697fd1b9e708bb8bb1fdb&chksm=b18e7c8f86f9f59933d6cbf0040ed796f06e37b23f17f1ae842eb22257de02338e1a8d751f6b&scene=21#wechat_redirect)

3.[win10 1909逆向之APIC中断和实验](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471421&idx=2&sn=e83cf7220dc1c4c06a2efc78593e30cc&chksm=b18e7b7786f9f2614ecce34e23be7f71a3d3516766aabda8f25ae41c81ef359a2c245503cf86&scene=21#wechat_redirect)

4.[EMET下EAF机制分析以及模拟实现](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468723&idx=2&sn=5a830d04185d80e1b6cfa639dc6c6c15&chksm=b18e71f986f9f8ef5b3c2fec51f69751e63a5d6bdbadf43b49728ba05606fc4ac63fda378c92&scene=21#wechat_redirect)

5.[sql注入学习分享](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468108&idx=1&sn=42c8ec155e13e3882cf4aeb60cdbb982&chksm=b18e0f8686f98690c9792298abb04dd243862ff8effd545dc668c7b1c682aaacf9797d899e97&scene=21#wechat_redirect)

6.[V8 Array.prototype.concat函数出现过的issues和他们的POC们](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468074&idx=2&sn=06eb27c1649bd4e3a3e43a46a9500add&chksm=b18e0e6086f9877644ba0de33658232f99213d1b1b074342260031cb529c1b7ad1b89b2e0204&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtk...