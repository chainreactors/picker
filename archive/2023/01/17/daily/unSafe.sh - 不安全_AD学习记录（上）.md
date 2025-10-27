---
title: AD学习记录（上）
url: https://buaq.net/go-145797.html
source: unSafe.sh - 不安全
date: 2023-01-17
fetch_date: 2025-10-04T04:02:05.873187
---

# AD学习记录（上）

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/8ee5f71cbad648f3b49ba45051957572.jpg)

AD学习记录（上）

本篇文章记录一下关于AD凭据获取和信息收集的方法，学习一下tryhackme的靶场的相关知识。有5种方法获取AD凭据，分别是NTLM 认证服务、LDAP 绑定凭证、认
*2023-1-16 19:52:0
Author: [xz.aliyun.com(查看原文)](/jump-145797.htm)
阅读量:44
收藏*

---

本篇文章记录一下关于AD凭据获取和信息收集的方法，学习一下tryhackme的靶场的相关知识。有5种方法获取AD凭据，分别是NTLM 认证服务、LDAP 绑定凭证、认证中继、Microsoft Deployment Toolkit、配置文件。

回到靶场，靶场利用的是LDAP密码回传攻击，设想这样一个场景，我们已经拿到了一台服务器的权限，在内网扫描的时候发现一台网络打印机的 Web 界面，如果如果提供弱口令或者其他方法进入打印机的管理页面，我们就可以修改打印机的配置，将此打印机的认证IP修改为我们的控制的IP，认证以明文的方式发送，我们就能直接获取域内的凭据了。以下为实际利用的情况：访问打印机服务：<http://printer.za.tryhackme.com/settings> 看上去我们知道了用户名，本次的密码被脱敏了，不过也许其他环境下查看一下HTML的源代码可能有惊喜。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193346-a346b450-9591-1.png)
修改DC的ip，让ip指向我们自己的机器，开启nc监听，看看是否有请求：
![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193402-acfef20a-9591-1.png)
很顺利，我们收到了打印机的请求，不过事情没这么简单，打印机会和DC进行LDAP的协商，所以我们没办法直接用nc就拿到账户密码，我们需要托管一个恶意的ldap服务器，并对其进行不安全的配置，以确保凭据以明文形式发送。

```
apt-get update && sudo apt-get -y install slapd ldap-utils && sudo systemctl enable slapd
```

执行完成后将会有如下选项，要我们设计ldap的管理员密码：
![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193530-e1c26094-9591-1.png)
完成安装，结果如下：
![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193541-e8622ede-9591-1.png)
使用dpkg-reconfigure -p low slapd重新配置ldap服务器：
1.选中否
![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193557-f1a9a1a2-9591-1.png)
2.域名填我们要攻击的域名，我这里就算是靶场的za.tryhackme.com
![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193629-0486f5b8-9592-1.png)
3.对组织填刚刚的域名，也是za.tryhackme.com
![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193640-0b3a1fd4-9592-1.png)
4.选中否，不会删除数据库
![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193652-127fb862-9592-1.png)

1. 在创建新数据库文件之前移动旧数据库文件，选中是
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193704-195e92b6-9592-1.png)
   6.设置完成
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193719-22c674fe-9592-1.png)
   7.我们需要新建一个文件，olcSaslSecProps.ldif写入以下内容。需要进一步解释一下，olcSaslSecProps字段指定SASL 安全属性，noanonymous的情况表示禁用匿名登录，minssf是指最小安全保护，如果等于0的，就是不保护。
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193733-2a9723fe-9592-1.png)
2. 我们启动服务ldapmodify -Y EXTERNAL -H ldapi:// -f ./olcSaslSecProps.ldif && sudo service slapd restart
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193746-329cde0e-9592-1.png)
   9.确保我们的ldap只支持明文，也就是如下supportedSASLMechanisms: PLAIN
   supportedSASLMechanisms: LOGIN，输入如下命令ldapsearch -H ldap:// -x -LLL -s base -b "" supportedSASLMechanisms
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193804-3d3228f6-9592-1.png)
   10.开启tcpdump抓取389的流量，另外关注域名字段附近的数据包，就能看到密码了。
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193816-449c729a-9592-1.png)
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116193822-47e62482-9592-1.png)

   **第三种，NTLM Relay攻击**
   在使用 Microsoft AD 的网络中，SMB 管理着从网络间文件共享到远程管理的一切事务，有两种不同的利用SMB进行NetNTLM身份验证利用的方法，第一种：由于NTLM Challenges可以被拦截，我们可以使用离线破解技术来恢复与NTLM Challenge相关的密码。然而，这个破解过程比直接破解 NTLM 哈希要慢得多。第二种：我们可以使用我们的控制的设备进行中间人攻击，在客户端和服务器之间中继 SMB 身份验证，这将为我们提供一个活动的身份验证会话和对目标服务器的访问。
   Responder 允许我们通过在 NetNTLM 身份验证期间使响应中毒来执行中间人攻击，诱使客户端与我们服务器交谈，而不是他们想要连接的实际服务器。在真实的LAN上，Responder 将尝试毒化任何检测到的本地链路多播名称解析 (LLMNR)、NetBIOS 名称服务器 (NBT-NS) 和 Web 代理自动发现 (WPAD) 请求。在大型 Windows 网络上，这些协议允许主机为同一本地网络上的所有主机执行自己的本地 DNS 解析。主机可以首先尝试通过发送 LLMNR 请求并查看是否有任何主机响应来确定他们正在寻找的主机是否在同一本地网络上，而不是使 DNS 服务器等网络资源负担过重。我的Kali机器已经连接到vpn上了,直接执行responder -I breached就可以开始投毒了：
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194003-83fb5a28-9592-1.png)
   稍等15分钟，成功拿到NTLM
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194019-8dfc62a6-9592-1.png)
   拿到NTLMv2-SSP Hash的值去hashcat破解，如下图：
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194041-9aea5752-9592-1.png)
   成破解出密码，如下图所示：
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194058-a530da74-9592-1.png)

   **第四种方法，利用Microsoft Deployment Toolkit**
   大型企业的管理员不可能拿着USB一个一个为每台电脑装软件，微软提供了Microsoft Deployment Toolkit(MDT)服务来管理企业资产。大型组织使用Preboot Execution Environment，即PXE （预引导执行环境）引导来允许连接到网络的新设备直接通过网络连接加载和安装操作系统，MDT 可用于创建、管理和托管 PXE 启动映像，下图是通信流程：
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194155-c6f2127c-9592-1.png)
   （1）用户发送DHCP发现（请求ip地址和pxe服务信息）
   （2）DHCP服务返回用户需要的ip和pex服务信息
   （3）用户发送DHCP请求，要分配ip地址给用户
   （4）服务返回DHCP承认
   （5）客户端执行启动服务发现
   （6）MDT服务返回承认消息，并发送PXR信息
   （7）客户端发送PXE boot请求
   （8）服务端通过TFTP返回PXE boot请求
   你可能会问拿到PXE的引导镜像有什么用？第一，可以注入提权向量，在PXE启动完成后获取管理员访问权限。第二可以抓取密码，获取AD内的账户密码。理论上我们按照通信流程就执行这种攻击，不过要让自己的设备加入进对方企业的域实在是太过苛刻（除了社工我想不出其他办法加入对面网络），我们就跳过前面的ip获取，假设我们已经拿到了一台服务器的权限，通过某种方法找到了MDT 服务器的 IP（也许是扫描，也许是历史文件等等），就像是如下靶场利用一般：
   这里是我们在靶场预先给好的ip地址，10.200.26.202和bcd文件名称，一般来说，我们需要把每个 BCD 文件都拿下来，检查配置情况，不过这里就只检查特定的bcd节约时间：
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194243-e36badaa-9592-1.png)
   使用tftp -i 10.200.26.202 GET "\Tmp\x64{8193F713-2552-4A20-9ABE-13A9443BAC58}.bcd" conf.bcd 获取
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194258-ec4d2124-9592-1.png)
   拿到.bcd文件之后我们需要确定系统镜像的位置，这里用到了一个powershell脚本PowerPXE.ps1 （[https://github.com/wavestone-cdt/powerpxe）](https://github.com/wavestone-cdt/powerpxe%EF%BC%89)
   依次执行即可获取系统路径
   powershell -executionpolicy bypass
   Import-Module .\PowerPXE.ps1
   Get-WimFile -bcdFile $BCDFile
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194313-f5478062-9592-1.png)
   拿到系统路径后我们就可以下载系统了，局域网网速一般都很快。
   tftp -i 10.200.26.202 GET "\Boot\x64\Images\LiteTouchPE\_x64.wim" pxeboot.wim 下载文件
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194355-0ecc350a-9593-1.png)
   也是刚刚用的脚本，使用Get-FindCredentials -WimFile pxeboot.wim成功恢复密码：
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194409-17123afc-9593-1.png)

   **第六种，配置文件泄露出AD用户的账户密码。**
   集中部署的应用程序的配置文件、注册表、应用服务、web服务的配置文件都值得我们关注，常用的工具有Seatbelt和winPEAS，可以自动化帮我们寻找敏感密码。本靶场已经提供了ma.db的数据库文件，它是McAfee Enterprise Endpoint Security的文件，McAfee 将安装期间使用的凭据嵌入到名为 ma.db 的文件中以连接回 orchestrator，靶场已经告诉我们文件位置：
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194445-2c4a65d4-9593-1.png)
   使用scp命令下载到本地来解密：
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194459-34748abe-9593-1.png)
   查看数据库也非常简单，直接kali下用sqlitebrowser ma.db直接打开：
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194512-3c302844-9593-1.png)
   翻找密码，成功找到域的账户auth\_user和auth\_password，需要解密auth\_password
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194528-45b85b48-9593-1.png)
   解密成功：
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230116194541-4d7c7ef4-9593-1.png)
   拿到了合法的账户通常我们就可以登录我们的目标主机了。但是上面拿到的账号，并不一定每个账号都能直接登录，这里要提一下runas.exe，Runas将凭据注入内存中，使得当前的cmd执行命令的使用用的是特定账号的权限。下面是常用的命令（需要管理员运行）：runas.exe /netonly /user:<domain>\<username> cmd.exe 之后会启动一个新的cmd.exe,为了确保账号正常工作，需要执行一下dir \<dc ip="">\SYSVOL命令来保证账号的有效性。</dc></username></domain>

   通常使用三种方式对AD进行信息收集：cmd、powershell、bloodhound,通常来说这三种都差不多，但就个人而言bloodhound是图形化的，非常方便，powershell的命令远比cmd的命令好记忆，看个人习惯去使用即可。需要注意，信息收集和漏洞利用密切相关，漏洞利用后又需要信息收集，渗透本身就是一个信息收集的过程，在复杂域下更是如此，这里就浅解释一下载体，具体信息在渗透中有什么作用将放到下篇仔细说明。
   在cmd下执行命令通常使用net命令，一般来说此类命令不太会被蓝队和EDR监控，不过这类命令执行必须要在域内的主机才可以执行，同时如果命令返回的数量太多，net就不会返回全部信息。常见的命令如下：

   ```
   net user /domain 列出域下的全部用户
   net user zoe.marshall /domain 检查zoe.marshall用户的详细信息
   net group /domain 检查域下的组
   net group "Tier 1 Admins" /domain 检查特定组的详细信息
   net accounts /domain列出账户策略信息
   ```

   在powershell中进行信息收集无需我们控制的机器加入到域环境内，仅仅只需要指定域服务器即可，以下是常用命令：

   ```
   Get-ADUser -Identity gordon.stevens -Server za.tryhackme.com -Properties *
   -Identity代表我们...