---
title: 做一个《异形》系列里面的活动探测器
url: https://mp.weixin.qq.com/s/SjeA80wamFodZloQc4gc6w
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:05:46.044311
---

# 做一个《异形》系列里面的活动探测器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1woCcbOsjVOopr1qLGKic7Rlic3v1Rvl0iaBeQtkuibT56kl5CiapVYbpb7RD7nQgtXp1Fg7doqRcd3icNXpXFZWiapmPKrTeQ0DmYab35VTxePs08/0?wx_fmt=jpeg)

# 做一个《异形》系列里面的活动探测器

原创

huoji
huoji

冲鸭安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 前言

如果你看过《异形》系列电影以及玩过《异形》系列的游戏，你一定对里面的那个探测器不陌生-异形系列里面经常会出现一个道具，叫活动探测器，他的作用很简单，有异形活动的时候发出BBB的声音.

《异形：隔离》里面的探测器：

![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVM2sVcwzo1ribv0f78IYRwC5TwBHTyMwiaVVRvY7qH3heqyPrOicJ1WzkZmqT2Wmyicmcs1RQlbUMxGibtJdoxLicJauIvYnoFKgKZr8/640?wx_fmt=png&from=appmsg)

《异形2》里面的M314探测器:
![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVP26IAL1MnJCLS5B5GG7N8uFJqNq3f0db10thBVdO5NB46Xxic2w5rOVIuruNlEuuSMhhRpdMYgqWyGHejHAMAvkibOpgq20RhAo/640?wx_fmt=png&from=appmsg)

这些探测器实际上只用一个作用，吓坏未成年看异形电影的小朋友，让他们每天晚上因为这种声音做噩梦

> 这不是我说的，是央视电影频道主持人锐评的

## 硬件准备

### 电影 VS 现实

首先我们得知道这些探测器原理，在现实中，能用的方案是mmwave radar，也就是说发微波探测到物体反射回来打到屏幕上告诉我们有没有物品。

与电影的差别：
在现实中mmwave并不能穿混泥土墙，这是因为他们的工作波段导致的。不过好像电影里面的也没有穿混泥土墙的需求，都是穿一下泡沫板。

> 电影里面那种逆天的穿墙性能和追踪性能，现实中是做不到的。最多能通过UWB去看附近有没有东西，但是定位不到那么准确。

### ESP32

![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVMUer9TSnn8rKw0pibEpHibFKHQJ4mIFugzJm5NG6L4IdJxU7PUvFsae1CewvrZ8Ma17gia7vs7pAqdxAvwuCGPdALVPhKRhj2Fias/640?wx_fmt=png&from=appmsg)

**ESP32简直是工业奇迹，我到现在还没整明白为什么这种小型计算机带蓝牙带wifi甚至是可以带摄像头的东西只要10块钱？？**

### TFT

一块屏幕
![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVM8CILviahYSM4xjuaa122ly1QJm7ov43Mryy8YCVgahAqRJficp1ib91JIAXXOXkjFiaojKM0agaND67fav8M5nQNfgl2Vu5icXjJ8/640?wx_fmt=png&from=appmsg)

### MMWAVE

这块选择很多，我选的是LD2460，LD2460最大距离是8M，支持360度和120度，对于我来说就够了

![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVM9HCCWahibiakWYq5NarOuzmhPoUR3u9eCptAJ31ibGxuHdvcFtq4QG5Gysf8Dzu3Zh71GlDrbrM2Rcz5rYmzc2pcArOqSLJ4ia2s/640?wx_fmt=png&from=appmsg)

## 组装

实际做起来很简单，为了简单我们可以先用面包板加一些线把他简单拼接起来，按照说明书的接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1woCcbOsjVNIz19aqVfpeibHHMfePgDyNibibQAdw6KdTcgwUNvZEks2gej7XSeiciboZ9WCicjKc063sHPGfKMVm46ReLcibRpLjSqXU67bAB8rcs/640?wx_fmt=png&from=appmsg)

这里不要相信GPT的。比如GPT5.4之前一直跟我说LD2460有两个TX RX GND只用接一个，实际上搞了半天我发现雷达咋都没信号，最后翻图纸才发现是GPT骗我，LD2460两个TX RX GND都得接。
最后长这样:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1woCcbOsjVOWvmYtPicRqJt3K0kLCxZ9gYibu6CbQ6cBiceqfkiaicmicCFjk3Tsq2M11g9muF4A82XJaal6V7l85icqI8eD9G4416vHx4YSBPBJ7o/640?wx_fmt=png&from=appmsg)

先绑着:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1woCcbOsjVPicH7Qo0OSFKKIFlje71AQ2ryZeavLH6AiaWuiav3q0R6vomKfRc25HEaJ5ZD73luiaGRxnkXI12Pqmq5Z8QG3Ax3OxjRGnBoQNNk/640?wx_fmt=png&from=appmsg)

剩下的就非常简单，把ESP32插入电脑，剩下的交给GPT,只需要丢给GPT LD2460的结构体就行，让GPT自己编程。vibe coding即可。LD2460支持调整模式，高灵敏什么的，我就稍微调整了一下。3M内如果没东西就切换成高灵敏模式探测8M的东西。否则就缩放成3M的高精度定位。

## 测试

所以我们来试试
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1woCcbOsjVNRR6BqtFS1a3wsQ1wbNL4R7eQNEHS02PhspQZea2w6TD0Pib1krQaVZc1ddibjg5MbCIZru5kJ9C829m14QdbgjhapNibrjwjJBI/640?wx_fmt=png&from=appmsg)
太丑了，让GPT改了一下样式, 经过测试，可以透过一些简单的遮挡物的。并且我发现，可能是因为反射的缘故？在室内如果不是完全密封的情况下，可以检测到人在混凝土墙背后，不过门完全关了就探测不到了，我猜测是因为有反射，**所以不是完全密封的情况下，也是能探测到人的**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1woCcbOsjVM1OCuQ4578H8NRBC68AibiaP1ibbHTGE1agLoMkEFqcjZy0GLqKMDu0WLaPapsOqHAJO2jISlroSOxCmrjExmZzKcTOpkZdy5pcQ/640?wx_fmt=png&from=appmsg)

拿去室外试试，效果也是嘎嘎的，在室内因为反射的缘故，:
![](https://mmbiz.qpic.cn/mmbiz_jpg/1woCcbOsjVPUHWDad2gIe8q64cX25NkumR4VOIznOQBuodxyChKfiaZo9FN8TDSpHSJqLusAS5Q1Uen3uagNCCibwL4jLQcwUIz2DO2xVSXhA/640?wx_fmt=jpeg&from=appmsg)

现在就跟游戏里面的很像了，还可以继续微调一下:
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1woCcbOsjVP6qOVGhtP2RiciaDZIXoDrDhtf6jIcHaXUxlaMNB2qgUOAAlJywIvN0QdKS7qm8S4dEfZSXUibnDeDvpbicagSiaJJqZ99vTWqHDSg/640?wx_fmt=png&from=appmsg)

## 后续

忘记加发声模块了，就先不加了，那声音听得我害怕。国外有一个老哥做了带发声模块的,原理跟我这个也差不太多

《Building a REAL Alien Motion Tracker》
https://www.youtube.com/watch?v=KpUjXUSlkbU&t=335s

还差一个3D打印，打印一个外壳然后塞进去就好了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVOYrTaOc64hFYOXxTKC2iaD7D6IW3XgSatdUwvXaVSI2q4CmiaDF7TINvumnYNbNE3ibVcSogEA4rtougMDxjvqekaQauHzsxPAFI/0?wx_fmt=png)

冲鸭安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVOYrTaOc64hFYOXxTKC2iaD7D6IW3XgSatdUwvXaVSI2q4CmiaDF7TINvumnYNbNE3ibVcSogEA4rtougMDxjvqekaQauHzsxPAFI/0?wx_fmt=png)

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