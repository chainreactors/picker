---
title: AI+硬件 WhaleBot鲸鱼小车复刻工程xa0TASK1 DIY所需硬件
url: https://mp.weixin.qq.com/s/OoYlK98jmr944S9eO1WxgQ
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:14:35.772943
---

# AI+硬件 WhaleBot鲸鱼小车复刻工程xa0TASK1 DIY所需硬件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/quuJmJ6Atj0OCy8QfiadCkmYtOIYkMvFK5Fs6Md7kre1dOtclCEvicJHvfcvmiaYK3KTncVH9gArHWOK8EdIYFSAQmtYEdSCQAK9avwyQichHFU/0?wx_fmt=jpeg)

# AI+硬件 WhaleBot鲸鱼小车复刻工程 TASK1 DIY所需硬件

网安杂谈
网安杂谈

网安杂谈

![]()

在小说阅读器中沉浸阅读

今天开始，咱们一起学习一下AI学习社区Datawhale的开源课程：AI+硬件 WhaleBot鲸鱼小车复刻工程。这个项目的目标是组装一个鲸鱼外形的**具备实时语音感知能力**的移动机器人。

笔记参考教程地址：https://github.com/datawhalechina/whale-bot，https://www.datawhale.cn/activity/518

Whale-Bot采用**天问ASRPRO开发板**作为其核心的语音交互引擎。将项目门槛降到了最低。**ASRPRO 的核心作用**是作为“听觉中枢”，ASRPRO芯片内置了高效的语音识别算法，通过**天问Block图像化编程**或简单的配置，可实现精准的关键词唤醒与本地指令解析，将复杂的语音信号直接转化为ESP32-S3易于理解的串口指令。

在ASRPRO完成本地唤醒后，主控**ESP32-S3**通过Wi-Fi接入云端API接入大语言模型或智能语音助手，实现真正的“智能对话”。

Task1介绍项目所需的工具和基本硬件。

有的元件可能需要锡焊，准备电烙铁与焊锡（一切问题解决的终点），杜邦线（公对公，公对母）；全套螺丝刀套件。502胶水，透明胶（或纳米胶），有条件也可以用热熔胶。下面这图是我花重金购置来的部分装备。

![](https://mmbiz.qpic.cn/mmbiz_jpg/quuJmJ6Atj093YJv8mIykbNRiaMdUVB8RmQJNMONibujHCNGT4huTb1B6DFp6ps479KMzDacMic1DL30LzPSfqPc5R03k2SW6Nb5a0AfGZUJ9E/640?wx_fmt=jpeg)

主要的组成部件包括：

1.主控：ESP32-S3-DevKitC (N16R8)

ESP32-S3-DevKitC-1是一款入门级开发板，搭载Wi-Fi+Bluetooth®LE模组ESP32-S3-WROOM-1，板上模组的大部分管脚均已引出至开发板两侧排针，开发人员可根据实际需求，轻松通过跳线连接多种外围设备，也可将开发板插在面包板上使用。

ESP32-S3-WROOM-1是一款通用型Wi-Fi+低功耗蓝牙MCU模组，搭载ESP32-S3系列芯片。除具有丰富的外设接口外，模组还拥有强大的神经网络运算能力和信号处理能力，适用于AIoT领域的多种应用场景，例如唤醒词检测和语音命令识别、人脸检测和识别、智能家居、智能家电、智能控制面板、智能扬声器等。

![](https://mmbiz.qpic.cn/mmbiz_png/quuJmJ6Atj2E8ibgjicKRuZ2K6oknohBoV8CgHGXuchhasAVqlfjFqSaj5v9uNbBHG5QxKV3KurpydDenrmK2PDjTvOUV4Egopgv2r7VRGS8Y/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/quuJmJ6Atj3dZJibmr8GkJgtQCY6ph3njICAZsYhBkgp5Y0u9HPAiaBibdiaSibKyOoFGxpI1icMrM3S1iaM0crY5rt5aDxTag5Xt8JfEJgtbtAJTc/640?wx_fmt=png)

2.语音识别模块：天问ASRPRO开发板（负责离线唤醒与语音转文字的前端处理）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/quuJmJ6Atj09Caf5lLpPHQ02aTE73tTfiadCFdj8lpmlxWEu497GicQAFrsSfjJNtc19vYk8t0wb8icdlibgmcKk6dkFCqGIuSoCyMhPqe0aZC0/640?wx_fmt=png)

3.麦克风：INMP441 全向麦克风模块（I2S接口）

4.功放模块：MAX98357A（I2S接口，音质更清晰）。

5.电机：N20 减速电机 x4 参数建议：12V，转速建议选择 300RPM 或 500RPM。

6.电机驱动： 迷你版 TB6612FNG x2

7.车轮：60mm 麦克纳姆轮（N20专用联轴器版）

8.显示屏：2.0寸LCD串口屏，嵌入在鲸鱼嘴部位置。

9.电源：12V 锂电池 + TPS5430 降压模块

10.外形：详见docs/外壳打印文件

11.PCB板：详见hardware/PCB及原理图

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

网安杂谈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

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