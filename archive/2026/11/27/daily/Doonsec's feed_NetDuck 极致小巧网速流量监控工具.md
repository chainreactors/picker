---
title: NetDuck 极致小巧网速流量监控工具
url: https://mp.weixin.qq.com/s/v70o8epgHkoqB5lO5X-FvQ
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:36:25.449575
---

# NetDuck 极致小巧网速流量监控工具

# NetDuck 极致小巧网速流量监控工具

原创

cosmic
cosmic

無相安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 我最初的要求很简单：一个类似于火绒流量监控悬浮窗一样小巧、无感的 Windows 网速监控工具

小巧一点，能贴边隐藏；用光柱显示上传和下载；展开以后，能看到每个应用到底用了多少流量。可作为火绒流量监控工具平替。

要求听起来不高，但现成工具里，有的功能很全，体积却太大；有的支持悬浮，又没有光柱和按应用累计流量。要把“小巧、贴边、光柱、应用明细”凑齐，选择并不多。

#

## 不太建议碰“绿化版”

网上有很多从火绒中独立提取出来的流量监控“绿化版”“破解版”，不太建议碰。

来源不明的安装包，可能被植入木马、窃取账号，或者捆绑推广软件。

---

## 于是，我给自己写了一个 NetDuck，求人不如求己。

![](https://mmbiz.qpic.cn/mmbiz_png/TQxicdiaQ6u3Dj19blEeB49xa5UQ25Ihos8aOE2cAknSGyO6ibMVqCiapsZHXJFfZUrrVJA9ncuU6BNwNWGZrMGhyebjCIqroHTibicic8OSsafGmQ/640?wx_fmt=png&from=appmsg)

#

## 平时只是屏幕边沿的一根线

NetDuck 贴在屏幕边缘时，只有`5px`厚。

默认主题下，上面橙色代表上传，下面绿色代表下载。鼠标移过去，窗口展开；移开后，它自己收回去。

只有拖到距离屏幕边缘`32px`以内才会吸附。放在屏幕中央也可以，它就是个普通悬浮窗，支持置顶和最小化。

多种主题，满足不同人群审美需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TQxicdiaQ6u3AhkAW3WRmzzUUiaHZ3uXcuXmFHPJ2vC4bjV51nnm5FVZSg5ZAac6Bb6FLeGbUeQlH0DmG7OVASbRW7gU7WxcsSnlwzklpicTJKs/640?wx_fmt=png&from=appmsg)

#

## 展开以后，该有的都有，运行速度极快，一触即达

* 实时上传和下载速度。
* 进程排行，以及 TCP / UDP 连接明细。
* 总上传、总下载，还有每个应用的累计流量。
* 单个应用重置、全部清零，也可以选择重启后清零。

累计数据默认保存在本机，重启不会丢。对经常需要确认“到底是哪个程序在占网速”的人来说，这几项功能十分实用。

另外，它还带了四套主题、托盘图标、全局快捷键和仅托盘模式。按`Ctrl + Alt + M`，随时展开、收起或从托盘恢复。

#

## 下载与运行

* 系统要求：Windows 10 / 11 x64。
* 首次运行需要管理员权限，ETW 才能把流量对应到具体进程。
* 如果提示缺少运行环境，安装 .NET 8 Desktop Runtime x64 即可。

> Github下载地址
>
> https://github.com/Drac4ry/NetDuck/releases

第一个版本，先到这里。

使用过程中如果发现 Bug，或者有想要的功能，欢迎去 GitHub 提 Issue。

```
作者注：NetDuck 由本人独立实现，本项目与火绒无隶属关系，也未使用火绒的源码、资源。本应用不上传流量数据，没有遥测、广告和自动更新，设置与累计流量只保存在本机。
```

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/t04xibgTJnicxlgib51nY05tn89vKXMAOK5XIicdNQk4wdJdCvfhhYbStkqq9QpnJn1R5XEGACFnfUic2P5HC8Y3Fdw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过