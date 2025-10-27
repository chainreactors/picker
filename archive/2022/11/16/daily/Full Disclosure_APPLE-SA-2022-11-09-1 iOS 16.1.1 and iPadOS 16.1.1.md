---
title: APPLE-SA-2022-11-09-1 iOS 16.1.1 and iPadOS 16.1.1
url: https://seclists.org/fulldisclosure/2022/Nov/7
source: Full Disclosure
date: 2022-11-16
fetch_date: 2025-10-03T22:55:20.938767
---

# APPLE-SA-2022-11-09-1 iOS 16.1.1 and iPadOS 16.1.1

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-11-09-1 iOS 16.1.1 and iPadOS 16.1.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 09 Nov 2022 15:19:17 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-11-09-1 iOS 16.1.1 and iPadOS 16.1.1

iOS 16.1.1 and iPadOS 16.1.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213505.

libxml2
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: An integer overflow was addressed through improved input
validation.
CVE-2022-40303: Maddie Stone of Google Project Zero

libxml2
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air
3rd generation and later, iPad 5th generation and later, and iPad
mini 5th generation and later
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: This issue was addressed with improved checks.
CVE-2022-40304: Ned Williamson and Nathan Wachholz of Google Project
Zero

All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmNsFNIACgkQ4RjMIDke
Nxl2og/7Bwq+DwNmc4conLeNZ/4RVZ8Abf2kKMj71ZJrSov1lvW6W9l3NswznKc9
pV0Cack8zm1she6dr+HNMYFcsSbFF/OTPKsf2jlZ3aZY5on7FpDdzB8bLDbw0dvS
nO2Oc1mgcsBMIuSJBliUfgF0d6L6Hrj7L8Ja0pQP0W5BhcbWbd91wgj2KAQpaX6r
gh7oEy7W5GRPJwLAdOfHmpzWws+PjZ3DMlLuGvGRLwEyizsLbq6rX166KG+asXZz
CeWygTuKKcpZHG6FwahogBFnfl1ccTGJv4UV/9Ks3WEaZCGx5lpkgw+5H9Wx2HgX
Tr9Sh01CQVADadfeGp/Iat0TE2hscMZaTm2A1ZdmOeyK70r0jXvCCHtna9spbPO7
N0OBERsqS9fC+X/XVHuehIzoUXxFUJAuaXD2weBZHJZBZ7MoUqNm50taDqoYUX0y
B2BU0uWOitKfghLRBuFhpuUZtRaZdRfDLSEjSxCTCtGwWnIj4lLlZbE9RAwNNCU1
2+z6pHHlTxZ9c6IiQF8mrIx4IJ0OMIk6oH3gm71l8T5FSMiLCcuInL0XwC5ragJ/
irrxq3GuXL8x+3BjgxnRy4kKy6KUwZsLFp7OI71X/hyjEIyhcXopiRz0PXrooluR
UtooyxSCV8M9u3658pFT2+X4WvQASmk3z+ZUnTBQXrfNgWkxyUs=
=JERa
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

### Current thread:

* **APPLE-SA-2022-11-09-1 iOS 16.1.1 and iPadOS 16.1.1** *Apple Product Security via Fulldisclosure (Nov 15)*

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