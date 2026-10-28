---
title: SCHUTZWERK-SA-2025-002: Privilege escalation in Lobster_pro through request replaying
url: https://seclists.org/fulldisclosure/2026/Oct/35
source: Full Disclosure
date: 2026-10-27
fetch_date: 2026-10-28T07:49:43.981266
---

# SCHUTZWERK-SA-2025-002: Privilege escalation in Lobster_pro through request replaying

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

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
[![Next](/images/right-icon-16x16.png)](36)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
[![Next](/images/right-icon-16x16.png)](36)

![](/shared/images/nst-icons.svg#search)

# SCHUTZWERK-SA-2025-002: Privilege escalation in Lobster\_pro through request replaying

---

*From*: David Brown via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 26 Oct 2026 15:46:40 +0100

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Privilege escalation via request replaying in Lobster_pro
=========================================================
```

Due to improper permission checks in Lobster\_pro, attackers are able to
interact with
endpoints that should require administrative privileges. This issue
affects Lobster\_pro

```
version 4.12.12-LTS and potentially other versions prior to 25.1.3.

Metadata
========

- - Affected product: Lobster_pro
```

- - Affected version: 4.12.12-LTS and potentially other versions prior
to 25.1.3

```
- - Vendor: Lobster DATA GmbH
```

- - Problem type(s): CWE-280 Improper handling of insufficient
permissions or privileges

```
- - CVE ID: CVE-2026-3322
- - CVE URL: https://www.cve.org/CVERecord?id=CVE-2026-3322
- - CVSS 4.0 score: 5.6
- - Advisory URL: https://www.schutzwerk.com/en/blog/schutzwerk-sa-2025-002/

Details
=======
```

The endpoint <https://lobster-pro-instance:443/BASE/user/search/tuple>
allows administrators
to retrieve the list of registered users for editing. Authenticated
attackers with
non-administrative privileges who have access to an administrative
request can replay the
request with their own session ID and gain access to personal data.
Attackers only need to
replace the headers X-Env-Clientid and X-Env-Sessiontoken with the
values of their own
unprivileged session. Similar attacks are likely possible by manually
forging the correct
Action Message Format[0] request data instead of intercepting an
administrative request.

```
Risk
====
```

An attacker can use this vulnerability to download a list of registered
users or
potentially perform other unauthorized actions. The amount of data
exposed depends on the

```
information stored in Lobster_pro.

Solution/Mitigation
===================

Update Lobster_pro to version 25.1.3 or later.

Timeline
========

- - 2025-06-26 Vulnerability reported to vendor
- - 2025-10-09 Vendor releases version 25.0.1 to address the vulnerability
- - 2025-11-19 Vendor releases version 25.1.3 with additional fixes
```

- - 2025-11-19 Vendor informs SCHUTZWERK about the patch release.
Publication delayed for

```
  undisclosed reasons.
- - 2026-10-26 Advisory released

Credits
=======

The vulnerability was discovered by Daniel Marner of SCHUTZWERK GmbH.

Footnotes
=========

[0] https://en.wikipedia.org/wiki/Action_Message_Format
-----BEGIN PGP SIGNATURE-----

iQJOBAEBCgA4FiEEgLsg7Oj/wY3LSF87GrXfkTIXLrsFAmrfZz0aHGFkdmlzb3Jp
ZXNAc2NodXR6d2Vyay5jb20ACgkQGrXfkTIXLrsQ9g/+MUYMsmoaxs5JxKD5Obas
SIbfHKCwSutmpE1Q8j0Ao5oG3IR9Zo0SgFhFFPelH5E7Q6lf2C0YbretCMvxCFXx
Ybg5VX9OFQFazRDP/9mx9LaT+ZSwBFLMnlPDM5Pwudn7xoNEoVmRbNIibwVhhzqB
U2Hmd0gHfUZbhtA95lCm6ODKBFxqV1MP/LRYbVM8Qp6BBT0V357VsVfUwAcNyKdo
ObmuXRA9p2iuElF67DwjAvLYNzU4C2/eUjLw9T9pJhKNs+hBh7hYFi6UefWOQ1MI
bNTMA9Ngw42Jed/Be69un9Fw0D+09CWx/PmXbcVnvEhpLLA846bbJ27uWJvuFn4t
waKpNx9uka2TRaFsF20VE3Wa+EaCT2OajFcZVXy+KOK4ZMNyeACStc0SI6kLOFIZ
MgvFc+GWq48DIJvAugt0d16O5tQcD/+rSt0RP/jV++hTUAeIUKEPjarJi4j+wkpj
QhDUBhl+R5cgmOr43bPhwYYUnd9uJMHa6p0X+54vnJPhv2zkDPRbJCMrNHkK4giK
Vc8F+Kvl6B4r0gbVKY5jD48Ups8tOLaX1S2KkixlwZf7vKQw4gIlJPMEPZt9dEaS
8K59OYPiIIe7prOk2nbZQjGQ344lezd9rEdV3UZgucRSRnnJb7sCX6hVC7K4DSeS
5wvZd03jEsRq4o+PWaKo9wg=
=vwsA
-----END PGP SIGNATURE-----

--
SCHUTZWERK GmbH, Pfarrer-Weiß-Weg 12, 89077 Ulm, Germany
Zertifiziert / Certified ISO 27001, 9001 and TISAX

Phone +49 731 977 191 0

advisories () schutzwerk com / www.schutzwerk.com

Geschäftsführer / Managing Directors:
Jakob Pietzka, Michael Schäfer

Amtsgericht Ulm /  HRB 727391
Datenschutz / Data Protection www.schutzwerk.com/datenschutz
```

**Attachment:
[OpenPGP\_signature.asc](att-35/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
[![Next](/images/right-icon-16x16.png)](36)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
[![Next](/images/right-icon-16x16.png)](36)

### Current thread:

* **SCHUTZWERK-SA-2025-002: Privilege escalation in Lobster\_pro through request replaying** *David Brown via Fulldisclosure (Oct 27)*

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