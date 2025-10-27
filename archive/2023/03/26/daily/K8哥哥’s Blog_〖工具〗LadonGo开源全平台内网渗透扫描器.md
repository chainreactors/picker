---
title: 〖工具〗LadonGo开源全平台内网渗透扫描器
url: http://k8gege.org/p/LadonGo.html
source: K8哥哥’s Blog
date: 2023-03-26
fetch_date: 2025-10-04T10:43:38.720367
---

# 〖工具〗LadonGo开源全平台内网渗透扫描器

[![logo](/../k8img/logo.png)

### K8哥哥](/ "K8gege")

## 没有绝对安全的系统

[K8哥哥’s Blog](http://k8gege.org)

* [Home](/)
* [Ladon](/Ladon/)
* [Code](/tags/Code/)
* [Exp](/tags/Exp/)
* [Tool](/tags/Tool/)
* [Music](https://k8music.github.io)
* [Archives](/archives/)
* [Friends](/friends/)
* [Rss](/atom.xml)

# 〖工具〗LadonGo开源全平台内网渗透扫描器

[Ladon](/categories/Ladon/)

[LadonGo](/tags/LadonGo/)

2023/03/25

本文于**909**
天之前发表

### 简介

LadonGo一款开源内网渗透扫描器框架，使用它可轻松一键探测C段、B段、A段存活主机、指纹识别、端口扫描、密码爆破、远程执行、高危漏洞检测等。4.3版本包含43个模块功能，高危漏洞检测MS17010、SmbGhost，远程执行SshCmd、WinrmCmd、PhpShell，10种协议密码爆破Smb/Ssh/Ftp/Mysql/Mssql/Oracle/Sqlplus/Winrm/HttpBasic/Redis，存活探测/信息收集/指纹识别OnlinePC、Ping、Icmp、SnmpScan，HttpBanner、HttpTitle、TcpBanner、WeblogicScan、OxidScan，端口扫描/服务探测PortScan。

### 功能模块

#### Detection

| . | . |
| --- | --- |
| OnlinePC | (Using ICMP/SNMP/Ping detect Online hosts) |
| PingScan | (Using system ping to detect Online hosts) |
| IcmpScan | (Using ICMP Protocol to detect Online hosts) |
| SnmpScan | (Using Snmp Protocol to detect Online hosts) |
| HttpBanner | (Using HTTP Protocol Scan Web Banner) |
| HttpTitle | (Using HTTP protocol Scan Web titles) |
| T3Scan | (Using T3 Protocol Scan Weblogic hosts) |
| PortScan | (Scan hosts open ports using TCP protocol) |
| TcpBanner | (Scan hosts open ports using TCP protocol) |
| OxidScan | (Using dcom Protocol enumeration network interfaces) |

#### VulDetection

| . | . |
| --- | --- |
| MS17010 | (Using SMB Protocol to detect MS17010 hosts) |
| SmbGhost | (Using SMB Protocol to detect SmbGhost hosts) |
| CVE-2021-21972 | (Check VMware vCenter 6.5 6.7 7.0 Rce Vul) |
| CVE-2021-26855 | (Check CVE-2021-26855 Microsoft Exchange SSRF) |

#### BruteForce

| . | . |
| --- | --- |
| SmbScan | (Using SMB Protocol to Brute-For 445 Port) |
| SshScan | (Using SSH Protocol to Brute-For 22 Port) |
| FtpScan | (Using FTP Protocol to Brute-For 21 Port) |
| 401Scan | (Using HTTP BasicAuth to Brute-For web Port) |
| MysqlScan | (Using Mysql Protocol to Brute-For 3306 Port) |
| MssqlScan | (Using Mssql Protocol to Brute-For 1433 Port) |
| OracleScan | (Using Oracle Protocol to Brute-For 1521 Port) |
| WinrmScan | (Using Winrm Protocol to Brute-For 5985 Port) |
| SqlplusScan | (Using Oracle Sqlplus Brute-For 1521 Port) |
| RedisScan | (Using Redis Protocol to Brute-For 6379 Port) |

#### RemoteExec

| . | . |
| --- | --- |
| SshCmd | (SSH Remote command execution Default 22 Port) |
| WinrmCmd | (Winrm Remote command execution Default 5985 Port) |
| PhpShell | (Php WebShell command execution Default 80 Port) |

#### Exploit

| . | . |
| --- | --- |
| PhpStudyDoor | (PhpStudy 2016 & 2018 BackDoor Exploit) |

### 源码编译

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` go get github.com/k8gege/LadonGo go build Ladon.go ``` |

### 快速编译

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` make windows make linux make mac ``` |

### 一键安装

#### Linux/Mac

|  |  |
| --- | --- |
| ``` 1 ``` | ``` make install ``` |

#### Windows

|  |  |
| --- | --- |
| ``` 1 ``` | ``` go run install.go ``` |

### 使用教程

#### 帮助

Ladon help
Ladon Detection
Ladon BruteForce

#### 用法

Ladon IP/机器名/CIDR 扫描模块

#### 例子

##### 信息收集、漏洞检测

Ping扫描C段存活主机（任意权限）
Ladon 192.168.1.8/24 PingScan

ICMP扫描C段存活主机(管理员权限)
Ladon 192.168.1.8/24 IcmpScan

SMB扫描C段永恒之蓝MS17010漏洞主机
Ladon 192.168.1.8/24 MS17010

SMB扫描C段永恒之黑SmbGhost漏洞主机
Ladon 192.168.1.8/24 SmbGhost

T3扫描C段开放WebLogic的主机
Ladon 192.168.1.8/24 T3Scan

HTTP扫描C段开放Web站点Banner
Ladon 192.168.1.8/24 BannerScan

##### 密码爆破、弱口令

扫描C段445端口Windows机器弱口令
Ladon 192.168.1.8/24 SmbScan

扫描C段22端口Linux机器SSH弱口令
Ladon 192.168.1.8/24 SshScan

扫描C段21端口FTP服务器弱口令
Ladon 192.168.1.8/24 SshScan

扫描C段3306端口Mysql服务器弱口令
Ladon 192.168.1.8/24 SshScan

### 扫描速度

1.和Ladon一样，ICMP探测C段仅需1秒
2.Ping扫描C段大约11秒，支持任意权限
3.其它模块自行测试

### 跨平台/全平台/全系统

#### TestOn

| ID | OS |
| --- | --- |
| 0 | WinXP |
| 1 | Win 2003 |
| 2 | Win 7 |
| 3 | Win 8.1 |
| 4 | Win 10 |
| 5 | Win 2008 R2 |
| 6 | Win 2012 R2 |
| 7 | Kali 2019 |
| 8 | SUSE 10 |
| 9 | CentOS 5.8 |
| 10 | CentOS 6.8 |
| 11 | Fedora 5 |
| 12 | RedHat 5.7 |
| 13 | BT5-R3 (Ubuntu 8) |
| 14 | MacOS 10.15 |

以上系统测试成功，其它系统未测，若某些系统不支持可自行编译

#### MacOS x64 10.15

![使用http访问查看图片](/k8img/LadonGo/MacMS17010.png)

#### Linux

![使用http访问查看图片](/k8img/LadonGo/LnxMS17010.PNG)

#### Windows

![使用http访问查看图片](/k8img/LadonGo/WinMS17010.PNG)

### Download

#### LadonGo (ALL OS)

<https://github.com/k8gege/LadonGo>

#### Ladon (Windows & Cobalt Strike)

历史版本: <https://github.com/k8gege/Ladon/releases>
911版本：<http://k8gege.org/Download>
10.10版本：K8小密圈

![](http://k8gege.org/img/k8team.jpg)

### 转载声明

K8博客文章随意转载，转载请注明出处！ © K8gege <http://k8gege.org>

![](../images/k8join2.png)

扫码加入K8小密圈

转载声明：
K8博客文章随意转载，转载请注明出处！ © [K8gege](http://k8gege.org)

[上一篇

〖EXP〗Ladon漏洞复现 CVE-2023-21839 Weblogic](/p/CVE-2023-21839.html "〖EXP〗Ladon漏洞复现 CVE-2023-21839 Weblogic")
[下一篇

〖教程〗ChatGPT编写Ladon渗透工具插件视频教程](/p/ChatGPT.html "〖教程〗ChatGPT编写Ladon渗透工具插件视频教程")

### Table of Contents

1. [简介](#%E7%AE%80%E4%BB%8B)
2. [功能模块](#%E5%8A%9F%E8%83%BD%E6%A8%A1%E5%9D%97)
   1. [Detection](#Detection)
   2. [VulDetection](#VulDetection)
   3. [BruteForce](#BruteForce)
   4. [RemoteExec](#RemoteExec)
   5. [Exploit](#Exploit)
3. [源码编译](#%E6%BA%90%E7%A0%81%E7%BC%96%E8%AF%91)
4. [快速编译](#%E5%BF%AB%E9%80%9F%E7%BC%96%E8%AF%91)
5. [一键安装](#%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85)
   1. [Linux/Mac](#Linux-Mac)
   2. [Windows](#Windows)
6. [使用教程](#%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)
   1. [帮助](#%E5%B8%AE%E5%8A%A9)
   2. [用法](#%E7%94%A8%E6%B3%95)
   3. [例子](#%E4%BE%8B%E5%AD%90)
      1. [信息收集、漏洞检测](#%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86%E3%80%81%E6%BC%8F%E6%B4%9E%E6%A3%80%E6%B5%8B)
      2. [密码爆破、弱口令](#%E5%AF%86%E7%A0%81%E7%88%86%E7%A0%B4%E3%80%81%E5%BC%B1%E5%8F%A3%E4%BB%A4)
7. [扫描速度](#%E6%89%AB%E6%8F%8F%E9%80%9F%E5%BA%A6)
8. [跨平台/全平台/全系统](#%E8%B7%A8%E5%B9%B3%E5%8F%B0-%E5%85%A8%E5%B9%B3%E5%8F%B0-%E5%85%A8%E7%B3%BB%E7%BB%9F)
   1. [TestOn](#TestOn)
   2. [MacOS x64 10.15](#MacOS-x64-10-15)
   3. [Linux](#Linux)
   4. [Windows](#Windows-2)
9. [Download](#Download)
   1. [LadonGo (ALL OS)](#LadonGo-ALL-OS)
   2. [Ladon (Windows & Cobalt Strike)](#Ladon-Windows-Cobalt-Strike)

Total:

Copyright ©
2020
 |
Powered by [K8gege](//k8gege.org)