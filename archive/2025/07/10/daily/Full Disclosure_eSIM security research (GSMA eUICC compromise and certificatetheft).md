---
title: eSIM security research (GSMA eUICC compromise and certificate	theft)
url: https://seclists.org/fulldisclosure/2025/Jul/4
source: Full Disclosure
date: 2025-07-10
fetch_date: 2025-10-06T23:53:15.470979
---

# eSIM security research (GSMA eUICC compromise and certificate	theft)

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# eSIM security research (GSMA eUICC compromise and certificate theft)

---

*From*: Security Explorations <contact () security-explorations com>
*Date*: Wed, 9 Jul 2025 10:28:06 +0200

---

```
Dear All,

We broke security of Kigen eUICC card with GSMA consumer certificates
installed into it.

The eUICC card makes it possible to install the so called eSIM profiles
into target chip. eSIM profiles are software representations of mobile
subscriptions. For many years such mobile subscriptions had a form of a
physical SIM card of various factors (SIM, microSIM, nonoSIM). With eSIM,
the subscription can come in a pure digital form (as a software bundle),
it can also carry Java Card applications.

According to Kigen:
1) eSIMs are "as secure and interoperable as SIM cards [...] thanks to
   the multi-layered GSMA eSIM certification scheme that protects device
   makers, device owners and mobile network operators (MNOs)"

2) "Kigen OS offers the highest level of logical security when employed
   on any SIM form factor, including a secure enclave" and "Kigen SIM OS
   features help differentiate, scale and grow revenues with zero compromise
   security"

The hack proves that our research on Java Card from 2019 did matter.
Oracle indicated the vulnerabilities we reported to the company in 2019
were rather irrelevant (the company referred to them as "security concerns")
/ did not affect their production Java Card VM. These are now proved to be
real bugs.

This is likely the first successful public hack against:
- consumer GSMA eUICC
- Kigen eSIM (Kigen press releases and web pages implicate over 2 billion
  SIMs enabled by Kigen secure SIM OS)
- EAL certified GSMA security chip (SLC37 chip based on 32-bit ARM SecurCore
  SC300 processor from Infineon)

The attack against Kigen eUICC relies both on physical access to sample card
along knowledge of the keys used for malicious Java app installation. The
remote over-the-air (OTA) vector can't be excluded - our Proof of Concept
code mimics a malicious applet installation over OTA SMS-PP protocol (Short
Message Service Point to Point) on a target Kigen eUICC. In that context,
knowledge of the keys is a primary requirement for target card compromise.

The hack proves no security / isolation for the eSIM profile and Java apps
(no security for eUICC memory content).

It's worth to note that while this work builds on our past Java Card
research
from 2019 (along 25 years of Java hacking experience), it required
development
of some new exploitation techniques / know-how.

We hope the hack brings eSIM security along associated security risks to
the focus of mobile network operators (MNOs), vendors, security researchers
and security companies. This is important in the context of somewhat bold
security claims / overconfidence of eUICC vendors (vide leaf eUICC cert
valid for 100 years) and MNO assumptions pertaining to profile trust and
its storage in a tamper-proof security element (MNO profile integrity / no
compromise / no tampering assumed).

More information about the core issues, fixes and hack implications can be
found at project pages:

https://security-explorations.com/esim-security.html

Thank you.

Best Regards,
Adam Gowdiak

----------------------------------
Security Explorations -
AG Security Research Lab
https://security-explorations.com
----------------------------------
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

### Current thread:

* **eSIM security research (GSMA eUICC compromise and certificate theft)** *Security Explorations (Jul 09)*

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