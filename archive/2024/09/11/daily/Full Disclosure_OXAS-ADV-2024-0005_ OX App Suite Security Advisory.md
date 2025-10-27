---
title: OXAS-ADV-2024-0005: OX App Suite Security Advisory
url: https://seclists.org/fulldisclosure/2024/Sep/24
source: Full Disclosure
date: 2024-09-11
fetch_date: 2025-10-06T18:30:34.728319
---

# OXAS-ADV-2024-0005: OX App Suite Security Advisory

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

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

![](/shared/images/nst-icons.svg#search)

# OXAS-ADV-2024-0005: OX App Suite Security Advisory

---

*From*: Martin Heiland via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 9 Sep 2024 08:59:37 +0200 (CEST)

---

```
Dear subscribers,

We're sharing our latest advisory with you and like to thank everyone who contributed in finding and solving those
vulnerabilities. Feel free to join our bug bounty programs for OX App Suite, Dovecot and PowerDNS at YesWeHack.

This advisory has also been published at
https://documentation.open-xchange.com/appsuite/security/advisories/html/2024/oxas-adv-2024-0005.html.

Yours sincerely,
  Martin Heiland, Open-Xchange GmbH

Classification: TLP:GREEN

Internal reference: MWB-2534
Type: CWE-601 (URL Redirection to Untrusted Site ('Open Redirect'))
Component: backend
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX App Suite backend 7.10.6-rev66, OX App Suite backend 8.24.7
First fixed revision: OX App Suite backend 7.10.6-rev67, OX App Suite backend 8.24.8
Discovery date: 2024-03-05
Solution date: 2024-07-08
Disclosure date: 2024-07-08
CVE: CVE-2024-22243
CVSS: 8.1 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N)

Details:
CVE-2024-22243 Spring Framework URL Parsing with Host Validation. A "open redirect" vulnerability has been reported for
a version of the Spring Framework which is shipped with OX App Suite.

Risk:
Please see CVE-2024-22243 "Spring Framework URL Parsing with Host Validation" for more information by the vendor of the
affected third-party component. No publicly available exploits are known.

Solution:
The Spring framework shipped with OX App Suite and depending components has been updated as a precaution to avoid
exposure to CVE-2024-22243.
```

**Attachment:
[signature.asc](att-24/signature_asc.bin)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

### Current thread:

* **OXAS-ADV-2024-0005: OX App Suite Security Advisory** *Martin Heiland via Fulldisclosure (Sep 09)*

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