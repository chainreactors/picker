---
title: Linux 权限、Capabilities 与周期任务
url: https://lucifer11.xyz/knowledge/linux/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:59.758941
---

# Linux 权限、Capabilities 与周期任务

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
3. [PCAP 凭据与 Python capabilities](#PCAP-%E5%87%AD%E6%8D%AE%E4%B8%8E-Python-capabilities)
4. [命令过滤与自定义 sudo 程序](#%E5%91%BD%E4%BB%A4%E8%BF%87%E6%BB%A4%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89-sudo-%E7%A8%8B%E5%BA%8F)
5. [cp 与 zip 的委托执行权限](#cp-%E4%B8%8E-zip-%E7%9A%84%E5%A7%94%E6%89%98%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90)
6. [PATH 解析与 SUID 子进程](#PATH-%E8%A7%A3%E6%9E%90%E4%B8%8E-SUID-%E5%AD%90%E8%BF%9B%E7%A8%8B)
7. [SNMP 扩展命令与目录 ACL](#SNMP-%E6%89%A9%E5%B1%95%E5%91%BD%E4%BB%A4%E4%B8%8E%E7%9B%AE%E5%BD%95-ACL)
8. [代理可达性与 CMS 文件权限](#%E4%BB%A3%E7%90%86%E5%8F%AF%E8%BE%BE%E6%80%A7%E4%B8%8E-CMS-%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90)
9. [FTP 备份哈希与编辑器权限](#FTP-%E5%A4%87%E4%BB%BD%E5%93%88%E5%B8%8C%E4%B8%8E%E7%BC%96%E8%BE%91%E5%99%A8%E6%9D%83%E9%99%90)
10. [历史流量线索与可写清理任务](#%E5%8E%86%E5%8F%B2%E6%B5%81%E9%87%8F%E7%BA%BF%E7%B4%A2%E4%B8%8E%E5%8F%AF%E5%86%99%E6%B8%85%E7%90%86%E4%BB%BB%E5%8A%A1)
11. [无线捕获、编辑历史与权限程序](#%E6%97%A0%E7%BA%BF%E6%8D%95%E8%8E%B7%E3%80%81%E7%BC%96%E8%BE%91%E5%8E%86%E5%8F%B2%E4%B8%8E%E6%9D%83%E9%99%90%E7%A8%8B%E5%BA%8F)
12. [既有回连配置与 sudo pip](#%E6%97%A2%E6%9C%89%E5%9B%9E%E8%BF%9E%E9%85%8D%E7%BD%AE%E4%B8%8E-sudo-pip)

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

# Linux 权限、Capabilities 与周期任务

发表于
2026-11-25

分类于

[系统安全](/categories/%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8/)
，
[Linux权限](/categories/%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8/Linux%E6%9D%83%E9%99%90/)

阅读次数：

本文字数：
27k

阅读时长 ≈
1:38

从服务用户到 root，需要追踪 sudo、SUID、capabilities、目录 ACL 和任务的实际运行身份。本章按原实验保留环境变量、文件所有者、任务触发和输出，便于检查条件是否成立。

从服务用户到 root，需要追踪 sudo、SUID、capabilities、目录 ACL 和任务的实际运行身份。本章按原实验保留环境变量、文件所有者、任务触发和输出，便于检查条件是否成立。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/linux/source.md)
展开全部技术记录

## 分析重点

Cap 的 Python capabilities、NullByte 的 PATH 和 Pit 的目录 ACL 属于不同权限机制。

HA-Dhanush、Sunset 和 WTF 保留工具委托执行的参数与身份变化。

Djinn、Tr0ll 与 SickOs 的自定义程序、清理任务和代理条件都有失败与成功记录。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [PCAP 凭据与 Python capabilities](#case-cap) | cap | PCAP、Capabilities、访问控制 |
| [命令过滤与自定义 sudo 程序](#case-djinn-1) | djinn-1 | 命令注入、sudo、输入过滤 |
| [cp 与 zip 的委托执行权限](#case-ha-dhanush) | HA-Dhanush | sudo、GTFOBins、SSH |
| [PATH 解析与 SUID 子进程](#case-nullbyte-1) | NullByte-1 | PATH、SUID、MySQL |
| [SNMP 扩展命令与目录 ACL](#case-pit) | pit | SNMP、ACL、计划任务 |
| [代理可达性与 CMS 文件权限](#case-sickos-1-1) | SickOs-1-1 | Squid、文件上传、凭据复用 |
| [FTP 备份哈希与编辑器权限](#case-sunset-1) | sunset-1 | FTP、密码审计、GTFOBins |
| [历史流量线索与可写清理任务](#case-tr0ll-1) | Tr0ll-1 | FTP、计划任务、OverlayFS |
| [无线捕获、编辑历史与权限程序](#case-tr0ll-3) | Tr0ll-3 | 无线取证、SUID、凭据泄露 |
| [既有回连配置与 sudo pip](#case-wtf-1) | WTF-1 | 网络配置、pip、sudo |

## PCAP 凭据与 Python capabilities

可下载的 PCAP 中包含 FTP 凭据，而本地 Python 的 capabilities 改变了 setuid 的权限条件。证据覆盖 Web 对象访问和本地进程能力。

来源 cap · 原记录 2021-06-06 · 11 个代码块 · 7 处图片引用

查看分析过程、攻击步骤与完整代码

#### introduce

OS: Linux
Difficulty: Easy
Points: 20
Release: 05 Jun 2021
IP: 10.10.10.245

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb1994.jpg)
* ![my htb rank](http://www.hackthebox.eu/badge/image/235857)

#### information gathering

first use nmap as usaul

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/cap] └─# nmap -sV -v -p- --min-rate=10000 10.10.10.245 PORT   STATE SERVICE VERSION 21/tcp open  ftp     vsftpd 3.0.3 22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0) 80/tcp open  http    gunicorn ``` |

There are three ports open 21:ftp 22:ssh 80:http

Let’s start with ftp let’s check anonymous login is allowed or not.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/cap] └─# ftp 10.10.10.245 Connected to 10.10.10.245. 220 (vsFTPd 3.0.3) Name (10.10.10.245:root): anonymous 331 Please specify the password. Password: 530 Login incorrect. Login failed. ``` |

Login failed! now let’s go on with port-80

#### Port-80

It’s a simple admin-panel.

After some manual enumeration i find nothing. let’s find some directories with help of gobuster.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/cap] └─# gobuster dir -u http://10.10.10.245/ -w /usr/share/seclists/Discovery/Web-Content/raft-small-words-lowercase.txt -t 50 =============================================================== Gobuster v3.1.0 by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart) =============================================================== [+] Url:                     http://10.10.10.245/ [+] Method:                  GET [+] Threads:                 50 [+] Wordlist:                /usr/share/SecLists/Discovery/Web-Content/raft-small-words-lowercase.txt [+] Negative Status codes:   404 [+] User Agent:              gobuster/3.1.0 [+] Timeout:                 10s =============================================================== 2021/06/05 21:28:05 Starting gobuster in directory enumeration mode =============================================================== /data                 (Status: 302) [Size: 208] [--> http://10.10.10.245/] /ip                   (Status: 200) [Size: 17464]                          /capture              (Status: 302) [Size: 220] [--> http://10.10.10.245/data/7]                                                                                  =============================================================== 2021/06/05 21:29:08 Finished =============================================================== ``` |

/data directory look interesting let’s go and check that.

It’s said not found it’s mean that the directory is exist but we need to find the file.

Let’s enumerate further inside /data directory with wfuzz.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/cap] └─# wfuzz -u http://10.10.10.245/data/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 --hc 302,404  /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information. ******************************************************** * Wfuzz 3.1.0 - The Web Fuzzer                         * ********************************************************  Target: http://10.10.10.245/data/FUZZ Total requests: 220560  ===================================================================== ID           Response   Lines    Word       Chars       Payload                                                            =====================================================================  000000051:   200        370 L    993 W      17149 Ch    "2"                                                                000000048:   200        370 L    993 W      17152 Ch    "01"                                                               000000060:   200        370 L    993 W      17143 Ch    "03"                                                               000000045:   200        370 L    993 W      17152 Ch    "1"                                                                000000070:   200        370 L    993 W      17143 Ch    "3"                                                                000000064:   200        370 L    993...