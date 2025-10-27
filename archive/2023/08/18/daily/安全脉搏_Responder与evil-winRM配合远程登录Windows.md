---
title: Responder与evil-winRM配合远程登录Windows
url: https://www.secpulse.com/archives/203051.html
source: 安全脉搏
date: 2023-08-18
fetch_date: 2025-10-04T11:58:55.346046
---

# Responder与evil-winRM配合远程登录Windows

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# Responder与evil-winRM配合远程登录Windows

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-08-17

49,327

## 0x01.evil-winRM

### 0x01.1概述

在使用和介绍Responder之前，先来了解一下`evil-winRM`:

`evil-winrm`是Windows远程管理(WinRM) Shell的终极版本。

Windows远程管理是WS 管理协议的 Microsoft 实施，该协议是基于标准 SOAP、不受防火墙影响的协议，允许不同供应商的硬件和操作系统相互操作。而微软将其包含在他们的系统中，是为了便于系统管理员在日常工作中，远程管理服务器，或通过脚本同时管理多台服务器，以提高他们的工作效率。

此程序可在启用此功能的任何Microsoft Windows服务器上使用（通常端口为5985），当然只有在你具有使用凭据和权限时才能使用。因此，我们说它可用于黑客攻击的后利用/渗透测试阶段。相对于攻击者来说，这个程序能为他们提供更好更简单易用的功能。当然，系统管理员也可以将其用于合法目的，但其大部分功能都集中于黑客攻击/渗透测试。

### 0x01.2安装和使用

**安装：**

方法一

```
sudo apt install evil-winrm
```

方法二：

```
git clone https://github.com/Hackplayers/evil-winrm.git
```

方法三：

```
gem install evil-winrm
```

**使用：**

首先查看帮助文档

```
root@kali:~# evil-winrm -h

Evil-WinRM shell v3.5
用法：evil-winrm -i IP -u USER [-s SCRIPTS_PATH] [-e EXES_PATH] [-P PORT] [-p PASS] [-H HASH] [-U URL] [-S] [-c PUBLIC_KEY_PATH ] [-k PRIVATE_KEY_PATH ] [-r 领域] [--spn SPN_PREFIX] [-l]
     -S, --ssl 启用 ssl
     -c, --pub-key PUBLIC_KEY_PATH 公钥证书的本地路径
     -k, --priv-key PRIVATE_KEY_PATH 私钥证书的本地路径
     -r, --realm DOMAIN Kerberos auth，还必须使用此格式在 /etc/krb5.conf 文件中设置 -> CONTOSO.COM = { kdc = fooserver.contoso.com }
     -s, --scripts PS_SCRIPTS_PATH Powershell 脚本本地路径
         --spn SPN_PREFIX Kerberos 身份验证的 SPN 前缀（默认 HTTP）
     -e, --executables EXES_PATH C# 可执行文件本地路径
     -i, --ip IP 远程主机IP或主机名。 Kerberos 身份验证的 FQDN（必需）
     -U, --url URL 远程 url 端点（默认 /wsman）
     -u, --user USER 用户名（如果不使用 kerberos，则需要）
     -p, --password PASS 密码
     -H, --hash HASH NTHash
     -P, --port PORT 远程主机端口（默认5985）
     -V, --version 显示版本
     -n, --no-colors 禁用颜色
     -N, --no-rpath-completion 禁用远程路径完成
     -l, --log 记录 WinRM 会话
     -h, --help 显示此帮助消息
```

## 0x02.Responder

### 0x02.1 概念

响应 LLMNR、NBT-NS 和 MDNS 投毒者。 它将根据名称后缀回答特定的 NBT-NS（NetBIOS 名称服务）查询（请参阅：<http://support.microsoft.com/kb/163409>）。默认情况下，该工具将仅响应适用于 SMB 的文件服务器服务请求。

### 0x02.2 特性

**内置 SMB 身份验证服务器**

默认情况下支持具有扩展安全性 NTLMSSP 的 NTLMv1、NTLMv2 哈希。 已成功测试从 Windows 95 到 Server 2012 RC、Samba 和 Mac OSX Lion。 NT4 支持明文密码，当设置`--lm`选项时，LM 哈希降级。该工具启动时默认启用此功能。

**内置 MSSQL 身份验证服务器**

为了将 SQL 身份验证重定向到此工具，您需要为 Windows Vista 之前的系统设置选项 -r（用于 SQL Server 查找的 NBT-NS 查询使用工作站服务名称后缀）（LLMNR 将用于 Vista 和 更高）。 该服务器支持 NTLMv1、LMv2 哈希。 此功能已在 Windows SQL Server 2005 和 2008 上成功测试。

**内置 HTTP 身份验证服务器**

为了将 HTTP 身份验证重定向到此工具，您需要为早于 Vista 的 Windows 版本设置选项 -r（用于 HTTP 服务器查找的 NBT-NS 查询使用工作站服务名称后缀发送）。 对于 Vista 及更高版本，将使用 LLMNR。 该服务器支持 NTLMv1、NTLMv2 哈希和基本身份验证。 该服务器已在 IE 6 至 IE 10、Firefox、Chrome、Safari 上成功测试。

注意：此模块也适用于从 Windows WebDav 客户端 (WebClient) 发出的 WebDav NTLM 身份验证。 您现在可以将自定义文件发送给受害者。

**内置 HTTPS 身份验证服务器**

与上面相同。 文件夹 certs/ 包含 2 个默认密钥，其中包括一个虚拟私钥。 这是故意的，目的是让 Responder 开箱即用。 添加了一个脚本，以防您需要生成自己的自签名密钥对。

**内置 LDAP 身份验证服务器**

为了将 LDAP 身份验证重定向到此工具，您需要为早于 Vista 的 Windows 版本设置选项 -r（用于 HTTP 服务器查找的 NBT-NS 查询使用工作站服务名称后缀发送）。 对于 Vista 及更高版本，将使用 LLMNR。 该服务器支持 NTLMSSP 哈希和简单身份验证（明文身份验证）。 该服务器已在 Windows 支持工具"ldp"和 LdapAdmin 上成功测试。

**内置 FTP、POP3、IMAP、SMTP 身份验证服务器**

该模块将收集明文凭据

【---- 帮助网安学习，以下所有学习资料免费领！领取资料加 we~@x：yj009991，备注 “安全脉搏” 获取！】
① 网安学习成长路径思维导图
② 60 + 网安经典常用工具包
③ 100+SRC 漏洞分析报告
④ 150 + 网安攻防实战技术电子书
⑤ 最权威 CISSP 认证考试指南 + 题库
⑥ 超 1800 页 CTF 实战技巧手册
⑦ 最新网安大厂面试题合集（含答案）
⑧ APP 客户端安全检测指南（安卓 + IOS）

**内置 DNS 服务器**

该服务器将回答 A 类查询。 当它与 ARP 欺骗结合起来时，这真的很方便。

**内置 WPAD 代理服务器**

如果启用了“自动检测设置”，此模块将捕获网络上启动 Internet Explorer 的任何人的所有 HTTP 请求。 该模块非常有效。 您可以在 Responder.conf 中配置自定义 PAC 脚本，并将 HTML 注入服务器的响应中。 请参阅 Responder.conf。

**浏览器监听器**

该模块允许在隐身模式下找到 PDC。

**指纹识别**

当使用选项 `-f`时，响应程序将对发出 LLMNR/NBT-NS 查询的每个主机进行指纹识别。 所有采集模块在指纹模式下仍然可以工作。

**ICMP 重定向**

```
python tools/Icmp-Redirect.py
```

适用于 Windows XP/2003 及更早版本上的 MITM 域成员。 这种攻击与 DNS 模块相结合非常有效。

**流氓 DHCP**

```
python tools/DHCP.py
```

DHCP 通知欺骗。 允许您让真正的 DHCP 服务器发布 IP 地址，然后发送 DHCP Inform 应答以将您的 IP 地址设置为主 DNS 服务器，以及您自己的 WPAD URL。

**分析模式**

该模块允许您查看网络上的 NBT-NS、BROWSER、LLMNR、DNS 请求，而不会破坏任何响应。 此外，您还可以被动映射域、MSSQL 服务器、工作站，看看 ICMP 重定向攻击在您的子网上是否可行。

### 0x02.3 Responder欺骗原理

在使用Responder之前，我们要先了解windwos默认开启的三种协议，这三种协议分别是**链路本地多播名称解析（LLMNR）**、**名称服务器(NBNS) 协议**和**多播DNS（mdns）协议**。

**LLMNR**

**链路本地多播名称解析（LLMNR）**是一个**基于域名系统（DNS）**数据包格式的协议，IPv4和IPv6的主机可以通过此协议对同一本地链路上的主机执行名称解析。Windows 操作系统从 Windows Vista开始就内嵌支持，Linux系统也通过systemd实现了此协议。它通过UDP 5355端口进行通信，且LLMNR支持IPV6。

**NBNS**

**网络基本输入/输出系统(NetBIOS)**名称服务器(NBNS) 协议是 TCP/IP 上的 NetBIOS (NetBT) 协议族的一部分，它在基于 NetBIOS 名称访问的网络上提供主机名和地址映射方法。通过UDP 137端口进行通信，但NBNS不支持IPV6。

**mDNS**

在计算机网络中 ，**多播DNS（ mDNS ）**协议将主机名解析为不包含本地名称服务器的小型网络中的IP地址。 它是一种零配置服务，使用与**单播域名系统（DNS）**基本相同的编程接口，数据包格式和操作语义。 虽然Stuart Cheshire将mDNS设计为独立协议，但它可以与标准DNS服务器协同工作。它通过UDP 5353端口进行通信，且mDNS也支持IPV6。

目前仅有windows 10以上的系统支持mdns，经测试发现，禁用了llmnr后mdns也会被禁用。

总的来说，以上几种协议在windows中都是默认启用的，主要作用都是在DNS服务器解析失败后，尝试对windows主机名称进行解析，正因为默认启用、且实现方式又类似于ARP协议，并没有一个认证的过程，所以就会引发各种基于这两种协议的欺骗行为，而Responder正是通过这种方式，欺骗受害机器，并使受害机器在后续认证中发送其凭证。

### 0x02.4 使用方法

```
root@kali:~#responder -h

用法：responder -I eth0 -w -d
或者：
responder -I eth0 -wd

选项：
   --version 显示程序的版本号并退出
   -h, --help 显示此帮助消息并退出
   -A, --analyze 分析模式。 此选项允许您查看NBT-NS，
                         BROWSER、LLMNR 请求没有响应。
   -I eth0，--接口=eth0
                         要使用的网络接口，可以使用“ALL”作为
                         所有接口的通配符
   -i 10.0.0.21,--ip=10.0.0.21
                         要使用的本地 IP（仅适用于 OSX）
   -6 2002:c0a8:f7:1:3ba8:aceb:b1a9:81ed, --externalip6=2002:c0a8:f7:1:3ba8:aceb:b1a9:81ed
                         使用其他 IPv6 地址对所有请求进行毒害
                         响应者之一。
   -e 10.0.0.22, --externalip=10.0.0.22
                         使用其他 IP 地址毒害所有请求
                         响应者之一。
   -b, --basic 返回基本 HTTP 身份验证。 默认值：NTLM
   -d, --DHCP 启用 DHCP 广播请求的应答。 这
                         选项将在 DHCP 响应中注入 WPAD 服务器。
                         ...