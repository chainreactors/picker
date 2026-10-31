---
title: openpilot 全新 SR 上线：这次升级了什么？
url: https://mp.weixin.qq.com/s/81lYu7ZcPl5b_Fmo46t8vg
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:45:09.997657
---

# openpilot 全新 SR 上线：这次升级了什么？

# openpilot 全新 SR 上线：这次升级了什么？

原创

青春是猫科动物
青春是猫科动物

Septemberend

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 先看模拟数据的视频

# 碎碎念

实际上，应该早就开始研究这些东西了，但是之前用的 op 版本（主要是 cp），都是其他人适配好了的 PC 版，且无法平滑迁移到最新版的 OP代码，也尝试适配过几次，但是最终都没有解决。

再后来就是，国庆放假的时候，车 24 小时上电，从 DBC 开始重新适配最新的 SP 代码，然后就适配成功了（不是那么简单），顺便加了 yolo 目标检测，验证了技术可行性，这是后话了。

目前也有很多无屏/投屏的产品设计及SR等，如无屏 C2、无屏米 8、开发板/主机投屏等，但是这些方案都是局限在当前产品和需求，且与 OP 版本强耦合，很难去适配不同的版本，不同的分支，维护升级也需要耗费较大精力；同时各个产品/分支的数据都是独立分开的，缺乏数据采集中转，统一展示，对于用户来说，非常不友好；当然，不排除本篇文章发出后，会有产品跟进，把各个分支数据统一采集展示，敬请期待。

# 核心

当前产品核心功能是数据中转采集及回传：SR 数据、行程数据等

1. 数据中转采集，通过统一的 PC桥，将不同版本，不同分支的 OP 的数据采集中转，前置处理后回传给 APP 端，由 APP 入库展示；
2. 行程数据统一入库，根据不同的分支/版本，进行归类展示；
3. 打通 APP 端与高德的操作，可以直接在 APP 端搜索目的地，点击快捷目的地进行导航；
4. 通过 APP操作 PC 上的多个OP：启动，停止，重启；
5. 提供语音提醒：接管提醒、脱手提醒、变道提醒等；
6. 额外功能：比亚迪车型已支持通过 APP 进行控制转向灯，即后续可以自动打灯+自动变道了；
7. SR 界面与本车灯光联动：本车模型尾灯，转向灯，雾灯实时联动本车；
8. 更重要的是，除了导航是单端生效，APP 是可以多设备使用的，如车机开一个APP，手机开一个 APP，两个终端都可以展示SR 数据，接收语音提醒/告警。

# 后话

1. 当前版本已经完成了技术验证，且已经能看到效果了，但是还有需要优化的地方：摄像头数量不够、硬件瓶颈导致yolo模型频率不够、SR 画面还是不够美观（目前还是 MC 风格）、SR 的目标不能平滑显示等，这些就等接下来慢慢迭代优化了，争取尽快将产品发布。

2. 如需加 OP 的 QQ 技术群和微信群，可在后台发送关键词：openpilot-helper，会有人邀请进群。

# 功能展示

## SR

![](https://mmbiz.qpic.cn/mmbiz_jpg/O29dZl6WmzzWKiay0Hye6xPVwEqgCgDeibIAkuqZeZlELHya9zR5S8Ms0KHUpAcpibCQHBY8ZVDbu1yCGIQpQXfsrZRlricaf1Vfdo5wRywAJias/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/O29dZl6WmzxtA40FE0bP7ns60s4h9Z4yHL1GJxKhWooxmZZ05K1iaicYwkkzD9eicmSGP76MabHoHe4IOrYNFBdpvQdDQ9icVEU1wpNegWs8uNg/640?wx_fmt=jpeg&from=appmsg)

## 高德地图对接

![](https://mmbiz.qpic.cn/mmbiz_jpg/O29dZl6WmzxtDhrztY0uBp6Prusayic6MBiaN2XuZibDc3VyYDXjxkH8cUVV1x0y6lLlrXhiblWMMfFfpqhWAkbmFX6EEFcpFvoFXBoRuPwnXMA/640?wx_fmt=jpeg&from=appmsg)

## 行程展示

![](https://mmbiz.qpic.cn/mmbiz_jpg/O29dZl6WmzzlbE5SvyALNLQhYiabFUuNtZRsaY9ueib9GSibVAicMkBMnW6abEsicW5ZKNHGCOQsTfYZEmNwGnwvqG6MiczyWWhj0aZsakYAMWZoE/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/O29dZl6Wmzz5oOES1t0ic2XA06mux4N35MoMMMR6DpibV7ibcB20OE8Y3T8cnZYL4Xsv0sXQfRLhJIlG7ZOnPCDjLC3upiaV75ibaaLvPltmnqyA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/O29dZl6WmzwUiaibsIsge9X8nQh0Vn6bfoP4n11jxMf6mLfFiaMsFAMFNHhPJiaxXibav8fqBaRI6Gqm8rnHGvNZ54CbrN96ia6qIUNWoib7xPvH2U/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/O29dZl6WmzzicN3UoNmqVKmkJ65iahbwHjaEOzRqCycWPKFHQKyAjI8Ivx9QvvnvpIjefXAAj1wheic7ZyERdfW8aibiakjibsoMiameicVF8RLTaFY/640?wx_fmt=jpeg&from=appmsg)

## 实验控灯-比亚迪车型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O29dZl6WmzwavDCgeVGuQBhAcEMTT41yNicjDASUoM3ZaA9taXmd8jy0ibjnqROZUrAWWvceiaTelWibGIoJRPcaxuADkia3uibL4nbcP8M26oewc/640?wx_fmt=png&from=appmsg)

语音提醒

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O29dZl6WmzzaI8sQ1YUMe9ZOlZsxdQJ1f8GBatUEyhllVY85sORCoqvsjicJCPRO1cDvqovYB7bqOe6BMcmzVqyCHUGEmzvd0iamhuNUqI2lU/640?wx_fmt=png&from=appmsg)

远程控制 PC 版 OP

![](https://mmbiz.qpic.cn/mmbiz_jpg/O29dZl6WmzxtoEX5nCjZU1mdG7QuII6192N6aXuHpIlYKLybccjqc6PvKsoJ76kAhthZqV3mZmArl0XOdcySYRAJCU2oun525Hq18yGr75o/640?wx_fmt=jpeg&from=appmsg)

离“天神之眼-D”又近了一步！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/R4OBJlic3TItPXMDQjk6vzaGBJxK1tnN8DpG46d8AYAaKZhHj8YGUwvayIMppejl9ml024fWHwUcQljhkMLMXXA/0?wx_fmt=png)

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