---
title: HTB Soccer Walkthrough
url: https://www.secjuice.com/htb-soccer-walkthrough/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-26
fetch_date: 2025-10-06T19:22:21.327690
---

# HTB Soccer Walkthrough

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

[TECHNICAL](/tag/technical/)

# HTB Soccer Walkthrough

Learn how to break into a soccer portal using vulnerabilities in the Tiny File Manager hidden route.

* [![Andy74](/content/images/size/w100/2020/01/avatar.png)](/author/andy74/)

#### [Andy74](/author/andy74/)

Nov 24, 2024
• 33 min read

![HTB Soccer Walkthrough](/content/images/size/w2000/2024/11/turkeys-doing-Cirque-du-Soleil-with-trapeze.png)

Turkeys performing at a modern circus show. Microsoft Copilot created this image.

A nice BOX, very average, to which however I would like to draw your attention because this BOX was the subject of another very interesting article, also published here on Secjuice, where ChatGPT, the AI that is having great success in this period, helped me to capture the first flag of the CTF. I'll leave you the [link](https://www.secjuice.com/) here. And now, let's get started.

The **nmap** scan:

```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-06 10:42 EST
Nmap scan report for 10.10.11.194
Host is up (0.11s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE         VERSION
22/tcp   open  ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 ad0d84a3fdcc98a478fef94915dae16d (RSA)
|   256 dfd6a39f68269dfc7c6a0c29e961f00c (ECDSA)
|_  256 5797565def793c2fcbdb35fff17c615c (ED25519)
80/tcp   open  http            nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://soccer.htb/
|_http-server-header: nginx/1.18.0 (Ubuntu)
9091/tcp open  xmltec-xmlmail?
| fingerprint-strings:
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Help, RPCCheck, SSLSessionReq, drda, informix:
|     HTTP/1.1 400 Bad Request
|     Connection: close
|   GetRequest:
|     HTTP/1.1 404 Not Found
|     Content-Security-Policy: default-src 'none'
|     X-Content-Type-Options: nosniff
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 139
|     Date: Fri, 06 Jan 2023 15:42:02 GMT
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error</title>
|     </head>
|     <body>
|     <pre>Cannot GET /</pre>
|     </body>
|     </html>
|   HTTPOptions, RTSPRequest:
|     HTTP/1.1 404 Not Found
|     Content-Security-Policy: default-src 'none'
|     X-Content-Type-Options: nosniff
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 143
|     Date: Fri, 06 Jan 2023 15:42:02 GMT
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error</title>
|     </head>
|     <body>
|     <pre>Cannot OPTIONS /</pre>
|     </body>
|_    </html>
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9091-TCP:V=7.93%I=7%D=1/6%Time=63B84168%P=x86_64-pc-linux-gnu%r(inf
SF:ormix,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20close\r\
SF:n\r\n")%r(drda,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x2
SF:0close\r\n\r\n")%r(GetRequest,168,"HTTP/1\.1\x20404\x20Not\x20Found\r\n
SF:Content-Security-Policy:\x20default-src\x20'none'\r\nX-Content-Type-Opt
SF:ions:\x20nosniff\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nCon
SF:tent-Length:\x20139\r\nDate:\x20Fri,\x2006\x20Jan\x202023\x2015:42:02\x
SF:20GMT\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x20html>\n<html\x20lang=
SF:\"en\">\n<head>\n<meta\x20charset=\"utf-8\">\n<title>Error</title>\n</h
SF:ead>\n<body>\n<pre>Cannot\x20GET\x20/</pre>\n</body>\n</html>\n")%r(HTT
SF:POptions,16C,"HTTP/1\.1\x20404\x20Not\x20Found\r\nContent-Security-Poli
SF:cy:\x20default-src\x20'none'\r\nX-Content-Type-Options:\x20nosniff\r\nC
SF:ontent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Length:\x20143\r
SF:\nDate:\x20Fri,\x2006\x20Jan\x202023\x2015:42:02\x20GMT\r\nConnection:\
SF:x20close\r\n\r\n<!DOCTYPE\x20html>\n<html\x20lang=\"en\">\n<head>\n<met
SF:a\x20charset=\"utf-8\">\n<title>Error</title>\n</head>\n<body>\n<pre>Ca
SF:nnot\x20OPTIONS\x20/</pre>\n</body>\n</html>\n")%r(RTSPRequest,16C,"HTT
SF:P/1\.1\x20404\x20Not\x20Found\r\nContent-Security-Policy:\x20default-sr
SF:c\x20'none'\r\nX-Content-Type-Options:\x20nosniff\r\nContent-Type:\x20t
SF:ext/html;\x20charset=utf-8\r\nContent-Length:\x20143\r\nDate:\x20Fri,\x
SF:2006\x20Jan\x202023\x2015:42:02\x20GMT\r\nConnection:\x20close\r\n\r\n<
SF:!DOCTYPE\x20html>\n<html\x20lang=\"en\">\n<head>\n<meta\x20charset=\"ut
SF:f-8\">\n<title>Error</title>\n</head>\n<body>\n<pre>Cannot\x20OPTIONS\x
SF:20/</pre>\n</body>\n</html>\n")%r(RPCCheck,2F,"HTTP/1\.1\x20400\x20Bad\
SF:x20Request\r\nConnection:\x20close\r\n\r\n")%r(DNSVersionBindReqTCP,2F,
SF:"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20close\r\n\r\n")%r
SF:(DNSStatusRequestTCP,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnecti
SF:on:\x20close\r\n\r\n")%r(Help,2F,"HTTP/1\.1\x20400\x20Bad\x20Request\r\
SF:nConnection:\x20close\r\n\r\n")%r(SSLSessionReq,2F,"HTTP/1\.1\x20400\x2
SF:0Bad\x20Request\r\nConnection:\x20close\r\n\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.06 seconds
```

And let's move immediately to the portal (port ***80***), which will certainly be our access point, of course, not before adding the "**soccer.htb**" domain to our **/etc/hosts** file.

![](https://www.secjuice.com/content/images/2023/02/img-00.png)

A football portal.

> And here, a sore point about me that I have to tell to allow those who have been following me for many time to get to know me better. Well, although football is the national sport of my homeland, ahimè, I don't follow football. Well yes, swimming against the tide, unfortunately as a bad Italian that I am, I'm not that passionate about sport and above all about football which I really don't like. After the digression, let's go back to our BOX.

There is nothing particular from **wappalyzer**.

![](https://www.secjuice.com/content/images/2023/02/img-01.png)

A simple **gobuster** scan for hidden routes.

```
┌──(in7rud3r㉿kali-muletto)-[~/Dropbox/hackthebox]
└─$ gobuster dir -u http://soccer.htb -w /usr/share/dirb/wordlists/common.txt
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://soccer.htb
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.4
[+] Timeout:                 10s
===============================================================
2023/01/06 12:40:23 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 162]
/.htaccess            (Status: 403) [Size: 162]
/.htpasswd            (Status: 403) [Size: 162]
/index.html           (Status: 200) [Size: 6917]
Progress: 4611 / 4615 (99.91%)
===============================================================
2023/01/06 12:41:16 Finished...