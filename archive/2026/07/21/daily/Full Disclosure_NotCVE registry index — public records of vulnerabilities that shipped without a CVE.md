---
title: NotCVE registry index — public records of vulnerabilities that shipped without a CVE
url: https://seclists.org/fulldisclosure/2026/Jul/23
source: Full Disclosure
date: 2026-07-21
fetch_date: 2026-07-22T05:04:25.938062
---

# NotCVE registry index — public records of vulnerabilities that shipped without a CVE

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

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# NotCVE registry index — public records of vulnerabilities that shipped without a CVE

---

*From*: NotCVE Advisories <advisories () notcve org>
*Date*: Thu, 16 Jul 2026 07:55:12 -0000

---

```
----------------------------------------------------------------------------
NotCVE Registry Index — 2026-07-16
----------------------------------------------------------------------------

[-] About the NotCVE registry:

NotCVE (https://notcve.org) assigns public identifiers to real, verifiable
vulnerabilities that did not receive a CVE — typically because the affected
vendor did not acknowledge the issue. Each record preserves the technical
details, affected products and disclosure timeline, and is never deleted: if
a CVE is assigned later, the entry keeps the original dates and cross-
references it.

A recent example: NotCVE-2026-0001 (Cloudflare Universal SSL CAA
augmentation, published 2026-01-19 without a CVE) was assigned
CVE-2026-14440 by the vendor 163 days later — which is exactly what this
registry is for. The original disclosure timeline is preserved. Details:
https://seclists.org/fulldisclosure/2026/Jul/22

[-] Current records:

[2026]

- Windows NTFS self-healing duplicate-name handling may allow delayed
  reparse point exposure from crafted file system images (CVSS 6.3)
  https://notcve.org/notcve/NotCVE-2026-0008
- Schlage/Allegion HandPunch Missing Authentication in TCP/3001 Management
  Protocol Allows Unauthenticated Remote Supervisor Enrollment and Data
  Disclosure (CVSS 9.8)
  https://notcve.org/notcve/NotCVE-2026-0007
- Hardcoded JWT Secret in ClawVet API Allows Session Token Forgery for
  Existing Users (CVSS 9.8)
  https://notcve.org/notcve/NotCVE-2026-0006
- Authenticated OS Command Injection via SSID in TP-Link TL-WR741ND V5 Web
  Management Interface (CVSS 8)
  https://notcve.org/notcve/NotCVE-2026-0005
- BestCrypt Volume Encryption improper signature-based sector bypass allows
  limited cleartext disclosure and plaintext injection (CVSS 5.7)
  https://notcve.org/notcve/NotCVE-2026-0004
- Deno @std/path isGlob quadratic runtime DoS prior to 1.1.2 (CVSS 5.9)
  https://notcve.org/notcve/NotCVE-2026-0003
- NetScaler ADC (VPX) before 14.1-60.52 missing SSH host key validation in
  HA/HA-INC synchronization can enable adversary-in-the-middle and root code
  execution (CVSS 7.5)
  https://notcve.org/notcve/NotCVE-2026-0002
- Cloudflare Universal SSL CAA augmentation may enable unauthorized DV
  certificate issuance by weakening RFC 8657 account binding (CVSS 8.7)
  https://notcve.org/notcve/NotCVE-2026-0001

[2025]

- Use of Vulnerable Go os.RemoveAll Enables Arbitrary Volume Deletion in
  Kubernetes (CVSS 7.5)
  https://notcve.org/notcve/NotCVE-2025-0003
- Symlink Race in Go os.RemoveAll Allows Privileged File Deletion (CVSS 7.5)
  https://notcve.org/notcve/NotCVE-2025-0004
- IBM Instana /auth/SignIn returnUrl Parameter Open Redirect (CVSS 4.1)
  https://notcve.org/notcve/NotCVE-2025-0002
- Docker Bridge Insufficient Isolation Allows LAN Access to Unpublished
  Ports (CVSS 6.5)
  https://notcve.org/notcve/NotCVE-2025-0001

[2024]

- Linux ASLR Weakness: Improper Bit-Mask Manipulation Reducing mmap Entropy
  by Half (CVSS 5.3)
  https://notcve.org/notcve/NotCVE-2024-0001
- AMD Bulldozer Linux ASLR weakness: Reducing entropy by 87.5% (CVSS 5.3)
  https://notcve.org/notcve/NotCVE-2024-0002

[2023]

- RSA signature verification bypass via Arbitrary Code Execution in Sansa
  Connect bootloader (CVSS 6.2)
  https://notcve.org/notcve/NotCVE-2023-0003
- Buffer overflow in NVD Tools (CVSS 7.5)
  https://notcve.org/notcve/NotCVE-2023-0002
- Secure Boot Bypass in MSM8916/APQ8016 Mobile SoC (CVSS 7.6)
  https://notcve.org/notcve/NotCVE-2023-0001

[-] What is next:

Each record will also be published individually on this list as a full
advisory (technical description, affected versions, timeline and
references), and new NotCVE IDs will be announced here as they are assigned.

[-] Requesting a NotCVE ID:

If you found a real, verifiable vulnerability and could not obtain a CVE for
it, you can request a NotCVE identifier at https://notcve.org/form/.
Anonymous and pseudonymous submissions are accepted. Submissions are
reviewed before publication, and researchers are credited in the NotCVE Hall
of Fame: https://notcve.org/hall/

--
NotCVE Advisories
advisories () notcve org · https://notcve.org
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

### Current thread:

* **NotCVE registry index — public records of vulnerabilities that shipped without a CVE** *NotCVE Advisories (Jul 20)*

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