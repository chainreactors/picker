---
title: 如何以一种意外的方式发现并找到 WinIO 内核驱动栈溢出漏洞
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247535137&idx=3&sn=e26eb362e18303614e9d972bab15b76a&chksm=c1e9c670f69e4f668ba0c2a2586fdf957ebc45dad4a219e01b0e5afcedcbac1bc720386aef15&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-03-04
fetch_date: 2025-10-04T08:39:55.821521
---

# 如何以一种意外的方式发现并找到 WinIO 内核驱动栈溢出漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguJ86m5mDbJOo3oc8pib7tf1hTkqmZkhiabviasmO0WBzfEyO3f65SKYIppDBZwXvj2SFRd5uE4SDBYQ/0?wx_fmt=jpeg)

# 如何以一种意外的方式发现并找到 WinIO 内核驱动栈溢出漏洞

关键基础设施安全应急响应中心

研究人员在OEM厂商的外围设备中发现了多个漏洞，这影响了这些OEM厂商（Razer、EVGA、MSI、AMI）的许多用户。这些漏洞源于一个众所周知的易受攻击的驱动程序，通常被称为WinIO/WinRing0。

本文会重点介绍一个有趣的TOCTOU漏洞案例（CVE-2022-25637），以及其他一些漏洞。

众所周知，MSI开发了一个名为MSI Dragon Center的便捷工具，其目的是检索有关计算机统计信息（即GPU/CPU使用情况）并控制硬件相关设置。

不过从实际反馈来看，它运行得并不好，出现了许多UI问题并且加载时间慢。有研究人员在调整MSI电脑上风扇的速度时，无疑发现了其中的问题，很可能是MSI使用了内核驱动程序。本文的作者检查证实了MSI使用内核驱动程序来执行Dragon Center提供的一些功能，即风扇控制功能是通过WMI对象或供应商特定的API(如NvAPI\_GPU\_SetCoolerLevels)完成的，并没有在Dragon Center代码中实现。此外，Dragon Center加载了一个名为WinIO的驱动程序，这显然与风扇控制的逻辑无关。综合上述事件，我开始研究WinIo驱动程序，因为它可能会构成一个有趣的攻击面。

WinIO是由www.internals.com开发的著名内核驱动程序（该网站已不再在线，但可以通过archive.org访问）。WinIO驱动程序库允许32位和64位Windows用户模式进程直接访问I/O端口、MSR寄存器和物理内存，它已被许多供应商广泛使用。由于它具有强大的功能，因此责任重大，驱动程序应该只允许特权用户使用这些功能。

然而，在WinIo中，情况有所不同，任何用户都可以与之交互，包括沙盒应用程序。WinIo可以简单地在设备对象上设置一个安全描述符，以避免低权限用户与其交互，如下面的代码片段所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0U6ia6l4b0R0xibricm4GegWCmib9sbA23L94Ex0k3T03yHSWXoGKoVeXnib9PGicITwofkwE9I8he0KQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

将SDDL应用于设备对象

我在我的设备上发现的WinIo版本是驱动程序的早期版本（我们怀疑它是WinIo 2.0版），即使是最简单的漏洞也极易对其发起攻击，一个简单的DeviceIoControl请求可能会破坏堆栈。通过使用具有IOCTL代码0x80102040的DeviceIoControl发送I/O请求，研究人员得到了一个memmove方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0U6ia6l4b0R0xibricm4GegWwqntsoOiariaIlwk5Dc02eBeXewI059WZDndVv7Uo0CSkc1W7evxKWxg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

WinIo调度函数：易受攻击的memmove/memcpy

此memmove缺少任何参数检查。更准确地说，它属于控制长度参数，该参数源自SystemBuffer。因此，通过指定大于IOPM本地变量长度的长度，我们可以很容易地破坏堆栈。因此，我们可以重写本地堆栈数据，这是一个经典的缓冲区溢出场景，它可以导致重写调用方的返回指针，再加上使用ROP链，最终导致权限升级。

然而，存在另一个漏洞，即通过物理内存映射的权限升级，这允许我们拥有一个强大的R/W原语。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic0U6ia6l4b0R0xibricm4GegW4YfV2bIpf8P5waCmahJiax9ZldbldelSaWxViaC2UlicwKuicUnud9XXUQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

WinIO中的任意内存R/W函数

此时，会出现一个问题，这个代码库是否可以用于其他地方\驱动程序？

# **寻找其他易受攻击的程序**

我们在VirusTotal中编写了一个相对简单的查询，并找到了114个潜在驱动程序的匹配项，，这些潜在驱动程序可能与我们的脆弱驱动程序共享相同的代码库。

通过快速浏览一些驱动程序的逆向代码，许多供应商似乎使用了WinIo驱动程序的相同易受攻击的代码库。

其中Razer Synapse Service.sys特别引起了我的注意。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ic0U6ia6l4b0R0xibricm4GegWriamUFgTNXfQiaadica1Xepib8WfrxdmjwK602QWex43KpNjnRCa5YGhdQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

Razer Synapse Servicesys VirusTotal结果

# **三个异常的Razer Synapse**

研究人员的设备上安装的是Razer Synapse，Razer Synapse(雷蛇云驱动)是款云端软件,配合Razer的键鼠使用,可以把游戏配置文件、宏,已经鼠标等的设置参数同步到云端。Razer Synapse加载了一些驱动程序，其中之一是Razer Synape服务。sys–具有不同名称的WinIo驱动程序。通常，当加载WinIo驱动程序时，不会对设备对象设置安全限制。然而，在这种情况下，它有一个限制性的安全描述符。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ic0U6ia6l4b0R0xibricm4GegWIK7aibKXDbic9xtouYUwGyT7O6IK7qS7lPUYn7ZZbptFYtDYRY88a08A/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

应用于Razer驱动程序的SDDL

此时，通常应该放弃此驱动程序，即使它是错误的，因为为了与此驱动程序交互，你需要具有高权限，这意味着你已经可以执行特权操作。

在Windows中，如果你以admin+的身份开始，那么让驱动程序做一些异常的操作并不会被视为是不安全的事情。由于驱动程序没有设置安全描述符，所以这一定是在其他地方完成的。

根据MSDN的描述：“设备对象的安全性可以由放置在INF文件中或传递给IoCreateDeviceSecure的SDDL字符串指定。”

现在，我们应该仔细分析一下INF文件，但令人惊讶的是，并没有INF文件！

不得不说这是一个很奇怪的情况，我们怀疑Razer Synapse Service.exe将SDDL设置为驱动程序创建的设备对象。为此，我们监控了Procmon中的系统，并注意到该程序负责加载Razer Synapse Service.sys驱动程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ic0U6ia6l4b0R0xibricm4GegWM0fib8Pmaf331WtHFHQMdjyvjY06646KRqHo56iadnKA4ec4GcFoGSIA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

准备安装 “Razer Synapse Service.sys”

我们需要对Razer Synapse Service.exe进行逆向工程，以了解它在何处应用安全描述符。幸运的是，它是用C#编写的，这将使我们的逆向工程工作更容易，因为我们可以使用reflector。

通过遍历模块列表，找出哪个模块负责加载内核驱动程序。我们将不同的模块反编译回C#（我们使用了DnSpy），然后继续查找与服务控制管理器（SC管理器）进行的任何通信。我们发现负责此事的模块是LibreHardwareMonitorLib（开源）。

如果我们仔细观察代码，就会发现一些奇怪的东西。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ic0U6ia6l4b0R0xibricm4GegWMv0XCQSMSicUcibqtMZIRPymY0uLf5BbaHfrkIQsD71FcIVLk0nL9VRA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

我们可以看到，在第11-14行中，服务尝试打开驱动程序创建的设备对象的句柄，然后为其设置新的安全描述符。我的意思是，他们在用户模式下使用了正确的方法，但他们一开始就不应该在用户模式空间中这样做。

如上所述，应用SDDL应该在内核中完成，并在设备创建时完成。事实上，它没有在内核空间中发生，这导致设备对象持有一个默认的安全描述符，该描述符允许低权限用户与设备对象交互。

这是检查使用时间漏洞的典型案例。如果我们能够利用这个短时间段获取设备对象的句柄，那么我们就可以滥用WinIo的漏洞。

# **漏洞利用**

“Razer Synapse Service”配置为自动启动。因此，我们不能从低权限用户的角度随意重新启动它。要利用该漏洞，就是要在不重新启动服务的情况下重新创建竞争条件（race condition）。

事实证明，使用synapse3提供的更新机制，触发这种情况相对容易。每当安装新更新或新插件时，Razer Synapse Service将重新启动。

重新启动过程包括卸载WinIo驱动程序，然后重新加载。因此，允许我们触发竞争条件。这是通过安装一个新模块来完成的，这一操作不需要特权，因为Synsapse3支持Alexa、Chroma Connect、Chroma Studio、Philips HUE等模块。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ic0U6ia6l4b0R0xibricm4GegWtkMcCFw84wpSYuOEsBF9PgTKwhbwb8HxS3IJLibr6OZQ9IIzGMZ1OiaQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

模块列表Synapse 3

如果我们选择安装其中一个模块，synapse3进程将通过命名管道向Razer Central Service发送命令，以安装所选模块。

RazerCentralService.exe启动模块安装，包括停止和启动RazerSynapse服务，从而卸载和加载驱动程序。为此，我们创建了一个POC，该POC完成了整个过程，在POC触发模块安装期间，一个无限的while循环尝试使用CreateFile API打开设备对象的句柄。我们设法在安全描述符更改之前打开了设备的句柄，换句话说，我们赢得了竞争。此时，服务更改安全描述符并不重要，因为我们拥有设备对象的有效句柄。

现在我们可以自由地与设备对象交互，可以利用WinIo的一些漏洞。在本文的POC中，我们利用了MSR R/W原语。写入MSR原语允许我们重写IA32\_LSTAR MSR。这个特定的MSR保存着指向处理系统调用的内核函数的指针(KiSystemCall64Shadow)。通过重写函数指针，我们可以实现任意的内核代码执行。

根据@\_xeroxz的经验，我们使用称为msrexec的工具轻松地开发了MSR写入原语漏洞。

# **总结**

这项研究是我们修设备风扇时无意中发现的一个漏洞，通过利用一个很酷的竞争条件，导致在内核中运行代码。

**参考及来源：**

https://www.cyberark.com/resources/threat-research-blog/inglourious-drivers-a-journey-of-finding-vulnerabilities-in-drivers

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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