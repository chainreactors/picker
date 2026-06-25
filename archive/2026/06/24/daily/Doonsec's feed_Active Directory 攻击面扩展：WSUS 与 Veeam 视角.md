---
title: Active Directory 攻击面扩展：WSUS 与 Veeam 视角
url: https://mp.weixin.qq.com/s/pruiziqUVNHz7_Qfopoq0w
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:02:39.894894
---

# Active Directory 攻击面扩展：WSUS 与 Veeam 视角

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icm4tzB0NhkjWwJD9IT43DNKK6arZ4IBUQlibnI7qTSQxslibsTOqMHLKFlBiatkSzECgaFhsP38LZtcGQcmsLCNl0wWTHa3u2Th1JnqzJHNnn8/0?wx_fmt=jpeg)

# Active Directory 攻击面扩展：WSUS 与 Veeam 视角

原创

词不达意
词不达意

词不达意安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### Active Directory

Active Directory (AD) 仍然是大多数企业网络的核心身份和访问管理系统 。由于其在身份验证和授权方面发挥着核心作用，因此也是攻击者最青睐的目标之一。

### 攻击面

常规测试AD，常用一些nday如`Zerologon`，`ADCS服务`以及`ACL滥用`等，下面我将补充一些近期学习到的攻击面。

#### 更新服务（WSUS）

微软 Windows 服务器更新服务（WSUS）一个用于补丁管理的核心企业组件，发现了一个严重的未经身份验证的远程代码执行`CVE-2025-59287`漏洞。WSUS通常在域内，可通过如下命令查询：

```
reg query "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WindowsUpdate" /v WUServer
```

通过`CVE-2025-59287`打入内存马可获取WSUS机器SYSTEM权限，利用该机器继续横向攻击。

#### 备份服务器（Veeam）

通常Veeam 备份服务器加入Windows域可以方便集中身份验证，`CVE-2025-23120`是Veeam中的一个严重远程代码执行 (RCE) 漏洞。它允许任何经过身份验证的域用户利用Veeam接口中不安全的反序列化缺陷，在备份服务器上执行任意代码。

由于Veeam负责备份和管理 VMware环境，拿下Veeam后以此入侵 vCenter  ESXi等虚拟化环境。

### 纷传介绍

![](https://mmbiz.qpic.cn/mmbiz_jpg/icm4tzB0NhkiaY8D2N4RG4ZNiaAMImhh7wLEE2pN6b3aUXibQic7et9Vc7PwUDN52FiclkRBpoRa4C72R31yu7BD6gsXDyrxByBlrpR6Z9VHyZpbE/640?wx_fmt=jpeg&from=appmsg)

### 圈子往期文件内容如下

* •冲锋马一键生成工具（一键生成免杀loader）
* •lnk文件一键生成工具（一键生成免杀钓鱼lnk文件）
* •bypass内存扫描插件（可绕过火绒、卡巴斯基等杀软内存扫描cs插件）
* •暗涌在线免杀平台（白文件patch免杀loader（分离、单文件）一键生成平台、支持反沙箱）
* •bypass任务计划工具（普通权限可添加、钓鱼快速免杀维权）
* •后渗透工具免杀（petobin，分离加载避免静态落地被秒）
* •BYOVD攻击一键结束赛门铁克进程
* •BinPatch免杀工具过国内主流杀软
* •白影(whiteShadow)自动化白加黑免杀工具v1.0
* •白影(whiteShadow)自动化白加黑免杀工具v2.1
* •Windows恶意软件常见API一览（PDF）
* •Maldev Academy 恶意软件开发完整课程（源码+VM镜像）
* •SplitRun一款exe免杀工具v1.0
* •cs4.5二开过火绒内存扫描
* •binfileBinder文件捆绑工具
* •RPC添加计划任务绕过360核晶
* •DarkTide内部版单文件免杀
* •VoidShell：x86-64 Linux ELF 加壳混淆工具

### 重要声明

本文所涉及的技术、思路和工具仅用于本地靶场安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担，禁止用于任何非法渗透测试，以及无授权违法测试，请遵守中华人民共和国网络安全法。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fQ2Bdxy1C5nUgyJyyHvl33mCCUsSib26NxViaiamWM5qOT7NAVcjlGAkGlkBYQF4j3dSHMprGM9aRTxjQ7ThqugRQ/0?wx_fmt=png)

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