---
title: FanchmWrt系统安装注意事项
url: https://mp.weixin.qq.com/s/DSDvr3vLtQVsiKPSxEV-QA
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:38:42.354360
---

# FanchmWrt系统安装注意事项

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4dGgALU2VXyJwdlrk3a9myOyMaia5zpg4TE6YoPrceQfe6eNibu90zicoRPPSoJdibTgrIDEvo8wkH0F2KScZ5Qib3g/0?wx_fmt=jpeg)

# FanchmWrt系统安装注意事项

原创

TT
TT

OpenWrt

![]()

在小说阅读器中沉浸阅读

FanchmWrt系统已经发布了一段时间，得到了大量用户的好评，当然也收到了一些问题反馈，问题主要涉及系统安装和插件安装，这篇文章给大家讲讲系统安装的注意事项。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXwSg6Sric07OfyiaF9aBnNvaOEFV6j0YQgrlKw7tRT0FVRM6SjB0JW0xJXhVeEB2xKCNGsylXWVI1og/640?wx_fmt=png&from=appmsg)

FanchmWrt是基于OpenWrt官方稳定版本开发的系统，完全保留官方固件的所有特性，加入了一些商用路由器级别的插件，比如终端管理、上网行为管理等，后续还会加入更多功能，该系统和官方OpenWrt完全兼容，可以相互升级，并且固件非常精简干净，X86的固件大小都只有20多兆，如果想用其他插件，直接在软件中心安装即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXwSg6Sric07OfyiaF9aBnNvaOvLMvdDxNnPuHl4ltDkWXZexY1oPHhgYzvQ5nzJic2yUPwL4DywI2IQw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXy5Jvpn4WVibTc6ibn2ibUUy9SAkjqPGp4dSfYTFk81XH3FYnBUIJckeHu6ZqAyibiccTa3qf0UVJN7KMQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXy5Jvpn4WVibTc6ibn2ibUUy9SOsS4kcQmNbiaPkTLYmQ0bON9Y0f6qMPvFo3DxOBonz9OkE3mibwkM8Ig/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXy5Jvpn4WVibTc6ibn2ibUUy9SIlX4clGb2cqFLo3qcct2Ajq0FE8waPsdPibrsJMKkVfaKAwcJGDMXGw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXy5Jvpn4WVibTc6ibn2ibUUy9SicGlpticKfcMOcLF3hhDhc2jZsfZAwKeyJAQrshyHy0U5DxaRYZf9Avw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXy5Jvpn4WVibTc6ibn2ibUUy9SzsZWQIBAKriaX4Y89MYQHvggtHTz9kvecQKa7FeqAUsM19db6ic9b0gw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXwSg6Sric07OfyiaF9aBnNvaOf4anicBoSwtYU61nLEOVw9qk6SWicibMibTcp1Q3ymfDmQ1mVORD5YggLg/640?wx_fmt=png&from=appmsg)

如何正确安装FanchmWrt？

建议大家先查看官方OpenWrt系统安装的教程，然后在OpenWrt系统的web界面升级FanchmWrt，教程都是通用的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXyJwdlrk3a9myOyMaia5zpg4xNopLQ2oCPQ33DMD6r4Z482nNia4yAFjowFzUAy897hSIS5fZeW5dlg/640?wx_fmt=png&from=appmsg)

itb固件如何升级？

大家可以发现，很多mt798x芯片设备的固件是itb格式的固件，这是openwrt新版本的固件格式，是无法在一些不死uboot下升级的，需要用官方openwrt对应的uboot才行，但是官方的uboot没有web界面，需要利用tftp升级，会麻烦一点。

过几天我也会适配一些设备的bin格式固件，比如jcg q30、h3c nx30等，这样就不用换uboot，直接通过uboot界面升级即可。

如何安装插件？

FanchmWrt支持安装常用的插件，只要不依赖特别冷门的内核模块，都可以安装成功，系统默认采用OpenWrt官方的软件源，当然如果你想使用国内的某些插件，也可以切换为ImmortalWrt软件源进行安装，注意需要把签名校验关闭，具体可以参考FanchmWrt官网的教程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXyJwdlrk3a9myOyMaia5zpg4XAL3qucMFVJeM1oNVwWLpy7dlJ2woia2ZIKtsVLc3SKglZqfXEOAQag/640?wx_fmt=png&from=appmsg)

X86设备支持安装docker，如果是安装docker请使用默认的OpenWrt软件源。

X86设备扩容

X86设备性能较强，一般都会安装一些大型插件，但是系统默认的可用空间是比较小的，需要对磁盘扩容，关于如何扩容，OpenWrt官方也给出了教程，我也在FanchmWrt文档中心进行了总结，可以参考。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXyJwdlrk3a9myOyMaia5zpg4RcZNVjREj1KzMeIic6OPyIUMFKwu0VpT5ZZh2EZnaY0FAhQz7WDzQpw/640?wx_fmt=png&from=appmsg)

之所以默认没有对系统扩容，主要还是为了兼容官方OpenWrt系统，如果做了默认扩容，就没法和官方OpenWrt系统互升了，如果要从OpenWrt切换为FanchmWrt，只能通过写盘重装。

这里我也征求大家的意见，看是否需要默认对系统扩容，可以在下方投票

设备支持

自动上次发布公测固件后，又发布了一些热门的设备固件，大家可以下载使用，FanchmWrt支持所有OpenWrt官方支持的设备，可以自行编译出对应的固件，但是为了正常运行，要求设备的闪存至少16MB，其他参数没有限制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4dGgALU2VXyJwdlrk3a9myOyMaia5zpg41O0saS9UE5KjIbQ1aznf8cr3RdLwyNKlV5w1Hjfiary2jiaEGTuS8ELw/640?wx_fmt=png&from=appmsg)

开发计划

关于AI魔改OpenWrt系统系列的文章暂停几周，这几周将会重点编写一些技术文档，让更多人用上FanchmWrt系统。通过一些交流群我发现很多用户连旁路由、软件源、DNS等都不会配置，急需来一些科普文章。

---

历史文章：

[支持刷机的路由器(2025)](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486582&idx=1&sn=9602044c4ef4b94f28b9473766958efa&scene=21#wechat_redirect)

[AI魔改OpenWrt系统第10周，公测固件发布](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486626&idx=1&sn=7a820e336e0690546d83b4bcffb2c9e3&scene=21#wechat_redirect)

[AI魔改OpenWrt系统第9周，代码已开源](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486612&idx=1&sn=edaefac9fccf9b98bb590eab4ac07f0f&scene=21#wechat_redirect)

[AI魔改OpenWrt系统（第8周）](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486575&idx=1&sn=2105974980d18290ae0d7cdca3ce4a5c&scene=21#wechat_redirect)

[OpenWrt支持手机App管理了](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486448&idx=1&sn=97a3276f3779ed7c82870a78c898d412&scene=21#wechat_redirect)

[H3C NX30 Pro路由器刷机教程（拆机版）](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486399&idx=1&sn=cc14c655ad52a395b35f79dca50f022c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/4dGgALU2VXwxOVx85bAbC3CbFUBYEHduhydpeBQNuGCgk5xPlneKvuO7LSjFTYdEMoSffnUichcTV8Z2xFF25Qg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=dm2rfhjh&tp=webp#imgIndex=15)

欢迎关注公众号

定期分享OpenWrt干货

OpenWrt应用过滤插件作者(2.5k star)

FanchmWrt系统作者

预览时标签不可点

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