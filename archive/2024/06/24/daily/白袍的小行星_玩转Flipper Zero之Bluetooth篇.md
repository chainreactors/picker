---
title: 玩转Flipper Zero之Bluetooth篇
url: https://red-team.tips/post/UG49Ltc0l/
source: 白袍的小行星
date: 2024-06-24
fetch_date: 2025-10-06T16:54:19.459862
---

# 玩转Flipper Zero之Bluetooth篇

[![](https://red-team.tips/images/avatar.png?v=1754980891100)](https://red-team.tips)

# 白袍的小行星

**Once a hacker, always a hacker!**

[首页](/)
[归档](/archives)
[标签](/tags)
[关于](/post/about)
[友链](/post/friends)

## 玩转Flipper Zero之Bluetooth篇

2024-06-23

4 min read
[# Flipper Zero](https://red-team.tips/tag/3xmZ3FVoMQ/)

# 0x1 前言

最近入手了一个`Flipper Zero`，打算学习下无线安全领域的知识，顺便记录下一些把玩经验。

我并没有使用官方固件，而是刷了`Momentum`：https://momentum-fw.dev/，相比官方固件，它集成了更多的app，开箱即用。

本篇就介绍下`Bluetooth`下的各种好玩的app，go!

# 0x2 BLE Spam

项目地址：https://github.com/simondankelmann/Bluetooth-LE-Spam

该项目主要是一个蓝牙滥用相关的app，主要有以下11种子功能：

**1. Kitchen Sink**

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20240623215514POCFKqimage.png)

这是一个集成功能，相当于会随机利用所有其他子模块的功能，这样就会影响到更多的周围设备（有种看门狗2里大停电的既视感）。

**2. BT Settings Flood**

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/202406232155572pPYTOimage.png)

顾名思义，它会大量生成各种虚假的蓝牙设备，对正准备进行蓝牙配对的人产生干扰，效果如下：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20240623215627Opc56Fimage.png)

**3. iOS 17 Lockup Crash**

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20240623215651aOif4jimage.png)

这个功能可以通过发送特定格式的BLE包，使得iOS 17.2以下的设备被迫重启，不过因为我手头上都是17.5的设备，所以没有测试成功。

**4. Apple Action Modals**

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20240623215716gTABWVimage.png)

伪造苹果设备的某些操作，可以让iOS设备弹窗，触发距离较长，几米内都能触发：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20240623215740f5GiOqimage.png)

**5. Apple Device Popups**

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20240623215758ZfybD6image.png)

和上一个类似，但这个是会弹类似设备配对时的框，所以需要触发距离很近，差不多30厘米之内才能触发。

**6. Android Device Conn：** 和前面针对苹果设备的类似，需要Google服务，但我手上没安卓设备，所以也没测试

**7. Samsung Buds Popup：** 同上，这个针对三星手机

**8. Samsung Watch Pair：** 弹配对三星手表的框

**9. Windows Device Found：** 这个则是针对开启了Windows快速配对功能，实测开启了会不停弹通知：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20240623215825nwQOVkimage.png)

**10. Lovespouse：** 这个比较搞，具体效果可以看：https://www.youtube.com/watch?v=LupcNkiKG\_M

10和11其实都是Lovespouse，但一个时全部开启，另一个则是全部禁用，就不分开说了。

# 0x3 Bluetooth Remote

可以将Flipper Zero变成一个有用的蓝牙设备，比如蓝牙鼠标，蓝牙键盘等等。

# 0x4 BT Trigger

和手机配对后，可以远程控制手机拍照，试了下还是挺好使的，虽然想不到使用场景😅

# 0x5 FindMy Flipper

项目地址：https://github.com/MatthewKuKanich/FindMyFlipper/

这项目让我有点失望，因为我本来是以为可以直接在"查找我的设备"处实时看到自己Flipper Zero位置的，但用了一下才发现，要实现这种需要先买一个AirTag进行Clone，自行生成的则只能通过接口手动获取，不能直接在你的苹果设备上看到Flipper Zero的位置。

# 0x6 PC Monitor

项目地址：https://github.com/TheSainEyereg/flipper-pc-monitor

一个用来监测主机各种指标的app，比如CPU占用、内存占用等等，需要在主机端先执行程序，再连接到Flipper Zero，之后打开该应用就能看到了：

# 0x7 结语

可以看出，Bluetooth方面的功能主要还是整蛊娱乐为主，都不怎么有实战意义，用来整蛊同事挺好玩的，但小心被打~

* [0x1 前言](#0x1-%E5%89%8D%E8%A8%80)
* [0x2 BLE Spam](#0x2-ble-spam)
* [0x3 Bluetooth Remote](#0x3-bluetooth-remote)
* [0x4 BT Trigger](#0x4-bt-trigger)
* [0x5 FindMy Flipper](#0x5-findmy-flipper)
* [0x6 PC Monitor](#0x6-pc-monitor)
* [0x7 结语](#0x7-%E7%BB%93%E8%AF%AD)

下一篇

[### 我的OSCE3之路——OSDA](https://red-team.tips/post/oHLNjm2cX/)

[RSS](https://red-team.tips/atom.xml)