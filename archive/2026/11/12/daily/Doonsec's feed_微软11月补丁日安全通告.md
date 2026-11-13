---
title: 微软11月补丁日安全通告
url: https://mp.weixin.qq.com/s/OXOPldDJ-MZd-UZnVOfJlQ
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:56:44.685011
---

# 微软11月补丁日安全通告

# 微软11月补丁日安全通告

新华三盾山实验室
新华三盾山实验室

新华三主动安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7oZltmpdIfQtHsu8VXwvxnF5Ziawnm3sddBJHvCG6TKkvRVEwKSnrlL4oxMqhTzuAjqnFCib7yQUkIWDq7HiaK0A3N9FRVaw1AmrqBrv2q25UY/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/cxHLBjHNucEia1fxf7BXVmTnlyyNfibESUHdUIqSMmZ07kLv8T0I8dlLOBr1f7pZzHUbibIyugibpkniacVfh9VjmricpVoguxZl0h3pLDpNwRJpQ/640?from=appmsg)

PART 01

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5J8xDEKvNECN6iaMhFMDh8SaLGn9bQ6MphMsnqP43WJBETzEbmANP4Cm08iba5RTud3ThdmYsDH4nFXI958CgS0icTziayTW2TaT0ZahN8kYfMw/640?from=appmsg)

漏洞综述

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dqiaRPJtz5j68Eu8S4vpjTE29nKMv3AZGq8nYHIwbWpTOkDb9P3LnrOcxgXUyopjduvXZXpeqJqXsmqpXgWuaWUDvWUhl6qgaEPzkOcFX4xI/640?from=appmsg)

漏洞背景

2026年11月，新华三盾山实验室监测发现Microsoft官方发布了11月安全更新，共发布1094个漏洞的补丁信息。在此次更新的补丁中，有64个漏洞被微软标记为严重漏洞，且部分漏洞存在在野利用，由于影响较大，新华三盾山实验室建议广大用户及时做好资产自查以及预防工作，以免遭受黑客攻击。

重点漏洞

CVE-2026-124194 | Microsoft Outlook欺骗漏洞

该漏洞为本月唯一在野外被积极利用的零日漏洞。未经身份验证的攻击者可发送特制的消息文件，并诱导用户在受影响版本的Microsoft Outlook中打开。打开文件可能导致Outlook在未显示常规外部内容警告的情况下连接到攻击者控制的网络位置，从而泄露用户的NTLMv2身份验证哈希。攻击者可利用该哈希进行实时中继攻击以冒充用户身份访问其他服务，或通过离线破解获取用户凭据，进而获得对企业账户的未授权访问。CISA已将该漏洞列入已知被利用漏洞目录，要求在2026年11月24日前完成修复。利用该漏洞需要网络连接和用户交互，预览窗格不受影响，所有受支持的经典Outlook版本均已获得补丁。

微软严重等级：Important（重要）CVSS:3.1评分：6.5

CVE-2026-116928 | Windows搜索远程代码执行漏洞

Microsoft Windows搜索组件中存在越界写入漏洞，允许未经身份验证的攻击者通过网络执行任意代码。该漏洞可经由Exchange服务器触达：攻击者仅需发送带有特制附件的电子邮件，当Exchange自动对附件进行索引时即可触发漏洞，无需收件人执行任何操作，属于针对高价值目标的零点击代码执行漏洞，攻击复杂度低。由于执行上下文未明确，应假定以SYSTEM权限运行。补丁针对Windows操作系统而非Exchange本身，运行Exchange Subscription Edition的用户安装操作系统补丁即可获得保护。

微软严重等级：Critical（严重） CVSS:3.1评分：9.8

CVE-2026-119958 | Windows LDAP轻量级目录访问协议远程代码执行漏洞

Windows轻量级目录访问协议（LDAP）中存在越界写入漏洞，允许未经身份验证的攻击者通过网络发送特制的LDAP调用执行任意代码，无需用户交互。由于代码在LDAP服务上下文中执行，该漏洞可能造成严重破坏，对域控制器构成重大威胁，建议尽快测试并部署补丁。

微软严重等级：Critical（严重） CVSS:3.1评分：9.8

CVE-2026-119952 | Windows Schannel远程代码执行漏洞

Windows Schannel（微软对传输层安全协议TLS的实现）中存在可观察时序差异漏洞，允许未经身份验证的攻击者通过网络发送特制恶意数据包在目标系统上执行代码。利用该漏洞需满足特定条件，降低了被广泛利用的可能性，但微软评估其被利用可能性较高，表明开发可靠漏洞利用代码是可行的。多数情况下攻击者无需在同一子网内已有立足点，且不能排除在某些场景下实现SYSTEM权限预认证远程代码执行的可能性。

微软严重等级：Critical（严重） CVSS:3.1评分：8.1

CVE-2026-119990 | Azure OpenAI权限提升漏洞

Azure OpenAI中存在关键功能缺少身份验证的漏洞，允许未经身份验证的攻击者通过网络提升权限。

微软严重等级：Critical（严重） CVSS:3.1评分：9.8

CVE-2026-114160 | Azure Managed Grafana权限提升漏洞

Azure Managed Grafana中存在服务器端请求伪造（SSRF）漏洞，允许未经身份验证的攻击者通过网络提升权限。

微软严重等级：Critical（严重） CVSS:3.1评分：9.8

CVE-2026-109469 | Entra设备注册权限提升漏洞

Entra设备注册服务中存在通过用户控制密钥实现的授权绕过漏洞，允许未经身份验证的攻击者通过网络提升权限，CVSS评分达到满分10.0。

微软严重等级：Critical（严重） CVSS:3.1评分：10.0

CVE-2026-120003 | Microsoft Office远程代码执行漏洞

Microsoft Office中存在基于堆的缓冲区溢出漏洞，允许未经身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.8

CVE-2026-118148 | Active Directory域服务权限提升漏洞

Active Directory域服务中存在不当身份验证漏洞，允许经过身份验证的攻击者通过网络提升权限。

微软严重等级：Critical（严重） CVSS:3.1评分：7.5

CVE-2026-119382 | Windows TPM权限提升漏洞

Windows可信平台模块（TPM）中存在基于堆的缓冲区溢出漏洞，允许经过身份验证的攻击者在本地提升权限。

微软严重等级：Critical（严重） CVSS:3.1评分：7.8

CVE-2026-119961 | Windows Internet信息服务远程代码执行漏洞

Windows Internet信息服务（IIS）中存在使用共享资源的并发执行不当同步（竞态条件）漏洞，允许未经身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.1

CVE-2026-119957 | Windows远程桌面服务权限提升漏洞

Windows远程桌面服务中存在双重释放漏洞，允许经过身份验证的攻击者在本地提升权限。

微软严重等级：Critical（严重） CVSS:3.1评分：7.8

CVE-2026-119962 | Windows CredSSP远程代码执行漏洞

Windows凭据安全支持提供程序协议（CredSSP）中存在双重释放漏洞，允许未经身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.1

CVE-2026-119969 | 图形字体远程代码执行漏洞

图形字体组件中存在基于堆的缓冲区溢出漏洞，允许未经身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.8

CVE-2026-119966 | Windows图形内核权限提升漏洞

Windows图形内核中存在整数溢出或回绕漏洞，允许经过身份验证的攻击者在本地提升权限。

微软严重等级：Critical（严重） CVSS:3.1评分：7.5

CVE-2026-119951 | Windows部署服务远程代码执行漏洞

Windows部署服务中存在释放后使用漏洞，允许未经身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.1

CVE-2026-110043 | Microsoft Office Outlook远程代码执行漏洞

Microsoft Office Outlook中存在基于堆的缓冲区溢出漏洞，允许未经身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.8

CVE-2026-120005 | Microsoft PowerPoint远程代码执行漏洞

Microsoft Office PowerPoint中存在基于堆的缓冲区溢出漏洞，允许未经身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.8

CVE-2026-118702 & CVE-2026-118701 & CVE-2026-118292 & CVE-2026-118713 & CVE-2026-118711 & CVE-2026-118296 & CVE-2026-118730 & CVE-2026-118297 & CVE-2026-120788 & CVE-2026-120786 & CVE-2026-120789 & CVE-2026-124170 | Microsoft Office Excel远程代码执行漏洞（多个内存破坏类漏洞）

Microsoft Office Excel中存在多个内存破坏类漏洞，包括基于堆的缓冲区溢出、基于栈的缓冲区溢出、双重释放及释放后使用等，允许未经身份验证的攻击者通过网络执行任意代码。本月Excel为受影响漏洞数量最多的产品之一，建议用户优先部署相关补丁。

微软严重等级：Critical（严重） CVSS:3.1评分：8.8 & 8.8 & 8.8 & 8.8 & 8.8 & 8.8 & 8.8 & 8.8 & 8.8 & 8.8 & 8.8 & 7.5

CVE-2026-118146 | Active Directory域服务远程代码执行漏洞

Active Directory域服务中存在不当授权漏洞，允许经过身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.8

CVE-2026-118207 | Microsoft Exchange Server远程代码执行漏洞

Microsoft Exchange Server中存在不当输入验证漏洞，允许经过身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.8

CVE-2026-118737 | Windows远程过程调用运行时远程代码执行漏洞

Windows远程过程调用（RPC）运行时中存在加密签名验证不当漏洞，允许未经身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.1

CVE-2026-113825 | Windows SMB服务器网络传输驱动远程代码执行漏洞

Windows SMB服务器网络传输驱动（srvnet.sys）中存在使用共享资源的并发执行不当同步（竞态条件）漏洞，允许经过身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：7.5

CVE-2026-112967 | Windows Xbox Live网络服务远程代码执行漏洞

Windows Xbox Live网络服务中存在基于堆的缓冲区溢出漏洞，允许未经身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：9.8

CVE-2026-125136 | Windows网络连接设备自动设置服务远程代码执行漏洞

Windows网络连接设备自动设置服务中存在基于堆的缓冲区溢出漏洞，允许未经身份验证的攻击者通过相邻网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.8

CVE-2026-125137 | Windows图形内核权限提升漏洞

Windows图形内核中存在基于堆的缓冲区溢出漏洞，允许经过身份验证的攻击者在本地提升权限。

微软严重等级：Critical（严重） CVSS:3.1评分：7.8

CVE-2026-122194 | Microsoft Defender远程代码执行漏洞

Microsoft Defender中存在空指针解引用漏洞，允许未经身份验证的攻击者通过网络执行任意代码。

微软严重等级：Critical（严重） CVSS:3.1评分：8.8

PART 02

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5J8xDEKvNECN6iaMhFMDh8SaLGn9bQ6MphMsnqP43WJBETzEbmANP4Cm08iba5RTud3ThdmYsDH4nFXI958CgS0icTziayTW2TaT0ZahN8kYfMw/640?from=appmsg)

影响范围

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dqiaRPJtz5j68Eu8S4vpjTE29nKMv3AZGq8nYHIwbWpTOkDb9P3LnrOcxgXUyopjduvXZXpeqJqXsmqpXgWuaWUDvWUhl6qgaEPzkOcFX4xI/640?from=appmsg)

* .NET
* AMD Zen
* ASP.NET Core
* Active Directory Domain Services
* ActiveSyncProvider
* Aspire
* Azure CLI
* Azure Confidential Clean Rooms
* Azure CycleCloud
* Azure DevOps
* Azure DevOps Server
* Azure File Sync
* Azure Firmware
* Azure Front Door (AFD)
* Azure Local
* Azure Managed Grafana
* Azure NFS mount helper (aznfs)
* Azure OpenAI
* Azure Pipelines
* Connected Devices Platform Service (Cdpsvc)
* Data Deduplication
* Data Sharing Service Client
* Desktop Window Manager
* Entra Device Registration
* Github Copilot
* Graphic Fonts
* HEIF Image Extensions
* HID Parser Library
* HID class driver
* JDBC Driver for SQL Server
* Kernel Transaction Manager
* Mailslot File System
* Mariner
* Microsoft 365 Agents SDK
* Microsoft Account
* Microsoft ActiveX Installer Service
* Microsoft Authentication Library (MSAL) for Node.js
* Microsoft Authentication Library for JavaScript
* Microsoft Azure Kubernetes Service
* Microsoft Bluetooth Driver
* Microsoft Color Management
* Microsoft Configuration Manager
* Microsoft Defender
* Microsoft Dynamics 365 (on-premises)
* Microsoft Edge (Chromium-based)
* Microsoft Entra Private Network Connector
* Microsoft Exchange Server
* Microsoft Graph
* Microsoft Graphics Component
* Microsoft High Performance Computing (HPC) Pack
* Microsoft Input Method Editor (IME)
* Microsoft JScript
* Microsoft Local Security Authority Server (lsasrv)
* Microsoft MCP Gateway
* Microsoft Office
* Microsoft Office Access
* Microsoft Office Excel
* Microsoft Office Outlook
* Microsoft Office PowerPoint
* Microsoft Office SharePoint
* Microsoft Office Visio
* Microsoft Office Word
* Microsoft PowerShell
* Microsoft PowerShell Core
* Microsoft QUIC
* Microsoft Remote Registry Service
* Microsoft Streaming Service
* Microsoft Teams
* Microsoft Teams for Android
* Microsoft Trace Data Helper
* Microsoft WDAC OLE DB provider for SQL
* Microsoft Windows App Store
* Microsoft Windows Codecs Library
* Microsoft Windows Media Foundation
* Microso...