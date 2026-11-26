---
title: 路径归一化、文件包含与日志内容
url: https://lucifer11.xyz/knowledge/files/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:52.917192
---

# 路径归一化、文件包含与日志内容

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
3. [alias 路径、日志内容与 Perl open](#alias-%E8%B7%AF%E5%BE%84%E3%80%81%E6%97%A5%E5%BF%97%E5%86%85%E5%AE%B9%E4%B8%8E-Perl-open)
4. [PHP 流包装器与受限菜单](#PHP-%E6%B5%81%E5%8C%85%E8%A3%85%E5%99%A8%E4%B8%8E%E5%8F%97%E9%99%90%E8%8F%9C%E5%8D%95)
5. [Weborf 读取与 Wine 执行](#Weborf-%E8%AF%BB%E5%8F%96%E4%B8%8E-Wine-%E6%89%A7%E8%A1%8C)
6. [Unicode 归一化与路径判断](#Unicode-%E5%BD%92%E4%B8%80%E5%8C%96%E4%B8%8E%E8%B7%AF%E5%BE%84%E5%88%A4%E6%96%AD)
7. [Cuppa 解析器与系统文件](#Cuppa-%E8%A7%A3%E6%9E%90%E5%99%A8%E4%B8%8E%E7%B3%BB%E7%BB%9F%E6%96%87%E4%BB%B6)

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

# 路径归一化、文件包含与日志内容

发表于
2026-11-25

分类于

[Web安全](/categories/Web%E5%AE%89%E5%85%A8/)
，
[文件与路径](/categories/Web%E5%AE%89%E5%85%A8/%E6%96%87%E4%BB%B6%E4%B8%8E%E8%B7%AF%E5%BE%84/)

阅读次数：

本文字数：
17k

阅读时长 ≈
1:03

路径的字符串表示、Web 映射和文件系统解析可能不同。本章保留 alias、Unicode、PHP 流包装器及日志内容如何影响读取或执行，同时保留源码与实际响应的对照。

路径的字符串表示、Web 映射和文件系统解析可能不同。本章保留 alias、Unicode、PHP 流包装器及日志内容如何影响读取或执行，同时保留源码与实际响应的对照。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/files/source.md)
展开全部技术记录

## 分析重点

Pikaboo 连接 alias、文件包含、FTP 日志和 Perl open。

Unicode 的 off-by-slash 与归一化发生在不同边界，原输入形式全部保留。

Pluck、W1R3S 与 Sunrise 继续展示私钥、菜单、文件服务与提权分支。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [alias 路径、日志内容与 Perl open](#case-pikaboo) | pikaboo | 路径穿越、LFI、日志注入、Perl |
| [PHP 流包装器与受限菜单](#case-pluck-1) | pluck-1 | LFI、PHP、SSH、Exim |
| [Weborf 读取与 Wine 执行](#case-sunset-sunrise) | sunset-sunrise | 路径穿越、Wine、sudo |
| [Unicode 归一化与路径判断](#case-unicode) | unicode | Unicode、路径穿越、JWT、Python |
| [Cuppa 解析器与系统文件](#case-w1r3s-1-0-1) | W1R3S-1-0-1 | LFI、Cuppa、文件读取 |

## alias 路径、日志内容与 Perl open

nginx alias 映射的差异暴露文件包含，FTP 日志内容连接执行；后续 LDAP 资料和 Perl open 的调用方式构成独立提权段。

来源 pikaboo · 原记录 2021-07-20 · 27 个代码块 · 13 处图片引用

查看分析过程、攻击步骤与完整代码

#### introduce

OS: Linux
Difficulty: Hard
Points: 40
Release: 17 Jul 2021
IP: 10.10.10.249

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb2022.jpg)
* ![my htb rank](http://www.hackthebox.eu/badge/image/235857)

#### Enumeration

use nmap as usual

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` # Nmap 7.91 scan initiated Sun Jul 18 01:44:59 2021 as: nmap -vvv -p 21,22,80 -A -v -oN intial.nmap 10.129.185.25 Nmap scan report for pikaboo.htb (10.129.185.25) Host is up, received syn-ack (0.32s latency). Scanned at 2021-07-18 01:45:01 EDT for 18s  PORT   STATE SERVICE REASON  VERSION 21/tcp open  ftp     syn-ack vsftpd 3.0.3 22/tcp open  ssh     syn-ack OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0) | ssh-hostkey:  |   2048 17:e1:13:fe:66:6d:26:b6:90:68:d0:30:54:2e:e2:9f (RSA) | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAgG6pLBPMmXneLGYurX9xbt6cE2IYdEN9J/ijCVrQbpUyVeTNWNoFnpB8+DIcppOtsJu0X3Iwpfb1eTmuop8q9nNlmyOcOTBHYOYLQwa+G4e90Bsku86ndqs+LU09sjqss5n3XdZoFqunNfZb7EirVVCgI80Lf8F+3XRRIX3ErqNrk2LiaQQY6fcAaNALaQy9ked7KydWDFYizO2dnu8ee2ncdXFMBeVDKGVfrlHAoRFoTmCEljCP1Vsjt69NDBudCGJBgU1MbItTF7DtbNQWGQmw8/9n9Jq8ic/YxOnIKRDDUuuWdE3sy2dPiw0ZVuG7V2GnkkMsGv0Qn3Uq9Qx7 |   256 92:86:54:f7:cc:5a:1a:15:fe:c6:09:cc:e5:7c:0d:c3 (ECDSA) | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIJl6Z/XtGXJwSnO57P3CesJfRbmGNra4AuSSHCGUocKchdp3JnNE704lMnocAevDwi9HsAKARxCup18UpPHz+I= |   256 f4:cd:6f:3b:19:9c:cf:33:c6:6d:a5:13:6a:61:01:42 (ED25519) |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINyHVcrR4jjhBG5vZsvKRsKO4SnXj3GqeMtwvFSvd4B4 80/tcp open  http    syn-ack nginx 1.14.2 | http-methods:  |_  Supported Methods: GET HEAD POST OPTIONS |_http-server-header: nginx/1.14.2 |_http-title: Pikaboo Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel  Read data files from: /usr/bin/../share/nmap Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . # Nmap done at Sun Jul 18 01:45:19 2021 -- 1 IP address (1 host up) scanned in 20.01 seconds ``` |

Looks like we have 3 ports FTP,SSH and WEB.
Let’s check FTP for anonymous login.

#### FTP

#### Anonymous Login

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` kali@kali:~/HackTheBox/Pikaboo$ ftp pikaboo.htb  Connected to pikaboo.htb. 220 (vsFTPd 3.0.3) Name (pikaboo.htb:kali): anonymous 331 Please specify the password. Password: 530 Login incorrect. Login failed. ftp> ``` |

Looks like we don’t have anonymous login so it is a dead end for now until we have some creds for it.

#### Web

#### Visiting website

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb2023.jpg)

Not much here there is a contact page but not much there as we cannot submit the form.
Then we have another page called pokatdex aka pokedex(For Pokemon fans like me).
Not necessary for the machine but had to put it in.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb2024.jpg)

Just checking for any pokemon in there we are redirected to the link.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb2025.jpg)

Here we have the link for the api but looks like it still is under construction so not much from here.
And finally there is admin page with requires basic authentication for logging in.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb2026.jpg)

Default creds and bruteforce should not work as this is hardbox so let’s think something other than that.

#### Intresting thing

Clicking cancel on the basic authentication dialogue box gives us something intresting.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb2027.jpg)

In the image you can see that it is saying it is using apache server on port 81 so there is two intresting thing first is why port 81 instead of standard port 80 but we will get back to that later and another is nmap says it’s nginx not apache so there must some sort of traffic forwarding and reverse proxy running on the backend and now to the port 81 part as nginx is running onport 80 that is why apache is on port 81 as both should be hosted on same machine.

#### Enumeration

Looking for version and exploit it seems to be running latest versions of both apache and nginx but I came across this article which specified that there could be path traversal due to misconfigured alias in nginx.

https://www.acunetix.com/vulnerabilities/web/path-traversal-via-misconfigured-nginx-alias/

so I thought to give it a try as it is pretty easy just go to the endpoint which ask for the creds and then use ../ and then go to the desired directory so I decided to give it a try.

#### Fuzzing

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` | ``` kali@kali:~/HackTheBox/Pikaboo$ ffuf -u http://pikaboo.htb/admin../FUZZ -w /usr/share/wordlists/dirb/big.txt -t 200          /'___\  /'___\           /'___\               /\ \__/ /\ \__/  __  __  /\ \__/               \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\               \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/                \ \_\   \ \_\  \ \____/  \ \_\                  \/_/    \/_/   \/___/    \/_/                v1.3.0 Kali Exclusive <3 ________________________________________________   :: Method           : GET  :: URL              : http://pikaboo.htb/admin../FUZZ  :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/big.txt  :: Follow redirects : false  :: Calibration ...