---
title: 【漏洞通告】微软4月多个安全漏洞
url: https://mp.weixin.qq.com/s/Q418HNHiqYF9YMZDchtyAA
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:50:57.764062
---

# 【漏洞通告】微软4月多个安全漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4S21m309ZrxTcMlpbYcseZiaxvnqJT081rlPficO1ZQfGI1vOgKbRnmdc3bmib84ualK3Kglp8AV87hXfNIVUqicP5Up7dztRWZ8WTh6R8hib69g/0?wx_fmt=jpeg)

# 【漏洞通告】微软4月多个安全漏洞

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## **一****、漏洞概述**

2026年4月15日，启明星辰安全应急响应中心（VSRC）监测到微软发布了4月安全更新，本次更新修复了165个漏洞，涵盖特权提升、远程代码执行、信息泄露等多种漏洞类型。漏洞级别分布如下：8个严重级别漏洞，153个重要级别漏洞，3个中危级别漏洞，1个低危级别漏洞（漏洞级别依据微软官方数据）。

其中，20个漏洞被微软标记为“更可能被利用”及“检测利用情形”，表明这些漏洞存在较高的利用风险，建议优先修复以降低潜在安全威胁。

|  |  |  |
| --- | --- | --- |
| CVE-ID | CVE 标题 | 漏洞级别 |
| CVE-2026-26151 | 远程桌面欺骗漏洞 | 重要 |
| CVE-2026-0390 | UEFI 安全启动安全功能绕过漏洞 | 重要 |
| CVE-2026-26169 | Windows 内核内存信息泄露漏洞 | 重要 |
| CVE-2026-27906 | Windows Hello 安全功能绕过漏洞 | 重要 |
| CVE-2026-27908 | Windows TDI 转换驱动程序 (tdx.sys) 特权提升漏洞 | 重要 |
| CVE-2026-27909 | Windows Search 服务特权提升漏洞 | 重要 |
| CVE-2026-27913 | Windows BitLocker 安全功能绕过漏洞 | 重要 |
| CVE-2026-27914 | Microsoft 管理控制台特权提升漏洞 | 重要 |
| CVE-2026-27921 | Windows TDI 转换驱动程序 (tdx.sys) 特权提升漏洞 | 重要 |
| CVE-2026-32070 | Windows 通用日志文件系统驱动程序提升权限漏洞 | 重要 |
| CVE-2026-32075 | Windows UPnP 设备主机特权漏洞提升 | 重要 |
| CVE-2026-32093 | Windows FUNCTION 发现服务 (fdwsd.dll) 特权提升漏洞 | 重要 |
| CVE-2026-32152 | 桌面窗口管理器特权提升漏洞 | 重要 |
| CVE-2026-32154 | 桌面窗口管理器特权提升漏洞 | 重要 |
| CVE-2026-32162 | Windows COM 特权提升漏洞 | 重要 |
| CVE-2026-32202 | Windows Shell 欺骗漏洞 | 重要 |
| CVE-2026-32225 | Windows Shell 安全功能绕过漏洞 | 重要 |
| CVE-2026-33825 | Microsoft Defender 权限提升漏洞 | 重要 |
| CVE-2026-33826 | Windows Active Directory 远程代码执行漏洞 | 严重 |
| CVE-2026-32201 | Microsoft SharePoint Server 欺骗漏洞 | 重要 |

**微软****4****月更新修复的完整漏洞列表如下****：**

|  |  |  |
| --- | --- | --- |
| CVE-ID | CVE 标题 | 漏洞级别 |
| CVE-2026-0390 | UEFI 安全启动安全功能绕过漏洞 | 重要 |
| CVE-2026-20806 | Windows COM 服务器信息泄露漏洞 | 重要 |
| CVE-2026-20928 | Windows 恢复环境安全功能绕过漏洞 | 重要 |
| CVE-2026-20930 | Windows 管理服务特权提升漏洞 | 重要 |
| CVE-2026-20945 | Microsoft SharePoint Server 欺骗漏洞 | 重要 |
| CVE-2026-23653 | GitHub Copilot 及 Visual Studio Code 信息泄露漏洞 | 重要 |
| CVE-2026-23657 | Microsoft Word 远程执行代码漏洞 | 重要 |
| CVE-2026-23666 | .NET Framework 拒绝服务漏洞 | 严重 |
| CVE-2026-23670 | Windows 基于虚拟化的安全性 (VBS) 安全功能绕过漏洞 | 重要 |
| CVE-2026-25184 | AppLocker 筛选器驱动程序 (applockerfltr.sys) 特权提升漏洞 | 重要 |
| CVE-2026-26143 | Microsoft PowerShell 安全功能绕过漏洞 | 重要 |
| CVE-2026-26149 | Microsoft Power Apps 安全功能绕过漏洞 | 重要 |
| CVE-2026-26151 | 远程桌面欺骗漏洞 | 重要 |
| CVE-2026-26152 | Microsoft Cryptographic Services 特权提升漏洞 | 重要 |
| CVE-2026-26153 | Windows 加密文件系统 (EFS) 特权提升漏洞 | 重要 |
| CVE-2026-26154 | Windows Server 更新服务 (WSUS) 篡改漏洞 | 重要 |
| CVE-2026-26155 | Microsoft 本地安全认证子系统服务信息泄露漏洞 | 重要 |
| CVE-2026-26156 | Windows Hyper-V 远程执行代码漏洞 | 重要 |
| CVE-2026-26159 | 远程桌面授权服务特权提升漏洞 | 重要 |
| CVE-2026-26160 | 远程桌面授权服务特权提升漏洞 | 重要 |
| CVE-2026-26161 | Windows 传感器数据服务特权提升漏洞 | 重要 |
| CVE-2026-26162 | Windows OLE 特权提升漏洞 | 重要 |
| CVE-2026-26163 | Windows 内核特权提升漏洞 | 重要 |
| CVE-2026-26165 | Windows Shell 特权提升漏洞 | 重要 |
| CVE-2026-26166 | Windows Shell 特权提升漏洞 | 重要 |
| CVE-2026-26167 | Windows 推送通知特权提升漏洞 | 重要 |
| CVE-2026-26168 | WinSock 的 Windows 辅助功能驱动程序特权提升漏洞 | 重要 |
| CVE-2026-26169 | Windows 内核内存信息泄露漏洞 | 重要 |
| CVE-2026-26170 | PowerShell 权限提升漏洞 | 重要 |
| CVE-2026-26171 | .NET 拒绝服务漏洞 | 重要 |
| CVE-2026-26172 | Windows 推送通知特权提升漏洞 | 重要 |
| CVE-2026-26173 | WinSock 的 Windows 辅助功能驱动程序特权提升漏洞 | 重要 |
| CVE-2026-26174 | Windows Server Update Service (WSUS) 特权提升漏洞 | 重要 |
| CVE-2026-26175 | Windows 启动管理器安全功能绕过漏洞 | 重要 |
| CVE-2026-26176 | Windows 客户端 Caching 驱动程序 (csc.sys) 特权提升漏洞 | 重要 |
| CVE-2026-26177 | WinSock 的 Windows 辅助功能驱动程序特权提升漏洞 | 重要 |
| CVE-2026-26178 | Windows 高级光栅化平台权限提升漏洞 | 重要 |
| CVE-2026-26179 | Windows 内核特权提升漏洞 | 重要 |
| CVE-2026-26180 | Windows 内核特权提升漏洞 | 重要 |
| CVE-2026-26181 | Microsoft 代理文件系统特权提升漏洞 | 重要 |
| CVE-2026-26182 | WinSock 的 Windows 辅助功能驱动程序特权提升漏洞 | 重要 |
| CVE-2026-26183 | 远程访问管理服务/API（RPC 服务器）特权提升漏洞 | 重要 |
| CVE-2026-26184 | Windows 投影文件系统特权提升漏洞 | 重要 |
| CVE-2026-27906 | Windows Hello 安全功能绕过漏洞 | 重要 |
| CVE-2026-27907 | Windows 储存空间控件特权提升漏洞 | 重要 |
| CVE-2026-27908 | Windows TDI 转换驱动程序 (tdx.sys) 特权提升漏洞 | 重要 |
| CVE-2026-27909 | Windows Search 服务特权提升漏洞 | 重要 |
| CVE-2026-27910 | Windows Installer 特权提升漏洞 | 重要 |
| CVE-2026-27911 | Windows 用户界面核心特权提升漏洞 | 重要 |
| CVE-2026-27912 | Windows Kerberos 特权提升漏洞 | 重要 |
| CVE-2026-27913 | Windows BitLocker 安全功能绕过漏洞 | 重要 |
| CVE-2026-27914 | Microsoft 管理控制台特权提升漏洞 | 重要 |
| CVE-2026-27915 | Windows UPnP 设备主机特权漏洞提升 | 重要 |
| CVE-2026-27916 | Windows UPnP 设备主机特权漏洞提升 | 重要 |
| CVE-2026-27917 | Windows WFP-NDIS 轻量级筛选器驱动程序 (wfpwfs.sys) 特权提升漏洞 | 重要 |
| CVE-2026-27918 | Windows Shell 特权提升漏洞 | 重要 |
| CVE-2026-27919 | Windows UPnP 设备主机特权漏洞提升 | 重要 |
| CVE-2026-27920 | Windows UPnP 设备主机特权漏洞提升 | 重要 |
| CVE-2026-27921 | Windows TDI 转换驱动程序 (tdx.sys) 特权提升漏洞 | 重要 |
| CVE-2026-27922 | WinSock 的 Windows 辅助功能驱动程序特权提升漏洞 | 重要 |
| CVE-2026-27923 | 桌面窗口管理器特权提升漏洞 | 重要 |
| CVE-2026-27924 | 桌面窗口管理器特权提升漏洞 | 重要 |
| CVE-2026-27925 | Windows UPnP 设备主机信息泄露漏洞 | 重要 |
| CVE-2026-27926 | Windows Cloud Files Mini Filter Driver 特权提升漏洞 | 重要 |
| CVE-2026-27927 | Windows 投影文件系统特权提升漏洞 | 重要 |
| CVE-2026-27928 | Windows Hello 安全功能绕过漏洞 | 重要 |
| CVE-2026-27929 | Windows LUA 文件虚拟化筛选器驱动特权提升漏洞 | 重要 |
| CVE-2026-27930 | Windows GDI 信息泄露漏洞 | 重要 |
| CVE-2026-27931 | Windows GDI 信息泄露漏洞 | 重要 |
| CVE-2026-32068 | Windows 简单搜索和发现协议 (SSDP) 服务特权提升漏洞 | 重要 |
| CVE-2026-32069 | Windows 投影文件系统特权提升漏洞 | 重要 |
| CVE-2026-32070 | Windows 通用日志文件系统驱动程序提升权限漏洞 | 重要 |
| CVE-2026-32071 | Windows 本地安全机构子系统服务 (LSASS) 拒绝服务漏洞 | 重要 |
| CVE-2026-32072 | Active Directory 欺骗漏洞 | 重要 |
| CVE-2026-32073 | WinSock 的 Windows 辅助功能驱动程序特权提升漏洞 | 重要 |
| CVE-2026-32074 | Windows 投影文件系统特权提升漏洞 | 重要 |
| CVE-2026-32075 | Windows UPnP 设备主机特权漏洞提升 | 重要 |
| CVE-2026-32076 | Windows 储存空间控件特权提升漏洞 | 重要 |
| CVE-2026-32077 | Windows UPnP 设备主机特权漏洞提升 | 重要 |
| CVE-2026-32078 | Windows 投影文件系统特权提升漏洞 | 重要 |
| CVE-2026-32079 | Web 帐户管理器信息泄露漏洞 | 重要 |
| CVE-2026-32080 | Windows WalletService 特权提升漏洞 | 重要 |
| CVE-2026-32081 | 程序包目录信息泄露漏洞 | 重要 |
| CVE-2026-32082 | Windows 简单搜索和发现协议 (SSDP) 服务特权提升漏洞 | 重要 |
| CVE-2026-32083 | Windows 简单搜索和发现协议 (SSDP) 服务特权提升漏洞 | 重要 |
| CVE-2026-32084 | Windows 打印后台处理程序信息泄露漏洞 | 重要 |
| CVE-2026-32085 | 远程过程调用信息泄露漏洞 | 重要 |
| CVE-2026-32086 | Windows FUNCTION 发现服务 (fdwsd.dll) 特权提升漏洞 | 重要 |
| CVE-2026-32087 | Windows FUNCTION 发现服务 (fdwsd.dll) 特权提升漏洞 | 重要 |
| CVE-2026-32088 | Windows 生物识别服务安全功能绕过漏洞 | 重要 |
| CVE-2026-32089 | Windows 语音中介 API 特权提升漏洞 | 重要 |
| CVE-2026-32090 | Windows 语音中介 API 特权提升漏洞 | 重要 |
| CVE-2026-32091 | Microsoft 代理文件系统特权提升漏洞 | 重要 |
| CVE-2026-32093 | Windows FUNCTION 发现服务 (fdwsd.dll) 特权提升漏洞 | 重要 |
| CVE-2026-32149 | Windows Hyper-V 远程执行代码漏洞 | 重要 |
| CVE-2026-32150 | Windows FUNCTION 发现服务 (fdwsd.dll) 特权提升漏洞 | 重要 |
| CVE-2026-32151 | Windows Shell 信息泄露漏洞 | 重要 |
| CVE-2026-32152 | 桌面窗口管理器特权提升漏洞 | 重要 |
| CVE-2026-32153 | Windows 语音运行时特权提升漏洞 | 重要 |
| CVE-2026-32154 | 桌面窗口管理器特权提升漏洞 | 重要 |
| CVE-2026-32155 | 桌面窗口管理器特权提升漏洞 | 重要 |
| CVE-2026-32156 | Windows UPnP 设备主机远程代码执行漏洞 | 重要 |
| CVE-2026-32157 | 远程桌面客户端远程执行代码漏洞 | 严重 |
| CVE-2026-32158 | Windows 推送通知特权提升漏洞 | 重要 |
| CVE-2026-32159 | Windows 推送通知特权提升漏洞 | 重要 |
| CVE-2026-32160 | Windows 推送通知特权提升漏洞 | 重要 |
| CVE-2026-32162 | Windows COM 特权提升漏洞 | 重要 |
| CVE-2026-32163 | Windows 用户界面核心特权提升漏洞 | 重要 |
| CVE-2026-32164 | Windows 用户界面核心特权提升漏洞 | 重要 |
| CVE-2026-32165 | Windows 用户界面核心特权提升漏洞 | 重要 |
| CVE-2026-32167 | SQL 服务器特权提升漏洞 | 重要 |
| CVE-2026-32168 | Azure Monitor 代理特权提升漏洞 | 重要 |
| CVE-2026-32171 | Azure 逻辑应用特权提升漏洞 | 重要 |
| CVE-2026-32176 | SQL 服务器特权提升漏洞 | 重要 |
| CVE-2026-32178 | .NET 欺骗漏洞 | 重要 |
| CVE-2026-32181 | 已连接用户体验和遥测服务拒绝服务漏洞 | 重要 |
| CVE-2026-32183 | Windows 截图工具远程代码执行漏洞 | 重要 |
| CVE-2026-32184 | Microsoft 高性能计算 (HPC) 包特权提升漏洞 | 重要 |
| CVE-2026-32188 | Microsoft Excel 信息泄露漏洞 | 重要 |
| CVE-2026-32189 | Microsoft Excel 远程执行代码漏洞 | 重要 |
| CVE-2026-32190 | Microsoft Office 远程执行代码漏洞 | 严重 |
| CVE-2026-32192 | Azure Monitor 代理特权提升漏洞 | 重要 |
| CVE-2026-32195 | Windows 内核特权提升漏洞 | 重要 |
| CVE-2026-32196 | Windows 管理中心欺骗漏洞 | 重要 |
| CVE-2026-32197 | Microsoft Excel 远程执行代码漏洞 | 重要 |
| CVE-2026-32198 | Microsoft Excel 远程执行代码漏洞 | 重要 |
| CVE-20...