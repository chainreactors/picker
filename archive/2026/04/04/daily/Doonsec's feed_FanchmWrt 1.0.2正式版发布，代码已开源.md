---
title: FanchmWrt 1.0.2正式版发布，代码已开源
url: https://mp.weixin.qq.com/s/k73aeGyn2kPAESTbWvKz_w
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:32:23.608018
---

# FanchmWrt 1.0.2正式版发布，代码已开源

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/raicmpgShpRmHY7kic04MSgN9hphgy01zBGx9dHZadeEQaeoz7POhv2fiahoFUFn7pxf26cUHnsCoPVzDZOYIpJuQogj8Gz0cMe5tfN4RSGZZ0/0?wx_fmt=jpeg)

# FanchmWrt 1.0.2正式版发布，代码已开源

原创

TT
TT

OpenWrt

![]()

在小说阅读器中沉浸阅读

前段时间发布了FanchmWrt 1.0.2 beta版本，收到了一些bug反馈，这几天对bug进行了修复，并且已经将所有最新代码提交到了github。代码默认分支切换到了25.12.2，基于OpenWrt最新稳定版本25.12.2集成FanchmWrt特有的功能。

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRlG2CPYtL2uIcicswks17B14Vy9UapGLcQfln2Iics40icu6f9kSWM2tzxIHnmeVtKQ5ibUXTpyzcznpfD6NsI63ZO8OMTra4ib3lYQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRnibCB2IrXiaCldWc806QjDkIqRNQrKMCjjWnHbXYecKEqkdpfDRTKEkzYHxoLghOZRohia6fc09dyC3Jx37iauR5dER8zrBItRzE0/640?wx_fmt=png&from=appmsg)

相对beta版本主要修改内容如下：

1. 修复高级模式某些菜单重复渲染问题。

2. 优化终端上下线记录模块，增加防抖机制。

3. 终端列表支持活跃状态显示。

4. 优化会话数统计图表显示。

5. 消除防火墙界面告警提示，默认去除iptables模块。

对于X86设备，修复了命令行终端IP地址无法修改的问题，X86重新上传了固件，如果前几天已经升级1.0.2版本，需要重新下载升级。

固件下载地址：

www.fanchmwrt.com

![](https://mmbiz.qpic.cn/mmbiz_png/raicmpgShpRlIbz0WOZnC2vLqcITl5iaiaeqACRnvSyF2ib1cN1ibMvCmtaErKrtVeq2nNxC7PpBQWpBkAvEY1Yu2G3hE4kjjOaXc2sY6QjEVgZY/640?wx_fmt=png&from=appmsg)

答疑：

下面针对反馈的问题进行简单答疑，有些问题我在官网或者在前面的文章中也已经讲解过。

1. 如何升级使用FanchmWrt系统？

升级方法和官方OpenWrt升级教程一样，可以通过OpenWrt官方的固件直接升级，注意一定要是OpenWrt官方发布的固件才可以直接通过页面升级，对于其他分支的OpenWrt无法通过界面直接升级，需要通过uboot升级或者重新刷机，对于798x系列的设备，uboot也要采用支持itb格式的版本，不同的uboot适用的固件不一样。

由于可刷机的设备非常多，我短时间也出不了太多设备刷机教程，官网有几款热门设备的教程，可以参考，由于有些厂商也不断在修改硬件，大家刷机前一定要多查看最新信息，看是否有翻车情况。考虑到很多用户不会刷机或者不想折腾，等FanchmWrt基础功能稳定后会定期出一些刷好的设备，有很多粉丝后台给我留言需要设备，由于现在开发任务比较重，还没有太多时间，所以对于新手需要再等一等。

2. FanchmWrt性能问题

FanchmWrt的基础性能和官方OpenWrt保持一致，包括有线转发、无线转发等，基线代码都是基于OpenWrt稳定版本，如果有疑问可以对比OpenWrt官方的版本测试，当然由于官方OpenWrt是没有加速之类的模块的，所以性能相比一些闭源的固件会差一点，但是用OpenWrt本来就是冲着开源生态来的，不然直接用官方的固件性能会更好。对于一般家庭来说，性能足够用了，不行就换配置高点的设备。

3. 如何安装国内的一些插件

immortalwrt的软件源集成了大量国内用户需要的软件包，可以在FanchmWrt的软件中心修改软件源为immortalwrt的，这样就可以直接安装特定插件，具体方法参照官网教程，非常简单，注意immortalwrt的25版本还没有发布，所以目前只有FanchmWrt的24版本才能用上immortalwrt的软件源，25版本需要immortalwrt官方发布。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/raicmpgShpRmUsKMBc8rmXiab4X2yUP4hheDk8G0Tg1t2IQZqVMicqGJR5y9pcsKqEadlUoqTZXLOVjUVFXCn3rsrNeTVdXJpkKGEfNlLKUfDs/640?wx_fmt=png&from=appmsg)

4. FanchmWrt可以安装OAF插件吗？

由于FanchmWrt的某些模块是基于OAF修改的，所以不能再次安装OAF，本身就已经有了应用过滤功能，支持了多规则配置，后面还会增加时长控制等。当然有些用户想安装OAF通过OPAssistant手机App管理设备，但是目前FanchmWrt还不支持，需要等后续开发，如果确实有App管理应用过滤的需求，暂时先用OAF的固件，等FanchmWrt上线App后再切换过来。

OAF官网：

www.openappfilter.com

注意事项：

1. 如果你想要安装更多的插件，推荐用24.10.4-1.0.2版本，因为OpenWrt最新的25版本采用了apk软件包，多少存在一些问题，还需要时间来验证。

2. FanchmWrt24.10.4-1.0.2目前发布了x86、798x、7621等热门芯片的产品，有些还只有beta版，正式版本会晚几天上传。

3. 如果固件已经是1.0.2-beta版本，可以通过页面直接升级到1.0.2，无需恢复出厂，后续的版本没有特别说明也都可以保留配置升级。

4.  对于Cudy tr3000设备，很多老铁需要用到USB，将其改造成CPE，最新的版本也默认集成了相关的驱动，可以正常使用。

计划：

接下来会整理一套基于OpenWrt主线分支的代码，用于适配更多的设备，比如JD无线宝系列，亚瑟、雅典娜、太乙等，敬请期待。

---

历史文章：

[FanchmWrt 1.0.2beta版本发布](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486667&idx=1&sn=6d15debe07f87711cba07fab0c614ba7&scene=21#wechat_redirect)

[FanchmWrt系统安装注意事项](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486636&idx=1&sn=a9643c0e95f7184ebf15eace9b5f8b0f&scene=21#wechat_redirect)

[AI魔改OpenWrt系统第9周，代码已开源](https://mp.weixin.qq.com/s?__biz=MzU4MTgxNDc2MQ==&mid=2247486612&idx=1&sn=edaefac9fccf9b98bb590eab4ac07f0f&scene=21#wechat_redirect)

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