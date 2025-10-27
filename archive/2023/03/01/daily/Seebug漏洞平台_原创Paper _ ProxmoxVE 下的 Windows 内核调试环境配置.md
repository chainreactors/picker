---
title: 原创Paper | ProxmoxVE 下的 Windows 内核调试环境配置
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650967549&idx=1&sn=e0466ea46609c8934acb8bc8f45090d7&chksm=8079cfcfb70e46d923d146acc3b67003b7b051c25c05c6ad1e553d1cd55bc407b680905007ed&scene=58&subscene=0#rd
source: Seebug漏洞平台
date: 2023-03-01
fetch_date: 2025-10-04T08:20:46.790089
---

# 原创Paper | ProxmoxVE 下的 Windows 内核调试环境配置

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCbIJhNs9uaOuRicic3GHOkCy2gq8hCFmRhriacSGFF5wMX0Gf8dasVmZUg/0?wx_fmt=jpeg)

# 原创Paper | ProxmoxVE 下的 Windows 内核调试环境配置

原创

404实验室

知道创宇404实验室

![](https://mmbiz.qpic.cn/mmbiz_gif/3k9IT3oQhT09IJjs3wGQbICd50va8zMqfnXZfD5LGdibcuOrtia3P4DpMAVfibZ8J4MsbHt0JW20QL8Wh0SO8zpyA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

作者：0x7F@知道创宇404实验室
日期：2023年2月27日

**0x00 前言**

参考资料

Windows内核调试常用于 windows 驱动开发调试、内核分析等，使用 WinDBG 可以很方便的进行本地内核调试，但本地内核调试存在较多的限制(如不能使用导致主机暂停运行的指令)，通常我们都会通过虚拟机软件搭建 windows 双机调试环境，其中一台作为调试机(debuger)，另一台作为被调试机(debugee)，双机调试几乎可以满足大部分的 windows 内核分析、调试等工作。

通过 Vmware 虚拟机软件搭建 windows 双机调试环境是最常见的方案，搭建步骤和坑点基本都由前辈梳理成章了，但我日常工作都由 ProxmoxVE 虚拟机支撑起来，遂想使用 ProxmoxVE 配置 windows 的内核调试环境，在此过程中遇到了不少难点。

本文对 ProxmoxVE 下的 windows 内核调试环境配置进行了详细介绍和实验演示，对其中的难点进行了简易分析，希望本文能对有相同需求的小伙伴提供一些帮助。

**0x01 基本环境**

参考资料

本文环境如下：

```
```
ProxmoxVE 7.2-3Windows10 1909 专业版
```
```

ProxmoxVE 是一套基于 KVM 的虚拟化解决方案，由于其开源特性以及 Linux 的亲和性，ProxmoxVE 通常在企业内部大量使用，同时也常常作为商业软件的底层支撑组件。同类软件还有大名鼎鼎的 Vmware 和 VirtualBox，这些软件在使用方面都大同小异。

ProxmoxVE 底层是一台 Debian 主机，然后基于 KVM+Qemu 实现了虚拟化软件，配置完成后可通过 web 控制台(https://[ip]:8006)进行管理和使用：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCWtdRIA7QJd5XEVxDf2hq8ibfUazibysiaGGXMc9b9kDpGUZC58CAeOWpg/640?wx_fmt=png)

[1.PVE的web控制台]

通常情况下，我们使用 Vmware 搭建 windows 双机调试环境，都以宿主机作为调试机(debuger)，以虚拟机作为被调试机(debugee)，通过 Vmware 配置串口设备(serial) 通信进行调试；

而 ProxmoxVE 是一台 Linux 主机，要搭建 windows 双机调试环境必需要两台虚拟机才行。

**0x02 本地内核调试**

参考资料

我们先从简单的本地内核调试环境开始，以此来准备基本的调试环境；在 ProxmoxVE 中安装 windows10 系统，并完成基本的配置如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCDwCOYQUgJIqDzK7331icnooibkhZDdjJLSqhmhhymdLX9mXLkhTiaTHYA/640?wx_fmt=png)

[2.本地内核调试环境]

我们从官网下载 WinDBG 并在 windows10 系统上进行安装：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCNkXiaaqGnf8Cupnlf1ibUoibnQuqn9tNo11AU0SibRVO1iaLNhMdsTpmKrw/640?wx_fmt=png)

[3.windbg安装配置]

并在环境变量中(系统变量)配置符号表设置：

```
```
_NT_SYMBOL_PATHSRV*c:\symbols*http://msdl.microsoft.com/download/symbols
```
```

> 配置完成后，WinDBG在调试过程中将自动从微软符号表服务器下载对应数据，并保存至 C:\symbols 下；
> 也可以在 WinDBG 中使用 Ctrl+S 配置符号表，不过采用环境变量的方式还可以方便其他应用使用该配置。

随后我们使用 bcdedit 修改 windows 的启动配置数据文件，使用管理员权限打开 powershell：

```
```
# 开启 debug$ bcdedit /debug on# 查看 bcdedit 配置$ bcdedit# 查看 dbgsettings 配置(默认为 local)$ bcdedit /dbgsettings
```
```

执行如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCIfs3Dj3cAzlL5KmgDiaLBIjjprESgma4zxQ0qhZvEVL0LFu67ewYSMw/640?wx_fmt=png)

[4.bcdedit配置本地调试]

> 通过 windows 开机启动项选择「启用调试模式」也是一样的，不过通过 bcdedit 修改是永久有效的。
> 如果不想影响目前的配置，可以通过 bcdedit /copy "{current}" /d "debug test" 复制当前配置，随后使用 bcdedit /set "{id}" debug on 进行配置，在开机时可选择不同的启动项进入系统。

随后重启 windows10 虚拟机生效配置，使用管理员权限启动 WinDBG，选择 File - Kernel Debug，选择 Local 本地调试标签：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCzyWC9IL30iaHKKIZOS2gruLGtUNRkLSKaSkm4dr7FLmdGFich4knRdHg/640?wx_fmt=png)

[5.windbg-local标签]

随后便可以正常进行本地内核调试，我们能够查看内核中的各项数据；但本地内核调试不能影响系统的运行，所以不能打断点、单步调试等，当然 go 指令也是不能使用的：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCzpUQpT3ibs0ITY131QuVWherlh2ib2XeiaKaH31YO9QyWedxah4rez4ug/640?wx_fmt=png)

[6.windbg本地内核调试]

**0x03 网络双机调试**

参考资料

从 windows8 开始微软提供了网络调试内核的方法，其简称为 kdnet，因为通信效率要比串口高，所以使用起来体验更好，是目前微软推荐的内核调试方法。

网络双机调试除了对系统版本有要求，对网卡也有一定的要求，支持的厂商和型号可以查阅 https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/supported-ethernet-nics-for-network-kernel-debugging-in-windows-10 ；除此之外，还需要两台主机位于同一子网内。

那么我们需要在 ProxmoxVE 再添加一台 windows10 虚拟机作为被调试机(debugee)，以我们上文本地内核调试中的主机作为调试机(debuger)，以此用两台虚拟机组成 windows 网络双机调试的环境，如下：

> 本地内核调试中的配置 bcdedit /debug on 不会影响该步骤，也可以手动设置 bcdedit /debug off 关闭调试功能。

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCtFzNAwjWILLDaVpykIUOX6pTSWfSh2ScmhXhiclBcfctML1GxjPXcuw/640?wx_fmt=png)

[7.网络双机调试环境]

搭建这台被调试机(debugee)时需要注意，在配置操作系统类型时应选择 Other 类型，如下：(如果选择 windows 类型，ProxmoxVE 在虚拟化时会提供 Hyper-V 的各项支持，以此来提高虚拟机的性能，但这些项导致网络调试无法正常运行，我们将在 ### 0x05 kdnet问题排查 进行简要分析)

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCB91QiaKGALLKfRdDVmDlKic9H6iakEGA1kb3HqDGaiao9fuB7ZFvKWpGXA/640?wx_fmt=png)

[8.系统类型配置为other]

由于配置为 Other 类型，ProxmoxVE 可能无法提供 windows 的推荐配置，最终导致无法正确安装 windows 系统，若遇到该问题可排查磁盘是否设置为 IDE 类型。

除此之外，在网卡配置阶段需要选择 Intel E1000，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCtnODBAmosX04XQZ7Lictt1iaxBXl9BEbbWs1QAibF4iaKmjEu11QO6IGhw/640?wx_fmt=png)

[9.网卡配置为intel e1000]

根据测试 e1000 网卡在系统内部的硬件 id 为 VEN\_8086&DEV\_100E，满足网络调试对网卡的要求；另外 Realtek RTL8139 不满足要求，而VirtIO 和 Vmware vmxnet3 需要安装特定驱动才能使用。

接下来完成 windows10 系统安装和基础配置，随后进行网络调试的配置；官方推荐使用 kdnet 工具进行自动配置，但并不能顺利配置；

我们从调试机(debuger) 的 WinDBG 目录中(C:\Program Files (x86)\Windows Kits\10\Debuggers\x64) 拷贝 kdnet.exe 和 VerifiedNICList.xml 到被调试机上(debugee)，按官方教程操作如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCeehplmiaCwpNBZbvDNcVqiauc5xE6nCvIOibou2oO8jyKicemBKzibetRAg/640?wx_fmt=png)

[10.kdnet自动配置失败]

虽然我们的网卡位于 VerifiedNICList 中，但 kdnet.exe 无法正确解析。我们按官方手动配置教程进行设置：

```
```
# 开启 debug$ bcdedit /debug on# 设置网络调试参数# 设置调试机(debuger)的 ip 地址为 10.0.25.192# 设置被调试机的端口为 50000 (必须>=49152)# 设置被调试机的连接密码为 p.a.s.s (必须为 x.x.x.x 格式)$ bcdedit /dbgsettings NET HOSTIP:10.0.25.192 PORT:50000 KEY:p.a.s.s# 查看调试配置$ bcdedit /dbgsettings
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBC3nGQgyToYVRxXYOo5ga4HGyibtZTOaeicf11abW0JWpTCiaFRsNGk6lLQ/640?wx_fmt=png)

[11.手动配置kdnet]

完成配置后重启生效；随即我们在调试机(debuger) 使用 WinDBG 进行网络调试配置，端口号为 50000，密钥为 p.a.s.s，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCmOrjTiaghFKbAmgjCBkQtS3ZZ5PyMg4E8MwlibEUxZA4A4LPXjTiaia8gg/640?wx_fmt=png)

[12.windbg-net标签]

无论被调试机(debugee) 是在运行期间还是重启阶段，都可以被调试机(debuger)正确连接并进行调试，连接成功后可使用 break 断下来：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCvxvsLNWkeBIOV2V36A7XheSpOkapTI19nTLOjdzG1eOd1ODiaCjKcxg/640?wx_fmt=png)

[13.windbg网络双机调试]

> 如果 ProxmoxVE 和虚拟机未采用 DHCP 分配 ip 地址，被调试机(debugee) 会在启动阶段卡在 windows logo 阶段 10min 左右，我们将在 ### 0x05 kdnet问题排查 进行简要分析。

**0x04 串口双机调试**

参考资料

### 微软从 windows8 才开始提供网络调试功能，如果要调试 windows7 系统则需要使用传统的串口双机调试的方法了。这里我们复用上文环境，配置 windows10 虚拟机的串口双机调试，windows7 同理可得，环境配置如下：

> 上文中网络双机调试中的各项配置、操作系统类型、网卡类型均不影响该步骤。

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCic0heflYWzCOBcMcCIdOLCgN2y3TR7BFeSCmPgmE4mjTtU6OFRZrGMA/640?wx_fmt=png)

[14.串口双机调试环境]

首先我们为两台 windows10 虚拟机添加串口(虚拟机关机后再开机硬件改动生效)，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCwVTI1mdg3PbBxS8QGhYMicR1BicKrXBibzK9xW7sCCIgm3gnqnAdnSMTw/640?wx_fmt=png)

[15.pve添加串口设备]

> 配置成功后，可在 windows 设备管理器中看到 com 设备。

目前这两个串口独立运行，我们通过 ssh 登录 ProxmoxVE 的控制台，使用 socat 将两个接口连接起来：

```
# 正常启动两台虚拟机后# pve(windows10-1)=132 / pve(windows10-2)=133# 使用 tmux 开启后台终端，socat 需要一直运行$ tmux# socat 连接两个串口设备# 使用 -v 查看运行日志# 使用 UNIX-CLIENT 的类型打开文件$ socat -v UNIX-CLIENT:/var/run/qemu-server/132.serial0 UNIX-CLIENT:/var/run/qemu-server/133.serial0
```

```
配置完成后，我们在被调试机(debugee)中设置串口调试：
```

```
```
# 开启 debug$ bcdedit /debug on# 设置串口调试参数# 设置调试串口为 1 (com1)# 设置串口波特率为 115200$ bcdedit /dbgsettings SERIAL DEBUGPORT:1 BAUDRATE:115200# 查看调试配置$ bcdedit /dbgsettings
```
```

执行如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCTicyTJJmXhE6cCSGP43nXiayRiaygkGLYNMUVsiakTugqd2Nffj3gVzs2Q/640?wx_fmt=png)

[16.bcdedit配置串口调试]

随后我们切换至调试机(debuger)下，使用 WinDBG 设置串口调试配置，波特率为 115200，端口为 1，不勾选 pipe，勾选 reconnect，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBCOUdtuia2x9QRHk4pzzKjxVFib9nvv6wItibf3gk2qeAwCyCYhOk4ZeKhg/640?wx_fmt=png)

[17.windbg-com标签]

设置完毕后，在 WinDBG 显示 Waiting to reconnect... 后，重启被调试机(debugee)，调试机(debuger)将在其系统启动时连接上去，使用 break 可将其断下来，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT2HQTvGbRsYlJu5roZy8XBC9m1ib80Z5JsFyUickH1xYBJ72wMGhCFicrToyqyOw7llUz8NGNwOc1JOw/640?wx_fmt=png)

[18.windbg串口双机调试]

> 我这里首次连接时 WinDBG 将异常退出，不过重新启动 WinDBG 并设置好参数即可成功连接。

**ProxmoxVE串口调试的一些补充**

熟悉 Vmware 搭建 windows 内核调试的朋友，通常都使用命名管道进行配置如 \\.\pipe\com1，但 ProxmoxVE 下的串口设备(se...