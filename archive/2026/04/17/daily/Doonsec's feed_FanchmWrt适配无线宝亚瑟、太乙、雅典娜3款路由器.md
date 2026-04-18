---
title: FanchmWrt适配无线宝亚瑟、太乙、雅典娜3款路由器
url: https://mp.weixin.qq.com/s/aa_VWj6OsW_7SeU7StG_CQ
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:25:03.652939
---

# FanchmWrt适配无线宝亚瑟、太乙、雅典娜3款路由器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/raicmpgShpRkl8eUIsWNNeJ3y45nmU3DLa49Jp0icyDuQ7fHqy4RNz8OJL4Niah3GxicckFVeW4Cz62XK4WnYzCI64ZVYiba3usmxWh0bewWRJkQ/0?wx_fmt=jpeg)

# FanchmWrt适配无线宝亚瑟、太乙、雅典娜3款路由器

原创

TT
TT

OpenWrt

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

大家好，前几天终于完成了京东无线宝系列三款设备的固件发布，这三款设备分别是亚瑟、太乙和雅典娜。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRmXTtnxxYOlDYQwpxBUAiavbJHcTSbvmXKN2A06IVnwzG4KNosWwMIbCokib83XSU7q3z0SJKIoicR2A9ELlroicXXMBH6I4LJqUuo/640?wx_fmt=png&from=appmsg)

前面之所以没有发布固件，是因为主线OpenWrt的稳定版本还没有支持，当前我发布的固件也是基于OpenWrt主线代码编译，修复了一些小BUG，通过一段时间的测试，基本功能没有问题。

由于是基于最新的OpenWrt代码编译，所以没有固定的OpenWrt版本号，属于snapshot版本，当前版本号命名为snapshot-1.0.2，之所以没有根据日期命名是因为容易误解，目前最新的OpenWrt稳定版本号也才到25.12.2。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRmLSWxmfhKSLrOSvm3lzu25JTc7VjqVphIm1m5mvKkF99pyKiaicqmJmGG9dH4HEqC8XBOItNyD1QYDZwSWajwOHuqJLhXwc8M7o/640?wx_fmt=png&from=appmsg)

这三款设备有什么特色？

都采用了高通IPQ6010主芯片(4核 ARM Cotex-A53架构)，主频1.8GHz，并且内存和存储都比较大，带有USB接口。

这三款设备都适合拿来刷机，既可以跑一些插件，又可以当轻Nas使用，并且性价比也高。现在全新的雅典娜也才不到300元，内存1G、存储128G、WiFi6 3频 6600Mbps，这个配置应该没有对手了。对于亚瑟和太乙(ER1)，目前官方没有全新的产品出售了，只能咸鱼或者其他平台购买，亚瑟二手价格不到100元，太乙200元左右。

我个人特别喜欢太乙这款产品，不带无线，纯做网关使用，内存2GB，特别适合刷FanchmWrt做一台上网行为管理设备，放在弱电箱也方便，如果是商用企业产品，这个配置最起码卖1000元以上。FanchmWrt后面的目标就是给大家提供企业级的软件，让大家的低成本设备用上企业级功能，比如上网行为管理、AC控制器、认证等。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRnwGiae1mfDPqFQOCMH04mMwKVMBmBxvDJ7Jfo6M3ZvoZEEEB5iaAJTSCCe5uJDTPqH2MjYWVrK8zToUKqyuv4a8icPF0qk5ZK5ls/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRlQP6ZiajViaTxzAWDZiaicJjvTFau5QnzceqdfZjv32V5KHx3zl8ZpFic7fym4JybaicDj5icdhZSzc60gXvJjbjZybY1AvFibxs0f41c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRlq6xjMgLfL12uJqXDMIia83wkRRlXicmn8WpTAniaSyKCBGuREpWCDIQWHy8Rzwltxuwxx2zbkc6GuADEhoFTYWmqzjTWUNbQZag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRlb0clp4EVyPuuxeFgRQepNElsSyWaEh9mT09VtWn0mqm8xB04ybngYLKQ86CsJmdGzJEYn43VtIk83eRmvQhn0v6pwicSwLqGw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRn0gaolZs7PibJFz5DYI8DTXoVj7ujj7vSTCcXz8XZ7ibXDElRSYPdhNTb5YkfwhhiberEXkG3QQVHwhK0dCeBiaGZPnE2O2GGHAb0/640?wx_fmt=png&from=appmsg)

固件特性

基础的功能和其他型号固件类似，包括FanchmWrt特色功能，比如上网行为管理、终端列表、仪表盘等，默认集成了一些常用的内核模块，方便安装插件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRlagibadO9eHws86t8NehwtS250RYj6qdJRicMSUNWhC72hqu4hcnrdehibWPH8sMk51I6odCjYU1ICxyDE6MkBKlq0El2cUrQ06g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRkuJ7QoYBica8xTcVDg6Fo2Y8hG0tBmN5HVJu9X6BGJIvvGiaaGTrIianMrQhCoWnuAeu4RtBJYZSng3nhPdicXhkLhEemLdRUUAn0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRnRO4eg6pA6SvVmul6EMFia4qB7PQarjPA99EGKcficnibDj1zZXRicS7adltOV1vnmzk0y4q8bEQOnvjfowbrYnZ2NWAyW82AV9JI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRmw0l7sBiaAdQQSs2HTjSdFhrYDbvriaK1D0fqsb7z9pgm2e7iarfGYKLBosL2ZyIk34xc1c68YkNkZia9GDhLpavmy5yryjGpNfAY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRlMcj6o5GSgE6eMGRIF9ibZCibbSGKwImYA6F8J6pyeoYno0aVNickBvPDLm0F7YicYFd5IlkibykUmWGfZfKNBrLqjoTcSWQXezqibg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRmrjnlFYyfk8mEtE0zyoDcDd4oGFSrN6HLm4GwddBzwZy6tia4a1Tj0icwKWCn2y2gvU7GiacotMjcluZN1EdcmT1DcibuX1hthPuo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXy5Jvpn4WVibTc6ibn2ibUUy9Sa6SNOxnbKSCAgRj63VEzfwv0vYKdtibzqN45NQPFRFRcV4Zr3X7U0SA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXy5Jvpn4WVibTc6ibn2ibUUy9Syz3tllha0a29F60x9fP9bOYYS9yddlSraiasNNXibHl5TeUDiafAKB4bQ/640?wx_fmt=png&from=appmsg)

如何升级？

首先要求以及刷好了不死uboot，通过uboot页面升级factory固件即可，后续升级新版本可以通过FanchmWrt页面升级sysupgrade固件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRmPMuS7hejsEIb63ufOUfyIHuibrqquN8KdzHKlYmUDFJYQ3Pk0E5Ftju9bUvLfzvgRncicM20iazhG4AwZ1aOHsTic2Sw29icuBICQ/640?wx_fmt=png&from=appmsg)

如何安装插件？

由于采用OpenWrt非正式版本代码编译，所以只能使用snapshot的软件源，可以切换为第三方的软件源安装更多国内插件。由于最新的OpenWrt代码采用了apk包格式，安装第三方插件需要强制校验签名，目前我修改了代码进行了强制安装处理，可以切换为immortalwrt软件源安装，注意在使用国内软件源镜像时，snapshot可能没有同步，可以切换为相近的rc版本软件源安装，比如25.10.0-rc版本，目前immortalwrt还没有正式发布25.12版本。

这里顺便说下其他型号设备25.12版本安装第三方插件的问题，目前切换源后无法直接通过页面安装，只能通过apk命令强制更新和安装软件包，可以参考FanchmWrt官方的安装文档，而24.10版本是没有限制的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRk1CssHibmKGkq7zfrAcfWpaqOHFIvD4dPGKxBbUbW0ZxElnQ49VDvDzDm0GQN5RRux4qgu1ojSc1Xibc5rDSEerXOtuTuCVXIYg/640?wx_fmt=png&from=appmsg)

当然还有很多用户反馈的产品没有支持，我在适配时要看主线OpenWrt有没有支持，如果没有支持，暂不做考虑，因为还有很多新功能等待开发，没有太多时间，如果急着用FanchmWrt，可以先准备一台已经支持的设备。

---

历史文章：

[FanchmWrt 1.0.2正式版发布，代码已开源](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486676&idx=1&sn=1783274587d3dc681496bf52e3dad3ac&scene=21#wechat_redirect)

[FanchmWrt系统安装注意事项](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486636&idx=1&sn=a9643c0e95f7184ebf15eace9b5f8b0f&scene=21#wechat_redirect)

[支持刷机的路由器(2025)](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486582&idx=1&sn=9602044c4ef4b94f28b9473766958efa&scene=21#wechat_redirect)

[AI魔改OpenWrt系统（第8周）](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486575&idx=1&sn=2105974980d18290ae0d7cdca3ce4a5c&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4dGgALU2VXwGPhSnjG6IhzI0wCrUicApDmpsL1c5VyoWFph6dicu8RydO8StibF1ibHIF7zOeAUrz31GPo9UGqNOTw/0?wx_fmt=png)

OpenWrt

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4dGgALU2VXwGPhSnjG6IhzI0wCrUicApDmpsL1c5VyoWFph6dicu8RydO8StibF1ibHIF7zOeAUrz31GPo9UGqNOTw/0?wx_fmt=png)

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