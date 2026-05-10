---
title: iOS虚拟手机可以玩窗口化融合的越狱插件
url: https://mp.weixin.qq.com/s/uMrkYH5Hj9x9QKzK6IuuWA
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:30:21.054947
---

# iOS虚拟手机可以玩窗口化融合的越狱插件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Sq4BUsrXeTibCV0ibEicAkpdh1ib52ic5cbrfdHqPMjswoOU4E8eaItInoxpwsvHlEY7aTM1cv2Blv25LeEKm76knrhQTzgjQicia3WxDzialUFBeBA/0?wx_fmt=jpeg)

# iOS虚拟手机可以玩窗口化融合的越狱插件

原创

非虫
非虫

软件安全与逆向分析

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

上一篇《iOS虚拟手机实现能力现状》已经把虚拟手机能跑、能装、能控、能切换环境这几件事讲清楚了。既然底座已经能稳定越狱、能保留状态、还能做自动化。所有的准备工作做好后，下一步要问的，肯定就是有什么好玩的插件？怎么给虚拟手机安装越狱插件？不要急，这一篇就讲这个。

本篇介绍的`MilkyWayReborn`是iOS上一个集多窗口和窗口缩放能力于一体的越狱tweak。它支持在同一块屏幕上，可以同时打开多个App窗口，而不是只能在虚拟手机屏幕的前台、后台和分屏之间来回切换。

顺便提一嘴，安卓设备现在也有了类似的工具，有机会我也会在后面的公众号文章中介绍，大家拭目以待吧。

## 项目介绍

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTicpam90A0r7OzBKnho07kic6wgPoZXjbubdgphoYeCyR72SJdIpYroksA6TPtEUsX5OJicAuzsZ03kEyjm2Xyo9bcJ6TXcjRTCYU/640?wx_fmt=png&from=appmsg)

先看仓库本身。

```
https://github.com/34306/MilkyWayReborn
```

这个仓库是一个越狱插件，包名是`com.milkyway.reborn`。仓库文档描述它是一个用于在同一屏幕上同时使用多个App的多任务tweak。查看它的control文件，定义是给iOS18和26用的窗口化多任务插件，也是`MilkyWay2`的现代重写版。这个版本范围对于安卓研究设备的版本号来说，够宽泛也够用了。

从工程结构看，它是典型的rootless的`Theos`包，`Makefile`里明确写了`THEOS_PACKAGE_SCHEME = rootless`，目标架构是`arm64`和`arm64e`。这意味着它不是传统老式越狱时代那种随便往系统目录里塞文件的玩法，而是按现代rootless越狱的布局来做的。

功能源码主干由这几个模块组成：

* `Tweak.x`

  ：负责hook系统和场景流程。
* `MWWindowView.m`

  ：负责窗口外壳、按钮和拖拽缩放。
* `MWBackgrounderManager`

  ：负责管理哪些App要保持前台状态。
* `MWSceneHelper`

  ：负责场景唤醒、休眠和查找。
* `MWPassthroughWindow`

  ：负责把内容挂到合适的透传窗口里。
* `MWThemeManager`

  ：负责窗口样式和控件外观。

基本能看出，它是直接插进`SpringBoard`和`Scene`系统里，把App变成可以拖来拖去的窗口。

## iOS虚拟手机越狱

要让这个插件跑起来，前提不是安装包，而是先把iOS虚拟手机搞成越狱状态。

在前一篇文章里，iOS虚拟手机的越狱路线已经讲过了，核心思路就是走`vphone-cli`的`Jailbreak`变体，而不是在系统起来以后再单独找一套传统越狱方案。这个路线会把系统、启动链、用户态工具和bootstrap一起准备好，最后给你一个已经具备`/var/jb`布局、能装包、能加载`Substrate`插件的虚拟iPhone。

如果你沿用前一篇的虚拟手机构建链，通常就是直接选`JB=1`这条路：

```
make setup_machine JB=1
```

简单的讲，虚拟手机越狱后，在安装插件之前，先确认这几件事：

1. `Sileo`

   或者等价的包管理器能正常打开。
2. `mobilesubstrate`

   已经在系统里。
3. `/var/jb`

   存在，说明是rootless布局。
4. SpringBoard重启后不会把越狱环境打回原形。
5. 你能在虚拟机里装一个最简单的tweak并让它生效。

如果这几步没问题，说明虚拟手机已经具备安装`MilkyWayReborn`的基础条件了。

## 安装越狱插件

`MilkyWayReborn`的安装方式很标准，就是越狱插件的那一套。因为它依赖`mobilesubstrate`，所以本质上是一个要被注入`SpringBoard`和目标App的动态tweak。

`make package`先生成`.deb`包。然后把编译好的包通过SSH丢进虚拟手机，接着使用`Sileo`或者`dpkg -i`安装，装完后respring一次，让`SpringBoard`重新加载注入链。对于rootless环境来说，这种方式最稳。

安装完成后，重启一次`SpringBoard`。再用一个简单App测试，长按图标菜单里有没有`Open in Window`。如果这个入口出现了，说明插件已经注入成功了。

## App窗口化技术

`MilkyWayReborn`的核心不是“加个小浮窗”，而是把一个App真的变成窗口。

它在主屏图标上挂了一个快捷动作，名字就是`Open in Window`。也就是说，你长按某个App图标时，不只是打开或者卸载，还能直接让这个App以窗口形态启动。这个入口很适合iOS虚拟手机，因为虚拟手机本来就强调可重复、可自动化的操作流程，少一次手动切换，体验就完整很多。

窗口本体也做得很完整。`MWWindowView`里能看到标题栏、关闭按钮、最小化按钮、最大化按钮和右下角缩放手柄。窗口可以拖动，缩放手柄可以拖拽改变大小，双击缩放手柄可以把窗口恢复到内容视图的原始比例，长按缩放手柄还会按当前设备方向做一次旋转校正。

插件最难的部分，不是画窗口，而是让窗口里的App别被系统赶回后台。`MilkyWayReborn`在这里下了很重的功夫。源码里能看到它对`FBScene`、`UIMutableApplicationSceneSettings`、`_UISceneHostingActivationStateHostComponent`和`SBApplication`都做了处理，目标很明确：只要这个App被标记为窗口化，就尽量维持它的foreground状态，避免Scene系统和RunningBoard把它当成普通后台应用处理掉。

更具体一点，它会做这些事：

* 记录需要保持前台的bundle ID和scene ID。
* 在场景更新时强制foreground。
* 在deactivationReasons变化时把退出理由压住。
* 在应用退出时清理状态，但不让残留assertion拖垮系统。
* 通过`RBSAssertion`和`BKSProcessAssertion`维持进程活性。
* 必要时再做一次`task_resume`或者`SIGCONT`补救。

`Tweak.x`里有一个很关键的入口：它会从图标快捷菜单启动目标App，等Scene真正起来以后，再把Scene包进`MWWindowView`，最后挂到主机窗口上。这样一来，多个App都可以各自拥有自己的窗口外壳，互不遮挡时就像并排桌面窗口，叠起来时又能靠拖拽切换前后层级。

`MWBackgrounderManager`在这里也很关键，它专门维护哪些bundle ID和scene ID应该被视为foreground。换句话说，这不是单个窗口的静态UI，而是一套可以持续追踪多个App状态的管理器。

这也是为什么它在iOS虚拟手机上特别合适。虚拟手机本来就适合反复回滚、反复验证和批量测试，一旦再加上这种窗口化能力，很多原本要来回切App的操作，就可以在一屏里完成。

## 总结

`MilkyWayReborn`不是系统级分屏方案，它是越狱插件，靠的是Scene、`SpringBoard`和私有API。换系统版本以后，相关hook点很容易漂移出现不兼容的问题。

另外，它依赖`mobilesubstrate`和rootless越狱布局。如果虚拟手机没越狱，或者bootstrap不完整，插件都不会起来。

还有一点很重要：它追求的是窗口化体验，不是多开沙盒隔离。也就是说，App本身的数据边界和系统限制并没有被重写，只是交互形态被改了。这个区别要分清，不然很容易把“窗口化”误解成“多开”。

如果把iOS虚拟手机看成一台研究机，那么`MilkyWayReborn`做的事情，就是给这台研究机补上一层桌面化交互能力。但关于App控制的玩法远不止如此，相信后面社区还会有更多这样优秀的插件诞生。

前一篇文章讲了“虚拟手机能不能稳定跑起来，能不能越狱，能不能自动化”。这一篇讲的是“既然能跑起来，能不能把它变成一台可以同时跑多个App的窗口机器”。那下一篇讲什么好呢？

最后，抛出一个问题：既然能控制App的启动与窗口化，那是否可以实现安卓系统上那样的“多开”功能？欢迎大家在评论区讨论。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

软件安全与逆向分析

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

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