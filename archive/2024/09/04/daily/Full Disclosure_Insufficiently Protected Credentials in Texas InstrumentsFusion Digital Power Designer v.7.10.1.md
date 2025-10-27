---
title: Insufficiently Protected Credentials in Texas Instruments	Fusion Digital Power Designer v.7.10.1
url: https://seclists.org/fulldisclosure/2024/Sep/1
source: Full Disclosure
date: 2024-09-04
fetch_date: 2025-10-06T18:42:46.224215
---

# Insufficiently Protected Credentials in Texas Instruments	Fusion Digital Power Designer v.7.10.1

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

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# Insufficiently Protected Credentials in Texas Instruments Fusion Digital Power Designer v.7.10.1

---

*From*: Gionathan Armando Reale via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 1 Sep 2024 11:53:28 +0200

---

```
Insufficiently Protected Credentials in Texas Instruments Fusion Digital Power Designer v.7.10.1

Credit: Gionathan Armando Reale

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Product:  Fusion Digital Power Designer - Version 7.10.1
# Vendor:   Texas Instruments
# CVE ID:   CVE-2024-41629
# Vulnerability Title: Insufficiently Protected Credentials
# Severity: Medium
# Author(s): Gionathan Armando Reale
# Date:     2024-08-15
#
#############################################################
Introduction:
An issue in Texas Instruments Fusion Digital Power Designer v.7.10.1 allows a local attacker to obtain sensitive
information via the plaintext storage of credentials.

Vulnerability PoC:

1. Create a connection within the application that requires credentials.
2. Access the file "C:/Program Files (x86)/Texas Instruments/Fusion Digial Power Designer/data/prefs-shared.xml"
3. Notice the credentials stored as plaintext.

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

### Current thread:

* **Insufficiently Protected Credentials in Texas Instruments Fusion Digital Power Designer v.7.10.1** *Gionathan Armando Reale via Fulldisclosure (Sep 02)*

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