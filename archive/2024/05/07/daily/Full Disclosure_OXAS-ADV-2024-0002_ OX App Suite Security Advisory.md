---
title: OXAS-ADV-2024-0002: OX App Suite Security Advisory
url: https://seclists.org/fulldisclosure/2024/May/3
source: Full Disclosure
date: 2024-05-07
fetch_date: 2025-10-06T17:19:48.885511
---

# OXAS-ADV-2024-0002: OX App Suite Security Advisory

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

# OXAS-ADV-2024-0002: OX App Suite Security Advisory

---

*From*: Martin Heiland via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 6 May 2024 09:20:46 +0200 (CEST)

---

```
Dear subscribers,

We're sharing our latest advisory with you and like to thank everyone who contributed in finding and solving those
vulnerabilities. Feel free to join our bug bounty programs for OX App Suite, Dovecot and PowerDNS at YesWeHack.

This advisory has also been published at
https://documentation.open-xchange.com/appsuite/security/advisories/html/2024/oxas-adv-2024-0002.html.

Yours sincerely,
  Martin Heiland, Open-Xchange GmbH

Internal reference: MWB-2471
Type: CWE-79 (Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting'))
Component: backend
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX App Suite backend 8.21
First fixed revision: OX App Suite backend 8.22
Discovery date: 2024-01-29
Solution date: 2024-03-04
CVE: CVE-2024-23187
CVSS: 6.5 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N)

Details:
XSS by abusing CID replacement. Content-ID based embedding of resources in E-Mails could be abused to trigger
client-side script code when using the "show more" option.

Risk:
Attackers could perform malicious API requests or extract information from the users account. Exploiting the
vulnerability requires user interaction. No publicly available exploits are known.

Solution:
Please deploy the provided updates and patch releases. CID replacement has been hardened to omit invalid identifiers.

---

Internal reference: OXUIB-2735
Type: CWE-79 (Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting'))
Component: frontend
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX App Suite frontend 8.21
First fixed revision: OX App Suite frontend 8.22
Discovery date: 2024-02-13
Solution date: 2024-03-04
CVE: CVE-2024-23186
CVSS: 6.5 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N)

Details:
XSS with mail displayname in mobile view. E-Mail containing malicious display-name information could trigger
client-side script execution when using specific mobile devices.

Risk:
Attackers could perform malicious API requests or extract information from the users account. No publicly available
exploits are known.

Solution:
Please deploy the provided updates and patch releases. We now use safer methods of handling external content when
embedding displayname information to the web interface.

---

Internal reference: OXUIB-2695
Type: CWE-79 (Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting'))
Component: frontend
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX App Suite frontend 8.21
First fixed revision: OX App Suite frontend 8.22
Discovery date: 2024-01-10
Solution date: 2024-03-04
CVE: CVE-2024-23188
CVSS: 6.5 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N)

Details:
XSS using mail attachment file names. Maliciously crafted E-Mail attachment names could be used to temporarily execute
script code in the context of the users browser session. Common user interaction is required for the vulnerability to
trigger.

Risk:
Attackers could perform malicious API requests or extract information from the users account. No publicly available
exploits are known.

Solution:
Please deploy the provided updates and patch releases. We now use safer methods of handling external content when
embedding attachment information to the web interface.

---

Internal reference: DOCS-5199
Type: CWE-200 (Exposure of Sensitive Information to an Unauthorized Actor)
Component: office
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX App Suite office 8.21
First fixed revision: OX App Suite office 8.22
Discovery date: 2024-01-10
Solution date: 2024-02-09
CVE: CVE-2024-23193
CVSS: 5.3 (CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N)

Details:
Documentconverter allows access to other user exported PDF files. E-Mails exported as PDF were stored in a cache that
did not consider specific session information for the related user account.

Risk:
Users of the same service node could access other users E-Mails in case they were exported as PDF for a brief moment
until caches were cleared. Successful exploitation requires good timing and modification of multiple request
parameters. No publicly available exploits are known.

Solution:
Please deploy the provided updates and patch releases. The cache for PDF exports now takes user session information
into consideration when performing authorization decisions.
```

**Attachment:
[signature.asc](att-3/signature_asc.bin)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

### Current thread:

* **OXAS-ADV-2024-0002: OX App Suite Security Advisory** *Martin Heiland via Fulldisclosure (May 06)*

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