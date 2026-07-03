---
title: Samsung Galaxy Buds – Zero-Click HFP/A2DP Takeover via L2CAP Session Preemption (Vendor Response: Working as Intended)
url: https://seclists.org/fulldisclosure/2026/Jul/5
source: Full Disclosure
date: 2026-07-02
fetch_date: 2026-07-03T05:48:59.522425
---

# Samsung Galaxy Buds – Zero-Click HFP/A2DP Takeover via L2CAP Session Preemption (Vendor Response: Working as Intended)

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# Samsung Galaxy Buds – Zero-Click HFP/A2DP Takeover via L2CAP Session Preemption (Vendor Response: Working as Intended)

---

*From*: 490h3fqwomf via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 05 Jun 2026 09:21:12 +0000

---

```
Hello Full Disclosure,

The following publicly available research describes a Bluetooth attack against Samsung Galaxy Buds that leverages
connection arbitration behavior between HFP and A2DP profiles to preempt an active audio session.

Title:

Zero-Click HFP/A2DP Takeover via L2CAP Session Preemption
Exploiting Seamless Earbud Connection Arbitration to Bypass Pairing Trust Boundaries

According to the published research, an attacker within Bluetooth range can force a transition of the active audio
session to an attacker-controlled device without requiring user interaction or. The writeup argues that this behavior
crosses expected trust boundaries associated with paired devices and may allow unauthorized audio routing or session
takeover under certain conditions.

The author states that the issue was reported to Samsung and that Samsung ultimately classified the observed behavior
as "working as intended."

Original publication:

Gist:

https://gist.github.com/mroldguy/98c77d25a3e01d6d966523dac353af86

Original:

https://paste.rs/UkBmF.md

Archived copy:

https://archive.is/6KXIp

Summary of the claims made in the publication:

-  Affects Samsung Galaxy Buds devices.
-  Relies on Bluetooth Classic profile behavior involving HFP and A2DP connection management.
-  Described as a zero-click attack requiring no user approval during takeover.
-  Does not require compromise of the target phone.
-  Reportedly allows an attacker within radio range to preempt an active session and become the active audio endpoint.
-  Vendor response is reported as "working as intended."

Interested readers should consult the original publication for technical details, proof-of-concept material, disclosure
timeline, testing methodology, and limitations.

I am not the author of this research. This message is a reference to an already-public disclosure and is being
forwarded for awareness and archival purposes.

Regards,

Anonymous (490h3fqwomf[)](mailto:490h3fqwomf () proton me)
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](8)

### Current thread:

* **Samsung Galaxy Buds – Zero-Click HFP/A2DP Takeover via L2CAP Session Preemption (Vendor Response: Working as Intended)** *490h3fqwomf via Fulldisclosure (Jul 02)*

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