---
title: Re: Microsoft PlayReady WMRMECC256 Key / root key issue	(attack #5)
url: https://seclists.org/fulldisclosure/2024/Aug/16
source: Full Disclosure
date: 2024-08-14
fetch_date: 2025-10-06T18:05:57.078557
---

# Re: Microsoft PlayReady WMRMECC256 Key / root key issue	(attack #5)

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# Re: Microsoft PlayReady WMRMECC256 Key / root key issue (attack #5)

---

*From*: Security Explorations <contact () security-explorations com>
*Date*: Tue, 13 Aug 2024 19:55:56 +0200

---

```
Hello All,

In my previous post, I shamefully confused two root keys (WMRMECC256
and ECC256MSBCertRootIssuer) while decribing the issue pertaining to
one of them.

The key exploited in the attack is called ECC256MSBCertRootIssuer Key
(not the WMRMECC256) and is identified by the following public
component:

86 4D 61 CF F2 25 6E 42 2C 56 8B 3C 28 00 1C FB
3E 15 27 65 85 84 BA 05 21 B7 9B 18 28 D9 36 DE
1D 82 6A 8F C3 E6 E7 FA 7A 90 D5 CA 29 46 F1 F6
4A 2E FB 9F 5D CF FE 7E 43 4E B4 42 93 FA C5 AB

This doesn't change much with respect to the described attack and
regarding reliance on shared root keys. There are just two such keys,
not one.
This is now both corrected and explained in a more detail at:

https://security-explorations.com/microsoft-warbird-pmp.html

Apologies for the confusion and error.

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

### Current thread:

* [Microsoft PlayReady WMRMECC256 Key / root key issue (attack #5)](15) *Security Explorations (Aug 13)*
  + **Re: Microsoft PlayReady WMRMECC256 Key / root key issue (attack #5)** *Security Explorations (Aug 13)*

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