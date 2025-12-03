---
title: Missing Critical Security Headers in Legality WHISTLEBLOWING
url: https://seclists.org/fulldisclosure/2025/Dec/0
source: Full Disclosure
date: 2025-12-02
fetch_date: 2025-12-03T03:17:17.336637
---

# Missing Critical Security Headers in Legality WHISTLEBLOWING

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

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![](/shared/images/nst-icons.svg#search)

# Missing Critical Security Headers in Legality WHISTLEBLOWING

---

*From*: Aerith Gainsborough via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sat, 29 Nov 2025 12:06:27 +0000

---

```
Advisory ID: LEGALITYWHISTLEBLOWING-2025-001
Title: Missing Critical Security Headers in Legality WHISTLEBLOWING
Date: 2025-11-29
Vendor: DigitalPA (segnalazioni.net)
Severity: High
CVSS v3.1 Base Score: 8.2 (High)
Vector: AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:N

Summary:

Multiple public deployments of Legality WHISTLEBLOWING by DigitalPA
are missing essential HTTP security headers.
This misconfiguration exposes users to client-side attacks including
cross-site scripting (XSS), clickjacking, referer leakage, and
unauthorized access to device APIs. Considering the sensitive nature
of disclosures processed on this platform, the absence of these
protections represents a significant systemic security risk.

Affected Headers:

The following security headers were missing in all tested installations:

- Content-Security-Policy
- Referrer-Policy
- Permissions-Policy
- Cross-Origin-Embedder-Policy
- Cross-Origin-Opener-Policy
- Cross-Origin-Resource-Policy

Additional Findings: CSP via is inadequate

As per guidance from:
- https://owasp.org/www-project-secure-headers/
- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
- https://www.w3.org/TR/CSP3/#delivery-html-meta-element
- https://content-security-policy.com
- https://www.crawlspider.com/content-security/

Proof of Concept:

Execute:

curl -sI -D- https://whistleblowing.giustizia.it/ | grep -iE
'content-security-policy|referrer-policy|permissions-policy|cross-origin-'

Expected result: no such headers appear in the response.

Impact:

- XSS risk: Lack of a Content-Security-Policy allows potential script injection
- Clickjacking: Absence of frame restrictions permits embedding in malicious
frames
- Referer leakage: Users clicking external links may leak context or internal
URLs
- Device metadata exposure: Without Permissions-Policy, access to APIs like
camera/microphone may not be properly restricted
- Cross-origin data leakage: Lack of COEP/CORP weakens isolation from external
origins

These vulnerabilities are especially critical in environments handling
anonymous, politically sensitive, or high-risk disclosures.

CVSS Scoring Rationale:

- Attack Vector: Network (N)
- Attack Complexity: Low (L)
- Privileges Required: None (N)
- User Interaction: Required (R)
- Scope: Unchanged (U)
- Confidentiality: High (H)
- Integrity: Low (L)
- Availability: None (N)

CVSS v3.1 Base Score: 8.2 (High)

Examples of Affected Systems:

• https://whistleblowing.giustizia.it/ - Italian Ministry of Justice
(governamental)

• https://tamoil.segnalazioni.net/ - Tamoil Italia S.p.A. (oil & gas / energy)
• https://toyota.segnalazioni.net/ - Toyota Motor Italia S.p.A. (automotive)
• https://fincantieri.segnalazioni.net/ - Fincantieri S.p.A.
(naval / shipbuilding; civil and military)
• https://realegroup.segnalazioni.net/ - Società Reale Mutua di Assicurazioni
(insurance)

• [Potentially others:
https://www.whistleblowing.software/en/customers-whistleblowing-software/]

Mitigation:

All Legality WHISTLEBLOWING deployments should enforce the following headers:

Content-Security-Policy: default-src 'self'; script-src 'self'; frame-ancestors
'none';
Referrer-Policy: no-referrer
Permissions-Policy: camera=(), microphone=(), geolocation=()
Cross-Origin-Embedder-Policy: require-corp
Cross-Origin-Resource-Policy: same-origin

Vendor Status:
No response as of 2025-11-29

Timeline:

2025-08-13 - Vulnerability discovered
2025-08-12 - Vendor contacted
2025-11-29 - Public disclosure

Standards & References:

The lack of critical HTTP security headers is not just a best-practice issue,
but a recognized security misconfiguration under multiple standards and
vulnerability classification systems:

- OWASP Top 10 – A05:2021 – Security Misconfiguration
https://owasp.org/Top10/A05_2021-Security_Misconfiguration/

Missing or improperly configured security headers are a common form of
misconfiguration, especially in systems dealing with sensitive data.

- MITRE CWE-693: Protection Mechanism Failure
https://cwe.mitre.org/data/definitions/693.html

The software does not provide or incorrectly implements mechanisms that enforce
a security policy, such as headers preventing script execution or cross-origin
data leaks.

- NIST SP 800-53 Rev. 5 – SC-34 & SC-18 (System Integrity & Data Protection)
https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final

Recommends browser-based protections such as content security policies and
limiting cross-origin data leakage.

- ISO/IEC 27001:2022 – Clause 8.25 & 8.28

Emphasizes secure configuration and protection of sensitive communications,
including at the application layer.

References:
- https://www.segnalazioni.net
- https://owasp.org/www-project-secure-headers/
- https://www.whistleblowing.software/en/customers-whistleblowing-software

Disclaimer:

This advisory is released in the interest of public security and transparency.

No exploitation has been attempted. Testing was performed non-intrusively
against publicly available deployments.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

### Current thread:

* **Missing Critical Security Headers in Legality WHISTLEBLOWING** *Aerith Gainsborough via Fulldisclosure (Dec 01)*

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
[![](/shared...