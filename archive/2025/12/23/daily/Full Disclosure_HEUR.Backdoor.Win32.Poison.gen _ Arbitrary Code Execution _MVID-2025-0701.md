---
title: HEUR.Backdoor.Win32.Poison.gen / Arbitrary Code Execution /	MVID-2025-0701
url: https://seclists.org/fulldisclosure/2025/Dec/27
source: Full Disclosure
date: 2025-12-23
fetch_date: 2025-12-24T03:23:09.805349
---

# HEUR.Backdoor.Win32.Poison.gen / Arbitrary Code Execution /	MVID-2025-0701

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

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

![](/shared/images/nst-icons.svg#search)

# HEUR.Backdoor.Win32.Poison.gen / Arbitrary Code Execution / MVID-2025-0701

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Sat, 20 Dec 2025 23:16:48 -0500

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2025
Original source:
https://malvuln.com/advisory/b2e50fa38510a5ea8e11f614b1c1d0d5.txt
Malvuln Intelligence Feed: https://intel.malvuln.com/
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: HEUR.Backdoor.Win32.Poison.gen
Vulnerability: Arbitrary Code Execution
Description: The malware looks for and executes a x32-bit
"WININET.dll" PE file in its current directory. Therefore, we can
hijack the DLL and execute our own code to intercept and terminate the
malware. Leverage RansomLordNG v1.0 for DLL generation, while written
as a proof-of-concept to specifically defeat ransomware, these DLLs
may also defeat other types of malware if vulnerable. All basic tests
were conducted successfully in a virtual machine environment.
RansomLordNG v1.0 currently includes enhanced logging, memory dump and
deweaponize features.
Family: Poison
Type: PE32
Attack-pattern TTP: Hijack Execution Flow (T1574)
MD5: b2e50fa38510a5ea8e11f614b1c1d0d5
SHA256: 0de336f07cc19a6fda4cf9dacf1c4be0c6fb17158182d5274355cffa494ac8ed
Vuln ID: MVID-2025-0701
Disclosure: 12/20/2025
Exploit/PoC:
1) Download RansomLordNG v1.0
    https://github.com/malvuln/RansomLord
2) Locate the x32 WININET.dll entry using the -m flag (DLL Map)
3) Use -g flag (Generate Exploit) to output an DLL, based on an
existing vulnerable malware in the victims list.
4) (Optional) -e flag to setup Windows event IOC logging in the
registry, this will log the SHA256 hash, full path and filename.

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

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

### Current thread:

* **HEUR.Backdoor.Win32.Poison.gen / Arbitrary Code Execution / MVID-2025-0701** *malvuln (Dec 22)*

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