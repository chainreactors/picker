---
title: RegistryTwo - HackTheBox
url: https://darkwing.moe/2023/07/28/RegistryTwo-HackTheBox/
source: 喵喵喵喵
date: 2023-07-29
fetch_date: 2025-10-04T11:50:59.732191
---

# RegistryTwo - HackTheBox

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

RegistryTwo - HackTheBox

# RegistryTwo - HackTheBox

##### 2023-07-28

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 443](#443)
   2. [2.2. 5000/5001](#5000-5001)
3. [3. Docker Registry](#Docker-Registry)
   1. [3.1. \_catalog](#catalog)
   2. [3.2. hosting-app tags](#hosting-app-tags)
   3. [3.3. DockerRegistryGrabber](#DockerRegistryGrabber)
4. [4. hosting-app](#hosting-app)
   1. [4.1. reconfigure](#reconfigure)
   2. [4.2. EditFileSessionManager LFI](#EditFileSessionManager-LFI)
   3. [4.3. /etc/hosting.ini](#etc-hosting-ini)
   4. [4.4. RMI](#RMI)
5. [5. RMI shell](#RMI-shell)
   1. [5.1. reverse shell](#reverse-shell)
6. [6. RMIClient](#RMIClient)
   1. [6.1. RMIClient](#RMIClient-1)
7. [7. user flag](#user-flag)
8. [8. quarantine](#quarantine)
9. [9. rmi server 劫持](#rmi-server-劫持)
10. [10. root flag](#root-flag)
    1. [10.1. shadow](#shadow)
11. [11. 参考资料](#参考资料)

# RegistryTwo - HackTheBox

2023-07-28

# 基本信息

* <https://app.hackthebox.com/machines/RegistryTwo>
* 10.10.11.223

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023072501.jpg)

# 端口扫描

22,443,5000,5001:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.223 Starting Nmap 7.94 ( https://nmap.org ) at 2023-07-25 13:23 CST Nmap scan report for 10.10.11.223 Host is up (0.17s latency). Not shown: 996 filtered tcp ports (no-response) PORT     STATE SERVICE            VERSION 22/tcp   open  ssh                OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   2048 fa:b0:03:98:7e:60:c2:f3:11:82:27:a1:35:77:9f:d3 (RSA) |   256 f2:59:06:dc:33:b0:9f:a3:5e:b7:63:ff:61:35:9d:c5 (ECDSA) |_  256 e3:ac:ab:ea:2b:d6:8e:f4:1f:b0:7b:05:0a:69:a5:37 (ED25519) 443/tcp  open  ssl/http           nginx 1.14.0 (Ubuntu) |_http-title: Did not follow redirect to https://www.webhosting.htb/ |_http-server-header: nginx/1.14.0 (Ubuntu) | ssl-cert: Subject: organizationName=free-hosting/stateOrProvinceName=Berlin/countryName=DE | Not valid before: 2023-02-01T20:19:22 |_Not valid after:  2024-02-01T20:19:22 |_ssl-date: TLS randomness does not represent time 5000/tcp open  ssl/http           Docker Registry (API: 2.0) |_http-title: Site doesn't have a title. | ssl-cert: Subject: commonName=*.webhosting.htb/organizationName=Acme, Inc./stateOrProvinceName=GD/countryName=CN | Subject Alternative Name: DNS:webhosting.htb, DNS:webhosting.htb | Not valid before: 2023-03-26T21:32:06 |_Not valid after:  2024-03-25T21:32:06 5001/tcp open  ssl/commplex-link? | ssl-cert: Subject: commonName=*.webhosting.htb/organizationName=Acme, Inc./stateOrProvinceName=GD/countryName=CN | Subject Alternative Name: DNS:webhosting.htb, DNS:webhosting.htb | Not valid before: 2023-03-26T21:32:06 |_Not valid after:  2024-03-25T21:32:06 | tls-alpn: |   h2 |_  http/1.1 | fingerprint-strings: |   FourOhFourRequest: |     HTTP/1.0 404 Not Found |     Content-Type: text/plain; charset=utf-8 |     X-Content-Type-Options: nosniff |     Date: Tue, 25 Jul 2023 05:26:29 GMT |     Content-Length: 10 |     found |   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: |     HTTP/1.1 400 Bad Request |     Content-Type: text/plain; charset=utf-8 |     Connection: close |     Request |   GetRequest: |     HTTP/1.0 200 OK |     Content-Type: text/html; charset=utf-8 |     Date: Tue, 25 Jul 2023 05:25:56 GMT |     Content-Length: 26 |     <h1>Acme auth server</h1> |   HTTPOptions: |     HTTP/1.0 200 OK |     Content-Type: text/html; charset=utf-8 |     Date: Tue, 25 Jul 2023 05:25:57 GMT |     Content-Length: 26 |_    <h1>Acme auth server</h1> |_ssl-date: TLS randomness does not represent time 1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service : SF-Port5001-TCP:V=7.94%T=SSL%I=7%D=7/25%Time=64BF5CE3%P=x86_64-apple-darwi SF:n22.4.0%r(GenericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConten SF:t-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n SF:400\x20Bad\x20Request")%r(GetRequest,8E,"HTTP/1\.0\x20200\x20OK\r\nCont SF:ent-Type:\x20text/html;\x20charset=utf-8\r\nDate:\x20Tue,\x2025\x20Jul\ SF:x202023\x2005:25:56\x20GMT\r\nContent-Length:\x2026\r\n\r\n<h1>Acme\x20 SF:auth\x20server</h1>\n")%r(HTTPOptions,8E,"HTTP/1\.0\x20200\x20OK\r\nCon SF:tent-Type:\x20text/html;\x20charset=utf-8\r\nDate:\x20Tue,\x2025\x20Jul SF:\x202023\x2005:25:57\x20GMT\r\nContent-Length:\x2026\r\n\r\n<h1>Acme\x2 SF:0auth\x20server</h1>\n")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20R SF:equest\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\ SF:x20close\r\n\r\n400\x20Bad\x20Request")%r(Help,67,"HTTP/1\.1\x20400\x20 SF:Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConn SF:ection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(SSLSessionReq,67,"HTT SF:P/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20char SF:set=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(Term SF:inalServerCookie,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type SF::\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x2 SF:0Bad\x20Request")%r(TLSSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Reques SF:t\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20cl SF:ose\r\n\r\n400\x20Bad\x20Request")%r(Kerberos,67,"HTTP/1\.1\x20400\x20B SF:ad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConne SF:ction:\x20close\r\n\r\n400\x20Bad\x20Request")%r(FourOhFourRequest,A7," SF:HTTP/1\.0\x20404\x20Not\x20Found\r\nContent-Type:\x20text/plain;\x20cha SF:rset=utf-8\r\nX-Content-Type-Options:\x20nosniff\r\nDate:\x20Tue,\x2025 SF:\x20Jul\x202023\x2005:26:29\x20GMT\r\nContent-Length:\x2010\r\n\r\nNot\ SF:x20found\n")%r(LPDString,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCont SF:ent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r SF:\n400\x20Bad\x20Request")%r(LDAPSearchReq,67,"HTTP/1\.1\x20400\x20Bad\x SF:20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnectio SF:n:\x20close\r\n\r\n400\x20Bad\x20Request"); Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 224.46 seconds ``` |

## 443

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.223 www.webhosting.htb ``` |

一个FREE WEB HOSTING：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023072502.jpg)

## 5000/5001

5000直接访问是空白，5001是Acme auth server：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023072503.jpg)

因为5000端口是空白，搜索测试发现是Docker Registry：

* 5000 - Pentesting Docker Registry - HackTricks
  <https://book.hacktricks.xyz/network-services-pentesting/5000-pentesting-docker-registry>

需要认证：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023072504.jpg)

# Docker Registry

5000需要认证，5001是auth server，那这两个应该是结合使用的，5001端口进行目录扫描发现auth端点：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` gobuster dir -w ~/Tools/dict/SecLists/Discovery/Web-Content/common.txt  -t 50 -u "https://10.10.11.223:5001/"  -k  /auth                 (Status: 200) [Size: 1332] ``` |

直接访问得到一个JWT:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/mast...