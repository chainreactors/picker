---
title: 横向移动：远程启用 RDP
url: https://mp.weixin.qq.com/s/XUPjcyEDauQ2h9B3rnzLmw
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:24:15.775173
---

# 横向移动：远程启用 RDP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0HFuPNFAf8P8mNia1uKkyQqJLQ23IYBjOicorSR57jsPR6XtpE2VNbukX0ok2d5LFDaDcXw6HHIiaicCQnCdsPAWr0PAY52dSF2icRA/0?wx_fmt=jpeg)

# 横向移动：远程启用 RDP

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

本文通过实际操作演示了多种在 Windows Server 2019 域控制器 (DC.ignite.local, 192.168.1.11) 上远程启用 RDP 的实际技术，并展示了如何使用 Kali Linux 上提供的各种 RDP 客户端连接到该域控制器。每种技术都利用了不同的工具和访问途径，充分展现了攻击者的攻击手段之丰富。

介绍

远程桌面协议 (RDP) 是一项强大的 Windows 服务，它允许通过网络以图形方式远程访问目标计算机。在红队演练和渗透测试中，攻击者在获得初始凭据或哈希值后，通常需要通过启用 RDP 并进行连接来扩大其操作范围——即使目标计算机上的 RDP 服务最初处于禁用状态。

第一阶段：侦察——确认 RDP 已禁用

Nmap端口扫描

此次行动首先使用 Nmap 进行有针对性的扫描，以确定域控制器上端口 3389（默认 RDP 端口）的当前状态。

```
nmap-p3389 192.168.1.11
```

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0F6CxaqOrfbexjxJTg0vFWganNqNgbBIBCqvH0AgRDbFcTkGibZEyZSegT7m0cXFhEHMABrZKQaNEhkzXnXHeBibUyDicGNovZsmw/640?wx_fmt=png&from=appmsg)

这证实了目标域控制器上的远程桌面服务已禁用。接下来，我们将使用几种不同的远程技术来启用 RDP。

第二阶段：解锁 RDP——6 种利用技术

方法一 — 通过 WMI 使用 NetExec (nxc) RDP 模块

攻击者使用 NetExec（一种现代网络凭证验证和利用框架）通过 SMB 协议上的专用模块和有效凭证在目标设备上启用 RDP。

```
nxcsmb 192.168.1.11-uadministrator-pIgnite@987 -M rdp -o ACTION=enable
```

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0Hyx95HRIBv8vLWm6agr6QRXVWyMEr5mSrXUfz6s93WrtCSevz1Rd3T6rqtZvEXL5ckfCE08ibojLSR8GWfzwrtufYSOyzYNF0o/640?wx_fmt=png&from=appmsg)

NetExec 以域管理员身份通过 SMB（端口 445）在域控制器上进行身份验证，然后使用内置的 RDP 模块并启用 ACTION=enable。之后，NetExec 通过 WMI (ncacn\_ip\_tcp) 启用 RDP，并确认 RDP 端口已设置为 3389。

验证1——3389 端口现已开放

后续的 Nmap 扫描确认 DC.ignite.local 上的 3389/tcp 端口已打开。ms-wbt-server 服务正在积极监听，验证了方法 1 已成功在目标上激活远程桌面服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0G1WEOnaNrWUWzjjRmWQ0mnkQ2CzeM5RbZXXfUL17jibEof5fvMGvwPFXEBSYxsk9qYo7E0hwm51EDh9n68DgiafKogPDBHhu7CM/640?wx_fmt=png&from=appmsg)

方法2——通过 wmiexec 使用哈希传递的 NetExec

在明文密码不可用但 NTLM 哈希值已知的场景中，攻击者利用 NetExec 的 -x 标志进行哈希传递 (PtH) 身份验证，借助以下命令通过 wmiexec 远程执行注册表命令：

```
nxc smb 192.168.1.11 -u Administrator -H 32196B56FFE6F45E294117B91A83BF38 -x 'reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0GrmtlJclltu4Lg7VVicK9CBicnAtGuD5000xfReffnvZic5uaaOy8hUTfKGde7MSIfibt5neSTSFOwUkC9LibyFCwES4s75vmjQIc0/640?wx_fmt=png&from=appmsg)

NetExec 身份验证成功（Null Auth：True，SMBv1：None），并通过 wmiexec 执行注册表命令。终端服务器路径下的注册表项 fDenyTSConnections 的值被设置为 0，从而直接启用远程桌面。操作成功完成。

技术 3 — Impacket-reg

Impacket 的 reg 工具允许攻击者通过 SMB 协议直接与远程目标的 Windows 注册表交互，从而提供了一种干净可靠的方法来修改注册表项。因此，要修改这些注册表项，我们将使用以下命令：

```
impacket-reg ignite.local/administrator:Ignite@987@192.168.1.11add -keyName "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" -v fDenyTSConnections -vt REG_DWORD -vd 0
```

Impacket-reg 以管理员身份进行身份验证，并直接向注册表中的 fDenyTSConnections 键写入 DWORD 值 0。该工具会显示键路径、值类型 (REG\_DWORD) 和新数据 (0) 来确认操作。此技术无需交互式 shell，完全通过 SMB 协议运行。

方法 4 — 使用注册表命令的 Impacket-psexec

Impacket 的 psexec 模块将服务二进制文件上传到目标系统，创建并启动 Windows 服务，并提供一个完全交互式的系统级 shell——攻击者可以直接从该 shell 执行以下注册表命令：

```
impacket-psexec ignite.local/administrator:Ignite@987@192.168.1.11
```

```
regadd"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0H7iajS8kNqF7y094BVwBKdoJZvFjKeZtnePpxibib15CG55CMXz8iaKCmZLWCy4mG1QBVRApCjge1t6CfCH0RSdWibP0JZlvE54Vjw/640?wx_fmt=png&from=appmsg)

该技术非常强大，因为它以 NT AUTHORITY\SYSTEM 身份运行，绕过了所有用户级别的限制。

技术 5 — 使用 PowerShell 的 Evil-WinRM

Evil-WinRM 是一个基于 Ruby 的攻击型 WinRM shell，专为渗透测试而设计。它通过 Windows 远程管理 (WinRM) 连接到 5985 端口，并借助以下命令在目标系统上建立完整的 PowerShell 会话：

```
evil-winrm-i 192.168.1.11-uadministrator-pIgnite@987
```

```
Set-ItemProperty -Path"HKLM:\System\CurrentControlSet\Control\Terminal Server" -Name"fDenyTSConnections" -Value0
```

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0EdCGmGjrWFWHy3NMfTkiayHleqPlKiaSObA2dc6fxlyMt9CvaOwY4Iic7Kkic3JWeklJdWtiaeYdwxhhWhMFPsAQ7QjPqzt4KXgWEk/640?wx_fmt=png&from=appmsg)

PowerShell cmdlet 会在后台静默应用更改。Evil-WinRM 提供了一个持久的交互式 shell，支持文件传输、脚本加载和绕过功能，使其成为 Active Directory 环境中常用的后渗透工具。

技术 6 — Samba 网络 RPC 注册表

Kali Linux 自带的 Samba net 工具提供基于 RPC 的注册表操作，无需任何第三方工具，只需使用标准的 Samba 套件即可。我们将使用以下命令来按需使用此工具：

```
net rpc registry setvalue 'HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server''fDenyTSConnections' dword '0' -U ignite.local/administrator%'Ignite@987' -S 192.168.1.11
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0GyrNyLghia2SzUngfEvhibyO8micicOn0ILqRBg08ZJMaFYdUHiaicQsThNZaczGv8cywPlWQ3KRFAbf5UQF4I4HjAiaUypZAspibJNrM/640?wx_fmt=png&from=appmsg)

这条单一命令通过 RPC 使用域凭据进行身份验证，并将 fDenyTSConnections DWORD 值直接设置为 0。它利用了 Samba 工具链的 RPC 注册表接口——一种隐蔽且轻量级的方法，不会上传二进制文件或创建服务，从而在目标系统上留下最小的痕迹。

技术 7 — Metasploit post/windows/manage/enable\_rdp

Metasploit Framework 的后渗透模块提供了一种自动化的、菜单驱动的方式，可以在活动的 Meterpreter 会话中启用 RDP。该模块如下：

```
use post/windows/manage/enable_rdp
setsession1
exploit
```

该模块检测到 RDP 已禁用并自动启用。它配置终端服务自动启动，在本地防火墙中打开 3389 端口，并记录一个清理资源文件以用于事后恢复。此技术非常适合在 Metasploit 工作流程中工作且已在目标主机上建立 Meterpreter 会话的操作人员。

第三阶段：通过 RDP 连接 — 三种客户端选项

通过上述任一方法成功启用 RDP 后，攻击者即可连接到域控制器的桌面。Kali Linux 支持多种 RDP 客户端，每种客户端的功能各不相同。

RDP客户端1 — rdesktop（基本连接）

```
rdesktop 192.168.1.11
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0EQwdZZVZZmEQYtylYbttD6d7JNoMdJZWh7eKMjzuT9gz82fOOv8uACtCGgYNqgXx3Y31Ehp9By3ZVrUX5a15OLyianObyalCdM/640?wx_fmt=png&from=appmsg)

rdesktop 是一款轻量级的开源 RDP 客户端，可在大多数 Linux 系统上使用。连接成功后会弹出关于 NLA（网络级身份验证）的证书警告——rdesktop 会绕过此警告，并渲染完整的 Windows Server 2019 标准评估版桌面。

RDP 客户端 2 — xfreerdp3，支持哈希传递协议

xfreerdp3 是 Kali Linux 上功能最丰富的 RDP 客户端，支持哈希传递 (/pth)、剪贴板共享、驱动器重定向和压缩等高级选项。因此，我们将使用以下命令连接到远程桌面：

```
xfreerdp3 /compression +auto-reconnect /u:administrator /pth:32196B56FFE6F45E294117B91A83BF38 /v:192.168.1.11 +clipboard
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0EqQNxbExvkrVRwskOtDaibICuMLYvPdHbiaqGkEWlwAgImxd16gJ5cbOEwFibUAS1NX1xD8L20PpMEItbruZfM7I2jxnGHqoH2t4/640?wx_fmt=png&from=appmsg)

直接使用 NTLM 哈希值无需输入明文密码。连接成功后，Windows 服务器管理器仪表板会打开，确认域控制器访问权限，并显示 AD CS 和 AD DS 角色。此方法尤其强大，因为即使不知道明文密码也能正常工作。

RDP 客户端 3 — Remmina（GUI 客户端）

Remmina 是一款功能齐全的图形化远程桌面客户端，它通过简洁美观的图形用户界面 (GUI) 支持 RDP、VNC、SSH 等多种协议。启动 Remmina 并使用域凭据配置目标 IP 地址 (192.168.1.11) 后，客户端即可与域控制器 (DC) 建立干净的 RDP 会话，并显示 Windows 服务器管理器仪表板。Remmina 非常适合需要稳定、易用的 GUI 以进行长时间访问或在目标上执行详细管理任务的操作人员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0EpMTcp5Ib1Z0diajyhMEYQ7Vn1JmtRSvdx5v7keLdkSlicM1c1HVgVqLVt0RIVeunsj7eFDpNI8RtAPPzOrVwnBgs6YicTNcrqus/640?wx_fmt=png&from=appmsg)

缓解策略

七种远程桌面协议 (RDP) 启用技术利用了凭证窃取、薄弱的协议（SMB/WMI/WinRM/RPC）以及不完善的网络控制。实施以下针对性防御措施，以加强纵深防御：

凭据加固：部署 LAPS/Windows LAPS，在已加入域的系统之间轮换本地管理员密码，使从一台主机窃取的哈希值在其他主机上失效（抵消技术 1-6 的影响）。强制使用 15 个字符以上的复杂密码、最小权限原则以及 PAW/分层管理员权限，以限制凭据泄露。

NTLM 阻止：通过 GPO 限制 NTLM（阻止 v1，审核 v2），在 VBS 中启用 Credential Guard 进行哈希隔离，并将管理员添加到受保护用户组以防止哈希传递（阻止技术 2，阶段 3 PtH RDP）。

SMB 限制：在防火墙/边界阻止 TCP/UDP 445；禁用 SMBv1；在 DC/服务器上强制执行 SMB 签名；通过 GPO 隐藏 ADMIN$/IPC$ 共享（在技术 1-4 中停止 NetExec、impacket-reg/psexec）。

WMI 控制：防火墙 DCOM（135 + 高端口）；收紧 WMI 命名空间 ACL（wmimgmt.msc）；使用 WDAC/AppLocker 阻止 WMI 脚本执行；监视 EID 4688 以查找远程 cmd/PowerShell 生成（阻止技术 1-2）。

禁用 WinRM：运行 Disable-PSRemoting -Force；阻止 5985/5986；启用完整的 PowerShell 日志记录（脚本/模块/转录）和受限语言模式（中和技术 5 Evil-WinRM）。

RPC 注册表锁定：通过 GPO 禁用 RemoteRegistry 服务；限制 HKLM\SYSTEM\CurrentControlSet\Control\SecurePipeServers\Winreg ACL；监视 EID 5039（阻止技术 6 Samba net rpc）。

RDP 网络限制： GPO 防火墙 TCP 3389 仅限已批准的网关；部署带 MFA 的 RD 网关；强制执行 NLA；将“允许通过 RDP 登录”限制为远程桌面用户组（使第 3 阶段 RDP 无效）。

服务/有效载荷预防：部署 EDR 以检测 Meterpreter；对来自 ADMIN$/TEMP 的新服务发出 EID 7045/4697 警报；使用 WDAC 阻止未签名的 psexec 二进制文件（阻止技术 7、技术 4）。

零信任分段：将数据中心隔离在 VLAN 中；阻止工作站到数据中心的管理端口；应用 ZTNA/微分段进行按流认证（打破扁平网络枢纽）。

检测规则： SIEM 前向安全/系统/PowerShell/WMI 日志；对 EID 4657（fDenyTSConnections 更改）、4624/4648（SMB/RDP 登录）、4698/7045（任务/服务）发出警报；使用此链进行搜索。

结论

本文证明，攻击者只要拥有有效的凭据或密码哈希值，就可以 通过至少七种不同的技术在 Windows Server 域控制器上启用 RDP   。 这些技术包括 NetExec 模块、Impacket 工具、Evil-WinRM PowerShell、原生 Samba RPC 和 Metasploit 后渗透模块。

一旦 RDP 激活，三个不同的 Kali Linux 客户端——rdesktop、xfreerdp3 和 Remmina——都能成功提供交互式图形会话，包括通过哈希传递协议 (Pass-the-Hash) 进行会话，而无需使用明文密码。组织必须通过强制执行网络分段、凭据轮换、部署 LAPS 和 RDP 网关策略来强化其环境，以检测...