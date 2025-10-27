---
title: Access Control in Paxton Net2 software
url: https://seclists.org/fulldisclosure/2024/Dec/0
source: Full Disclosure
date: 2024-12-04
fetch_date: 2025-10-06T19:41:55.062789
---

# Access Control in Paxton Net2 software

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

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![](/shared/images/nst-icons.svg#search)

# Access Control in Paxton Net2 software

---

*From*: Jeroen Hermans via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 2 Dec 2024 17:30:45 +0100

---

```
CloudAware Security Advisory
```

[CVE pending]: Potential PII leak and incorrect access control in Paxton
Net2 software

```
========================================================================
Summary
========================================================================
```

Insecure backend database in the Paxton Net2 software. Possible leaking
of PII incorrect access control.

```
No physical access to computer running Paxton Net2 is required.

========================================================================
Product
========================================================================
* Paxton Net2Â  (all current versions)

========================================================================
Detailed description
========================================================================
```

By exploiting MSSQL single usermode it is possible to gain administrator
rights to the Net2 database. In this database
plaintext PIN codes for building entrance can be found and changed. It
is also possible to add users to the system and
enable/disable users in the system. By reading tables in the MSSQL table
PII is leaked. In order to gain access local
access to the computer running Net2 is necessary, but this can also be
over a network using e.g. Anydesk which makes

```
physical access not necessary.
```

The vendor has not acknowledged the vulnerability after contact. There
is no fix planned.

```
========================================================================
Solution
========================================================================
```

As the vendor has not acknowledged the vulnerability there is no
effective remediation for this vulnerability.
The most effective measure at this moment is closely monitoring who has
local access to the machine running the Net2

```
software.

========================================================================
Mitigation
========================================================================
```

There is no known effective mitigation. Limiting who has local access to
the machine running the Net2 software seems

```
the most effective measure.

========================================================================
Weblinks
========================================================================
```

It has been decided not to release the exploit code yet as there is no
mitigration possible. Discoverers are willing to

```
share exploit code at request to help with mitigration.

========================================================================
Discoverers
========================================================================
Jeroen Hermans, CloudAware j.hermans[at]cloudaware[dot]eu
Emiel van Berlo, Danego emiel[at]danego[dot]nl

========================================================================
History
========================================================================
Nov 12 2024: Requested latest Net2 software from Paxton
Nov 26, 2024: Obtained latest Net2 software for other source
Nov 26, 2024: Informed Paxton about vulnerability
Nov 27, 2024: Release of exploit code
```

Dec 2, 2024: Refused CVE reservation by Paxton & request of CVE
reservation directly at Mitre

**Attachment:
[OpenPGP\_0x52DD23305307A27C.asc](att-0/OpenPGP_0x52DD23305307A27C_asc.bin)**
*Description:* OpenPGP public key

**Attachment:
[OpenPGP\_signature.asc](att-0/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

### Current thread:

* **Access Control in Paxton Net2 software** *Jeroen Hermans via Fulldisclosure (Dec 02)*

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