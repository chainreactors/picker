---
title: WordPress 插件与管理权限
url: https://lucifer11.xyz/knowledge/cms-wordpress/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:46.546860
---

# WordPress 插件与管理权限

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
3. [WordPress 账户与配置凭据](#WordPress-%E8%B4%A6%E6%88%B7%E4%B8%8E%E9%85%8D%E7%BD%AE%E5%87%AD%E6%8D%AE)
4. [Web 写入与内核提权候选](#Web-%E5%86%99%E5%85%A5%E4%B8%8E%E5%86%85%E6%A0%B8%E6%8F%90%E6%9D%83%E5%80%99%E9%80%89)
5. [认证响应、去重字典与交互式程序](#%E8%AE%A4%E8%AF%81%E5%93%8D%E5%BA%94%E3%80%81%E5%8E%BB%E9%87%8D%E5%AD%97%E5%85%B8%E4%B8%8E%E4%BA%A4%E4%BA%92%E5%BC%8F%E7%A8%8B%E5%BA%8F)
6. [插件盲注与双因素验证材料](#%E6%8F%92%E4%BB%B6%E7%9B%B2%E6%B3%A8%E4%B8%8E%E5%8F%8C%E5%9B%A0%E7%B4%A0%E9%AA%8C%E8%AF%81%E6%9D%90%E6%96%99)
7. [插件文件读取与数据库写入](#%E6%8F%92%E4%BB%B6%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E4%B8%8E%E6%95%B0%E6%8D%AE%E5%BA%93%E5%86%99%E5%85%A5)

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

# WordPress 插件与管理权限

发表于
2026-11-25

分类于

[Web安全](/categories/Web%E5%AE%89%E5%85%A8/)
，
[CMS与插件](/categories/Web%E5%AE%89%E5%85%A8/CMS%E4%B8%8E%E6%8F%92%E4%BB%B6/)

阅读次数：

本文字数：
20k

阅读时长 ≈
1:12

WordPress 实验分别涉及登录反馈、插件读取、上传、数据库和本地任务。本章把同一入口之后的不同权限路径并列，保留原插件版本、账户状态与操作结果。

WordPress 实验分别涉及登录反馈、插件读取、上传、数据库和本地任务。本章把同一入口之后的不同权限路径并列，保留原插件版本、账户状态与操作结果。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/cms-wordpress/source.md)
展开全部技术记录

## 分析重点

Phoenix 的盲注与上传属于两个插件，OTP 和 rsync 是后续系统阶段。

Stapler 同时保留文件读取、数据库写入、历史记录与内核分支。

EVM、Mr Robot 与 Hackademic 保留账户确认和实际文件执行证据。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [WordPress 账户与配置凭据](#case-evm) | evm | WordPress、凭据泄露、文件上传 |
| [Web 写入与内核提权候选](#case-hackademic-rtb1) | Hackademic-RTB1 | WordPress、文件上传、内核 |
| [认证响应、去重字典与交互式程序](#case-mr-robot-1) | Mr-Robot-1 | WordPress、密码审计、SUID |
| [插件盲注与双因素验证材料](#case-phoenix) | phoenix | WordPress、SQL注入、2FA、rsync |
| [插件文件读取与数据库写入](#case-stapler-1) | Stapler-1 | WordPress、LFI、MySQL、内核 |

## WordPress 账户与配置凭据

原链由用户名枚举、后台认证到插件执行，再追踪本地泄露的 root 密码。保留各次工具输出与认证结果。

来源 evm · 原记录 2020-05-23 · 8 个代码块 · 1 处图片引用

查看分析过程、攻击步骤与完整代码

#### name

Name: EVM: 1
Date release: 2 Nov 2019

#### download

Download: https://mega.nz/#F!pVV1CKYI!ABCpQ0qUdbuYIszf0ljH1w
Download (Mirror): https://download.vulnhub.com/evm/EVM.ova
Download (Torrent): https://download.vulnhub.com/evm/EVM.ova.torrent

#### description

This is super friendly box intended for Beginner’s

This may work better with VirtualBox than VMware

#### information gathering

first use nmap as usual

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` root@kali:~# nmap -sn -v 192.168.56.* Nmap scan report for 192.168.56.103 Host is up (0.00026s latency). MAC Address: 08:00:27:90:6F:5B (Oracle VirtualBox virtual NIC) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 ``` | ``` root@kali:~# nmap -sV -sC -T4 -p- -v -A 192.168.56.103 PORT    STATE SERVICE     VERSION 22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0) | ssh-hostkey:  |   2048 a2:d3:34:13:62:b1:18:a3:dd:db:35:c5:5a:b7:c0:78 (RSA) |   256 85:48:53:2a:50:c5:a0:b7:1a:ee:a4:d8:12:8e:1c:ce (ECDSA) |_  256 36:22:92:c7:32:22:e3:34:51:bc:0e:74:9f:1c:db:aa (ED25519) 53/tcp  open  domain      ISC BIND 9.10.3-P4 (Ubuntu Linux) | dns-nsid:  |_  bind.version: 9.10.3-P4-Ubuntu 80/tcp  open  http        Apache httpd 2.4.18 ((Ubuntu)) | http-methods:  |_  Supported Methods: GET HEAD POST OPTIONS |_http-server-header: Apache/2.4.18 (Ubuntu) |_http-title: Apache2 Ubuntu Default Page: It works 110/tcp open  pop3        Dovecot pop3d |_pop3-capabilities: PIPELINING TOP RESP-CODES CAPA UIDL SASL AUTH-RESP-CODE 139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP) 143/tcp open  imap        Dovecot imapd |_imap-capabilities: ID OK LITERAL+ IDLE LOGIN-REFERRALS SASL-IR more ENABLE have listed post-login capabilities Pre-login IMAP4rev1 LOGINDISABLEDA0001 445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP) MAC Address: 08:00:27:90:6F:5B (Oracle VirtualBox virtual NIC) Device type: general purpose Running: Linux 3.X|4.X OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4 OS details: Linux 3.2 - 4.9 Uptime guess: 0.003 days (since Sat May 23 02:15:27 2020) Network Distance: 1 hop TCP Sequence Prediction: Difficulty=259 (Good luck!) IP ID Sequence Generation: All zeros Service Info: Host: UBUNTU-EXTERMELY-VULNERABLE-M4CH1INE; OS: Linux; CPE: cpe:/o:linux:linux_kernel  Host script results: |_clock-skew: mean: 1h19m58s, deviation: 2h18m33s, median: -1s | nbstat: NetBIOS name: UBUNTU-EXTERMEL, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown) | Names: |   UBUNTU-EXTERMEL<00>  Flags: <unique><active> |   UBUNTU-EXTERMEL<03>  Flags: <unique><active> |   UBUNTU-EXTERMEL<20>  Flags: <unique><active> |   WORKGROUP<00>        Flags: <group><active> |_  WORKGROUP<1e>        Flags: <group><active> | smb-os-discovery:  |   OS: Windows 6.1 (Samba 4.3.11-Ubuntu) |   Computer name: ubuntu-extermely-vulnerable-m4ch1ine |   NetBIOS computer name: UBUNTU-EXTERMELY-VULNERABLE-M4CH1INE\x00 |   Domain name: \x00 |   FQDN: ubuntu-extermely-vulnerable-m4ch1ine |_  System time: 2020-05-23T02:20:13-04:00 | smb-security-mode:  |   account_used: guest |   authentication_level: user |   challenge_response: supported |_  message_signing: disabled (dangerous, but default) | smb2-security-mode:  |   2.02:  |_    Message signing enabled but not required | smb2-time:  |   date: 2020-05-23T06:20:13 |_  start_date: N/A ``` |

* Enumeration

use dirb

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 ``` | ``` root@kali:~# dirb http://192.168.56.103/  ----------------- DIRB v2.22     By The Dark Raver -----------------  START_TIME: Mon May 25 06:24:07 2020 URL_BASE: http://192.168.56.103/ WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt  -----------------  GENERATED WORDS: 4612                                                            ---- Scanning URL: http://192.168.56.103/ ---- + http://192.168.56.103/index.html (CODE:200|SIZE:10821)                                             + http://192.168.56.103/info.php (CODE:200|SIZE:83014)                                               + http://192.168.56.103/server-status (CODE:403|SIZE:302)                                            ==> DIRECTORY: http://192.168.56.103/wordpress/                                                                                                                                                           ---- Entering directory: http://192.168.56.103/wordpress/ ---- + http://192.168.56.103/wordpress/index.php (CODE:301|SIZE:0)                                        ==> DIRECTORY: http://192.168.56.103/wordpress/wp-admin/                                             ==> DIRECTORY: http://192.168.56.103/wordpress/wp-content/                                           ==> DIRECTORY: http://192.168.56.103/wordpress/wp-includes/                                          + http://192.168.56.103/wordpress/xmlrpc.php (CODE:405|SIZE:42)                                                                                                                                           ---- Entering directory: http://192.168.56.103/wordpress/wp-admin/ ---- + h...