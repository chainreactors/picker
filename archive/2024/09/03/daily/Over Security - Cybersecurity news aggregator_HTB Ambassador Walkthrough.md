---
title: HTB Ambassador Walkthrough
url: https://www.secjuice.com/htb-ambassador-walkthrough/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-03
fetch_date: 2025-10-06T18:27:29.166740
---

# HTB Ambassador Walkthrough

[![Secjuice](https://www.secjuice.com/content/images/2018/12/Logo-1.png)](https://www.secjuice.com)

* [Donate](https://opencollective.com/secjuice)
* [About Us](https://secjuice.com/about-us/)
* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/OSINT/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)
* [Hire A Writer](https://secjuice.com/hire-infosec-cybersecurity-writer/)
* [Rankings](https://secjuice.com/secjuice-writers-ranking/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

# HTB Ambassador Walkthrough

Discover how using an access token can allow breaking into a development server.

* [![Andy74](/content/images/size/w100/2020/01/avatar.png)](/author/andy74/)

#### [Andy74](/author/andy74/)

Sep 2, 2024
• 20 min read

![HTB Ambassador Walkthrough](/content/images/size/w2000/2024/09/secjuice-labor-day01-1.png)

This image was generated using Microsoft Copilot.

A simple and really fun BOX.

Let's start with the **nmap** scan:

```
Starting Nmap 7.93 ( https://nmap.org ) at 2022-10-19 21:25 CEST
Nmap scan report for 10.10.11.183
Host is up (0.11s latency).
Not shown: 995 closed tcp ports (conn-refused)
PORT     STATE    SERVICE VERSION
22/tcp   open     ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 29dd8ed7171e8e3090873cc651007c75 (RSA)
|   256 80a4c52e9ab1ecda276439a408973bef (ECDSA)
|_  256 f590ba7ded55cb7007f2bbc891931bf6 (ED25519)
80/tcp   open     http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Ambassador Development Server
|_http-generator: Hugo 0.94.2
|_http-server-header: Apache/2.4.41 (Ubuntu)
3000/tcp open     ppp?
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Content-Type: text/html; charset=utf-8
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2Fnice%2520ports%252C%2FTri%256Eity.txt%252ebak; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Wed, 19 Oct 2022 19:26:41 GMT
|     Content-Length: 29
|     href="/login">Found</a>.
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie:
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest:
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Content-Type: text/html; charset=utf-8
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2F; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Wed, 19 Oct 2022 19:26:09 GMT
|     Content-Length: 29
|     href="/login">Found</a>.
|   HTTPOptions:
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2F; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Wed, 19 Oct 2022 19:26:14 GMT
|_    Content-Length: 0
3306/tcp open     mysql   MySQL 8.0.30-0ubuntu0.20.04.2
| mysql-info:
|   Protocol: 10
|   Version: 8.0.30-0ubuntu0.20.04.2
|   Thread ID: 84
|   Capabilities flags: 65535
|   Some Capabilities: Support41Auth, SupportsCompression, Speaks41ProtocolOld, LongPassword, SupportsTransactions, FoundRows, InteractiveClient, LongColumnFlag, ConnectWithDatabase, IgnoreSigpipes, Speaks41ProtocolNew, DontAllowDatabaseTableColumn, IgnoreSpaceBeforeParenthesis, SwitchToSSLAfterHandshake, ODBCClient, SupportsLoadDataLocal, SupportsMultipleStatments, SupportsMultipleResults, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: eq\x7F>F0\x13\x1D-o\x1B.G.[43"4\x17
|_  Auth Plugin Name: caching_sha2_password
7921/tcp filtered unknown
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3000-TCP:V=7.93%I=7%D=10/19%Time=63504F53%P=x86_64-pc-linux-gnu%r(G
SF:enericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20
SF:text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\
SF:x20Request")%r(GetRequest,174,"HTTP/1\.0\x20302\x20Found\r\nCache-Contr
SF:ol:\x20no-cache\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nExpi
SF:res:\x20-1\r\nLocation:\x20/login\r\nPragma:\x20no-cache\r\nSet-Cookie:
SF:\x20redirect_to=%2F;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nX-Conte
SF:nt-Type-Options:\x20nosniff\r\nX-Frame-Options:\x20deny\r\nX-Xss-Protec
SF:tion:\x201;\x20mode=block\r\nDate:\x20Wed,\x2019\x20Oct\x202022\x2019:2
SF:6:09\x20GMT\r\nContent-Length:\x2029\r\n\r\n<a\x20href=\"/login\">Found
SF:</a>\.\n\n")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-T
SF:ype:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400
SF:\x20Bad\x20Request")%r(HTTPOptions,12E,"HTTP/1\.0\x20302\x20Found\r\nCa
SF:che-Control:\x20no-cache\r\nExpires:\x20-1\r\nLocation:\x20/login\r\nPr
SF:agma:\x20no-cache\r\nSet-Cookie:\x20redirect_to=%2F;\x20Path=/;\x20Http
SF:Only;\x20SameSite=Lax\r\nX-Content-Type-Options:\x20nosniff\r\nX-Frame-
SF:Options:\x20deny\r\nX-Xss-Protection:\x201;\x20mode=block\r\nDate:\x20W
SF:ed,\x2019\x20Oct\x202022\x2019:26:14\x20GMT\r\nContent-Length:\x200\r\n
SF:\r\n")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-
SF:Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n40
SF:0\x20Bad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Re
SF:quest\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x
SF:20close\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie,67,"HTTP/
SF:1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charse
SF:t=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TLSSes
SF:sionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text
SF:/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20R
SF:equest")%r(Kerberos,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-T
SF:ype:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400
SF:\x20Bad\x20Request")%r(FourOhFourRequest,1A1,"HTTP/1\.0\x20302\x20Found
SF:\r\nCache-Control:\x20no-cache\r\nContent-Type:\x20text/html;\x20charse
SF:t=utf-8\r\nExpires:\x20-1\r\nLocation:\x20/login\r\nPragma:\x20no-cache
SF:\r\nSet-Cookie:\x20redirect_to=%2Fnice%2520ports%252C%2FTri%256Eity\.tx
SF:t%252ebak;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nX-Content-Type-Op
SF:tions:\x20nosniff\r\nX-Frame-Options:\x20deny\r\nX-Xss-Protection:\x201
SF:;\x20mode=block\r\nDate:\x20Wed,\x2019\x20Oct\x202022\x2019:26:41\x20GM
SF:T\r\nContent-Length:\x2029\r\n\r\n<a\x20href=\"/login\">Found</a>\.\n\n
SF:");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 146.07 seconds
```

Woo, a lot of information! Five ports open: ***22*** for **ssh**, ***80*** and ***3000*** for **http**, ***3306*** with a **mySQL** instance and ***7921*** unknown). Insert the usual domain (**ambassador.htb**) in the **/etc/hosts** file and proceed with the analysis.

### 80 - HTTP

![](https://www.secjuice.com/content/images/2022/10/img-00-1.png)![](https://www.secjuice.com/content/images/2022/10/img-01-1.png)

At first glance, it looks like a simple blog with just one post. The only message posted seems to give some clues on how to access via **ssh**, but it is not very clear, and despite some attempts, I cannot log in. I proceed with a simple **dirb** session.

```
┌──(in7rud3r㉿kali-muletto)-[~/Dropbox/hackthebox/_10.10.11.183 ...