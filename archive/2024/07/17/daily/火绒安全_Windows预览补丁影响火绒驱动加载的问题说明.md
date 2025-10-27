---
title: Windows预览补丁影响火绒驱动加载的问题说明
url: https://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247519455&idx=1&sn=c319fe6428e6536974f5115f1b9fa3ff&chksm=eb7052e0dc07dbf6bdddc7dea0cb556518bfffd564e53894a998142b2d1e26e9dddfb7c73b8d&scene=58&subscene=0#rd
source: 火绒安全
date: 2024-07-17
fetch_date: 2025-10-06T17:42:29.985077
---

# Windows预览补丁影响火绒驱动加载的问题说明

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz5eOQeQZXyhOqBvuYX8U4ZCaqibaXYPDGcEpNYwGBFmeqtOx4cXQJCibLF9gibWUJQ0PN69APqmJvrHg/0?wx_fmt=jpeg)

# Windows预览补丁影响火绒驱动加载的问题说明

原创

火绒安全

火绒安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4nrnOI1emtFr0UYnrLKytAvy2gia6ZuIUJs14h2pEIwpiaWPCTTuCQIDibx9dlfXoyrNyVEWb8DVUUA/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

尊敬的火绒用户：

大家好，近期我们收到多位用户反馈火绒安全软件服务异常的问题，经火绒工程师排查确认，微软于 7 月 11 日更新的Windows 11 预览版本补丁 **KB5040527**安装后，会影响火绒驱动加载，导致火绒安全软件服务异常，受影响的产品包括火绒安全软件5.0、6.0、火绒安全企业版1.0终端、2.0终端，补丁相关信息如下：

https://blogs.windows.com/windows-insider/2024/07/11/releasing-windows-11-builds-22621-3951-and-22631-3951-to-the-release-preview-channel/

该补丁更新了系统文件DriverSiPolicy.p7b，文件路径为C:\Windows\System32\CodeIntegrity\driversipolicy.p7b，相关更新信息如下：

[Windows Kernel Vulnerable Driver Blocklist file (**DriverSiPolicy.p7b**)] This update adds to the list of drivers that are at risk for Bring Your Own Vulnerable Driver (BYOVD) attacks.

DriverSiPolicy.p7b 是一个规则文件。Windows Defender 的“Microsoft 易受攻击的驱动程序阻止列表”功能会使用这个规则文件，阻止满足规则的驱动程序启动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5eOQeQZXyhOqBvuYX8U4ZCoqM6UqVKDCZylwgakdm00GQYpeBicicXIcZeAaibpNDdJbeThXyiacVHsQ/640?wx_fmt=png&from=appmsg)

该功能说明见微软官网链接https://learn.microsoft.com/zh-cn/windows/security/application-security/application-control/windows-defender-application-control/design/microsoft-recommended-driver-block-rules。DriverSiPolicy.p7b 是一个二进制文件，可以通过工具转为原始XML规则进行查看。KB5040527补丁更新的driversipolicy.p7b文件转为XML之后，信息如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5eOQeQZXyhOqBvuYX8U4ZCpClV4ARxzOxOicVpCz8mrB9GcnfRoCicicFvpZ2HDpw3xsibp2Fu5FbmHw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5eOQeQZXyhOqBvuYX8U4ZCWUz2zNhmKicFkHD0x6QKx8nvpaSVdKUYDhLYD25QgqKKFNG5feNlrsQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5eOQeQZXyhOqBvuYX8U4ZCiaBJibUQ73b4ia4qs7T0ggic8iaoweicib4RkR8AsgeWolB5aazjn7eDMu77Q/640?wx_fmt=png&from=appmsg)

根据实际测试结果，微软技术支持页面的相关描述，和对该XML字段的解读。可以确认火绒的驱动相关程序sysdiag和hrfwdrw.sys全版本被加入到阻止列表，并且火绒数字签名也被加入到阻止列表。

火绒工程师通过更新补丁复现该问题，得到两个版本的driversipolicy.p7b文件。其中一个文件拉黑了sysdiag.sys、hrfwdrv.sys的版本和火绒的数字签名信息，另一个文件仅拉黑了火绒的数字签名信息。而结果都是更新KB5040527补丁后火绒驱动无法启动。目前我们正在积极与微软沟通，若您在使用过程中出现此问题，请参考以下方案解决。

**临时解决方案**

1.进入Windows安全中心，找到设备安全性，点击内核隔离功能下的内核隔离详细信息链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5eOQeQZXyhOqBvuYX8U4ZCZErmZrTjCicwEataYkjz61F6QbITJG1PK1YNdqfeWgz63BHuf6Lujog/640?wx_fmt=png&from=appmsg)

2.关闭“Microsoft 易受攻击的驱动程序阻止列表”功能后重启系统即可解决。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5eOQeQZXyhOqBvuYX8U4ZCknLLdDdSh36Ae71gyPyQ3zwomaLG2uWN0CeosrYJ2Tug8VickL7aKvA/640?wx_fmt=png&from=appmsg)

若以上方式不适用于您的设备，需要按照以下步骤卸载相关补丁：

1.Win+R打开运行窗口，输入control后点击确定打开控制面板。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5eOQeQZXyhOqBvuYX8U4ZCqR26R23VGyPQWMTWkHZnP77ru0aUQ8I8WkLq6Z91ksjTzfREV3GL6g/640?wx_fmt=png&from=appmsg)

2.选择程序（又称程序和功能）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5eOQeQZXyhOqBvuYX8U4ZCuwesWNFY5outX97kKVTEjJkefznA0BPKtcTNaZ5vwJT5gDZQtGeGyA/640?wx_fmt=png&from=appmsg)

3.选择查看已安装的更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5eOQeQZXyhOqBvuYX8U4ZCWWJSUbacTo8R58sEsiaaBxH5LDO6Zicric9ib9jEHL9al7CzZYpYiafib0lg/640?wx_fmt=png&from=appmsg)

4.卸载KB5040527补丁后重启系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5eOQeQZXyhOqBvuYX8U4ZCxfpvo4dXqnYypgDnAM3g3vbAxnbg4fgd3Zw5Zbaibh799yDS9n8Al1Q/640?wx_fmt=png&from=appmsg)

若以上方法均无法解决您的问题，请及时与我们联系，感谢您对火绒的支持！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

火绒安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

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