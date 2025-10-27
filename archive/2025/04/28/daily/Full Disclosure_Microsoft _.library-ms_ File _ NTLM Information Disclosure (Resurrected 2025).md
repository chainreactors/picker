---
title: Microsoft ".library-ms" File / NTLM Information Disclosure (Resurrected 2025)
url: https://seclists.org/fulldisclosure/2025/Apr/28
source: Full Disclosure
date: 2025-04-28
fetch_date: 2025-10-06T22:05:29.398184
---

# Microsoft ".library-ms" File / NTLM Information Disclosure (Resurrected 2025)

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

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

![](/shared/images/nst-icons.svg#search)

# Microsoft ".library-ms" File / NTLM Information Disclosure (Resurrected 2025)

---

*From*: hyp3rlinx <apparitionsec () gmail com>
*Date*: Fri, 25 Apr 2025 23:27:56 -0400

---

```
[-] Microsoft ".library-ms" File / NTLM Information Disclosure
Spoofing (Resurrected 2025) / CVE-2025-24054

[+] John Page (aka hyp3rlinx)
[+] x.com/hyp3rlinx
[+] ISR: ApparitionSec

Back in 2018, I reported a ".library-ms" File NTLM information
disclosure vulnerability to MSRC and was told "it was not severe
enough", that being said I post it anyways. Seven years passed, until
other researchers re-reported it. Subsequently this security flaw was
finally deemed important by Microsoft and it received CVE-2025-24054,
for which I was finally retroactively credited as the original
reporter.

Circa 2025 updated:
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-24054

[References]
https://web.archive.org/web/20190106181024/https://hyp3rlinx.altervista.org/advisories/MICROSOFT-WINDOWS-.LIBRARY-MS-FILETYPE-INFORMATION-DISCLOSURE.txt
https://packetstorm.news/files/id/148556/
https://cxsecurity.com/issue/WLB-2018070160

[Network Access]
Remote

[Original Disclosure Timeline]
Vendor Notification:  Jun 29, 2018
MSRC Response:   Jul 12, 2018  "risk is not severe enough to justify
immediate servicing."
July 14, 2018 : Public Disclosure

[+] Disclaimer
The information contained within this advisory is supplied "as-is"
with no warranties or guarantees of fitness of use or otherwise.
Permission is hereby granted for the redistribution of this advisory,
provided that it is not altered except by reformatting it, and that
due credit is given. Permission is explicitly given for insertion in
vulnerability databases and similar, provided that due credit is given
to the author. The author is not responsible for any misuse of the
information contained herein and accepts no responsibility for any
damage caused by the use or misuse of this information. The author
prohibits any malicious use of security related information or
exploits by the author or elsewhere. All content copyright (c).

hyp3rlinx
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

### Current thread:

* **Microsoft ".library-ms" File / NTLM Information Disclosure (Resurrected 2025)** *hyp3rlinx (Apr 26)*

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