---
title: MobileSentinel 1.0（移动哨兵）
url: https://blog.upx8.com/3335
source: 黑海洋 - WIKI
date: 2023-03-25
fetch_date: 2025-10-04T10:37:31.394122
---

# MobileSentinel 1.0（移动哨兵）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# MobileSentinel 1.0（移动哨兵）

发布时间:
2023-03-24

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
9927

![](https://img.776161.xyz/img/20230324/3485770899.png)

# Mobile Sentinel

demo：[https://youtu.be/FiiELuFvwu0](https://blog.upx8.com/go/aHR0cHM6Ly95b3V0dS5iZS9GaWlFTHVGdnd1MA)

Mobile Sentinel 是一款Android应用程序，可以让您检测部分的LTE和（未来）5G网络中的漏洞。在当前版本中，Mobile Sentinel 专注于检测ReVoLTE漏洞( [www.revolte](https://blog.upx8.com/go/aHR0cDovL3d3dy5yZXZvbHRlLWF0dGFjay5uZXQv) )-attack Mobile Sentinel 。需要基于 Qualcomm 的具有访问权限的 Android 手机，因为它建立在 Qualcomm 的 mdlog 工具之上。

该应用程序包：

* 自动测试测试运行以测试 ReVoLTE 漏洞
* 用于捕捉蜂巢流量（目前仅限RRC）和查看应用内部协议消息的日志记录视频
* 将捕获的流量写入PCAP文件
* 日志上传到http服务器功能（开发中）

## 安装

[从这里](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1JVQi1TeXNTZWMvbW9iaWxlX3NlbnRpbmVsL3JlbGVhc2VzL2Rvd25sb2FkLzEuMC9Nb2JpbGVTZW50aW5lbC5hcGs)下载最新的APK版本并直接安装在设备上。

```
adb install MobileSentinel.apk
```

或者，可以直接从设备的文件系统安装应用程序。

## 设置

* 配置日志上传设置：此设置允许您更改将日志文件上传到服务器的行为。选项：
  + 求上传：每次测试运行后都会询问您是否要上传数据（默认）。
  + 从不上传：从不上传日志。
  + 始终上传：将始终上传日志。

* 更改呼叫号码：此设置允许您更改为测试呼叫的电话号码。*重要提示：可能存在付费风险。*默认号码是德国电话号码。

## 结构说明

您也可以从源代码构建应用程序，但是，您需要[Chaquopy SDK](https://blog.upx8.com/go/aHR0cHM6Ly9jaGFxdW8uY29tL2NoYXF1b3B5L2xpY2Vuc2Uv)许可以证明才能在Android Studio之外部配置应用程序。

## 要求

* 带高通基带的Android手机
* 手机和使用的 SIM 卡必须支持 VoLTE
* 之前需要最低Android Pie (9.0)

*确保向应用程序授予超级用户权限并接受请求的权限，因为没有该应用程序将无法运行。*

## 测试设备

* 小米 Mi A3 (Android 9.0)
* 一加6T（安卓9.0）
* 小米MIX 3 5G（安卓9.0）

## 使用的库

Mobile Sentinel 使用以下库：

* [Chaquopy SDK](https://blog.upx8.com/go/aHR0cHM6Ly9jaGFxdW8uY29tL2NoYXF1b3B5L2xpY2Vuc2Uv)
* [SCAT](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2Znc2VjdC9zY2F0)
* [Pycrate](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1Axc2VjL3B5Y3JhdGU)

## 已知道错误

* 某些带有高速基站的手机不允许从 DIAG 界面提取蜂巢网络流量

[取消回复](https://blog.upx8.com/3335#respond-post-3335)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")