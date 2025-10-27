---
title: Soccer - HackTheBox
url: https://darkwing.moe/2022/12/19/Soccer-HackTheBox/
source: 喵喵喵喵
date: 2022-12-20
fetch_date: 2025-10-04T01:57:06.051043
---

# Soccer - HackTheBox

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

Soccer - HackTheBox

# Soccer - HackTheBox

##### 2022-12-19

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.194](#10-10-11-194)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 目录扫描](#目录扫描)
4. [4. Tiny File Manager](#Tiny-File-Manager)
   1. [4.1. webshell](#webshell)
5. [5. soc-player.htb](#soc-player-htb)
   1. [5.1. websocket](#websocket)
   2. [5.2. sql injection](#sql-injection)
   3. [5.3. sql-exp.py](#sql-exp-py)
6. [6. user flag](#user-flag)
7. [7. 提权信息](#提权信息)
8. [8. 提权 & root flag](#提权-amp-root-flag)
   1. [8.1. dstat\_miao.py](#dstat-miao-py)
   2. [8.2. shadow](#shadow)
9. [9. 参考资料](#参考资料)

# Soccer - HackTheBox

2022-12-19

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/519>
* ## 10.10.11.194

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121901.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.194 Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-19 13:26 CST Nmap scan report for 10.10.11.194 Host is up (0.19s latency). Not shown: 997 closed tcp ports (conn-refused) PORT     STATE SERVICE         VERSION 22/tcp   open  ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   3072 ad0d84a3fdcc98a478fef94915dae16d (RSA) |   256 dfd6a39f68269dfc7c6a0c29e961f00c (ECDSA) |_  256 5797565def793c2fcbdb35fff17c615c (ED25519) 80/tcp   open  http            nginx 1.18.0 (Ubuntu) |_http-server-header: nginx/1.18.0 (Ubuntu) |_http-title: Did not follow redirect to http://soccer.htb/ 9091/tcp open  xmltec-xmlmail? | fingerprint-strings: |   DNSStatusRequestTCP, DNSVersionBindReqTCP, Help, RPCCheck, SSLSessionReq, drda, informix: |     HTTP/1.1 400 Bad Request |     Connection: close |   GetRequest: |     HTTP/1.1 404 Not Found |     Content-Security-Policy: default-src 'none' |     X-Content-Type-Options: nosniff |     Content-Type: text/html; charset=utf-8 |     Content-Length: 139 |     Date: Mon, 19 Dec 2022 05:27:30 GMT |     Connection: close |     <!DOCTYPE html> |     <html lang="en"> |     <head> |     <meta charset="utf-8"> |     <title>Error</title> |     </head> |     <body> |     <pre>Cannot GET /</pre> |     </body> |     </html> |   HTTPOptions: |     HTTP/1.1 404 Not Found |     Content-Security-Policy: default-src 'none' |     X-Content-Type-Options: nosniff |     Content-Type: text/html; charset=utf-8 |     Content-Length: 143 |     Date: Mon, 19 Dec 2022 05:27:30 GMT |     Connection: close |     <!DOCTYPE html> |     <html lang="en"> |     <head> |     <meta charset="utf-8"> |     <title>Error</title> |     </head> |     <body> |     <pre>Cannot OPTIONS /</pre> |     </body> |     </html> |   RTSPRequest: |     HTTP/1.1 404 Not Found |     Content-Security-Policy: default-src 'none' |     X-Content-Type-Options: nosniff |     Content-Type: text/html; charset=utf-8 |     Content-Length: 143 |     Date: Mon, 19 Dec 2022 05:27:31 GMT |     Connection: close |     <!DOCTYPE html> |     <html lang="en"> |     <head> |     <meta charset="utf-8"> |     <title>Error</title> |     </head> |     <body> |     <pre>Cannot OPTIONS /</pre> |     </body> |_    </html> 1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service : SF-Port9091-TCP:V=7.93%I=7%D=12/19%Time=639FF63C%P=x86_64-apple-darwin21.5 SF:.0%r(informix,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20 SF:close\r\n\r\n")%r(drda,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnec SF:tion:\x20close\r\n\r\n")%r(GetRequest,168,"HTTP/1\.1\x20404\x20Not\x20F SF:ound\r\nContent-Security-Policy:\x20default-src\x20'none'\r\nX-Content- SF:Type-Options:\x20nosniff\r\nContent-Type:\x20text/html;\x20charset=utf- SF:8\r\nContent-Length:\x20139\r\nDate:\x20Mon,\x2019\x20Dec\x202022\x2005 SF::27:30\x20GMT\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x20html>\n<html\ SF:x20lang=\"en\">\n<head>\n<meta\x20charset=\"utf-8\">\n<title>Error</tit SF:le>\n</head>\n<body>\n<pre>Cannot\x20GET\x20/</pre>\n</body>\n</html>\n SF:")%r(HTTPOptions,16C,"HTTP/1\.1\x20404\x20Not\x20Found\r\nContent-Secur SF:ity-Policy:\x20default-src\x20'none'\r\nX-Content-Type-Options:\x20nosn SF:iff\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Length:\ SF:x20143\r\nDate:\x20Mon,\x2019\x20Dec\x202022\x2005:27:30\x20GMT\r\nConn SF:ection:\x20close\r\n\r\n<!DOCTYPE\x20html>\n<html\x20lang=\"en\">\n<hea SF:d>\n<meta\x20charset=\"utf-8\">\n<title>Error</title>\n</head>\n<body>\ SF:n<pre>Cannot\x20OPTIONS\x20/</pre>\n</body>\n</html>\n")%r(RTSPRequest, SF:16C,"HTTP/1\.1\x20404\x20Not\x20Found\r\nContent-Security-Policy:\x20de SF:fault-src\x20'none'\r\nX-Content-Type-Options:\x20nosniff\r\nContent-Ty SF:pe:\x20text/html;\x20charset=utf-8\r\nContent-Length:\x20143\r\nDate:\x SF:20Mon,\x2019\x20Dec\x202022\x2005:27:31\x20GMT\r\nConnection:\x20close\ SF:r\n\r\n<!DOCTYPE\x20html>\n<html\x20lang=\"en\">\n<head>\n<meta\x20char SF:set=\"utf-8\">\n<title>Error</title>\n</head>\n<body>\n<pre>Cannot\x20O SF:PTIONS\x20/</pre>\n</body>\n</html>\n")%r(RPCCheck,2F,"HTTP/1\.1\x20400 SF:\x20Bad\x20Request\r\nConnection:\x20close\r\n\r\n")%r(DNSVersionBindRe SF:qTCP,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20close\r\n SF:\r\n")%r(DNSStatusRequestTCP,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n SF:Connection:\x20close\r\n\r\n")%r(Help,2F,"HTTP/1\.1\x20400\x20Bad\x20Re SF:quest\r\nConnection:\x20close\r\n\r\n")%r(SSLSessionReq,2F,"HTTP/1\.1\x SF:20400\x20Bad\x20Request\r\nConnection:\x20close\r\n\r\n"); Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 80.21 seconds ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.194 soccer.htb ``` |

足球俱乐部：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121902.jpg)

# 目录扫描

目录扫描发现tiny，是一个Tiny File Manager(字典要稍微大点)：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` gobuster dir -w ~/Tools/dict/SecLists/Discovery/Web-Content/raft-medium-directories.txt  -t 50 -u http://soccer.htb/  /tiny                 (Status: 301) [Size: 178] [--> http://soccer.htb/tiny/] ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121903.jpg)

# Tiny File Manager

默认账号密码登录：

* prasathmani/tinyfilemanager: Single-file PHP file manager, browser and manage your files efficiently and easily with tinyfilemanager
  <https://github.com/prasathmani/tinyfilemanager>

|  |  |
| --- | --- |
| ``` 1 ``` | ``` Default username/password: admin/admin@123 and user/12345. ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121904.jpg)

## webshell

文件上传得到webshell，根目录不可写，uploads目录可写可执行：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121905.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121906.jpg)

# soc-player.htb

查看nginx配置文件可以发现另一个vhost：soc-player.htb

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` ls /etc/nginx/sites-available/ cat /etc/nginx/sites-available/soc-player.htb ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022121907.jpg)

添加hosts后查看：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.194 soccer.htb soc-player.soccer.htb ``` |

可以发现顶部多出login，signup等选项：

![](https://github.com/zjicmDarkWi...