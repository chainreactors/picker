---
title: Missing Critical Security Headers in OpenBlow
url: https://seclists.org/fulldisclosure/2025/Jul/13
source: Full Disclosure
date: 2025-07-14
fetch_date: 2025-10-06T23:26:26.129847
---

# Missing Critical Security Headers in OpenBlow

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# Missing Critical Security Headers in OpenBlow

---

*From*: Tifa Lockhart via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sat, 12 Jul 2025 08:44:28 +0000

---

```
Advisory ID: OPENBLOW-2025-003
Title: Missing Critical Security Headers in OpenBlow
Date: 2025-07-12
Vendor: OpenBlow (openblow.it)
Severity: High
CVSS v3.1 Base Score: 8.2 (High)
Vector: AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:N

Summary:

Multiple public deployments of the OpenBlow whistleblowing software lack
critical HTTP security headers. These configurations expose users to client-side
vulnerabilities including XSS, clickjacking, API misuse, and referer leakage.
Given the extreme sensitivity of users interactions and the prominent
institutions involved, this represents a serious systemic flaw.

Affected Headers:

The following security headers were missing in all tested installations:

- Content-Security-Policy
- Referrer-Policy
- Permissions-Policy
- Cross-Origin-Embedder-Policy
- Cross-Origin-Resource-Policy

In addition, cookie flags (`Secure`, `HttpOnly`, `SameSite`) are not enforced
consistently for third-party cookies (e.g. `__cf_bm`, `__cfruid`).

Additional Findings: CSP via is Inadequate

Some installations of OpenBlow were found to include a Content-Security-Policy
via the HTML `<meta>` tag, using constructs such as:

However, this approach is inadequate and insecure, for the following reasons:

- Delayed Enforcement: Browsers apply CSP meta tags only after parsing the
`<head>` section, allowing inline scripts or injections before CSP is active.
- Limited Feature Support: Key directives such as `frame-ancestors` and
`report-uri` are ignored when declared via <meta>.
- Overridden by HTTP: Meta-delivered policies are superseded if any CSP headers
are sent via HTTP, creating confusion and misconfiguration risk.
- Browser Inconsistencies: Not all browsers support CSP via meta in a uniform or
reliable way.

CSP must be delivered via HTTP response headers to provide meaningful protection
against XSS, data exfiltration, and content injection.

As per guidance from:
- https://owasp.org/www-project-secure-headers/
- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
- https://www.w3.org/TR/CSP3/#delivery-html-meta-element
- https://content-security-policy.com
- https://www.crawlspider.com/content-security/

Proof of Concept:

Execute:

curl -sI -D- https://whistleblowing.eni.com/ | grep -iE
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

These issues are especially critical in platforms processing anonymous,
politically sensitive, or high-risk disclosures, where user metadata must be
protected at all costs.

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

• https://whistleblowing.eni.com - ENI (Energy sector)
• https://aruba.openblow.it - Aruba (IT services)
• https://whistleblowing.esteri.it - Ministry of Foreign Affairs (Italy)
• [Potentially others - see Google Dork section]

Google Dork:

A simple search allows anyone to enumerate OpenBlow instances:

intext:"Powered by OpenBlow"

This passive fingerprinting facilitates reconnaissance and targeting of
vulnerable endpoints.

Mitigation:

All OpenBlow deployments should enforce the following headers:

Content-Security-Policy: default-src 'self'; script-src 'self'; frame-ancestors
'none';
Referrer-Policy: no-referrer
Permissions-Policy: camera=(), microphone=(), geolocation=()
Cross-Origin-Embedder-Policy: require-corp
Cross-Origin-Resource-Policy: same-origin

Additionally:
- All cookies, including those from CDN or load balancers, should be flagged as
Secure; HttpOnly; SameSite=Strict.

Vendor Status:

No response as of 2025-07-12

Timeline:

2025-03-06 - Vulnerability discovered
2025-03-10 - Vendor contacted
2025-07-12 - Public disclosure

Standards & References

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

- https://www.openblow.it
- https://owasp.org/www-project-secure-headers/
- https://www.google.com/search?q=intext%3A"Powered+by+OpenBlow";

Disclaimer:

This advisory is released in the interest of public security and transparency.

No exploitation has been attempted. Testing was performed non-intrusively
against publicly available deployments.

For coordination, contact me at tifa.lockhart () atomicmail io
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

### Current thread:

* **Missing Critical Security Headers in OpenBlow** *Tifa Lockhart via Fulldisclosure (Jul 12)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)
...