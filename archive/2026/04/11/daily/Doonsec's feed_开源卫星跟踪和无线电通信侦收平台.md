---
title: 开源卫星跟踪和无线电通信侦收平台
url: https://mp.weixin.qq.com/s/bFvLoVNGkKZVhcEsQWzf8g
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:44:32.221779
---

# 开源卫星跟踪和无线电通信侦收平台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TRfiawmTBsXaKacicq9vJOalA1jHBclUCm9NVhDvcN2icyxhIZFcxcNRLDeT0QZocAJq62qPWKFicm6JR5CriaMepBdWPXhoXZqw20ycWmz8tZyA/0?wx_fmt=jpeg)

# 开源卫星跟踪和无线电通信侦收平台

原创

少钧
少钧

OSINT情报世界

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

****![](https://mmbiz.qpic.cn/mmbiz_png/TRfiawmTBsXa3p1DR5vwbJUVpSuryx3ZZLN2ORN8BWhmo0jtAlGUichKWzic2jqcNnoI6nWcMzevef6bicljZstWbNhmfSquPfGI882ag1JnxzY/640?wx_fmt=png&from=appmsg)

账号调整通知：由于原公众号“开源情报俱乐部”无法使用，后续所有境外组织机构及OSINT相关内容改为此号分享。**

**培训通知：**2026年5月网络情报分析实战技能培训与CISAW认证时间为5月18-5月22日。需要系统化提升OSINT实战技能的朋友请添加微信号（osintclub007）咨询详细课程内容与安排。**

---

这是一款功能齐全的开源软件解决方案，用于卫星跟踪和无线电通信。它专为业余无线电爱好者、卫星发烧友和研究人员设计，提供了一个全面易用的平台，用于监测航天器、控制无线电设备以及接收来自卫星的实时无线电信号。

它打破了传统业余无线电界软件碎片化的痛点，将高精度轨道模型（TLE）、硬件天线伺服控制、软件定义无线电（SDR）集成、自动多普勒频移校正、以及信号解码全部收束于一个基于Web的现代化响应式仪表盘中。更关键的是，它集成了AI实时语音转写与无人值守的自动化侦收任务调度功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TRfiawmTBsXZB0hvvRqE1M9x1I7Ak6fwwibhXFhS2icYlDLJbg387cSaukW6S0BDCRJgy9jhvuBHdhBMKOyp8zjV5qgzSXNcuVHSYJywL9NS8E/640?wx_fmt=png&from=appmsg)

从战略生态来看，这个工具代表了太空监测能力的彻底下沉与平民化。

过去，要完成“预测卫星过境->控制天线对准->抵消多普勒效应->录制IQ数据->解码遥测信号/气象云图”这一完整闭环，需要极高的技术门槛和多套系统的繁琐串联。该工具通过自动化的任务流，将上述过程压缩为“一键部署”。这意味着，任何非国家级的民间组织、研究机构甚至是个人，只需极低的硬件成本（如几百元的RTL-SDR接收机和一台树莓派），就能建立起一个具备军用级自动化监控逻辑的全球太空资产侦收节点。

Ground Station系统支持SigMF格式的宽带IQ原始数据记录，并能自动化地对大量卫星频段进行扫海与解码。这意味着，如果卫星下行链路（如下传的遥测数据、未经高强度加密的业务指令或图像）存在任何安全降级，这套系统部署在全球的无数个开源节点，就会像“数字吸尘器”一样，将这些本该隐秘的空间数据扒得一干二净。企业必须重新评估其星地链路的物理加密层级，因为“通过技术门槛来掩护安全”的时代已经被这种一站式开源工具彻底终结。

![](https://mmbiz.qpic.cn/mmbiz_png/TRfiawmTBsXYeMaA0YKEpmTBAOgIScrP1wuBEpVjMHYFVOEibOzbD89xmYtH8AsvrtBYsibPkGNYMxHyX7ialPzVYC0ebMXRPa1UI3PoiaVhzDZU/640?wx_fmt=png&from=appmsg)

卫星跟踪控制台：专用跟踪界面显示目标卫星的轨道参数、过顶预测和实时位置数据

![](https://mmbiz.qpic.cn/mmbiz_png/TRfiawmTBsXaZrvQibXpMD4HqiblpgnF1FyonBITLk4w92kweJM1JraYJMcZpofD1ibItOhRJgDx13BqGgmwTCSPwJ7dF04a4cBuqO4I2MpBWlI/640?wx_fmt=png&from=appmsg)

SDR瀑布视图：瀑布视图在活跃的卫星通信期间带有实时转录叠加

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TRfiawmTBsXaF0z0ddibImscklqAKdxo46ib4lia4VshmuBGBRjtdepd1yXqEcHAVW95UDrc4ia25k1kD3GZ5GIX7iarwrERFaQphUQ2uiaUsU9jcE/640?wx_fmt=png&from=appmsg)

瀑布包解码（GMSK）带有实时GMSK数据包解码和解码输出详细信息

![](https://mmbiz.qpic.cn/mmbiz_png/TRfiawmTBsXYibQgGekxuZmRjA058RxtPQsicpCAwUgzqWricVCOibB3WoW5TugZpibam1ZRU0rFkeDXoGhA0qzWlGsc56TpN5xGkX6ibJzng7hgkQ/640?wx_fmt=png&from=appmsg)

遥测数据包查看器（十六进制+ASCII）：数据包查看器以十六进制显示遥测有效负载字节，并与ASCII并列显示

![](https://mmbiz.qpic.cn/mmbiz_png/TRfiawmTBsXYp2NRcAYflQftRyeBFg09Eq64nicjgTJkFNVxDVNVywGMu5I5W2uMsXk9yDaT5FMlPia8mDAhvBiaxmzA9FQ9V8Gy6Ggo2HiaAEuA/640?wx_fmt=png&from=appmsg)

TLE数据同步：TLE同步页面显示实时进度和卫星数据库更新

![](https://mmbiz.qpic.cn/mmbiz_png/TRfiawmTBsXbhVh9HrBiakOwtJIjrzFbQsbEIlKFZTtPjw1pF5FTS03wCl6ZjicKP7GBKIPW1kZFrEIiaiaibxjNFTGibGafZMukbia805NNkxeETWQ/640?wx_fmt=png&from=appmsg)

全面的SDR设备管理界面，支持RTL-SDR、SoapySDR和UHD/USRP无线电设备，并具备远程功能。

![](https://mmbiz.qpic.cn/mmbiz_png/TRfiawmTBsXaRrxkF2cAnQW9R6YKiakpIyjlrX6UkmMnOZV8LW4lngqjzKMgiabWg1Y0OYZvEfC86fP2eJ64TibtxSRfrEO1sOUPwxib3FjqwgDg/640?wx_fmt=png&from=appmsg)

文件浏览器视图显示了解码的天气图像、数据包输出和保存的转录。

![](https://mmbiz.qpic.cn/mmbiz_png/TRfiawmTBsXYlLibd06tyq9ey54HGP2PdsfRTAIlQuKa3XBkQRJfAZh4XphEibuRF0AIHu79ibzsHeoGUu3JvEtNN3kY52KumGOvFXFxsttgck4/640?wx_fmt=png&from=appmsg)

自动观测仪界面，显示即将过境的任务状态

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TRfiawmTBsXaNtqibptEF9VbSYwKmyZyvP3lvyZJ9BSPwicapFfsnkoTToGXSo3iavGaIxjAkLZAhpJhNia6mVISTDibwHCURso99dMuVv17QXIfM/640?wx_fmt=png&from=appmsg)

线程和进程链IQ样本经过的流程，显示DSP管道中的性能和数据流

### **主要特点**

**实时卫星跟踪：**使用高精度轨道模型跟踪数百颗卫星。TLE数据自动从CelesTrak和SatNOGS更新。

**自动天线旋转控制：**与流行的天线旋转器接口，自动跟踪从头顶经过的卫星。

**电台控制(Hamlib):**在卫星过境期间，使用Doppler校正控制与Hamlib兼容的电台。

**SDR集成：**从广泛的SDR设备（包括RTL-SDR、SoapySDR和UHD/USRP无线电设备）流式传输和录制实时无线电信号。

**IQ记录与回放：**以完整的元数据（中心频率、采样率、卫星信息）记录原始IQ数据，并通过虚拟SDR设备回放记录以进行分析和调试。

**数据解码：**使用AX25 USP Geoscan帧解码SSTV、FSK、GFSK、GMSK和BPSK。目前LoRa和AFSK解码器还无法工作。

**AI驱动的转录：**通过Gemini Live或Deepgram对解调音频进行实时语音转文字。注重隐私并带有用户密钥，可选翻译和文件输出至backend/data/transcriptions/。

**计划观测：** 定义详细的观测任务，在卫星经过时自动收听、解码、转录和记录音频和IQ，无需人工干预。

**SatDump集成：**通过SatDump解码来自METEOR-M2（LRPT和HRPT）的天气卫星图像，并结合自动观测。

**性能监控：**实时可视化信号处理管道，显示组件之间的数据流（SDR→FFT→解调器→解码器→浏览器），队列健康监控，吞吐率以及组件统计数据，以诊断瓶颈并优化性能。

**响应式网页界面：**一个使用Material-UI构建的现代、响应式和直观的网页界面，能够无缝适应桌面、平板电脑和移动设备，使您能够从网络的任何地方控制地面站的所有方面。在平板电脑和手机上效果极佳。

### **计划观测&自动过境记录**

地面站包含一套全面的自动化观测系统，能够无需用户干预即可调度并执行卫星过境任务。

**监控的卫星：** 定义卫星监控模板，包括硬件配置、信号参数和任务定义。系统会自动生成所有符合条件的轨道的定期观测。

**自动过境计划：**根据可配置的标准（最小仰角，提前窗口）自动计算和安排即将发生的卫星过境。调度器使用APScheduler在信号获取（AOS）时触发观测，并在信号丢失（LOS）时停止。

**灵活的任务组合：**每个观察可以包括多个并发任务：IQ记录（SigMF格式）、音频记录（WAV）、协议解码（AFSK、GMSK、SSTV）和可选的人工智能转录。

**硬件编排：**在预定观测期间，自动控制SDR设备、天线旋转器（带卫星跟踪）和设备（带多普勒校正）。

**实时观测能力：**用户可以通过网页界面实时观察任何自动观测通道-查看光谱瀑布图，收听解调音频，并观看实时解码器输出。当使用与自动观测相同的SDR时，用户可以不受干扰地监控，但请注意，更改SDR的中心频率或带宽将影响正在进行的观测。

**多SDR观测：**自动观测可以在一个SDR上运行，同时额外的SDR并行记录、解码并收听相同的通联。

**状态管理：**实时观察状态跟踪（计划中、运行中、已完成、失败、已取消、错过），并自动清理旧的已完成观察。

**会话管理：**自动观测在隔离的内部VFO会话（命名空间：“internal:<observation\_id>”）中运行。当使用不同的SDR时，用户会话和自动观测完全独立，互不干扰。

传统的无线电爱好者享受在深夜手动调节旋钮、在充满底噪的电流声中捕捉微弱外太空信号的纯粹物理快感。而Ground Station的出现，迎合了现代人对“全知全能与效率至上”的系统性依赖。使用者不再需要守在电台前，只需在Web界面上设定好参数，系统就会自动完成捕获并把解码好的图像和文本喂到眼前。分析师在获得了极大的数据吞吐量的同时，也主动切断了与电磁波进行物理交互的原始感官连接。

https://github.com/sgoudelis/ground-station

**知识星球**

由于之前公众号及知识星球的许多深度调查文章无法查看，后续境外各种组织机构的详细内容报告都存放于知识星球**“OSINT世界”**

![](https://mmbiz.qpic.cn/mmbiz_jpg/TRfiawmTBsXY2iaqWIibUxxOXylcGibWh0LcANNUiaoBJwecVwR5EPgBAY7YsZTNqnicOutxqKfIKM1icnZEVOsDicPQ8QsbFOsSkdYTttMTutHTY0M/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/TRfiawmTBsXa3p1DR5vwbJUVpSuryx3ZZLN2ORN8BWhmo0jtAlGUichKWzic2jqcNnoI6nWcMzevef6bicljZstWbNhmfSquPfGI882ag1JnxzY/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/TRfiawmTBsXZ0IvlgnKW3s3up9hJnUrwLDtwr0Z4Vn5NL0rAW0Frcq9fzrJJdeEd6iaW2JQWLRYbGIZRYJ2b1x50icOcphd6p6Zaz9icb7dJyVI/0?wx_fmt=png)

OSINT情报世界

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/TRfiawmTBsXZ0IvlgnKW3s3up9hJnUrwLDtwr0Z4Vn5NL0rAW0Frcq9fzrJJdeEd6iaW2JQWLRYbGIZRYJ2b1x50icOcphd6p6Zaz9icb7dJyVI/0?wx_fmt=png)

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