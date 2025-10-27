---
title: libelf 0.8.12 Stack-based buffer overflow in gmo2msg (libelf) via unbounded sprintf of lang argument
url: https://seclists.org/fulldisclosure/2025/Sep/64
source: Full Disclosure
date: 2025-09-24
fetch_date: 2025-10-02T20:36:11.665334
---

# libelf 0.8.12 Stack-based buffer overflow in gmo2msg (libelf) via unbounded sprintf of lang argument

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

[![Previous](/images/left-icon-16x16.png)](63)
[By Date](date.html#64)
[![Next](/images/right-icon-16x16.png)](65)

[![Previous](/images/left-icon-16x16.png)](63)
[By Thread](index.html#64)
[![Next](/images/right-icon-16x16.png)](65)

![](/shared/images/nst-icons.svg#search)

# libelf 0.8.12 Stack-based buffer overflow in gmo2msg (libelf) via unbounded sprintf of lang argument

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Fri, 19 Sep 2025 22:24:20 -0400

---

```
gmo2msg in libelf contains a stack-based buffer overflow in po/gmo2msg.c
when constructing filenames from the first program argument (lang). The
program uses a fixed-size local buffer (char buf[1024]) and writes into it
using sprintf(buf, "%s.gmo", lang) and sprintf(buf, "%s.msg", lang) without
validating the length of lang. Supplying a sufficiently long lang argument
(e.g., ~1200 bytes) causes sprintf to write past the end of buf, leading to
a stack-buffer-overflow that crashes the process and may enable code
execution under favorable conditions.

*Impact:*

   -

   Immediate, reproducible crash when passing a long lang argument.
   -

   If the binary is executed in a privileged context (e.g., run by a
   privileged service, installed setuid, package scripts), or on targets with
   downgraded exploit mitigations, a reliable exploit may be feasible.
   -

   Memory corruption could be used as a primitive in a larger exploit chain.

*Proof of Concept:*

./gmo2msg "$(python3 -c 'print("A"*1200)')"

*Output:*

=================================================================
==11304==ERROR: AddressSanitizer: stack-buffer-overflow on address ...
WRITE of size 1205 at ...
    #0 0x... in vsprintf (...)
    #1 0x... in sprintf (...)
    #2 0x... in main /root/libelf/./po/gmo2msg.c:64:5
...
This frame has 1 object(s):
  [32, 1056) 'buf' (line 40) <== Memory access at offset 1056 overflows
this variable
SUMMARY: AddressSanitizer: stack-buffer-overflow ... in vsprintf
==11304==ABORTING
Aborted
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](63)
[By Date](date.html#64)
[![Next](/images/right-icon-16x16.png)](65)

[![Previous](/images/left-icon-16x16.png)](63)
[By Thread](index.html#64)
[![Next](/images/right-icon-16x16.png)](65)

### Current thread:

* **libelf 0.8.12 Stack-based buffer overflow in gmo2msg (libelf) via unbounded sprintf of lang argument** *Ron E (Sep 22)*

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