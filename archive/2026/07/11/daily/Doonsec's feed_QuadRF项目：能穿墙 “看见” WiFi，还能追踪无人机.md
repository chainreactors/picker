---
title: QuadRF项目：能穿墙 “看见” WiFi，还能追踪无人机
url: https://mp.weixin.qq.com/s/F1ewM24x50cXXmuQ59CHfw
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:06:22.636968
---

# QuadRF项目：能穿墙 “看见” WiFi，还能追踪无人机

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqr0yrcv3JxvDV8sAYrW2pvTmmPCicAVnvHl1xulw38MI5giahn6uom2449Q0LWaSJ6Ck4QrKTiaIGCGUTS3SdMYMQOGCn518vsag/0?wx_fmt=jpeg)

# QuadRF项目：能穿墙 “看见” WiFi，还能追踪无人机

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

QuadRF是一款以树莓派 5 和**FPGA**为核心打造的**相控阵无线电设备**（由多个独立天线单元组成，通过精准控制信号相位实现定向收发），时序控制精度可达**皮秒级**（1 皮秒为万亿分之一秒，是实现精准波束控制的核心前提），可完成高级信号处理与**波束成形**（调整多天线信号相位，让波束在特定方向叠加增强的技术）。它既能穿墙探测 WiFi 信号，也能追踪飞行中的无人机。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqBKicfekCXbdGDBOYEP69fjU32aG3yvdKlUbG6sWx1fDHAGer0J1bHBfkVKyy5rBeibjmSicHEuRPrkhVGpWg3shPzU9sY1lQwpw/640?wx_fmt=jpeg&from=appmsg)

当用户将电脑接入网络时，用**Wireshark**这类工具就能看到所有可能从未察觉的隐藏流量。WiFi 数据包也是同理，只不过它们在空气中传输，无需物理接触就能被窃听。QuadRF 自带的软件可以实现射频信号的流式传输与解码，还可以将数据导出到性能更强的电脑上，开展 WiFi 流量分析之类的工作。

吉尔林在全球知名硬件极客社区**Hackaday**上发现 QuadRF 之后，联系到了该设备的开发者马丁・麦科密克。

QuadRF 只是马丁主导的一个更大项目的组成部分：

他正在打造一套月球级别的天线阵列，可用于**EME（地球 - 月球 - 地球通信，又称月球反射通信，以月球为天然信号反射面实现超远距离无线电传输）**实验和**射电天文学**（通过接收天体无线电波观测宇宙的天文学分支）研究。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDoKH0LdTTAYkJ6HOrXG6KCn8AHSicyndrMOBiaDREP2RpnuvDqrBQy1u9Tg7aVx5wReh5grc7IBD8AcHq84j0d7GB57DW8K5vIKU/640?wx_fmt=jpeg&from=appmsg)

在吉尔林看来，马丁的设计灵感源自 SpaceX 的初代星链终端**Dishy**（因圆盘外形得名，是消费级相控阵卫星天线的代表产品）， 这也合情合理，毕竟马丁曾在 SpaceX 就职，正是 Dishy 研发团队的一员。

这套相控阵天线系统没有被锁死在专属卫星系统里，理想情况下，持有执照的操作人员可以将多台 QuadRF 模块串联起来，开展各类新奇的无线电实验，

**EIRP（等效全向辐射功率，衡量射频系统定向发射能力的核心指标）**最高可达 1.15 兆瓦，也就是增益极强的定向天线，可实现大功率射频实验。

而 QuadRF 是缩小后的手持版本，功率还不足以把信号发射到月球，但在本地**SDR（软件定义无线电，用软件替代传统硬件电路实现射频信号处理，仅需更换软件即可适配不同频段与协议）**应用、射频环境可视化场景中依然相当实用，至少在它支持的 4.9-6GHz **C 波段**（无线电频谱中 4-8GHz 的频段，广泛用于 WiFi、卫星通信、气象雷达等场景）内表现出色。

## QuadRF 实测体验

吉尔林特意询问马丁，能否寄来一台 QuadRF 原型机，供他和父亲一同测试， 他的父亲是一名退休的广播无线电工程师。此前他已在垂直硬件众筹平台**Crowd Supply**上预订了基础套件（售价 499 美元），但他希望亲身体验验证，QuadRF 是否真如 ScaleRF 发布的演示视频中那般实用、易上手。

评测结论显示，这款设备的用户界面仍有粗糙之处，但实际表现令吉尔林十分惊艳，尤其是所有运算均在树莓派 5 上运行的前提下。设备开机后，树莓派会启动并创建一个 WiFi 热点。用户连接该热点后访问 `http://quadrf/`，页面会在浏览器内运行一个**VNC（虚拟网络计算，可通过网络访问其他设备图形化系统界面的远程桌面协议）**会话，可从中启动**GNU Radio**（SDR 领域主流的开源开发框架，提供模块化的信号处理工具）、各类 SDR 软件，甚至还有团队定制的**AR（增强现实，将虚拟信息叠加到现实画面中的技术）**射频可视化工具。

这款 AR 可视化工具是所有自带软件里最具新意的部分，尽管在实际 SDR 应用中的实用性不算最高。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqjwYJHthQZwjbCceSU252Cro7q3GXSJUjyjPYwwvqM9Fm5Km964nibeqjmGsRsSrl3Tmx1XoxEHUy4En0z68hibfMicsbvk96suY/640?wx_fmt=jpeg&from=appmsg)

设备界面完成度不算高，但用户可以调整摄像头和相控阵的对齐位置，也能调节接收器**增益**（衡量天线对特定方向信号的放大接收能力，增益越高，对远距离弱信号的捕捉能力越强）。调整完成后，设备会将 4.9-6GHz 频段的信号可视化成彩色 “光斑”。这个早期版本的界面上没有显示数值刻度，但吉尔林在工作室周围测试时，工作室的 5GHz WiFi（工作在 100 信道，约 5.5GHz）显示为浅蓝色，邻居的 WiFi 网络则显示为红色或绿色。如果选购移动扩展包，套装内包含电池组和手持手机支架，用户可以手持设备四处走动，实时分析 C 波段的部分频段。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqIxz4hc3EVSEsoomAN6bJfTvAGbmGEv3n8w4OtoiaHXWuicQ0vTibAm2zwurq5JOYnXZAZRcldzbX84bSMhoKTvvgyibTS2ljTOz0/640?wx_fmt=jpeg&from=appmsg)

吉尔林与父亲将大疆 Mini Pro 4 无人机飞到工作室后方，QuadRF 毫不费力便识别出了空中的无人机。无人机飞远后，吉尔林需要调高增益才能持续追踪信号；他认为如果能加入**AGC（自动增益控制，可根据信号强度自动调整放大倍率，保持输出信号稳定的功能）**，或是优化增益调节的操作逻辑会更好，毕竟手持这套设备移动时，界面操作略显笨重。据介绍，本次众筹的反响远超预期，后续量产产品的外壳会改为注塑成型（吉尔林拿到的原型版本为 3D 打印外壳）。

## 树莓派 5 MIPI 接口：赋能高带宽射频传输

令吉尔林颇感兴趣的一项设计是，设备利用树莓派的**MIPI（移动产业处理器接口，原本用于连接摄像头、显示屏的高速串行接口，具备高带宽、低延迟的特点）**通道，实现低延迟 SDR **I/Q（同相 / 正交信号，SDR 领域的通用信号格式，用两路相位差 90° 的信号表征射频信号的幅度与相位）**信号流传输，数据速率超过 5Gbps。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDoeQKbWic7awruPgxLKjjaglmqbLBn1a34b0icKibu3hwJuazf7WQdyxap9fRGejk0chIJNKUBq76uMbojicCIvsEoRGmicwF9DEPh4/640?wx_fmt=jpeg&from=appmsg)

根据 QuadRF 官方文档的介绍（scalerf.com/docs/）：

通过树莓派的摄像头和显示屏 FFC（柔性扁平线缆，薄型易弯折的设备内部连接线）的 MIPI 接口传输 I/Q 信号是一种全新的方案，优势十分突出。MIPI 接口通过树莓派的**RP1 芯片**（树莓派 5 搭载的定制南桥芯片，负责处理绝大多数外设接口的传输）实现，支持超过 5Gbps 的低延迟全双工数据传输。它比 USB 更简单可靠，几乎不会给射频板增加额外硬件成本，还能稳定支持数百**MSPS（每秒百万采样，衡量信号采样速率的单位，数值越高，设备可处理的信号带宽越宽）**的 I/Q 信号传输，不会出现卡顿或采样丢失。摄像头和显示屏本身就是高带宽信号流式传输的典型应用，它们的标准数字接口适配 SDR 场景自然是水到渠成。

为了实现这一功能，研发团队对树莓派 5 的 MIPI 协议进行了逆向工程（因为信号需经过 RP1 芯片）。按照这套架构，用户可以将多台 QuadRF 模块串联起来，每台模块可独立计算自身的相位偏移。吉尔林尚不确定该设计的实际落地效果，但认为其思路相当巧妙。**PCIe（通用高速扩展总线，常用于外接固态硬盘、高速网卡等高性能外设）**接口在应急场景下也能实现类似功能，但 QuadRF 的这套方案将 PCIe 接口空余出来，用户可以外接高速存储设备，或是搭配比树莓派自带接口速率更高的网卡。

往期：[安卓17 IonStack全链路0day漏洞利用链](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451187608&idx=1&sn=d0397197cbc8664d3cdba598ba15c196&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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