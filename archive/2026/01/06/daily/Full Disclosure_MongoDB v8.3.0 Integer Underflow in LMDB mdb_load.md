---
title: MongoDB v8.3.0 Integer Underflow in LMDB mdb_load
url: https://seclists.org/fulldisclosure/2026/Jan/8
source: Full Disclosure
date: 2026-01-06
fetch_date: 2026-01-07T03:30:40.915012
---

# MongoDB v8.3.0 Integer Underflow in LMDB mdb_load

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# MongoDB v8.3.0 Integer Underflow in LMDB mdb\_load

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Wed, 31 Dec 2025 23:17:45 -0500

---

```
This integer underflow vulnerability enables heap metadata corruption and
information disclosure through carefully crafted LMDB dump files.

*Impact:*

   - *Denial of Service*: Immediate crash (confirmed)
   - *Information Disclosure*: Heap metadata leak via OOB read

Root Cause:The readline() function fails to validate that the input line
length is non-zero before performing decrement operations, causing integer
underflow. An attacker can craft a malicious LMDB dump file containing
empty lines that trigger the vulnerability when processed by mdb_load:
*Output:*

./mdb_load -T /tmp/lmdb_asan <
/root/wiredtiger/third_party/openldap_liblmdb/findings/default/crashes/id:000007,sig:06,src:000012+000030,time:43032,execs:522id:000007,sig:06,src:000012+000030,time:43032,execs:52230,op:splice,rep:13
mdb_load.c:214:9: runtime error: addition of unsigned offset to
0x521000000100 overflowed to 0x5210000000ff
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior mdb_load.c:214:9
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

### Current thread:

* **MongoDB v8.3.0 Integer Underflow in LMDB mdb\_load** *Ron E (Jan 05)*

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