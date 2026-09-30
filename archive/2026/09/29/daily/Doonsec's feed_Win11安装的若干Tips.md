---
title: Win11安装的若干Tips
url: https://mp.weixin.qq.com/s/ZU-13LsrT1Yhyt7bKUsTMg
source: Doonsec's feed
date: 2026-09-29
fetch_date: 2026-09-30T07:41:02.466713
---

# Win11安装的若干Tips

# Win11安装的若干Tips

原创

沈沉舟
沈沉舟

青衣十三楼飞花堂

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

```
创建: 2026-09-22 08:53
更新: 2026-09-25 11:40
链接: https://scz.617.cn/windows/202609220853.txt
```

装英文企业版Win11 IoT LTSC 2024 x64，这种版本受支持的周期更长，适合高级用户。用(虚拟)光盘启动，能选中文的时候选中文，不能选的时候保持英文，装完后有机会更改。中途提示输入Key，选"没有Key"，弹出另一个界面，选"Windows 11 IoT Enterprise LTSC"。碰上隐私提示，全关。

若网卡驱动缺失，得先解决之。假设网卡驱动已就位，ncpa.cpl配置网络。

通网后，第一件事是激活，不要着急配置系统，否则容易白配，重启后可能回滚，没有持久化。我不怎么研究激活，这都是小钻风的领域。他推荐这个

Microsoft Activation Scripts (MAS)

```
https://massgrave.dev/
```

最简用法是，在PowerShell里执行(无需管理员权限)

```
irm https://get.activated.win | iex
```

其激活原理是，模拟从已激活低版本Windows升级到Win11，永久激活。注意，MAS被多家杀毒厂商标注为恶意软件，但它的github星有192K。用不用，自己定，我不做其他评论。

一旦冒险激活，就是永久，相比之下，KMS需要180天刷新一次。有意思的是，对于适用版本的Win10、11，之前用KMS激活的，仍可用MAS再次激活，彻底丢弃KMS。

激活后，再去设置里下载中文语言包，切换界面、安装中文输入法。然后就是一些小配置，比如我的常用配置路径

```
timedate.cpl

    修改时间、设置NTP服务器

intl.cpl

    调整日期、时间的格式

rundll32.exe shell32.dll,Control_RunDLL desk.cpl,ScreenSaver,@ScreenSaver

    屏保

desk.cpl,any

    桌面图标设置

sysdm.cpl

    开启远程桌面，关闭远程协助

OptionalFeatures.exe

    启用或关闭Windows功能，比如安装WSL

控制面板\所有控制面板项\自动播放(关闭)
```

---

```
设置
  个性化
    任务栏
      任务栏对齐方式
        靠左
  Windows更新
    高级选项
      需要重新启动才能完成更新时通知我
        On
      传递优化
        允许从其他电脑下载
          Off
  隐私和安全性
    Windows安全中心
      病毒和威胁防护
        云提供的保护
          Off
        自动提交样本
          Off
    诊断和反馈
      (能关就关)
```

下面是小钻风提供的Office 2024安装方案

在官网下载Office Deployment Tool

```
https://www.microsoft.com/en-us/download/details.aspx?id=49117
```

假设下回来是officedeploymenttool\_20326-20112.exe，提取里面的setup.exe

```
X:\Office2024\setup.exe
```

编辑

```
X:\Office2024\Office2024.xml
```

---

```
<Configuration>
  <Add OfficeClientEdition="64" Channel="PerpetualVL2024">
    <Product ID="ProPlus2024Volume" PIDKEY="XJ2XN-FW8RK-P4HMP-DKDBV-GCVGB">
      <Language ID="zh-cn" />
      <ExcludeApp ID="Access" />
      <ExcludeApp ID="Bing" />
      <!--ExcludeApp ID="Excel" /-->
      <ExcludeApp ID="Groove" />
      <ExcludeApp ID="Lync" />
      <ExcludeApp ID="OneDrive" />
      <ExcludeApp ID="OneNote" />
      <ExcludeApp ID="Outlook" />
      <!--ExcludeApp ID="PowerPoint" /-->
      <ExcludeApp ID="Publisher" />
      <ExcludeApp ID="Teams" />
      <!--ExcludeApp ID="Word" /-->
    </Product>
    <!--
    <Product ID="ProjectPro2024Volume" PIDKEY="FQQ23-N4YCY-73HQ3-FM9WC-76HF4">
      <Language ID="zh-cn" />
    </Product>
    <Product ID="VisioPro2024Volume" PIDKEY="B7TN8-FJ8V3-7QYCP-HQPMV-YY89G">
      <Language ID="zh-cn" />
    </Product>
    -->
  </Add>
  <Display Level="Full" AcceptEULA="TRUE" />
  <Property Name="AUTOACTIVATE" Value="0" />
  <Property Name="DeviceBasedLicensing" Value="0" />
  <Property Name="FORCEAPPSHUTDOWN" Value="FALSE"/>
  <Property Name="PinIconsToTaskbar" Value="FALSE"/>
  <Property Name="SCLCacheOverride" Value="0" />
  <Property Name="SharedComputerLicensing" Value="0" />
  <RemoveMSI />
  <Updates Enabled="TRUE" />
</Configuration>
```

具体配置可自行修改。下载离线安装包

```
cd /d X:\Office2024
setup.exe /download Office2024.xml
```

下载过程无任何图形界面，等待setup.exe结束即可，约3.5G。生成目录

```
X:\Office2024\Office\
```

离线安装

```
setup.exe /configure Office2024.xml
```

若提示

We couldn't find the specified configuration file.
Check the file path and file name.
Go online for additional help.
Error Code 0-2048 (0)

则在管理员级cmd中执行上述命令。离线安装若提示"下载"，那是误提示，实际应提示"安装"，要耗一小会儿。结束后可appwiz.cpl确认安装，并实际打开Excel试试。

最好用KMS激活Office 2024，此处略。不过，MAS也提供激活方案，未测试。

关于ODT安装，还可参看

《Microsoft Office Professional Plus 2016离线安装指南》

```
https://scz.617.cn/windows/202203031006.txt
```

调整Office隐私相关设置

```
文件
  帐户
    管理设置
      可选的连接体验
        Off
  更多
    选项
      常规
        用户名
          李四 (可改成空格，但不要完全删除，否则会自动恢复)
        缩写
          李 (可改成空格，但不要完全删除，否则会自动恢复)
```

还可参看

《删除Office文档个人隐私信息》

```
https://scz.617.cn/windows/202505301701.txt
```

IoT LTSC版没有Microsoft Store，但可以安装官方的"App Installer"。有多种办法补装，我用的方案如下

```
https://apps.microsoft.com/detail/9nblggh4nns1
https://store.rg-adguard.net/
```

从微软官网获取App Installer相关包

```
Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
Microsoft.UI.Xaml.2.8_8.2501.31001.0_x64__8wekyb3d8bbwe.Appx
Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64__8wekyb3d8bbwe.Appx
Microsoft.VCLibs.140.00_14.0.33519.0_x64__8wekyb3d8bbwe.Appx
Microsoft.WindowsAppRuntime.1.8_8000.946.1701.0_x64__8wekyb3d8bbwe.Msix
```

在PowerShell中执行

```
Get-AppxPackage -Name Microsoft.UI.Xaml.2.8 | Select Name, Architecture, Version, PackageFullName, Status
Get-AppxPackage -Name Microsoft.VCLibs.140.00 | Select Name, Architecture, Version, PackageFullName, Status
Get-AppxPackage -Name Microsoft.VCLibs.140.00.UWPDesktop | Select Name, Architecture, Version, PackageFullName, Status
Get-AppxPackage -Name Microsoft.WindowsAppRuntime.1.8 | Select Name, Architecture, Version, PackageFullName, Status
Get-AppxPackage -Name Microsoft.DesktopAppInstaller | Select Name, Architecture, Version, PackageFullName, Status
```

假设缺下面三个包，补装之

```
Add-AppxPackage -Path Microsoft.WindowsAppRuntime.1.8_8000.946.1701.0_x64__8wekyb3d8bbwe.Msix
Add-AppxPackage -Path Microsoft.VCLibs.140.00.UWPDesktop_14.0.33728.0_x64__8wekyb3d8bbwe.Appx
Add-AppxPackage -Path Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
```

确认winget就位

```
where.exe winget
winget --version
```

拥有winget后，相当于拥有命令行版Microsoft Store，至少可以安装那些无需登录即可下载的商店应用。比如，安装"Windows Terminal"

```
winget source list
winget source update
winget search --source msstore "Windows Terminal"
winget show --id 9N0DX20HK701 --source msstore
winget install 9N0DX20HK701
winget uninstall 9N0DX20HK701
winget upgrade --id 9N0DX20HK701 --source msstore
```

这很像Linux的apt安装。Win-R，shell:AppsFolder，右键选中"终端"，创建快捷方式。

可以从Store装PowerToys

```
winget search --source msstore "Microsoft PowerToys"
winget show --id XP89DCGQ3K6VLD --source msstore
winget install XP89DCGQ3K6VLD
winget uninstall XP89DCGQ3K6VLD
winget upgrade --id XP89DCGQ3K6VLD --source msstore
```

安装到"%LOCALAPPDATA%\PowerToys"。若想安装到"%ProgramFiles%\PowerToys"，从github下载相应版本

```
https://github.com/microsoft/PowerToys/
```

其他软件安装，就不啰嗦了，视个人需要而不同。

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPOa7YUszQ2zP2AFStE4UScicKMwhEqpde0j0FEheXVmbxSG8JFKDG3K8piaJjMHLjicL5zKemTibjvuQg/0?wx_fmt=png)

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