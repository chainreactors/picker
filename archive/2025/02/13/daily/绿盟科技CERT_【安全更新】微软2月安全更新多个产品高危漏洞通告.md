---
title: 【安全更新】微软2月安全更新多个产品高危漏洞通告
url: https://mp.weixin.qq.com/s?__biz=Mzk0MjE3ODkxNg==&mid=2247488964&idx=1&sn=5c9f88f88b6352a5f7228166b197151c&chksm=c2c642cff5b1cbd9c7666dcb0fadf92f57c3869762078c3bc3e9e1feeb1b67141c5fbfcc5cfb&scene=58&subscene=0#rd
source: 绿盟科技CERT
date: 2025-02-13
fetch_date: 2025-10-06T20:35:40.304047
---

# 【安全更新】微软2月安全更新多个产品高危漏洞通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VvfsuOanecpBVDdTuBibVxm8bndrInnhw83IqUIVKic49CeM03MuIMqK7ZVQh8fViadUMeCNfQHj3MtBa0sXX2Uvw/0?wx_fmt=jpeg)

# 【安全更新】微软2月安全更新多个产品高危漏洞通告

原创

NS-CERT

绿盟科技CERT

**通告编号:NS-2025-0007**

2025-02-12

|  |  |
| --- | --- |
| **TA****G：** | **安全更新、Windows、Microsoft Office、Azure、Apps、Microsoft Visual Studio** |
| **漏洞危害：** | **攻击者利用本次安全更新中的漏洞，可造成权限提升、远程代码执行等** |
| **版本：** | **1.0** |

**1**

**漏洞概述**

2月12日，绿盟科技CERT监测到微软发布2月安全更新补丁，修复了63个安全问题，涉及Windows、Microsoft Office、Azure、Apps、Microsoft Visual Studio等广泛使用的产品，其中包括权限提升、远程代码执行等高危漏洞类型。

本月微软月度更新修复的漏洞中，严重程度为关键（Critical）的漏洞有4个，重要（Important）漏洞有56个。其中包括2个已检测到在野利用的漏洞：

Windows Storage权限提升漏洞（CVE-2025-21391）

Windows Ancillary Function Driver for WinSock权限提升漏洞（CVE-2025-21418）

请相关用户尽快更新补丁进行防护，完整漏洞列表请参考附录

参考链接：

https://msrc.microsoft.com/update-guide/en-us/releaseNote/2025-Feb

**SEE MORE →**

**2****重点漏洞简述**

根据产品流行度和漏洞重要性筛选出此次更新中包含影响较大的漏洞，请相关用户重点进行关注：

**Windows辅助功能驱动程序的WinSock权限提升漏洞（CVE-2025-21418）：**

Windows辅助功能驱动程序的WinSock中存在权限提升漏洞，由于Winsock的辅助函数驱动程序存在边界错误，经过身份验证的本地攻击者可以触发堆缓冲区溢出，从而获得系统的SYSTEM权限。该漏洞已存在在野利用，CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-21418

**Windows存储权限提升漏洞（CVE-2025-21391）：**

Windows存储中存在权限提升漏洞，由于Windows存储中的不正确链接解析，本地攻击者可以在目标系统上以SYSTEM权限执行代码，删除任意文件。该漏洞已存在在野利用，CVSS评分7.1。

官方通告链接：

https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-21391

**Windows轻量级目录访问协议(LDAP)远程代码执行漏洞（CVE-2025-21376）:**

Windows LDAP存在远程代码执行漏洞，未经身份验证的攻击者通过发送特制的LDAP请求，赢得竞争条件后可导致缓冲区溢出，在目标系统上执行任意代码。CVSS评分为8.1。

官方通告链接：

https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-21376

**Microsoft Excel远程代码执行漏洞（CVE-2025-21381）:**

Microsoft Excel存在远程代码执行漏洞，由于Microsoft Excel中的不可信指针解引用，远程攻击者通过诱导受害者打开特制的excel文件，从而在目标系统上执行任意代码。CVSS评分为7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-21381

**DHCP客户端服务远程代码执行漏洞（CVE-2025-21379）:**

DHCP客户端服务存在远程代码执行漏洞，由于DHCP客户端服务中的释放后重利用问题，本地网络中的攻击者可以进行中间人攻击，从而可在目标系统上以SYSTEM权限执行代码。CVSS评分为7.1。

官方通告链接：

https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-21379

**NTLM哈希泄露欺骗漏洞（CVE-2025-21377）:**

NTLM存在哈希泄露欺骗漏洞，攻击者可以通过欺骗用户点击特殊的链接来获得NTLMV2哈希，从而利用此哈希以该用户的身份登录系统。该漏洞已公开披露，CVSS评分为6.5。

官方通告链接：

https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-21377

**Microsoft SharePoint Server远程代码执行漏洞（CVE-2025-21400）:**

Microsoft SharePoint Server存在远程代码执行漏洞，由于Microsoft SharePoint服务器中的不当授权，攻击者可以欺骗受害者客户端连接到恶意服务器，从而在目标系统上执行任意代码。CVSS评分为8.0。

官方通告链接：

https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-21400

**Windows 磁盘清理工具权限提升漏洞（CVE-2025-21420）：**

Windows 磁盘清理工具中存在权限提升漏洞，由于Windows 磁盘清理工具中存在不正确链接解析，本地攻击者可以利用漏洞获得目标系统的SYSTEM权限。CVSS评分7.8。

官方通告链接：

https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-21420

**3****影响范围**

以下为部分重点关注漏洞的受影响产品版本，其他漏洞影响产品范围请参阅官方通告链接。

|  |  |
| --- | --- |
| **漏洞编号** | **受影响产品版本** |
| CVE-2025-21418  CVE-2025-21376  CVE-2025-21377 | Windows   Server 2025 (Server Core installation)  Windows   Server 2025  Windows   Server 2022, 23H2 Edition (Server Core installation)  Windows   Server 2022 (Server Core installation)  Windows   Server 2022  Windows   Server 2019 (Server Core installation)  Windows   Server 2019  Windows   Server 2016 (Server Core installation)  Windows   Server 2016  Windows   Server 2012 R2 (Server Core installation)  Windows   Server 2012 R2  Windows   Server 2012 (Server Core installation)  Windows   Server 2012  Windows   Server 2008 R2 for x64-based Systems Service Pack 1 (Server Core   installation)  Windows   Server 2008 R2 for x64-based Systems Service Pack 1  Windows   Server 2008 for x64-based Systems Service Pack 2 (Server Core installation)  Windows   Server 2008 for x64-based Systems Service Pack 2  Windows   Server 2008 for 32-bit Systems Service Pack 2 (Server Core installation)  Windows   Server 2008 for 32-bit Systems Service Pack 2  Windows   11 Version 24H2 for x64-based Systems  Windows   11 Version 24H2 for ARM64-based Systems  Windows   11 Version 23H2 for x64-based Systems  Windows   11 Version 23H2 for ARM64-based Systems  Windows   11 Version 22H2 for x64-based Systems  Windows   11 Version 22H2 for ARM64-based Systems  Windows   10 Version 22H2 for x64-based Systems  Windows   10 Version 22H2 for ARM64-based Systems  Windows   10 Version 22H2 for 32-bit Systems  Windows   10 Version 21H2 for x64-based Systems  Windows   10 Version 21H2 for ARM64-based Systems  Windows   10 Version 21H2 for 32-bit Systems  Windows   10 Version 1809 for x64-based Systems  Windows   10 Version 1809 for 32-bit Systems  Windows   10 Version 1607 for x64-based Systems  Windows   10 Version 1607 for 32-bit Systems  Windows   10 for x64-based Systems  Windows   10 for 32-bit Systems |
| CVE-2025-21391 | Windows Server 2016 (Server Core installation)  Windows Server 2016  Windows 10 Version 1607 for x64-based Systems  Windows 10 Version 1607 for 32-bit Systems  Windows 10 for x64-based Systems  Windows 10 for 32-bit Systems  Windows Server 2025  Windows 11 Version 24H2 for x64-based Systems  Windows 11 Version 24H2 for ARM64-based Systems  Windows Server 2022, 23H2 Edition (Server Core   installation)  Windows 11 Version 23H2 for x64-based Systems  Windows 11 Version 23H2 for ARM64-based Systems  Windows Server 2025 (Server Core installation)  Windows 10 Version 22H2 for 32-bit Systems  Windows 10 Version 22H2 for ARM64-based Systems  Windows 10 Version 22H2 for x64-based Systems  Windows 11 Version 22H2 for x64-based Systems  Windows 11 Version 22H2 for ARM64-based Systems  Windows 10 Version 21H2 for x64-based Systems  Windows 10 Version 21H2 for ARM64-based Systems  Windows 10 Version 21H2 for 32-bit Systems  Windows Server 2022 (Server Core installation)  Windows Server 2022  Windows Server 2019 (Server Core installation)  Windows Server 2019  Windows 10 Version 1809 for x64-based Systems  Windows 10 Version 1809 for 32-bit Systems |
| CVE-2025-21381 | Microsoft   Excel 2016 (64-bit edition)  Microsoft   Excel 2016 (32-bit edition)  Microsoft   Office LTSC for Mac 2024  Microsoft   Office LTSC 2024 for 64-bit editions  Microsoft   Office LTSC 2024 for 32-bit editions  Microsoft   Office LTSC 2021 for 32-bit editions  Microsoft   Office LTSC 2021 for 64-bit editions  Microsoft   Office LTSC for Mac 2021  Microsoft   365 Apps for Enterprise for 64-bit Systems  Microsoft   365 Apps for Enterprise for 32-bit Systems  Microsoft   Office 2019 for 64-bit editions  Microsoft   Office 2019 for 32-bit editions  Office   Online Server |
| CVE-2025-21379 | Windows   Server 2025  Windows   11 Version 24H2 for x64-based Systems  Windows   11 Version 24H2 for ARM64-based Systems  Windows   Server 2025 (Server Core installation) |
| CVE-2025-21400 | Microsoft   SharePoint Server Subscription Edition  Microsoft   SharePoint Server 2019  Microsoft   SharePoint Enterprise Server 2016 |
| CVE-2025-21420 | Windows   Server 2012 R2 (Server Core installation)  Windows   Server 2012  Windows   Server 2012 (Server Core installation)  Windows   Server 2012 R2  Windows   10 Version 1607 for x64-based Systems  Windows   Server 2016 (Server Core installation)  Windows   10 Version 1607 for 32-bit Systems  Windows   Server 2016  Windows   10 for x64-based Systems  Windows   11 Version 24H2 for ARM64-based Systems  Windows   11 Version 24H2 for x64-based Systems  Windows   10 for 32-bit Systems  Windows   Server 2025  Windows   Server 2022, 23H2 Edition (Server Core installation)  Windows   11 Version 23H2 for x64-based Systems  Windows   11 Version 23H2 for ARM64-based Systems  Windows   Server 2025 (Server Core installation)  Windows   10 Version 1809 for x64-based Systems  Windows   10 Version 22H2 for 32-bit Systems  Windows   10 Version 21H2 for 32-bit Systems  Windows   10 Version 1809 for 32-bit Systems  Windows   10 Version 22H2 for x64-based Systems  Windows   10 Version 22H2 for ARM64-based Systems  Windows   Server 2019  Windows   11 Version 22H2 for x64-based Systems  Windows   11...