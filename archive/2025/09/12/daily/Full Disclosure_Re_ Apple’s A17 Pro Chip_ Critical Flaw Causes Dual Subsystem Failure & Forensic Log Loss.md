---
title: Re: Apple’s A17 Pro Chip: Critical Flaw Causes Dual Subsystem Failure & Forensic Log Loss
url: https://seclists.org/fulldisclosure/2025/Sep/37
source: Full Disclosure
date: 2025-09-12
fetch_date: 2025-10-02T20:03:11.338087
---

# Re: Apple’s A17 Pro Chip: Critical Flaw Causes Dual Subsystem Failure & Forensic Log Loss

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

[![Previous](/images/left-icon-16x16.png)](36)
[By Date](date.html#37)
[![Next](/images/right-icon-16x16.png)](38)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#37)
[![Next](/images/right-icon-16x16.png)](39)

![](/shared/images/nst-icons.svg#search)

# Re: Apple’s A17 Pro Chip: Critical Flaw Causes Dual Subsystem Failure & Forensic Log Loss

---

*From*: Matthew Fernandez <matthew.fernandez () gmail com>
*Date*: Mon, 8 Sep 2025 17:22:37 -0700

---

```
On 9/4/25 20:57, Joseph Goydish II via Fulldisclosure wrote:
```

> ```
> TITLE:
> APPLE'S A17 PRO SILICON FLAW: SHARED I²C4 BUS BETWEEN SECURE ENCLAVE AND DIGITIZER CAUSES CASCADING SYSTEM FAILURE
>
> …
> CONCLUSION:
> This is a HIGH-SEVERITY HARDWARE DESIGN FLAW…
> ```

```

```

Can you elaborate on why you consider this high severity? From the
description, it sounds as if this behaviour is fail-closed. That is, the
effects are limited to DoS, with security properties preserved.

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](36)
[By Date](date.html#37)
[![Next](/images/right-icon-16x16.png)](38)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#37)
[![Next](/images/right-icon-16x16.png)](39)

### Current thread:

* [Apple’s A17 Pro Chip: Critical Flaw Causes Dual Subsystem Failure & Forensic Log Loss](0) *Joseph Goydish II via Fulldisclosure (Sep 08)*
  + **Re: Apple’s A17 Pro Chip: Critical Flaw Causes Dual Subsystem Failure & Forensic Log Loss** *Matthew Fernandez (Sep 10)*
    - *Message not available*
      * [Re: [FD] Apple’s A17 Pro Chip: Critical Flaw Causes Dual Subsystem Failure & Forensic Log Loss](39) *josephgoyd via Fulldisclosure (Sep 15)*

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