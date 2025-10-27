---
title: RAVEN 2 Walkthrough (OSWE like machine )
url: https://infosecwriteups.com/raven-2-walkthrough-oswe-like-machine-98bdfc62b9bf?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-02
fetch_date: 2025-10-04T00:17:17.229474
---

# RAVEN 2 Walkthrough (OSWE like machine )

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F98bdfc62b9bf&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fraven-2-walkthrough-oswe-like-machine-98bdfc62b9bf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fraven-2-walkthrough-oswe-like-machine-98bdfc62b9bf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-98bdfc62b9bf---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-98bdfc62b9bf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# RAVEN 2 Walkthrough (OSWE like machine )

[![Hashar Mujahid](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*eIN8F1x85V9OMBf50NuoLg.gif)](https://hasharmujahid.medium.com/?source=post_page---byline--98bdfc62b9bf---------------------------------------)

[Hashar Mujahid](https://hasharmujahid.medium.com/?source=post_page---byline--98bdfc62b9bf---------------------------------------)

10 min read

·

Nov 30, 2022

--

Listen

Share

Hi! My name is Hashar Mujahid and Today we are going to solve a room from vulnhub which is listed as OSWE like machine by TJ-Null.

Press enter or click to view image in full size

![]()

Raven

## **ENUMERATION:**

### HOST DISCOVERY:

We will start with discovering potential targets on our network. We can use multiple tools for this purpose like netdiscover, fping or nmap.

```
fping -a -g 192.168.59.0/24 2>/dev/null

root@kali:/home/kali/Desktop/ctfs/Raven2-Vulnhun# fping -a -g 192.168.59.0/24 2>/dev/null
192.168.59.1
192.168.59.2
192.168.59.128
192.168.59.130 ==> HOST IP ADRESS
```

We can perform the same thing with nmap.

```
root@kali:/home/kali/Desktop/ctfs/Raven2-Vulnhun# nmap -sn 192.168.59.0/24
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-30 02:40 EST
Nmap scan report for 192.168.59.1
Host is up (0.00067s latency).
MAC Address: 00:50:56:C0:00:08 (VMware)
Nmap scan report for 192.168.59.2
Host is up (0.00054s latency).
MAC Address: 00:50:56:E4:EA:5C (VMware) ===> Target
Nmap scan report for 192.168.59.128
Host is up (0.00061s latency).
MAC Address: 00:0C:29:7A:56:5E (VMware)
Nmap scan report for 192.168.59.254
Host is up (0.00056s latency).
MAC Address: 00:50:56:FE:B2:BF (VMware)
Nmap scan report for 192.168.59.130
Host is up.
Nmap done: 256 IP addresses (5 hosts up) scanned in 4.76 seconds
```

Now we have our target’s ip address. Next thing we want to do is to run a port scan to see which ports are open and what services are being run on those ports.

### PORT SCAN:

We can use nmap to perform this task for us.

```
root@kali:/home/kali/Desktop/ctfs/Raven2-Vulnhun# sudo nmap -sC -sV -p- -oN nmap/scan 192.168.59.128
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-30 02:44 EST
Stats: 0:00:04 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 30.47% done; ETC: 02:45 (0:00:07 remaining)
Nmap scan report for 192.168.59.128
Host is up (0.00087s latency).
Not shown: 65531 closed tcp ports (reset)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 6.7p1 Debian 5+deb8u4 (protocol 2.0)
| ssh-hostkey:
|   1024 2681c1f35e01ef93493d911eae8b3cfc (DSA)
|   2048 315801194da280a6b90d40981c97aa53 (RSA)
|   256 1f773119deb0e16dca77077684d3a9a0 (ECDSA)
|_  256 0e8571a8a2c308699c91c03f8418dfae (ED25519)
80/tcp    open  http    Apache httpd 2.4.10 ((Debian))
|_http-title: Raven Security
|_http-server-header: Apache/2.4.10 (Debian)
111/tcp   open  rpcbind 2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          36026/tcp6  status
|   100024  1          42894/tcp   status
|   100024  1          49163/udp6  status
|_  100024  1          54484/udp   status
42894/tcp open  status  1 (RPC #100024)
MAC Address: 00:0C:29:7A:56:5E (VMware)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.36 seconds
```

Our Target is running SSH service on port 22 a web server on port 80 and rpc on 111 and 42894.

We should also perform a udp scan.

```
root@kali:/home/kali/Desktop/ctfs/Raven2-Vulnhun# sudo nmap -sU -oN nmap/udp-scan 192.168.59.128
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-30 02:48 EST
Stats: 0:02:15 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 2.49% done; ETC: 04:20 (1:28:55 remaining)
Nmap scan report for 192.168.59.128
Host is up (0.00087s latency).
Not shown: 997 closed udp ports (port-unreach)
PORT     STATE         SERVICE
68/udp   open|filtered dhcpc
111/udp  open          rpcbind
1007/udp open|filtered unknown
MAC Address: 00:0C:29:7A:56:5E (VMware)

Nmap done: 1 IP address (1 host up) scanned in 1218.88 seconds
```

Let’s enumerate these services.

### WEB ENUMERATION:

We have a webserver running at port 80 let’s visit it and find some usefull information.

Press enter or click to view image in full size

![]()

### Directory Scan:

We can use dirsearch to search for directories.

```
root@kali:/home/kali/Desktop/ctfs/Raven2-Vulnhun# dirsearch --url http://192.168.59.128/

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10927

Output File: /root/.dirsearch/reports/192.168.59.128/-_22-11-30_04-59-53.txt

Error Log: /root/.dirsearch/logs/errors-22-11-30_04-59-53.log

Target: http://192.168.59.128/

[04:59:53] Starting:
[04:59:54] 301 -  313B  - /js  ->  http://192.168.59.128/js/
[04:59:55] 200 -   18KB - /.DS_Store
[05:00:09] 200 -   13KB - /about.html
[05:00:42] 200 -    9KB - /contact.php
[05:00:45] 301 -  314B  - /css  ->  http://192.168.59.128/css/
[05:00:59] 301 -  316B  - /fonts  ->  http://192.168.59.128/fonts/
[05:01:06] 301 -  314B  - /img  ->  http://192.168.59.128/img/
[05:01:07] 200 -   16KB - /index.html
[05:01:10] 200 -    4KB - /js/
[05:01:19] 301 -  317B  - /manual  ->  http://192.168.59.128/manual/
[05:01:19] 200 -  626B  - /manual/index.html
[05:01:48] 403 -  302B  - /server-status
[05:01:48] 403 -  303B  - /server-status/
[05:02:06] 200 -    5KB - /vendor/
[05:02:10] 200 -    2KB - /wordpress/wp-login.php
[05:02:11] 200 -   51KB - /wordpress/bash
```

Visiting the directories to find some interesting information. Found some interesting information in `/vendor` directory.

!...