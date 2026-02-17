---
title: 基于DSP结构的软件无线电的硬件组成---零中频数字无线电(二)
url: https://mp.weixin.qq.com/s/7R117ErXrCodbszlrSmziA
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:19:47.117295
---

# 基于DSP结构的软件无线电的硬件组成---零中频数字无线电(二)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0plbPNoicicKSib7sia1IMZRfz2UWG6DPYPgQfj9BTN2ibD971BAibrxGGgrDbRnbWOM8Pa2tz8xMw7yawCgmWRu8AJ9Lnlm8dHqLmqia0H7S9Lf4o/0?wx_fmt=jpeg)

# 基于DSP结构的软件无线电的硬件组成---零中频数字无线电(二)

原创

班班高
班班高

网络安全自学

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6nNyjd9QeAUdlJnqcbr4Ys8FkITF5IX4d9ER5WHB4uz0CSWlE3X4LMvu9yaZhib7zPDu1QEJQEveg/640?wx_fmt=gif)

**点击上方蓝字  关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC7SjNGMmDlqHKXEtpiaH6GxlKkhZA3ecMxLq3e1LiaV4pKn6nicfEXoCg3Ij97wdpUaCfoJRWw1u68mQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/eyEIlSYjffibe2qDJAEOJcuBtMuGM1Xo3gjoKa8YkZNOicX44eiaTb0arX7Frib1lgdX8iamGGlpvtyj8ibfib1dIjiakA/640?from=appmsg)

**马年行大运  新春纳百福**

![](https://mmbiz.qpic.cn/mmbiz_png/eyEIlSYjffibe2qDJAEOJcuBtMuGM1Xo3gjoKa8YkZNOicX44eiaTb0arX7Frib1lgdX8iamGGlpvtyj8ibfib1dIjiakA/640?from=appmsg)

基于DSP结构的软件无线电的硬件组成

---零中频数字无线电(二)

      基于DSP结构的零中频无线电有两种架构：**模拟****零中频架构**和**数字****零中频架构**，上期内容：[基于DSP结构的软件无线电的硬件组成---零中频数字无线电(一)](https://mp.weixin.qq.com/s?__biz=MzI3NzQ3NzY4OA==&mid=2247484136&idx=1&sn=207e5533ccd729cf206613cb53c84e26&scene=21#wechat_redirect)中**已经对****模拟零中频架构进行了讲解**。本期内容讲解**数字****零中频架构**。**注：**模拟零中频架构并不属于软件无线电的范畴，我们先讲解模拟零中频架构的知识点是为了方便引出数字零中频架构，便于你将本期内容和上期内容作对比，更快的对比出模拟零中频架构和数字零中频架构的异同点。

      和基于DSP结构的零中频无线电中的模拟零中频架构的硬件组成类似，在基于DSP结构的零中频无线电中的**数字****零中频架构**中也无中频信号处理部分，同样只由射频前端和基带信号生成及处理两个部分组成。以下以接收方向为例讲解这两个部分的硬件组成。

**一、射频前端**

      射频前端由天线和射频前端模块组成。射频前端模块包括线性射频放大器，抗混叠滤波器。

**1.1****线性射频放大器**

      线性射频放大器用于对接收到的微弱射频信号进行放大，以提高信噪比，使射频信号的电平达到或优于后续电路可处理的最低要求。

**1.2 抗混叠滤波器**

      抗混叠滤波器属于带通滤波器。它的作用是滤除天线接收到的信号中，我们关心的目标频段之外的噪声和干扰，并且最重要的是限制信号的带宽，以防止在后续的ADC采样过程中产生“混叠”现象。**注：**我们将在下期详解本期内容所提到的“**混叠”**现象，如需学习请持续关注。

**二、基带信号生成及处理**

**2.1 基带信号生成**

**2.1.1 ADC模块**

      射频前端的射频信号经过**ADC(模数转换器)**进行数字化后传输给DDC模块。

**2.1.2 DDC模块**

     **DDC(数字下变频器)**接收由ADC模块输出的单路数字射频信号，并使用由内部本地振荡器产生的两路相互正交的数字本振信号分别与输入的单路数字射频信号进行时域相乘，从而实现数字下变频，得到I路和Q路的基带信号后由DDC内部的抽取滤波器滤除高频分量，最终得到低频数字基带I/Q信号。DDC(数字下变频器)将I路和Q路的低频数字基带信号传输给DSP去恢复出最终的0和1比特流。

**2.2 基带信号处理**

      DSP核心处理单元接收来自DDC的低频数字基带信号，执行所有通信协议和信号处理算法，实现如下功能：

    ①信号解调：如对QAM调制信号、QPSK调制信号、OFDM调制信号进行解调；

    ②信道解码：如Turbo、LDPC、Viterbi解码，纠正传输中的错误；

    ③均衡：补偿信道造成的失真；

    ④同步：包括载波同步，符号同步、帧同步；

    ⑤协议栈处理：如MAC层，网络层等。

**注：**经过DSP解调出的数据（如比特流数据，语音数据）将会通过USB、PCIe等接口发送给嵌入式处理器或电脑，供上层应用使用。

**本节内容概括**：

![gzh思维导图.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/0plbPNoicicKSicmslWJfWu9JmJjvg3MRiatqA2BdNvnanJqlqqhha7biaOKDtzrrxEJoZhS11BrHYvzyV0HiaaOCT3qCWprEcamfmzNBVJUR2viaU/640?from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KzC2TfrDajDdIvfvMXyFs0bcsf7sicEBZsoCfFotNF6HbcrIqyNKTXCnMLBzAR0n9NTK7bFKGdOlxZTgicYics35A/0?wx_fmt=png)

网络安全自学

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KzC2TfrDajDdIvfvMXyFs0bcsf7sicEBZsoCfFotNF6HbcrIqyNKTXCnMLBzAR0n9NTK7bFKGdOlxZTgicYics35A/0?wx_fmt=png)

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