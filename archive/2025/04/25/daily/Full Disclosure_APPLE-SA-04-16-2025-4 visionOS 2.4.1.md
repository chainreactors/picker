---
title: APPLE-SA-04-16-2025-4 visionOS 2.4.1
url: https://seclists.org/fulldisclosure/2025/Apr/26
source: Full Disclosure
date: 2025-04-25
fetch_date: 2025-10-06T22:07:42.405199
---

# APPLE-SA-04-16-2025-4 visionOS 2.4.1

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-04-16-2025-4 visionOS 2.4.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 16 Apr 2025 13:54:14 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-04-16-2025-4 visionOS 2.4.1

visionOS 2.4.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/122402.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

CoreAudio
Available for: Apple Vision Pro
Impact: Processing an audio stream in a maliciously crafted media file
may result in code execution. Apple is aware of a report that this issue
may have been exploited in an extremely sophisticated attack against
specific targeted individuals on iOS.
Description: A memory corruption issue was addressed with improved
bounds checking.
CVE-2025-31200: Apple and Google Threat Analysis Group

RPAC
Available for: Apple Vision Pro
Impact: An attacker with arbitrary read and write capability may be able
to bypass Pointer Authentication. Apple is aware of a report that this
issue may have been exploited in an extremely sophisticated attack
against specific targeted individuals on iOS.
Description: This issue was addressed by removing the vulnerable code.
CVE-2025-31201: Apple

Instructions on how to update visionOS are available at
https://support.apple.com/118481. To check the software version
on your Apple Vision Pro, open the Settings app and choose General >
About.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEsz9altA7uTI+rE/qX+5d1TXaIvoFAmgABy8ACgkQX+5d1TXa
Ivrang/7BbMWMNA2hlaLbrO/2skpKd6F2cK9LKILFzivIWDadD4M7wZVRGo0TM4Y
fN1cOW+iGtd4BmCFnKYMIjc89f+WXkL+dESLiD3ujwy73RmUIGfbhr6GkgGJkcHt
Dccx71oumDDO9FY1IUyZuBCONGuC8vcfbgKjdaeiLpkzbBDMSMNna+HVvA4nUExP
j2ApivOFXcbhBO7Bw6DZkavXU+9wbZhHHkKt+QZifdB6vMzz854bDdaT1JNt9l80
YdwBEPE8+0TXAWRX4VToOKg1Zn8AT7LmK3PCnB+xuCRbh5zgWIOT7hVvEtvaPlHl
uup5Av2CJoFdfXzP5PJ8lUfxG/NRiGZX8XykYakp2y7sPQcwUkU56N2uoWhO95Wh
bhZoy6hN5bkptD8Kbnj/LyyEUNT3Hk1Gd9o9pxhnp7GvwNtZqOAC8/5nIMsoy06S
AJeNUj1WAJJ9a9o/2S0Au3KpR6ccVb6UXXJ+d71xhIPjyXqJTnC/mKrzsx6yjGTP
qaj/Zr7cZh36BXa6a5Fv3z1I7AR7uwR2hxHG/dOund/RUGeRxoTEbcl1rmzAVZeF
N4JsOvHtBboz5B3xs9P11Q9FMGzbyeuO8Yttqb4oXJOd97XA5T67iLiuDfCPgYxk
3GCs5pKAoKW3HrQpO8wwwX/vloZBOt7idy+81IUQ80GIaMkS9rU=
=cfH0
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

### Current thread:

* **APPLE-SA-04-16-2025-4 visionOS 2.4.1** *Apple Product Security via Fulldisclosure (Apr 23)*

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