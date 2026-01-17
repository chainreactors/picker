---
title: 【大话工控安全】工业控制系统行业知识：电力行业电网变电站场景
url: https://mp.weixin.qq.com/s/aXh1vzMQ-zzgssMfLpbZkA
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:22:06.057683
---

# 【大话工控安全】工业控制系统行业知识：电力行业电网变电站场景

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icKb2wsWzy9NPowYOibGDTvxBicLHHAStUEoNjdrvicf838zTxmP1uxmLwLRiaibiaz4gwiaRZpMdwXBu6mP7BFSVdXS0g/0?wx_fmt=jpeg)

# 【大话工控安全】工业控制系统行业知识：电力行业电网变电站场景

原创

老付话安全
老付话安全

老付话安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/7UnMUNqGIz071DWbJdrzpdJpDxlHDFtnMDlvK8TeibfibdovgH3vMKfIloQibicL6TTiaXQib28nacKJv8qx7AJNnm8g/640?wx_fmt=gif)

**点击蓝字**

**关注我们**

关注我，带给你不一样的精彩

世界因你的沉淀而出彩

**始于理论，源于实践，终于实战**

**老付话安全，每天一点点**

**激情永无限，进步看得见**

![](https://mmbiz.qpic.cn/mmbiz_png/lB1oaPhdMNvxZ67rEjeQWUFqwCxiacBblWHRAxzuoMfYPQXETZ7Y5bsGSLBPy2QGDKIbia74ruAWgJXhWkMlGgkA/640?wx_fmt=png)

**严正声明**

本号所写文章方法和工具只用于学习和交流，严禁使用文章所述内容中的方法未经许可的情况下对生产系统进行方法验证实施，发生一切问题由相关个人承担法律责任，其与本号无关。

特此声明！！！

本文字数：

4366字

阅读时间：

11分钟

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmkPpdz6eLJ8DdlDNUBqveKtiacEVRcfsmdBFkicRIT6Jx5UjOKE0ia3ovA/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmWXkibyqRGYwGCtfKsZVPyXib1Hnia07via66RuViaMOMicKXfLQeRKxgd9Ow/640?from=appmsg)

**相关内容**回顾****

[【大话工控安全】工业控制系统行业知识：电力行业相关术语及系统功能介绍-变电站电力监控系统](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247485842&idx=1&sn=7fd85151dfa6c46d6b4560f5e1186c75&scene=21#wechat_redirect)

[【大话工控安全】工业控制系统行业知识：电力行业相关术语及系统功能介绍-发电厂电力监控系统](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247485838&idx=1&sn=bb647629936371e65b62b31e3abd7343&scene=21#wechat_redirect)

[【大话工控安全】工业控制系统行业知识：电力行业相关术语及系统功能介绍-地县调度中心监控系统](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247485837&idx=1&sn=315489560f3657c8ef0fd35c070edbb5&scene=21#wechat_redirect)

[【大话工控安全】工业控制系统行业知识：电力行业相关术语及系统功能介绍-电力监控调度系统](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247485841&idx=1&sn=9fed06b6a69ef4ec983857b98fa72d13&scene=21#wechat_redirect)

电力变电站系统的发展趋势：

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PRgpLme0UV0sL35MDwv5jGq4y0x3nTLPUa2mMHW7ZrDqg9dDBAKbNMsibkibkV8eicln7hJVKwDJxicg/640?wx_fmt=png&from=appmsg)

随着IEC61850标准的应用和一次设备的发展，电力系统已经经历了数字化变电站、智能变电站、新一代智能变电站三个阶段。智能供电系统是行业发展的需要，而数字化是智能化的基础。

智能变电站定义：

首先它采用先进、可靠、集成、低碳、环保的智能设备。其次它以全站信息数字化、通信平台网络化、信息共享标准化为基本要求，自动完成信息采集、测量、控制、保护、计量和监测等基本功能，并可根据需要支持电网实时自动控制、智能调节、在线分析决策、协同互动等高级功能的变电站。

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PRgpLme0UV0sL35MDwv5jGWNhky7czGugAl0qzM6A177omJ1THJ8fGcU286pj4Kr0GYmOTibXvbIA/640?wx_fmt=png&from=appmsg)

变电站（变流所、升压站、开闭所）的组成部分：

+ 一次系统（设备）：完成电能的传输、分配和电压变换功能。

+ 二次系统（设备）：完成对一次设备及其流过电能的测量、监视、告警、控制、保护以及开关闭锁等功能、远动系统。

关于一次、二次系统包含哪些设备详见：

什么是数字化变电站： 变电站二次控制系统采用数字化电气测量技 术，二次侧提供数字化的电流、电压输出信号，变电站信息实现基于 IEC61850标准的统一信息建模，站内自动化系统实现分层、分布式布置，LED设备之间的信息交互以网络方式实现，断路器操作具有智能化判别。

数字化变电站特点：数据采集数字化、系统分层分布化、系统结构紧凑化 、系统建模标准化、信息交互网络化、信息应用集成化、设备检修状 态化、设备操作智能化。

智能变电站： 伴随智能电网的概念出现，在现代输电网中，大部分传感器和执行机构等一次设备，以及保护、测量、控制等二次设备都安装在变电站中。以全站信息数字化、通信平台网络化、信息共享标准化为基本要求，自动完成信息采集、测量、控制、保护、计量和监测等功能。实现电网的自动控制、智能调节、在线决策等高级应用。

智能变电站技术特征：信息采集就地化、信息共享网络化、信息应用智能化 、设备检修状态化。

变电站监控系统的主要功能：

1.数据采集

（1）模拟量的采集：包括各段母线电压、频率、线路有功功率、 无功功率、电流、主变有功功率、无功功率、电流、馈线有功功率、电流、电容（抗）器无功功率和电流、站内直流电压和所用变电压、主变温度、热电的气压、水电的水位等非电气参数 。

（2）状态量的采集：发电厂、变电站中断路器位置状态、隔离开关位置信号、继电保护动作状态、同期检测状态、有载调压变压器分接头状态、厂站一次设备告警信号等 。

（3）电量的采集：传统采集是指电能表输出一种反映电能流量的脉冲信号，采用感应式电能表，由电能表转动的圈数来反映电能量大小 。但这种方法抗干扰性差，采用微机电能计量仪表，全部由单片机和集成电路构成，通过采集的交流电压和电流量，由软件计算出有功电能和无功电能。从功能、准确度和性能价格比大大优于脉冲电能表。

2.事件顺序记录

（1）SOE 事件顺序记录

（2）SOE包括断路器的调合闸记录、保护动作顺序记录等

注：连续记录所有重要开关量（如断路器分/合闸、保护动作、报警信号）变化的过程。它不仅仅是记录事件本身，更重要的是记录每个事件发生的精确时刻，从而能够按时间顺序重现事件发生的全过程。

3.故障记录、故障录波和故障测距

4.操作控制功能

5.安全监视功能

6.人机联系功能

7.打印功能

8.数据处理和记录功能

9.谐波分析与监视

10.通信功能

11.时钟功能

12.自诊断功能

变电站监控系统的基本结构：

(1)集中组屏式

(2)分层分布式

(3)完全分散式

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9MFl1LCgCibJeCV1F21OkZHVYX4tY8b7YkTdXSqhre8sozecX77R5KgBpvzygTIrHiaW21ytB2FzvrQ/0?wx_fmt=png)

老付话安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9MFl1LCgCibJeCV1F21OkZHVYX4tY8b7YkTdXSqhre8sozecX77R5KgBpvzygTIrHiaW21ytB2FzvrQ/0?wx_fmt=png)

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