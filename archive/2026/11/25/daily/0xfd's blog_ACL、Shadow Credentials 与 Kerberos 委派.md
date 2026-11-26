---
title: ACL、Shadow Credentials 与 Kerberos 委派
url: https://lucifer11.xyz/knowledge/delegation/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:51.855958
---

# ACL、Shadow Credentials 与 Kerberos 委派

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
3. [Kerberos 专用认证与 ACL 路径](#Kerberos-%E4%B8%93%E7%94%A8%E8%AE%A4%E8%AF%81%E4%B8%8E-ACL-%E8%B7%AF%E5%BE%84)
4. [DNS 记录、gMSA 与服务委派](#DNS-%E8%AE%B0%E5%BD%95%E3%80%81gMSA-%E4%B8%8E%E6%9C%8D%E5%8A%A1%E5%A7%94%E6%B4%BE)
5. [对象继承、跨会话 Relay 与 RBCD](#%E5%AF%B9%E8%B1%A1%E7%BB%A7%E6%89%BF%E3%80%81%E8%B7%A8%E4%BC%9A%E8%AF%9D-Relay-%E4%B8%8E-RBCD)

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

# ACL、Shadow Credentials 与 Kerberos 委派

发表于
2026-11-25

分类于

[身份与域安全](/categories/%E8%BA%AB%E4%BB%BD%E4%B8%8E%E5%9F%9F%E5%AE%89%E5%85%A8/)
，
[目录权限与委派](/categories/%E8%BA%AB%E4%BB%BD%E4%B8%8E%E5%9F%9F%E5%AE%89%E5%85%A8/%E7%9B%AE%E5%BD%95%E6%9D%83%E9%99%90%E4%B8%8E%E5%A7%94%E6%B4%BE/)

阅读次数：

本文字数：
21k

阅读时长 ≈
1:15

域内权限变化通常表现为目录属性、组成员和票据的连续变化。本章保留 Absolute、Intelligence 和 Rebound 的原账户路径，分别标明认证限制、对象控制和委派前提。

域内权限变化通常表现为目录属性、组成员和票据的连续变化。本章保留 Absolute、Intelligence 和 Rebound 的原账户路径，分别标明认证限制、对象控制和委派前提。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/delegation/source.md)
展开全部技术记录

## 分析重点

Absolute 的禁用 NTLM、交互登录权限与成员回滚影响每次工具调用。

Intelligence 连接 DNS、gMSA 与服务票据，时钟同步是原环境的实际问题。

Rebound 的继承 ACL、cross-session relay、KCD 与 RBCD 分支均保留原失败和成功返回。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [Kerberos 专用认证与 ACL 路径](#case-htb-absolute) | htb-absolute | Kerberos、ACL、Shadow Credentials、KrbRelay |
| [DNS 记录、gMSA 与服务委派](#case-intelligence) | intelligence | DNS、gMSA、Kerberos、委派 |
| [对象继承、跨会话 Relay 与 RBCD](#case-rebound) | rebound | Kerberos、RBCD、gMSA、ACL |

## Kerberos 专用认证与 ACL 路径

禁用 NTLM、账户限制和组成员回滚影响工具选择。保留 AS-REP、BloodHound、Shadow Credentials、交互登录及 KrbRelay 的成功与失败分支。

来源 htb-absolute · 原记录 2023-05-29 · 64 个代码块 · 22 处图片引用

查看分析过程、攻击步骤与完整代码

#### 简述

本文是insane难度的HTB absolute机器的域渗透部分，其中大量的Kerberos，ACL，KrbRelay，bloodhound，Shadow Credentials Attack，ldap enumeration，PTH，GROUPS权限修改，interactive session等域渗透只是细节是此box的特色，主要参考0xdf’s blog absolute walkthrough和HTB的absolute官方writeup paper记录这篇博客加深记忆和理解，及供后续做深入研究查阅，备忘。

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Absolute.png)

#### 信息收集

#### nmap

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 ``` | ``` root@fdvoid0# nmap -p- --min-rate 10000 10.10.11.181 Starting Nmap 7.80 ( https://nmap.org ) at 2023-05-21 06:36 EDT Nmap scan report for 10.10.11.181 Host is up (0.087s latency). Not shown: 65509 closed ports PORT      STATE SERVICE 53/tcp    open  domain 80/tcp    open  http 88/tcp    open  kerberos-sec 135/tcp   open  msrpc 139/tcp   open  netbios-ssn 389/tcp   open  ldap 445/tcp   open  microsoft-ds 464/tcp   open  kpasswd5 593/tcp   open  http-rpc-epmap 636/tcp   open  ldapssl 3268/tcp  open  globalcatLDAP 3269/tcp  open  globalcatLDAPssl 5985/tcp  open  wsman 9389/tcp  open  adws 47001/tcp open  winrm 49664/tcp open  unknown 49665/tcp open  unknown 49666/tcp open  unknown 49667/tcp open  unknown 49673/tcp open  unknown 49674/tcp open  unknown 49675/tcp open  unknown 49686/tcp open  unknown 49692/tcp open  unknown 49699/tcp open  unknown 49703/tcp open  unknown  Nmap done: 1 IP address (1 host up) scanned in 8.50 seconds  root@fdvoid0# nmap -sCV -p 53,80,88,135,139,389,445,464,593,636,3268,3269,5985,9389 10.10.11.181 Starting Nmap 7.80 ( https://nmap.org ) at 2023-05-21 06:37 EDT Nmap scan report for 10.10.11.181 Host is up (0.088s latency).  PORT     STATE SERVICE       VERSION 53/tcp   open  domain? | fingerprint-strings: |   DNSVersionBindReqTCP: |     version |_    bind 80/tcp   open  http          Microsoft IIS httpd 10.0 | http-methods: |_  Potentially risky methods: TRACE |_http-server-header: Microsoft-IIS/10.0 |_http-title: Absolute 88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-05-21 17:38:06Z) 135/tcp  open  msrpc         Microsoft Windows RPC 139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn 389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: absolute.htb0., Site: Default-First-Site-Name) | ssl-cert: Subject: commonName=dc.absolute.htb | Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc.absolute.htb | Not valid before: 2022-06-09T08:14:24 |_Not valid after:  2023-06-09T08:14:24 |_ssl-date: 2023-05-21T17:40:40+00:00; +6h59m59s from scanner time. 445/tcp  open  microsoft-ds? 464/tcp  open  kpasswd5? 593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0 636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: absolute.htb0., Site: Default-First-Site-Name) | ssl-cert: Subject: commonName=dc.absolute.htb | Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc.absolute.htb | Not valid before: 2022-06-09T08:14:24 |_Not valid after:  2023-06-09T08:14:24 |_ssl-date: 2023-05-21T17:40:39+00:00; +7h00m00s from scanner time. 3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: absolute.htb0., Site: Default-First-Site-Name) | ssl-cert: Subject: commonName=dc.absolute.htb | Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc.absolute.htb | Not valid before: 2022-06-09T08:14:24 |_Not valid after:  2023-06-09T08:14:24 |_ssl-date: 2023-05-21T17:40:40+00:00; +6h59m59s from scanner time. 3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: absolute.htb0., Site: Default-First-Site-Name) | ssl-cert: Subject: commonName=dc.absolute.htb | Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:dc.absolute.htb | Not valid before: 2022-06-09T08:14:24 |_Not valid after:  2023-06-09T08:14:24 |_ssl-date: 2023-05-21T17:40:39+00:00; +7h00m00s from scanner time. 5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP) |_http-server-header: Microsoft-HTTPAPI/2.0 |_http-title: Not Found 9389/tcp open  mc-nmf        .NET Message Framing 1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service : SF-Port53-TCP:V=7.80%I=7%D=5/21%Time=6469F493%P=x86_64-pc-linux-gnu%r(DNSV SF:ersionBindReqTCP,20,"\0\x1e\0\x06\x81\x04\0\x01\0\0\0\0\0\0\x07version\ SF:x04bind\0\0\x10\0\x03"); Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows  Host script results: |_clock-skew: mean: 6h59m59s, deviation: 0s, median: 6h59m59s | smb2-security-mode: |   2.02: |_    Message signing enabled and required | smb2-time: |   date: 2023-05-21T17:40:25 |_  start_date: N/A  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 161.96 seconds ``` |

IIS版本表明Absolute正在运行Windows 10/Server 2016或更高版本。LDAP扫描显示了dc.absolute.htb的hostname。现在把它和基本域添加到的/etc/hosts文件中:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.181 dc.absolute.htb absolute.htb ``` |

有一个7小时的时差，如果要做任何Kerberos相关的认证需要注意。

注意到WinRM(5985)在找到creds时是打开的

#### SMB - TCP 445

无法在没有密码的情况下连接到SMB:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/absolute] └─# crackmapexec smb 10.10.11.181 --shares SMB         10.10.11.181    445    DC  ...