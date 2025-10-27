---
title: BBOT 2.1.0 - Local Privilege Escalation via Malicious Module	Execution
url: https://seclists.org/fulldisclosure/2025/Apr/19
source: Full Disclosure
date: 2025-04-25
fetch_date: 2025-10-06T22:08:14.152553
---

# BBOT 2.1.0 - Local Privilege Escalation via Malicious Module	Execution

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# BBOT 2.1.0 - Local Privilege Escalation via Malicious Module Execution

---

*From*: Housma mardini <housma () gmail com>
*Date*: Fri, 18 Apr 2025 16:12:49 +0400

---

```
Hi Full Disclosure,

I'd like to share a local privilege escalation technique involving BBOT
(Bighuge BLS OSINT Tool) when misconfigured with sudo access.

---

Exploit Title: BBOT 2.1.0 - Local Privilege Escalation via Malicious Module
Execution
Date: 2025-04-16
Exploit Author: Huseyin Mardinli
Vendor Homepage: https://github.com/blacklanternsecurity/bbot
Version: 2.1.0.4939rc (tested)
Tested on: Kali Linux Rolling (2025.1)
CVE: N/A
Platform: Linux
Type: Local

### Description:

BBOT allows execution of custom Python modules during OSINT scans. When
configured as a sudo-executable (e.g., via NOPASSWD), a malicious module
can escalate privileges via the `setup()` function.

### PoC Steps:

1. Clone:
   git clone https://github.com/Housma/bbot-privesc.git

2. Run with sudo:
   sudo /usr/local/bin/bbot -t dummy.com -p preset.yml --event-types ROOT

3. A root shell is spawned via `bash -p` from within the module.

### GitHub (Full Write-up + PoC):
https://github.com/Housma/bbot-privesc

---

This exploit highlights how trusted open-source tools can be abused in
real-world environments.

Regards,
Huseyin Mardinli
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](20)

### Current thread:

* **BBOT 2.1.0 - Local Privilege Escalation via Malicious Module Execution** *Housma mardini (Apr 23)*

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