---
title: 【安全更新】微软4月安全更新多个产品高危漏洞通告
url: https://mp.weixin.qq.com/s/vqCWhkAK0GECS_SQ-xC5Gg
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:47:06.492935
---

# 【安全更新】微软4月安全更新多个产品高危漏洞通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tZgxn6yByvL3uxzSmzokrjbeDxyicIPHUSaowzdGTDM07oYicDNRPP2wXlvqvibymOOhpzeqGMapHEaIcZdLblCLFkseksmyVjNJcIRffI6pm4/0?wx_fmt=jpeg)

# 【安全更新】微软4月安全更新多个产品高危漏洞通告

原创

NS-CERT
NS-CERT

绿盟科技CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**通告编号:NS-2026-0009**

2026-04-15

|  |  |
| --- | --- |
| **TA****G：** | **安全更新、Windows、Office、Visual Studio、SQL Server** |
| **漏洞危害：** | **攻击者利用本次安全更新中的漏洞，可造成权限提升、远程代码执行等** |
| **版本：** | **1.0** |

**1**

**漏洞概述**

4月15日，绿盟科技CERT监测到微软发布4月安全更新补丁，修复了165个安全问题，涉及Windows、Microsoft Office、Microsoft SQL Server、Microsoft Visual Studio、Microsoft .NET Framework、Azure等广泛使用的产品，其中包括权限提升、远程代码执行等高危漏洞类型。

本月微软月度更新修复的漏洞中，严重程度为关键的漏洞有8个，重要漏洞有154个，中危漏洞有2个，低危漏洞有1个。其中包括1个已检测到在野利用的漏洞：

Microsoft SharePoint Server欺骗漏洞（CVE-2026-32201）

请相关用户尽快更新补丁进行防护，完整漏洞列表请参考附录。

参考链接：

https://msrc.microsoft.com/update-guide/releaseNote/2026-Apr

**SEE MORE →**

**2****重点漏洞简述**

根据产品流行度和漏洞重要性筛选出此次更新中包含影响较大的漏洞，请相关用户重点进行关注：

**Microsoft SharePoint Server欺骗漏洞（CVE-2026-32201）：**

Microsoft SharePoint Server中存在欺骗漏洞，由于SharePoint Server 的输入验证不当，未经身份验证的攻击者可通过网络进行欺骗攻击，从而查看部分敏感信息并篡改已公开的信息。该漏洞存在在野利用，CVSS评分9.0。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32201

**Windows Kerberos权限提升漏洞（CVE-2026-27912）：**

Windows Kerberos中存在权限提升漏洞，由于Kerberos服务票据请求的验证过程中存在授权不当问题，经过身份验证的攻击者可通过操纵Kerberos票据字段绕过安全检查，在相邻网络上提升权限，可能获取域管理员权限。CVSS评分8.0。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-27912

**Remote Desktop Client远程代码执行漏洞（CVE-2026-32157）：**

Remote Desktop Client中存在远程代码执行漏洞，由于Remote Desktop Client在处理RDP连接参数时存在释放后重用（Use After Free）问题，未经身份验证的攻击者可通过诱导用户连接到恶意RDP服务器，从而在客户端主机上执行任意代码。CVSS评分8.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32157

**Windows TCP/IP远程代码执行漏洞（CVE-2026-33827）：**

Windows TCP/IP中存在远程代码执行漏洞，由于Windows TCP/IP中使用共享资源时的同步机制不当，未经身份验证的攻击者可通过网络利用此漏洞执行任意代码。CVSS评分8.1。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33827

**Windows Shell安全功能绕过漏洞（CVE-2026-32225）：**

Windows Shell中存在安全功能绕过漏洞，由于Windows Shell中的保护机制失败，未经身份验证的攻击者可通过诱导受害者打开特制的.lnk文件，从而绕过SmartScreen安全防护，导致未经授权的操作或访问。CVSS 评分8.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32225

**Windows Internet Key Exchange (IKE) Service Extensions远程代码执行漏洞（CVE-2026-33824）：**

Windows Internet Key Exchange (IKE) Service Extensions中存在远程代码执行漏洞，由于Windows IKE扩展中存在双重释放（Double Free）问题，未经身份验证的攻击者可通过向启用了IKEv2Windows系统发送特制的数据包，从而实现远程代码执行。CVSS评分9.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33824

**Microsoft Defender权限提升漏洞（CVE-2026-33825）******：****

Microsoft Defender中存在权限提升漏洞，由于Microsoft Defender中的访问控制粒度不足，经过身份验证的本地攻击者可将权限提升到SYSTEM。CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33825

**Windows Active Directory远程代码执行漏洞（CVE-2026-33826）：**

Windows Active Directory中存在远程代码执行漏洞，由于Windows Active Directory中的输入验证不当，经过身份验证的攻击者可通过相邻网络向RPC主机发送特制的RPC调用，从而实现远程代码执行。CVSS评分8.0。

官方通告链接：

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33826

**3****影响范围**

以下为部分重点关注漏洞的受影响产品版本，其他漏洞影响产品范围请参阅官方通告链接。

|  |  |
| --- | --- |
| 漏洞编号 | 受影响产品版本 |
| CVE-2026-32201 | Microsoft SharePoint Server Subscription Edition  Microsoft SharePoint Enterprise Server 2016  Microsoft SharePoint Server 2019 |
| CVE-2026-27912 | Windows Server 2012 R2 (Server Core installation)  Windows Server 2012 R2  Windows Server 2012 (Server Core installation)  Windows Server 2012  Windows Server 2016 (Server Core installation)  Windows Server 2016  Windows Server 2025  Windows Server 2022, 23H2 Edition (Server Core installation)  Windows Server 2025 (Server Core installation)  Windows Server 2022 (Server Core installation)  Windows Server 2022  Windows Server 2019 (Server Core installation)  Windows Server 2019 |
| CVE-2026-32157 | Windows Server 2012 R2 (Server Core installation)  Windows Server 2012 R2  Windows Server 2012 (Server Core installation)  Windows Server 2012  Windows Server 2016 (Server Core installation)  Windows Server 2016  Windows 10 Version 1607 for x64-based Systems  Windows 10 Version 1607 for 32-bit Systems  Windows Server 2025  Windows 11 Version 24H2 for x64-based Systems  Windows 11 Version 24H2 for ARM64-based Systems  Windows Server 2022, 23H2 Edition (Server Core installation)  Windows 11 Version 23H2 for x64-based Systems  Windows 11 Version 23H2 for ARM64-based Systems  Windows 11 Version 25H2 for x64-based Systems  Windows 11 Version 25H2 for ARM systems  Windows Server 2025 (Server Core installation)  Windows 10 Version 22H2 for 32-bit Systems  Windows 10 Version 22H2 for ARM64-based Systems  Windows 10 Version 22H2 for x64-based Systems  Windows 10 Version 21H2 for x64-based Systems  Windows 10 Version 21H2 for ARM64-based Systems  Windows 10 Version 21H2 for 32-bit Systems  Windows Server 2022 (Server Core installation)  Windows Server 2022  Remote Desktop client for Windows Desktop  Windows Server 2019 (Server Core installation)  Windows Server 2019  Windows 10 Version 1809 for x64-based Systems  Windows 10 Version 1809 for 32-bit Systems  Windows App Client for Windows Desktop  Windows 11 version 26H1 for x64-based Systems  Windows 11 Version 26H1 for ARM64-based Systems |
| CVE-2026-33827  CVE-2026-32225 | Windows 10 Version 22H2 for ARM64-based Systems  Windows 10 Version 22H2 for x64-based Systems  Windows 10 Version 21H2 for x64-based Systems  Windows 10 Version 21H2 for ARM64-based Systems  Windows 10 Version 21H2 for 32-bit Systems  Windows Server 2022 (Server Core installation)  Windows Server 2022  Windows Server 2019 (Server Core installation)  Windows Server 2019  Windows 10 Version 1809 for x64-based Systems  Windows 10 Version 1809 for 32-bit Systems  Windows Server 2025 (Server Core installation)  Windows 10 Version 22H2 for 32-bit Systems  Windows Server 2012 R2 (Server Core installation)  Windows Server 2012 R2  Windows Server 2012 (Server Core installation)  Windows Server 2012  Windows Server 2016 (Server Core installation)  Windows Server 2016  Windows 10 Version 1607 for x64-based Systems  Windows 10 Version 1607 for 32-bit Systems  Windows 11 Version 26H1 for ARM64-based Systems  Windows 11 version 26H1 for x64-based Systems  Windows Server 2025  Windows 11 Version 24H2 for x64-based Systems  Windows 11 Version 24H2 for ARM64-based Systems  Windows Server 2022, 23H2 Edition (Server Core installation)  Windows 11 Version 23H2 for x64-based Systems  Windows 11 Version 23H2 for ARM64-based Systems  Windows 11 Version 25H2 for x64-based Systems  Windows 11 Version 25H2 for ARM systems |
| CVE-2026-33824 | Windows Server 2016 (Server Core installation)  Windows Server 2016  Windows 10 Version 1607 for x64-based Systems  Windows 10 Version 1607 for 32-bit Systems  Windows 11 Version 26H1 for ARM64-based Systems  Windows 11 version 26H1 for x64-based Systems  Windows Server 2025  Windows 11 Version 24H2 for x64-based Systems  Windows 11 Version 24H2 for ARM64-based Systems  Windows Server 2022, 23H2 Edition (Server Core installation)  Windows 11 Version 23H2 for x64-based Systems  Windows 11 Version 23H2 for ARM64-based Systems  Windows 11 Version 25H2 for x64-based Systems  Windows 11 Version 25H2 for ARM systems  Windows Server 2025 (Server Core installation)  Windows 10 Version 22H2 for 32-bit Systems  Windows 10 Version 22H2 for ARM64-based Systems  Windows 10 Version 22H2 for x64-based Systems  Windows 10 Version 21H2 for x64-based Systems  Windows 10 Version 21H2 for ARM64-based Systems  Windows 10 Version 21H2 for 32-bit Systems  Windows Server 2022 (Server Core installation)  Windows Server 2022  Windows Server 2019 (Server Core installation)  Windows Server 2019  Windows 10 Version 1809 for x64-based Systems  Windows 10 Version 1809 for 32-bit Systems |
| CVE-2026-33825 | Microsoft Defender Antimalware Platform |
| CVE-2026-33826 | Windows Server 2012 R2 (Server Core installation)  Windows Server 2012 R2  Windows Server 2016 (Server Core installation)  Windows Server 201...