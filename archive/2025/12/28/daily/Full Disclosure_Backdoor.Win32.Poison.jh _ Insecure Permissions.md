---
title: Backdoor.Win32.Poison.jh / Insecure Permissions
url: https://seclists.org/fulldisclosure/2025/Dec/31
source: Full Disclosure
date: 2025-12-28
fetch_date: 2025-12-29T03:34:38.908783
---

# Backdoor.Win32.Poison.jh / Insecure Permissions

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

[![Previous](/images/left-icon-16x16.png)](30)
[By Date](date.html#31)
[![Next](/images/right-icon-16x16.png)](32)

[![Previous](/images/left-icon-16x16.png)](30)
[By Thread](index.html#31)
[![Next](/images/right-icon-16x16.png)](32)

![](/shared/images/nst-icons.svg#search)

# Backdoor.Win32.Poison.jh / Insecure Permissions

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Tue, 23 Dec 2025 01:22:37 -0500

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2025
Original source:
https://malvuln.com/advisory/3d9821cbe836572410b3c5485a7f76ca.txt
Malvuln Intelligence Feed: https://intel.malvuln.com/
Contact: malvuln13 () gmail com
Media: x.com/malvuln

Threat: Backdoor.Win32.Poison.jh
Vulnerability: Insecure Permissions
Description: The malware creates the directory 28463 under
C:\Windows\SysWOW64, granting Full (F) permissions to the Everyone
user group. This allows any local user to modify or replace any
dropped files, enabling trivial malware disruption or execution
hijacking. This reflects poor operational security exposing malware
components to local tampering.
Family: Poison
Type: PE32
Attack-pattern TTP: File and Directory Permissions Modification (T1222.001)
MD5: 3d9821cbe836572410b3c5485a7f76ca
SHA256: 2229d26afafb4b7fe1eaaa92ce1251c00eda9bac3f1371c470e7bbd5ae0a5bf9
Vuln ID: MVID-2025-0704
Dropped files: YJBE.exe
Disclosure: 12/23/2025

Exploit/PoC:
C:\>cacls C:\Windows\SysWOW64\28463\YJBE.exe
C:\Windows\SysWOW64\28463\YJBE.exe Everyone:(ID)F

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

[![Previous](/images/left-icon-16x16.png)](30)
[By Date](date.html#31)
[![Next](/images/right-icon-16x16.png)](32)

[![Previous](/images/left-icon-16x16.png)](30)
[By Thread](index.html#31)
[![Next](/images/right-icon-16x16.png)](32)

### Current thread:

* **Backdoor.Win32.Poison.jh / Insecure Permissions** *malvuln (Dec 27)*

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