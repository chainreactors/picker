---
title: OXAS-ADV-2025-0002: OX App Suite Security Advisory
url: https://seclists.org/fulldisclosure/2025/Nov/12
source: Full Disclosure
date: 2025-11-07
fetch_date: 2025-11-08T03:06:36.791693
---

# OXAS-ADV-2025-0002: OX App Suite Security Advisory

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# OXAS-ADV-2025-0002: OX App Suite Security Advisory

---

*From*: Martin Heiland via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 31 Oct 2025 11:10:38 +0100 (CET)

---

```
Dear subscribers,

We're sharing our latest advisory with you and like to thank everyone who contributed in finding and solving those
vulnerabilities. Feel free to join our bug bounty programs for OX App Suite, Dovecot and PowerDNS at YesWeHack.

This advisory has also been published at
https://documentation.open-xchange.com/appsuite/security/advisories/html/2025/oxas-adv-2025-0002.html.

Yours sincerely,
  Martin Heiland, Open-Xchange GmbH

Classification: TLP:GREEN

Internal reference: appsuite/platform/core#336
Type: CWE-1021 (Improper Restriction of Rendered UI Layers or Frames)
Component: backend
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX App Suite backend 7.6.3-rev77, OX App Suite backend 8.35.111, OX App Suite backend 8.38.82,
OX App Suite backend 8.39.79, OX App Suite backend 8.40.57
First fixed revision: OX App Suite backend 7.6.3-rev78, OX App Suite backend 8.35.112, OX App Suite backend 8.38.83, OX
App Suite backend 8.39.80, OX App Suite backend 8.40.58
Discovery date: 2025-07-09
Solution date: 2025-07-10
CVE: CVE-2025-30191
CVSS: 5.4 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N)

Details:
HTML "form" elements can be used for spoofing and redressing. Malicious content from E-Mail can be used to perform a
redressing attack.

Risk:
Users can be tricked to perform unintended actions or provide sensitive information to a third party which would enable
further threats. No publicly available exploits are known

Solution:
Attribute values containing HTML fragments are now denied by the sanitization procedure.

---

Internal reference: appsuite/support#763
Type: CWE-400 (Uncontrolled Resource Consumption)
Component: ui middleware
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX App Suite ui middleware 2.1.7
First fixed revision: OX App Suite ui middleware 2.1.8
Discovery date: 2025-08-06
Solution date: 2025-08-12
CVE: CVE-2025-30188
CVSS: 7.5 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H)

Details:
Version information can be used to pollute caches and cause denial of service. Malicious or unintentional API requests
can be used to add significant amount of data to caches.

Risk:
Caches may evict information that is required to operate the web frontend, which leads to unavailability of the
component. No publicly available exploits are known

Solution:
Please deploy the provided updates and patch releases.
```

**Attachment:
[signature.asc](att-12/signature_asc.bin)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

### Current thread:

* **OXAS-ADV-2025-0002: OX App Suite Security Advisory** *Martin Heiland via Fulldisclosure (Nov 07)*

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