---
title: Defense in depth -- the Microsoft way (part 91): yet another	30 year old bug of the "Properties" shell extension
url: https://seclists.org/fulldisclosure/2025/Aug/2
source: Full Disclosure
date: 2025-08-06
fetch_date: 2025-10-07T00:50:24.843928
---

# Defense in depth -- the Microsoft way (part 91): yet another	30 year old bug of the "Properties" shell extension

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

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# Defense in depth -- the Microsoft way (part 91): yet another 30 year old bug of the "Properties" shell extension

---

*From*: Stefan Kanthak via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 3 Aug 2025 19:47:08 +0200

---

```
Hi @ll,

this extends the previous post titled Defense in depth -- the
Microsoft way (part 90): "Digital Signature" property sheet
missing without "Read Extended Attributes" access permission
<https://seclists.org/fulldisclosure/2025/Jul/39>, to document
another facette of this 30 year old bug in the "Properties" shell
extension.

About 35 years ago Microsoft began to implement their "New Technology
File System" (NTFS) for their upcoming Windows NT operating system.
NTFS supports the extended attributes of the HPFS file system which
Microsoft and IBM had developed for their OS/2 operating system before.
NTFS' initial version, released with Windows NT 3.1 in 1993, had no
access control and did not support named (alternate) data streams;
both were added for Windows NT 3.5, released one year later, with
separate access permissions for reading or writing data streams,
attributes and extended attributes
(<https://msdn.microsoft.com/en-us/library/aa364404.aspx> and
<https://technet.microsoft.com/en-us/library/cc783530.aspx>).

Internet Explorer 4.0, introduced about 30 years ago, began to add
the "mark of the web" to files downloaded from the Internet -- an
alternate data stream named "Zone.Identifier"
(<https://msdn.microsoft.com/en-us/library/ms537628.aspx>).

At the same time Microsoft replaced the file manager as well as the
program manager shipped with their Windows operating systems by
"Windows Explorer", the graphical shell of Windows since then.

For files with a "mark of the web", its "Properties" shell extension
is supposed to show the message

| Security    This file came from another            [ Unblock ]
|             computer and might be blocked to               Â¯
|             help protect this computer.

on its "General" property sheet, including the button [Unblock] to
remove the "mark of the web".

This message is but not displayed if the "Read Extended Attributes"
permission is not granted, despite that it is NOT required to read
the files' data streams!

stay tuned, and far away from bug-riddled software
Stefan Kanthak

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

### Current thread:

* **Defense in depth -- the Microsoft way (part 91): yet another 30 year old bug of the "Properties" shell extension** *Stefan Kanthak via Fulldisclosure (Aug 04)*

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