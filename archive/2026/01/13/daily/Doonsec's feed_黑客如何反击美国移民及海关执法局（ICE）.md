---
title: 黑客如何反击美国移民及海关执法局（ICE）
url: https://mp.weixin.qq.com/s/vy7evQED0A1-5GCaXs42lA
source: Doonsec's feed
date: 2026-01-13
fetch_date: 2026-01-14T03:33:17.766068
---

# 黑客如何反击美国移民及海关执法局（ICE）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkpMibchcmeNze5icd5QqsmxnvhKdyAO2cuLTiaiccfckcHicGkVIobKDM5AOydmoA7ZdhYWqIsPlw4NO6A/0?wx_fmt=jpeg)

# 黑客如何反击美国移民及海关执法局（ICE）

原创

黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

美国移民及海关执法局（ICE）已斥资数亿美元用于监控技术，监视美国境内的任何人，甚至可能是全球所有人。

详情可见[美国移民及海关执法局（ICE）的监控工具们](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184730&idx=1&sn=ab5c3b4cbbb0db1bf11df0c119d0b9f9&scene=21#wechat_redirect)

面对如此强大的力量，人们很难想象该如何自卫。

但一些富有创新精神的黑客已经开始着手开展反监控项目，旨在通过巧妙运用技术来保护他们的社区。

先谈一下Flock公司，这家公司开发了许多自动车牌识别（ALPR）和其他摄像头技术。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqia9gK8eOF6YY3HcUvP393EEbp2HCkx1ZOsly0ibwkubkicq3icVrDmibSNhmzKIDmRDvcZpCD0IgYmaw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqia9gK8eOF6YY3HcUvP393ExGcJuBI8ee7Go3bXCLZuA8THdrktkLVtUgKZ9nnZ1tO8pFjmWU8GKA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqia9gK8eOF6YY3HcUvP393Eo03ZdPR170wP96b4J8H5wT8Ir8D00zweWzE7dhXmy1icdjicm8JzdcuA/640?wx_fmt=jpeg)

美国许多大大小小的市政当局都与Flock公司签署了协议，使用车牌识别器来追踪城市中所有车辆的行驶轨迹。尽管这些协议是由地方警察部门签署的，但美国移民及海关执法局（ICE）通常也能获得访问权限。

由于Flock摄像头的普及，人们很想知道社区里有多少个摄像头以及它们的具体位置。

OUI-SPY项目可以帮助解决这个问题，它是一款小型开源硬件。

https://github.com/colonelpanichacks/oui-spy

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqia9gK8eOF6YY3HcUvP393EMiaxvXBicSE4skBOzZEpZicnuyKRCqspS8Oicdw7WJ2eLgLfmcS4nN9g0Q/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqia9gK8eOF6YY3HcUvP393EKqicS0OHITZnRATlBM3c7NzWp8HufkZ4XR4mHvfvv6lfEIyf4dbM1UQ/640?wx_fmt=jpeg)

OUI-SPY运行在名为ESP-32的Arduino芯片上。

该芯片可以加载多种程序，例如“Flock You”，它可以检测Flock摄像头；

“Sky-Spy”，它可以检测空中无人机。

此外，还有“BLE Detect”，它可以检测各种蓝牙信号，包括Axon、Meta的Ray-Ban等设备发出的信号（这些设备会秘密录像）。

https://github.com/sh4d0wm45k/glass-detect/blob/main/glass-detect/glass-detect.ino

它还具有一种追踪模式，可以用来追踪特定设备。活动人士和研究人员可以使用这个工具来绘制不同技术的分布图，并量化监控的扩散程度。

还有一款名为Wigle 的开源应用，

https://wigle.net/

它主要用于绘制 Wi-Fi 地图，但也具备在检测到特定 Wi-Fi 或蓝牙标识符时发出语音警报的功能。这意味着您可以设置 Wigle，以便在检测到附近有 Flock、Axon 或其他恶意软件时收到通知。

一位YouTube博主想出了一个办法，只需在车牌上涂抹一些轻微的视觉噪点，就能骗过Flock摄像头，使其无法识别车牌。

https://www.youtube.com/watch?v=Pp9MwZkHiMQ

这种噪点并不显眼，人眼仍然能够看清车牌，但却能彻底阻止Flock设备识别出他的车牌。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqia9gK8eOF6YY3HcUvP393E2x0mWttMtMrZCo4nDmZTgYrCu7I1bmn8YJkZB7SwX24n2icrW3spVGA/640?wx_fmt=jpeg)

一些美国的州已经禁止驾驶员遮挡车牌，因此不建议采取这种做法。

该人员后来发现数百台配置错误的Flock摄像头，其管理员界面在没有密码的情况下暴露在公共互联网上。

这意味着任何能上网的人都可以查看实时监控画面、下载30天的视频、查看日志等等。

这些摄像头对准了公园、公共步道、繁忙的十字路口，甚至还有一个游乐场。这严重违反了公众信任，对于一家声称致力于公共安全的公司来说，这是一个巨大的错误。

其他黑客也承担起了开源情报和社区报告的任务。deflock.me和alpr.watch就是一个有趣的例子，它们是由众包方式生成的车牌自动识别摄像头地图。与 OUI-SPY 项目类似，这使得活动人士能够绘制并曝光其所在社区的 Flock 监控摄像头。

https://www.atlasofsurveillance.org/

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqia9gK8eOF6YY3HcUvP393E2XDsdHO3ibicsicoGj3Sep2IDyGiaxUDba1QhngShY16bydr3g8pYs7xAA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqia9gK8eOF6YY3HcUvP393E6hIqtbicVCTCWiaRRPV0s6vib8dl2q3teZHhUKGdTAtA3SHDtJZAf4rLw/640?wx_fmt=jpeg)

此外，还有几款举报移民执法局（ICE）活动的应用程序发布，包括用于举报所在地区ICE人员踪迹的应用程序，例如Stop ICE Alerts、ICEOUT.org和ICE Block。

https://stopice.net/

https://iceout.org/

ICEBlock应加州总检察长帕姆·邦迪的要求被苹果公司下架，我们已就此事提起诉讼。还有一款名为Eyes Up的应用程序，用于安全地记录和存档ICE的突袭行动，该应用程序已于今年早些时候被苹果公司下架。

另一个记录美国移民及海关执法局 (ICE) 并创建大量开源情报的有趣项目是ICE List Wiki，其中包含与 ICE 签订合同的公司、与 ICE 发生的事件和遭遇以及 ICE 使用的车辆等信息。

https://wiki.icelist.is/index.php?title=Main\_Page

即使不懂编程的人也能参与其中。在芝加哥，人们使用哨子来提醒邻居美国移民及海关执法局（ICE）人员已出现或正在附近活动。许多人利用3D打印技术制作哨子和使用说明手册，分发给社区居民，从而扩大了哨子的覆盖范围，使邻居们能够更早地收到预警。

许多黑客开始为他们的社群举办网络安全培训，或建立提供安全建议的网站，包括如何将数据从监控行业的监视下移除。为了覆盖更广泛的群体，一些培训师甚至开始在电子游戏（例如《堡垒之夜》）中举办关于如何保护社群以及在移民执法局突袭中该如何应对的培训。

此外，EFF 还开发了 Rayhunter 项目，用于检测基站模拟器。Rayhunter 运行在廉价的移动热点设备上，使用起来也不需要深厚的技术知识。

本篇为随笔，仅供参考，相关工程自行研究。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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