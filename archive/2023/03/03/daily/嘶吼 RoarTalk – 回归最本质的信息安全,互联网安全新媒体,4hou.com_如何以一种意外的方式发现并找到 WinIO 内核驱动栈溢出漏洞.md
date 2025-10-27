---
title: 如何以一种意外的方式发现并找到 WinIO 内核驱动栈溢出漏洞
url: https://www.4hou.com/posts/oJG3
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-03
fetch_date: 2025-10-04T08:29:59.493685
---

# 如何以一种意外的方式发现并找到 WinIO 内核驱动栈溢出漏洞

如何以一种意外的方式发现并找到 WinIO 内核驱动栈溢出漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 如何以一种意外的方式发现并找到 WinIO 内核驱动栈溢出漏洞

luochicun
[技术](https://www.4hou.com/category/technology)
2023-03-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)136744

收藏

导语：本文会重点介绍一个有趣的TOCTOU漏洞案例（CVE-2022-25637），以及其他一些漏洞。

研究人员在OEM厂商的外围设备中发现了多个漏洞，这影响了这些OEM厂商（Razer、EVGA、MSI、AMI）的许多用户。这些漏洞源于一个众所周知的易受攻击的驱动程序，通常被称为WinIO/WinRing0。

本文会重点介绍一个有趣的TOCTOU漏洞案例（CVE-2022-25637），以及其他一些漏洞。

众所周知，MSI开发了一个名为MSI Dragon Center的便捷工具，其目的是检索有关计算机统计信息（即GPU/CPU使用情况）并控制硬件相关设置。

不过从实际反馈来看，它运行得并不好，出现了许多UI问题并且加载时间慢。有研究人员在调整MSI电脑上风扇的速度时，无疑发现了其中的问题，很可能是MSI使用了内核驱动程序。本文的作者检查证实了MSI使用内核驱动程序来执行Dragon Center提供的一些功能，即风扇控制功能是通过WMI对象或供应商特定的API(如NvAPI\_GPU\_SetCoolerLevels)完成的，并没有在Dragon Center代码中实现。此外，Dragon Center加载了一个名为WinIO的驱动程序，这显然与风扇控制的逻辑无关。综合上述事件，我开始研究WinIo驱动程序，因为它可能会构成一个有趣的攻击面。

WinIO是由www.internals.com开发的著名内核驱动程序（该网站已不再在线，但可以通过archive.org访问）。WinIO驱动程序库允许32位和64位Windows用户模式进程直接访问I/O端口、MSR寄存器和物理内存，它已被许多供应商广泛使用。由于它具有强大的功能，因此责任重大，驱动程序应该只允许特权用户使用这些功能。

然而，在WinIo中，情况有所不同，任何用户都可以与之交互，包括沙盒应用程序。WinIo可以简单地在设备对象上设置一个安全描述符，以避免低权限用户与其交互，如下面的代码片段所示。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675930153143367.png "1675930153143367.png")

将SDDL应用于设备对象

我在我的设备上发现的WinIo版本是驱动程序的早期版本（我们怀疑它是WinIo 2.0版），即使是最简单的漏洞也极易对其发起攻击，一个简单的DeviceIoControl请求可能会破坏堆栈。通过使用具有IOCTL代码0x80102040的DeviceIoControl发送I/O请求，研究人员得到了一个memmove方法。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675930162176308.png "1675930162176308.png")

WinIo调度函数：易受攻击的memmove/memcpy

此memmove缺少任何参数检查。更准确地说，它属于控制长度参数，该参数源自SystemBuffer。因此，通过指定大于IOPM本地变量长度的长度，我们可以很容易地破坏堆栈。因此，我们可以重写本地堆栈数据，这是一个经典的缓冲区溢出场景，它可以导致重写调用方的返回指针，再加上使用ROP链，最终导致权限升级。

然而，存在另一个漏洞，即通过物理内存映射的权限升级，这允许我们拥有一个强大的R/W原语。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675930170273120.png "1675930170273120.png")

WinIO中的任意内存R/W函数

此时，会出现一个问题，这个代码库是否可以用于其他地方\驱动程序？

**寻找其他易受攻击的程序**

我们在VirusTotal中编写了一个相对简单的查询，并找到了114个潜在驱动程序的匹配项，，这些潜在驱动程序可能与我们的脆弱驱动程序共享相同的代码库。

通过快速浏览一些驱动程序的逆向代码，许多供应商似乎使用了WinIo驱动程序的相同易受攻击的代码库。

其中Razer Synapse Service.sys特别引起了我的注意。

![4.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675930178397017.jpeg "1675930178397017.jpeg")

Razer Synapse Servicesys VirusTotal结果

**三个异常的Razer Synapse**

研究人员的设备上安装的是Razer Synapse，Razer Synapse(雷蛇云驱动)是款云端软件,配合Razer的键鼠使用,可以把游戏配置文件、宏,已经鼠标等的设置参数同步到云端。Razer Synapse加载了一些驱动程序，其中之一是Razer Synape服务。sys–具有不同名称的WinIo驱动程序。通常，当加载WinIo驱动程序时，不会对设备对象设置安全限制。然而，在这种情况下，它有一个限制性的安全描述符。

![5.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675930186110964.jpeg "1675930186110964.jpeg")

应用于Razer驱动程序的SDDL

此时，通常应该放弃此驱动程序，即使它是错误的，因为为了与此驱动程序交互，你需要具有高权限，这意味着你已经可以执行特权操作。

在Windows中，如果你以admin+的身份开始，那么让驱动程序做一些异常的操作并不会被视为是不安全的事情。由于驱动程序没有设置安全描述符，所以这一定是在其他地方完成的。

根据MSDN的描述：“设备对象的安全性可以由放置在INF文件中或传递给IoCreateDeviceSecure的SDDL字符串指定。”

现在，我们应该仔细分析一下INF文件，但令人惊讶的是，并没有INF文件！

不得不说这是一个很奇怪的情况，我们怀疑Razer Synapse Service.exe将SDDL设置为驱动程序创建的设备对象。为此，我们监控了Procmon中的系统，并注意到该程序负责加载Razer Synapse Service.sys驱动程序。

![6.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675930196639865.jpeg "1675930196639865.jpeg")

准备安装 “Razer Synapse Service.sys”

我们需要对Razer Synapse Service.exe进行逆向工程，以了解它在何处应用安全描述符。幸运的是，它是用C#编写的，这将使我们的逆向工程工作更容易，因为我们可以使用reflector。

通过遍历模块列表，找出哪个模块负责加载内核驱动程序。我们将不同的模块反编译回C#（我们使用了DnSpy），然后继续查找与服务控制管理器（SC管理器）进行的任何通信。我们发现负责此事的模块是LibreHardwareMonitorLib（开源）。

如果我们仔细观察代码，就会发现一些奇怪的东西。

![7.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675930204201005.jpeg "1675930204201005.jpeg")

我们可以看到，在第11-14行中，服务尝试打开驱动程序创建的设备对象的句柄，然后为其设置新的安全描述符。我的意思是，他们在用户模式下使用了正确的方法，但他们一开始就不应该在用户模式空间中这样做。

如上所述，应用SDDL应该在内核中完成，并在设备创建时完成。事实上，它没有在内核空间中发生，这导致设备对象持有一个默认的安全描述符，该描述符允许低权限用户与设备对象交互。

这是检查使用时间漏洞的典型案例。如果我们能够利用这个短时间段获取设备对象的句柄，那么我们就可以滥用WinIo的漏洞。

**漏洞利用**

“Razer Synapse Service”配置为自动启动。因此，我们不能从低权限用户的角度随意重新启动它。要利用该漏洞，就是要在不重新启动服务的情况下重新创建竞争条件（race condition）。

事实证明，使用synapse3提供的更新机制，触发这种情况相对容易。每当安装新更新或新插件时，Razer Synapse Service将重新启动。

重新启动过程包括卸载WinIo驱动程序，然后重新加载。因此，允许我们触发竞争条件。这是通过安装一个新模块来完成的，这一操作不需要特权，因为Synsapse3支持Alexa、Chroma Connect、Chroma Studio、Philips HUE等模块。

![8.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675930213528303.jpeg "1675930213528303.jpeg")

模块列表Synapse 3

如果我们选择安装其中一个模块，synapse3进程将通过命名管道向Razer Central Service发送命令，以安装所选模块。

RazerCentralService.exe启动模块安装，包括停止和启动RazerSynapse服务，从而卸载和加载驱动程序。为此，我们创建了一个POC，该POC完成了整个过程，在POC触发模块安装期间，一个无限的while循环尝试使用CreateFile API打开设备对象的句柄。我们设法在安全描述符更改之前打开了设备的句柄，换句话说，我们赢得了竞争。此时，服务更改安全描述符并不重要，因为我们拥有设备对象的有效句柄。

现在我们可以自由地与设备对象交互，可以利用WinIo的一些漏洞。在本文的POC中，我们利用了MSR R/W原语。写入MSR原语允许我们重写IA32\_LSTAR MSR。这个特定的MSR保存着指向处理系统调用的内核函数的指针(KiSystemCall64Shadow)。通过重写函数指针，我们可以实现任意的内核代码执行。

根据@\_xeroxz的经验，我们使用称为msrexec的工具轻松地开发了MSR写入原语漏洞。

**总结**

这项研究是我们修设备风扇时无意中发现的一个漏洞，通过利用一个很酷的竞争条件，导致在内核中运行代码。

本文翻译自：https://www.cyberark.com/resources/threat-research-blog/inglourious-drivers-a-journey-of-finding-vulnerabilities-in-drivers如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?SPE8BVPQ)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/07/6cfb327dad8fe371f6fa.jpg)

# [luochicun](https://www.4hou.com/member/aOZG)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/aOZG)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

![]()

[公司简介](htt...