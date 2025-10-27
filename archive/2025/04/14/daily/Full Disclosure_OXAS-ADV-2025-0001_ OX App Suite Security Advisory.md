---
title: OXAS-ADV-2025-0001: OX App Suite Security Advisory
url: https://seclists.org/fulldisclosure/2025/Apr/14
source: Full Disclosure
date: 2025-04-14
fetch_date: 2025-10-06T22:04:49.657154
---

# OXAS-ADV-2025-0001: OX App Suite Security Advisory

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

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# OXAS-ADV-2025-0001: OX App Suite Security Advisory

---

*From*: Martin Heiland via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 7 Apr 2025 09:11:36 +0200 (CEST)

---

```
Dear subscribers,

We're sharing our latest advisory with you and like to thank everyone who contributed in finding and solving those
vulnerabilities. Feel free to join our bug bounty programs for OX App Suite, Dovecot and PowerDNS at YesWeHack.

This advisory has also been published at
https://documentation.open-xchange.com/appsuite/security/advisories/html/2025/oxas-adv-2025-0001.html.

Yours sincerely,
  Martin Heiland, Open-Xchange GmbH

Classification: TLP:GREEN

Internal reference: appsuite/web-apps/ui#785
Type: CWE-79 (Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting'))
Component: frontend
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX App Suite frontend 7.10.6-rev49
First fixed revision: OX App Suite frontend 7.10.6-rev50
Discovery date: 2024-12-13
Solution date: 2025-01-08
Disclosure date: 2025-01-27
CVE: CVE-2024-47875
CVSS: 10.0 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:H)

Details:
Vulnerable DOMPurify shipped with App Suite 7.10.6 and 7.6.3. The DOMPurify third-party library has been updated to
resolve known vulnerabilities.

Risk:
This is done as a precautionary measure, at this time none of the related vulnerabilities is known to be exploitable in
context of OX App Suite. No publicly available exploits are known.

Solution:
Third-party libraries have been updated.

---

Internal reference: DOCS-5081
Type: CWE-611 (Improper Restriction of XML External Entity Reference)
Component: office
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX App Suite office 7.10.6-rev15
First fixed revision: OX App Suite office 7.10.6-rev16
Discovery date: 2023-09-12
Solution date: 2024-12-03
Disclosure date: 2025-01-27
CVE: CVE-2022-0839
CVSS: 9.8 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)

Details:
Resolving third-party vulnerabilities in the office master (7.10.6) repo. Several third-party libraries have been
updated to resolve known vulnerabilities. This includes H2, Xalan, Liquibase and Spring Boot.

Risk:
This is done as a precautionary measure, at this time none of the related vulnerabilities is known to be exploitable in
context of OX App Suite. No publicly available exploits are known.

Solution:
Third-party libraries have been updated.

---

Internal reference: DOCS-5338
Type: CWE-79 (Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting'))
Component: office
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX App Suite office 7.10.6-rev11
First fixed revision: OX App Suite office 7.10.6-rev12
Discovery date: 2024-12-12
Solution date: 2025-01-27
Disclosure date: 2025-01-27
CVE: CVE-2021-23358
CVSS: 7.2 (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

Details:
Resolving third-party vulnerabilities in the office-ui master (7.10.6) repo. Several third-party libraries have been
updated to resolve known vulnerabilities. This includes grunt, dompurify, codecept, underscore and requirejs.

Risk:
This is done as a precautionary measure, at this time none of the related vulnerabilities is known to be exploitable in
context of OX App Suite. No publicly available exploits are known.

Solution:
Third-party libraries have been updated.
```

**Attachment:
[signature.asc](att-14/signature_asc.bin)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

### Current thread:

* **OXAS-ADV-2025-0001: OX App Suite Security Advisory** *Martin Heiland via Fulldisclosure (Apr 13)*

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