---
title: APPLE-SA-08-18-2026-1 Safari 26.6.1
url: https://seclists.org/fulldisclosure/2026/Aug/69
source: Full Disclosure
date: 2026-08-20
fetch_date: 2026-08-21T03:05:27.830839
---

# APPLE-SA-08-18-2026-1 Safari 26.6.1

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

[![Previous](/images/left-icon-16x16.png)](68)
[By Date](date.html#69)
[![Next](/images/right-icon-16x16.png)](70)

[![Previous](/images/left-icon-16x16.png)](68)
[By Thread](index.html#69)
[![Next](/images/right-icon-16x16.png)](70)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-08-18-2026-1 Safari 26.6.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 18 Aug 2026 15:51:27 -0400

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-08-18-2026-1 Safari 26.6.1

Safari 26.6.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/148286.

Apple maintains a Security Releases page at
https://support.apple.com/100100 which lists recent
software updates with security advisories.

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: An out-of-bounds access issue was addressed with improved
bounds checking.
WebKit Bugzilla: 317632
CVE-2026-64784: Janggoon Lee of Out of Bounds, OpenAI Codex Security -
Amy Burnett

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 313452
CVE-2026-43795: wwwlk
WebKit Bugzilla: 318348
CVE-2026-65338: OpenAI Codex Security - Amy Burnett

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: The issue was addressed with improved memory handling.
WebKit Bugzilla: 318405
CVE-2026-65341: Henock Habte

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A memory corruption vulnerability was addressed with
improved locking.
WebKit Bugzilla: 321480
CVE-2026-64782: Seonwook Kim, Shubham Chaskar, lattice, Josef Korbel

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: The issue was addressed with improved input validation.
WebKit Bugzilla: 321484
CVE-2026-64781: Thomas Guillem

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: This issue was addressed through improved state management.
WebKit Bugzilla: 321517
CVE-2026-65351: Niels Hofmans
WebKit Bugzilla: 316996
CVE-2026-65340: Claudio Bozzato and Francesco Benvenuto of Cisco Talos,
Josef Korbel (Citadelo)
WebKit Bugzilla: 317142
CVE-2026-65337: OpenAI Codex Security - Amy Burnett
WebKit Bugzilla: 317349
CVE-2026-65336: Josef Korbel
WebKit Bugzilla: 316723
CVE-2026-65335: OpenAI Codex Security - Amy Burnett
WebKit Bugzilla: 317603
CVE-2026-65333: OpenAI Codex Security - Amy Burnett
WebKit Bugzilla: 317450
CVE-2026-65332: OpenAI Codex Security - Amy Burnett
WebKit Bugzilla: 317611
CVE-2026-65331: OpenAI Codex Security - Amy Burnett

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process crash
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 316347
CVE-2026-64715: Hossein Lotfi (@hosselot) of TrendAI Zero Day Initiative

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 316918
CVE-2026-64780: OpenAI Codex Security - Amy Burnett

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A memory corruption issue was addressed with improved state
management.
WebKit Bugzilla: 316791
CVE-2026-65334: OpenAI Codex Security - Amy Burnett

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to memory
corruption
Description: A memory corruption issue was addressed with improved
memory handling.
WebKit Bugzilla: 317317
CVE-2026-43794: Dung Do (@_piers2) of Calif.io

WebKit
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected process termination
Description: A use-after-free issue was addressed with improved memory
management.
WebKit Bugzilla: 313703
CVE-2026-64787: 杉山 壮太, Shubham Chaskar

WebKit History
Available for: macOS Sonoma and macOS Sequoia
Impact: Visiting a maliciously crafted website may leak sensitive data
Description: The issue was addressed with improved checks.
WebKit Bugzilla: 315528
CVE-2026-64778: Mohit Negi

WebKit Storage
Available for: macOS Sonoma and macOS Sequoia
Impact: Processing maliciously crafted web content may lead to an
unexpected Safari crash
Description: A memory corruption vulnerability was addressed with
improved locking.
WebKit Bugzilla: 321485
CVE-2026-64779: Shubham Chaskar, Tommy DeVoss from Braze Security Team
(@thedawgyg)

Additional recognition

WebKit
We would like to acknowledge Henock Habte for their assistance.

Safari 26.6.1 may be obtained from the Mac App Store.

All information is also posted on the Apple Security Releases
web site: https://support.apple.com/100100.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEhjkl+zMLNwFiCT1o4Ifiq8DH7PUFAmqEtoMACgkQ4Ifiq8DH
7PXAJw//TT8E/xNXFpPvYP4AalRggghX1B0wdLSFdd2py/EsbRloEErOZf5dZ52E
wl3IwcqcNoCbGrcWYx1zFhSn92sgqV6eOQ6ff4BpLp82BRTeISDllKHpX+aZ1LsR
9AL69KgQ4nQjoalq0e8vc4+cE3H59YKg4xC5vXMMt/tNZKfdzwB8x8yZNEFkl1So
j7wAkOtBudbQOo4yaXs7hqBsutkMgxuPr79nIJYv0ye8fbk9IfhA3dKRnSIBYpGe
1coG9gQ/5DMn1IF0AQ0H3Tg9ZxBZcQVpSMs2EuLYzV84eUZ4Pp8lBansDnMZdaSc
SKP08qQ0CRD0Q3xh2L8hzYKYocNpXtOW12BSuIaY3BC/QgPHwTZQEECbpTuleQLe
NFZxY9JEWPtzr5CEq3crlaXihtNbeQA4VhgSrWhYFdUaLKDFBBHIat5wEVlMPgt1
n+ml4wUzdRdfOI9GMeCPbZqIvySdf+EALS+opMzCeXb6HJ84qo8dLi9BMUESucfp
EmSW2dwAAHreuYwykHEuZoFjd3uR0eicEmTHPV/Ujm6NJOgD7qv0cO7jTfc91KuC
udOqx2AcyJLKRupddWeUBYVXZLzQO9XUnUa8K5w2tIqhd3PT+HwsnFb7k4GpaUIK
vj31dfQghVhRuqRDApLd+CVsjsKR6NkZenBKhhf3knDDoMX/dPI=
=LOpe
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](68)
[By Date](date.html#69)
[![Next](/images/right-icon-16x16.png)](70)

[![Previous](/images/left-icon-16x16.png)](68)
[By Thread](index.html#69)
[![Next](/images/right-icon-16x16.png)](70)

### Current thread:

* **APPLE-SA-08-18-2026-1 Safari 26.6.1** *Apple Product Security via Fulldisclosure (Aug 19)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download]...