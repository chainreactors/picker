---
title: OXAS-ADV-2022-0002: OX App Suite Security Advisory
url: https://seclists.org/fulldisclosure/2023/Feb/3
source: Full Disclosure
date: 2023-02-15
fetch_date: 2025-10-04T06:42:02.911539
---

# OXAS-ADV-2022-0002: OX App Suite Security Advisory

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

# OXAS-ADV-2022-0002: OX App Suite Security Advisory

---

*From*: Martin Heiland via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 9 Feb 2023 08:40:01 +0000 (WET)

---

```
Dear subscribers,

we're sharing our latest advisory with you and like to thank everyone who contributed in finding and solving those
vulnerabilities. Feel free to join our bug bounty programs for OX AppSuite, Dovecot and PowerDNS at YesWeHack.

A CSAF representation of this advisory has been published at
https://documentation.open-xchange.com/security/advisories/.

Yours sincerely,
  Martin Heiland, Open-Xchange GmbH

Internal reference: OXUIB-1795
Vulnerability type: CWE-80 (Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS))
Component: backend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Last affected revision: OX App Suite backend 7.10.5-rev50, OX App Suite backend 7.10.6-rev29
First fixed revision: OX App Suite backend 7.10.5-rev51, OX App Suite backend 7.10.6-rev30
Discovery date: 2022-07-29
Solution date: 2022-10-21
Disclosure date: 2023-02-08
CVE: CVE-2022-37306
CVSS: 4.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N)

Details:
XSS using "upsell" triggers. Non-alphanumeric content can be injected by the user as JS content for the "upsell"
module. As a result, the code will be executed during subsequent logins and opening the "Portal" application, enabling
a persistent cross-site scripting attack vector.

Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering
unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would
require temporary access to the users account or lure a user to a compromised account. No publicly available exploits
are known.

Solution:
We improved the allow-list sanitizing algorithm to deal with non-alphanumeric code.

---

Internal reference: OXUIB-1933
Vulnerability type: CWE-80 (Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS))
Component: frontend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Last affected revision: OX App Suite frontend 7.10.5-rev38, OX App Suite frontend 7.10.6-rev19
First fixed revision: OX App Suite frontend 7.10.5-rev39, OX App Suite frontend 7.10.6-rev20
Discovery date: 2022-09-26
Solution date: 2022-10-21
Disclosure date: 2023-02-08
CVE: CVE-2022-43696
CVSS: 4.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N)

Details:
XSS using "upsell ads". HTML content can be injected by the user as JS content for the "upsell ads" module. As a
result, the code will be executed during subsequent logins and opening the "Portal" application, enabling a persistent
cross-site scripting attack vector.

Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering
unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would
require temporary access to the users account or lure a user to a compromised account. No publicly available exploits
are known.

Solution:
We improved the sanitization process for upsell ads.

---

Internal reference: MWB-1784
Vulnerability type: CWE-80 (Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS))
Component: backend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Last affected revision: OX App Suite backend 7.10.5-rev50, OX App Suite backend 7.10.6-rev29
First fixed revision: OX App Suite backend 7.10.5-rev51, OX App Suite backend 7.10.6-rev30
Discovery date: 2022-08-16
Solution date: 2022-10-25
Disclosure date: 2023-02-08
CVE: CVE-2022-43697
CVSS: 4.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N)

Details:
"Tracking" features can be used to inject arbitrary script code. In case activity tracking adapters are enabled but not
defined, users can use jslob to define own tracking settings for an account. This allows adding arbitrary values to
trigger a specific URL or load a library.

Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering
unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would
require temporary access to the users account or lure a user to a compromised account. No publicly available exploits
are known.

Solution:
We made the related jslob configuration endpoint read-only for users.

---

Internal reference: MWB-1823
Vulnerability type: CWE-918 (Server-Side Request Forgery (SSRF))
Component: backend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Last affected revision: OX App Suite backend 7.10.5-rev50, OX App Suite backend 7.10.6-rev29
First fixed revision: OX App Suite backend 7.10.5-rev51, OX App Suite backend 7.10.6-rev30
Discovery date: 2022-09-14
Solution date: 2022-10-24
Disclosure date: 2023-02-08
CVE: CVE-2022-43698
CVSS: 5.0 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N)

Details:
SSRF using POP3 account updates. When changing a valid external POP3 mail account as a user, the operation to update
the accounts settings did not consider deny-list values.

Risk:
Server-initiated requests can be directed to internal resources that are restricted based on deny-list settings. This
can be used to determine "internal" addresses and services, depending on measurement and content of error responses.
While no data of such services can be exfiltrated, the risk is a violation of perimeter based security policies. No
publicly available exploits are known.

Solution:
We now check compliance with existing deny-list content when updating POP3 mail accounts.

---

Internal reference: MWB-1862
Vulnerability type: CWE-918 (Server-Side Request Forgery (SSRF))
Component: backend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Last affected revision: OX App Suite backend 7.10.5-rev50, OX App Suite backend 7.10.6-rev29
First fixed revision: OX App Suite backend 7.10.5-rev51, OX App Suite backend 7.10.6-rev30
Discovery date: 2022-10-06
Solution date: 2022-11-07
Disclosure date: 2023-02-08
CVE: CVE-2022-43699
CVSS: 5.0 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N)

Details:
Mail account discovery can be abused for SSRF. The external E-Mail autodiscovery feature performs connections checks
based on the E-Mail addresses host-part. Those do not take existing deny-lists into respect, allowing attackers with
access to DNS records of a domain to redirect requests to illegal addresses.

Risk:
Server-initiated requests can be directed to internal resources that are restricted based on deny-list settings. This
can be used to determine "internal" addresses and services, depending on measurement and content of error responses.
While no data of such services can be exfiltrated, the risk is a violation of perimeter based security policies. No
publicly available exploits are known.

Solution:
We check for compliance with existing deny-list content when performing mail account autodiscovery.

---

Internal reference: MWB-1882, DOCS-4580
Vulnerability type: CWE-94 (Improper Control of Generation of Code ('Code Injection'))
Component: office
Report confidence: Confir...