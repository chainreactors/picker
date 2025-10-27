---
title: 红队神器-Evil-Winrm详细使用指南 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17202253.html
source: 博客园 - 渗透测试中心
date: 2023-03-11
fetch_date: 2025-10-04T09:16:20.791938
---

# 红队神器-Evil-Winrm详细使用指南 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [红队神器-Evil-Winrm详细使用指南](https://www.cnblogs.com/backlion/p/17202253.html "发布于 2023-03-10 09:18")

### 前言

Evil-winrm
工具最初是由 Hackplayers 团队开发的。开发该工具的目的是尽可能简化渗透测试，尤其是在 Microsoft Windows 环境中。
Evil-winrm 使用 PowerShell 远程协议 (PSRP)，且系统和网络管理员经常使用Windows Remote
Management 协议进行上传和管理。 WinRM 是一种基于对防火墙友好的SOAP 协议，可通过 HTTP默认 端口 5985
与 HTTP 传输一起使用。有关 PowerShell 远程处理的更多信息，请参考访问 Microsoft 的官方网站。

<https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-psremoting?view=powershell-7.3>

### Evil-winrm介绍

Evil-winrm 是一款使用ruby 语言开发的开源工具。 该工具具有许多很酷的功能，包括使用纯文本密码远程登录、SSL
加密登录、 NTLM 哈希登录、密钥登录、文件传输、日志存储等功能。该开发工具的作者不断更新工具并长期维护更新。 使用
evil-winrm，我们可以获得远程主机的 PowerShell命令终端会话。 该工具已在Kali Linux系统中集成，但如果您想单独下载使用，则可以从其官方 git 存储库下载它。

下载链接：  [https: //github.com/Hackplayers/evil-winrm](https://github.com/Hackplayers/evil-winrm)

### Winrm 服务发现

正如上文提到的那样，如果在远程主机中启用了
Winrm 服务，则会联想到使用 evil-winrm 工具。 为了确认目标系统是否开启了winrm服务，我们可以使用 nmap 查找两个默认的 winrm 服务端口 5895 和
5896 是否打开。 从 nmap 扫描结果中，我们发现 winrm 服务已启用，因此我们可以使用 evil-winrm 工具进行登录并执行我们将在横向阶段探索的其他任务。

nmap -p   5985  ,  5986   192.168 .1 .19

### ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091812296-761646061.png)

### Evil-winrm  help命令帮助

要列出 evil-winrm 的所有可用的功能，我们可以简单地使用 -h 标志，它将列出所有带有描述的帮助命令。

```
evil-winrm -h
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091813306-1791686835.png)

### 使用纯文本密码登录

假设我们在账户枚举阶段获得了明文密码，并且注意到远程主机启用了 winrm 服务 ，我们可以使用 evil-winrm 在目标系统上进行远程会话，使用方法是带有-i 参数的目标系统IP地址、带有 -u 参数的目标系统用户名，带有-p参数的目标系统密码。 如下图所示，我们可以看到已经建立了一个远程 PowerShell 会话。

```
evil-winrm -i 192.168.1.19 -u administrator -p Ignite@987
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091814013-1687837742.png)

### 使用纯文本密码登录 - 启用 SSL

正如上文提到的那样，winrm 服务可通过 HTTP 协议传输流量，然后我们可以使用安全套接字层 (SSL) 功能来确保连接安全。 一旦启用 SSL 功能，我们的数据将通过加密的安全套接字层进行传输。使用 evil-winrm，我们可以使用-S 参数来建立与远程主机的安全传输的命令。

```
evil-winrm -i 192.168.1.19 -u administrator -p Ignite@987 -S
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091814913-1666008939.png)

### 使用 NTLM Hash 登录 - 通过哈希攻击

在内网渗透或解决任何与
Windows 权限提升和 Active Directory 利用相关的项目中，我们经常通过各种攻击方法获得 NTLM 哈希值。
如果我们在 Windows 内网环境中，我们可以利用 evil-winrm 通过执行传递哈希攻击来建立 PowerShell
会话，这样可以将哈希作为密码而不是使用纯文本密码进行远程登陆。 除此之外，这种攻击还支持其他协议。 传递哈希我们可以使用-H 参数 。

```
evil-winrm -i 192.168.1.19 -u administrator -H 32196B56FFE6F45E294117B91A83BF38
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091815919-322255289.png)

### 加载 Powershell 脚本

Evil-winrm 还提供了一项允许我们使用来自目标主机自带的powershell脚本的功能。 可以直接将脚本加载到内存中 ，我们可以使用带有-s 参数接目标系统的powershell脚本的相对路径 。 此外，该工具还提供了我们在导入任何脚本之前经常需要用到的 AMSI 功能。 在下面的示例中，我们将绕过 AMSI 功能，直接从系统中调用
Invoke-Mimiktz.ps1 脚本到目标主机中并将其加载到内存中。 之后，可以使用 mimikatz 命令。 本次出于演示目的，我们直接从缓存中转储了系统登陆凭据。 转储凭据后，我们可以再次使用获得的 NTLM 哈希进行哈希传递攻击。

<https://github.com/clymb3r/PowerShell/blob/master/Invoke-Mimikatz/Invoke-Mimikatz.ps1>

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091816698-1045152289.png)

```
evil-winrm -i 192.168.1.19 -u administrator -p Ignite@987 -s /opt/privsc/powershell
Bypass-4MSI
Invoke-Mimikatz.ps1
Invoke-Mimikatz
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091817650-2062958944.png)

### 使用 Evil-winrm 存储日志

此功能表示在获取远程会话后，将执行命令的日志保存到我们的本地系统中。 我们在平时做项目时，都需要攻击凭据，以便进行后续报告输出。可以使用 -l 参数将 将所有日志保存到我们的主机系统中 ，默认保存到 /root/evil-winrm-logs 目录中。在下面的示例中，我们可以同时使用了 ipconfig 命令并将命令输出信息保存到主机系统中。

```
evil-winrm -i 192.168.1.19 -u administrator -p Ignite@987 -l
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091818503-1169021792.png)

可以通过检查保存的日志内容来验证是否存将命令日志输出存储成功，可以看到已经存储了我们上文命令输出的日志信息。

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091819303-1925120427.png)

### 禁用远程完整路径功能

默认情况下，该工具带有远程完整路径功能，但如果我们希望禁用远程路径完整功能，我们可以 在命令中使用-N参数。 这取决于个人是否喜欢打开或关闭路径完整功能，但如果您对自动完整路功能感到满意，则可以随意使用其默认功能。

```
 evil-winrm -i 192.168.1.19 -u administrator -p Ignite@987 -N
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091820319-334324530.png)

### 禁用彩色界面

每当我们使用 evil-winrm 建立任何远程会话时，都会生成一个漂亮的彩色命令行界面。 尽管如此，如果我们希望禁用彩色界面功能，那么我们也可以在建立会话时使用-n 参数来禁用该功能。

```
 evil-winrm -i 192.168.1.19 -u administrator -p Ignite@987 -N
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091821002-86216428.png)

### 运行可执行文件

此功能旨在解决我们在进行 PowerShell 会话时在评估期间遇到的实时问题和困难，我们不能将其放到命令行中。 在这种情况下，我们希望能够在 evil-winrm 会话中运行 exe 可执行文件。 假设我们有一个要在目标系统中运行的可执行文件。

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091821739-279820440.png)

Hackplayers 团队再次设计了该工具并添加了一个额外的功能，可以在 evil-winrm PowerShell 会话中运行所有可执行文件。 同样，我们可以使用 -e 参数来执行 exe 可执行二进制文件。 在下面的示例中，其中 WinPEAS.exe 可执行文件存储在本地计算机 /opt/privsc目录中，并使用 附加功能（  evil-winrm 菜单中的Invoke-Binary命令 ）来运行它。 此功能允许我们执行在命令行 shell 中运行的任何 exe 二进制文件。

```
evil-winrm -i 192.168.1.19 -u administrator -p Ignite@987 -e /opt/privsc
Bypass-4MSI
menu
Invoke-Binary /opt/privsc/winPEASx64.exe
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091822804-340723136.png)

一旦我们设置了可执行文件路径，我们就可以使用我们希望在目标系统中运行的任何可执行文件。 在下面的示例中，我们调用 WinPEASx64.exe 并使用 evil-winrm 将其运行到目标系统中。

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091823704-102115081.png)

### 使用 Evil-winrm 进行服务查询

有时后渗透测试工具，无法检测到目标系统中运行的服务名称。
在这种情况下，我们可以使用 evil-winrm 来查找目标系统中运行的服务名称。 为此，我们可以再次转到菜单并使用服务功能。
它将列出所有运行程序主机的服务。

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091824661-464154626.png)

### 使用 Evil-winrm 进行文件传输

毫无疑问，evil-winrm 已尽最大努力使我们的使用尽可能地简单。 我们总是需要将文件从攻击机器传输到远程机器以执行其命令操作。 而 evil-winrm 工具提供的一项非常实用的功能，尤其是在我们面对目标系统中设置的出站流量规则以及我们将 evil-winrm 与代理一起使用时的情况下。 在下面的示例中，我们将/root目录中的notes.txt文件上传 到目标系统中。

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091825389-2110387118.png)

文件从目标系统下载到攻击者的机器上。 同样，我们可以使用下面命令进行下载：

```
download notes.txt /root/raj/notes.txt
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091826103-463726946.png)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230310091826844-1420175986.png)

### 从 Docker 使用 Evil-winrm

此工具也可以安装在
docker 中。 如果我们在安装到evil-winrm的docker中，那么我们也可以从docker中调用它。
它将...