---
title: 〖工具〗LadonGo开源全平台内网渗透扫描器
url: https://buaq.net/go-155272.html
source: unSafe.sh - 不安全
date: 2023-03-26
fetch_date: 2025-10-04T10:42:19.083050
---

# 〖工具〗LadonGo开源全平台内网渗透扫描器

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/edd54b895ae5a03d982098cda61aca95.jpg)

〖工具〗LadonGo开源全平台内网渗透扫描器

简介LadonGo一款开源内网渗透扫描器框架，使用它可轻松一键探测C段、B段、A段存活主机、指纹识别、端口扫描、密码爆破、远程执行、高危漏洞检测等。4.3版本包含43个模块功能，高危
*2023-3-25 21:40:0
Author: [k8gege.org(查看原文)](/jump-155272.htm)
阅读量:132
收藏*

---

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
| ``` 1 ``` | ``` go get github.com/k8gege/LadonGo go build Ladon.go ``` |

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

![image](http://k8gege.org/k8img/LadonGo/MacMS17010.png)

#### Linux

![image](http://k8gege.org/k8img/LadonGo/LnxMS17010.PNG)

#### Windows

![image](http://k8gege.org/k8img/LadonGo/WinMS17010.PNG)

### Download

#### LadonGo (ALL OS)

<https://github.com/k8gege/LadonGo>

#### Ladon (Windows & Cobalt Strike)

历史版本: <https://github.com/k8gege/Ladon/releases>
911版本：<http://k8gege.org/Download>
10.10版本：K8小密圈

![](http://k8gege.org/img/k8team.jpg)

文章来源: http://k8gege.org/p/LadonGo.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)