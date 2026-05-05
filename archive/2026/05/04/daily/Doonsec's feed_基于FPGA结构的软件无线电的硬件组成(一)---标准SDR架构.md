---
title: 基于FPGA结构的软件无线电的硬件组成(一)---标准SDR架构
url: https://mp.weixin.qq.com/s/G6Ar2nB1wfUVNdhT-kbfpA
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:58:36.464295
---

# 基于FPGA结构的软件无线电的硬件组成(一)---标准SDR架构

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0plbPNoicicKQo08qzD0KxJR7CWkXBr8ToAwUTRgSBk61EGvdGWsianSPnUSFsfWDTFGBBYjVzHtcFKANTtxOZetpSvEJWqYQUulpafa7q3zl8/0?wx_fmt=jpeg)

# 基于FPGA结构的软件无线电的硬件组成(一)---标准SDR架构

原创

班班高
班班高

网络安全自学

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前言

基于FPGA结构的软件无线电的硬件组成(一)
---标准SDR架构，付费学习全部知识，让你豁然开朗～

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4QYcCTShbuLQicldysPuicGHiaPS0td0RGE7xItMDSkUibt7xIiaibWE4yP2PfvR9gaq0XjlezUQA8D8aVDcmJ03gsKpn6M0dDrzmhibhWKe8c1nec/640?from=appmsg)

**青春力量 生生不息**

![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6nNyjd9QeAUdlJnqcbr4Ys8FkITF5IX4d9ER5WHB4uz0CSWlE3X4LMvu9yaZhib7zPDu1QEJQEveg/640?wx_fmt=gif)

**点击上方蓝字  关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC7SjNGMmDlqHKXEtpiaH6GxlKkhZA3ecMxLq3e1LiaV4pKn6nicfEXoCg3Ij97wdpUaCfoJRWw1u68mQ/640?wx_fmt=png)

基于FPGA结构的软件无线电的硬件组成(一)

---标准SDR架构

      基于FPGA结构的软件无线电有两种架构：**标准SDR架构**和**全卸载架构**。本期内容讲解**标准SDR架构**。

      基于FPGA结构的软件无线电中的标准SDR架构，其硬件由射频前端，模拟前端、FPGA信号处理核心、GPP(通用处理器)四个部分组成。

**注：以下内容提到的信号接收链路和信号发射链路通过天线开关或双工器连接到同一个物理天线上。**

**一、射频前端**

      射频前端由天线和射频前端模块组成。按信号接收链路和信号发射链路的不同，射频前端模块包含的器件也不相同，具体如1.1节和1.2节所示。

**1.1 信号接收链路**

     包含：滤波器、低噪声放大器(英文简称:LNA)。

     作用：滤波器为天线接收到的信号过滤掉带外干扰，低噪声放大器将信号放大后送给下一级。

**1.2 信号发射链路**

     包含：滤波器、驱动放大器(可选)、功率放大器(英文简称:PA)。

     作用：滤波器过滤掉信号杂散后将信号送给功率放大器，驱动放大器(可选)用于优化功率放大器的输入功率与线性度，功率放大器将滤波器送来的小信号线性放大到足够的功率。

**二、模拟前端**

**2.1 信号接收链路**

     包含：模拟混频器、抗混叠滤波器、ADC(模数转换器）。

    作用：模拟混频器将LNA送来的射频信号“搬移”到低频（基带），然后由抗混叠滤波器滤掉高频杂波，最后由ADC对信号进行模数转换后将数字信号发送给FPGA。

**2.2 信号发射链路**

     包含：DAC（数模转换器）、重建滤波器、模拟混频器。

     作用：FPGA发来的数字基带信号被DAC数模转换，数模转换后输出的模拟信号经过重建滤波器后由模拟混频器“搬移”到射频频率发送给射频前端的滤波器。

**注：**重建滤波器起到三个作用：1、平滑DAC的阶梯状输出；2、滤除DAC产生的镜像频率；3、通过滤除高频噪声，防止高频噪声进入后续射频电路。

**三、****FPGA信号处理核心**

**3.1 信号接收链路**

     包含：1、DDC（数字下变频）；2、抽取滤波器；3、匹配滤波器；4、FFT(快速傅里叶变换)；5、同步算法；6、信道估计。

     总的作用：将ADC输出的海量高速数字数据降速，去除干扰后发送给GPP。

     每部分作用：

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