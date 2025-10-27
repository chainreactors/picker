---
title: Microsoft PlayReady WMRMECC256 Key / root key issue (attack #5)
url: https://seclists.org/fulldisclosure/2024/Aug/15
source: Full Disclosure
date: 2024-08-14
fetch_date: 2025-10-06T18:05:58.235768
---

# Microsoft PlayReady WMRMECC256 Key / root key issue (attack #5)

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# Microsoft PlayReady WMRMECC256 Key / root key issue (attack #5)

---

*From*: Security Explorations <contact () security-explorations com>
*Date*: Tue, 13 Aug 2024 15:13:52 +0200

---

```
Hello All,

There is an architectural / design issue of PlayReady, which can be
successfully exploited to gain access to license server by arbitrary
clients. The problem has its origin in flat certificate namespace /
reliance on a single root key in PlayReady along no auth at license
server end by default (deemed as no bug by Microsoft).

PlayReady client certificates encountered in Windows 10 / 11 and
CANAL+ STB device environments share a common feature. They are all
digitally signed by the so called WMRMECC256 Key identified by the
following public component:

    C8 B6 AF 16 EE 94 1A AD AA 53 89 B4 AF 2C 10 E3
    56 BE 42 AF 17 5E F3 FA CE 93 25 4E 7B 0B 3D 9B
    98 2B 27 B5 CB 23 41 32 6E 56 AA 85 7D BF D5 C6
    34 CE 2C F9 EA 74 FC A8 F2 AF 59 57 EF EE A5 62

Such an approach implicates the following:
- all PlayReady license servers deployed across different content
providers need to embed private key of WMRMECC256 Key for client
identity verification purposes. Compromise of one provider can
potentially impact other providers too,
- client identities originating from different environments are to be
successfully validated by PlayReady license server as long as the
client identity certificate chain is signed by WMRMECC256 Key.

We exploited the above flat certificate namespace / reliance on a
single root key in PlayReady in the context of CANAL+ environment.

On Aug 12, 2024, the compromised STB certificate used by us to
demonstrate the possibility of a massive piracy in CANAL+ environment
has been finally revoked.

Compromised device certificate revocation hasn't addressed the core of
the issue though (no client auth at PlayReady license server end). It
took us less than an hour to change the code of our POC (PlayReady
Toolkit) in order to make it work again, successfully obtain licenses
for content and download arbitrary movies from CANAL+ VOD library, all
regardless of the certificate revocation.

We imported the identity file generated for Windows 10 PlayReady
client to it (some arbitrary identity from May 2024) along private
signing and encryption keys corresponding to it and obtained through
attacks #3 and #4 (complete client identity compromise).

The end result was a fully functional POC and Windows PlayReady client
working in what one would assume to be an isolated PlayReady
environment of CANAL+ set-top-boxes. Microsoft PlayReady license
server successfully accepted and processed identity certificate chain
with obfuscated keys and leaf certs specific to Windows environment.

Such an operation of PlayReady license server makes any certificate
revocations to be rather irrelevant (vide hundreds of millions of
identities associated with Windows PlayReady clients).

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **Microsoft PlayReady WMRMECC256 Key / root key issue (attack #5)** *Security Explorations (Aug 13)*
  + [Re: Microsoft PlayReady WMRMECC256 Key / root key issue (attack #5)](16) *Security Explorations (Aug 13)*

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