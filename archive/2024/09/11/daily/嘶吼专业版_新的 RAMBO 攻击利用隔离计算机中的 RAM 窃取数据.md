---
title: 新的 RAMBO 攻击利用隔离计算机中的 RAM 窃取数据
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247577888&idx=1&sn=cfb6c0ff1f4f7265e8691b474dee4fc1&chksm=e914611ade63e80c991084d049b2238e45009b443d2bb69f875e4db551213f0ecdc1efa469a9&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-09-11
fetch_date: 2025-10-06T18:29:39.146159
---

# 新的 RAMBO 攻击利用隔离计算机中的 RAM 窃取数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibwbNL2nnR0VXVRPatSwTCk0UPuW7wic05vxezR9BViczbDYh4PLu1ehJdKeQ4r75cibbKLWgzv30xhQ/0?wx_fmt=jpeg)

# 新的 RAMBO 攻击利用隔离计算机中的 RAM 窃取数据

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一种被称为“RAMBO”（用于进攻的隔离内存总线辐射）的新型侧信道攻击会从设备的 RAM 产生电磁辐射，以从隔离的计算机发送数据。

隔离系统通常用于对安全性要求极高的任务关键型环境，例如政府、武器系统和核电站，这些系统与公共互联网和其他网络隔离，以防止恶意软件感染和数据盗窃。

尽管这些系统没有连接到更广泛的网络，但它们仍然可能受到通过物理介质如USB 驱动器，引入恶意软件感染或发起复杂供应链攻击。

该恶意软件可以秘密操作，以调制隔离系统的 RAM 组件，从而允许将机密从计算机传输到附近的接收者。属于此类攻击的最新方法来自以色列大学的研究人员，由 Mordechai Guri 领导，他是隐蔽攻击渠道方面经验丰富的专家，曾开发出使用网卡 LED、USB 驱动器 RF 信号、SATA 电缆和电源泄漏数据的方法。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibwbNL2nnR0VXVRPatSwTCk0ZqdkFrQRGSy06s3HqERibZXlFhricKicUvSJgyhlAPlYwLx6kCiaF7PEA/640?wx_fmt=png&from=appmsg)RAMBO 攻击如何运作

为了实施 Rambo 攻击，攻击者会在隔离的计算机上植入恶意软件，以收集敏感数据并准备传输。它通过操纵内存访问模式（内存总线上的读/写操作）从设备的 RAM 产生受控的电磁辐射来传输数据。

这些发射本质上是恶意软件在 RAM 内快速切换电信号（开关键控“OOK”）的副产品，该过程不会受到安全产品的主动监控，也无法被标记或停止。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibwbNL2nnR0VXVRPatSwTCkAtVnEx7C7riaia0w7S1vo7dCiaysltvPiau1CdPBqb6VKnYneufTmFZNFA/640?wx_fmt=png&from=appmsg)

执行 OOK 调制的代码

发射的数据被编码为“1”和“0”，在无线电信号中表示为“开”和“关”。研究人员选择使用曼彻斯特编码来增强错误检测并确保信号同步，从而减少接收端出现错误解释的可能性。

攻击者可能会使用带有天线的相对便宜的软件定义无线电 (SDR) 来拦截调制的电磁辐射并将其转换回二进制信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibwbNL2nnR0VXVRPatSwTCkNvmc4lbicILODXNLAAtmiaiacTBL3c9PJOW42ExzRJuAoQMDBv3b9PWlQ/640?wx_fmt=png&from=appmsg)

单词“DATA”的EM信号

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibwbNL2nnR0VXVRPatSwTCk0ZqdkFrQRGSy06s3HqERibZXlFhricKicUvSJgyhlAPlYwLx6kCiaF7PEA/640?wx_fmt=png&from=appmsg)性能和限制

RAMBO 攻击的数据传输速率高达 1,000 比特每秒 (bps)，相当于每秒 128 字节，或 0.125 KB/s。

按照这个速率，窃取 1 兆字节数据大约需要 2.2 小时，因此 RAMBO 更适合窃取少量数据，如文本、按键和小文件。

研究人员发现，在测试攻击时可以实时进行键盘记录。但是，窃取密码需要 0.1 到 1.28 秒，窃取 4096 位 RSA 密钥需要 4 到 42 秒，窃取小图像需要 25 到 250 秒，具体取决于传输速度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibwbNL2nnR0VXVRPatSwTCkDDcb4fBPWticSv8bm4pHZFRDV6mKvRObNIreolYgXPkiasU71cqWvAqw/640?wx_fmt=png&from=appmsg)

数据传输速度

快速传输的最大范围限制为 300 厘米，误码率为 2-4%。中速传输可将距离增加到 450 厘米，同时误码率相同。最后，误码率几乎为零的慢速传输可以在长达 7 米的距离内可靠地工作。

研究人员还尝试了高达 10,000 bps 的传输，但发现任何超过 5,000 bps 的速度都会导致信噪比非常低，从而无法进行有效的数据传输。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibwbNL2nnR0VXVRPatSwTCk0ZqdkFrQRGSy06s3HqERibZXlFhricKicUvSJgyhlAPlYwLx6kCiaF7PEA/640?wx_fmt=png&from=appmsg)阻止 RAMBO

Arxiv 上发表的技术论文提供了几项缓解建议来减轻 RAMBO 攻击和类似的基于电磁的隐蔽通道攻击，但它们都引入了各种花费开销。

建议实施严格的区域限制以增强物理防御、RAM 干扰以破坏源头的隐蔽通道、外部 EM 干扰以破坏无线电信号，以及法拉第外壳以阻止气隙系统向外发出 EM 辐射。

研究人员针对虚拟机内运行的敏感进程测试了 RAMBO，发现它仍然有效。然而，由于主机内存容易与主机操作系统和其他虚拟机发生各种交互，攻击可能会很快被阻止。

参考及来源：https://www.bleepingcomputer.com/news/security/new-rambo-attack-steals-data-using-ram-in-air-gapped-computers/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibwbNL2nnR0VXVRPatSwTCkdShicpF5BJsQG0yqFp6p22HOphToib1ObjrFJqZK0ZEnqEB0ZCnc9qaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibwbNL2nnR0VXVRPatSwTCkapicb6QbaR076kq4ves0ljEnqlFv8cKV9KpoVuQMSZicV7SlGdsqC6eA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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