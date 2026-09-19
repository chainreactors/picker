---
title: windows server 2022安装winget方法
url: https://mp.weixin.qq.com/s/T8-roCeuCckzZbCf0SAgQA
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:54:17.398217
---

# windows server 2022安装winget方法

# windows server 2022安装winget方法

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# windows server 2022安装winget方法

## 缘起

公司开始逐渐要求使用云电脑办公了，云电脑主流的都是server系统，且版本不高。

只有新版本的 11+ 及 Server 2025+ 会自带winget，所以需要在老版本上安装winget。

## 方法

winget微软开源了，地址：

https://github.com/microsoft/winget-cli/

至少需要下载如下3个文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvcsHENuiaAX6egicqC3E9q26WFVxpLcbNzOkGftamB3bUHC95icUU5yiavvdxT0F7TgIUqrA5C9fvrsPNCdILIMepR2IUfjO4XHqJo/640?wx_fmt=png&from=appmsg)

## 安装

1. 先顺序安装这三个：

解压DesktopAppInstaller\_Dependencies.zip后，打开x64文件夹：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvfdL1uTcaHFeicyu8icOQKRq7G3uHmicXs17KMNiczvKicVnF8HSFhAnuC7RK7NanWbTu7mUBmTwz98xpHiaaq8u7cQN2n8vrCyyhE8Y/640?wx_fmt=png&from=appmsg)

安装脚本：

启动powershell

```
Import-Module -Name Appx -UseWindowsPowerShell

Add-AppxPackage Microsoft.VCLibs.140.00_14.0.33519.0_x64.appx
Add-AppxPackage Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64.appx
Add-AppxPackage Microsoft.WindowsAppRuntime.1.8_8000.616.304.0_x64.appx
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvdhRDD2icFnfEwX102CgEhZwQdssj44fuTwujDDd9mBicQqETUia8HJ6meLsvA5LaJocINPCnRxCoDoMAPeuNx1fZyyLZC1yOA3HE/640?wx_fmt=png&from=appmsg)

2. 安装msixbundle

```
Add-AppxProvisionedPackage -Online -PackagePath .\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle -LicensePath .\e53e159d00e04f729cc2180cffd1c02e_License1.xml
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvco5lIMCJeIJL3bCBk9ngEuHibM54uGRT9ZuqO1x7fE5xwjP9crHJcGlzymT11N2tleejWMvH12ia3iaFx4N46AlWTknxJVWUdxh4/640?wx_fmt=png&from=appmsg)

## 基本设置

winget使用github来存储的，所以必须要安装的是git

```
winget install Git.Git
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulveKOxtjLqDR3TdptBPscK60n7nw3FtypZL1eicnnaHGwkllNLHlbry28ju9tRV6fibJs8MSe9J9BUVyZgJ9wBGbLlXFHJUwj0Y5U/640?wx_fmt=png&from=appmsg)

安装windows最好用的terminal：

```
winget install Microsoft.WindowsTerminal
```

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvezego4X0jSnibpdY13oSd2OkTR4oNic6XGNZ88bLo9dSayYFgv8J2pehI9CrLcd3XwtszwDqk59nV5ydQZbhPyIOfno9NadrdBo/640?wx_fmt=png&from=appmsg)

安装微软的linux工具集

```
winget install Microsoft.Coreutils
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvdyklGHWXRv7icWClTd1KDM28icyGaagAdC1XQUKmvFFFR0bAibHCKexryHU9sVt2T138hsgsSOh4an3N6A371T6WWZZ7hv1YqzPE/640?wx_fmt=png&from=appmsg)

这个工具集专门介绍过：

[微软把Linux命令搬进Win11：Coreutils开源项目重磅发布](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651407&idx=1&sn=4b599795396e52d43cb3ecc132b979ee&scene=21#wechat_redirect)

## 镜像修改

大家网络环境都不是太好，用国内镜像比较好：

```
# 替换 USTC 镜像
winget source remove winget
winget source add winget https://mirrors.ustc.edu.cn/winget-source

# 重置为官方地址
winget source reset winget
```

## 其他安装方法

鉴于低版本系统安装的不方便，还是有大佬总结了一键脚本的：

部署 WinGet 的 PS 脚本到 PowerShell Gallery 仓库

详细减少可以看github：https://gist.github.com/erwinkersten/626ed456c1bd84fd5e023b081d6d450e

使用方法：

```
Install-Script -Name winget-install
winget-install -Force
```

这个脚本只是将手工安装自动化了，还是需要网络环境的，我试了失败，才手工安装的，网络好的可以试试

## 小结

其实windows对应程序员来说，也没必mac差的那么不堪，自己折腾折腾还是可以的。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

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