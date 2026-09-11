---
title: 【安全更新】微软9月安全更新多个产品高危漏洞通告
url: https://mp.weixin.qq.com/s/yYFG4CjwEZWAgnKLogUxVw
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:49:37.154649
---

# 【安全更新】微软9月安全更新多个产品高危漏洞通告

# 【安全更新】微软9月安全更新多个产品高危漏洞通告

NS-CERT
NS-CERT

绿盟科技CERT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**通告编号 NS-2026-0022**

2026-09-09

|  |  |
| --- | --- |
| **TAG：** | **安全更新、Windows、Office、Azure、Visual Studio Code** |
| **漏洞危害：** | **攻击者利用本次安全更新中的漏洞，可造成权限提升、远程代码执行等** |
| **版本：** | **1.0** |

**1**

**漏洞概述**

9月9日，绿盟科技CERT监测到微软发布9月安全更新补丁，修复了974个安全问题，涉及Windows、Microsoft Office、Azure、Visual Studio Code、Microsoft SQL Server等广泛使用的产品，其中包括权限提升、远程代码执行等高危漏洞类型。

本月微软月度更新修复的漏洞中，严重程度为关键（Critical）的漏洞有114个，重要（Important）漏洞有860。其中包括2个已检测到在野利用的漏洞：

Windows Update Stack权限提升漏洞（CVE-2026-81963）

Windows高级本地过程调用 (ALPC) 权限提升漏洞（CVE-2026-85880）

请相关用户尽快更新补丁进行防护，完整漏洞列表请参考附录。

参考链接：

https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep

**SEE MORE →**

**2****重点漏洞简述**

根据产品流行度和漏洞重要性筛选出此次更新中包含影响较大的漏洞，请相关用户重点进行关注：

**Windows Update Stack权限提升漏洞（CVE-2026-81963）：**

由于Windows Update Stack组件存在不当链接解析（Link Following）漏洞，经过身份验证的本地攻击者可利用该漏洞执行文件访问时的链接跟随操作，从而获取系统SYSTEM权限。该漏洞存在在野利用，CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963

**Windows高级本地过程调用(ALPC)权限提升漏洞（CVE-2026-85880）:**

由于Windows高级本地过程调用(ALPC)组件存在基于堆的缓冲区溢出（Heap-based Buffer Overflow）漏洞，经过身份验证的本地攻击者可通过发送精心构造的ALPC请求或运行特殊应用程序，从而提升系统权限。该漏洞存在在野利用，CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880

**Microsoft DHCP客户端权限提升漏洞（CVE-2026-69777）:**

由于Microsoft DHCP客户端组件存在权限提升漏洞，经过身份验证的本地攻击者可运行精心构造的应用程序，从而提升系统权限。CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69777

**Microsoft安装服务权限提升漏洞（CVE-2026-69605）：**

由于Microsoft安装服务组件存在权限提升漏洞，经过身份验证的本地攻击者可运行特制的程序或利用该漏洞，从而实现本地权限提升。CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69605

**Win32k信息泄露漏洞（CVE-2026-69832）：**

由于Win32k组件存在信息泄露漏洞，经过身份验证的本地攻击者可运行精心构造的应用程序，从而导致敏感系统信息泄露。CVSS评分5.6。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69832

**Windows Cloud Files Mini Filter Driver权限提升漏洞（CVE-2026-80093）：**

由于Windows Cloud Files Mini Filter Driver组件存在释放后重用（Use-After-Free）漏洞，经过身份验证的本地攻击者可利用该漏洞执行特殊操作，从而实现本地权限提升。CVSS评分7.0。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-80093

**Windows DNS Server远程代码执行漏洞（CVE-2026-69730/CVE-2026-69813/CVE-2026-72987/CVE-2026-69858/CVE-2026-69827）：**

由于Windows DNS Server组件存在释放后重用（Use-After-Free）漏洞，未经过身份验证的攻击者可通过向目标服务器发送精心构造的恶意数据包，从而实现远程代码执行。CVSS评分9.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69730

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69813

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72987

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69858

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69827

**Windows DNS权限提升漏洞（CVE-2026-69310）：**

由于Windows DNS组件存在权限提升漏洞，经过身份验证的本地攻击者可利用该漏洞，从而实现本地权限提升。CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69310

**Windows Kerberos远程代码执行漏洞（CVE-2026-69676）：**

由于Windows Kerberos协议组件存在远程代码执行漏洞，攻击者可通过网络发送精心构造的请求，从而实现远程代码执行。CVSS评分8.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69676

**Windows Management Instrumentation (WMI) 权限提升漏洞（CVE-2026-69451）：**

由于Windows Management Instrumentation (WMI) 组件存在权限提升漏洞，经过身份验证的本地攻击者可运行特制的应用程序，从而实现本地权限提升。CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69451

**Windows TCP/IP 权限提升漏洞（CVE-2026-69385）：**

由于Windows TCP/IP堆栈组件存在权限提升漏洞，本地攻击者可利用该漏洞，从而实现本地权限提升。CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69385

**Windows Win32k 权限提升漏洞（CVE-2026-69779/CVE-2026-69498/CVE-2026-69301/CVE-2026-69274/CVE-2026-68880/CVE-2026-70289）：**

由于Windows Win32k内核组件存在权限提升漏洞，经过身份验证的本地攻击者可运行精心构造的应用程序，从而实现本地权限提升。CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69779

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69498

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69301

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69274

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68880

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-70289

**Windows 内核信息泄露漏洞（CVE-2026-69723/CVE-2026-69406/CVE-2026-69466 /CVE-2026-69473/CVE-2026-69366/CVE-2026-68884/CVE-2026-68846）：**

由于Windows内核组件存在信息泄露漏洞，经过身份验证的本地攻击者可运行特制的程序，从而导致敏感内核信息泄露。CVSS评分5.5。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69723

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69406

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69466

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69473

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69366

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68884

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68846

**Windows 基于虚拟化的安全性 (VBS) 信息泄露漏洞（CVE-2026-83501）：**

由于Windows基于虚拟化的安全性(VBS)组件存在越界读取（Out-of-bounds Read）漏洞，攻击者可利用该漏洞绕过安全边界并读取受保护的内存数据，从而导致敏感信息泄露。CVSS评分5.5。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83501

**Windows部署服务远程代码执行漏洞（CVE-2026-72957）：**

由于Windows部署服务组件存在远程代码执行漏洞，攻击者可通过网络发送精心构造的请求，从而导致远程代码执行。CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72957

**Microsoft SQL Server远程代码执行漏洞（CVE-2026-67378/CVE-2026-67631/CVE-2026-67636/CVE-2026-67643）：**

由于Microsoft SQL Server存在不可信指针解引用（Untrusted Pointer Dereference）漏洞，已通过身份验证的攻击者可通过网络向受影响的数据库发送精心构造的恶意请求利用此漏洞，从而在目标系统上实现远程代码执行。CVSS评分8.5。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-67378

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-67631

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-67636

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-67643

**Microsoft Office远程代码执行漏洞（CVE-2026-69285/CVE-2026-69632/CVE-2026-77898/CVE-2026-78505）：** 由于Microsoft Office存在基于堆的缓冲区溢出漏洞，攻击者可诱导用户打开恶意伪装的文档文件利用此漏洞，从而在目标系统上实现远程代码执行。CVSS评分8.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69285

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69632

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-77898

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-78505

**Microsoft Word远程代码执行漏洞（CVE-2026-81952/CVE-2026-77504）：** 由于Microsoft Office Word存在缓冲区溢出或双重释放等内存破坏漏洞，攻击者可诱导受害者加载带有恶意代码的文本文件利用此漏洞，从而在目标系统上实现远程代码执行。CVSS评分8.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81952

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-77504

**Microsoft Excel远程代码执行漏洞（CVE-2026-81949）：**

由于 Microsoft Office Excel 存在整数溢出或绕过漏洞，攻击者可诱导用户在本地运行包含特定畸形数据的表格文件利用此漏洞，从而在目标系统上实现远程代码执行。CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81949

**3****影响范围**

以下为部分重点关注漏洞的受影响产品版本，其他漏洞影响产品范围请参阅官方通告链接。

漏洞编号

受影响产品版本

CVE-2026-85880
CVE-2026-68880
CVE-2026-70289

Windows Server 2012 R2 (Server Core installation)
Windows Server 2012 R2
Windows Server 2012 (Server Core installation)
Windows Server 2012
Windows Server 2016 (Server Core installation)
Windows 10 Version 1607 for x64-based Systems
Windows Server 2016
Windows 10 Version 1607 for 32-bit Systems
Windows 10 Version 22H2 for 32-bit Systems
Windows 10 Version 22H2 for ARM64-based Systems
Windows 10 Version 22H2 for x64-based Systems
Windows 10 Version 21H2 for x64-based Systems
Windows 10 Version 21H2 for ARM64-based Systems
Windows 10 Version 21H2 for 32-bit Systems
Windows Server 2022 (Server Core installation)
Windows Server 2022
Windows Server 2019 (Server Core installation)
Windows Server 2019
Windows 10 Version 1809 for x64-based Systems
Windows 10 Version 1809 for 32-bit Systems

CVE-2026-69777

Windows 11 Version 26H1 for ARM64-based Systems
Windows 11 version 26H1 for x64-based Systems
Windows 11 Version 24H2 for ARM64-based Systems
Windows 11 Version 25H2 for x64-based Systems
Windows 11 Version 24H2 for x64-based Systems
Windows 11 Versi...