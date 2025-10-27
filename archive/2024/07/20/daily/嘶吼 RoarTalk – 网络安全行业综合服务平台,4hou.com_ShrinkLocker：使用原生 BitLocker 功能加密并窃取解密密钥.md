---
title: ShrinkLocker：使用原生 BitLocker 功能加密并窃取解密密钥
url: https://www.4hou.com/posts/qoxG
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-20
fetch_date: 2025-10-06T17:41:29.067497
---

# ShrinkLocker：使用原生 BitLocker 功能加密并窃取解密密钥

ShrinkLocker：使用原生 BitLocker 功能加密并窃取解密密钥 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# ShrinkLocker：使用原生 BitLocker 功能加密并窃取解密密钥

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-07-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)85445

收藏

导语：本文将详细分析在事件响应工作中获得的恶意代码，并提供缓解此类威胁的建议。

**介绍**

攻击者总是能找到各种创造性的方法来绕过防御功能并达到他们的目的，例如通过打包程序、加密程序和代码混淆来实现。然而，逃避检测以及最大化兼容性的最佳方法之一是使用操作系统自身的功能。

在勒索软件威胁的背景下，一个值得注意的情况是利用加密 DLL ADVAPI32.dll 中存在的导出函数，例如 CryptAcquireContextA、CryptEncrypt 和 CryptDecrypt。通过这种方式，攻击者可以确保恶意软件在支持此 DLL 的各种版本的操作系统中运行并模拟正常行为。

而在最近的一次事件响应中，另一种巧妙的技术引起了安全研究人员的注意：使用原生 BitLocker 功能加密并窃取解密密钥。BitLocker 的最初目的是解决丢失、被盗或不当退役设备导致数据被盗或泄露的风险，然而，威胁者发现这种机制可以被重新用于实现恶意目的，且效果非常好。

在该事件中，攻击者能够部署并运行一个高级 VBS 脚本，该脚本利用 BitLocker 进行未经授权的文件加密。安全研究人员在墨西哥、印度尼西亚和约旦发现了此脚本及其修改版本。本文将详细分析在事件响应工作中获得的恶意代码，并提供缓解此类威胁的建议。

这不是我们第一次看到 BitLocker 用于加密驱动器并索要赎金。以前，攻击者在访问和控制关键系统后，会使用此 Microsoft 实用程序来加密这些系统。然而，在这种情况下，攻击者采取了额外的措施来最大限度地扩大攻击造成的损害，并阻碍对事件的有效响应。

**VBScript 分析**

一个有趣的现象是，攻击者没有像威胁者通常做的那样费心混淆大部分代码。对此最合理的解释是，当脚本执行时，他们已经完全控制了目标系统。它以 Disk.vbs 的形式存储在 C:\ProgramData\Microsoft\Windows\Templates\ 中。

它的第一行包含一个函数，该函数使用 ADODB.Stream 对象将字符串转换为其二进制表示形式。此函数稍后用于编码要在 HTTP POST 请求中发送的数据。

![Bitlocker_abuse_01.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684430172362.png "1720682724211610.png")

Stream\_StringToBinary 函数

脚本主要功能的第一步是使用 Windows 管理规范 (WMI) 在 Win32\_OperatingSystem 类的帮助下查询有关操作系统的信息。对于查询结果中的每个对象，脚本都会检查当前域是否与目标不同。如果不同，脚本将自动完成。

之后，它会检查操作系统的名称是否包含“xp”、“2000”、“2003”或“vista”，如果 Windows 版本与其中任何一个匹配，脚本将自动完成并删除自身。

![Bitlocker_abuse_02.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684431132210.png "1720682763123434.png")

执行的初始条件

此后，脚本继续依赖 WMI 查询有关操作系统的信息。然后，它会执行磁盘大小调整操作，这些操作可能会因操作系统版本检查的结果而异。这些操作仅在固定驱动器（DriveType = 3）上执行。文件系统中通常存在以下驱动器类型：

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684432113118.png "1720682840129351.png")

恶意软件不会尝试在网络驱动器（DriveType = 4）上执行相同操作的可能原因是为了避免触发网络上的检测工具。

为了调整 Windows Server 2008 或 2012 中的本地驱动器大小，脚本会检查主启动分区并保存此信息。它会保存不同分区的索引，然后使用 diskpart 执行以下操作：

**·**将每个非启动分区的大小缩小 100 MB。这将在启动卷以外的每个分区中创建 100 MB 的未分配空间；

**·**将未分配空间拆分为新的 100 MB 主分区；

**·**使用覆盖选项格式化分区，这会在必要时强制先卸载卷，并为每个分区分配文件系统和驱动器号；

**·**激活分区；如果缩小过程成功，则将“ok”保存为变量，以便脚本可以继续。

![Bitlocker_abuse_03.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684433155522.png "1720682924113881.png")

Windows Server 2008 和 2012 中脚本执行的磁盘大小调整操作

如果操作成功，代码将使用实用程序 bcdboot 和之前保存为启动卷的驱动器号在新的主分区上重新安装启动文件。

![Bitlocker_abuse_04.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684433110207.png "1720682963310530.png")

重新安装引导文件

其他操作系统版本的分区缩小操作类似，但出于兼容性原因，使用不同的代码段实现。下面的示例显示了应用于 Windows 版本 7、8 和 8.1 的过程。

![Bitlocker_abuse_05.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684434858259.png "1720683002192899.png")

Windows 版本 7、8 或 8.1 中的磁盘大小调整操作

对于 Windows 2008 或 7，分区压缩过程完成后，变量 matchingDrives 会保存以逗号分隔的驱动器号，但前提是文件系统为 NFTS、exFAT、FAT32、ReFS 或 FAT。代码经过修改，可打印示例：

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684435338343.png "1720683087158047.png")

然后，该脚本添加以下注册表项：

**·**fDenyTSConnections = 1：禁用 RDP 连接；

**·**scforceoption = 1：强制智能卡身份验证；

**·**UseAdvancedStartup = 1：要求使用 BitLocker PIN 进行预启动身份验证；

**·**EnableBDEWithNoTPM = 1：允许在没有兼容 TPM 芯片的情况下使用 BitLocker；

**·**UseTPM = 2：如果可用，允许使用 TPM；

**·**UseTPMPIN = 2：如果可用，允许使用带有 TPM 的启动 PIN；

**·**UseTPMKey = 2：如果可用，允许使用带有 TPM 的启动密钥；

**·**UseTPMKeyPIN = 2：如果可用，允许使用带有 TPM 的启动密钥和 PIN；

**·**EnableNonTPM = 1：允许在没有兼容 TPM 芯片的情况下使用 BitLocker，需要 ·USB 闪存驱动器上的密码或启动密钥；

**·**UsePartialEncryptionKey = 2：要求使用带有 TPM 的启动密钥；

**·**UsePIN = 2：要求使用带有 TPM 的启动 PIN。

如果脚本检测到错误，它将重新启动系统。

![Bitlocker_abuse_07.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684436200395.png "1720683232784687.png")

注册表修改

通过动态分析恶意软件，我们可以确认执行的注册表更改：

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684437208741.png "1720683287138455.png")

此外，有多个函数执行这些操作，每个函数都是为不同版本的 Windows 设计的。在某些条件下，它会通过远程服务器管理工具的 ID 266 检查 BitLocker 驱动器加密工具是否处于活动状态。然后，恶意软件会检查 BitLocker 驱动器加密服务 (BDESVC) 是否正在运行。如果没有，它会启动该服务。

![Bitlocker_abuse_08.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684438848063.png "1720683314180510.png")

BDESVC 验证

该脚本还将新启动分区的标签更改为攻击者的电子邮件，如下图所示，以便受害者可以联系他们。

![Bitlocker_abuse_09.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684439456414.png "1720683344135101.png")

驱动器标签修改

![Bitlocker_abuse_10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684439278642.png "1720683393176530.png")

攻击者的电子邮件作为驱动器标签

之后，恶意软件会禁用用于保护 BitLocker 加密密钥的保护程序并将其删除。删除方法可能因操作系统版本而异。在 Windows Server 2008 或 Windows 7 场景中，这是通过 VBS 功能实现的，之后脚本使用 PowerShell 强制删除保护程序。

完成删除后，它可以使用数字密码作为保护器和加密功能。

![Bitlocker_abuse_11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684440861622.png "1720683435494308.png")

保护器删除

删除默认保护器的原因是为了避免用户恢复密钥，如下例所示：

![Bitlocker_abuse_12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684441106817.png "1720683467185178.png")

BitLocker密钥的恢复

接下来，恶意软件使用以下元素的随机乘法和替换来生成 64 个字符的加密密钥：

**·**一个包含数字 0-9 的变量；

**·**著名的全字母句子“敏捷的棕色狐狸跳过了懒狗”，有小写和大写两种形式，其中包含英文字母表的每个字母；

**·**特殊字符。

该密码的随机性由受影响系统的各种元素（例如已用内存和网络统计信息）组成的种子实现。稍后，这些信息将发送给攻击者。我们在自己的环境中测试了密钥生成逻辑，对脚本进行了轻微修改后，就能看到生成的密码。

![Bitlocker_abuse_13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684442159336.png "1720683543141206.png")

密钥生成过程

然后，代码将先前生成的加密密钥转换为安全字符串（一种防止在内存中创建字符串对象的 PowerShell 选项），并有效地在驱动器上启用 BitLocker。

然后，脚本使用以下选项创建 HTTP POST 请求对象：

**·**使用 WinHTTP 版本 5.1。

**·**接受法语。

**·**忽略 SSL 错误（httpRequest.Option(4) = 13056 à WinHttpRequestOption\_SslErrorIgnoreFlags）。

**·**禁用重定向（httpRequest.Option(6) = false à WinHttpRequestOption\_EnableRedirects）。

攻击者使用域名trycloudflare.com来混淆其真实地址。该域名是合法的，属于CloudFlare，用于为开发人员提供快速隧道。攻击者配置的子域名是scottish-agreement-laundry-further。

![Bitlocker_abuse_14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684443132763.png "1720683683155266.png")

创建请求

该恶意软件还将有关机器和生成的密码的信息作为 POST 请求的有效负载，如下图所示。

![Bitlocker_abuse_15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684444148459.png "1720683712138408.png")

POST 请求中要发送的信息

该脚本还包含一个循环，如果发生错误，则会尝试将信息发送给攻击者五次。

![Bitlocker_abuse_16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684444138676.png "1720683808880582.png")

重试程序

通过一些调整，我们能够打印发送给攻击者的数据，如下图所示。请注意，数据包括计算机名称、Windows 版本、受影响的驱动器和密码字符串。因此，受害者的 IP 地址也将记录在攻击者的服务器上，从而允许他们跟踪每个受害者。

![Bitlocker_abuse_17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240711/1720684445119944.png "1720683845933778.png")

要发送的信息

删除 BitLock...