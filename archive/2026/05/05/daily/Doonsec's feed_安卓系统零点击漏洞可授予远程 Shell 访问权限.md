---
title: 安卓系统零点击漏洞可授予远程 Shell 访问权限
url: https://mp.weixin.qq.com/s/T4iES_vBJkMRrL9BvqIh2Q
source: Doonsec's feed
date: 2026-05-05
fetch_date: 2026-05-06T05:07:42.576432
---

# 安卓系统零点击漏洞可授予远程 Shell 访问权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NhgQBRxHKMiau1vPDkocPcAyb9z6gOXJe1m7oMJibss8YZZYTdqsY7S9czdMCAjN650fb3ohJ9kIXsGhxM6ZP6BUgakheQfRia5o/0?wx_fmt=jpeg)

# 安卓系统零点击漏洞可授予远程 Shell 访问权限

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

谷歌发布了 2026 年 5 月 Android 安全公告，提醒业界注意一个极其严重的远程代码执行 (RCE)漏洞。

该严重漏洞编号为 CVE-2026-0073，存在于 Android 系统核心组件的深处。

它允许攻击者获得远程 shell 访问权限，而无需设备所有者进行任何点击、下载或操作。

威胁行为者可以发起这种零点击攻击，这意味着他们只需要在同一本地网络上或在物理上靠近目标，即可利用存在漏洞的移动设备。

## **Android零点击漏洞**

CVE-2026-0073 的根源在于 adbd 子组件，即Android Debug Bridge 守护程序。

开发人员通常利用此系统服务与设备通信、运行终端命令和修改系统行为。

由于该漏洞允许攻击者以“shell”用户身份执行远程代码，因此攻击者可以绕过正常的应用程序沙箱。

它们不需要任何特殊的执行权限或用户交互即可成功部署恶意载荷。

把addbd服务想象成安全企业大楼上的一个限制维修的门。

这种漏洞就像一把通过无线连接工作的万能钥匙，允许入侵者悄无声息地解锁大门，并向建筑物的内部系统发出指令，而保安人员却浑然不觉。

这种毫无阻碍的访问方式使得该漏洞极其危险，并且对高级威胁行为者极具吸引力。

由于 adbd 服务是 Project Mainline 组件，并通过 Google Play 系统更新进行分发，因此该缺陷会影响最近几代操作系统。

Android 14、Android 15、Android 16 和 Android 16-QPR2 设备目前存在风险。

谷歌已在 2026 年 5 月 1 日的安全补丁级别中解决了这一关键问题，详情请参阅 2026 年 5 月 Android 安全公告。

所有安卓硬件合作伙伴至少提前一个月获悉了此漏洞，以便他们准备通过无线方式进行固件更新。

相应的源代码补丁也已推送至Android 开源项目 (AOSP)代码库，以确保更广泛的生态系统的持续平台稳定性。

设备所有者必须优先立即安装最新的安全更新，以防止潜在的安全漏洞被利用。

要确认设备是否受到保护，请进入系统设置，并确认安全补丁级别为 2026 年 5 月 1 日或更高版本。

用户还应手动检查是否有待处理的 Google Play 系统更新，因为某些运行 Android 10 或更高版本的设备可能会通过此替代渠道收到有针对性的组件补丁。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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