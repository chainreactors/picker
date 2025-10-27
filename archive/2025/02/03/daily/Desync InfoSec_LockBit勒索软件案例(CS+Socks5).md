---
title: LockBit勒索软件案例(CS+Socks5)
url: https://mp.weixin.qq.com/s?__biz=MzkzMDE3ODc1Mw==&mid=2247489011&idx=1&sn=cdefefd425a7437c3ef0df558eb05375&chksm=c27f665df508ef4b1dd69002004b822d8088e12e7ddb41fb844da301a2dc60d7acacb9ed6733&scene=58&subscene=0#rd
source: Desync InfoSec
date: 2025-02-03
fetch_date: 2025-10-06T20:39:24.674608
---

# LockBit勒索软件案例(CS+Socks5)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoE73IK0fHHSC6zklSHeeL6gdY4icICg4nu1LztwicUGaFzicVG8PEuzBnYA/0?wx_fmt=jpeg)

# LockBit勒索软件案例(CS+Socks5)

safest\_place

Desync InfoSec

![](https://mmbiz.qpic.cn/mmbiz_gif/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoE0eauGpZ0FN05LOOs8NBUOBIadcuoH4YOibLn1DQjnKxObY2hUuuY1Rg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoEUJ0SqoTX9jMyhQ0RcYjqIrcz1AT413cT5lByPelfvQWVIKz8vYP5pQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoE0eauGpZ0FN05LOOs8NBUOBIadcuoH4YOibLn1DQjnKxObY2hUuuY1Rg/640?wx_fmt=gif&from=appmsg)

**蛇来运转，鸿运新年**

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoElwrXjfsf5SJYxpjndgiaGVk7iaLDwtaIRPjLvMxOb5cIH0sm6bcdfxtQ/640?wx_fmt=png&from=appmsg)

HAPPY SPRING FESTIVAL

读者朋友们新年快乐！

2025年一起继续学习新的知识

为网络安全添砖加瓦

来个红包，![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)解密之后支付宝口令红包领取：

```
H4sIAKA1n2cA/wWAIREAAAgDkyEQzPMRmKF/gp0wQ59+K5cSnxMMAAAA
```

# 关键要点

* • 此入侵始于下载和执行伪装成 Windows Media Configuration Utility 的 Cobalt Strike 载荷。
* • 攻击者使用 Rclone 从环境中窃取数据。起初，他们尝试用 FTP 传输外带数据，但失败了，然后才开始使用 MEGA.io。一天后，他们再次尝试使用FTP外带数据，这次他们成功了。
* • 攻击者使用计划任务、GhostSOCKS 和 SystemBC 代理以及 Cobalt Strike C2会话访问权限，在环境中创建了多个权限维持后门。
* • 攻击者在入侵开始的第 11 天，从整个被入侵的网络中部署了LockBit 勒索软件。

# 案例总结

此次入侵始于 2024 年 1 月底，当时用户下载并执行了一个伪装成合法的 Microsoft Windows Media Configuration Utility文件setup\_wm.exe，这个文件是一个Cobalt Strike 载荷，并且文件图标与合法程序一致。一旦执行便会与C2服务器建立通信。

在边界突破后大约 30 分钟，Cobalt Strike载荷开始执行一些信息收集操作，执行nltest寻找域控服务器。由于用户直接使用高权限运行了CS载荷，攻击者可以直接利用 SMB 和远程服务将两个代理工具（SystemBC 和 GhostSOCKS）部署到域控制器上。

在域控服务器上Windows Defender检测到了这些工具，起初我们以为这两个工具都被成功拦截了，然而实际上，GhostSOCKS没有运行起来，但 SystemBC 代理仍然处于活动状态，这样攻击者就从域控服务器与C2建立了远程控制会话。攻击者开始在最初失陷的机器上执行其他操作，通过进程注入到WUAUCLT.exe 进程，并尝试从LSASS进程转储登录凭证。

攻击者将 Seatbelt 和 SharpView CLR 模块加载到注入的进程中，并创建计划任务执行 SystemBC 和 GhostSOCKS 代理以进行权限维持。

入侵开始约一个小时后，攻击者使用相同的账户利用远程服务横向移动到文件服务器，在横向移动中部署了一个 Cobalt Strike PowerShell 会话，这个会话连接到另一个C2服务器。

在文件服务器上，攻击者还是相同的套路，部署使用 SystemBC 和 GhostSOCKS 代理，并创建计划任务进行权限维持。不久之后，攻击者通过已建立的代理隧道之一启动了与文件服务器的 RDP 会话。

攻击者在访问主机上的本地组策略编辑器之前，使用任务管理器查看了正在运行的进程。有证据表明他们专门检查了 Windows Defender 配置。在此活动仅几分钟后，就观察到对 Windows Defender 设置的注册表修改，这使我们得出结论，攻击者在本地组策略编辑器中进行了更改。

攻击者浏览了文件服务器上的文件共享，并发现了一个包含存储凭据的敏感文档。接下来，他们尝试将 Cobalt Strike PowerShell 载荷部署到备份服务器。这个操作被成功阻断，但他们从最初的失陷主机发出远程 WMI 命令，禁用了目标服务器上的 Windows Defender 实时监控。不久之后，他们成功通过远程服务将 Cobalt Strike 载荷部署到了备份服务器上，并建立了C2会话。

攻击者通过启动远程 PowerShell 会话来执行 Active Directory 信息收集命令。他们还尝试访问域控制器上的 NTDS.dit 文件。但是，Windows Defender 似乎阻止了这一尝试。同时，在文件服务器上，攻击者执行了一个名为 check.exe 的二进制文件，该二进制文件执行了各种发现活动。此工具探测远程主机，收集其可用性、磁盘使用情况和已安装程序等信息。

攻击者通过 RDP 访问备份服务器，在那里他们查看备份配置并部署 GhostSOCKS 代理，创建计划任务进行权限维持。在此之后，他们的活动暂停了大约两个小时，然后才恢复。

在入侵开始大约四个小时后，攻击者开始尝试外带数据。他们使用文件服务器上的 Internet Explorer 访问多个临时文件共享站点。尽管这些站点通常用于暂存有效负载，但未检测到任何下载。这表明攻击者可能开始上传数据，而不是下载渗透工具。

在尝试外带数据大约 20 分钟后，攻击者开始使用 Rclone 进行数据外带。他们最初尝试通过 FTP传输数据失败了，因为所有连接到他们配置的 FTP 服务器的连接尝试都失败了。这种明显的挫败感导致他们的活动暂停了几个小时。返回后，他们在文件服务器上部署了一个新的 GhostSOCKS 二进制文件，这次通过注册表run key进行权限维持，而不是计划任务。

攻击者再次尝试使用 Rclone 外带数据，这次将 Mega.io 作为远程服务器。成功建立了连接，随后发生了大规模数据泄露，持续了大约 40 分钟。

经过 15 小时的平静后，攻击者开始查看域控制器上 DNS 管理器中的 DNS 配置。然后，他们返回文件服务器，并重新尝试使用 Rclone 和新配置的 FTP 服务器进行数据外带。这一次连接成功，他们开始向新的FTP服务器传输数据并持续了16个小时。同时，在传输数据的同时，他们访问了备份服务器并执行了 PowerShell 脚本，以从备份软件的数据库中提取存储的凭据。

攻击者停止了渗透活动，直到第11天，他们将重点转移到最终目标 — 勒索软件部署上。他们以备份服务器为文件存储点，上传了多个批处理脚本，这些脚本的功能就是自动化部署勒索软件。利用 PsExec 和 BITSAdmin 等工具，他们将勒索软件二进制文件分发到远程主机中，并通过 WMI 和 PsExec 远程执行。为了避免进程被拦截，他们部署了额外的脚本来禁用 Windows Defender 并修改整个网络的 RDP 设置。

攻击者系统地执行了这些脚本，部署了勒索软件二进制ds.exe，该二进制文件被确定为 LockBit 勒索软件。他们成功地将勒索软件传播到环境中的所有 Windows 主机，实现了不到 239 小时的勒索软件攻击时间 （TTR），从边界突破到完成勒索软件部署跨越了 11 个自然日。

# Analysts分析师

由r3nzsec、MyDFIR和MittenSec完成的分析和报告

# 入侵路径分析

## 边界突破

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoE7WwTsggChD7eQDfxicoOJ5uJEXaLz084Ua8btuKdMzIT68G3wGEzbeQ/640?wx_fmt=png&from=appmsg "null")

入侵始于 2024 年 1 月，受害者执行了一个名为 setup\_wm.exe 的文件，该文件是从 URL hxxps://accessservicesonline.com/setup\_wm.exe下载的。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoE3STf8FQic1Luzibd0AAB3ZNtpiaOjoo44Lqvn6KaAqEAyweWVLa2dgJIg/640?wx_fmt=png&from=appmsg "null")

文件setup\_wm.exe是一个加载程序，旨在部署 Cobalt Strike 载荷。域 accessservicesonline[.]com 已被多家安全厂商标记为恶意，并与 Cobalt Strike 相关的活动相关联。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoEogSJJ4UaMDa0hFCiaXfFVeibfQMM8FYaRCcGbHMdGRrLqRkLLOaE6s6Q/640?wx_fmt=png&from=appmsg "null")

## 载荷执行

攻击者使用各种手段执行恶意文件。虽然他们在多台主机上创建了计划任务以维持权限，但他们也手动运行了其中的许多任务来执行各种恶意代理工具，如 SystemBC 和 GhostSOCKS。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoEZ0rJkyQA5J8cMzmedgeGbrBfAp0rOB2P4r63qHd9B097ibagbZdfpkQ/640?wx_fmt=png&from=appmsg "null")

服务执行也被广泛使用，并在横向移动部分进行了深入讨论。其他观察到的执行模式依赖于 WMI、批处理脚本和 Psexec，这些模式在特定于其使用的其他部分中进行了介绍。

## 权限维持

### 计划任务

我们在环境中的多个系统中发现了多个计划任务。这些任务不仅限于最初的失陷主机，而且在整个受感染的网络中都有。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoELDL86icGibf7UiaRxr1afWI2M3hicFjxSKSVzJlztHf2IXMHPRj4ic5UaBw/640?wx_fmt=png&from=appmsg "null")

计划任务配置 XML 示例：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoEbEa4qyndGibYQTjzAaoiboqq9LZqX7yjopekWKFdX8ibZzM9N9L9CiaiaCw/640?wx_fmt=png&from=appmsg "null")

### 注册表run key

作为第二种权限维持方法，攻击者利用 Windows 注册表中的“Run”键在用户登录时自动执行 GhostSOCKS 有效负载。这是通过以下 PowerShell 命令完成的：

```
powershell -WindowStyle hidden -Command "if (-Not (Test-Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\App')) { Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run' -Name 'App' -Value '%PUBLIC%\\Music\\svchosts.exe' }"
```

## 权限提升

攻击者利用进程注入技术（例如注入合法进程 WUAUCLT.exe）来访问关键系统资源，包括 LSASS 内存空间。

此外，攻击者在 SYSTEM 权限下创建并执行计划任务。例如，他们通过计划任务部署了 DLL 文件（svcmc.dll 和 svcmcc.dll），确保在系统启动时执行这些文件。这些任务是使用以下命令创建和运行的：

```
schtasks /create /ru SYSTEM /sc ONSTART /tn Update2 /tr "cmd /c rundll32 %PUBLIC%\music\svcmc.dll, MainFunc" schtasks /run /TN Update2
```

此外，攻击者在横向移动期间，利用管理权限在文件服务器上执行基于 PowerShell 的 Cobalt Strike载荷。攻击者还利用 SMB 传输 SystemBC DLL 和 Golang 后门等工具，这些工具都是通过 SYSTEM 权限执行的。

## 防御规避

为了欺骗用户，加载程序使用相同的文件名和可执行图标模仿合法的 Microsoft Windows Media Configuration Utility。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoEt2RFXHtcfibCwduxpGkupPgL7PGUxpy4revD0zuicRPiasqkibdlgiawvKw/640?wx_fmt=png&from=appmsg "null")

作为其防御规避策略的一部分，攻击者采用了多种方法来禁用 Windows Defender。在文件服务器上，攻击者编辑了与 Windows Defender 相关的组策略设置。攻击者打开组策略：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoEDGib57aX8SfBJIC7zr5ibfBnRIrhicdtBpicKib8xP0kAfVzf6k8X7yJ28Q/640?wx_fmt=png&from=appmsg "null")

攻击者感兴趣的部分：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoEV7V446bhJMLyscUn4UxPOmOMCCszLDMlJAF7sql7QWcmeJx38UYebQ/640?wx_fmt=png&from=appmsg "null")

几分钟后在主机上观察到注册表修改：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoEXWfe2ia9ThIIsf3EfcEMSIx6eaFJRDvRcMD6n9uUcC7I6xGfcyJ1Rrw/640?wx_fmt=png&from=appmsg "null")

下面显示的命令利用 WMIC 在备份服务器上远程创建进程。然后，执行一个 PowerShell 脚本，该脚本用于禁用Windows Defender 实时监控。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoEztDSzLCKMcfftsZq5Nd71bmoKNr2lHkB4g4HYDYBZPRHavvJcBzZhQ/640?wx_fmt=png&from=appmsg "null")

使用 CreateRemoteThread API 调用观察到进程注入到多个系统上的各种合法进程中。钓鱼文件和后来的各种 PowerShell Cobalt Strike 载荷都存在这种行为。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoEyaRuJ4BCM9cBDr9PS4fibSWAAVV8PVX1XrJJW7gwJN4cOPFzsYQgrIA/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoE6Kxu9W4UhUjRsjB2j3eLa2pnfibJSkIU4TXKffYelgPOu3M8xY2zYhw/640?wx_fmt=png&from=appmsg "null")

## 凭证访问

在凭证访问阶段，攻击者利用注入的进程 WUAUCLT 来访问最初的失陷主机、文件服务器和备份服务器上的 LSASS 内存空间。授予的访问权限为 0x1010 和 0x1fffff，这两者都说明攻击者在窃取凭据。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeKO0s1X4WKYIF9J73DDmoEEAU9BN4kaMvYWOIJyQibPPgWAltpSEptBde76Be7NnBZ6v7J5XukDVQ/640?wx_fmt=png&from=appmsg "null")

代码0x1010分解如下：

* • 0x00000010 （VMRead）：授予从进程读取内存的能力。
* • 0x00001000 （QueryLimitedInfo）：允许检索某些与进程相关的信息。

相比之下，0x1fffff标志对进程的完全访问权限，使其成...