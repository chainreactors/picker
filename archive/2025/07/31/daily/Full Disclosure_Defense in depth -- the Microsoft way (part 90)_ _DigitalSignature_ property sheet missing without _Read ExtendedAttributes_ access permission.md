---
title: Defense in depth -- the Microsoft way (part 90): "Digital	Signature" property sheet missing without "Read Extended	Attributes" access permission
url: https://seclists.org/fulldisclosure/2025/Jul/39
source: Full Disclosure
date: 2025-07-31
fetch_date: 2025-10-06T23:56:28.326740
---

# Defense in depth -- the Microsoft way (part 90): "Digital	Signature" property sheet missing without "Read Extended	Attributes" access permission

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

[![Previous](/images/left-icon-16x16.png)](38)
[By Date](date.html#39)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](38)
[By Thread](index.html#39)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Defense in depth -- the Microsoft way (part 90): "Digital Signature" property sheet missing without "Read Extended Attributes" access permission

---

*From*: Stefan Kanthak via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Jul 2025 18:22:02 +0200

---

```
Hi @ll,

about 35 years ago Microsoft began to implement their "New Technology
File System" (NTFS) for their upcoming Windows NT operating system.
NTFS supports the extended attributes of the HPFS file system which
Microsoft and IBM had developed for their OS/2 operating system before.
NTFS' initial version, released with Windows NT 3.1 in 1993, had no
access control; this was added for Windows NT 3.5, released one year
later, with separate access permissions for reading or writing data,
attributes and extended attributes
(<https://technet.microsoft.com/en-us/library/cc783530.aspx>).

About 30 years ago Microsoft introduced "Authenticode" to sign portable
executable image files (.AX, .DLL, .EXE, .OCX, .SYS, ...), cabinet
archive files (.CAB, .MSU, ...) and installer package files (.MSI, .MSP,
...) using X.509 digital certificates.
Authenticode signatures are embedded into the files' data.

At the same time Microsoft replaced the file manager as well as the
program manager shipped with their Windows operating systems by
"Windows Explorer", the graphical shell of Windows since then.
For files with embedded Authenticode signature its "Properties" shell
extension is supposed to show a property sheet "Digital Signature".

This but fails unless the "Read Extended Attributes" permission is
granted, despite this permission is NOT required to read the files'
data including any Authenticode signature.

stay tuned, and far away from bug-riddled software
Stefan Kanthak
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](38)
[By Date](date.html#39)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](38)
[By Thread](index.html#39)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **Defense in depth -- the Microsoft way (part 90): "Digital Signature" property sheet missing without "Read Extended Attributes" access permission** *Stefan Kanthak via Fulldisclosure (Jul 29)*

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