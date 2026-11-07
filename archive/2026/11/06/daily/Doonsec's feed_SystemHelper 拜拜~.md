---
title: SystemHelper 拜拜~
url: https://mp.weixin.qq.com/s/4tcG70SKtEzFNuDDmLqXVw
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:56:44.049056
---

# SystemHelper 拜拜~

# SystemHelper 拜拜~

原创

大表哥吆
大表哥吆

kali笔记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 最近关于 SystemHelper 这个“安卓”程序有点扯。但究竟如何，我们也不敢说，也不敢问，我们选择卸载。在非ROOT清空下，如何卸载呢？

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBordebccwhSRpKolhQoM9zFF9ibOGu6QbKB6HprmFECIh2JyHB79Ook4rGQdgSxSRjicR13Wqt3UVlGqX4dxOc987z75vFI6ueqkAQ/640?wx_fmt=gif&from=appmsg)实验准备![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBorctxpG0ZEqR9qLBRiaHKdicOc13ngUpfsnicNYIO5PKuJicfHMKImw6RnNvGLdKDT0JeM2mSrOFKFqjzvicqaOLVCoiahibLaZ6D5twuE/640?wx_fmt=gif&from=appmsg)

无 Root、 无解锁 Bootloader、 手机自带的 USB 调试即可搞定。（本文基于小米 15 Pro / HyperOS 3 实测）

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBoreE5E46exfZMPXtYwUOPbb0kQ1shFrdlq2QCIHmtnq87LAxez6UuAKIkCJw5JSMCwOLZWpaSOGoTHicNydXNT2DcCf7qfSFkAbo/640?wx_fmt=png&from=appmsg)

手机开启「开发者选项」中的 **USB 调试**（小米机型：设置 → 我的设备 → 全部参数，连点「MIUI/HyperOS 版本」7 次即可解锁开发者选项）。
电脑安装好 **ADB 工具**，并用数据线连接手机，允许 USB 调试授权。

# ![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBordkiao60IzcI72BrZPbhlATJhSP5txtrKfWu9bZ2zAbs0aOkT9zYGA9673aJiciay6TD3TenGjDFuIeup9RuEGVunNnRhd9c70HoU/640?wx_fmt=gif&from=appmsg)卸载![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBoresrLuDqRAYsnvibblIibr8mKIN99XEXHT45NjLvBiaF1X0Evldg3fDjXVoYeAm3M92EmpWtZjcESibFRKwGs6PnvEWXUb2hdm2JW8/640?wx_fmt=gif&from=appmsg)

接下来，我们来看看如何轻松卸载。
**01 确认设备连接**

```
adb devices
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBordzynjaGaaOibfbMDj1KmGiap2E1cHGQjtsEkIL5xNS2Yj6ibMwrtxdo0wicuEibTfRSSBIsibM7miaWUj2OSFsL9CKUbiaILNW9iaFIicbA/640?wx_fmt=png&from=appmsg)

**02 查找应用包名**

```
#win环境adb.exe shell pm list packages | findstr /i systemhelper#linux环境adb shell pm list packages | grep -i systemhelper
```

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfhfLcU9UvwWdodiaw7zbJeibwgIicYW2JKpjPCHFZBEHpICeWMt1U1kmqdiagEhYmZHiby6sXic6BrGIlNCMK3n5cQYkmiaWzktAyWno/640?wx_fmt=png&from=appmsg)

`com.mobiletools.systemhelper`查到包名。

⚠️ **注意**：列表里可能还会出现 `com.qualcomm.qti.services.systemhelper`，那是高通系统底层服务，**千万不要删**！

**03 对当前用户卸载（核心命令）**

```
adb shell pm uninstall --user 0 com.mobiletools.systemhelper
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoreHpcdFwnNAMumeOqSvLDxpgGlPvBLuxfKmMdzHekia5Ygz4Ja24ZlOQQeMwlAIibQkXuRBic2ey6CCm5ia29LK3emhddHIEGuMx3s/640?wx_fmt=png&from=appmsg)

看到 `Success` 就说明成功了！应用会立刻从桌面消失、停止运行。这个命令的关键在于 `--user 0` 参数：它表示「仅对当前用户卸载」，从而绕开系统特权分区的限制，全程无需 Root。

**04 重启手机会不会又出现？**

正常重启不会恢复，应用会一直保持卸载状态。但如果以后系统做 OTA 大版本升级或恢复出厂设置，预置应用有可能被重新拉回，届时再执行一次第 3 步即可。

当然，如果你不会用命令，可以开启USB试调后。直接让智能体完成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorcbic9eEhcyoFk14Wmxfqawa3uibibZ5SEwciacZuHmXwJk5HRAeN9WegMjA0JbyNiaoFYSdFotgW4ia5UTkr0xPMiaWfNzDAumBwZZnY/640?wx_fmt=png&from=appmsg)![卸载效果](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBord9eRpMiaRia2kIs99KAmK6hMFt55bylE45ObjsPFb2DwoicGFlf2bNpVO5nVuZt2gMIMjjEObmLiaFzficFQlib9d1O3d4o9opKecq0/640?wx_fmt=png&from=appmsg)

卸载效果

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorelzDSKo9DMF1953Ahicibvt5S9mTSicMsziadmibElIF0IxIHDEZRIdxnAsvsTHC0pBnY4xKVRN225VXSqKXh0DvPflXLYiclxd0o18/640?wx_fmt=png&from=appmsg)

更多精彩文章 欢迎关注我们

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQuRQ/0?wx_fmt=png)

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