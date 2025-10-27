---
title: 【漏洞预警】微软2月多个安全漏洞
url: https://mp.weixin.qq.com/s?__biz=MzAxNDM3NTM0NQ==&mid=2657045247&idx=1&sn=e99542169f15d3b8c755b7bfb2a43a24&chksm=803faa21b74823375d0d9b7dc7937a621552a92123135e18e6bc1a5987271e4d11b22bb01f70&scene=58&subscene=0#rd
source: SecPulse安全脉搏
date: 2023-02-17
fetch_date: 2025-10-04T06:52:52.971782
---

# 【漏洞预警】微软2月多个安全漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5u08OUQmyqflgviarQP4ibV0eqiba65iakAwhU8TI1vMXib51XTlhHBg4xIrb2fB08b4brtxZcLG2W6GY3zCHeVRzJQ/0?wx_fmt=jpeg)

# 【漏洞预警】微软2月多个安全漏洞

安识科技

SecPulse安全脉搏

![](https://mmbiz.qpic.cn/mmbiz_png/8ku0nsiagdhZ9kibMY9pUOGdBncITwAvicQeeuiaicSCVicKic2vwDia14DHgndlQTwHzB8M0PlShruddeHfkeorBjdotg/640?wx_fmt=png)

1. **通告信息**

![](https://mmbiz.qpic.cn/mmbiz_png/PiapXScWtibK67XvgLiaz6hQibAvcPPHRqNZGYltRKU2WaibdTo9wtQafErQMNA34QBtGgQiazJibwGLlwwN2srxqxapw/640?wx_fmt=png)

2023年2月14日，微软发布了2月安全更新，本次更新修复了包括3个0 day漏洞在内的75个安全漏洞（不包括Microsoft Edge和其它漏洞），其中有9个漏洞评级为“严重”。

对此，安识科技建议广大用户及时升级到安全版本,并做好资产自查以及预防工作，以免遭受黑客攻击。

##

![](https://mmbiz.qpic.cn/mmbiz_png/8ku0nsiagdhZ9kibMY9pUOGdBncITwAvicQeeuiaicSCVicKic2vwDia14DHgndlQTwHzB8M0PlShruddeHfkeorBjdotg/640?wx_fmt=png)

2. **漏洞概述**

![](https://mmbiz.qpic.cn/mmbiz_png/PiapXScWtibK67XvgLiaz6hQibAvcPPHRqNZGYltRKU2WaibdTo9wtQafErQMNA34QBtGgQiazJibwGLlwwN2srxqxapw/640?wx_fmt=png)

本次发布的安全更新涉及.NET and Visual Studio、.NET Framework、Microsoft Defender for Endpoint、Microsoft Dynamics、Microsoft Exchange Server、Microsoft Graphics Component、Microsoft Office OneNote、Microsoft Office SharePoint、Microsoft Office Word、SQL Server、Visual Studio、Windows Active Directory、Windows iSCSI、Windows Protected EAP (PEAP)和Windows Win32K等多个产品和组件。

本次修复的漏洞中，涉及提权漏洞、远程代码执行漏洞、信息泄露漏洞、拒绝服务漏洞、安全功能绕过漏洞和欺骗漏洞等。

微软本次共修复了3个被积极利用的0 day漏洞（指漏洞已被公开披露或被积极利用但没有可用的官方修复程序），如下：

CVE-2023-21823：Windows Graphics Component 远程代码执行漏洞

Windows 图形组件存在远程代码执行漏洞，该漏洞的CVSSv3评分为7.8，成功利用该漏洞可以获得 SYSTEM 权限。该漏洞暂未公开披露，但已检测到漏洞利用，Microsoft Store（已启用自动更新）将自动更新受影响的客户。

CVE-2023-21715：Microsoft Publisher 安全功能绕过漏洞

Microsoft Publisher存在安全功能绕过漏洞，该漏洞的CVSSv3评分为7.3，成功利用该漏洞的威胁者可以绕过用于阻止不受信任或恶意文件的Office宏策略，但利用该漏洞需要用户交互（如通过诱使受害者从网站下载并打开特制文件）。该漏洞暂未公开披露，但已检测到漏洞利用。

CVE-2023-23376：Windows Common Log File System Driver 特权提升漏洞

Windows 通用日志文件系统驱动程序存在特权提升漏洞，该漏洞的CVSSv3评分为7.8，成功利用该漏洞可以获得 SYSTEM 权限。该漏洞暂未公开披露，但已检测到漏洞利用。

本次安全更新中评级为严重的9个漏洞包括：

CVE-2023-21808：.NET 和 Visual Studio 远程代码执行漏洞

CVE-2023-21716：Microsoft Word 远程代码执行漏洞

该漏洞的CVSSv3评分为9.8，未经身份验证的威胁者可以发送包含 RTF Payload的恶意电子邮件，以获得在用于打开恶意文件的应用程序中执行命令的权限。注意，预览窗格是该漏洞的攻击媒介之一。

CVE-2023-21718：Microsoft SQL ODBC 驱动程序远程代码执行漏洞

CVE-2023-21815/ CVE-2023-23381：Visual Studio 远程代码执行漏洞

CVE-2023-21803：Windows iSCSI 发现服务远程代码执行漏洞

该漏洞的CVSSv3评分为9.8，启用 iSCSI Initiator 客户端应用程序的系统易受该漏洞影响，默认情况下，iSCSI Initiator 客户端应用程序被禁用，此状态下该漏洞无法被利用。

CVE-2023-21692/CVE-2023-21690：Microsoft Protected Extensible Authentication Protocol (PEAP) 远程代码执行漏洞

这些漏洞的CVSSv3评分均为9.8，未经身份验证的威胁者可以通过在网络上发送特制的恶意 PEAP 数据包来攻击 Microsoft Protected Extensible Authentication Protocol (PEAP) 服务器。

CVE-2023-21689：Microsoft Protected Extensible Authentication Protocol (PEAP) 远程代码执行漏洞

该漏洞的CVSSv3评分为9.8，利用该漏洞的非特权威胁者可以在任意或远程代码执行中以服务器帐户为目标，并尝试通过网络调用在服务器帐户的上下文中触发恶意代码。

微软2月更新涉及的完整漏洞列表如下：

|  |  |  |
| --- | --- | --- |
| CVE-ID | CVE 标题 | 严重性 |
| CVE-2023-21808 | .NET 和 Visual Studio 远程代码执行漏洞 | 严重 |
| CVE-2023-21716 | Microsoft Word 远程代码执行漏洞 | 严重 |
| CVE-2023-21718 | Microsoft SQL   ODBC 驱动程序远程代码执行漏洞 | 严重 |
| CVE-2023-21815 | Visual Studio 远程代码执行漏洞 | 严重 |
| CVE-2023-23381 | Visual Studio 远程代码执行漏洞 | 严重 |
| CVE-2023-21803 | Windows iSCSI 发现服务远程代码执行漏洞 | 严重 |
| CVE-2023-21692 | Microsoft   Protected Extensible Authentication Protocol (PEAP) 远程代码执行漏洞 | 严重 |
| CVE-2023-21690 | Microsoft   Protected Extensible Authentication Protocol (PEAP) 远程代码执行漏洞 | 严重 |
| CVE-2023-21689 | Microsoft   Protected Extensible Authentication Protocol (PEAP) 远程代码执行漏洞 | 严重 |
| CVE-2023-21722 | .NET Framework 拒绝服务漏洞 | 高危 |
| CVE-2023-23390 | 3D Builder 远程代码执行漏洞 | 高危 |
| CVE-2023-23377 | 3D Builder 远程代码执行漏洞 | 高危 |
| CVE-2023-23378 | 打印 3D 远程代码执行漏洞 | 高危 |
| CVE-2023-21777 | Azure App   Service on Azure Stack Hub 特权提升漏洞 | 高危 |
| CVE-2023-21703 | Azure Data Box 网关远程代码执行漏洞 | 高危 |
| CVE-2023-21564 | Azure DevOps 服务器跨站脚本漏洞 | 高危 |
| CVE-2023-21553 | Azure DevOps 服务器远程代码执行漏洞 | 高危 |
| CVE-2023-23382 | Azure 机器学习计算实例信息泄露漏洞 | 高危 |
| CVE-2023-21699 | Windows   Internet 存储名称服务 (iSNS) 服务器信息泄露漏洞 | 高危 |
| CVE-2023-21697 | Windows   Internet 存储名称服务 (iSNS) 服务器信息泄露漏洞 | 高危 |
| CVE-2023-21809 | Microsoft   Defender for Endpoint 安全功能绕过漏洞 | 高危 |
| CVE-2023-23379 | Microsoft   Defender for IoT特权提升漏洞 | 高危 |
| CVE-2023-21807 | Microsoft   Dynamics 365 (on-premises) 跨站脚本漏洞 | 高危 |
| CVE-2023-21573 | Microsoft   Dynamics 365 (on-premises) 跨站脚本漏洞 | 高危 |
| CVE-2023-21571 | Microsoft   Dynamics 365 (on-premises) 跨站脚本漏洞 | 高危 |
| CVE-2023-21572 | Microsoft   Dynamics 365 (on-premises) 跨站脚本漏洞 | 高危 |
| CVE-2023-21778 | Microsoft   Dynamics 统一服务台远程代码执行漏洞 | 高危 |
| CVE-2023-21570 | Microsoft   Dynamics 365 (on-premises) 跨站脚本漏洞 | 高危 |
| CVE-2023-21710 | Microsoft   Exchange Server 远程代码执行漏洞 | 高危 |
| CVE-2023-21707 | Microsoft   Exchange Server 远程代码执行漏洞 | 高危 |
| CVE-2023-21706 | Microsoft   Exchange Server 远程代码执行漏洞 | 高危 |
| CVE-2023-21529 | Microsoft   Exchange Server 远程代码执行漏洞 | 高危 |
| CVE-2023-21804 | Windows 图形组件特权提升漏洞 | 高危 |
| CVE-2023-21823 | Windows 图形组件远程代码执行漏洞 | 高危 |
| CVE-2023-21714 | Microsoft   Office 信息泄露漏洞 | 高危 |
| CVE-2023-21721 | Microsoft   OneNote 欺骗漏洞 | 高危 |
| CVE-2023-21715 | Microsoft Publisher   安全功能绕过漏洞 | 高危 |
| CVE-2023-21717 | Microsoft   SharePoint Server 特权提升漏洞 | 高危 |
| CVE-2023-21693 | Microsoft   PostScript 打印机驱动程序信息泄露漏洞 | 高危 |
| CVE-2023-21801 | Microsoft   PostScript 打印机驱动程序远程代码执行漏洞 | 高危 |
| CVE-2023-21684 | Microsoft   PostScript 打印机驱动程序远程代码执行漏洞 | 高危 |
| CVE-2023-21686 | Microsoft WDAC   OLE DB provider for SQL Server远程代码执行漏洞 | 高危 |
| CVE-2023-21685 | Microsoft WDAC   OLE DB provider for SQL Server远程代码执行漏洞 | 高危 |
| CVE-2023-21799 | Microsoft WDAC   OLE DB provider for SQL Server远程代码执行漏洞 | 高危 |
| CVE-2023-21802 | Windows Media 远程代码执行漏洞 | 高危 |
| CVE-2023-21806 | Power BI 报表服务器欺骗漏洞 | 高危 |
| CVE-2023-21713 | Microsoft SQL   Server 远程代码执行漏洞 | 高危 |
| CVE-2023-21528 | Microsoft SQL   Server 远程代码执行漏洞 | 高危 |
| CVE-2023-21705 | Microsoft SQL   Server 远程代码执行漏洞 | 高危 |
| CVE-2023-21568 | Microsoft SQL   Server 集成服务（VS扩展）远程代码执行漏洞 | 高危 |
| CVE-2023-21704 | Microsoft ODBC   Driver for SQL Server远程代码执行漏洞 | 高危 |
| CVE-2023-21566 | Visual Studio 特权提升漏洞 | 高危 |
| CVE-2023-21567 | Visual Studio 拒绝服务漏洞 | 高危 |
| CVE-2023-21816 | Windows Active   Directory 域服务 API 拒绝服务漏洞 | 高危 |
| CVE-2023-21688 | NT 操作系统内核提权漏洞 | 高危 |
| CVE-2023-23376 | Windows 通用日志文件系统驱动程序特权提升漏洞 | 高危 |
| CVE-2023-21812 | Windows 通用日志文件系统驱动程序特权提升漏洞 | 高危 |
| CVE-2023-21813 | Windows 安全通道拒绝服务漏洞 | 高危 |
| CVE-2023-21819 | Windows 安全通道拒绝服务漏洞 | 高危 |
| CVE-2023-21820 | Windows 分布式文件系统 (DFS) 远程代码执行漏洞 | 高危 |
| CVE-2023-21694 | Windows 传真服务远程代码执行漏洞 | 高危 |
| CVE-2023-21687 | HTTP.sys 信息泄露漏洞 | 高危 |
| CVE-2023-21800 | Windows   Installer 特权提升漏洞 | 高危 |
| CVE-2023-21700 | Windows iSCSI 发现服务拒绝服务漏洞 | 高危 |
| CVE-2023-21702 | Windows iSCSI 服务拒绝服务漏洞 | 高危 |
| CVE-2023-21811 | Windows iSCSI 服务拒绝服务漏洞 | 高危 |
| CVE-2023-21817 | Windows   Kerberos 特权提升漏洞 | 高危 |
| CVE-2023-21805 | Windows MSHTML 平台远程代码执行漏洞 | 高危 |
| CVE-2023-21797 | Microsoft ODBC 驱动程序远程代码执行漏洞 | 高危 |
| CVE-2023-21798 | Microsoft ODBC 驱动程序远程代码执行漏洞 | 高危 |
| CVE-2023-21695 | Microsoft   Protected Extensible Authentication Protocol (PEAP) 远程代码执行漏洞 | 高危 |
| CVE-2023-21701 | Microsoft Protected   Extensible Authentication Protocol (PEAP) 拒绝服务漏洞 | 高危 |
| CVE-2023-21691 | Microsoft   Protected Extensible Authentication Protocol (PEAP) 信息泄露漏洞 | 高危 |
| CVE-2023-21818 | Windows 安全通道拒绝服务漏洞 | 高危 |
| CVE-2023-21822 | Windows 图形组件特权提升漏洞 | 高危 |
| CVE-2023-23374 | Microsoft Edge（基于 Chromium）远程代码执行漏洞 | 中危 |
| CVE-2023-21794 | Microsoft Edge（基于 Chromium）欺骗漏洞 | 低危 |
| CVE-2023-21720 | Microsoft Edge（基于 Chromium）篡改漏洞 | 低危 |
| CVE-2019-15126 | MITRE：CVE-2019-15126 特定时间和手工制作的流量可能导致 WLAN 设备出现内部错误（与状态转换相关） | 未知 |

##

![](https://mmbiz.qpic.cn/mmbiz_png/8ku0nsiagdhZ9kibMY9pUOGdBncITwAvicQeeuiaicSCVicKic2vwDia14DHgndlQTwHzB8M0PlShruddeHfkeorBjdotg/640?wx_fmt=png)

3. **漏洞危害**

![](https://mmbiz.qpic.cn/mmbiz_png/PiapXScWtibK67XvgLiaz6hQibAvcPPHRqNZGYltRKU2WaibdTo9wtQafErQMNA34QBtGgQiazJibwGLlwwN2srxqxapw/640?wx_fmt=png)

攻击者可利用以上漏洞在目标系统中执行恶意命令以及非法操作。

##

![](https://mmbiz.q...