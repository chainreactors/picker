---
title: HTB Support Walkthrough
url: https://www.secjuice.com/htb-support-walkthrough/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-03
fetch_date: 2025-10-06T18:27:26.715477
---

# HTB Support Walkthrough

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

# HTB Support Walkthrough

Observe how to use Rubeus to break into an Active Directory server.

* [![Andy74](/content/images/size/w100/2020/01/avatar.png)](/author/andy74/)

#### [Andy74](/author/andy74/)

Sep 2, 2024
• 36 min read

![HTB Support Walkthrough](/content/images/size/w2000/2024/09/secjuice-labor-day04.png)

This image was generated using Microsoft Copilot.

Windows machines are always very interesting to investigate because they have specific attacks that clearly stand out from Linux machines. Sometimes the solution to identifying their attacks is at your fingertips, but choosing the right method to arrive at the answer takes a lot more time than expected. Thus, a lot of time was wasted on finding the solution to this machine towards the end when I already had the solution right at my fingertips. Nonetheless, the fun was certainly not lacking.

As usually happens on a Windows machine, the **nmap** scan reveals a myriad of open ports.

```
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-28 11:30 CEST
Nmap scan report for 10.10.11.174
Host is up (0.11s latency).
Not shown: 989 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-08-28 09:13:39Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: support.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: support.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: -17m25s
| smb2-time:
|   date: 2022-08-28T09:13:46
|_  start_date: N/A
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 75.97 seconds
```

Start to analyze them all and try to find out what they hide, but first of all insert the htb domain for this BOX (**support.htb**) in our **/etc/hosts** file.

#### Port 53 - DNS

There is a **DNS** server on this port, so we can query it for the base records registered within it.

```
┌──(in7rud3r㉿kali-muletto)-[~/Dropbox/hackthebox/_10.10.11.174 - Support (win)]
└─$ dig version.bind CHAOS TXT @10.10.11.174

; <<>> DiG 9.18.4-2-Debian <<>> version.bind CHAOS TXT @10.10.11.174
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOTIMP, id: 59086
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 674839c2a602b51c (echoed)
;; QUESTION SECTION:
;version.bind.                  CH      TXT

;; Query time: 108 msec
;; SERVER: 10.10.11.174#53(10.10.11.174) (UDP)
;; WHEN: Sun Aug 28 11:34:30 CEST 2022
;; MSG SIZE  rcvd: 53
```

Nothing so interesting; let's go a little deeper and scan and interrogate the service on all the records. I recently "played" on another BOX Windows, and I had prepared a little script **sh** that did just this thing; let's take it back and modify it ad hoc for this specific scenario.

```
┌──(in7rud3r㉿kali-muletto)-[~/…/hackthebox/_10.10.11.174 - Support (win)/attack/dns]
└─$ cat scan.sh
dig ANY @10.10.11.174 support.htb     #Any information
dig A @10.10.11.174 support.htb       #Regular DNS request
dig AAAA @10.10.11.174 support.htb    #IPv6 DNS request
dig TXT @10.10.11.174 support.htb     #Informaeion
dig MX @10.10.11.174 support.htb      #Emails related
dig NS @10.10.11.174 support.htb      #DNS that resolves that name
dig -x 10.10.11.174 @10.10.11.174   #Reverse lookup

┌──(in7rud3r㉿kali-muletto)-[~/…/hackthebox/_10.10.11.174 - Support (win)/attack/dns]
└─$ ./scan.sh

; <<>> DiG 9.18.4-2-Debian <<>> ANY @10.10.11.174 support.htb
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 23563
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 2

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;support.htb.                   IN      ANY

;; ANSWER SECTION:
support.htb.            600     IN      A       10.10.11.174
support.htb.            3600    IN      NS      dc.support.htb.
support.htb.            3600    IN      SOA     dc.support.htb. hostmaster.support.htb. 105 900 600 86400 3600

;; ADDITIONAL SECTION:
dc.support.htb.         3600    IN      A       10.10.11.174

;; Query time: 108 msec
;; SERVER: 10.10.11.174#53(10.10.11.174) (TCP)
;; WHEN: Sun Aug 28 11:46:39 CEST 2022
;; MSG SIZE  rcvd: 136

; <<>> DiG 9.18.4-2-Debian <<>> A @10.10.11.174 support.htb
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 18114
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;support.htb.                   IN      A

;; ANSWER SECTION:
support.htb.            600     IN      A       10.10.11.174

;; Query time: 108 msec
;; SERVER: 10.10.11.174#53(10.10.11.174) (UDP)
;; WHEN: Sun Aug 28 11:46:39 CEST 2022
;; MSG SIZE  rcvd: 56

; <<>> DiG 9.18.4-2-Debian <<>> AAAA @10.10.11.174 support.htb
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 38798
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;support.htb.                   IN      AAAA

;; AUTHORITY SECTION:
support.htb.            3600    IN      SOA     dc.support.htb. hostmaster.support.htb. 105 900 600 86400 3600

;; Query time: 108 msec
;; SERVER: 10.10.11.174#53(10.10.11.174) (UDP)
;; WHEN: Sun Aug 28 11:46:39 CEST 2022
;; MSG SIZE  rcvd: 90

; <<>> DiG 9.18.4-2-Debian <<>> TXT @10.10.11.174 support.htb
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 14509
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;support.htb.                   IN      TXT

;; AUTHORITY SECTION:
support.htb.            3600    IN      SOA     dc.support.htb. hostmaster.support.htb. 105 900 600 86400 3600

;; Query time: 108 msec
;; SERVER: 10.10.11.174#53(10.10.11.174) (UDP)
;; WHEN: Sun Aug 28 11:46:39 CEST 2022
;; MSG SIZE  rcvd: 90

; <<>> DiG 9.18.4-2-Debian <<>> MX @10.10.11.174 support.htb
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 15656
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;support.htb.                   IN      MX

;; AUTHORITY SECTION:
support.htb.            3600    IN      SOA     dc.supp...