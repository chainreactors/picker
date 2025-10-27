---
title: Netgear Router Administrative Web Interface Lacks Transport Encryption By Default
url: https://seclists.org/fulldisclosure/2025/Feb/12
source: Full Disclosure
date: 2025-02-17
fetch_date: 2025-10-06T20:48:11.821976
---

# Netgear Router Administrative Web Interface Lacks Transport Encryption By Default

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
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# Netgear Router Administrative Web Interface Lacks Transport Encryption By Default

---

*From*: Ryan Delaney via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 13 Feb 2025 15:25:14 -0600

---

```
<!--
# Exploit Title: Netgear Router Administrative Web Interface Lacks
Transport Encryption By Default
# Date: 02-13-2025
# Exploit Author: Ryan Delaney
# Author Contact: ryan.delaney () owasp org
# Vendor Homepage: https://www.netgear.com
# Version: Netgear C7800 Router, F/W 6.01.07, possibly others
# Tested on: Netgear C7800 Router, F/W 6.01.07
# CVE: CVE-2022-41545

The administrative web interface of a Netgear C7800 Router running firmware
version 6.01.07 (and possibly others) authenticates users via basic
authentication, with an HTTP header containing a base64 value of the
plaintext username and password. Because the web server also does not
utilize transport security by default, this renders the administrative
credentials vulnerable to eavesdropping by an adversary during every
authenticated request made by a client to the router over a WLAN, or a LAN,
should the adversary be able to perform a man-in-the-middle attack.
-->
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
[![Next](/images/right-icon-16x16.png)](14)

### Current thread:

* **Netgear Router Administrative Web Interface Lacks Transport Encryption By Default** *Ryan Delaney via Fulldisclosure (Feb 16)*
  + [Re: Netgear Router Administrative Web Interface Lacks Transport Encryption By Default](14) *Gynvael Coldwind (Feb 17)*

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