---
title: APPLE-SA-2023-02-13-3 Safari 16.3.1
url: https://seclists.org/fulldisclosure/2023/Feb/6
source: Full Disclosure
date: 2023-02-15
fetch_date: 2025-10-04T06:41:59.666638
---

# APPLE-SA-2023-02-13-3 Safari 16.3.1

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2023-02-13-3 Safari 16.3.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 13 Feb 2023 17:44:51 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2023-02-13-3 Safari 16.3.1

Safari 16.3.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213638.

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution. Apple is aware of a report that this issue
may have been actively exploited.
Description: A type confusion issue was addressed with improved
checks.
WebKit Bugzilla: 251944
CVE-2023-23529: an anonymous researcher

All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmPq5PMACgkQ4RjMIDke
NxmFTBAA05jcHEZOdXuE0BQKft0qoWItZ2Dg0p/ONxiqS9ihNDqBt+6q+yOORvr4
Vr2iVpCpo4F5nQv/qBApGCS84SVN9rRIM1VteOYIObgpo37CceODrbywjSTHcD6G
bR47ra8reQK10sDSIoQtX1XKGUltUC/RfKnVDtk/coNu7TJj/VVg2YNPOlQFc5ET
ie0d/NOcK+8Ds1NvK4HQ0Gfq+KHmE507T7nAMfcK4YVlZCtkz4YHEa9w9AcIgmQ4
nzlOSEs5mHu2egr70Xy8+CL7i82Oh2FBzVetLkDhhrZppjykX7zK4Lc0cbABpiaI
u/6ObPGhoW4sFfPCJa8NSflRLKe+aNHdyuzjuqx8rSeqFdP4+rhdI/X2Z/9VKsB/
1Tch55nuBhEGZTejmdwtorGf1+otfW5XpWOGXwnE9sR0qjVvwPwfuK5noLUoLvBR
fiK6xaKUG6IXEYCt0rVncJJ9QtJJKYvqhbf3OwNodrA/V9AAm2MTtIo514BkfZHt
v01xOm7tv35a+5QFcoW/iJBvdTxGVCwzb+2AshMCqO9MQxt8cWknC41K0l6Fl6Yl
/P0qzUJr4NoG72LwW0PqaHimWDVAqJcAHsESe/1qnLO3rZItQJByxURc4wUpHAoj
sFBEBtLiS7FNHOvw4bM1ylQIXXoiFD7sE9NpvksUDzNoRdyAEOM=
=b0uc
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

### Current thread:

* **APPLE-SA-2023-02-13-3 Safari 16.3.1** *Apple Product Security via Fulldisclosure (Feb 14)*

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