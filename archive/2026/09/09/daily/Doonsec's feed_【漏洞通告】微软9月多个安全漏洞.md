---
title: 【漏洞通告】微软9月多个安全漏洞
url: https://mp.weixin.qq.com/s/p-HXXlx6SY2XkVH3R5hLqA
source: Doonsec's feed
date: 2026-09-09
fetch_date: 2026-09-10T06:46:16.088193
---

# 【漏洞通告】微软9月多个安全漏洞

# 【漏洞通告】微软9月多个安全漏洞

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## **一****、漏洞概述**

2026年9月9日，启明星辰安全应急响应中心（VSRC）监测到微软发布了9月安全更新，本次更新修复了973个漏洞，涵盖特权提升、远程代码执行、信息泄露等多种漏洞类型。漏洞级别分布如下：113个严重级别漏洞，860个重要级别漏洞（漏洞级别依据微软官方数据）。

其中，60个漏洞被微软标记为“更可能被利用”及“检测利用情形”，表明这些漏洞存在较高的利用风险，建议优先修复以降低潜在安全威胁。

|  |  |  |
| --- | --- | --- |
| CVE-ID | CVE 标题 | 漏洞级别 |
| CVE-2026-68846 | Windows 内核特权提升漏洞 | 重要 |
| CVE-2026-68876 | Windows 程序兼容性助手服务特权提升漏洞 | 重要 |
| CVE-2026-68880 | Windows Win32k 特权提升漏洞 | 重要 |
| CVE-2026-68884 | Windows 内核特权提升漏洞 | 重要 |
| CVE-2026-69274 | Windows Win32k 特权提升漏洞 | 重要 |
| CVE-2026-69277 | Microsoft 本地安全机构 (LSA) 服务器特权提升漏洞 | 重要 |
| CVE-2026-69301 | Windows Win32k 特权提升漏洞 | 重要 |
| CVE-2026-69305 | Microsoft Windows Search 组件特权提升漏洞 | 重要 |
| CVE-2026-69310 | Windows DNS 特权提升漏洞 | 重要 |
| CVE-2026-69337 | Windows 注册表特权提升漏洞 | 重要 |
| CVE-2026-69364 | Windows 打印后台处理程序组件特权提升漏洞 | 重要 |
| CVE-2026-69366 | Windows 内核特权提升漏洞 | 重要 |
| CVE-2026-69385 | Windows TCP/IP 特权提升漏洞 | 重要 |
| CVE-2026-69391 | Windows 代理基础结构服务特权提升漏洞 | 重要 |
| CVE-2026-69406 | Windows 内核信息泄露漏洞 | 重要 |
| CVE-2026-69436 | Windows 错误报告特权提升漏洞 | 重要 |
| CVE-2026-69450 | Windows 错误报告特权提升漏洞 | 重要 |
| CVE-2026-69451 | Windows Management Instrumentation (WMI) 特权提升漏洞 | 重要 |
| CVE-2026-69459 | Windows Power Dependency Coordinator 特权提升漏洞 | 重要 |
| CVE-2026-69460 | Windows 现代设备管理 (MDM) 特权提升漏洞 | 重要 |
| CVE-2026-69466 | Windows 内核特权提升漏洞 | 重要 |
| CVE-2026-69467 | Microsoft 图形组件特权提升漏洞 | 重要 |
| CVE-2026-69473 | Windows 内核特权提升漏洞 | 重要 |
| CVE-2026-69478 | Windows 设备关联服务特权提升漏洞 | 重要 |
| CVE-2026-69498 | Windows Win32k 特权提升漏洞 | 重要 |
| CVE-2026-69525 | 远程桌面服务远程执行代码漏洞 | 重要 |
| CVE-2026-69541 | 虚拟硬盘(VHD) 微型端口驱动程序特权提升漏洞 | 重要 |
| CVE-2026-69585 | Microsoft Windows Search 组件特权提升漏洞 | 重要 |
| CVE-2026-69600 | Microsoft Windows Search 组件特权提升漏洞 | 重要 |
| CVE-2026-69605 | Microsoft 安装服务特权提升漏洞 | 重要 |
| CVE-2026-69623 | Windows HTTP 打印提供程序远程代码执行漏洞 | 重要 |
| CVE-2026-69676 | Windows Kerberos 远程代码执行漏洞 | 严重 |
| CVE-2026-69714 | Windows 设备关联服务特权提升漏洞 | 重要 |
| CVE-2026-69723 | Windows 内核信息泄露漏洞 | 重要 |
| CVE-2026-69730 | Windows DNS Server Remote Code Execution Vulnerability | 严重 |
| CVE-2026-69757 | Windows TCP/IP 特权提升漏洞 | 重要 |
| CVE-2026-69777 | Microsoft DHCP 客户端特权提升漏洞 | 重要 |
| CVE-2026-69779 | Windows Win32k 特权提升漏洞 | 重要 |
| CVE-2026-69832 | Win32k 信息泄露漏洞 | 重要 |
| CVE-2026-69852 | Windows Routing and Remote Access Service (RRAS) 远程代码执行漏洞 | 严重 |
| CVE-2026-69854 | Spring Cloud Azure 特权提升 漏洞 | 严重 |
| CVE-2026-69857 | Azure Cosmos DB 欺骗漏洞 | 严重 |
| CVE-2026-69911 | Microsoft Windows Search 组件特权提升漏洞 | 重要 |
| CVE-2026-69921 | Windows 打印后台处理程序组件特权提升漏洞 | 重要 |
| CVE-2026-70289 | Windows Win32k 特权提升漏洞 | 重要 |
| CVE-2026-70342 | WinSock 的 Windows 辅助功能驱动程序特权提升漏洞 | 重要 |
| CVE-2026-70562 | Windows 音频服务特权提升漏洞 | 重要 |
| CVE-2026-70583 | Windows Core Messaging Elevation of Privilege Vulnerability | 重要 |
| CVE-2026-70585 | NFS ONCRPC XDR Driver 的 Windows 服务远程代码执行漏洞 | 严重 |
| CVE-2026-71340 | Windows 文件历史记录服务特权提升漏洞 | 重要 |
| CVE-2026-71343 | Windows Remote Access Connection Manager Remote Code Execution Vulnerability | 重要 |
| CVE-2026-72936 | Windows SMB 客户端远程执行代码漏洞 | 重要 |
| CVE-2026-72940 | Windows Schannel 远程代码执行漏洞 | 重要 |
| CVE-2026-72957 | Windows 部署服务远程代码执行漏洞 | 严重 |
| CVE-2026-77500 | Windows 设备关联服务特权提升漏洞 | 重要 |
| CVE-2026-78454 | Windows CD-ROM 驱动程序 信息泄露 漏洞 | 重要 |
| CVE-2026-80093 | Windows Cloud Files Mini Filter Driver 特权提升漏洞 | 重要 |
| CVE-2026-81963 | Windows Update Stack 特权提升漏洞 | 重要 |
| CVE-2026-83501 | Windows 基于虚拟化的安全性 (VBS) 信息泄露漏洞 | 严重 |
| CVE-2026-85880 | Windows 高级本地过程调用 (ALPC) 特权提升漏洞 | 重要 |

**微软****9****月更新修复的完整漏洞列表如下****：**

|  |  |  |
| --- | --- | --- |
| CVE-ID | CVE 标题 | 漏洞级别 |
| CVE-2026-47297 | Microsoft SQL Server 远程执行代码漏洞 | 重要 |
| CVE-2026-50349 | WinSock 的 Windows 辅助功能驱动程序特权提升漏洞 | 重要 |
| CVE-2026-55007 | Microsoft Exchange Server 远程执行代码漏洞 | 重要 |
| CVE-2026-56172 | Windows VHD 微型端口驱动程序特权提升漏洞 | 重要 |
| CVE-2026-56177 | Windows Server 特权提升漏洞 | 重要 |
| CVE-2026-56198 | Microsoft Trace Data Helper Elevation of Privilege Vulnerability | 重要 |
| CVE-2026-57098 | Microsoft Remote Desktop 适用于 Windows 的应用 信息泄露 漏洞 | 重要 |
| CVE-2026-57099 | ASP.NET Core 拒绝服务漏洞 | 重要 |
| CVE-2026-58599 | HEVC Video 扩展程序远程执行代码漏洞 | 严重 |
| CVE-2026-58600 | HEVC 视频扩展特权提升漏洞 | 重要 |
| CVE-2026-58611 | Xbox 游戏服务特权提升漏洞 | 重要 |
| CVE-2026-58649 | .NET 信息泄漏漏洞 | 重要 |
| CVE-2026-62694 | Windows Installer 特权提升漏洞 | 重要 |
| CVE-2026-62697 | Windows 推送通知特权提升漏洞 | 重要 |
| CVE-2026-62706 | Microsoft Windows Media Foundation 远程执行代码漏洞 | 重要 |
| CVE-2026-62744 | Microsoft Windows Media Foundation 远程执行代码漏洞 | 重要 |
| CVE-2026-62759 | Windows 网络登录 (Netlogon) 欺骗漏洞 | 重要 |
| CVE-2026-62762 | Windows Active Directory 域服务拒绝服务漏洞 | 重要 |
| CVE-2026-62801 | Microsoft PowerShell 安全功能绕过漏洞 | 重要 |
| CVE-2026-62804 | Microsoft Word 远程执行代码漏洞 | 重要 |
| CVE-2026-62810 | Active Directory Certificate Services (AD CS) 特权提升 漏洞 | 重要 |
| CVE-2026-62813 | Windows Active Directory 域服务远程代码执行漏洞 | 重要 |
| CVE-2026-62895 | Azure Arc SQL Server 扩展 特权提升 漏洞 | 重要 |
| CVE-2026-62906 | Microsoft Discovery Studio 信息泄露 漏洞 | 严重 |
| CVE-2026-62916 | Microsoft Entra ID 特权提升漏洞 | 严重 |
| CVE-2026-63523 | Skype for Business 欺骗漏洞 | 重要 |
| CVE-2026-64918 | Microsoft Office 欺骗漏洞 | 重要 |
| CVE-2026-65669 | Microsoft SQL Server 特权提升漏洞 | 严重 |
| CVE-2026-65772 | Microsoft Dynamics 365（本地）远程执行代码漏洞 | 严重 |
| CVE-2026-65812 | Android 版 Microsoft Teams 信息披露漏洞 | 重要 |
| CVE-2026-65818 | Power Automate 特权提升漏洞 | 严重 |
| CVE-2026-66302 | Skype for Business 远程执行代码漏洞 | 严重 |
| CVE-2026-66303 | Skype for Business 和 Lync 拒绝服务漏洞 | 重要 |
| CVE-2026-66304 | Skype for Business 信息泄漏漏洞 | 重要 |
| CVE-2026-66305 | Skype for Business 欺骗漏洞 | 重要 |
| CVE-2026-66306 | Skype for Business 信息泄漏漏洞 | 重要 |
| CVE-2026-66307 | Skype for Business 和 Lync 拒绝服务漏洞 | 重要 |
| CVE-2026-66308 | Skype for Business 和 Lync 拒绝服务漏洞 | 重要 |
| CVE-2026-66814 | Microsoft SQL Server 特权提升漏洞 | 重要 |
| CVE-2026-66816 | Microsoft SQL Server 安全功能绕过漏洞 | 重要 |
| CVE-2026-66818 | Microsoft SQL Server 特权提升漏洞 | 重要 |
| CVE-2026-66819 | Microsoft SQL Server 特权提升漏洞 | 重要 |
| CVE-2026-66820 | SQL 服务器特权提升漏洞 | 重要 |
| CVE-2026-67368 | Microsoft SQL Server 特权提升漏洞 | 重要 |
| CVE-2026-67369 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-67370 | Microsoft SQL Server 特权提升漏洞 | 重要 |
| CVE-2026-67373 | Microsoft SQL Server 远程执行代码漏洞 | 重要 |
| CVE-2026-67376 | Microsoft SQL Server 拒绝服务漏洞 | 重要 |
| CVE-2026-67378 | Microsoft SQL Server 远程执行代码漏洞 | 严重 |
| CVE-2026-67379 | Microsoft SQL Server 远程执行代码漏洞 | 重要 |
| CVE-2026-67380 | Microsoft SQL Server 远程执行代码漏洞 | 重要 |
| CVE-2026-67381 | Microsoft SQL Server 特权提升漏洞 | 重要 |
| CVE-2026-67383 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-67384 | Microsoft SQL Server 远程执行代码漏洞 | 重要 |
| CVE-2026-67385 | Microsoft SQL Server 远程执行代码漏洞 | 重要 |
| CVE-2026-67386 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-67388 | Microsoft SQL Server 远程执行代码漏洞 | 重要 |
| CVE-2026-67389 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-67390 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-67393 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-67624 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-67629 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-67630 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-67631 | Microsoft SQL Server 远程执行代码漏洞 | 严重 |
| CVE-2026-67633 | Microsoft SQL Server 拒绝服务漏洞 | 重要 |
| CVE-2026-67636 | Microsoft SQL Server 远程执行代码漏洞 | 严重 |
| CVE-2026-67638 | Microsoft SQL Server 远程执行代码漏洞 | 重要 |
| CVE-2026-67639 | Microsoft SQL Server 远程执行代码漏洞 | 重要 |
| CVE-2026-67641 | Microsoft SQL Server 拒绝服务漏洞 | 重要 |
| CVE-2026-67642 | Microsoft SQL Server 远程执行代码漏洞 | 重要 |
| CVE-2026-67643 | Microsoft SQL Server 远程执行代码漏洞 | 严重 |
| CVE-2026-67645 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-67648 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-68775 | Microsoft SQL Server 远程执行代码漏洞 | 重要 |
| CVE-2026-68776 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-68777 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-68778 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-68779 | Microsoft SQL Server 信息泄露漏洞 | 重要 |
| CVE-2026-68780 | Microsoft SQL Server ...